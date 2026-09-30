#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 18: The Compromise of 1867 (b1-kiegyezes)."""

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

def build_unit_18_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.kiegyezes.01",
        "lesson": "b1-kiegyezes-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "passzív ellenállás", "translation": "passive resistance (non-violent defiance)", "pos": "noun"},
            {"lemma": "adómegtagadás", "translation": "tax refusal, withholding imperial taxes", "pos": "noun"},
            {"lemma": "Bach-korszak", "translation": "Bach era (1850s imperial absolutism)", "pos": "noun"},
            {"lemma": "megtorlás", "translation": "retaliation, reprisal, retribution", "pos": "noun"},
            {"lemma": "osztrák bürokrácia", "translation": "Austrian bureaucracy", "pos": "noun"},
            {"lemma": "nemzeti dac", "translation": "national defiance, stubborn pride", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kiegyezes-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.kiegyezes.02",
        "lesson": "b1-kiegyezes-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "a haza bölcse", "translation": "'Sage of the Nation' (Deák's epithet)", "pos": "noun"},
            {"lemma": "Deák Ferenc", "translation": "Ferenc Deák", "pos": "noun"},
            {"lemma": "Húsvéti cikk", "translation": "Easter Article of 1865", "pos": "noun"},
            {"lemma": "tárgyalási alap", "translation": "basis for negotiation", "pos": "noun"},
            {"lemma": "Pragmatica Sanctio", "translation": "Pragmatic Sanction of 1723", "pos": "noun"},
            {"lemma": "történelmi kompromisszum", "translation": "historic compromise", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kiegyezes-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.kiegyezes.03",
        "lesson": "b1-kiegyezes-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Ferenc József", "translation": "Emperor-King Franz Joseph I", "pos": "noun"},
            {"lemma": "Erzsébet királyné", "translation": "Queen Elisabeth ('Sisi')", "pos": "noun"},
            {"lemma": "koronázás", "translation": "royal coronation ceremony", "pos": "noun"},
            {"lemma": "Szent Korona", "translation": "Holy Crown of Hungary", "pos": "noun"},
            {"lemma": "koronázási eskü", "translation": "coronation oath to uphold the constitution", "pos": "noun"},
            {"lemma": "Mátyás-templom", "translation": "Matthias Church (Church of Our Lady) in Buda", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kiegyezes-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.kiegyezes.04",
        "lesson": "b1-kiegyezes-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "dualizmus", "translation": "Dualism (Austro-Hungarian dual state structure)", "pos": "noun"},
            {"lemma": "közös ügyek", "translation": "common affairs (foreign policy, defense, finance)", "pos": "noun"},
            {"lemma": "önálló kormány", "translation": "autonomous / independent government", "pos": "noun"},
            {"lemma": "Andrássy Gyula", "translation": "Count Gyula Andrássy (prime minister)", "pos": "noun"},
            {"lemma": "parlamentáris monarchia", "translation": "parliamentary constitutional monarchy", "pos": "noun"},
            {"lemma": "vámunió", "translation": "customs union between Austria and Hungary", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kiegyezes-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.kiegyezes.05",
        "lesson": "b1-kiegyezes-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "gazdasági fellendülés", "translation": "economic boom, rapid upswing", "pos": "noun"},
            {"lemma": "vasútépítés", "translation": "railway construction boom", "pos": "noun"},
            {"lemma": "polgári fejlődés", "translation": "civic / bourgeois modernization", "pos": "noun"},
            {"lemma": "jogfolytonosság", "translation": "legal continuity of Hungarian statehood", "pos": "noun"},
            {"lemma": "stabilitás", "translation": "political and institutional stability", "pos": "noun"},
            {"lemma": "történelmi mérleg", "translation": "historical balance sheet / assessment", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kiegyezes-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.kiegyezes.01.concessive-comp",
        "title": "Concessive Clauses in History: Annak ellenére, hogy a forradalom elbukott...",
        "sections": [
            {
                "type": "text",
                "title": "Explaining Compromise Through Concession",
                "content": "To explain the transition from defeat in 1849 to agreement in 1867: *Annak ellenére, hogy a szabadságharc katonailag elbukott, az áprilisi törvények eszméi nem vesztek el.*"
            },
            {
                "type": "examples",
                "title": "Concessive historical structures",
                "items": [
                    {
                        "spanish": "Annak ellenére, hogy Bécs kemény megtorlást alkalmazott, a magyar nemzet nem tört meg.",
                        "english": "Despite the fact that Vienna applied harsh reprisals, the Hungarian nation did not break."
                    },
                    {
                        "spanish": "Bár a nemesek nem fizettek adót, a passzív ellenállás óriási anyagi kárt okozott Bécsnek.",
                        "english": "Although the nobles did not pay taxes, passive resistance caused immense financial damage to Vienna."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kiegyezes-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.kiegyezes.02.purpose-azert-hogy",
        "title": "Purpose and Negotiation: azért tette közzé, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Political Intentions with azért, hogy",
                "content": "To narrate Deák's diplomatic chess moves: *Deák azért írta a Húsvéti cikket, hogy megnyissa az utat a békés megegyezés előtt.* The clause uses *hogy + subjunctive (-jon/-jen)*."
            },
            {
                "type": "examples",
                "title": "Political intentions in sentences",
                "items": [
                    {
                        "spanish": "Deák azért ragaszkodott a törvényekhez, hogy megvédje a nemzet önállóságát.",
                        "english": "Deák insisted on the laws in order to protect the nation's autonomy."
                    },
                    {
                        "spanish": "A felek azért ültek tárgyalóasztalhoz, hogy véget vessenek a bizonytalanságnak.",
                        "english": "The parties sat down at the negotiating table so that they could put an end to uncertainty."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kiegyezes-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.kiegyezes.03.ceremonial-coronation",
        "title": "Ceremonial Royal Register: királlyá koronázták, esküt tett",
        "sections": [
            {
                "type": "text",
                "title": "The Grammar of Royal Coronations",
                "content": "Coronation acts use the translative suffix *-vá/-vé*: *magyar királlyá koronázták* ('crowned him king of Hungary'). The monarch swore *hogy megtartja a magyar alkotmányt*."
            },
            {
                "type": "examples",
                "title": "Coronation expressions",
                "items": [
                    {
                        "spanish": "1867 júniusában Ferenc Józsefet a Mátyás-templomban magyar királlyá koronázták.",
                        "english": "In June 1867 Franz Joseph was crowned king of Hungary in Matthias Church."
                    },
                    {
                        "spanish": "A király ünnepélyes koronázási esküt tett a nemzet alkotmányára.",
                        "english": "The king took a solemn coronation oath upon the nation's constitution."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kiegyezes-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.kiegyezes.04.dual-structures",
        "title": "Dualistic Contrastive Structures: egyrészt... másrészt...",
        "sections": [
            {
                "type": "text",
                "title": "Explaining the Austro-Hungarian Dual Structure",
                "content": "To explain the division of powers: *A kiegyezés értelmében egyrészt közösek maradtak a hadügyek és a külügyek, másrészt Magyarország teljesen önálló kormányt kapott.*"
            },
            {
                "type": "examples",
                "title": "Explaining dual powers",
                "items": [
                    {
                        "spanish": "Egyrészt a Monarchia erős nagyhatalom maradt, másrészt a belső ügyekben önállóságot élvezett.",
                        "english": "On the one hand the Monarchy remained a strong great power; on the other hand it enjoyed autonomy in internal affairs."
                    },
                    {
                        "spanish": "A közös ügyeket minisztériumok irányították, miközben a törvényhozás Pesten független volt.",
                        "english": "Joint affairs were managed by ministries, while legislation in Pest was independent."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kiegyezes-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.kiegyezes.05.historical-assessment",
        "title": "Evaluating Historical Outcomes: lehetővé tette, hozzájárult ahhoz, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Assessing Historical Impacts at B1",
                "content": "To balance the historical legacy: *A kiegyezés lehetővé tette a gazdasági fellendülést, ugyanakkor fenntartotta a Monarchia belső feszültségeit.*"
            },
            {
                "type": "examples",
                "title": "Assessing historical outcomes",
                "items": [
                    {
                        "spanish": "A béke korszaka hozzájárult ahhoz, hogy Budapest igazi világvárossá fejlődjön.",
                        "english": "The era of peace contributed to Budapest developing into a true world city."
                    },
                    {
                        "spanish": "A történelmi mérleg szerint a kiegyezés a nemzet túlélését és modernizációját biztosította.",
                        "english": "According to the historical assessment, the compromise ensured the nation's survival and modernization."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kiegyezes-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Narrative Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.kiegyezes.01",
        "title": "A csendes dac és a passzív ellenállás",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Following the tragic defeat of 1849, the Austrian minister Alexander Bach installs a suffocating police bureaucracy. But Hungarians invent passive resistance: refusing to speak German, ignoring imperial decrees, and practicing stubborn tax refusal while wearing traditional Hungarian coats.",
        "characters": [
            "Deák Ferenc",
            "Bach-huszárok (osztrák hivatalnokok)",
            "Magyar birtokosok"
        ],
        "location": "Pest, Balaton-felvidék, Kehida",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1850-ben sötét csend borult Magyarországra. A szabadságharc leverése után Alexander Bach bécsi belügyminiszter osztrák hivatalnokok ezreit, a nép által 'Bach-huszároknak' csúfolt csinovnyikokat küldte az országba."
            },
            {
                "type": "narration",
                "text": "A megtorlás kegyetlen volt, de a fegyveres harc helyét egy zseniális új fegyver vette át: a nemzeti dac és a passzív ellenállás."
            },
            {
                "type": "dialogue",
                "speaker": "Deák Ferenc",
                "text": "Ha erőszakkal elveszik a jogainkat, nem fogunk fegyvert, de egyetlen lépést sem teszünk feléjük. Nem engedünk, és nem működünk együtt!"
            },
            {
                "type": "narration",
                "text": "A magyar urak nem vállaltak hivatalt az osztrák közigazgatásban. Amikor a bécsi tisztviselők adót akartak behajtani, a gazdák széttárták a karjukat, mondván: nincs pénzük, az adómegtagadás mindennapos szokássá vált."
            },
            {
                "type": "narration",
                "text": "Az emberek magyaros zsinóros ruhát, bocskait öltöttek, és a kávéházakban némán pipázva tüntettek az elnyomás ellen. Bécs hiába költött milliókat a rendőrségre, az országot nem tudta megtörni."
            },
            {
                "type": "dialogue",
                "speaker": "Magyar birtokosok",
                "text": "Bíró urak, vigyék a bútorainkat, ha akarják! De a lelkünket és a nemzet jogait soha nem fogják birtokolni!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes-01-passzivellenallas.json", story_01)

    story_02 = {
        "id": "story.b1.kiegyezes.02",
        "title": "A Haza Bölcse és a Húsvéti cikk",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Ferenc Deák, residing in the modest Queen of England Hotel in Pest, carves wooden boxes, smokes his pipe, and bides his time. On Easter 1865, he pens the legendary Easter Article in Pesti Napló, offering a brilliant, realistic compromise based on the 1723 Pragmatic Sanction.",
        "characters": [
            "Deák Ferenc",
            "Kemény Zsigmond szerkesztő",
            "Bécsi udvar"
        ],
        "location": "Pest, Angol Királynő Szálló",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Pesten, a Duna-parti Angol Királynő Szálló két egyszerű szobájában élt egy csendes, testes úr: Deák Ferenc, akit a nép méltán hívott úgy, mint a haza bölcse."
            },
            {
                "type": "narration",
                "text": "Deák nem kért pénzt, nem fogadott el rangokat. Szabadidejében fafaragással bíbelődött, órákig pipázott, de elméje olyan éles volt, mint a legfinomabb borotva."
            },
            {
                "type": "dialogue",
                "speaker": "Deák Ferenc",
                "text": "A jogainkból nem engedünk, de a valóságot sem tagadhatjuk le. Magyarország és a Monarchia közös érdekeit békésen kell összehangolni."
            },
            {
                "type": "narration",
                "text": "1865 húsvétján a Pesti Napló hasábjain megjelent Deák névtelen írása, a híres Húsvéti cikk. Ez a szöveg kínálta fel a történelmi kompromisszum alapját a bécsi udvarnak."
            },
            {
                "type": "narration",
                "text": "Deák a Pragmatica Sanctio elvére hivatkozva kijelentette: Magyarország kész közösen kezelni a birodalom biztonságát, ha Bécs maradéktalanul helyreállítja az önálló magyar alkotmányt."
            },
            {
                "type": "dialogue",
                "speaker": "Kemény Zsigmond",
                "text": "Deák úr, ez a cikk megnyitotta a zárt kapukat! Bécsben végre megértették, hogy Magyarország nélkül nem épülhet stabil birodalom!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes-02-deakferenc.json", story_02)

    story_03 = {
        "id": "story.b1.kiegyezes.03",
        "title": "A koronázás fényei és Erzsébet királyné",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On June 8, 1867, Budapest witnesses one of the most dazzling spectacles in European history. In the Matthias Church, Franz Joseph is crowned with Saint Stephen's Crown, while the beloved Queen Elisabeth ('Sisi'), wearing a dress by Charles Worth, seals the reconciliation.",
        "characters": [
            "Ferenc József",
            "Erzsébet királyné (Sisi)",
            "Andrássy Gyula",
            "Simor János érsek"
        ],
        "location": "Buda, Mátyás-templom, Lánchíd",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1867. június 8-án hajnalban a budai Várnegyedben ágyúlövések köszöntötték a felkelő napot. Tizennyolc év kíméletlen harc és elidegenedés után eljött a történelmi megbékélés napja."
            },
            {
                "type": "narration",
                "text": "A zsúfolásig megtelt Mátyás-templomban Liszt Ferenc Koronázási miséje csendült fel. Simor János érsek és a magyar miniszterelnök, gróf Andrássy Gyula a király fejére helyezte a Szent Koronát."
            },
            {
                "type": "dialogue",
                "speaker": "Ferenc József",
                "text": "Esküszöm az élő Istenre, hogy Magyarország törvényeit és ősi szabadságát sértetlenül fenntartom!"
            },
            {
                "type": "narration",
                "text": "Az igazi diadal azonban a gyönyörű Erzsébet királynéé, Sisié volt, aki tiszta szívből szerette a magyarokat, és éveken át harcolt Bécsben a kiegyezésért."
            },
            {
                "type": "narration",
                "text": "Amikor Sisi magyar díszruhában kilépett a templomból, a Lánchíd felől felzúgott az 'Éljen Erzsébet!' kiáltás. A sebek lassan gyógyulni kezdtek."
            },
            {
                "type": "dialogue",
                "speaker": "Andrássy Gyula",
                "text": "Királyné asszonyunk, a magyar nemzet hűsége és szeretete örökre az Ön pajzsa marad."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes-03-koronazas.json", story_03)

    story_04 = {
        "id": "story.b1.kiegyezes.04",
        "title": "A dualizmus világa: Közös ügyek és önállóság",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Austro-Hungarian Monarchy is established as a unique dual-state superpower. Emperor Franz Joseph reigns over both halves, foreign affairs and the army are managed jointly, but in Pest, a sovereign parliament and prime minister govern Hungarian domestic destiny.",
        "characters": [
            "Andrássy Gyula",
            "Deák Ferenc",
            "Kossuth Lajos (emigrációban)"
        ],
        "location": "Pest, Sándor-palota, Bécs",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kiegyezéssel megszületett a dualizmus különleges rendszere: az Osztrák–Magyar Monarchia. Két egyenrangú állam szövetsége jött létre egyetlen közös uralkodó alatt."
            },
            {
                "type": "narration",
                "text": "A birodalmi nagyság érdekében a külügy, a hadügy és az ezekre vonatkozó pénzügy közös maradt. A közös minisztériumok Bécsben működtek, de mindkét félnek beleszólása volt a döntésekbe."
            },
            {
                "type": "dialogue",
                "speaker": "Andrássy Gyula",
                "text": "Önálló kormánnyal rendelkezünk Pesten, saját oktatással, igazságszolgáltatással és belüggyel. Ez a reális maximum, amit elérhettünk."
            },
            {
                "type": "narration",
                "text": "A rendszernek azonban voltak ellenzői is. Az emigrációban élő Kossuth Lajos híres 'Kasszandra-levelében' figyelmeztetett: a Habsburgokhoz való kötődés veszélybe sodorhatja Magyarországot egy jövőbeli háborúban."
            },
            {
                "type": "dialogue",
                "speaker": "Kossuth Lajos",
                "text": "Ne kössétek a magyar nemzet sorsát egy hanyatló birodalomhoz! Az önálló nemzeti lét a jövő egyetlen záloga!"
            },
            {
                "type": "narration",
                "text": "A parlamenti többség mégis Deák és Andrássy útját választotta. A vámunió és a közös piac évtizedekig tartó soha nem látott stabilitást hozott."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes-04-dualizmus.json", story_04)

    story_05 = {
        "id": "story.b1.kiegyezes.05",
        "title": "A gazdasági robbanás és a jogfolytonosság",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "With peace secured, Hungary experiences an unprecedented economic explosion. Capital pours into railways, banks, and factories; Buda and Pest unite into Budapest in 1873. The historical legacy of 1867 preserved the continuity of Hungarian constitutional law.",
        "characters": [
            "Baross Gábor (a vasminiszter)",
            "Budapesti polgárok",
            "Állampolgársági kérdező"
        ],
        "location": "Budapest, Nyugati pályaudvar, Duna-part",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kiegyezés aláírása után a magyar gazdaság úgy robbant be, mint egy addig elzárt gőzmozdony. A politikai stabilitás nyomán hatalmas külföldi tőke áramlott az országba."
            },
            {
                "type": "narration",
                "text": "Pár év alatt több ezer kilométernyi modern vasútvonal hálózta be a Kárpát-medencét. A Duna partján hatalmas gőzmalmok és gyárak épültek, a magyar búza világhírűvé vált."
            },
            {
                "type": "dialogue",
                "speaker": "Baross Gábor",
                "text": "A vasút nem csupán sín és vagon: a vasút a gazdasági vérkeringés és a nemzeti összetartozás legfőbb eszköze!"
            },
            {
                "type": "narration",
                "text": "1873-ban Pest, Buda és Óbuda egyesülésével megszületett a csodálatos világváros, Budapest. A békés fejlődés biztosította a polgári átalakulás győzelmét."
            },
            {
                "type": "dialogue",
                "speaker": "Állampolgársági kérdező",
                "text": "Mit jelent 1867 a nemzet számára? A jogfolytonosság megmentését, a magyar alkotmányosság diadalát és fél évszázadnyi békét."
            },
            {
                "type": "narration",
                "text": "Deák Ferenc bölcs kompromisszuma megmentette a nemzetet a pusztulástól, és megnyitotta a kaput a modern polgári Magyarország aranykora előtt."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes-05-fejlodes.json", story_05)

    # Combined Story for Library
    story_combined = {
        "id": "story.b1.kiegyezes",
        "title": "A kiegyezés és a dualizmus születése",
        "level": "B1",
        "order": 18,
        "type": "world",
        "estimatedMinutes": 9,
        "summary": "From the stubborn passive resistance of the Bach era and Deák's masterly Easter Article, to the glittering coronation of Franz Joseph and Sisi in 1867, and the golden decades of economic growth that transformed Budapest into a world metropolis.",
        "characters": [
            "Deák Ferenc",
            "Ferenc József",
            "Erzsébet királyné (Sisi)",
            "Andrássy Gyula"
        ],
        "location": "Pest, Buda, Bécs, Mátyás-templom",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az 1849-es vereség után a Bach-korszak elnyomása alatt a magyarok passzív ellenállással és dacos kitartással védték nemzeti jogaikat."
            },
            {
                "type": "narration",
                "text": "A haza bölcse, Deák Ferenc 1865-ös Húsvéti cikkével megalapozta a reális, méltányos megegyezést a Pragmatica Sanctio szellemében."
            },
            {
                "type": "narration",
                "text": "1867. június 8-án a Mátyás-templomban magyar királlyá koronázták Ferenc Józsefet, miközben a magyarok rajongva ünnepelték Erzsébet királynét, Sisit."
            },
            {
                "type": "narration",
                "text": "A dualizmus megteremtette az önálló magyar parlamentet és kormányt Andrássy Gyula vezetésével, fenntartva a közös hadügyet és külügyet."
            },
            {
                "type": "narration",
                "text": "A kiegyezés fél évszázados békét, vasútépítési lázat és gazdasági virágzást hozott, megteremtve Budapest modern metropoliszát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kiegyezes.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-kiegyezes-{padded}",
            "exercises": [
                {
                    "id": f"b1-kiegyezes-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [
                        [curr_voc["words"][0]["lemma"], curr_voc["words"][0]["translation"]],
                        [curr_voc["words"][1]["lemma"], curr_voc["words"][1]["translation"]],
                        [curr_voc["words"][2]["lemma"], curr_voc["words"][2]["translation"]],
                        [curr_voc["words"][3]["lemma"], curr_voc["words"][3]["translation"]]
                    ]
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat mutatja be helyesen a kiegyezéshez vezető utat? (Lesson {i})",
                    "options": [
                        "Annak ellenére, hogy a forradalom elbukott, Deák megőrizte az alkotmányos jogokat.",
                        "Annak ellenére mert forradalom elbukni ezért nem lett béke.",
                        "Mivel Deák nem beszélt ezért a király rögtön elfogadta a törvényt."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Deák Ferencet bölcs és békés politikájáért a haza ____ nevezték. (sage / wise man)",
                    "answer": "bölcsének"
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Deák azért írta a Húsvéti cikket, ____ megnyissa az utat a békés tárgyalások előtt. (so that)",
                    "answer": "hogy"
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a dualizmus rendszere az 1867-es kiegyezés után?",
                    "options": [
                        "Két önálló állam (Ausztria és Magyarország) szövetségét egy közös uralkodó alatt.",
                        "Két király egyidejű uralkodását Magyarországon.",
                        "Két különálló pénznem bevezetését minden egyes faluban."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "1867-ben Ferenc Józsefet a Mátyás-templomban magyar királlyá koronáz____. (they crowned him)",
                    "answer": "ták"
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "kiegyezés", "biztosította", "a", "magyar", "nemzet", "törvényes", "önállóságát", "és", "fejlődését."],
                    "solution": ["A", "kiegyezés", "biztosította", "a", "magyar", "nemzet", "törvényes", "önállóságát", "és", "fejlődését."]
                },
                {
                    "id": f"b1-kiegyezes-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mely három ügy volt közös Ausztria és Magyarország között a dualizmusban?",
                    "options": [
                        "A hadügy, a külügy és az ezekre vonatkozó pénzügy.",
                        "Az oktatásügy, a mezőgazdaság és az erdőgazdálkodás.",
                        "A helyi rendőrség, a színházak és a posta."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-kiegyezes-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-kiegyezes-consolidation",
        "exercises": [
            {
                "id": "b1-kiegyezes-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["passzív ellenállás", "passive resistance"],
                    ["a haza bölcse", "Sage of the Nation"],
                    ["Szent Korona", "Holy Crown of Hungary"],
                    ["dualizmus", "Dualism"]
                ]
            },
            {
                "id": "b1-kiegyezes-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás összegzi helyesen az 1867-es kiegyezés történelmi eredményét?",
                "options": [
                    "Helyreállította a magyar alkotmányosságot és fél évszázados gazdasági békét hozott.",
                    "Megszüntette a magyar nyelvet mint hivatalos államnyelvet.",
                    "Azonnali háborúba sodorta az országot az európai nagyhatalmakkal."
                ],
                "correct": 0
            },
            {
                "id": "b1-kiegyezes-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Deák híres 1865-ös írásának neve a ____ cikk volt. (Easter)",
                "answer": "Húsvéti"
            },
            {
                "id": "b1-kiegyezes-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A király esküt tett arra, hogy tiszteletben tartja az ősi ____. (constitution -t)",
                "answer": "alkotmányt"
            },
            {
                "id": "b1-kiegyezes-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Erzsébet", "királyné", "szeretete", "a", "magyarok", "iránt", "megkönnyítette", "a", "békés", "kiegyezést."],
                "solution": ["Erzsébet", "királyné", "szeretete", "a", "magyarok", "iránt", "megkönnyítette", "a", "békés", "kiegyezést."]
            },
            {
                "id": "b1-kiegyezes-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki volt Magyarország miniszterelnöke a kiegyezés idején, 1867-ben?",
                "options": [
                    "Gróf Andrássy Gyula",
                    "Alexander Bach",
                    "Rákóczi Ferenc"
                ],
                "correct": 0
            },
            {
                "id": "b1-kiegyezes-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Habsburgok és a magyar rendek közös uralkodását rögzítő 1723-as törvény neve: Pragmatica ____. (Sanctio)",
                "answer": "Sanctio"
            },
            {
                "id": "b1-kiegyezes-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit hozott a kiegyezés Budapest számára a 19. század végén?",
                "options": [
                    "Pest, Buda és Óbuda egyesülését, rohamos vasútépítést és modern világvárossá válást.",
                    "A város falainak lerombolását és elnéptelenedését.",
                    "A dunai hajózás teljes betiltását."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kiegyezes-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A bukás után új út: a passzív ellenállás", "After Defeat, a New Path"),
        "02": ("Deák Ferenc és a Húsvéti cikk", "Ferenc Deák's Compromise"),
        "03": ("Ferenc József magyar király lesz", "Franz Joseph, King of Hungary"),
        "04": ("A dualizmus: közös ügyek és függetlenség", "A Dual Monarchy"),
        "05": ("Mit hozott a kiegyezés Magyarországnak?", "What the Compromise Changed")
    }

    story_refs = {
        "01": "stories/world/b1/b1-kiegyezes-01-passzivellenallas.json",
        "02": "stories/world/b1/b1-kiegyezes-02-deakferenc.json",
        "03": "stories/world/b1/b1-kiegyezes-03-koronazas.json",
        "04": "stories/world/b1/b1-kiegyezes-04-dualizmus.json",
        "05": "stories/world/b1/b1-kiegyezes-05-fejlodes.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.kiegyezes-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Concessive Connectors, Purpose Clauses & Dual Constitutional Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events, figures and consequences of {en_t}.",
                        "I can use concessive connectors (annak ellenére, hogy) and ceremonial forms in Hungarian.",
                        "I can answer essential citizenship interview questions regarding the 1867 Compromise.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-kiegyezes-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-kiegyezes-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-kiegyezes-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-kiegyezes-{padded}.ex01",
                        f"b1-kiegyezes-{padded}.ex02",
                        f"b1-kiegyezes-{padded}.ex03",
                        f"b1-kiegyezes-{padded}.ex04",
                        f"b1-kiegyezes-{padded}.ex05",
                        f"b1-kiegyezes-{padded}.ex06",
                        f"b1-kiegyezes-{padded}.ex07",
                        f"b1-kiegyezes-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-kiegyezes-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.kiegyezes-consolidation",
        "title": "Összefoglalás: A kiegyezés (1867) (The Compromise of 1867 Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of the 1867 Compromise, Dualism & Constitutional Heritage",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-kiegyezes.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-kiegyezes-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-kiegyezes-consolidation.ex01",
                    "b1-kiegyezes-consolidation.ex02",
                    "b1-kiegyezes-consolidation.ex03",
                    "b1-kiegyezes-consolidation.ex04",
                    "b1-kiegyezes-consolidation.ex05",
                    "b1-kiegyezes-consolidation.ex06",
                    "b1-kiegyezes-consolidation.ex07",
                    "b1-kiegyezes-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-kiegyezes-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 18 (b1-kiegyezes)!")

if __name__ == "__main__":
    build_unit_18_citizenship()
