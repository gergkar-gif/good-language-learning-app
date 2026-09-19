#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 15: The Reform Age (b1-reformkor)."""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_json(rel_path, data):
    full_path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

def build_unit_15_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.reformkor.01",
        "lesson": "b1-reformkor-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Széchenyi István", "translation": "Count István Széchenyi", "pos": "noun"},
            {"lemma": "a legnagyobb magyar", "translation": "'the Greatest Hungarian'", "pos": "noun"},
            {"lemma": "Tudományos Akadémia", "translation": "Hungarian Academy of Sciences", "pos": "noun"},
            {"lemma": "egyévi jövedelem", "translation": "one year's income / estate revenue", "pos": "noun"},
            {"lemma": "birtokos nemes", "translation": "landowning nobleman", "pos": "noun"},
            {"lemma": "nemzetfejlesztés", "translation": "national development", "pos": "noun"},
            {"lemma": "Hitel", "translation": "Credit (Széchenyi's 1830 book)", "pos": "noun"},
            {"lemma": "polgárosodás", "translation": "bourgeois transformation, modernization", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-reformkor-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.reformkor.02",
        "lesson": "b1-reformkor-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Lánchíd", "translation": "Chain Bridge (Buda-Pest)", "pos": "noun"},
            {"lemma": "Duna-szabályozás", "translation": "regulation of the Danube", "pos": "noun"},
            {"lemma": "Vaskapu", "translation": "Iron Gates (Danube gorge)", "pos": "noun"},
            {"lemma": "gőzhajózás", "translation": "steam navigation", "pos": "noun"},
            {"lemma": "hídpénz", "translation": "bridge toll", "pos": "noun"},
            {"lemma": "nemesi adómentesség megtörése", "translation": "breaking noble tax exemption", "pos": "noun"},
            {"lemma": "modernizáció", "translation": "modernization", "pos": "noun"},
            {"lemma": "infrastruktúra", "translation": "infrastructure", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-reformkor-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.reformkor.03",
        "lesson": "b1-reformkor-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Kossuth Lajos", "translation": "Lajos Kossuth", "pos": "noun"},
            {"lemma": "Országgyűlési Tudósítások", "translation": "Parliamentary Reports", "pos": "noun"},
            {"lemma": "Pesti Hírlap", "translation": "Pesti Hírlap newspaper", "pos": "noun"},
            {"lemma": "politikai sajtó", "translation": "political press, journalism", "pos": "noun"},
            {"lemma": "cenzúra kijátszása", "translation": "circumventing censorship", "pos": "noun"},
            {"lemma": "közteherviselés", "translation": "universal taxation, public burden sharing", "pos": "noun"},
            {"lemma": "jobbágyfelszabadítás", "translation": "emancipation of serfs", "pos": "noun"},
            {"lemma": "szónoki tehetség", "translation": "oratorical talent, eloquence", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-reformkor-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.reformkor.04",
        "lesson": "b1-reformkor-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hivatalos nyelv", "translation": "official state language", "pos": "noun"},
            {"lemma": "1844-es nyelvtörvény", "translation": "Language Act of 1844", "pos": "noun"},
            {"lemma": "latin nyelv háttérbe szorulása", "translation": "replacement of Latin language", "pos": "noun"},
            {"lemma": "Kölcsey Ferenc", "translation": "Ferenc Kölcsey", "pos": "noun"},
            {"lemma": "Himnusz", "translation": "Hungarian National Anthem (1823)", "pos": "noun"},
            {"lemma": "Vörösmarty Mihály", "translation": "Mihály Vörösmarty", "pos": "noun"},
            {"lemma": "Szózat", "translation": "Szózat (Appeal - 1836 anthem)", "pos": "noun"},
            {"lemma": "Nemzeti Színház", "translation": "National Theatre (opened 1837)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-reformkor-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.reformkor.05",
        "lesson": "b1-reformkor-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Védegylet", "translation": "Protection Association (1844)", "pos": "noun"},
            {"lemma": "magyar ipar támogatása", "translation": "support of domestic industry", "pos": "noun"},
            {"lemma": "Pilvax kávéház", "translation": "Pilvax Café (meeting place of youths)", "pos": "noun"},
            {"lemma": "fiatal értelmiség", "translation": "young intelligentsia, March Youths", "pos": "noun"},
            {"lemma": "reformországgyűlés", "translation": "Reform Diet", "pos": "noun"},
            {"lemma": "forradalmi hangulat", "translation": "revolutionary mood, atmosphere", "pos": "noun"},
            {"lemma": "európai változások", "translation": "European changes, Spring of Nations", "pos": "noun"},
            {"lemma": "nemzeti megújulás", "translation": "national renewal", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-reformkor-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.reformkor.01.evidential-allitolag",
        "title": "Evidential & Modal Particles: állítólag, bizonyára, feltehetően",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Degrees of Certainty and Hearsay",
                "content": "To report opinions, rumours, and historical assessments: *állítólag* (allegedly / supposedly), *bizonyára* (surely / certainly), *feltehetően* (presumably): *Széchenyi állítólag már ifjúkorában megfogadta, hogy felemeli a nemzetet.*"
            },
            {
                "type": "examples",
                "title": "Evidential particles in history",
                "items": [
                    {
                        "spanish": "Kossuth szónoki beszédei bizonyára minden hallgatót magukkal ragadtak.",
                        "english": "Kossuth's oratorical speeches surely captivated every listener."
                    },
                    {
                        "spanish": "A bécsi kancellária állítólag titkos megfigyelőket küldött Pozsonyba.",
                        "english": "The Viennese chancellery allegedly sent secret observers to Pozsony."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-reformkor-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.reformkor.02.modal-particles-bizonyara",
        "title": "Deduction and Logical Probability: kétségkívül, nyilvánvalóan, aligha",
        "sections": [
            {
                "type": "text",
                "title": "Formulating Analytical Judgments",
                "content": "Analytical historical discourse uses logical probability markers: *kétségkívül* (undoubtedly), *nyilvánvalóan* (obviously), *aligha* (hardly / scarcely): *Széchenyi nélkül kétségkívül lassabb lett volna a modernizáció.*"
            },
            {
                "type": "examples",
                "title": "Deduction examples",
                "items": [
                    {
                        "spanish": "A Lánchíd felépítése kétségkívül a polgári átalakulás szimbóluma volt.",
                        "english": "The construction of the Chain Bridge was undoubtedly the symbol of bourgeois transformation."
                    },
                    {
                        "spanish": "A cenzúra aligha tudta megállítani a független sajtó terjedését.",
                        "english": "Censorship could hardly stop the spread of the independent press."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-reformkor-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.reformkor.03.reformist-imperatives-kell",
        "title": "Debating Political Necessity: szükséges, elengedhetetlen, kell",
        "sections": [
            {
                "type": "text",
                "title": "The Rhetoric of Political Reform",
                "content": "Reform debates argue what *must* be done using predicative adjectives: *elengedhetetlen, hogy... + subjunctive* (it is indispensable that...), *halaszthatatlan feladat* (an urgent task that cannot be postponed)."
            },
            {
                "type": "examples",
                "title": "Reform rhetoric examples",
                "items": [
                    {
                        "spanish": "Kossuth szerint elengedhetetlen volt, hogy a nemesség is adót fizessen.",
                        "english": "According to Kossuth, it was indispensable that the nobility also pay tax."
                    },
                    {
                        "spanish": "A jobbágyfelszabadítás halaszthatatlan feladattá vált a nemzet számára.",
                        "english": "The emancipation of serfs became an urgent task for the nation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-reformkor-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.reformkor.04.temporal-pre-revolution",
        "title": "Pre-Revolutionary Anticipation: küszöbén áll, közeledtére, nyomában",
        "sections": [
            {
                "type": "text",
                "title": "Expressions of Anticipation and Thresholds",
                "content": "Narrating the eve of major change: *valaminek a küszöbén áll* (stands on the threshold of something), *valaminek a hatására* (under the impact of something), *nap mint nap érezhetővé vált* (became perceptible day by day)."
            },
            {
                "type": "examples",
                "title": "Threshold examples",
                "items": [
                    {
                        "spanish": "1848 tavaszán Magyarország a forradalmi átalakulás küszöbén állt.",
                        "english": "In the spring of 1848, Hungary stood on the threshold of revolutionary transformation."
                    },
                    {
                        "spanish": "A párizsi események hírére forradalmi hangulat uralkodott el Pesten.",
                        "english": "At the news of the Paris events, a revolutionary mood took hold of Pest."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-reformkor-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.reformkor.05.epithets-apposition",
        "title": "Historical Epithets in Apposition: Széchenyi, a legnagyobb magyar",
        "sections": [
            {
                "type": "text",
                "title": "Honorific Epithets in Hungarian History",
                "content": "Great figures carry fixed appositive epithets: *Széchenyi István, a legnagyobb magyar* ('the Greatest Hungarian'), *Deák Ferenc, a haza bölcse* ('the Sage of the Homeland'), *Kossuth Lajos, a nemzet szónoka*."
            },
            {
                "type": "examples",
                "title": "Epithet examples",
                "items": [
                    {
                        "spanish": "Kossuth nevezte Széchenyit a legnagyobb magyarnak a viták ellenére.",
                        "english": "It was Kossuth who called Széchenyi the greatest Hungarian, despite their debates."
                    },
                    {
                        "spanish": "Kölcsey Ferenc Himnusz című verse a nemzet imádságává vált.",
                        "english": "Ferenc Kölcsey's poem Himnusz became the prayer of the nation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-reformkor-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (01 to 05 + Omnibus) in TRIH Narrative Style
    # -------------------------------------------------------------------------
    stories_content = {
        "b1-reformkor-01-szechenyi.json": [
            "1825 őszén Pozsonyban a fiatal gróf, Széchenyi István olyan lépést tett, amely örökre megváltoztatta Magyarországot.",
            "A gazdag birtokos nemes felállt az országgyűlésen, és birtokainak teljes egyévi jövedelem összegét ajánlotta fel.",
            "Ebből a nemes felajánlásból született meg a Magyar Tudományos Akadémia a magyar nyelv és tudomány ápolására.",
            "1830-ban megjelent korszakalkotó könyve, a Hitel, amely a modern polgárosodás gazdasági programját hirdette meg.",
            "Kossuth Lajos méltán nevezte őt így: a legnagyobb magyar. Széchenyi zseniális nemzetfejlesztés munkája elindította a reformkort."
        ],
        "b1-reformkor-02-lanchid.json": [
            "Hogyan lehet összekötni egy folyó által elválasztott két történelmi várost? Széchenyi merész álmokat szőtt.",
            "Elindult a nagyszabású Duna-szabályozás, a Vaskapu szikláinak átrobbantásával pedig megnyílt a modern gőzhajózás útja.",
            "Felépült az első állandó kőhíd, a csodálatos Lánchíd, amely Buda és Pest szívét kapcsolta össze.",
            "A híd átadásakor a hídpénz fizetése mindenkire kötelező volt, ezzel megkezdődött a nemesi adómentesség megtörése.",
            "A korszerű infrastruktúra és a gyors modernizáció révén a magyar főváros Közép-Európa virágzó központjává fejlődött."
        ],
        "b1-reformkor-03-kossuth.json": [
            "Miközben Széchenyi hidakat és gyárakat épített, egy zseniális ügyvéd a szavak erejével ébresztette fel az országot.",
            "Kossuth Lajos a diákok segítségével kézzel másolta az Országgyűlési Tudósítások lapjait, hogy a cenzúra kijátszása sikerüljön.",
            "Később a Pesti Hírlap szerkesztőjeként megteremtette az első modern politikai sajtó felületét a nemzet számára.",
            "Páratlan szónoki tehetség révén két forradalmi eszmét hirdetett: a közteherviselést és a teljes jobbágyfelszabadítás ügyét.",
            "Kossuth szenvedélyes hangja milliókhoz jutott el, és a reformellenzék legfőbb vezéralakjává emelte a fiatal politikust."
        ],
        "b1-reformkor-04-nyelv.json": [
            "Évszázadokon át a latin volt az országgyűlés nyelve. De mikor szólalhatott meg a haza végre a saját anyanyelvén?",
            "1844-ben a rendek elfogadták a történelmi 1844-es nyelvtörvény rendelkezését, amellyel a magyar lett a hivatalos nyelv.",
            "Ezzel lezárult a latin nyelv háttérbe szorulása a közigazgatásban, a bíróságokon és a felsőfokú oktatásban.",
            "Kölcsey Ferenc 1823-ban megírta a nemzet imádságát, a Himnusz költeményt, Vörösmarty Mihály pedig a hazafias Szózat sorait.",
            "Megnyitotta kapuit a pesti Nemzeti Színház is, ahol a magyar színjátszás a nemzeti önazonosság szent temploma lett."
        ],
        "b1-reformkor-05-forradalom.json": [
            "1848 kora tavaszán forró izgalom vibrált a levegőben. Európa városaiban sorra törtek ki a felkelések.",
            "Kossuth kezdeményezésére megalakult a Védegylet, amely hat éven át a magyar ipar támogatása mellett kötelezte el tagjait.",
            "A pesti Pilvax kávéház füstös termeiben a forradalmi fiatal értelmiség Petőfi Sándor és Jókai Mór körül gyülekezett.",
            "A pozsonyi reformországgyűlés termeiben a követek feszülten figyelték a megrázó európai változások híreit.",
            "A forradalmi hangulat tetőfokára hágott: a nemzeti megújulás órája megkondult, és készen állt a március 15-i csoda."
        ],
        "b1-reformkor.json": [
            "1825-ben Széchenyi István egyévi jövedelmét felajánlva megalapította a Magyar Tudományos Akadémiát, elindítva a reformkort.",
            "Széchenyi megépítette a Lánchidat, szabályozta a Dunát, és a hídpénzzel megtörte a nemesség adómentességét.",
            "Kossuth Lajos a Pesti Hírlapban a jobbágyfelszabadításért és az általános közteherviselésért harcolt zseniális szónoklatokkal.",
            "1844-ben a magyar lett a hivatalos államnyelv, miközben Kölcsey Himnusza és Vörösmarty Szózata nemzeti szimbólummá vált.",
            "A Pilvax kávéházban gyülekező fiatalok készen álltak a cselekvésre: 1848 tavaszán a reformok átadták helyüket a forradalomnak."
        ]
    }

    write_json("content/hu/stories/world/b1/b1-reformkor-01-szechenyi.json", {
        "id": "story.b1.reformkor.01",
        "title": "Széchenyi István, a legnagyobb magyar",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How Count István Széchenyi offered one year of his income to found the Academy of Sciences and published 'Hitel' (Credit), launching the Reform Era.",
        "characters": ["Széchenyi István", "Magyar követek"],
        "location": "Pozsony, Pest",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor-01-szechenyi.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-reformkor-02-lanchid.json", {
        "id": "story.b1.reformkor.02",
        "title": "A Lánchíd és a korszerű modernizáció",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The construction of the Chain Bridge linking Buda and Pest, Danube river regulation, steam shipping, and breaking the nobility's ancient tax exemption.",
        "characters": ["Széchenyi István", "Clark Ádám"],
        "location": "Buda, Pest, Duna",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor-02-lanchid.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-reformkor-03-kossuth.json", {
        "id": "story.b1.reformkor.03",
        "title": "Kossuth Lajos és a független politikai sajtó",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Lajos Kossuth's courageous journalism: evading Habsburg censorship with handwritten parliamentary reports, editing Pesti Hírlap, and championing serf emancipation.",
        "characters": ["Kossuth Lajos", "Pesti szerkesztők"],
        "location": "Pozsony, Pest",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor-03-kossuth.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-reformkor-04-nyelv.json", {
        "id": "story.b1.reformkor.04",
        "title": "A magyar nyelv diadala és nemzeti jelképei",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The landmark 1844 language law making Hungarian the official state language, Kölcsey's Himnusz, Vörösmarty's Szózat, and the founding of the National Theatre.",
        "characters": ["Kölcsey Ferenc", "Vörösmarty Mihály"],
        "location": "Pozsony, Pest",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor-04-nyelv.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-reformkor-05-forradalom.json", {
        "id": "story.b1.reformkor.05",
        "title": "A forradalom küszöbén: a Pilvax és a márciusi ifjak",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The electric atmosphere on the eve of March 1848: the Védegylet, young radicals at the Pilvax café, European uprisings, and the threshold of revolution.",
        "characters": ["Petőfi Sándor", "Jókai Mór", "Vasvári Pál"],
        "location": "Pest, Pilvax kávéház",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor-05-forradalom.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-reformkor.json", {
        "id": "story.b1.reformkor",
        "title": "A reformkor (1825–1848)",
        "level": "B1",
        "order": 15,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The magnificent saga of the Hungarian Reform Era: Széchenyi's foundational vision, the Chain Bridge, Kossuth's political press, the 1844 language act, and the eve of 1848.",
        "characters": ["Széchenyi István", "Kossuth Lajos", "Petőfi Sándor"],
        "location": "Magyarország, Pozsony, Pest",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-reformkor.json"]]
    })

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-reformkor-01",
        "exercises": [
            {
                "id": "b1-reformkor-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Széchenyi István", "Count István Széchenyi"],
                    ["a legnagyobb magyar", "'the Greatest Hungarian'"],
                    ["Tudományos Akadémia", "Academy of Sciences"],
                    ["egyévi jövedelem", "one year's estate income"]
                ]
            },
            {
                "id": "b1-reformkor-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["birtokos nemes", "landowning nobleman"],
                    ["nemzetfejlesztés", "national development"],
                    ["Hitel", "Credit (1830 book)"],
                    ["polgárosodás", "bourgeois transformation"]
                ]
            },
            {
                "id": "b1-reformkor-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit ajánlott fel Széchenyi István az 1825-ös pozsonyi országgyűlésen?",
                "options": [
                    "Birtokainak teljes egyévi jövedelmét a Tudományos Akadémia megalapítására.",
                    "Arany kardját a császárnak.",
                    "A bécsi palotáját a francia nagykövetnek."
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-01.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1830-ban jelent meg Széchenyi korszakalkotó gazdasági műve a ____. (Credit)",
                "answer": "Hitel"
            },
            {
                "id": "b1-reformkor-01.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Széchenyi gróf ____ már gyermekkorában megfogadta a nemzet szolgálatát. (supposedly / allegedly)",
                "answer": "állítólag"
            },
            {
                "id": "b1-reformkor-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kinek a szavait idézzük, amikor Széchenyit 'a legnagyobb magyarnak' nevezzük?",
                "options": [
                    "Kossuth Lajosét",
                    "Napóleonét",
                    "Mátyás királyét"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A polgárosodás és a gazdasági fejlődés elindítása Széchenyi legfőbb célkitűzése volt.",
                "tiles": ["A", "polgárosodás", "és", "a", "gazdasági", "fejlődés", "elindítása", "Széchenyi", "legfőbb", "célkitűzése", "volt."]
            },
            {
                "id": "b1-reformkor-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gazdag ____ felajánlása után más főurak is jelentős összegekkel támogatták az Akadémiát. (landowning noble)",
                "answer": "birtokos nemes"
            },
            {
                "id": "b1-reformkor-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért tartjuk 1825-öt vagy 1830-at a magyar reformkor kezdetének?",
                "options": [
                    "Mert ekkor indult meg a szervezett társadalmi és gazdasági megújulás a polgári Magyarországért.",
                    "Mert ekkor vezették be a vasutat Amerikában.",
                    "Mert ekkor épült fel a budapesti metró."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-reformkor-02",
        "exercises": [
            {
                "id": "b1-reformkor-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Lánchíd", "Chain Bridge"],
                    ["Duna-szabályozás", "Danube regulation"],
                    ["Vaskapu", "Iron Gates"],
                    ["gőzhajózás", "steam navigation"]
                ]
            },
            {
                "id": "b1-reformkor-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hídpénz", "bridge toll"],
                    ["nemesi adómentesség megtörése", "breaking noble tax exemption"],
                    ["modernizáció", "modernization"],
                    ["infrastruktúra", "infrastructure"]
                ]
            },
            {
                "id": "b1-reformkor-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért volt a Lánchíd megépítése forradalmi jogi lépés a nemesség számára?",
                "options": [
                    "Mert a hídpénzt a nemeseknek is meg kellett fizetniük, ami megtörte az adómentességet.",
                    "Mert a nemesek nem mehettek át a hídon gyalog.",
                    "Mert a hídon aranyból készültek a láncok."
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Buda és Pest közötti első állandó kőhíd a csodálatos ____ lett. (Chain Bridge)",
                "answer": "Lánchíd"
            },
            {
                "id": "b1-reformkor-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Lánchíd felépítése ____ az ország polgári átalakulásának jelképévé vált. (undoubtedly)",
                "answer": "kétségkívül"
            },
            {
                "id": "b1-reformkor-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik veszélyes folyószakasz szikláit robbantották ki a Duna hajózhatóvá tételére?",
                "options": [
                    "a Vaskaput",
                    "a Rajna vízesést",
                    "a Szuez-csatornát"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A folyók szabályozása és a gőzhajózás megindítása új lendületet adott a kereskedelemnek.",
                "tiles": ["A", "folyók", "szabályozása", "és", "a", "gőzhajózás", "megindítása", "új", "lendületet", "adott", "a", "kereskedelemnek."]
            },
            {
                "id": "b1-reformkor-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A korszerű ____ kiépítése nélkül a magyar gazdaság nem tudott volna bekapcsolódni Európa vérkeringésébe. (infrastructure)",
                "answer": "infrastruktúra"
            },
            {
                "id": "b1-reformkor-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki tervezte és építette a Lánchidat Széchenyi felkérésére?",
                "options": [
                    "William Tierney Clark és Clark Ádám angol mérnökök.",
                    "Eiffel mérnök Párizsból.",
                    "Leonardo da Vinci."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-reformkor-03",
        "exercises": [
            {
                "id": "b1-reformkor-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Kossuth Lajos", "Lajos Kossuth"],
                    ["Országgyűlési Tudósítások", "Parliamentary Reports"],
                    ["Pesti Hírlap", "Pesti Hírlap newspaper"],
                    ["politikai sajtó", "political press"]
                ]
            },
            {
                "id": "b1-reformkor-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["cenzúra kijátszása", "circumventing censorship"],
                    ["közteherviselés", "universal public burden sharing"],
                    ["jobbágyfelszabadítás", "serf emancipation"],
                    ["szónoki tehetség", "oratorical talent"]
                ]
            },
            {
                "id": "b1-reformkor-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan játszotta ki Kossuth a szigorú bécsi cenzúrát az 1830-as években?",
                "options": [
                    "Kézzel másolt magánlevelekként terjesztette az országgyűlés valódi eseményeit.",
                    "Titkos rádióadót üzemeltetett a pincében.",
                    "Megvesztegette a bécsi rendőrfőnököt."
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1841-től Kossuth a ____ szerkesztőjeként a reformeszmék legfőbb szószólója lett. (Pesti Hírlap)",
                "answer": "Pesti Hírlap"
            },
            {
                "id": "b1-reformkor-03.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kossuth szerint elengedhetetlen volt, hogy megvalósuljon a teljes jobbágyfelszabadítás. (indispensable)",
                "answer": "elengedhetetlen"
            },
            {
                "id": "b1-reformkor-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit követelt a reformellenzék a földművelő parasztság helyzetének megváltoztatására?",
                "options": [
                    "jobbágyfelszabadítást kártalanítással",
                    "további robotmunkát ingyen",
                    "a parasztok elköltöztetését külföldre"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Kossuth Lajos szónoki beszédei hatalmas lelkesedést váltottak ki a reformországgyűlés ifjúsága körében.",
                "tiles": ["Kossuth", "Lajos", "szónoki", "beszédei", "hatalmas", "lelkesedést", "váltottak", "ki", "a", "reformországgyűlés", "ifjúsága", "körében."]
            },
            {
                "id": "b1-reformkor-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A polgári Magyarország megteremtésének alapköve a nemesi adómentesség eltörlése és az általános ____ volt. (universal taxation)",
                "answer": "közteherviselés"
            },
            {
                "id": "b1-reformkor-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miben különbözött Széchenyi és Kossuth politikai látásmódja?",
                "options": [
                    "Széchenyi óvatos, felülről irányított gazdasági reformokat akart, míg Kossuth gyors társadalmi és politikai átalakulást sürgetett.",
                    "Széchenyi a törököket akarta visszahívni, Kossuth pedig Ausztriához akart csatlakozni.",
                    "Nem volt semmilyen különbség köztük."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-reformkor-04",
        "exercises": [
            {
                "id": "b1-reformkor-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hivatalos nyelv", "official state language"],
                    ["1844-es nyelvtörvény", "Language Act of 1844"],
                    ["Kölcsey Ferenc", "author of Himnusz"],
                    ["Vörösmarty Mihály", "author of Szózat"]
                ]
            },
            {
                "id": "b1-reformkor-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["latin nyelv háttérbe szorulása", "replacement of Latin"],
                    ["Himnusz", "Hungarian National Anthem (1823)"],
                    ["Szózat", "Szózat (1836 anthem)"],
                    ["Nemzeti Színház", "National Theatre (1837)"]
                ]
            },
            {
                "id": "b1-reformkor-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben lett a magyar az állam hivatalos nyelve a latin helyett?",
                "options": [
                    "1844-ben",
                    "1526-ban",
                    "1956-ban"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az 1823-ban Csekén írt költemény, a ____ zenéjét Erkel Ferenc szerezte. (National Anthem)",
                "answer": "Himnusz"
            },
            {
                "id": "b1-reformkor-04.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kölcsey Ferenc remekműve a nemzet legszentebb közös imádságává ____. (became / has become)",
                "answer": "vált"
            },
            {
                "id": "b1-reformkor-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik híres vers kezdődik így: 'Hazádnak rendületlenül légy híve, ó magyar'?",
                "options": [
                    "Vörösmarty Mihály: Szózat",
                    "Petőfi Sándor: Nemzeti dal",
                    "Arany János: Toldi"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "1837-ben Pesten megnyílt a Nemzeti Színház a magyar anyanyelv és kultúra ápolására.",
                "tiles": ["1837-ben", "Pesten", "megnyílt", "a", "Nemzeti", "Színház", "a", "magyar", "anyanyelv", "és", "kultúra", "ápolására."]
            },
            {
                "id": "b1-reformkor-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A történelmi ____ kimondta, hogy a törvényeket és a rendeleteket kizárólag magyar nyelven kell megszövegezni. (1844 language act)",
                "answer": "1844-es nyelvtörvény"
            },
            {
                "id": "b1-reformkor-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi a Himnusz és a Szózat legfontosabb közös üzenete?",
                "options": [
                    "A hazaszeretet, a nemzeti hűség és az áldozathozatal a magyar nemzet megmaradásáért.",
                    "Hogy a királyi udvarnak mindig igazat kell adni.",
                    "Hogy a színházakban nem szabad verseket szavalni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-reformkor-05",
        "exercises": [
            {
                "id": "b1-reformkor-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Védegylet", "Protection Association (1844)"],
                    ["magyar ipar támogatása", "support of domestic industry"],
                    ["Pilvax kávéház", "Pilvax Café"],
                    ["fiatal értelmiség", "young intelligentsia"]
                ]
            },
            {
                "id": "b1-reformkor-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["reformországgyűlés", "Reform Diet"],
                    ["forradalmi hangulat", "revolutionary mood"],
                    ["európai változások", "European changes (Spring of Nations)"],
                    ["nemzeti megújulás", "national renewal"]
                ]
            },
            {
                "id": "b1-reformkor-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol gyülekeztek a pesti fiatal radikális költők és írók 1848 márciusában?",
                "options": [
                    "a Pilvax kávéházban",
                    "a bécsi operában",
                    "a pozsonyi várudvaron"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Kossuth kezdeményezésére jött létre a ____ a hazai termékek védelmére. (Protection Association)",
                "answer": "Védegylet"
            },
            {
                "id": "b1-reformkor-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1848 kora tavaszán Magyarország a nagy történelmi forradalom küszöbén állt. (on the threshold of)",
                "answer": "küszöbén állt"
            },
            {
                "id": "b1-reformkor-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki volt a Pilvax kávéházban gyülekező márciusi ifjak legismertebb költő vezére?",
                "options": [
                    "Petőfi Sándor",
                    "Károly Róbert",
                    "Szulejmán szultán"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A forradalmi hangulat napról napra erősödött a pesti egyetemi ifjúság körében.",
                "tiles": ["A", "forradalmi", "hangulat", "napról", "napra", "erősödött", "a", "pesti", "egyetemi", "ifjúság", "körében."]
            },
            {
                "id": "b1-reformkor-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A párizsi forradalom hírére a pozsonyi ____ követei azonnal a reformok elfogadását követelték. (Reform Diet)",
                "answer": "reformországgyűlés"
            },
            {
                "id": "b1-reformkor-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan vezetett a reformkor közvetlenül az 1848. március 15-i forradalomhoz?",
                "options": [
                    "A két évtizedes szellemi és gazdasági előkészítés megteremtette a polgári átalakulás programját és a nemzet egységét.",
                    "A reformkor elbukott és az emberek elfelejtették a terveket.",
                    "Ausztria császára kérte fel a pesti diákokat a forradalomra."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-reformkor-consolidation",
        "exercises": [
            {
                "id": "b1-reformkor-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Széchenyi István", "a legnagyobb magyar"],
                    ["Lánchíd", "hídpénz fizetése"],
                    ["Kossuth Lajos", "Pesti Hírlap & jobbágyfelszabadítás"],
                    ["1844-es nyelvtörvény", "magyar mint hivatalos államnyelv"]
                ]
            },
            {
                "id": "b1-reformkor-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a bizonyosságot a reformkor megítélésében?",
                "options": [
                    "A reformkor kétségkívül a modern Magyarország születésének legdicsőbb korszaka.",
                    "A reformkor kétségkívül volt lenni a legszebb.",
                    "A reformkor bizonyára volna volt a legszebb."
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pesti ____ kávéházban gyülekeztek a márciusi ifjak 1848 tavaszán. (Pilvax)",
                "answer": "Pilvax"
            },
            {
                "id": "b1-reformkor-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemzet felvirágoztatása minden hazafi számára elengedhetetlen ____ volt. (task)",
                "answer": "feladat"
            },
            {
                "id": "b1-reformkor-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Széchenyi és Kossuth vitái megtermékenyítették a magyar politikai gondolkodást.",
                "tiles": ["Széchenyi", "és", "Kossuth", "vitái", "megtermékenyítették", "a", "magyar", "politikai", "gondolkodást."]
            },
            {
                "id": "b1-reformkor-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik intézmény alapításához ajánlotta fel Széchenyi egyévi jövedelmét?",
                "options": [
                    "a Magyar Tudományos Akadémiához",
                    "a bécsi hadiakadémiához",
                    "a szegedi halpiachoz"
                ],
                "correct": 0
            },
            {
                "id": "b1-reformkor-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Kölcsey Ferenc 1823-ban írta meg a nemzet szent imádságát a ____. (National Anthem)",
                "answer": "Himnuszt"
            },
            {
                "id": "b1-reformkor-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen kérdések hangzanak el a leggyakrabban a magyar állampolgársági interjún a reformkorról?",
                "options": [
                    "Kik voltak a reformkor legfontosabb alakjai (Széchenyi, Kossuth), mikor lett a magyar a hivatalos nyelv, és hogyan készítették elő 1848-at?",
                    "Milyen autómárkákat szerettek a reformkori nemesek?",
                    "Hány repülőtere volt Pestnek 1840-ben?"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-reformkor-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Széchenyi István, a legnagyobb magyar", "István Széchenyi, 'the Greatest Hungarian'"),
        "02": ("A Lánchíd és a korszerű modernizáció", "Modernizing a Country"),
        "03": ("Kossuth Lajos és a független politikai sajtó", "Lajos Kossuth's Rise"),
        "04": ("A magyar nyelv diadala és nemzeti jelképei", "Language, Culture & National Feeling"),
        "05": ("A forradalom küszöbén: a Pilvax és a márciusi ifjak", "A Country on the Eve of Revolution")
    }

    story_refs = {
        "01": "stories/world/b1/b1-reformkor-01-szechenyi.json",
        "02": "stories/world/b1/b1-reformkor-02-lanchid.json",
        "03": "stories/world/b1/b1-reformkor-03-kossuth.json",
        "04": "stories/world/b1/b1-reformkor-04-nyelv.json",
        "05": "stories/world/b1/b1-reformkor-05-forradalom.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.reformkor-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Evidential & Modal Particles in Reformist Discourse",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events and figures of {en_t}.",
                        "I can use modal and evidential particles (állítólag, bizonyára) in Hungarian.",
                        "I can understand key concepts tested in the Hungarian naturalization interview.",
                        "I can master eight new vocabulary items related to the Reform Age."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-reformkor-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-reformkor-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-reformkor-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-reformkor-{padded}.ex01",
                        f"b1-reformkor-{padded}.ex01b",
                        f"b1-reformkor-{padded}.ex02",
                        f"b1-reformkor-{padded}.ex03",
                        f"b1-reformkor-{padded}.ex04",
                        f"b1-reformkor-{padded}.ex05",
                        f"b1-reformkor-{padded}.ex06",
                        f"b1-reformkor-{padded}.ex07",
                        f"b1-reformkor-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-reformkor-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.reformkor-consolidation",
        "title": "A reformkor összefoglalása (Unit 15 Consolidation)",
        "level": "B1",
        "grammar": "Synthesis: The Reform Era & The Eve of 1848",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can synthesize the full 1825–1848 Reform Era saga.",
                    "I can confidently answer Hungarian citizenship questions on Széchenyi, Kossuth, and the 1844 language act.",
                    "I can review and apply all 40 unit vocabulary items and evidential structures."
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-reformkor.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-reformkor-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-reformkor-consolidation.ex01",
                    "b1-reformkor-consolidation.ex02",
                    "b1-reformkor-consolidation.ex03",
                    "b1-reformkor-consolidation.ex04",
                    "b1-reformkor-consolidation.ex05",
                    "b1-reformkor-consolidation.ex06",
                    "b1-reformkor-consolidation.ex07",
                    "b1-reformkor-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-reformkor-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 15 (b1-reformkor)!")

if __name__ == "__main__":
    build_unit_15_citizenship()
