#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 16: The 1848–49 Revolution (b1-forradalom)."""

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

def build_unit_16_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.forradalom.01",
        "lesson": "b1-forradalom-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Pilvax kávéház", "translation": "Pilvax coffee house (center of the youth)", "pos": "noun"},
            {"lemma": "márciusi ifjak", "translation": "Youth of March (reformist revolutionaries)", "pos": "noun"},
            {"lemma": "cenzúra", "translation": "censorship", "pos": "noun"},
            {"lemma": "sajtószabadság", "translation": "freedom of the press", "pos": "noun"},
            {"lemma": "Nemzeti Színház", "translation": "National Theatre", "pos": "noun"},
            {"lemma": "forradalmi hangulat", "translation": "revolutionary atmosphere", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-forradalom-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.forradalom.02",
        "lesson": "b1-forradalom-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Tizenkét Pont", "translation": "The Twelve Points (manifesto of demands)", "pos": "noun"},
            {"lemma": "felelős minisztérium", "translation": "responsible ministry / cabinet in Buda-Pest", "pos": "noun"},
            {"lemma": "jobbágyfelszabadítás", "translation": "emancipation of serfs", "pos": "noun"},
            {"lemma": "törvény előtti egyenlőség", "translation": "equality before the law", "pos": "noun"},
            {"lemma": "nemzetőrség", "translation": "National Guard (civilian militia)", "pos": "noun"},
            {"lemma": "politikai fogoly", "translation": "political prisoner", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-forradalom-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.forradalom.03",
        "lesson": "b1-forradalom-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Batthyány Lajos", "translation": "Count Lajos Batthyány (first prime minister)", "pos": "noun"},
            {"lemma": "áprilisi törvények", "translation": "April Laws (constitutional transformation)", "pos": "noun"},
            {"lemma": "Függetlenségi Nyilatkozat", "translation": "Declaration of Independence (1849)", "pos": "noun"},
            {"lemma": "debreceni Nagytemplom", "translation": "Great Reformed Church of Debrecen", "pos": "noun"},
            {"lemma": "trónfosztás", "translation": "dethronement of the Habsburg dynasty", "pos": "noun"},
            {"lemma": "kormányzó-elnök", "translation": "Governor-President (Kossuth's title)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-forradalom-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.forradalom.04",
        "lesson": "b1-forradalom-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "honvédsereg", "translation": "Hungarian revolutionary army (Honvéd)", "pos": "noun"},
            {"lemma": "Görgei Artúr", "translation": "General Artúr Görgei", "pos": "noun"},
            {"lemma": "tavaszi hadjárat", "translation": "Spring Campaign of 1849", "pos": "noun"},
            {"lemma": "orosz cári beavatkozás", "translation": "Tsarist Russian military intervention", "pos": "noun"},
            {"lemma": "Isaszegi csata", "translation": "Battle of Isaszeg", "pos": "noun"},
            {"lemma": "katonai túlerő", "translation": "military superiority, overwhelming numerical odds", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-forradalom-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.forradalom.05",
        "lesson": "b1-forradalom-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "világosi fegyverletétel", "translation": "surrender at Világos (August 13, 1849)", "pos": "noun"},
            {"lemma": "aradi tizenhárom vértanú", "translation": "13 Martyrs of Arad (executed generals)", "pos": "noun"},
            {"lemma": "nemzeti gyásznap", "translation": "national day of mourning (October 6)", "pos": "noun"},
            {"lemma": "Haynau rémuralma", "translation": "General Haynau's reign of terror", "pos": "noun"},
            {"lemma": "kivégzés", "translation": "execution", "pos": "noun"},
            {"lemma": "szabadságeszme", "translation": "ideal of liberty and constitutionalism", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-forradalom-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.forradalom.01.reported-speech-quoting",
        "title": "Quoting Speeches & Demands: azt követelték, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Reporting Declarations and Demands in 1848",
                "content": "When narrating political turning points, reporting verbs take subordinate clauses with the subjunctive: *A márciusi ifjak azt követelték, hogy töröljék el a cenzúrát.* Direct quotes often use *így kiáltott fel / ezt mondta*."
            },
            {
                "type": "examples",
                "title": "Quoting political demands",
                "items": [
                    {
                        "spanish": "Petőfi kijelentette, hogy a sajtószabadság a nemzet legelső joga.",
                        "english": "Petőfi declared that freedom of the press was the nation's foremost right."
                    },
                    {
                        "spanish": "A tömeg azt kiáltotta a nyomdánál, hogy nem engednek a cenzoroknak.",
                        "english": "The crowd shouted at the printing house that they would not yield to the censors."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-forradalom-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.forradalom.02.subjunctive-manifesto",
        "title": "Subjunctive of Demands in Manifestos: Kívánjuk, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Subjunctive in Official Demands (The 12 Points)",
                "content": "The famous 12 Points use the formula *Kívánjuk a sajtó szabadságát!* and third-person imperative/subjunctive forms: *Legyen béke, szabadság és egyetértés!* ('Let there be peace, liberty, and concord!')."
            },
            {
                "type": "examples",
                "title": "Demands with subjunctive",
                "items": [
                    {
                        "spanish": "Kívánjuk, hogy a törvény előtt minden polgár egyenlő legyen.",
                        "english": "We demand that every citizen be equal before the law."
                    },
                    {
                        "spanish": "Szabadítsák ki a politikai foglyokat a börtönből!",
                        "english": "Let the political prisoners be liberated from prison!"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-forradalom-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.forradalom.03.formal-declarations",
        "title": "Constitutional Proclamations: Kikiáltani, kimondani",
        "sections": [
            {
                "type": "text",
                "title": "Formal Language of Independence and Laws",
                "content": "Official acts use solemn verbs of statecraft: *kimondani a függetlenséget* ('to declare independence'), *trónfosztottnak nyilvánítani* ('to declare dethroned'), *életbe léptetni a törvényeket* ('to enact laws')."
            },
            {
                "type": "examples",
                "title": "Constitutional formulas",
                "items": [
                    {
                        "spanish": "1849 áprilisában az országgyűlés kimondta a Habsburg-ház trónfosztását.",
                        "english": "In April 1849 the parliament pronounced the dethronement of the House of Habsburg."
                    },
                    {
                        "spanish": "Batthyány Lajos kormánya megkezdte a modern polgári állam kiépítését.",
                        "english": "The government of Lajos Batthyány commenced building the modern civic state."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-forradalom-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.forradalom.04.military-narrative",
        "title": "Narrative Sequencing in Campaign Battles: miután, miközben",
        "sections": [
            {
                "type": "text",
                "title": "Sequencing Campaign Events",
                "content": "Describing battles and strategic movements connects clauses with *miután* ('after'), *miközben* ('while'), and *mielőtt* ('before'): *Miután a honvédek bevették a várat, a főváros felszabadult.*"
            },
            {
                "type": "examples",
                "title": "Battle narrative clauses",
                "items": [
                    {
                        "spanish": "Miközben a tavaszi hadjárat folyt, Görgei serege egymás után aratta a győzelmeket.",
                        "english": "While the Spring Campaign was underway, Görgei's army scored victory after victory."
                    },
                    {
                        "spanish": "Mielőtt az orosz cári hadsereg belépett volna, a honvédek visszaverték a császáriakat.",
                        "english": "Before the Tsarist Russian army entered, the Honvéd soldiers had repelled the imperial troops."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-forradalom-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.forradalom.05.commemorative-register",
        "title": "Commemorative & Memorial Register: emlékére, tiszteletére",
        "sections": [
            {
                "type": "text",
                "title": "Commemoration and National Mourning",
                "content": "Official citizenship topics regarding memorialization employ postpositional phrases: *valakinek az emlékére* ('in memory of'), *tiszteletére* ('in honor of'), *hajt fejet* ('bows head in respect')."
            },
            {
                "type": "examples",
                "title": "Memorial phrases in citizenship context",
                "items": [
                    {
                        "spanish": "Október hatodikán a nemzet fejet hajt az aradi tizenhárom vértanú emléke előtt.",
                        "english": "On October 6th the nation bows its head before the memory of the thirteen martyrs of Arad."
                    },
                    {
                        "spanish": "Bár a szabadságharcot leverték, a szabadságeszme örökre gyökeret vert a szívekben.",
                        "english": "Although the war of independence was suppressed, the ideal of liberty took root forever in hearts."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-forradalom-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Narrative Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.forradalom.01",
        "title": "Eső és forradalom Pesten",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "March 15, 1848 begins on a cold, pouring morning in Pest. Petőfi and the March Youth gather at the Pilvax coffee house, marching through wet cobblestone streets to Landerer's printing press to seize freedom of the press without shedding a drop of blood.",
        "characters": [
            "Petőfi Sándor",
            "Jókai Mór",
            "Vasvári Pál",
            "Landerer Lajos"
        ],
        "location": "Pest, Pilvax kávéház, Hatvani utca",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848. március 15-én reggel Pesten sűrű, hideg tavaszi eső esett. Aki csak tehette, behúzódott a meleg szobába, ám a Pilvax kávéház sarkában forrt a levegő."
            },
            {
                "type": "narration",
                "text": "A fiatal költő, Petőfi Sándor és barátai, a márciusi ifjak nem a kényelemmel törődtek: egész Európa forrongott, s ők tudták, eljött a cselekvés órája."
            },
            {
                "type": "dialogue",
                "speaker": "Petőfi Sándor",
                "text": "Barátaim! Bécsben kitört a forradalom, nem várhatunk tovább. Ma kivívjuk a magyar nép szabadságát!"
            },
            {
                "type": "narration",
                "text": "Kivonultak az utcára, s az egyetemek ifjúsága azonnal csatlakozott hozzájuk. Az esernyők alatt hömpölygő tömeg egyenesen Landerer és Heckenast nyomdájához vonult, mert a legelső cél a cenzúra eltörlése és a sajtószabadság volt."
            },
            {
                "type": "dialogue",
                "speaker": "Jókai Mór",
                "text": "A nép nevében lefoglaljuk a gépeket! Cenzori engedély nélkül nyomtatjuk ki a Nemzeti dalt és a Tizenkét Pontot!"
            },
            {
                "type": "narration",
                "text": "A nyomdagépek kattogva munkához láttak. Délutánra a Nemzeti Színház előtt tízezrek ünnepeltek: vér nélkül, tiszta lélekkel győzött a pesti forradalmi hangulat."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom-01-marcius15.json", story_01)

    story_02 = {
        "id": "story.b1.forradalom.02",
        "title": "Mit kíván a magyar nemzet?",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On the afternoon of March 15, thousands gather outside the National Museum in the rain. Vasvári and Jókai read out the Twelve Points: an independent ministry, emancipation of the serfs, equality before the law, and the release of political prisoner Táncsics.",
        "characters": [
            "Petőfi Sándor",
            "Jókai Mór",
            "Vasvári Pál",
            "Táncsics Mihály"
        ],
        "location": "Pest, Nemzeti Múzeum, Budai Vár",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Délután a Nemzeti Múzeum előtti hatalmas tér megtelt emberekkel. Diákok, polgárok, kézművesek és parasztok álltak vállvetve a szűnni nem akaró márciusi záporban."
            },
            {
                "type": "narration",
                "text": "A múzeum lépcsőjén Vasvári Pál és Jókai Mór felolvasta a történelmi Tizenkét Pontot, amely megfogalmazta, mit kíván a magyar nemzet."
            },
            {
                "type": "dialogue",
                "speaker": "Jókai Mór",
                "text": "Kívánjuk a sajtó szabadságát, felelős minisztériumot Buda-Pesten, törvény előtti egyenlőséget és a jobbágyfelszabadítást!"
            },
            {
                "type": "narration",
                "text": "Minden egyes pontot ujjongó éljenzés kísért. A nép követelte a közös teherviselést és egy önálló nemzetőrség azonnali felállítását is."
            },
            {
                "type": "narration",
                "text": "Később a tömeg átkelt a hajóhídon Budára, a helytartótanács elé. A rémült császári tisztviselők minden követelést aláírtak, s a börtönből kiszabadult a bátor politikai fogoly, Táncsics Mihály."
            },
            {
                "type": "dialogue",
                "speaker": "Vasvári Pál",
                "text": "Ma megszületett a szabad Magyarország! Egyetlen puskalövés nélkül hajtottuk végre a nemzet akaratát!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom-02-tizenketpont.json", story_02)

    story_03 = {
        "id": "story.b1.forradalom.03",
        "title": "A törvényes forradalom és a függetlenség",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Batthyány forms Hungary's first responsible government, and the April Laws transform the kingdom into a modern civic state. But when the Habsburg court attacks, the parliament retreats to Debrecen, where Kossuth proclaims full independence in the Great Church.",
        "characters": [
            "Batthyány Lajos",
            "Kossuth Lajos",
            "V. Ferdinánd király"
        ],
        "location": "Pozsony, Pest, Debreceni Nagytemplom",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848 áprilisában V. Ferdinánd király kénytelen volt szentesíteni a korszakalkotó áprilisi törvényeket. Gróf Batthyány Lajos vezetésével megalakult az első felelős magyar kormány."
            },
            {
                "type": "narration",
                "text": "Magyarország néhány hét alatt modern polgári állammá vált: megszűnt a nemesi adómentesség, a jobbágyok földbirtokos polgárokká lettek."
            },
            {
                "type": "dialogue",
                "speaker": "Batthyány Lajos",
                "text": "A törvény szent és sérthetetlen. A nemzet békésen átlépett a modern alkotmányosság korszakába."
            },
            {
                "type": "narration",
                "text": "Ám a bécsi udvar hamarosan fegyverrel támadt Magyarországra. 1849 telén a kormány és az országgyűlés a hófúvásos alföldi központba, Debrecenbe menekült."
            },
            {
                "type": "narration",
                "text": "1849. április 14-én a debreceni Nagytemplomban Kossuth Lajos felolvasta a Függetlenségi Nyilatkozatot. A gyűlés egyhangúlag kimondta a Habsburg-ház trónfosztását."
            },
            {
                "type": "dialogue",
                "speaker": "Kossuth Lajos",
                "text": "Magyarország független, önálló európai állam! Nem ismerünk el zsarnokot a hazánk felett!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom-03-fuggetlenseg.json", story_03)

    story_04 = {
        "id": "story.b1.forradalom.04",
        "title": "A tavaszi hadjárat csodája",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The young Honvéd army, led by the brilliant Artúr Görgei, performs miracles during the Spring Campaign of 1849. At Hatvan, Tápióbicske, and Isaszeg, the Hungarian forces smash the imperial armies and retake Buda, terrifying Vienna.",
        "characters": [
            "Görgei Artúr",
            "Klapka György",
            "Damjanich János",
            "Kossuth Lajos"
        ],
        "location": "Isaszeg, Vác, Buda vára",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1849 tavaszán a semmiből felállított ifjú honvédsereg csodát tett a hadszíntéren. A katonák egyszerű szűrben és atillában, de lángoló hazaszeretettel harcoltak."
            },
            {
                "type": "narration",
                "text": "A hadsereg élén a szigorú, zseniális tábornok, Görgei Artúr állt, aki elképesztő stratégiai érzékkel irányította a tavaszi hadjárat hadmozdulatait."
            },
            {
                "type": "dialogue",
                "speaker": "Görgei Artúr",
                "text": "Előre, fiúk! A cél nem csupán a csata megnyerése, hanem hazánk szent földjének teljes felszabadítása!"
            },
            {
                "type": "narration",
                "text": "Az Isaszegi csata véres délutánján a honvédek megállíthatatlan rohammal törték át a császári vonalakat. A győzelem hírére Bécsben megkondultak a vészharangok."
            },
            {
                "type": "narration",
                "text": "Május 21-én a honvédek hősies ostrommal visszafoglalták Buda várát. Ferenc József császár belátta, hogy egyedül képtelen legyőzni a magyar szabadságharcot, s a cárhoz fordult segítségért."
            },
            {
                "type": "dialogue",
                "speaker": "Damjanich János",
                "text": "Amíg egyetlen honvéd él e földön, a zászlót magasra tartjuk! De a cári seregek érkezése új, kíméletlen próbatétel elé állít minket."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom-04-szabadsagharc.json", story_04)

    story_05 = {
        "id": "story.b1.forradalom.05",
        "title": "Világos és az aradi vértanúk öröksége",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Faced with overwhelming Austrian and Russian forces, Görgei lays down arms at Világos before the Russian general. The brutal Austrian retribution executes Batthyány and the Thirteen Martyrs at Arad, turning their sacrifice into the eternal cornerstone of Hungarian liberty.",
        "characters": [
            "Görgei Artúr",
            "Haynau tábornok",
            "Batthyány Lajos",
            "Aulich Lajos"
        ],
        "location": "Világos, Arad, Pest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1849 augusztusában Magyarország reménytelen helyzetbe került: a kétszázezer fős orosz cári beavatkozás és a császári csapatok hatalmas katonai túlerővel zárták körül a hazát."
            },
            {
                "type": "narration",
                "text": "Görgei Artúr, hogy megkímélje a seregét a felesleges vérontástól, augusztus 13-án a világosi fegyverletétel mellett döntött: fegyvereit az orosz Rüdiger tábornok előtt tette le."
            },
            {
                "type": "dialogue",
                "speaker": "Görgei Artúr",
                "text": "A túlerő legyőzött minket, de becsületünket nem vehetik el. A nemzet élni akar, és élni is fog."
            },
            {
                "type": "narration",
                "text": "A győzelmet könyörtelen bosszú követte: Haynau rémuralma véres ítéletekkel sújtotta a honvédeket. 1849. október 6-án Pesten kivégezték Batthyány Lajos miniszterelnököt."
            },
            {
                "type": "narration",
                "text": "Ugyanezen a hajnalon Aradon golyó és kötél általi kivégzés várta a honvédsereg legkiválóbb vezetőit, az aradi tizenhárom vértanút. Október hatodika azóta a nemzeti gyásznap."
            },
            {
                "type": "dialogue",
                "speaker": "Aulich Lajos",
                "text": "Szolgáltam a hazát hűséggel mindhalálig. A szabadságeszme, amiért meghalunk, soha nem vész el!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom-05-vilagos.json", story_05)

    # Combined Story for Library
    story_combined = {
        "id": "story.b1.forradalom",
        "title": "Az 1848–49-es forradalom és szabadságharc",
        "level": "B1",
        "order": 16,
        "type": "world",
        "estimatedMinutes": 9,
        "summary": "The epic story of 1848–49: from the rainy morning at Pilvax and the Twelve Points, through the April Laws and Kossuth's proclamation in Debrecen, to the glorious Spring Campaign and the tragic sacrifice of the Arad Martyrs.",
        "characters": [
            "Petőfi Sándor",
            "Kossuth Lajos",
            "Batthyány Lajos",
            "Görgei Artúr"
        ],
        "location": "Pest, Pozsony, Debrecen, Isaszeg, Arad",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848. március 15-én esős reggelen indult el a magyar nép szabadságharca: a Pilvax kávéházból induló márciusi ifjak vér nélkül kivívták a sajtószabadságot."
            },
            {
                "type": "narration",
                "text": "A Nemzeti Múzeum lépcsőjén felolvasott Tizenkét Pont követelte a jobbágyfelszabadítást, a törvény előtti egyenlőséget és a felelős magyar minisztériumot."
            },
            {
                "type": "narration",
                "text": "Az áprilisi törvények megteremtették a modern polgári államot Batthyány Lajos vezetésével, ám a bécsi udvar fegyverrel rontott az országra."
            },
            {
                "type": "narration",
                "text": "Debrecenben Kossuth kikiáltotta a függetlenséget, miközben Görgei honvédserege a tavaszi hadjáratban visszafoglalta Budát."
            },
            {
                "type": "narration",
                "text": "Bár a cári orosz beavatkozás és a világosi fegyverletétel leverte a küzdelmet, az aradi tizenhárom vértanú áldozata a magyar nemzet szabadságeszméjének örök jelképévé vált."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-forradalom.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-forradalom-{padded}",
            "exercises": [
                {
                    "id": f"b1-forradalom-{padded}.ex01",
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
                    "id": f"b1-forradalom-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Hogyan fogalmazzuk meg helyesen a forradalmi követelést? (Lesson {i})",
                    "options": [
                        "Kívánjuk, hogy a cenzúrát azonnal töröljék el és legyen sajtószabadság.",
                        "Kívánjuk cenzúrát törölni volt és lenni sajtószabadság.",
                        "Kívánunk sajtószabadságot lenni hogy törölte cenzúra."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-forradalom-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A forradalom legfontosabb eszméje a nemzeti függetlenség és a polgári _____ volt. (freedom / szabadság)",
                    "answer": "szabadság"
                },
                {
                    "id": f"b1-forradalom-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A tömeg azt követelte, ____ engedjék szabadon a politikai foglyokat. (that)",
                    "answer": "hogy"
                },
                {
                    "id": f"b1-forradalom-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Kik voltak a márciusi ifjak?",
                    "options": [
                        "A Pilvax kávéházban gyülekező radikális reformpárti fiatal értelmiségiek és diákok.",
                        "Császári tisztek, akik betiltották a magyar nyelvű könyveket.",
                        "Bécsi kereskedők, akik fegyvereket adtak el a cári hadseregnek."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-forradalom-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Miután elfoglalták a nyomdát, a forradalmárok cenzori engedély ____ nyomtatták ki a kiáltványt. (without)",
                    "answer": "nélkül"
                },
                {
                    "id": f"b1-forradalom-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "magyar", "nemzet", "szabad", "és", "független", "európai", "államként", "akar", "élni."],
                    "solution": ["A", "magyar", "nemzet", "szabad", "és", "független", "európai", "államként", "akar", "élni."]
                },
                {
                    "id": f"b1-forradalom-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért fontos téma 1848 a magyar állampolgársági interjún?",
                    "options": [
                        "Mert március 15. a modern polgári Magyarország és a nemzeti szabadság születésnapja.",
                        "Mert ekkor nyert először olimpiai aranyérmet a magyar válogatott.",
                        "Mert ekkor vezették be a forintot a korona helyett."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-forradalom-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-forradalom-consolidation",
        "exercises": [
            {
                "id": "b1-forradalom-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["márciusi ifjak", "Youth of March"],
                    ["Tizenkét Pont", "The Twelve Points"],
                    ["jobbágyfelszabadítás", "emancipation of serfs"],
                    ["aradi tizenhárom vértanú", "13 Martyrs of Arad"]
                ]
            },
            {
                "id": "b1-forradalom-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás foglalja össze helyesen 1848–49 történelmi jelentőségét?",
                "options": [
                    "Bár a cári túlerő leverte a szabadságharcot, a polgári átalakulás vívmányai visszafordíthatatlanok maradtak.",
                    "A forradalom miatt Magyarország teljesen megszűnt létezni mint önálló európai nemzet.",
                    "A harcokban senki sem vett részt, mert a király azonnal elfogadta az összes pontot."
                ],
                "correct": 0
            },
            {
                "id": "b1-forradalom-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Október 6. Magyarországon hivatalos nemzeti ____ nap. (mourning)",
                "answer": "gyász"
            },
            {
                "id": "b1-forradalom-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kossuth kijelentette, hogy a nemzet nem enged a ____ jogaiból. (constitutional)",
                "answer": "alkotmányos"
            },
            {
                "id": "b1-forradalom-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tizenhárom", "aradi", "vértanú", "hősies", "áldozata", "örökre", "a", "nemzet", "szívében", "él."],
                "solution": ["A", "tizenhárom", "aradi", "vértanú", "hősies", "áldozata", "örökre", "a", "nemzet", "szívében", "él."]
            },
            {
                "id": "b1-forradalom-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki volt Magyarország első alkotmányos miniszterelnöke 1848-ban?",
                "options": [
                    "Gróf Batthyány Lajos",
                    "Görgei Artúr",
                    "Haynau tábornok"
                ],
                "correct": 0
            },
            {
                "id": "b1-forradalom-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A március 15-i forradalom híres jelszava: Legyen béke, szabadság és ____! (concord / agreement)",
                "answer": "egyetértés"
            },
            {
                "id": "b1-forradalom-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik dokumentumot fogadta el az országgyűlés 1849 áprilisában Debrecenben?",
                "options": [
                    "A Függetlenségi Nyilatkozatot, kimondva a Habsburg-ház trónfosztását.",
                    "A bécsi békét és a feltétel nélküli megadást.",
                    "Az Európai Unióhoz való csatlakozási szerződést."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-forradalom-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("1848. március 15.", "March 15, 1848"),
        "02": ("A Tizenkét Pont", "The Twelve Points"),
        "03": ("A függetlenség kimondása", "Declaring Independence"),
        "04": ("A szabadságharc és a tavaszi hadjárat", "The War of Independence"),
        "05": ("A világosi fegyverletétel és a vértanúk", "Defeat at Világos & The Martyrs")
    }

    story_refs = {
        "01": "stories/world/b1/b1-forradalom-01-marcius15.json",
        "02": "stories/world/b1/b1-forradalom-02-tizenketpont.json",
        "03": "stories/world/b1/b1-forradalom-03-fuggetlenseg.json",
        "04": "stories/world/b1/b1-forradalom-04-szabadsagharc.json",
        "05": "stories/world/b1/b1-forradalom-05-vilagos.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.forradalom-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Political Declarations, Subjunctive Demands & 1848 Narrative Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events and figures of {en_t}.",
                        "I can quote political demands and understand subjunctive forms in manifestos.",
                        "I can master essential history topics tested in the Hungarian citizenship interview.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-forradalom-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-forradalom-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-forradalom-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-forradalom-{padded}.ex01",
                        f"b1-forradalom-{padded}.ex02",
                        f"b1-forradalom-{padded}.ex03",
                        f"b1-forradalom-{padded}.ex04",
                        f"b1-forradalom-{padded}.ex05",
                        f"b1-forradalom-{padded}.ex06",
                        f"b1-forradalom-{padded}.ex07",
                        f"b1-forradalom-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-forradalom-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.forradalom-consolidation",
        "title": "Összefoglalás: Az 1848–49-es forradalom (The 1848–49 Revolution Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of 1848–49 Revolutionary History & Citizenship Concepts",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-forradalom.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-forradalom-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-forradalom-consolidation.ex01",
                    "b1-forradalom-consolidation.ex02",
                    "b1-forradalom-consolidation.ex03",
                    "b1-forradalom-consolidation.ex04",
                    "b1-forradalom-consolidation.ex05",
                    "b1-forradalom-consolidation.ex06",
                    "b1-forradalom-consolidation.ex07",
                    "b1-forradalom-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-forradalom-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 16 (b1-forradalom)!")

if __name__ == "__main__":
    build_unit_16_citizenship()
