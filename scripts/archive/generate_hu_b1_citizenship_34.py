#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 34: Hungarian Culture, Science & Heritage (b1-nemzetiertekek)."""

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

def build_unit_34_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.nemzetiertekek.01",
        "lesson": "b1-nemzetiertekek-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nobel-díj", "translation": "Nobel Prize (highest international scientific accolade)", "pos": "noun"},
            {"lemma": "felfedezés", "translation": "scientific discovery", "pos": "noun"},
            {"lemma": "C-vitamin", "translation": "Vitamin C (isolated from paprika by Albert Szent-Györgyi)", "pos": "noun"},
            {"lemma": "kutatás", "translation": "scientific research, investigation", "pos": "noun"},
            {"lemma": "áttörés", "translation": "breakthrough, revolutionary advance", "pos": "noun"},
            {"lemma": "tudós", "translation": "scientist, scholar, researcher", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiertekek-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.nemzetiertekek.02",
        "lesson": "b1-nemzetiertekek-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "találmány", "translation": "invention, ingenious creation", "pos": "noun"},
            {"lemma": "feltaláló", "translation": "inventor", "pos": "noun"},
            {"lemma": "golyóstoll", "translation": "ballpoint pen (invented by László Bíró)", "pos": "noun"},
            {"lemma": "bűvös kocka", "translation": "Rubik's Cube / Magic Cube (invented by Ernő Rubik)", "pos": "noun"},
            {"lemma": "dinamó", "translation": "dynamo (electric generator invented by Ányos Jedlik)", "pos": "noun"},
            {"lemma": "anyák megmentője", "translation": "savior of mothers (Ignác Semmelweis, pioneer of antiseptic handwashing)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiertekek-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.nemzetiertekek.03",
        "lesson": "b1-nemzetiertekek-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "zeneszerző", "translation": "musical composer", "pos": "noun"},
            {"lemma": "népdalgyűjtés", "translation": "folk song collecting (ethnomusicological fieldwork)", "pos": "noun"},
            {"lemma": "Kodály-módszer", "translation": "Kodály method (world-renowned music education pedagogy)", "pos": "noun"},
            {"lemma": "zeneművészet", "translation": "art of music, musical culture", "pos": "noun"},
            {"lemma": "Magyar Rapszódiák", "translation": "Hungarian Rhapsodies (masterpieces by Ferenc Liszt)", "pos": "noun"},
            {"lemma": "operett", "translation": "operetta (musical theater genre popularized by Imre Kálmán)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiertekek-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.nemzetiertekek.04",
        "lesson": "b1-nemzetiertekek-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "irodalmi örökség", "translation": "literary heritage", "pos": "noun"},
            {"lemma": "költészet", "translation": "poetry, verse", "pos": "noun"},
            {"lemma": "képzőművészet", "translation": "fine arts, visual arts", "pos": "noun"},
            {"lemma": "festőművész", "translation": "painter, fine artist", "pos": "noun"},
            {"lemma": "nemzeti öntudat", "translation": "national consciousness, civic cultural identity", "pos": "noun"},
            {"lemma": "remekmű", "translation": "masterpiece, magnum opus", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiertekek-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.nemzetiertekek.05",
        "lesson": "b1-nemzetiertekek-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hungarikum", "translation": "Hungarikum (officially certified distinctive Hungarian national value)", "pos": "noun"},
            {"lemma": "világörökség", "translation": "UNESCO World Heritage", "pos": "noun"},
            {"lemma": "hagyományőrzés", "translation": "preservation of traditions and folkloric customs", "pos": "noun"},
            {"lemma": "népművészet", "translation": "folk art, decorative vernacular craft", "pos": "noun"},
            {"lemma": "Tokaji aszú", "translation": "Tokaji Aszú (historic noble rot sweet wine of the Tokaj region)", "pos": "noun"},
            {"lemma": "busójárás", "translation": "Busó carnival of Mohács (UNESCO intangible heritage winter-farewell rite)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiertekek-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.nemzetiertekek.01.scientific-discoveries",
        "title": "Scientific Discoveries & Passive Participles in -ott/-ett",
        "sections": [
            {
                "type": "text",
                "title": "Narrating Discoveries with Participles",
                "content": "When narrating scientific accomplishments and Nobel distinctions, Hungarian uses past participles functioning as adjectives (*felfedezett*, *feltalált*, *kifejlesztett*, *elismert*), combined with instrumental arguments (*-val/-vel tüntették ki*)."
            },
            {
                "type": "examples",
                "title": "Scientific attribution examples",
                "items": [
                    {"spanish": "Szent-Györgyi Albertet a szegedi paprikából kivont C-vitaminért tüntették ki Nobel-díjjal.", "english": "Albert Szent-Györgyi was awarded the Nobel Prize for Vitamin C extracted from Szeged paprika."},
                    {"spanish": "Karikó Katalint és Krausz Ferencet 2023-ban tüntették ki a legrangosabb tudományos elismeréssel.", "english": "Katalin Karikó and Ferenc Krausz were honored with the most prestigious scientific distinction in 2023."},
                    {"spanish": "A magyar tudósok által kifejlesztett eljárások megváltoztatták a világot.", "english": "The procedures developed by Hungarian scientists transformed the world."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiertekek-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.nemzetiertekek.02.essive-designation",
        "title": "Designation with the Essive-Modal Case: -ként and -ként tartják számon",
        "sections": [
            {
                "type": "text",
                "title": "Recognizing Historic Roles",
                "content": "To define the historic status of innovators and benefactors, Hungarian uses the essive-modal suffix *-ként* ('as / in the capacity of'), governed by recognition verbs like *tart számon* (keep in record, recognize) or *válik ismertté* (become known as)."
            },
            {
                "type": "examples",
                "title": "Essive designation examples",
                "items": [
                    {"spanish": "Semmelweis Ignácot az anyák megmentőjeként tartja számon a világ orvostörténelme.", "english": "The medical history of the world recognizes Ignác Semmelweis as the savior of mothers."},
                    {"spanish": "Jedlik Ányos a dinamó feltalálójaként írta be magát a technika történetébe.", "english": "Ányos Jedlik wrote himself into the history of technology as the inventor of the dynamo."},
                    {"spanish": "Bíró László golyóstolla világszerte ismertté vált.", "english": "László Bíró's ballpoint pen became known worldwide."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiertekek-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.nemzetiertekek.03.cultural-valencies",
        "title": "Cultural Contribution Valencies: Hozzájárul, gyökerezik, megalapoz",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Valencies in Music & Culture",
                "content": "To express artistic impact, standard Hungarian deploys precise verbal governors: *hozzájárul vmihez* (contribute to), *gyökerezik vmiben* (be rooted in), and *megalapoz vmit* (lay the foundation for)."
            },
            {
                "type": "examples",
                "title": "Cultural valency examples",
                "items": [
                    {"spanish": "Bartók Béla és Kodály Zoltán zenéje az ősi magyar népdalkincsben gyökerezik.", "english": "The music of Béla Bartók and Zoltán Kodály is rooted in the ancient treasury of Hungarian folk songs."},
                    {"spanish": "A Kodály-módszer világszerte hozzájárult a zenei nevelés megújulásához.", "english": "The Kodály method contributed worldwide to the renewal of music education."},
                    {"spanish": "Liszt Ferenc zongoraművészete és Magyar Rapszódiái egyetemes sikert arattak.", "english": "Ferenc Liszt's piano artistry and Hungarian Rhapsodies achieved universal acclaim."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiertekek-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.nemzetiertekek.04.canonical-influence",
        "title": "Canonical Influence & Superlatives: Kiemelkedő alakja, legjelentősebb",
        "sections": [
            {
                "type": "text",
                "title": "Characterizing Canonical Figures",
                "content": "When presenting prominent authors, poets, and visual artists in the citizenship examination, Hungarian uses canonical superlatives (*a legjelentősebb költőnk*) and structural genitive idioms (*kiemelkedő alakja a...*, *meghatározó mérföldköve a...*)."
            },
            {
                "type": "examples",
                "title": "Canonical characterization examples",
                "items": [
                    {"spanish": "Petőfi Sándor és Arany János a 19. századi magyar költészet legkiemelkedőbb alakjai.", "english": "Sándor Petőfi and János Arany are the most prominent figures of 19th-century Hungarian poetry."},
                    {"spanish": "Munkácsy Mihály festményei a nemzeti és az egyetemes képzőművészet remekművei közé tartoznak.", "english": "Mihály Munkácsy's paintings belong among the masterpieces of national and universal fine art."},
                    {"spanish": "Ady Endre és József Attila művei máig mély hatást gyakorolnak a nemzeti öntudatra.", "english": "The works of Endre Ady and Attila József continue to exert a profound impact on national consciousness to this day."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiertekek-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.nemzetiertekek.05.heritage-designation",
        "title": "Designating National Heritage: Hungarikummá nyilvánít, védelmet élvez",
        "sections": [
            {
                "type": "text",
                "title": "Administrative & Folkloric Designations",
                "content": "Official recognition of traditions and crafts employs the translative-factitive suffix *-vá/-vé* (*hungarikummá nyilvánítják* - is declared a Hungarikum) and formal predicates of preservation: *védelmet élvez* (enjoys protection), *megőrzi a hagyományt* (preserves tradition)."
            },
            {
                "type": "examples",
                "title": "Heritage designation examples",
                "items": [
                    {"spanish": "A törvény értelmében a Tokaji aszút kiemelkedő nemzeti értékké és hungarikummá nyilvánították.", "english": "Pursuant to the law, Tokaji aszú was declared an outstanding national value and a Hungarikum."},
                    {"spanish": "A mohácsi busójárás az UNESCO szellemi kulturális örökségének részét képezi.", "english": "The Busó festival of Mohács forms part of UNESCO's intangible cultural heritage."},
                    {"spanish": "Hollókő ófaluja hűen megőrzi a palóc népi építészet évszázados hagyományait.", "english": "The old village of Hollókő faithfully preserves the centuries-old traditions of Palóc vernacular architecture."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiertekek-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized World Stories (5 segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.nemzetiertekek.01",
        "title": "A magyar tudomány csillagai és a Nobel-díjasok",
        "level": "B1",
        "lesson": 1,
        "order": 34,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The remarkable contributions of Hungarian scientists and Nobel laureates to universal human knowledge, from Albert Szent-Györgyi's isolation of Vitamin C in Szeged to Katalin Karikó and Ferenc Krausz's 2023 Nobel prizes.",
        "characters": [],
        "location": "Szeged és Budapest",
        "grammar": ["Scientific Discoveries & Passive Participles in -ott/-ett"],
        "vocabularyTopics": ["nobel_prize", "science", "discoveries"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország lélekszámához képest kivételesen sok világhírű tudóssal gazdagította az egyetemes emberi műveltséget. A magyar szellemi alkotóerő egyik legszebb bizonyítéka a magyar vagy magyar származású Nobel-díjasok hosszú sora."
            },
            {
                "type": "narration",
                "text": "Szent-Györgyi Albert a szegedi egyetem laboratóriumában kutatva a helyi fűszerpaprikából vonta ki a tiszta C-vitamint. Munkásságáért 1937-ben orvosi Nobel-díjjal tüntették ki, és mindmáig ő az egyetlen, aki Magyarországon végzett kutatásaiért kapta meg az elismerést."
            },
            {
                "type": "narration",
                "text": "A magyar fizikusok, köztük Wigner Jenő és Gábor Dénes – a holográfia atyja –, forradalmasították a modern fizika és technika világát. Kiemelkedő alakja volt a tudománynak Neumann János is, aki a modern számítógép működési elveit alapozta meg."
            },
            {
                "type": "narration",
                "text": "A magyar tudomány sikertörténete a legújabb korban is folytatódik. 2023-ban a világ figyelme ismét Magyarországra irányult, amikor két kiváló tudós is átvehette a legrangosabb svéd királyi elismerést."
            },
            {
                "type": "narration",
                "text": "Karikó Katalin biokémikus az mRNS-alapú vakcinák kifejlesztését lehetővé tevő áttörésért orvosi, Krausz Ferenc fizikus pedig az attofizikai kísérletekért fizikai Nobel-díjat kapott, büszkeséget hozva az egész nemzetnek."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek-01-tudomany.json", story_01)

    story_02 = {
        "id": "story.b1.nemzetiertekek.02",
        "title": "A magyar találmányok és újítók világa",
        "level": "B1",
        "lesson": 2,
        "order": 34,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Exploring legendary Hungarian inventions that shaped modern everyday life: Ányos Jedlik's dynamo, Ignác Semmelweis's antiseptic hygiene, László Bíró's ballpoint pen, and Ernő Rubik's world-famous cube.",
        "characters": [],
        "location": "Budapest",
        "grammar": ["Designation with the Essive-Modal Case: -ként and -ként tartják számon"],
        "vocabularyTopics": ["inventions", "innovators", "daily_life"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A mindennapi életben használt tárgyak és műszaki vívmányok között meglepően sok magyar származású találmány található. A magyar mérnökök és feltalálók találékonysága világszerte hírnevet szerzett az országnak."
            },
            {
                "type": "narration",
                "text": "Jedlik Ányos bencés szerzetes és természettudós már 1861-ben megalkotta a villamos dinamó elvét, megelőzve külföldi kortársait. Ugyancsak ő készített először szódavizet Magyarországon, megteremtve a fröccs kultúrájának alapját."
            },
            {
                "type": "narration",
                "text": "Semmelweis Ignác orvostanár a klórmeszes kézmosás kötelező bevezetésével drámaian csökkentette a gyermekágyi láz miatti halálozást. Felfedezésének köszönhetően az orvostörténelem „az anyák megmentőjeként” tiszteli őt."
            },
            {
                "type": "narration",
                "text": "A 20. században Bíró László újságíró megalkotta a golyóstollat, amely felváltotta a pacázó töltőtollakat. Sok országban ma is az ő nevéből képzett szóval – például angolul „biro” – nevezik ezt az íróeszközt."
            },
            {
                "type": "narration",
                "text": "Rubik Ernő 1974-ben alkotta meg a háromdimenziós mechanikus logikai játékot, a Bűvös Kockát. A Rubik-kocka azóta az emberi kreativitás és a matematikai gondolkodás univerzális szimbólumává vált a világ minden táján."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek-02-talalmanyok.json", story_02)

    story_03 = {
        "id": "story.b1.nemzetiertekek.03",
        "title": "A magyar zenei örökség: Liszttől Bartókig és Kodályig",
        "level": "B1",
        "lesson": 3,
        "order": 34,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The monumental legacy of Hungarian music: Ferenc Liszt's piano romanticism, the ethnomusicological revolution of Béla Bartók and Zoltán Kodály, and the global popularity of Hungarian operetta.",
        "characters": [],
        "location": "Zeneakadémia, Budapest",
        "grammar": ["Cultural Contribution Valencies: Hozzájárul, gyökerezik, megalapoz"],
        "vocabularyTopics": ["classical_music", "composers", "pedagogy"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar zeneművészet az európai kultúra egyik legerősebb tartóoszlopa. A 19. században Liszt Ferenc zeneszerző és zongoravirtuóz teremtette meg a modern pódiumművészetet, és Magyar Rapszódiáiban büszkén hirdette hazája zenei motívumait."
            },
            {
                "type": "narration",
                "text": "A 20. század elején Bartók Béla és Kodály Zoltán elindult a magyar falvakba, hogy fonográffal rögzítse az évszázados paraszti népdalkincset. Ez a kutatás nemcsak megmentette a nemzeti hagyományt, hanem új utat nyitott a modern komolyzenében."
            },
            {
                "type": "narration",
                "text": "Bartók zseniális művei, mint A kékszakállú herceg vára vagy a Zene húros hangszerekre, az egyetemes 20. századi zene legnagyobb remekművei közé tartoznak, ötvözve az ősi ritmust a legmagasabb szintű művészi szerkesztéssel."
            },
            {
                "type": "narration",
                "text": "Kodály Zoltán felismerte, hogy a zenei műveltség minden gyermek alapvető joga. Az általa kidolgozott zeneoktatási rendszer, a Kodály-módszer a tiszta éneklésre és a népdalokra épül, és ma Japántól Amerikáig tanítják."
            },
            {
                "type": "narration",
                "text": "A könnyedebb műfajokban a magyar operett ért el páratlan sikereket. Kálmán Imre és Lehár Ferenc dallamai, mint a Csárdáskirálynő vagy A víg özvegy, a világ leghíresebb színházaiban arattak és aratnak ma is fergeteges sikert."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek-03-zene.json", story_03)

    story_04 = {
        "id": "story.b1.nemzetiertekek.04",
        "title": "A magyar irodalom és képzőművészet panteonja",
        "level": "B1",
        "lesson": 4,
        "order": 34,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "A tribute to Hungary's literary and artistic pantheon: the national poetry of Petőfi, Arany, Ady, and József Attila, alongside the visionary canvases of Mihály Munkácsy and Tivadar Csontváry Kosztka.",
        "characters": [],
        "location": "Nemzeti Galéria és Petőfi Irodalmi Múzeum",
        "grammar": ["Canonical Influence & Superlatives: Kiemelkedő alakja, legjelentősebb"],
        "vocabularyTopics": ["literature", "fine_arts", "heritage"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar nemzet történetében az irodalom mindig több volt egyszerű művészetnél: a költők és írók a nemzet lelkiismereteként és vezetőiként léptek fel a sorsfordító pillanatokban."
            },
            {
                "type": "narration",
                "text": "Petőfi Sándor a szabadság és a szerelem lánglelkű dalnoka volt, míg Arany János a magyar nyelv verhetetlen mestereként teremtett örök értékeket epikus költeményeivel, balladájával és a Toldi-trilógiával."
            },
            {
                "type": "narration",
                "text": "A 20. század hajnalán a Nyugat folyóirat és Ady Endre modern költészete új távlatokat nyitott, míg József Attila a nagyvárosi ember magányát és a társadalmi igazságvágyat emelte megrázó költői magasságokba."
            },
            {
                "type": "narration",
                "text": "A képzőművészetben Munkácsy Mihály aratott világraszóló sikert monumentális festményeivel. A Krisztus-trilógia és a Golgota drámai realizmusa Párizstól Amerikáig elvarázsolta a műértő közönséget."
            },
            {
                "type": "narration",
                "text": "Mellette Csontváry Kosztka Tivadar különleges, misztikus színekkel megfestett látomásai – mint a Magányos cédrus – a magyar festészet egyedülálló, senki máshoz nem hasonlítható kincsei közé tartoznak."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek-04-irodalom.json", story_04)

    story_05 = {
        "id": "story.b1.nemzetiertekek.05",
        "title": "Hungarikumok, népi hagyományok és a világörökség",
        "level": "B1",
        "lesson": 5,
        "order": 34,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Exploring distinctive national treasures: official Hungarikums like Tokaji wine and Herend porcelain, folk traditions such as Matyó embroidery and the Mohács Busójárás, and UNESCO World Heritage landscapes.",
        "characters": [],
        "location": "Tokaj, Hollókő és Mohács",
        "grammar": ["Designating National Heritage: Hungarikummá nyilvánít, védelmet élvez"],
        "vocabularyTopics": ["hungarikum", "world_heritage", "folklore"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország külön törvénnyel védi és támogatja azokat a nemzeti értékeket, amelyek egyediségükkel, minőségükkel és jellegzetességükkel a magyarság csúcsteljesítményét képviselik: ezek a hungarikumok."
            },
            {
                "type": "narration",
                "text": "A gasztronómiai hungarikumok közül kiemelkedik a Tokaji aszú, a „királyok bora, a borok királya”, a kalocsai és szegedi fűszerpaprika, valamint az autentikus magyar gulyásleves és a bajai halászlé."
            },
            {
                "type": "narration",
                "text": "A kézműves remekművek világában a Herendi és Zsolnay porcelán képviseli a legmagasabb luxust és eleganciát. A herendi minták királyi udvarok étkezőasztalait díszítették Angliától Ausztriáig."
            },
            {
                "type": "narration",
                "text": "A népi kultúrában a kalocsai és matyó hímzés pompás virágmotívumai, valamint a mohácsi télbúcsúztató busójárás ijesztő maszkjai az UNESCO szellemi kulturális világörökségének elismert részei."
            },
            {
                "type": "narration",
                "text": "Magyarország természeti és épített öröksége is gazdag: a Hortobágy végtelen pusztája, a Fertő tó vidéke, Hollókő élő ófaluja és a budapesti Duna-part a Budai Várral mind a világörökség védelme alatt állnak, őrizve a nemzet büszkeségét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek-05-hungarikumok.json", story_05)

    story_combined = {
        "id": "story.b1.nemzetiertekek",
        "title": "A magyar kultúra, tudomány és nemzeti értékek öröksége",
        "level": "B1",
        "order": 34,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive compendium on Hungary's scientific, musical, literary, and folkloric heritage. From Nobel laureates and revolutionary inventions to classical masterpieces, UNESCO sites, and cherished Hungarikums.",
        "characters": [],
        "location": "Magyarország",
        "grammar": [
            "Scientific Discoveries & Passive Participles in -ott/-ett",
            "Designation with the Essive-Modal Case: -ként and -ként tartják számon",
            "Cultural Contribution Valencies: Hozzájárul, gyökerezik, megalapoz",
            "Canonical Influence & Superlatives: Kiemelkedő alakja, legjelentősebb",
            "Designating National Heritage: Hungarikummá nyilvánít, védelmet élvez"
        ],
        "vocabularyTopics": [
            "science",
            "inventions",
            "music",
            "literature",
            "hungarikum"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország szellemi és kulturális öröksége a nemzet legfőbb megtartó ereje. A Kárpát-medence népe az évszázadok során olyan tudományos és művészeti értékeket teremtett, amelyek mélyen beépültek az egyetemes emberi civilizációba."
            },
            {
                "type": "narration",
                "text": "A magyar tudomány kiválóságát Nobel-díjasok sora fémjelzi: Szent-Györgyi Albert paprikából kivont C-vitaminjától kezdve Neumann János számítógépes elvein át egészen Karikó Katalin és Krausz Ferenc 2023-as Nobel-díjáig."
            },
            {
                "type": "narration",
                "text": "A hétköznapi életet forradalmasító találmányok között ott találjuk Bíró László golyóstollát, Jedlik Ányos dinamóját, Semmelweis Ignác fertőtlenítő felismerését és Rubik Ernő zseniális Bűvös Kockáját."
            },
            {
                "type": "narration",
                "text": "A magyar zene Liszt Ferenc rapszódiáitól Bartók Béla modernitásán és Kodály Zoltán pedagógiáján át a bécsi operettszínpadokat meghódító Kálmán Imre dallamáig a világ minden hangversenytermében otthon van."
            },
            {
                "type": "narration",
                "text": "Az irodalom és képzőművészet terén Petőfi, Arany, Ady és József Attila versei, valamint Munkácsy Mihály és Csontváry Kosztka Tivadar remekművei formálják a nemzeti identitást és a hazaszeretetet."
            },
            {
                "type": "narration",
                "text": "Végül a hungarikumok törvénye védi a Tokaji aszút, a szegedi paprikát, a Herendi porcelánt, a mohácsi busójárást és Hollókő ófaluját. Ezek az értékek bizonyítják, hogy a magyar kultúra élő, gazdag és méltó az egész világ megbecsülésére."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiertekek.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-nemzetiertekek-01",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miről híres Szent-Györgyi Albert orvos és tudós?",
                "options": [
                    "A C-vitamin szegedi paprikából való kivonásáért orvosi Nobel-díjat kapott",
                    "A gőzgép feltalálásáért kapott kitüntetést",
                    "Az első magyar vasútvonal tervezője volt"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szent-Györgyit Nobel-díjjal tüntet_____ ki a kutatásaiért. (was awarded - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-nemzetiertekek-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Karikó", "Katalin", "Nobel-díjat", "kapott", "az", "mRNS", "kutatásáért."],
                "solution": ["Karikó", "Katalin", "Nobel-díjat", "kapott", "az", "mRNS", "kutatásáért."]
            },
            {
                "id": "b1-nemzetiertekek-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik évben kapott Nobel-díjat Karikó Katalin és Krausz Ferenc?",
                "options": [
                    "2023-ban",
                    "1990-ben",
                    "2010-ben"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A magyar tudósok számos fontos tudományos felfedezés_____ tettek. (discoveries - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetiertekek-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Ki dolgozta ki a modern digitális számítógépek működési alapelveit?",
                "options": [
                    "Neumann János",
                    "Gárdonyi Géza",
                    "Deák Ferenc"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "tudományos", "kutatás", "kiemelkedő", "áttörést", "hozott."],
                "solution": ["A", "tudományos", "kutatás", "kiemelkedő", "áttörést", "hozott."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-nemzetiertekek-02",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kit neveznek a világ orvostörténetében 'az anyák megmentőjének'?",
                "options": [
                    "Semmelweis Ignácot",
                    "Bíró Lászlót",
                    "Jedlik Ányost"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Semmelweiset a világ az anyák megmentője_____ tartja számon. (as - ként)",
                "answer": "ként"
            },
            {
                "id": "b1-nemzetiertekek-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bíró", "László", "találta", "fel", "a", "golyóstollat."],
                "solution": ["Bíró", "László", "találta", "fel", "a", "golyóstollat."]
            },
            {
                "id": "b1-nemzetiertekek-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki találta fel a világhírű Bűvös Kockát (Rubik-kockát)?",
                "options": [
                    "Rubik Ernő",
                    "Jedlik Ányos",
                    "Puskás Tivadar"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A dinamó elvét Jedlik Ányos természettudós talál_____ ki. (invented - ta)",
                "answer": "ta"
            },
            {
                "id": "b1-nemzetiertekek-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen higiéniai szabály bevezetésével mentett meg Semmelweis Ignác ezernyi életet?",
                "options": [
                    "A klóros vizes kézmosás kötelezővé tételével",
                    "A sebészeti maszkok elhagyásával",
                    "A kórházak fűtésének leállításával"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magyar", "találmányok", "meghódították", "az", "egész", "világot."],
                "solution": ["A", "magyar", "találmányok", "meghódították", "az", "egész", "világot."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-nemzetiertekek-03",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik híres magyar zeneszerző komponálta a Magyar Rapszódiákat?",
                "options": [
                    "Liszt Ferenc",
                    "Kálmán Imre",
                    "Erkel Ferenc"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bartók és Kodály művészete a népdalok kincsé_____ gyökerezik. (in - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-nemzetiertekek-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "Kodály-módszer", "hozzájárult", "a", "zeneoktatás", "megújulásához."],
                "solution": ["A", "Kodály-módszer", "hozzájárult", "a", "zeneoktatás", "megújulásához."]
            },
            {
                "id": "b1-nemzetiertekek-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen műfajban aratott világsikert Kálmán Imre (pl. Csárdáskirálynő)?",
                "options": [
                    "Operett",
                    "Egyházi kórusmű",
                    "Szimfónia"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Bartók Béla az ősi magyar népdalgyűjtés_____ végzett fonográffal. (collecting - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetiertekek-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Ki szerezte Magyarország nemzeti himnuszának (Kölcsey Ferenc szövege) zenéjét?",
                "options": [
                    "Erkel Ferenc",
                    "Liszt Ferenc",
                    "Bartók Béla"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magyar", "zeneművészet", "az", "egyetemes", "kultúra", "része."],
                "solution": ["A", "magyar", "zeneművészet", "az", "egyetemes", "kultúra", "része."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-nemzetiertekek-04",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik költőnk írta a Toldi-trilógiát és a Walesi bárdokat?",
                "options": [
                    "Arany János",
                    "Ady Endre",
                    "József Attila"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Petőfi a 19. század legkiemelkedő_____ költője volt. (most prominent - bb)",
                "answer": "bb"
            },
            {
                "id": "b1-nemzetiertekek-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Munkácsy", "Mihály", "festményei", "világhírű", "remekművek."],
                "solution": ["Munkácsy", "Mihály", "festményei", "világhírű", "remekművek."]
            },
            {
                "id": "b1-nemzetiertekek-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik festmény Csontváry Kosztka Tivadar egyik leghíresebb szimbolikus alkotása?",
                "options": [
                    "Magányos cédrus",
                    "Ásító inas",
                    "Lila ruhás nő"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A költők művei erősítik a nemzeti öntudat_____. (consciousness - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-nemzetiertekek-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik folyóirat indította el a modern magyar irodalom megújulását a 20. század elején?",
                "options": [
                    "Nyugat",
                    "Pesti Hírlap",
                    "Magyar Hírmondó"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-04.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "irodalmi", "örökség", "összeköti", "a", "nemzedékeket."],
                "solution": ["Az", "irodalmi", "örökség", "összeköti", "a", "nemzedékeket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-nemzetiertekek-05",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hungarikum' kifejezés?",
                "options": [
                    "A magyarság csúcsteljesítményét jelképező, hivatalosan elismert nemzeti érték",
                    "Minden Magyarországon gyártott importtermék",
                    "Egy speciális állami adófajta"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Tokaji aszút törvényben nyilvánították hungarikum_____. (into Hungarikum - má)",
                "answer": "má"
            },
            {
                "id": "b1-nemzetiertekek-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "mohácsi", "busójárás", "az", "UNESCO", "örökségének", "része."],
                "solution": ["A", "mohácsi", "busójárás", "az", "UNESCO", "örökségének", "része."]
            },
            {
                "id": "b1-nemzetiertekek-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik magyar falu őrzi élő skanzenként a palóc népi építészet világörökségét?",
                "options": [
                    "Hollókő",
                    "Tihany",
                    "Visegrád"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Herendi porcelán a magyar kézműves népművészet és iparművészet remekmű_____. (masterpiece - e)",
                "answer": "e"
            },
            {
                "id": "b1-nemzetiertekek-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan szokás nevezni a híres Tokaji aszút XIV. Lajos francia király mondása nyomán?",
                "options": [
                    "A királyok bora, a borok királya",
                    "A nemzet legédesebb itala",
                    "A puszta folyékony aranya"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hagyományőrzés", "fontos", "feladata", "a", "társadalomnak."],
                "solution": ["A", "hagyományőrzés", "fontos", "feladata", "a", "társadalomnak."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-nemzetiertekek-consolidation",
        "exercises": [
            {
                "id": "b1-nemzetiertekek-consolidation.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik magyar személyiség kapta meg a Nobel-díjat a C-vitamin kutatásáért?",
                "options": [
                    "Szent-Györgyi Albert",
                    "Neumann János",
                    "Rubik Ernő"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kutatókat a legmagasabb elismeréssel tüntet_____ ki. (were awarded - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Semmelweiset", "az", "anyák", "megmentőjeként", "tiszteli", "a", "világ."],
                "solution": ["Semmelweiset", "az", "anyák", "megmentőjeként", "tiszteli", "a", "világ."]
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik párosítás tartalmaz kizárólag hivatalosan elismert hungarikumokat?",
                "options": [
                    "Tokaji aszú, Herendi porcelán, mohácsi busójárás",
                    "Kávé, banán, narancslé",
                    "Televízió, mikrohullámú sütő, mosógép"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Bartók és Kodály munkássága a magyar zeneművészet alapköv_____. (cornerstone - e)",
                "answer": "e"
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik nemzeti parkunk képezi a végtelen alföldi puszta és a pásztorkultúra világörökségét?",
                "options": [
                    "Hortobágyi Nemzeti Park",
                    "Aggteleki Nemzeti Park",
                    "Bükki Nemzeti Park"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiertekek-consolidation.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nemzeti", "értékek", "megőrzése", "mindannyiunk", "közös", "kötelessége."],
                "solution": ["A", "nemzeti", "értékek", "megőrzése", "mindannyiunk", "közös", "kötelessége."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiertekek-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.nemzetiertekek-01",
        "unit": 34,
        "title": "A magyar tudomány csillagai és a Nobel-díjasok",
        "level": "B1",
        "grammar": "Scientific Discoveries & Passive Participles in -ott/-ett",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss famous Hungarian scientists and their Nobel Prize achievements.",
                    "I can form passive participial structures in -ott/-ett to narrate scientific honors.",
                    "I can master 6 vocabulary items for science, discovery, and breakthroughs.",
                    "I can read about Albert Szent-Györgyi, Katalin Karikó, and Ferenc Krausz."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-nemzetiertekek-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-nemzetiertekek-01-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek-01-tudomany.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-01-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-01.ex01",
                    "b1-nemzetiertekek-01.ex02",
                    "b1-nemzetiertekek-01.ex03",
                    "b1-nemzetiertekek-01.ex04",
                    "b1-nemzetiertekek-01.ex05",
                    "b1-nemzetiertekek-01.ex06",
                    "b1-nemzetiertekek-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.nemzetiertekek-02",
        "unit": 34,
        "title": "A magyar találmányok és újítók világa",
        "level": "B1",
        "grammar": "Designation with the Essive-Modal Case: -ként and -ként tartják számon",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can identify world-changing Hungarian inventions from the dynamo to the Rubik's cube.",
                    "I can use the essive suffix -ként to express roles and historic status.",
                    "I can learn 6 essential terms for inventions and innovators.",
                    "I can explain Semmelweis Ignác's lifesaving antiseptic discovery."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-nemzetiertekek-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-nemzetiertekek-02-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek-02-talalmanyok.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-02-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-02.ex01",
                    "b1-nemzetiertekek-02.ex02",
                    "b1-nemzetiertekek-02.ex03",
                    "b1-nemzetiertekek-02.ex04",
                    "b1-nemzetiertekek-02.ex05",
                    "b1-nemzetiertekek-02.ex06",
                    "b1-nemzetiertekek-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.nemzetiertekek-03",
        "unit": 34,
        "title": "A magyar zenei örökség: Liszttől Bartókig és Kodályig",
        "level": "B1",
        "grammar": "Cultural Contribution Valencies: Hozzájárul, gyökerezik, megalapoz",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the masterpieces of Liszt, Bartók, Kodály, and Hungarian operetta.",
                    "I can use verbal governors of contribution and cultural origin in Hungarian.",
                    "I can acquire 6 vocabulary words for musical heritage and pedagogy.",
                    "I can understand the worldwide impact of the Kodály music education method."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-nemzetiertekek-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-nemzetiertekek-03-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek-03-zene.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-03-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-03.ex01",
                    "b1-nemzetiertekek-03.ex02",
                    "b1-nemzetiertekek-03.ex03",
                    "b1-nemzetiertekek-03.ex04",
                    "b1-nemzetiertekek-03.ex05",
                    "b1-nemzetiertekek-03.ex06",
                    "b1-nemzetiertekek-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.nemzetiertekek-04",
        "unit": 34,
        "title": "A magyar irodalom és képzőművészet panteonja",
        "level": "B1",
        "grammar": "Canonical Influence & Superlatives: Kiemelkedő alakja, legjelentősebb",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss classical Hungarian poets (Petőfi, Arany, Ady, József Attila) and painters (Munkácsy, Csontváry).",
                    "I can formulate canonical descriptions using superlatives and genitive constructions.",
                    "I can acquire 6 key terms for literature, fine arts, and national identity.",
                    "I can appreciate how Hungarian literature shaped the national conscience."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-nemzetiertekek-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-nemzetiertekek-04-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek-04-irodalom.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-04-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-04.ex01",
                    "b1-nemzetiertekek-04.ex02",
                    "b1-nemzetiertekek-04.ex03",
                    "b1-nemzetiertekek-04.ex04",
                    "b1-nemzetiertekek-04.ex05",
                    "b1-nemzetiertekek-04.ex06",
                    "b1-nemzetiertekek-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.nemzetiertekek-05",
        "unit": 34,
        "title": "Hungarikumok, népi hagyományok és a világörökség",
        "level": "B1",
        "grammar": "Designating National Heritage: Hungarikummá nyilvánít, védelmet élvez",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe officially certified Hungarikums (Tokaji aszú, Herend porcelain) and folk traditions (Busójárás).",
                    "I can use the translative -vá/-vé to discuss legal designations of heritage.",
                    "I can master 6 vocabulary items for UNESCO heritage, crafts, and folklore.",
                    "I can explain Hungary's World Heritage sites including Hollókő and the Hortobágy."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-nemzetiertekek-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-nemzetiertekek-05-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek-05-hungarikumok.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-05-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-05.ex01",
                    "b1-nemzetiertekek-05.ex02",
                    "b1-nemzetiertekek-05.ex03",
                    "b1-nemzetiertekek-05.ex04",
                    "b1-nemzetiertekek-05.ex05",
                    "b1-nemzetiertekek-05.ex06",
                    "b1-nemzetiertekek-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.nemzetiertekek-consolidation",
        "unit": 34,
        "title": "A magyar nemzeti értékek és örökség (Consolidation)",
        "level": "B1",
        "grammar": "Comprehensive review of Hungarian culture, science, and national heritage",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Consolidate all 30 vocabulary items on Hungarian culture, science, inventions, and Hungarikums.",
                    "Review participial attributions, essive designations in -ként, and translative designations in -vá/-vé.",
                    "Read the full compendium on Hungary's cultural and scientific pantheon.",
                    "Demonstrate readiness for the Hungarian citizenship exam questions on national culture and science."
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-nemzetiertekek.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-nemzetiertekek-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiertekek-consolidation.ex01",
                    "b1-nemzetiertekek-consolidation.ex02",
                    "b1-nemzetiertekek-consolidation.ex03",
                    "b1-nemzetiertekek-consolidation.ex04",
                    "b1-nemzetiertekek-consolidation.ex05",
                    "b1-nemzetiertekek-consolidation.ex06",
                    "b1-nemzetiertekek-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiertekek-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_34_citizenship()
