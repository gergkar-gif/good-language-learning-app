#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 4, 5, and 6:
  - Unit 4: b2-szinhazmuveszet (The National Stage: Theatre, Censorship & Politics)
  - Unit 5: b2-bartokkodaly (Bartók, Kodály & the Ethnomusicological Revolution)
  - Unit 6: b2-festeszet (Light, Myth & Modernism: Hungarian Visual Arts)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402


UNIT_04_SZINHAZMUVESZET = {
    "unit_num": 4,
    "slug": "szinhazmuveszet",
    "title": "The National Stage: Theatre, Censorship & Politics",
    "grammar_skill": "b2-nehogy-subjunctive",
    "vocab_skill": "b2-szinhazmuveszet-vocab",
    "theme": "Hungarian theatre, operetta and political stage",
    "location": "Budapest (Nemzeti Színház, Vígszínház, Operettszínház)",
    "intro_body": [
        "In 19th- and 20th-century Hungary, the theatre was never merely a place of evening entertainment. Before Hungary had an independent parliament or a free press, the stage functioned as the nation's living forum—where the Hungarian language itself was defended, historical allegories bypassed imperial censors, and social transformations were debated in the spotlight.",
        "In this unit, you will trace the history of the Hungarian stage from the 1837 opening of the Pesti Magyar Színház (built entirely through public donations) and the revolutionary performance of Katona József's Bánk bán on March 15, 1848, to the cosmopolitan brilliance of Molnár Ferenc at the Vígszínház, the worldwide triumph of Budapest operetta, and the subtle cat-and-mouse game between directors and censors. Grammatically, you will master indirect commands, jussive clauses (-jon/-jen), and negative purpose clauses with nehogy ('lest / so that ... not')."
    ],
    "combined_story_title": "Függöny fel: Színház és szabadság",
    "combined_story_summary": "How the Hungarian stage served as a forum for national survival, social satire, and artistic brilliance from the 1837 opening of the National Theatre and Bánk bán in 1848 to the golden age of Budapest comedy and operetta.",
    "lessons": [
        {
            "num": 1,
            "title": "Building a National Theatre Through Public Donations",
            "grammar_label": "Subjunctive purpose clauses with hogy + -jon/-jen",
            "goals": [
                "I can explain how the Pesti Magyar Színház was founded through public donations in 1837.",
                "I can form purpose and indirect command clauses using hogy + subjunctive (-jon/-jen).",
                "I can use B2 theatrical and civic heritage vocabulary accurately."
            ],
            "story_segment": {
                "seg_slug": "nemzetiszinhaz",
                "title": "Közadakozásból épült kőszínház",
                "summary": "In the 1830s, Hungarian actors moved from wandering troupes to a permanent stone theatre in Pest built entirely through public donations.",
                "location": "Pest, Kerepesi út (1837)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A tizenkilencedik század elején a magyar színjátszásnak még nem volt állandó otthona, ezért a vándorszínészek szekereken járták az országot, hogy minden kisvárosban megszólalhasson a magyar szó. Pesten és Budán akkoriban német nyelvű színházak működtek, miközben a reformkor vezetői egyre sürgetőbben követelték, hogy a fővárosban végre önálló magyar kőszínház épüljön."
                    },
                    {
                        "type": "narration",
                        "text": "Széchenyi István és Grassalkovich Antal herceg felhívást tettek közzé, hogy a nemzet saját erejéből, közadakozásból teremtse meg a teátrumot. Nemcsak a főurak adományoztak telket és aranyforintokat, hanem szegény diákok, iparosok és falusi tanítók is félretették a fillérjeiket, nehogy a nemzeti ügy pénzhiány miatt elbukjon."
                    },
                    {
                        "type": "narration",
                        "text": "Az építkezés során a vármegyék küldöttei szigorúan ügyeltek arra, hogy a munkálatok egyetlen napra se álljanak le. A kortársak úgy tekintettek az épülő színházra, mint a magyar nyelv templomára, amely biztosítja, hogy a hazai drámairodalom méltó körülmények között fejlődjön."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor 1837. augusztus 22-én a Pesti Magyar Színházban először gördült fel a függöny, Vörösmarty Mihály Árpád ébredése című ünnepi játékát mutatták be. A nézőtéren ülő polgárok könnyek között tapsoltak, mert érezték, hogy a színpad a nemzeti önállóság előszobájává vált."
                    },
                    {
                        "type": "narration",
                        "text": "Néhány évvel később az intézmény hivatalosan is felvette a Nemzeti Színház nevet, hogy mindenki számára világos legyen: ez a színpad az egész ország szellemi központja. A vándorszínészek egykori álma így vált a modern magyar kultúra egyik legfontosabb alapkövévé."
                    }
                ]
            },
            "words": [
                {"lemma": "közadakozás", "translation": "public donation / subscription", "pos": "noun"},
                {"lemma": "vándorszínész", "translation": "strolling player / itinerant actor", "pos": "noun"},
                {"lemma": "kőszínház", "translation": "permanent stone theatre", "pos": "noun"},
                {"lemma": "függöny", "translation": "stage curtain", "pos": "noun"},
                {"lemma": "nézőtér", "translation": "auditorium / house", "pos": "noun"},
                {"lemma": "színjátszás", "translation": "acting / theatrical art", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "purpose-subjunctive",
                "title": "Purpose & Indirect Command Clauses with hogy + Subjunctive",
                "text1_title": "Expressing Purpose and Desired Outcomes",
                "text1": "In B2 Hungarian, whenever a main clause expresses purpose ('in order that'), public appeals ('demanded that'), or institutional precaution ('ensured that'), the subordinate clause introduced by hogy requires the subjunctive/imperative mood (-j- suffix: épüljön, fejlődjön, megszólaljon). Notice how the verbal prefix stays attached in positive purpose clauses (hogy megszólalhasson), whereas in negative clauses with ne or nehogy the prefix separates or follows the negative particle.",
                "text2_title": "Vowel Harmony in -jon/-jen/-jön",
                "text2": "In the 3rd person singular indefinite, back-vowel verbs take -jon (adományozzon, álljon), unrounded front-vowel verbs take -jen (teremtsen, szerepeljen), and rounded front-vowel verbs take -jön (épüljön, fejlődjön). Definite transitive verbs take -ja/-je (hogy a nemzet saját erejéből teremtse meg a színházat).",
                "table_title": "Indicative Statement vs. Subjunctive Purpose Clause",
                "table_rows": [
                    ["Kőszínház épül Pesten. (Indicative)", "Követelték, hogy kőszínház épüljön Pesten. (Subjunctive)"],
                    ["A nemzet megteremti a teátrumot.", "Felhívást tettek közzé, hogy a nemzet teremtse meg a teátrumot."],
                    ["A drámairodalom szabadon fejlődik.", "Ez biztosítja, hogy a drámairodalom szabadon fejlődjön."],
                    ["A munkálatok nem állnak le.", "Ügyeltek arra, hogy a munkálatok ne álljanak le."]
                ],
                "examples": [
                    {"spanish": "A vándorszínészek járták az országot, hogy mindenütt megszólaljon a magyar szó.", "english": "The itinerant actors toured the country so that the Hungarian word might be heard everywhere."},
                    {"spanish": "A reformerek azt akarták, hogy a színház közadakozásból épüljön fel.", "english": "The reformers wanted the theatre to be built from public donations."},
                    {"spanish": "Ügyeltek arra, hogy az építkezés egyetlen napra se álljon le.", "english": "They took care that construction should not stop for even a single day."}
                ],
                "tip": "When a verb with a separable prefix (like megteremt or felépül) is used as a strong request or command inside a hogy-clause, placing the verb before the prefix (hogy teremtse meg) emphasizes the imperative force of the appeal."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "pairs": [
                        ["közadakozás", "public donation / subscription"],
                        ["vándorszínész", "itinerant actor"],
                        ["kőszínház", "permanent stone theatre"],
                        ["függöny", "stage curtain"],
                        ["nézőtér", "auditorium"],
                        ["színjátszás", "theatrical art"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "question": "Milyen forrásból épült fel a Pesti Magyar Színház 1837-re?",
                    "options": [
                        "Nemzeti közadakozásból, amelyhez főurak és egyszerű polgárok is hozzájárultak.",
                        "Kizárólag a bécsi császári udvar titkos támogatásából.",
                        "Külföldi bankok hiteléből és jegyárbevételből."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "sentence": "Amikor 1837-ben először gördült fel a _____, a közönség könnyek között tapsolt.",
                    "answer": "függöny",
                    "english": "When the stage curtain rose for the first time in 1837, the audience applauded in tears."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "question": "Which verb form correctly completes the purpose clause: 'A reformerek követelték, hogy Pesten önálló magyar kőszínház _____.'?",
                    "options": ["épüljön", "épül", "épült", "épülne"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "sentence": "A küldöttek ügyeltek arra, hogy a munkálatok egyetlen napra se _____ le. (áll - 3rd pl. subjunctive)",
                    "answer": "álljanak",
                    "english": "The delegates made sure that the works should not stop for even a single day."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "tiles": ["Azt", "akarták,", "hogy", "a", "színház", "közadakozásból", "épüljön", "fel."],
                    "solution": ["Azt", "akarták,", "hogy", "a", "színház", "közadakozásból", "épüljön", "fel."],
                    "english": "They wanted the theatre to be built through public donations."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "prompt": [
                        {"speaker": "Történész", "text": "Miért volt olyan fontos a vándorszínészek kitartása a reformkorban?"},
                        {"speaker": "Dramaturg", "text": "_____"}
                    ],
                    "options": [
                        "Azért járták az országot, hogy minden kisvárosban megszólalhasson a magyar szó.",
                        "Mert nem szerettek kőszínházban játszani a pesti nézőtér előtt.",
                        "Hogy a német színészekkel együtt lépnek fel Bécsben."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik művel nyitotta meg kapuit a Pesti Magyar Színház 1837. augusztus 22-én?",
                    "options": [
                        "Vörösmarty Mihály Árpád ébredése című ünnepi játékával.",
                        "Katona József Bánk bán című tragédiájával.",
                        "Molnár Ferenc A Pál utcai fiúk című darabjával."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Bánk bán and the Stage as Political Forum",
            "grammar_label": "Negative purpose clauses with nehogy + subjunctive",
            "goals": [
                "I can describe the historical role of Katona József's Bánk bán on March 15, 1848.",
                "I can construct negative purpose and warning clauses using nehogy + subjunctive.",
                "I can discuss historical allegory and dramatic conflict in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "bankbanszinhaz",
                "title": "Bánk bán és a márciusi díszelőadás",
                "summary": "Written by Katona József in 1815 and long obstructed by imperial censors, Bánk bán became the emblem of the 1848 revolution on the night of March 15.",
                "location": "Nemzeti Színház, Pest (1848. március 15.)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Katona József már 1815-ben megírta a Bánk bán című történelmi tragédiát, ám a császári cenzúra évtizedekig akadályozta a darab pesti bemutatását, nehogy a közönség az idegen udvaroncok elleni lázadásként értelmezze a művet. A dráma a tizenharmadik századi Magyarországon játszódik, ahol Gertrudis királyné meráni kísérete kifosztja a népet, miközben a nagyúr, Bánk bán a királyi hűség és a hazafiúi kötelesség között őrlődik."
                    },
                    {
                        "type": "narration",
                        "text": "Katona olyan összetett jellemeket alkotott, hogy a tragédia nem egyszerű politikai röpirat, hanem mély lélektani dráma lett. Tiborc, az elszegényedett jobbágy panasza azonban minden korabeli néző szívébe markolt, ezért a hatóságok éberen figyeltek, nehogy a színházban zavargás törjön ki."
                    },
                    {
                        "type": "narration",
                        "text": "1848. március 15-én a pesti forradalmi ifjúság követelte, hogy a Nemzeti Színház még aznap este tűzze műsorra a Bánk bánt. A színház igazgatósága engedett a kérésnek, és a homlokzatot nemzetiszínű zászlókkal díszítették fel, hogy az egész város lássa az ünnepi fordulatot."
                    },
                    {
                        "type": "narration",
                        "text": "Az esti díszelőadás közben a zsúfolásig megtelt nézőtér követelte, hogy a színészek szavalják el a Nemzeti dalt és énekeljék el a Himnuszt. Egressy Gábor kokárdával a mellén lépett a rivaldafénybe, miközben a karzatról Jókai Mór csitította a felhevült tömeget, nehogy a lelkesedés rendbontásba csapjon át."
                    },
                    {
                        "type": "narration",
                        "text": "Attól az estétől kezdve a Bánk bán — majd később Erkel Ferenc belőle komponált operája — a magyar színháztörténet legfőbb nemzeti jelképévé vált. Valahányszor a történelem viharai elhallgattatták a sajtót, a közönség Tiborc és Bánk szavaiban kereste az igazságot."
                    }
                ]
            },
            "words": [
                {"lemma": "díszelőadás", "translation": "gala performance", "pos": "noun"},
                {"lemma": "tragédia", "translation": "tragedy", "pos": "noun"},
                {"lemma": "rivaldafény", "translation": "footlights / limelight", "pos": "noun"},
                {"lemma": "karzat", "translation": "gallery / balcony (in theatre)", "pos": "noun"},
                {"lemma": "udvaronc", "translation": "courtier", "pos": "noun"},
                {"lemma": "műsorra tűz", "translation": "to put on the bill / program", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "nehogy-negative-purpose",
                "title": "Negative Purpose Clauses with nehogy + Subjunctive",
                "text1_title": "How nehogy ('lest / so that ... not') Works",
                "text1": "To warn against an undesired outcome or explain a precaution taken so something does NOT happen, Hungarian uses the conjunction nehogy followed immediately by a verb in the subjunctive (-jon/-jen/-jön). Unlike hogy ... ne, where ne sits right before the verb, nehogy stands at the very start of the subordinate clause and already carries the negative meaning—never add a second ne after nehogy!",
                "text2_title": "Word Order and Verbal Prefixes after nehogy",
                "text2": "In a nehogy clause, the verb usually keep its prefix attached (nehogy elbukjon, nehogy értelmezze) or places the focused element right before the verb (nehogy zavargás törjön ki, nehogy rendbontásba csapjon át). This distinction between hogy ... ne (prefix splits: hogy ne törjön ki) and nehogy (nehogy kitörjön / nehogy zavargás törjön ki) is a classic B2 hallmark.",
                "table_title": "hogy ... ne vs. nehogy",
                "table_rows": [
                    ["Ügyeltek, hogy ne törjön ki zavargás.", "Ügyeltek, nehogy zavargás törjön ki."],
                    ["Vigyázz, hogy ne késs el az előadásról!", "Vigyázz, nehogy elkéss az előadásról!"],
                    ["Cenzúrázták a művet, hogy ne lázadjon fel a nép.", "Cenzúrázták a művet, nehogy fellázadjon a nép."],
                    ["Csitította a tömeget, hogy ne legyen rendbontás.", "Csitította a tömeget, nehogy rendbontás legyen."]
                ],
                "examples": [
                    {"spanish": "A cenzúra akadályozta a bemutatót, nehogy a közönség lázadásként értelmezze a művet.", "english": "Censorship obstructed the premiere lest the audience interpret the work as a rebellion."},
                    {"spanish": "Jókai csitította a tömeget, nehogy a lelkesedés rendbontásba csapjon át.", "english": "Jókai calmed the crowd so that the enthusiasm would not turn into disorder."},
                    {"spanish": "Időben megvettük a jegyeket a karzatra, nehogy lemaradjunk a díszelőadásról.", "english": "We bought the tickets for the gallery in time lest we miss the gala performance."}
                ],
                "tip": "Never combine nehogy with ne (*nehogy ne késs el* is double negation). Use either hogy ne késs el OR nehogy elkéss."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "pairs": [
                        ["díszelőadás", "gala performance"],
                        ["tragédia", "tragedy"],
                        ["rivaldafény", "footlights / limelight"],
                        ["karzat", "gallery / balcony"],
                        ["udvaronc", "courtier"],
                        ["műsorra tűz", "to put on the program"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "question": "Ki mondja el a Bánk bánban a szegény jobbágyok keserű panaszát?",
                    "options": ["Tiborc", "Egressy Gábor", "Gertrudis királyné", "Meráni Ottó"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "sentence": "Egressy Gábor kokárdával a mellén lépett a _____ elé 1848. március 15-én.",
                    "answer": "rivaldafény",
                    "english": "Gábor Egressy stepped before the footlights with a cockade on his chest on March 15, 1848."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "question": "Choose the grammatically correct sentence with 'nehogy':",
                    "options": [
                        "A cenzúra betiltotta a darabot, nehogy zavargás törjön ki.",
                        "A cenzúra betiltotta a darabot, nehogy zavargás kitör.",
                        "A cenzúra betiltotta a darabot, nehogy ne törjön ki zavargás.",
                        "A cenzúra betiltotta a darabot, nehogy zavargás tört ki."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "sentence": "Jókai Mór a karzatról csitította a tömeget, _____ a lelkesedés rendbontásba csapjon át.",
                    "answer": "nehogy",
                    "english": "Mór Jókai calmed the crowd from the balcony lest the enthusiasm turn into disorder."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "tiles": ["Vigyáztak,", "nehogy", "a", "hatóságok", "bezárják", "a", "színházat."],
                    "solution": ["Vigyáztak,", "nehogy", "a", "hatóságok", "bezárják", "a", "színházat."],
                    "english": "They were careful lest the authorities close down the theatre."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "prompt": [
                        {"speaker": "Diák", "text": "Miért nem engedélyezte a cenzúra évtizedekig a Bánk bán pesti bemutatóját?"},
                        {"speaker": "Tanár", "text": "_____"}
                    ],
                    "options": [
                        "Attól tartottak, nehogy a közönség az idegen udvaroncok elleni lázadásként értelmezze a drámát.",
                        "Mert Katona József kérte, hogy soha ne tűzzék műsorra a darabot.",
                        "Hogy a nézők inkább operettet nézzenek a Nemzeti Színházban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mi történt 1848. március 15-én este a Nemzeti Színházban?",
                    "options": [
                        "A Bánk bán díszelőadását félbeszakítva a közönség a Nemzeti dalt és a Himnuszt követelte.",
                        "A császári katonaság bezárta a színházat, mielőtt a függöny felgördült volna.",
                        "Katona József személyesen olvasta fel a Tizenkét pontot a színpadon."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "The Rise of the Vígszínház and Urban Comedy",
            "grammar_label": "Jussive and concessive subjunctive clauses (akárhogy is + -jon/-jen)",
            "goals": [
                "I can explain how the Vígszínház (1896) and Molnár Ferenc modernized Hungarian theatre.",
                "I can use third-person jussive clauses (hadd + -jon/-jen, legyen) and concessive subjunctives.",
                "I can talk about bourgeois comedy, dramaturgy, and international theatrical success."
            ],
            "story_segment": {
                "seg_slug": "vigszinhaz",
                "title": "A Vígszínház csillogása és Molnár Ferenc világsikere",
                "summary": "Opened in 1896 on the Grand Boulevard, the Vígszínház introduced naturalism, sparkling urban comedy, and the international hits of Ferenc Molnár.",
                "location": "Budapest, Szent István körút (1896–1920-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Miközben a Nemzeti Színház a patetikus szavalóművészet és a történelmi tragédiák fellegvára maradt, a gyorsan polgárosodó Budapestnek új, modern színpadra volt szüksége. 1896-ban, a millennium évében nyílt meg a Nagykörúton a Vígszínház, amelynek aranyozott, neobarokk nézőtere a fővárosi polgárság kedvenc találkozóhelyévé vált."
                    },
                    {
                        "type": "narration",
                        "text": "A Vígszínház első igazgatója, Ditrói Mór megkövetelte a társulattól, hogy a színészek hagyjanak fel a mesterkélt deklamálással, és úgy beszéljenek a színpadon, ahogyan az emberek a pesti szalonokban és kávéházakban társalognak. Hadd lássa a közönség a saját mindennapi életét, szerelmi bonyodalmait és társadalmi ellentmondásait a tükörben!"
                    },
                    {
                        "type": "narration",
                        "text": "Ebben a szellemi műhelyben bontakozott ki Molnár Ferenc drámaírói zsenije, akinek Liliom, A testőr és Játék a kastélyban című vígjátékai néhány éven belül meghódították Bécset, Berlint, Párizst és a New York-i Broadwayt is. Molnár mesterien értett ahhoz, hogy a szellemes párbeszédek mögött felsejtsen valami kesernyés emberi líra, nehogy a vígjáték puszta bohózattá silányuljon."
                    },
                    {
                        "type": "narration",
                        "text": "A Liliom címszereplője, a városligeti körhintás legény egyszerre nyers és végtelenül esendő figura, akinek sorsa még a legkeményebb kritikusokat is meghatotta. Akárhogy is ítélje meg a külvilág a külvárosi csavargót, Molnár drámája bebizonyította, hogy az igazi költészet a hétköznapi sorsokban rejlik."
                    },
                    {
                        "type": "narration",
                        "text": "A két világháború között a budapesti színházi élet olyan pezsgővé vált, hogy az európai színházigazgatók rendszeresen Pestre utaztak, hogy elsőként vásárolják meg a legújabb magyar színdarabok előadási jogát."
                    }
                ]
            },
            "words": [
                {"lemma": "vígjáték", "translation": "comedy (play)", "pos": "noun"},
                {"lemma": "társulat", "translation": "theatre company / troupe", "pos": "noun"},
                {"lemma": "címszereplő", "translation": "title character / protagonist", "pos": "noun"},
                {"lemma": "párbeszéd", "translation": "dialogue", "pos": "noun"},
                {"lemma": "bohózat", "translation": "farce", "pos": "noun"},
                {"lemma": "előadási jog", "translation": "performance rights", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "jussive-hadd-subjunctive",
                "title": "Jussive Clauses (hadd + Subjunctive) & Concessive Subjunctives",
                "text1_title": "Third-Person Jussive with hadd + Subjunctive",
                "text1": "To express 'let someone do something' or 'allow something to happen' in the 1st plural or 3rd person, Hungarian pairs the particle hadd with the subjunctive mood: Hadd lássa a közönség a saját életét! ('Let the audience see its own life!'), Hadd beszéljenek természetesen a színészek! ('Let the actors speak naturally!').",
                "text2_title": "Concessive Clauses with akárhogy / bármilyen + Subjunctive",
                "text2": "Universal concessive expressions meaning 'no matter how / however much' (akárhogy is, bármennyire is, bárki) frequently take the subjunctive at B2 to emphasize hypothetical or generalized concession: Akárhogy is ítélje meg a külvilág ('However the outside world may judge him...').",
                "table_title": "Jussive & Concessive Subjunctive Patterns",
                "table_rows": [
                    ["hadd + -jon/-jen/-ja/-je", "Hadd lássa a közönség az igazságot! (Let the audience see the truth!)"],
                    ["hogy + felhagyjon valamivel", "Megkövetelte, hogy a társulat hagyjon fel a deklamálással."],
                    ["akárhogy is + subjunctive", "Akárhogy is ítélje meg a kritika, a darab világsiker lett."],
                    ["nehogy + silányuljon", "Lírát csempészett a műbe, nehogy puszta bohózattá silányuljon."]
                ],
                "examples": [
                    {"spanish": "Hadd lássa a közönség a saját mindennapi életét a színpadon!", "english": "Let the audience see its own everyday life on stage!"},
                    {"spanish": "Ditrói Mór megkövetelte, hogy a színészek hagyjanak fel a mesterkélt szavalással.", "english": "Mór Ditrói demanded that the actors abandon artificial declamation."},
                    {"spanish": "Akárhogy is ítélje meg a külvilág Liliomot, a sorsa mindenkit meghat.", "english": "However the outside world may judge Liliom, his fate moves everyone."}
                ],
                "tip": "Notice that after hadd, the verbal prefix stays attached to the verb (Hadd mondja el a véleményét!), because hadd itself occupies the pre-verbal slot."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "pairs": [
                        ["vígjáték", "comedy (play)"],
                        ["társulat", "theatre company / troupe"],
                        ["címszereplő", "title character"],
                        ["párbeszéd", "dialogue"],
                        ["bohózat", "farce"],
                        ["előadási jog", "performance rights"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "question": "Milyen változást hozott a Vígszínház a magyar színjátszásban 1896 után?",
                    "options": [
                        "A mesterkélt szavalás helyett természetes, polgári társalgási stílust honosított meg.",
                        "Kizárólag középkori latin nyelvű drámákat tűzött műsorra.",
                        "Betiltotta a párbeszédeket, és néma pantomimet játszott."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "sentence": "Molnár Ferenc ügyelt arra, hogy a szellemes _____ mögött mindig legyen emberi érzelem is.",
                    "answer": "párbeszéd",
                    "english": "Ferenc Molnár took care that behind the witty dialogue there was always human emotion as well."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "question": "Which form correctly completes the jussive sentence: 'Hadd _____ a közönség a saját életét a színpadon!'?",
                    "options": ["lássa", "lát", "látta", "látni"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "sentence": "Molnár lírát szőtt a darabba, nehogy a vígjáték puszta bohózattá _____. (silányul)",
                    "answer": "silányuljon",
                    "english": "Molnár wove lyricism into the play lest the comedy degenerate into mere farce."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "tiles": ["Megkövetelte,", "hogy", "a", "társulat", "hagyjon", "fel", "a", "mesterkélt", "szavalással."],
                    "solution": ["Megkövetelte,", "hogy", "a", "társulat", "hagyjon", "fel", "a", "mesterkélt", "szavalással."],
                    "english": "He demanded that the company abandon artificial declamation."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "prompt": [
                        {"speaker": "Kritikus", "text": "Miért utaztak a külföldi színházigazgatók olyan gyakran Budapestre a húszas években?"},
                        {"speaker": "Színháztörténész", "text": "_____"}
                    ],
                    "options": [
                        "Azért jöttek, hogy elsőként vásárolják meg a legújabb magyar vígjátékok előadási jogát.",
                        "Nehogy megismerjék Molnár Ferenc darabjait a Broadwayn.",
                        "Mert a Vígszínházban nem volt sem társulat, sem nézőtér."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Ki a Molnár Ferenc által írt Liliom címszereplője?",
                    "options": [
                        "Egy városligeti körhintás legény, aki egyszerre nyers és esendő figura.",
                        "Egy tizenharmadik századi magyar nádor a királyi udvarban.",
                        "A Vígszínház alapító igazgatója."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Budapest Operetta Conquers the World",
            "grammar_label": "Subjunctive after verbs of fear and precaution (attól tart, hogy / nehogy)",
            "goals": [
                "I can discuss the golden age of Hungarian operetta (Lehár Ferenc, Kálmán Imre).",
                "I can distinguish between attól tart, hogy + indicative and attól tart, nehogy + subjunctive.",
                "I can describe musical theatre roles (primadonna, bonviván, szubrett, táncoskomikus)."
            ],
            "story_segment": {
                "seg_slug": "operettvilag",
                "title": "A csárdáskirálynőtől A víg özvegyig",
                "summary": "Lehár Ferenc and Kálmán Imre fused Viennese waltz elegance with fiery Hungarian csárdás rhythms, turning Budapest operetta into a global phenomenon.",
                "location": "Budapest, Nagymező utca – Budapesti Operettszínház",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század első évtizedeiben a pesti Nagymező utca — a „pesti Broadway” — zenétől és pezsgődurranástól volt hangos. Lehár Ferenc A víg özvegy és Kálmán Imre A csárdáskirálynő című műveivel olyan zenei nyelvet teremtett, amely a bécsi keringő eleganciáját a magyar csárdás tüzes ritmusával ötvözte."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar operett szigorú szerepkörökre épült, hogy a közönség minden előadáson megkapja a maga romantikus álmát és felszabadult humorát. A primadonna és a bonviván szerelmi kettősei a nagy érzelmeket hordozták, míg a szubrett és a táncoskomikus akrobatikus tánca és szellemes riposztjai gondoskodtak arról, nehogy az előadás túlságosan érzelgőssé váljon."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Kálmán Imre 1915-ben, az első világháború kellős közepén bemutatta A csárdáskirálynőt, sokan attól tartottak, nehogy a háborús gyász idején ízléstelennek tűnjön a csillogó mulatság. A mű azonban éppen azért aratott elsöprő diadalt, mert az összeomló monarchia társadalmának groteszk görbe tükrét mutatta fel."
                    },
                    {
                        "type": "narration",
                        "text": "Fedák Sári és Honthy Hanna legendás primadonnák voltak, akiknek minden mozdulatát és kalapját utánozták a pesti hölgyek. A karmesterek és rendezők kínosan ügyeltek a tempóra, nehogy egyetlen poén vagy magas hang is elvesszen a zenekari árok robajában."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar operett dallamai Londontól Tokióig máig teltházas előadásokon csendülnek fel, bizonyítva, hogy a könnyednek tűnő műfaj mögött rendkívüli zenei és színpadi mesterségbeli tudás áll."
                    }
                ]
            },
            "words": [
                {"lemma": "operett", "translation": "operetta", "pos": "noun"},
                {"lemma": "primadonna", "translation": "prima donna / leading soprano", "pos": "noun"},
                {"lemma": "bonviván", "translation": "bon vivant / leading romantic tenor", "pos": "noun"},
                {"lemma": "zenekari árok", "translation": "orchestra pit", "pos": "expression"},
                {"lemma": "karmester", "translation": "conductor", "pos": "noun"},
                {"lemma": "teltházas", "translation": "sold-out / full-house", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "fear-precaution-nehogy",
                "title": "Expressions of Fear & Precaution: attól tart / gondoskodik róla, nehogy",
                "text1_title": "Fearing Something Might Happen: attól tart, nehogy + Subjunctive",
                "text1": "After verbs of fear or anxiety (attól tart, fél attól, aggódik), Hungarian speakers use either hogy + future/indicative (attól tartottak, hogy ízléstelen lesz) OR nehogy + subjunctive (attól tartottak, nehogy ízléstelennek tűnjön). Remember that here nehogy means 'that ... might' (positive fear in English), NOT 'that ... might not'!",
                "text2_title": "Precautionary Verbs: gondoskodik róla / ügyel rá, nehogy",
                "text2": "Verbs of care and precaution (gondoskodik arról, kínosan ügyel arra, vigyáz arra) pair naturally with nehogy + subjunctive to express preventing a flaw: gondoskodtak arról, nehogy az előadás érzelgőssé váljon ('they saw to it that the performance did not become overly sentimental').",
                "table_title": "Fear & Precaution Constructions at B2",
                "table_rows": [
                    ["attól tart, nehogy + subjunctive", "Attól tartottak, nehogy ízléstelennek tűnjön a mulatság."],
                    ["gondoskodik arról, nehogy + subj.", "A szubrett gondoskodott arról, nehogy érzelgőssé váljon a darab."],
                    ["kínosan ügyel arra, nehogy + subj.", "A karmester ügyelt arra, nehogy egyetlen poén is elvesszen."],
                    ["vigyáz, nehogy + subjunctive", "A bonviván vigyázott, nehogy elkéssen a belépőjével."]
                ],
                "examples": [
                    {"spanish": "Sokan attól tartottak, nehogy a háború idején ízléstelennek tűnjön az operett.", "english": "Many feared that during wartime the operetta might seem in poor taste."},
                    {"spanish": "A táncoskomikus gondoskodott arról, nehogy az előadás túlságosan érzelgőssé váljon.", "english": "The comic dancer saw to it that the performance did not become overly sentimental."},
                    {"spanish": "A karmester ügyelt a tempóra, nehogy egyetlen magas hang is elvesszen a zenekari árokban.", "english": "The conductor watched the tempo lest a single high note be lost in the orchestra pit."}
                ],
                "tip": "Be careful translating 'attól tartok, nehogy elvesszen': in English this means 'I am afraid it might get lost' (NOT 'might not get lost'). The nehogy reflects the speaker's desire that the feared event NOT happen."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "pairs": [
                        ["operett", "operetta"],
                        ["primadonna", "leading soprano"],
                        ["bonviván", "leading romantic tenor"],
                        ["zenekari árok", "orchestra pit"],
                        ["karmester", "conductor"],
                        ["teltházas", "sold-out / full-house"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "question": "Melyik két zenei világot ötvözte Lehár Ferenc és Kálmán Imre operettművészete?",
                    "options": [
                        "A bécsi keringő eleganciáját és a magyar csárdás tüzes ritmusát.",
                        "Az olasz barokk operát és az amerikai dzsesszt.",
                        "A középkori egyházi éneket és a francia sanzont."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "sentence": "A _____ pálcájának intésére felcsendült a nyitány a zenekari árokban.",
                    "answer": "karmester",
                    "english": "At the cue of the conductor's baton, the overture sounded in the orchestra pit."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "question": "What does 'Attól tartottak, nehogy ízléstelennek tűnjön a darab' mean in English?",
                    "options": [
                        "They feared that the play might seem in poor taste.",
                        "They feared that the play would not seem in poor taste.",
                        "They hoped that the play would seem in poor taste.",
                        "They knew that the play was in poor taste."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "sentence": "A karmester kínosan ügyelt a tempóra, nehogy egyetlen poén is _____ a zenekari árok robajában. (elveszik - 3rd sg. subjunctive)",
                    "answer": "elvesszen",
                    "english": "The conductor carefully watched the tempo lest a single punchline be lost in the roar of the orchestra pit."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "tiles": ["Gondoskodtak", "arról,", "nehogy", "az", "előadás", "túlságosan", "érzelgőssé", "váljon."],
                    "solution": ["Gondoskodtak", "arról,", "nehogy", "az", "előadás", "túlságosan", "érzelgőssé", "váljon."],
                    "english": "They saw to it that the performance did not become overly sentimental."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "prompt": [
                        {"speaker": "Rendező", "text": "Miért olyan fontos a szubrett és a táncoskomikus szerepe az operettben?"},
                        {"speaker": "Primadonna", "text": "_____"}
                    ],
                    "options": [
                        "Az ő humoruk gondoskodik arról, nehogy az előadás túlságosan érzelgőssé váljon.",
                        "Hogy a karmester ne tudjon vezényelni a zenekari árokban.",
                        "Mert a bonviván soha nem énekel szerelmi kettőst."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mikor mutatta be Kálmán Imre A csárdáskirálynő című operettjét?",
                    "options": [
                        "1915-ben, az első világháború idején.",
                        "1837-ben, a Pesti Magyar Színház megnyitóján.",
                        "1956 őszén a Nemzeti Színházban."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Director's Vision vs. State Censorship",
            "grammar_label": "Subjunctive in indirect directives and elliptical warnings",
            "goals": [
                "I can analyze how Hungarian theatre used allegory and double-speak ('sorok között olvasás') under state censorship.",
                "I can use indirect directives (felszólít, utasít, figyelmeztet, hogy / nehogy) with full subjunctive precision.",
                "I can discuss staging, censorship categories (Tiltott, Tűrt, Támogatott), and artistic autonomy."
            ],
            "story_segment": {
                "seg_slug": "rendezoescenzor",
                "title": "Sorok között a színpadon: Rendezők és cenzorok",
                "summary": "During the decades of state socialism and the 'Three Ts' policy, Hungarian directors and actors turned classic plays and grotesques into coded conversations with the audience.",
                "location": "Budapest és Kaposvár (1960–1980-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század második felében a magyar kultúrpolitikát az úgynevezett „három T” — Tiltott, Tűrt, Támogatott — rendszere határozta meg. A minisztériumi cenzorok minden főpróbára beültek, hogy ellenőrizzék a rendezést, nehogy a színpadról a fennálló rendszert bíráló politikai utalás hangozzék el."
                    },
                    {
                        "type": "narration",
                        "text": "A színházművészet azonban éppen a korlátozások közepette fejlesztette tökélyre a „sorok közötti” beszéd művészetét. Ha egy kortárs darabot betiltottak, a rendezők Shakespeare, Molière vagy Madách Imre klasszikusait vették elő, és egyetlen hangsúllyal, díszletelemmel vagy jelmezzel elérték, hogy a nézőtér azonnal megértse a jelenre vonatkozó áthallást."
                    },
                    {
                        "type": "narration",
                        "text": "Örkény István groteszk tragikomédiái — mint a Tóték vagy a Macskajáték — zseniálisan ábrázolták a kisember kiszolgáltatottságát a zsarnoki hatalommal szemben. A hatóságok gyakran figyelmeztették a színházigazgatókat, nehogy túl messzire menjenek az iróniával, ám a közönség összekacsintását nem lehetett betiltani."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1970-es és 80-as években a vidéki műhelyek, különösen a kaposvári Csiky Gergely Színház, a művészi szabadság szigeteivé váltak. A fővárosi értelmiségiek vonatra ültek, hogy megnézzék a bátor kaposvári előadásokat, mielőtt a cenzúra esetleg levenné őket a műsorról."
                    },
                    {
                        "type": "narration",
                        "text": "Így maradt a magyar színpad a rendszerváltásig a társadalmi önvizsgálat legérzékenyebb helyszíne, ahol a kimondatlan szavak sokszor hangosabban szóltak, mint a hivatalos szónoklatok."
                    }
                ]
            },
            "words": [
                {"lemma": "főpróba", "translation": "dress rehearsal", "pos": "noun"},
                {"lemma": "cenzor", "translation": "censor", "pos": "noun"},
                {"lemma": "áthallás", "translation": "political double entendre / resonance", "pos": "noun"},
                {"lemma": "díszlet", "translation": "stage set / scenery", "pos": "noun"},
                {"lemma": "tragikomédia", "translation": "tragicomedy", "pos": "noun"},
                {"lemma": "sorok között olvas", "translation": "to read between the lines", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "indirect-directives-warnings",
                "title": "Indirect Directives, Warnings & Archaic/Literary Subjunctive (-jék)",
                "text1_title": "Directives and Warnings: figyelmeztet / utasít / eléri, hogy + Subjunctive",
                "text1": "Verbs of warning (figyelmeztet, óva int), command (utasít, felszólít), and achievement of effect (eléri, hogy) govern the subjunctive. When the warning is negative ('warned them not to go too far'), Hungarian uses either hogy ne menjenek túl messzire or nehogy túl messzire menjenek.",
                "text2_title": "Recognizing the Literary -jék Subjunctive Ending",
                "text2": "In elevated cultural and theatrical prose, you will encounter the classical 3rd-person singular -ik verb subjunctive ending -jék/-ják alongside modern -jon/-jen: nehogy politikai utalás hangozzék el (= hangozzon el), nehogy megismétlődjék (= megismétlődjön). Being able to recognize and interpret both forms is essential for reading B2-C1 Hungarian essays.",
                "table_title": "Indirect Directives & Literary Subjunctive Variants",
                "table_rows": [
                    ["figyelmeztet, nehogy + subj.", "Figyelmeztették az igazgatót, nehogy túl messzire menjen."],
                    ["eléri, hogy + subjunctive", "Egyetlen jelmezzel elérték, hogy a nézőtér megértse az áthallást."],
                    ["Modern: hangozzon el", "Literary: nehogy politikai utalás hangozzék el a színpadon."],
                    ["Modern: változzon meg", "Literary: nehogy a mű eredeti üzenete megváltozzék."]
                ],
                "examples": [
                    {"spanish": "A cenzorok beültek a főpróbára, nehogy politikai utalás hangozzék el.", "english": "The censors sat in on the dress rehearsal lest a political allusion be voiced."},
                    {"spanish": "A rendező egyetlen díszletelemmel elérte, hogy a nézőtér megértse az áthallást.", "english": "With a single set piece, the director achieved that the audience understood the political double entendre."},
                    {"spanish": "Figyelmeztették a színházigazgatókat, nehogy túl messzire menjenek az iróniával.", "english": "They warned the theatre directors not to go too far with irony."}
                ],
                "tip": "Notice the difference between 'elérték, hogy a nézők megértették' (indicative: factual result 'they achieved the fact that the audience understood') and 'elérték, hogy a nézőtér megértse' (subjunctive: intentional artistic aim)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "pairs": [
                        ["főpróba", "dress rehearsal"],
                        ["cenzor", "censor"],
                        ["áthallás", "political double entendre"],
                        ["díszlet", "stage set / scenery"],
                        ["tragikomédia", "tragicomedy"],
                        ["sorok között olvas", "to read between the lines"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "question": "Mit jelentett a kultúrpolitikában a „három T” kifejezés?",
                    "options": [
                        "Tiltott, Tűrt, Támogatott.",
                        "Társulat, Tragédia, Tapsvihar.",
                        "Tudomány, Tehetség, Tisztelet."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-szinhazmuveszet-vocab"],
                    "sentence": "A nézők megtanultak a sorok között olvasni, és azonnal értették a politikai _____-t.",
                    "answer": "áthallás",
                    "english": "The spectators learned to read between the lines and immediately understood the political double entendre."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "question": "Which sentence correctly uses an indirect warning with 'nehogy'?",
                    "options": [
                        "A hatóságok figyelmeztették az igazgatót, nehogy túl messzire menjen az iróniával.",
                        "A hatóságok figyelmeztették az igazgatót, nehogy túl messzire megy az iróniával.",
                        "A hatóságok figyelmeztették az igazgatót, nehogy ne menjen túl messzire az iróniával.",
                        "A hatóságok figyelmeztették az igazgatót, nehogy túl messzire ment az iróniával."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "sentence": "A rendező egyetlen jelmezzel elérte, hogy a közönség azonnal _____ a rejtett üzenetet. (megért - 3rd sg. def. subjunctive)",
                    "answer": "megértse",
                    "english": "With a single costume, the director ensured that the audience immediately understood the hidden message."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "tiles": ["A", "cenzorok", "beültek", "a", "főpróbára,", "nehogy", "politikai", "utalás", "hangozzon", "el."],
                    "solution": ["A", "cenzorok", "beültek", "a", "főpróbára,", "nehogy", "politikai", "utalás", "hangozzon", "el."],
                    "english": "The censors sat in on the dress rehearsal lest a political allusion be voiced."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-nehogy-subjunctive"],
                    "prompt": [
                        {"speaker": "Dramaturg", "text": "Hogyan tudtak a rendezők mégis üzenetet közvetíteni, ha a kortárs darabot betiltották?"},
                        {"speaker": "Színész", "text": "_____"}
                    ],
                    "options": [
                        "Klasszikus drámákat vettek elő, és a díszlettel elérték, hogy a nézőtér megértse a jelenre vonatkozó áthallást.",
                        "Megkérték a cenzorokat, hogy írják át a tragikomédiát operetté.",
                        "Bezárták a kaposvári színházat, nehogy a közönség vonatra üljön."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik vidéki színház vált az 1970-es és 80-as években a magyar színházi megújulás és szabadság legendás műhelyévé?",
                    "options": [
                        "A kaposvári Csiky Gergely Színház.",
                        "A bécsi Burgtheater.",
                        "A pozsonyi városi színház."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can trace the evolution of Hungarian theatre from the 1837 National Theatre and 1848 Bánk bán to Molnár Ferenc, operetta, and state-socialist allegory.",
            "I can form positive purpose clauses with hogy + subjunctive (-jon/-jen) and negative purpose/precaution clauses with nehogy + subjunctive.",
            "I can use third-person jussive (hadd + subjunctive) and indirect directive structures accurately.",
            "I can employ 30 key B2 theatrical and cultural terms in context."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-szinhazmuveszet-vocab"],
                "pairs": [
                    ["közadakozás", "public donation"],
                    ["díszelőadás", "gala performance"],
                    ["címszereplő", "title character"],
                    ["zenekari árok", "orchestra pit"],
                    ["főpróba", "dress rehearsal"],
                    ["áthallás", "political double entendre"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-nehogy-subjunctive"],
                "question": "Which conjunction and verb mood are required to express 'lest / so that ... not' without adding a second 'ne'?",
                "options": [
                    "nehogy + subjunctive (-jon/-jen)",
                    "nehogy + ne + subjunctive",
                    "hogy + indicative present",
                    "mielőtt + past tense"
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-szinhazmuveszet-vocab"],
                "question": "Melyik fogalom jelenti a színházi előadás előtti utolsó, jelmezes és díszletes próbát?",
                "options": ["főpróba", "karzat", "közadakozás", "bohózat"],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-szinhazmuveszet-vocab"],
                "sentence": "A vándorszínészek után 1837-ben végre állandó magyar _____ nyílt Pesten.",
                "answer": "kőszínház",
                "english": "After the itinerant actors, a permanent Hungarian stone theatre finally opened in Pest in 1837."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-nehogy-subjunctive"],
                "sentence": "A polgárok összeadták a pénzt, nehogy a nemzeti ügy pénzhiány miatt _____. (elbukik - 3rd sg. subjunctive)",
                "answer": "elbukjon",
                "english": "The citizens pooled their money lest the national cause fail due to lack of funds."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-nehogy-subjunctive"],
                "sentence": "Ditrói Mór azt akarta, hogy a színészek természetesen _____ a színpadon. (beszél - 3rd pl. subjunctive)",
                "answer": "beszéljenek",
                "english": "Mór Ditrói wanted the actors to speak naturally on stage."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-nehogy-subjunctive"],
                "prompt": [
                    {"speaker": "Karmester", "text": "Miért intetted óva a zenekart a második felvonás előtt?"},
                    {"speaker": "Rendező", "text": "_____"}
                ],
                "options": [
                    "Figyelmeztettem őket, nehogy túl hangosan játsszanak a primadonna halk áriája alatt.",
                    "Mert azt akartam, hogy a nézőtér azonnal hazamegy.",
                    "Hogy nehogy ne hallja a cenzor a szöveget."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-nehogy-subjunctive"],
                "question": "Choose the sentence that accurately expresses 'Let the audience judge the play for itself!':",
                "options": [
                    "Hadd ítélje meg a közönség maga a színdarabot!",
                    "Nehogy megítélje a közönség a színdarabot!",
                    "A közönség ítéli meg hadd a színdarabot!",
                    "Hogy a közönség megítélte a színdarabot!"
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-nehogy-subjunctive"],
                "prompt": [
                    {"speaker": "Néző", "text": "Siessünk a ruhatárhoz, már harangoztak a harmadik felvonásra!"},
                    {"speaker": "Barát", "text": "_____"}
                ],
                "options": [
                    "Igazad van, foglaljuk el gyorsan a helyünket, nehogy kizárjanak minket a nézőtérről!",
                    "Maradjunk a büfében, hogy pontosan látjuk a díszletet!",
                    "Sietünk, nehogy ne maradjunk le a függönyről!"
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-nehogy-subjunctive"],
                "tiles": ["A", "karmester", "ügyelt", "arra,", "nehogy", "egyetlen", "hang", "is", "elvesszen."],
                "solution": ["A", "karmester", "ügyelt", "arra,", "nehogy", "egyetlen", "hang", "is", "elvesszen."],
                "english": "The conductor took care lest even a single note be lost."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-nehogy-subjunctive"],
                "tiles": ["Hadd", "szólaljon", "meg", "a", "magyar", "szó", "minden", "színpadon!"],
                "solution": ["Hadd", "szólaljon", "meg", "a", "magyar", "szó", "minden", "színpadon!"],
                "english": "Let the Hungarian word be heard on every stage!"
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-nehogy-subjunctive"],
                "template": [
                    {
                        "prompt": "Write a sentence explaining why Hungarian citizens donated money in the 1830s (use 'nehogy' + subjunctive).",
                        "answer": "A polgárok adományoztak, nehogy a nemzeti színház ügye pénzhiány miatt elbukjon."
                    },
                    {
                        "prompt": "Write a sentence explaining what directors wanted the audience to understand through classical plays (use 'hogy' + subjunctive).",
                        "answer": "A rendezők azt akarták, hogy a közönség a sorok között olvasva megértse a politikai áthallást."
                    }
                ]
            }
        ]
    }
}


UNIT_05_BARTOKKODALY = {
    "unit_num": 5,
    "slug": "bartokkodaly",
    "title": "Bartók, Kodály & the Ethnomusicological Revolution",
    "grammar_skill": "b2-frequentative-verbs",
    "vocab_skill": "b2-bartokkodaly-vocab",
    "theme": "Bartók, Kodály and Hungarian ethnomusicology",
    "location": "Erdély, Zeneakadémia és a magyar falvak",
    "intro_body": [
        "At the dawn of the 20th century, most urban Hungarians believed that 'Hungarian folk music' meant the sentimental gypsy-style table songs (magyar nóta) played in city cafés. Then two young composers from the Budapest Academy of Music—Béla Bartók and Zoltán Kodály—strapped heavy Edison wax-cylinder phonographs onto their backs and set out on foot into remote villages across the Carpathian Basin.",
        "What they recorded from elderly peasant singers was a revelation: an ancient, five-tone (pentatonic) musical layer dating back over a millennium to the Eurasian steppes. Their discovery not only transformed Bartók into one of the most radical modernists of 20th-century classical music, but also inspired the Kodály Concept—now a UNESCO World Heritage educational method—and the urban Táncház revival movement. Grammatically, you will master frequentative, iterative, and diminutive verb suffixes (-gat/-get, -dogál/-degél/-dögél) alongside distributive temporal expressions."
    ],
    "combined_story_title": "Fonográfhenger a faluvégen: Bartók és Kodály útja",
    "combined_story_summary": "How Béla Bartók and Zoltán Kodály trekked into remote villages with Edison phonograph cylinders to preserve ancient pentatonic folk songs, revolutionizing 20th-century classical composition and global music education.",
    "lessons": [
        {
            "num": 1,
            "title": "With Phonograph Cylinders into the Villages",
            "grammar_label": "Frequentative verbs with -gat/-get (repeated purposeful action)",
            "goals": [
                "I can describe how Bartók and Kodály recorded peasant singers using Edison wax cylinders.",
                "I can form and interpret frequentative verbs ending in -gat/-get (kérdezget, hallgat, jegyezget).",
                "I can use vocabulary related to fieldwork, archival recording, and oral tradition."
            ],
            "story_segment": {
                "seg_slug": "fonografhenger",
                "title": "Viaszhengerek a hátizsákban: Indulás a falvakba",
                "summary": "Beginning in 1905–1906, Kodály and Bartók travelled to isolated villages with Edison phonographs to capture authentic peasant singing before modernization erased it.",
                "location": "Nyitra vármegye és Csík (1905–1907)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1905 és 1906 nyarán két fiatal zeneszerző, Kodály Zoltán és Bartók Béla hátizsákot vett a vállára, és elindult a vasútvonalaktól távol eső falvakba. Magukkal vitték az Edison-féle fonográfot és egy láda törékeny viaszhengert, hogy eredeti hangzásában örökítsék meg az idős parasztasszonyok és pásztorok énekét."
                    },
                    {
                        "type": "narration",
                        "text": "A terepmunka korántsem volt egyszerű: a zeneszerzők napokon át gyalogoltak a poros dűlőutakon, és esténként türelmesen kérdezgették a falusiakat, ki ismeri még a legrégebbi dallamokat. Az idős énekesek eleinte gyanakodva nézegették a különös tölcséres szerkezetet, de amikor visszahallgatták a saját hangjukat a viaszhengerről, ámulatukban elmosolyodtak."
                    },
                    {
                        "type": "narration",
                        "text": "Bartókék nem elégedtek meg a puszta kottázással: minden egyes hajlítást, ritmikai szabadságot és tájszólást aprólékosan lejegyzetelgettek a gyűjtőfüzetükbe. Esténként, gyertyafény mellett órákig tisztogatták a hengereket és rendszerezgették a felvett strófákat."
                    },
                    {
                        "type": "narration",
                        "text": "Néhány évtized alatt több mint tízezer dallamot gyűjtöttek össze a Kárpát-medence magyar, román, szlovák és rutén falvaiban. Rájöttek, hogy a népdal nem múzeumi tárgy, hanem élő szellemi örökség, amely nemzedékről nemzedékre változgat, miközben megőrzi ősi magját."
                    },
                    {
                        "type": "narration",
                        "text": "Ezek a megsárgult gyűjtőfüzetek és sercegő fonográfhengerek ma a Zenetudományi Intézet legféltettebb kincsei, amelyek nélkül a magyar zenei identitás fele örökre feledésbe merült volna."
                    }
                ]
            },
            "words": [
                {"lemma": "fonográfhenger", "translation": "phonograph wax cylinder", "pos": "noun"},
                {"lemma": "terepmunka", "translation": "fieldwork", "pos": "noun"},
                {"lemma": "népdalgyűjtés", "translation": "folk-song collecting", "pos": "noun"},
                {"lemma": "kottázás", "translation": "musical notation / transcription", "pos": "noun"},
                {"lemma": "hajlítás", "translation": "vocal ornamentation / melisma", "pos": "noun"},
                {"lemma": "szellemi örökség", "translation": "intangible / intellectual heritage", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "frequentative-gat-get",
                "title": "Frequentative Verbs with -gat/-get (Iterative & Patient Action)",
                "text1_title": "Forming Iterative Verbs with -gat/-get",
                "text1": "In Hungarian, adding the suffix -gat (back vowel) or -get (front vowel) to a transitive or intransitive verb expresses an action performed repeatedly, in small increments, or with patient persistence over time. For instance, kérdez means 'to ask once', whereas kérdezget means 'to keep asking around patiently'; néz means 'to look', whereas nézeget means 'to examine / look over repeatedly'.",
                "text2_title": "Linking Vowels (-ogat/-eget/-öget)",
                "text2": "After stems ending in two consonants or a long vowel + consonant, a linking vowel is inserted before -gat/-get: tisztít -> tisztogat ('to clean repeatedly/carefully'), írogat ('to jot down from time to time'), néz -> nézeget, töröl -> törölget.",
                "table_title": "Base Verb vs. Frequentative -gat/-get Verb",
                "table_rows": [
                    ["kérdez (asks)", "kérdezget (asks around repeatedly / interviews patiently)"],
                    ["néz (looks)", "nézeget (examines / looks over again and again)"],
                    ["rendszerez (systematizes)", "rendszerezget (sorts and organizes bit by bit)"],
                    ["tisztít (cleans)", "tisztogat (cleans carefully one after another)"]
                ],
                "examples": [
                    {"spanish": "Esténként türelmesen kérdezgették a falusiakat a régi dallamokról.", "english": "In the evenings they patiently asked the villagers around about the old melodies."},
                    {"spanish": "Az idős énekesek gyanakodva nézegették a különös tölcséres fonográfot.", "english": "The elderly singers kept eyeing the strange horn-shaped phonograph suspiciously."},
                    {"spanish": "Gyertyafény mellett órákig tisztogatták a viaszhengereket.", "english": "By candlelight they carefully cleaned the wax cylinders for hours."}
                ],
                "tip": "Note that hallgat ('to listen to' / 'to remain silent') was historically a -gat derivative of hall ('to hear'), which lexicalized into an everyday verb!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "pairs": [
                        ["fonográfhenger", "phonograph wax cylinder"],
                        ["terepmunka", "fieldwork"],
                        ["népdalgyűjtés", "folk-song collecting"],
                        ["kottázás", "musical transcription"],
                        ["hajlítás", "vocal ornamentation"],
                        ["szellemi örökség", "intangible heritage"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "question": "Milyen eszközzel rögzítették Bartókék az idős falusi énekesek hangját 1906-ban?",
                    "options": [
                        "Edison-féle fonográffal és viaszhengerekkel.",
                        "Digitális szalagos magnetofonnal a stúdióban.",
                        "Csak emlékezetből, hangfelvétel nélkül."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "sentence": "A zeneszerzők minden apró ritmikai szabadságot és énekesi _____-t lejegyeztek a kottában.",
                    "answer": "hajlítás",
                    "english": "The composers noted down every tiny rhythmic liberty and vocal ornamentation in the score."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-frequentative-verbs"],
                    "question": "What nuance does 'kérdezgették a falusiakat' add compared to 'megkérdezték a falusiakat'?",
                    "options": [
                        "It expresses repeated, patient questioning of multiple villagers over time.",
                        "It indicates that they asked only a single question and left immediately.",
                        "It puts the verb into the passive conditional mood.",
                        "It means they refused to ask the villagers anything."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "sentence": "Az idős asszonyok eleinte gyanakodva _____ a különös tölcséres gépet. (néz - frequentative 3rd pl. past def.)",
                    "answer": "nézegették",
                    "english": "At first the elderly women kept looking over the strange horn-shaped machine suspiciously."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "tiles": ["Gyertyafény", "mellett", "órákig", "tisztogatták", "a", "törékeny", "viaszhengereket."],
                    "solution": ["Gyertyafény", "mellett", "órákig", "tisztogatták", "a", "törékeny", "viaszhengereket."],
                    "english": "By candlelight they carefully cleaned the fragile wax cylinders for hours."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-frequentative-verbs"],
                    "prompt": [
                        {"speaker": "Zenetörténész", "text": "Mit csináltak a kutatók esténként, miután véget ért a falusi terepmunka?"},
                        {"speaker": "Archivista", "text": "_____"}
                    ],
                    "options": [
                        "Órákon át rendszerezgették a felvett strófákat, és tisztogatták a fonográfhengereket.",
                        "Elfelejtették a kottázást, mert nem volt náluk gyűjtőfüzet.",
                        "Csak egyszer kérdezték meg a városi zenészeket."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Hogyan reagáltak a falusi énekesek, amikor először visszahallgatták a saját hangjukat a fonográfhengerről?",
                    "options": [
                        "Ámulatukban elmosolyodtak, és feloldódott a kezdeti gyanakvásuk.",
                        "Összetörték a viaszhengereket, és elzavarták a kutatókat.",
                        "Pénzt követeltek minden egyes elénekelt strófáért."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Urban Nóta vs. Ancient Pentatonic Folk Song",
            "grammar_label": "Diminutive-frequentative verbs (-dogál/-degél/-dögél)",
            "goals": [
                "I can explain the difference between 19th-century urban magyar nóta and ancient pentatonic peasant songs.",
                "I can use contemplative/leisurely frequentative verbs ending in -dogál/-degél/-dögél.",
                "I can describe musical structures such as pentatónia, ereszkedő dallamív, and parlando-rubato."
            ],
            "story_segment": {
                "seg_slug": "pentatonnepdal",
                "title": "Városi magyar nóta vagy ősi pentaton népdal?",
                "summary": "Bartók and Kodály proved that the popular urban 'magyar nóta' was composed 19th-century salon music, whereas true peasant music preserved an ancient Eurasian pentatonic scale.",
                "location": "Csík és Gyergyó (Erdély, 1907)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A tizenkilencedik század végén a városi közönség meg volt győződve arról, hogy a kávéházakban és vendéglőkben cigányzenekarok által húzott „magyar nóta” azonos az ősi magyar népzenével. Amikor a polgárok borozgatás közben dúdolgatták ezeket az érzelmes műdalokat, nem is sejtették, hogy valójában tizenkilencedik századi városi szerzők szerzeményeit hallgatják."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Bartók Béla 1907 nyarán a székelyföldi Csík vármegyébe érkezett, és a hegyi falvakban üldögélve hallgatta az idős parasztok énekét, tudományos villámcsapásként érte a felismerés. Az ottani dallamok nem a nyugati dúr-moll hangrendszerre épültek, hanem egy félhangok nélküli, ötfokú — úgynevezett pentaton — skálára."
                    },
                    {
                        "type": "narration",
                        "text": "Ezek az ősi, ereszkedő dallamívű vagy kvintváltó énekek pontosan olyan szerkezetet mutattak, mint a belső-ázsiai és volgai rokon népek dallamai. A pásztorok a nyáj mellett mendegélve vagy a fonóban beszélgetve évszázadokon át szinte változatlanul őrizték meg a honfoglalás előtti zenei anyanyelvet."
                    },
                    {
                        "type": "narration",
                        "text": "Bartók két fő előadásmódot különböztetett meg a régi stílusú népdalokban: a beszédszerűen szabad, díszített parlando-rubato éneklést, valamint a feszes, táncos tempójú giusto előadást. Mindkettő éles ellentétben állt a városi szalonok szentimentális műdalaival."
                    },
                    {
                        "type": "narration",
                        "text": "Kodály és Bartók közös kiadványai alapjaiban rengették meg a korabeli zenei közvéleményt, mert igazolták, hogy a valódi parasztzene a legmagasabb rendű klasszikus művészettel egyenrangú tökéletességet hordoz."
                    }
                ]
            },
            "words": [
                {"lemma": "pentaton", "translation": "pentatonic (five-tone scale)", "pos": "adjective"},
                {"lemma": "műdal", "translation": "composed popular song / art song", "pos": "noun"},
                {"lemma": "dallamív", "translation": "melodic arch / contour", "pos": "noun"},
                {"lemma": "kvintváltó", "translation": "fifth-shifting (melodic structure)", "pos": "adjective"},
                {"lemma": "hangrendszer", "translation": "tonal system / scale system", "pos": "noun"},
                {"lemma": "zenei anyanyelv", "translation": "musical mother tongue", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "diminutive-frequentative-dogal",
                "title": "Contemplative & Leisurely Frequentatives: -dogál / -degél / -dögél",
                "text1_title": "Uncharried, Continuous Actions with -dogál/-degél/-dögél",
                "text1": "While -gat/-get expresses active, repeated effort, the compound suffix -dogál (back), -degél (unrounded front), and -dögél (rounded front) conveys an unhurried, peaceful, or contemplative ongoing action ('sitting around quietly', 'strolling along slowly', 'living modestly'): ül -> üldögél ('sits quietly for a while'), megy -> mendegél ('strolls/ambles along'), él -> éldegél ('lives quietly').",
                "text2_title": "Combining -gat/-get and -dogál/-degél with Adverbial Participles",
                "text2": "In narrative prose, these suffixes often combine with -va/-ve adverbial participles or közben phrases to paint a vivid background scene: a hegyi falvakban üldögélve ('sitting quietly in the mountain villages'), a nyáj mellett mendegélve ('ambling along beside the flock'), borozgatás közben dúdolgatták ('they hummed while sipping wine').",
                "table_title": "Standard Verb vs. -dogál / -degél / -dögél",
                "table_rows": [
                    ["ül (sits)", "üldögél (sits leisurely / lingers quietly)"],
                    ["megy (goes / walks)", "mendegél (ambles / strolls along unhurriedly)"],
                    ["áll (stands)", "álldogál (stands around waiting / lingers)"],
                    ["él (lives)", "éldegél (lives quietly / gets by peacefully)"]
                ],
                "examples": [
                    {"spanish": "A polgárok borozgatás közben dúdolgatták a városi műdalokat.", "english": "While sipping wine, the townspeople hummed the urban composed songs."},
                    {"spanish": "Bartók a csíki falvakban üldögélve hallgatta az idős parasztok énekét.", "english": "Sitting quietly in the villages of Csík, Bartók listened to the singing of the elderly peasants."},
                    {"spanish": "A pásztorok a nyáj mellett mendegélve őrizték meg az ősi pentaton dallamokat.", "english": "Strolling along beside the flock, the shepherds preserved the ancient pentatonic melodies."}
                ],
                "tip": "Notice the Irregular Stem in megy -> mendegél (preserving the historical nasal stem men-, just like menni / mentem)!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "pairs": [
                        ["pentaton", "pentatonic (five-tone)"],
                        ["műdal", "composed popular song"],
                        ["dallamív", "melodic contour"],
                        ["kvintváltó", "fifth-shifting"],
                        ["hangrendszer", "tonal system"],
                        ["zenei anyanyelv", "musical mother tongue"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "question": "Milyen hangrendszerre épülnek a legősibb magyar népdalok, amelyeket Bartók Csíkban fedezett fel?",
                    "options": [
                        "Félhangok nélküli, ötfokú (pentaton) skálára.",
                        "Kizárólag a tizenkilencedik századi bécsi keringő akkordjaira.",
                        "Tizenkét fokú elektronikus hangsorra."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "sentence": "A városi vendéglőkben játszott „magyar nóta” valójában tizenkilencedik századi szerzők által írt _____ volt.",
                    "answer": "műdal",
                    "english": "The 'magyar nóta' played in urban restaurants was actually a composed song written by 19th-century authors."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-frequentative-verbs"],
                    "question": "Which verb means 'to stroll / amble along unhurriedly' (derived from 'megy')?",
                    "options": ["mendegél", "megyeget", "méndogál", "mentegel"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "sentence": "A zeneszerző a tornácon _____ hallgatta a székely asszonyok énekét. (üldögél - adverbial participle)",
                    "answer": "üldögélve",
                    "english": "Sitting quietly on the porch, the composer listened to the singing of the Székely women."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "tiles": ["A", "polgárok", "borozgatás", "közben", "dúdolgatták", "a", "népszerű", "műdalokat."],
                    "solution": ["A", "polgárok", "borozgatás", "közben", "dúdolgatták", "a", "népszerű", "műdalokat."],
                    "english": "While sipping wine, the citizens hummed the popular composed songs."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-frequentative-verbs"],
                    "prompt": [
                        {"speaker": "Hallgató", "text": "Mi a különbség az „ül” és az „üldögél” ige jelentésárnyalata között?"},
                        {"speaker": "Nyelvész", "text": "_____"}
                    ],
                    "options": [
                        "Az „üldögél” békés, ráérős, huzamosabb ideig tartó cselekvést fejez ki.",
                        "Az „üldögél” azt jelenti, hogy valaki dühösen felugrik a székről.",
                        "Semmi különbség nincs, az „üldögél” csak jövő időben használható."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit jelent a népdalok előadásában a „parlando-rubato” kifejezés?",
                    "options": [
                        "Beszédszerűen szabad, díszített, kötött tempó nélküli előadásmódot.",
                        "Feszes, katonás, tánclépésekhez igazodó tempót.",
                        "Zenekari kísérettel előadott városi operettáriát."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "Bartók's Radical Modernism",
            "grammar_label": "Distributive temporal expressions (évről évre, faluról falura) with iterative verbs",
            "goals": [
                "I can explain how Bartók integrated folk rhythms and pentatonic intervals into modern classical masterpieces.",
                "I can combine distributive reduplicated nouns (faluról falura, hangról hangra) with iterative verbs.",
                "I can discuss key Bartók works such as A kékszakállú herceg vára, A csodálatos mandarin, and Cantata Profana."
            ],
            "story_segment": {
                "seg_slug": "bartokmodernizmus",
                "title": "A parasztdaltól a modern koncertpódiumig",
                "summary": "Bartók fused the asymmetrical rhythms and pentatonic harmonies of peasant music with radical 20th-century modernism in Bluebeard's Castle, The Miraculous Mandarin, and Cantata Profana.",
                "location": "Budapest (Zeneakadémia) és az európai koncerttermek",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Bartók Béla számára a népdalgyűjtés nem nosztalgikus múltidézés volt, hanem a huszadik századi modern zeneszerzés megújításának kulcsa. Ahogy faluról falura járogatott a Kárpát-medencében, felismerte, hogy az ősi pentaton hangközök és a bolgár táncok aszimmetrikus ritmusai felszabadítják a zenét a tizenkilencedik századi romantika elcsépelt szabályai alól."
                    },
                    {
                        "type": "narration",
                        "text": "Balázs Béla szövegkönyvére komponált egyfelvonásos operája, A kékszakállú herceg vára 1918-ban került színpadra. A műben Judit ajtóról ajtóra nyitogatja a herceg komor várának hét titkos kamráját, miközben a zenekar a lélek legmélyebb magányát szólaltatja meg a magyar parlando-rubato hanglejtésével."
                    },
                    {
                        "type": "narration",
                        "text": "A csodálatos mandarin című táncjáték már a modern nagyváros kegyetlen, zakatoló világát vitte színpadra, olyan merész disszonanciákkal, hogy az 1926-os kölni ősbemutató után a polgármester erkölcsi okokra hivatkozva betiltotta az előadást. Bartók azonban rendíthetetlenül csiszolgatta saját zenei nyelvét, amelyben a természet éjszakai neszei és a paraszti ritmusok szerves egységgé olvadtak össze."
                    },
                    {
                        "type": "narration",
                        "text": "1930-ban született meg a Cantata Profana — A kilenc csodaszarvas —, amely egy román kolinda nyomán meséli el a szarvassá változott fiúk történetét. A szarvasok már nem térhetnek vissza az apai házba, mert agancsuk nem fér be az ajtón: csak a tiszta forrásvízből ihatnak."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Európában eluralkodott a fasizmus, Bartók 1940-ben tiltakozásul elhagyta Magyarországot, és az Egyesült Államokba emigrált, ám utolsó műveiben — köztük a Concertóban — is szülőföldje dallamait idézgette meg."
                    }
                ]
            },
            "words": [
                {"lemma": "zeneszerzés", "translation": "musical composition", "pos": "noun"},
                {"lemma": "disszonancia", "translation": "dissonance", "pos": "noun"},
                {"lemma": "ősbemutató", "translation": "world premiere", "pos": "noun"},
                {"lemma": "szövegkönyv", "translation": "libretto", "pos": "noun"},
                {"lemma": "aszimmetrikus", "translation": "asymmetrical", "pos": "adjective"},
                {"lemma": "tiszta forrás", "translation": "pure source / spring", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "distributive-iterative-structures",
                "title": "Distributive Reduplication (faluról falura) + Iterative Verbs",
                "text1_title": "Pairing -ról/-ről ... -ra/-re with -gat/-get Verbs",
                "text1": "In B2 Hungarian, distributive noun phrases built with the pattern Noun-ról/-ről Noun-ra/-re ('from village to village', 'from door to door', 'from year to year') naturally pair with frequentative -gat/-get verbs to express systematic progression across multiple targets: Judit ajtóról ajtóra nyitogatja a kamrákat ('Judit opens the chambers door by door'); faluról falura járogatott ('he went from village to village').",
                "text2_title": "Refining & Evoking Over Time: csiszolgat, idézget, nyitogat",
                "text2": "Notice how -gat/-get transforms artistic verbs: csiszol ('polishes') -> csiszolgat ('continually refines/hones over years'), felidéz ('recalls once') -> idézget ('repeatedly evokes motifs of...'), kinyit ('opens once') -> nyitogat ('opens one after another').",
                "table_title": "Distributive Phrase + Frequentative Verb Combinations",
                "table_rows": [
                    ["faluról falura + járogat", "Faluról falura járogatott a Kárpát-medencében."],
                    ["ajtóról ajtóra + nyitogat", "Judit ajtóról ajtóra nyitogatja a hét titkos kamrát."],
                    ["évről évre + csiszolgat", "Évről évre csiszolgatta egyéni zenei nyelvét."],
                    ["műről műre + idézget", "Utolsó éveiben is szülőföldje dallamait idézgette meg."]
                ],
                "examples": [
                    {"spanish": "Judit ajtóról ajtóra nyitogatja a herceg várának hét titkos kamráját.", "english": "Judit opens the seven secret chambers of the duke's castle door by door."},
                    {"spanish": "Bartók rendíthetetlenül csiszolgatta saját modern zenei nyelvét.", "english": "Bartók steadfastly honed his own modern musical language."},
                    {"spanish": "Amerikai emigrációjában is szülőföldje dallamait idézgette meg.", "english": "Even in his American emigration, he repeatedly evoked the melodies of his homeland."}
                ],
                "tip": "When a verbal prefix is used with a frequentative verb to stress repeated evocation across multiple works, the prefix can either stay attached or follow in progressive aspect, e.g. dallamokat idézgetett fel / meg."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "pairs": [
                        ["zeneszerzés", "musical composition"],
                        ["disszonancia", "dissonance"],
                        ["ősbemutató", "world premiere"],
                        ["szövegkönyv", "libretto"],
                        ["aszimmetrikus", "asymmetrical"],
                        ["tiszta forrás", "pure source / spring"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "question": "Melyik Bartók-mű ér véget azzal a jelképes üzenettel, hogy a szarvassá változott fiúk már csak „tiszta forrásból” ihatnak?",
                    "options": [
                        "A Cantata Profana (A kilenc csodaszarvas).",
                        "A kékszakállú herceg vára.",
                        "A csárdáskirálynő."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "sentence": "A csodálatos mandarin 1926-os kölni _____-ja után a polgármester betiltotta a darabot.",
                    "answer": "ősbemutató",
                    "english": "After the 1926 Cologne world premiere of The Miraculous Mandarin, the mayor banned the piece."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-frequentative-verbs"],
                    "question": "Which sentence combines a distributive phrase with a frequentative verb to mean 'Judit opens the doors one after another'?",
                    "options": [
                        "Judit ajtóról ajtóra nyitogatja a vár kamráit.",
                        "Judit egy ajtóval kinyitotta a vár kamráit.",
                        "Judit ajtótól ajtóig nyitni fogja a kamrát.",
                        "Judit az ajtóban álldogált egyszer."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "sentence": "Bartók évtizedeken át rendíthetetlenül _____ egyéni zenei nyelvét. (csiszol - frequentative 3rd sg. past def.)",
                    "answer": "csiszolgatta",
                    "english": "For decades Bartók steadfastly honed his individual musical language."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "tiles": ["Judit", "ajtóról", "ajtóra", "nyitogatja", "a", "hét", "titkos", "kamrát."],
                    "solution": ["Judit", "ajtóról", "ajtóra", "nyitogatja", "a", "hét", "titkos", "kamrát."],
                    "english": "Judit opens the seven secret chambers door by door."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-frequentative-verbs"],
                    "prompt": [
                        {"speaker": "Zongorista", "text": "Hogyan hatott a népdalgyűjtés Bartók saját zeneszerzői stílusára?"},
                        {"speaker": "Zenekritikus", "text": "_____"}
                    ],
                    "options": [
                        "Ahogy faluról falura járogatott, az ősi pentaton hangközöket és ritmusokat beépítette a modern zenébe.",
                        "Lemondott a disszonanciáról, és csak tizenkilencedik századi keringőket írogatott.",
                        "Soha többé nem idézgette fel a magyar dallamokat."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Miért hagyta el Bartók Béla Magyarországot 1940-ben?",
                    "options": [
                        "Az európai fasizmus előretörése elleni erkölcsi tiltakozásul emigrált az Egyesült Államokba.",
                        "Mert kinevezték a kölni operaház főigazgatójává.",
                        "Mert nem érdekelték többé a Kárpát-medencei népdalok."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "The Kodály Concept: Music Belongs to Everyone",
            "grammar_label": "Habitual and pedagogical iterative verbs (énekelget, gyakorolgat, tapsolgat)",
            "goals": [
                "I can explain Zoltán Kodály's philosophy ('Legyen a zene mindenkié!') and relative solmization.",
                "I can use iterative verbs to describe step-by-step skill acquisition and classroom practice.",
                "I can discuss choral culture, musical literacy, and the Psalmus Hungaricus."
            ],
            "story_segment": {
                "seg_slug": "kodalymodszer",
                "title": "Legyen a zene mindenkié: A Kodály-módszer diadalútja",
                "summary": "Zoltán Kodály transformed music education across Hungary and the world through relative solmization, hand signs, choral singing, and folk songs as a child's musical mother tongue.",
                "location": "Budapest és Kecskemét (1923–1960-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Miközben Bartók a modern koncertzene határait feszegette, Kodály Zoltán arra tette fel az életét, hogy az egész magyar társadalmat megtanítsa zeneileg írni és olvasni. Híres jelmondata — „Legyen a zene mindenkié!” — azt hirdette, hogy a zenei műveltség nem kiváltságos kevesek luxusa, hanem minden gyermek alapvető joga."
                    },
                    {
                        "type": "narration",
                        "text": "Kodály megfigyelte, hogy az iskolákban silány minőségű, idegen dalocskákat énekelgetnek a gyerekekkel, ezért Ádám Jenővel közösen teljesen új énekkönyveket állított össze. Módszerének alapja az a meggyőződés volt, hogy a gyermeknek először a saját zenei anyanyelvét — vagyis a magyar népdalt — kell elsajátítania, mielőtt más népek klasszikus mesterműveit tanulmányozgatná."
                    },
                    {
                        "type": "narration",
                        "text": "A hangszervásárlás sok család számára túl drága lett volna, ám Kodály hangsúlyozta, hogy a legtökéletesebb hangszer, az emberi énekhang mindannyiunk torkában ott rejlik. Az iskolások napról napra kézjelekkel mutogatták a hangközöket, és a relatív szolmizáció — a dó-ré-mi-fá-szó-lá-ti — segítségével könnyedén olvasták a kottát."
                    },
                    {
                        "type": "narration",
                        "text": "Zeneszerzőként Kodály a magyar kórusművészetet is világszínvonalra emelte, az 1923-ban bemutatott Psalmus Hungaricus és a Háry János pedig a nemzeti önismeret mesterműveivé váltak. Kecskeméten, szülővárosában jött létre az első ének-zenei általános iskola, ahol a mindennapos éneklés bizonyítottan fejlesztette a tanulók matematikai és nyelvi képességeit is."
                    },
                    {
                        "type": "narration",
                        "text": "A Kodály-módszert ma Japántól az Egyesült Államokig és Ausztráliáig ezernyi iskolában alkalmazzák, az UNESCO pedig a szellemi kulturális örökség legjobb megőrzési gyakorlatai közé választotta."
                    }
                ]
            },
            "words": [
                {"lemma": "szolmizáció", "translation": "solmization (do-re-mi sight-singing)", "pos": "noun"},
                {"lemma": "kórusművészet", "translation": "choral art", "pos": "noun"},
                {"lemma": "kézjel", "translation": "hand sign (Curwen/Kodály hand signs)", "pos": "noun"},
                {"lemma": "énekhang", "translation": "singing voice", "pos": "noun"},
                {"lemma": "hangköz", "translation": "musical interval", "pos": "noun"},
                {"lemma": "relatív szolmizáció", "translation": "movable-do solfege", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "pedagogical-iterative-verbs",
                "title": "Iterative Verbs in Skill Acquisition & Evaluative Diminutives",
                "text1_title": "Step-by-Step Practice: gyakorolgat, mutogat, tanulmányozgat",
                "text1": "When describing pedagogical practice or gradual mastery, -gat/-get expresses regular, incremental training: a gyerekek napról napra kézjelekkel mutogatták a hangközöket ('day by day the children practiced showing the intervals with hand signs').",
                "text2_title": "Attenuative / Critical Nuance of -gat/-get",
                "text2": "Depending on context, -gat/-get can also express a slightly casual, superficial, or unsystematic action ('merely dabbling in something'): silány dalocskákat énekelgetnek ('they just casually sing mediocre little songs') vs. tudatosan énekelnek ('they sing with conscious artistry'). Recognizing whether -gat/-get signals patient diligence OR casual dabbling is a key B2 reading skill!",
                "table_title": "Patient Diligence vs. Casual Dabbling with -gat/-get",
                "table_rows": [
                    ["Patient practice: mutogatja a kézjeleket", "Napról napra kézjelekkel mutogatták a hangközöket."],
                    ["Gradual study: tanulmányozgatja a kottát", "Előbb a népdalt tanulja meg, mielőtt a szimfóniákat tanulmányozgatná."],
                    ["Casual dabbling: dalocskákat énekelget", "Korábban csak silány dalocskákat énekelgettek az iskolában."],
                    ["Incremental rhythm: tapsolgatja a ritmust", "Az elsősök lelkesen tapsolgatták az aszimmetrikus ritmusokat."]
                ],
                "examples": [
                    {"spanish": "Az iskolások napról napra kézjelekkel mutogatták a hangközöket.", "english": "Day by day the schoolchildren practiced showing the intervals with hand signs."},
                    {"spanish": "Kodály kifogásolta, hogy az iskolákban silány dalocskákat énekelgetnek.", "english": "Kodály objected that in schools they were casually singing mediocre little songs."},
                    {"spanish": "A kisdiákok már az első évben bátran olvasgatták a pentaton kottákat.", "english": "Even in the first year, the young pupils were confidently reading pentatonic scores bit by bit."}
                ],
                "tip": "When paired with a diminutive noun like dalocska ('little song'), a -gat/-get verb (dalocskákat énekelget) strongly conveys ironic understatement."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "pairs": [
                        ["szolmizáció", "solmization (do-re-mi)"],
                        ["kórusművészet", "choral art"],
                        ["kézjel", "hand sign"],
                        ["énekhang", "singing voice"],
                        ["hangköz", "musical interval"],
                        ["relatív szolmizáció", "movable-do solfege"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "question": "Mi volt Kodály Zoltán zenepedagógiai programjának híres jelmondata?",
                    "options": [
                        "„Legyen a zene mindenkié!”",
                        "„A zene csak a zongoravirtuózoké!”",
                        "„Felejtsük el a kottázást!”"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "sentence": "A _____ szolmizáció és a kézjelek segítségével a gyerekek hangszer nélkül is megtanulnak kottát olvasni.",
                    "answer": "relatív",
                    "english": "With the help of movable-do solmization and hand signs, children learn to read sheet music even without an instrument."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-frequentative-verbs"],
                    "question": "In the sentence 'Korábban csak silány dalocskákat énekelgettek az iskolában', what tone does 'énekelgettek' convey?",
                    "options": [
                        "Casual, unsystematic, or superficial singing ('just singing little songs').",
                        "A single heroic performance at the National Opera.",
                        "Strict future obligation.",
                        "Passive prohibition by the state."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "sentence": "Az iskolások napról napra kézjelekkel _____ a különböző hangközöket. (mutat - frequentative 3rd pl. past def.)",
                    "answer": "mutogatták",
                    "english": "Day by day the schoolchildren practiced showing the different intervals with hand signs."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "tiles": ["Az", "elsősök", "lelkesen", "tapsolgatták", "a", "népdalok", "ritmusát."],
                    "solution": ["Az", "elsősök", "lelkesen", "tapsolgatták", "a", "népdalok", "ritmusát."],
                    "english": "The first-graders enthusiastically clapped out the rhythm of the folk songs repeatedly."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-frequentative-verbs"],
                    "prompt": [
                        {"speaker": "Szülő", "text": "Miért nem zongorával vagy hegedűvel kezdik a zenei nevelést a Kodály-módszerben?"},
                        {"speaker": "Énektanár", "text": "_____"}
                    ],
                    "options": [
                        "Mert az emberi énekhang mindenkinek a torkában ott van, és a gyerekek kézjelekkel mutogatva könnyen megtanulják a hangközöket.",
                        "Mert Kodály megtiltotta, hogy a gyerekek hangszereket nézegessenek.",
                        "Hogy senki se tudjon kórusművészetet hallgatni."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik városban jött létre az első ének-zenei általános iskola, Kodály Zoltán szülővárosában?",
                    "options": [
                        "Kecskeméten.",
                        "Kölnben.",
                        "Kaposváron."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "From the Táncház Movement to UNESCO Heritage",
            "grammar_label": "Reciprocal and communal iterative verbs (-gatják egymást, próbálgat)",
            "goals": [
                "I can explain how the 1970s Budapest Táncház movement revived living Transylvanian folk dance and music.",
                "I can use iterative verbs for communal practice, improvisation, and cultural transmission (próbálgat, cserélget, tanulgat).",
                "I can discuss traditional instruments (háromhúros brácsa, gardon) and UNESCO intangible heritage."
            ],
            "story_segment": {
                "seg_slug": "tanchazmozgalom",
                "title": "A széki táncház: Élő hagyomány a nagyváros szívében",
                "summary": "In 1972, Ferenc Sebő, Béla Halmos, and Sándor Tímár launched the urban Táncház movement in Budapest, turning folk dance from stage choreography back into living social culture.",
                "location": "Budapest (Liszt Ferenc tér) és Szék (Erdély, 1972)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1960-as évek végére a néptánc Magyarországon jobbára színpadi látványossággá merevedett, amelyet gondosan betanult koreográfiák szerint adtak elő. Ekkor azonban néhány fiatal budapesti zenész — köztük Sebő Ferenc és Halmos Béla — valamint Martin György tánckutató és Tímár Sándor koreográfus felfedezték, hogy az erdélyi Mezőségben, különösen Szék faluban, a táncház még mindig a fiatalok élő hétvégi szórakozási formája."
                    },
                    {
                        "type": "narration",
                        "text": "1972 májusában Budapesten, a Liszt Ferenc téri Könyvtárklubban megrendezték az első városi táncházat, ahol már nem volt külön színpad és nézőtér. A városi egyetemisták és fiatalok körbeálltak, és lépésről lépésre próbálgatták a széki tempót, a négyest és a csárdást, miközben az idősebb táncosok javítgatták a tartásukat."
                    },
                    {
                        "type": "narration",
                        "text": "A vonósbandában a prímás hegedűje mellett a háromhúros, egyenes pallójú brácsa és a bőgő diktálta a feszes ritmust, a gyimesi zenében pedig az ütőgardon adta a lüktetést. A zenészek és a táncosok órákon át figyelték egymás rezdüléseit, és szabadon variálgatták a figurákat, ahogyan a falusi mulatságokban szokás."
                    },
                    {
                        "type": "narration",
                        "text": "A táncházmozgalom pillanatok alatt országos kulturális jelenséggé nőtte ki magát, amely a Kádár-korszak szürke évtizedeiben a közösségi összetartozás és az önazonosság friss levegőjét jelentette a fiatalok számára."
                    },
                    {
                        "type": "narration",
                        "text": "2011-ben az UNESCO a táncházmódszert — mint a szellemi kulturális örökség átörökítésének magyar modelljét — felvette a világ legjobb megőrzési gyakorlatainak jegyzékébe, méltó módon folytatva Bartók és Kodály egykori küldetését."
                    }
                ]
            },
            "words": [
                {"lemma": "táncház", "translation": "folk dance house (communal dance event)", "pos": "noun"},
                {"lemma": "prímás", "translation": "lead fiddler (of a traditional string band)", "pos": "noun"},
                {"lemma": "brácsa", "translation": "three-stringed folk viola (kontra)", "pos": "noun"},
                {"lemma": "ütőgardon", "translation": "percussive cello-like folk instrument", "pos": "noun"},
                {"lemma": "koreográfia", "translation": "choreography", "pos": "noun"},
                {"lemma": "átörökítés", "translation": "intergenerational transmission / passing on", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "communal-iterative-verbs",
                "title": "Iterative Verbs of Experimentation & Variation (próbálgat, variálgat, javítgat)",
                "text1_title": "Trial, Correction, and Improvisation",
                "text1": "When learners or artists acquire a living physical skill like folk dancing or musical improvisation, Hungarian uses -gat/-get verbs to highlight trial-and-error experimentation and continuous refinement: próbál ('tries once') -> próbálgat ('tries out repeatedly / gets the feel of'), javít ('corrects') -> javítgat ('keeps adjusting/correcting gently'), variál ('varies') -> variálgat ('improvises variations on').",
                "text2_title": "Contrast with Perfective Prefixed Verbs",
                "text2": "Compare kijavította a hibát ('he corrected the mistake once and for all') with javítgatták a fiatalok tartását ('they kept gently adjusting the young dancers' posture throughout the evening'). In B2 cultural narratives, the unprefixed -gat/-get form captures the communal atmosphere of ongoing learning.",
                "table_title": "Perfective Single Action vs. Iterative Communal Process",
                "table_rows": [
                    ["kipróbálta a lépést (tried the step once)", "lépésről lépésre próbálgatták a széki csárdást (kept trying out the steps)"],
                    ["kijavította a tartását (corrected his posture)", "az idősebbek türelmesen javítgatták a tartásukat (kept gently adjusting)"],
                    ["megváltoztatta a figurát (changed the figure)", "szabadon variálgatták a táncfigurákat (kept improvising variations)"],
                    ["kicserélte a hangszerét (swapped his instrument)", "egymás között cserélgették a felvételeket (kept trading recordings)"]
                ],
                "examples": [
                    {"spanish": "A fiatalok lépésről lépésre próbálgatták a széki csárdást.", "english": "Step by step, the young people kept trying out the csárdás of Szék."},
                    {"spanish": "Az idősebb táncosok türelmesen javítgatták a kezdők tartását.", "english": "The older dancers patiently kept adjusting the beginners' posture."},
                    {"spanish": "A táncosok szabadon variálgatták a figurákat a prímás zenéjére.", "english": "The dancers freely improvised variations on the figures to the lead fiddler's music."}
                ],
                "tip": "Notice how distributive phrases like lépésről lépésre ('step by step') or estéről estére ('evening after evening') reinforce the iterative aspect of -gat/-get verbs."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "pairs": [
                        ["táncház", "communal folk dance house"],
                        ["prímás", "lead fiddler"],
                        ["brácsa", "folk viola (kontra)"],
                        ["ütőgardon", "percussive folk cello"],
                        ["koreográfia", "choreography"],
                        ["átörökítés", "transmission of heritage"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "question": "Miben különbözött az 1972-ben indult budapesti táncházmozgalom a korábbi színpadi néptáncegyüttesektől?",
                    "options": [
                        "Nem színpadi látványosságként, hanem élő, közösségi szórakozási és improvizációs formaként élesztette újjá a néptáncot.",
                        "Betiltotta a prímás és a brácsa használatát.",
                        "Csak hivatásos balettművészek léphettek be a terembe."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-bartokkodaly-vocab"],
                    "sentence": "Az UNESCO 2011-ben a szellemi örökség _____-ének magyar modelljeként ismerte el a táncházmódszert.",
                    "answer": "átörökítés",
                    "english": "In 2011 UNESCO recognized the táncház method as the Hungarian model for the transmission of intangible heritage."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-frequentative-verbs"],
                    "question": "Which verb form best expresses 'the beginners kept trying out the dance steps step by step'?",
                    "options": [
                        "próbálgatták",
                        "kipróbálták egyszer",
                        "próbálni fognak",
                        "megpróbál"
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "sentence": "Az idősebb táncosok egész este türelmesen _____ a kezdők testtartását. (javít - frequentative 3rd pl. past def.)",
                    "answer": "javítgatták",
                    "english": "All evening the older dancers patiently kept adjusting the beginners' posture."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-frequentative-verbs"],
                    "tiles": ["A", "fiatalok", "lépésről", "lépésre", "próbálgatták", "a", "széki", "táncot."],
                    "solution": ["A", "fiatalok", "lépésről", "lépésre", "próbálgatták", "a", "széki", "táncot."],
                    "english": "Step by step the young people kept trying out the dance of Szék."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-frequentative-verbs"],
                    "prompt": [
                        {"speaker": "Újságíró", "text": "Hogyan tanulták meg a városi fiatalok a bonyolult mezőségi tánclépéseket?"},
                        {"speaker": "Táncházvezető", "text": "_____"}
                    ],
                    "options": [
                        "Körbeálltak a teremben, és estéről estére próbálgatták a lépéseket, miközben egymást javítgatták.",
                        "Csak tankönyvből olvasták el egyszer a koreográfiát.",
                        "Megvárták, amíg a prímás abbahagyja a muzsikálást."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik erdélyi (mezőségi) falu élő táncházi hagyománya szolgált közvetlen mintául az 1972-es első budapesti táncházhoz?",
                    "options": [
                        "Szék.",
                        "Nagybánya.",
                        "Debrecen."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can explain the ethnomusicological revolution of Bartók and Kodály, from wax-cylinder fieldwork and pentatonic discovery to modernist composition, the Kodály Concept, and the Táncház revival.",
            "I can form and use frequentative verbs in -gat/-get across active, pedagogical, and communal contexts.",
            "I can distinguish contemplative -dogál/-degél/-dögél verbs from standard and -gat/-get verbs.",
            "I can combine distributive temporal/spatial expressions (faluról falura, lépésről lépésre) with iterative verbs."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-bartokkodaly-vocab"],
                "pairs": [
                    ["fonográfhenger", "phonograph wax cylinder"],
                    ["pentaton", "pentatonic (five-tone)"],
                    ["tiszta forrás", "pure source / spring"],
                    ["relatív szolmizáció", "movable-do solfege"],
                    ["táncház", "communal folk dance house"],
                    ["átörökítés", "transmission of heritage"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-frequentative-verbs"],
                "question": "Which suffix pair expresses a peaceful, leisurely, contemplative ongoing action such as 'sitting quietly' (üldögél) or 'ambling along' (mendegél)?",
                "options": [
                    "-dogál / -degél / -dögél",
                    "-tat / -tet",
                    "-hat / -het",
                    "-na / -ne"
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-bartokkodaly-vocab"],
                "question": "Melyik fogalom jelöli a népdalok beszédszerűen szabad, kötött ütem nélküli előadásmódját?",
                "options": ["parlando-rubato", "szolmizáció", "disszonancia", "koreográfia"],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-bartokkodaly-vocab"],
                "sentence": "A Kodály-módszerben a gyerekek _____-ekkel mutatják a hangközöket éneklés közben.",
                "answer": "kézjel",
                "english": "In the Kodály method, children show the musical intervals with hand signs while singing."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-frequentative-verbs"],
                "sentence": "A kutatók esténként türelmesen _____ a falusiakat a legrégebbi dallamokról. (kérdez - frequentative 3rd pl. past def.)",
                "answer": "kérdezgették",
                "english": "In the evenings the researchers patiently asked the villagers around about the oldest melodies."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-frequentative-verbs"],
                "sentence": "A pásztor a nyáj mellett _____ fújta a furulyáját. (mendegél - adverbial participle)",
                "answer": "mendegélve",
                "english": "Strolling along beside the flock, the shepherd played his flute."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-frequentative-verbs"],
                "prompt": [
                    {"speaker": "Népzenekutató", "text": "Hogyan dolgozták fel Bartókék a terepmunka során rögzített több ezer dallamot?"},
                    {"speaker": "Múzeumigazgató", "text": "_____"}
                ],
                "options": [
                    "Éveken át hangról hangra kottázgatták és rendszerezgették a viaszhengerek felvételeit.",
                    "Csak egyszer hallgatták meg őket, majd kitörölték a gyűjtőfüzetet.",
                    "A kávéházban üldögélve városi műdalokat írtak belőlük."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-frequentative-verbs"],
                "question": "Select the sentence that combines a distributive phrase with an iterative verb:",
                "options": [
                    "A zeneszerző faluról falura járogatva gyűjtötte az ősi pentaton dallamokat.",
                    "A zeneszerző egy faluban járt tegnap délután.",
                    "A zeneszerző elment a faluba, hogy aludjon.",
                    "A zeneszerzők megérkeztek a Zeneakadémiára."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-frequentative-verbs"],
                "prompt": [
                    {"speaker": "Egyetemista", "text": "Nem baj, ha még nem tudom pontosan a széki csárdás lépéseit?"},
                    {"speaker": "Prímás", "text": "_____"}
                ],
                "options": [
                    "Dehogy baj, gyere csak, itt mindenki estéről estére próbálgatja a figurákat!",
                    "De igen, itt csak az táncolhat, aki már tíz éve színpadon szerepel.",
                    "Üldögélj inkább otthon, nehogy meghalld a zenét!"
                ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-frequentative-verbs"],
                "tiles": ["A", "kutatók", "faluról", "falura", "járogatva", "gyűjtötték", "a", "népdalokat."],
                "solution": ["A", "kutatók", "faluról", "falura", "járogatva", "gyűjtötték", "a", "népdalokat."],
                "english": "Going from village to village, the researchers collected the folk songs."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-frequentative-verbs"],
                "tiles": ["A", "tornácon", "üldögélve", "hallgattuk", "az", "idős", "énekeseket."],
                "solution": ["A", "tornácon", "üldögélve", "hallgattuk", "az", "idős", "énekeseket."],
                "english": "Sitting quietly on the porch, we listened to the elderly singers."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-frequentative-verbs"],
                "template": [
                    {
                        "prompt": "Write a sentence describing how Bartók and Kodály questioned villagers and cleaned wax cylinders during fieldwork (use -gat/-get verbs).",
                        "answer": "Bartók és Kodály napközben türelmesen kérdezgették a falusiakat, esténként pedig órákig tisztogatták a fonográfhengereket."
                    },
                    {
                        "prompt": "Write a sentence describing how young people learn folk dances in the táncház (use a distributive phrase + a -gat/-get verb).",
                        "answer": "A fiatalok a táncházban estéről estére próbálgatják a lépéseket, miközben a tapasztaltabbak javítgatják a tartásukat."
                    }
                ]
            }
        ]
    }
}


UNIT_06_FESTESZET = {
    "unit_num": 6,
    "slug": "festeszet",
    "title": "Light, Myth & Modernism: Hungarian Visual Arts",
    "grammar_skill": "b2-adverbial-participles",
    "vocab_skill": "b2-festeszet-vocab",
    "theme": "Hungarian painting, Nagybánya and Bauhaus",
    "location": "Párizs, Nagybánya, Budapest és Dessau",
    "intro_body": [
        "From the monumental, bitumen-dark canvases of Mihály Munkácsy that captivated Paris salons in the 1870s to the sunlit violet meadows of Pál Szinyei Merse's Majális and the plein-air artists' colony of Nagybánya, Hungarian visual art underwent one of Europe's most dramatic transformations.",
        "In the 20th century, this visual revolution branched in two unforgettable directions: the solitary, mythic cosmic visions of Tivadar Csontváry Kosztka (The Lonely Cedar, Ruins of the Greek Theatre at Taormina) and the geometric constructivism and photography of László Moholy-Nagy at the Bauhaus. Grammatically, you will master adverbial participles in -va/-ve (simultaneous manner vs. anterior sequence), the stative passive construction (van + -va/-ve), and literary causative participles in -ván/-vén."
    ],
    "combined_story_title": "A Majálistól a Bauhausig: Magyar festők és látomások",
    "combined_story_summary": "The journey of Hungarian visual art from Munkácsy's dramatic canvases and Szinyei Merse's sunlight-filled Majális through the Nagybánya artists' colony and Csontváry's solitary visions to Moholy-Nagy at the Bauhaus.",
    "lessons": [
        {
            "num": 1,
            "title": "Munkácsy and Historical Monumentalism",
            "grammar_label": "Adverbial participles (-va/-ve) for simultaneous manner and posture",
            "goals": [
                "I can trace Mihály Munkácsy's rise from a carpenter's apprentice to a celebrated painter in Paris.",
                "I can form and use adverbial participles in -va/-ve to express manner and accompanying state.",
                "I can use art-historical vocabulary (vászon, ecsetvonás, chiaroscuro, műterem)."
            ],
            "story_segment": {
                "seg_slug": "munkacsy",
                "title": "Az asztalosműhelytől a párizsi szalonokig: Munkácsy Mihály",
                "summary": "Rising from an orphan carpenter's apprentice in Békéscsaba, Mihály Munkácsy conquered the 1870 Paris Salon with The Last Day of a Condemned Man and painted monumental masterpieces.",
                "location": "Békéscsaba, Párizs és Debrecen (1870–1880-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Munkácsy Mihály — eredeti nevén Lieb Mihály — árva asztalosinasból küzdötte fel magát a tizenkilencedik századi európai festészet csúcsára. Ifjúkorában Békéscsabán asztalosként dolgozva, ládákat és bútorokat festegetve ébredt rá arra, hogy a színek és az emberi arcok ábrázolása jelenti számára az igazi hivatást."
                    },
                    {
                        "type": "narration",
                        "text": "1870-ben a párizsi Szalonban bemutatta a Siralomház című festményét, amely egyetlen éjszaka alatt világhírűvé tette. A képen a kivégzésére váró betyár az asztalra támaszkodva, komor tekintettel mered maga elé, miközben a falusiak megrendülve búcsúznak tőle."
                    },
                    {
                        "type": "narration",
                        "text": "Munkácsy drámai erejét a sötét, bitumenes alapozás és a hirtelen felvillanó világos színfoltok éles ellentéte adta. Párizsi palotájának hatalmas műtermében állványra erősítve festette óriási vásznait, köztük a Krisztus-trilógiát, amelyet Budapesten és Amerikában is százezrek csodáltak meg."
                    },
                    {
                        "type": "narration",
                        "text": "Az Ásító inas vagy a Rőzsehordó nő című képein a szegény sorsú embereket nem leereszkedő sajnálattal, hanem mély emberi méltósággal felruházva örökítette meg. Bár a bitumenes festék az évtizedek során sötétedni kezdett, a restaurátorok gondos munkájának köszönhetően a művek ma is eredeti drámai erejükben ragyognak."
                    },
                    {
                        "type": "narration",
                        "text": "A debreceni Déri Múzeumban ma együtt látható a monumentális Krisztus-trilógia három óriásvászna, amelyek előtt megállva minden látogató átérzi a tizenkilencedik századi magyar festészet aranykorát."
                    }
                ]
            },
            "words": [
                {"lemma": "vászon", "translation": "canvas", "pos": "noun"},
                {"lemma": "műterem", "translation": "artist's studio / atelier", "pos": "noun"},
                {"lemma": "ecsetvonás", "translation": "brushstroke", "pos": "noun"},
                {"lemma": "alapozás", "translation": "priming / underpainting", "pos": "noun"},
                {"lemma": "festőállvány", "translation": "easel", "pos": "noun"},
                {"lemma": "fény-árnyék hatás", "translation": "chiaroscuro / light-and-shadow effect", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "adverbial-participle-manner",
                "title": "Adverbial Participles (-va/-ve) for Manner, Posture & Accompanying Action",
                "text1_title": "Forming -va/-ve Participles",
                "text1": "Hungarian forms its adverbial participle (határozói igenév) by attaching -va (to back-vowel verb stems: dolgozva, támaszkodva, megállva) or -ve (to front-vowel verb stems: festegetve, megrendülve, felöltözve) directly to the dictionary stem. For verbs in -ik, drop -ik before adding -va/-ve (támaszkodik -> támaszkodva).",
                "text2_title": "Simultaneous Manner & Emotional State",
                "text2": "When attached to an active verb, the -va/-ve participle answers HOGYAN? ('how / in what posture or emotional state?') and shares the subject of the main verb: az asztalra támaszkodva mered maga elé ('leaning on the table, he stares ahead'); a falusiak megrendülve búcsúznak tőle ('deeply moved, the villagers bid him farewell').",
                "table_title": "Verb Stem -> Adverbial Participle (-va/-ve)",
                "table_rows": [
                    ["dolgozik (works) -> dolgozva", "Asztalosként dolgozva ébredt rá a hivatására."],
                    ["támaszkodik (leans) -> támaszkodva", "Az asztalra támaszkodva mered maga elé."],
                    ["megrendül (is deeply moved) -> megrendülve", "A falusiak megrendülve búcsúznak az elítélttől."],
                    ["felruház (endows) -> felruházva", "Mély emberi méltósággal felruházva ábrázolta őket."]
                ],
                "examples": [
                    {"spanish": "A betyár az asztalra támaszkodva, komor tekintettel mered maga elé.", "english": "Leaning on the table, the outlaw stares ahead with a grim gaze."},
                    {"spanish": "A falusiak megrendülve búcsúznak a kivégzésére váró fogolytól.", "english": "Deeply moved, the villagers bid farewell to the prisoner awaiting execution."},
                    {"spanish": "Az óriásvásznak előtt megállva minden látogató átérzi a drámai erőt.", "english": "Standing before the giant canvases, every visitor feels the dramatic power."}
                ],
                "tip": "In well-formed B2 Hungarian, the implied subject of a manner -va/-ve participle should match the subject of the main finite verb (Az óriásvásznak előtt megállva [a látogató] átérzi...)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-festeszet-vocab"],
                    "pairs": [
                        ["vászon", "canvas"],
                        ["műterem", "artist's studio"],
                        ["ecsetvonás", "brushstroke"],
                        ["alapozás", "underpainting / priming"],
                        ["festőállvány", "easel"],
                        ["fény-árnyék hatás", "light-and-shadow effect"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "question": "Melyik festményével aratott Munkácsy Mihály 1870-ben világraszóló sikert a párizsi Szalonban?",
                    "options": [
                        "A Siralomház című festménnyel.",
                        "A Majális című festménnyel.",
                        "A Magányos cédrus című képpel."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "sentence": "Munkácsy párizsi _____-ében hatalmas állványokon álltak az óriási vásznak.",
                    "answer": "műterem",
                    "english": "In Munkácsy's Paris studio, the giant canvases stood on huge easels."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-adverbial-participles"],
                    "question": "Which adverbial participle correctly completes: 'A betyár az asztalra _____, komor tekintettel mered maga elé.' (from támaszkodik)?",
                    "options": ["támaszkodva", "támaszkodve", "támaszkodikva", "támaszkodott"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "sentence": "A falusiak _____ búcsúznak a kivégzésére váró elítélttől. (megrendül - adverbial participle)",
                    "answer": "megrendülve",
                    "english": "Deeply moved, the villagers bid farewell to the condemned man awaiting execution."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "tiles": ["Az", "óriásvásznak", "előtt", "megállva", "mindenki", "átérzi", "a", "drámai", "erőt."],
                    "solution": ["Az", "óriásvásznak", "előtt", "megállva", "mindenki", "átérzi", "a", "drámai", "erőt."],
                    "english": "Stopping before the giant canvases, everyone feels the dramatic power."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-adverbial-participles"],
                    "prompt": [
                        {"speaker": "Művészettörténész", "text": "Hogyan ábrázolta Munkácsy a szegény sorsú embereket a zsánerképein?"},
                        {"speaker": "Kurátor", "text": "_____"}
                    ],
                    "options": [
                        "Nem leereszkedő sajnálattal, hanem mély emberi méltósággal felruházva festette meg őket.",
                        "A műteremben ülve teljesen elfelejtette az arcukat.",
                        "Geometriai köröket rajzolva a Bauhaus stílusában."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik magyar város múzeumában látható ma együtt Munkácsy Mihály Krisztus-trilógiájának mindhárom óriásvászna?",
                    "options": [
                        "Debrecenben, a Déri Múzeumban.",
                        "Pécsett, a Csontváry Múzeumban.",
                        "Kecskeméten, a Kodály Intézetben."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 2,
            "title": "Szinyei Merse and the Plein-Air Turn at Nagybánya",
            "grammar_label": "Anterior sequence with prefixed participles (megérkezve, kilépve) vs. simultaneous -va/-ve",
            "goals": [
                "I can explain the significance of Szinyei Merse Pál's Majális (1873) and the 1896 Nagybánya artists' colony.",
                "I can contrast prefixed adverbial participles (anterior action: kilépve) with unprefixed ones (simultaneous: ragyogva).",
                "I can use impressionist and plein-air painting vocabulary in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "nagybanya",
                "title": "Napfény a zöld mezőn: A Majális és a nagybányai művésztelep",
                "summary": "Szinyei Merse Pál painted his radiant Majális in 1873, and two decades later Hollósy Simon and Ferenczy Károly founded the Nagybánya colony, bringing Hungarian painting out into the open air.",
                "location": "Jernye és Nagybánya (1873–1896)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Miközben a korabeli európai akadémiákon még sötét tónusú történelmi jeleneteket festettek, Szinyei Merse Pál 1873-ban megalkotta a magyar festészet egyik legderűsebb remekművét, a Majálist. A festő a francia impresszionistáktól függetlenül, a természet megfigyeléséből kiindulva örökítette meg a tavaszi domboldalon piknikező társaságot és a fűben hasaló, lila ruhás hölgyet."
                    },
                    {
                        "type": "narration",
                        "text": "A korabeli konzervatív kritika azonban értetlenül fogadta a vakító napfényt és a harsány zöldeket: a bírálatoktól elkeseredve Szinyei Merse visszavonult jernyei birtokára, és évekig alig vett ecsetet a kezébe. Csak húsz évvel később, egy új festőnemzedék színre lépésével ismerték fel, hogy a Majális évtizedekkel megelőzte a korát."
                    },
                    {
                        "type": "narration",
                        "text": "1896 tavaszán Hollósy Simon, Ferenczy Károly és társaik Münchenből hazatérve megalapították a nagybányai művésztelepet. A sötét akadémiai műtermekből a szabad ég alá kilépve közvetlenül a Zazar folyó partján és a környező hegyekben állították fel festőállványaikat."
                    },
                    {
                        "type": "narration",
                        "text": "A plein air — vagyis a szabadban való festés — lényege az volt, hogy a művész a napfény és a levegő rezgését a maga pillanatnyi valóságában ragadja meg. Ferenczy Károly a fák lombján átszűrődő fényt tanulmányozva teremtette meg a modern magyar tájképfestészet poétikus nyelvét."
                    },
                    {
                        "type": "narration",
                        "text": "Nagybánya rövid idő alatt a magyar modernizmus bölcsőjévé vált, amelynek szellemi öröksége festőnemzedékek egész sorát indította el a huszadik század útján."
                    }
                ]
            },
            "words": [
                {"lemma": "művésztelep", "translation": "artists' colony", "pos": "noun"},
                {"lemma": "tájkép", "translation": "landscape painting", "pos": "noun"},
                {"lemma": "színfolt", "translation": "patch of color", "pos": "noun"},
                {"lemma": "impresszionizmus", "translation": "impressionism", "pos": "noun"},
                {"lemma": "tónus", "translation": "tone / shade", "pos": "noun"},
                {"lemma": "szabad ég alatt", "translation": "in the open air (plein air)", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "prefixed-participles-sequence",
                "title": "Anterior vs. Simultaneous Adverbial Participles (-va/-ve)",
                "text1_title": "Prefixed Participles for Immediate Prior Action ('Having done X...')",
                "text1": "When an adverbial participle carries a perfective verbal prefix (hazatérve, kilépve, elkeseredve, megérkezve), it expresses an action or change of state that occurred immediately BEFORE or as the direct cause of the main clause: Münchenből hazatérve megalapították a művésztelepet ('Having returned home from Munich, they founded the artists' colony'); a bírálatoktól elkeseredve visszavonult ('Embittered by the criticisms, he withdrew').",
                "text2_title": "Unprefixed Participles for Ongoing Process ('While doing X...')",
                "text2": "By contrast, unprefixed verbs in -va/-ve describe an ongoing activity simultaneous with the main verb: a fák lombján átszűrődő fényt tanulmányozva teremtette meg... ('Studying the light filtering through the foliage, he created...').",
                "table_title": "Simultaneous (Unprefixed) vs. Anterior/Causal (Prefixed) -va/-ve",
                "table_rows": [
                    ["tanulmányozva (while studying)", "A fényt tanulmányozva teremtette meg az új stílust."],
                    ["hasalva (lying prone - ongoing)", "A lila ruhás hölgy a fűben hasalva élvezi a napsütést."],
                    ["hazatérve (having returned home)", "Münchenből hazatérve megalapították a művésztelepet."],
                    ["elkeseredve (having grown embittered)", "A bírálatoktól elkeseredve visszavonult a birtokára."]
                ],
                "examples": [
                    {"spanish": "A bírálatoktól elkeseredve Szinyei Merse visszavonult jernyei birtokára.", "english": "Embittered by the criticisms, Szinyei Merse withdrew to his estate in Jernye."},
                    {"spanish": "A sötét műtermekből a szabad ég alá kilépve a folyóparton festettek.", "english": "Stepping out from the dark studios into the open air, they painted on the riverbank."},
                    {"spanish": "Ferenczy a fák lombján átszűrődő fényt tanulmányozva alkotta meg tájképeit.", "english": "Studying the light filtering through the foliage of the trees, Ferenczy created his landscapes."}
                ],
                "tip": "Never split the verbal prefix from an adverbial participle! Even if there is a focused phrase before it, the prefix stays attached: Münchenből hazatérve (never *térve haza*)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-festeszet-vocab"],
                    "pairs": [
                        ["művésztelep", "artists' colony"],
                        ["tájkép", "landscape painting"],
                        ["színfolt", "patch of color"],
                        ["impresszionizmus", "impressionism"],
                        ["tónus", "tone / shade"],
                        ["szabad ég alatt", "in the open air"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "question": "Mi volt a nagybányai művésztelep (1896) legfontosabb festészeti újítása?",
                    "options": [
                        "A sötét akadémiai műtermek helyett a szabad ég alatt (plein air) festették a napfényt és a természetet.",
                        "Betiltották a tájképek festését, és csak fekete-fehér fotókat készítettek.",
                        "Kizárólag középkori templomi freskókat másoltak."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "sentence": "Hollósy Simon és Ferenczy Károly 1896-ban alapították meg a híres nagybányai _____-et.",
                    "answer": "művésztelep",
                    "english": "Simon Hollósy and Károly Ferenczy founded the famous Nagybánya artists' colony in 1896."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-adverbial-participles"],
                    "question": "In 'Münchenből hazatérve megalapították a művésztelepet', what temporal relationship does 'hazatérve' express?",
                    "options": [
                        "An completed anterior action ('Having returned home from Munich...').",
                        "A future action that has not happened yet.",
                        "A passive prohibition.",
                        "A negative purpose clause."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "sentence": "A korabeli igazságtalan bírálatoktól _____ Szinyei Merse évekig nem festett. (elkeseredik - adverbial participle)",
                    "answer": "elkeseredve",
                    "english": "Embittered by the unfair contemporary criticisms, Szinyei Merse did not paint for years."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "tiles": ["A", "sötét", "műtermekből", "kilépve", "a", "szabad", "ég", "alatt", "festettek."],
                    "solution": ["A", "sötét", "műtermekből", "kilépve", "a", "szabad", "ég", "alatt", "festettek."],
                    "english": "Stepping out of the dark studios, they painted in the open air."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-adverbial-participles"],
                    "prompt": [
                        {"speaker": "Diák", "text": "Hogyan született meg Szinyei Merse Pál Majális című festménye 1873-ban?"},
                        {"speaker": "Festőművész", "text": "_____"}
                    ],
                    "options": [
                        "A francia impresszionistáktól függetlenül, a tavaszi természet megfigyeléséből kiindulva festette meg a napsütötte domboldalt.",
                        "Párizsba utazva lemásolta Munkácsy Siralomház című képét.",
                        "A nagybányai művésztelepen tanulva 1920-ban készítette el."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Ki a Szinyei Merse Pál Majális című festményének legismertebb alakja az előtérben?",
                    "options": [
                        "A zöld fűben hasaló, lila ruhás hölgy.",
                        "Az asztalra támaszkodó betyár.",
                        "A libanoni magányos cédrus."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 3,
            "title": "The Solitary Vision of Csontváry Kosztka",
            "grammar_label": "Literary causal/anterior participles (-ván/-vén)",
            "goals": [
                "I can recount the life and visionary art of Tivadar Csontváry Kosztka (from apothecary to painter of the 'Sun Path').",
                "I can recognize and use the elevated literary participle in -ván/-vén (hallván, látván, lévén).",
                "I can discuss symbolism, mythic landscapes, and the Csontváry Museum in Pécs."
            ],
            "story_segment": {
                "seg_slug": "csontvary",
                "title": "A napút festője: Csontváry Kosztka Tivadar látomásai",
                "summary": "At age 27, pharmacist Tivadar Csontváry Kosztka heard an inner voice prophesying he would become the greatest plein-air painter in the world, leading to his mythic canvases in Taormina, Baalbek, and Lebanon.",
                "location": "Igló, Taormina, Libanon és Pécs",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar festészettörténet legtitokzatosabb alakja, Csontváry Kosztka Tivadar huszonhét éves koráig gyógyszerészként dolgozott a felvidéki Iglón. Egy nap azonban, az utcán álló ökrös szekeret lerajzolva, belső égi szózatot hallott: „Te leszel a világ legnagyobb napút-festője, nagyobb Raffaellónál!”"
                    },
                    {
                        "type": "narration",
                        "text": "Hallván a különös próféciát, Csontváry nem fogott azonnal eszelős festésbe, hanem tíz éven át gácsi gyógyszertárában dolgozva takarékoskodott, hogy biztosítsa anyagi függetlenségét. Csak negyvenéves kora körül indult útnak, hogy bejárja Dalmáciát, Olaszországot, Egyiptomot, Palesztinát és Libanont, keresvén a világ „nagy motívumait”."
                    },
                    {
                        "type": "narration",
                        "text": "A taorminai görög színház romjai vagy a Baalbek című gigantikus vásznain olyan izzó, kozmikus színeket használt, amilyeneket előtte még senki sem kevert ki a palettáján. Csontváry a „napút” kifejezéssel azt a ragyogó fényjelenséget jelölte, amikor a lemenő vagy felkelő nap mágikus színekbe öltözteti a tájat."
                    },
                    {
                        "type": "narration",
                        "text": "Életművének legmegrendítőbb alkotása a Magányos cédrus, amelyet a libanoni hegyekben festett meg. A viharoktól megtépázott, mégis büszkén az ég felé nyújtózó fa egyszerre a magyar sors szimbóluma és a meg nem értett, magányos művész önarcképe."
                    },
                    {
                        "type": "narration",
                        "text": "Halála után a feltekert óriásvásznakat kis híján fuvarosoknak adták el ponyvának, ám egy fiatal építész, Gerlóczy Gedeon az utolsó pillanatban felvásárolta őket. Ennek a mentőakciónak köszönhetően ma a pécsi Csontváry Múzeumban csodálhatjuk meg a zseniális látomásokat."
                    }
                ]
            },
            "words": [
                {"lemma": "látomás", "translation": "vision", "pos": "noun"},
                {"lemma": "paletta", "translation": "palette", "pos": "noun"},
                {"lemma": "önarckép", "translation": "self-portrait", "pos": "noun"},
                {"lemma": "szimbólum", "translation": "symbol", "pos": "noun"},
                {"lemma": "életmű", "translation": "oeuvre / life's work", "pos": "noun"},
                {"lemma": "napút", "translation": "sun-path (Csontváry's term for radiant atmospheric light)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "literary-participle-van-ven",
                "title": "The Literary & Causal Adverbial Participle (-ván/-vén)",
                "text1_title": "How -ván/-vén Differs from -va/-ve",
                "text1": "Alongside everyday -va/-ve, Hungarian possesses an elevated literary adverbial participle formed with -ván (back vowel) and -vén (front vowel): hallván ('upon hearing / since he heard'), látván ('seeing that'), keresvén ('seeking'), lévén ('being'). While -va/-ve primarily describes manner or state, -ván/-vén explicitly highlights CAUSALITY ('since / inasmuch as') or immediate mental reaction ('upon realizing').",
                "text2_title": "The Suppletive Participle lévén ('being / inasmuch as')",
                "text2": "The verb van ('to be') has NO *-va* form; its adverbial participle is always lévén (or বিধায়/voltán in archaic idioms): Független ember lévén senkinek sem tartozott elszámolással ('Being an independent man, he owed an account to no one').",
                "table_title": "Standard -va/-ve vs. Literary Causal -ván/-vén",
                "table_rows": [
                    ["hallva (hearing)", "Hallván a próféciát, tíz évig takarékoskodott. (Upon hearing...)"],
                    ["látva (seeing)", "Látván a feltekert vásznakat, Gerlóczy azonnal megvette őket."],
                    ["keresve (searching)", "Bejárta a Közel-Keletet, keresvén a világ nagy motívumait."],
                    ["van -> lévén (being)", "Magányos zseni lévén nem csatlakozott egyetlen iskolához sem."]
                ],
                "examples": [
                    {"spanish": "Hallván a különös próféciát, Csontváry tíz éven át takarékoskodott.", "english": "Upon hearing the strange prophecy, Csontváry saved money for ten years."},
                    {"spanish": "Bejárta Libanont, keresvén a festészet nagy motívumait.", "english": "He travelled through Lebanon, seeking the great motifs of painting."},
                    {"spanish": "Magányos látnok lévén a saját útját járta a művészetben.", "english": "Being a solitary visionary, he walked his own path in art."}
                ],
                "tip": "Always use lévén (never *levő* or *vanva*) when translating 'Being a [noun/adjective], he...' as a causal clause!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-festeszet-vocab"],
                    "pairs": [
                        ["látomás", "vision"],
                        ["paletta", "palette"],
                        ["önarckép", "self-portrait"],
                        ["szimbólum", "symbol"],
                        ["életmű", "oeuvre / life's work"],
                        ["napút", "sun-path (radiant light)"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "question": "Ki mentette meg Csontváry Kosztka Tivadar óriásvásznait attól, hogy halála után ponyvaként adják el őket?",
                    "options": [
                        "Gerlóczy Gedeon fiatal építész.",
                        "Munkácsy Mihály Párizsban.",
                        "Hollósy Simon Nagybányán."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "sentence": "A Magányos cédrus egyszerre a magyar sors szimbóluma és a magányos művész szellemi _____-e.",
                    "answer": "önarckép",
                    "english": "The Lonely Cedar is at once a symbol of Hungarian destiny and the spiritual self-portrait of the solitary artist."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-adverbial-participles"],
                    "question": "Which word is the adverbial participle of 'van' ('being / inasmuch as')?",
                    "options": ["lévén", "lenve", "való", "voltván"],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "sentence": "_____ a veszélyt, hogy a képeket kocsiponyvának adják el, Gerlóczy azonnal megvásárolta az életművet. (lát - literary participle in -ván)",
                    "answer": "Látván",
                    "english": "Seeing the danger that the paintings would be sold as wagon tarpaulins, Gerlóczy immediately bought the oeuvre."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "tiles": ["Magányos", "látnok", "lévén", "Csontváry", "a", "saját", "útját", "járta."],
                    "solution": ["Magányos", "látnok", "lévén", "Csontváry", "a", "saját", "útját", "járta."],
                    "english": "Being a solitary visionary, Csontváry walked his own path."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-adverbial-participles"],
                    "prompt": [
                        {"speaker": "Látogató", "text": "Miért dolgozott Csontváry még tíz évig gyógyszerészként, miután meghallotta az égi szózatot?"},
                        {"speaker": "Múzeumpedagógus", "text": "_____"}
                    ],
                    "options": [
                        "Gyakorlatias ember lévén előbb biztosítani akarta az anyagi függetlenségét az utazásokhoz.",
                        "Mert nem szeretett a szabad ég alatt festeni.",
                        "Nehogy bárki megnézze a képeit a pécsi múzeumban."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Mit értett Csontváry Kosztka Tivadar a „napút” kifejezés alatt?",
                    "options": [
                        "Azt a ragyogó légköri fényjelenséget, amikor a nap izzó, mágikus színekbe öltözteti a tájat.",
                        "Egy vasútvonalat Budapest és Párizs között.",
                        "A fekete-fehér fotogramok készítésének technikáját."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 4,
            "title": "Hungarian Avant-Garde and Moholy-Nagy at the Bauhaus",
            "grammar_label": "Stative passive (van + -va/-ve / lett + -va/-ve) vs. active manner participle",
            "goals": [
                "I can explain the contribution of Kassák Lajos's MA circle and László Moholy-Nagy at the Bauhaus.",
                "I can distinguish the stative passive construction (meg van világítva, fel van szerelve) from active -va/-ve manner clauses.",
                "I can discuss constructivism, photograms, typography, and kinetic light art."
            ],
            "story_segment": {
                "seg_slug": "moholynagy",
                "title": "Fény-tér-modulátor: Moholy-Nagy László és a Bauhaus",
                "summary": "Inspired by Lajos Kassák's activist avant-garde journal MA, László Moholy-Nagy became the youngest professor at the Bauhaus, pioneering photography, typography, and kinetic light sculpture.",
                "location": "Budapest, Weimar, Dessau és Chicago (1919–1946)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az első világháború utáni összeomlásban a fiatal magyar művészek radikálisan új válaszokat kerestek. Kassák Lajos MA című folyóirata körül olyan avantgárd alkotók gyűltek össze, akik elutasították a polgári szalonfestészetet, és úgy vélték, hogy a művészetnek a modern ipari társadalom egész környezetét át kell formálnia."
                    },
                    {
                        "type": "narration",
                        "text": "Ebből a szellemi körből indult el Moholy-Nagy László, akit Walter Gropius 1923-ban, mindössze huszonnyolc évesen meghívott a weimari, majd dessaui Bauhaus tanárának. A Bauhaus műhelyeiben a festészet, az építészet, a formatervezés és a tipográfia nem volt egymástól elválasztva, hanem egységes rendszerbe volt foglalva."
                    },
                    {
                        "type": "narration",
                        "text": "Moholy-Nagy szerint a huszadik század művésze már nemcsak pigmentekkel, hanem tiszta fénnyel fest. Fotogramjain a tárgyak közvetlenül a fényérzékeny papírra vannak helyezve, fényképezőgép nélkül létrehozva titokzatos, lebegő árnyékformákat."
                    },
                    {
                        "type": "narration",
                        "text": "1930-ban megalkotta híres kinetikus szobrát, a Fény-tér-modulátort, amely krómozott acélból, üvegből és elektromos motorból volt összeállítva. Amikor a szerkezet forgásba van hozva és reflektorokkal meg van világítva, a falakon végtelenül változó fény-árnyék színház születik."
                    },
                    {
                        "type": "narration",
                        "text": "Breuer Marcell csővázas bútoraival együtt Moholy-Nagy munkássága alapozta meg a modern vizuális kultúrát, amelyet később Chicagóban, a New Bauhaus élén adott tovább az amerikai formatervezőknek."
                    }
                ]
            },
            "words": [
                {"lemma": "avantgárd", "translation": "avant-garde", "pos": "noun/adjective"},
                {"lemma": "formatervezés", "translation": "industrial / product design", "pos": "noun"},
                {"lemma": "fotogram", "translation": "photogram (cameraless photograph)", "pos": "noun"},
                {"lemma": "tipográfia", "translation": "typography", "pos": "noun"},
                {"lemma": "kinetikus", "translation": "kinetic (moving)", "pos": "adjective"},
                {"lemma": "konstruktivizmus", "translation": "constructivism", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "stative-passive-van-va",
                "title": "Stative Passive (van/volt/lett + -va/-ve) vs. Active Participle",
                "text1_title": "Describing Resulting State with van + Prefixed -va/-ve",
                "text1": "Hungarian does not use a Germanic-style agentive passive in everyday prose; instead, to describe a RESULTING STATE achieved by a prior transitive action, it combines van / volt / lesz / lett with a prefixed adverbial participle: A szerkezet meg van világítva ('The structure is illuminated'), A papírra vannak helyezve ('They are placed on the paper'), Egységes rendszerbe volt foglalva ('It was integrated into a unified system').",
                "text2_title": "Word Order: Prefix + van/volt + Stem-va/-ve",
                "text2": "Notice the iconic word order of the Hungarian stative passive in neutral affirmative sentences: the verbal prefix separates and stands BEFORE van/volt/lett, while the stem-va/-ve follows: meg van világítva, össze volt állítva, el van választva. In negative sentences, nincs/nem replaces van right after or before the prefix: nem volt egymástól elválasztva / nincs elválasztva.",
                "table_title": "Active Manner (-va/-ve) vs. Stative Passive (Prefix + van + -va/-ve)",
                "table_rows": [
                    ["Active manner: Fénnyel kísérletezve alkotott.", "Experimenting with light, he created works."],
                    ["Stative present: A szobor meg van világítva.", "The sculpture is illuminated (resulting state)."],
                    ["Stative past: Acélból volt összeállítva.", "It was assembled from steel."],
                    ["Dynamic passive: Forgásba lett hozva.", "It got set into rotation."]
                ],
                "examples": [
                    {"spanish": "Amikor a szerkezet reflektorokkal meg van világítva, fény-árnyék színház születik.", "english": "When the structure is illuminated with spotlights, a theatre of light and shadow is born."},
                    {"spanish": "A Fény-tér-modulátor krómozott acélból és üvegből volt összeállítva.", "english": "The Light-Space Modulator was assembled from chromed steel and glass."},
                    {"spanish": "A Bauhausban a művészet és a formatervezés nem volt egymástól elválasztva.", "english": "At the Bauhaus, art and design were not separated from each other."}
                ],
                "tip": "Watch the prefix split in neutral positive stative passives: 'meg van világítva' (NOT *van megvilágítva*)."
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-festeszet-vocab"],
                    "pairs": [
                        ["avantgárd", "avant-garde"],
                        ["formatervezés", "product / industrial design"],
                        ["fotogram", "cameraless photograph"],
                        ["tipográfia", "typography"],
                        ["kinetikus", "kinetic (moving)"],
                        ["konstruktivizmus", "constructivism"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "question": "Mi volt Moholy-Nagy László 1930-ban bemutatott Fény-tér-modulátora?",
                    "options": [
                        "Acélból, üvegből és elektromos motorból összeállított kinetikus (mozgó) fényszobor.",
                        "Egy olajfestmény a nagybányai Zazar folyóról.",
                        "Egy hagyományos bronz lovasszobor a Hősök terén."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "sentence": "A _____ készítésekor a tárgyakat fényképezőgép nélkül, közvetlenül a fényérzékeny papírra helyezik.",
                    "answer": "fotogram",
                    "english": "When making a photogram, objects are placed directly onto light-sensitive paper without a camera."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-adverbial-participles"],
                    "question": "Which sentence has the correct neutral word order for the Hungarian stative passive ('The sculpture is illuminated with spotlights')?",
                    "options": [
                        "A szobor reflektorokkal meg van világítva.",
                        "A szobor reflektorokkal van megvilágítva.",
                        "A szobor reflektorokkal megvilágítva lévén.",
                        "A szobor reflektorokkal világítva meg van."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "sentence": "A Fény-tér-modulátor krómozott acélból és üvegből volt _____. (összeállít - adverbial participle)",
                    "answer": "összeállítva",
                    "english": "The Light-Space Modulator was assembled from chromed steel and glass."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "tiles": ["A", "szerkezet", "reflektorokkal", "meg", "van", "világítva."],
                    "solution": ["A", "szerkezet", "reflektorokkal", "meg", "van", "világítva."],
                    "english": "The structure is illuminated with spotlights."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-adverbial-participles"],
                    "prompt": [
                        {"speaker": "Építészhallgató", "text": "Hogyan viszonyult egymáshoz a képzőművészet és az ipari formatervezés a Bauhausban?"},
                        {"speaker": "Professzor", "text": "_____"}
                    ],
                    "options": [
                        "Nem volt egymástól elválasztva, hanem egységes alkotói rendszerbe volt foglalva.",
                        "Szigorúan tilos volt gépeket használni a műhelyekben.",
                        "A tipográfia teljesen el volt felejtve."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik amerikai városban alapította meg Moholy-Nagy László a New Bauhaus intézményét emigrációja után?",
                    "options": [
                        "Chicagóban.",
                        "San Franciscóban.",
                        "Bostonban."
                    ],
                    "correct": 0
                }
            ]
        },
        {
            "num": 5,
            "title": "Art Museums, Collectors, and Cultural Memory",
            "grammar_label": "Complex participial clauses in art criticism and museum curation",
            "goals": [
                "I can discuss Budapest's major art institutions (Szépművészeti Múzeum, Magyar Nemzeti Galéria, Műcsarnok).",
                "I can weave together active (-va/-ve), causal (-ván/-vén), and stative (van + -va/-ve) participles in B2 descriptions.",
                "I can describe art patronage, restoration, and exhibition curation in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szepmuveszeti",
                "title": "A Hősök terétől a Budai Várig: Múzeumok és műgyűjtők",
                "summary": "From the Esterházy collection and the 1906 opening of the Museum of Fine Arts on Heroes' Square to the Hungarian National Gallery in Buda Castle, museums safeguard the nation's visual memory.",
                "location": "Budapest (Hősök tere és Budai Vár)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar képzőművészeti kincsek közgyűjteményi megőrzése a tizenkilencedik században az Esterházy hercegek világhírű képtárának megvásárlásával vett nagy lendületet. A magyar állam 1871-ben megvásárolván a több száz európai remekművet — köztük Raffaello, El Greco és Goya alkotásait —, megteremtette a későbbi Szépművészeti Múzeum alapját."
                    },
                    {
                        "type": "narration",
                        "text": "1906-ban a Hősök tere két oldalán már egymással szemben állt a Schickedanz Albert és Herzog Fülöp Ferenc által tervezett két neoklasszicista épület: a Szépművészeti Múzeum és a kortárs kiállításoknak helyet adó Műcsarnok. A huszadik század első felében olyan polgári műgyűjtők és mecénások, mint Hatvany Ferenc vagy Nemes Marcell, saját vagyonukat áldozva vásárolták meg a legértékesebb magyar és európai festményeket."
                    },
                    {
                        "type": "narration",
                        "text": "A második világháború ostroma alatt számos műkincs megsérült vagy elhurcolva külföldre került, ezért a békekötés után évtizedekig tartó kutatómunkára és restaurálásra volt szükség. Ma a magyar festészet és szobrászat történeti gyűjteménye a Budai Várpalota épületében, a Magyar Nemzeti Galériában van elhelyezve."
                    },
                    {
                        "type": "narration",
                        "text": "A galéria termeit végigjárva a látogató a középkori szárnyas oltároktól Munkácsy, Szinyei Merse és Csontváry vásznain át egészen a huszadik századi avantgárdig követheti végig a magyar látásmód alakulását. A festmények gondosan klimatizált termekben, korszerű világítással ellátva várják az érdeklődőket."
                    },
                    {
                        "type": "narration",
                        "text": "Így kapcsolódik össze a múlt és a jelen: a művészek egykori magányos látomásai ma közös kulturális emlékezetünk elválaszthatatlan részévé válva gazdagítják minden új nemzedék életét."
                    }
                ]
            },
            "words": [
                {"lemma": "közgyűjtemény", "translation": "public collection", "pos": "noun"},
                {"lemma": "műgyűjtő", "translation": "art collector", "pos": "noun"},
                {"lemma": "mecénás", "translation": "art patron / benefactor", "pos": "noun"},
                {"lemma": "restaurálás", "translation": "art restoration", "pos": "noun"},
                {"lemma": "szárnyas oltár", "translation": "winged altarpiece (triptych)", "pos": "expression"},
                {"lemma": "műkincs", "translation": "art treasure / artwork", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "participial-clauses-synthesis",
                "title": "Synthesizing Participial Clauses in B2 Cultural Prose",
                "text1_title": "Three Functions of -va/-ve & -ván/-vén in One System",
                "text1": "In sophisticated Hungarian art writing, you will see all three participial functions working side by side: (1) Active simultaneous/sequential -va/-ve modifying the subject (A galéria termeit végigjárva a látogató követheti...); (2) Attributive/descriptive modifier with -val/-vel + ellátva/felruházva (korszerű világítással ellátva várják az érdeklődőket); and (3) Stative passive Predicate (a Budai Várpalotában van elhelyezve).",
                "text2_title": "Word Order When an Adverbial Phrase Precedes van + -va/-ve",
                "text2": "Notice a subtle B2 rule! Earlier we saw that in a neutral sentence the prefix stands before van: A gyűjtemény el van helyezve. However, when a focused locative phrase stands immediately before the verb ('in Buda Castle'), van moves right after the focused location and the prefix reattaches to the participle: a Budai Várpalotában van elhelyezve ('it is housed IN BUDA CASTLE')!",
                "table_title": "Neutral Stative Passive vs. Location-Focused Stative Passive",
                "table_rows": [
                    ["Neutral: A gyűjtemény el van helyezve.", "The collection is housed / installed (state focus)."],
                    ["Location focus: A Budai Várban van elhelyezve.", "It is housed IN BUDA CASTLE (location focus)."],
                    ["Manner focus: Gondosan van restaurálva.", "It is CAREFULLY restored."],
                    ["Causal -ván: Megvásárolván a képtárat...", "Having purchased the gallery, the state created..."]
                ],
                "examples": [
                    {"spanish": "A magyar festészet gyűjteménye ma a Budai Várpalotában van elhelyezve.", "english": "Today the collection of Hungarian painting is housed in Buda Castle Palace."},
                    {"spanish": "A galéria termeit végigjárva a látogató végigkövetheti a művészet alakulását.", "english": "Walking through the halls of the gallery, the visitor can trace the evolution of art."},
                    {"spanish": "Az állam megvásárolván az Esterházy-képtárat, megteremtette a múzeum alapját.", "english": "Having purchased the Esterházy picture gallery, the state created the foundation of the museum."}
                ],
                "tip": "Remember the focus rule: Neutral = Prefix + van + stem-va (el van helyezve); Focused Location/Adverb = [Location] + van + prefix-stem-va (a Budai Várban van elhelyezve)!"
            },
            "exercises": [
                {
                    "type": "matching",
                    "category": "vocabulary",
                    "stage": "introduce",
                    "teaches": ["b2-festeszet-vocab"],
                    "pairs": [
                        ["közgyűjtemény", "public collection"],
                        ["műgyűjtő", "art collector"],
                        ["mecénás", "art patron"],
                        ["restaurálás", "restoration"],
                        ["szárnyas oltár", "winged altarpiece"],
                        ["műkincs", "art treasure"]
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "question": "Melyik főnemesi család világhírű képtárának 1871-es állami megvásárlása alapozta meg a budapesti Szépművészeti Múzeumot?",
                    "options": [
                        "Az Esterházy hercegek képtárának megvásárlása.",
                        "A Bauhaus dessaui műhelyének megvásárlása.",
                        "A kaposvári színház díszleteinek megvásárlása."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "stage": "controlled",
                    "teaches": ["b2-festeszet-vocab"],
                    "sentence": "A háborúban megsérült festmények gondos _____ után visszanyerték eredeti színeiket.",
                    "answer": "restaurálás",
                    "english": "After careful restoration, the paintings damaged in the war regained their original colors."
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "stage": "controlled",
                    "teaches": ["b2-adverbial-participles"],
                    "question": "Why does the prefix stay attached in 'A gyűjtemény a Budai Várban van elhelyezve' instead of splitting ('el van helyezve')?",
                    "options": [
                        "Because the locative phrase 'a Budai Várban' is in the pre-verbal focus position right before 'van'.",
                        "Because 'elhelyezve' is a noun rather than a participle.",
                        "Because 'van' is in the subjunctive mood.",
                        "Because the sentence is negative."
                    ],
                    "correct": 0
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "sentence": "A Magyar Nemzeti Galéria termeit _____ a látogató megcsodálhatja a szárnyas oltárokat. (végigjár - adverbial participle)",
                    "answer": "végigjárva",
                    "english": "Walking through the halls of the Hungarian National Gallery, the visitor can admire the winged altarpieces."
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "stage": "practice",
                    "teaches": ["b2-adverbial-participles"],
                    "tiles": ["A", "gyűjtemény", "a", "Budai", "Várpalotában", "van", "elhelyezve."],
                    "solution": ["A", "gyűjtemény", "a", "Budai", "Várpalotában", "van", "elhelyezve."],
                    "english": "The collection is housed in Buda Castle Palace."
                },
                {
                    "type": "dialogue-complete",
                    "category": "dialogue",
                    "stage": "dialogue",
                    "teaches": ["b2-adverbial-participles"],
                    "prompt": [
                        {"speaker": "Turista", "text": "Hol láthatom Budapesten Szinyei Merse Majálisát és a középkori magyar szárnyas oltárokat?"},
                        {"speaker": "Idegenvezető", "text": "_____"}
                    ],
                    "options": [
                        "A magyar festészet történeti gyűjteménye a Budai Várban, a Magyar Nemzeti Galériában van elhelyezve.",
                        "Ezek a képek a Vígszínház zenekari árkában vannak elrejtve.",
                        "Minden festmény el lett adva ponyvának."
                    ],
                    "correct": 0
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "stage": "reading",
                    "question": "Melyik két neoklasszicista művészeti intézmény áll egymással szemben a budapesti Hősök terén?",
                    "options": [
                        "A Szépművészeti Múzeum és a Műcsarnok.",
                        "A Nemzeti Színház és az Operettszínház.",
                        "A Zeneakadémia és a Déri Múzeum."
                    ],
                    "correct": 0
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can trace Hungarian visual art from Munkácsy's salon realism and Szinyei Merse's Majális through the Nagybánya colony and Csontváry's cosmic visions to Moholy-Nagy at the Bauhaus.",
            "I can form and use active adverbial participles in -va/-ve for both simultaneous manner and anterior sequence.",
            "I can recognize and employ literary causal participles in -ván/-vén (including lévén).",
            "I can construct both neutral (meg van világítva) and focus-shifted (a Budai Várban van elhelyezve) stative passives."
        ],
        "exercises": [
            {
                "type": "matching",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-festeszet-vocab"],
                "pairs": [
                    ["műterem", "artist's studio"],
                    ["művésztelep", "artists' colony"],
                    ["önarckép", "self-portrait"],
                    ["fotogram", "cameraless photograph"],
                    ["közgyűjtemény", "public collection"],
                    ["restaurálás", "art restoration"]
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "teaches": ["b2-adverbial-participles"],
                "question": "Which sentence illustrates a focused-location stative passive?",
                "options": [
                    "A festmények a Budai Várpalotában vannak elhelyezve.",
                    "A festő a tájat tanulmányozva keverte a színeket.",
                    "Magányos zseni lévén nem csatlakozott az iskolához.",
                    "A látogató megállt a vászon előtt."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "teaches": ["b2-festeszet-vocab"],
                "question": "Melyik fogalom jelenti azt a tehetős műpártolót, aki anyagi támogatásával segíti a művészeket és a múzeumokat?",
                "options": ["mecénás", "vándorszínész", "prímás", "cenzor"],
                "correct": 0
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "teaches": ["b2-festeszet-vocab"],
                "sentence": "A nagybányai festők a szabad ég alatt, közvetlenül a természetben állították fel a _____-aikat.",
                "answer": "festőállvány",
                "english": "The painters of Nagybánya set up their easels in the open air, directly in nature."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-adverbial-participles"],
                "sentence": "Münchenből _____ Hollósy Simonék megalapították a nagybányai művésztelepet. (hazatér - adverbial participle)",
                "answer": "hazatérve",
                "english": "Having returned home from Munich, Simon Hollósy and his colleagues founded the Nagybánya artists' colony."
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "teaches": ["b2-adverbial-participles"],
                "sentence": "Független alkotó _____ Csontváry nem tartozott egyetlen festőiskolához sem. (van - literary participle)",
                "answer": "lévén",
                "english": "Being an independent creator, Csontváry did not belong to any school of painting."
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-adverbial-participles"],
                "prompt": [
                    {"speaker": "Látogató", "text": "Hogyan működik Moholy-Nagy László Fény-tér-modulátora a kiállítóteremben?"},
                    {"speaker": "Kurátor", "text": "_____"}
                ],
                "options": [
                    "Amikor a szerkezet forgásba van hozva és reflektorokkal meg van világítva, mozgó árnyékformákat vetít a falra.",
                    "A kertben üldögélve festették meg olajfestékkel a vászonra.",
                    "Nehogy bárki bekapcsolja a világítást a teremben."
                ],
                "correct": 0
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "teaches": ["b2-adverbial-participles"],
                "question": "Choose the sentence where the -ván/-vén participle expresses a causal reason ('Since he saw the danger...'):",
                "options": [
                    "Látván a veszélyt, hogy a vásznakat eladják ponyvának, Gerlóczy azonnal megvette őket.",
                    "A szobor reflektorokkal meg van világítva.",
                    "A fűben hasalva élvezték a tavaszi napsütést.",
                    "A falakon képek vannak felakasztva."
                ],
                "correct": 0
            },
            {
                "type": "dialogue-complete",
                "category": "dialogue",
                "stage": "in-context",
                "teaches": ["b2-adverbial-participles"],
                "prompt": [
                    {"speaker": "Restaurátor", "text": "Miért sötétedtek be Munkácsy Mihály korai festményei az évtizedek során?"},
                    {"speaker": "Művészettörténész", "text": "_____"}
                ],
                "options": [
                        "Sötét bitumenes alapozást használva érte el a drámai fény-árnyék hatást, ám ez az anyag idővel kémiailag megváltozott.",
                        "Mert a képek a szabad ég alatt voltak hagyva a Zazar folyó partján.",
                        "Mert fényérzékeny papírra voltak helyezve."
                    ],
                "correct": 0
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-adverbial-participles"],
                "tiles": ["A", "galéria", "termeit", "végigjárva", "megcsodáltuk", "a", "festményeket."],
                "solution": ["A", "galéria", "termeit", "végigjárva", "megcsodáltuk", "a", "festményeket."],
                "english": "Walking through the halls of the gallery, we admired the paintings."
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "teaches": ["b2-adverbial-participles"],
                "tiles": ["A", "festmények", "korszerű", "világítással", "vannak", "ellátva."],
                "solution": ["A", "festmények", "korszerű", "világítással", "vannak", "ellátva."],
                "english": "The paintings are equipped with modern lighting."
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "teaches": ["b2-adverbial-participles"],
                "template": [
                    {
                        "prompt": "Write a sentence explaining how the Nagybánya painters worked after stepping out of dark studios (use a prefixed -va/-ve participle).",
                        "answer": "A sötét akadémiai műtermekből a szabad ég alá kilépve közvetlenül a természetben festették meg a napfényt."
                    },
                    {
                        "prompt": "Write a sentence describing where the historical collection of Hungarian painting is housed today (use a stative passive construction with 'van elhelyezve').",
                        "answer": "A magyar festészet történeti gyűjteménye ma a Budai Várpalotában, a Magyar Nemzeti Galériában van elhelyezve."
                    }
                ]
            }
        ]
    }
}


def main():
    for spec in (UNIT_04_SZINHAZMUVESZET, UNIT_05_BARTOKKODALY, UNIT_06_FESTESZET):
        build_culture_unit(spec)


if __name__ == "__main__":
    main()
