#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 17: Kossuth, Petőfi & the National Cause (b1-nemzetiugy)."""

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

def build_unit_17_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.nemzetiugy.01",
        "lesson": "b1-nemzetiugy-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "emigráció", "translation": "political exile, emigration", "pos": "noun"},
            {"lemma": "szónoki tehetség", "translation": "oratorical talent, eloquence", "pos": "noun"},
            {"lemma": "amerikai körút", "translation": "American tour (Kossuth's 1851-52 journey)", "pos": "noun"},
            {"lemma": "Kossuth-bankó", "translation": "Kossuth banknote (revolutionary currency)", "pos": "noun"},
            {"lemma": "nemzetközi elismertség", "translation": "international recognition", "pos": "noun"},
            {"lemma": "Duna-konföderáció", "translation": "Danubian Confederation plan", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiugy-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.nemzetiugy.02",
        "lesson": "b1-nemzetiugy-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nemzet költője", "translation": "poet of the nation (Petőfi's epithet)", "pos": "noun"},
            {"lemma": "lánglelkű", "translation": "fiery-souled, passionate", "pos": "adjective"},
            {"lemma": "Segesvári csata", "translation": "Battle of Segesvár (1849)", "pos": "noun"},
            {"lemma": "hazaszeretet", "translation": "patriotism, love of homeland", "pos": "noun"},
            {"lemma": "forradalmi költészet", "translation": "revolutionary poetry", "pos": "noun"},
            {"lemma": "hősi halál", "translation": "heroic death on the battlefield", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiugy-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.nemzetiugy.03",
        "lesson": "b1-nemzetiugy-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nemzeti dal", "translation": "National Song (Petőfi's rallying poem)", "pos": "noun"},
            {"lemma": "Talpra magyar", "translation": "'Rise, Magyar!' (opening imperative call)", "pos": "noun"},
            {"lemma": "rab vagy szabad", "translation": "slave or free (the core dilemma)", "pos": "noun"},
            {"lemma": "eskü", "translation": "solemn oath, pledge", "pos": "noun"},
            {"lemma": "nemzeti fogadalom", "translation": "national vow / pledge", "pos": "noun"},
            {"lemma": "költői felhívás", "translation": "poetic appeal, stirring call", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiugy-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.nemzetiugy.04",
        "lesson": "b1-nemzetiugy-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kokárda", "translation": "cockade (ribbon rosette worn on March 15)", "pos": "noun"},
            {"lemma": "nemzeti trikolór", "translation": "national tricolor flag (red-white-green)", "pos": "noun"},
            {"lemma": "piros-fehér-zöld", "translation": "red-white-green", "pos": "adjective"},
            {"lemma": "nemzeti címer", "translation": "national coat of arms", "pos": "noun"},
            {"lemma": "Kossuth-címer", "translation": "Kossuth coat of arms (without the royal crown)", "pos": "noun"},
            {"lemma": "nemzeti jelkép", "translation": "national symbol", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiugy-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.nemzetiugy.05",
        "lesson": "b1-nemzetiugy-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nemzeti ünnep", "translation": "national holiday", "pos": "noun"},
            {"lemma": "megemlékezés", "translation": "commemoration, remembrance ceremony", "pos": "noun"},
            {"lemma": "koszorúzás", "translation": "wreath-laying ceremony", "pos": "noun"},
            {"lemma": "ünnepi műsor", "translation": "festive program, ceremonial event", "pos": "noun"},
            {"lemma": "állampolgári eskü", "translation": "citizenship oath", "pos": "noun"},
            {"lemma": "történelmi örökség", "translation": "historical heritage", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiugy-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.nemzetiugy.01.participle-actions",
        "title": "Adverbial Participle -va/-ve in Historical Descriptions",
        "sections": [
            {
                "type": "text",
                "title": "Simultaneous and Manner Actions with -va/-ve",
                "content": "To describe figures acting while moving: *Kossuth városról városra utazva szónokolt a szabadságról.* ('Kossuth, travelling from city to city, spoke about freedom.'). The suffix *-va / -ve* creates vivid narration."
            },
            {
                "type": "examples",
                "title": "Historical descriptions with -va/-ve",
                "items": [
                    {
                        "spanish": "Kossuth Angliában és Amerikában szónokolva hódította meg a közönséget.",
                        "english": "Speaking across England and America, Kossuth conquered audiences."
                    },
                    {
                        "spanish": "A nemzet határait elhagyva sem mondott le soha a hazájáról.",
                        "english": "Even having left the borders of the nation, he never abandoned his homeland."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiugy-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.nemzetiugy.02.dedication-purpose",
        "title": "Expressing Devotion: életét áldozta azért, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Purpose and Sacrifice in National Biographies",
                "content": "Discussing national heroes combines *áldoz* ('sacrifices') or *küzd* ('struggles') with purpose clauses: *Petőfi életét áldozta azért, hogy Magyarország szabad legyen.*"
            },
            {
                "type": "examples",
                "title": "Expressing sacrifice and dedication",
                "items": [
                    {
                        "spanish": "A költő mindvégig azért harcolt, hogy a nép felszabaduljon a szolgaságból.",
                        "english": "The poet fought to the very end so that the people would be liberated from bondage."
                    },
                    {
                        "spanish": "Lánglelkű verseivel lelkesítette a honvédeket a harctéren.",
                        "english": "With his fiery-souled poems he inspired the Honvéd soldiers on the battlefield."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiugy-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.nemzetiugy.03.rhetorical-imperative",
        "title": "Rhetorical Imperative: Talpra magyar! Esküszünk...",
        "sections": [
            {
                "type": "text",
                "title": "Poetic Invocations and Collective Vows",
                "content": "Petőfi's *Nemzeti dal* uses imperative directives (*Talpra magyar!*, *Rabok legyünk vagy szabadok?*) followed by the collective oath formula: *Esküszünk, hogy rabok tovább nem leszünk!*"
            },
            {
                "type": "examples",
                "title": "Rhetorical vows in Hungarian culture",
                "items": [
                    {
                        "spanish": "A költemény felhívása egy egész nemzetet ébresztett fel álmából.",
                        "english": "The poem's appeal awakened an entire nation from its slumber."
                    },
                    {
                        "spanish": "Az eskü szavai máig minden magyar szívében visszhangoznak március idusán.",
                        "english": "The words of the oath still echo in every Hungarian heart on the ides of March."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiugy-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.nemzetiugy.04.symbolic-attributive",
        "title": "Describing National Symbols: A piros az erőt, a fehér a hűséget...",
        "sections": [
            {
                "type": "text",
                "title": "The Meaning of National Colors and Emblems",
                "content": "In Hungarian citizenship interviews, candidates explain national symbols: *A piros az erőt (vagy a vért), a fehér a hűséget (vagy a békét), a zöld a reményt jelképezi.* Notice the verb *jelképez* ('symbolizes')."
            },
            {
                "type": "examples",
                "title": "Explaining national symbols",
                "items": [
                    {
                        "spanish": "A kokárda a forradalom és a nemzeti összetartozás legszebb jelképe.",
                        "english": "The cockade is the finest symbol of the revolution and national cohesion."
                    },
                    {
                        "spanish": "A nemzeti trikolór három színe mély történelmi jelentést hordoz.",
                        "english": "The three colors of the national tricolor carry deep historical meaning."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiugy-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.nemzetiugy.05.ceremonial-citizenship",
        "title": "Ceremonial Register for Citizenship: esküt tesz, tiszteletet ad",
        "sections": [
            {
                "type": "text",
                "title": "Solemn State Ceremonies and Naturalization",
                "content": "Official citizenship procedures employ ceremonial verb-noun phrases: *állampolgársági esküt tesz* ('takes the citizenship oath'), *tisztelettel emlékezik* ('remembers with respect'), *fejet hajt az elődök előtt* ('bows head before predecessors')."
            },
            {
                "type": "examples",
                "title": "Ceremonial citizenship phrases",
                "items": [
                    {
                        "spanish": "Az állampolgársági vizsgán a jelölt számot ad a magyar történelem és kultúra ismeretéről.",
                        "english": "In the citizenship exam the applicant demonstrates knowledge of Hungarian history and culture."
                    },
                    {
                        "spanish": "Március 15-én országszerte koszorúzásokat és ünnepi műsorokat tartanak.",
                        "english": "On March 15th wreath-laying ceremonies and festive programs are held nationwide."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiugy-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Narrative Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.nemzetiugy.01",
        "title": "Kossuth Lajos Amerikában és a világban",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "After the defeat of 1849, Kossuth escapes to the Ottoman Empire and embarks on a historic tour across Great Britain and America. Speaking in rich, Shakespearean English, his oratorical brilliance enchants hundreds of thousands, turning him into a global champion of liberty.",
        "characters": [
            "Kossuth Lajos",
            "Amerikai elnök",
            "Hallgatóság"
        ],
        "location": "New York, Washington, London",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1851 telén egy gőzhajó futott be New York kikötőjébe. A fedélzeten egy fekete bársonykabátos, szakállas férfi állt: Kossuth Lajos, a magyar forradalom száműzött vezetője."
            },
            {
                "type": "narration",
                "text": "Az amerikaiak megőrültek érte: százezrek vonultak az utcára, hogy megpillantsák a férfit, aki szembeszállt a Habsburgok és a cár birodalmával. Az emigráció nem törte meg a lelkét."
            },
            {
                "type": "dialogue",
                "speaker": "Kossuth Lajos",
                "text": "Nem kéregetni jöttem hozzátok, hanem a szabadság szent ügyéért szólni, amely összeköti a világ minden becsületes emberét!"
            },
            {
                "type": "narration",
                "text": "Kossuth zseniális szónoki tehetség birtokában volt. Tiszta, veretes angolsággal beszélt, amelyet börtönévei alatt Shakespeare műveiből tanult meg."
            },
            {
                "type": "narration",
                "text": "Az amerikai körút során az elnök és a kongresszus is fogadta. Kossuth-bankó gyűjtések indultak, és városokat neveztek el róla Amerikában."
            },
            {
                "type": "dialogue",
                "speaker": "Kossuth Lajos",
                "text": "A magyar szabadságharc lángja nem aludt ki. Amíg él egyetlen magyar, a nemzetközi elismertség és a függetlenség reménye velünk marad!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy-01-kossuthemigracio.json", story_01)

    story_02 = {
        "id": "story.b1.nemzetiugy.02",
        "title": "Petőfi Sándor, a lánglelkű költő",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Petőfi Sándor lived like a comet: passionate, uncompromising, and dedicated to the people. He wrote masterpieces on rickety tavern tables and insisted on riding to the frontline in Transylvania under General Bem, meeting a mysterious heroic death at Segesvár.",
        "characters": [
            "Petőfi Sándor",
            "Bem József tábornok",
            "Szendrey Júlia"
        ],
        "location": "Pest, Kolozsvár, Segesvár",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Petőfi Sándor olyan volt, mint egy üstökös: mindössze huszonhat évet élt ezen a földön, de egész Magyarországot lángra lobbantotta költészetével."
            },
            {
                "type": "narration",
                "text": "A lánglelkű költő soha nem alkudott meg. Nem kastélyokban élt, hanem az egyszerű emberek között: a forradalmi költészet számára nem játék volt, hanem szent hivatás."
            },
            {
                "type": "dialogue",
                "speaker": "Petőfi Sándor",
                "text": "Ha a nemzet fegyvert fogott a szabadságért, a költőnek nem a szobában, hanem a csatamezőn van a helye!"
            },
            {
                "type": "narration",
                "text": "Amikor a cári hadsereg betört Erdélybe, Petőfi feleségét és újszülött fiát hátrahagyva azonnal a lengyel szabadsághős, Bem József tábornok seregébe sietett."
            },
            {
                "type": "narration",
                "text": "1849. július 31-én a véres Segesvári csata sűrűjében látták őt utoljára, kard nélkül, fehér ingben futva a lovasok előtt. Testét soha nem találták meg."
            },
            {
                "type": "dialogue",
                "speaker": "Bem tábornok",
                "text": "Petőfi fiam, vigyázz magadra, mert te vagy a magyar nemzet legszebb dalos madara! De a sors könyvébe hősi halál volt megírva."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy-02-petofikolto.json", story_02)

    story_03 = {
        "id": "story.b1.nemzetiugy.03",
        "title": "A Nemzeti dal születése és hatalma",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How Petőfi wrote the immortal 'Nemzeti dal' just days before March 15. The thunderous opening line 'Talpra magyar, hí a haza!' and the collective oath 'Esküszünk, esküszünk!' became the battle-cry of a whole nation that echoes across Hungarian history.",
        "characters": [
            "Petőfi Sándor",
            "Jókai Mór",
            "A pesti nép"
        ],
        "location": "Pest, Pilvax kávéház, Landerer nyomda",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848 márciusának elején Petőfi egy kis füzetbe firkantotta a sorokat, amelyek örökre meghatározták a magyar nemzeti önazonosságot."
            },
            {
                "type": "dialogue",
                "speaker": "Petőfi Sándor",
                "text": "Talpra magyar, hí a haza! Itt az idő, most vagy soha! Rabok legyünk vagy szabadok? Ez a kérdés, válasszatok!"
            },
            {
                "type": "narration",
                "text": "A költemény nem bonyolult elmélet volt, hanem szívdobbanás. Amikor március 15-én délelőtt a nyomda előtt felolvasta, a tömeg dermedten figyelt, majd egyszerre zúgott fel a válasz."
            },
            {
                "type": "dialogue",
                "speaker": "A pesti nép",
                "text": "A magyarok Istenére esküszünk, esküszünk, hogy rabok tovább nem leszünk!"
            },
            {
                "type": "narration",
                "text": "Ez a nemzeti fogadalom erősebbnek bizonyult minden császári rendeletnél. A Nemzeti dal pillanatok alatt tízezer példányban terjedt el az utcákon."
            },
            {
                "type": "narration",
                "text": "A vers felhívása máig a szabadságvágy legfőbb kifejezése: minden március 15-i ünnepségen diákok százezrei szavalják e sorokat."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy-03-nemzetidal.json", story_03)

    story_04 = {
        "id": "story.b1.nemzetiugy.04",
        "title": "Kokárda a szívek felett: Nemzeti jelképeink",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The origins of Hungary's beloved national symbols: how Szendrey Júlia sewed the first tricolor cockade for Petőfi, the deep meaning of the red-white-green colors, and the debate between the Holy Crown and the republican Kossuth coat of arms.",
        "characters": [
            "Szendrey Júlia",
            "Petőfi Sándor",
            "Kossuth Lajos"
        ],
        "location": "Pest, Dohány utca",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848. március 15-én reggel Petőfi felesége, a tehetséges és bátor Szendrey Júlia vörös, fehér és zöld szalagokból varrt egy kis kerek rozettát."
            },
            {
                "type": "dialogue",
                "speaker": "Szendrey Júlia",
                "text": "Tűzd a szíved fölé, Sándor! Ez a kokárda hirdesse mindenkinek, hogy a magyar szabadságért dobog a melled!"
            },
            {
                "type": "narration",
                "text": "A délután folyamán a pesti hölgyek ezrével osztogatták a nemzeti trikolór szalagjait. A piros az erőt és a kiontott vért, a fehér a hűséget és a békét, a zöld a jövő reményét jelképezte."
            },
            {
                "type": "narration",
                "text": "A forradalom idején a királyi koronát levették a nemzeti címerről: megszületett a Kossuth-címer, amely a polgári köztársasági eszme tiszta jelképe lett."
            },
            {
                "type": "dialogue",
                "speaker": "Kossuth Lajos",
                "text": "A címer és a zászló nem puszta dísz. Ezekben él nemzetünk ezeréves múltja és szabadságvágya."
            },
            {
                "type": "narration",
                "text": "Bár a történelem viharai sokszor változtattak az államformán, a piros-fehér-zöld kokárda mind a mai napig összeköti a világ magyarságát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy-04-kokarda.json", story_04)

    story_05 = {
        "id": "story.b1.nemzetiugy.05",
        "title": "Március 15.: Miért ünnepel a nemzet?",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "March 15 is one of Hungary's three official national holidays and a central topic on the citizenship interview. Across cities and diaspora communities, citizens pin cockades, lay wreaths at Petőfi statues, and celebrate the birth of modern civic Hungary.",
        "characters": [
            "Ünneplő család",
            "Polgármester",
            "Állampolgársági vizsgabiztos"
        ],
        "location": "Budapest, Múzeumkert, Kossuth tér",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Minden év március 15-én reggel felvonják a nemzeti zászlót a Parlament előtt. Az egész ország ünnepi díszbe öltözik: idős és fiatal kokárdát tűz a kabátjára."
            },
            {
                "type": "narration",
                "text": "A Múzeumkertben ezrek gyűlnek össze, miközben a költők szavait visszhangozzák a lépcsők. A koszorúzás során a nemzet fejet hajt Petőfi és a szabadsághősök szobra előtt."
            },
            {
                "type": "dialogue",
                "speaker": "Polgármester",
                "text": "1848 márciusa nem a múltról szól, hanem rólunk. Arról tanít, hogy a szabadság és a felelősség elválaszthatatlan egymástól."
            },
            {
                "type": "narration",
                "text": "Nem véletlen, hogy a magyar állampolgársági interjún szinte mindig megkérdezik: Miért nemzeti ünnep március 15., és mit jelképez a kokárda?"
            },
            {
                "type": "dialogue",
                "speaker": "Állampolgársági vizsgabiztos",
                "text": "Aki leteszi a magyar állampolgári esküt, az részévé válik ennek az ezeréves történelmi örökségnek és szellemi közösségnek."
            },
            {
                "type": "narration",
                "text": "Március 15. a nemzeti egység és az újjászületés ünnepe: amíg a kokárdát büszkén viseljük, a szabadság eszméje eleven marad."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy-05-marciusunnep.json", story_05)

    # Combined Story for Library
    story_combined = {
        "id": "story.b1.nemzetiugy",
        "title": "Kossuth, Petőfi és a nemzeti szimbólumok",
        "level": "B1",
        "order": 17,
        "type": "world",
        "estimatedMinutes": 9,
        "summary": "The heroes and symbols of 1848: Kossuth's global crusade in exile, Petőfi's blazing poetry and sacrifice at Segesvár, the electric vow of the Nemzeti dal, the tricolor cockade, and the lasting meaning of March 15 in modern Hungarian civic life.",
        "characters": [
            "Kossuth Lajos",
            "Petőfi Sándor",
            "Szendrey Júlia"
        ],
        "location": "Pest, Segesvár, Washington, Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Kossuth Lajos az emigrációban sem adta fel a küzdelmet: zseniális szónoki tehetségével bejárta Amerikát, és a magyar szabadság ügyét világszerte ismertté tette."
            },
            {
                "type": "narration",
                "text": "Petőfi Sándor, a nemzet lánglelkű költője nemcsak írt a szabadságról, de életét áldozta érte a Segesvári csatában Bem tábornok oldalán."
            },
            {
                "type": "narration",
                "text": "A Nemzeti dal és a 'Talpra magyar!' felhívása örök esküvé vált: a nemzet egy emberként fogadta meg, hogy soha többé nem lesz rab."
            },
            {
                "type": "narration",
                "text": "A Szendrey Júlia által megalkotott piros-fehér-zöld kokárda és a Kossuth-címer a nemzeti összetartozás legfontosabb jelképévé emelkedett."
            },
            {
                "type": "narration",
                "text": "Március 15. nemzeti ünnepünk: a szabadság, a polgári egyenlőség és az állampolgári hűség örök emléknapja."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiugy.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-nemzetiugy-{padded}",
            "exercises": [
                {
                    "id": f"b1-nemzetiugy-{padded}.ex01",
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
                    "id": f"b1-nemzetiugy-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen a nemzeti fogadalmat vagy cselekvést? (Lesson {i})",
                    "options": [
                        "Kossuth városról városra utazva szónokolt a szabadságról.",
                        "Kossuth utazni volt hogy szónokoljon beszéd.",
                        "Kossuth mivel utazott ezért nem beszélt senkinek."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A magyar nemzeti trikolór három színe: piros, fehér és ____. (green)",
                    "answer": "zöld"
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A költő életét áldozta azért, ____ hazája szabad legyen. (so that)",
                    "answer": "hogy"
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit szimbolizál a kokárda viselése március 15-én?",
                    "options": [
                        "A forradalom emlékét, a nemzeti szabadságvágyat és az összetartozást.",
                        "Hogy valaki katonaként szolgál az osztrák hadseregben.",
                        "A tavaszi mezőgazdasági munkák kezdetét."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A nemzeti dal híres sora: Talpra magyar, hí a ____! (homeland)",
                    "answer": "haza"
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Március", "tizenötödikén", "országszerte", "koszorúzásokat", "és", "ünnepségeket", "tartanak."],
                    "solution": ["Március", "tizenötödikén", "országszerte", "koszorúzásokat", "és", "ünnepségeket", "tartanak."]
                },
                {
                    "id": f"b1-nemzetiugy-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik híres csatában tűnt el Petőfi Sándor 1849-ben?",
                    "options": [
                        "A Segesvári csatában, Bem tábornok seregében.",
                        "A mohácsi csatában a törökök ellen.",
                        "A lipcsei népek csatájában Napóleon oldalán."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-nemzetiugy-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-nemzetiugy-consolidation",
        "exercises": [
            {
                "id": "b1-nemzetiugy-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Nemzeti dal", "National Song"],
                    ["kokárda", "cockade rosette"],
                    ["állampolgári eskü", "citizenship oath"],
                    ["hősi halál", "heroic death"]
                ]
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelképeznek a magyar nemzeti színek a hivatalos állampolgársági magyarázat szerint?",
                "options": [
                    "A piros az erőt, a fehér a hűséget, a zöld a reményt.",
                    "A piros a tüzet, a fehér a tejet, a zöld az erdőket.",
                    "A piros a királyt, a fehér a pápát, a zöld a hadsereget."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A királyi korona nélküli nemzeti címert ____ címernek nevezzük. (Kossuth)",
                "answer": "Kossuth"
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemzet tisztelettel fejet hajt a hősök emléke ____. (before / in front of)",
                "answer": "előtt"
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "március", "tizenötödiki", "ünnep", "a", "magyar", "nemzet", "szabadságszeretetének", "örök", "jelképe."],
                "solution": ["A", "március", "tizenötödiki", "ünnep", "a", "magyar", "nemzet", "szabadságszeretetének", "örök", "jelképe."]
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kinek az emléke előtt tisztelegnek a március 15-i koszorúzások alkalmával?",
                "options": [
                    "Petőfi Sándor, Kossuth Lajos és az 1848-as szabadsághősök előtt.",
                    "A bécsi udvar cenzorai és rendőrtisztjei előtt.",
                    "A török szultán seregei előtt."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Nemzeti dal refrénje: Esküszünk, hogy rabok tovább nem ____! (will be)",
                "answer": "leszünk"
            },
            {
                "id": "b1-nemzetiugy-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan fogadták Kossuth Lajost az Egyesült Államokban 1851-ben?",
                "options": [
                    "Hatalmas tömegek ünnepelték, az elnök fogadta és a szabadság apostolaként tisztelték.",
                    "Azonnal börtönbe zárták mint veszélyes külföldi lázadót.",
                    "Senki sem ment el a beszédeire a nyelvi nehézségek miatt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiugy-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Kossuth Lajos emigrációban", "Lajos Kossuth in Exile"),
        "02": ("Petőfi Sándor, a forradalom költője", "Sándor Petőfi, Poet of the Revolution"),
        "03": ("A Nemzeti dal", "The Nemzeti Dal"),
        "04": ("1848 jelképei: kokárda és címer", "Symbols of 1848"),
        "05": ("Miért nemzeti ünnep március 15.?", "Why March 15 Is a National Holiday")
    }

    story_refs = {
        "01": "stories/world/b1/b1-nemzetiugy-01-kossuthemigracio.json",
        "02": "stories/world/b1/b1-nemzetiugy-02-petofikolto.json",
        "03": "stories/world/b1/b1-nemzetiugy-03-nemzetidal.json",
        "04": "stories/world/b1/b1-nemzetiugy-04-kokarda.json",
        "05": "stories/world/b1/b1-nemzetiugy-05-marciusunnep.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.nemzetiugy-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Adverbial Participles, Rhetorical Imperatives & National Symbols Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the legacy and cultural impact of {en_t}.",
                        "I can use adverbial participles (-va/-ve) and ceremonial register in Hungarian.",
                        "I can answer key citizenship interview questions on national symbols and holidays.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-nemzetiugy-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-nemzetiugy-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-nemzetiugy-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-nemzetiugy-{padded}.ex01",
                        f"b1-nemzetiugy-{padded}.ex02",
                        f"b1-nemzetiugy-{padded}.ex03",
                        f"b1-nemzetiugy-{padded}.ex04",
                        f"b1-nemzetiugy-{padded}.ex05",
                        f"b1-nemzetiugy-{padded}.ex06",
                        f"b1-nemzetiugy-{padded}.ex07",
                        f"b1-nemzetiugy-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-nemzetiugy-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.nemzetiugy-consolidation",
        "title": "Összefoglalás: Kossuth, Petőfi és a nemzeti ügy (National Cause Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of National Symbols, March 15 & Citizenship Heritage",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-nemzetiugy.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-nemzetiugy-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-nemzetiugy-consolidation.ex01",
                    "b1-nemzetiugy-consolidation.ex02",
                    "b1-nemzetiugy-consolidation.ex03",
                    "b1-nemzetiugy-consolidation.ex04",
                    "b1-nemzetiugy-consolidation.ex05",
                    "b1-nemzetiugy-consolidation.ex06",
                    "b1-nemzetiugy-consolidation.ex07",
                    "b1-nemzetiugy-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiugy-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 17 (b1-nemzetiugy)!")

if __name__ == "__main__":
    build_unit_17_citizenship()
