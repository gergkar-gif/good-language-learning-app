#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 30: National Holidays & Remembrance Days (b1-nemzetiunnepek)."""

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

def build_unit_30_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.nemzetiunnepek.01",
        "lesson": "b1-nemzetiunnepek-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "március tizenötödike", "translation": "March 15th (national holiday of the 1848 Civic Revolution)", "pos": "noun"},
            {"lemma": "1848-as forradalom", "translation": "1848 Revolution and War of Independence for freedom and civic equality", "pos": "noun"},
            {"lemma": "polgári átalakulás", "translation": "civic transformation ending feudalism (press freedom, equality)", "pos": "noun"},
            {"lemma": "Nemzeti dal", "translation": "National Song (Petőfi's revolutionary rallying poem: 'Talpra magyar')", "pos": "noun"},
            {"lemma": "tizenkét pont", "translation": "12 points (the March youth's democratic demands for freedom)", "pos": "noun"},
            {"lemma": "Pilvax kávéház", "translation": "Pilvax Café (historic meeting place of the revolutionary youth)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiunnepek-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.nemzetiunnepek.02",
        "lesson": "b1-nemzetiunnepek-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "augusztus huszadika", "translation": "August 20th (official state holiday of Saint Stephen and State Founding)", "pos": "noun"},
            {"lemma": "államalapítás ünnepe", "translation": "holiday of the founding of the Christian Hungarian state", "pos": "noun"},
            {"lemma": "Szent István napja", "translation": "Saint Stephen's Day honoring Hungary's first crowned king", "pos": "noun"},
            {"lemma": "új kenyér ünnepe", "translation": "blessing of the new bread baked from freshly harvested wheat", "pos": "noun"},
            {"lemma": "tisztavatás", "translation": "military officer inauguration ceremony on Kossuth Square", "pos": "noun"},
            {"lemma": "ünnepi tűzijáték", "translation": "festive fireworks display over the Danube between the Buda and Pest bridges", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiunnepek-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.nemzetiunnepek.03",
        "lesson": "b1-nemzetiunnepek-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "október huszonharmadika", "translation": "October 23rd (national holiday of 1956 & proclamation of the Republic)", "pos": "noun"},
            {"lemma": "1956-os forradalom emléknapja", "translation": "memorial day of the 1956 Revolution and Freedom Fight", "pos": "noun"},
            {"lemma": "köztársaság kikiáltása", "translation": "proclamation of the third Republic of Hungary in 1989", "pos": "noun"},
            {"lemma": "lyukas zászló", "translation": "tricolor with the communist coat-of-arms cut out in 1956", "pos": "noun"},
            {"lemma": "forradalmi mártírok", "translation": "revolutionary martyrs who gave their lives for Hungarian liberty", "pos": "noun"},
            {"lemma": "hivatalos nemzeti ünnep", "translation": "official national holiday celebrated across the country", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiunnepek-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.nemzetiunnepek.04",
        "lesson": "b1-nemzetiunnepek-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "aradi vértanúk emléknapja", "translation": "Memorial Day of the Martyrs of Arad (October 6th)", "pos": "noun"},
            {"lemma": "október hatodika", "translation": "October 6th (national day of mourning for the executed 1849 generals)", "pos": "noun"},
            {"lemma": "Batthyány Lajos", "translation": "Count Lajos Batthyány (first constitutional Prime Minister, executed Oct 6, 1849)", "pos": "noun"},
            {"lemma": "kivégzés", "translation": "martyrdom / execution by the Austrian imperial court martial", "pos": "noun"},
            {"lemma": "Nemzeti Összetartozás Napja", "translation": "Day of National Cohesion (June 4th, marking the 1920 Trianon Treaty)", "pos": "noun"},
            {"lemma": "június negyedike", "translation": "June 4th (day of national unity and cross-border cohesion)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiunnepek-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.nemzetiunnepek.05",
        "lesson": "b1-nemzetiunnepek-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kommunizmus áldozatainak emléknapja", "translation": "Memorial Day for Victims of Communist Dictatorship (February 25th)", "pos": "noun"},
            {"lemma": "február huszonötödike", "translation": "February 25th (date of MP Béla Kovács's arrest by Soviet troops in 1947)", "pos": "noun"},
            {"lemma": "Kovács Béla elhurcolása", "translation": "unlawful abduction of Smallholders Party General Secretary to the Gulag", "pos": "noun"},
            {"lemma": "holokauszt emléknapja", "translation": "Memorial Day for Hungarian Victims of the Holocaust (April 16th)", "pos": "noun"},
            {"lemma": "április tizenhatodika", "translation": "April 16th (marking the 1944 establishment of the first ghettos)", "pos": "noun"},
            {"lemma": "gettósítás", "translation": "forced ghettoization and deportation of Hungarian Jewish citizens in 1944", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetiunnepek-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.nemzetiunnepek.01.commemorative-dates",
        "title": "Commemorative Dates & Occasions: alkalmából, tiszteletére",
        "sections": [
            {
                "type": "text",
                "title": "Calendar Expressions and Postpositions of Occasion",
                "content": "Official commemorations use specific postpositions: *március 15. alkalmából* ('on the occasion of March 15th'), *a szabadságharcosok tiszteletére* ('in honor of the freedom fighters' - dative possessive), *az évforduló napján* ('on the day of the anniversary')."
            },
            {
                "type": "examples",
                "title": "Date and occasion examples",
                "items": [
                    {
                        "spanish": "Március 15. alkalmából országszerte megemlékezéseket tartanak az 1848-as forradalom tiszteletére.",
                        "english": "On the occasion of March 15th, commemorations are held nationwide in honor of the 1848 revolution."
                    },
                    {
                        "spanish": "A polgárok kokárdát viselnek a szívük felett a forradalmi ifjúság emlékére.",
                        "english": "Citizens wear cockades over their hearts in memory of the revolutionary youth."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiunnepek-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.nemzetiunnepek.02.state-ceremony-verbs",
        "title": "State Ceremonial Protocol: felvonja a lobogót, tisztet avat",
        "sections": [
            {
                "type": "text",
                "title": "Official State Ritual Phrases",
                "content": "*Katonai tiszteletadással felvonja a nemzeti lobogót* ('raises the national flag with military honors'), *tisztet avat* ('inaugurates officers'), *megáldja az új kenyeret* ('blesses the new bread'), *ünnepi beszédet mond* ('delivers a festive speech')."
            },
            {
                "type": "examples",
                "title": "State ritual examples",
                "items": [
                    {
                        "spanish": "Augusztus 20-án reggel a Kossuth téren katonai tiszteletadással felvonják a nemzeti lobogót.",
                        "english": "On the morning of August 20th on Kossuth Square, they raise the national flag with military honors."
                    },
                    {
                        "spanish": "Az államfő jelenlétében a frissen végzett honvédtisztek leteszik az ünnepélyes tisztik esküt.",
                        "english": "In the presence of the head of state, newly graduated defense officers take the solemn officer's oath."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiunnepek-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.nemzetiunnepek.03.dual-anniversary-syntax",
        "title": "Dual Anniversaries: egyszerre emlékezik meg... és...",
        "sections": [
            {
                "type": "text",
                "title": "Linking Two Historic Milestones on October 23rd",
                "content": "October 23rd unites two historical turning points: *Egyszerre emlékezünk meg az 1956-os forradalom kitöréséről és a Magyar Köztársaság 1989-es kikiáltásáról.* Governed by *megemlékezik vmiről* (delative *-ról/-ről*)."
            },
            {
                "type": "examples",
                "title": "Dual anniversary examples",
                "items": [
                    {
                        "spanish": "Október 23-án Magyarország kettős történelmi évfordulót ünnepel.",
                        "english": "On October 23rd, Hungary celebrates a double historical anniversary."
                    },
                    {
                        "spanish": "A nemzet egyszerre tiszteleg az 1956-os hősök előtt és ünnepli a modern demokrácia 1989-es megszületését.",
                        "english": "The nation simultaneously pays tribute to the 1956 heroes and celebrates the 1989 birth of modern democracy."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiunnepek-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.nemzetiunnepek.04.homage-and-reverence",
        "title": "Solemn Homage to Martyrs: fejet hajt, koszorút helyez el",
        "sections": [
            {
                "type": "text",
                "title": "Registers of National Mourning and Reverence",
                "content": "*Fejet hajt az aradi vértanúk emléke előtt* ('bows head before the memory of the martyrs of Arad'), *koszorút helyez el az emlékműnél* ('lays a wreath at the monument' - adessive *-nál/-nél*), *nemzeti gyásznapként tart számon* ('observes as a national day of mourning')."
            },
            {
                "type": "examples",
                "title": "Homage examples",
                "items": [
                    {
                        "spanish": "Október 6-án a nemzet néma főhajtással emlékezik a tizenhárom aradi vértanúra és Batthyány Lajos miniszterelnökre.",
                        "english": "On October 6th, the nation commemorates the thirteen martyrs of Arad and Prime Minister Lajos Batthyány with silent bowed heads."
                    },
                    {
                        "spanish": "Június 4-én a harangok zúgása emlékeztet a nemzeti összetartozás elszakíthatatlan kötelékére.",
                        "english": "On June 4th, the tolling of church bells reminds of the unbreakable bond of national cohesion."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiunnepek-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.nemzetiunnepek.05.remembrance-and-warnings",
        "title": "Remembrance and Warnings: figyelmeztetésként szolgál",
        "sections": [
            {
                "type": "text",
                "title": "Moral Lessons of 20th Century Tragedies",
                "content": "*Figyelmeztetésként szolgál a jövő nemzedékek számára* ('serves as a warning for future generations'), *méltósággal megőrzi az áldozatok emlékét* ('preserves with dignity the memory of the victims'), *soha többé nem ismétlődhet meg* ('can never again be repeated')."
            },
            {
                "type": "examples",
                "title": "Warning examples",
                "items": [
                    {
                        "spanish": "A totalitárius diktatúrák áldozatainak emléknapjai örök figyelmeztetésként szolgálnak a szabadság védelmére.",
                        "english": "The memorial days for victims of totalitarian dictatorships serve as an eternal warning to defend freedom."
                    },
                    {
                        "spanish": "A magyar állam kötelessége, hogy tisztelettel megőrizze minden meghurcolt és elpusztított polgárának emlékét.",
                        "english": "It is the duty of the Hungarian state to preserve with respect the memory of every persecuted and destroyed citizen."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetiunnepek-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Story Files (5 regular lesson stories + 1 combined omnibus story)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.nemzetiunnepek.01",
        "lesson": 1,
        "order": 1,
        "title": "Március 15.: A szabadság és a polgári Magyarország születése",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "March 15th is Hungary's most joyous and inspiring national holiday, commemorating the 1848 Revolution. From the gathering of Petőfi and Jókai at the Pilvax Café to the printing of the 12 Points and the National Song at Landerer's press without censorship, and the sea of umbrellas outside the National Museum, March 15th marks the birth of modern civic Hungary.",
        "characters": [
            "Petőfi Sándor szelleme",
            "Kokárdás diák a Nemzeti Múzeum lépcsőjén",
            "Idős nagymama unokájával"
        ],
        "location": "Budapest, Pilvax kávéház és a Nemzeti Múzeum kertje",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1848. március 15-én esős, hűvös reggel virradt Pestre. A Pilvax kávéházban fiatal írók, költők és egyetemisták gyűltek össze Petőfi Sándor, Jókai Mór és Vasvári Pál vezetésével."
            },
            {
                "type": "dialogue",
                "speaker": "Petőfi Sándor",
                "text": "Európa lángokban áll, eljött a cselekvés ideje! Nem kérünk többé engedélyt a cenzortól! Ma a nép maga szerzi vissza a szabadságát!"
            },
            {
                "type": "narration",
                "text": "A márciusi ifjak Landerer és Heckenast nyomdájához vonultak, s a cenzúra pecsétje nélkül kinyomtatták a Nemzeti dalt és a 12 pontot: kívánták a sajtó szabadságát, a felelős kormányt, a törvény előtti egyenlőséget és a közteherviselést."
            },
            {
                "type": "dialogue",
                "speaker": "Kokárdás diák a múzeumkertben",
                "text": "Délután a Nemzeti Múzeum előtt tízezres tömeg zúgta Petőfivel: 'A magyarok istenére esküszünk, esküszünk, hogy rabok tovább nem leszünk!' Ez a pillanat teremtette meg a modern polgári Magyarországot!"
            },
            {
                "type": "narration",
                "text": "Március 15-e ma a tavasz, a szabadság és a nemzeti összefogás legkedvesebb ünnepe, amikor minden magyar ember büszkén tűzi szívére a nemzeti színű kokárdát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek-01-marcius15.json", story_01)

    story_02 = {
        "id": "story.b1.nemzetiunnepek.02",
        "lesson": 2,
        "order": 2,
        "title": "Augusztus 20.: Szent István napja és az államalapítás ünnepe",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "August 20th is Hungary's oldest national holiday and the official state holiday. Commemorating the 1083 canonization of King Saint Stephen and the founding of the Christian Hungarian state in the year 1000, it is celebrated with the raising of the flag and officer inauguration on Kossuth Square, the blessing of the new bread, the Saint Right procession, and evening fireworks over the Danube.",
        "characters": [
            "Frissen felavatott honvédtiszt a Kossuth téren",
            "Pékmester az új kenyér ünnepén",
            "Családanya a Duna-parton az esti tűzijátéknál"
        ],
        "location": "Budapest, Kossuth tér, a Szent István-bazilika és a Duna-part",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Augusztus 20-a Magyarország legősibb nemzeti ünnepe, amelyet már Szent László király idején, 1083-ban törvénybe iktattak István király szentté avatásának emlékére. Ez a nap a magyar államalapítás és az ezeréves keresztény államiság ünnepe."
            },
            {
                "type": "dialogue",
                "speaker": "Frissen avatott honvédtiszt",
                "text": "Reggel a Parlament előtt a köztársasági elnök és a hadsereg előtt tesszük le az esküt. A kardomat a hazám és a magyar nemzet védelmére ajánlom, Szent István örökségéhez híven!"
            },
            {
                "type": "narration",
                "text": "Augusztus 20-a egyben az új kenyér ünnepe is: országszerte megáldják a friss búzából sütött, nemzeti szalaggal átkötött kenyeret, amely a megmaradást és a bőséget szimbolizálja."
            },
            {
                "type": "dialogue",
                "speaker": "Pékmester",
                "text": "A föld megadta a termést, mi pedig megsütöttük az új kenyeret. Ahogy a kenyér táplálja a testet, úgy táplálja a hazaszeretet és a hit a nemzet lelkét!"
            },
            {
                "type": "narration",
                "text": "Délután a Szent István-bazilikából elindul a Szent Jobb-körmenet, este pedig százezrek gyűlnek össze a Duna partjain, hogy megcsodálják a folyó felett ragyogó lenyűgöző ünnepi tűzijátékot."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek-02-augusztus20.json", story_02)

    story_03 = {
        "id": "story.b1.nemzetiunnepek.03",
        "lesson": 3,
        "order": 3,
        "title": "Október 23.: A szabadságharc és a köztársaság kettős ünnepe",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "October 23rd carries double historic weight: it marks the outbreak of the heroic 1956 Revolution against Soviet tyranny and, on its 33rd anniversary in 1989, the official proclamation of the free and democratic Republic of Hungary. From the university students at the Bem statue in 1956 to the jubilant crowds at Kossuth Square in 1989, October 23rd embodies Hungary's unquenchable thirst for freedom.",
        "characters": [
            "1956-os veterán",
            "1989-es fiatal parlamenti tudósító",
            "Egyetemista fáklyás felvonuló"
        ],
        "location": "Budapest, Bem tér, Corvin köz és a Parlament Kossuth tere",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Október 23-án Magyarország kettős történelmi évfordulót ünnepel. Ezen a napon 1956-ban a békés egyetemi felvonulás a 20. század legtisztább forradalmává nőtt a szovjet elnyomás és a kommunista diktatúra ellen."
            },
            {
                "type": "dialogue",
                "speaker": "1956-os veterán",
                "text": "Október 23-án délután a Bem-szobornál még csak énekeltünk és követeltük a szabadságot. De este a rádiónál már dörögtek a fegyverek! A nép nem bírt tovább rab lenni: kivágtuk a címert a zászlóból, és szembeszálltunk a zsarnoksággal!"
            },
            {
                "type": "narration",
                "text": "Harminchárom évvel később, 1989. október 23-án a történelem beteljesítette a pesti srácok álmát: Szűrös Mátyás a Parlament erkélyéről kikiáltotta a független, demokratikus Magyar Köztársaságot."
            },
            {
                "type": "dialogue",
                "speaker": "1989-es tudósító",
                "text": "A Kossuth téren százezer ember énekelte a Himnuszt zokogva. Az 1956-os mártírok áldozata győzött: véget ért a diktatúra, megszületett a szabad jogállam!"
            },
            {
                "type": "narration",
                "text": "Október 23-án este fáklyás menet vonul végig a Műegyetemtől a Bem térig, tisztelegve a hősök előtt, akik vérükkel váltották meg a mai Magyarország szabadságát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek-03-oktober23.json", story_03)

    story_04 = {
        "id": "story.b1.nemzetiunnepek.04",
        "lesson": 4,
        "order": 4,
        "title": "Nemzeti emléknapok: Aradi vértanúk és az Összetartozás Napja",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Alongside the three national holidays, Hungary observes official national days of remembrance. October 6th is the National Day of Mourning for the 13 martyred generals executed in Arad and Prime Minister Count Lajos Batthyány executed in Pest in 1849. June 4th is the Day of National Cohesion, transforming the trauma of the 1920 Trianon Treaty into a celebration of cross-border unity and cultural survival.",
        "characters": [
            "Történész az Aradi emlékhelynél",
            "Erdélyi magyar diák a Nemzeti Összetartozás Emlékhelyénél"
        ],
        "location": "Arad, a vesztőhely és a budapesti Alkotmány utca",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A három piros betűs nemzeti ünnep mellett a magyar naptár kiemelt nemzeti emléknapokat is tartalmaz. Október 6-a a nemzeti gyász napja: 1849-ben ezen a napon végezte ki a bosszúszomjas osztrák hadbíróság Aradon a szabadságharc tizenhárom tábornokát, Pesten pedig gróf Batthyány Lajos miniszterelnököt."
            },
            {
                "type": "dialogue",
                "speaker": "Történész",
                "text": "A vértanúk tudták, mi vár rájuk, mégis emelt fővel léptek a vesztőhelyre. Damjanich János, Aulich Lajos, Kiss Ernő és társaik nem a vereséget, hanem az erkölcsi győzelmet jelentik a nemzet emlékezetében."
            },
            {
                "type": "narration",
                "text": "Június 4-e a Nemzeti Összetartozás Napja. 1920-ban ezen a napon írták alá a trianoni békediktátumot, amely elszakította az ország területének kétharmadát és több millió magyart. 2010 óta ez a nap a határokon átívelő nemzeti egység és élni akarás szimbóluma."
            },
            {
                "type": "dialogue",
                "speaker": "Erdélyi magyar diák",
                "text": "A Parlament előtti emlékhely falára felvésték a történelmi Magyarország összes településének nevét. Nem a határváltoztatásról beszélünk, hanem a közös nyelvről, a kultúráról és arról a szeretetről, ami örökre összeköt minket!"
            },
            {
                "type": "narration",
                "text": "Ezek az emléknapok megtanítják a magyarokat arra, hogy a múlt sebei nem gyengítenek, hanem megerősítik a nemzet összetartozásának hitét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek-04-emleknapok.json", story_04)

    story_05 = {
        "id": "story.b1.nemzetiunnepek.05",
        "lesson": 5,
        "order": 5,
        "title": "A diktatúrák áldozatai: Február 25. és Április 16.",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary honors the victims of 20th-century totalitarianism on two solemn remembrance days. February 25th marks the Memorial Day for Victims of Communist Dictatorships, commemorating the 1947 illegal arrest of MP Béla Kovács and the suffering of hundreds of thousands in Recsk, Gulag camps, and show trials. April 16th is the Holocaust Memorial Day, marking the 1944 ghettoization of Hungarian Jewry.",
        "characters": [
            "A Terror Háza Múzeum történésze",
            "Holokauszt-túlélő unokája a Duna-parti Cipőknél"
        ],
        "location": "Budapest, Terror Háza Múzeum (Andrássy út 60.) és a Duna-part",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A 20. század két kegyetlen totalitárius eszméje – a nemzetiszocializmus és a kommunizmus – mély sebeket ejtett a magyar társadalmon. A demokratikus Országgyűlés két törvényes emléknapot rendelt az áldozatok tiszteletére."
            },
            {
                "type": "dialogue",
                "speaker": "Terror Háza történésze",
                "text": "Február 25-e a kommunista diktatúrák áldozatainak emléknapja. 1947-ben ezen a napon hurcolták el a szovjet hatóságok Kovács Bélát, a Kisgazdapárt főtitkárát. Ezen a napon a Gulágra hurcolt százezrekre, a Recskre internáltakra és a koncepciós perek mártírjaira emlékezünk."
            },
            {
                "type": "narration",
                "text": "Április 16-a a holokauszt magyarországi áldozatainak emléknapja: 1944-ben ezen a napon kezdődött meg Kárpátalján a magyar zsidóság gettókba zárása, amelyet a haláltáborokba való könyörtelen deportálás követett."
            },
            {
                "type": "dialogue",
                "speaker": "Túlélő unokája a Duna-parti Cipőknél",
                "text": "Több mint félmillió magyar zsidó honfitársunkat pusztították el a nácik és a nyilasok. Itt a Duna-parton állva a hideg vascipők előtt megfogadjuk: a gyűlöletnek soha többé nem engedünk teret a hazánkban!"
            },
            {
                "type": "narration",
                "text": "Ezen emléknapok üzenete egyértelmű: a szabadság, az emberi élet szentsége és a jogállamiság feladása mindig barbársághoz vezet, amelyet éber felelősséggel kell megakadályoznunk."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek-05-aldozatok.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.nemzetiunnepek.combined",
        "title": "Magyarország nemzeti ünnepei és emléknapjai",
        "level": "B1",
        "order": 30,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "A comprehensive panoramic chronicle of Hungary's three official national holidays and solemn remembrance days. From March 15th (1848 Civic Revolution, cockades, 12 Points); August 20th (King Saint Stephen, State Founding, New Bread); October 23rd (1956 Revolution and 1989 Republic); October 6th (Martyrs of Arad); June 4th (Day of National Cohesion); to February 25th and April 16th (Victims of Communism and the Holocaust). These days define Hungarian historical consciousness, identity, and civic duty.",
        "characters": [
            "Történész professzor",
            "Állampolgári esküt tevő új polgár",
            "Múzeumpedagógus"
        ],
        "location": "Budapest, Kossuth tér, Hősök tere és a Nemzeti Múzeum",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország törvényei három hivatalos nemzeti ünnepet határoznak meg: Március 15-e az 1848-as polgári forradalom és a modern parlamentarizmus születése; Augusztus 20-a az államalapítás, Szent István király és az ezeréves keresztény államiság napja; Október 23-a pedig az 1956-os forradalom és a szabad Magyar Köztársaság 1989-es kikiáltásának kettős ünnepe."
            },
            {
                "type": "narration",
                "text": "Ezeken az ünnepeken a nemzet tisztelettel adózik a szabadságot kivívó hősök előtt: felvonják a nemzeti lobogót az Országház előtt, kokárdát tűznek a kabátokra, kenyeret áldanak és emlékező fáklyás felvonulásokat tartanak."
            },
            {
                "type": "narration",
                "text": "A nemzeti naptár mély tisztelettel őrzi a tragédiák és a helytállás emléknapjait is: Október 6-án az aradi vértanúk és Batthyány Lajos gróf önfeláldozására emlékezünk; Június 4-én a Nemzeti Összetartozás Napja a trianoni határokon átívelő testvéri köteléket ünnepli; míg Február 25-e és Április 16-a a kommunizmus és a holokauszt áldozatainak méltóságát állítja elénk örök figyelmeztetésül."
            },
            {
                "type": "narration",
                "text": "Ezen ünnepek és emléknapok mély ismerete a magyar nemzeti identitás és az állampolgári tudat elengedhetetlen fundamentuma minden leendő és jelenlegi magyar polgár számára."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetiunnepek.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-nemzetiunnepek-01",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-01.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mit ünneplünk március 15-én Magyarországon?",
                "options": [
                    "Az 1848–49-es forradalom és szabadságharc kezdetét, a modern polgári Magyarország születését.",
                    "Szent István király államalapítását.",
                    "A NATO-csatlakozás évfordulóját."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Március 15. alkalmából a polgárok kokárdát tűznek a szívük fölé a szabadság tiszteleté_____. (in its honor - re)",
                "answer": "re"
            },
            {
                "id": "b1-nemzetiunnepek-01.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "márciusi", "ifjak", "a", "Pilvax", "kávéházban", "fogalmazták", "meg", "követeléseiket."],
                "solution": ["A", "márciusi", "ifjak", "a", "Pilvax", "kávéházban", "fogalmazták", "meg", "követeléseiket."]
            },
            {
                "id": "b1-nemzetiunnepek-01.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik híres versét szavalta el Petőfi Sándor 1848. március 15-én a forradalmi tömegnek?",
                "options": [
                    "A Nemzeti dalt ('Talpra magyar, hí a haza!').",
                    "A Himnuszt.",
                    "A Szózatot."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A márciusi ifjak kinyomtatták a tizenkét pon_____, amely a sajtószabadságot követelte. (accusative - tot)",
                "answer": "tot"
            },
            {
                "id": "b1-nemzetiunnepek-01.ex06",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hol gyűlt össze a legnagyobb ünneplő tömeg 1848. március 15-én délután Pesten?",
                "options": [
                    "A Nemzeti Múzeum lépcsője előtt.",
                    "A budai Vár udvarán.",
                    "A Margit-szigeten."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az 1848-as forradalom békés polgári átalakulást hoz_____ Magyarországon. (brought - ott)",
                "answer": "ott"
            },
            {
                "id": "b1-nemzetiunnepek-01.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Március", "15-e", "a", "magyar", "szabadság", "és", "egyetértés", "szimbóluma."],
                "solution": ["Március", "15-e", "a", "magyar", "szabadság", "és", "egyetértés", "szimbóluma."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-nemzetiunnepek-02",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-02.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mit ünnepel Magyarország augusztus 20-án hivatalos állami ünnepként?",
                "options": [
                    "Az államalapítást és Szent István király emlékét, valamint az új kenyér ünnepét.",
                    "Az 1956-os forradalom kitörését.",
                    "A köztársaság kikiáltását."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Augusztus 20-án katonai tiszteletadással felvonják a nemzeti lobogó_____. (accusative - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetiunnepek-02.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "tisztavatás", "a", "Kossuth", "téren", "zajlik", "az", "államfő", "jelenlétében."],
                "solution": ["A", "tisztavatás", "a", "Kossuth", "téren", "zajlik", "az", "államfő", "jelenlétében."]
            },
            {
                "id": "b1-nemzetiunnepek-02.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Ki volt az a magyar király, aki az államot alapította és megkoronázásával beléptette az országot a keresztény Európába?",
                "options": [
                    "Szent István király (1000-ben).",
                    "Hunyadi Mátyás.",
                    "Károly Róbert."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az ünnep napján országszerte megáldják az új kenyér_____. (accusative - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetiunnepek-02.ex06",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Milyen látványos esemény zárja hagyományosan az augusztus 20-i ünnepnap estéjét Budapesten?",
                "options": [
                    "A Duna felett rendezett hatalmas ünnepi tűzijáték és drónshow.",
                    "Egy nemzetközi labdarúgó-mérkőzés.",
                    "A karácsonyi vásár megnyitója."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szent István király ezeréves keresztény államot alapí_____. (founded - tott)",
                "answer": "tott"
            },
            {
                "id": "b1-nemzetiunnepek-02.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Augusztus", "20-a", "Magyarország", "hivatalos", "állami", "ünnepe."],
                "solution": ["Augusztus", "20-a", "Magyarország", "hivatalos", "állami", "ünnepe."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-nemzetiunnepek-03",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-03.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mely két sorsdöntő történelmi esemény kapcsolódik október 23-hoz?",
                "options": [
                    "Az 1956-os forradalom kitörése és a Magyar Köztársaság 1989-es kikiáltása.",
                    "A mohácsi csata és a pozsonyi csata.",
                    "István király megkoronázása és halála."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemzet tisztelettel adózik az 1956-os forradalom mártírjai elő_____. (postposition - tt)",
                "answer": "tt"
            },
            {
                "id": "b1-nemzetiunnepek-03.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "lyukas", "zászló", "az", "1956-os", "forradalom", "halhatatlan", "szimbóluma."],
                "solution": ["A", "lyukas", "zászló", "az", "1956-os", "forradalom", "halhatatlan", "szimbóluma."]
            },
            {
                "id": "b1-nemzetiunnepek-03.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Kik indították el a békés tüntetést 1956. október 23-án délután Budapesten?",
                "options": [
                    "Az egyetemi diákok és fiatalok.",
                    "A szovjet tábornokok.",
                    "A külföldi diplomaták."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1989. október 23-án a Parlament erkélyéről kikiáltották a Magyar Köztársaság_____. (accusative - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-nemzetiunnepek-03.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen ünnepi megemlékezést tartanak hagyományosan október 22-én este Budapesten?",
                "options": [
                    "Fáklyás felvonulást a Műegyetemtől a Bem-szoborhoz az 1956-os ifjúság útvonalán.",
                    "Katonai díszszemlét repülőgépekkel.",
                    "Csendes könyvvásárt a Vörösmarty téren."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Október 23-a Magyarország kettős történelmi ünnepének számí_____. (counts as - k)",
                "answer": "k"
            },
            {
                "id": "b1-nemzetiunnepek-03.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "nép", "mindig", "hű", "marad", "a", "szabadság", "eszméjéhez."],
                "solution": ["A", "magyar", "nép", "mindig", "hű", "marad", "a", "szabadság", "eszméjéhez."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-nemzetiunnepek-04",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-04.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mire emlékezik a magyar nemzet október 6-án, a hivatalos nemzeti gyásznapon?",
                "options": [
                    "Az aradi vértanúkra (13 honvédtábornokra) és Batthyány Lajos miniszterelnökre, akiket 1849-ben végeztek ki.",
                    "A mohácsi csatavesztésre.",
                    "A tatárjárás áldozataira."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Október 6-án a nemzet néma főhajtással emlékezik a hősök áldozatára, és koszorút helyez _____ az emlékműveknél. (prefix - el)",
                "answer": "el"
            },
            {
                "id": "b1-nemzetiunnepek-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Június", "4-e", "a", "Nemzeti", "Összetartozás", "Napja", "Magyarországon."],
                "solution": ["Június", "4-e", "a", "Nemzeti", "Összetartozás", "Napja", "Magyarországon."]
            },
            {
                "id": "b1-nemzetiunnepek-04.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik történelmi esemény évfordulója június 4-e?",
                "options": [
                    "Az 1920-as trianoni békediktátum aláírásának napja.",
                    "A nándorfehérvári diadal napja.",
                    "Buda visszafoglalása a töröktől."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Gróf Batthyány Lajos volt az első felelős magyar miniszterelnök, akit Pesten végeztek _____. (prefix - ki)",
                "answer": "ki"
            },
            {
                "id": "b1-nemzetiunnepek-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi az üzenete a Nemzeti Összetartozás Napjának a modern Magyarországon?",
                "options": [
                    "Hogy a határok elválasztanak, de a közös nyelv, kultúra és történelem örökre összeköti a világ magyarságát.",
                    "Hogy minden határt azonnal le kell zárni.",
                    "Hogy el kell felejteni a külhoni magyarokat."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az aradi vértanúk emléke örökké élni fog a nemzet szívé_____. (inessive - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-nemzetiunnepek-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "történelmi", "emlékezet", "erősíti", "a", "nemzet", "összetartozását."],
                "solution": ["A", "történelmi", "emlékezet", "erősíti", "a", "nemzet", "összetartozását."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-nemzetiunnepek-05",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-05.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik nap a Kommunista Diktatúrák Áldozatainak Emléknapja Magyarországon?",
                "options": [
                    "Február 25-e (Kovács Béla kisgazda politikus 1947-es elhurcolásának napja).",
                    "Január 1-je.",
                    "December 24-e."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A totalitárius elnyomás áldozataira méltósággal és tisztelettel emlékez_____. (we remember - ünk)",
                "answer": "ünk"
            },
            {
                "id": "b1-nemzetiunnepek-05.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Április", "16-a", "a", "holokauszt", "magyarországi", "áldozatainak", "emléknapja."],
                "solution": ["Április", "16-a", "a", "holokauszt", "magyarországi", "áldozatainak", "emléknapja."]
            },
            {
                "id": "b1-nemzetiunnepek-05.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Miért pont április 16-át jelölte ki az Országgyűlés a holokauszt magyarországi emléknapjául?",
                "options": [
                    "Mert 1944-ben ezen a napon kezdődött meg Kárpátalján a magyar zsidók gettókba zárása.",
                    "Mert aznap ért véget a második világháború.",
                    "Mert aznap foglalták el Budapestet."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Terror Háza Múzeum hűen bemutatja mindkét diktatúra kegyetlen rémtettei_____. (accusative plural - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetiunnepek-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit szimbolizál a budapesti Duna-parton található híres 'Cipők a Duna-parton' holokauszt-emlékmű?",
                "options": [
                    "A nyilas fegyveresek által a Dunába lőtt ártatlan zsidó áldozatok emlékét.",
                    "Egy korabeli cipőgyár termékeit.",
                    "A budapesti divathét szabadtéri installációját."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ezek a tragédiák örök figyelmeztetésként szolgál_____ a szabadság és az emberi élet védelmére. (serve - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-nemzetiunnepek-05.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "emberi", "méltóság", "és", "a", "szabadság", "mindenek", "felett", "áll."],
                "solution": ["Az", "emberi", "méltóság", "és", "a", "szabadság", "mindenek", "felett", "áll."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-nemzetiunnepek-consolidation",
        "exercises": [
            {
                "id": "b1-nemzetiunnepek-consolidation.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik a három hivatalos magyar nemzeti ünnep?",
                "options": [
                    "Március 15., Augusztus 20. és Október 23.",
                    "Május 1., Június 4. és Október 6.",
                    "Január 1., Pünkösd és Karácsony."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex02",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "Március 15. az 1848-as forradalom, Augusztus 20. az államalapítás, Október 23. pedig az 1956-os forradalom ünne_____. (its holiday - pe)",
                "answer": "pe"
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Október", "6-án", "az", "aradi", "vértanúk", "hősiességére", "emlékezünk."],
                "solution": ["Október", "6-án", "az", "aradi", "vértanúk", "hősiességére", "emlékezünk."]
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik nemzeti ünnephez kapcsolódik az 'új kenyér ünnepe' és a tisztavatás?",
                "options": [
                    "Augusztus 20-hoz (Szent István napjához).",
                    "Március 15-höz.",
                    "Október 23-hoz."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex05",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "Június 4-e a Nemzeti Összetartozás Napja a trianoni békeszerződés aláírásának emléké_____. (in its memory - re)",
                "answer": "re"
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "nemzeti", "ünnepek", "összefogják", "a", "magyar", "társadalmat."],
                "solution": ["A", "nemzeti", "ünnepek", "összefogják", "a", "magyar", "társadalmat."]
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex07",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "Február 25-e a kommunizmus, április 16-a pedig a holokauszt áldozatainak emléknap_____. (its day - ja)",
                "answer": "ja"
            },
            {
                "id": "b1-nemzetiunnepek-consolidation.ex08",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mi a célja a magyar állampolgársági eskü letételének a nemzeti ünnepek és a haza tükrében?",
                "options": [
                    "Hogy az új állampolgár hitet tegyen a magyar nemzet, annak törvényei, nyelve, kultúrája és szabadsága mellett.",
                    "Hogy az új polgár ingyen belépőt kapjon a múzeumokba.",
                    "Hogy elmondja kedvenc versét a polgármesternek."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetiunnepek-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Március 15.: A polgári forradalom és szabadságharc", "March 15th: Civic Revolution & Freedom"),
        "02": ("Augusztus 20.: Államalapítás és Szent István ünnepe", "August 20th: State Founding & Saint Stephen"),
        "03": ("Október 23.: 1956 forradalma és a Köztársaság", "October 23rd: 1956 Revolution & Republic"),
        "04": ("Október 6. és Június 4.: Vértanúk és Összetartozás", "October 6 & June 4: Martyrs & National Cohesion"),
        "05": ("A totalitárius diktatúrák áldozatainak emléknapjai", "Memorial Days for Victims of Totalitarianism")
    }

    story_refs = {
        "01": "stories/world/b1/b1-nemzetiunnepek-01-marcius15.json",
        "02": "stories/world/b1/b1-nemzetiunnepek-02-augusztus20.json",
        "03": "stories/world/b1/b1-nemzetiunnepek-03-oktober23.json",
        "04": "stories/world/b1/b1-nemzetiunnepek-04-emleknapok.json",
        "05": "stories/world/b1/b1-nemzetiunnepek-05-aldozatok.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.nemzetiunnepek-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Commemorative Syntax, State Protocol & Solemn Historical Memorialization",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and explain {en_t} in Hungarian.",
                        "I can use commemorative, ceremonial, and historical Hungarian vocabulary.",
                        "I can answer essential citizenship exam questions regarding March 15, August 20, October 23, October 6, and June 4.",
                        "I can master six target vocabulary items in authentic cultural context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-nemzetiunnepek-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-nemzetiunnepek-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-nemzetiunnepek-{padded}-ex.json",
                    "exerciseRefs": [f"b1-nemzetiunnepek-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-nemzetiunnepek-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.nemzetiunnepek-consolidation",
        "title": "Összefoglalás: Nemzeti ünnepek és emléknapok (National Holidays Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of National Holidays, Memorial Days & Civic Historical Memory",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-nemzetiunnepek.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-nemzetiunnepek-consolidation-ex.json",
                "exerciseRefs": [f"b1-nemzetiunnepek-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetiunnepek-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 30 (b1-nemzetiunnepek)!")

if __name__ == "__main__":
    build_unit_30_citizenship()
