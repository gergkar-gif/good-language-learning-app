#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 16, 17, and 18:
  - Unit 16: b2-urbanusnepi (Great Intellectual Debates: Urbanists vs. Populists)
  - Unit 17: b2-mediatortenet (From the Town Crier to the Digital Public Sphere)
  - Unit 18: b2-politikairetorika (Public Memory, Monuments & Political Rhetoric)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402


UNIT_16_URBANUSNEPI = {
    "unit_num": 16,
    "slug": "urbanusnepi",
    "title": "Great Intellectual Debates: Urbanists vs. Populists",
    "grammar_skill": "b2-polemical-connectors",
    "vocab_skill": "b2-urbanusnepi-vocab",
    "theme": "The Népi vs. Urbánus intellectual debate in Hungary",
    "location": "Budapest, Debrecen és Monor",
    "intro_body": [
        "No intellectual controversy shaped twentieth-century Hungarian culture more profoundly than the debate between the 'népi' (populist / agrarian-sociographer) writers and the 'urbánus' (cosmopolitan / bourgeois-modernist) thinkers. Emerging in the interwar decades, both camps sought a cure for Hungary's semi-feudal inequalities, yet they looked into two very different mirrors of the nation.",
        "In this unit, you will follow the village sociographers into the estates of the Alföld and Transdanubia, visit the editorial tables of the journal Szép Szó in Budapest, examine the arguments of István Bibó and Attila József, witness the historic 1985 clandestine meeting at Monor where the two camps joined forces for democracy, and trace echoes of the debate today. Grammatically, you will master high-register polemical, adversative, and concessive connectors (holott, jóllehet, csakhogy, ellenben, ezzel szemben)."
    ],
    "combined_story_title": "Két tükör, egy ország: A népi–urbánus vita története",
    "combined_story_summary": "The history of Hungary's defining twentieth-century intellectual debate between the Népi (populist/village sociographer) writers and the Urbánus (cosmopolitan modernist) thinkers, culminating in the historic 1985 Monor meeting.",
    "lessons": [
        {
            "num": 1,
            "title": "Village Sociographers and the 'Népi' Diagnosis",
            "grammar_label": "Counter-reality adversative clauses with holott ('whereas in fact')",
            "goals": [
                "I can explain the aims and methods of the 1930s Hungarian village sociography (falukutatás) movement.",
                "I can use holott to expose a contradiction between an official claim or appearance and the underlying reality.",
                "I can discuss agrarian social history and literary sociography using B2 Hungarian vocabulary."
            ],
            "story_segment": {
                "seg_slug": "falukutatok",
                "title": "Jegyzetfüzettel a puszták népe között",
                "summary": "In the 1930s, writers and sociologists like Gyula Illyés, Géza Féja, Imre Kovács, and Ferenc Erdei traveled to Hungary's destitute villages and manorial estates, creating the genre of literary sociography to shock the urban public.",
                "location": "Dunántúli uradalmak és a Viharsarok (1930-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1930-as évek elején a hivatalos revizionista propaganda idilli, harmonikus falvakkal és elégedett földművesekkel büszkélkedett a képeslapokon, holott a magyar agrártársadalom alsó rétegei, a nincstelen zsellérek és az uradalmi cselédek szinte középkori kiszolgáltatottságban tengődtek. A nagybirtokrendszer érintetlenül hagyta a félfeudális viszonyokat, miközben hárommillió szegényparaszt számára a saját föld elérhetetlen álom maradt."
                    },
                    {
                        "type": "narration",
                        "text": "Erre a drámai társadalmi vakfoltra irányította rá a figyelmet a népi írók és falukutatók nemzedéke, akik az irodalmi képzelet helyett a helyszíni megfigyelést, a statisztikát és a mélyinterjút választották fegyverül. Illyés Gyula 1936-ban megjelent Puszták népe című művében saját dunántúli felmenőinek sorsán keresztül mutatta be, hogyan formálja a cselédsor generációk lelkét és testtartását."
                    },
                    {
                        "type": "narration",
                        "text": "A Magyarország felfedezése című könyvsorozat keretében Féja Géza a Viharsarok, Kovács Imre a néma forradalomba burkolózó egykéző falvak, Erdei Ferenc pedig az alföldi mezővárosok valóságát térképezte fel. A hatóságok több szerző ellen sajtópert indítottak izgatás vádjával, holott a falukutatók csupán a hivatalos népszámlálási és egészségügyi adatokat szólaltatták meg emberi sorsokon keresztül."
                    },
                    {
                        "type": "narration",
                        "text": "Németh László és társai úgy vélték, hogy a nemzet szellemi megújulása nem indulhat ki kizárólag a nyugati mintákat másoló nagyvárosi szalonokból. Szerintük a parasztság évszázadokig megőrzött nyelvi és kulturális öröksége olyan tartalék, amelyet földreformmal, népfőiskolákkal és tehetséggondozással kell beemelni a modern magyar polgárosodásba."
                    },
                    {
                        "type": "narration",
                        "text": "A szociográfia így vált a harmincas évek legmeghatározóbb szellemi műfajává: egyszerre volt könyörtelen vádirat a nagybirtokrendszer ellen és segélykiáltás egy olyan társadalmi réteg nevében, amelynek addig nem volt saját hangja az országos nyilvánosságban."
                    }
                ]
            },
            "words": [
                {"lemma": "falukutató", "translation": "village sociographer / rural social researcher", "pos": "noun"},
                {"lemma": "szociográfia", "translation": "sociography (literary-sociological field study)", "pos": "noun"},
                {"lemma": "nagybirtokrendszer", "translation": "latifundia / system of large landed estates", "pos": "noun"},
                {"lemma": "zsellér", "translation": "cottager / landless agricultural laborer", "pos": "noun"},
                {"lemma": "uradalmi cseléd", "translation": "manorial farmhand / estate servant", "pos": "noun"},
                {"lemma": "földreform", "translation": "land reform / agrarian redistribution", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "holott-adversative",
                "title": "Exposing Contradictions with holott ('whereas in fact')",
                "text1_title": "Semantic Precision of holott in Polemical Prose",
                "text1": "In B2 essays and historical debates, holott ('whereas in fact', 'while in reality', 'even though in truth') is far sharper than a simple de or pedig. It introduces a second clause that directly refutes or unmasks the false impression, official claim, or misguided assumption stated in the first clause.",
                "text2_title": "Word Order and Punctuation",
                "text2": "A comma always precedes holott. Because holott is a subordinating/coordinating polemical conjunction standing at the head of the second clause, the element immediately following it often carries natural contrastive emphasis: 'A propaganda idilli falvakkal büszkélkedett, holott a zsellérek nyomorban éltek.'",
                "table_title": "Using holott to Unmask Appearance vs. Reality",
                "table_rows": [
                    ["A plakátok jólétet hirdettek, holott a cselédek éheztek.", "The posters proclaimed prosperity, whereas in fact the farmhands were starving."],
                    ["Izgatással vádolták a szerzőt, holott csak a tényeket írta le.", "They accused the author of incitement, whereas in reality he merely described the facts."],
                    ["Sokan távoli egzotikumnak hitték a pusztát, holott az ország szívében feküdt.", "Many believed the puszta to be a distant exotica, whereas in fact it lay in the heart of the country."]
                ],
                "examples": [
                    {"spanish": "A hivatalos propaganda harmonikus falvakkal büszkélkedett, holott az uradalmi cselédek kiszolgáltatottságban tengődtek.", "english": "Official propaganda boasted of harmonious villages, whereas in fact manorial farmhands eked out an existence in vulnerability."},
                    {"spanish": "A hatóságok sajtópert indítottak ellenük, holott a falukutatók csupán a valóságot térképezték fel.", "english": "The authorities launched press trials against them, even though in truth the village sociographers merely mapped out reality."},
                    {"spanish": "Azt hitték, a kérdés magától megoldódik, holott gyökeres földreformra volt szükség.", "english": "They thought the issue would resolve itself, whereas in fact radical land reform was needed."}
                ],
                "tip": "Use holott whenever the first clause expresses a widespread illusion, official pretension, or unfair accusation that the second clause proves false with hard evidence."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "pairs": [
                        ["falukutató", "village sociographer"],
                        ["szociográfia", "literary-sociological field study"],
                        ["nagybirtokrendszer", "system of large landed estates"],
                        ["zsellér", "landless agricultural laborer"],
                        ["uradalmi cseléd", "manorial estate servant"],
                        ["földreform", "agrarian land redistribution"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "question": "Mi volt az 1930-as években kibontakozó szociográfiai mozgalom legfőbb célja?",
                    "options": [
                        "Helyszíni megfigyelésekkel és adatokkal feltárni a szegényparasztság és az uradalmi cselédek nyomorúságos helyzetét.",
                        "Idilli, romantikus pásztortörténetekkel szórakoztatni a nagyvárosi közönséget.",
                        "Megvédeni a félfeudális nagybirtokrendszer érinthetetlenségét."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "sentence": "Illyés Gyula Puszták népe című műve a magyar irodalmi _____ egyik legmeghatározóbb klasszikusa.",
                    "answer": "szociográfia",
                    "english": "Gyula Illyés's work People of the Puszta is one of the most defining classics of Hungarian literary sociography."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-polemical-connectors"],
                    "question": "Which connector best completes this sentence to expose the contradiction between official claims and factual reality? 'Féja Gézát izgatással vádolták a bíróságon, _____ a könyvében közölt adatok a hivatalos statisztikákból származtak.'",
                    "options": ["holott", "miszerint", "ugyanis", "tehát"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "sentence": "A képeslapok gondtalan falusi életről árulkodtak, _____ hárommillió nincstelen paraszt várt hiába saját földre.",
                    "answer": "holott",
                    "english": "The postcards spoke of a carefree village life, whereas in fact three million landless peasants waited in vain for land of their own."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "tiles": ["Izgatással", "vádolták", "őket,", "holott", "csupán", "az", "igazságot", "írták", "le."],
                    "solution": ["Izgatással", "vádolták", "őket,", "holott", "csupán", "az", "igazságot", "írták", "le."],
                    "english": "They were accused of incitement, whereas in fact they merely wrote down the truth."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-polemical-connectors"],
                    "prompt": [
                        {"speaker": "Irodalomtörténész", "text": "Miért váltott ki akkora politikai botrányt a Magyarország felfedezése könyvsorozat a harmincas években?"},
                        {"speaker": "Szociológus", "text": "_____"}
                    ],
                    "options": [
                        "Mert a hatalom harmonikusnak állította be a vidéket, holott a falukutatók könyörtelen pontossággal leplezték le a nagybirtokrendszer elmaradottságát.",
                        "Mert a szerzők nem jártak vidéken, holott mindenki szerette a verseket.",
                        "Mert a könyvek kizárólag középkori latin kódexeket elemeztek."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen eszközökkel dolgoztak a harmincas évek falukutató írói a szöveg szerint?",
                    "options": [
                        "Helyszíni megfigyeléssel, statisztikai adatokkal és mélyinterjúkkal térképezték fel a vidéki társadalom valóságát.",
                        "Kizárólag levéltári lovagregényekből merítettek ihletet.",
                        "Kormányzati megrendelésre készítettek idegenforgalmi prospektusokat."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Cosmopolitan Modernity and the 'Urbánus' Vision",
            "grammar_label": "High-register concessive clauses with jóllehet and ámbár ('albeit / although')",
            "goals": [
                "I can describe the intellectual program of the Urbánus camp and the journal Szép Szó.",
                "I can construct nuanced concessive arguments using jóllehet and ámbár.",
                "I can use B2 vocabulary related to constitutionalism, bourgeois radicalism, and European modernity."
            ],
            "story_segment": {
                "seg_slug": "urbanusok",
                "title": "A Szép Szó szerkesztősége és az európai mérce",
                "summary": "Centered around Budapest cafés and the journal Szép Szó (edited by Attila József, Pál Ignotus, and Ferenc Fejtő), the Urbánus intellectuals argued that Hungary's salvation lay in democratic institutions, individual liberty, and European civic modernity.",
                "location": "Budapest, Belvárosi kávéházak és a Szép Szó szerkesztősége (1936–1939)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Miközben a népi írók a magyar falu mélyrétegeit kutatták, Budapesten egy másik meghatározó szellemi tábor bontott zászlót, amelyet a kortársak urbánusoknak, vagyis városi elkötelezettségű gondolkodóknak neveztek. Szellemi fellegváruk az 1936-ban alapított Szép Szó című folyóirat volt, amelyet József Attila, Ignotus Pál és Fejtő Ferenc szerkesztett."
                    },
                    {
                        "type": "narration",
                        "text": "Az urbánus esszéisták és publicisták jól látták a magyar vidék nyomorát, jóllehet az ország megújításának kulcsát nem a paraszti hagyományok szakralizálásában, hanem a nyugati típusú polgári demokrácia, a jogállamiság és az emberi szabadságjogok kiteljesítésében keresték. Úgy érveltek, hogy szabadság és törvény előtti egyenlőség nélkül bármilyen földosztás csak újabb szolgasághoz vezetne."
                    },
                    {
                        "type": "narration",
                        "text": "A Szép Szó köre a huszadik század legmodernebb szellemi áramlatait — a freudi pszichoanalízist, a kritikai társadalomelméletet és a francia felvilágosodás racionalizmusát — igyekezett meghonosítani a hazai közgondolkodásban. József Attila híres programcikkében hangsúlyozta, hogy a szellem emberének az értelem és az érzelmi tisztánlátás nevében kell fellépnie a fasizmus és a fajelméletek terjedő őrületével szemben."
                    },
                    {
                        "type": "narration",
                        "text": "Az urbánus gondolkodókat ellenfeleik gyakran vádolták azzal, hogy idegenek a magyar rögvalóságtól és csak a pesti aszfalt világát ismerik, jóllehet soraikban olyan költők és kritikusok álltak, akik a legmélyebb szociális érzékenységgel fordultak a munkásság és a kisemmizettek felé. Számukra a város nem a romlottság szimbóluma volt, hanem a szabad sajtó, a szakszervezetek és a kritikai nyilvánosság terepe."
                    },
                    {
                        "type": "narration",
                        "text": "Hatvany Lajos, Zsolt Béla, Csécsy Imre és Fejtő Ferenc írásai arra figyelmeztettek, hogy Magyarország nem zárkózhat be egy sérelmi, harmadik utas utópiába: a Kárpát-medence népeinek sorsa elválaszthatatlan az európai alkotmányos kultúra védelmétől."
                    }
                ]
            },
            "words": [
                {"lemma": "jogállamiság", "translation": "rule of law / constitutional governance", "pos": "noun"},
                {"lemma": "polgárosodás", "translation": "embourgeoisement / civic modernization", "pos": "noun"},
                {"lemma": "kozmpolita", "translation": "cosmopolitan", "pos": "adjective"},
                {"lemma": "racionalizmus", "translation": "rationalism", "pos": "noun"},
                {"lemma": "szabadságjog", "translation": "civil liberty / fundamental right", "pos": "noun"},
                {"lemma": "harmadik utas", "translation": "Third-Way (neither Western capitalist nor Soviet collectivist)", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "jollehet-concessive",
                "title": "High-Register Concessive Framing with jóllehet and ámbár",
                "text1_title": "Moving Beyond bár to jóllehet in Academic & Essay Style",
                "text1": "While everyday Hungarian uses bár or habár for 'although', B2 literary, historical, and journalistic prose favors jóllehet ('albeit', 'although it is true that', 'granted that') and the slightly more classical ámbár. Literally composed of jól + lehet ('it may well be'), jóllehet graciously concedes a valid point in one clause while maintaining the weight of the main argument in the other.",
                "text2_title": "Clause Placement (Initial vs. Post-Main Clause)",
                "text2": "A jóllehet-clause can either precede the main clause (often picked up by mégis or azonban in the main clause) or follow the main clause to add a balanced qualification: 'Jóllehet az urbánusok Budapesten éltek, pontosan érzékelték az ország szociális válságát' OR 'Az urbánusok a polgári szabadságjogokat helyezték előtérbe, jóllehet a földkérdés súlyát sem vitatták.'",
                "table_title": "Concessive Structures with jóllehet in Intellectual Debate",
                "table_rows": [
                    ["Jóllehet a két tábor módszerei eltértek, mindkettő elutasította a feudalizmust.", "Although the methods of the two camps differed, both rejected feudalism."],
                    ["Az urbánusok a nyugati demokráciát tekintették mércének, jóllehet ismerték a hazai sajátosságokat.", "The Urbanists regarded Western democracy as the benchmark, albeit they knew domestic particularities."],
                    ["Ámbár a folyóirat csak néhány évig működött, hatása évtizedekig megmaradt.", "Albeit the journal operated for only a few years, its impact endured for decades."]
                ],
                "examples": [
                    {"spanish": "Az urbánus esszéisták jól látták a vidék nyomorát, jóllehet a megoldást a polgári demokrácia kiépítésében keresték.", "english": "The Urbanist essayists clearly saw the misery of the countryside, although they sought the solution in building bourgeois democracy."},
                    {"spanish": "Jóllehet sokan a pesti aszfalt íróinak nevezték őket, a Szép Szó szerzői mély szociális érzékenységgel írtak.", "english": "Although many called them writers of the Pest asphalt, the authors of Szép Szó wrote with deep social sensitivity."},
                    {"spanish": "A két irányzat élesen vitázott egymással, jóllehet a totális diktatúrákat mindkét fél elutasította.", "english": "The two currents debated each other sharply, even though both sides rejected totalitarian dictatorships."}
                ],
                "tip": "Unlike holott (which refutes a false claim), jóllehet acknowledges a genuine truth before weighing it against an even more decisive principle."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "pairs": [
                        ["jogállamiság", "rule of law"],
                        ["polgárosodás", "civic modernization"],
                        ["szabadságjog", "civil liberty"],
                        ["racionalizmus", "rationalism"],
                        ["harmadik utas", "Third-Way"],
                        ["kozmpolita", "cosmopolitan"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "question": "Melyik folyóirat volt az urbánus értelmiség és József Attila legfontosabb szellemi műhelye az 1930-as évek második felében?",
                    "options": [
                        "A Szép Szó, amelyet József Attila, Ignotus Pál és Fejtő Ferenc szerkesztett.",
                        "A Gazdasági Értesítő.",
                        "A Csíksomlyói Kalendárium."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "sentence": "Az urbánus gondolkodók szerint az egyéni _____ és a törvény előtti egyenlőség nélkül nem képzelhető el modern társadalom.",
                    "answer": "szabadságjogok",
                    "english": "According to Urbanist thinkers, without individual civil liberties and equality before the law, a modern society is unimaginable."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-polemical-connectors"],
                    "question": "How does 'jóllehet' differ in nuance from 'holott' in B2 argumentative Hungarian?",
                    "options": [
                        "'Jóllehet' concedes a true point ('although / granted that') while advancing a broader argument, whereas 'holott' unmasks a false claim or contradiction.",
                        "'Jóllehet' can only be used in questions, whereas 'holott' is used in commands.",
                        "'Jóllehet' means 'therefore', whereas 'holott' means 'for example'.",
                        "There is no difference; both mean 'because'."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "sentence": "_____ a Szép Szó csak néhány évig jelenhetett meg, esszéi alapjaiban gazdagították a magyar politikai kultúrát.",
                    "answer": "Jóllehet",
                    "english": "Although Szép Szó could only be published for a few years, its essays fundamentally enriched Hungarian political culture."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "tiles": ["Élesen", "vitáztak,", "jóllehet", "mindkét", "tábor", "elutasította", "a", "diktatúrát."],
                    "solution": ["Élesen", "vitáztak,", "jóllehet", "mindkét", "tábor", "elutasította", "a", "diktatúrát."],
                    "english": "They debated sharply, although both camps rejected dictatorship."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-polemical-connectors"],
                    "prompt": [
                        {"speaker": "Politológus", "text": "Igaz az a vád, hogy az urbánus írókat egyáltalán nem érdekelte a szegénység kérdése?"},
                        {"speaker": "Esztéta", "text": "_____"}
                    ],
                    "options": [
                        "Egyáltalán nem: jóllehet a nyugati jogállamiságot tekintették mércének, József Attila és társai rendkívüli szociális érzékenységgel védték a munkásságot és a nincsteleneket.",
                        "Igen, mert a Szép Szó kizárólag középkori lovagi tornákról közölt cikkeket.",
                        "Nem tudjuk, mert egyetlen számuk sem maradt fenn a könyvtárakban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Miben látták az urbánus gondolkodók Magyarország modernizációjának legfőbb zálogát?",
                    "options": [
                        "A nyugati típusú polgári demokrácia, a jogállamiság és az egyéni szabadságjogok kiteljesítésében.",
                        "A városi ipar felszámolásában és a céhek visszaállításában.",
                        "A sajtószabadság korlátozásában."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "Where the Two Camps Agreed—and Clashed",
            "grammar_label": "Sharp polemical pivots with csakhogy ('except that / the catch is') and mindazonáltal ('nevertheless')",
            "goals": [
                "I can analyze the shared diagnoses and sharp disagreements between the Népi and Urbánus camps.",
                "I can explain how thinkers like Attila József and István Bibó sought to transcend the false binary.",
                "I can deploy csakhogy and mindazonáltal to pivot persuasively in a debate."
            ],
            "story_segment": {
                "seg_slug": "vitapontok",
                "title": "Hídépítők a két part között: József Attila és Bibó István",
                "summary": "Though polemics between the two camps often grew bitter, Hungary's greatest minds—Attila József in the 1930s and political philosopher István Bibó in the 1940s—recognized that peasant emancipation and constitutional liberty could only succeed together.",
                "location": "Budapest és Debrecen (1934–1947)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ha ma visszalapozunk a Válasz, a Kelet Népe és a Szép Szó harmincas évekbeli évfolyamaiba, meglepve tapasztaljuk, milyen sok kérdésben értett egyet a két szemben álló szellemi tábor. Mindkét fél elviselhetetlennek tartotta az arisztokratikus nagybirtokrendszert, csakhogy amíg a népiek a parasztság felemelésétől várták a nemzet megújulását, addig az urbánusok a városi polgárság és a munkásság politikai emancipációját sürgették."
                    },
                    {
                        "type": "narration",
                        "text": "A viták hevében mindkét oldalon születtek igazságtalan torzítások és gyanakvó címkék. A népiek egy része kozmopolita gyökértelenséggel vádolta a pesti liberális sajtót, csakhogy ezzel gyakran a korabeli kirekesztő közbeszéd érveit visszhangozta; az urbánus kritikusok némelyike pedig romantikus ködösítésnek minősítette a falukutatást, mindazonáltal a szociográfiai művek tényanyagát ők sem hagyhatták figyelmen kívül."
                    },
                    {
                        "type": "narration",
                        "text": "A korszak legnagyobb szellemei azonban nem voltak hajlandók választani a falu és a város hamis alternatívája között. József Attila egyszerre volt a Szép Szó szerkesztője és a magyar paraszti sors egyik legmélyebb megénekeltetője: Hazám című szonettciklusában és A Dunánál című ódájában a társadalmi igazságosságot és az európai humanizmust elválaszthatatlan egységként fogalmazta meg."
                    },
                    {
                        "type": "narration",
                        "text": "A második világháború után Bibó István, a huszadik század legjelentősebb magyar politikai gondolkodója külön tanulmányokban elemezte a népi írók válságát és a magyar demokrácia zsákutcáit. Bibó rámutatott, hogy a parasztság társadalmi felszabadítása valóban nemzeti létkérdés, csakhogy ez a folyamat azonnal kisiklik, ha elszakad a nyugati alkotmányos szabadságjogok és a demokratikus intézmények tiszteletétől."
                    },
                    {
                        "type": "narration",
                        "text": "Bibó szintézise máig érvényes tanulsággal szolgál: egy közép-európai nemzetben a közösségi szolidaritás és az egyéni szabadság nem egymás ellenségei, hanem egymás előfeltételei."
                    }
                ]
            },
            "words": [
                {"lemma": "emancipáció", "translation": "emancipation / equal enfranchisement", "pos": "noun"},
                {"lemma": "hamis alternatíva", "translation": "false dichotomy / false dilemma", "pos": "noun"},
                {"lemma": "szintézis", "translation": "synthesis", "pos": "noun"},
                {"lemma": "kirekesztő", "translation": "exclusionary", "pos": "adjective"},
                {"lemma": "előfeltétel", "translation": "prerequisite / precondition", "pos": "noun"},
                {"lemma": "zsákutca", "translation": "dead end / cul-de-sac", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "csakhogy-mindazonaltal",
                "title": "Polemical Pivots: csakhogy ('the catch is') and mindazonáltal ('nevertheless')",
                "text1_title": "Introducing the Crucial Catch with csakhogy",
                "text1": "In analytical argumentation, csakhogy ('except that', 'only', 'the catch is that', 'however') dramatizes the exact point where a promising agreement or theory breaks down. Look at how István Bibó's reasoning works: 'A parasztság felszabadítása valóban létkérdés, csakhogy ez a folyamat kisiklik, ha elszakad a demokratikus intézményektől.'",
                "text2_title": "Maintaining Balance with mindazonáltal",
                "text2": "By contrast, mindazonáltal ('nevertheless', 'nonetheless', 'for all that') belongs to formal, measured academic prose. After acknowledging a flaw or criticism in the preceding clause, mindazonáltal reasserts an enduring value or undeniable achievement: 'A vita sokszor éles volt, mindazonáltal mindkét tábor maradandó műveket alkotott.'",
                "table_title": "Comparing csakhogy and mindazonáltal in Argumentation",
                "table_rows": [
                    ["Mindkét fél elutasította a feudalizmust, csakhogy másutt keresték a kiutat.", "Both sides rejected feudalism, except that they looked for the way out in different places."],
                    ["A terv papíron nagyszerűnek tűnt, csakhogy hiányoztak hozzá a demokratikus garanciák.", "The plan looked splendid on paper, the catch being that democratic guarantees were lacking."],
                    ["A népi mozgalom nem volt mentes az ellentmondásoktól, mindazonáltal történelmi érdemei vitathatatlanok.", "The populist movement was not free of contradictions; nevertheless, its historical merits are indisputable."]
                ],
                "examples": [
                    {"spanish": "Mindkét fél elviselhetetlennek tartotta a nagybirtokrendszert, csakhogy eltérő társadalmi rétegektől várták a megújulást.", "english": "Both sides considered the latifundia system unbearable, except that they expected renewal from different social strata."},
                    {"spanish": "Az urbánus kritikusok vitatták a népi romantikát, mindazonáltal a szociográfiák tényanyagát ők is elismerték.", "english": "Urbanist critics contested populist romanticism; nevertheless, they too acknowledged the factual material of the sociographies."},
                    {"spanish": "A közösségi felemelkedés elengedhetetlen, csakhogy szabadságjogok nélkül könnyen zsákutcába jut.", "english": "Communal uplift is indispensable, only without civil liberties it easily reaches a dead end."}
                ],
                "tip": "Think of csakhogy as zooming in on a critical obstacle ('ah, but here is the problem!'), whereas mindazonáltal zooms out to restore fair judgment ('even so, taking all this into account...')."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "pairs": [
                        ["emancipáció", "equal enfranchisement / emancipation"],
                        ["hamis alternatíva", "false dichotomy"],
                        ["szintézis", "synthesis"],
                        ["kirekesztő", "exclusionary"],
                        ["előfeltétel", "prerequisite"],
                        ["zsákutca", "dead end"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "question": "Hogyan értelmezte Bibó István a népi és az urbánus célkitűzések viszonyát?",
                    "options": [
                        "Úgy, hogy a parasztság társadalmi emancipációja és a nyugati alkotmányos szabadságjogok nem egymás ellenségei, hanem egymás előfeltételei.",
                        "Úgy, hogy a városokat teljesen le kell bontani a mezőgazdaság érdekében.",
                        "Úgy, hogy a két tábor között soha semmilyen párbeszéd nem lehetséges."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "sentence": "József Attila és Bibó István elutasította a falu és a város közötti _____ alternatívát, és a két hagyomány szintézisére törekedett.",
                    "answer": "hamis",
                    "english": "Attila József and István Bibó rejected the false dichotomy between village and city, striving for a synthesis of the two traditions."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-polemical-connectors"],
                    "question": "Which connector introduces a decisive 'catch' or obstacle that complicates an initial statement? 'A két tábor egyaránt modernizálni akarta az országot, _____ a megvalósítás sorrendjében élesen szembekerültek egymással.'",
                    "options": ["csakhogy", "jóllehet", "ugyanis", "következésképpen"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "sentence": "A harmincas évek vitái sokszor igazságtalan személyeskedésbe torkolltak, _____ a korszak esszéirodalma páratlan szellemi gazdagságról tanúskodik.",
                    "answer": "mindazonáltal",
                    "english": "The debates of the thirties often degenerated into unfair personal attacks; nevertheless, the essay literature of the era testifies to unmatched intellectual richness."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "tiles": ["A", "földreform", "szükséges", "volt,", "csakhogy", "jogállamiság", "nélkül", "nem", "elegendő."],
                    "solution": ["A", "földreform", "szükséges", "volt,", "csakhogy", "jogállamiság", "nélkül", "nem", "elegendő."],
                    "english": "Land reform was necessary, except that without the rule of law it is not sufficient."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-polemical-connectors"],
                    "prompt": [
                        {"speaker": "Egyetemi hallgató", "text": "Miért tekintjük József Attilát hídépítőnek a népi és az urbánus irányzat között?"},
                        {"speaker": "Professzor", "text": "_____"}
                    ],
                    "options": [
                        "Mert a Szép Szó szerkesztőjeként az európai racionalizmust képviselte, mindazonáltal költészetében a magyar paraszti és munkássors legmélyebb rétegeit szólaltatta meg.",
                        "Mert soha életében nem írt egyetlen politikai vagy társadalmi tárgyú verset sem.",
                        "Mert betiltotta a folyóiratokat Budapesten és Debrecenben."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen veszélyre figyelmeztetett Bibó István a második világháború utáni tanulmányaiban?",
                    "options": [
                        "Arra, hogy a népi felemelkedés azonnal zsákutcába jut, ha elszakad a demokratikus intézmények és a szabadságjogok tiszteletétől.",
                        "Arra, hogy túl sok könyvtár épült a kistelepüléseken.",
                        "Arra, hogy a magyar nyelv nem alkalmas tudományos vitákra."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "The Monor Meeting (1985): Bridging the Divide",
            "grammar_label": "Symmetric and topical contrasts with ellenben and ezzel szemben",
            "goals": [
                "I can recount the historical significance of the June 1985 Monor meeting between the Népi writers and the Democratic Opposition.",
                "I can contrast two perspectives or political strategies using ellenben and ezzel szemben.",
                "I can discuss opposition movements, minority protection, and democratic transition in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "monoritalalkozo",
                "title": "Negyvenöt értelmiségi a monorierdei kempingben (1985)",
                "summary": "In June 1985, under the watchful eyes of state security, forty-five leading figures of the populist movement and the urban democratic opposition met in a forest camp near Monor, forging a historic dialogue that paved the way for the 1989 transition.",
                "location": "Monorierdő, Kemping (1985. június 14–16.)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A Kádár-korszak évtizedeiben a hatalom tudatosan játszotta ki egymás ellen a magyar értelmiség különböző csoportjait. Aczél György kultúrpolitikája gondosan ügyelt arra, hogy a nemzeti és kisebbségi sorskérdésekért aggódó népi írók, valamint az emberi jogokat és a szamizdat sajtót szervező városi demokratikus ellenzék tagjai ne találjanak közös hangot egymással."
                    },
                    {
                        "type": "narration",
                        "text": "1985. június 14-én és 16-án azonban történelmi áttörés történt: Donáth Ferenc — az 1956-os forradalom egykori elítéltje, aki mindkét táborban megkérdőjelezhetetlen tekintélynek örvendett — negyvenöt vezető értelmiségit hívott össze a Monor melletti erdei kempingbe. A hivatalos bejelentés szerint baráti hétvégére érkeztek a résztvevők, ezzel szemben a tanácskozás a háború utáni első szabad, cenzúrázatlan ellenzéki parlamentként működött."
                    },
                    {
                        "type": "narration",
                        "text": "A fák alatti hosszú asztaloknál egymás mellett foglalt helyet Csoóri Sándor és Csurka István a népi oldalról, Kis János, Haraszti Miklós és Konrád György ellenben a demokratikus ellenzék emberi jogi álláspontját ismertette. Mindkét irányzat súlyosnak ítélte a Kádár-rendszer gazdasági és erkölcsi válságát, miközben nyíltan szembesítették egymást saját korábbi előítéleteikkel."
                    },
                    {
                        "type": "narration",
                        "text": "A monori találkozó egyik legfontosabb eredménye az volt, hogy a két tábor kölcsönösen elismerte egymás legfőbb erkölcsi alapvetését. A városi demokraták kimondták, hogy az erdélyi és felvidéki magyar kisebbségek jogfosztottsága egyetemes emberi jogi kérdés; a népi felszólalók ezzel szemben elfogadták, hogy a nemzeti megmaradás nem képzelhető el többpárti demokrácia és alkotmányos szabadságjogok nélkül."
                    },
                    {
                        "type": "narration",
                        "text": "Bár a rendszerváltás közeledtével a két irányzat később külön pártokba — a Magyar Demokrata Fórumba és a Szabad Demokraták Szövetségébe — tömörült, az 1985-ös monori kézfogás bizonyította, hogy a diktatúra falát csak a szellemi árkok betemetésével lehetett lebontani."
                    }
                ]
            },
            "words": [
                {"lemma": "demokratikus ellenzék", "translation": "Democratic Opposition (urban human-rights dissidents)", "pos": "noun"},
                {"lemma": "kisebbségvédelem", "translation": "protection of national minorities", "pos": "noun"},
                {"lemma": "jogfosztottság", "translation": "disenfranchisement / deprivation of rights", "pos": "noun"},
                {"lemma": "többpárti", "translation": "multi-party", "pos": "adjective"},
                {"lemma": "kijátszik egymás ellen", "translation": "to play off against one another (divide and rule)", "pos": "expression"},
                {"lemma": "áttörés", "translation": "breakthrough", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "ellenben-ezzel-szemben",
                "title": "Symmetric Contrast with ellenben and ezzel szemben",
                "text1_title": "Post-Topic Placement of ellenben ('by contrast / on the other hand')",
                "text1": "In sophisticated B2 prose, ellenben ('by contrast', 'on the other hand') functions much like the contrastive enclitic viszont, except in a higher, more literary register. While it can stand at the start of a clause, it is most idiomatic immediately after the contrasted topic: 'Csoóri Sándor a kisebbségi sorskérdéseket elemezte; Kis János ellenben az alkotmányos garanciákra helyezte a hangsúlyt.'",
                "text2_title": "Clause-Initial Anchoring with ezzel szemben ('in contrast to this')",
                "text2": "Ezzel szemben (literally 'facing/opposite this') explicitly points back to the entire preceding proposition or situation and sets up a direct structural counterpoint. It typically stands at the beginning of the second clause or immediately after the new subject: 'A hatalom a megosztottságban bízott; ezzel szemben Monoron negyvenöt értelmiségi ült közös asztalhoz.'",
                "table_title": "Contrasting Two Actors or Positions with ellenben vs. ezzel szemben",
                "table_rows": [
                    ["A népiek a közösségi sorskérdéseket hangsúlyozták, az urbánusok ellenben az egyéni jogokat.", "The populists emphasized communal questions of destiny; the urbanists, by contrast, emphasized individual rights."],
                    ["A hivatalos bejelentés baráti hétvégéről szólt; ezzel szemben szabad politikai tanácskozás zajlott.", "The official announcement spoke of a friendly weekend; in contrast to this, a free political conference took place."],
                    ["A cenzúra elszigeteltséget akart, Donáth Ferenc ellenben párbeszédet kezdeményezett.", "Censorship wanted isolation; Ferenc Donáth, on the other hand, initiated dialogue."]
                ],
                "examples": [
                    {"spanish": "A hivatalos bejelentés szerint baráti hétvégére érkeztek, ezzel szemben a tanácskozás szabad ellenzéki fórumként működött.", "english": "According to the official announcement they arrived for a friendly weekend; in contrast to this, the conference operated as a free opposition forum."},
                    {"spanish": "Csoóri Sándor a népi oldalt képviselte, Kis János ellenben a demokratikus ellenzék álláspontját ismertette.", "english": "Sándor Csoóri represented the populist side; János Kis, by contrast, presented the standpoint of the democratic opposition."},
                    {"spanish": "A hatalom megosztásra törekedett, a monori résztvevők ezzel szemben kölcsönösen elismerték egymás alapértékeit.", "english": "The regime strove for division; the participants at Monor, by contrast, mutually recognized each other's core values."}
                ],
                "tip": "Place ellenben right after the contrasted subject/topic ('Kis János ellenben...') for effortless native rhythm!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "pairs": [
                        ["demokratikus ellenzék", "urban human-rights dissident movement"],
                        ["kisebbségvédelem", "protection of national minorities"],
                        ["jogfosztottság", "deprivation of rights"],
                        ["többpárti", "multi-party"],
                        ["kijátszik egymás ellen", "to play off against one another"],
                        ["áttörés", "breakthrough"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "question": "Miért volt történelmi jelentőségű az 1985. júniusi monori találkozó?",
                    "options": [
                        "Mert évtizedes elszigeteltség után először ült közös asztalhoz a népi ellenzék és a városi demokratikus ellenzék negyvenöt vezető személyisége.",
                        "Mert ott írták alá az első magyar vasútépítési szerződést.",
                        "Mert a Kádár-kormány ott osztott állami kitüntetéseket a cenzoroknak."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "sentence": "Aczél György kultúrpolitikája évtizedeken át próbálta _____ egymás ellen a népi és az urbánus értelmiséget.",
                    "answer": "kijátszani",
                    "english": "For decades, György Aczél's cultural policy tried to play the populist and urbanist intelligentsia off against one another."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-polemical-connectors"],
                    "question": "Where is 'ellenben' most idiomatically placed when contrasting a second subject ('Kis János') with a first subject ('Csoóri Sándor')?",
                    "options": [
                        "Immediately after the contrasted second subject: 'Csoóri Sándor a népi hagyományról beszélt, Kis János ellenben az emberi jogi garanciákat elemezte.'",
                        "At the very end of the sentence after the period.",
                        "Between the definite article 'a' and its noun.",
                        "Inside the verb prefix."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "sentence": "Az állambiztonság a két tábor szakadására számított; _____ Monoron a résztvevők közös jegyzőkönyvben rögzítették az előadásokat.",
                    "answer": "ezzel szemben",
                    "english": "State security counted on a split between the two camps; in contrast to this, at Monor the participants recorded the lectures in shared minutes."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "tiles": ["A", "hatalom", "megosztást", "akart,", "Donáth", "Ferenc", "ellenben", "párbeszédet", "teremtett."],
                    "solution": ["A", "hatalom", "megosztást", "akart,", "Donáth", "Ferenc", "ellenben", "párbeszédet", "teremtett."],
                    "english": "The regime wanted division; Ferenc Donáth, by contrast, created dialogue."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-polemical-connectors"],
                    "prompt": [
                        {"speaker": "Történész", "text": "Hogyan közeledett egymáshoz a két tábor álláspontja a kisebbségek és a demokrácia kérdésében Monoron?"},
                        {"speaker": "Résztvevő", "text": "_____"}
                    ],
                    "options": [
                        "Az urbánus demokraták elismerték, hogy a határon túli magyarok védelme emberi jogi kötelesség, a népi írók ezzel szemben kimondták, hogy többpárti jogállam nélkül nincs nemzeti megújulás.",
                        "Mindkét fél úgy döntött, hogy felhagynak az írással és külföldre költöznek.",
                        "A résztvevők nem beszéltek politikáról, ellenben egész hétvégén horgásztak."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Ki volt az az 1956-os politikus, akinek a tekintélye lehetővé tette a monori találkozó megszervezését?",
                    "options": [
                        "Donáth Ferenc, akit mind a népi írók, mind a demokratikus ellenzék tagjai tiszteltek.",
                        "Aczél György kulturális miniszterhelyettes.",
                        "Rákosi Mátyás."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Echoes of the Debate in Modern Hungary",
            "grammar_label": "Synthesizing polemical, concessive, and contrastive connectors in B2 essay discourse",
            "goals": [
                "I can trace how the Népi–Urbánus fault line influenced post-1989 Hungarian party politics and cultural debates.",
                "I can combine holott, jóllehet, csakhogy, ellenben, and ezzel szemben to construct a balanced B2 analytical essay.",
                "I can evaluate modern urban–rural relations and European identity in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "modernvisszhangok",
                "title": "Szellemi törésvonalak a rendszerváltás után és ma",
                "summary": "After 1989, the vocabulary of the interwar debate returned to Hungarian political life, shaping party identities and cultural journalism, even as 21st-century sociologists point out how globalization and infrastructure have transformed both city and countryside.",
                "location": "Budapest és a kortárs magyar nyilvánosság (1989–napjainkig)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1989–1990-es rendszerváltás hajnalán sokan remélték, hogy a szabad választásokkal a régi népi–urbánus ellentét végleg a tankönyvek lapjaira kerül, csakhogy a születő többpártrendszer szinte azonnal újraélesztette a történelmi törésvonalakat. A lakiteki sátorban megalakult Magyar Demokrata Fórum elsősorban a népi-nemzeti hagyományra, a Szabad Demokraták Szövetsége ellenben az urbánus-liberális örökségre építette politikai arculatát."
                    },
                    {
                        "type": "narration",
                        "text": "A kilencvenes évek sajtóvitáiban a két fogalom gyakran szimbolikus lövészárokká merevedett, jóllehet a huszadik század végi magyar társadalom már alig hasonlított a harmincas évek agrárországára. Az egykori uradalmi cselédek és zsellérek világa eltűnt, Budapest és a vidéki egyetemi városok között pedig állandóvá vált a szellemi és gazdasági átjárás."
                    },
                    {
                        "type": "narration",
                        "text": "A huszonegyedik században a vita új fogalmi köntösben — gyakran a nemzeti szuverenitás és az európai föderalizmus, illetve a globális hálózatok és a helyi közösségek közötti feszültségként — tér vissza a közbeszédbe. Egyes publicisták ma is kibékíthetetlen ellentétként ábrázolják a főváros és a vidék viszonyát, holott a mindennapi életben a digitalizáció, az ingázás és a hazai turizmus szorosan összekapcsolja a két teret."
                    },
                    {
                        "type": "narration",
                        "text": "A kortárs szociológusok arra hívják fel a figyelmet, hogy a valódi társadalmi kihívások ma már nem ideológiai címkék mentén húzódnak. Miközben a szimbolikus kultúrharc a régi jelszavakat ismétli, ezzel szemben a kistelepülések elöregedése, a minőségi oktatáshoz való hozzáférés és a megfizethető városi lakhatás olyan gyakorlati kérdések, amelyek közös megoldást kívánnak."
                    },
                    {
                        "type": "narration",
                        "text": "Ha ma újraolvassuk Illyés Gyula, József Attila és Bibó István műveit, láthatjuk, hogy a népi és az urbánus hagyomány együtt alkotja a modern magyar önismeret két felét: az egyik a helyi közösségek iránti felelősségre, a másik a szabad és kritikus európai horizontra emlékeztet bennünket."
                    }
                ]
            },
            "words": [
                {"lemma": "törésvonal", "translation": "fault line / cleavage (in politics or society)", "pos": "noun"},
                {"lemma": "szuverenitás", "translation": "sovereignty", "pos": "noun"},
                {"lemma": "kultúrharc", "translation": "culture war (Kulturkampf)", "pos": "noun"},
                {"lemma": "lövészárok", "translation": "trench (often figurative: ideological trench)", "pos": "noun"},
                {"lemma": "önismeret", "translation": "self-knowledge / national self-understanding", "pos": "noun"},
                {"lemma": "átjárás", "translation": "passage / permeability / mobility between spheres", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "polemical-synthesis",
                "title": "Architecting a Multi-Paragraph B2 Debate Essay",
                "text1_title": "Choosing the Exact Polemical Connector for Each Move",
                "text1": "At the B2 level, mastering Hungarian essay style means selecting the exact connector that matches the logical relationship between your claims:\n• Use jóllehet to grant a valid historical or sociological nuance before stating your main thesis.\n• Use holott to dismantle an unfounded stereotype or false dichotomy with empirical facts.\n• Use csakhogy to pinpoint the practical obstacle that derailed an expectation.\n• Use ellenben (post-topic) and ezzel szemben (clause-initial) to balance two movements, parties, or perspectives symmetrically.",
                "text2_title": "Avoiding Repetitive 'de' and 'viszont' Chains",
                "text2": "In spoken A2/B1 Hungarian, speakers often chain clauses together with de ('but') and viszont ('however'). Replacing those with the five polemical connectors of this unit immediately elevates your writing to the register of Hungarian literary journals, university seminars, and C1-ready commentary.",
                "table_title": "Summary Matrix of B2 Polemical & Concessive Connectors",
                "table_rows": [
                    ["jóllehet / ámbár (concessive)", "Jóllehet a társadalom átalakult, a vita szókincse tovább élt."],
                    ["holott (counter-reality)", "Sokan kibékíthetetlennek tartják a két tábort, holott egymásra vannak utalva."],
                    ["csakhogy (the catch)", "Sokan a vita lezárását várták, csakhogy a pártok újraélesztették azt."],
                    ["ellenben / ezzel szemben (contrast)", "Az egyik fél a hagyományt, a másik ellenben az intézményeket hangsúlyozta."]
                ],
                "examples": [
                    {"spanish": "Sokan remélték, hogy a vita a múlté lesz, csakhogy a születő pártrendszer újraélesztette a történelmi törésvonalakat.", "english": "Many hoped that the debate would belong to the past, except that the emerging party system revived the historical fault lines."},
                    {"spanish": "A fogalmak gyakran lövészárokká merevedtek, jóllehet a társadalom már alig hasonlított a harmincas évek világára.", "english": "The concepts often hardened into trenches, although society barely resembled the world of the 1930s anymore."},
                    {"spanish": "Egyesek kibékíthetetlen ellentétet látnak, holott a két hagyomány együtt alkotja a magyar önismeret egészét.", "english": "Some see an irreconcilable opposition, whereas in fact the two traditions together form the whole of Hungarian self-understanding."}
                ],
                "tip": "When writing a B2 opinion essay, try to pair one concessive clause (jóllehet...) with one empirical refutation (holott...) in your body paragraphs."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "pairs": [
                        ["törésvonal", "political or social fault line"],
                        ["szuverenitás", "sovereignty"],
                        ["kultúrharc", "culture war"],
                        ["lövészárok", "ideological trench"],
                        ["önismeret", "self-understanding"],
                        ["átjárás", "mobility / permeability between spheres"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "question": "Hogyan jelent meg a népi–urbánus törésvonal az 1989–1990-es rendszerváltás után?",
                    "options": [
                        "Az újonnan alakuló pártok és kulturális folyóiratok arculatában, majd a nemzeti szuverenitásról és az európai integrációról szóló vitákban.",
                        "Teljesen eltűnt, és soha többé nem említették a sajtóban.",
                        "Kizárólag a közlekedési szabályok módosításában."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-urbanusnepi-vocab"],
                    "sentence": "A népi és az urbánus hagyomány nem egymást kizáró ellentét, hanem a modern magyar nemzeti _____ két egymást kiegészítő fele.",
                    "answer": "önismeret",
                    "english": "The populist and urbanist traditions are not mutually exclusive opposites, but two complementary halves of modern Hungarian national self-understanding."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-polemical-connectors"],
                    "question": "Choose the connector pair that accurately completes both blanks: '_____ a harmincas évek agrárvilága régen megszűnt, egyes publicisták mégis a régi jelszavakat ismétlik, _____ a mai falvak és városok gondjai közös megoldást kívánnak.'",
                    "options": [
                        "Jóllehet ... holott",
                        "Holott ... miszerint",
                        "Mivel ... csakhogy",
                        "Tehát ... ellenben"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "sentence": "Az egyik politikai irányzat a helyi hagyományok védelmére épített, a másik _____ az európai intézményi garanciákat helyezte előtérbe.",
                    "answer": "ellenben",
                    "english": "One political current built on the protection of local traditions; the other, by contrast, foregrounded European institutional guarantees."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-polemical-connectors"],
                    "tiles": ["Jóllehet", "a", "társadalom", "átalakult,", "a", "történelmi", "törésvonalak", "fennmaradtak."],
                    "solution": ["Jóllehet", "a", "társadalom", "átalakult,", "a", "történelmi", "törésvonalak", "fennmaradtak."],
                    "english": "Although society transformed, the historical fault lines persisted."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-polemical-connectors"],
                    "prompt": [
                        {"speaker": "Szerkesztő", "text": "Van még értelme a huszonegyedik században népi és urbánus táborról beszélni?"},
                        {"speaker": "Társadalomkutató", "text": "_____"}
                    ],
                    "options": [
                        "Jóllehet a szimbolikus politikában gyakran visszatérnek ezek a címkék, a valóságban a digitalizáció és a mobilitás összekapcsolja a várost és a vidéket, csakhogy a régi előítéletek lassan kopnak ki.",
                        "Nincs, mert Magyarországon ma már senki sem lakik városokban.",
                        "Igen, mert a lakosság fele még mindig uradalmi cselédként dolgozik."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen tanulságot kínál ma Illyés Gyula, József Attila és Bibó István öröksége a szöveg zárása szerint?",
                    "options": [
                        "Azt, hogy a helyi közösségek iránti szociális felelősség és a szabad, kritikus európai horizont együtt alkotja a magyar kultúra egészét.",
                        "Azt, hogy a városi és a vidéki íróknak tilos egymás műveit olvasniuk.",
                        "Azt, hogy a szociográfia műfaját be kell tiltani."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can explain the origins, key figures, and historical evolution of the Népi–Urbánus debate from the 1930s through the 1985 Monor meeting to today.",
            "I can use holott, jóllehet, csakhogy, ellenben, and ezzel szemben with precision in polemical and academic Hungarian.",
            "I can synthesize competing viewpoints without falling into false dichotomies.",
            "I can deploy 30 B2 intellectual history and sociological terms accurately."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-urbanusnepi-vocab"],
                "pairs": [
                    ["falukutató", "village sociographer"],
                    ["jogállamiság", "rule of law"],
                    ["hamis alternatíva", "false dichotomy"],
                    ["demokratikus ellenzék", "urban human-rights dissident movement"],
                    ["törésvonal", "political / social fault line"],
                    ["szintézis", "synthesis"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-polemical-connectors"],
                "question": "Which connector is specifically used to unmask a contradiction between an outward appearance/claim and the real facts ('whereas in fact')?",
                "options": ["holott", "jóllehet", "miszerint", "ugyanis"],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-urbanusnepi-vocab"],
                "question": "Hol találkozott 1985 júniusában a népi írók és a városi demokratikus ellenzék negyvenöt képviselője Donáth Ferenc meghívására?",
                "options": [
                    "A Monor melletti erdei kempingben.",
                    "A párizsi Sorbonne dísztermében.",
                    "A bécsi operaházban.",
                    "A pozsonyi országgyűlésben."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-urbanusnepi-vocab"],
                "sentence": "A harmincas években Féja Géza, Illyés Gyula és Kovács Imre az irodalmi _____ műfajával tárta fel a szegényparasztság sorsát.",
                "answer": "szociográfia",
                "english": "In the 1930s, Géza Féja, Gyula Illyés, and Imre Kovács revealed the plight of the poor peasantry through the genre of literary sociography."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-polemical-connectors"],
                "sentence": "A hivatalos sajtó idillinek festette le a falusi életet, _____ hárommillió nincstelen paraszt élt föld nélkül.",
                "answer": "holott",
                "english": "The official press painted village life as idyllic, whereas in fact three million destitute peasants lived without land."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-polemical-connectors"],
                "sentence": "Mindkét tábor elutasította a félfeudális rendszert, _____ a modernizáció legfőbb szereplőjét más társadalmi rétegben látták.",
                "answer": "csakhogy",
                "english": "Both camps rejected the semi-feudal system, except that they saw the main protagonist of modernization in different social strata."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-polemical-connectors"],
                "prompt": [
                    {"speaker": "Eszmetörténész", "text": "Hogyan viszonyult egymáshoz a népi és az urbánus tábor a monori találkozón?"},
                    {"speaker": "Politológus", "text": "_____"}
                ],
                "options": [
                    "Jóllehet a múltbeli sérelmeket is őszintén megvitatták, közösen mondták ki, hogy a kisebbségvédelem és a többpárti jogállamiság elválaszthatatlan egymástól.",
                    "A találkozó tíz perc után félbeszakadt, mert senki sem akart felszólalni.",
                    "Mindkét fél az egypártrendszer fenntartása mellett szavazott."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-polemical-connectors"],
                "question": "Which sentence demonstrates native B2 placement of 'ellenben' and 'ezzel szemben'?",
                "options": [
                    "A hatalom a megosztottságra épített; ezzel szemben Monoron a népi írók a közösségi jogokról, az urbánusok ellenben az alkotmányos garanciákról beszéltek egymást tisztelve.",
                    "Ellenben a népi írók szemben ezzel beszéltek.",
                    "A hatalom ellenben szemben ezzel volt.",
                    "Monoron szemben ezzel ellenben ültek."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-polemical-connectors"],
                "prompt": [
                    {"speaker": "Kritikus", "text": "Miért tartjuk Bibó István 1945 utáni tanulmányait a magyar politikai gondolkodás csúcspontjának?"},
                    {"speaker": "Szociológus", "text": "_____"}
                ],
                "options": [
                    "Mert rámutatott, hogy a parasztság felemelése elengedhetetlen, csakhogy szabadságjogok és demokratikus intézmények nélkül bármilyen népi mozgalom zsákutcába jut.",
                    "Mert bebizonyította, hogy a falukutatás teljesen felesleges volt.",
                    "Mert azt javasolta, hogy szüntessék meg az összes pesti folyóiratot."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-polemical-connectors"],
                "tiles": ["A", "hatalom", "elszigeteltséget", "akart,", "ezzel", "szemben", "Monoron", "párbeszéd", "született."],
                "solution": ["A", "hatalom", "elszigeteltséget", "akart,", "ezzel", "szemben", "Monoron", "párbeszéd", "született."],
                "english": "The regime wanted isolation; in contrast to this, dialogue was born at Monor."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-polemical-connectors"],
                "tiles": ["Csoóri", "a", "népi", "oldalt,", "Kis", "ellenben", "a", "demokratikus", "ellenzéket", "képviselte."],
                "solution": ["Csoóri", "a", "népi", "oldalt,", "Kis", "ellenben", "a", "demokratikus", "ellenzéket", "képviselte."],
                "english": "Csoóri represented the populist side; Kis, by contrast, represented the democratic opposition."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-polemical-connectors"],
                "template": [
                    {
                        "prompt": "Write a sentence contrasting the official interwar image of Hungarian villages with the reality uncovered by village sociographers (use 'holott').",
                        "answer": "A hivatalos propaganda harmonikus falvakról beszélt, holott a szociográfusok kimutatták, hogy az uradalmi cselédek nyomorban éltek."
                    },
                    {
                        "prompt": "Write a sentence acknowledging the fierce debates between the two camps while affirming their common democratic convergence at Monor (use 'jóllehet' and 'ellenben' or 'mégis').",
                        "answer": "Jóllehet a népi és az urbánus értelmiség évtizedeken át élesen vitázott egymással, Monoron mégis közösen álltak ki a többpárti demokrácia és a kisebbségvédelem mellett."
                    }
                ]
            }
        ]
    }
}


UNIT_17_MEDIATORTENET = {
    "unit_num": 17,
    "slug": "mediatortenet",
    "title": "From the Town Crier to the Digital Public Sphere",
    "grammar_skill": "b2-evidential-framing",
    "vocab_skill": "b2-mediatortenet-vocab",
    "theme": "Hungarian journalism, Telefonhírmondó and media history",
    "location": "Pest-Buda és a modern budapesti szerkesztőségek",
    "intro_body": [
        "Hungary's media history is a story of remarkable political courage and technological ingenuity. In 1841, Lajos Kossuth transformed a dry news sheet into the Pesti Hírlap, inventing the modern Hungarian political editorial (vezércikk) and forging a nationwide reform public sphere. Half a century later, in 1893, Tivadar Puskás launched Budapest's Telefonhírmondó—the world's first daily spoken 'newspaper' transmitted over telephone wires, thirty years before broadcast radio.",
        "In this unit, you will trace the evolution of the Hungarian public sphere from Kossuth's printing press and Puskás's telephone earpieces through 20th-century radio and television milestones to the post-1989 media market and contemporary digital literacy. Grammatically, you will master epistemic and evidential framing expressions (értesülések szerint, úgy hírlik, a jelek szerint, minden jel arra mutat, hogy...)."
    ],
    "combined_story_title": "A Telefonhírmondótól az algoritmusokig",
    "combined_story_summary": "From Lajos Kossuth's Pesti Hírlap (1841) and Tivadar Puskás's pioneering Telefonhírmondó (1893—the world's first telephone newspaper) to radio, television, post-1989 press transformation, and digital media literacy.",
    "lessons": [
        {
            "num": 1,
            "title": "Kossuth's Pesti Hírlap and the Birth of Modern Journalism",
            "grammar_label": "Source-attributive evidential postpositional phrases (értesülések szerint, sajtóhírek szerint)",
            "goals": [
                "I can explain how Lajos Kossuth revolutionized Hungarian journalism with Pesti Hírlap in 1841.",
                "I can attribute claims and reports to specific or institutional sources using szerint phrases.",
                "I can discuss censorship, editorials, and the Reform Era public sphere in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "pestihirlap",
                "title": "Kossuth Lajos vezércikkei és a Pesti Hírlap forradalma (1841)",
                "summary": "When bookseller Gusztáv Landerer received permission in 1841 to launch Pesti Hírlap with Lajos Kossuth as editor, the Vienna court hoped to co-opt a troublesome opposition voice; instead, Kossuth created modern Hungarian political journalism.",
                "location": "Pest, Hatvani utca (1841–1844)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1830-as években a magyarországi újságok még száraz hírlevelek voltak, amelyek a szigorú előzetes cenzúra miatt legfeljebb külföldi udvari eseményekről és időjárási furcsaságokról számolhattak be. Kossuth Lajos először kézzel másolt Országgyűlési Tudósításaival, majd a vármegyei vitákat ismertető Törvényhatósági Tudósításokkal kerülte meg a nyomdai tilalmat, mígnem a bécsi udvar három év börtönre ítélte."
                    },
                    {
                        "type": "narration",
                        "text": "1840-es szabadulása után meglepő fordulat történt: korabeli bécsi értesülések szerint Metternich kancellár és a rendőri vezetés úgy vélte, könnyebben féken tarthatja Kossuthot, ha hivatalos, cenzúrázott lapot engedélyeznek számára. Landerer Gusztáv pesti nyomdász így kapott engedélyt a Pesti Hírlap megindítására, amelynek első száma 1841. január 2-án jelent meg Kossuth szerkesztésében."
                    },
                    {
                        "type": "narration",
                        "text": "A számítás azonban visszájára sült el. Kossuth meghonosította a magyar sajtóban a vezércikk műfaját: a lap első oldalán szenvedélyes, mégis jogilag kikezdhetetlen érveléssel követelte a jobbágyfelszabadítást, a közteherviselést, az esküdtszékeket és a hazai ipar védelmét. A nyomdai kimutatások szerint a Pesti Hírlap előfizetőinek száma néhány hónap alatt a kezdeti hatvanról több mint ötezerre ugrott, s egy-egy példányt a kávéházakban és kaszinókban tucatnyian olvastak fel egymásnak."
                    },
                    {
                        "type": "narration",
                        "text": "A lap sikere heves sajtóvitát váltott ki: Széchenyi István A Kelet Népe című röpiratában arra figyelmeztetett, hogy Kossuth érzelmekre ható stílusa forradalmi szakadékba sodorhatja az országot. Kossuth tiszteletteljes, de határozott vezércikkekben válaszolt a legnagyobb magyarnak, s ezzel megszületett a modern magyar politikai nyilvánosság."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor 1844-ben Kossuthot eltávolították a szerkesztői székből, a magyar olvasóközönség már visszafordíthatatlanul hozzászokott ahhoz, hogy a sajtó nem a hatalom szócsöve, hanem a közügyek szabad vitatere."
                    }
                ]
            },
            "words": [
                {"lemma": "vezércikk", "translation": "lead editorial / leading article", "pos": "noun"},
                {"lemma": "előzetes cenzúra", "translation": "prior censorship (pre-publication review)", "pos": "noun"},
                {"lemma": "előfizető", "translation": "subscriber", "pos": "noun"},
                {"lemma": "röpirat", "translation": "pamphlet / political tract", "pos": "noun"},
                {"lemma": "közteherviselés", "translation": "universal taxation / shared public burden", "pos": "noun"},
                {"lemma": "nyilvánosság", "translation": "public sphere / publicity", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "source-attribution-szerint",
                "title": "Evidential Source Attribution with szerint Phrases",
                "text1_title": "Distancing the Writer from Unverified or Reported Claims",
                "text1": "In B2 journalism and historical writing, authors carefully signal how they know a piece of information. Hungarian builds source-attributive phrases using a plural or modified noun phrase followed by the postposition szerint ('according to'):\n• sajtóhírek szerint ('according to press reports')\n• korabeli értesülések szerint ('according to contemporary intelligence/reports')\n• a nyomdai kimutatások szerint ('according to printing-house records')\n• szemtanúk beszámolói szerint ('according to eyewitness accounts')",
                "text2_title": "Register and Word Order in News & Historical Prose",
                "text2": "Unlike English, where 'according to X' often sits at the end of a sentence after a comma, Hungarian places the szerint phrase at the very beginning of the clause (as the frame-setting topic) so the reader immediately knows the epistemic status of the claim that follows.",
                "table_title": "High-Frequency Evidential Attribution Formulas",
                "table_rows": [
                    ["Korabeli értesülések szerint Bécs így akarta ellenőrizni Kossuthot.", "According to contemporary reports, Vienna wanted to control Kossuth this way."],
                    ["A nyomdai adatok szerint az előfizetők száma ötezer fölé emelkedett.", "According to printing records, the number of subscribers rose above five thousand."],
                    ["A kortársak beszámolói szerint egyetlen lapszámot tucatnyian olvastak.", "According to contemporaries' accounts, a single issue was read by dozens."]
                ],
                "examples": [
                    {"spanish": "Korabeli bécsi értesülések szerint Metternich úgy vélte, könnyebben féken tarthatja Kossuthot egy cenzúrázott lappal.", "english": "According to contemporary Viennese reports, Metternich believed he could more easily keep Kossuth in check with a censored paper."},
                    {"spanish": "A nyomdai kimutatások szerint a Pesti Hírlap előfizetőinek száma néhány hónap alatt ötezerre ugrott.", "english": "According to printing records, the number of Pesti Hírlap subscribers jumped to five thousand within a few months."},
                    {"spanish": "Sajtótörténeti kutatások szerint Kossuth vezércikkei teremtették meg a modern magyar politikai újságírást.", "english": "According to press-history research, Kossuth's editorials created modern Hungarian political journalism."}
                ],
                "tip": "Never put a comma after an initial szerint phrase in Hungarian: write 'Sajtóhírek szerint a lap azonnal elfogyott' (no comma after szerint!)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "pairs": [
                        ["vezércikk", "lead editorial"],
                        ["előzetes cenzúra", "pre-publication censorship"],
                        ["előfizető", "subscriber"],
                        ["röpirat", "political pamphlet"],
                        ["közteherviselés", "universal taxation"],
                        ["nyilvánosság", "public sphere"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "question": "Milyen új újságírói műfajt honosított meg Kossuth Lajos az 1841-ben indult Pesti Hírlap első oldalán?",
                    "options": [
                        "A politikai és társadalmi reformok mellett érvelő vezércikket.",
                        "A keresztrejtvényt és a sporthíradót.",
                        "A tőzsdei telefonközvetítést."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "sentence": "Széchenyi István A Kelet Népe című _____ bírálta Kossuth Lajos érzelmekre ható újságírói stílusát.",
                    "answer": "röpiratában",
                    "english": "In his pamphlet People of the East, István Széchenyi criticized Lajos Kossuth's emotionally charged journalistic style."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-evidential-framing"],
                    "question": "Which phrase idiomatically attributes a historical claim to contemporary reports at the start of a Hungarian sentence?",
                    "options": [
                        "Korabeli értesülések szerint",
                        "Korabeli értesülések által",
                        "Korabeli értesülésekből miatt",
                        "Korabeli értesülések helyett"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "sentence": "A nyomdai kimutatások _____ a Pesti Hírlap példányszáma néhány hónap alatt meghaladta az ötezret.",
                    "answer": "szerint",
                    "english": "According to printing-house records, the circulation of Pesti Hírlap exceeded five thousand within a few months."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "tiles": ["Korabeli", "beszámolók", "szerint", "egy", "lapszámot", "tucatnyian", "olvastak", "fel."],
                    "solution": ["Korabeli", "beszámolók", "szerint", "egy", "lapszámot", "tucatnyian", "olvastak", "fel."],
                    "english": "According to contemporary accounts, a single issue was read aloud by dozens."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-evidential-framing"],
                    "prompt": [
                        {"speaker": "Diák", "text": "Miért engedélyezte a bécsi udvar 1841-ben, hogy a börtönből szabadult Kossuth Lajos újságot szerkesszen?"},
                        {"speaker": "Történész", "text": "_____"}
                    ],
                    "options": [
                        "Titkosrendőri jelentések szerint Metternich abban bízott, hogy az előzetes cenzúra alatt álló lapban könnyebben kordában tarthatják Kossuthot.",
                        "Mert Metternich maga is a Pesti Hírlap vezércikkírója akart lenni.",
                        "Mert 1841-ben Bécsben eltörölték a monarchiát."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen reformokat sürgetett Kossuth Lajos a Pesti Hírlap vezércikkeiben?",
                    "options": [
                        "A jobbágyfelszabadítást, a közteherviselést, az esküdtszékek felállítását és a hazai ipar védelmét.",
                        "A latin hivatalos nyelv örökös fenntartását.",
                        "A vármegyei gyűlések bezárását."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Tivadar Puskás and Budapest's Telefonhírmondó (1893)",
            "grammar_label": "Hearsay and unverified-report evidentials (úgy hírlik, hogy...; állítólag; a szóbeszéd szerint)",
            "goals": [
                "I can describe how Tivadar Puskás invented and operated the Telefonhírmondó in Budapest starting in 1893.",
                "I can mark rumors, unconfirmed news, and popular hearsay using úgy hírlik, hogy..., állítólag, and a szóbeszéd szerint.",
                "I can use B2 telecommunications and turn-of-the-century media vocabulary."
            ],
            "story_segment": {
                "seg_slug": "telefonhirmondo",
                "title": "A beszélő újság: Puskás Tivadar Telefonhírmondója (1893)",
                "summary": "Three decades before the birth of commercial radio broadcasting, Hungarian inventor Tivadar Puskás launched the Telefonhírmondó in Budapest on February 15, 1893—transmitting live news, stock prices, and opera performances over telephone lines.",
                "location": "Budapest, Magyar utca és Rákóczi út (1893)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Amikor 1893. február 15-én Budapesten megszólalt a világ első beszélő újságja, a Telefonhírmondó, a fővárosi polgárok közül sokan még hitetlenkedve csóválták a fejüket. Úgy hírlik, hogy egyes kávéházi törzsvendégek kezdetben bűvészmutatványnak tartották a falra szerelt két fülhallgatót, amelyből pontosan óránként csendült fel a bemondó, vagyis a „stentor” tiszta, zengő hangja."
                    },
                    {
                        "type": "narration",
                        "text": "A találmány atyja Puskás Tivadar volt, aki korábban Thomas Alva Edison közvetlen munkatársaként dolgozott a telefonközpontok kifejlesztésén. Puskás felismerte, hogy a telefonvezeték nemcsak két ember magánbeszélgetésére alkalmas, hanem arra is, hogy egy központi stúdióból egyszerre több ezer előfizető lakásába, szállodai szobájába és orvosi várótermébe továbbítsanak szerkesztett műsort."
                    },
                    {
                        "type": "narration",
                        "text": "A Telefonhírmondó harminc évvel a rádió születése előtt feltalálta a modern műsorszórást. A szigorú napirend szerint reggel kilenctől este kilencig negyedórás és félórás blokkokban követték egymást a tőzsdei árfolyamok, az országgyűlési tudósítások, a pontos időjelzés, a színházi kritikák, valamint az angol, német és francia nyelvleckék."
                    },
                    {
                        "type": "narration",
                        "text": "A szerkesztőség különösen büszke volt arra, hogy a kósza pletykákkal szemben csak ellenőrzött tényeket közölt. Ha a városban valamilyen szenzációs hír terjedt el — például állítólag lemondott egy miniszter vagy összeomlott egy külföldi bankház —, a bemondó azonnal jelezte, mi az, ami a szóbeszéd szerint csupán találgatás, és mi az, amit a távirati iroda hivatalosan is megerősített."
                    },
                    {
                        "type": "narration",
                        "text": "Esténként pedig a fülhallgatókból a Magyar Királyi Operaház és a Népszínház élő előadásai szóltak: a budapesti családok a saját nappalijukban hallgathatták az operák áriáit, miközben a világ más nagyvárosaiban még csak álmodoztak a távoli hangközvetítésről."
                    }
                ]
            },
            "words": [
                {"lemma": "műsorszórás", "translation": "broadcasting", "pos": "noun"},
                {"lemma": "telefonközpont", "translation": "telephone exchange", "pos": "noun"},
                {"lemma": "bemondó", "translation": "announcer / newsreader", "pos": "noun"},
                {"lemma": "fülhallgató", "translation": "earpiece / headphones", "pos": "noun"},
                {"lemma": "árfolyam", "translation": "exchange rate / stock quotation", "pos": "noun"},
                {"lemma": "szóbeszéd", "translation": "rumor / word of mouth / talk of the town", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "hearsay-ugy-hirlik",
                "title": "Hearsay and Unconfirmed Reports: úgy hírlik, állítólag, a szóbeszéd szerint",
                "text1_title": "Signaling Rumor or Unverified Information",
                "text1": "When a journalist or speaker wishes to report a circulating rumor without endorsing its truth, Hungarian uses three classic hearsay markers:\n1. Úgy hírlik, (hogy)... ('Word has it that...', 'It is rumored/reported that...') — an impersonal verb derived from hír ('news').\n2. Állítólag ('allegedly / supposedly') — an adverb derived from állít ('claims').\n3. A szóbeszéd szerint / A híresztelések szerint ('according to rumor / town talk').",
                "text2_title": "Combining Hearsay with Factual Correction",
                "text2": "In B2 media commentary, these markers are frequently paired with an adversative clause (holott, valójában, ezzel szemben) to contrast rumor with verified fact: 'Úgy hírlik, hogy a miniszter lemondott, valójában azonban csak vidéki látogatásra utazott.'",
                "table_title": "Hearsay Markers in Media & Historical Reporting",
                "table_rows": [
                    ["Úgy hírlik, hogy a bankház fizetésképtelenné vált.", "Word has it / It is reported that the banking house became insolvent."],
                    ["A fülhallgató állítólag az Operaház előadását is közvetíti.", "The earpiece allegedly broadcasts the Opera House performance as well."],
                    ["A városi szóbeszéd szerint bűvésztrükk volt a készülék.", "According to city rumor, the device was a magic trick."]
                ],
                "examples": [
                    {"spanish": "Úgy hírlik, hogy egyes kávéházi törzsvendégek kezdetben bűvészmutatványnak tartották a két fülhallgatót.", "english": "Word has it that some café regulars initially considered the two earpieces a magic trick."},
                    {"spanish": "Ha állítólag lemondott egy miniszter, a Telefonhírmondó azonnal ellenőrizte a távirati irodánál.", "english": "If a minister had allegedly resigned, the Telefonhírmondó immediately checked with the telegraph agency."},
                    {"spanish": "A szóbeszéd szerint a készülék drága volt, valójában azonban egyetlen napi újság áráért elő lehetett fizetni rá.", "english": "According to rumor the device was expensive, whereas in reality one could subscribe for the price of a single daily newspaper."}
                ],
                "tip": "Úgy hírlik is a fixed impersonal 3rd-person singular present form (or past: úgy hírlett). Never conjugate it for 1st or 2nd person!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "pairs": [
                        ["műsorszórás", "broadcasting"],
                        ["telefonközpont", "telephone exchange"],
                        ["bemondó", "announcer / newsreader"],
                        ["fülhallgató", "earpiece / headphones"],
                        ["árfolyam", "stock price / exchange rate"],
                        ["szóbeszéd", "rumor / word of mouth"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "question": "Miért tekintjük Puskás Tivadar 1893-as budapesti Telefonhírmondóját világtörténelmi újdonságnak?",
                    "options": [
                        "Mert harminc évvel a rádió megjelenése előtt telefonvezetéken keresztül valósította meg a napi rendszeres hírközlést és élő kulturális műsorszórást.",
                        "Mert ez volt a világ első színes televíziócsatornája.",
                        "Mert postagalambokkal kézbesítette a tőzsdei árfolyamokat."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "sentence": "A budapesti előfizetők esténként a falra akasztott két _____ keresztül hallgathatták a Magyar Királyi Operaház élő közvetítését.",
                    "answer": "fülhallgatón",
                    "english": "In the evenings, Budapest subscribers could listen to the live broadcast of the Royal Hungarian Opera House through the two earpieces hung on the wall."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-evidential-framing"],
                    "question": "Which expression means 'Word has it that / It is rumored that...' in Hungarian journalistic prose?",
                    "options": [
                        "Úgy hírlik, hogy...",
                        "Úgy parancsolják, hogy...",
                        "Azért hírlik, mert...",
                        "Mindenki hírlik, hogy..."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "sentence": "A tőzsdén elterjedt a hír, hogy _____ összeomlott egy külföldi bankház, de a bemondó hamarosan cáfolta a pletykát.",
                    "answer": "állítólag",
                    "english": "News spread on the stock exchange that a foreign bank had allegedly collapsed, but the announcer soon refuted the rumor."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "tiles": ["Úgy", "hírlik,", "hogy", "az", "új", "készülék", "operát", "is", "közvetít."],
                    "solution": ["Úgy", "hírlik,", "hogy", "az", "új", "készülék", "operát", "is", "közvetít."],
                    "english": "Word has it that the new device broadcasts opera as well."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-evidential-framing"],
                    "prompt": [
                        {"speaker": "Kávéházi vendég", "text": "Igaz az a hír, hogy ma délután lemondott a pénzügyminiszter Bécsben?"},
                        {"speaker": "Főszerkesztő", "text": "_____"}
                    ],
                    "options": [
                        "A városi szóbeszéd szerint valóban lemondott, ám a Telefonhírmondó legfrissebb távirati jelentése szerint csupán rövid szabadságra utazott.",
                        "Nem tudhatjuk, mert Budapesten nincsenek sem újságok, sem telefonvezetékek.",
                        "Igen, mert a rádió már 1848-ban bemondta."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen műsorokat sugárzott napközben a Telefonhírmondó az előfizetőknek?",
                    "options": [
                        "Tőzsdei árfolyamokat, országgyűlési híreket, pontos időjelzést, színházi kritikákat, nyelvleckéket és esti operaközvetítéseket.",
                        "Kizárólag vasúti menetrendeket éjféltől hajnalig.",
                        "Csak némafilmeket feliratokkal."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "Radio and Television in Historical Turning Points",
            "grammar_label": "Inferential evidentials (a jelek szerint; minden jel arra mutat, hogy...; úgy tűnik, hogy...)",
            "goals": [
                "I can explain the historical role of Hungarian Radio (1925, 1956) and Hungarian Television (1957, 1989).",
                "I can express evidence-based inference using a jelek szerint and minden jel arra mutat, hogy...",
                "I can discuss broadcast history and collective memory in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "radiotelevizio",
                "title": "A Bródy Sándor utcai stúdiótól a televíziós történelmi pillanatokig",
                "summary": "From the launch of Magyar Rádió in December 1925 and the dramatic siege of October 23, 1956, to family television evenings in the Kádár era and the live broadcast of June 16, 1989, electronic media stood at the center of Hungarian history.",
                "location": "Budapest, Bródy Sándor utca és Szabadság tér (1925–1989)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1925. december 1-jén a Telefonhírmondó tapasztalataira építve megkezdte rendszeres adását a Magyar Rádió, amely néhány évvel később a Bródy Sándor utcai palotába költözött. A harmincas és negyvenes években a rádió vált az ország legfőbb hírközlő és kulturális intézményévé: itt csendültek fel Bartók Béla és Kodály Zoltán népdalfeldolgozásai, de a háborús években ugyanezen a hullámhosszon olvasták be a frontjelentéseket és a légiriadókat is."
                    },
                    {
                        "type": "narration",
                        "text": "1956. október 23-án este a Bródy Sándor utcai épület a magyar történelem sorsfordító helyszínévé vált, amikor az egyetemisták a tizenhat pont beolvasását követelték. A következő napokban a családok feszülten tapadtak a rádiókészülékekre: a jelek szerint a Szabad Kossuth Rádió közleményeiből és november 4-én hajnalban Nagy Imre drámai szózatából értesült a világ arról, hogy a szovjet csapatok támadást indítottak Budapest ellen."
                    },
                    {
                        "type": "narration",
                        "text": "1957 májusában elindult a Magyar Televízió rendszeres adása a Szabadság téri székházból, és a hatvanas évek végétől a képernyő alapjaiban alakította át a családok mindennapjait. Hétfőnként adásszünet volt, ám a Táncdalfesztivál döntői, a Delta tudományos híradója vagy A Hét című vasárnap esti politikai magazin idején szinte elnéptelenedtek az utcák."
                    },
                    {
                        "type": "narration",
                        "text": "A nyolcvanas évek második felében a televíziós és rádiós műhelyekben egyre bátrabb oknyomozó riportok és közéleti viták születtek. Minden jel arra mutatott, hogy az állampárti tájékoztatási monopólium megrepedt: a Panoráma külpolitikai adásai és a 168 Óra rádióműsora olyan tabutémákat érintett, amelyekről korábban csak suttogni lehetett."
                    },
                    {
                        "type": "narration",
                        "text": "A szimbolikus fordulópont 1989. június 16-án érkezett el, amikor a Magyar Televízió egyenes adásban, cenzúra nélkül közvetítette Nagy Imre és mártírtársai hősök terén tartott újratemetését. Milliók látták egyszerre a képernyőn, amint a hivatalos hazugságok korszaka lezárul."
                    }
                ]
            },
            "words": [
                {"lemma": "hullámhossz", "translation": "wavelength / frequency", "pos": "noun"},
                {"lemma": "adásszünet", "translation": "broadcast sign-off / transmission break (e.g. Mondays)", "pos": "noun"},
                {"lemma": "egyenes adás", "translation": "live broadcast", "pos": "noun"},
                {"lemma": "monopólium", "translation": "monopoly", "pos": "noun"},
                {"lemma": "oknyomozó", "translation": "investigative (journalism)", "pos": "adjective"},
                {"lemma": "tabutéma", "translation": "taboo topic", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "inferential-evidentials",
                "title": "Inferential Evidential Framing: a jelek szerint and minden jel arra mutat, hogy...",
                "text1_title": "Drawing Conclusions from Observable Signs",
                "text1": "Unlike hearsay markers (which rely on what others say), inferential evidentials show that the speaker or analyst is deducing a conclusion from observable symptoms, trends, or historical clues:\n• a jelek szerint ('by all indications / as the signs suggest')\n• minden jel arra mutat, hogy... ('every sign points to the fact that...')\n• úgy tűnik / úgy látszik, hogy... ('it appears / seems that...')",
                "text2_title": "Case Government in minden jel arra mutat, hogy...",
                "text2": "Notice the cataphoric pronoun arra (sublative -ra on az) before the verb mutat ('points to'): 'Minden jel arra mutatott, hogy a tájékoztatási monopólium megrepedt.' This structure allows you to embed a complex clause smoothly as the target of the inference.",
                "table_title": "Inferential Evidentials in Analytical Commentary",
                "table_rows": [
                    ["A jelek szerint a lakosság már nem hitt a hivatalos közleményeknek.", "By all indications, the population no longer believed the official communiqués."],
                    ["Minden jel arra mutatott, hogy a cenzúra rendszere felbomlóban van.", "Every sign pointed to the fact that the system of censorship was disintegrating."],
                    ["Úgy tűnt, hogy az egyenes adás örökre megváltoztatja a közbeszédet.", "It seemed that the live broadcast would change public discourse forever."]
                ],
                "examples": [
                    {"spanish": "A jelek szerint a Szabad Kossuth Rádió közleményeiből értesült a világ a budapesti eseményekről.", "english": "By all indications, the world learned of the events in Budapest from the communiqués of Free Kossuth Radio."},
                    {"spanish": "Minden jel arra mutatott, hogy az állampárti tájékoztatási monopólium végleg megrepedt.", "english": "Every sign pointed to the fact that the state-party information monopoly had cracked for good."},
                    {"spanish": "Az utcák elnéptelenedéséből úgy tűnt, hogy az egész ország a Táncdalfesztivál döntőjét nézi.", "english": "From the emptying of the streets, it appeared that the entire country was watching the final of the Táncdalfesztivál."}
                ],
                "tip": "Use a jelek szerint when you want a concise adverbial phrase inside a single clause; use minden jel arra mutat, hogy... when you want to build dramatic analytical weight before a full subordinate clause."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "pairs": [
                        ["hullámhossz", "wavelength / radio frequency"],
                        ["adásszünet", "transmission break (no broadcasting)"],
                        ["egyenes adás", "live broadcast"],
                        ["monopólium", "monopoly"],
                        ["oknyomozó", "investigative"],
                        ["tabutéma", "taboo subject"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "question": "Miért volt történelmi jelentőségű a Magyar Televízió 1989. június 16-i közvetítése?",
                    "options": [
                        "Mert cenzúra nélkül, egyenes adásban közvetítette Nagy Imre és mártírtársai újratemetését a Hősök teréről.",
                        "Mert ekkor vezették be a hétfői adásszünetet.",
                        "Mert ekkor szólalt meg először a Telefonhírmondó."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "sentence": "A nyolcvanas évek végén a rádiós és televíziós magazinműsorok egyre több korábbi _____ mertek nyíltan bemutatni.",
                    "answer": "tabutémát",
                    "english": "At the end of the eighties, radio and television magazine programs dared to openly present more and more former taboo topics."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-evidential-framing"],
                    "question": "Which sublative demonstrative pronoun completes the inferential expression: 'Minden jel _____ mutatott, hogy a tájékoztatási monopólium véget ér'?",
                    "options": ["arra", "abban", "attól", "azzal"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "sentence": "A _____ szerint az 1960-as évek végétől a televízió vált a magyar családok legfőbb esti szórakozási formájává.",
                    "answer": "jelek",
                    "english": "By all indications (according to the signs), from the late 1960s television became the main form of evening entertainment for Hungarian families."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "tiles": ["Minden", "jel", "arra", "mutat,", "hogy", "a", "cenzúra", "megbukott."],
                    "solution": ["Minden", "jel", "arra", "mutat,", "hogy", "a", "cenzúra", "megbukott."],
                    "english": "Every sign points to the fact that censorship has failed."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-evidential-framing"],
                    "prompt": [
                        {"speaker": "Médiakutató", "text": "Hogyan érzékelhették a nézők a nyolcvanas évek végén, hogy közeledik a rendszerváltás?"},
                        {"speaker": "Szerkesztő", "text": "_____"}
                    ],
                    "options": [
                        "Minden jel arra mutatott, hogy a régi tabuk ledőlnek: a rádióban és a televízióban oknyomozó riportok hangzottak el, majd 1989 júniusában egyenes adásban láthattuk Nagy Imre újratemetését.",
                        "Abból, hogy a televízióban betiltották a híradót és csak némafilmeket vetítettek.",
                        "Abból, hogy minden háztartásban leszerelték a rádiókészülékeket."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik utcában működött a Magyar Rádió híres stúdiópalotája, amely 1956. október 23-án a forradalom egyik központi helyszíne lett?",
                    "options": [
                        "A Bródy Sándor utcában.",
                        "Az Andrássy úton.",
                        "A Trefort utcában."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "The Privatization of Media After 1989",
            "grammar_label": "Epistemic hedging and cautious attribution (feltételezhetően, valószínűsíthetően, saját bevallása szerint)",
            "goals": [
                "I can analyze the transformation of the Hungarian press after 1989, including the 1990s 'media war' and the 1996 dual broadcasting law.",
                "I can hedge analytical claims using feltételezhetően, valószínűsíthetően, and saját bevallása szerint.",
                "I can discuss public-service vs. commercial broadcasting in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "mediapiac1989",
                "title": "Sajtószabadság, médiaháború és a kereskedelmi televíziózás hajnala",
                "summary": "Following the abolition of censorship in 1989, hundreds of new publications sprang up overnight, while political struggles over public radio and television led to the 1996 Media Act and the launch of nationwide commercial channels in 1997.",
                "location": "Budapest (1989–1998)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1989-ben az engedélyezési kényszer megszűnésével valóságos sajtórobbanás zajlott le Magyarországon: néhány hónap alatt több száz új napilap, hetilap és folyóirat jelent meg az újságosbódékban. Az egykori állampárti megyei lapokat külföldi — német, osztrák és svájci — médiavállalatok vásárolták fel, miközben az országos napilapok szerkesztőségei a politikai függetlenség és a piaci túlélés között keresték az egyensúlyt."
                    },
                    {
                        "type": "narration",
                        "text": "Miközben a nyomtatott sajtó gyorsan magánkézbe került, az egyetlen országos rádió és televízió még évekig állami tulajdonban maradt. A kilencvenes évek elején kirobbant úgynevezett „médiaháború” során a kormányzat és az ellenzék élesen vitázott arról, ki nevezheti ki a közszolgálati intézmények elnökeit; a vitában Hankiss Elemér és Gombár Csaba elnökök saját bevallásuk szerint a BBC független közszolgálati modelljét próbálták meghonosítani."
                    },
                    {
                        "type": "narration",
                        "text": "A politikai patthelyzetet végül az 1996-os médiatörvény oldotta fel, amely kétharmados parlamenti többséggel megszüntette az állami műsorszórási monopóliumot, és megteremtette a duális médiarendszert. A törvény értelmében a közszolgálati csatornák mellett országos földfelszíni frekvenciát kaptak a magántulajdonú kereskedelmi televíziók is."
                    },
                    {
                        "type": "narration",
                        "text": "1997 őszén néhány nap különbséggel indult el a TV2 és az RTL Klub, amelyek gyökeresen átalakították a magyar nézői szokásokat. A hirdetési bevételekből élő csatornák feltételezhetően azért tudtak hónapok alatt milliós közönséget elhódítani a közszolgálati televíziótól, mert a hivatalos protokollt felváltották a dinamikus híradók, a napi sorozatok és a szórakoztató show-műsorok."
                    },
                    {
                        "type": "narration",
                        "text": "A kereskedelmi fordulat ugyanakkor új vitákat is nyitott: a kritikusok arra figyelmeztettek, hogy a nézettségi verseny és a bulvárosodás valószínűsíthetően háttérbe szorítja a mélyebb kulturális és oktatási műsorokat."
                    }
                ]
            },
            "words": [
                {"lemma": "közszolgálati", "translation": "public-service (broadcasting)", "pos": "adjective"},
                {"lemma": "kereskedelmi", "translation": "commercial (broadcasting / channel)", "pos": "adjective"},
                {"lemma": "nézettség", "translation": "viewership / ratings", "pos": "noun"},
                {"lemma": "bulvárosodás", "translation": "tabloidization / sensationalism", "pos": "noun"},
                {"lemma": "frekvencia", "translation": "broadcasting frequency", "pos": "noun"},
                {"lemma": "hirdetési bevétel", "translation": "advertising revenue", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "epistemic-hedging-adverbs",
                "title": "Epistemic Hedging: feltételezhetően, valószínűsíthetően, saját bevallása szerint",
                "text1_title": "Adverbial Participles of Epistemic Possibility (-hatóan/-hetően)",
                "text1": "In B2/C1 analytical prose, Hungarian derives cautious epistemic adverbs by adding the potential participle suffix -ható/-hető plus the adverbial ending -an/-en to cognitive verbs:\n• feltételez ('assumes/hypothesizes') → feltételezhetően ('presumably / as may be assumed')\n• valószínűsít ('renders probable') → valószínűsíthetően ('in all likelihood / plausibly')\n• vélelmez ('presumes') → vélelmezhetően ('presumably')\nThese forms allow a writer to propose a causal explanation without overstating certainty.",
                "text2_title": "Self-Report Attribution with saját bevallása szerint",
                "text2": "When quoting or summarizing a public figure's own stated motives with critical objectivity, Hungarian uses saját bevallása szerint (singular: 'by his/her own admission / according to his/her own account') or saját bevallásuk szerint (plural). It signals neither blind endorsement nor hostility—simply that the claim represents the actor's own self-characterization.",
                "table_title": "Epistemic Hedging & Self-Report Formulas",
                "table_rows": [
                    ["A csatornák feltételezhetően a dinamikus műsorok miatt nyertek teret.", "The channels presumably gained ground because of their dynamic programming."],
                    ["A nézettségi verseny valószínűsíthetően átalakította a híradókat is.", "The ratings competition in all likelihood transformed news broadcasts as well."],
                    ["Az elnökök saját bevallásuk szerint a BBC modelljét követték.", "By their own account, the presidents followed the BBC model."]
                ],
                "examples": [
                    {"spanish": "Hankiss Elemér és Gombár Csaba saját bevallásuk szerint a BBC független közszolgálati modelljét próbálták meghonosítani.", "english": "By their own account, Elemér Hankiss and Csaba Gombár tried to introduce the independent public-service model of the BBC."},
                    {"spanish": "Az új csatornák feltételezhetően azért hódítottak el milliós közönséget, mert szakítottak a merev protokollal.", "english": "The new channels presumably won over an audience of millions because they broke with rigid protocol."},
                    {"spanish": "A bulvárosodás valószínűsíthetően hozzájárult a komoly kulturális műsorok visszaszorulásához.", "english": "Tabloidization plausibly contributed to the retreat of serious cultural programs."}
                ],
                "tip": "Notice the vowel harmony in feltételezhetően (front vowels: -hetően) versus valószínűsíthetően and várhatóan (back vowels: -hatóan)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "pairs": [
                        ["közszolgálati", "public-service"],
                        ["kereskedelmi", "commercial"],
                        ["nézettség", "viewership / ratings"],
                        ["bulvárosodás", "tabloidization"],
                        ["frekvencia", "broadcast frequency"],
                        ["hirdetési bevétel", "advertising revenue"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "question": "Mit hozott létre az 1996-os médiatörvény Magyarországon?",
                    "options": [
                        "A duális médiarendszert, amelyben a közszolgálati csatornák mellett országos kereskedelmi televíziók és rádiók is működhetnek.",
                        "Az állami televíziós monopólium örökös fenntartását.",
                        "A nyomtatott napilapok betiltását."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "sentence": "Az 1997-ben indult kereskedelmi televíziók működését nem állami támogatásból, hanem piaci _____ finanszírozták.",
                    "answer": "hirdetési bevételekből",
                    "english": "The operation of the commercial televisions launched in 1997 was financed not from state subsidies, but from market advertising revenues."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-evidential-framing"],
                    "question": "Which phrase objectively attributes a stated intention or motive to the speakers themselves ('by their own account / admission')?",
                    "options": [
                        "saját bevallásuk szerint",
                        "saját bevallásuk ellenére",
                        "saját bevallásuk helyett",
                        "saját bevallásuk nélkül"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "sentence": "A külföldi befektetők _____ azért vásárolták fel a megyei napilapokat, mert biztos helyi előfizetői táborral rendelkeztek. (feltételez - potential adverb in -hetően)",
                    "answer": "feltételezhetően",
                    "english": "Foreign investors presumably bought up the county dailies because they had a reliable local subscriber base."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "tiles": ["Az", "elnök", "saját", "bevallása", "szerint", "a", "függetlenséget", "védte."],
                    "solution": ["Az", "elnök", "saját", "bevallása", "szerint", "a", "függetlenséget", "védte."],
                    "english": "By his own account, the president defended independence."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-evidential-framing"],
                    "prompt": [
                        {"speaker": "Újságíró", "text": "Miért változott meg olyan látványosan a magyar televíziós kultúra 1997 őszén?"},
                        {"speaker": "Médiatörténész", "text": "_____"}
                    ],
                    "options": [
                        "Mert a duális médiarendszer elindulásával a kereskedelmi csatornák a nézettségi versenyre építettek, ami valószínűsíthetően felgyorsította a szórakoztató műfajok térnyerését.",
                        "Mert 1997-ben minden magyar családtól begyűjtötték a televíziókészülékeket.",
                        "Mert a parlament betiltotta a hirdetések sugárzását."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik két országos kereskedelmi televíziócsatorna indult el 1997 őszén Magyarországon?",
                    "options": [
                        "A TV2 és az RTL Klub.",
                        "A Telefonhírmondó és a Szép Szó.",
                        "A BBC és a CNN magyar nyelvű földi adása."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Navigating Polarization in the Digital Age",
            "grammar_label": "Synthesizing evidentiality, source verification, and epistemic stance in digital media analysis",
            "goals": [
                "I can trace the rise of Hungarian online journalism since the late 1990s and analyze the challenges of algorithmic echo chambers.",
                "I can combine source attribution, hearsay markers, inferential evidentials, and hedging adverbs in B2 media criticism.",
                "I can discuss fact-checking, crowdfunding, and digital media literacy in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "digitalisnyilvanossag",
                "title": "Hírportálok, algoritmusok és a kritikus médiatudatosság",
                "summary": "From the pioneering Hungarian internet portals of the late 1990s to today's social media algorithms, podcasts, and reader-funded investigative outlets, navigating the digital public sphere requires active source criticism.",
                "location": "Budapest, kortárs szerkesztőségek és digitális tér (1998–napjainkig)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1990-es évek legvégén Magyarország Európában is az elsők között hozott létre önálló, nagy hatású internetes hírportálokat: az Origo és az Index születésekor a nyomtatott lapok szerkesztői még úgy vélték, az online újságírás csupán múló divat lesz. Néhány évtizeddel később azonban minden jel arra mutat, hogy az internet és az okostelefon vált a hírfogyasztás elsődleges csatornájává."
                    },
                    {
                        "type": "narration",
                        "text": "A közösségi média térhódításával a hagyományos szerkesztőségi kapuőr szerepét fokozatosan átvették az algoritmusok, amelyek a kattintásszámot és az érzelmi felháborodást jutalmazzák. Médiafogyasztási felmérések szerint a felhasználók jelentős része ma már zárt véleménybuborékokban tájékozódik, ahol kizárólag a saját előzetes meggyőződését megerősítő tartalmakkal találkozik."
                    },
                    {
                        "type": "narration",
                        "text": "Ebben a környezetben különösen gyorsan terjednek az ellenőrizetlen álhírek és a mesterséges intelligenciával manipulált felvételek. Ha egy névtelen oldalon úgy hírlik, hogy valamilyen rendkívüli esemény történt, a tudatos olvasónak azonnal fel kell tennie a kérdést: megjelölték-e a hír eredeti forrását, vagy csupán kattintásvadász híresztelésről van szó?"
                    },
                    {
                        "type": "narration",
                        "text": "Az utóbbi években a magyar médiapiacon új finanszírozási és tartalmi modellek is megjelentek: a hirdetőknek és politikai szereplőknek való kiszolgáltatottság helyett egyre több oknyomozó műhely, elemző podcast és független portál épít közvetlen olvasói mikroadományokra és előfizetésekre."
                    },
                    {
                        "type": "narration",
                        "text": "Kossuth Lajos Pesti Hírlapjától és Puskás Tivadar Telefonhírmondójától a mai digitális nyilvánosságig egyetlen alapelv maradt változatlan: a demokratikus közbeszéd minősége azon múlik, hogy az állampolgárok meg tudják-e különböztetni a szóbeszédet a bizonyított tényektől."
                    }
                ]
            },
            "words": [
                {"lemma": "véleménybuborék", "translation": "echo chamber / filter bubble", "pos": "noun"},
                {"lemma": "kattintásvadász", "translation": "clickbait", "pos": "adjective"},
                {"lemma": "álhír", "translation": "fake news / fabricated report", "pos": "noun"},
                {"lemma": "médiatudatosság", "translation": "media literacy", "pos": "noun"},
                {"lemma": "kapuőr", "translation": "gatekeeper (editorial filter)", "pos": "noun"},
                {"lemma": "mikroadomány", "translation": "micro-donation / crowdfunding contribution", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "evidential-spectrum-synthesis",
                "title": "The Complete B2 Evidential Spectrum: From Rumor to Verified Fact",
                "text1_title": "Calibrating Epistemic Certainty in Hungarian",
                "text1": "Across this unit, you have acquired a four-tier toolkit for signaling source reliability in Hungarian:\n1. Unverified Rumor / Hearsay: úgy hírlik, hogy...; állítólag; a szóbeszéd szerint\n2. Plausible Hypothesis / Hedging: feltételezhetően; valószínűsíthetően\n3. Observable Inference / Trend: a jelek szerint; minden jel arra mutat, hogy...\n4. Explicit Source Attribution: [forrás] szerint (médiafogyasztási felmérések szerint, saját bevallása szerint)",
                "text2_title": "Critical Fact-Checking Syntax",
                "text2": "In B2 media literacy essays, combine a hearsay or self-report frame in the first clause with an empirical source frame in the second: 'Állítólag a felvétel tegnap készült, a független tényellenőrzők vizsgálata szerint azonban egy három évvel ezelőtti eseményt ábrázol.'",
                "table_title": "Four-Tier Evidential Calibration",
                "table_rows": [
                    ["Úgy hírlik / Állítólag (Hearsay)", "Állítólag titkos megállapodás született a felek között."],
                    ["Feltételezhetően / Valószínűsíthetően (Hedging)", "Az algoritmus valószínűsíthetően a felháborodást jutalmazza."],
                    ["A jelek szerint / Minden jel arra mutat (Inference)", "Minden jel arra mutat, hogy a podcastok szerepe nő."],
                    ["Felmérések szerint (Explicit attribution)", "Kutatások szerint a fiatalok okostelefonon olvasnak híreket."]
                ],
                "examples": [
                    {"spanish": "Médiafogyasztási felmérések szerint a felhasználók jelentős része zárt véleménybuborékokban tájékozódik.", "english": "According to media consumption surveys, a significant portion of users get their information in closed echo chambers."},
                    {"spanish": "Minden jel arra mutat, hogy az okostelefon vált a hírfogyasztás elsődleges csatornájává.", "english": "Every sign points to the fact that the smartphone has become the primary channel of news consumption."},
                    {"spanish": "Ha egy névtelen oldalon úgy hírlik, hogy botrány történt, érdemes több független forrásból ellenőrizni az állítást.", "english": "If word has it on an anonymous page that a scandal occurred, it is worth verifying the claim from several independent sources."}
                ],
                "tip": "Using this four-tier evidential spectrum in B2 writing exams demonstrates sophisticated critical thinking and native-like control of Hungarian journalistic register."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "pairs": [
                        ["véleménybuborék", "echo chamber / filter bubble"],
                        ["kattintásvadász", "clickbait"],
                        ["álhír", "fake news"],
                        ["médiatudatosság", "media literacy"],
                        ["kapuőr", "editorial gatekeeper"],
                        ["mikroadomány", "crowdfunding micro-donation"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "question": "Mit értünk a digitális nyilvánosságban a „véleménybuborék” fogalma alatt?",
                    "options": [
                        "Azt a jelenséget, amikor az algoritmusok miatt a felhasználó szinte kizárólag a saját előzetes nézeteit megerősítő hírekkel találkozik.",
                        "A Telefonhírmondó rézből készült fülhallgatóját.",
                        "A nyomtatott napilapok hétvégi mellékletét."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-mediatortenet-vocab"],
                    "sentence": "Az érzelmi felháborodásra építő, félrevezető címeket a modern sajtókritika _____ címeknek nevezi.",
                    "answer": "kattintásvadász",
                    "english": "Misleading headlines built on emotional outrage are called clickbait headlines by modern press criticism."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-evidential-framing"],
                    "question": "Which sentence properly contrasts an unverified rumor with documented fact-checking?",
                    "options": [
                        "Állítólag a fotó tegnap készült, a tényellenőrzők vizsgálata szerint azonban egy régi felvételről van szó.",
                        "Szerint a fotó tegnap készült, állítólag azonban tényellenőrzők.",
                        "Minden jel arra mutat, hogy állítólag szerint.",
                        "A fotó saját bevallása szerint tegnap készült."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "sentence": "Médiafogyasztási _____ szerint egyre több magyar olvasó támogatja közvetlen mikroadományokkal a független szerkesztőségeket.",
                    "answer": "felmérések",
                    "english": "According to media consumption surveys, more and more Hungarian readers support independent editorial offices with direct micro-donations."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-evidential-framing"],
                    "tiles": ["Kutatások", "szerint", "az", "algoritmusok", "erősítik", "a", "véleménybuborékokat."],
                    "solution": ["Kutatások", "szerint", "az", "algoritmusok", "erősítik", "a", "véleménybuborékokat."],
                    "english": "According to research, algorithms reinforce echo chambers."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-evidential-framing"],
                    "prompt": [
                        {"speaker": "Olvasó", "text": "Hogyan védekezhetünk a közösségi médiában terjedő manipulált hírek ellen?"},
                        {"speaker": "Médiakutató", "text": "_____"}
                    ],
                    "options": [
                        "Úgy, hogy ha egy oldalon úgy hírlik valami, ami túl szenzációsnak tűnik, megnézzük, milyen bizonyított források szerint írták a cikket.",
                        "Úgy, hogy minden névtelen bejegyzést azonnal továbbosztunk ellenőrzés nélkül.",
                        "Úgy, hogy csak a kattintásvadász szalagcímeket olvassuk el."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen új finanszírozási formára támaszkodik ma számos független magyar oknyomozó műhely és elemző podcast?",
                    "options": [
                        "Közvetlen olvasói mikroadományokra és előfizetésekre.",
                        "Kizárólag tizenkilencedik századi vármegyei adókra.",
                        "Postai bélyegárusításra."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can trace the key milestones of Hungarian media history from Kossuth's Pesti Hírlap (1841) and Puskás's Telefonhírmondó (1893) to radio, television, and digital portals.",
            "I can calibrate source reliability using szerint attributions, hearsay markers (úgy hírlik, állítólag), inferential evidentials (a jelek szerint, minden jel arra mutat), and epistemic adverbs (feltételezhetően, valószínűsíthetően).",
            "I can critically evaluate media polarization, tabloidization, and echo chambers in B2 Hungarian.",
            "I can actively use 30 B2 journalism and media-studies vocabulary items."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-mediatortenet-vocab"],
                "pairs": [
                    ["vezércikk", "lead editorial"],
                    ["műsorszórás", "broadcasting"],
                    ["egyenes adás", "live broadcast"],
                    ["közszolgálati", "public-service"],
                    ["véleménybuborék", "echo chamber"],
                    ["médiatudatosság", "media literacy"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-evidential-framing"],
                "question": "Which expression signals an unconfirmed rumor ('word has it that...') rather than a verified statistical report?",
                "options": [
                    "Úgy hírlik, hogy...",
                    "A nyomdai kimutatások szerint...",
                    "A népszámlálási adatok szerint...",
                    "A hivatalos jegyzőkönyv szerint..."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-mediatortenet-vocab"],
                "question": "Ki találta fel és indította el 1893 februárjában Budapesten a világ első telefonos hírmondó szolgálatát, a Telefonhírmondót?",
                "options": [
                    "Puskás Tivadar.",
                    "Landerer Gusztáv.",
                    "Kempelen Farkas.",
                    "Eötvös Loránd."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-mediatortenet-vocab"],
                "sentence": "Kossuth Lajos 1841-ben a Pesti Hírlap első oldalán honosította meg a politikai _____ műfaját a magyar újságírásban.",
                "answer": "vezércikk",
                "english": "In 1841, on the front page of Pesti Hírlap, Lajos Kossuth introduced the genre of the political lead editorial in Hungarian journalism."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-evidential-framing"],
                "sentence": "Minden jel _____ mutatott, hogy a nyolcvanas évek végén az állampárti tájékoztatási monopólium felbomlik.",
                "answer": "arra",
                "english": "Every sign pointed to the fact that at the end of the eighties the state-party information monopoly was disintegrating."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-evidential-framing"],
                "sentence": "A kereskedelmi csatornák _____ azért nyertek gyorsan nagy közönséget, mert szakítottak a merev hivatalos stílussal. (feltételez - adverb in -hetően)",
                "answer": "feltételezhetően",
                "english": "Commercial channels presumably won a large audience quickly because they broke with the rigid official style."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-evidential-framing"],
                "prompt": [
                    {"speaker": "Történelemtanár", "text": "Hogyan fogadták a budapestiek 1893-ban Puskás Tivadar beszélő újságját?"},
                    {"speaker": "Múzeumi kurátor", "text": "_____"}
                ],
                "options": [
                    "Korabeli beszámolók szerint sokan először bűvésztrükknek hitték a fülhallgatókat, ám a pontos tőzsdei hírek és az esti operaközvetítések gyorsan meggyőzték az előfizetőket.",
                    "Senki sem fizetett elő rá, ezért egy hét után megszüntették.",
                    "A városi szóbeszéd szerint csak latin nyelvű verseket olvastak fel benne."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-evidential-framing"],
                "question": "Which sentence accurately uses 'saját bevallása szerint' to report a public figure's stated motivation?",
                "options": [
                    "A főszerkesztő saját bevallása szerint a BBC független közszolgálati mércéjét tartotta szem előtt.",
                    "A fülhallgató saját bevallása szerint rézből készült.",
                    "Az algoritmus saját bevallása szerint tegnap esett az eső.",
                    "A vezércikk saját bevallása szerint ötezer példányban kelt el."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-evidential-framing"],
                "prompt": [
                    {"speaker": "Médiapedagógus", "text": "Mire kell figyelnie egy kritikus olvasónak, amikor szenzációs hírrel találkozik az interneten?"},
                    {"speaker": "Egyetemista", "text": "_____"}
                ],
                "options": [
                    "Arra, hogy megkülönböztesse az állítólagos szóbeszédet a megnevezett, független források szerint igazolt tényektől.",
                    "Arra, hogy minél gyorsabban továbbküldje a kattintásvadász szalagcímeket.",
                    "Arra, hogy soha ne olvasson el egyetlen vezércikket sem."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-evidential-framing"],
                "tiles": ["A", "jelek", "szerint", "az", "online", "portálok", "átvették", "a", "vezető", "szerepet."],
                "solution": ["A", "jelek", "szerint", "az", "online", "portálok", "átvették", "a", "vezető", "szerepet."],
                "english": "By all indications, online portals have taken over the leading role."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-evidential-framing"],
                "tiles": ["Sajtóhírek", "szerint", "az", "előfizetők", "száma", "rekordot", "döntött."],
                "solution": ["Sajtóhírek", "szerint", "az", "előfizetők", "száma", "rekordot", "döntött."],
                "english": "According to press reports, the number of subscribers broke a record."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-evidential-framing"],
                "template": [
                    {
                        "prompt": "Write a sentence reporting how Pesti Hírlap's subscriber numbers grew in 1841 (use 'nyomdai kimutatások szerint').",
                        "answer": "A nyomdai kimutatások szerint a Pesti Hírlap előfizetőinek száma néhány hónap alatt több mint ötezerre emelkedett."
                    },
                    {
                        "prompt": "Write a sentence explaining why media literacy is essential in the age of algorithmic echo chambers (use 'minden jel arra mutat, hogy...').",
                        "answer": "Minden jel arra mutat, hogy a véleménybuborékok és az álhírek korában a kritikus médiatudatosság elengedhetetlen a demokratikus tájékozódáshoz."
                    }
                ]
            }
        ]
    }
}


UNIT_18_POLITIKAIRETORIKA = {
    "unit_num": 18,
    "slug": "politikairetorika",
    "title": "Public Memory, Monuments & Political Rhetoric",
    "grammar_skill": "b2-cataphoric-clauses",
    "vocab_skill": "b2-politikairetorika-vocab",
    "theme": "Hungarian monuments, memory politics and parliamentary oratory",
    "location": "Budapest (Hősök tere, Kossuth tér, Szoborpark)",
    "intro_body": [
        "In Central Europe, public spaces are rarely neutral: every regime change is etched into bronze, carved into marble, or painted over street signs. From the monumental colonnade of the 1896 Millennium Monument at Heroes' Square to the toppled statues gathered in Memento Park, Budapest's urban topography reflects dramatic shifts in how Hungarians have remembered—and contested—their national past.",
        "In this unit, you will examine the symbolic architecture of Heroes' Square, investigate the dizzying history of renaming Budapest's grand boulevards, explore the conceptual philosophy behind Ákos Eleőd's Szoborpark, analyze the classic rhetorical traditions of Hungarian parliamentary orators on Kossuth tér, and dissect the contemporary politics of memory (emlékezetpolitika). Grammatically, you will master cataphoric demonstrative noun anchors that introduce complement clauses (arra a döntésre jutott, hogy...; abban a szellemben, hogy...; azzal a céllal, hogy...; arról a kérdésről, hogy...)."
    ],
    "combined_story_title": "Ledöntött és felállított szobrok: A magyar emlékezetpolitika",
    "combined_story_summary": "How Hungarian political regimes inscribed their vision of history onto city squares and street names: from the 1896 Millennium monument at Heroes' Square to Memento Park and parliamentary rhetoric.",
    "lessons": [
        {
            "num": 1,
            "title": "Millennium Grandeur: The Making of Hősök tere",
            "grammar_label": "Sublative cataphoric noun anchors (arra a döntésre/következtetésre jutott, hogy...)",
            "goals": [
                "I can explain the historical design and political symbolism of the Millennium Monument at Hősök tere.",
                "I can anchor complement clauses using sublative cataphoric demonstrative phrases like arra a döntésre jutott, hogy...",
                "I can use B2 architectural and monument-history vocabulary in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "hosoktere",
                "title": "Gábriel arkangyal és a királyok pantheonja (1896)",
                "summary": "Designed for the 1896 Millennial Exhibition by architect Albert Schickedanz and sculptor György Zala, the Millennium Monument at Heroes' Square turned Hungary's first thousand years into a grand national stage—whose statues were repeatedly swapped by later regimes.",
                "location": "Budapest, Hősök tere (1896–1919)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1896-ban a magyar nemzet a honfoglalás ezeréves évfordulóját ünnepelte, és a dualista korszak vezetői arra a döntésre jutottak, hogy a Városliget bejáratánál olyan reprezentatív emlékművet emelnek, amely méltó a birodalom társbérlőjévé vált ország önbizalmához. Schickedanz Albert építész és Zala György szobrász tervei alapján megszületett a Hősök tere monumentális együttese."
                    },
                    {
                        "type": "narration",
                        "text": "A tér közepén magasodó harminchat méteres korinthoszi oszlop tetejére Gábriel arkangyal bronzalakja került, aki a Szent Koronát és a kettős keresztet tartja a magasba, emlékeztetve arra a legendára, miszerint Isten küldötte szólította fel II. Szilveszter pápát az államalapító István király megkoronázására. Az oszlop talapzatánál Árpád fejedelem és a hét honfoglaló vezér lovasszobra vigyázza a nemzet szimbolikus bölcsőjét."
                    },
                    {
                        "type": "narration",
                        "text": "A két félköríves oszlopcsarnok a magyar történelem nagy alakjainak pantheonjaként épült fel, ám a szobrok sorsa hűen tükrözte a huszadik század politikai viharait. Az eredeti oszlopcsarnokban az Árpád-házi, a vegyesházi és az erdélyi uralkodók mellett még öt Habsburg király — köztük I. Ferenc József — szobra is helyet kapott, abból a megfontolásból kiindulva, hogy az Osztrák–Magyar Monarchia közös uralkodója egyben a magyar alkotmány garanciája."
                    },
                    {
                        "type": "narration",
                        "text": "1919-ben a Tanácsköztársaság idején a Habsburg-szobrokat ledöntötték és vörös drapériával takarták el az egész emlékművet; a Horthy-korszakban ugyan visszaállították őket, ám a második világháború után, 1945-ben a döntéshozók végleg arra az elhatározásra jutottak, hogy a Habsburg uralkodók helyére Bocskai István, Bethlen Gábor, Thököly Imre és II. Rákóczi Ferenc függetlenségi fejedelem, valamint Kossuth Lajos alakját állítják."
                    },
                    {
                        "type": "narration",
                        "text": "A Hősök tere így vált a magyar történelem kőbe és bronzba öntött palimpszesztjévé: minden egymást követő korszak a saját politikai narratíváját igyekezett belefaragni a nemzet központi emlékművébe."
                    }
                ]
            },
            "words": [
                {"lemma": "honfoglalás", "translation": "Conquest of the Carpathian Basin (896)", "pos": "noun"},
                {"lemma": "pantheon", "translation": "pantheon / hall of national heroes", "pos": "noun"},
                {"lemma": "oszlopcsarnok", "translation": "colonnade / portico", "pos": "noun"},
                {"lemma": "reprezentatív", "translation": "representative / ceremonial / stately", "pos": "adjective"},
                {"lemma": "palimpszeszt", "translation": "palimpsest (layered historical text or space)", "pos": "noun"},
                {"lemma": "államalapító", "translation": "state-founding (e.g. King Saint Stephen)", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "sublative-cataphoric-anchors",
                "title": "Sublative Cataphoric Anchors: arra a döntésre/következtetésre jutott, hogy...",
                "text1_title": "Forward-Pointing Demonstratives with Noun Phrases",
                "text1": "In Hungarian B2/C1 syntax, when a speaker or historical actor arrives at a decision, realization, or conclusion, formal style avoids leaving the verb bare. Instead, a sublative demonstrative (arra) modifies a categorized abstract noun, creating a forward-pointing anchor that prepares the reader for the hogy complement clause:\n• arra a döntésre / elhatározásra jutott, hogy... ('arrived at the decision to / that...')\n• arra a következtetésre jutott, hogy... ('came to the conclusion that...')\n• arra a meggyőződésre épült, hogy... ('was built on the conviction that...')\n• arra a kérdésre kereste a választ, hogy... ('sought the answer to the question whether/how...')",
                "text2_title": "Grammatical Agreement in the Demonstrative Phrase",
                "text2": "The demonstrative pronoun az always assimilates its case suffix to match the noun that follows it. In the sublative (-ra/-re), az becomes arra: arra a döntésre, arra a megfontolásra. The noun and demonstrative agree in case, while the hogy clause completes the content of the decision.",
                "table_title": "Sublative Cataphoric Frames in Historical Narration",
                "table_rows": [
                    ["A vezetők arra a döntésre jutottak, hogy új emlékművet emelnek.", "The leaders arrived at the decision to erect a new monument."],
                    ["A kutatók arra a következtetésre jutottak, hogy a szobrokat többször kicserélték.", "Researchers came to the conclusion that the statues had been replaced several times."],
                    ["Az alkotók arra a kérdésre kerestek választ, hogy ki testesíti meg a nemzetet.", "The creators sought an answer to the question of who personifies the nation."]
                ],
                "examples": [
                    {"spanish": "A dualista korszak vezetői arra a döntésre jutottak, hogy reprezentatív emlékművet emelnek a Városliget bejáratánál.", "english": "The leaders of the Dualist era arrived at the decision to erect a representative monument at the entrance to City Park."},
                    {"spanish": "1945 után a döntéshozók arra az elhatározásra jutottak, hogy a Habsburgok helyére függetlenségi fejedelmeket állítanak.", "english": "After 1945, decision-makers reached the resolution to place independence princes in place of the Habsburgs."},
                    {"spanish": "A történészek arra a következtetésre jutottak, hogy a tér a magyar történelem palimpszesztje.", "english": "Historians came to the conclusion that the square is a palimpsest of Hungarian history."}
                ],
                "tip": "Remember: both the demonstrative and the noun take -ra/-re: 'arra a döntésre' (never 'az a döntésre')."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "pairs": [
                        ["honfoglalás", "Conquest of the Carpathian Basin"],
                        ["pantheon", "hall of national heroes"],
                        ["oszlopcsarnok", "colonnade / portico"],
                        ["reprezentatív", "ceremonial / representative"],
                        ["palimpszeszt", "palimpsest"],
                        ["államalapító", "state-founding"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "question": "Milyen történelmi évforduló alkalmából épült meg a budapesti Hősök tere millenniumi emlékműve?",
                    "options": [
                        "A honfoglalás ezeréves évfordulójára, 1896-ban.",
                        "A mohácsi csata háromszázadik évfordulójára.",
                        "A Lánchíd megnyitásának emlékére."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "sentence": "A Hősök terén álló két félköríves _____ a magyar történelem legjelentősebb uralkodóinak és fejedelmeinek állít emléket.",
                    "answer": "oszlopcsarnok",
                    "english": "The two semicircular colonnades standing on Heroes' Square commemorate the most significant rulers and princes of Hungarian history."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-cataphoric-clauses"],
                    "question": "Which cataphoric phrase idiomatically prepares the complement clause: 'A bizottság _____ jutott, hogy új szobrokat kell felállítani'?",
                    "options": [
                        "arra a döntésre",
                        "abban a döntésben",
                        "arról a döntésről",
                        "azzal a döntéssel"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "sentence": "A politikusok arra az _____ jutottak, hogy a Habsburg királyok helyére erdélyi fejedelmek szobrát állítják. (elhatározás in sublative)",
                    "answer": "elhatározásra",
                    "english": "The politicians reached the resolution to erect statues of Transylvanian princes in place of the Habsburg kings."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "tiles": ["A", "kormány", "arra", "a", "döntésre", "jutott,", "hogy", "emlékművet", "épít."],
                    "solution": ["A", "kormány", "arra", "a", "döntésre", "jutott,", "hogy", "emlékművet", "épít."],
                    "english": "The government arrived at the decision to build a monument."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-cataphoric-clauses"],
                    "prompt": [
                        {"speaker": "Művészettörténész", "text": "Hogyan változott meg a Hősök tere szoborcsarnoka a második világháború után?"},
                        {"speaker": "Kurátor", "text": "_____"}
                    ],
                    "options": [
                        "A döntéshozók arra a következtetésre jutottak, hogy a Habsburg királyok szobrait végleg eltávolítják, és függetlenségi vezetőkkel, például Kossuth Lajossal helyettesítik őket.",
                        "Az egész teret lebontották és sportpályát építettek a helyére.",
                        "Minden szobrot aranyra festettek, de nem cseréltek ki senkit."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Ki látható a Hősök tere közepén álló harminchat méteres oszlop tetején?",
                    "options": [
                        "Gábriel arkangyal, aki a Szent Koronát és a kettős keresztet tartja a magasba.",
                        "Schickedanz Albert építész.",
                        "I. Ferenc József császár és király."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "When Street Names Change Overnight",
            "grammar_label": "Inessive & superessive cataphoric anchors (abban a szellemben, hogy...; azon az alapon, hogy...)",
            "goals": [
                "I can explain how Budapest street names served as ideological palimpsests across 20th-century political regime changes.",
                "I can anchor complement clauses using abban a szellemben/hitben, hogy... and azon az alapon, hogy...",
                "I can analyze the tension between official urban nomenclature and everyday vernacular memory."
            ],
            "story_segment": {
                "seg_slug": "utcanevek",
                "title": "Sugár út, Sztálin út, Andrássy út: Budapest utcanévtáblái",
                "summary": "Few cities in Europe renamed their central boulevards as frequently as Budapest: from Andrássy út becoming Sztálin út and Népköztársaság útja, to the Oktogon becoming Mussolini tér and November 7. tér, city maps mirrored the ideological convulsions of the twentieth century.",
                "location": "Budapest, Andrássy út és az Oktogon (1876–1990)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ha egy budapesti polgár a huszadik század folyamán végigsétált a Deák tértől a Hősök teréig húzódó elegáns sugárúton, a táblák felirataiból pontosan leolvashatta, éppen milyen ideológiai szél fúj az országban. Az eredetileg Sugár útnak keresztelt, majd 1885-ben a miniszterelnökről Andrássy útra átnevezett fasor neve a huszadik században ötször változott meg a politikai rezsimek parancsára."
                    },
                    {
                        "type": "narration",
                        "text": "1950-ben, Rákosi Mátyás uralma idején a pártvezetés abban a szellemben határozott az átnevezésről, hogy a magyar főváros legszebb sugárútjának a szovjet diktátor, Joszif Sztálin nevét kell viselnie. Az Oktogont ezzel párhuzamosan előbb a harmincas években Mussolini térre, majd 1945 után November 7. térre keresztelték át, azon az alapon, hogy a városlakóknak a mindennapi közlekedés során is a bolsevik forradalomra kell emlékezniük."
                    },
                    {
                        "type": "narration",
                        "text": "1956 októberében a forradalmi ifjúság azonnal leverte a Sztálin út táblákat, és helyükre a Magyar Ifjúság útja feliratot festette. A szabadságharc leverése után azonban a Kádár-rendszer kényelmetlennek találta a Sztálin nevet, így a kompromisszumos Népköztársaság útja elnevezést választotta, abban a reményben, hogy a semleges szocialista terminológia feledtetni tudja a forradalmat."
                    },
                    {
                        "type": "narration",
                        "text": "A budapestiek hétköznapi nyelve azonban meglepő ellenállást tanúsított a hivatalos kánonnal szemben. Bár a villamosokon és az igazolványokban évtizedekig a November 7. tér szerepelt, a pesti ember a magánbeszélgetésekben továbbra is csak az Oktogonra hivatkozott, abban a meggyőződésben, hogy a geometrikus térforma régebbi és maradandóbb, mint a múló politikai szeszélyek."
                    },
                    {
                        "type": "narration",
                        "text": "1990-ben a rendszerváltó Fővárosi Közgyűlés visszaadta az Andrássy út és az Oktogon nevét. A folyamat rávilágított arra a sajátos közép-európai tapasztalatra, hogy a városi térkép nem csupán tájékozódási eszköz, hanem a hatalom és a társadalmi emlékezet állandó küzdőtere."
                    }
                ]
            },
            "words": [
                {"lemma": "utcanévtábla", "translation": "street name sign", "pos": "noun"},
                {"lemma": "átnevezés", "translation": "renaming", "pos": "noun"},
                {"lemma": "rezsim", "translation": "regime", "pos": "noun"},
                {"lemma": "kánon", "translation": "canon (official historical narrative)", "pos": "noun"},
                {"lemma": "szeszély", "translation": "whim / caprice", "pos": "noun"},
                {"lemma": "közgyűlés", "translation": "general assembly (e.g. Budapest City Council)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "inessive-superessive-cataphoric-anchors",
                "title": "Inessive & Superessive Cataphoric Anchors: abban a szellemben / azon az alapon, hogy...",
                "text1_title": "Inessive Anchors (abban a szellemben / hitben / reményben, hogy...)",
                "text1": "When explaining the guiding spirit, philosophical assumption, or hopeful rationale behind an action, Hungarian employs an inessive demonstrative phrase (abban) modifying a mental state noun:\n• abban a szellemben, hogy... ('in the spirit of / that...')\n• abban a hitben, hogy... ('in the belief that...')\n• abban a reményben, hogy... ('in the hope that...')\n• abban a meggyőződésben, hogy... ('in the conviction that...')",
                "text2_title": "Superessive Anchors (azon az alapon / ponton, hogy...)",
                "text2": "When citing a legal basis, ideological ground, or conceptual premise, Hungarian shifts to the superessive case (azon):\n• azon az alapon, hogy... ('on the grounds / basis that...')\n• azon a feltételezésen alapul, hogy... ('is based on the assumption that...')\n• azon a ponton, ahol / amikor... ('at the point where / when...')",
                "table_title": "Inessive vs. Superessive Cataphoric Anchors",
                "table_rows": [
                    ["A pártvezetés abban a szellemben határozott, hogy átírják a térképet.", "The party leadership resolved in the spirit that they would rewrite the map."],
                    ["A lakosok abban a hitben éltek, hogy az Oktogon neve örök.", "The residents lived in the belief that the name of the Oktogon was eternal."],
                    ["Azon az alapon nevezték át, hogy a múltat el kell törölni.", "They renamed it on the grounds that the past had to be erased."]
                ],
                "examples": [
                    {"spanish": "A pártvezetés abban a szellemben döntött, hogy a legszebb sugárútnak Sztálin nevét kell viselnie.", "english": "The party leadership decided in the spirit that the most beautiful avenue must bear Stalin's name."},
                    {"spanish": "Azon az alapon nevezték át az Oktogont, hogy a bolsevik forradalomra kell emlékeztetnie a járókelőket.", "english": "They renamed the Oktogon on the grounds that it must remind passersby of the Bolshevik revolution."},
                    {"spanish": "A pesti polgárok abban a meggyőződésben beszéltek, hogy a város formája maradandóbb a múló rezsimeknél.", "english": "The citizens of Pest spoke in the conviction that the city's form is more enduring than transient regimes."}
                ],
                "tip": "Double-check case matching: inessive (-ban/-ben) takes abban; superessive (-on/-en/-ön) takes azon."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "pairs": [
                        ["utcanévtábla", "street name sign"],
                        ["átnevezés", "renaming"],
                        ["rezsim", "regime"],
                        ["kánon", "official historical canon"],
                        ["szeszély", "caprice / whim"],
                        ["közgyűlés", "general assembly"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "question": "Milyen elnevezéseket viselt a mai Andrássy út a huszadik század során a szöveg szerint?",
                    "options": [
                        "Sugár út, Andrássy út, Sztálin út, Magyar Ifjúság útja, Népköztársaság útja, majd ismét Andrássy út.",
                        "Csak és kizárólag Andrássy út volt a neve fennállása óta.",
                        "Váci utca és Rákóczi út között váltakozott."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "sentence": "A budapestiek a Kádár-korszakban is az Oktogon nevet használták a magánbeszélgetésekben a hivatalos November 7. tér _____ helyett.",
                    "answer": "átnevezés",
                    "english": "In the Kádár era, Budapest residents still used the name Oktogon in private conversations instead of the official November 7 Square renaming."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-cataphoric-clauses"],
                    "question": "Which inessive cataphoric phrase means 'in the spirit that...'?",
                    "options": [
                        "abban a szellemben, hogy...",
                        "arra a szellemre, hogy...",
                        "azzal a szellemmel, hogy...",
                        "arról a szellemről, hogy..."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "sentence": "A hatóságok azon az _____ indultak ki, hogy a szimbolikus terek átalakításával formálhatják az állampolgárok tudatát. (alap in superessive)",
                    "answer": "alapon",
                    "english": "The authorities proceeded on the grounds (basis) that they could shape citizens' consciousness by transforming symbolic spaces."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "tiles": ["A", "lakosok", "abban", "a", "hitben", "éltek,", "hogy", "a", "név", "örök."],
                    "solution": ["A", "lakosok", "abban", "a", "hitben", "éltek,", "hogy", "a", "név", "örök."],
                    "english": "The residents lived in the belief that the name was eternal."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-cataphoric-clauses"],
                    "prompt": [
                        {"speaker": "Városszociológus", "text": "Miért nem tudta a Rákosi- és a Kádár-rendszer teljesen kitörölni az Oktogon nevet a budapestiek emlékezetéből?"},
                        {"speaker": "Helytörténész", "text": "_____"}
                    ],
                    "options": [
                        "Mert a lakosok abban a meggyőződésben használták a régi nevet, hogy a tér nyolcszögletű formája és várostörténeti emléke maradandóbb a rezsimek ideológiai átnevezéseinél.",
                        "Mert senki sem tudta elolvasni a cirill betűs táblákat.",
                        "Mert az Oktogonon soha nem járt villamos."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mire festették át az 1956-os forradalmárok a Sztálin út feliratot a forradalom napjaiban?",
                    "options": [
                        "Magyar Ifjúság útja.",
                        "Lenin körút.",
                        "Kossuth Lajos tér."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "Memento Park: Where Toppled Statues Go",
            "grammar_label": "Instrumental & causal cataphoric anchors (azzal a céllal/feltétellel, hogy...)",
            "goals": [
                "I can describe the concept and cultural significance of Ákos Eleőd's Memento Park (Szoborpark).",
                "I can anchor purpose and conditional clauses using azzal a céllal, hogy... and azzal a feltétellel, hogy...",
                "I can discuss historical iconoclasm, architectural memory, and totalitarian relics in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szoborpark",
                "title": "Ákos Eleőd Szoborparkja: Demokrácia a szocialista óriások között (1993)",
                "summary": "Instead of smashing or melting down communist-era monuments after 1989, Budapest chose an innovative cultural solution: architect Ákos Eleőd designed Memento Park on the Tétényi plateau to preserve 42 totalitarian statues as a warning and reflection on dictatorship.",
                "location": "Budapest, Tétényi-fennsík (1993)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1989–1990-ben a közép- és kelet-európai országok mind szembesültek azzal a nehéz kérdéssel, hogy mit kezdjenek a szocialista évtizedek gigantikus köztéri emlékműveivel. Sok városban a dühös tömeg barbár módon szétverte a szobrokat, vagy a kohókban beolvasztották őket, Budapest vezetése azonban azzal a kezdeményezéssel állt elő, hogy a történelem tanulságait nem a megsemmisítés, hanem a kritikai kontextusba helyezés szolgálja a leginkább."
                    },
                    {
                        "type": "narration",
                        "text": "A Fővárosi Közgyűlés pályázatát Eleőd Ákos fiatal építész nyerte meg, aki azzal a határozott művészi céllal tervezte meg a Tétényi-fennsíkon felépülő Szoborparkot, vagyis a Memento Parkot, hogy az intézmény ne a diktatúra gúnyirata, de ne is annak dicsőítése legyen, hanem méltóságteljes mementó a demokrácia erejéről. Eleőd úgy fogalmazott: „Ez a park a diktatúráról szól, de abban a pillanatban, amikor ez megfogalmazódhatott, a demokráciáról is szól.”"
                    },
                    {
                        "type": "narration",
                        "text": "Az 1993-ban megnyílt parkba negyvenkét olyan szobor került ki a főváros tereiről, amelyeket korábban a szovjet megszállás és a kommunista ideológia szimbólumaként állítottak fel. Itt kapott helyet a fegyvert magasba tartó szovjet katona, Osztapenko és Steinmetz kapitány monumentális alakja, valamint a Tanácsköztársaság dühödten rohanó tengerésze."
                    },
                    {
                        "type": "narration",
                        "text": "A park bejáratánál az építész egy hatalmas, klasszicista kulisszafalat emelt, amely a díszes homlokzat mögött valójában semmit sem támaszt meg, ezzel a látvánnyal érzékeltetve a totalitárius hatalom ürességét. A falra Illyés Gyula 1956-os híres költeményének, az Egy mondat a zsarnokságról című versnek a sorait vésték fel."
                    },
                    {
                        "type": "narration",
                        "text": "A Memento Park másik jelképévé a Sztálin-dísztribün és a csizmák másolata vált: 1956. október 23-án a pesti nép ledöntötte a Városliget szélén pöffeszkedő bronzkolosszust, és a talapzaton csupán a diktátor hatalmas csizmái maradtak állva. A park így nem a gyűlöletet táplálja, hanem a történelmi emlékezet szabadságát ünnepli."
                    }
                ]
            },
            "words": [
                {"lemma": "mementó", "translation": "memento / solemn reminder / warning", "pos": "noun"},
                {"lemma": "kulisszafal", "translation": "stage-prop facade / theatrical screen", "pos": "noun"},
                {"lemma": "totalitárius", "translation": "totalitarian", "pos": "adjective"},
                {"lemma": "megsemmisítés", "translation": "destruction / annihilation", "pos": "noun"},
                {"lemma": "dísztribün", "translation": "ceremonial reviewing stand / grandstand", "pos": "noun"},
                {"lemma": "bronzmonumentum", "translation": "bronze monument", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "instrumental-cataphoric-anchors",
                "title": "Instrumental & Causal Cataphoric Anchors: azzal a céllal/feltétellel, hogy...",
                "text1_title": "Forming Purpose and Condition with azzal a + Noun Phrase",
                "text1": "While everyday Hungarian uses azért, hogy + subjunctive for purpose, formal and academic prose prefers an instrumental cataphoric noun phrase (azzal a...) to specify the exact legal, philosophical, or artistic intention behind an action:\n• azzal a céllal / szándékkal, hogy... ('with the aim/intention that / to...')\n• azzal a feltétellel, hogy... ('on the condition that...')\n• azzal az indokkal, hogy... ('on the grounds/justification that...')\n• azzal a felhívással, hogy... ('with the appeal that...')",
                "text2_title": "Subjunctive vs. Indicative Complement",
                "text2": "When the anchor expresses purpose or obligation (azzal a céllal, azzal a feltétellel), the verb in the hogy-clause is conjugated in the subjunctive (-jon/-jen/-jön):\n'Eleőd azzal a céllal tervezte a parkot, hogy a tér elgondolkodtassa a látogatókat.'\nWhen the anchor explains a factual justification (azzal az indokkal), the complement verb can be in the indicative.",
                "table_title": "Instrumental Cataphoric Patterns",
                "table_rows": [
                    ["Eleőd azzal a céllal indult a pályázaton, hogy új értelmet adjon a szobroknak.", "Eleőd entered the competition with the goal of giving new meaning to the statues."],
                    ["Azzal a feltétellel költöztették át őket, hogy nem semmisítik meg az alkotásokat.", "They relocated them on the condition that they would not destroy the works."],
                    ["Azzal az indokkal távolították el a szobrokat, hogy diktatúrát dicsőítettek.", "They removed the statues on the justification that they glorified dictatorship."]
                ],
                "examples": [
                    {"spanish": "Budapest vezetése azzal a kezdeményezéssel állt elő, hogy a szobrokat ne olvasszák be, hanem külön parkban őrizzék meg.", "english": "Budapest's leadership came forward with the initiative that the statues should not be melted down, but preserved in a separate park."},
                    {"spanish": "Eleőd Ákos azzal a határozott céllal tervezte meg a Memento Parkot, hogy méltóságteljes mementója legyen a demokráciának.", "english": "Ákos Eleőd designed Memento Park with the definite aim of being a dignified memento of democracy."},
                    {"spanish": "A kulisszafalat azzal a látvánnyal építették fel, hogy érzékeltesse a totalitárius hatalom ürességét.", "english": "The stage facade was built with the spectacle that it convey the emptiness of totalitarian power."}
                ],
                "tip": "Always ensure the demonstrative az assimilates to azzal before the consonant in a/az: 'azzal a céllal' (never 'az a céllal')."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "pairs": [
                        ["mementó", "solemn reminder / warning"],
                        ["kulisszafal", "theatrical facade screen"],
                        ["totalitárius", "totalitarian"],
                        ["megsemmisítés", "annihilation / destruction"],
                        ["dísztribün", "reviewing grandstand"],
                        ["bronzmonumentum", "bronze monument"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "question": "Hogyan oldotta meg Budapest a kommunista köztéri szobrok sorsát a rendszerváltás után?",
                    "options": [
                        "Nem semmisítették meg őket, hanem a Tétényi-fennsíkon létrehozott Memento Parkba (Szoborparkba) gyűjtötték össze történelmi mementóként.",
                        "Mindegyiket beolvasztották és fegyvereket gyártottak belőlük.",
                        "Az összes szobrot az eredeti helyén hagyták."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "sentence": "Eleőd Ákos a Memento Park bejáratánál egy díszes, de mögötte üres _____ emelt a totalitárius hatalom látszatának jelképeként.",
                    "answer": "kulisszafalat",
                    "english": "At the entrance of Memento Park, Ákos Eleőd erected an ornate but empty stage-prop facade as a symbol of the pretense of totalitarian power."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-cataphoric-clauses"],
                    "question": "Which instrumental cataphoric phrase means 'with the goal/aim that...'?",
                    "options": [
                        "azzal a céllal, hogy...",
                        "arra a célra, hogy...",
                        "abban a célban, hogy...",
                        "arról a célról, hogy..."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "sentence": "A főváros azzal a _____ engedélyezte a park megépítését, hogy a műemlékek történelmi kontextusban maradnak. (feltétel in instrumental)",
                    "answer": "feltétellel",
                    "english": "The capital permitted the construction of the park on the condition that the monuments remain in historical context."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "tiles": ["Eleőd", "azzal", "a", "céllal", "tervezte,", "hogy", "mementót", "állítson."],
                    "solution": ["Eleőd", "azzal", "a", "céllal", "tervezte,", "hogy", "mementót", "állítson."],
                    "english": "Eleőd designed it with the aim of creating a memento."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-cataphoric-clauses"],
                    "prompt": [
                        {"speaker": "Külföldi turista", "text": "Miért nem döntötték le végleg a szovjet szobrokat Budapesten 1989 után?"},
                        {"speaker": "Idegenvezető", "text": "_____"}
                    ],
                    "options": [
                        "Mert a döntéshozók azzal a megfontolással hozták létre a Szoborparkot, hogy a demokrácia nem a múlt eltörléséből, hanem a zsarnokság kritikai megértéséből merít erőt.",
                        "Mert a szobrok túl nehezek voltak ahhoz, hogy elmozdítsák őket.",
                        "Mert nem találtak darukat a fővárosban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik híres magyar költemény sorai olvashatók a Memento Park bejárati téglafalán?",
                    "options": [
                        "Illyés Gyula: Egy mondat a zsarnokságról.",
                        "Petőfi Sándor: Nemzeti dal.",
                        "Vörösmarty Mihály: Szózat."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Traditions of Hungarian Parliamentary Oratory",
            "grammar_label": "Delative & ablative cataphoric anchors (arról a kérdésről/témáról, hogy...; abból a megfontolásból, hogy...)",
            "goals": [
                "I can analyze the historical rhetorical styles of great Hungarian parliamentary orators (Kölcsey, Deák, Kossuth, Apponyi).",
                "I can anchor debate topics and motives using arról a kérdésről, hogy... and abból a megfontolásból, hogy...",
                "I can discuss classical rhetoric, legal argumentation, and parliamentary debate in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szonoklattortenet",
                "title": "A pozsonyi diétától a Steindl-palota kupolaterméig",
                "summary": "Hungarian parliamentary oratory evolved from the Latinate legal debates of the Pozsony Diet into an art form: Ferenc Kölcsey's moral precision, Ferenc Deák's calm constitutional logic, Lajos Kossuth's fiery romantic pathos, and Albert Apponyi's polyglot eloquence.",
                "location": "Pozsony és a budapesti Országház (1832–1920)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar politikai kultúra gerincét évszázadokon át az országgyűlési szónoklat művészete alkotta. A reformkori pozsonyi diétákon az ifjú követek még a latin jogászi retorikán és a klasszikus köztársasági mintákon edződtek, ám amikor az 1830-as években az anyanyelvhasználatért vívott küzdelem a parlament falait is elérte, a magyar szónoklat a nemzeti szabadság leghatásosabb fegyverévé magasztosult."
                    },
                    {
                        "type": "narration",
                        "text": "A korabeli követek arról a kérdésről vitáztak a leghevesebben, hogy a jogkiterjesztés és a jobbágyfelszabadítás miként egyeztethető össze a nemesi alkotmánnyal. Kölcsey Ferenc morális mélységű, cizellált beszédeiben arra tanította kortársait, hogy a haza csak akkor maradhat fenn, ha a népesség minden tagja egyenlő jogokat kap; Deák Ferenc ellenben higgadt, jogászi szigorral érvelt, abból a megfontolásból kiindulva, hogy a Habsburg udvarral szemben csak a tételes jog és a törvényesség tisztelete hozhat tartós sikert."
                    },
                    {
                        "type": "narration",
                        "text": "Kossuth Lajos ezzel szemben a romantikus pátosz mestere volt: amikor 1848 júliusában az első népképviseleti országgyűlésen kétszázezer újonc és negyvenkétmillió forint megajánlását kérte a nemzet védelmére, a képviselők felállva, zúgó viharként kiáltották: „Megadjuk!” Kossuth nem száraz adatokkal hatott, hanem a hallgatóság nemzeti büszkeségére és erkölcsi felelősségére apellált."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1902-ben átadott Steindl-féle neogótikus Országház falai között a dualizmus korának szónokai — Tisza Kálmán, Tisza István, Andrássy Gyula és Apponyi Albert — folytatták a hagyományt. Gróf Apponyi Albert híres, több nyelven elmondott trianoni védőbeszédében arról a dilemmáról győzködte a párizsi békekonferencia küldötteit, hogy az ezeréves történelmi határok szétzúzása Közép-Európa békéjét veszélyezteti."
                    },
                    {
                        "type": "narration",
                        "text": "A modern média korszakában a hosszú órákig tartó szónoklatok helyét ugyan átvették a néhány perces televíziós viták és az internetes videók, ám a klasszikus orátori örökség — a hiteles érvelés, a nyelvi gazdagság és a szellemi bátorság — ma is a minőségi parlamentarizmus zsinórmértéke."
                    }
                ]
            },
            "words": [
                {"lemma": "szónoklat", "translation": "speech / oration / address", "pos": "noun"},
                {"lemma": "retorika", "translation": "rhetoric / art of public speaking", "pos": "noun"},
                {"lemma": "diéta", "translation": "Diet (historical feudal assembly)", "pos": "noun"},
                {"lemma": "népképviseleti", "translation": "popular-representative (parliament elected by citizens)", "pos": "adjective"},
                {"lemma": "zsinórmérték", "translation": "benchmark / touchstone / gold standard", "pos": "noun"},
                {"lemma": "pátosz", "translation": "pathos (impassioned rhetorical elevation)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "delative-ablative-cataphoric-anchors",
                "title": "Delative & Ablative Cataphoric Anchors: arról a kérdésről / abból a megfontolásból, hogy...",
                "text1_title": "Delative Anchors (arról a kérdésről / témáról / dilemmáról, hogy...)",
                "text1": "When introducing the subject of a debate, speech, or philosophical inquiry, Hungarian places a delative demonstrative (arról) before the topic noun:\n• arról a kérdésről vitáztak, hogy... ('they debated the question whether/how...')\n• arról a dilemmáról beszélt, hogy... ('he spoke about the dilemma that...')\n• arról a tényről számolt be, hogy... ('reported on the fact that...')\nThis construction frames the entire complement clause as the exact topic under discussion.",
                "text2_title": "Ablative Anchors (abból a megfontolásból / célzatból, hogy...)",
                "text2": "When explaining an underlying motive, premise, or starting consideration, Hungarian uses an ablative demonstrative phrase (abból):\n• abból a megfontolásból kiindulva, hogy... ('proceeding from the consideration that...')\n• abból a feltevésből indult ki, hogy... ('proceeded from the premise that...')\n• attól a félelemtől vezérelve, hogy... ('guided by the fear that...')",
                "table_title": "Delative vs. Ablative Cataphoric Frames",
                "table_rows": [
                    ["A követek arról a kérdésről vitáztak, hogy ki kapjon szavazati jogot.", "The deputies debated the question of who should receive voting rights."],
                    ["Apponyi arról a dilemmáról beszélt, hogy mi hoz békét Közép-Európában.", "Apponyi spoke about the dilemma of what brings peace to Central Europe."],
                    ["Deák abból a megfontolásból indult ki, hogy a jogfolytonosság a legfontosabb.", "Deák proceeded from the consideration that legal continuity was paramount."]
                ],
                "examples": [
                    {"spanish": "A korabeli követek arról a kérdésről vitáztak a leghevesebben, hogy a jobbágyfelszabadítás miként valósítható meg.", "english": "Contemporary deputies debated most fiercely about the question of how serf emancipation could be achieved."},
                    {"spanish": "Deák Ferenc abból a megfontolásból indult ki, hogy a törvényesség tisztelete hozhat tartós sikert.", "english": "Ferenc Deák proceeded from the consideration that respect for legality could bring enduring success."},
                    {"spanish": "Kossuth Lajos arról győzte meg a képviselőket, hogy a nemzet védelme azonnali áldozatot követel.", "english": "Lajos Kossuth convinced the representatives that defending the nation demanded immediate sacrifice."}
                ],
                "tip": "Match delative -ról/-ről with arról, and elative/ablative -ból/-ből with abból: 'arról a kérdésről' vs. 'abból a megfontolásból'."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "pairs": [
                        ["szónoklat", "oration / political speech"],
                        ["retorika", "rhetoric"],
                        ["diéta", "historical parliamentary Diet"],
                        ["népképviseleti", "popular-representative"],
                        ["zsinórmérték", "touchstone / gold standard"],
                        ["pátosz", "impassioned pathos"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "question": "Hogyan jellemezte a szöveg Deák Ferenc és Kossuth Lajos szónoki stílusának különbségét?",
                    "options": [
                        "Deák a higgadt, tételes jogi érvelésre épített, míg Kossuth a romantikus pátosz és a lelkesítő erkölcsi meggyőzés mestere volt.",
                        "Mindketten csak latinul voltak hajlandók beszélni.",
                        "Kossuth kizárólag gazdasági grafikonokat mutatott be némán."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "sentence": "1848 nyarán Pesten ült össze az első magyar _____ országgyűlés, amelyen már nem a rendek, hanem a választott képviselők döntöttek.",
                    "answer": "népképviseleti",
                    "english": "In the summer of 1848, the first Hungarian popular-representative parliament convened in Pest, where elected representatives rather than feudal estates made decisions."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-cataphoric-clauses"],
                    "question": "Which delative cataphoric phrase introduces the question being debated?",
                    "options": [
                        "arról a kérdésről, hogy...",
                        "arra a kérdésre, hogy...",
                        "abban a kérdésben, hogy...",
                        "azzal a kérdéssel, hogy..."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "sentence": "Deák Ferenc abból a _____ indult ki, hogy a jogfolytonosság védelme a legerősebb fegyver a bécsi udvarral szemben. (megfontolás in elative)",
                    "answer": "megfontolásból",
                    "english": "Ferenc Deák proceeded from the consideration that defending legal continuity was the strongest weapon against the court in Vienna."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "tiles": ["A", "képviselők", "arról", "a", "témáról", "vitáztak,", "hogy", "ki", "szavazhat."],
                    "solution": ["A", "képviselők", "arról", "a", "témáról", "vitáztak,", "hogy", "ki", "szavazhat."],
                    "english": "The representatives debated the topic of who could vote."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-cataphoric-clauses"],
                    "prompt": [
                        {"speaker": "Egyetemista", "text": "Miért tartják Kossuth 1848. júliusi beszédét a magyar retorika egyik csúcsteljesítményének?"},
                        {"speaker": "Történész", "text": "_____"}
                    ],
                    "options": [
                        "Mert nem száraz paragrafusokat sorolt, hanem arról a történelmi felelősségről beszélt, hogy a szabadság védelmében az egész nemzetnek összefogásra van szüksége.",
                        "Mert a beszéd csak három másodpercig tartott.",
                        "Mert németül beszélt, hogy a bécsi követek is megértsék."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Ki tervezte a budapesti Duna-parton magasodó neogótikus Országházat, amelyet 1902-ben adtak át?",
                    "options": [
                        "Steindl Imre.",
                        "Schickedanz Albert.",
                        "Ybl Miklós."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Why History Remains Live Politics in Central Europe",
            "grammar_label": "Synthesizing cataphoric demonstrative noun anchors across all cases in argumentative essays",
            "goals": [
                "I can analyze the politics of memory (emlékezetpolitika) in Central Europe and explain István Bibó's diagnosis of collective historical hysteria.",
                "I can integrate sublative (arra), inessive (abban), instrumental (azzal), and delative (arról) cataphoric noun anchors in a polished B2 essay.",
                "I can evaluate competing historical narratives and advocate for pluralistic democratic remembrance."
            ],
            "story_segment": {
                "seg_slug": "emlekezetpolitika",
                "title": "A Szabadság tér szoborháborúi és a demokratikus emlékezet",
                "summary": "In Budapest's Szabadság tér and Kossuth tér, monuments from the 1848 revolution, the Soviet liberation, and 20th-century traumas stand side by side, illustrating why memory politics remains a live wire in Central Europe and how democratic societies can transcend historical hysteria.",
                "location": "Budapest, Szabadság tér és Kossuth tér (napjainkig)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Kevés hely sűríti magába olyan drámai erővel a magyar történelem ellentmondásait, mint a belvárosi Szabadság tér. A tér egykor az 1848–49-es szabadságharc után felépített hírhedt osztrák katonai erőd, a megfélemlítés szimbólumaként emelt Újépület helyén jött létre, ahol Batthyány Lajos első magyar miniszterelnököt kivégezték; ma pedig egymástól néhány lépésre áll a szovjet katonai emlékmű, a német megszállás vitatott áldozati szobra és Ronald Reagan amerikai elnök bronzalakja."
                    },
                    {
                        "type": "narration",
                        "text": "A politikatudomány ezt a jelenséget emlékezetpolitikának nevezi: a hatalom birtokosai arra a következtetésre jutottak, hogy a nemzeti szimbólumok, évfordulók és szobrok feletti ellenőrzés a legitimáció és a társadalmi kohézió legfontosabb forrása. Egy-egy új emlékmű felállítása vagy régi szobrok áthelyezése sohasem csupán művészeti kérdés, hanem nyílt állásfoglalás a múlt értelmezésében."
                    },
                    {
                        "type": "narration",
                        "text": "Bibó István híres esszéjében arra figyelmeztetett, hogy a kelet- és közép-európai kisállamok történetét állandó egzisztenciális félelem kíséri: a nemzetek abból a rettegésből táplálkoznak, hogy a szomszédos népek vagy a nagyhatalmak megsemmisítik kultúrájukat és függetlenségüket. Ez a félelem könnyen politikai hisztériába torkollik, amelyben a saját bűnökért mindig a külső ellenséget teszik felelőssé, s a múltat szelektív dicsőségtablóvá egyszerűsítik."
                    },
                    {
                        "type": "narration",
                        "text": "A demokratikus emlékezetpolitika ezzel szemben azon az elven alapul, hogy a nemzet érettsége az önkritika képességében mérhető. A totalitárius rezsimek azzal az igénnyel léptek fel, hogy egyetlen hivatalos kánont kényszerítsenek a társadalomra; a plurális demokrácia ellenben teret enged a párhuzamos narratíváknak, a történészvitáknak és az áldozatok iránti közös részvétnek."
                    },
                    {
                        "type": "narration",
                        "text": "A köztéri szobrok végső soron kérdéseket szegeznek a mindenkori jelenhez: nemcsak arra emlékeztetnek, milyenek voltak elődeink, hanem arra a próbatételre is késztetnek bennünket, hogy milyen értékek mentén akarjuk felépíteni a jövőnket."
                    }
                ]
            },
            "words": [
                {"lemma": "emlékezetpolitika", "translation": "politics of memory / memory politics", "pos": "noun"},
                {"lemma": "kohézió", "translation": "cohesion (social cohesion)", "pos": "noun"},
                {"lemma": "hisztéria", "translation": "hysteria (collective historical hysteria in Bibó's sense)", "pos": "noun"},
                {"lemma": "önkritika", "translation": "self-criticism / self-reflection", "pos": "noun"},
                {"lemma": "áldozatvállalás", "translation": "willingness to sacrifice", "pos": "noun"},
                {"lemma": "próbatétel", "translation": "trial / ordeal / moral test", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "cataphoric-synthesis",
                "title": "Mastering Cataphoric Demonstrative Noun Anchors Across Cases",
                "text1_title": "Case System of Cataphoric Anchor Phrases",
                "text1": "In advanced B2 writing, demonstrative noun anchors link complex subordinate clauses to the main clause with architectural elegance. Review the full case paradigm:\n• Sublative (arra a...): arra a döntésre / következtetésre jutott, hogy... (Arrival at a decision or conclusion)\n• Inessive (abban a...): abban a szellemben / hitben / reményben, hogy... (Guiding spirit, belief, hope)\n• Superessive (azon az...): azon az alapon / elven nyugszik, hogy... (Foundational principle or ground)\n• Instrumental (azzal a...): azzal a céllal / szándékkal / feltétellel, hogy... (Purpose or condition)\n• Delative (arról a...): arról a kérdésről / dilemmáról tanácskozott, hogy... (Topic of debate)\n• Ablative (abból a...): abból a megfontolásból / tényből indult ki, hogy... (Starting premise or motive)",
                "text2_title": "Stylistic Power in Essay Discourse",
                "text2": "Without these cataphoric anchors, Hungarian sentences often collapse into repetitive 'azt gondolta, hogy...' or 'azért csinálta, mert...'. Adding specific abstract nouns (döntés, szellem, alap, cél, kérdés, megfontolás) gives your prose the authoritative gravity expected in Hungarian academic, political, and cultural essays.",
                "table_title": "Cataphoric Case Matrix for Essay Writing",
                "table_rows": [
                    ["Sublative: arra a következtetésre, hogy...", "Arra a következtetésre jutottunk, hogy a párbeszéd szükséges."],
                    ["Inessive: abban a szellemben, hogy...", "Abban a szellemben kell emlékeznünk, hogy megbecsüljük egymást."],
                    ["Superessive: azon az elven, hogy...", "A demokrácia azon az elven alapul, hogy a polgár szabad."],
                    ["Instrumental: azzal a céllal, hogy...", "A szobrot azzal a céllal állították, hogy figyelmeztessen."],
                    ["Delative: arról a kérdésről, hogy...", "Arról a kérdésről beszélünk, hogy mit jelent a felelősség."]
                ],
                "examples": [
                    {"spanish": "A hatalom képviselői arra a következtetésre jutottak, hogy a szimbólumok ellenőrzése a legfőbb cél.", "english": "Representatives of power reached the conclusion that control over symbols is the chief goal."},
                    {"spanish": "A demokratikus emlékezet azon az elven alapul, hogy a nemzet nagysága az önkritika képességében mérhető.", "english": "Democratic memory is based on the principle that the greatness of a nation is measured in the capacity for self-criticism."},
                    {"spanish": "A totalitárius hatalom azzal az igénnyel lépett fel, hogy egyetlen hivatalos kánont kényszerítsen a társadalomra.", "english": "Totalitarian power acted with the pretension that it impose a single official canon onto society."}
                ],
                "tip": "In your writing exam, select the noun that precisely describes your cognitive act: deciding (döntés), hoping (remény), grounding (alap), aiming (cél), questioning (kérdés), or considering (megfontolás)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "pairs": [
                        ["emlékezetpolitika", "politics of memory"],
                        ["kohézió", "social cohesion"],
                        ["hisztéria", "collective historical hysteria"],
                        ["önkritika", "self-criticism / self-reflection"],
                        ["áldozatvállalás", "willingness to sacrifice"],
                        ["próbatétel", "moral test / ordeal"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "question": "Mire figyelmeztetett Bibó István a közép- és kelet-európai nemzetek történelmi félelmeivel kapcsolatban?",
                    "options": [
                        "Arra, hogy az állandó egzisztenciális fenyegetettség érzése politikai hisztériát szülhet, amely megakadályozza a reális önkritikát.",
                        "Arra, hogy a nemzeteknek tilos szobrokat emelniük a tereken.",
                        "Arra, hogy a Szabadság téren le kell tiltani a gyalogos forgalmat."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-politikairetorika-vocab"],
                    "sentence": "A demokratikus társadalom érettsége abban mutatkozik meg, hogy képes a múlt tévedéseivel szembenéző _____ gyakorlására.",
                    "answer": "önkritika",
                    "english": "The maturity of a democratic society is shown in being capable of exercising self-criticism that confronts past mistakes."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-cataphoric-clauses"],
                    "question": "Which cataphoric phrase correctly uses the superessive case to introduce a foundational principle?",
                    "options": [
                        "azon az elven, hogy...",
                        "abban az elvben, hogy...",
                        "arra az elvre, hogy...",
                        "arról az elvről, hogy..."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "sentence": "A történész abból a _____ indult ki, hogy a köztéri emlékművek a mindenkori politikai hatalom üzenetét közvetítik. (tény in elative)",
                    "answer": "tényből",
                    "english": "The historian proceeded from the fact that public monuments convey the message of the political power of the time."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-cataphoric-clauses"],
                    "tiles": ["A", "demokrácia", "azon", "az", "elven", "alapul,", "hogy", "a", "vita", "szabad."],
                    "solution": ["A", "demokrácia", "azon", "az", "elven", "alapul,", "hogy", "a", "vita", "szabad."],
                    "english": "Democracy is based on the principle that debate is free."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-cataphoric-clauses"],
                    "prompt": [
                        {"speaker": "Filozófus", "text": "Hogyan különböztethető meg a totalitárius emlékezetpolitika a plurális demokrácia emlékezetétől?"},
                        {"speaker": "Politológus", "text": "_____"}
                    ],
                    "options": [
                        "A diktatúra azzal a követeléssel lép fel, hogy egyetlen kánont erőltessen mindenkire, a demokrácia ellenben azon az elven alapul, hogy a sokszínű történelmi tapasztalatok egymás mellett létezhetnek.",
                        "A demokráciában egyáltalán nincsenek sem szobrok, sem múzeumok.",
                        "Nincs köztük különbség, mert a történelem soha nem változik."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik miniszterelnök kivégzésének helyén épült fel a pesti Szabadság tér az Újépület lebontása után?",
                    "options": [
                        "Batthyány Lajos, az első felelős magyar miniszterelnök.",
                        "Kossuth Lajos kormányzóelnök.",
                        "Andrássy Gyula gróf."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can explain how Hungarian monuments (Hősök tere, Szoborpark, Szabadság tér) and street names reflect regimes, collective memory, and memory politics.",
            "I can analyze classic Hungarian parliamentary rhetoric from Reform Era orators to the modern era.",
            "I can fluently construct cataphoric demonstrative noun anchors in all cases (arra a..., abban a..., azon az..., azzal a..., arról a..., abból a...).",
            "I can deploy 30 B2 terms related to public memory, monuments, oratory, and political culture."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-politikairetorika-vocab"],
                "pairs": [
                    ["emlékezetpolitika", "politics of memory"],
                    ["palimpszeszt", "palimpsest"],
                    ["kulisszafal", "theatrical stage facade"],
                    ["népképviseleti", "popular-representative"],
                    ["zsinórmérték", "benchmark / touchstone"],
                    ["önkritika", "self-criticism / self-reflection"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-cataphoric-clauses"],
                "question": "Which cataphoric demonstrative phrase introduces a purpose with the noun 'cél'?",
                "options": [
                    "azzal a céllal, hogy...",
                    "arra a célra, hogy...",
                    "abban a célban, hogy...",
                    "arról a célról, hogy..."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-politikairetorika-vocab"],
                "question": "Ki tervezte a budapesti Tétényi-fennsíkon található Memento Parkot (Szoborparkot) 1993-ban?",
                "options": [
                    "Eleőd Ákos építész.",
                    "Steindl Imre építész.",
                    "Zala György szobrász.",
                    "Ybl Miklós építész."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-politikairetorika-vocab"],
                "sentence": "A budapesti Hősök tere emlékműve a magyar történelem kőbe és bronzba vésett _____ vált, mivel a különböző rezsimek kicserélték az uralkodók szobrait.",
                "answer": "palimpszesztjévé",
                "english": "The monument of Heroes' Square in Budapest became a palimpsest carved into stone and bronze, as various regimes replaced the statues of rulers."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-cataphoric-clauses"],
                "sentence": "A Fővárosi Közgyűlés arra a _____ jutott, hogy a szocialista szobrokat nem beolvasztani kell, hanem külön parkban bemutatni. (döntés in sublative)",
                "answer": "döntésre",
                "english": "The Budapest City Council reached the decision that the socialist statues should not be melted down, but displayed in a separate park."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-cataphoric-clauses"],
                "sentence": "Deák Ferenc abból a _____ indult ki, hogy a jogállamiság és a törvényesség tisztelete a nemzet megmaradásának alapja. (megfontolás in elative)",
                "answer": "megfontolásból",
                "english": "Ferenc Deák proceeded from the consideration that the rule of law and respect for legality were the foundation of the nation's survival."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-cataphoric-clauses"],
                "prompt": [
                    {"speaker": "Építészhallgató", "text": "Miért különleges művészeti alkotás a Memento Park kulisszafala?"},
                    {"speaker": "Oktató", "text": "_____"}
                ],
                "options": [
                    "Mert Eleőd Ákos azzal a szándékkal tervezte a díszes homlokzatot, hogy a látogató a mögötte lévő ürességet látva megértse a totalitárius diktatúra illuzórikus jellegét.",
                    "Mert a falon van Budapest legnagyobb moziplakátja.",
                    "Mert a falat kizárólag aranytéglákból építették fel."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-cataphoric-clauses"],
                "question": "Which sentence demonstrates proper grammatical agreement and natural word order in a cataphoric clause?",
                "options": [
                    "A miniszter azzal a határozott céllal lépett a szószékre, hogy meggyőzze a képviselőket a reform szükségességéről.",
                    "A miniszter arra a határozott céllal lépett a szószékre.",
                    "A miniszter abban a határozott céllal lépett a szószékre.",
                    "A miniszter az a céllal lépett a szószékre."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-cataphoric-clauses"],
                "prompt": [
                    {"speaker": "Politológus", "text": "Hogyan definiálhatjuk a modern plurális emlékezetpolitikát Bibó István gondolatai alapján?"},
                    {"speaker": "Szociológus", "text": "_____"}
                ],
                "options": [
                    "Úgy, hogy a demokrácia azon az elven nyugszik, hogy a közösség mer szembenézni saját múltjának árnyoldalaival is, ahelyett hogy hisztérikus mítoszokba menekülne.",
                    "Úgy, hogy a politikusok minden évben új szobrot rendelnek minden utcára.",
                    "Úgy, hogy a parlamentben betiltják a történelmi vitákat."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-cataphoric-clauses"],
                "tiles": ["A", "bizottság", "arra", "a", "döntésre", "jutott,", "hogy", "új", "emlékművet", "emel."],
                "solution": ["A", "bizottság", "arra", "a", "döntésre", "jutott,", "hogy", "új", "emlékművet", "emel."],
                "english": "The committee reached the decision to erect a new monument."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-cataphoric-clauses"],
                "tiles": ["Kossuth", "azzal", "a", "céllal", "szónokolt,", "hogy", "lelkesítse", "a", "nemzetet."],
                "solution": ["Kossuth", "azzal", "a", "céllal", "szónokolt,", "hogy", "lelkesítse", "a", "nemzetet."],
                "english": "Kossuth spoke with the aim of inspiring the nation."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-cataphoric-clauses"],
                "template": [
                    {
                        "prompt": "Write a sentence describing the decision to build the Millennium Monument at Hősök tere in 1896 (use 'arra a döntésre jutottak, hogy...').",
                        "answer": "A vezetők 1896-ban arra a döntésre jutottak, hogy a honfoglalás ezeréves évfordulójára monumentális oszlopcsarnokot emelnek a Hősök terén."
                    },
                    {
                        "prompt": "Write a sentence explaining the democratic principle of memory politics (use 'azon az elven alapul, hogy...').",
                        "answer": "A demokratikus emlékezetpolitika azon az elven alapul, hogy a nemzeti önismeret az őszinte önkritikából és a közös felelősségvállalásból fakad."
                    }
                ]
            }
        ]
    }
}


if __name__ == "__main__":
    print("Building Hungarian B2 Culture Units 16, 17, and 18...")
    build_culture_unit(UNIT_16_URBANUSNEPI)
    build_culture_unit(UNIT_17_MEDIATORTENET)
    build_culture_unit(UNIT_18_POLITIKAIRETORIKA)
    print("All 3 Culture Track units (16, 17, 18) built successfully!")


