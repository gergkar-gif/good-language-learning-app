#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 24: Processes & How Things Work (b1-24)."""

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

def build_unit_24_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.24.01",
        "lesson": "b1-24-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "működés", "translation": "operation, functioning, mechanism", "pos": "noun"},
            {"lemma": "folyamat", "translation": "process, progression", "pos": "noun"},
            {"lemma": "gépezet", "translation": "machinery, mechanism, apparatus", "pos": "noun"},
            {"lemma": "szabályozás", "translation": "regulation, control, adjustment", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-24-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.24.02",
        "lesson": "b1-24-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "összetevő", "translation": "component, ingredient, constituent element", "pos": "noun"},
            {"lemma": "alapanyag", "translation": "raw material, base ingredient", "pos": "noun"},
            {"lemma": "szerkezet", "translation": "structure, framework, build", "pos": "noun"},
            {"lemma": "illeszkedés", "translation": "fit, fitting together, alignment", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-24-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.24.03",
        "lesson": "b1-24-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "átalakulás", "translation": "transformation, conversion", "pos": "noun"},
            {"lemma": "hatásmechanizmus", "translation": "mechanism of action, working principle", "pos": "noun"},
            {"lemma": "kölcsönhatás", "translation": "interaction, mutual effect", "pos": "noun"},
            {"lemma": "áramlás", "translation": "flow, stream, circulation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-24-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.24.04",
        "lesson": "b1-24-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "üzemzavar", "translation": "malfunction, breakdown, operational failure", "pos": "noun"},
            {"lemma": "karbantartás", "translation": "maintenance, servicing, upkeep", "pos": "noun"},
            {"lemma": "hatékonyság", "translation": "efficiency, effectiveness", "pos": "noun"},
            {"lemma": "teljesítmény", "translation": "performance, output, capacity", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-24-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.24.05",
        "lesson": "b1-24-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "finomhangolás", "translation": "fine-tuning, precise calibration", "pos": "noun"},
            {"lemma": "optimalizálás", "translation": "optimization, maximizing performance", "pos": "noun"},
            {"lemma": "automatizálás", "translation": "automation, automatic processing", "pos": "noun"},
            {"lemma": "végeredmény", "translation": "end result, final outcome", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-24-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.24.01.middle-verbs",
        "title": "Process Verbs: The Middle Suffix -ódik / -ődik",
        "sections": [
            {
                "type": "text",
                "title": "Natural Reflexive Processes",
                "content": "Hungarian often expresses processes happening without an overt human agent using *-ódik / -ődik*: *készül* ('is being made'), *megoldódik* ('resolves itself / gets solved'), *átalakul* ('transforms'), *kifejlődik* ('develops')."
            },
            {
                "type": "examples",
                "title": "Automatic processes",
                "items": [
                    {
                        "spanish": "A probléma magától megoldódott, amint újraindították a gépet.",
                        "english": "The problem resolved itself as soon as the machine was restarted."
                    },
                    {
                        "spanish": "A rendszerben minden adat automatikusan frissül.",
                        "english": "In the system, all data is updated automatically."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.24.01.impersonal-process",
        "title": "Impersonal Process Phrasing: sor kerül vmire, végbemegy",
        "sections": [
            {
                "type": "text",
                "title": "Formal Process Descriptors",
                "content": "*Sor kerül vmire* ('something takes place / comes to pass'), *végbemegy a folyamat* ('the process takes place / runs its course'), *üzembe helyez* ('to put into operation')."
            },
            {
                "type": "examples",
                "title": "Procedural phrasing",
                "items": [
                    {
                        "spanish": "A tesztelés után hamarosan sor kerül az új üzem beindítására.",
                        "english": "After testing, the startup of the new plant will soon take place."
                    },
                    {
                        "spanish": "A kémiai átalakulás rendkívül gyorsan ment végbe a tartályban.",
                        "english": "The chemical transformation took place extremely rapidly in the tank."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.24.02.composition-all-vmibol",
        "title": "Describing Structure: áll vmiből, összetevődik",
        "sections": [
            {
                "type": "text",
                "title": "Component Formulations",
                "content": "To express what an apparatus consists of: *áll vmiből* ('consists of sth'), *részekre tagolódik* ('divides into parts'), *összeáll vmiből* ('is assembled from sth')."
            },
            {
                "type": "examples",
                "title": "Structural makeup",
                "items": [
                    {
                        "spanish": "A bonyolult szerkezet több ezer apró, precíz alkatrészből áll.",
                        "english": "The complex structure consists of thousands of tiny, precise components."
                    },
                    {
                        "spanish": "A recept kizárólag természetes és minőségi alapanyagokból épül fel.",
                        "english": "The recipe is built up exclusively from natural and high-quality raw ingredients."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.24.02.manner-illeszkedes",
        "title": "Fit and Alignment: pontosan illeszkedik, összhangban működik",
        "sections": [
            {
                "type": "text",
                "title": "Mechanical and Organic Alignment",
                "content": "*Illeszkedik vmihez/vmibe* ('fits into / aligns with sth'), *összhangban működik* ('operates in harmony'), *zökkenőmentesen kapcsolódik* ('connects seamlessly')."
            },
            {
                "type": "examples",
                "title": "Alignment in systems",
                "items": [
                    {
                        "spanish": "A fogaskerekek milliméterre pontosan illeszkednek egymásba.",
                        "english": "The cogs fit into one another with millimeter precision."
                    },
                    {
                        "spanish": "Minden egyes modul zökkenőmentesen kapcsolódik a központi egységhez.",
                        "english": "Every single module connects seamlessly to the central unit."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.24.03.cause-effect-mechanisms",
        "title": "Mechanism of Action: hatást fejt ki, kölcsönhatásba lép",
        "sections": [
            {
                "type": "text",
                "title": "Action and Reaction",
                "content": "*Hatást gyakorol vmire / hatást fejt ki* ('exerts an effect on sth'), *kölcsönhatásba lép vmivel* ('interacts with sth'), *előidéz vmit* ('triggers / brings about sth')."
            },
            {
                "type": "examples",
                "title": "Scientific and functional effects",
                "items": [
                    {
                        "spanish": "A gyógyszer a sejtek szintjén fejti ki jótékony hatását.",
                        "english": "The medicine exerts its beneficial effect at the cellular level."
                    },
                    {
                        "spanish": "A két anyag kölcsönhatásba lép egymással, ami hőt termel.",
                        "english": "The two substances interact with each other, producing heat."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.24.03.flow-and-circulation",
        "title": "Flow & Circulation: átáramlik, keringést végez",
        "sections": [
            {
                "type": "text",
                "title": "Fluid and Energy Dynamics",
                "content": "*Átáramlik a csöveken* ('flows through the pipes'), *folyamatos keringést végez* ('performs continuous circulation'), *egyenletesen oszlik el* ('distributes evenly')."
            },
            {
                "type": "examples",
                "title": "Dynamics in action",
                "items": [
                    {
                        "spanish": "A hűtőfolyadék zárt rendszerben áramlik körbe-körbe.",
                        "english": "The coolant circulates round and round in a closed system."
                    },
                    {
                        "spanish": "Az energia egyenletesen oszlik el a teljes hálózatban.",
                        "english": "The energy distributes evenly throughout the entire network."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.24.04.troubleshooting-verbs",
        "title": "Troubleshooting & Maintenance: elhárítja az üzemzavart, karbantartást végez",
        "sections": [
            {
                "type": "text",
                "title": "Operational Malfunctions",
                "content": "*Üzemzavar lép fel* ('a breakdown occurs'), *elhárítja a hibát* ('clears the defect'), *rendszeres karbantartást igényel* ('requires regular maintenance')."
            },
            {
                "type": "examples",
                "title": "Maintenance phrases",
                "items": [
                    {
                        "spanish": "A műszaki szakemberek gyorsan elhárították a váratlan üzemzavart.",
                        "english": "The technical experts quickly resolved the unexpected operational breakdown."
                    },
                    {
                        "spanish": "A biztonságos működéshez évenkénti alapos karbantartás szükséges.",
                        "english": "Thorough annual maintenance is required for safe operation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.24.04.measuring-efficiency",
        "title": "Measuring Output: növeli a hatékonyságot, csúcsteljesítményt nyújt",
        "sections": [
            {
                "type": "text",
                "title": "Performance Terms",
                "content": "*Növeli a hatékonyságot* ('increases efficiency'), *csúcsteljesítményt nyújt* ('delivers peak performance'), *kihasználja a kapacitást* ('utilizes the capacity')."
            },
            {
                "type": "examples",
                "title": "Performance metrics",
                "items": [
                    {
                        "spanish": "Az új motor harminc százalékkal nagyobb hatékonysággal működik.",
                        "english": "The new engine operates with thirty percent greater efficiency."
                    },
                    {
                        "spanish": "A turbina a tesztek során csúcsteljesítményt nyújtott.",
                        "english": "The turbine delivered peak performance during testing."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.24.05.sequential-instruction",
        "title": "Step-by-Step Instructions: először, ezután, végül",
        "sections": [
            {
                "type": "text",
                "title": "Procedural Sequence Connectors",
                "content": "To explain procedures sequentially: *először is* ('first of all'), *ezt követően / ezután* ('subsequently / after this'), *párhuzamosan ezzel* ('in parallel with this'), *végezetül* ('in conclusion / finally')."
            },
            {
                "type": "examples",
                "title": "Step-by-step procedures",
                "items": [
                    {
                        "spanish": "Először ellenőrizzük az áramellátást, ezt követően csatlakoztassuk a kábeleket!",
                        "english": "First check the power supply, then subsequently connect the cables!"
                    },
                    {
                        "spanish": "Végezetül kalibráljuk a műszereket a pontos eredményekhez!",
                        "english": "Finally, calibrate the instruments for accurate results!"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.24.05.automation-and-outcomes",
        "title": "Automation & Optimization: optimalizál, automatizálttá válik",
        "sections": [
            {
                "type": "text",
                "title": "Automated End States",
                "content": "*Automatizálttá válik* ('becomes automated'), *finomhangolást végez* ('carries out fine-tuning'), *a kívánt végeredményt hozza* ('yields the desired end result')."
            },
            {
                "type": "examples",
                "title": "Automation in action",
                "items": [
                    {
                        "spanish": "A modern gyártósor szinte teljesen automatizálttá vált az évek során.",
                        "english": "The modern production line has become almost entirely automated over the years."
                    },
                    {
                        "spanish": "A finomhangolás után a rendszer azonnal a kívánt végeredményt hozta.",
                        "english": "After fine-tuning, the system immediately yielded the desired end result."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-24-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-24-01",
        "exercises": [
            {
                "id": "b1-24-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'gépezet' szó tágabb értelemben?",
                "options": [
                    "Egy összetett műszaki vagy szervezeti rendszer működési mechanizmusát.",
                    "Egyetlen egyszerű fa evőeszközt.",
                    "Egy erdőben található turistautat."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A probléma magától megoldó_____, miután újraindították a szervert. (resolved itself - dott)",
                "answer": "dott"
            },
            {
                "id": "b1-24-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Hamarosan", "sor", "kerül", "az", "új", "berendezés", "üzembe", "helyezésére."],
                "solution": ["Hamarosan", "sor", "kerül", "az", "új", "berendezés", "üzembe", "helyezésére."]
            },
            {
                "id": "b1-24-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'szabályozás' egy gépi folyamatban?",
                "options": [
                    "A paraméterek és a működés pontos irányítását, korlátok között tartását.",
                    "A gép teljes lekapcsolását örökre.",
                    "A műszerfal lefestését új színre."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gyártási folya_____ minden lépését szigorúan ellenőrzik a mérnökök. (process - mat)",
                "answer": "mat"
            },
            {
                "id": "b1-24-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki a spontán, cselekvő nélküli folyamatot?",
                "options": [
                    "A csavar magától kilazul a rázkódástól.",
                    "A szerelő kicsavarta a csavart a falból.",
                    "Megkértem Pétert, hogy lazítsa meg a csavart."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kémiai átalakulás meglepően gyorsan ment vég____ a lombikban. (took place - be)",
                "answer": "be"
            },
            {
                "id": "b1-24-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "korszerű", "szabályozás", "megakadályozza", "a", "motor", "túlmelegedését."],
                "solution": ["A", "korszerű", "szabályozás", "megakadályozza", "a", "motor", "túlmelegedését."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-24-02",
        "exercises": [
            {
                "id": "b1-24-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'összetevő' szó?",
                "options": [
                    "Egy szerkezet vagy anyag valamely alkotórésze, eleme.",
                    "Egy teljes egészében elkészült épület.",
                    "Egy postai csomagküldő szelvény."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bonyolult szerkezet több ezer apró alkatrészből _____ fel. (is built up - épül)",
                "answer": "épül"
            },
            {
                "id": "b1-24-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "fogaskerekek", "tökéletesen", "illeszkednek", "egymás", "fogazatába."],
                "solution": ["A", "fogaskerekek", "tökéletesen", "illeszkednek", "egymás", "fogazatába."]
            },
            {
                "id": "b1-24-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az 'alapanyag' jelentése a gyártásban?",
                "options": [
                    "A termék előállításához felhasznált kiindulási nyersanyag.",
                    "A boltban eladott késztermék csomagolása.",
                    "A raktárépület betonozott padlója."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gép vázát alkotó acél szerke_____ rendkívül strapabíró. (structure - zet)",
                "answer": "zet"
            },
            {
                "id": "b1-24-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen magyarul: 'The mechanism consists of three parts'?",
                "options": [
                    "A szerkezet három részből áll.",
                    "A szerkezet három részen áll.",
                    "A szerkezet három részre áll."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden egyes alkatrész pontosan illesz_____ a helyére a vázban. (fits - kedik)",
                "answer": "kedik"
            },
            {
                "id": "b1-24-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "természetes", "alapanyagok", "garantálják", "a", "termék", "kiváló", "minőségét."],
                "solution": ["A", "természetes", "alapanyagok", "garantálják", "a", "termék", "kiváló", "minőségét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-24-03",
        "exercises": [
            {
                "id": "b1-24-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hatásmechanizmus' kifejezés?",
                "options": [
                    "Azt a működési elvet, ahogyan egy anyag vagy erő kifejti a hatását.",
                    "A gépkocsi kézifékének mechanikus karját.",
                    "Egy gyári munkás munkanaplóját."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A két vegyszer azonnal kölcsönhatásba lépett egy_____ a lombikban. (with one another - mással)",
                "answer": "mással"
            },
            {
                "id": "b1-24-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hűtőfolyadék", "folyamatosan", "áramlik", "át", "a", "vastag", "csöveken."],
                "solution": ["A", "hűtőfolyadék", "folyamatosan", "áramlik", "át", "a", "vastag", "csöveken."]
            },
            {
                "id": "b1-24-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'kölcsönhatás'?",
                "options": [
                    "Két vagy több elem egymásra gyakorolt kölcsönös hatását.",
                    "Kölcsönkért pénzösszeg visszafizetését banki átutalással.",
                    "Egyirányú, válasz nélküli rádióadást."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hőmérséklet emelkedésével látványos átalakul_____ ment végbe az anyagban. (transformation - ás)",
                "answer": "ás"
            },
            {
                "id": "b1-24-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonzat tartozik a 'hatást gyakorol' kifejezéshez?",
                "options": [
                    "-ra/-re (Hatást gyakorol a gazdaságra.)",
                    "-val/-vel (Hatást gyakorol a gazdasággal.)",
                    "-ban/-ben (Hatást gyakorol a gazdaságban.)"
                ],
                "correct": 0
            },
            {
                "id": "b1-24-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új szer közvetlen hatást fejt _____ a beteg sejtekre. (exerts - ki)",
                "answer": "ki"
            },
            {
                "id": "b1-24-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "levegő", "egyenletes", "áramlása", "biztosítja", "a", "kellemes", "hőmérsékletet."],
                "solution": ["A", "levegő", "egyenletes", "áramlása", "biztosítja", "a", "kellemes", "hőmérsékletet."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-24-04",
        "exercises": [
            {
                "id": "b1-24-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'üzemzavar' kifejezés?",
                "options": [
                    "Egy berendezés vagy rendszer működésében fellépő váratlan meghibásodást.",
                    "A munkaidő végét jelző gyári sípszót.",
                    "Az új kollégák bemutatkozó látogatását."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A műszaki csapat fél órán belül elhárította a váratlan üzem_____. (breakdown - zavart)",
                "answer": "zavart"
            },
            {
                "id": "b1-24-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "rendszeres", "karbantartás", "megelőzi", "a", "komolyabb", "műszaki", "hibákat."],
                "solution": ["A", "rendszeres", "karbantartás", "megelőzi", "a", "komolyabb", "műszaki", "hibákat."]
            },
            {
                "id": "b1-24-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hatékonyság' egy gépi berendezésnél?",
                "options": [
                    "A felhasznált energia és az elért hasznos eredmény kedvező arányát.",
                    "A berendezés külső festésének fényességét.",
                    "A gép súlyát kilogrammban mérve."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A turbina a tesztelés alatt maximális teljesít_____ működött. (output - ménnyel)",
                "answer": "ménnyel"
            },
            {
                "id": "b1-24-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igekötős ige jelenti a hiba megszüntetését?",
                "options": [
                    "Elhárít (elhárítja a hibát).",
                    "Meghárít (meghárítja a hibát).",
                    "Ráhárít (ráhárítja a hibát)."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új berendezés húsz százalékkal nagyobb hatékony_____ dolgozik. (with efficiency - sággal)",
                "answer": "sággal"
            },
            {
                "id": "b1-24-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magas", "teljesítmény", "mellé", "alacsony", "energiafogyasztás", "társul."],
                "solution": ["A", "magas", "teljesítmény", "mellé", "alacsony", "energiafogyasztás", "társul."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-24-05",
        "exercises": [
            {
                "id": "b1-24-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'finomhangolás' folyamata?",
                "options": [
                    "A rendszer apró, aprólékos beállítását a tökéletes működés érdekében.",
                    "Egy zongora eladását a hangszerboltban.",
                    "A hangosbeszélő maximális hangerejének beállítását."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Először ellenőrizzük a csatlakozást, ez_____ indítsuk el a programot! (then / after this - után)",
                "answer": "után"
            },
            {
                "id": "b1-24-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "gyártósor", "a", "fejlesztések", "révén", "teljesen", "automatizálttá", "vált."],
                "solution": ["A", "gyártósor", "a", "fejlesztések", "révén", "teljesen", "automatizálttá", "vált."]
            },
            {
                "id": "b1-24-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'optimalizálás'?",
                "options": [
                    "Egy folyamat vagy rendszer átalakítását a lehető legkedvezőbb, leghatékonyabb működésre.",
                    "A munkavégzés teljes feladását és a gyár lezárását.",
                    "A hibák figyelmen kívül hagyását."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kitartó munka végere_____ minden várakozást felülmúlt. (end result - dménye)",
                "answer": "dménye"
            },
            {
                "id": "b1-24-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés vezeti be a folyamat legutolsó lépését?",
                "options": [
                    "Végezetül...",
                    "Mindenekelőtt...",
                    "Kezdetben..."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A mérnökök célja a gyártási folyamat folyamatos optimalizá_____. (optimizing - lása)",
                "answer": "lása"
            },
            {
                "id": "b1-24-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "gondos", "finomhangolás", "meghozta", "a", "kívánt", "tökéletes", "végeredményt."],
                "solution": ["A", "gondos", "finomhangolás", "meghozta", "a", "kívánt", "tökéletes", "végeredményt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-24-consolidation",
        "exercises": [
            {
                "id": "b1-24-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik képző fejezi ki, hogy valami magától, önműködően megy végbe?",
                "options": [
                    "-ódik / -ődik (megoldódik, átalakul)",
                    "-tat / -tet (megoldat, dolgoztat)",
                    "-gat / -get (olvasgat, nézeget)"
                ],
                "correct": 0
            },
            {
                "id": "b1-24-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A zárt gépezetben a folyadék zökkenőmentesen áramlik körbe-_____. (round and round - körbe)",
                "answer": "körbe"
            },
            {
                "id": "b1-24-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "precíz", "működés", "és", "a", "szabályozás", "a", "biztonság", "alapfeltétele."],
                "solution": ["A", "precíz", "működés", "és", "a", "szabályozás", "a", "biztonság", "alapfeltétele."]
            },
            {
                "id": "b1-24-consolidation.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A rendszeres karban_____ nélkülözhetetlen a gépek hosszú élettartamához. (maintenance - tartás)",
                "answer": "tartás"
            },
            {
                "id": "b1-24-consolidation.ex05",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "automatizálás", "jelentősen", "növeli", "a", "termelés", "hatékonyságát."],
                "solution": ["Az", "automatizálás", "jelentősen", "növeli", "a", "termelés", "hatékonyságát."]
            },
            {
                "id": "b1-24-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, ha egy mechanizmus 'finomhangolásra' szorul?",
                "options": [
                    "Apró, precíz beállításokkal kell tökéletesíteni a működését.",
                    "Teljesen ki kell dobni a kukába.",
                    "Újra kell festeni a külső burkolatot."
                ],
                "correct": 0
            },
            {
                "id": "b1-24-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vizsgálat során feltárták a váratlan üzemzavar közvetlen kiindulási ok_____. (its cause - át)",
                "answer": "át"
            },
            {
                "id": "b1-24-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen 'gépezetet' kell kiismerniük a diákoknak Ottlik Géza 'Iskola a határon' című remekművében?",
                "options": [
                    "A katonaiskola szigorú, kíméletlen és zárt intézményi rendszerét, megtanulva megőrizni belső szabadságukat.",
                    "Egy gőzmozdony gépészeti meghibásodását az állomáson.",
                    "A kőszegi óragyár harangjátékának fogaskerekeit."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-24-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.24.classic",
        "title": "Iskola a határon",
        "level": "B1",
        "order": 24,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Géza Ottlik's philosophical classic 'Iskola a határon' (School at the Frontier). Arriving at the rigorous military boarding school in Kőszeg, the cadets Bébé, Medve, and Szulovszky discover that the institution functions like a colossal, impassive mechanism. They gradually learn how every component of the school apparatus operates, how to adapt without losing their souls, and how genuine human solidarity survives inside the most unbending clockwork.",
        "characters": [
            "Bébé (Both Benedek), a növendék és elbeszélő",
            "Medve Gábor, a csendes lázadó",
            "Bognár tiszthelyettes, az iskola vasfegyelmének őre"
        ],
        "location": "A kőszegi katonai alreáliskola udvara és hálóterme",
        "author": "Ottlik Géza",
        "work": "Iskola a határon (1959)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kőszegi katonaiskola hatalmas kőépülete nem egyszerű iskola volt: óriási, fenséges és könyörtelen gépezetként működött. Minden reggel pontosan ugyanabban a másodpercben szólalt meg a kürt, s a mechanizmus fogaskerekei megállíthatatlanul forogni kezdtek."
            },
            {
                "type": "dialogue",
                "speaker": "Bognár tiszthelyettes",
                "text": "Itt nincsenek egyéni kívánságok! Minden növendék egy-egy alkatrész a nagy szerkezetben. Ha egyetlen csavar is kilazul, az egész gépezet működése megbillen!"
            },
            {
                "type": "narration",
                "text": "A fiúk kezdetben nem értették a szabályozás szigorú logikáját. A napirend lépésről lépésre, percről percre szabályozta a létezést: az ébredést, a sorakozót, a csajkák kiosztását és a lépéstávolságot a kavicsos udvaron."
            },
            {
                "type": "dialogue",
                "speaker": "Medve Gábor",
                "text": "Bébé, nézd meg ezt az egészet! Azt hiszik, ha géppé alakítanak bennünket, elveszítjük az emberségünket. De tévednek. Minél merevebb a külső szerkezet, annál tisztábban kell ragyognia a belső szabadságunknak."
            },
            {
                "type": "narration",
                "text": "Idővel a növendékek megtanulták, hogyan működik a gépezet. Nem lázadtak hiába a kőfalak ellen, hanem összekapaszkodtak. Megtanulták a hallgatás, a hűség és az egymásért vállalt felelősség titkos nyelvét."
            },
            {
                "type": "dialogue",
                "speaker": "Bébé",
                "text": "A gépezet darált, forgott és csiszolt minket éveken át. De a végeredmény nem az lett, amit a rideg parancsok vártak: a kíméletlen mechanizmus mélyén életre szóló, széttörhetetlen barátság kovácsolódott."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-24-ottlik.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("How Mechanisms Work", "Hogyan működnek a dolgok? Működés és szabályozás"),
            "02": ("Components & Frameworks", "Alkotóelemek és szerkezetek: Összetevők és illeszkedés"),
            "03": ("Actions and Reactions", "Hatásmechanizmus és átalakulás: Kölcsönhatások és áramlás"),
            "04": ("Troubleshooting and Upkeep", "Üzemzavar és karbantartás: Hatékonyság és teljesítmény"),
            "05": ("Automation & Perfection", "Optimalizálás és automatizálás: Lépésről lépésre a végeredményig")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.24-{padded}",
            "unit": 24,
            "title": en_title,
            "level": "B1",
            "grammar": "Process Reflexives (-ódik/-ődik), Procedural Connectors & Technical Descriptions",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can describe how mechanisms operate and explain processes step-by-step in Hungarian.",
                "I can talk about components, troubleshooting, maintenance, and system optimization.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can describe how mechanisms operate and explain processes step-by-step in Hungarian.",
                        "I can talk about components, troubleshooting, maintenance, and system optimization.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-24-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-24-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-24-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-24-{padded}-ex.json",
                    "exerciseRefs": [f"b1-24-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-24-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.24-consolidation",
        "unit": 24,
        "title": "Unit 24 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Operational Mechanisms, Systems Discourse & Procedural Rigor",
        "sections": [
            {
                "type": "story",
                "title": "Iskola a határon (Ottlik Géza)",
                "ref": "stories/classics/b1/b1-24-ottlik.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-24-consolidation-ex.json",
                "exerciseRefs": [f"b1-24-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-24-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 24 (b1-24)!")

if __name__ == "__main__":
    build_unit_24_core()
