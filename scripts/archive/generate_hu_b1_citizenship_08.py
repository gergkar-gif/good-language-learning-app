#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 8: Matthias Corvinus & the Renaissance Court (b1-matyas)."""

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

def build_unit_8_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.matyas.01",
        "lesson": "b1-matyas-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "trón", "translation": "throne", "pos": "noun"},
            {"lemma": "megválasztás", "translation": "election (to office)", "pos": "noun"},
            {"lemma": "koronázás", "translation": "coronation", "pos": "noun"},
            {"lemma": "ifjú", "translation": "youth, young man / youthful", "pos": "adjective"},
            {"lemma": "tárgyalás", "translation": "negotiation", "pos": "noun"},
            {"lemma": "holló", "translation": "raven (Corvinus emblem)", "pos": "noun"},
            {"lemma": "címerpajzs", "translation": "coat of arms shield", "pos": "noun"},
            {"lemma": "főnemes", "translation": "magnate, aristocrat", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-matyas-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.matyas.02",
        "lesson": "b1-matyas-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fekete sereg", "translation": "Black Army (Matthias's standing army)", "pos": "noun"},
            {"lemma": "zsoldos", "translation": "mercenary", "pos": "noun"},
            {"lemma": "állandó hadsereg", "translation": "standing army", "pos": "noun"},
            {"lemma": "hadvezér", "translation": "military commander, general", "pos": "noun"},
            {"lemma": "fegyverzet", "translation": "armament, weaponry", "pos": "noun"},
            {"lemma": "hadisarc", "translation": "war contribution, tribute", "pos": "noun"},
            {"lemma": "hadviselés", "translation": "warfare", "pos": "noun"},
            {"lemma": "fegyelem", "translation": "discipline", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-matyas-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.matyas.03",
        "lesson": "b1-matyas-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "reneszánsz", "translation": "Renaissance", "pos": "noun"},
            {"lemma": "humanista", "translation": "humanist", "pos": "noun"},
            {"lemma": "könyvtár", "translation": "library", "pos": "noun"},
            {"lemma": "corvina", "translation": "Corvina (manuscript from Matthias's library)", "pos": "noun"},
            {"lemma": "tudós", "translation": "scholar, scientist", "pos": "noun"},
            {"lemma": "építészet", "translation": "architecture", "pos": "noun"},
            {"lemma": "művészet", "translation": "art", "pos": "noun"},
            {"lemma": "visegrádi palota", "translation": "palace of Visegrád", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-matyas-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.matyas.04",
        "lesson": "b1-matyas-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "igazságos", "translation": "just, fair", "pos": "adjective"},
            {"lemma": "álruha", "translation": "disguise", "pos": "noun"},
            {"lemma": "adóreform", "translation": "tax reform", "pos": "noun"},
            {"lemma": "füstadó", "translation": "chimney/hearth tax (füstpénz)", "pos": "noun"},
            {"lemma": "rendtartás", "translation": "maintenance of order / ordinance", "pos": "noun"},
            {"lemma": "bíráskodás", "translation": "administration of justice / judging", "pos": "noun"},
            {"lemma": "törvényesség", "translation": "legality, rule of law", "pos": "noun"},
            {"lemma": "népmese", "translation": "folktale", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-matyas-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.matyas.05",
        "lesson": "b1-matyas-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "halál", "translation": "death", "pos": "noun"},
            {"lemma": "örökség", "translation": "heritage, legacy", "pos": "noun"},
            {"lemma": "mondás", "translation": "saying, adage", "pos": "noun"},
            {"lemma": "közmondás", "translation": "proverb", "pos": "noun"},
            {"lemma": "utókor", "translation": "posterity", "pos": "noun"},
            {"lemma": "gyász", "translation": "mourning, grief", "pos": "noun"},
            {"lemma": "történelmi korszak", "translation": "historical era", "pos": "noun"},
            {"lemma": "virágkor", "translation": "golden age, heyday", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-matyas-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.matyas.01.superlatives-history",
        "title": "Superlative & Absolute Comparisons: legfiatalabb, egyik legnagyobb",
        "sections": [
            {
                "type": "text",
                "title": "Using superlatives in historical descriptions",
                "content": "To characterize prominent historical monarchs, Hungarian uses the superlative prefix *leg-* (*legfiatalabb* = the youngest, *legerősebb* = the strongest) often combined with *egyik* ('one of the...'): *az egyik legnagyobb uralkodó* (one of the greatest rulers)."
            },
            {
                "type": "examples",
                "title": "Superlative historical examples",
                "items": [
                    {
                        "spanish": "Mátyás király az egyik leghíresebb uralkodó volt a magyar történelemben.",
                        "english": "King Matthias was one of the most famous rulers in Hungarian history."
                    },
                    {
                        "spanish": "A Duna jegén gyűlt össze a nép a király megválasztására.",
                        "english": "The people gathered on the ice of the Danube for the election of the king."
                    },
                    {
                        "spanish": "Alig tizenöt évesen lépett a magyar trónra a fiatal Hunyadi Mátyás.",
                        "english": "At barely fifteen years of age, the young Matthias Hunyadi ascended the Hungarian throne."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-matyas-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.matyas.02.correlative-comparative",
        "title": "Correlative Comparisons: minél ..., annál ...",
        "sections": [
            {
                "type": "text",
                "title": "Expressing proportional relationships with minél... annál",
                "content": "The correlative pair *minél ... annál ...* corresponds to English 'the more ..., the more ...'. It takes comparative adjectives or adverbs in both clauses."
            },
            {
                "type": "examples",
                "title": "Military correlatives",
                "items": [
                    {
                        "spanish": "Minél fegyelmezettebb volt a fekete sereg, annál több győzelmet aratott.",
                        "english": "The more disciplined the Black Army was, the more victories it achieved."
                    },
                    {
                        "spanish": "Minél jobban fizették a zsoldosokat, annál hűségesebben harcoltak.",
                        "english": "The better the mercenaries were paid, the more loyally they fought."
                    },
                    {
                        "spanish": "Mátyás állandó zsoldoshadsereget hozott létre a határok védelmére.",
                        "english": "Matthias established a standing mercenary army for the defence of the borders."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-matyas-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.matyas.03.cultural-flourishing",
        "title": "Cultural Flourishing & Patronage: virágzott, meghonosított",
        "sections": [
            {
                "type": "text",
                "title": "Describing Renaissance art and learning",
                "content": "To narrate the cultural golden age, Hungarian uses verbs like *virágzik* (to flourish, bloom), *meghonosít* (to naturalize / introduce into the country), and *felvirágoztat* (to cause to flourish)."
            },
            {
                "type": "examples",
                "title": "Renaissance cultural sentences",
                "items": [
                    {
                        "spanish": "Mátyás udvarában virágzott a reneszánsz művészet és az itáliai humanizmus.",
                        "english": "In Matthias's court, Renaissance art and Italian humanism flourished."
                    },
                    {
                        "spanish": "A Bibliotheca Corviniana a korszak egyik legértékesebb könyvtára volt.",
                        "english": "The Bibliotheca Corviniana was one of the most valuable libraries of the era."
                    },
                    {
                        "spanish": "Híres itáliai tudósok és építészek érkeztek Budára és Visegrádra.",
                        "english": "Famous Italian scholars and architects arrived in Buda and Visegrád."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-matyas-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.matyas.04.folktale-narration",
        "title": "Folktale & Legend Framing: a mesék szerint, álruhában",
        "sections": [
            {
                "type": "text",
                "title": "Reporting folktales and legendary justice",
                "content": "Folklore traditions are framed with *a népmesék szerint* (according to folktales), *a legenda úgy tartja* (the legend has it), and adverbial states like *álruhában* (in disguise, essive-modal *-ban / -ben*)."
            },
            {
                "type": "examples",
                "title": "Folklore and justice examples",
                "items": [
                    {
                        "spanish": "A népmesék szerint Mátyás király gyakran álruhában járta az országot.",
                        "english": "According to folktales, King Matthias often traveled the country in disguise."
                    },
                    {
                        "spanish": "Szigorúan megbüntette a korrupt földesurakat, és megvédte a szegényeket.",
                        "english": "He severely punished corrupt landlords and protected the poor."
                    },
                    {
                        "spanish": "Az adóreform révén bevezette a füstadót a kincstár bevételeinek növelésére.",
                        "english": "Through tax reform, he introduced the chimney tax to increase treasury revenues."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-matyas-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.matyas.05.historical-sayings",
        "title": "Historical Proverbs & Memorial Framing: Meghalt Mátyás, oda az igazság",
        "sections": [
            {
                "type": "text",
                "title": "Understanding historical adages and collective mourning",
                "content": "Famous historical adages like *„Meghalt Mátyás, oda az igazság”* summarize collective cultural judgment. In Hungarian grammar, *oda van valami* means something is lost, gone, or perished."
            },
            {
                "type": "examples",
                "title": "Historical legacy examples",
                "items": [
                    {
                        "spanish": "A közmondás szerint: „Meghalt Mátyás, oda az igazság.”",
                        "english": "According to the proverb: 'King Matthias is dead, justice has perished.'"
                    },
                    {
                        "spanish": "A király halála után a Magyar Királyság aranykora véget ért.",
                        "english": "After the king's death, the golden age of the Hungarian Kingdom came to an end."
                    },
                    {
                        "spanish": "Az utókor ma is a legnagyobb nemzeti hősök között tiszteli az igazságos királyt.",
                        "english": "Posterity still respects the just king among the greatest national heroes today."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-matyas-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.matyas.01",
        "title": "Mátyás megválasztása a Duna jegén",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In January 1458, the Hungarian nobility gathered on the frozen Danube beneath Buda Castle to elect the young Matthias Corvinus, son of hero János Hunyadi, to the throne.",
        "characters": [],
        "location": "Buda, Pest, a befagyott Duna",
        "grammar": ["superlatives-history"],
        "vocabularyTopics": ["Királyválasztás 1458", "Hunyadi Mátyás"],
        "paragraphs": [
            {"type": "narration", "text": "1458 dermesztően hideg telén a Duna vize vastag jéggé fagyott Buda és Pest között."},
            {"type": "narration", "text": "A hős nándorfehérvári győző, Hunyadi János ifjabbik fiát, Mátyást a nemesek egyhangúlag királlyá választották."},
            {"type": "narration", "text": "A hagyomány szerint a lelkes néptömeg a befagyott folyó jegén éljenezte az alig tizenöt éves ifjú uralkodót."},
            {"type": "narration", "text": "Mátyás családjának címere a csőrében aranygyűrűt tartó fekete holló volt, erről kapta a Corvinus nevet."},
            {"type": "narration", "text": "Az új király határozott lépésekkel vette át az ország irányítását, és hamarosan megerősítette a királyi tekintélyt."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas-01-megvalasztas.json", story_01)

    story_02 = {
        "id": "story.b1.matyas.02",
        "title": "A fekete sereg és a hadviselés",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "King Matthias established the legendary Black Army, one of Europe's first permanent professional standing armies, securing borders against Ottoman raids and conquering Vienna.",
        "characters": [],
        "location": "Bécs, cseh határok, végvárak",
        "grammar": ["correlative-comparative"],
        "vocabularyTopics": ["Fekete sereg", "Állandó hadsereg"],
        "paragraphs": [
            {"type": "narration", "text": "Mátyás király felismerte, hogy a nemesi felkelés nem elegendő az ország biztonságos védelméhez."},
            {"type": "narration", "text": "Ezért felállította a híres fekete sereget, Közép-Európa egyik legelső állandó zsoldoshadseregét."},
            {"type": "narration", "text": "A kitűnően felszerelt nehézlovasság és a modern tűzfegyverekkel harcoló gyalogság vasszigorú fegyelemben szolgált."},
            {"type": "narration", "text": "A sereg sikeresen visszaverte az oszmán betöréseket délen, és 1485-ben még Bécset is elfoglalta."},
            {"type": "narration", "text": "A fekete sereg ereje garantálta Magyarország katonai nagyhatalmi státuszát a tizenötödik század végén."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas-02-feketesereg.json", story_02)

    story_03 = {
        "id": "story.b1.matyas.03",
        "title": "A reneszánsz udvar és a Corvina",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Under Matthias and Queen Beatrice of Aragon, the royal courts at Buda and Visegrád became Europe's foremost Renaissance centers north of the Alps, home to the famous Corvina library.",
        "characters": [],
        "location": "Buda vára, Visegrádi palota",
        "grammar": ["cultural-flourishing"],
        "vocabularyTopics": ["Reneszánsz művészet", "Bibliotheca Corviniana"],
        "paragraphs": [
            {"type": "narration", "text": "Mátyás király és felesége, Beatrix aragóniai hercegnő Budát és Visegrádot igazi reneszánsz központtá emelte."},
            {"type": "narration", "text": "Itálián kívül Magyarország volt az első európai ország, ahol meghonosodott a reneszánsz művészet és az építészet."},
            {"type": "narration", "text": "A visegrádi palota vörösmárvány szökőkútjai és díszes függőkertjei lenyűgözték a külföldi diplomatákat."},
            {"type": "narration", "text": "A király létrehozta a Bibliotheca Corviniana könyvtárat, amely több ezer kézzel festett, felbecsülhetetlen értékű kódexet őrzött."},
            {"type": "narration", "text": "A budai könyvmásoló és miniatúrafestő műhely Európa legkiválóbb humanista tudósait vonzotta magához."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas-03-reneszanszudvar.json", story_03)

    story_04 = {
        "id": "story.b1.matyas.04",
        "title": "Mátyás király és az igazságos bíráskodás",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Known as 'Matthias the Just', the king modernized taxation through the chimney tax (füstpénz) and entered national folklore as the disguised monarch defending the common folk.",
        "characters": [],
        "location": "Magyar falvak, királyi bíróság",
        "grammar": ["folktale-narration"],
        "vocabularyTopics": ["Mátyás az igazságos", "Adóreform"],
        "paragraphs": [
            {"type": "narration", "text": "Mátyás uralkodása nemcsak a hadi sikerekről és a művészetről szólt, hanem a szigorú törvényességről is."},
            {"type": "narration", "text": "A király átfogó adóreformot hajtott végre: a kapuadó helyett bevezette a füstadót, amit minden háztartásnak fizetnie kellett."},
            {"type": "narration", "text": "A népmesék szerint Mátyás gyakran egyszerű álruhát öltött, hogy megnézze, hogyan bánnak a bírák a szegény emberekkel."},
            {"type": "narration", "text": "A gőgös urakat keményen megleckéztette, az elnyomott jobbágyoknak pedig igazságot szolgáltatott."},
            {"type": "narration", "text": "Ezért emlékezik rá a magyar nép mindmáig szeretettel úgy, mint Mátyás, az igazságos király."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas-04-igazsagossag.json", story_04)

    story_05 = {
        "id": "story.b1.matyas.05",
        "title": "Meghalt Mátyás, oda az igazság",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "When King Matthias died in Vienna in 1490 without a legitimate heir, Hungary entered rapid political fragmentation, crystallizing the enduring proverb 'King Matthias is dead, justice has perished.'",
        "characters": [],
        "location": "Bécs, Székesfehérvár, Buda",
        "grammar": ["historical-sayings"],
        "vocabularyTopics": ["Mátyás halála 1490", "Nemzeti emlékezet"],
        "paragraphs": [
            {"type": "narration", "text": "1490 tavaszán váratlan és megrendítő hír érkezett Bécsből: a nagy király negyvenhét évesen hirtelen meghalt."},
            {"type": "narration", "text": "A gyászoló nemzet Székesfehérváron, a királyi bazilikában helyezte örök nyugalomra a dicsőséges uralkodót."},
            {"type": "narration", "text": "Mátyásnak nem volt törvényes fia, így a halála után a főnemesek azonnal egymás ellen fordultak a hatalomért."},
            {"type": "narration", "text": "A fekete sereg feloszlott, a virágzó gazdaság meggyengült, és az oszmán veszély újra fenyegetővé vált."},
            {"type": "narration", "text": "Ekkor született a fájdalmas mondás, amely ma is él a magyar nyelvben: „Meghalt Mátyás, oda az igazság.”"}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas-05-orokseg.json", story_05)

    story_combined = {
        "id": "story.b1.matyas",
        "title": "Mátyás király és a reneszánsz udvar",
        "level": "B1",
        "order": 8,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The grand historical arc of Renaissance Hungary under King Matthias Corvinus (1458–1490): his dramatic Danube election, the invincible Black Army, European Renaissance patronage and the Corvina library, the legend of 'Matthias the Just', and the national grief following his sudden death in 1490.",
        "characters": [],
        "location": "Buda, Visegrád, Bécs, Székesfehérvár",
        "grammar": ["superlatives-history", "correlative-comparative", "cultural-flourishing", "folktale-narration", "historical-sayings"],
        "vocabularyTopics": ["Hunyadi Mátyás", "Reneszánsz aranykor", "Fekete sereg", "Corvina könyvtár", "Igazságos Mátyás"],
        "paragraphs": [
            {"type": "narration", "text": "1458 telén a befagyott Duna jegén a magyar rendek királlyá választották a hős Hunyadi János fiát, a fiatal Mátyást. A fekete hollós címerű uralkodó határozott kézzel erősítette meg a központi hatalmat, és Európa egyik legtekintélyesebb államává emelte a Magyar Királyságot."},
            {"type": "narration", "text": "A határok védelmére és hadjárataihoz Mátyás felállította a fekete sereget, az akkori kontinens legfegyelmezettebb állandó zsoldoshadseregét. A nehézlovasság és a tüzérség nemcsak a déli oszmán betöréseket állította meg, de 1485-ben még Bécset is elfoglalta."},
            {"type": "narration", "text": "Itáliai felesége, Beatrix révén a budai és visegrádi királyi palota az Alpoktól északra fekvő legelső reneszánsz kulturális központtá vált. A király által alapított Bibliotheca Corviniana kódexei a kor legkiválóbb tudósait és művészeit vonzották Magyarországra."},
            {"type": "narration", "text": "Modern adóreformjai — mint a füstadó bevezetése — biztosították a kincstár bevételeit, miközben szigorú bíráskodása és a népmesék álruhás történetei a nép körében megteremtették 'Mátyás, az igazságos' halhatatlan legendáját."},
            {"type": "narration", "text": "Amikor Mátyás 1490-ben Bécsben váratlanul elhunyt, az ország aranykora tragikusan lezárult. A nemzet fájdalmát örökítette meg a mindmáig élő magyar közmondás: 'Meghalt Mátyás, oda az igazság.'"}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-matyas.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-matyas-01",
        "exercises": [
            {
                "id": "b1-matyas-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["trón", "throne"],
                    ["megválasztás", "election"],
                    ["koronázás", "coronation"],
                    ["ifjú", "young man / youth"]
                ]
            },
            {
                "id": "b1-matyas-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["holló", "raven (Corvinus emblem)"],
                    ["címerpajzs", "coat of arms shield"],
                    ["főnemes", "magnate / aristocrat"],
                    ["tárgyalás", "negotiation"]
                ]
            },
            {
                "id": "b1-matyas-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben választották magyar királlyá Hunyadi Mátyást?",
                "options": ["1458-ban.", "1490-ben.", "1526-ban."],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "A hagyomány szerint hol gyűlt össze a nép Mátyás megválasztásakor?",
                "options": ["A befagyott Duna jegén Buda és Pest között.", "A pannonhalmi apátságban.", "A Balaton partján."],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mátyás király a magyar történelem egyik ... uralkodója volt.",
                "options": ["legjelentősebb", "jelentősebb", "jelentős"],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "A Hunyadi család címerében egy aranygyűrűt tartó fekete [holló] látható.",
                "options": ["holló", "oroszlán", "sas"],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Ki volt Hunyadi Mátyás édesapja?",
                "options": [
                    "Hunyadi János, a nándorfehérvári diadal hős hadvezére.",
                    "Szent István király.",
                    "Károly Róbert király."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Honnan származik a 'Corvinus' melléknév?",
                "options": [
                    "A holló latin nevéből (corvus), amely a családi címer madara volt.",
                    "Egy római császár nevéből.",
                    "A korona szóból."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hány éves volt Mátyás, amikor trónra lépett 1458-ban?",
                "options": ["Alig tizenöt éves.", "Harmincöt éves.", "Ötvenéves."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-matyas-02",
        "exercises": [
            {
                "id": "b1-matyas-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fekete sereg", "Black Army"],
                    ["zsoldos", "mercenary"],
                    ["állandó hadsereg", "standing army"],
                    ["hadvezér", "military commander"]
                ]
            },
            {
                "id": "b1-matyas-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fegyverzet", "weaponry / armament"],
                    ["hadisarc", "war contribution / tribute"],
                    ["hadviselés", "warfare"],
                    ["fegyelem", "discipline"]
                ]
            },
            {
                "id": "b1-matyas-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt a 'fekete sereg' a 15. századi Magyarországon?",
                "options": [
                    "Mátyás király állandó zsoldoshadserege, amely magas szintű fegyelemmel rendelkezett.",
                    "Egy sötét ruhás vallási rend.",
                    "A bányászok csapata."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik külföldi fővárost foglalta el Mátyás hadserege 1485-ben?",
                "options": ["Bécset.", "Prágát.", "Varsót."],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Minél jobban felszerelt volt a sereg, ... több sikert ért el a csatákban.",
                "options": ["annál", "akkor", "azért"],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "A király [állandó hadsereget] tartott fenn a királyi kincstár bevételeiből.",
                "options": ["állandó hadsereget", "alagutat", "bizonyítványt"],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért volt korszakalkotó a fekete sereg Európában?",
                "options": [
                    "Mert az elsők között hozott létre békeidőben is működő állandó zsoldoshadsereget.",
                    "Mert csak lovakból állt.",
                    "Mert ingyen harcolt a királyért."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kik szolgáltak a fekete seregben?",
                "options": [
                    "Profi cseh, német, magyar és lengyel zsoldoskatonák.",
                    "Csak külföldi szerzetesek.",
                    "Kizárólag jobbágyok."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi biztosította a fekete sereg megbízható fenntartását?",
                "options": [
                    "A király által szedett rendszeres hadiadók és a fegyelem.",
                    "A szomszédos országok ajándékai.",
                    "A templomi perselypénz."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-matyas-03",
        "exercises": [
            {
                "id": "b1-matyas-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["reneszánsz", "Renaissance"],
                    ["humanista", "humanist"],
                    ["könyvtár", "library"],
                    ["corvina", "Corvina manuscript"]
                ]
            },
            {
                "id": "b1-matyas-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["tudós", "scholar / scientist"],
                    ["építészet", "architecture"],
                    ["művészet", "art"],
                    ["visegrádi palota", "palace of Visegrád"]
                ]
            },
            {
                "id": "b1-matyas-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt a Bibliotheca Corviniana?",
                "options": [
                    "Mátyás király híres reneszánsz könyvtára Budán, tele díszes kéziratokkal.",
                    "A fekete sereg fegyverraktára.",
                    "Egy visegrádi lovagi torna."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan nevezték Mátyás könyvtárának értékes, kézzel másolt köteteit?",
                "options": ["Corvináknak.", "Kódexeknek.", "Krónikáknak."],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mátyás udvarában ... a reneszánsz kultúra és a tudomány.",
                "options": ["virágzott", "virágzik volt", "virágozni fogott"],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "Beatrix királyné révén itáliai [humanista] művészek érkeztek Budára.",
                "options": ["humanista", "zsoldos", "alagút"],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért büszke az utókor a magyar reneszánsz kultúrára?",
                "options": [
                    "Mert Magyarország volt az első ország Itálián kívül, ahol felvirágzott a reneszánsz.",
                    "Mert itt találták fel a könyvnyomtatást.",
                    "Mert minden magyar ember megtanult olaszul."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik két királyi rezidencia volt a magyar reneszánsz építészet csúcsa?",
                "options": [
                    "A budai várpalota és a visegrádi királyi palota.",
                    "Esztergom és Székesfehérvár.",
                    "Debrecen és Szeged."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Honnan származott Mátyás felesége, Beatrix királyné?",
                "options": ["Nápolyból (Itáliából).", "Párizsból.", "Madridból."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-matyas-04",
        "exercises": [
            {
                "id": "b1-matyas-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["igazságos", "just, fair"],
                    ["álruha", "disguise"],
                    ["adóreform", "tax reform"],
                    ["füstadó", "chimney/hearth tax"]
                ]
            },
            {
                "id": "b1-matyas-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rendtartás", "ordinance / maintenance of order"],
                    ["bíráskodás", "judging / administration of justice"],
                    ["törvényesség", "rule of law / legality"],
                    ["népmese", "folktale"]
                ]
            },
            {
                "id": "b1-matyas-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen jelzővel illeti Mátyást a magyar néphagyomány?",
                "options": ["Mátyás, az igazságos.", "Mátyás, a hódító.", "Mátyás, a rettegett."],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "A népmesék szerint miért öltött álruhát a király?",
                "options": [
                    "Hogy a saját szemével lássa az egyszerű nép sorsát és az urak viselkedését.",
                    "Mert nem szeretett királyi ruhát hordani.",
                    "Hogy elmeneküljön a palotából."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "A legendák szerint Mátyás király gyakran ... járta az országot.",
                "options": ["álruhában", "álruháról", "álruhához"],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "A király [füstadót] vezetett be minden egyes kémény után a kincstár gyarapítására.",
                "options": ["füstadót", "hágót", "corvinát"],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért volt igazságosabb a füstadó, mint a korábbi kapuadó?",
                "options": [
                    "Mert nem portánként, hanem háztartásonként (kéményenként) kellett fizetni, így az urak nem trükközhettek a kapukkal.",
                    "Mert a szegényeknek egyáltalán nem kellett adózniuk.",
                    "Mert arany helyett búzával fizettek."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen témájú mesék fűződnek Mátyás király nevéhez?",
                "options": [
                    "Olyan történetek, ahol a bölcs és igazságos király megbünteti a gőgös urakat és megjutalmazza a becsületes szegényeket.",
                    "Sárkányokról és óriásokról szóló mesék.",
                    "Tengeri utazásokról szóló történetek."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan gondoskodott Mátyás a törvényességről a bíróságokon?",
                "options": [
                    "Szigorú rendeletekkel szabályozta az ítélkezést és független szakembereket bízott meg bíráskodással.",
                    "Eltörölte az írott törvényeket.",
                    "Csak külföldi bírákat alkalmazott."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-matyas-05",
        "exercises": [
            {
                "id": "b1-matyas-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["halál", "death"],
                    ["örökség", "heritage / legacy"],
                    ["mondás", "saying / adage"],
                    ["közmondás", "proverb"]
                ]
            },
            {
                "id": "b1-matyas-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["utókor", "posterity"],
                    ["gyász", "mourning"],
                    ["történelmi korszak", "historical era"],
                    ["virágkor", "golden age / heyday"]
                ]
            },
            {
                "id": "b1-matyas-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikor hunyt el Mátyás király Bécsben?",
                "options": ["1490-ben.", "1456-ban.", "1526-ban."],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik híres magyar közmondás fűződik Mátyás király halálához?",
                "options": [
                    "„Meghalt Mátyás, oda az igazság.”",
                    "„Késő bánat ebgondolat.”",
                    "„Aki mer, az nyer.”"
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "A közmondásban az 'oda az igazság' kifejezés azt jelenti, hogy az igazság ...",
                "options": ["elveszett, véget ért.", "megérkezett.", "virágzik."],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "Mátyás halálával a Magyar Királyság dicsőséges [virágkora] ért véget.",
                "options": ["virágkora", "csomagja", "pótlóbusza"],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért fontos Mátyás kora a magyar nemzeti identitásban?",
                "options": [
                    "Mert ez volt az önálló, erős és virágzó középkori Magyar Királyság utolsó fénykora a török hódoltság előtt.",
                    "Mert ekkor vezették be a modern vasutat.",
                    "Mert ekkor csatlakozott Magyarország a NATO-hoz."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mi történt a fekete sereggel Mátyás király halála után?",
                "options": [
                    "Mivel az új gyenge uralkodók nem fizették a zsoldot, a sereg feloszlott, az ország védtelen maradt.",
                    "A sereg tovább növekedett.",
                    "A sereg átköltözött Itáliába."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol temették el Mátyás királyt?",
                "options": ["Székesfehérváron, a királyi bazilikában.", "Bécsben.", "Buda várában."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-matyas-consolidation",
        "exercises": [
            {
                "id": "b1-matyas-consolidation.ex01",
                "type": "matching",
                "category": "review",
                "pairs": [
                    ["1458", "Mátyás királlyá választása a Duna jegén"],
                    ["fekete sereg", "állandó, fegyelmezett zsoldoshadsereg"],
                    ["Bibliotheca Corviniana", "híres budai reneszánsz kódexkönyvtár"],
                    ["1490", "Mátyás király halála Bécsben"]
                ]
            },
            {
                "id": "b1-matyas-consolidation.ex02",
                "type": "matching",
                "category": "review",
                "pairs": [
                    ["Corvina", "díszes kézzel festett királyi kódex"],
                    ["füstadó", "háztartásonként fizetett királyi adó"],
                    ["álruha", "a király titkos népviselete a mesékben"],
                    ["„Meghalt Mátyás...”", "„...oda az igazság.”"]
                ]
            },
            {
                "id": "b1-matyas-consolidation.ex03",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik madár tartott aranygyűrűt a csőrében a Hunyadiak címerén?",
                "options": ["A holló.", "A sas.", "A sólyom."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex04",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik ország kultúrája hatott a legerősebben Mátyás budai udvarára?",
                "options": ["Itália (az olasz reneszánsz).", "Franciaország.", "Oroszország."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex05",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hogyan hívták Mátyás itáliai születésű királynéját?",
                "options": ["Beatrix aragóniai hercegnőnek.", "Erzsébetnek.", "Máriának."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex06",
                "type": "multiple-choice",
                "category": "review",
                "question": "Mit jelent az a mondás, hogy 'Meghalt Mátyás, oda az igazság'?",
                "options": [
                    "Hogy Mátyás halálával megszűnt az igazságos bíráskodás és a rend az országban.",
                    "Hogy a bíróságok bezártak a gyász miatt.",
                    "Hogy a könyvek elvesztek a könyvtárból."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex07",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik híres dunai palotát építette át Mátyás csodás reneszánsz rezidenciává?",
                "options": ["A visegrádi királyi palotát.", "Az esztergomi várat.", "A pozsonyi várat."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex08",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen adót vezetett be Mátyás a kapuadó helyébe?",
                "options": ["A füstadót (füstpénzt).", "A tizedet.", "A vámot."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex09",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik hadseregtípust képviselte a fekete sereg?",
                "options": [
                    "Állandó, jól fizetett és fegyelmezett zsoldoshadsereget.",
                    "Önkéntes paraszti sereget.",
                    "Kizárólag lovagi tornacsapatot."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex10",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hány Corvinát őrzött meg a történelem Mátyás könyvtárából?",
                "options": [
                    "Több mint kétszázat a világ különböző nagy könyvtáraiban.",
                    "Egyet sem, mind elégett.",
                    "Több mint százezret."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex11",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik nyugati császári várost foglalta el Mátyás 1485-ben?",
                "options": ["Bécset.", "Rómát.", "Berlint."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex12",
                "type": "multiple-choice",
                "category": "review",
                "question": "Miért hívják Mátyást mind a mai napig 'az igazságosnak'?",
                "options": [
                    "Mert a néphagyomány szerint megvédte a szegényeket a gazdag urak elnyomásától.",
                    "Mert sosem hozott törvényeket.",
                    "Mert nem szedett adót senkitől."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex13",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hol koronázták meg hivatalosan Mátyást a Szent Koronával 1464-ben?",
                "options": ["Székesfehérváron.", "Budán.", "Visegrádon."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex14",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hogyan mondjuk magyarul: 'The more disciplined the army was, the more it won'?",
                "options": [
                    "Minél fegyelmezettebb volt a sereg, annál többet győzött.",
                    "Mikor fegyelmezett a sereg, akkor győzött.",
                    "Fegyelmes sereg győztesen harcolt."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex15",
                "type": "multiple-choice",
                "category": "review",
                "question": "Ki volt Mátyás király nagy hírű hadvezére a fekete sereg élén?",
                "options": ["Kinizsi Pál.", "Kapisztrán János.", "Csák Máté."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex16",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik évszázadban uralkodott Mátyás király?",
                "options": ["A 15. században (1458–1490).", "A 13. században.", "A 18. században."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex17",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen kulturális korszak jellemezte Mátyás uralkodását?",
                "options": ["A reneszánsz és a humanizmus korszaka.", "A barokk korszak.", "A romantika kora."],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex18",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hová járt Mátyás a mesék szerint álruhában?",
                "options": [
                    "A falvakba és mezővárosokba, a nép közé.",
                    "Csak a budai palota pincéjébe.",
                    "Külföldi tengerekre."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex19",
                "type": "multiple-choice",
                "category": "review",
                "question": "Miért kérdezik gyakran Mátyás királyt az állampolgársági interjún?",
                "options": [
                    "Mert Mátyás a magyar nemzeti emlékezet egyik legkiemelkedőbb, legnépszerűbb történelmi alakja.",
                    "Mert ő írta a jelenlegi Alaptörvényt.",
                    "Mert ő alapította Budapestet."
                ],
                "correct": 0
            },
            {
                "id": "b1-matyas-consolidation.ex20",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen sors várt a virágzó királyságra Mátyás halála után a 16. században?",
                "options": [
                    "A központi hatalom összeomlott, és az ország a mohácsi csata után három részre szakadt.",
                    "A királyság örökre megőrizte nagyhatalmi státuszát.",
                    "Magyarország békés köztársasággá vált."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-matyas-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.matyas-01",
        "title": "The Election of Matthias - Mátyás megválasztása",
        "level": "B1",
        "grammar": "Superlative & absolute comparisons: legfiatalabb, egyik legjelentősebb",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can narrate the dramatic January 1458 election of young Matthias on the frozen Danube.",
                    "I can explain the origin of the Corvinus name and the raven emblem with the gold ring.",
                    "I can use superlative and absolute comparative structures in historical descriptions.",
                    "I can use eight new vocabulary items related to medieval coronations and monarchical succession."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-matyas-01-megvalasztas.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-matyas-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-matyas-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-matyas-01-ex.json", "exerciseRefs": [
                "b1-matyas-01.ex01", "b1-matyas-01.ex01b", "b1-matyas-01.ex02", "b1-matyas-01.ex03",
                "b1-matyas-01.ex04", "b1-matyas-01.ex05", "b1-matyas-01.ex06", "b1-matyas-01.ex07", "b1-matyas-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the dramatic January 1458 election of young Matthias on the frozen Danube.",
                    "I can explain the origin of the Corvinus name and the raven emblem with the gold ring.",
                    "I can use superlative and absolute comparative structures in historical descriptions.",
                    "I can use eight new vocabulary items related to medieval coronations and monarchical succession."
                ]
            }
        ],
        "goal": [
            "I can narrate the dramatic January 1458 election of young Matthias on the frozen Danube.",
            "I can explain the origin of the Corvinus name and the raven emblem with the gold ring.",
            "I can use superlative and absolute comparative structures in historical descriptions.",
            "I can use eight new vocabulary items related to medieval coronations and monarchical succession."
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.matyas-02",
        "title": "The Black Army - A fekete sereg",
        "level": "B1",
        "grammar": "Correlative comparisons: minél ..., annál ...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the composition, discipline, and weaponry of Matthias's Black Army (fekete sereg).",
                    "I can explain why creating a professional standing army was revolutionary in 15th-century Europe.",
                    "I can use correlative comparative sentences (minél fegyelmezettebb, annál sikeresebb).",
                    "I can discuss Matthias's military campaigns, border defense, and the 1485 capture of Vienna."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-matyas-02-feketesereg.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-matyas-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-matyas-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-matyas-02-ex.json", "exerciseRefs": [
                "b1-matyas-02.ex01", "b1-matyas-02.ex01b", "b1-matyas-02.ex02", "b1-matyas-02.ex03",
                "b1-matyas-02.ex04", "b1-matyas-02.ex05", "b1-matyas-02.ex06", "b1-matyas-02.ex07", "b1-matyas-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the composition, discipline, and weaponry of Matthias's Black Army (fekete sereg).",
                    "I can explain why creating a professional standing army was revolutionary in 15th-century Europe.",
                    "I can use correlative comparative sentences (minél fegyelmezettebb, annál sikeresebb).",
                    "I can discuss Matthias's military campaigns, border defense, and the 1485 capture of Vienna."
                ]
            }
        ],
        "goal": [
            "I can describe the composition, discipline, and weaponry of Matthias's Black Army (fekete sereg).",
            "I can explain why creating a professional standing army was revolutionary in 15th-century Europe.",
            "I can use correlative comparative sentences (minél fegyelmezettebb, annál sikeresebb).",
            "I can discuss Matthias's military campaigns, border defense, and the 1485 capture of Vienna."
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.matyas-03",
        "title": "A Renaissance Court in Buda - Reneszánsz udvar Budán",
        "level": "B1",
        "grammar": "Cultural flourishing & patronage: virágzott, meghonosodott, felvirágoztat",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain why Hungary was the first country outside Italy to adopt Renaissance art and humanism.",
                    "I can describe the Bibliotheca Corviniana and the cultural significance of the Corvina codices.",
                    "I can describe the palaces at Buda and Visegrád, their red marble fountains, and hanging gardens.",
                    "I can use eight new vocabulary items related to Renaissance scholarship, literature, and art."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-matyas-03-reneszanszudvar.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-matyas-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-matyas-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-matyas-03-ex.json", "exerciseRefs": [
                "b1-matyas-03.ex01", "b1-matyas-03.ex01b", "b1-matyas-03.ex02", "b1-matyas-03.ex03",
                "b1-matyas-03.ex04", "b1-matyas-03.ex05", "b1-matyas-03.ex06", "b1-matyas-03.ex07", "b1-matyas-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain why Hungary was the first country outside Italy to adopt Renaissance art and humanism.",
                    "I can describe the Bibliotheca Corviniana and the cultural significance of the Corvina codices.",
                    "I can describe the palaces at Buda and Visegrád, their red marble fountains, and hanging gardens.",
                    "I can use eight new vocabulary items related to Renaissance scholarship, literature, and art."
                ]
            }
        ],
        "goal": [
            "I can explain why Hungary was the first country outside Italy to adopt Renaissance art and humanism.",
            "I can describe the Bibliotheca Corviniana and the cultural significance of the Corvina codices.",
            "I can describe the palaces at Buda and Visegrád, their red marble fountains, and hanging gardens.",
            "I can use eight new vocabulary items related to Renaissance scholarship, literature, and art."
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.matyas-04",
        "title": "Justice & Good Government - Mátyás, az igazságos",
        "level": "B1",
        "grammar": "Folktale framing: a mesék szerint, álruhában járta az országot",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain why King Matthias earned the popular title 'Matthias the Just' (Mátyás, az igazságos).",
                    "I can describe the folklore motif of the king traveling among the people in disguise (álruhában).",
                    "I can explain Matthias's fiscal reform: replacing the gate tax with the chimney tax (füstadó).",
                    "I can use eight new vocabulary items related to taxation, justice, and folklore traditions."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-matyas-04-igazsagossag.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-matyas-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-matyas-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-matyas-04-ex.json", "exerciseRefs": [
                "b1-matyas-04.ex01", "b1-matyas-04.ex01b", "b1-matyas-04.ex02", "b1-matyas-04.ex03",
                "b1-matyas-04.ex04", "b1-matyas-04.ex05", "b1-matyas-04.ex06", "b1-matyas-04.ex07", "b1-matyas-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain why King Matthias earned the popular title 'Matthias the Just' (Mátyás, az igazságos).",
                    "I can describe the folklore motif of the king traveling among the people in disguise (álruhában).",
                    "I can explain Matthias's fiscal reform: replacing the gate tax with the chimney tax (füstadó).",
                    "I can use eight new vocabulary items related to taxation, justice, and folklore traditions."
                ]
            }
        ],
        "goal": [
            "I can explain why King Matthias earned the popular title 'Matthias the Just' (Mátyás, az igazságos).",
            "I can describe the folklore motif of the king traveling among the people in disguise (álruhában).",
            "I can explain Matthias's fiscal reform: replacing the gate tax with the chimney tax (füstadó).",
            "I can use eight new vocabulary items related to taxation, justice, and folklore traditions."
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.matyas-05",
        "title": "\"King Matthias Is Dead, Justice Has Perished\" - Meghalt Mátyás, oda az igazság",
        "level": "B1",
        "grammar": "Proverbs & collective memorial: Meghalt Mátyás, oda az igazság",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the circumstances of King Matthias's sudden death in Vienna in 1490.",
                    "I can analyze the famous proverb 'Meghalt Mátyás, oda az igazság' and its cultural resonance.",
                    "I can outline what happened to Hungary following 1490: dissolution of the Black Army and decline.",
                    "I can confidently answer citizenship interview questions regarding Matthias's golden age."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-matyas-05-orokseg.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-matyas-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-matyas-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-matyas-05-ex.json", "exerciseRefs": [
                "b1-matyas-05.ex01", "b1-matyas-05.ex01b", "b1-matyas-05.ex02", "b1-matyas-05.ex03",
                "b1-matyas-05.ex04", "b1-matyas-05.ex05", "b1-matyas-05.ex06", "b1-matyas-05.ex07", "b1-matyas-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain the circumstances of King Matthias's sudden death in Vienna in 1490.",
                    "I can analyze the famous proverb 'Meghalt Mátyás, oda az igazság' and its cultural resonance.",
                    "I can outline what happened to Hungary following 1490: dissolution of the Black Army and decline.",
                    "I can confidently answer citizenship interview questions regarding Matthias's golden age."
                ]
            }
        ],
        "goal": [
            "I can explain the circumstances of King Matthias's sudden death in Vienna in 1490.",
            "I can analyze the famous proverb 'Meghalt Mátyás, oda az igazság' and its cultural resonance.",
            "I can outline what happened to Hungary following 1490: dissolution of the Black Army and decline.",
            "I can confidently answer citizenship interview questions regarding Matthias's golden age."
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.matyas-consolidation",
        "title": "Unit 8 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can narrate the entire historical reign of King Matthias Corvinus from 1458 to 1490.",
                    "I can explain the Black Army, the Renaissance court in Buda and Visegrád, and the Corvina library.",
                    "I can discuss tax reform (füstadó), judicial fairness, and the proverb 'Meghalt Mátyás, oda az igazság'.",
                    "I can answer all citizenship interview questions on Matthias Corvinus with complete fluency."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-matyas-consolidation-ex.json", "exerciseRefs": [
                "b1-matyas-consolidation.ex01", "b1-matyas-consolidation.ex02", "b1-matyas-consolidation.ex03", "b1-matyas-consolidation.ex04",
                "b1-matyas-consolidation.ex05", "b1-matyas-consolidation.ex06", "b1-matyas-consolidation.ex07", "b1-matyas-consolidation.ex08",
                "b1-matyas-consolidation.ex09", "b1-matyas-consolidation.ex10", "b1-matyas-consolidation.ex11", "b1-matyas-consolidation.ex12",
                "b1-matyas-consolidation.ex13", "b1-matyas-consolidation.ex14", "b1-matyas-consolidation.ex15", "b1-matyas-consolidation.ex16",
                "b1-matyas-consolidation.ex17", "b1-matyas-consolidation.ex18", "b1-matyas-consolidation.ex19", "b1-matyas-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the entire historical reign of King Matthias Corvinus from 1458 to 1490.",
                    "I can explain the Black Army, the Renaissance court in Buda and Visegrád, and the Corvina library.",
                    "I can discuss tax reform (füstadó), judicial fairness, and the proverb 'Meghalt Mátyás, oda az igazság'.",
                    "I can answer all citizenship interview questions on Matthias Corvinus with complete fluency."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-matyas-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_8_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 8!")
