#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 10, 11, and 12:
  - Unit 10: b2-gimnaziumok (The Fasori & Eötvös Tradition: Elite Education)
  - Unit 11: b2-pszichoanalizis (The Budapest School of Psychoanalysis & the Mind)
  - Unit 12: b2-talalmanyok (From Kempelen's Chess Turk to Rubik's Cube)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402


UNIT_10_GIMNAZIUMOK = {
    "unit_num": 10,
    "slug": "gimnaziumok",
    "title": "The Fasori & Eötvös Tradition: Elite Education",
    "grammar_skill": "b2-causative-agents",
    "vocab_skill": "b2-gimnaziumok-vocab",
    "theme": "Hungarian secondary schools, Fasori Gimnázium and Eötvös Collegium",
    "location": "Budapest (Fasori Evangélikus Gimnázium, Minta Gimnázium, Eötvös Collegium)",
    "intro_body": [
        "How did a few secondary schools within a two-kilometer radius in early 20th-century Budapest educate Eugene Wigner, John von Neumann, Edward Teller, Theodore von Kármán, and Leo Szilard? Historians of science often point to the extraordinary pedagogical culture of Hungary's classic gimnáziumok and teacher-training institutions.",
        "In this unit, you will step inside László Rátz's legendary mathematics classroom at the Fasori Evangélikus Gimnázium, explore Mór Kármán's Minta Gimnázium, examine the meritocratic mission of Baron Loránd Eötvös's Collegium, and debate modern dilemmas between talent nurturing and social equity. Grammatically, you will master causative verb derivation (-at/-et, -tat/-tet) and the case-marking of intermediate agents with -val/-vel."
    ],
    "combined_story_title": "Rátz tanár úr katedrája: A magyar iskola titka",
    "combined_story_summary": "Inside the legendary classrooms of the Fasori Gimnázium, the Minta Gimnázium, and the Eötvös József Collegium: how visionary teachers like László Rátz and Mór Kármán educated Nobel laureates and shaped Hungarian pedagogy.",
    "lessons": [
        {
            "num": 1,
            "title": "Inside the Fasori Gimnázium Classroom",
            "grammar_label": "Causative suffixes -at/-et and -tat/-tet with transitive verbs",
            "goals": [
                "I can explain how László Rátz és Mikola Sándor nurtured scientific talent at the Fasori Gimnázium.",
                "I can form causative verbs using -at/-et and -tat/-tet according to syllable count and stem type.",
                "I can use B2 academic and historical classroom vocabulary accurately."
            ],
            "story_segment": {
                "seg_slug": "fasorigimnazium",
                "title": "A Városligeti fasor katedrája",
                "summary": "At the Fasori Evangélikus Gimnázium, mathematics teacher László Rátz recognized the genius of young John von Neumann and Eugene Wigner, replacing rote memorization with creative problem-solving.",
                "location": "Budapest, Városligeti fasor (1910-es évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század első évtizedeiben a Városligeti fasorban álló evangélikus gimnázium külsejében alig különbözött a főváros többi középiskolájától, ám a falai között olyan szellemi műhely működött, amelyet később a világ tudománytörténészei is csodálattal emlegettek. Ebben az iskolában koptatta a padokat Wigner Jenő, a későbbi Nobel-díjas fizikus, és néhány évvel utána Neumann János, a modern számítástudomány megalapítója."
                    },
                    {
                        "type": "narration",
                        "text": "A legendás eredmények mögött elsősorban Rátz László matematikatanár és Mikola Sándor fizikatanár állt, akik soha nem elégedtek meg azzal, hogy a képleteket gépiesen bemagoltassák a tanulókkal. Rátz tanár úr minden órán önálló gondolkodásra késztette a diákokat: ahelyett, hogy kész megoldásokat diktált volna, a legtehetségesebb fiúkkal vezettette le a táblánál az új tételeket."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Rátz észrevette, hogy a tizenegy éves Neumann János matematikai képességei messze meghaladják a középiskolai tananyagot, behívatta az édesapját az igazgatói irodába. Meggyőzte a családot, hogy a fiút egyetemi tanárokkal, köztük Szegő Gáborral is taníttassák különórákon, miközben az iskolában továbbra is a kortársaival együtt érettségizik."
                    },
                    {
                        "type": "narration",
                        "text": "Wigner Jenő évtizedekkel később is meghatottan idézte fel, hogy Rátz László nemcsak a Középiskolai Matematikai Lapok feladatait oldatta meg velük, hanem saját könyvtárából is rendszeresen kölcsönzött nekik szakmunkákat. A tanár úr arcképe haláláig kint függött Wigner princetoni dolgozószobájának falán, mert a tudós úgy érezte, tőle tanulta meg a tudományos alázatot."
                    },
                    {
                        "type": "narration",
                        "text": "A fasori szellem lényege a felekezeti nyitottság és a szigorú szakmai igényesség ötvözete volt: az evangélikus iskola kapui minden felekezetű diák előtt nyitva álltak, így a pesti polgárság legkülönbözőbb rétegeiből érkező tehetségek inspirálhatták egymást."
                    }
                ]
            },
            "words": [
                {"lemma": "katedra", "translation": "teacher's desk / dais / professorship", "pos": "noun"},
                {"lemma": "bemagoltat", "translation": "to make someone cram / memorize by rote", "pos": "verb"},
                {"lemma": "levezettet", "translation": "to have someone derive / deduce (a proof)", "pos": "verb"},
                {"lemma": "érettségizik", "translation": "to take the secondary school leaving exam (Matura)", "pos": "verb"},
                {"lemma": "felekezeti", "translation": "denominational / confessional", "pos": "adjective"},
                {"lemma": "igényesség", "translation": "high standards / exactingness", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "causative-formation",
                "title": "Causative Verb Derivation (-at/-et vs. -tat/-tet)",
                "text1_title": "Forming Causative Verbs ('to have someone do something')",
                "text1": "In B2 Hungarian, causative suffixes turn an action verb into 'make/have someone do X'. Short, monosyllabic verb stems (unless ending in consonant + t) generally take -at/-et (ír → írat, mos → mosat, kér → kéret), whereas polysyllabic stems and monosyllables ending in consonant + t take -tat/-tet (olvas → olvastat, tanít → taníttat, megold → megoldat / levezet → levezettet).",
                "text2_title": "Marking the Intermediate Agent with -val/-vel",
                "text2": "When the base verb is transitive (already has a direct object in -t), the person who actually performs the action (the causee or intermediate agent) is marked with the instrumental suffix -val/-vel: 'Rátz a diákokkal vezettette le a tételt' (Rátz had the students derive the theorem). Notice how the direct object (a tételt) triggers definite conjugation on the causative verb (vezettette).",
                "table_title": "Base Verb vs. Causative Verb & Agent Marking",
                "table_rows": [
                    ["A diák megoldja a feladatot.", "A tanár a diákkal oldatja meg a feladatot."],
                    ["A tanulók bemagolják a képleteket.", "A tanár nem magoltatja be a tanulókkal a képleteket."],
                    ["Az egyetemi tanár tanítja a fiút.", "Az apa egyetemi tanárral taníttatja a fiút."],
                    ["A fiú levezeti a bizonyítást.", "Rátz a fiúval vezetteti le a bizonyítást."]
                ],
                "examples": [
                    {"spanish": "Rátz tanár úr a legtehetségesebb fiúkkal vezettette le az új tételeket.", "english": "Mr. Rátz had the most talented boys derive the new theorems."},
                    {"spanish": "Soha nem elégedtek meg azzal, hogy a képleteket gépiesen bemagoltassák a tanulókkal.", "english": "They were never satisfied with having the pupils mechanically cram the formulas."},
                    {"spanish": "A családot meggyőzte, hogy a fiút egyetemi tanárokkal is taníttassák.", "english": "He convinced the family to have the boy taught by university professors as well."}
                ],
                "tip": "Pay attention to stem-final -t in verbs like tanít ('teaches') or készít ('prepares'): when you add -tat/-tet, the double t (taníttat, készíttet) is both pronounced long and written with two t's!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "pairs": [
                        ["katedra", "teacher's dais / desk"],
                        ["bemagoltat", "to make someone cram by rote"],
                        ["levezettet", "to have someone derive a proof"],
                        ["érettségizik", "to take the Matura exam"],
                        ["felekezeti", "denominational"],
                        ["igényesség", "high standards"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "question": "Milyen módszerrel tanított Rátz László a Fasori Evangélikus Gimnáziumban?",
                    "options": [
                        "Nem magoltatta be gépiesen a képleteket, hanem a diákokkal vezettette le az új tételeket.",
                        "Minden órán némán lemásoltatta a tankönyv oldalait.",
                        "Kizárólag felekezeti énekeket taníttatott a matematikaórákon."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "sentence": "A tanár úr a katedráról figyelt, miközben a diákkal _____ le a geometriai bizonyítást a táblánál.",
                    "answer": "vezettette",
                    "english": "The teacher watched from the dais while having the student derive the geometric proof at the blackboard."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-causative-agents"],
                    "question": "How is the intermediate agent ('the students') marked in the causative sentence: 'A tanár _____ oldatta meg a nehéz feladatot'?",
                    "options": ["a diákokkal", "a diákokat", "a diákoknak", "a diákoktól"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "sentence": "Neumann János édesapja egyetemi professzorokkal _____ a rendkívül tehetséges fiút. (tanít - 3rd sg. def. past causative)",
                    "answer": "taníttatta",
                    "english": "John von Neumann's father had the extraordinarily talented boy taught by university professors."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "tiles": ["Rátz", "tanár", "úr", "a", "diákokkal", "vezettette", "le", "az", "új", "tételt."],
                    "solution": ["Rátz", "tanár", "úr", "a", "diákokkal", "vezettette", "le", "az", "új", "tételt."],
                    "english": "Mr. Rátz had the students derive the new theorem."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-causative-agents"],
                    "prompt": [
                        {"speaker": "Tudománytörténész", "text": "Miért tartotta Wigner Jenő élete végéig a szobájában Rátz László fényképét?"},
                        {"speaker": "Fizikus", "text": "_____"}
                    ],
                    "options": [
                        "Mert Rátz nemcsak a matematikai lapok feladatait oldatta meg velük, hanem valódi tudományos igényességre nevelte őket.",
                        "Mert Rátz tanár úr Princetoni Egyetemen építtetett neki új laboratóriumot.",
                        "Mert minden reggel bemagoltatta velük a telefonkönyvet."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit tanácsolt Rátz László Neumann János édesapjának, amikor felismerte a fiú kivételes képességeit?",
                    "options": [
                        "Hogy egyetemi tanárokkal, például Szegő Gáborral is taníttassák különórákon.",
                        "Hogy azonnal vegyék ki a gimnáziumból, és küldjék külföldi katonai iskolába.",
                        "Hogy tiltsák el a matematikától az érettségiig."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Kármán Mór and the Minta Gimnázium Model",
            "grammar_label": "Causatives of intransitive verbs vs. transitive verbs (accusative vs. instrumental causee)",
            "goals": [
                "I can describe how Mór Kármán established the Minta Gimnázium as a training school for Hungarian teachers.",
                "I can distinguish between accusative causees (from intransitive base verbs) and instrumental causees (from transitive base verbs).",
                "I can discuss pedagogical methodology and curriculum reform in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "mintagimnazium",
                "title": "Kármán Mór és a Trefort utcai Minta Gimnázium",
                "summary": "Founded in 1872 by Mór Kármán with the support of Minister Ágoston Trefort, the Practicing Secondary School ('Minta') trained generations of teachers and educated pioneers like Theodore von Kármán and Edward Teller.",
                "location": "Budapest, Trefort utca (1872–1920)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1867-es kiegyezés után Eötvös József és Trefort Ágoston kultuszminiszterek felismerték, hogy a modern magyar közoktatás csak akkor emelkedhet európai színvonalra, ha a leendő középiskolai tanárokat gyakorlóiskolákban készítik fel a pályára. Trefort ezért Lipcsébe küldte a fiatal filozófust és pedagógust, Kármán Mórt, majd hazatérése után, 1872-ben rábízta a budapesti gyakorló főgimnázium megszervezését."
                    },
                    {
                        "type": "narration",
                        "text": "Az intézményt a köznyelv hamarosan csak Minta Gimnáziumként kezdte emlegetni, mert Kármán Mór teljesen új pedagógiai elveket honosított meg benne. A tanárjelölteket nem elméleti előadásokkal fárasztotta, hanem tapasztalt vezetőtanárok felügyelete mellett azonnal tanítani állította őket a katedrára, majd közösen elemeztette velük a megtartott órák minden percét."
                    },
                    {
                        "type": "narration",
                        "text": "Kármán Mór saját fia, Kármán Tódor — a modern aerodinamika és az űrhajózás későbbi világhírű úttörője — szintén a Minta Gimnázium padjaiban nevelkedett. Amikor a hatéves Tódor fejszámolási bravúrjaival elkápráztatta a vendégeket, édesapja szigorúan leállította a mutatványt, és inkább irodalmat, történelmet meg művészettörténetet olvastatott vele, hogy a fiú személyisége harmonikusan fejlődjön."
                    },
                    {
                        "type": "narration",
                        "text": "A Trefort utcai iskolában a tanárok a diákokat nem passzív hallgatókként ültették a padokba, hanem kísérleteztették, vitatkoztatták és önálló megfigyelésekre bátorították őket. Itt érettségizett később Teller Ede és Polányi Mihály is, akik mindketten kiemelték, milyen sokat köszönhettek a Minta szabad, kérdezésre épülő légkörének."
                    },
                    {
                        "type": "narration",
                        "text": "Kármán Mór tantervi reformja egész Magyarországon éreztette a hatását: a klasszikus latin és görög műveltség mellé egyenrangúként emelte be a természettudományokat és a modern irodalmat. A Minta Gimnázium így vált a magyar tanárképzés bölcsőjévé."
                    }
                ]
            },
            "words": [
                {"lemma": "gyakorlóiskola", "translation": "teacher-training / demonstration school", "pos": "noun"},
                {"lemma": "tanárjelölt", "translation": "trainee teacher / teacher candidate", "pos": "noun"},
                {"lemma": "tanterv", "translation": "curriculum / syllabus", "pos": "noun"},
                {"lemma": "vitatkoztat", "translation": "to engage in debate / make someone debate", "pos": "verb"},
                {"lemma": "kísérleteztet", "translation": "to have someone conduct experiments", "pos": "verb"},
                {"lemma": "fejszámolás", "translation": "mental arithmetic", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "intransitive-vs-transitive-causatives",
                "title": "Accusative vs. Instrumental Causees in Causative Constructions",
                "text1_title": "When the Base Verb is Intransitive (-t on the Causee)",
                "text1": "If the underlying verb is intransitive (has no direct object of its own, such as ül 'sits', vitatkozik 'debates', kísérletezik 'experiments', dolgozik 'works'), making it causative turns the performer of the action into the direct object in the accusative (-t): 'A tanár vitatkoztatta a diákokat' (The teacher made the students debate); 'Kármán nem fárasztotta a tanárjelölteket' (Kármán did not tire out the trainee teachers).",
                "text2_title": "When the Base Verb is Transitive (-val/-vel on the Causee)",
                "text2": "By contrast, as soon as the sentence includes a direct object of the action itself (irodalmat olvas, az órát elemzi), the direct object slot (-t) is already occupied. Therefore, the person made to perform the action shifts to the instrumental case (-val/-vel): 'Az apa irodalmat olvastatott a fiúval' (The father had the boy read literature); 'Kármán a tanárjelöltekkel elemeztette a megtartott órákat'.",
                "table_title": "Intransitive Base (Causee in -t) vs. Transitive Base (Causee in -val/-vel)",
                "table_rows": [
                    ["A diákok vitatkoznak. (Intransitive)", "A tanár vitatkoztatja a diákokat. (Causee = -t)"],
                    ["A diákok kísérleteznek. (Intransitive)", "A tanár kísérletezteti a diákokat. (Causee = -t)"],
                    ["A fiú irodalmat olvas. (Transitive)", "Az apa irodalmat olvastat a fiúval. (Causee = -val)"],
                    ["A jelöltek elemzik az órát. (Transitive)", "Kármán a jelöltekkel elemezteti az órát. (Causee = -vel)"]
                ],
                "examples": [
                    {"spanish": "A tanárok vitatkoztatták és kísérleteztették a diákokat az órán.", "english": "The teachers had the students debate and conduct experiments in class."},
                    {"spanish": "Kármán Mór a tanárjelöltekkel elemeztette a megtartott órák minden percét.", "english": "Mór Kármán had the trainee teachers analyze every minute of the lessons delivered."},
                    {"spanish": "Édesapja inkább történelmet és irodalmat olvastatott a fiatal Tódorral.", "english": "His father had young Theodore read history and literature instead."}
                ],
                "tip": "Notice that lexicalized causative pairs like ül → ültet ('sits → seats') or áll → állít ('stands → sets/places') follow the exact same rule: 'leültette a diákokat a padokba' takes -t because ül is intransitive!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "pairs": [
                        ["gyakorlóiskola", "teacher-training school"],
                        ["tanárjelölt", "trainee teacher"],
                        ["tanterv", "curriculum"],
                        ["vitatkoztat", "to make someone debate"],
                        ["kísérleteztet", "to have someone experiment"],
                        ["fejszámolás", "mental arithmetic"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "question": "Mi volt a Kármán Mór által 1872-ben megszervezett Minta Gimnázium legfőbb küldetése?",
                    "options": [
                        "Gyakorlóiskolaként felkészíteni a leendő középiskolai tanárokat és megújítani a magyar tantervet.",
                        "Kizárólag fejszámoló művészeket képezni a külföldi színházak számára.",
                        "Megszüntetni a természettudományok oktatását a középiskolákban."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "sentence": "A tapasztalt vezetőtanárok minden megtartott óra után szakmailag irányították a fiatal _____ munkáját.",
                    "answer": "tanárjelöltek",
                    "english": "After every lesson delivered, the experienced mentor teachers professionally guided the work of the young trainee teachers."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-causative-agents"],
                    "question": "Why does 'a diákokat' take the accusative (-t) in 'A tanár vitatkoztatta a diákokat', whereas 'a fiúval' takes -val in 'Az apa irodalmat olvastatott a fiúval'?",
                    "options": [
                        "Because 'vitatkozik' is intransitive (no other direct object), while 'irodalmat olvas' already has a direct object ('irodalmat').",
                        "Because plural nouns always take -t and singular nouns always take -val.",
                        "Because 'olvastat' is in the past tense while 'vitatkoztat' is in the present tense.",
                        "Because 'diák' is animate and 'irodalom' is inanimate."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "sentence": "Kármán Mór a tanárjelöltekkel _____ a megtartott tanórák tapasztalatait. (elemez - 3rd sg. def. past causative)",
                    "answer": "elemeztette",
                    "english": "Mór Kármán had the trainee teachers analyze the experiences of the lessons taught."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "tiles": ["Az", "édesapja", "irodalmat", "és", "történelmet", "olvastatott", "a", "fiatal", "Tódorral."],
                    "solution": ["Az", "édesapja", "irodalmat", "és", "történelmet", "olvastatott", "a", "fiatal", "Tódorral."],
                    "english": "His father had young Theodore read literature and history."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-causative-agents"],
                    "prompt": [
                        {"speaker": "Pedagógus", "text": "Miért nem engedte Kármán Mór, hogy a hatéves fia csak fejszámolással kápráztassa el a vendégeket?"},
                        {"speaker": "Életrajzíró", "text": "_____"}
                    ],
                    "options": [
                        "Mert harmonikus személyiséget akart nevelni belőle, ezért inkább irodalmat és művészettörténetet olvastatott vele.",
                        "Mert nem tudta, hogyan kell a tanárjelölteket a katedrára állítani.",
                        "Mert Trefort Ágoston betiltotta a matematikát a Minta Gimnáziumban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik két későbbi világhírű tudós érettségizett Kármán Tódoron kívül a Trefort utcai Minta Gimnáziumban?",
                    "options": [
                        "Teller Ede és Polányi Mihály.",
                        "Bolyai János és Kőrösi Csoma Sándor.",
                        "Kempelen Farkas és Jedlik Ányos."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "The Eötvös Collegium and Intellectual Meritocracy",
            "grammar_label": "Institutional and double-object causative constructions",
            "goals": [
                "I can explain how Baron Loránd Eötvös founded the Eötvös József Collegium in 1895 on the model of the École Normale Supérieure.",
                "I can use institutional causative verbs (alapíttat, építtet, pályáztat, fordíttat) with clear agency.",
                "I can discuss meritocracy and social mobility in higher education."
            ],
            "story_segment": {
                "seg_slug": "eotvoscollegium",
                "title": "A Ménesi úti szellemi műhely",
                "summary": "Modeled on the Paris École Normale Supérieure and founded in 1895 by physicist Loránd Eötvös, the Eötvös József Collegium gave gifted students from poor provincial backgrounds world-class training.",
                "location": "Budapest, Ménesi út (1895–1930-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1895-ben Eötvös Loránd világhírű fizikus és kultuszminiszter a párizsi École Normale Supérieure mintájára olyan bentlakásos elitkollégiumot alapított Budapesten, amely édesapja, Eötvös József báró nevét vette fel. A cél az volt, hogy az ország legkiválóbb, ám gyakran szerény anyagi sorból származó vidéki fiataljaiból világszínvonalú tanárokat és tudósokat képezzenek."
                    },
                    {
                        "type": "narration",
                        "text": "A felvételi vizsga legendásan szigorú volt, de a bekerülésnél sem a családi vagyon, sem a társadalmi rang nem számított. Az állam a Ménesi úton impozáns épületet emeltetett a Collegium számára, ahol a hallgatók teljes ellátást, saját dolgozószobát és Európa egyik leggazdagabb szakkönyvtárát kapták meg, hogy kizárólag a tudománynak szentelhessék az idejüket."
                    },
                    {
                        "type": "narration",
                        "text": "Bartoniek Géza igazgató és a Collegium professzorai az egyetemi előadásokon túl saját szemináriumokat tartottak, amelyeken eredeti forrásokat fordíttattak le a diákokkal, és mindenkitől legalább két-három idegen nyelv folyékony ismeretét követelték meg. A műhelymunkában olyan későbbi óriások nőttek fel, mint Kodály Zoltán zeneszerző, Szekfű Gyula történész vagy Kosztolányi Dezső és Babits Mihály kortársai."
                    },
                    {
                        "type": "narration",
                        "text": "Az Eötvös-kollégisták nem elszigetelt elefántcsonttoronyban éltek: végzésük után a minisztérium az ország különböző vidéki és fővárosi gimnáziumaiba helyeztette őket, hogy a Ménesi úton elsajátított kritikai gondolkodást minden vármegyébe elvigyék. Egyetlen évtized alatt érezhetően megemelkedett a magyar középiskolai oktatás általános színvonala."
                    },
                    {
                        "type": "narration",
                        "text": "Az Eötvös Collegium így bizonyította be, hogy az érdemelvű tehetséggondozás és a társadalmi mobilitás nem zárja ki egymást: ha a közösség a legszegényebb faluból érkező tehetséget is a legjobb mesterekkel taníttatja, abból az egész nemzet szellemi tőkét kovácsolhat."
                    }
                ]
            },
            "words": [
                {"lemma": "bentlakásos", "translation": "residential / boarding (college or school)", "pos": "adjective"},
                {"lemma": "érdemelvű", "translation": "meritocratic / based on merit", "pos": "adjective"},
                {"lemma": "tehetséggondozás", "translation": "talent nurturing / gifted education", "pos": "noun"},
                {"lemma": "műhelymunka", "translation": "workshop / seminar research work", "pos": "noun"},
                {"lemma": "szellemi tőke", "translation": "intellectual capital", "pos": "expression"},
                {"lemma": "elefántcsonttorony", "translation": "ivory tower", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "institutional-causatives",
                "title": "Institutional Causatives: Commissioning vs. Performing an Action",
                "text1_title": "Institutional vs. Direct Action in Historical Narratives",
                "text1": "In historical and academic Hungarian, carefully distinguishing between base transitive verbs (épít 'builds', fordít 'translates', áthelyez 'transfers') and their causative counterparts (építtet / emeltet 'commissions to be built', fordíttat 'has translated', helyeztet 'has placed/assigned') shows whether a leader or institution performed the task personally or commissioned experts/students to do it.",
                "text2_title": "Agentless Institutional Causatives",
                "text2": "When the intermediate builder or clerk is obvious from context, the -val/-vel phrase can be omitted while the causative suffix remains on the verb: 'Az állam a Ménesi úton impozáns épületet emeltetett' (The state had an imposing building erected on Ménesi Road). When the performers are pedagogically important, they are explicitly stated with -val/-vel: 'A professzorok eredeti forrásokat fordíttattak le a diákokkal'.",
                "table_title": "Direct Action vs. Institutional Causative",
                "table_rows": [
                    ["Az építész felépítette a kollégiumot.", "Az állam új kollégiumot építtetett a Ménesi úton."],
                    ["A diákok lefordították a görög forrásokat.", "A professzorok a diákokkal fordíttatták le a forrásokat."],
                    ["A tanárok vidéki iskolákban tanítottak.", "A minisztérium vidéki iskolákba helyeztette a végzősöket."],
                    ["A legjobb mesterek tanítják a tehetségeket.", "A közösség a legjobb mesterekkel taníttatja a tehetségeket."]
                ],
                "examples": [
                    {"spanish": "Az állam a Ménesi úton impozáns épületet emeltetett a Collegium számára.", "english": "The state had an imposing building erected on Ménesi Road for the Collegium."},
                    {"spanish": "A szemináriumokon eredeti forrásokat fordíttattak le a hallgatókkal.", "english": "In the seminars, they had the students translate original sources."},
                    {"spanish": "A közösség a legjobb mesterekkel taníttatja a vidéki tehetségeket.", "english": "The community has rural talents taught by the best masters."}
                ],
                "tip": "Compare 'Eötvös Loránd megalapította a Collegiumot' (he personally founded it as minister) with 'Az állam új épületet emeltetett' (the state commissioned architects and builders to erect the building)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "pairs": [
                        ["bentlakásos", "residential / boarding"],
                        ["érdemelvű", "meritocratic"],
                        ["tehetséggondozás", "talent nurturing"],
                        ["műhelymunka", "seminar / workshop work"],
                        ["szellemi tőke", "intellectual capital"],
                        ["elefántcsonttorony", "ivory tower"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "question": "Melyik nyugat-európai intézmény mintájára hozta létre Eötvös Loránd 1895-ben az Eötvös József Collegiumot?",
                    "options": [
                        "A párizsi École Normale Supérieure mintájára.",
                        "A londoni Királyi Zeneakadémia mintájára.",
                        "A bécsi katonai kadétiskola mintájára."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "sentence": "Az Eötvös Collegiumban az _____ kiválasztás érvényesült: a felvételin nem a családi vagyon, hanem a tudás számított.",
                    "answer": "érdemelvű",
                    "english": "Meritocratic selection prevailed at the Eötvös Collegium: at admission, knowledge counted rather than family wealth."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-causative-agents"],
                    "question": "Which sentence expresses 'The professors had the students translate original historical sources'?",
                    "options": [
                        "A professzorok eredeti történeti forrásokat fordíttattak le a hallgatókkal.",
                        "A professzorok eredeti történeti forrásokat fordítottak le a hallgatóknak.",
                        "A hallgatók a professzorokkal fordítottak le eredeti forrásokat.",
                        "A professzorok lefordították a hallgatókat a forrásokkal."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "sentence": "A kultuszminisztérium a budai Ménesi úton modern épületet _____ a bentlakásos kollégium számára. (emel - 3rd sg. indef. past causative)",
                    "answer": "emeltetett",
                    "english": "The Ministry of Culture had a modern building erected on Ménesi Road in Buda for the residential college."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "tiles": ["A", "professzorok", "eredeti", "forrásokat", "fordíttattak", "le", "a", "diákokkal."],
                    "solution": ["A", "professzorok", "eredeti", "forrásokat", "fordíttattak", "le", "a", "diákokkal."],
                    "english": "The professors had the students translate original sources."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-causative-agents"],
                    "prompt": [
                        {"speaker": "Oktatáskutató", "text": "Hogyan hatott az Eötvös Collegium a vidéki gimnáziumok szakmai színvonalára?"},
                        {"speaker": "Történész", "text": "_____"}
                    ],
                    "options": [
                        "A minisztérium a végzett kollégistákat az ország különböző gimnáziumaiba helyeztette, így a kritikai szellem mindenütt elterjedt.",
                        "A kollégisták egész életükben elzárkóztak a Ménesi úti elefántcsonttoronyba.",
                        "Bezáratták az összes vidéki középiskolát, hogy mindenki Párizsban tanuljon."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen feltételeket biztosított a Collegium a szegény sorsú, de kiemelkedő tehetségű hallgatóknak?",
                    "options": [
                        "Teljes ellátást, lakhatást és Európa egyik leggazdagabb szakkönyvtárát, hogy kizárólag a tudománynak élhessenek.",
                        "Magas tandíjat kellett fizetniük, amelyet gyári munkával törlesztettek.",
                        "Csak levelező tagozaton vehettek részt a szemináriumokon."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Denominational, State, and Alternative Schools",
            "grammar_label": "Permissive vs. coercive causatives (hagy, enged vs. -tat/-tet, kényszerít)",
            "goals": [
                "I can trace the historical shifts of Hungarian church, state, and alternative schools from Pannonhalma and Sárospatak through 1948 nationalization to 1989.",
                "I can contrast coercive/directive causatives (-tat/-tet) with permissive constructions (hagyja / engedi, hogy...).",
                "I can use precise vocabulary related to educational governance and autonomy."
            ],
            "story_segment": {
                "seg_slug": "iskolatipusok",
                "title": "Pannonhalmától az alternatív műhelyekig",
                "summary": "For centuries, Benedictine, Piarist, Reformed, and Lutheran schools formed the backbone of Hungarian education; nationalized in 1948, they were reborn alongside alternative schools around 1989.",
                "location": "Pannonhalma, Sárospatak, Debrecen és Budapest",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar oktatástörténet gerincét évszázadokon át az egyházi iskolák alkották: a ezeréves pannonhalmi bencés gimnázium, a piaristák városi iskolái, valamint a sárospataki és debreceni református kollégiumok. Ezek az intézmények nemcsak klasszikus nyelvi műveltséget adtak, hanem önképzőköröket működtettek, ahol a tanárok hagyták, hogy a diákok saját irodalmi folyóiratokat szerkesszenek és szabadon vitázzanak."
                    },
                    {
                        "type": "narration",
                        "text": "1948 nyarán azonban gyökeres fordulat következett be: a kommunista hatalom államosíttatta a felekezeti iskolák túlnyomó többségét, a szerzetesrendeket pedig néhány kivétellel feloszlatta. Az új oktatáspolitika egységes ideológiai keretet kényszerített az iskolákra, és központi tankönyveket íratott minden tantárgyhoz."
                    },
                    {
                        "type": "narration",
                        "text": "Még a legnehezebb évtizedekben is maradtak azonban szellemi szigetek: a pannonhalmi, győri, kecskeméti és budapesti piarista vagy ferences gimnáziumok — szigorú állami kvóták mellett — megőrizhették működésüket. Eközben az állami gimnáziumokban, például a budapesti Fazekas Mihály Gimnázium speciális matematikai osztályaiban, kiváló pedagógusok teremtettek szabad gondolkodású műhelyeket."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1980-as évek végén, a rendszerváltás hajnalán új pedagógiai mozgalom bontakozott ki: Horn György és társai megalapították az Alternatív Közgazdasági Gimnáziumot (AKG), miközben a Waldorf- és Montessori-iskolák is megjelentek. Ezek a műhelyek szakítottak a poroszoktól örökölt frontális oktatással, és engedték, hogy a tanulók egyéni tanulási utakat válasszanak."
                    },
                    {
                        "type": "narration",
                        "text": "1990 után az egyházak visszakapták egykori történelmi épületeiket, így a mai magyar középiskolai palettán az állami, a felekezeti és az alapítványi alternatív gimnáziumok egymással versengve és egymást gazdagítva működnek."
                    }
                ]
            },
            "words": [
                {"lemma": "államosíttat", "translation": "to have nationalized / order the nationalization of", "pos": "verb"},
                {"lemma": "önképzőkör", "translation": "student literary and debating society", "pos": "noun"},
                {"lemma": "szerzetesrend", "translation": "monastic / religious order", "pos": "noun"},
                {"lemma": "frontális oktatás", "translation": "frontal / lecture-style teaching", "pos": "expression"},
                {"lemma": "alapítványi", "translation": "foundation-run / charter", "pos": "adjective"},
                {"lemma": "pedagógiai autonómia", "translation": "pedagogical autonomy", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "permissive-vs-coercive-causatives",
                "title": "Directive Causatives (-tat/-tet) vs. Permissive Constructions (hagy, enged)",
                "text1_title": "Distinguishing Order/Commission from Permission",
                "text1": "In Hungarian, morphological causatives with -tat/-tet usually express directive or commissioning agency ('ordered / commissioned / caused someone to do X': 'központi tankönyveket íratott', 'államosíttatta az iskolákat'), though in special contexts they can mean 'let oneself be X-ed'. To clearly express pedagogical freedom and permission ('let / allow students to do X'), B2 writers prefer 'hagyja / engedi, hogy + subjunctive' or 'hagy + infinitive'.",
                "text2_title": "Syntactic Patterns with hagy and enged",
                "text2": "Compare the two structures: 1) With a finite clause: 'A tanárok hagyták, hogy a diákok szabadon vitázzanak' (The teachers let the students debate freely). 2) With an infinitive: 'A tanárok szabadon vitázni hagyták a diákokat' (The teachers let the students debate freely). Contrasting directive -tat/-tet with permissive hagy/enged is ideal for comparing authoritarian and student-centered schooling.",
                "table_title": "Directive Causative (-tat/-tet) vs. Permissive (hagy / enged)",
                "table_rows": [
                    ["A minisztérium központi tankönyveket íratott. (Directive)", "A tanárok hagyták, hogy a diákok folyóiratot szerkesszenek. (Permissive)"],
                    ["A hatalom államosíttatta az egyházi iskolákat. (Directive)", "Az alternatív iskola engedi, hogy a diák egyéni utat válasszon. (Permissive)"],
                    ["A tanár bemagoltatta a szabályokat. (Directive)", "A mentor szabadon kísérletezni hagyta a tanulókat. (Permissive)"]
                ],
                "examples": [
                    {"spanish": "1948-ban a hatalom államosíttatta a felekezeti iskolák túlnyomó többségét.", "english": "In 1948, the authorities had the vast majority of denominational schools nationalized."},
                    {"spanish": "Az önképzőkörökben a tanárok hagyták, hogy a diákok saját folyóiratot szerkesszenek.", "english": "In the student societies, the teachers let the students edit their own journal."},
                    {"spanish": "Az alternatív műhelyek engedték, hogy a tanulók egyéni tanulási utakat válasszanak.", "english": "The alternative workshops allowed learners to choose individual learning paths."}
                ],
                "tip": "When contrasting two educational philosophies in an essay, pair an institutional causative ('központi tananyagot íratott elő') with a permissive subjunctive clause ('míg az alternatív iskola engedte, hogy a diákok maguk válasszanak témát')."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "pairs": [
                        ["államosíttat", "to have nationalized"],
                        ["önképzőkör", "student literary & debating society"],
                        ["szerzetesrend", "monastic / religious order"],
                        ["frontális oktatás", "lecture-style frontal teaching"],
                        ["alapítványi", "foundation-run"],
                        ["pedagógiai autonómia", "pedagogical autonomy"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "question": "Mi történt 1948-ban a magyarországi felekezeti gimnáziumok túlnyomó többségével?",
                    "options": [
                        "A kommunista hatalom államosíttatta őket, és egységes központi tankönyveket íratott.",
                        "Mindegyiket átalakították alapítványi Waldorf-iskolává.",
                        "Valamennyi iskola Bécsbe és Párizsba költözött."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "sentence": "A sárospataki és debreceni kollégiumokban működő _____ lehetőséget adott a diákoknak az irodalmi vitákra.",
                    "answer": "önképzőkör",
                    "english": "The student debating society operating in the colleges of Sárospatak and Debrecen gave students the opportunity for literary debates."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-causative-agents"],
                    "question": "Which sentence contrasts a directive causative (-tat/-tet) with a permissive structure (hagy/enged)?",
                    "options": [
                        "Míg a minisztérium egységes tankönyveket íratott, az alternatív iskola engedte, hogy a diákok szabadon kutassanak.",
                        "A minisztérium egységes tankönyveket írt, és a diákok szabadon kutattak.",
                        "A tanárok tankönyveket olvastak, mert a diákok az iskolában tanultak.",
                        "Az iskola épülete szép volt, ezért sok diák jelentkezett."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "sentence": "Az új oktatási vezetés minden tantárgyhoz központi tankönyveket _____ a szakértőkkel. (ír - 3rd sg. indef. past causative)",
                    "answer": "íratott",
                    "english": "The new educational leadership had the experts write centralized textbooks for every subject."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "tiles": ["A", "tanárok", "hagyták,", "hogy", "a", "diákok", "saját", "folyóiratot", "szerkesszenek."],
                    "solution": ["A", "tanárok", "hagyták,", "hogy", "a", "diákok", "saját", "folyóiratot", "szerkesszenek."],
                    "english": "The teachers let the students edit their own journal."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-causative-agents"],
                    "prompt": [
                        {"speaker": "Szülő", "text": "Miben különbözött az 1980-as évek végén alapított Alternatív Közgazdasági Gimnázium a hagyományos porosz oktatástól?"},
                        {"speaker": "Igazgató", "text": "_____"}
                    ],
                    "options": [
                        "Nem kényszerített mindenkire frontális oktatást, hanem engedte, hogy a diákok egyéni tanulási utakat válasszanak.",
                        "Minden órán kétszer annyi évszámot magoltatott be a tanulókkal, mint az állami iskolák.",
                        "Államosíttatta az összes pannonhalmi és sárospataki könyvtárat."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik budapesti állami gimnázium vált híressé a huszadik század második felében a speciális matematikai tagozatáról?",
                    "options": [
                        "A Fazekas Mihály Gimnázium.",
                        "A Nemzeti Színház Színésziskolája.",
                        "A lipcsei gyakorlóiskola."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Modern Debates: Excellence vs. Equal Opportunity",
            "grammar_label": "Passive/reflexive readings of causative verbs (felvételiztet, vizsgáztat, versenyeztet)",
            "goals": [
                "I can analyze contemporary Hungarian debates around six- and eight-year gimnáziumok, academic olympiads, and equal opportunity.",
                "I can use institutional examination and competition causatives (vizsgáztat, versenyeztet, felvételiztet) fluently.",
                "I can formulate nuanced B2 arguments balancing elite talent incubation with social equity."
            ],
            "story_segment": {
                "seg_slug": "eselyegyenloseg",
                "title": "Kiválóság és esélyegyenlőség mérlegén",
                "summary": "Today's Hungarian school system wrestles with a classic dilemma: how to preserve world-beating mathematical and scientific talent incubation while ensuring equal educational opportunity for rural and disadvantaged children.",
                "location": "Budapest és a magyar vidék (21. század)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A mai magyar közoktatás egyik legélénkebb szakmai vitája körülbelül ugyanazt a kérdést járja körül, amely már Eötvös Lorándot is foglalkoztatta: miként lehet egyszerre megőrizni a csúcsteljesítményre képes elitgimnáziumok hagyományát és biztosítani a társadalmi esélyegyenlőséget minden gyermek számára?"
                    },
                    {
                        "type": "narration",
                        "text": "Az 1990-es évektől újra megjelentek a hat- és nyolcosztályos gimnáziumok, amelyek már tíz- vagy tizenkét éves korban központi írásbelivel és szóbelivel felvételiztetik a diákokat. A legnépszerűbb fővárosi és megyeszékhelyi gimnáziumok sokszor négyszeres-ötszörös túljelentkezés mellett válogathatnak, és tanáraik nemzetközi diákolimpiákra készíttetik fel a legtehetségesebb fiatalokat."
                    },
                    {
                        "type": "narration",
                        "text": "Az oktatásszociológusok ugyanakkor arra figyelmeztetnek, hogy a korai szelekció gyakran a tehetősebb, diplomás családok gyermekeinek kedvez, akik magántanárokkal készíttethetik fel a gyerekeiket a felvételire. Ha a legmotiváltabb tanulókat már tízévesen elszívják az általános iskolákból, a hátrányos helyzetű kistelepülések iskoláiban még nehezebbé válik a felzárkóztatás."
                    },
                    {
                        "type": "narration",
                        "text": "Erre a kihívásra válaszolnak az olyan kezdeményezések és szakkollégiumi hálózatok, amelyek ösztöndíjakkal és hétvégi tehetségműhelyekkel támogatják a falusi diákokat. Ezek a programok egyetemi hallgatókkal mentoráltatják a tehetséges vidéki általános iskolásokat, hogy a lakóhely ne dönthesse el előre senkinek a sorsát."
                    },
                    {
                        "type": "narration",
                        "text": "Rátz László, Kármán Mór és Eötvös Loránd öröksége ma is arra emlékeztet: a magyar iskola igazi titka soha nem a puszta privilégium volt, hanem az a pedagógiai elhivatottság, amely minden társadalmi rétegben képes felfedezni és kibontakoztatni a szellemi tehetséget."
                    }
                ]
            },
            "words": [
                {"lemma": "esélyegyenlőség", "translation": "equal opportunity", "pos": "noun"},
                {"lemma": "felvételiztet", "translation": "to administer entrance exams to / examine applicants", "pos": "verb"},
                {"lemma": "korai szelekció", "translation": "early academic tracking / selection", "pos": "expression"},
                {"lemma": "túljelentkezés", "translation": "oversubscription (of applicants)", "pos": "noun"},
                {"lemma": "felzárkóztatás", "translation": "remedial support / catching up / inclusion", "pos": "noun"},
                {"lemma": "diákolimpia", "translation": "international student science olympiad", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "examination-competition-causatives",
                "title": "Lexicalized School & Examination Causatives (vizsgáztat, versenyeztet, felvételiztet)",
                "text1_title": "Specialized Educational Causatives",
                "text1": "Hungarian educational discourse relies heavily on specialized causative verbs derived from intransitive student activities: vizsgázik ('takes an exam') → vizsgáztat ('examines / gives an exam to'), felvételizik ('takes an entrance exam') → felvételiztet ('runs entrance exams for'), versenyez ('competes') → versenyeztet ('enters students in competitions'), felzárkózik ('catches up') → felzárkóztat ('provides remedial support to').",
                "text2_title": "Combining Direct Objects and Mentors",
                "text2": "Because vizsgázik and versenyez are intransitive, the examined or competing students stand in the accusative (-t): 'A gimnázium tízéves korban felvételizteti a gyerekeket.' Meanwhile, with transitive phrasal verbs like felkészít valakit valamire ('prepares someone for something'), adding -tet introduces a commissioned tutor in -val/-vel: 'A szülők magántanárokkal készíttetik fel a gyerekeiket a felvételire.'",
                "table_title": "Student Action (Intransitive) vs. Institutional Action (Causative)",
                "table_rows": [
                    ["A diákok tízévesen felvételiznek.", "A nyolcosztályos gimnázium tízévesen felvételizteti a diákokat."],
                    ["A tanulók diákolimpián versenyeznek.", "A szakkör vezetője diákolimpián versenyezteti a tanulókat."],
                    ["A hátrányos helyzetű diákok felzárkóznak.", "A mentorprogram felzárkóztatja a hátrányos helyzetű diákokat."],
                    ["A magántanár felkészíti a gyereket.", "A szülők magántanárral készíttetik fel a gyereket."]
                ],
                "examples": [
                    {"spanish": "A nyolcosztályos gimnáziumok már tízéves korban felvételiztetik a diákokat.", "english": "Eight-year secondary schools administer entrance exams to students as early as age ten."},
                    {"spanish": "Sok család magántanárokkal készítteti fel a gyerekeit a központi írásbelire.", "english": "Many families have their children prepared for the central written exam by private tutors."},
                    {"spanish": "A program egyetemi hallgatókkal mentoráltatja a tehetséges vidéki diákokat.", "english": "The program has university students mentor talented rural pupils."}
                ],
                "tip": "Notice the noun derivatives formed with -ás/-és from these causatives: felzárkóztatás ('remedial inclusion'), tehetséggondozás, versenyeztetés ('entering students into competitions')."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "pairs": [
                        ["esélyegyenlőség", "equal opportunity"],
                        ["felvételiztet", "to administer entrance exams to"],
                        ["korai szelekció", "early academic selection"],
                        ["túljelentkezés", "oversubscription of applicants"],
                        ["felzárkóztatás", "remedial catching-up support"],
                        ["diákolimpia", "student science olympiad"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "question": "Milyen veszélyre hívják fel a figyelmet az oktatásszociológusok a hat- és nyolcosztályos gimnáziumok kapcsán?",
                    "options": [
                        "A korai szelekció növelheti a társadalmi egyenlőtlenségeket, mert a tehetősebb családok magántanárokkal készíttethetik fel a gyerekeiket.",
                        "Hogy a diákok túl kevés matematikát tanulnak a diákolimpiákra való felkészülés közben.",
                        "Hogy egyetlen diák sem jelentkezik többé fővárosi gimnáziumokba."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-gimnaziumok-vocab"],
                    "sentence": "A legnépszerűbb gimnáziumokban gyakori az ötszörös _____, ezért a központi írásbeli minden pontja számít.",
                    "answer": "túljelentkezés",
                    "english": "Fivefold oversubscription is common in the most popular secondary schools, so every point on the central written exam counts."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-causative-agents"],
                    "question": "Choose the correct causative form to complete: 'A szülők tapasztalt magántanárral _____ fel a gyereket a felvételire.'",
                    "options": ["készíttették", "készítették", "készültek", "készíttetett"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "sentence": "A nyolcosztályos gimnáziumok már a negyedik általános iskolai év végén _____ a jelentkező tanulókat. (felvételizik - 3rd pl. def. pres. causative)",
                    "answer": "felvételiztetik",
                    "english": "Eight-year secondary schools administer entrance exams to applying pupils as early as the end of fourth grade."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-causative-agents"],
                    "tiles": ["A", "program", "egyetemi", "hallgatókkal", "mentoráltatja", "a", "vidéki", "diákokat."],
                    "solution": ["A", "program", "egyetemi", "hallgatókkal", "mentoráltatja", "a", "vidéki", "diákokat."],
                    "english": "The program has university students mentor rural pupils."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-causative-agents"],
                    "prompt": [
                        {"speaker": "Szociológus", "text": "Hogyan lehetne egyszerre megőrizni a tehetséggondozás magas színvonalát és javítani az esélyegyenlőséget?"},
                        {"speaker": "Pedagógus", "text": "_____"}
                    ],
                    "options": [
                        "Úgy, ha a kistelepüléseken élő tehetségeket ösztöndíjas műhelyekben mentoráltatjuk és felzárkóztatjuk, mint egykor az Eötvös Collegium tette.",
                        "Úgy, ha betiltjuk az összes nemzetközi matematikai diákolimpiát.",
                        "Úgy, ha minden szülővel kötelezően magántanárt fizettetünk."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen segítséget nyújtanak a modern tehetséggondozó és szakkollégiumi programok a falusi diákoknak?",
                    "options": [
                        "Ösztöndíjakkal, hétvégi műhelyekkel és egyetemi hallgatók által végzett mentorálással támogatják őket.",
                        "Felmentik őket az érettségi vizsga letétele alól.",
                        "Kizárólag sportversenyeken versenyeztetik őket."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can explain the historical role of the Fasori Gimnázium, the Minta Gimnázium, and the Eötvös Collegium in Hungarian scientific and cultural achievements.",
            "I can derive causative verbs with -at/-et and -tat/-tet and accurately assign -t or -val/-vel to the intermediate agent.",
            "I can contrast directive causatives (-tat/-tet) with permissive constructions (hagy, enged).",
            "I can use 30 B2 educational and academic heritage terms in speech and writing."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-gimnaziumok-vocab"],
                "pairs": [
                    ["katedra", "teacher's dais / desk"],
                    ["gyakorlóiskola", "teacher-training school"],
                    ["érdemelvű", "meritocratic"],
                    ["önképzőkör", "student literary society"],
                    ["esélyegyenlőség", "equal opportunity"],
                    ["túljelentkezés", "oversubscription"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-causative-agents"],
                "question": "In the sentence 'Rátz tanár úr a diákokkal vezettette le az új tételt', why is 'a diákokkal' in the instrumental case (-val/-vel)?",
                "options": [
                    "Because 'levezet' is a transitive verb with its own direct object ('az új tételt'), so the causee takes -val/-vel.",
                    "Because 'diákok' is the direct object of the base verb.",
                    "Because every plural noun in Hungarian takes -val/-vel in the past tense.",
                    "Because 'levezet' means 'to accompany someone by bus'."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-gimnaziumok-vocab"],
                "question": "Melyik intézményt alapította Eötvös Loránd 1895-ben a párizsi École Normale Supérieure mintájára?",
                "options": [
                    "Az Eötvös József Collegiumot a budai Ménesi úton.",
                    "A Fasori Evangélikus Gimnáziumot.",
                    "Az Alternatív Közgazdasági Gimnáziumot.",
                    "A sárospataki református kollégiumot."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-gimnaziumok-vocab"],
                "sentence": "Kármán Mór a Trefort utcai Minta Gimnáziumban a leendő pedagógusokat, vagyis a _____ készítette fel a hivatásukra.",
                "answer": "tanárjelölteket",
                "english": "At the Minta Gimnázium on Trefort Street, Mór Kármán prepared future educators, that is, the trainee teachers, for their profession."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-causative-agents"],
                "sentence": "Neumann János édesapja egyetemi professzorokkal _____ a rendkívül tehetséges fiút. (tanít - 3rd sg. def. past causative)",
                "answer": "taníttatta",
                "english": "John von Neumann's father had the extraordinarily talented boy taught by university professors."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-causative-agents"],
                "sentence": "A professzorok a szemináriumokon eredeti görög és latin forrásokat _____ le a kollégistákkal. (fordít - 3rd pl. indef. past causative)",
                "answer": "fordíttattak",
                "english": "In the seminars, the professors had the Collegium students translate original Greek and Latin sources."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-causative-agents"],
                "prompt": [
                    {"speaker": "Tanfelügyelő", "text": "Hogyan zajlik a szakmai felkészítés a Trefort utcai gyakorlóiskolában?"},
                    {"speaker": "Vezetőtanár", "text": "_____"}
                ],
                "options": [
                    "A tanárjelölteket azonnal a katedrára állítjuk, majd az óra után közösen elemeztetjük velük a tapasztalatokat.",
                    "Csak elméleti könyveket másoltatunk a tanárjelöltektől.",
                    "Nem engedjük, hogy a tanárjelöltek bejöjjenek az épületbe."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-causative-agents"],
                "question": "Which sentence accurately uses an intransitive-based causative where the students take the accusative (-t)?",
                "options": [
                    "A fizikatanár rendszeresen kísérleteztette és vitatkoztatta a diákokat az órán.",
                    "A fizikatanár rendszeresen kísérleteztette a diákokkal az órát.",
                    "A diákok kísérleteztették a fizikatanárral a padokat.",
                    "A fizikatanár kísérletezett a diákokkal a felvételire."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-causative-agents"],
                "prompt": [
                    {"speaker": "Újságíró", "text": "Miért bírálják sokan a tízéves korban tartott központi gimnáziumi felvételiket?"},
                    {"speaker": "Oktatáskutató", "text": "_____"}
                ],
                "options": [
                    "Mert a tehetősebb családok drága magántanárokkal készíttetik fel a gyerekeiket, ami rontja az esélyegyenlőséget.",
                    "Mert a gimnáziumok nem felvételiztetik a jelentkezőket.",
                    "Mert a diákolimpiákon tilos matematikából versenyezni."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-causative-agents"],
                "tiles": ["A", "szülők", "magántanárral", "készíttették", "fel", "a", "fiukat", "a", "vizsgára."],
                "solution": ["A", "szülők", "magántanárral", "készíttették", "fel", "a", "fiukat", "a", "vizsgára."],
                "english": "The parents had their son prepared for the exam by a private tutor."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-causative-agents"],
                "tiles": ["Az", "állam", "új", "épületet", "emeltetett", "a", "Ménesi", "úton."],
                "solution": ["Az", "állam", "új", "épületet", "emeltetett", "a", "Ménesi", "úton."],
                "english": "The state had a new building erected on Ménesi Road."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-causative-agents"],
                "template": [
                    {
                        "prompt": "Write a sentence explaining how László Rátz taught theorems in class (use 'levezettet' + 'a diákokkal').",
                        "answer": "Rátz László nem magoltatta be a képleteket, hanem a diákokkal vezettette le az új tételeket a táblánál."
                    },
                    {
                        "prompt": "Write a sentence describing how modern mentoring programs support talented rural pupils (use 'mentoráltat' + 'egyetemi hallgatókkal').",
                        "answer": "A tehetséggondozó program egyetemi hallgatókkal mentoráltatja a hátrányos helyzetű vidéki diákokat."
                    }
                ]
            }
        ]
    }
}


UNIT_11_PSZICHOANALIZIS = {
    "unit_num": 11,
    "slug": "pszichoanalizis",
    "title": "The Budapest School of Psychoanalysis & the Mind",
    "grammar_skill": "b2-reflexive-middle",
    "vocab_skill": "b2-pszichoanalizis-vocab",
    "theme": "The Budapest School of Psychoanalysis and Flow psychology",
    "location": "Budapest, Bécs, London és Chicago",
    "intro_body": [
        "In 1918, Sigmund Freud declared that Budapest was poised to become the European capital of psychoanalysis. At the center of this intellectual movement stood Sándor Ferenczi, a physician and thinker whose warm, empathetic clinical style—developed in constant conversation with the writers of the literary journal Nyugat in Budapest's cafés—gave birth to the internationally influential 'Budapest School' of psychoanalysis.",
        "In this unit, you will follow the journey of Hungarian psychology from Ferenczi's circle and his literary patients (Kosztolányi, Karinthy, Géza Csáth, Attila József), through Michael Balint's transformation of the doctor-patient relationship in London and the underground survival of psychoanalysis during state socialism, to Mihály Csíkszentmihályi's world-famous theory of 'Flow' (optimal experience). Grammatically, you will master reflexive and middle-voice verb derivations (-kodik/-kedik/-ködik, inchoative -ul/-ül vs. transitive -ít) and psychological verb-case government."
    ],
    "combined_story_title": "A díványtól a flow-élményig: Ferenczi és a budapesti iskola",
    "combined_story_summary": "How Sándor Ferenczi made Budapest a European center of psychoanalysis in dialogue with modernist poets, and how Hungarian psychologists from Michael Balint to Mihály Csíkszentmihályi transformed our understanding of empathy and optimal human experience.",
    "lessons": [
        {
            "num": 1,
            "title": "Sándor Ferenczi and Freud's 'Capital of Psychoanalysis'",
            "grammar_label": "Inchoative/middle -ul/-ül vs. causative/transitive -ít in psychological processes",
            "goals": [
                "I can explain how Sándor Ferenczi founded the Hungarian Psychoanalytical Society in 1913 and made Budapest a hub of depth psychology.",
                "I can distinguish between spontaneous/internal psychological changes (-ul/-ül, -ódik/-ődik) and externally triggered actions (-ít, -ol/-el).",
                "I can use B2 psychoanalytical and clinical vocabulary accurately."
            ],
            "story_segment": {
                "seg_slug": "ferenczisandor",
                "title": "Ferenczi Sándor és a lélek fővárosa",
                "summary": "Meeting Sigmund Freud in 1908, Budapest neurologist Sándor Ferenczi founded the Hungarian Psychoanalytical Society in 1913 and hosted the landmark 1918 International Congress in Budapest.",
                "location": "Budapest és Bécs (1908–1919)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Amikor Ferenczi Sándor budapesti idegorvos 1908-ban először találkozott Sigmund Freuddal Bécsben, olyan szellemi barátság és alkotói szövetség vette kezdetét, amely negyed századon át több mint ezerkétszáz levélben örökítődött meg. Ferenczi nem elégedett meg azzal, hogy lefordítsa Freud műveit, hanem 1913-ban megalapította a Magyarországi Pszichoanalitikai Egyesületet."
                    },
                    {
                        "type": "narration",
                        "text": "Míg Bécsben a pszichoanalízis sokáig az orvosi egyetem falain kívülre szorult, Budapesten a tudományos, irodalmi és társadalomtudományi értelmiség azonnal nyitottan fordult az új lélektan felé. Az emberek kíváncsian figyelték, hogyan tárulnak fel az álmokban, elszólásokban és elfojtott emlékekben a tudattalan folyamatok."
                    },
                    {
                        "type": "narration",
                        "text": "Az első világháború utolsó hónapjaiban, 1918 szeptemberében a Magyar Tudományos Akadémia dísztermében rendezték meg az ötödik Nemzetközi Pszichoanalitikai Kongresszust, ahol Ferenczit a nemzetközi egyesület elnökévé választották. A háborús sebesültek lelki sebeit vizsgálva világossá vált, hogy a súlyos megrázkódtatás nem idegi gyengeségből fakad, hanem a feldolgozatlan traumából."
                    },
                    {
                        "type": "narration",
                        "text": "1919 tavaszán a budapesti egyetemen a világon elsőként Ferenczi Sándor kapott önálló pszichoanalitikai tanszéket. Bár a történelmi viharok néhány hónap múlva elsodorták a katedráját, és sok tanítványa emigrációba kényszerült, a budapesti műhely szellemisége már nem semmisülhetett meg."
                    },
                    {
                        "type": "narration",
                        "text": "Ferenczi megfigyelte, hogy a páciens állapota csak akkor javul tartósan, ha a rendelőben a hűvös távolságtartás helyett őszinte emberi bizalom alakul ki. Ez a felismerés alapozta meg a világhírű budapesti pszichoanalitikai iskolát."
                    }
                ]
            },
            "words": [
                {"lemma": "tudattalan", "translation": "the unconscious (mind)", "pos": "noun"},
                {"lemma": "elfojtás", "translation": "repression (psychological)", "pos": "noun"},
                {"lemma": "feltárul", "translation": "to be revealed / to unfold / to open up", "pos": "verb"},
                {"lemma": "elszólás", "translation": "slip of the tongue (Freudian slip)", "pos": "noun"},
                {"lemma": "mélylélektan", "translation": "depth psychology", "pos": "noun"},
                {"lemma": "megrázkódtatás", "translation": "shock / emotional trauma / upheaval", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "inchoative-middle-vs-transitive",
                "title": "Middle & Inchoative Verbs (-ul/-ül, -ódik/-ődik) vs. Transitive Verbs (-ít)",
                "text1_title": "Spontaneous Inner Processes vs. External Interventions",
                "text1": "Psychological prose in Hungarian relies heavily on paired verb suffixes that distinguish whether a process unfolds internally inside the subject (-ul/-ül or -ódik/-ődik, middle/inchoative voice, conjugation in -ik) or is actively carried out by an external agent (-ít or transitive stem). Compare: feltár ('uncovers/reveals something') vs. feltárul ('opens up / reveals itself'); kialakít ('shapes/forms something') vs. kialakul ('develops/takes shape'); feldolgoz ('processes something') vs. feldolgozódik ('gets processed').",
                "text2_title": "Using -ul/-ül and -ódik/-ődik in Academic Register",
                "text2": "In B2 psychological descriptions, -ul/-ül and -ódik/-ődik allow you to describe mental transformations without clumsy passive constructions: 'Az álmokban feltárulnak a tudattalan vágyak' (In dreams, unconscious desires are revealed / unfold); 'A rendelőben őszinte bizalom alakul ki' (Sincere trust develops in the consulting room); 'A barátság több mint ezer levélben örökítődött meg' (The friendship was immortalized in over a thousand letters).",
                "table_title": "Transitive Action (-ít / active) vs. Middle/Inchoative Process (-ul/-ül, -ódik/-ődik)",
                "table_rows": [
                    ["Az orvos feltárja az elfojtott emléket.", "Az álomban feltárul az elfojtott emlék."],
                    ["A terapeuta bizalmat alakít ki.", "A beszélgetés során őszinte bizalom alakul ki."],
                    ["A kezelés javítja a páciens állapotát.", "A páciens állapota fokozatosan javul."],
                    ["A levelek megörökítették a barátságot.", "A barátság ezer levélben örökítődött meg."]
                ],
                "examples": [
                    {"spanish": "Az álmokban és elszólásokban feltárulnak a tudattalan folyamatok.", "english": "Unconscious processes are revealed in dreams and slips of the tongue."},
                    {"spanish": "A páciens állapota csak akkor javul, ha őszinte bizalom alakul ki.", "english": "The patient's condition improves only if sincere trust develops."},
                    {"spanish": "A két tudós barátsága több mint ezerkétszáz levélben örökítődött meg.", "english": "The two scientists' friendship was immortalized in more than twelve hundred letters."}
                ],
                "tip": "Whenever you want to translate English 'is revealed', 'develops', 'is restored' (helyreáll / megújul), or 'gets resolved' (megoldódik) in psychological writing, check whether the -ul/-ül or -ódik/-ődik partner of the verb exists!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "pairs": [
                        ["tudattalan", "the unconscious"],
                        ["elfojtás", "psychological repression"],
                        ["feltárul", "to unfold / be revealed"],
                        ["elszólás", "slip of the tongue"],
                        ["mélylélektan", "depth psychology"],
                        ["megrázkódtatás", "emotional shock / trauma"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "question": "Milyen világtörténelmi jelentőségű esemény történt 1919 tavaszán a budapesti egyetemen Ferenczi Sándor kinevezésével?",
                    "options": [
                        "A világon elsőként Budapesten jött létre önálló egyetemi pszichoanalitikai tanszék.",
                        "Ferenczi bezáratta az összes neurológiai klinikát Európában.",
                        "A Magyar Tudományos Akadémia betiltotta az álmok vizsgálatát."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "sentence": "A véletlennek tűnő _____ és az álomképek mögött gyakran elfojtott vágyak vagy félelmek húzódnak meg.",
                    "answer": "elszólások",
                    "english": "Behind seemingly accidental slips of the tongue and dream images, repressed desires or fears often lie hidden."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-reflexive-middle"],
                    "question": "Which verb form is needed when 'őszinte bizalom' (sincere trust) is the subject that develops spontaneously: 'A rendelőben őszinte bizalom _____ ki'?",
                    "options": ["alakul", "alakít", "alakítja", "alakulja"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "sentence": "A szabad asszociáció során fokozatosan _____ fel a gyermekkori emlékek. (feltárul - 3rd pl. pres.)",
                    "answer": "tárulnak",
                    "english": "During free association, childhood memories gradually unfold / are revealed."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "tiles": ["A", "terápia", "során", "őszinte", "emberi", "bizalom", "alakult", "ki."],
                    "solution": ["A", "terápia", "során", "őszinte", "emberi", "bizalom", "alakult", "ki."],
                    "english": "Sincere human trust developed during the therapy."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-reflexive-middle"],
                    "prompt": [
                        {"speaker": "Orvostanhallgató", "text": "Miben tért el a budapesti fogadtatás a bécsi akadémiai közegtől az 1910-es években?"},
                        {"speaker": "Pszichológus", "text": "_____"}
                    ],
                    "options": [
                        "Míg Bécsben az egyetem falain kívülre szorult az irányzat, Budapesten az írók és tudósok azonnal nyitottan fordultak a mélylélektan felé.",
                        "Budapesten senki sem olvasta Ferenczi Sándor és Freud levelezését.",
                        "Bécsben minden költő kötelezően pszichoanalitikusnak tanult."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit állapított meg Ferenczi Sándor a háborús sebesültek lelki állapotát vizsgálva 1918-ban?",
                    "options": [
                        "Azt, hogy a tünetek nem jellemgyengeségből, hanem a feldolgozatlan háborús megrázkódtatásból (traumából) fakadnak.",
                        "Azt, hogy a háborús sebesülteknek nincs szükségük semmiféle beszélgetésre.",
                        "Azt, hogy az álmoknak semmi közük a tudattalanhoz."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "When Poets Met Analysts in Café Ignotus",
            "grammar_label": "Reflexive and behavioral verbs in -kodik/-kedik/-ködik and -kozik/-kezik/-közik",
            "goals": [
                "I can describe the unique alliance between Sándor Ferenczi and the modernist writers of Nyugat (Ignotus, Kosztolányi, Karinthy, Csáth, Attila József).",
                "I can use reflexive and behavioral verbs in -kodik/-kedik/-ködik and -kozik/-kezik/-közik (önmarcangol, szembenéz, megnyílik, foglalkozik).",
                "I can analyze literary self-reflection and psychological portraiture in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "koltokesanalitikusok",
                "title": "Költők a díványon és a kávéházi törzsasztalnál",
                "summary": "Unlike anywhere else in Europe, Budapest's modernist poets—Kosztolányi, Karinthy, Csáth, and Attila József—shared café tables with Ferenczi, weaving psychoanalysis directly into modern Hungarian literature.",
                "location": "Budapest, New York és Centrál kávéház (1910–1937)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Európában szinte egyedülálló módon Budapesten a pszichoanalízis nem zárt orvosi rendelőben született meg, hanem a New York és a Centrál kávéház márványasztalainál, a Nyugat folyóirat íróinak társaságában. Ignotus, a Nyugat főszerkesztője maga is alapító tagja volt a Magyarországi Pszichoanalitikai Egyesületnek, Ferenczi Sándor pedig minden héten együtt vacsorázott Kosztolányi Dezsővel és Karinthy Frigyessel."
                    },
                    {
                        "type": "narration",
                        "text": "Az írók nemcsak intellektuális divatból érdeklődtek a lélektan iránt, hanem saját alkotói válságaikkal és szorongásaikkal is bátran szembenéztek. Kosztolányi unokatestvére, az orvos és novellista Csáth Géza már 1909-ben naplószerű esettanulmányban örökítette meg egy páciense tudattalan világát, Kosztolányi pedig az Édes Anna és a Pacsirta című regényeiben az elfojtott érzelmek mesteri ábrázolására vállalkozott."
                    },
                    {
                        "type": "narration",
                        "text": "A harmincas években József Attila, a huszadik századi magyar líra egyik legnagyobb alakja maga is analízisbe járt, és fájdalmas őszinteséggel vallott gyermekkori elhagyatottságáról. A Szabad-ötletek jegyzéke című megrázó dokumentumban és kései verseiben a költő kíméletlenül megnyilatkozott saját belső démonairól."
                    },
                    {
                        "type": "narration",
                        "text": "A kávéházi beszélgetések során az analitikusok is rengeteget tanultak a költőktől: felismerték, hogy a metafora, a humor és a nyelvi játék éppen olyan kaput nyit a tudattalanhoz, mint az álomfejtés. Amikor Karinthy Frigyes paródiáiban a lélekbúvárokon élcelődött, valójában a legmélyebb önismereti kérdésekkel foglalkozott."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a termékeny egymásra hatás tette a huszadik század eleji magyar irodalmat olyan kivételesen érzékennyé a lélek rezdüléseire: Budapesten a költészet és a pszichoanalízis közös nyelven beszélt."
                    }
                ]
            },
            "words": [
                {"lemma": "esettanulmány", "translation": "case study", "pos": "noun"},
                {"lemma": "álomfejtés", "translation": "dream interpretation", "pos": "noun"},
                {"lemma": "önismeret", "translation": "self-knowledge / self-awareness", "pos": "noun"},
                {"lemma": "szorongás", "translation": "anxiety / anguish", "pos": "noun"},
                {"lemma": "megnyilatkozik", "translation": "to express oneself / manifest / open up", "pos": "verb"},
                {"lemma": "szembenéz", "translation": "to face / confront (with -val/-vel)", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "reflexive-behavioral-verbs",
                "title": "Reflexive & Behavioral Verbs (-kozik/-kezik/-közik, -kodik/-kedik/-ködik)",
                "text1_title": "True Reflexives and Self-Directed Actions (-kozik/-kezik/-közik)",
                "text1": "Many Hungarian verbs ending in -kozik/-kezik/-közik express actions directed back at or emerging from the self: bemutatkozik ('introduces oneself'), megnyilatkozik ('reveals oneself / speaks out'), vállalkozik valamire ('undertakes / commits oneself to something'), foglalkozik valamivel ('engages with / deals with something'), emlékezik valamire ('remembers / reflects on something'). All of these belong to the -ik conjugation.",
                "text2_title": "Behavioral Verbs Derived from Nouns and Adjectives (-kodik/-kedik/-ködik)",
                "text2": "The suffix -kodik/-kedik/-ködik (and -skodik/-skedik) turns a noun or adjective into 'behaves as / acts in the manner of': barát ('friend') → barátkozik, kritikus → kritizál / akadékoskodik, titok ('secret') → titkolózik, élcelődik ('banters / pokes fun at, with -on/-en/-ön'). Notice that these psychological and behavioral verbs govern specific oblique cases rather than a direct object (-t)!",
                "table_title": "Key Psychological & Behavioral Verbs and Their Case Government",
                "table_rows": [
                    ["foglalkozik + -val/-vel", "A költők mélyen foglalkoztak az önismereti kérdésekkel."],
                    ["szembenéz + -val/-vel", "Az írók bátran szembenéztek a saját szorongásaikkal."],
                    ["vállalkozik + -ra/-re", "Kosztolányi az elfojtott érzelmek ábrázolására vállalkozott."],
                    ["megnyilatkozik + -ról/-ről / -ban/-ben", "József Attila őszintén megnyilatkozott a belső válságáról."]
                ],
                "examples": [
                    {"spanish": "Az írók saját alkotói válságaikkal és szorongásaikkal is bátran szembenéztek.", "english": "The writers bravely confronted their own creative crises and anxieties as well."},
                    {"spanish": "Kosztolányi az elfojtott érzelmek mesteri ábrázolására vállalkozott.", "english": "Kosztolányi undertook the masterful depiction of repressed emotions."},
                    {"spanish": "Karinthy a legmélyebb önismereti kérdésekkel foglalkozott.", "english": "Karinthy engaged with the deepest questions of self-knowledge."}
                ],
                "tip": "Never use an accusative (-t) object with foglalkozik, szembenéz, or vállalkozik: always pair foglalkozik and szembenéz with -val/-vel, and vállalkozik with -ra/-re!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "pairs": [
                        ["esettanulmány", "case study"],
                        ["álomfejtés", "dream interpretation"],
                        ["önismeret", "self-knowledge"],
                        ["szorongás", "anxiety"],
                        ["megnyilatkozik", "to open up / express oneself"],
                        ["szembenéz", "to confront / face"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "question": "Melyik irodalmi folyóirat írói körével ápolt szoros baráti és szakmai kapcsolatot Ferenczi Sándor a pesti kávéházakban?",
                    "options": [
                        "A Nyugat folyóirat íróival, köztük Ignotusszal, Kosztolányi Dezsővel és Karinthy Frigyessel.",
                        "A tizenkilencedik századi bécsi udvari krónikásokkal.",
                        "Kizárólag a párizsi szürrealista festőkkel."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "sentence": "Csáth Géza orvosként és íróként már 1909-ben részletes _____ írt egy páciense lelki világáról.",
                    "answer": "esettanulmányt",
                    "english": "As a physician and writer, Géza Csáth wrote a detailed case study about a patient's inner world as early as 1909."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-reflexive-middle"],
                    "question": "Which case suffix is required by the reflexive verb 'vállalkozik' in: 'Kosztolányi az elfojtott érzelmek ábrázolásá_____ vállalkozott'?",
                    "options": ["-ra (ábrázolására)", "-t (ábrázolását)", "-val (ábrázolásával)", "-tól (ábrázolásától)"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "sentence": "A modern magyar írók nem menekültek el a kételyeik elől, hanem bátran _____ a saját szorongásaikkal. (szembenéz - 3rd pl. past)",
                    "answer": "szembenéztek",
                    "english": "Modern Hungarian writers did not flee from their doubts, but bravely confronted their own anxieties."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "tiles": ["Karinthy", "a", "legmélyebb", "önismereti", "kérdésekkel", "foglalkozott."],
                    "solution": ["Karinthy", "a", "legmélyebb", "önismereti", "kérdésekkel", "foglalkozott."],
                    "english": "Karinthy dealt with the deepest questions of self-knowledge."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-reflexive-middle"],
                    "prompt": [
                        {"speaker": "Irodalomtörténész", "text": "Hogyan hatott a pszichoanalízis Kosztolányi Dezső és József Attila művészetére?"},
                        {"speaker": "Kritikus", "text": "_____"}
                    ],
                    "options": [
                        "Kosztolányi regényeiben az elfojtott érzelmek ábrázolására vállalkozott, József Attila pedig verseiben a gyermekkori traumáival nézett szembe.",
                        "Mindketten felhagytak az írással, és kizárólag neurológiai tankönyveket fordítottak.",
                        "Elutasították az önismeretet, és soha nem jártak pesti kávéházakba."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit tanultak a budapesti pszichoanalitikusok a költőkkel folytatott kávéházi beszélgetések során?",
                    "options": [
                        "Azt, hogy a metafora, a humor és a nyelvi játék éppen olyan kaput nyit a tudattalanhoz, mint az álomfejtés.",
                        "Azt, hogy a költészet veszélyes a mentális egészségre.",
                        "Azt, hogy a páciensekkel tilos magyarul beszélni."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "Trauma, Empathy, and the Doctor-Patient Relationship",
            "grammar_label": "Reciprocal constructions (egymásra hangolódik) and psychological case frames",
            "goals": [
                "I can explain how Ferenczi's trauma theory and Michael Balint's (Bálint Mihály) 'Balint groups' revolutionized clinical medicine.",
                "I can use reciprocal expressions (egymásra hangolódik, egymáshoz viszonyul) and empathy-related case frames (belehelyezkedik valamibe, együttérez valakivel).",
                "I can discuss the doctor-patient relationship and infant attachment in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "balintmihaly",
                "title": "Bálint Mihály és az orvos mint gyógyszer",
                "summary": "Building on Ferenczi's relational sensitivity, Alice and Michael Balint (alongside Imre Hermann and René Spitz) studied early mother-child attachment and created London's 'Balint groups' for doctors worldwide.",
                "location": "Budapest és London (1930–1960-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A budapesti pszichoanalitikai iskola legfontosabb újítása az volt, hogy a korai anya-gyermek kapcsolatot és az empátiát állította a gyógyítás középpontjába. Hermann Imre a megkapaszkodási ösztönt vizsgálta, Bálint Mihály és felesége, Bálint Alice pedig kimutatták, hogy a csecsemő nem elszigetelt lényként születik a világra, hanem kezdettől fogva érzelmi viszonyban áll az édesanyjával."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor a harmincas évek végén a fasizmus térnyerése miatt Bálint Mihály Nagy-Britanniába emigrált, magával vitte Ferenczi Sándor szellemi örökségét a londoni Tavistock Klinikára. Ott figyelte meg, hogy a háziorvosokhoz forduló betegek panaszai mögött milyen gyakran húzódik meg magány, veszteség vagy kimondatlan lelki konfliktus."
                    },
                    {
                        "type": "narration",
                        "text": "1957-ben megjelent Az orvos, a betege és a betegség című világhírű könyve, amelyben Bálint megfogalmazta híres tételét: a gyógyításban a leggyakrabban felírt „gyógyszer” maga az orvos. Nemcsak az számít ugyanis, milyen tablettát ad a doktor, hanem az is, hogyan viszonyul a szenvedő emberhez, és mennyire képes belehelyezkedni a beteg helyzetébe."
                    },
                    {
                        "type": "narration",
                        "text": "Ennek fejlesztésére hozta létre a ma már világszerte működő Bálint-csoportokat, ahol orvosok és terapeuták rendszeresen összegyűlnek, hogy egy-egy nehéz esetet megbeszélve megértsék saját érzelmi reakcióikat. A csoporttagok egymásra hangolódva tanulják meg, hogyan hallgassák meg a pácienst ítélkezés nélkül."
                    },
                    {
                        "type": "narration",
                        "text": "Ferenczi Sándortól és Bálint Mihálytól a modern kötődéselméletig egyenes út vezetett: a budapesti iskola bebizonyította, hogy a gyógyulás mindig két ember kölcsönös, empatikus kapcsolatában születik meg."
                    }
                ]
            },
            "words": [
                {"lemma": "kötődés", "translation": "attachment / emotional bond", "pos": "noun"},
                {"lemma": "belehelyezkedik", "translation": "to put oneself into (another's position, with -ba/-be)", "pos": "verb"},
                {"lemma": "ráhangolódik", "translation": "to attune oneself to (with -ra/-re)", "pos": "verb"},
                {"lemma": "viszonyul", "translation": "to relate to / have an attitude toward (with -hoz/-hez/-höz)", "pos": "verb"},
                {"lemma": "anya-gyermek kapcsolat", "translation": "mother-child relationship", "pos": "expression"},
                {"lemma": "háziorvos", "translation": "general practitioner (GP) / family doctor", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "relational-psychological-verbs",
                "title": "Relational & Empathy Verbs: Specific Case Government and Reciprocity",
                "text1_title": "Directional Cases with Psychological Verbs",
                "text1": "Notice how Hungarian relational verbs encode emotional movement through specific spatial case suffixes: belehelyezkedik a beteg helyzetébe ('puts oneself INTO the patient's situation', illative -ba/-be); ráhangolódik a másik emberre ('attunes oneself ONTO the other person', sublative -ra/-re); viszonyul a pácienshez ('relates TO the patient', allative -hoz/-hez/-höz); együttérez a szenvedővel ('empathizes WITH the sufferer', instrumental -val/-vel).",
                "text2_title": "Reciprocal Pronouns (egymás-) with Middle Verbs",
                "text2": "To express mutual emotional attunement in group therapy or relationships, attach the appropriate case suffix required by the verb directly to the reciprocal pronoun egymás ('each other'): egymásra hangolódnak ('they attune to one another'), egymáshoz viszonyulnak ('they relate to one another'), egymásban bíznak ('they trust in one another').",
                "table_title": "Relational Verb + Required Case Suffix",
                "table_rows": [
                    ["belehelyezkedik + -ba/-be", "Az orvos belehelyezkedik a beteg helyzetébe."],
                    ["ráhangolódik + -ra/-re", "A csoporttagok egymásra hangolódnak a beszélgetésben."],
                    ["viszonyul + -hoz/-hez/-höz", "Fontos, hogyan viszonyul a doktor a szenvedő emberhez."],
                    ["kötődik + -hoz/-hez/-höz", "A csecsemő kezdettől fogva erősen kötődik az édesanyjához."]
                ],
                "examples": [
                    {"spanish": "Nem mindegy, hogyan viszonyul az orvos a szenvedő emberhez.", "english": "It matters greatly how the physician relates to the suffering person."},
                    {"spanish": "A jó terapeuta képes belehelyezkedni a páciens helyzetébe.", "english": "A good therapist is able to put themselves into the patient's position."},
                    {"spanish": "A Bálint-csoportban a résztvevők egymásra hangolódva elemzik az eseteket.", "english": "In the Balint group, participants analyze the cases while attuning to one another."}
                ],
                "tip": "Whenever a Hungarian verb has a directional prefix like bele-, rá-, or hozzá-, the noun it governs almost always echoes that prefix's case suffix: belehelyezkedik a helyzetbe (-ba/-be), ráhangolódik a beteggel → a betegre (-ra/-re)!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "pairs": [
                        ["kötődés", "emotional attachment / bond"],
                        ["belehelyezkedik", "to put oneself into (a situation)"],
                        ["ráhangolódik", "to attune oneself to"],
                        ["viszonyul", "to relate to"],
                        ["anya-gyermek kapcsolat", "mother-child relationship"],
                        ["háziorvos", "general practitioner (GP)"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "question": "Mi volt Bálint Mihály híres tétele Az orvos, a betege és a betegség című könyvében?",
                    "options": [
                        "Az, hogy a gyógyításban a leggyakrabban felírt „gyógyszer” maga az orvos és az ő empatikus viszonyulása.",
                        "Az, hogy a háziorvosoknak soha nem szabad beszélgetniük a betegekkel.",
                        "Az, hogy a csecsemőknek nincs szükségük anyai kötődésre."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "sentence": "A Bálint-csoportok eredetileg londoni _____ számára jöttek létre, hogy megértsék a rendelőkben zajló lelki folyamatokat.",
                    "answer": "háziorvosok",
                    "english": "Balint groups were originally created for London general practitioners so they could understand the psychological processes taking place in their clinics."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-reflexive-middle"],
                    "question": "Which case suffix echoes the prefix 'bele-' in: 'A jó orvos képes belehelyezkedni a páciens _____'?",
                    "options": ["helyzetébe (-ba/-be)", "helyzetére (-ra/-re)", "helyzetétől (-tól/-től)", "helyzetét (-t)"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "sentence": "A gyógyulás sikere azon is múlik, hogyan _____ a terapeuta a hozzá forduló emberhez. (viszonyul - 3rd sg. pres.)",
                    "answer": "viszonyul",
                    "english": "The success of healing also depends on how the therapist relates to the person turning to them."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "tiles": ["Az", "orvosnak", "képesnek", "kell", "lennie", "belehelyezkedni", "a", "beteg", "helyzetébe."],
                    "solution": ["Az", "orvosnak", "képesnek", "kell", "lennie", "belehelyezkedni", "a", "beteg", "helyzetébe."],
                    "english": "The doctor must be able to put themselves into the patient's position."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-reflexive-middle"],
                    "prompt": [
                        {"speaker": "Klinikai szakpszichológus", "text": "Mi történik egy Bálint-csoport ülésén, amikor az orvosok egy nehéz esetet vitatnak meg?"},
                        {"speaker": "Háziorvos", "text": "_____"}
                    ],
                    "options": [
                        "A résztvevők egymásra hangolódva vizsgálják meg, hogyan viszonyultak a beteghez, és milyen érzelmeket váltott ki belőlük a találkozás.",
                        "Csak gyógyszerkémiai képleteket írnak fel egymásnak a táblára.",
                        "Megtiltják, hogy az orvos belehelyezkedjen a páciens helyzetébe."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit mutattak ki a budapesti iskola kutatói — Hermann Imre, Bálint Mihály és Bálint Alice — a csecsemőkorról?",
                    "options": [
                        "Azt, hogy a csecsemő nem elszigetelt lényként születik, hanem kezdettől fogva elemi kötődésben és érzelmi viszonyban él az édesanyjával.",
                        "Azt, hogy az érzelmi kötődés csak tizennyolc éves kor után alakul ki.",
                        "Azt, hogy a csecsemők nem érzékelik a környezetüket."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Suppression and Rebirth After 1989",
            "grammar_label": "Passive-like middle verbs (-ódik/-ődik) in historical and institutional contexts",
            "goals": [
                "I can explain how psychoanalysis was banned as 'bourgeois pseudoscience' in 1949, survived in private apartments around Imre Hermann, and was rehabilitated in the 1980s–1990s.",
                "I can use middle/mediopassive verbs in -ódik/-ődik (kiszorul, feloszlik, újjászerveződik, megőrződik) to narrate institutional history.",
                "I can discuss child psychology (Lucy Liebermann, Lilly Hajdu, György Vikár) and professional continuity."
            ],
            "story_segment": {
                "seg_slug": "ujjaszuletes1989",
                "title": "A lakásszemináriumoktól az újjászületésig",
                "summary": "Dissolved in 1949 under Stalinism, the Budapest psychoanalytical tradition survived through Imre Hermann's apartment seminars and child clinics before experiencing a dramatic renaissance around 1989.",
                "location": "Budapest (1949–1993)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A második világháború pusztítása után a budapesti pszichoanalitikus közösség alig kezdhette meg az újjáépítést, amikor 1949 elején újabb csapás érte: a sztálinista kultúrpolitika „polgári áltudománynak” minősítette a pszichoanalízist. Az egyesület feloszlott, a folyóiratokat betiltották, a mélylélektan pedig évtizedekre kiszorult az egyetemi katedrákról."
                    },
                    {
                        "type": "narration",
                        "text": "A hagyomány mégsem szakadt meg teljesen, mert a mesterek és tanítványok közötti élő kapcsolat a magánlakások csendjében megőrződött. Hermann Imre budai lakásán esténként fiatal orvosok és pszichológusok — köztük Vikár György és Nemes Lívia — gyűltek össze, ahol titkos szemináriumokon és kiképző analízisekben adódott tovább Ferenczi Sándor szellemi öröksége."
                    },
                    {
                        "type": "narration",
                        "text": "A hivatalos egészségügyben a gyermekpszichológiai és nevelési tanácsadók jelentettek menedéket: Liebermann Lucy és kortársai a gyermekek beszédzavarainak és szorongásainak gyógyítása közben a legkorszerűbb dinamikus szemléletet alkalmazták. A szakmai tudás így a tilalom évei alatt is folyamatosan gazdagodott."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1970-es és 1980-as években a politikai enyhüléssel párhuzamosan a pszichoanalízis fokozatosan visszakapcsolódott a nemzetközi vérkeringésbe. 1989-ben hivatalosan is újjászerveződött a Magyar Pszichoanalitikai Egyesület, majd 1993-ban — Ferenczi Sándor születésének százhuszadik évfordulóján — ismét nemzetközi konferenciák és egyetemi képzések nyíltak meg Budapesten."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor a londoni és amerikai emigrációból hazalátogató kutatók találkoztak a hazai tanítványokkal, megdöbbenve tapasztalták, hogy a lakásszemináriumokban megőrzött budapesti iskola szellemisége semmit sem veszített az erejéből."
                    }
                ]
            },
            "words": [
                {"lemma": "áltudomány", "translation": "pseudoscience", "pos": "noun"},
                {"lemma": "újjászerveződik", "translation": "to be reorganized / reconstitute itself", "pos": "verb"},
                {"lemma": "megőrződik", "translation": "to be preserved / survive intact", "pos": "verb"},
                {"lemma": "kiszorul", "translation": "to be pushed out / marginalized (from, with -ból/-ből / -ról/-ről)", "pos": "verb"},
                {"lemma": "nevelési tanácsadó", "translation": "child guidance / educational counseling clinic", "pos": "expression"},
                {"lemma": "hagyományőrzés", "translation": "preservation of tradition", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "mediopassive-institutional-verbs",
                "title": "Mediopassive Verbs in -ódik/-ődik for Institutional & Historical Processes",
                "text1_title": "Why Hungarian Prefers -ódik/-ődik to the Periphrastic Passive",
                "text1": "Unlike English or German, modern Hungarian rarely uses a 'to be + participle' passive for ongoing historical processes. Instead, B2 academic prose uses mediopassive verbs formed with -ódik (back vowel) and -ődik (front vowel) alongside -ul/-ül: megőrződik ('is preserved'), továbbadódik ('is passed down'), újjászerveződik ('is reorganized'), visszakapcsolódik ('reconnects / is reintegrated'), kiszorul ('is squeezed out').",
                "text2_title": "Pairing Separable Prefixes with -ódik/-ődik",
                "text2": "Notice how verbal prefixes combine seamlessly with -ódik/-ődik and split when focused or negated: 'A hagyomány a magánlakásokban őrződött meg' (focus on 'in private apartments'); '1989-ben hivatalosan is újjászerveződött az egyesület' (prefix stays attached when neutral).",
                "table_title": "Active Transitive vs. Mediopassive (-ódik/-ődik)",
                "table_rows": [
                    ["A tanítványok megőrizték a hagyományt.", "A hagyomány a magánlakásokban őrződött meg."],
                    ["A mesterek továbbadták a tudást.", "A tudás titkos szemináriumokon adódott tovább."],
                    ["1989-ben újjászervezték az egyesületet.", "1989-ben újjászerveződött az egyesület."],
                    ["A szakemberek visszakapcsolták az országot a hálózatba.", "A szakma visszakapcsolódott a nemzetközi vérkeringésbe."]
                ],
                "examples": [
                    {"spanish": "A mesterek és tanítványok közötti kapcsolat a magánlakásokban megőrződött.", "english": "The bond between masters and disciples was preserved in private apartments."},
                    {"spanish": "Titkos szemináriumokon adódott tovább Ferenczi Sándor szellemi öröksége.", "english": "Sándor Ferenczi's intellectual heritage was passed on in secret seminars."},
                    {"spanish": "1989-ben hivatalosan is újjászerveződött a Magyar Pszichoanalitikai Egyesület.", "english": "In 1989, the Hungarian Psychoanalytical Society was officially reorganized."}
                ],
                "tip": "When focusing the place or manner before a prefixed -ódik/-ődik verb, remember to split the prefix behind the verb: 'A tudás titkos szemináriumokon adódott tovább' (not *továbbadódott*)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "pairs": [
                        ["áltudomány", "pseudoscience"],
                        ["újjászerveződik", "to be reorganized"],
                        ["megőrződik", "to be preserved"],
                        ["kiszorul", "to be pushed out / marginalized"],
                        ["nevelési tanácsadó", "child guidance clinic"],
                        ["hagyományőrzés", "preservation of tradition"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "question": "Hogyan maradt fenn a budapesti pszichoanalitikai hagyomány az 1949-es betiltás után?",
                    "options": [
                        "Hermann Imre és társai magánlakásokban tartott szemináriumokon és gyermekpszichológiai rendelőkben adták tovább a tudást.",
                        "Az állampárt kötelező tantárggyá tette a mélylélektant minden gyárban.",
                        "Teljesen feledésbe merült, és 1989-ig senki sem hallott Ferenczi Sándorról."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "sentence": "1949-ben a hivatalos ideológia polgári _____ bélyegezte a pszichoanalízist, ezért az egyesület feloszlott.",
                    "answer": "áltudománynak",
                    "english": "In 1949, official ideology branded psychoanalysis a bourgeois pseudoscience, so the society dissolved."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-reflexive-middle"],
                    "question": "Which mediopassive (-ódik/-ődik) form correctly completes: 'A rendszerváltás idején hivatalosan is _____ a Magyar Pszichoanalitikai Egyesület'?",
                    "options": ["újjászerveződött", "újjászervezte", "újjászervezett", "újjászerveződni"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "sentence": "A szellemi örökség a lakásszemináriumok csendjében nemzedékről nemzedékre _____ tovább. (továbbadódik - 3rd sg. past, split prefix)",
                    "answer": "adódott",
                    "english": "In the quiet of apartment seminars, the intellectual heritage was passed down from generation to generation."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "tiles": ["A", "szakma", "fokozatosan", "visszakapcsolódott", "a", "nemzetközi", "vérkeringésbe."],
                    "solution": ["A", "szakma", "fokozatosan", "visszakapcsolódott", "a", "nemzetközi", "vérkeringésbe."],
                    "english": "The profession gradually reconnected to the international mainstream."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-reflexive-middle"],
                    "prompt": [
                        {"speaker": "Történész", "text": "Milyen szerepet játszottak a gyermekpszichológiai és nevelési tanácsadók a tilalom évtizedeiben?"},
                        {"speaker": "Pszichiáter", "text": "_____"}
                    ],
                    "options": [
                        "Menedéket nyújtottak a szakembereknek, így a dinamikus szemlélet a gyermekek gyógyítása közben sértetlenül megőrződött.",
                        "Bezárták az összes óvodát, hogy senki se tanulhasson pszichológiát.",
                        "Csak felnőtt páciensek álomfejtésével foglalkoztak az egyetemeken."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen évfordulót ünnepelt a nemzetközi pszichoanalitikai közösség Budapesten 1993-ban?",
                    "options": [
                        "Ferenczi Sándor születésének százhuszadik évfordulóját.",
                        "A Nemzeti Színház megnyitásának századik évfordulóját.",
                        "A Rubik-kocka feltalálásának ötvenedik évfordulóját."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Csíkszentmihályi and the Psychology of Optimal Experience",
            "grammar_label": "Complete synthesis of middle/reflexive verbs (belefeledkezik, elmélyül, kiteljesedik)",
            "goals": [
                "I can explain Mihály Csíkszentmihályi's concept of 'Flow' (áramlatélmény) and positive psychology.",
                "I can use absorption and self-actualization verbs (belefeledkezik valamibe, elmélyül valamiben, kiteljesedik) accurately.",
                "I can synthesize the trajectory of Hungarian psychology from repairing trauma to cultivating human flourishing."
            ],
            "story_segment": {
                "seg_slug": "flowelmeny",
                "title": "Csíkszentmihályi Mihály és az áramlatélmény",
                "summary": "Studying painters, chess players, and surgeons in Chicago, Hungarian-born psychologist Mihály Csíkszentmihályi discovered 'Flow'—the state of complete absorption where skill and challenge meet.",
                "location": "Fiume, Budapest és Chicago (1960–2000-es évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Míg a huszadik század első felének pszichológiája elsősorban a lelki sebek, a szorongás és a trauma gyógyítására összpontosított, a Fiuméban született magyar pszichológus, Csíkszentmihályi Mihály egy látszólag egyszerű, mégis forradalmi kérdést tett fel: mi teszi az emberi életet igazán örömtelivé és értelmessé?"
                    },
                    {
                        "type": "narration",
                        "text": "A Chicagói Egyetem professzoraként Csíkszentmihályi festőművészeket, zeneszerzőket, sakkozókat, sebészeket és hegymászókat figyelt meg munka közben. Észrevette, hogy amikor egy alkotó teljesen belefeledkezik a tevékenységébe, megszűnik számára az időérzék, a külső zajok elhalványulnak, és az ember szinte eggyé válik azzal, amit csinál."
                    },
                    {
                        "type": "narration",
                        "text": "Ezt a tudatállapotot nevezte el „flow”-nak, magyarul áramlatélménynek, mert az interjúalanyok úgy írták le, mintha egy sodró vízfolyás vinné őket előre erőlködés nélkül. A kutatások igazolták, hogy a flow akkor jön létre, amikor a feladat nehézsége és az egyén felkészültsége magas szinten egyensúlyba kerül: ha a kihívás túl kicsi, unalomba süppedünk, ha túl nagy, eluralkodik rajtunk a szorongás."
                    },
                    {
                        "type": "narration",
                        "text": "Csíkszentmihályi elmélete az 1990-ben megjelent Flow — Az áramlat című könyve után az egész világon, így Magyarországon is a pozitív pszichológia alapkövévé vált. Pedagógusok, zenetanárok és munkahelyi vezetők egyaránt felismerték, hogy az ember akkor teljesedik ki, ha értelmes célokért küzdve elmélyülhet a feladataiban."
                    },
                    {
                        "type": "narration",
                        "text": "A budapesti pszichoanalitikai iskola és a flow-pszichológia így egészíti ki egymást: Ferenczi és Bálint megtanították, hogyan gyógyulnak be a lélek sebei az empatikus kapcsolatban, Csíkszentmihályi pedig megmutatta, hogyan bontakozik ki a szabad, alkotó emberi tudat."
                    }
                ]
            },
            "words": [
                {"lemma": "áramlatélmény", "translation": "flow experience (optimal experience)", "pos": "noun"},
                {"lemma": "belefeledkezik", "translation": "to lose oneself in / become absorbed in (with -ba/-be)", "pos": "verb"},
                {"lemma": "kiteljesedik", "translation": "to fulfill oneself / blossom / reach full potential", "pos": "verb"},
                {"lemma": "elmélyül", "translation": "to immerse oneself in / deepen (with -ban/-ben)", "pos": "verb"},
                {"lemma": "időérzék", "translation": "sense of time", "pos": "noun"},
                {"lemma": "eluralkodik", "translation": "to take hold / overcome (with -on/-en/-ön)", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "absorption-flourishing-verbs",
                "title": "Verbs of Absorption, Immersion, and Self-Actualization",
                "text1_title": "Contrast Between Illative (-ba/-be) and Inessive (-ban/-ben) Absorption",
                "text1": "When describing mental focus in B2 Hungarian, pay close attention to the prefix-case harmony of two key verbs: 1) belefeledkezik a munkába ('loses oneself INTO the work', illative -ba/-be echoing bele-); 2) elmélyül a feladatban ('immerses oneself IN the task', inessive -ban/-ben). Meanwhile, eluralkodik ('takes control over / overwhelms') takes the superessive (-on/-en/-ön): 'Eluralkodik rajtunk a szorongás' (Anxiety takes hold over us).",
                "text2_title": "Inchoative Verbs in -edik/-odik for Personal Growth",
                "text2": "Adjectives and participles can form middle/inchoative verbs in -edik/-odik meaning 'becomes increasingly X': teljes ('complete') → kiteljesedik ('fulfills oneself / reaches full potential'), gazdag ('rich') → gazdagodik ('becomes richer'). These verbs provide high-register equivalents for English 'flourish' and 'self-actualize'.",
                "table_title": "Absorption & Growth Verbs with Their Case Frames",
                "table_rows": [
                    ["belefeledkezik + -ba/-be", "Az alkotó teljesen belefeledkezik a festésbe."],
                    ["elmélyül + -ban/-ben", "A kutató órákra elmélyül a kísérletben."],
                    ["eluralkodik + -on/-en/-ön", "Túl nehéz feladatnál eluralkodik rajtunk a szorongás."],
                    ["kiteljesedik (intransitive)", "Az ember az alkotó munkában teljesedik ki."]
                ],
                "examples": [
                    {"spanish": "Amikor egy alkotó teljesen belefeledkezik a tevékenységébe, megszűnik számára az időérzék.", "english": "When a creator completely loses themselves in their activity, the sense of time ceases for them."},
                    {"spanish": "Ha a kihívás túl nagy a tudásunkhoz képest, eluralkodik rajtunk a szorongás.", "english": "If the challenge is too great compared to our skill, anxiety takes hold of us."},
                    {"spanish": "Az ember akkor teljesedik ki, ha értelmes célokért küzdve elmélyülhet a munkájában.", "english": "A person reaches full potential when, striving for meaningful goals, they can immerse themselves in their work."}
                ],
                "tip": "Memorize the contrast: belefeledkezik a játékba (-ba/-be: movement into forgetful absorption) vs. elmélyül a gondolataiban (-ban/-ben: deep immersion inside thoughts)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "pairs": [
                        ["áramlatélmény", "flow experience"],
                        ["belefeledkezik", "to lose oneself in"],
                        ["kiteljesedik", "to fulfill one's potential"],
                        ["elmélyül", "to immerse oneself in"],
                        ["időérzék", "sense of time"],
                        ["eluralkodik", "to take hold over / overwhelm"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "question": "Milyen feltétel mellett jön létre Csíkszentmihályi Mihály szerint a flow, vagyis az áramlatélmény?",
                    "options": [
                        "Amikor a feladat jelentette kihívás és az egyén képességei magas szinten egyensúlyba kerülnek.",
                        "Amikor a feladat annyira könnyű, hogy közben unalomba süppedünk.",
                        "Amikor a feladat megoldhatatlanul nehéz, és eluralkodik rajtunk a szorongás."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-pszichoanalizis-vocab"],
                    "sentence": "Az intenzív alkotás pillanataiban teljesen megszűnik az ember _____, és az órák perceknek tűnnek.",
                    "answer": "időérzéke",
                    "english": "In moments of intense creation, a person's sense of time completely ceases, and hours seem like minutes."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-reflexive-middle"],
                    "question": "Which case suffixes correctly complete the pair: 'belefeledkezik a zené_____ és elmélyül a dallamok_____'?",
                    "options": ["-be / -ban (zenébe / dallamokban)", "-ben / -ba (zenében / dallamokba)", "-t / -at (zenét / dallamokat)", "-ről / -tól (zenéről / dallamoktól)"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "sentence": "Ha a követelmény messze meghaladja a felkészültségünket, könnyen _____ rajtunk a bénító szorongás. (eluralkodik - 3rd sg. pres.)",
                    "answer": "eluralkodik",
                    "english": "If the requirement far exceeds our preparedness, paralyzing anxiety easily takes hold of us."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-reflexive-middle"],
                    "tiles": ["A", "festőművész", "teljesen", "belefeledkezett", "az", "alkotó", "munkába."],
                    "solution": ["A", "festőművész", "teljesen", "belefeledkezett", "az", "alkotó", "munkába."],
                    "english": "The painter completely lost himself in the creative work."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-reflexive-middle"],
                    "prompt": [
                        {"speaker": "Zenetanár", "text": "Hogyan tudod alkalmazni Csíkszentmihályi Mihály elméletét a zongoraórákon?"},
                        {"speaker": "Kolléga", "text": "_____"}
                    ],
                    "options": [
                        "Mindig olyan darabot választok, amelyben a kihívás és a diák tudása egyensúlyban van, így a tanuló belefeledkezhet a zenélésbe.",
                        "Olyan nehéz darabot adok az első órán, hogy azonnal eluralkodjon a diákon a szorongás.",
                        "Megtiltom, hogy a növendékek elmélyüljenek a gyakorlásban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen hivatású embereket figyelt meg és kérdezett ki Csíkszentmihályi Mihály a flow-kutatásai során?",
                    "options": [
                        "Festőművészeket, zeneszerzőket, sakkozókat, sebészeket és hegymászókat.",
                        "Kizárólag alvó csecsemőket.",
                        "Csak tizenkilencedik századi vándorszínészeket."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can trace the history of Hungarian psychology from Sándor Ferenczi and the literary cafés of Budapest to Michael Balint and Mihály Csíkszentmihályi.",
            "I can distinguish between transitive (-ít) and inchoative/mediopassive (-ul/-ül, -ódik/-ődik) verbs in psychological prose.",
            "I can use reflexive and relational psychological verbs with their exact directional cases (szembenéz -val, belehelyezkedik -be, ráhangolódik -ra, belefeledkezik -be, elmélyül -ban).",
            "I can employ 30 B2 psychological and mental-health terms accurately."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-pszichoanalizis-vocab"],
                "pairs": [
                    ["tudattalan", "the unconscious"],
                    ["esettanulmány", "case study"],
                    ["kötődés", "emotional attachment"],
                    ["újjászerveződik", "to be reorganized"],
                    ["áramlatélmény", "flow experience"],
                    ["belefeledkezik", "to lose oneself in"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-reflexive-middle"],
                "question": "Which sentence uses the correct middle/inchoative verb form for an internal process ('sincere trust develops')?",
                "options": [
                    "A beszélgetések során őszinte bizalom alakul ki az orvos és a páciens között.",
                    "A beszélgetések során őszinte bizalom alakít ki az orvos és a páciens között.",
                    "Őszinte bizalmat alakulnak ki a rendelőben.",
                    "A páciens bizalommal alakított a rendelőre."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-pszichoanalizis-vocab"],
                "question": "Ki alapította meg 1913-ban a Magyarországi Pszichoanalitikai Egyesületet, és lett 1919-ben a világ első egyetemi pszichoanalitikai professzora?",
                "options": [
                    "Ferenczi Sándor.",
                    "Rátz László.",
                    "Kempelen Farkas.",
                    "Jedlik Ányos."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-pszichoanalizis-vocab"],
                "sentence": "Bálint Mihály londoni munkássága nyomán jöttek létre a háziorvosok önismeretét fejlesztő _____.",
                "answer": "Bálint-csoportok",
                "english": "Following Michael Balint's work in London, the Balint groups that develop general practitioners' self-awareness were established."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-reflexive-middle"],
                "sentence": "A jó terapeuta ítélkezés nélkül figyel, és képes _____ a szenvedő ember helyzetébe. (belehelyezkedik - infinitive)",
                "answer": "belehelyezkedni",
                "english": "A good therapist listens without judgment and is able to put themselves into the suffering person's position."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-reflexive-middle"],
                "sentence": "A tilalom évtizedei alatt a budapesti iskola szellemisége Hermann Imre lakásszemináriumain _____ meg. (megőrződik - 3rd sg. past, split prefix)",
                "answer": "őrződött",
                "english": "During the decades of prohibition, the spirit of the Budapest School was preserved in Imre Hermann's apartment seminars."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-reflexive-middle"],
                "prompt": [
                    {"speaker": "Irodalmár", "text": "Miért volt olyan különleges a pesti kávéházak szerepe a pszichoanalízis történetében?"},
                    {"speaker": "Pszichológus", "text": "_____"}
                ],
                "options": [
                    "Mert a Nyugat költői és az analitikusok egy asztalnál ültek, és együtt foglalkoztak az önismeret és a tudattalan kérdéseivel.",
                    "Mert a kávéházakban betiltották az álomfejtést és a regényírást.",
                    "Mert Ferenczi Sándor csak németül volt hajlandó beszélgetni a pincérekkel."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-reflexive-middle"],
                "question": "Select the sentence where all three psychological verbs govern their correct case suffixes:",
                "options": [
                    "A művész szembenéz a kétségeivel, belefeledkezik a munkába, és elmélyül az alkotásban.",
                    "A művész szembenéz a kétségeit, belefeledkezik a munkában, és elmélyül az alkotásba.",
                    "A művész szembenéz a kétségeire, belefeledkezik a munkától, és elmélyül az alkotással.",
                    "A művész szembenéz a kétségeknek, belefeledkezik a munkát, és elmélyül az alkotáson."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-reflexive-middle"],
                "prompt": [
                    {"speaker": "Hallgató", "text": "Hogyan függ össze a feladat nehézsége a szorongással és a flow-élménnyel Csíkszentmihályi modelljében?"},
                    {"speaker": "Professzor", "text": "_____"}
                ],
                "options": [
                    "Ha a kihívás túl nagy, eluralkodik rajtunk a szorongás, de ha egyensúlyban áll a tudásunkkal, belefeledkezünk a tevékenységbe.",
                    "Minél unalmasabb a feladat, annál könnyebben alakul ki az áramlatélmény.",
                    "A flow csak akkor jön létre, ha egyáltalán nem foglalkozunk a feladattal."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-reflexive-middle"],
                "tiles": ["A", "csoporttagok", "egymásra", "hangolódva", "beszélik", "meg", "az", "eseteket."],
                "solution": ["A", "csoporttagok", "egymásra", "hangolódva", "beszélik", "meg", "az", "eseteket."],
                "english": "Attuning to one another, the group members discuss the cases."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-reflexive-middle"],
                "tiles": ["Az", "ember", "az", "értelmes,", "alkotó", "munkában", "teljesedik", "ki."],
                "solution": ["Az", "ember", "az", "értelmes,", "alkotó", "munkában", "teljesedik", "ki."],
                "english": "A person reaches full potential in meaningful, creative work."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-reflexive-middle"],
                "template": [
                    {
                        "prompt": "Write a sentence explaining how a good physician relates to a patient according to Michael Balint (use 'viszonyul + -hoz/-hez' and 'belehelyezkedik + -ba/-be').",
                        "answer": "A jó orvos empatikusan viszonyul a pácienshez, és képes belehelyezkedni a szenvedő ember helyzetébe."
                    },
                    {
                        "prompt": "Write a sentence describing what happens when an artist enters the state of Flow (use 'belefeledkezik + -ba/-be' and 'megszűnik').",
                        "answer": "Amikor a művész teljesen belefeledkezik az alkotó munkába, megszűnik számára az időérzék."
                    }
                ]
            }
        ]
    }
}


UNIT_12_TALALMANYOK = {
    "unit_num": 12,
    "slug": "talalmanyok",
    "title": "From Kempelen's Chess Turk to Rubik's Cube",
    "grammar_skill": "b2-obligatory-participle",
    "vocab_skill": "b2-talalmanyok-vocab",
    "theme": "Hungarian inventions, engineering and design",
    "location": "Pozsony, Budapest, Buenos Aires és London",
    "intro_body": [
        "From an 18th-century mechanical speaking machine in Pozsony and the world's first closed-core electric transformers in Budapest to the ballpoint pen in your pocket, three-dimensional holography on bank cards, and the Rubik's Cube on your desk, Hungarian inventors have repeatedly reshaped everyday life across the globe.",
        "In this unit, you will explore the engineering breakthroughs of Farkas Kempelen, Ányos Jedlik, the Ganz engineers (Károly Zipernowsky, Miksa Déri, Ottó Bláthy), László Bíró, Dénes Gábor, and Ernő Rubik. Grammatically, you will master the future/obligatory passive participle (-andó/-endő: megoldandó feladat, követendő példa) alongside formal postpositions of technical means and agency (révén, útján, segítségével, köszönhetően)."
    ],
    "combined_story_title": "Gondolatból tárgy: Hét találmány, amely megváltoztatta a hétköznapokat",
    "combined_story_summary": "From Farkas Kempelen's speaking machine and Ányos Jedlik's dynamo to the Ganz transformers, László Bíró's ballpoint pen, Dénes Gábor's holography, and Ernő Rubik's iconic cube.",
    "lessons": [
        {
            "num": 1,
            "title": "Kempelen's Automata and Early Engineering",
            "grammar_label": "Obligatory/future passive participles (-andó/-endő) as prenominal modifiers",
            "goals": [
                "I can describe Farkas Kempelen's Chess-Playing Turk, his acoustic speaking machine, and his hydraulic engineering works.",
                "I can form and use obligatory/future passive participles (-andó/-endő) according to vowel harmony.",
                "I can use B2 historical engineering and mechanical vocabulary accurately."
            ],
            "story_segment": {
                "seg_slug": "kempelenfarkas",
                "title": "Kempelen Farkas sakkozó törökje és beszélőgépe",
                "summary": "In 18th-century Pozsony and Vienna, polymath Farkas Kempelen dazzled Maria Theresa's court with the Chess-Playing Turk while pioneering phonetic speech synthesis with his mechanical speaking machine.",
                "location": "Pozsony és Bécs (1769–1791)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1769-ben Mária Terézia királynő a bécsi udvarban egy francia szemfényvesztő mágneses kísérleteit nézte végig, majd megkérdezte a jelen lévő magyar udvari tanácsost, a pozsonyi születésű Kempelen Farkast, tudna-e ennél is bámulatosabb szerkezetet építeni. Kempelen fél év múlva állított be a palotába a híres sakkozó törökkel: egy életnagyságú, turbános bábúval, amely fogaskerekekkel teli szekrény mögött ülve sorra legyőzte az udvar legjobb sakkozóit."
                    },
                    {
                        "type": "narration",
                        "text": "Bár a sakkozó automata belsejében valójában egy zseniális rejtekhelyen ülő emberi sakkozó irányította a mágneses bábukat, a szerkezet mechanikai megoldásai egész Európát lázba hozták, és később még Napóleonnal is megmérkőztek. Maga Kempelen azonban a törököt csupán szellemes illúziónak tekintette, és figyelme a valódi, tudományosan megoldandó feladatok felé fordult."
                    },
                    {
                        "type": "narration",
                        "text": "Két évtizedes kutatómunkával megalkotta a világ első működő mechanikus beszélőgépét, amely fújtatóval, síppal és bőrből formált hangképző üregekkel utánozta az emberi tüdőt, a hangszálakat és a szájüreget. A szerkezet nem előre rögzített dallamot játszott le, hanem a billentyűk lenyomásával valódi szavakat és mondatokat ejtett ki latinul, franciául és olaszul."
                    },
                    {
                        "type": "narration",
                        "text": "Kempelen a vakon született bécsi énekesnő és zeneszerző, Paradis Mária Terézia számára tapintható domború betűket és kézi sajtót is szerkesztett, miközben a Budai Vár vízellátását biztosító szivattyútelepet és a schönbrunni szökőkutak hidraulikáját tervezte meg. Minden munkájában a gyakorlatban alkalmazandó mérnöki elveket kereste."
                    },
                    {
                        "type": "narration",
                        "text": "1791-ben megjelent, Az emberi beszéd mechanizmusa című könyvével Kempelen Farkas a modern fonetika és a beszédszintézis tudományos alapkövét tette le: a látványos udvari illúzióból így született meg a jövő hangtechnikája."
                    }
                ]
            },
            "words": [
                {"lemma": "fogaskerék", "translation": "cogwheel / gear", "pos": "noun"},
                {"lemma": "fújtató", "translation": "bellows", "pos": "noun"},
                {"lemma": "beszédszintézis", "translation": "speech synthesis", "pos": "noun"},
                {"lemma": "megoldandó", "translation": "to be solved / requiring a solution", "pos": "adjective"},
                {"lemma": "alkalmazandó", "translation": "to be applied / applicable", "pos": "adjective"},
                {"lemma": "szemfényvesztő", "translation": "illusionist / conjurer", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "obligatory-participles-intro",
                "title": "The Obligatory / Future Passive Participle (-andó / -endő)",
                "text1_title": "Forming and Interpreting -andó/-endő",
                "text1": "Alongside the active present participle (-ó/-ő: sakkozó török 'chess-playing Turk') and the past/completed participle (-t/-tt: rögzített dallam 'recorded melody'), Hungarian possesses a third participle exclusively characteristic of B2–C1 formal and technical registers: the obligatory or future passive participle formed with -andó (back-vowel verbs) and -endő (front-vowel verbs). It translates 'to be [verb]ed / that must or will be [verb]ed': megoldandó feladat ('problem to be solved'), követendő példa ('example to be followed'), alkalmazandó elv ('principle to be applied').",
                "text2_title": "Prenominal Position and Prefix Retention",
                "text2": "Like all Hungarian participial modifiers, the -andó/-endő phrase stands strictly BEFORE the noun it modifies, and any verbal prefix stays attached: 'a gyakorlatban alkalmazandó mérnöki elvek' (the engineering principles to be applied in practice); 'a Budai Várba feljuttatandó víz mennyisége' (the amount of water to be pumped up to Buda Castle).",
                "table_title": "The Three Hungarian Participles Compared",
                "table_rows": [
                    ["Present (-ó/-ő): active / ongoing", "a sakkozó automata / a beszélő gép"],
                    ["Past (-t/-tt): completed / passive", "az előre rögzített dallam / a megépített híd"],
                    ["Future/Obligatory (-andó/-endő): to be done", "a tudományosan megoldandó feladat / a követendő példa"],
                    ["Extended -andó/-endő phrase", "a gyakorlatban alkalmazandó mérnöki elvek"]
                ],
                "examples": [
                    {"spanish": "Kempelen figyelme a valódi, tudományosan megoldandó feladatok felé fordult.", "english": "Kempelen's attention turned toward genuine tasks to be solved scientifically."},
                    {"spanish": "Minden munkájában a gyakorlatban alkalmazandó mérnöki elveket kereste.", "english": "In all his work, he sought the engineering principles to be applied in practice."},
                    {"spanish": "A beszélőgépben a kiejtendő hangokat fújtató és bőrüregek formálták meg.", "english": "In the speaking machine, the sounds to be pronounced were shaped by bellows and leather cavities."}
                ],
                "tip": "Notice the vowel harmony: megold → megoldandó, alkalmaz → alkalmazandó, megtart → megtartandó (back vowels) vs. követ → követendő, kiejt → kiejtendő, elvégzendő (front vowels)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "pairs": [
                        ["fogaskerék", "cogwheel / gear"],
                        ["fújtató", "bellows"],
                        ["beszédszintézis", "speech synthesis"],
                        ["megoldandó", "to be solved"],
                        ["alkalmazandó", "to be applied"],
                        ["szemfényvesztő", "illusionist / conjurer"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "question": "Melyik találmányával tette le Kempelen Farkas a modern fonetika és a beszédszintézis tudományos alapjait?",
                    "options": [
                        "A fújtatóval és bőr hangképző üregekkel működő mechanikus beszélőgépével és 1791-es könyvével.",
                        "A golyóstoll kapilláris csatornáinak megtervezésével.",
                        "A váltakozó áramú transzformátor szabadalmaztatásával."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "sentence": "A sakkozó török szekrényében látható _____ csupán a nézők figyelmét terelték el a rejtekhelyről.",
                    "answer": "fogaskerekek",
                    "english": "The cogwheels visible inside the Chess Turk's cabinet merely distracted the spectators' attention from the hiding place."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-obligatory-participle"],
                    "question": "Which obligatory participle (-andó/-endő) correctly translates 'the engineering task to be completed' (from elvégez 'to complete')?",
                    "options": [
                        "az elvégzendő mérnöki feladat",
                        "az elvégzett mérnöki feladat",
                        "az elvégző mérnöki feladat",
                        "az elvégezandó mérnöki feladat"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "sentence": "A mérnökök részletesen kiszámították a Budai Várba _____ víz napi mennyiségét. (feljuttat - obligatory participle)",
                    "answer": "feljuttatandó",
                    "english": "The engineers calculated in detail the daily amount of water to be pumped up to Buda Castle."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "tiles": ["Kempelen", "a", "tudományosan", "megoldandó", "feladatok", "felé", "fordult."],
                    "solution": ["Kempelen", "a", "tudományosan", "megoldandó", "feladatok", "felé", "fordult."],
                    "english": "Kempelen turned toward the tasks to be solved scientifically."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-obligatory-participle"],
                    "prompt": [
                        {"speaker": "Múzeumi kurátor", "text": "Miért tartotta maga Kempelen Farkas sokkal fontosabbnak a beszélőgépet, mint a világhírű sakkozó törököt?"},
                        {"speaker": "Tudománytörténész", "text": "_____"}
                    ],
                    "options": [
                        "Mert a török ügyes illúzió volt, míg a beszélőgép valódi, akusztikailag megoldandó kérdésekre adott tudományos választ.",
                        "Mert a sakkozó török soha egyetlen játszmát sem tudott megnyerni Bécsben.",
                        "Mert Mária Terézia betiltotta a sakkjátékot a palotában."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Hogyan segítette Kempelen Farkas a vakon született bécsi zeneszerzőt, Paradis Mária Teréziát?",
                    "options": [
                        "Tapintható domború betűket és kézi nyomdasajtót szerkesztett a számára.",
                        "Megtanította a sakkozó török belsejében elrejtőzni.",
                        "Folyékony tintával működő golyóstollat ajándékozott neki."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Jedlik, Ganz, and the Electrification of Cities",
            "grammar_label": "Formal postpositions of technical means and agency (révén, útján, segítségével)",
            "goals": [
                "I can explain Ányos Jedlik's dynamo principle and the 1885 ZBD transformer invented by Károly Zipernowsky, Miksa Déri, and Ottó Bláthy at the Ganz Works.",
                "I can use formal postpositions of means (révén, útján, segítségével, által) with possessive or unmarked noun phrases.",
                "I can discuss electrical engineering and industrial patents in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "jedlikganz",
                "title": "A dinamótól a Ganz-transzformátorig",
                "summary": "Benedictine physicist Ányos Jedlik formulated the dynamo principle in the 1850s, and in 1885 the Budapest Ganz engineers Zipernowsky, Déri, and Bláthy invented the closed-core transformer that electrified modern cities.",
                "location": "Győr és Budapest, Ganz-gyár (1828–1885)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar elektrotechnika története egy csendes bencés szerzetes-fizikus, Jedlik Ányos szertárában kezdődött, aki Győrött, Pozsonyban, majd a pesti egyetemen kísérletezett az elektromágnességgel. Jedlik már 1827–1828-ban megépítette a világ első elektromágneses forgonyát, vagyis a villanymotor ősét, majd legalább hat évvel Werner Siemens előtt felismerte és leírta az öngerjesztés elvét, amelynek révén megalkotta az első dinamót."
                    },
                    {
                        "type": "narration",
                        "text": "Míg a szerény bencés tanár eredményei sokáig az egyetemi szertár falai között maradtak, néhány évtizeddel később a budapesti Ganz-gyár villamos osztályán világraszóló ipari áttörés született. Az 1880-as évek elején a legnagyobb megoldandó műszaki probléma az volt, hogyan lehet a villamos energiát nagy távolságra, hatalmas hálózati veszteség nélkül eljuttatni."
                    },
                    {
                        "type": "narration",
                        "text": "Három magyar mérnök — Zipernowsky Károly, Déri Miksa és Bláthy Ottó Titusz — 1885 tavaszán szabadalmaztatta a zárt vasmagú transzformátort, valamint a párhuzamos kapcsolású váltakozó áramú elosztórendszert. Maga a „transzformátor” elnevezés is az ő budapesti szabadalmuk útján terjedt el a világ összes nyelvében."
                    },
                    {
                        "type": "narration",
                        "text": "Az új rendszer segítségével a távoli vízierőművekben megtermelt nagyfeszültségű áramot szinte veszteség nélkül lehetett a városokba vezetni, majd a fogyasztók előtt biztonságos feszültségűre alakítani. A Ganz-mérnökök 1892-ben a Rómától huszonhét kilométerre fekvő Tivoli vízierőmű révén világították ki az olasz fővárost, bebizonyítva a váltakozó áram fölényét."
                    },
                    {
                        "type": "narration",
                        "text": "Kandó Kálmán később ugyanezen a Ganz-hagyományon építkezve valósította meg a vasúti fővonalak váltakozó áramú villamosítását: a pesti gyár rajzasztalain született meg a modern városi energiaellátás gerince."
                    }
                ]
            },
            "words": [
                {"lemma": "transzformátor", "translation": "electrical transformer", "pos": "noun"},
                {"lemma": "váltakozó áram", "translation": "alternating current (AC)", "pos": "expression"},
                {"lemma": "szabadalmaztat", "translation": "to patent / have patented", "pos": "verb"},
                {"lemma": "öngerjesztés", "translation": "self-excitation (dynamo principle)", "pos": "noun"},
                {"lemma": "révén", "translation": "by means of / through / thanks to (postposition)", "pos": "postposition"},
                {"lemma": "útján", "translation": "by way of / through the channel of (postposition)", "pos": "postposition"}
            ],
            "grammar_doc": {
                "slug": "postpositions-of-means",
                "title": "Formal Postpositions of Technical Means (révén, útján, segítségével)",
                "text1_title": "Replacing Everyday -val/-vel in Scientific & Historical Prose",
                "text1": "While everyday Hungarian expresses instruments with -val/-vel, B2 technical and historical prose uses three compound postpositions derived from possessed nouns to specify how a breakthrough operates: 1) segítségével ('with the help/aid of' — concrete instrument or system); 2) révén ('by means of / thanks to' — underlying discovery, principle, or project); 3) útján ('by way of / through the process or channel of' — method, patent, or physical transmission).",
                "text2_title": "Possessive Agreement vs. Unmarked Noun before révén, útján, segítségével",
                "text2": "Just like standard Hungarian postpositions, the noun preceding révén, útján, and segítségével stands in its unmarked nominative form (or takes -nak/-nek if separated or demonstrative): 'az öngerjesztés elve révén' / 'a vízierőmű révén' (thanks to the hydroelectric plant); 'az új rendszer segítségével' (with the help of the new system); 'elektromágneses indukció útján' (by way of electromagnetic induction).",
                "table_title": "Choosing Between révén, útján, and segítségével",
                "table_rows": [
                    ["segítségével (concrete tool / system)", "Az új transzformátor segítségével csökkentették a veszteséget."],
                    ["révén (achieved result / enabling cause)", "A tivoli vízierőmű révén világították ki Rómát."],
                    ["útján (process / mechanism / channel)", "A szó a budapesti szabadalom útján terjedt el a világban."],
                    ["Combined with -andó/-endő", "A távvezeték útján továbbítandó áram feszültségét megnövelték."]
                ],
                "examples": [
                    {"spanish": "Jedlik felismerte az öngerjesztés elvét, amelynek révén megalkotta az első dinamót.", "english": "Jedlik recognized the principle of self-excitation, by means of which he created the first dynamo."},
                    {"spanish": "A „transzformátor” szó a budapesti szabadalmuk útján terjedt el a világban.", "english": "The word 'transformer' spread throughout the world by way of their Budapest patent."},
                    {"spanish": "Az új rendszer segítségével a nagyfeszültségű áramot a városokba lehetett vezetni.", "english": "With the help of the new system, high-voltage current could be conducted into cities."}
                ],
                "tip": "When linking a relative clause with révén or segítségével, attach the 3rd person possessive suffix to the relative pronoun's dative form: 'az elv, amelynek révén...' (the principle by means of which...) or 'a rendszer, amelynek segítségével...' (the system with the help of which...)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "pairs": [
                        ["transzformátor", "electrical transformer"],
                        ["váltakozó áram", "alternating current (AC)"],
                        ["szabadalmaztat", "to patent"],
                        ["öngerjesztés", "self-excitation"],
                        ["révén", "by means of / thanks to"],
                        ["útján", "by way of / through"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "question": "Ki volt az a három magyar mérnök, aki 1885-ben a Ganz-gyárban szabadalmaztatta a zárt vasmagú transzformátort?",
                    "options": [
                        "Zipernowsky Károly, Déri Miksa és Bláthy Ottó Titusz.",
                        "Kempelen Farkas, Rubik Ernő és Bíró László.",
                        "Wigner Jenő, Neumann János és Teller Ede."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "sentence": "Jedlik Ányos bencés fizikus már Werner Siemens előtt leírta az _____ elvét, amely a dinamó működésének alapja.",
                    "answer": "öngerjesztés",
                    "english": "Benedictine physicist Ányos Jedlik described the principle of self-excitation, which is the basis of the dynamo's operation, even before Werner Siemens."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-obligatory-participle"],
                    "question": "Which relative + postposition phrase correctly completes: 'A Ganz-mérnökök megépítették a transzformátort, _____ Róma utcáit is kivilágították'?",
                    "options": [
                        "amelynek segítségével",
                        "amelyet segítségével",
                        "amelyből révén",
                        "amelyre útján"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "sentence": "A vízierőműben megtermelt és nagy távolságra _____ villamos energiát először feltranszformálták. (szállít - obligatory participle)",
                    "answer": "szállítandó",
                    "english": "The electrical energy produced in the hydroelectric plant and to be transported over a long distance was first stepped up by a transformer."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "tiles": ["Az", "új", "transzformátor", "segítségével", "csökkentették", "a", "hálózati", "veszteséget."],
                    "solution": ["Az", "új", "transzformátor", "segítségével", "csökkentették", "a", "hálózati", "veszteséget."],
                    "english": "With the help of the new transformer, they reduced network power loss."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-obligatory-participle"],
                    "prompt": [
                        {"speaker": "Mérnökhallgató", "text": "Miért volt olyan döntő jelentőségű az 1892-es tivoli–római erőművi távvezeték?"},
                        {"speaker": "Professzor", "text": "_____"}
                    ],
                    "options": [
                        "Mert a Ganz-féle transzformátorok révén sikerült huszonhét kilométer távolságból, minimális veszteséggel kivilágítani egy világvárost.",
                        "Mert Jedlik Ányos ott mutatta be a sakkozó törököt az olasz királynak.",
                        "Mert bebizonyította, hogy a villamos energiát nem lehet drótok útján továbbítani."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Milyen nemzetközi nyelvi hatása volt Zipernowsky, Déri és Bláthy 1885-ös budapesti szabadalmának?",
                    "options": [
                        "Az általuk alkotott „transzformátor” kifejezés terjedt el a világ szinte valamennyi nyelvében.",
                        "A világ összes erőművében kötelezővé tették a magyar nyelv használatát.",
                        "A dinamó szót lecserélték fújtatóra."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "László Bíró and the Pen That Never Smudged",
            "grammar_label": "Extended participial attributes combining -andó/-endő and postpositional phrases",
            "goals": [
                "I can narrate how journalist László Bíró and his chemist brother György invented the modern ballpoint pen (biro) from Budapest to Buenos Aires.",
                "I can construct complex prenominal participial modifiers with -andó/-endő and postpositions of means.",
                "I can use vocabulary relating to printing, viscosity, capillarity, and industrial design."
            ],
            "story_segment": {
                "seg_slug": "birolaszlo",
                "title": "Bíró László és a gyorsan száradó nyomdafesték",
                "summary": "Frustrated by smudging fountain pens in Budapest editorial offices, journalist László Bíró noticed how fast newspaper ink dried on rotary presses and created the capillary ballpoint pen with his brother György.",
                "location": "Budapest, Párizs és Buenos Aires (1931–1945)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1930-as évek Budapestjén Bíró László újságíróként és szerkesztőként naponta bosszankodott a hagyományos töltőtollakon: a vékony acélhegy gyakran felsértette a papírt, a vízalapú tinta pedig elkenődött a kéziratokon, és hosszú percekig kellett itatóspapírral szárítgatni a sürgősen nyomdába küldendő cikkeket."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Bíró egy pesti nyomdában figyelte a hatalmas forgó hengereket, észrevette, hogy a sűrű nyomdafesték a papírral érintkezve szinte azonnal megszárad, és nem hagy foltot maga után. Ebből a megfigyelésből született meg a gondolat: olyan írószert kell készíteni, amelynek hegyében egy apró, szabadon forgó acélgolyó viszi fel a sűrű festéket a papírra."
                    },
                    {
                        "type": "narration",
                        "text": "A megoldandó kémiai és fizikai nehézségek azonban óriásiak voltak, mert a sűrű festék a hagyományos csövekben nem folyt le a tollhegyig. Bíró László ezért fogorvos és vegyész testvére, Bíró György segítségével kezdte kikísérletezni a megfelelő viszkozitású pasztát, valamint a hajszálcsövesség (kapillaritás) elvén működő adagolócsatornákat."
                    },
                    {
                        "type": "narration",
                        "text": "Az első szabadalmat még 1938-ban Budapesten és Párizsban jegyeztették be, ám a fasizmus elől a testvérpárnak emigrálnia kellett, és 1940-ben Argentínában, Buenos Airesben telepedtek le. Ott alapították meg üzemüket, ahol a „Birome” néven forgalomba hozott golyóstoll rövid idő alatt meghódította a piacot; Argentínában a feltaláló születésnapján, szeptember 29-én ma is a Feltalálók Napját ünneplik."
                    },
                    {
                        "type": "narration",
                        "text": "A második világháború alatt a Brit Királyi Légierő harmincezer darabot rendelt a golyóstollból, mert a pilóták térképein nagy magasságban, alacsony légnyomás mellett sem folyt ki belőle a festék. A angol nyelvben azóta is „biro” néven emlegetett találmány így vált a huszadik század legelterjedtebb használati tárgyává."
                    }
                ]
            },
            "words": [
                {"lemma": "töltőtoll", "translation": "fountain pen", "pos": "noun"},
                {"lemma": "golyóstoll", "translation": "ballpoint pen", "pos": "noun"},
                {"lemma": "nyomdafesték", "translation": "printing ink", "pos": "noun"},
                {"lemma": "hajszálcsövesség", "translation": "capillarity / capillary action", "pos": "noun"},
                {"lemma": "elkenődik", "translation": "to smudge / smear", "pos": "verb"},
                {"lemma": "viszkozitás", "translation": "viscosity", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "extended-obligatory-participles",
                "title": "Extended Prenominal Modifiers with -andó/-endő",
                "text1_title": "Building Complex Technical Attributes Before the Noun",
                "text1": "In Hungarian journalistic and patent prose, an -andó/-endő participle can govern its own adverbials of place, time, or means, all packed neatly between the definite article (a/az) and the head noun: 'a sürgősen nyomdába küldendő cikkek' (the articles to be sent urgently to the printing house); 'az acélgolyó útján papírra felviendő festék' (the ink to be applied to paper by way of the steel ball).",
                "text2_title": "Irregular -v- Stem Participles (teendő, viendő, veendő)",
                "text2": "Pay special attention to the small group of monosyllabic verbs whose stems alternate with -v- (tesz 'does/puts', visz 'carries', vesz 'takes/buys', eszik 'eats', iszik 'drinks', lesz 'will be'). Their obligatory participles are formed from the short vowel stem: teendő ('thing to be done / task'), felviendő ('to be applied/carried up'), figyelembe veendő ('to be taken into consideration'), elérendő ('to be achieved'). Notice that teendő has also lexicalized as a standalone noun ('sok a teendőnk' = we have a lot to do)!",
                "table_title": "Regular and -v- Stem Obligatory Participles",
                "table_rows": [
                    ["küld → küldendő", "a sürgősen nyomdába küldendő cikkek (articles to be sent to press)"],
                    ["kiküszöböl → kiküszöbölendő", "a kiküszöbölendő műszaki hiba (the technical flaw to be eliminated)"],
                    ["tesz → teendő", "a legfontosabb teendők listája (the list of most important tasks to be done)"],
                    ["figyelembe vesz → figyelembe veendő", "a tervezésnél figyelembe veendő légnyomás (air pressure to be taken into account)"]
                ],
                "examples": [
                    {"spanish": "Hosszú percekig kellett szárítgatni a sürgősen nyomdába küldendő cikkeket.", "english": "One had to blot for long minutes the articles to be sent urgently to the printing press."},
                    {"spanish": "A nagy magasságban figyelembe veendő alacsony légnyomás sem okozott szivárgást.", "english": "Even the low air pressure to be taken into consideration at high altitude caused no leakage."},
                    {"spanish": "Bíró László a testvére segítségével kísérletezte ki a megfelelő viszkozitású pasztát.", "english": "László Bíró developed the paste of proper viscosity with the help of his brother."}
                ],
                "tip": "Remember the fixed idiom 'figyelembe veendő tényező' ('a factor to be taken into account')—it is one of the most frequent B2–C1 academic collocations in Hungarian!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "pairs": [
                        ["töltőtoll", "fountain pen"],
                        ["golyóstoll", "ballpoint pen"],
                        ["nyomdafesték", "printing ink"],
                        ["hajszálcsövesség", "capillary action"],
                        ["elkenődik", "to smudge / smear"],
                        ["viszkozitás", "viscosity"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "question": "Milyen nyomdai megfigyelés adta Bíró Lászlónak a golyóstoll alapötletét Budapesten?",
                    "options": [
                        "Az, hogy a forgó hengereken használt sűrű nyomdafesték a papíron szinte azonnal megszárad és nem kenődik el.",
                        "Az, hogy a lúdtoll sokkal gyorsabban ír, mint az írógép.",
                        "Az, hogy a vízalapú tinta soha nem fogy ki az üvegből."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "sentence": "A hagyományos _____ tintája a repülőgépekben, nagy magasságban az alacsony légnyomás miatt gyakran kifolyt.",
                    "answer": "töltőtollak",
                    "english": "The ink of traditional fountain pens often leaked in airplanes at high altitude due to low air pressure."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-obligatory-participle"],
                    "question": "What is the correct obligatory participle of the irregular verb phrase 'figyelembe vesz' ('takes into account')?",
                    "options": [
                        "figyelembe veendő",
                        "figyelembe veszendő",
                        "figyelembe vett",
                        "figyelembe vevő"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "sentence": "A szerkesztőségben órákig szárítgatták a sürgősen nyomdába _____ kéziratokat. (küld - obligatory participle)",
                    "answer": "küldendő",
                    "english": "In the editorial office, they blotted for hours the manuscripts to be sent urgently to the printing house."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "tiles": ["A", "légnyomás", "a", "tervezésnél", "figyelembe", "veendő", "tényező", "volt."],
                    "solution": ["A", "légnyomás", "a", "tervezésnél", "figyelembe", "veendő", "tényező", "volt."],
                    "english": "Air pressure was a factor to be taken into account in the design."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-obligatory-participle"],
                    "prompt": [
                        {"speaker": "Tervezőmérnök", "text": "Hogyan oldotta meg Bíró László és Bíró György, hogy a sűrű festék egyenletesen jusson el az acélgolyóhoz?"},
                        {"speaker": "Kémikus", "text": "_____"}
                    ],
                    "options": [
                        "A megfelelő viszkozitású paszta és a hajszálcsövesség (kapillaritás) elvén működő csatornák révén.",
                        "Úgy, hogy fújtatóval fújták bele a vizet a töltőtollba.",
                        "Úgy, hogy a pilótákkal minden percben felrázatták a tollat."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik országban ünneplik ma is a Feltalálók Napját szeptember 29-én, Bíró László születésnapján?",
                    "options": [
                        "Argentínában, ahol Bíró László 1940-ben letelepedett és elindította a Birome gyártását.",
                        "Japánban, ahol az első golyóstollmúzeum épült.",
                        "Svédországban, a Nobel-díjak átadásának helyszínén."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Dénes Gábor and the Invention of Holography",
            "grammar_label": "Predicative and nominalized uses of -andó/-endő and causal/instrumental postpositions (köszönhetően, folytán)",
            "goals": [
                "I can explain how Dénes Gábor invented holography in 1947 while trying to improve the electron microscope, earning the 1971 Nobel Prize in Physics.",
                "I can distinguish positive causal postpositions (köszönhetően 'thanks to') from neutral/technical ones (révén, folytán 'owing to / as a consequence of').",
                "I can discuss wave optics, interference, and 3D imaging in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "gabordenes",
                "title": "Gábor Dénes és a teljes kép megőrzése",
                "summary": "Waiting on a tennis court in Rugby, England in 1947, Budapest-born physicist Dénes Gábor conceived holography—recording both the amplitude and phase of light waves—which blossomed once the laser was invented in 1960.",
                "location": "Budapest, Rugby és London (1947–1971)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A budapesti születésű Gábor Dénes már gimnazista korában otthoni laboratóriumot rendezett be a testvérével, majd a Műegyetem és a berlini tanulmányok után Nagy-Britanniában telepedett le. 1947 húsvétján az angliai Rugby városában, egy teniszpálya padján várakozva villant az eszébe a gondolat, amely megoldotta az elektronmikroszkóp képalkotásának régóta kiküszöbölendő hibáját."
                    },
                    {
                        "type": "narration",
                        "text": "Gábor Dénes felismerte, hogy a hagyományos fényképezés azért ad síkbeli képet, mert csupán a fényhullámok erősségét (amplitúdóját) rögzíti, miközben a térbeli mélységet hordozó fázisinformáció teljesen elvész. Ha azonban a tárgyról visszaverődő hullámot egy koherens referenciahullámmal hozzák interferenciába, a rögzítendő interferenciakép a teljes információt megőrzi."
                    },
                    {
                        "type": "narration",
                        "text": "Az új eljárást a görög „holosz” (teljes) és „graphé” (írás) szavakból holográfiának, vagyis teljes feljegyzésnek nevezte el. Amikor a hologramot később megfelelő fénnyel megvilágítják, a szemlélő előtt a levegőben lebegve jelenik meg a tárgy tökéletes, háromdimenziós térbeli mása."
                    },
                    {
                        "type": "narration",
                        "text": "Bár az elmélet 1947-ben készen állt, a gyakorlati áttörésre több mint egy évtizedet kellett várni, mert akkoriban még nem létezett elég tiszta, koherens fényforrás. Az 1960-ban feltalált lézersugárnak köszönhetően azonban a holográfia egyik napról a másikra világméretű iparággá vált, és Gábor Dénes 1971-ben átvehette a fizikai Nobel-díjat."
                    },
                    {
                        "type": "narration",
                        "text": "Ma a bankkártyák és útlevelek biztonsági jeleitől az orvosi képalkotásig és az optikai adattárolásig számtalan területen használjuk Gábor Dénes találmányát, aki idős korában a Római Klub tagjaként az emberiség előtt álló, közösen megoldandó jövőkutatási kérdésekkel is szenvedélyesen foglalkozott."
                    }
                ]
            },
            "words": [
                {"lemma": "holográfia", "translation": "holography", "pos": "noun"},
                {"lemma": "fényhullám", "translation": "light wave", "pos": "noun"},
                {"lemma": "interferencia", "translation": "wave interference", "pos": "noun"},
                {"lemma": "lézersugár", "translation": "laser beam", "pos": "noun"},
                {"lemma": "térbeli", "translation": "three-dimensional / spatial", "pos": "adjective"},
                {"lemma": "kiküszöbölendő", "translation": "to be eliminated / to be overcome", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "causal-instrumental-postpositions",
                "title": "Nuances of Cause and Means: köszönhetően (-nak/-nek) vs. révén & folytán",
                "text1_title": "Government Difference: köszönhetően (+ -nak/-nek) vs. révén (+ Nominative)",
                "text1": "One of the most important B2 grammar distinctions in Hungarian involves postpositions of positive cause and technical means: 1) köszönhetően ('thanks to / owing positively to') is derived from a participle and ALWAYS governs the dative case (-nak/-nek): 'az 1960-ban feltalált lézersugárnak köszönhetően' (thanks to the laser beam invented in 1960). 2) révén ('by means of / through') and folytán ('as a consequence of / due to') are possessed nouns and take an UNMARKED nominative noun before them: 'a referenciahullám révén' (by means of the reference wave), 'az interferencia folytán' (as a consequence of interference).",
                "text2_title": "Predicative and Substantivized Uses of -andó/-endő",
                "text2": "Beyond standing before a noun ('a rögzítendő kép'), -andó/-endő participles can stand in the predicate ('Ez a hiba sürgősen kiküszöbölendő' = This flaw must be urgently eliminated) or act as nouns ('az emberiség előtt álló teendők' = the tasks facing humanity).",
                "table_title": "Case Government of Technical & Causal Postpositions",
                "table_rows": [
                    ["Noun + -nak/-nek + köszönhetően", "A lézersugárnak köszönhetően a holográfia világméretűvé vált."],
                    ["Unmarked Noun + révén", "Az interferencia révén a fázisinformáció is megőrződik."],
                    ["Unmarked Noun + segítségével", "Az elektronmikroszkóp segítségével vizsgálták az anyag szerkezetét."],
                    ["Unmarked Noun + folytán", "A fényforrás hiánya folytán tíz évet kellett várni az áttörésre."]
                ],
                "examples": [
                    {"spanish": "Az 1960-ban feltalált lézersugárnak köszönhetően a holográfia világméretű iparággá vált.", "english": "Thanks to the laser beam invented in 1960, holography became a worldwide industry."},
                    {"spanish": "A rögzítendő interferenciakép a fényhullám teljes információját megőrzi.", "english": "The interference image to be recorded preserves the complete information of the light wave."},
                    {"spanish": "Gábor Dénes az elektronmikroszkóp régóta kiküszöbölendő hibáját akarta kijavítani.", "english": "Dénes Gábor wanted to fix the long-standing flaw of the electron microscope that needed to be eliminated."}
                ],
                "tip": "Never forget the -nak/-nek before köszönhetően ('a lézernek köszönhetően'), and never add -nak/-nek before a simple noun + révén ('a lézer révén')!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "pairs": [
                        ["holográfia", "holography"],
                        ["fényhullám", "light wave"],
                        ["interferencia", "wave interference"],
                        ["lézersugár", "laser beam"],
                        ["térbeli", "spatial / three-dimensional"],
                        ["kiküszöbölendő", "to be eliminated"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "question": "Miért veszti el a hagyományos fényképezés a tárgyak térbeli mélységét Gábor Dénes felismerése szerint?",
                    "options": [
                        "Mert csupán a fényhullámok erősségét (amplitúdóját) rögzíti, míg a fázisinformáció elvész.",
                        "Mert túl sok lézersugarat használ a sötétkamrában.",
                        "Mert a papír nem képes megtartani a nyomdafestéket."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "sentence": "A „holográfia” szó a görög „teljes feljegyzés” kifejezésből ered, mert a hologram a tárgy tökéletes _____ mását adja vissza.",
                    "answer": "térbeli",
                    "english": "The word 'holography' comes from the Greek expression for 'complete recording', because a hologram reproduces a perfect spatial (3D) replica of the object."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-obligatory-participle"],
                    "question": "Why is 'a lézersugárnak köszönhetően' grammatical while '*a lézersugár köszönhetően' is incorrect?",
                    "options": [
                        "Because 'köszönhetően' always governs the dative suffix -nak/-nek on the preceding noun phrase.",
                        "Because 'lézersugár' is a plural verb.",
                        "Because 'köszönhetően' can only be used at the very beginning of a sentence.",
                        "Because 'révén' and 'köszönhetően' both require the accusative -t."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "sentence": "A fotoüvegre _____ interferenciakép nemcsak az amplitúdót, hanem a hullámok fázisát is megőrzi. (rögzít - obligatory participle)",
                    "answer": "rögzítendő",
                    "english": "The interference image to be recorded onto the photographic plate preserves not only the amplitude, but also the phase of the waves."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "tiles": ["Az", "új", "lézersugárnak", "köszönhetően", "a", "holográfia", "világsikerré", "vált."],
                    "solution": ["Az", "új", "lézersugárnak", "köszönhetően", "a", "holográfia", "világsikerré", "vált."],
                    "english": "Thanks to the new laser beam, holography became a worldwide success."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-obligatory-participle"],
                    "prompt": [
                        {"speaker": "Fizikatanár", "text": "Miért kellett Gábor Dénes 1947-es felfedezése után még több mint tíz évet várni a holográfia gyakorlati elterjedésére?"},
                        {"speaker": "Diák", "text": "_____"}
                    ],
                    "options": [
                        "Mert csak az 1960-ban feltalált lézersugár révén állt rendelkezésre elég tiszta, koherens fényforrás.",
                        "Mert 1960-ig senki sem tudta lefordítani a görög „holosz” szót magyarra.",
                        "Mert Gábor Dénes megtiltotta az elektronmikroszkóp használatát."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik évben részesült fizikai Nobel-díjban Gábor Dénes a holográfia feltalálásáért?",
                    "options": [
                        "1971-ben.",
                        "1885-ben.",
                        "1918-ban."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Ernő Rubik's Spatial Teaching Tool Becomes a Global Icon",
            "grammar_label": "Full synthesis of obligatory participles (-andó/-endő) and formal instrumental postpositions",
            "goals": [
                "I can tell the story of how architect Ernő Rubik created the Magic Cube (Bűvös kocka) in 1974 in Budapest to teach three-dimensional geometry.",
                "I can combine obligatory participles (-andó/-endő) and postpositions of means (révén, útján, segítségével, köszönhetően) in B2 expository writing.",
                "I can discuss spatial thinking, algorithmic problem-solving, and Hungarian design heritage."
            ],
            "story_segment": {
                "seg_slug": "rubikerno",
                "title": "A Bűvös kocka: oktatási segédeszközből világjelkép",
                "summary": "In spring 1974, young Budapest architecture teacher Ernő Rubik built a wooden prototype to demonstrate 3D spatial movement to his design students—and accidentally created the best-selling puzzle in human history.",
                "location": "Budapest, Iparművészeti Főiskola (1974–1982)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1974 tavaszán a harmincéves Rubik Ernő, a budapesti Iparművészeti Főiskola építész- és formatervező tanára nem világméretű játékipari sikert akart létrehozni, hanem egy szemléltetendő geometriai problémára keresett kézzelfogható megoldást. Azt szerette volna megmutatni a hallgatóinak, miként mozoghatnak egy térbeli test egyes elemei egymáson úgy, hogy közben maga a szerkezet ne essen szét."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor a huszonhat kis fakockából és a központi csillagcsuklóból összeállított első prototípus elkészült, Rubik színes papírlapokat ragasztott a hat oldalra, majd néhányszor elforgatta az elemeket. Hamarosan szembesült a negyvenhárom-trillió lehetséges állás döbbenetes matematikájával: maga a feltaláló is közel egy hónapon át kísérletezett, mire saját algoritmusai segítségével visszaállította az eredeti, egyszínű oldalakat."
                    },
                    {
                        "type": "narration",
                        "text": "A „Bűvös kocka” néven 1975-ben szabadalmaztatott térbeli logikai játék először Magyarországon vált szenzációvá: villamosokon, iskolapadokban és kávéházakban mindenki a színes oldalakat forgatta. 1980-tól kezdve a nemzetközi forgalmazás révén a Rubik-kocka áttörte a vasfüggönyt, és néhány év alatt több százmillió példányban kelt el a földkerekségen."
                    },
                    {
                        "type": "narration",
                        "text": "1982 júniusában éppen Budapesten, a Vigadó épületében rendezték meg az első Rubik-kocka-világbajnokságot, miközben a kocka bekerült a New York-i Modern Művészetek Múzeumának (MoMA) állandó formatervezési gyűjteményébe is. Matematikusok, informatikusok és kognitív pszichológusok számára egyaránt a csoportelmélet és az algoritmikus gondolkodás követendő modelljévé vált."
                    },
                    {
                        "type": "narration",
                        "text": "Kempelen Farkas fogaskerekeitől Rubik Ernő kockájáig így zárul be a kör: a legmaradandóbb magyar találmányok mindig a tudományos kíváncsiság, a pedagógiai képzelet és a tiszta formai elegancia találkozásából születtek."
                    }
                ]
            },
            "words": [
                {"lemma": "bűvös kocka", "translation": "Magic Cube (the original Hungarian name of Rubik's Cube)", "pos": "expression"},
                {"lemma": "formatervezés", "translation": "industrial / product design", "pos": "noun"},
                {"lemma": "prototípus", "translation": "prototype", "pos": "noun"},
                {"lemma": "szemléltetendő", "translation": "to be demonstrated / illustrated", "pos": "adjective"},
                {"lemma": "algoritmus", "translation": "algorithm / sequence of moves", "pos": "noun"},
                {"lemma": "követendő", "translation": "to be followed / exemplary", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "obligatory-participles-synthesis",
                "title": "Synthesizing -andó/-endő and Technical Postpositions in B2 Prose",
                "text1_title": "High-Frequency Academic Collocations with -andó/-endő",
                "text1": "To sound completely natural at B2–C1 level, master the classic collocations where -andó/-endő joins design and scientific nouns: szemléltetendő térbeli mozgás ('spatial movement to be demonstrated'), követendő modell / példa ('model / example to be followed'), megoldandó logikai rejtvény ('logical puzzle to be solved'), visszaállítandó eredeti állapot ('original state to be restored').",
                "text2_title": "Weaving Participles and Means Postpositions Together",
                "text2": "You can combine an instrumental postposition (segítségével, révén, útján) directly inside a prenominal -andó/-endő modifier: 'az algoritmusok segítségével visszaállítandó eredeti állapot' (the original state to be restored with the help of algorithms). This compact structure is the hallmark of polished Hungarian expository style.",
                "table_title": "Classic B2 Design & Engineering Collocations",
                "table_rows": [
                    ["szemléltetendő probléma", "Rubik egy szemléltetendő geometriai problémára keresett megoldást."],
                    ["visszaállítandó állapot", "Az algoritmus segítségével visszaállítandó oldalakat egy hónapig forgatta."],
                    ["követendő modell", "A kocka az algoritmikus gondolkodás követendő modelljévé vált."],
                    ["forgalmazás révén", "A nemzetközi forgalmazás révén a játék áttörte a vasfüggönyt."]
                ],
                "examples": [
                    {"spanish": "Rubik Ernő egy szemléltetendő geometriai problémára keresett kézzelfogható megoldást.", "english": "Ernő Rubik was looking for a tangible solution to a geometric problem to be demonstrated."},
                    {"spanish": "Saját algoritmusai segítségével állította vissza az eredeti, egyszínű oldalakat.", "english": "With the help of his own algorithms, he restored the original single-colored sides."},
                    {"spanish": "A kocka az algoritmikus gondolkodás követendő modelljévé vált.", "english": "The cube became an exemplary model (a model to be followed) of algorithmic thinking."}
                ],
                "tip": "Note the historical fun fact: the adjective maradandó ('lasting / enduring', literally 'that which will remain') is itself an ancient -andó participle derived from marad ('remains')!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "pairs": [
                        ["bűvös kocka", "Magic Cube (Rubik's Cube)"],
                        ["formatervezés", "industrial design"],
                        ["prototípus", "prototype"],
                        ["szemléltetendő", "to be demonstrated"],
                        ["algoritmus", "algorithm"],
                        ["követendő", "to be followed / exemplary"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "question": "Milyen eredeti céllal készítette el Rubik Ernő 1974-ben a kocka első fa prototípusát?",
                    "options": [
                        "Oktatási segédeszközként akarta szemléltetni a térbeli mozgást az Iparművészeti Főiskola hallgatóinak.",
                        "A Brit Királyi Légierő pilótáinak tervezett iránytűt.",
                        "Mária Terézia udvari sakkozói számára épített új automatát."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-talalmanyok-vocab"],
                    "sentence": "A találmányt Magyarországon eredetileg _____ néven szabadalmaztatták 1975-ben, mielőtt világszerte Rubik-kockaként vált ismertté.",
                    "answer": "Bűvös kocka",
                    "english": "The invention was originally patented in Hungary under the name 'Magic Cube' in 1975 before becoming known worldwide as the Rubik's Cube."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-obligatory-participle"],
                    "question": "Which phrase correctly uses an obligatory participle to express 'the original state to be restored with the help of algorithms'?",
                    "options": [
                        "az algoritmusok segítségével visszaállítandó eredeti állapot",
                        "az algoritmusok segítségével visszaállított eredeti állapot",
                        "az algoritmusok segítségével visszaállító eredeti állapot",
                        "az algoritmusok köszönhetően visszaállítandó állapot"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "sentence": "A Rubik-kocka a modern ipari formatervezésben és a matematikaoktatásban egyaránt _____ példává vált. (követ - obligatory participle)",
                    "answer": "követendő",
                    "english": "The Rubik's Cube became an example to be followed in both modern industrial design and mathematics education."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-obligatory-participle"],
                    "tiles": ["Rubik", "saját", "algoritmusai", "segítségével", "állította", "vissza", "az", "oldalakat."],
                    "solution": ["Rubik", "saját", "algoritmusai", "segítségével", "állította", "vissza", "az", "oldalakat."],
                    "english": "Rubik restored the sides with the help of his own algorithms."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-obligatory-participle"],
                    "prompt": [
                        {"speaker": "Formatervező", "text": "Miért került be a Rubik-kocka a New York-i Modern Művészetek Múzeumának (MoMA) állandó gyűjteményébe?"},
                        {"speaker": "Kurátor", "text": "_____"}
                    ],
                    "options": [
                        "Mert a központi csillagcsukló révén a bonyolult matematikai feladványt utolérhetetlenül tiszta formai eleganciával oldotta meg.",
                        "Mert Gábor Dénes lézersugár segítségével vetítette ki a falra.",
                        "Mert ez volt az egyetlen kocka, amelyet nem lehetett elforgatni."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Hol rendezték meg a világ első hivatalos Rubik-kocka-világbajnokságát 1982 júniusában?",
                    "options": [
                        "Budapesten, a pesti Vigadó épületében.",
                        "Buenos Airesben, a Feltalálók Napján.",
                        "Londonban, a Tavistock Klinikán."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can explain the scientific and historical significance of Farkas Kempelen, Ányos Jedlik, the Ganz engineers, László Bíró, Dénes Gábor, and Ernő Rubik.",
            "I can form and use obligatory/future passive participles (-andó/-endő) across back-vowel, front-vowel, and irregular -v- stems.",
            "I can accurately employ formal postpositions of technical means and cause (segítségével, révén, útján + nominative vs. köszönhetően + -nak/-nek).",
            "I can use 30 B2 engineering, physics, and industrial design terms in context."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-talalmanyok-vocab"],
                "pairs": [
                    ["beszédszintézis", "speech synthesis"],
                    ["transzformátor", "electrical transformer"],
                    ["hajszálcsövesség", "capillary action"],
                    ["holográfia", "holography"],
                    ["formatervezés", "industrial design"],
                    ["algoritmus", "algorithm"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-obligatory-participle"],
                "question": "Which suffix pair forms the Hungarian obligatory / future passive participle ('to be solved / to be followed')?",
                "options": [
                    "-andó / -endő (megoldandó, követendő)",
                    "-ó / -ő (megoldó, követő)",
                    "-va / -ve (megoldva, követve)",
                    "-tat / -tet (megoldat, követtet)"
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-talalmanyok-vocab"],
                "question": "Melyik magyar feltaláló kapott 1971-ben fizikai Nobel-díjat a holográfia — vagyis a fényhullámok teljes, térbeli rögzítésének — kidolgozásáért?",
                "options": [
                    "Gábor Dénes.",
                    "Bíró László.",
                    "Jedlik Ányos.",
                    "Zipernowsky Károly."
                ],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-talalmanyok-vocab"],
                "sentence": "Bíró László és Bíró György a _____ elvén működő apró csatornákkal érte el, hogy a sűrű festék eljusson az acélgolyóhoz.",
                "answer": "hajszálcsövesség",
                "english": "László Bíró and György Bíró ensured that the thick ink reached the steel ball through tiny channels operating on the principle of capillarity."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-obligatory-participle"],
                "sentence": "A magassági repülés során az alacsony légnyomás komolyan figyelembe _____ tényező volt a toll tervezésénél. (vesz - obligatory participle)",
                "answer": "veendő",
                "english": "During high-altitude flight, low air pressure was a factor seriously to be taken into account in the design of the pen."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-obligatory-participle"],
                "sentence": "Az 1960-ban feltalált _____ köszönhetően a holográfia elmélete végre a gyakorlatban is megvalósulhatott. (lézersugár + required case)",
                "answer": "lézersugárnak",
                "english": "Thanks to the laser beam invented in 1960, the theory of holography could finally be realized in practice."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-obligatory-participle"],
                "prompt": [
                    {"speaker": "Ipari formatervező", "text": "Mi a közös Bíró László golyóstollában és Rubik Ernő bűvös kockájában?"},
                    {"speaker": "Tudománytörténész", "text": "_____"}
                ],
                "options": [
                    "Mindkettő egy hétköznapi, gyakorlatban megoldandó problémából indult ki, és zseniális mechanikai egyszerűsége révén vált világjelképpé.",
                    "Mindkettőt Mária Terézia bécsi palotájában mutatták be 1769-ben.",
                    "Mindkettő nagyfeszültségű váltakozó árammal működik."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-obligatory-participle"],
                "question": "Choose the sentence where BOTH the obligatory participle and the postposition of means are used grammatically:",
                "options": [
                    "A Ganz-féle transzformátor segítségével csökkentették a nagy távolságra szállítandó áram veszteségét.",
                    "A Ganz-féle transzformátornak segítségével csökkentették a szállítottandó áram veszteségét.",
                    "A Ganz-féle transzformátor köszönhetően csökkentették a szállítandó áramot.",
                    "A Ganz-féle transzformátor révén a nagy távolságra szállító áram vesztesége lett."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-obligatory-participle"],
                "prompt": [
                    {"speaker": "Múzeumpedagógus", "text": "Hogyan működött Kempelen Farkas 1791-es mechanikus beszélőgépe?"},
                    {"speaker": "Látogató", "text": "_____"}
                ],
                "options": [
                    "A kiejtendő hangokat nem előre rögzített hengerről játszotta le, hanem fújtató és bőrüregek segítségével élőben formálta meg.",
                    "Egy szekrénybe bújtatott színész beszélt a fújtató belsejéből.",
                    "Lézersugár útján vetítette ki a betűket a falra."
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-obligatory-participle"],
                "tiles": ["A", "távvezeték", "útján", "szállítandó", "áram", "feszültségét", "megnövelték."],
                "solution": ["A", "távvezeték", "útján", "szállítandó", "áram", "feszültségét", "megnövelték."],
                "english": "They increased the voltage of the current to be transported by way of the transmission line."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-obligatory-participle"],
                "tiles": ["A", "kocka", "a", "térbeli", "gondolkodás", "követendő", "modelljévé", "vált."],
                "solution": ["A", "kocka", "a", "térbeli", "gondolkodás", "követendő", "modelljévé", "vált."],
                "english": "The cube became a model to be followed of spatial thinking."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-obligatory-participle"],
                "template": [
                    {
                        "prompt": "Write a sentence explaining how the Ganz engineers enabled the electrification of distant cities (use 'segítségével' or 'révén' and a -andó/-endő participle).",
                        "answer": "A Ganz-mérnökök a zárt vasmagú transzformátor segítségével csökkentették a nagy távolságra szállítandó villamos energia veszteségét."
                    },
                    {
                        "prompt": "Write a sentence explaining why Ernő Rubik built the first prototype of the Magic Cube (use 'szemléltetendő').",
                        "answer": "Rubik Ernő az egyetemi órákon szemléltetendő térbeli mozgások bemutatására építette meg a Bűvös kocka első prototípusát."
                    }
                ]
            }
        ]
    }
}


def main():
    for spec in (UNIT_10_GIMNAZIUMOK, UNIT_11_PSZICHOANALIZIS, UNIT_12_TALALMANYOK):
        build_culture_unit(spec)


if __name__ == "__main__":
    main()
