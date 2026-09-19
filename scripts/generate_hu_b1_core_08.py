#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 8: Travel & Mobility (b1-08)."""

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

def build_unit_8_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.08.01",
        "lesson": "b1-08-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "célállomás", "translation": "destination", "pos": "noun"},
            {"lemma": "átszállás", "translation": "transfer, connection", "pos": "noun"},
            {"lemma": "menetrend", "translation": "timetable, schedule", "pos": "noun"},
            {"lemma": "jegykezelés", "translation": "ticket validation / inspection", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-08-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.08.02",
        "lesson": "b1-08-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "alagút", "translation": "tunnel", "pos": "noun"},
            {"lemma": "hágó", "translation": "mountain pass", "pos": "noun"},
            {"lemma": "folyópart", "translation": "riverbank", "pos": "noun"},
            {"lemma": "térkép", "translation": "map", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-08-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.08.03",
        "lesson": "b1-08-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "indulás", "translation": "departure", "pos": "noun"},
            {"lemma": "érkezés", "translation": "arrival", "pos": "noun"},
            {"lemma": "késés", "translation": "delay", "pos": "noun"},
            {"lemma": "tartam", "translation": "duration", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-08-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.08.04",
        "lesson": "b1-08-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "csomag", "translation": "luggage, parcel, baggage", "pos": "noun"},
            {"lemma": "vágány", "translation": "platform, railway track", "pos": "noun"},
            {"lemma": "pótlóbusz", "translation": "replacement bus", "pos": "noun"},
            {"lemma": "panasz", "translation": "complaint", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-08-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.08.05",
        "lesson": "b1-08-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szállás", "translation": "accommodation, lodging", "pos": "noun"},
            {"lemma": "foglalás", "translation": "reservation, booking", "pos": "noun"},
            {"lemma": "látnivaló", "translation": "sight, attraction", "pos": "noun"},
            {"lemma": "útiterv", "translation": "itinerary, travel plan", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-08-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.08.01.motion-postpositions",
        "title": "Postpositions of Motion: keresztül, át, felé, felől",
        "sections": [
            {
                "type": "text",
                "title": "Expressing trajectory and direction with postpositions",
                "content": "In Hungarian, spatial movement often uses postpositions: *keresztül* (through, across), *felé* (towards), and *felől* (from the direction of). Unlike English prepositions, they stand after the noun (which is in the nominative case, or takes a superessive case with *keresztül* / *át*)."
            },
            {
                "type": "examples",
                "title": "Motion postpositions in travel",
                "items": [
                    {
                        "spanish": "A vonat a városon keresztül halad a célállomás felé.",
                        "english": "The train travels through the city towards the destination."
                    },
                    {
                        "spanish": "A hegyek felől hideg szél fújt az állomáson.",
                        "english": "A cold wind was blowing at the station from the direction of the mountains."
                    },
                    {
                        "spanish": "Átszállás nélkül utazhatunk a Balaton felé.",
                        "english": "We can travel towards Lake Balaton without a transfer."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.08.01.public-transport-terms",
        "title": "Navigating Public Transport: átszállás, menetrend",
        "sections": [
            {
                "type": "text",
                "title": "Collocations for tickets and schedules",
                "content": "Key verbal compounds include *átszáll vmire* (to change onto something, taking the sublative *-ra / -re*) and *menetrend szerint* (according to timetable)."
            },
            {
                "type": "examples",
                "title": "Public transit phrases",
                "items": [
                    {
                        "spanish": "A menetrend szerint tíz percünk van az átszállásra.",
                        "english": "According to the schedule, we have ten minutes for the transfer."
                    },
                    {
                        "spanish": "Felszállás előtt érvényesíteni kell a jegyet a jegykezelőnél.",
                        "english": "Before boarding, one must validate the ticket at the ticket validator."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.08.02.verbal-prefixes-motion",
        "title": "Directional Verbal Prefixes: át-, fel-, le-, be-",
        "sections": [
            {
                "type": "text",
                "title": "Verbal prefixes expressing physical crossing and movement",
                "content": "Hungarian verbal prefixes modify motion verbs: *átkel* (to cross over), *átmegy* (to go across), *beér* (to arrive in/reach), and *felmegy* (to go up). When followed by *keresztül* or *-on / -en / -ön át*, they describe crossing terrain like rivers, passes, and tunnels."
            },
            {
                "type": "examples",
                "title": "Crossing terrain",
                "items": [
                    {
                        "spanish": "A vonat lassan haladt át a hosszú alagúton.",
                        "english": "The train passed slowly through the long tunnel."
                    },
                    {
                        "spanish": "Gyalog keltünk át a folyó feletti hídon.",
                        "english": "We crossed the bridge over the river on foot."
                    },
                    {
                        "spanish": "A térkép segítségével könnyen megtaláltuk a hegyi hágót.",
                        "english": "With the help of the map, we easily found the mountain pass."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.08.03.terminative-case-ig",
        "title": "The Terminative Case: -ig in Space & Time",
        "sections": [
            {
                "type": "text",
                "title": "Expressing spatial endpoints and time limits with -ig",
                "content": "The suffix *-ig* (up to, until, as far as) marks both the physical end-point of a journey and the temporal limit. Unlike most case suffixes, *-ig* does not vary with vowel harmony — it is always *-ig*."
            },
            {
                "type": "examples",
                "title": "Spatial and temporal endpoints",
                "items": [
                    {
                        "spanish": "Budapesttől Debrecenig utaztunk vonattal.",
                        "english": "We traveled by train from Budapest as far as Debrecen."
                    },
                    {
                        "spanish": "Az indulástól az érkezésig két óra telt el.",
                        "english": "From departure to arrival, two hours elapsed."
                    },
                    {
                        "spanish": "Húsz perces késésig a vasúttársaság nem fizet kártérítést.",
                        "english": "Up to a twenty-minute delay, the railway company does not pay compensation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.08.04.travel-mishaps",
        "title": "Expressing Mishaps & Solutions: lekésik, eltéved, panaszt tesz",
        "sections": [
            {
                "type": "text",
                "title": "Dealing with travel disruptions",
                "content": "When things go wrong while traveling, verbs take prefixes showing loss or error: *lekési a vonatot* (to miss the train), *eltéved* (to get lost), *elveszíti a csomagját* (to lose one's luggage). To seek redress, use *panaszt tesz* (to file a complaint)."
            },
            {
                "type": "examples",
                "title": "Disruption expressions",
                "items": [
                    {
                        "spanish": "A késés miatt elkéstünk, és lekéstük a csatlakozást.",
                        "english": "Because of the delay, we were late and missed the connection."
                    },
                    {
                        "spanish": "Pótlóbusz jár a felújítás alatt álló szakaszon.",
                        "english": "A replacement bus runs on the section under renovation."
                    },
                    {
                        "spanish": "Az ügyfélszolgálaton tettünk panaszt az elveszett csomag miatt.",
                        "english": "We filed a complaint at customer service because of the lost luggage."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.08.05.trip-planning-synthesis",
        "title": "Synthesizing Travel Plans: útiterv, szállásfoglalás, látnivalók",
        "sections": [
            {
                "type": "text",
                "title": "Putting together a complete travel itinerary",
                "content": "Combining postpositions of motion (*felé*, *át*), the terminative *-ig*, and compound nouns (*szállásfoglalás*, *útiterv*), you can discuss complex vacation itineraries, hotel bookings, and sightseeing."
            },
            {
                "type": "examples",
                "title": "Itinerary planning",
                "items": [
                    {
                        "spanish": "Az útiterv szerint három napot töltünk Egerben a látnivalók megtekintésével.",
                        "english": "According to the itinerary, we will spend three days in Eger visiting the sights."
                    },
                    {
                        "spanish": "A szállásfoglalást már hetekkel az utazás előtt elintéztem.",
                        "english": "I arranged the accommodation booking weeks before the trip."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-08-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Reading: Mikszáth Kálmán: Szent Péter esernyője
    # -------------------------------------------------------------------------
    classic_08 = {
        "id": "story.b1.08.classic",
        "title": "A glogovai utazás",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 6,
        "characters": ["Bélyi János pap", "Wibra Gyuri", "A kocsis"],
        "grammar": ["motion-postpositions", "terminative-case-ig", "travel-mishaps"],
        "vocabularyTopics": ["travel", "carriage", "mountains", "legend"],
        "summary": "An adapted retelling inspired by Kálmán Mikszáth's beloved classic novel Szent Péter esernyője: travelers journey by carriage through the rugged northern mountains and muddy roads toward Glogova, pursuing the mysterious umbrella said to hold miraculous fortunes.",
        "source": "Adaptation inspired by the public-domain novel Szent Péter esernyője by Kálmán Mikszáth",
        "author": "Kálmán Mikszáth",
        "work": "Szent Péter esernyője",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A nehéz postakocsi lassan zötykölődött a felvidéki hegyek felé. Az őszi eső napok óta megállás nélkül esett, és a szűk utak mély sárrá változtak a fenyvesek között."
            },
            {
                "type": "narration",
                "text": "A fiatal ügyvéd, Wibra Gyuri, türelmetlenül nézett ki a hintó kis ablakán. A célállomásig, a kicsiny Glogova falujáig még hosszú mérföldek voltak hátra az erdőn keresztül."
            },
            {
                "type": "narration",
                "text": "„Hé, kocsis! — szólt ki Gyuri az esőben ázó lovasnak. — Mikorra érünk át a hegyi hágón? A menetrend szerint már rég az állomáson kellene lennünk!” A kocsis csak a fejét csóválta: „Ebben a viharban örülhetünk, ha nem törik el a kerék az alagút előtt.”"
            },
            {
                "type": "narration",
                "text": "Gyurit nem az időjárás bosszantotta a legjobban, hanem az az elképesztő történet, amit a falvakban beszéltek. Mindenki egy különös, vörös esernyőről suttogott, amelyet állítólag maga Szent Péter hozott a glogovai pap kishúgának a nagy zápor idején."
            },
            {
                "type": "narration",
                "text": "Az emberek azt hitték, hogy az esernyő csodát tesz és gazdagságot hoz mindenkinek, aki a közelébe ér. De Gyuri tudta, hogy a kopott ernyő nyelében valami sokkal valóságosabb kincs rejtőzik: a néhai gazdag nagybácsi elveszett vagyona."
            },
            {
                "type": "narration",
                "text": "Végül a ködből kibontakoztak Glogova egyszerű házai és a fatemplom tornya. A hintó megállt a parókia kapujában. Gyuri mély lélegzetet vett, felvette a bőrtáskáját, és elindult a tornác felé: a hosszú és fáradságos utazás véget ért, de az igazi titok felfedése még csak most kezdődött."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-08-szentpeter.json", classic_08)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-08-01",
        "exercises": [
            {
                "id": "b1-08-01-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which postposition means 'towards'?",
                "options": ["felé", "alatt", "után"],
                "correct": 0,
                "teaches": ["postposition-fele"]
            },
            {
                "id": "b1-08-01-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is 'célállomás' in English?",
                "options": ["destination (final station)", "timetable", "ticket price"],
                "correct": 0,
                "teaches": ["vocab-celallomas"]
            },
            {
                "id": "b1-08-01-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["célállomás", "destination"],
                    ["átszállás", "transfer / connection"],
                    ["menetrend", "timetable"],
                    ["jegykezelés", "ticket inspection / validation"]
                ],
                "teaches": ["vocab-transit"]
            },
            {
                "id": "b1-08-01-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A vonat a Duna ... halad a pályaudvarról.",
                "options": ["felé", "felől", "közben"],
                "correct": 0,
                "teaches": ["motion-fele"]
            },
            {
                "id": "b1-08-01-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "A [menetrend] szerint a gyorsvonat tíz percen belül indul.",
                "options": ["menetrend", "térkép", "hágó"],
                "correct": 0,
                "teaches": ["menetrend-usage"]
            },
            {
                "id": "b1-08-01-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence is natural?",
                "options": [
                    "Közvetlen vonattal, átszállás nélkül utazunk Szegedre.",
                    "Átszállásban nélkül vonattal utazunk Szeged.",
                    "Szeged felől átszállással nem megy vonatunk."
                ],
                "correct": 0,
                "teaches": ["atszallas-sentence"]
            },
            {
                "id": "b1-08-01-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["pontos menetrend", "accurate timetable"],
                    ["közvetlen átszállás", "direct transfer"],
                    ["végső célállomás", "final destination"],
                    ["automatikus jegykezelés", "automated ticket validation"]
                ],
                "teaches": ["transit-collocations"]
            },
            {
                "id": "b1-08-01-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Hol kell érvényesíteni a menetjegyet felszállás előtt?",
                "options": [
                    "A jegykezelő automatánál a peronon vagy a járművön.",
                    "A szálloda recepcióján.",
                    "A hegyi hágónál."
                ],
                "correct": 0,
                "teaches": ["jegykezeles-reading"]
            },
            {
                "id": "b1-08-01-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "A hegyek [felől] hűvös szellő érkezett a völgybe.",
                "options": ["felől", "felé", "után"],
                "correct": 0,
                "teaches": ["felol-usage"]
            },
            {
                "id": "b1-08-01-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent: 'Ez a vonat közvetlenül a célállomásra megy'?",
                "options": [
                    "This train goes directly to the destination without transfers.",
                    "This train is cancelled.",
                    "This train only carries luggage."
                ],
                "correct": 0,
                "teaches": ["transit-translation"]
            },
            {
                "id": "b1-08-01-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Van közvetlen járat Pécsre, vagy átszállással kell menni?\n— ...",
                "options": [
                    "Szerencsére van egy közvetlen InterCity, nem kell átszállnod.",
                    "A jegyet tegnap vettem a zöldségesnél.",
                    "Nem szeretem a hideg időt télen."
                ],
                "correct": 0,
                "teaches": ["transit-dialogue-1"]
            },
            {
                "id": "b1-08-01-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Megnézted a menetrendet az interneten?\n— ...",
                "options": [
                    "Igen, a vonat pontosan 14:25-kor indul a Déli pályaudvarról.",
                    "Nem találtam meg a cipőmet a szekrényben.",
                    "Tegnap este kenyeret sütöttem vacsorára."
                ],
                "correct": 0,
                "teaches": ["transit-dialogue-2"]
            },
            {
                "id": "b1-08-01-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We are travelling towards the capital.'?",
                "options": [
                    "A főváros felé utazunk.",
                    "A fővárosból állunk.",
                    "A fővárosban fekszünk."
                ],
                "correct": 0,
                "teaches": ["production-fele"]
            },
            {
                "id": "b1-08-01-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Where is the ticket validation machine?'?",
                "options": [
                    "Hol van a jegykezelő automata?",
                    "Mikor érkezik a célállomás?",
                    "Miért késik a menetrend?"
                ],
                "correct": 0,
                "teaches": ["production-ticket"]
            },
            {
                "id": "b1-08-01-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which postposition indicates direction TOWARDS?",
                "options": ["felé", "felől", "között"],
                "correct": 0,
                "teaches": ["check-fele"]
            },
            {
                "id": "b1-08-01-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "What does 'átszállás' mean?",
                "options": ["transfer / connection", "sleeping car", "luggage cart"],
                "correct": 0,
                "teaches": ["check-atszallas"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-08-02",
        "exercises": [
            {
                "id": "b1-08-02-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which postposition means 'through' or 'across'?",
                "options": ["keresztül", "helyett", "szerint"],
                "correct": 0,
                "teaches": ["keresztul-intro"]
            },
            {
                "id": "b1-08-02-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is 'hágó' in English geography?",
                "options": ["mountain pass", "waterfall", "desert"],
                "correct": 0,
                "teaches": ["vocab-hago"]
            },
            {
                "id": "b1-08-02-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["alagút", "tunnel"],
                    ["hágó", "mountain pass"],
                    ["folyópart", "riverbank"],
                    ["térkép", "map"]
                ],
                "teaches": ["vocab-terrain"]
            },
            {
                "id": "b1-08-02-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A vonat áthaladt a hosszú hegyi ...",
                "options": ["alagúton.", "térképen.", "hágóra."],
                "correct": 0,
                "teaches": ["alagut-case"]
            },
            {
                "id": "b1-08-02-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "Gyalog mentünk végig a szép Duna-[folyóparton].",
                "options": ["folyóparton", "alagútban", "menetrenddel"],
                "correct": 0,
                "teaches": ["folyopart-usage"]
            },
            {
                "id": "b1-08-02-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which phrase means 'across the forest'?",
                "options": ["az erdőn keresztül", "az erdő után", "az erdő felől"],
                "correct": 0,
                "teaches": ["erdon-keresztul"]
            },
            {
                "id": "b1-08-02-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["átkel a hídon", "crosses over the bridge"],
                    ["áthalad az alagúton", "passes through the tunnel"],
                    ["a folyópart mentén sétál", "walks along the riverbank"],
                    ["megnézi a térképen", "looks it up on the map"]
                ],
                "teaches": ["movement-phrases"]
            },
            {
                "id": "b1-08-02-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért van szükség térképre a hegyekben való túrázáshoz?",
                "options": [
                    "Hogy megtaláljuk a helyes ösvényt és a hágókat, és ne tévedjünk el.",
                    "Hogy lefényképezzük a fákat.",
                    "Hogy megvegyük a vonatjegyet."
                ],
                "correct": 0,
                "teaches": ["hiking-reading"]
            },
            {
                "id": "b1-08-02-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "A kirándulók sikeresen átkeltek a magas [hágón].",
                "options": ["hágón", "alagútban", "szobában"],
                "correct": 0,
                "teaches": ["hagon-context"]
            },
            {
                "id": "b1-08-02-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent az 'átkelés'?",
                "options": ["Crossing over / transit.", "Waking up.", "Falling asleep."],
                "correct": 0,
                "teaches": ["atkeles-translation"]
            },
            {
                "id": "b1-08-02-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Merre vezet a legrövidebb út a völgybe?\n— ...",
                "options": [
                    "A hegyen keresztül, az erdős hágón át.",
                    "A tegnapi vacsora nagyon finom volt.",
                    "Nem találtam meg a könyvemet."
                ],
                "correct": 0,
                "teaches": ["route-dialogue"]
            },
            {
                "id": "b1-08-02-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Van nálad térkép a környékről?\n— ...",
                "options": [
                    "Igen, a telefonomon letöltöttem a részletes turistatérképet.",
                    "Nem vettem új nadrágot a boltban.",
                    "A repülőgép késve szállt le tegnap."
                ],
                "correct": 0,
                "teaches": ["map-dialogue"]
            },
            {
                "id": "b1-08-02-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'The road leads through a dark tunnel.'?",
                "options": [
                    "Az út egy sötét alagúton keresztül vezet.",
                    "Az út az alagút előtt megállt.",
                    "Az alagútban nincsen semmilyen út."
                ],
                "correct": 0,
                "teaches": ["production-tunnel"]
            },
            {
                "id": "b1-08-02-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We walked along the riverbank.'?",
                "options": [
                    "A folyópart mentén sétáltunk.",
                    "A folyón átúsztunk gyorsan.",
                    "A folyópartról elkéstünk reggel."
                ],
                "correct": 0,
                "teaches": ["production-riverbank"]
            },
            {
                "id": "b1-08-02-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'alagút'?",
                "options": ["tunnel", "bridge", "tower"],
                "correct": 0,
                "teaches": ["check-alagut"]
            },
            {
                "id": "b1-08-02-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Complete: 'A hídon ...' (across)",
                "options": ["keresztül", "alatt", "után"],
                "correct": 0,
                "teaches": ["check-keresztul"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-08-03",
        "exercises": [
            {
                "id": "b1-08-03-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which suffix marks the endpoint ('up to / as far as / until')?",
                "options": ["-ig", "-nál / -nél", "-tól / -től"],
                "correct": 0,
                "teaches": ["terminative-case-ig"]
            },
            {
                "id": "b1-08-03-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is the difference between 'indulás' and 'érkezés'?",
                "options": ["departure vs arrival", "ticket vs train", "seat vs luggage"],
                "correct": 0,
                "teaches": ["indulas-erkezes"]
            },
            {
                "id": "b1-08-03-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["indulás", "departure"],
                    ["érkezés", "arrival"],
                    ["késés", "delay"],
                    ["tartam", "duration"]
                ],
                "teaches": ["vocab-time-motion"]
            },
            {
                "id": "b1-08-03-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Budapesttől Bécs... két és fél óra az út.",
                "options": ["-ig", "-ban", "-hoz"],
                "correct": 0,
                "teaches": ["ig-spatial"]
            },
            {
                "id": "b1-08-03-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "Húsz perces [késéssel] futott be a vonat az állomásra.",
                "options": ["késéssel", "érkezéssel", "menetrenddel"],
                "correct": 0,
                "teaches": ["kesessel-context"]
            },
            {
                "id": "b1-08-03-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence expresses travel duration?",
                "options": [
                    "Az utazás időtartama három óra volt.",
                    "A vonat zöld színűre van festve.",
                    "A kalauz jegyeket ellenőrizte tegnap."
                ],
                "correct": 0,
                "teaches": ["duration-sentence"]
            },
            {
                "id": "b1-08-03-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["pontos indulás", "punctual departure"],
                    ["várható érkezés", "expected arrival"],
                    ["jelentős késés", "significant delay"],
                    ["az út időtartama", "duration of the journey"]
                ],
                "teaches": ["transit-time-phrases"]
            },
            {
                "id": "b1-08-03-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mikor kell a peronon várni a vonatot?",
                "options": [
                    "Az indulási idő előtt legalább 10-15 perccel.",
                    "Két nappal az utazás után.",
                    "Csak este tizenegykor."
                ],
                "correct": 0,
                "teaches": ["travel-etiquette"]
            },
            {
                "id": "b1-08-03-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Reggeltől [estig] tartott a kimerítő buszozás a hegyekben.",
                "options": ["estig", "este", "estén"],
                "correct": 0,
                "teaches": ["reggeltol-estig"]
            },
            {
                "id": "b1-08-03-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent: 'Meddig tart az út?'",
                "options": ["How long does the trip take?", "Where does the road turn?", "Who is on the train?"],
                "correct": 0,
                "teaches": ["meddig-tart-translation"]
            },
            {
                "id": "b1-08-03-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Mennyi a vonat várható késése?\n— ...",
                "options": [
                    "Körülbelül huszonöt perc a műszaki hiba miatt.",
                    "A jegy ára háromezer forint volt.",
                    "Nem szeretem az esernyőket."
                ],
                "correct": 0,
                "teaches": ["delay-dialogue"]
            },
            {
                "id": "b1-08-03-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Meddig érvényes a bérleted?\n— ...",
                "options": [
                    "A hónap utolsó napjáig érvényes.",
                    "A pályaudvarig sétáltam reggel.",
                    "Két csomagom van a csomagtartóban."
                ],
                "correct": 0,
                "teaches": ["validity-dialogue"]
            },
            {
                "id": "b1-08-03-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We travelled as far as Lake Balaton.'?",
                "options": [
                    "A Balatonig utaztunk.",
                    "A Balatonról jöttünk haza.",
                    "A Balatonban fürödtünk este."
                ],
                "correct": 0,
                "teaches": ["production-ig"]
            },
            {
                "id": "b1-08-03-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'What is the estimated time of arrival?'?",
                "options": [
                    "Mikorra várható az érkezés?",
                    "Mikor volt a korábbi indulás?",
                    "Hányadik vágányról indulunk?"
                ],
                "correct": 0,
                "teaches": ["production-arrival"]
            },
            {
                "id": "b1-08-03-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which suffix means 'until / up to'?",
                "options": ["-ig", "-nál", "-ról"],
                "correct": 0,
                "teaches": ["check-ig"]
            },
            {
                "id": "b1-08-03-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'késés'?",
                "options": ["delay", "knife", "ticket"],
                "correct": 0,
                "teaches": ["check-keses"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-08-04",
        "exercises": [
            {
                "id": "b1-08-04-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which verb means 'to miss (a train/bus)'?",
                "options": ["lekési a vonatot", "felszáll a vonatra", "megérkezik a vonattal"],
                "correct": 0,
                "teaches": ["lekesi-usage"]
            },
            {
                "id": "b1-08-04-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is a 'pótlóbusz'?",
                "options": ["replacement bus (when trains/trams are halted)", "express train", "airport taxi"],
                "correct": 0,
                "teaches": ["potlobusz-usage"]
            },
            {
                "id": "b1-08-04-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["csomag", "luggage / baggage"],
                    ["vágány", "railway track / platform"],
                    ["pótlóbusz", "replacement bus"],
                    ["panasz", "complaint"]
                ],
                "teaches": ["vocab-mishaps"]
            },
            {
                "id": "b1-08-04-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A vonat a harmadik ... érkezik.",
                "options": ["vágányra", "csomagra", "panaszra"],
                "correct": 0,
                "teaches": ["vagany-usage"]
            },
            {
                "id": "b1-08-04-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "Az utas hivatalos [panaszt] tett a megrongálódott bőrönd miatt.",
                "options": ["panaszt", "pótlóbuszt", "vágányt"],
                "correct": 0,
                "teaches": ["panaszt-tesz"]
            },
            {
                "id": "b1-08-04-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence describes a travel mishap?",
                "options": [
                    "A csatlakozást elkéstük, és ott maradt a peronon a csomagom.",
                    "Nagyon finom kávét ittunk a kocsiban.",
                    "Sütött a nap az egész út alatt."
                ],
                "correct": 0,
                "teaches": ["mishap-comprehension"]
            },
            {
                "id": "b1-08-04-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["lekési a csatlakozást", "misses the connecting train"],
                    ["panaszt nyújt be", "submits a complaint"],
                    ["elveszett csomag", "lost luggage"],
                    ["pótlóbuszra száll át", "transfers to a replacement bus"]
                ],
                "teaches": ["mishap-collocations"]
            },
            {
                "id": "b1-08-04-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Hová kell fordulni, ha elvész a csomagunk a repülőtéren vagy vasúton?",
                "options": [
                    "Az elveszett tárgyak osztályához vagy az ügyfélszolgálathoz.",
                    "A vasúti vágányhoz a sínek közé.",
                    "A könyvesbolthoz az utcán."
                ],
                "correct": 0,
                "teaches": ["lost-and-found-reading"]
            },
            {
                "id": "b1-08-04-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Pályafelújítás miatt a szakaszon [pótlóbuszok] szállítják az utasokat.",
                "options": ["pótlóbuszok", "hajók", "repülők"],
                "correct": 0,
                "teaches": ["potlobusz-context"]
            },
            {
                "id": "b1-08-04-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent a 'vágányzár'?",
                "options": [
                    "Track closure (service suspended on that railway line).",
                    "Opening of a new station.",
                    "Buying tickets in cash."
                ],
                "correct": 0,
                "teaches": ["vaganyzar-translation"]
            },
            {
                "id": "b1-08-04-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Segítség, ott hagytam a táskámat a vonaton!\n— ...",
                "options": [
                    "Azonnal menjünk az ügyfélszolgálatra, és jelentsük be a kalauznál!",
                    "Semmi baj, vegyünk egy fagylaltot!",
                    "A tegnapi film nagyon hosszú volt."
                ],
                "correct": 0,
                "teaches": ["lost-bag-dialogue"]
            },
            {
                "id": "b1-08-04-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Miért áll a vonat a nyílt pályán?\n— ...",
                "options": [
                    "Azt mondják, felsővezeték-szakadás van, és pótlóbusz fog jönni.",
                    "Mert elfelejtettem megvenni a kenyeret.",
                    "A kalauz nem szereti a gyorsvonatokat."
                ],
                "correct": 0,
                "teaches": ["breakdown-dialogue"]
            },
            {
                "id": "b1-08-04-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We missed the train due to the delay.'?",
                "options": [
                    "A késés miatt lekéstük a vonatot.",
                    "A késéssel felszálltunk a vonatra.",
                    "A vonatról nem késtünk soha."
                ],
                "correct": 0,
                "teaches": ["production-missed-train"]
            },
            {
                "id": "b1-08-04-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Which track does the train depart from?'?",
                "options": [
                    "Hányadik vágányról indul a vonat?",
                    "Melyik pótlóbusszal utazol haza?",
                    "Hol vetted meg a csomagodat?"
                ],
                "correct": 0,
                "teaches": ["production-track"]
            },
            {
                "id": "b1-08-04-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'vágány' in railway terminology?",
                "options": ["track / platform", "ticket window", "conductor"],
                "correct": 0,
                "teaches": ["check-vagany"]
            },
            {
                "id": "b1-08-04-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which verb forms 'panaszt ...' (to file a complaint)?",
                "options": ["tesz", "lát", "kér"],
                "correct": 0,
                "teaches": ["check-panasz"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-08-05",
        "exercises": [
            {
                "id": "b1-08-05-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'látnivaló' mean?",
                "options": ["sight / tourist attraction", "ticket counter", "railway carriage"],
                "correct": 0,
                "teaches": ["vocab-latnivalo"]
            },
            {
                "id": "b1-08-05-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'útiterv' mean?",
                "options": ["itinerary / travel plan", "passport", "hotel key"],
                "correct": 0,
                "teaches": ["vocab-utiterv"]
            },
            {
                "id": "b1-08-05-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["szállás", "accommodation / lodging"],
                    ["foglalás", "reservation / booking"],
                    ["látnivaló", "sight / attraction"],
                    ["útiterv", "itinerary"]
                ],
                "teaches": ["vocab-trip-planning"]
            },
            {
                "id": "b1-08-05-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Időben le kell adnunk a szállás... a főszezonban.",
                "options": ["foglalást", "látnivalót", "hágót"],
                "correct": 0,
                "teaches": ["foglalas-collocation"]
            },
            {
                "id": "b1-08-05-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "Összeállítottuk az egyhetes utazás részletes [útitervét].",
                "options": ["útitervét", "késését", "alagútját"],
                "correct": 0,
                "teaches": ["utiterv-usage"]
            },
            {
                "id": "b1-08-05-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence describes planning a trip?",
                "options": [
                    "Lefoglaltuk a szállást és összeírtuk a főbb látnivalókat.",
                    "A cipőm nagyon vizes lett az esőben.",
                    "A boltban nincs több friss tej."
                ],
                "correct": 0,
                "teaches": ["planning-concept"]
            },
            {
                "id": "b1-08-05-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["kényelmes szállás", "comfortable accommodation"],
                    ["sikeres foglalás", "successful booking"],
                    ["történelmi látnivalók", "historic sights"],
                    ["részletes útiterv", "detailed itinerary"]
                ],
                "teaches": ["planning-collocations"]
            },
            {
                "id": "b1-08-05-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért hasznos útitervet készíteni egy utazás előtt?",
                "options": [
                    "Hogy optimálisan beosszuk az időnket és ne maradjunk le a legszebb helyekről.",
                    "Hogy több pénzt fizessünk a vasúton.",
                    "Hogy otthon felejtsük a csomagot."
                ],
                "correct": 0,
                "teaches": ["planning-reading"]
            },
            {
                "id": "b1-08-05-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Eger városa tele van híres történelmi [látnivalókkal].",
                "options": ["látnivalókkal", "pótlóbuszokkal", "menetrendekkel"],
                "correct": 0,
                "teaches": ["latnivalokkal-context"]
            },
            {
                "id": "b1-08-05-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent a 'szállásfoglalás megerősítése'?",
                "options": [
                    "Confirmation of accommodation booking.",
                    "Cancelling the trip.",
                    "Paying for railway luggage."
                ],
                "correct": 0,
                "teaches": ["booking-confirm-translation"]
            },
            {
                "id": "b1-08-05-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Találtál már megfelelő szállást a hétvégére?\n— ...",
                "options": [
                    "Igen, foglaltam egy csendes panziót a vár közelében.",
                    "A vonat már elment tíz perccel ezelőtt.",
                    "Nem szeretem a hideg vacsorát."
                ],
                "correct": 0,
                "teaches": ["booking-dialogue"]
            },
            {
                "id": "b1-08-05-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Milyen látnivalókat nézünk meg holnap délelőtt?\n— ...",
                "options": [
                    "Először a múzeumot, utána pedig a történelmi belvárost járjuk be.",
                    "Nem találtam meg a villamosbérletemet reggel.",
                    "Tegnap esett az eső a városban."
                ],
                "correct": 0,
                "teaches": ["sightseeing-dialogue"]
            },
            {
                "id": "b1-08-05-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We booked the accommodation online.'?",
                "options": [
                    "Interneten foglaltuk le a szállást.",
                    "A szállásról interneten beszéltünk.",
                    "Szállás nélkül mentünk a városba."
                ],
                "correct": 0,
                "teaches": ["production-booking"]
            },
            {
                "id": "b1-08-05-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'There are many wonderful sights in this region.'?",
                "options": [
                    "Sok csodálatos látnivaló van ezen a vidéken.",
                    "A vidéken nem látunk semmit a ködben.",
                    "Látnivaló nélkül utazunk Szegedre."
                ],
                "correct": 0,
                "teaches": ["production-sights"]
            },
            {
                "id": "b1-08-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikszáth Kálmán elbeszélésében hová utazik Wibra Gyuri a postakocsin?",
                "options": [
                    "Glogova falujába, a hegyeken keresztül.",
                    "Bécsbe, egy jogi konferenciára.",
                    "A tengerpartra nyaralni."
                ],
                "correct": 0,
                "teaches": ["mikszath-reading-1"]
            },
            {
                "id": "b1-08-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért siet Gyuri a rossz idő ellenére Glogovára?",
                "options": [
                    "Mert a híres vörös esernyőben keresi a néhai nagybácsi örökségét.",
                    "Mert meglátogatja az édesanyját.",
                    "Mert lekéste a vasúti csatlakozást."
                ],
                "correct": 0,
                "teaches": ["mikszath-reading-2"]
            },
            {
                "id": "b1-08-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan utaznak a szereplők Mikszáth regényrészletében?",
                "options": [
                    "Postakocsin, sáros és nehezen járható hegyi utakon.",
                    "Modern gyorsvonattal.",
                    "Folyami gőzhajón."
                ],
                "correct": 0,
                "teaches": ["mikszath-reading-3"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-08-consolidation",
        "exercises": [
            {
                "id": "b1-08-consolidation-1",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["célállomás", "destination"],
                    ["menetrend", "timetable"],
                    ["alagút", "tunnel"],
                    ["szállás", "accommodation"]
                ]
            },
            {
                "id": "b1-08-consolidation-2",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["átszállás", "transfer"],
                    ["hágó", "mountain pass"],
                    ["vágány", "platform / track"],
                    ["útiterv", "itinerary"]
                ]
            },
            {
                "id": "b1-08-consolidation-3",
                "type": "multiple-choice",
                "category": "recognize",
                "question": "Which postposition expresses direction 'towards'?",
                "options": ["felé", "felől", "között"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-4",
                "type": "multiple-choice",
                "category": "recall",
                "question": "Complete: 'Budapesttől Debrecen...' (as far as Debrecen)",
                "options": ["-ig", "-ban", "-hoz"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-5",
                "type": "fill-in-the-blank",
                "category": "recall",
                "sentence": "A vonat a hosszú hegyi [alagúton] haladt keresztül.",
                "options": ["alagúton", "térképen", "menetrenden"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-6",
                "type": "multiple-choice",
                "category": "recall",
                "question": "Which phrase means 'to miss the train'?",
                "options": ["lekési a vonatot", "felszáll a vonatra", "vezeti a vonatot"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-7",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "A vágányzár idején az utasokat ... szállítják az állomások között.",
                "options": ["pótlóbuszok", "repülőgépek", "hajók"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-8",
                "type": "fill-in-the-blank",
                "category": "in-context",
                "sentence": "Időben el kell intézni a [szállásfoglalást] a nyári szezonra.",
                "options": ["szállásfoglalást", "késést", "panaszt"],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-9",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "Mit jelent az 'útiterv' egy utazó számára?",
                "options": [
                    "A megtekinteni kívánt helyek és időpontok pontos listáját.",
                    "A vonatjegy árát.",
                    "A poggyász súlyát."
                ],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-10",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'We travelled through the mountains towards the lake.'",
                "options": [
                    "A hegyeken keresztül utaztunk a tó felé.",
                    "A hegyről a tóba mentünk tegnap.",
                    "A hegy alatt nem láttuk a tavat."
                ],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-11",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'From morning until evening we visited the sights.'",
                "options": [
                    "Reggeltől estig a látnivalókat jártuk be.",
                    "Reggel és este szállást foglaltunk.",
                    "Reggelről estére elveszett a csomagunk."
                ],
                "correct": 0
            },
            {
                "id": "b1-08-consolidation-12",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'Which track does the train depart from?'",
                "options": [
                    "Hányadik vágányról indul a vonat?",
                    "Mikor érkezik meg a csomag?",
                    "Hol van a menetrend kiírva?"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-08-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.08-01",
        "unit": 8,
        "title": "Getting There",
        "level": "B1",
        "grammar": "Postpositions of motion: keresztül, át, felé, felől; public transport navigation",
        "goal": [
            "I can navigate public transport schedules, transfers, and destinations.",
            "I can use spatial postpositions of motion like felé and felől.",
            "I can use four new vocabulary items related to transit and journeys.",
            "I can ask for directions and transfer information at train stations."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can navigate public transport schedules, transfers, and destinations.",
                    "I can use spatial postpositions of motion like felé and felől.",
                    "I can use four new vocabulary items related to transit and journeys.",
                    "I can ask for directions and transfer information at train stations."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-08-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-intro-1", "b1-08-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-controlled-1", "b1-08-01-controlled-2", "b1-08-01-controlled-3", "b1-08-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-practice-1", "b1-08-01-practice-2", "b1-08-01-practice-3", "b1-08-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-dialogue-1", "b1-08-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-writing-1", "b1-08-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-08-01-ex.json", "exerciseRefs": ["b1-08-01-check-1", "b1-08-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can navigate public transport schedules, transfers, and destinations.",
                    "I can use spatial postpositions of motion like felé and felől.",
                    "I can use four new vocabulary items related to transit and journeys.",
                    "I can ask for directions and transfer information at train stations."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.08-02",
        "unit": 8,
        "title": "Through, Across, Toward",
        "level": "B1",
        "grammar": "Verbal prefixes of motion (át-, be-, le-) with terrain nouns and postposition keresztül",
        "goal": [
            "I can describe moving through geographical terrain, tunnels, and passes.",
            "I can combine motion prefixes (átkel, áthalad) with postpositions like keresztül.",
            "I can use four new vocabulary items related to landscape and topography.",
            "I can read and give trail and road descriptions using a map."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe moving through geographical terrain, tunnels, and passes.",
                    "I can combine motion prefixes (átkel, áthalad) with postpositions like keresztül.",
                    "I can use four new vocabulary items related to landscape and topography.",
                    "I can read and give trail and road descriptions using a map."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-08-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-intro-1", "b1-08-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-controlled-1", "b1-08-02-controlled-2", "b1-08-02-controlled-3", "b1-08-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-practice-1", "b1-08-02-practice-2", "b1-08-02-practice-3", "b1-08-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-dialogue-1", "b1-08-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-writing-1", "b1-08-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-08-02-ex.json", "exerciseRefs": ["b1-08-02-check-1", "b1-08-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe moving through geographical terrain, tunnels, and passes.",
                    "I can combine motion prefixes (átkel, áthalad) with postpositions like keresztül.",
                    "I can use four new vocabulary items related to landscape and topography.",
                    "I can read and give trail and road descriptions using a map."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.08-03",
        "unit": 8,
        "title": "Until When, From When",
        "level": "B1",
        "grammar": "Terminative case -ig in space and time; travel duration expressions",
        "goal": [
            "I can use the terminative case -ig to specify destinations and time limits.",
            "I can discuss departure, arrival, duration, and delays accurately.",
            "I can use four new vocabulary items related to scheduling and journey time.",
            "I can understand and calculate travel time differences."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can use the terminative case -ig to specify destinations and time limits.",
                    "I can discuss departure, arrival, duration, and delays accurately.",
                    "I can use four new vocabulary items related to scheduling and journey time.",
                    "I can understand and calculate travel time differences."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-08-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-intro-1", "b1-08-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-controlled-1", "b1-08-03-controlled-2", "b1-08-03-controlled-3", "b1-08-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-practice-1", "b1-08-03-practice-2", "b1-08-03-practice-3", "b1-08-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-dialogue-1", "b1-08-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-writing-1", "b1-08-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-08-03-ex.json", "exerciseRefs": ["b1-08-03-check-1", "b1-08-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can use the terminative case -ig to specify destinations and time limits.",
                    "I can discuss departure, arrival, duration, and delays accurately.",
                    "I can use four new vocabulary items related to scheduling and journey time.",
                    "I can understand and calculate travel time differences."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.08-04",
        "unit": 8,
        "title": "When Travel Goes Wrong",
        "level": "B1",
        "grammar": "Travel mishaps and problem resolution: lekésik, pótlóbusz, panaszt tesz",
        "goal": [
            "I can handle unexpected travel disruptions, missed trains, and delays.",
            "I can describe lost luggage and file complaints at customer service.",
            "I can use four new vocabulary items related to railway problems.",
            "I can ask about alternative routes and replacement buses (pótlóbusz)."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can handle unexpected travel disruptions, missed trains, and delays.",
                    "I can describe lost luggage and file complaints at customer service.",
                    "I can use four new vocabulary items related to railway problems.",
                    "I can ask about alternative routes and replacement buses (pótlóbusz)."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-08-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-intro-1", "b1-08-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-controlled-1", "b1-08-04-controlled-2", "b1-08-04-controlled-3", "b1-08-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-practice-1", "b1-08-04-practice-2", "b1-08-04-practice-3", "b1-08-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-dialogue-1", "b1-08-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-writing-1", "b1-08-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-08-04-ex.json", "exerciseRefs": ["b1-08-04-check-1", "b1-08-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can handle unexpected travel disruptions, missed trains, and delays.",
                    "I can describe lost luggage and file complaints at customer service.",
                    "I can use four new vocabulary items related to railway problems.",
                    "I can ask about alternative routes and replacement buses (pótlóbusz)."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.08-05",
        "unit": 8,
        "title": "Planning a Trip",
        "level": "B1",
        "grammar": "Synthesis: complete trip planning, itineraries, bookings, and regional exploration",
        "goal": [
            "I can prepare a full travel itinerary, reserve accommodation, and select sights.",
            "I can use four new vocabulary items related to vacation planning.",
            "I can express recommendations for exploring Hungarian towns and regions.",
            "I can read and understand an adapted excerpt from Mikszáth's Szent Péter esernyője."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can prepare a full travel itinerary, reserve accommodation, and select sights.",
                    "I can use four new vocabulary items related to vacation planning.",
                    "I can express recommendations for exploring Hungarian towns and regions.",
                    "I can read and understand an adapted excerpt from Mikszáth's Szent Péter esernyője."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-08-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-08-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-intro-1", "b1-08-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-controlled-1", "b1-08-05-controlled-2", "b1-08-05-controlled-3", "b1-08-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-practice-1", "b1-08-05-practice-2", "b1-08-05-practice-3", "b1-08-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-dialogue-1", "b1-08-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-writing-1", "b1-08-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: A glogovai utazás",
                "ref": "stories/classics/b1/b1-08-szentpeter.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-08-05-ex.json", "exerciseRefs": ["b1-08-05-reading-1", "b1-08-05-reading-2", "b1-08-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can prepare a full travel itinerary, reserve accommodation, and select sights.",
                    "I can use four new vocabulary items related to vacation planning.",
                    "I can express recommendations for exploring Hungarian towns and regions.",
                    "I can read and understand an adapted excerpt from Mikszáth's Szent Péter esernyője."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.08-consolidation",
        "unit": 8,
        "title": "Unit 8 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can navigate Hungarian public transit, timetables, and ticket inspections.",
                    "I can use spatial postpositions of motion (keresztül, felé, felől) and the -ig case.",
                    "I can manage travel mishaps, replacement buses, delays, and complaints.",
                    "I can create complete travel itineraries and describe hotel bookings and sights."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-08-consolidation-ex.json", "exerciseRefs": ["b1-08-consolidation-1", "b1-08-consolidation-2", "b1-08-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-08-consolidation-ex.json", "exerciseRefs": ["b1-08-consolidation-4", "b1-08-consolidation-5", "b1-08-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-08-consolidation-ex.json", "exerciseRefs": ["b1-08-consolidation-7", "b1-08-consolidation-8", "b1-08-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-08-consolidation-ex.json", "exerciseRefs": ["b1-08-consolidation-10", "b1-08-consolidation-11", "b1-08-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can navigate Hungarian public transit, timetables, and ticket inspections.",
                    "I can use spatial postpositions of motion (keresztül, felé, felől) and the -ig case.",
                    "I can manage travel mishaps, replacement buses, delays, and complaints.",
                    "I can create complete travel itineraries and describe hotel bookings and sights."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-08-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_8_core()
    print("Successfully built Hungarian B1 Core Unit 8!")
