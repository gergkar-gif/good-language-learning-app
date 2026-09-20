#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 33: Local Governments & Public Administration (b1-onkormanyzat)."""

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

def build_unit_33_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.onkormanyzat.01",
        "lesson": "b1-onkormanyzat-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "helyi önkormányzat", "translation": "local government, municipality", "pos": "noun"},
            {"lemma": "önkormányzatiság", "translation": "local autonomy, municipal self-governance", "pos": "noun"},
            {"lemma": "település", "translation": "settlement, locality, populated place", "pos": "noun"},
            {"lemma": "község", "translation": "village, rural municipality", "pos": "noun"},
            {"lemma": "város", "translation": "city, town, urban municipality", "pos": "noun"},
            {"lemma": "főváros és kerületek", "translation": "capital city and its municipal districts", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-onkormanyzat-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.onkormanyzat.02",
        "lesson": "b1-onkormanyzat-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "polgármester", "translation": "mayor, head of the local municipality", "pos": "noun"},
            {"lemma": "képviselő-testület", "translation": "body of representatives, municipal council", "pos": "noun"},
            {"lemma": "főpolgármester", "translation": "Lord Mayor (head of Budapest municipality)", "pos": "noun"},
            {"lemma": "helyi rendelet", "translation": "local municipal decree, municipal bylaw", "pos": "noun"},
            {"lemma": "jegyző", "translation": "town clerk, chief administrative officer, notary", "pos": "noun"},
            {"lemma": "polgármesteri hivatal", "translation": "mayor's office, town hall, municipal secretariat", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-onkormanyzat-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.onkormanyzat.03",
        "lesson": "b1-onkormanyzat-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vármegye", "translation": "county (traditional territorial administrative division of Hungary)", "pos": "noun"},
            {"lemma": "vármegyei önkormányzat", "translation": "county self-government, county municipality", "pos": "noun"},
            {"lemma": "vármegyei közgyűlés", "translation": "county general assembly", "pos": "noun"},
            {"lemma": "megyei jogú város", "translation": "city with county rights (urban center with county-level status)", "pos": "noun"},
            {"lemma": "területi közigazgatás", "translation": "territorial public administration", "pos": "noun"},
            {"lemma": "településfejlesztés", "translation": "regional and settlement development, spatial planning", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-onkormanyzat-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.onkormanyzat.04",
        "lesson": "b1-onkormanyzat-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kormányhivatal", "translation": "government office (capital or county state administrative office)", "pos": "noun"},
            {"lemma": "főispán", "translation": "lord lieutenant, government commissioner heading the county government office", "pos": "noun"},
            {"lemma": "járás", "translation": "district (sub-county administrative territorial subdivision)", "pos": "noun"},
            {"lemma": "járási hivatal", "translation": "district administrative office", "pos": "noun"},
            {"lemma": "kormányablak", "translation": "Citizen Window, one-stop integrated state administrative customer service center", "pos": "noun"},
            {"lemma": "ügyintézés", "translation": "official paperwork, handling of administrative procedures", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-onkormanyzat-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.onkormanyzat.05",
        "lesson": "b1-onkormanyzat-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "helyi közszolgáltatás", "translation": "local public service (utilities, schooling, cleaning)", "pos": "noun"},
            {"lemma": "közvilágítás", "translation": "public street lighting", "pos": "noun"},
            {"lemma": "hulladékgazdálkodás", "translation": "municipal waste management, refuse collection", "pos": "noun"},
            {"lemma": "helyi adó", "translation": "local municipal tax (e.g. property, local business tax)", "pos": "noun"},
            {"lemma": "helyi népszavazás", "translation": "local municipal referendum", "pos": "noun"},
            {"lemma": "közmeghallgatás", "translation": "public hearing, municipal town hall meeting", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-onkormanyzat-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.onkormanyzat.01.municipal-competence",
        "title": "Municipal Autonomy: Gondoskodik vmiről & Igazgatja ügyeit",
        "sections": [
            {
                "type": "text",
                "title": "Local Self-Governance",
                "content": "Hungarian constitutional law defines municipalities as autonomous communities: *gondoskodik a helyi közügyekről* (cares for local public affairs) and *önállóan igazgatja ügyeit* (manages its affairs autonomously). The verb *gondoskodik* governs the delative case (*-ról/-ről*)."
            },
            {
                "type": "examples",
                "title": "Municipal competence examples",
                "items": [
                    {"spanish": "A helyi önkormányzat a választópolgárok közösségét képviseli.", "english": "The local government represents the community of voters."},
                    {"spanish": "A település önállóan gondoskodik a helyi közügyek intézéséről.", "english": "The locality independently attends to the administration of local public affairs."},
                    {"spanish": "Magyarországon minden községnek és városnak joga van az önkormányzatisághoz.", "english": "In Hungary, every village and town has the right to local self-governance."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-onkormanyzat-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.onkormanyzat.02.mayoral-powers",
        "title": "Mayoral & Council Governance: Rendeletet alkot & Irányít",
        "sections": [
            {
                "type": "text",
                "title": "Administrative Authority",
                "content": "Describing municipal management uses standard administrative verbal collocations: the representative body *rendeletet alkot* (issues a local decree) and *dönt a költségvetésről* (decides on the budget), while the mayor *vezeti az ülést* (chairs the meeting) and the clerk (*jegyző*) *vezeti a hivatalt* (heads the administrative office)."
            },
            {
                "type": "examples",
                "title": "Mayoral power examples",
                "items": [
                    {"spanish": "A polgármestert a helyi lakosok közvetlenül választják meg öt évre.", "english": "The mayor is directly elected by local residents for a term of five years."},
                    {"spanish": "A képviselő-testület helyi rendeleteket alkot a település rendjéről.", "english": "The body of representatives passes local decrees regarding the order of the town."},
                    {"spanish": "A jegyző felel a hivatal szakszerű és törvényes működéséért.", "english": "The town clerk is responsible for the professional and lawful functioning of the town hall."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-onkormanyzat-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.onkormanyzat.03.regional-coordination",
        "title": "County Competencies: Összehangol & Fejlesztési feladatok",
        "sections": [
            {
                "type": "text",
                "title": "Regional Coordination",
                "content": "Hungary's 19 counties (*vármegyék*) focus on strategic territorial development: *összehangolja a településfejlesztést* (coordinates regional development) and *képviseli a vármegye területét* (represents the county territory). Cities with county rights (*megyei jogú városok*) exercise both municipal and county-level tasks."
            },
            {
                "type": "examples",
                "title": "Regional coordination examples",
                "items": [
                    {"spanish": "Magyarország területe tizenkilenc vármegyére és a fővárosra oszlik.", "english": "Hungary's territory is divided into nineteen counties and the capital city."},
                    {"spanish": "A vármegyei közgyűlés dönt a területi fejlesztési tervekről.", "english": "The county general assembly decides on regional development plans."},
                    {"spanish": "A megyei jogú városok önállóan látják el a vármegyei feladatokat is.", "english": "Cities with county rights independently carry out county-level tasks as well."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-onkormanyzat-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.onkormanyzat.04.administrative-procedures",
        "title": "Public Administration: Ügyet intéz a kormányablakban",
        "sections": [
            {
                "type": "text",
                "title": "One-Stop Citizen Services",
                "content": "Interacting with state administrative agencies involves procedural vocabulary: *ügyet intéz a kormányablakban* (conducts paperwork at the Citizen Window), *kérelmet nyújt be* (submits an application), and *hatósági bizonyítványt állít ki* (issues an official certificate)."
            },
            {
                "type": "examples",
                "title": "Administrative procedure examples",
                "items": [
                    {"spanish": "Az állampolgárok a kormányablakokban intézhetik hivatalos ügyeiket.", "english": "Citizens can handle their official matters at the Citizen Windows."},
                    {"spanish": "A kormányhivatalt a miniszterelnök javaslatára kinevezett főispán vezeti.", "english": "The government office is headed by the lord lieutenant appointed on the proposal of the Prime Minister."},
                    {"spanish": "A járási hivatalok intézik a helyi okmányok és engedélyek kiadását.", "english": "District offices handle the issuance of local personal documents and permits."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-onkormanyzat-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.onkormanyzat.05.civic-participation",
        "title": "Civic Participation: Helyi népszavazás & Közmeghallgatás",
        "sections": [
            {
                "type": "text",
                "title": "Direct Local Democracy",
                "content": "Residents influence community affairs through direct participation: *helyi népszavazást kezdeményez* (initiates a local referendum), *kérdést tesz fel a közmeghallgatáson* (asks questions at the public hearing), and *befizeti a helyi adót* (pays the municipal tax)."
            },
            {
                "type": "examples",
                "title": "Civic participation examples",
                "items": [
                    {"spanish": "A képviselő-testület évente legalább egyszer közmeghallgatást tart.", "english": "The body of representatives holds a public hearing at least once a year."},
                    {"spanish": "A helyi lakosok népszavazáson dönthetnek fontos közösségi kérdésekről.", "english": "Local residents can decide on important community questions in a referendum."},
                    {"spanish": "A település bevételeit a helyi adók és az állami támogatások biztosítják.", "english": "The locality's revenues are ensured by local taxes and state subsidies."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-onkormanyzat-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 Serialized + 1 Combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.onkormanyzat.01",
        "title": "A helyi önkormányzatok szerepe: a közösségek önrendelkezése",
        "level": "B1",
        "lesson": 1,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The constitutional foundations of Hungarian local government: municipal autonomy, villages, towns, and capital districts.",
        "characters": [],
        "location": "Magyarországi települések és önkormányzatok",
        "grammar": [
            "grammar.b1.onkormanyzat.01.municipal-competence"
        ],
        "vocabularyTopics": [
            "helyi önkormányzat",
            "önkormányzatiság",
            "település",
            "község",
            "város"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország demokratikus berendezkedésének egyik legfontosabb pillére a helyi önkormányzatiság. Az Alaptörvény kimondja, hogy a helyi közösségeknek alkotmányos joguk van önállóan dönteni a mindennapi életüket érintő közügyekről."
            },
            {
                "type": "narration",
                "text": "Nem minden döntést a budapesti minisztériumokban kell meghozni: a falu vagy a város lakói tudják a legjobban, mire van szükségük a saját utcájukban, iskolájukban vagy rendelőjükben."
            },
            {
                "type": "narration",
                "text": "Magyarországon a települési önkormányzatok közé tartoznak a községek, a nagyközségek, a városok, a megyei jogú városok, valamint a főváros és annak huszonhárom kerülete."
            },
            {
                "type": "narration",
                "text": "Minden településen a helyi választópolgárok választják meg azokat a képviselőket, akik a közösség jövőjét irányítják és kezelik a helyi vagyont."
            },
            {
                "type": "narration",
                "text": "Ez az önállóság biztosítja, hogy a magyar közigazgatás közvetlenül az állampolgárok szolgálatában álljon."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat-01-onkormanyzatok.json", story_01)

    story_02 = {
        "id": "story.b1.onkormanyzat.02",
        "title": "A polgármester és a képviselő-testület: a település vezetése",
        "level": "B1",
        "lesson": 2,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The executive leadership of the mayor, legislative function of the representative body, and administrative role of the town clerk.",
        "characters": [],
        "location": "Polgármesteri hivatal, városháza",
        "grammar": [
            "grammar.b1.onkormanyzat.02.mayoral-powers"
        ],
        "vocabularyTopics": [
            "polgármester",
            "képviselő-testület",
            "főpolgármester",
            "helyi rendelet",
            "jegyző"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A település első számú választott politikai vezetője a polgármester, akit a helyi lakosok közvetlenül választanak meg öt évre."
            },
            {
                "type": "narration",
                "text": "Budapest egészét a főpolgármester vezeti, míg a huszonhárom fővárosi kerület élén kerületi polgármesterek állnak."
            },
            {
                "type": "narration",
                "text": "A polgármester munkáját a képviselő-testület támogatja és ellenőrzi. A testület nyilvános üléseken dönt a költségvetésről és alkot helyi rendeleteket."
            },
            {
                "type": "narration",
                "text": "A helyi rendeletek a település kötelező jogszabályai, amelyek azonban soha nem lehetnek ellentétesek a magasabb szintű országos törvényekkel."
            },
            {
                "type": "narration",
                "text": "A polgármesteri hivatal szakszerű és törvényes működéséért a jegyző felel, aki képzett közigazgatási szakemberként őrzi a jogszerűséget."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat-02-polgarmester.json", story_02)

    story_03 = {
        "id": "story.b1.onkormanyzat.03",
        "title": "A magyar vármegyék és a területi közigazgatás",
        "level": "B1",
        "lesson": 3,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Hungary's 19 counties, Saint Stephen's historical royal counties, the county assembly, and cities with county rights.",
        "characters": [],
        "location": "Magyarország 19 vármegyéje és megyei jogú városai",
        "grammar": [
            "grammar.b1.onkormanyzat.03.regional-coordination"
        ],
        "vocabularyTopics": [
            "vármegye",
            "vármegyei önkormányzat",
            "vármegyei közgyűlés",
            "megyei jogú város",
            "településfejlesztés"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A vármegye több mint ezeréves múltra tekint vissza a magyar államiság történetében: Szent István király alapította meg a királyi vármegyék szilárd hálózatát."
            },
            {
                "type": "narration",
                "text": "Ma Magyarország területe tizenkilenc vármegyére és a fővárosra oszlik. A vármegyék a regionális szintű önkormányzatiságot képviselik."
            },
            {
                "type": "narration",
                "text": "A vármegyei önkormányzat döntéshozó szerve a vármegyei közgyűlés, amelynek tagjait a vármegye választópolgárai pártlistákon választják meg."
            },
            {
                "type": "narration",
                "text": "A vármegyék fő feladata a térségi területfejlesztés, a vidéki gazdaság koordinálása, valamint a környezetvédelmi és turisztikai programok összehangolása."
            },
            {
                "type": "narration",
                "text": "Emellett a huszonöt legnagyobb vidéki település megyei jogú városként működik, így saját határain belül önállóan látja el a vármegyei hatásköröket is."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat-03-varmegyek.json", story_03)

    story_04 = {
        "id": "story.b1.onkormanyzat.04",
        "title": "A kormányablakok és a járási hivatalok világa",
        "level": "B1",
        "lesson": 4,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "State territorial administration, county government offices headed by the főispán, districts, and the one-stop Citizen Windows.",
        "characters": [],
        "location": "Kormányablakok és járási hivatalok országszerte",
        "grammar": [
            "grammar.b1.onkormanyzat.04.administrative-procedures"
        ],
        "vocabularyTopics": [
            "kormányhivatal",
            "főispán",
            "járás",
            "járási hivatal",
            "kormányablak",
            "ügyintézés"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A választott önkormányzatok mellett országszerte működik a területi államigazgatás rendszere is, amely a központi Kormány hatásköreit gyakorolja."
            },
            {
                "type": "narration",
                "text": "Minden vármegyében és Budapesten kormányhivatal működik, amelyet a miniszterelnök javaslatára kinevezett főispán vezet."
            },
            {
                "type": "narration",
                "text": "A vármegyék kisebb közigazgatási egységekre, úgynevezett járásokra oszlanak. Magyarországon ma 174 járás működik a vármegyékben."
            },
            {
                "type": "narration",
                "text": "A járási hivatalok legismertebb ügyfélszolgálati központjai a kormányablakok. Itt valósul meg az úgynevezett egyablakos ügyintézés."
            },
            {
                "type": "narration",
                "text": "A polgárok egyetlen helyen intézhetik személyi igazolványukat, útlevelüket, jogosítványukat, lakcímkártyájukat és családtámogatási kérelmeiket."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat-04-kormanyablak.json", story_04)

    story_05 = {
        "id": "story.b1.onkormanyzat.05",
        "title": "Helyi közszolgáltatások és a helyi demokrácia eszközei",
        "level": "B1",
        "lesson": 5,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Municipal public services (utilities, kindergartens, waste management), municipal taxes, public hearings, and local referendums.",
        "characters": [],
        "location": "A helyi közösség élete",
        "grammar": [
            "grammar.b1.onkormanyzat.05.civic-participation"
        ],
        "vocabularyTopics": [
            "helyi közszolgáltatás",
            "közvilágítás",
            "hulladékgazdálkodás",
            "helyi adó",
            "helyi népszavazás",
            "közmeghallgatás"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A települések mindennapi működését a megbízható helyi közszolgáltatások biztosítják: ivóvízellátás, csatornázás, közvilágítás és hulladékgazdálkodás."
            },
            {
                "type": "narration",
                "text": "Az önkormányzatok tartják fenn az óvodákat, a háziorvosi rendelőket, a helyi könyvtárakat, valamint gondozzák a közterületeket és parkokat."
            },
            {
                "type": "narration",
                "text": "E feladatok ellátását a helyben beszedett adók (pl. építményadó, iparűzési adó) és a központi költségvetési támogatások fedezik."
            },
            {
                "type": "narration",
                "text": "A helyi demokrácia fontos eszköze az évente kötelező közmeghallgatás, ahol bármely lakos közvetlenül kérdezheti a polgármestert és képviselőket."
            },
            {
                "type": "narration",
                "text": "Kiemelkedő helyi ügyekben a választópolgárok helyi népszavazást kezdeményezhetnek, amely közvetlen döntési jogot ad a közösség kezébe."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat-05-kozszolgaltatas.json", story_05)

    story_comb = {
        "id": "story.b1.onkormanyzat",
        "title": "Helyi önkormányzatok és területi közigazgatás Magyarországon",
        "level": "B1",
        "lesson": 33,
        "order": 33,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive compendium on local self-government, municipalities, mayors, counties, Citizen Windows, and public services in Hungary.",
        "characters": [],
        "location": "Magyarország önkormányzati rendszere és közigazgatása",
        "grammar": [
            "grammar.b1.onkormanyzat.01.municipal-competence",
            "grammar.b1.onkormanyzat.02.mayoral-powers",
            "grammar.b1.onkormanyzat.03.regional-coordination",
            "grammar.b1.onkormanyzat.04.administrative-procedures",
            "grammar.b1.onkormanyzat.05.civic-participation"
        ],
        "vocabularyTopics": [
            "helyi önkormányzat",
            "polgármester",
            "vármegye",
            "kormányablak",
            "közszolgáltatás",
            "helyi népszavazás"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország alkotmányos rendjében a helyi önkormányzatiság az állampolgárok közvetlen önrendelkezését és a helyi közügyek önálló intézését szolgálja."
            },
            {
                "type": "narration",
                "text": "A települések – községek, városok, megyei jogú városok, valamint Budapest és kerületei – saját választott polgármesterrel és képviselő-testülettel rendelkeznek."
            },
            {
                "type": "narration",
                "text": "A képviselő-testület helyi rendeleteket alkot, elfogadja a költségvetést, míg a jegyző a szakmai apparátust vezetve őrzi a törvényességet."
            },
            {
                "type": "narration",
                "text": "Regionális szinten a tizenkilenc vármegye önkormányzata összehangolja a térségi területfejlesztési, vidéki gazdasági és környezeti terveket."
            },
            {
                "type": "narration",
                "text": "Az államigazgatást a vármegyékben a főispán vezette kormányhivatalok és a járási hivatalok látják el, ahol a kormányablakok egyablakos rendszere biztosítja a modern ügyintézést."
            },
            {
                "type": "narration",
                "text": "A helyi közszolgáltatások megbízhatósága, valamint a közmeghallgatások és helyi népszavazások intézménye garancia arra, hogy a hatalom a polgárok javát szolgálja."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-onkormanyzat.json", story_comb)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 8 exercises each)
    # -------------------------------------------------------------------------
    # Lesson 01 Exercises
    ex_01 = {
        "lesson": "b1-onkormanyzat-01",
        "exercises": [
            {
                "id": "b1-onkormanyzat-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az önkormányzatiság a magyar Alaptörvény szerint?",
                "options": [
                    "A helyi közösségek jogát a helyi közügyek önálló intézésére és eldöntésére.",
                    "A központi minisztériumok teljes ellenőrzését minden falu felett.",
                    "A polgárok kötelező katonai szolgálatát saját falujukban."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A települési önkormányzat önállóan gondoskodik a helyi közügyek intézésé_____. (of its administration - ről)",
                "answer": "ről"
            },
            {
                "id": "b1-onkormanyzat-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "helyi", "önkormányzat", "a", "választópolgárok", "közösségét", "képviseli."],
                "solution": ["A", "helyi", "önkormányzat", "a", "választópolgárok", "közösségét", "képviseli."]
            },
            {
                "id": "b1-onkormanyzat-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány kerületre oszlik a magyar főváros, Budapest?",
                "options": [
                    "Huszonhárom kerületre.",
                    "Tizenkilenc kerületre.",
                    "Tíz kerületre."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden magyar községnek joga van az önkormányzatiság_____. (to self-governance - hoz)",
                "answer": "hoz"
            },
            {
                "id": "b1-onkormanyzat-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Ki választja meg a helyi önkormányzati képviselőket?",
                "options": [
                    "A helyi választópolgárok a választásokon.",
                    "A köztársasági elnök kinevezéssel.",
                    "A parlament elnöke határozatban."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A település önállóan kezeli a helyi vagyon_____ . (assets - t)",
                "answer": "t"
            },
            {
                "id": "b1-onkormanyzat-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "helyi", "közösség", "ismeri", "legjobban", "a", "saját", "igényeit."],
                "solution": ["A", "helyi", "közösség", "ismeri", "legjobban", "a", "saját", "igényeit."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-01-ex.json", ex_01)

    # Lesson 02 Exercises
    ex_02 = {
        "lesson": "b1-onkormanyzat-02",
        "exercises": [
            {
                "id": "b1-onkormanyzat-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány évre választják meg a polgármestert Magyarországon?",
                "options": [
                    "Öt évre.",
                    "Négy évre.",
                    "Hat évre."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A hivatal szakszerű és törvényes működéséért a jegyző felel_____. (is responsible - no ending, stem only)",
                "answer": "felel"
            },
            {
                "id": "b1-onkormanyzat-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "képviselő-testület", "helyi", "rendeleteket", "alkot", "a", "településen."],
                "solution": ["A", "képviselő-testület", "helyi", "rendeleteket", "alkot", "a", "településen."]
            },
            {
                "id": "b1-onkormanyzat-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a helyi rendelet?",
                "options": [
                    "A képviselő-testület által hozott, a településen kötelező jogszabály.",
                    "A miniszterelnök személyes levele a polgármesternek.",
                    "A helyi újság szerkesztőségi cikke."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A helyi rendelet nem lehet ellentétes a magasabb szintű törvények_____. (with laws - kel)",
                "answer": "kel"
            },
            {
                "id": "b1-onkormanyzat-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Ki vezeti Budapest főváros egészének önkormányzatát?",
                "options": [
                    "A főpolgármester.",
                    "A belügyminiszter.",
                    "A kerületi jegyző."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A képviselő-testület ülései a nyilvánosság számára nyitott_____ . (open - ak)",
                "answer": "ak"
            },
            {
                "id": "b1-onkormanyzat-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "polgármestert", "a", "helyi", "lakosok", "közvetlenül", "választják", "meg."],
                "solution": ["A", "polgármestert", "a", "helyi", "lakosok", "közvetlenül", "választják", "meg."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-02-ex.json", ex_02)

    # Lesson 03 Exercises
    ex_03 = {
        "lesson": "b1-onkormanyzat-03",
        "exercises": [
            {
                "id": "b1-onkormanyzat-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány vármegye van Magyarországon?",
                "options": [
                    "Tizenkilenc vármegye.",
                    "Húsz vármegye.",
                    "Huszonöt vármegye."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vármegyék rendszerét Szent István király alapít_____ meg. (founded - otta)",
                "answer": "otta"
            },
            {
                "id": "b1-onkormanyzat-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "vármegyék", "összehangolják", "a", "térségi", "területfejlesztési", "terveket."],
                "solution": ["A", "vármegyék", "összehangolják", "a", "térségi", "területfejlesztési", "terveket."]
            },
            {
                "id": "b1-onkormanyzat-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a megyei jogú város sajátossága?",
                "options": [
                    "Saját területén a vármegyei önkormányzati feladatokat is maga látja el.",
                    "Független a magyar Alaptörvénytől.",
                    "Nem tarthat helyi választásokat."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-03.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vármegyei közgyűlés dönt a fejlesztési tervek_____. (about plans - ről)",
                "answer": "ről"
            },
            {
                "id": "b1-onkormanyzat-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan választják meg a vármegyei közgyűlés tagjait?",
                "options": [
                    "Pártlistás arányos választási rendszerben.",
                    "A miniszterelnök személyes kinevezésével.",
                    "A polgármesterek sorsolásával."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A huszonöt legnagyobb vidéki város megyei jogú városként működ_____ . (operates - ik)",
                "answer": "ik"
            },
            {
                "id": "b1-onkormanyzat-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Magyarország", "területe", "tizenkilenc", "vármegyére", "és", "Budapestre", "oszlik."],
                "solution": ["Magyarország", "területe", "tizenkilenc", "vármegyére", "és", "Budapestre", "oszlik."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-03-ex.json", ex_03)

    # Lesson 04 Exercises
    ex_04 = {
        "lesson": "b1-onkormanyzat-04",
        "exercises": [
            {
                "id": "b1-onkormanyzat-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'kormányablak' a mai magyar közigazgatásban?",
                "options": [
                    "Egyablakos, integrált ügyfélszolgálati központ hivatalos okmányok intézésére.",
                    "A parlament épületének díszes bejárata.",
                    "Egy állami televízióműsor neve."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vármegyei kormányhivatalt a miniszterelnök által javasolt főispán vezet_____. (leads - i)",
                "answer": "i"
            },
            {
                "id": "b1-onkormanyzat-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kormányablakban", "gyorsan", "intézhetjük", "el", "a", "személyi", "igazolványt."],
                "solution": ["A", "kormányablakban", "gyorsan", "intézhetjük", "el", "a", "személyi", "igazolványt."]
            },
            {
                "id": "b1-onkormanyzat-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen szintű területi egységekre oszlanak a vármegyék az államigazgatásban?",
                "options": [
                    "Járásokra.",
                    "Kantonokra.",
                    "Kormányzóságokra."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az állampolgárok kényelmesen intézik el hivatalos ügyeik_____. (their affairs - et)",
                "answer": "et"
            },
            {
                "id": "b1-onkormanyzat-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mi a különbség az önkormányzat és a kormányhivatal között?",
                "options": [
                    "Az önkormányzatot a lakosok választják, a kormányhivatal pedig a központi kormány kirendeltsége.",
                    "Nincs különbség, mindkettőt a polgármester irányítja.",
                    "Az önkormányzat bíróságként működik."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A járási hivatalok intézik a helyi okmányok és engedélyek kiadásá_____ . (their issuance - t)",
                "answer": "t"
            },
            {
                "id": "b1-onkormanyzat-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "vármegyék", "kisebb", "területi", "egységekre,", "járásokra", "oszlanak."],
                "solution": ["A", "vármegyék", "kisebb", "területi", "egységekre,", "járásokra", "oszlanak."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-04-ex.json", ex_04)

    # Lesson 05 Exercises
    ex_05 = {
        "lesson": "b1-onkormanyzat-05",
        "exercises": [
            {
                "id": "b1-onkormanyzat-05.ex01",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen közszolgáltatásokról gondoskodik a helyi települési önkormányzat?",
                "options": [
                    "Ivóvízellátásról, közvilágításról, szemétszállításról és óvodák fenntartásáról.",
                    "Honvédelemről és külpolitikáról.",
                    "Autópályák nemzetközi díjainak beszedéséről."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A képviselő-testület évente legalább egyszer közmeghallgatás_____ tart a lakosoknak. (public hearing - t)",
                "answer": "t"
            },
            {
                "id": "b1-onkormanyzat-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "lakosok", "helyi", "népszavazáson", "dönthetnek", "fontos", "közösségi", "kérdésekről."],
                "solution": ["A", "lakosok", "helyi", "népszavazáson", "dönthetnek", "fontos", "közösségi", "kérdésekről."]
            },
            {
                "id": "b1-onkormanyzat-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit tehet a polgár egy közmeghallgatáson?",
                "options": [
                    "Kérdést tehet fel a polgármesternek és javaslatot nyújthat be a közösség javára.",
                    "Elbocsáthatja a jegyzőt.",
                    "Megváltoztathatja az országos adótörvényeket."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A település bevételeit a helyi adók és állami támogatások biztosít_____ . (ensure - ják)",
                "answer": "ják"
            },
            {
                "id": "b1-onkormanyzat-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor érvényes és eredményes a helyi népszavazás?",
                "options": [
                    "Ha a választópolgárok több mint fele érvényesen szavazott, és többségük azonos választ adott.",
                    "Ha legalább tíz ember részt vesz rajta.",
                    "Ha a polgármester utólag jóváhagyja."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az önkormányzat gondoskodik a tiszta ivóvíz_____ és a hulladékgazdálkodásról. (drinking water - ről)",
                "answer": "ről"
            },
            {
                "id": "b1-onkormanyzat-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "jól", "működő", "önkormányzat", "a", "polgárok", "felelősségvállalásán", "alapul."],
                "solution": ["A", "jól", "működő", "önkormányzat", "a", "polgárok", "felelősségvállalásán", "alapul."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-05-ex.json", ex_05)

    # Consolidation Exercises
    ex_con = {
        "lesson": "b1-onkormanyzat-consolidation",
        "exercises": [
            {
                "id": "b1-onkormanyzat-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kik vezetik a magyarországi települések önkormányzatait?",
                "options": [
                    "A közvetlenül választott polgármester és a képviselő-testület.",
                    "A megyei bírák és katonai vezetők.",
                    "A parlament elnöke és a miniszterek."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A polgármesteri hivatal szakmai vezetéséért és a törvényességért a jegyző felel_____. (is responsible - no suffix needed, felel)",
                "answer": "felel"
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "helyi", "önkormányzat", "önállóan", "rendezi", "a", "település", "közügyeit."],
                "solution": ["A", "helyi", "önkormányzat", "önállóan", "rendezi", "a", "település", "közügyeit."]
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány vármegye és hány budapesti kerület van Magyarországon?",
                "options": [
                    "19 vármegye és 23 fővárosi kerület.",
                    "20 vármegye és 10 kerület.",
                    "12 vármegye és 15 kerület."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vármegyei kormányhivatalt a miniszterelnök javaslatára kinevezett főispán vezet_____. (leads - i)",
                "answer": "i"
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen kötelező ereje van a helyi rendeletnek?",
                "options": [
                    "A település területén mindenkire nézve kötelező érvényű jogszabály.",
                    "Csak önkéntes ajánlás a lakosoknak.",
                    "Csak a polgármesterre kötelező."
                ],
                "correct": 0
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kormányablakokban gyorsan intézhetők a személyi okmány_____ . (documents - ok)",
                "answer": "ok"
            },
            {
                "id": "b1-onkormanyzat-consolidation.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "önkormányzat", "gondoskodik", "az", "ivóvízről", "és", "a", "közvilágításról."],
                "solution": ["Az", "önkormányzat", "gondoskodik", "az", "ivóvízről", "és", "a", "közvilágításról."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-onkormanyzat-consolidation-ex.json", ex_con)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.onkormanyzat-01",
        "unit": 33,
        "title": "A helyi önkormányzatok és az önkormányzatiság (Local Governments & Autonomy)",
        "level": "B1",
        "grammar": "Constitutional Basis of Municipal Autonomy, Local Affairs & Settlements in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain municipal autonomy and self-governance in Hungary.",
                    "I can distinguish settlement types: villages, towns, and capital districts.",
                    "I can use 6 key terms for local self-government and municipal administration.",
                    "I can read the world story about the role of local self-governance."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-onkormanyzat-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-onkormanyzat-01-gr.json"},
            {
                "type": "story",
                "title": "A helyi önkormányzatok szerepe",
                "ref": "stories/world/b1/b1-onkormanyzat-01-onkormanyzatok.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-onkormanyzat-01-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-01.ex01",
                    "b1-onkormanyzat-01.ex02",
                    "b1-onkormanyzat-01.ex03",
                    "b1-onkormanyzat-01.ex04",
                    "b1-onkormanyzat-01.ex05",
                    "b1-onkormanyzat-01.ex06",
                    "b1-onkormanyzat-01.ex07",
                    "b1-onkormanyzat-01.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.onkormanyzat-02",
        "unit": 33,
        "title": "A polgármester és a képviselő-testület vezetése (Mayors, Councils & Decrees)",
        "level": "B1",
        "grammar": "Mayoral Executive Power, Municipal Decrees & Administrative Legality in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the election and powers of the mayor and Lord Mayor.",
                    "I can understand municipal council procedures and local decrees.",
                    "I can explain the legal oversight role of the town clerk (jegyző).",
                    "I can read the story about municipal leadership and town hall administration."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-onkormanyzat-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-onkormanyzat-02-gr.json"},
            {
                "type": "story",
                "title": "A polgármester és a képviselő-testület",
                "ref": "stories/world/b1/b1-onkormanyzat-02-polgarmester.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-onkormanyzat-02-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-02.ex01",
                    "b1-onkormanyzat-02.ex02",
                    "b1-onkormanyzat-02.ex03",
                    "b1-onkormanyzat-02.ex04",
                    "b1-onkormanyzat-02.ex05",
                    "b1-onkormanyzat-02.ex06",
                    "b1-onkormanyzat-02.ex07",
                    "b1-onkormanyzat-02.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.onkormanyzat-03",
        "unit": 33,
        "title": "A magyar vármegyék és a regionális fejlődés (Hungarian Counties & Regional Planning)",
        "level": "B1",
        "grammar": "County Governance, Spatial Planning & Cities with County Rights in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the historical and modern structure of Hungary's 19 counties.",
                    "I can describe the role of the county general assembly in regional development.",
                    "I can explain the special status of cities with county rights.",
                    "I can read the story on the historical continuity of the Hungarian vármegye."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-onkormanyzat-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-onkormanyzat-03-gr.json"},
            {
                "type": "story",
                "title": "A magyar vármegyék és a regionális közigazgatás",
                "ref": "stories/world/b1/b1-onkormanyzat-03-varmegyek.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-onkormanyzat-03-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-03.ex01",
                    "b1-onkormanyzat-03.ex02",
                    "b1-onkormanyzat-03.ex03",
                    "b1-onkormanyzat-03.ex04",
                    "b1-onkormanyzat-03.ex05",
                    "b1-onkormanyzat-03.ex06",
                    "b1-onkormanyzat-03.ex07",
                    "b1-onkormanyzat-03.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.onkormanyzat-04",
        "unit": 33,
        "title": "Kormányhivatalok, járások és kormányablakok (Government Offices & Citizen Windows)",
        "level": "B1",
        "grammar": "State Territorial Administration, Lord Lieutenants (főispán) & Integrated Citizen Services",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can distinguish elected self-governments from central state administrative offices.",
                    "I can describe the county government office headed by the lord lieutenant (főispán).",
                    "I can explain how to handle administrative matters at a Citizen Window (kormányablak).",
                    "I can read the story on one-stop public administration in Hungarian districts."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-onkormanyzat-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-onkormanyzat-04-gr.json"},
            {
                "type": "story",
                "title": "A kormányablakok és a járási hivatalok",
                "ref": "stories/world/b1/b1-onkormanyzat-04-kormanyablak.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-onkormanyzat-04-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-04.ex01",
                    "b1-onkormanyzat-04.ex02",
                    "b1-onkormanyzat-04.ex03",
                    "b1-onkormanyzat-04.ex04",
                    "b1-onkormanyzat-04.ex05",
                    "b1-onkormanyzat-04.ex06",
                    "b1-onkormanyzat-04.ex07",
                    "b1-onkormanyzat-04.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.onkormanyzat-05",
        "unit": 33,
        "title": "Helyi közszolgáltatások és a helyi demokrácia (Local Services & Civic Democracy)",
        "level": "B1",
        "grammar": "Municipal Public Utilities, Local Taxes, Public Hearings & Municipal Referendums",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can identify essential municipal services: water, lighting, waste, kindergartens.",
                    "I can explain local revenue sources: municipal taxes and state grants.",
                    "I can understand civic participation through annual public hearings and local referendums.",
                    "I can read the story on community responsibility and active citizenship."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-onkormanyzat-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-onkormanyzat-05-gr.json"},
            {
                "type": "story",
                "title": "Helyi közszolgáltatások és a helyi demokrácia",
                "ref": "stories/world/b1/b1-onkormanyzat-05-kozszolgaltatas.json"
            },
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-onkormanyzat-05-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-05.ex01",
                    "b1-onkormanyzat-05.ex02",
                    "b1-onkormanyzat-05.ex03",
                    "b1-onkormanyzat-05.ex04",
                    "b1-onkormanyzat-05.ex05",
                    "b1-onkormanyzat-05.ex06",
                    "b1-onkormanyzat-05.ex07",
                    "b1-onkormanyzat-05.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-05.json", lesson_05)

    lesson_con = {
        "id": "lesson.b1.onkormanyzat-consolidation",
        "unit": 33,
        "title": "Unit 33 Consolidation (Helyi önkormányzatok és közigazgatás)",
        "level": "B1",
        "grammar": "Consolidation of Hungarian Local Governance, Municipalities & Administration",
        "sections": [
            {
                "type": "story",
                "title": "Helyi önkormányzatok és területi közigazgatás Magyarországon",
                "ref": "stories/world/b1/b1-onkormanyzat.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-onkormanyzat-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-onkormanyzat-consolidation.ex01",
                    "b1-onkormanyzat-consolidation.ex02",
                    "b1-onkormanyzat-consolidation.ex03",
                    "b1-onkormanyzat-consolidation.ex04",
                    "b1-onkormanyzat-consolidation.ex05",
                    "b1-onkormanyzat-consolidation.ex06",
                    "b1-onkormanyzat-consolidation.ex07",
                    "b1-onkormanyzat-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-onkormanyzat-consolidation.json", lesson_con)

    print("Successfully built Hungarian B1 Citizenship Unit 33 (b1-onkormanyzat)!")

if __name__ == "__main__":
    build_unit_33_citizenship()
