#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 26: The Kádár Era & Goulash Communism (b1-kadarkorszak)."""

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

def build_unit_26_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.kadarkorszak.01",
        "lesson": "b1-kadarkorszak-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kádári kiegyezés", "translation": "Kádár's compromise (tacit social contract of private peace for political silence)", "pos": "noun"},
            {"lemma": "pufajkások", "translation": "quilted jacket militia (paramilitary units crushing post-1956 resistance)", "pos": "noun"},
            {"lemma": "amnesztiarendelet", "translation": "general amnesty decree of 1963 releasing political prisoners", "pos": "noun"},
            {"lemma": "konszolidáció", "translation": "political consolidation and normalization under Kádár", "pos": "noun"},
            {"lemma": "aki nincs ellenünk, az velünk van", "translation": "'whoever is not against us is with us' (famous Kádár slogan of 1961)", "pos": "expression"},
            {"lemma": "megtorló perek", "translation": "retribution show trials following the 1956 revolution", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kadarkorszak-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.kadarkorszak.02",
        "lesson": "b1-kadarkorszak-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Új Gazdasági Mechanizmus", "translation": "New Economic Mechanism (1968 market-oriented economic reform)", "pos": "noun"},
            {"lemma": "háztáji gazdaság", "translation": "household plot farming (private agricultural plots permitted alongside co-ops)", "pos": "noun"},
            {"lemma": "maszek", "translation": "private entrepreneur / private craftsman ('magánszektor')", "pos": "noun"},
            {"lemma": "vállalati önállóság", "translation": "company autonomy / decentralization in socialist planning", "pos": "noun"},
            {"lemma": "második gazdaság", "translation": "second economy (legal and semi-legal private work and farming)", "pos": "noun"},
            {"lemma": "reformközgazdászok", "translation": "reform economists (Nyers Rezső and colleagues steering modernization)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kadarkorszak-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.kadarkorszak.03",
        "lesson": "b1-kadarkorszak-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "gulyáskommunizmus", "translation": "'goulash communism' (Hungarian model of relative consumer abundance)", "pos": "noun"},
            {"lemma": "a legvidámabb barakk", "translation": "'the happiest barrack' (Western nickname for socialist Hungary)", "pos": "expression"},
            {"lemma": "frizsiderszocializmus", "translation": "'refrigerator socialism' (focus on consumer durables and living standards)", "pos": "noun"},
            {"lemma": "Trabant gépkocsi", "translation": "Trabant car (iconic East German two-stroke vehicle on long waiting lists)", "pos": "noun"},
            {"lemma": "balatoni nyaralás", "translation": "Lake Balaton summer holiday (central hub of socialist domestic tourism)", "pos": "noun"},
            {"lemma": "hétvégi telek", "translation": "weekend hobby garden / plot (beloved private escape of urban families)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kadarkorszak-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.kadarkorszak.04",
        "lesson": "b1-kadarkorszak-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "három T kategória", "translation": "'Three Ts' cultural policy: támogatott, tűrt, tiltott (supported, tolerated, banned)", "pos": "noun"},
            {"lemma": "Aczél György", "translation": "György Aczél (supreme cultural arbiter and ideological gatekeeper)", "pos": "noun"},
            {"lemma": "öncenzúra", "translation": "self-censorship practiced by writers and filmmakers to avoid bans", "pos": "noun"},
            {"lemma": "szamizdat irodalom", "translation": "samizdat literature (underground dissident publications)", "pos": "noun"},
            {"lemma": "Beszélő folyóirat", "translation": "Beszélő (famed illegal underground democratic opposition journal)", "pos": "noun"},
            {"lemma": "ellenzéki értelmiség", "translation": "dissident intellectual opposition questioning party monopoly", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kadarkorszak-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.kadarkorszak.05",
        "lesson": "b1-kadarkorszak-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "államadósság", "translation": "sovereign national debt accumulated from Western lenders", "pos": "noun"},
            {"lemma": "hitelfelvétel", "translation": "borrowing foreign currency loans to sustain consumer living standards", "pos": "noun"},
            {"lemma": "IMF-csatlakozás", "translation": "joining the International Monetary Fund (1982 economic lifeline)", "pos": "noun"},
            {"lemma": "életszínvonal stagnálása", "translation": "stagnation and subsequent decline of living standards in the 1980s", "pos": "noun"},
            {"lemma": "gazdasági kifulladás", "translation": "economic exhaustion and systemic bankruptcy of state socialism", "pos": "noun"},
            {"lemma": "Kádár János leváltása", "translation": "ouster of János Kádár at the May 1988 party conference", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-kadarkorszak-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.kadarkorszak.01.compromise-and-pardon",
        "title": "Tacit Compromises and Reversals: aki nincs ellenünk...",
        "sections": [
            {
                "type": "text",
                "title": "The Negative Conditional Inversion",
                "content": "Kádár turned Rákosi's slogan (*'Aki nincs velünk, az ellenünk van'*) upside down: *'Aki nincs ellenünk, az velünk van'* ('Whoever is not against us is with us'). In Hungarian syntax, relative pronoun clauses with negative existential predicates (*nincs ellenünk*) allow pragmatism over total ideological adherence."
            },
            {
                "type": "examples",
                "title": "Examples in historical discourse",
                "items": [
                    {
                        "spanish": "Aki nem lázad nyíltan a hatalom ellen, azt a rendszer békén hagyja a mindennapi életben.",
                        "english": "Whoever does not openly rebel against power, the regime leaves them alone in daily life."
                    },
                    {
                        "spanish": "Az 1963-as amnesztiarendelet következtében a politikai foglyok többsége kiszabadult a börtönökből.",
                        "english": "As a consequence of the 1963 amnesty decree, the majority of political prisoners were released from prisons."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kadarkorszak-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.kadarkorszak.02.economic-reforms",
        "title": "Permissive Modality in Socialist Economics: -hat/-het and engedélyez",
        "sections": [
            {
                "type": "text",
                "title": "Permissive Verb Forms and Dual Spheres",
                "content": "To describe the regulated private sphere (*második gazdaság*, *maszek*), Hungarian utilizes potential suffix forms (*-hat/-het*) and verbs of institutional permission (*engedélyez, biztosít, lehetővé tesz*)."
            },
            {
                "type": "examples",
                "title": "Examples in economic history",
                "items": [
                    {
                        "spanish": "A termelőszövetkezeti tagok háztáji földjeiken maguknak termelhettek zöldséget és húst.",
                        "english": "Cooperative members could produce vegetables and meat for themselves on their household plots."
                    },
                    {
                        "spanish": "A reformok lehetővé tették, hogy a vállalatok önállóbb gazdasági döntéseket hozzanak.",
                        "english": "The reforms made it possible for enterprises to make more independent economic decisions."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kadarkorszak-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.kadarkorszak.03.living-standards",
        "title": "Comparative Registers of Welfare: viszonylagos bőség, legvidámabb",
        "sections": [
            {
                "type": "text",
                "title": "Superlatives and Modifiers of Relative Comfort",
                "content": "The description of 'goulash communism' hinges on comparative structures: *a legvidámabb barakk* (superlative *leg-...-abb*), *viszonylag magasabb életszínvonal*, and adverbs expressing contrast with the rest of the Eastern Bloc (*míg máshol hiánycikk volt, addig Magyarországon kapható volt*)."
            },
            {
                "type": "examples",
                "title": "Everyday welfare examples",
                "items": [
                    {
                        "spanish": "Magyarország a keleti blokk legvidámabb barakkjává vált a viszonylagos árubőség miatt.",
                        "english": "Hungary became the happiest barrack of the Eastern Bloc due to the relative abundance of goods."
                    },
                    {
                        "spanish": "A családok hétvégi telket és Trabantot vásárolhattak az összegyűjtött forintokból.",
                        "english": "Families could purchase a weekend plot and a Trabant from their accumulated forints."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kadarkorszak-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.kadarkorszak.04.three-ts-censorship",
        "title": "Tripartite Classification: a három T (támogatott, tűrt, tiltott)",
        "sections": [
            {
                "type": "text",
                "title": "Passive Participial Adjectives as Categories",
                "content": "Aczél's cultural hegemony functioned through three past participles functioning as substantive categories: *támogatott* (supported), *tűrt* (tolerated), and *tiltott* (prohibited/banned). Expressing boundaries requires precise verbal aspect (*cenzúráz, betilt, engedélyez, szemet huny*)."
            },
            {
                "type": "examples",
                "title": "Cultural censorship examples",
                "items": [
                    {
                        "spanish": "A hatalom a kritikus hangú műveket gyakran nem betiltotta, hanem csupán a tűrt kategóriába sorolta.",
                        "english": "The authorities often did not ban critical works outright, but merely classified them in the tolerated category."
                    },
                    {
                        "spanish": "A szamizdat kiadványokat illegálisan másolták és terjesztették a rendőrség szeme elől elrejtve.",
                        "english": "Samizdat publications were illegally copied and distributed hidden from the eyes of the police."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kadarkorszak-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.kadarkorszak.05.debt-and-decline",
        "title": "Causality and Inevitability: hitelfelvétel következtében, vezetett vmihez",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Economic Decline and Systemic Exhaustion",
                "content": "Explaining macro-historical causes relies on postpositions of cause (*következtében, révén, miatt*) and resultative verbs with allative case (*-hoz/-hez/-höz vezetett, eredményezett*)."
            },
            {
                "type": "examples",
                "title": "Decline examples",
                "items": [
                    {
                        "spanish": "A fenntarthatatlan életszínvonal finanszírozása hatalmas nyugati államadóssághoz vezetett.",
                        "english": "Financing unsustainable living standards led to massive Western sovereign debt."
                    },
                    {
                        "spanish": "A gazdaság kifulladása miatt a pártvezetés kénytelen volt leváltani a megöregedett Kádár Jánost.",
                        "english": "Due to the exhaustion of the economy, the party leadership was forced to replace the aged János Kádár."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-kadarkorszak-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Story Files (5 regular lesson stories + 1 combined omnibus story)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.kadarkorszak.01",
        "lesson": 1,
        "order": 1,
        "title": "A kádári kiegyezés: a megtorlástól a konszolidációig",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "After the brutal bloodbath and executions of 1956-1961, János Kádár realized terror alone could not stabilize his rule. In 1961 he reversed Rákosi's totalitarian formula, declaring 'whoever is not against us is with us'. With the 1963 general amnesty, a quiet, cynical compromise was forged: political acquiescence in exchange for private peace and material security.",
        "characters": [
            "Kádár János pártfőtitkár",
            "Amnesztiával szabadult forradalmár mérnök",
            "Budapesti tanárnő"
        ],
        "location": "Budapest, a Parlament és a Margit körúti börtön kapuja",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A forradalom utáni véres megtorlás évei után, 1961-ben Kádár János új jelszót hirdetett a pártkongresszuson: 'Aki nincs ellenünk, az velünk van.' Rákosi rettegésre épülő rendszerét a hallgatólagos kompromisszum váltotta fel."
            },
            {
                "type": "dialogue",
                "speaker": "Kádár János pártfőtitkár",
                "text": "Nem követeljük meg mindenkitől, hogy lelkes kommunista legyen. Csak annyit kérünk, hogy tegye a dolgát a munkahelyén, és ne kérdőjelezze meg a párt vezető szerepét és a szovjet szövetséget!"
            },
            {
                "type": "narration",
                "text": "1963-ban Kádár amnesztiarendeletet hozott: a politikai foglyok ezrei térhettek haza a börtönökből a családjukhoz. Megkezdődött a konszolidáció korszaka."
            },
            {
                "type": "dialogue",
                "speaker": "Amnesztiával szabadult mérnök",
                "text": "Hét év börtön után végre átölelhetem a gyermekeimet. Nem beszélhetek 1956-ról, nem politizálhatok, de mérnökként dolgozhatok. Ez egy keserű, mégis élhető béke."
            },
            {
                "type": "narration",
                "text": "A magyar társadalom lassan elfogadta a láthatatlan alkut: lemondott a politikai szabadságról a mindennapi nyugalom és a fokozatosan javuló életszínvonal fejében."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak-01-megtorlas.json", story_01)

    story_02 = {
        "id": "story.b1.kadarkorszak.02",
        "lesson": 2,
        "order": 2,
        "title": "Az Új Gazdasági Mechanizmus (1968)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On January 1, 1968, Hungary launched the New Economic Mechanism under reform economist Rezső Nyers. Departing from rigid Soviet central planning, it introduced enterprise autonomy, profit incentives, and legal room for household farming ('háztáji'). The second economy allowed millions to augment their income through diligent private work.",
        "characters": [
            "Nyers Rezső reformközgazdász",
            "Falusi tsz-tag gazdálkodó",
            "Vállalati igazgató Győrben"
        ],
        "location": "Budapest, Tervhivatal és egy alföldi termelőszövetkezet",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1968. január 1-jén életbe lépett az Új Gazdasági Mechanizmus. A szocialista táborban egyedülálló módon Magyarországon teret engedtek a piaci mechanizmusoknak és a vállalati önállóságnak."
            },
            {
                "type": "dialogue",
                "speaker": "Nyers Rezső reformközgazdász",
                "text": "A tervutasításos rendszer elavult. Nem dönthet a minisztérium minden egyes cipő áráról! Érdekeltté kell tennünk az embereket a profitban és a jó minőségű termelésben!"
            },
            {
                "type": "narration",
                "text": "A reform legéletképesebb eleme a háztáji gazdaságok támogatása volt. A falusi emberek a közös munka után saját telkükön neveltek sertést, szedtek paprikát és szőlőt, amit szabadon értékesíthettek a piacon."
            },
            {
                "type": "dialogue",
                "speaker": "Falusi gazdálkodó",
                "text": "Nappal a tsz földjén vezetem a traktort, este pedig a saját háztájimban dolgozom a családdal. Kemény munka, de a jövedelemből házat építünk a fiamnak!"
            },
            {
                "type": "narration",
                "text": "Megszületett a 'második gazdaság' és a 'maszek' világa: a kisiparosok és a szorgalmas családok munkája tette a magyar boltok polcait telivé a szomszédos országok üres boltjaival szemben."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak-02-mechanizmus.json", story_02)

    story_03 = {
        "id": "story.b1.kadarkorszak.03",
        "lesson": 3,
        "order": 3,
        "title": "A legvidámabb barakk és a gulyáskommunizmus",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In the 1970s, Western observers dubbed Hungary 'the happiest barrack' of the Soviet bloc. 'Goulash communism' (or 'refrigerator socialism') promised meat on the table, affordable consumer goods, small weekend garden plots, and summer holidays at Lake Balaton. While people waited years for a Trabant car, life seemed remarkably comfortable compared to Romania or the USSR.",
        "characters": [
            "Középkorú budapesti tisztviselő",
            "Felesége, gépírónő",
            "Keletnémet turista a Balaton partján"
        ],
        "location": "Siófok és a budapesti Skála áruház",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az 1970-es évekre Magyarország a keleti blokk irigyelt szigetévé vált. A nyugati újságírók 'gulyáskommunizmusnak' nevezték a jóléti modellt, amely bőséges élelmiszerellátást és olcsó közszolgáltatásokat biztosított."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti tisztviselő",
                "text": "Öt évig vártunk a fehér Trabantra a Merkúrnál, de tegnap végre átvettük a telepen! Holnap lemegyünk a hétvégi telekre a Balatonra, viszünk húst a Lehel téri piacról és csinálunk egy jó bográcsgulyást!"
            },
            {
                "type": "narration",
                "text": "A Balaton a kelet- és nyugatnémet családok találkozóhelyévé vált, ahol a vasfüggöny által elválasztott rokonok minden nyáron újra megölelhették egymást egy lángos mellett Siófokon."
            },
            {
                "type": "dialogue",
                "speaker": "Keletnémet turista",
                "text": "Budapest maga a csoda! A Skála áruházban van nyugati farmer, narancs, hanglemez és szalámi. Nálunk Lipcsében ilyenről álmodni sem lehet!"
            },
            {
                "type": "narration",
                "text": "Ez volt a 'frizsiderszocializmus': a televízió, az automata mosógép és a telek békéje elfedte a határok zártságát és a szabadság hiányát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak-03-gulyas.json", story_03)

    story_04 = {
        "id": "story.b1.kadarkorszak.04",
        "lesson": 4,
        "order": 4,
        "title": "A három T világa: kultúrpolitika és szamizdat",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Kádár's cultural supremo, György Aczél, managed artistic life through the legendary 'Three Ts': támogatott (supported), tűrt (tolerated), and tiltott (prohibited). While regime-friendly art received funding and critical literature was gingerly tolerated, true dissidents were banned. By the late 1970s, underground intellectuals established samizdat networks and published the illegal journal Beszélő.",
        "characters": [
            "Aczél György kultúrpolitikus",
            "Fiatal ellenzéki író",
            "Szamizdatot nyomtató egyetemi hallgató"
        ],
        "location": "Budapest, a Szépirodalmi Könyvkiadó és egy zuglói pince",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kádári korszak szellemi életét Aczél György rafinált kultúrpolitikája irányította: a 'három T' rendszere. Nem tiltottak be mindent mereven, mint Rákosi idején, hanem ügyesen sakkoztak az alkotókkal."
            },
            {
                "type": "dialogue",
                "speaker": "Aczél György",
                "text": "A támogatott művészeknek díjakat és lakást adunk. A kényelmetlen kérdéseket felvető írókat tűrjük, de szűk példányszámban. Ám aki a párt ellen szervezkedik, az tiltott, és nem kaphat nyilvánosságot!"
            },
            {
                "type": "narration",
                "text": "Sokan az öncenzúra finom művészetét választották: a sorok között írtak, allegóriákba rejtve a bírálatot. Ám a hetvenes évek végén megszületett a bátor demokratikus ellenzék."
            },
            {
                "type": "dialogue",
                "speaker": "Egyetemista a zuglói pincében",
                "text": "Éjszaka kézi sokszorosítógépen nyomjuk a 'Beszélő' legújabb számát. Az emberi jogokról és a határon túli magyarságról írunk. Ha a rendőrség ránk tör, börtön vár ránk, de az igazságot nem lehet örökre elhallgattatni!"
            },
            {
                "type": "narration",
                "text": "A szamizdat füzetek kézről kézre jártak a budapesti lakásokban, fokozatosan megtörve a párt információ-monopóliumát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak-04-haromt.json", story_04)

    story_05 = {
        "id": "story.b1.kadarkorszak.05",
        "lesson": 5,
        "order": 5,
        "title": "Adósságcsapda és a rendszer kifulladása (1980-as évek)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The illusion of socialist prosperity was financed not by superior productivity, but by skyrocketing Western loans. The global oil crises and structural inefficiencies plunged Hungary into an inescapable debt spiral. In 1982 Hungary joined the IMF to avert immediate default. By 1988, as living standards fell, an exhausted János Kádár was removed, paving the path toward systemic collapse.",
        "characters": [
            "Magyar Nemzeti Bank elnöke",
            "Nyugati bankár Zürichben",
            "Kádár János az 1988-as pártértekezleten"
        ],
        "location": "Budapest, Magyar Nemzeti Bank és az Építők Rózsa Ferenc Művelődési Háza",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az 1980-as évekre világossá vált a fájdalmas valóság: a 'gulyáskommunizmus' jólétét nem a gazdaság teljesítménye, hanem a hatalmas összegű nyugati dollárhitelek finanszírozták."
            },
            {
                "type": "dialogue",
                "speaker": "Magyar Nemzeti Bank elnöke",
                "text": "Az államadósságunk meghaladta a húszmilliárd dollárt. Ha nem kapunk sürgősen újabb hiteleket, fizetésképtelenné válunk! 1982-ben be kell lépnünk a Nemzetközi Valutaalapba (IMF)!"
            },
            {
                "type": "narration",
                "text": "A hitelek kamatainak törlesztése felemésztette a költségvetést. Az árak emelkedni kezdtek, az életszínvonal érezhetően romlott, és a boltokban megjelent az infláció."
            },
            {
                "type": "dialogue",
                "speaker": "Kádár János (1988 májusában)",
                "text": "Évtizedeken át szolgáltam ezt a népet... De érzem, a világ megváltozott körülöttünk. A szocializmus új válaszokat követel, amiket én már nem tudok megadni."
            },
            {
                "type": "narration",
                "text": "1988 májusában a párt országos értekezlete leváltotta a megfáradt Kádár Jánost a főtitkári posztról. A kádárizmus kifulladt, és feltartóztathatatlanul megkezdődött a kommunista rendszer felbomlása."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak-05-eladosodas.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.kadarkorszak.combined",
        "title": "A Kádár-korszak története: a gulyáskommunizmustól a válságig (1956–1988)",
        "level": "B1",
        "order": 26,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "A panoramic historical chronicle of the Kádár era spanning 1956 to 1988. From the brutal post-1956 retributions to the 1963 amnesty and the pragmatism of 'whoever is not against us is with us'; the economic experiment of the 1968 New Economic Mechanism and second economy; the consumer illusion of 'goulash communism' and 'the happiest barrack'; cultural governance through the 'Three Ts' and the rise of samizdat dissidents; ending with the debt crisis of the 1980s that brought the socialist model to systemic exhaustion.",
        "characters": [
            "Kádár János, az MSZMP főtitkára",
            "Nyers Rezső, gazdasági reformer",
            "Aczél György, kultúrpolitikai vezető",
            "Demokratikus ellenzéki értelmiségi"
        ],
        "location": "Budapest, a Parlament, a Balaton és az Építők Művelődési Háza",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az 1956-os forradalom leverése után Kádár János a szovjet tankok árnyékában vette át az ország vezetését. Miután a kegyetlen megtorlás megtörte az ellenállást, Kádár belátta: állandó rettegésben nem lehet kormányozni. 1961-ben meghirdette a történelmi fordulatot jelentő elvet: 'Aki nincs ellenünk, az velünk van.'"
            },
            {
                "type": "narration",
                "text": "Az 1963-as általános amnesztiarendelet után a rendszer konszolidálódott. 1968-ban életbe lépett az Új Gazdasági Mechanizmus: decentralizálták a vállalatokat, és teret engedtek a háztáji gazdaságoknak. A szorgalmas magyar családok a 'második gazdaságban' megtermelt jövedelemből saját otthont és javakat építhettek."
            },
            {
                "type": "narration",
                "text": "A hetvenes években Magyarország 'a legvidámabb barakk' lett a vasfüggöny mögött. A 'gulyáskommunizmus' tele boltokat, balatoni hétvégi telket és Trabant autókat jelentett. A szellemi életet Aczél György a 'támogatott, tűrt, tiltott' kategóriákkal tartotta kordában, míg a független gondolatokat szamizdat füzetekben másolták."
            },
            {
                "type": "narration",
                "text": "Ám a kényelmes jólét illúzióját a felhalmozódó nyugati dollárhitelek tartották fenn. Az 1980-as évekre az államadósság fenntarthatatlanná vált, az életszínvonal hanyatlani kezdett. 1988 májusában a párt leváltotta a megöregedett Kádárt: a békés átmenet és a rendszerváltoztatás kapuja kinyílt."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-kadarkorszak.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-kadarkorszak-01",
        "exercises": [
            {
                "id": "b1-kadarkorszak-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelentett Kádár János híres mondása: 'Aki nincs ellenünk, az velünk van'?",
                "options": [
                    "A hatalom békén hagyja azokat az embereket a magánéletben, akik nem lázadnak aktívan a párturalom ellen.",
                    "Mindenkinek kötelező belépnie a kommunista pártba.",
                    "Minden ellenvéleményt azonnali kivégzéssel fognak büntetni."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az 1963-as amnesztiarendelet következtében a politikai foglyok többsége kiszabadul_____ a börtönből. (was released - hatott)",
                "answer": "hatott"
            },
            {
                "id": "b1-kadarkorszak-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kádári", "konszolidáció", "alapja", "a", "társadalmi", "béke", "volt."],
                "solution": ["A", "kádári", "konszolidáció", "alapja", "a", "társadalmi", "béke", "volt."]
            },
            {
                "id": "b1-kadarkorszak-01.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik évben adta ki Kádár kormánya a politikai foglyok nagy részét érintő általános amnesztiát?",
                "options": [
                    "1963-ban.",
                    "1956-ban.",
                    "1989-ben."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A forradalom leverését követő véres megtorlást a fegyveres pufajkás_____ segítségével hajtották végre. (plural - ok)",
                "answer": "ok"
            },
            {
                "id": "b1-kadarkorszak-01.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miben különbözött Kádár konszolidációja Rákosi 1950-es évekbeli totális terrorjától?",
                "options": [
                    "Nem követelt állandó ideológiai fanatizmust, megelégedett a lakosság passzív engedelmességével.",
                    "Visszaállította a valódi többpártrendszert és a szabad választásokat.",
                    "Kivezette a szovjet csapatokat az ország területéről."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Aki nem vett részt politikai tüntetésen, az biztonságban él_____ a mindennapokban. (could live - hetett)",
                "answer": "hetett"
            },
            {
                "id": "b1-kadarkorszak-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kádári", "kiegyezés", "megteremtette", "a", "viszonylagos", "nyugalmat."],
                "solution": ["A", "kádári", "kiegyezés", "megteremtette", "a", "viszonylagos", "nyugalmat."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-kadarkorszak-02",
        "exercises": [
            {
                "id": "b1-kadarkorszak-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi volt az 1968-ban bevezetett Új Gazdasági Mechanizmus fő célja?",
                "options": [
                    "A merev tervutasításos rendszer lazítása, a vállalati önállóság és a piaci elemek bevonása.",
                    "A pénzforgalom teljes megszüntetése és a jegyrendszer bevezetése.",
                    "Minden magántulajdon azonnali államosítása."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A reformok lehetővé tet_____ a tsz-tagok számára a háztáji gazdálkodást. (made it possible - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-kadarkorszak-02.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "második", "gazdaság", "jelentős", "többletjövedelmet", "biztosított", "a", "családoknak."],
                "solution": ["A", "második", "gazdaság", "jelentős", "többletjövedelmet", "biztosított", "a", "családoknak."]
            },
            {
                "id": "b1-kadarkorszak-02.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Kik voltak a 'maszekok' a szocialista korszakban?",
                "options": [
                    "A magánszektorban dolgozó kisiparosok, kereskedők és szolgáltatók.",
                    "A külföldi kémelhárítás tisztjei.",
                    "A szovjet pártkongresszus küldöttei."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A reformközgazdászok Nyers Rezső vezetésével dolgoz_____ ki az új gazdasági irányelveket. (elaborated - ták)",
                "answer": "ták"
            },
            {
                "id": "b1-kadarkorszak-02.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért bizonyult sikeresnek a háztáji gazdaság a falvakban?",
                "options": [
                    "Mert a parasztság saját érdekeltségből rengeteget dolgozott rajta, és bőséges árut vitt a városi piacokra.",
                    "Mert az állam ingyen osztott ki traktort minden falusi lakosnak.",
                    "Mert a szovjet hadsereg vásárolta fel az összes terményt."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A gyárak önállóan dönthet_____ bizonyos termékek előállításáról és áráról. (could decide - tek)",
                "answer": "tek"
            },
            {
                "id": "b1-kadarkorszak-02.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "háztáji", "gazdaságok", "megtöltötték", "a", "magyar", "boltok", "polcait."],
                "solution": ["A", "háztáji", "gazdaságok", "megtöltötték", "a", "magyar", "boltok", "polcait."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-kadarkorszak-03",
        "exercises": [
            {
                "id": "b1-kadarkorszak-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miért hívták a nyugati megfigyelők Magyarországot 'a legvidámabb barakknak'?",
                "options": [
                    "Mert a többi szocialista országhoz képest itt szabadabb volt a légkör és sokkal jobb az életszínvonal.",
                    "Mert itt volt a legtöbb cirkuszi szórakozóhely Európában.",
                    "Mert kötelező volt vidám dalokat énekelni a gyárakban."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Magyarország a keleti blokk legvidámabb barakkjává vál_____. (became - t)",
                "answer": "t"
            },
            {
                "id": "b1-kadarkorszak-03.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "gulyáskommunizmus", "alapja", "a", "biztos", "élelmiszerellátás", "volt."],
                "solution": ["A", "gulyáskommunizmus", "alapja", "a", "biztos", "élelmiszerellátás", "volt."]
            },
            {
                "id": "b1-kadarkorszak-03.ex04",
                "type": "multiple-choice",
                "category": "culture",
                "question": "Melyik jármű vált a kádári korszak jellegzetes családi autójává, amire éveket kellett várni?",
                "options": [
                    "A kétütemű Trabant (és Wartburg).",
                    "A luxuskategóriás Mercedes.",
                    "A londoni emeletes busz."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Nyáron a családok tízezrei utaztak a Balaton partjára nyaral_____. (to vacation - ni)",
                "answer": "ni"
            },
            {
                "id": "b1-kadarkorszak-03.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelentett a 'frizsiderszocializmus' kifejezés a mindennapi életben?",
                "options": [
                    "A fogyasztási javak, a hűtőszekrény, a televízió és a hétvégi telek megszerzésére összpontosító életformát.",
                    "A sarki hidegben végzett kötelező bányamunkát.",
                    "A lakások központi fűtésének lekapcsolását télen."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A budapesti boltokban viszonylag könnyebben lehetett déligyümölcsöt vásárol_____, mint Bukarestben. (to buy - ni)",
                "answer": "ni"
            },
            {
                "id": "b1-kadarkorszak-03.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "balatoni", "nyaralás", "minden", "család", "számára", "elérhető", "volt."],
                "solution": ["A", "balatoni", "nyaralás", "minden", "család", "számára", "elérhető", "volt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-kadarkorszak-04",
        "exercises": [
            {
                "id": "b1-kadarkorszak-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelentett az Aczél György nevéhez fűződő 'három T' kultúrpolitikai elve?",
                "options": [
                    "Támogatott, tűrt és tiltott kategóriákat a művészetben és az irodalomban.",
                    "Tanulni, tanítani, termelni.",
                    "Tudomány, technika, társadalom."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A hatalom a veszélyesnek ítélt könyveket azonnal be_____tiltotta. (prefix - be)",
                "answer": "be"
            },
            {
                "id": "b1-kadarkorszak-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szamizdat", "irodalmat", "illegális", "nyomdákban", "másolták", "és", "terjesztették."],
                "solution": ["A", "szamizdat", "irodalmat", "illegális", "nyomdákban", "másolták", "és", "terjesztették."]
            },
            {
                "id": "b1-kadarkorszak-04.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Mi volt a 'Beszélő' a kádári korszak utolsó évtizedében?",
                "options": [
                    "A demokratikus ellenzék legfontosabb illegális szamizdat folyóirata.",
                    "Egy televíziós humorműsor a Magyar Televízióban.",
                    "A kommunista párt hivatalos napilapja."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A cenzúrát elkerülendő sok író az öncenzú_____ eszközéhez nyúlt alkotás közben. (stem suffix - rá)",
                "answer": "rá"
            },
            {
                "id": "b1-kadarkorszak-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan jutott el a cenzúrázatlan hír és szabad gondolat a magyar értelmiséghez?",
                "options": [
                    "Szamizdat kiadványokon és a Szabad Európa Rádió adásain keresztül.",
                    "A párt által kiadott Népszabadság címoldaláról.",
                    "A moszkvai Pravda napilapból."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A művészek gyakran a sorok között fogalmazták meg bírálat_____ a rendszerről. (their critique - ukat)",
                "answer": "ukat"
            },
            {
                "id": "b1-kadarkorszak-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "ellenzéki", "értelmiség", "nyíltan", "követelte", "az", "alapvető", "emberi", "jogokat."],
                "solution": ["Az", "ellenzéki", "értelmiség", "nyíltan", "követelte", "az", "alapvető", "emberi", "jogokat."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-kadarkorszak-05",
        "exercises": [
            {
                "id": "b1-kadarkorszak-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miért adósodott el katasztrofálisan Magyarország a kádári korszak végére?",
                "options": [
                    "Mert a vezetés hatalmas nyugati hitelekből finanszírozta a mesterségesen fenntartott életszínvonalat.",
                    "Mert Magyarország fizette a Szovjetunió teljes űrkutatási programját.",
                    "Mert aranyhidat építettek a Dunán."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A hatalmas adósságteher a gazdaság összeomlásá_____ vezetett a nyolcvanas években. (allative suffix - hoz)",
                "answer": "hoz"
            },
            {
                "id": "b1-kadarkorszak-05.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Magyarország", "1982-ben", "belépett", "a", "Nemzetközi", "Valutaalapba."],
                "solution": ["Magyarország", "1982-ben", "belépett", "a", "Nemzetközi", "Valutaalapba."]
            },
            {
                "id": "b1-kadarkorszak-05.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik évben váltották le Kádár Jánost a pártfőtitkári tisztségéből?",
                "options": [
                    "1988 májusában.",
                    "1970-ben.",
                    "2004-ben."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gazdaság kifulladása miatt az életszínvonal folyamatosan csökken_____ kezdett. (infinitive - ni)",
                "answer": "ni"
            },
            {
                "id": "b1-kadarkorszak-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi jellemezte Magyarország gazdasági helyzetét az 1980-as évek végén?",
                "options": [
                    "Hatalmas államadósság, növekvő infláció és a szocialista modell kimerülése.",
                    "Óriási gazdasági robbanás és a világ legnagyobb devizatartaléka.",
                    "A teljes ipar azonnali és sikeres privatizációja."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A megöregedett Kádár János már nem tudott új válaszokat ad_____ a válságra. (to give - ni)",
                "answer": "ni"
            },
            {
                "id": "b1-kadarkorszak-05.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "szocialista", "gazdasági", "modell", "végérvényesen", "kifulladt", "az", "évtized", "végére."],
                "solution": ["A", "szocialista", "gazdasági", "modell", "végérvényesen", "kifulladt", "az", "évtized", "végére."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-kadarkorszak-consolidation",
        "exercises": [
            {
                "id": "b1-kadarkorszak-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi jellemezte a kádári kiegyezés társadalmi kompromisszumát?",
                "options": [
                    "A politikai jogok feladása a magánélet viszonylagos békéjéért és az anyagi biztonságért.",
                    "A szovjet hadsereg elleni állandó fegyveres harc.",
                    "A teljes kapitalista piacgazdaság azonnali bevezetése."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex02",
                "type": "fill-blank",
                "category": "history",
                "sentence": "1968-ban indult el az Új Gazdasági Mechaniz_____. (stem suffix - mus)",
                "answer": "mus"
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kádárizmus", "időszaka", "több", "mint", "három", "évtizeden", "át", "tartott."],
                "solution": ["A", "kádárizmus", "időszaka", "több", "mint", "három", "évtizeden", "át", "tartott."]
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hogyan tekint a modern magyar történettudomány a 'gulyáskommunizmus' korszakára?",
                "options": [
                    "Nyugati hitelekből fizetett, illuzórikus jólétként, amely elodázta az elkerülhetetlen gazdasági reformokat.",
                    "Magyarország történetének legsikeresebb, örökké fenntartható gazdasági csodájaként.",
                    "Egy olyan korszaként, amelyben egyetlen ember sem dolgozott."
                ],
                "correct": 0
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kulturális életben Aczél György bevezette a három T kategóriá_____. (accusative - ját)",
                "answer": "ját"
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "nyugati", "hitelek", "felhalmozódása", "súlyos", "adósságválsághoz", "vezetett."],
                "solution": ["A", "nyugati", "hitelek", "felhalmozódása", "súlyos", "adósságválsághoz", "vezetett."]
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az illegális ellenzéki írásokat szamizdat formájában terjesztet_____. (they distributed - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-kadarkorszak-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik politikai esemény jelezte Kádár János korszakának végét 1988 májusában?",
                "options": [
                    "A párt országos értekezletén felmentették Kádárt a főtitkári pozícióból.",
                    "Kádár királlyá koronázása a Mátyás-templomban.",
                    "Kádár azonnali emigrálása Moszkvába."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-kadarkorszak-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A kádári kiegyezés és konszolidáció", "Kádár's Compromise & Consolidation"),
        "02": ("Az Új Gazdasági Mechanizmus és a maszekok", "New Economic Mechanism & the Second Economy"),
        "03": ("A legvidámabb barakk és a gulyáskommunizmus", "The Happiest Barrack & Goulash Communism"),
        "04": ("A 'három T' és a szamizdat kultúra", "The 'Three Ts' & Samizdat Dissidence"),
        "05": ("Az adósságcsapda és a rendszer kifulladása", "The Debt Trap & Systemic Exhaustion")
    }

    story_refs = {
        "01": "stories/world/b1/b1-kadarkorszak-01-megtorlas.json",
        "02": "stories/world/b1/b1-kadarkorszak-02-mechanizmus.json",
        "03": "stories/world/b1/b1-kadarkorszak-03-gulyas.json",
        "04": "stories/world/b1/b1-kadarkorszak-04-haromt.json",
        "05": "stories/world/b1/b1-kadarkorszak-05-eladosodas.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.kadarkorszak-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Tacit Compromises, Economic Modality & Macroeconomic Retrospective in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} during the Kádár era.",
                        "I can use social, economic, and historical terminology of socialist Hungary.",
                        "I can answer essential citizenship exam questions regarding Kádár, 1968, and 1980s debt crisis.",
                        "I can master six target vocabulary items in historical context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-kadarkorszak-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-kadarkorszak-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-kadarkorszak-{padded}-ex.json",
                    "exerciseRefs": [f"b1-kadarkorszak-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-kadarkorszak-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.kadarkorszak-consolidation",
        "title": "Összefoglalás: A Kádár-korszak (Kádár Era Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of Kádár Era Discourse, Living Standards & Economic Transition",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-kadarkorszak.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-kadarkorszak-consolidation-ex.json",
                "exerciseRefs": [f"b1-kadarkorszak-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-kadarkorszak-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 26 (b1-kadarkorszak)!")

if __name__ == "__main__":
    build_unit_26_citizenship()
