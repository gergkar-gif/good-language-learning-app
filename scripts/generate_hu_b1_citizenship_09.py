#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 9: The Battle of Mohács (1526) (b1-mohacs)."""

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

def build_unit_9_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.mohacs.01",
        "lesson": "b1-mohacs-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "meggyengült", "translation": "weakened", "pos": "adjective"},
            {"lemma": "belső viszály", "translation": "internal strife, factional strife", "pos": "noun"},
            {"lemma": "parasztfelkelés", "translation": "peasant revolt (1514 Dózsa revolt)", "pos": "noun"},
            {"lemma": "jobbágyság", "translation": "serfdom, peasantry", "pos": "noun"},
            {"lemma": "megtorlás", "translation": "retaliation, reprisal", "pos": "noun"},
            {"lemma": "kincstár", "translation": "royal treasury", "pos": "noun"},
            {"lemma": "zsoldoshiány", "translation": "shortage of mercenaries", "pos": "noun"},
            {"lemma": "széthúzás", "translation": "discord, disunity", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mohacs-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.mohacs.02",
        "lesson": "b1-mohacs-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szultán", "translation": "sultan (Suleiman I)", "pos": "noun"},
            {"lemma": "hadjárat", "translation": "military campaign, expedition", "pos": "noun"},
            {"lemma": "déli végvár", "translation": "southern border fortress", "pos": "noun"},
            {"lemma": "ostrom", "translation": "siege", "pos": "noun"},
            {"lemma": "ágyú", "translation": "cannon, artillery", "pos": "noun"},
            {"lemma": "túlerő", "translation": "numerical superiority, overwhelming force", "pos": "noun"},
            {"lemma": "segítségkérés", "translation": "plea for help, appeal for assistance", "pos": "noun"},
            {"lemma": "elszigeteltség", "translation": "isolation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mohacs-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.mohacs.03",
        "lesson": "b1-mohacs-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hadrend", "translation": "battle array, battle order", "pos": "noun"},
            {"lemma": "roham", "translation": "charge, assault", "pos": "noun"},
            {"lemma": "lovasság", "translation": "cavalry", "pos": "noun"},
            {"lemma": "tüzérségi tűz", "translation": "artillery fire", "pos": "noun"},
            {"lemma": "megfutamodás", "translation": "rout, chaotic flight", "pos": "noun"},
            {"lemma": "mocsár", "translation": "marsh, swamp", "pos": "noun"},
            {"lemma": "fővezér", "translation": "commander-in-chief (Tomori Pál)", "pos": "noun"},
            {"lemma": "taktika", "translation": "tactics", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mohacs-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.mohacs.04",
        "lesson": "b1-mohacs-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "II. Lajos", "translation": "Louis II of Hungary", "pos": "noun"},
            {"lemma": "Csele-patak", "translation": "Csele brook", "pos": "noun"},
            {"lemma": "nehéz páncél", "translation": "heavy armor", "pos": "noun"},
            {"lemma": "fulladás", "translation": "drowning, suffocation", "pos": "noun"},
            {"lemma": "holttest", "translation": "corpse, body", "pos": "noun"},
            {"lemma": "menekülés", "translation": "escape, flight", "pos": "noun"},
            {"lemma": "trónörökös", "translation": "heir to the throne", "pos": "noun"},
            {"lemma": "dinasztikus válság", "translation": "dynastic crisis", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mohacs-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.mohacs.05",
        "lesson": "b1-mohacs-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fordulópont", "translation": "turning point", "pos": "noun"},
            {"lemma": "korszakhatár", "translation": "era boundary, watershed", "pos": "noun"},
            {"lemma": "nemzeti emlékezet", "translation": "national memory", "pos": "noun"},
            {"lemma": "közmondás", "translation": "proverb, adage", "pos": "noun"},
            {"lemma": "történelmi tanulság", "translation": "historical lesson", "pos": "noun"},
            {"lemma": "emlékhely", "translation": "memorial site", "pos": "noun"},
            {"lemma": "megmaradás", "translation": "national survival, persistence", "pos": "noun"},
            {"lemma": "gyász", "translation": "mourning, national mourning", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mohacs-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.mohacs.01.causality-preconditions",
        "title": "Causality & Historical Preconditions: miatt, következtében, eredményeképpen",
        "sections": [
            {
                "type": "text",
                "title": "Explaining Historical Causes and Consequences",
                "content": "To analyze complex historical causation, Hungarian uses postpositions denoting cause: *miatt* (+ nominative: 'because of'), *következtében* (+ genitive *-nak/-nek*: 'as a consequence of'), and *eredményeképpen* ('as a result of')."
            },
            {
                "type": "examples",
                "title": "Historical causation examples",
                "items": [
                    {
                        "spanish": "A nemesi széthúzás miatt az ország hadereje súlyosan meggyengült.",
                        "english": "Because of noble disunity, the country's armed forces were severely weakened."
                    },
                    {
                        "spanish": "Az 1514-es parasztfelkelés megtorlásának következtében a jobbágyok elvesztették szabad költözési jogukat.",
                        "english": "As a consequence of the retaliation for the 1514 peasant revolt, the serfs lost their right to free movement."
                    },
                    {
                        "spanish": "A kincstár üressége miatt a király nem tudott zsoldosokat toborozni.",
                        "english": "Because of the empty treasury, the king was unable to recruit mercenaries."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mohacs-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.mohacs.02.temporal-clauses",
        "title": "Temporal Conjunctions in Military Narratives: amikor, miután, mielőtt",
        "sections": [
            {
                "type": "text",
                "title": "Chronological Sequencing in Military History",
                "content": "Narrating campaigns requires temporal conjunctions: *amikor* (when), *miután* (after + past tense), and *mielőtt* (before + conditional or past). Notice that *mielőtt* frequently takes the conditional mood (*mielőtt megérkezett volna* = before it had arrived)."
            },
            {
                "type": "examples",
                "title": "Temporal campaign examples",
                "items": [
                    {
                        "spanish": "Miután I. Szulejmán szultán trónra lépett, azonnal hadjáratot indított Magyarország ellen.",
                        "english": "After Sultan Suleiman I ascended the throne, he immediately launched a campaign against Hungary."
                    },
                    {
                        "spanish": "Nándorfehérvár 1521-ben elesett, mielőtt a királyi sereg felmenthette volna.",
                        "english": "Nándorfehérvár fell in 1521 before the royal army could have relieved it."
                    },
                    {
                        "spanish": "Amikor az oszmán fősereg átkelt a Dráván, a magyar vezetők még mindig vitatkoztak.",
                        "english": "When the main Ottoman army crossed the Drava, the Hungarian leaders were still arguing."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mohacs-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.mohacs.03.rapid-sequence",
        "title": "Expressing Rapid Succession & Tactical Drama: alighogy... máris, hirtelen",
        "sections": [
            {
                "type": "text",
                "title": "Describing sudden and overwhelming events",
                "content": "Military engagements that turn abruptly use correlative constructions such as *alighogy... máris* ('no sooner had... than already...'), *rövid idő alatt* ('in a short time'), and *hirtelen* ('suddenly')."
            },
            {
                "type": "examples",
                "title": "Tactical sequence examples",
                "items": [
                    {
                        "spanish": "Alighogy megindult a magyar lovasroham, máris pusztító ágyútűzbe ütközött.",
                        "english": "Hardly had the Hungarian cavalry charge begun when it already met devastating cannon fire."
                    },
                    {
                        "spanish": "Rövid idő alatt a magyar hadrend felbomlott a hatalmas oszmán túlerővel szemben.",
                        "english": "Within a short time, the Hungarian battle line collapsed against overwhelming Ottoman superior numbers."
                    },
                    {
                        "spanish": "Tomori Pál kalocsai érsek, a sereg fővezére, hősiesen harcolva esett el a csatamezőn.",
                        "english": "Pál Tomori, archbishop of Kalocsa and commander-in-chief, fell on the battlefield fighting heroically."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mohacs-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.mohacs.04.participles-tragedy",
        "title": "Attributive & Predicative Participles in Tragedy: elmerült, megfulladt, menekülő",
        "sections": [
            {
                "type": "text",
                "title": "Using Past & Present Participles in Tragic Historical Accounts",
                "content": "Hungarian uses the past participle suffix *-t / -tt* and present participle *-ó / -ő* to characterize historical figures and their fates: *a megfulladt uralkodó* (the drowned monarch), *a menekülő katonák* (the fleeing soldiers)."
            },
            {
                "type": "examples",
                "title": "Participial tragedy examples",
                "items": [
                    {
                        "spanish": "A menekülő II. Lajos király a megáradt Csele-patakba bukott nehéz lovával.",
                        "english": "The fleeing King Louis II fell into the flooded Csele brook with his heavy horse."
                    },
                    {
                        "spanish": "A vízbe fulladt fiatal király halála azonnal dinasztikus válságot idézett elő.",
                        "english": "The death of the young king, who drowned in the water, immediately precipitated a dynastic crisis."
                    },
                    {
                        "spanish": "Az elhunyt uralkodónak nem volt gyermeke, így a Jagelló-ház magyar ága kihalt.",
                        "english": "The deceased monarch had no children, so the Hungarian branch of the Jagiellonian dynasty died out."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mohacs-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.mohacs.05.proverb-fatalism",
        "title": "Proverbial Framing & Cultural Resilience: Több is veszett Mohácsnál",
        "sections": [
            {
                "type": "text",
                "title": "Understanding the Famous Hungarian Adage",
                "content": "The famous proverb *„Több is veszett Mohácsnál”* ('More was lost at Mohács') is used in modern Hungarian to console someone experiencing a setback or failure, implying that no matter how bad the current misfortune is, the nation survived even the cataclysm of 1526."
            },
            {
                "type": "examples",
                "title": "Proverb and collective memory examples",
                "items": [
                    {
                        "spanish": "Ha valamilyen kisebb baj történik, a magyarok gyakran azt mondják: „Több is veszett Mohácsnál.”",
                        "english": "If some minor trouble occurs, Hungarians often say: 'More was lost at Mohács.'"
                    },
                    {
                        "spanish": "1526. augusztus 29-e a magyar történelem legnagyobb és legfájdalmasabb korszakhatára.",
                        "english": "August 29, 1526, is the greatest and most painful historical turning point in Hungarian history."
                    },
                    {
                        "spanish": "A mohácsi nemzeti emlékhely ma a középkori magyar állam mártírjaira emlékeztet.",
                        "english": "The Mohács national memorial site commemorates the martyrs of the medieval Hungarian state today."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mohacs-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.mohacs.01",
        "title": "A meggyengült királyság és a belső viszályok",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Following King Matthias's death in 1490, royal central power collapsed under the Jagiellon kings. The brutal suppression of the 1514 Dózsa peasant revolt left Hungarian society deeply divided on the eve of the Ottoman invasion.",
        "characters": [],
        "location": "Buda vára, magyar nemesi udvarok",
        "grammar": ["causality-preconditions"],
        "vocabularyTopics": ["A Jagelló-korszak", "Belső viszályok", "1514 parasztfelkelés"],
        "paragraphs": [
            {"type": "narration", "text": "Mátyás király halála után a fekete sereget feloszlatták, és a királyi kincstár gyorsan kiürült."},
            {"type": "narration", "text": "A Jagelló-házi uralkodók, II. Ulászló és a fiatal II. Lajos idején a főnemesek és köznemesek közötti pártharcok megbénították a kormányzatot."},
            {"type": "narration", "text": "1514-ben Dózsa György vezetésével hatalmas parasztfelkelés tört ki az elnyomó földesurak ellen."},
            {"type": "narration", "text": "A nemesek kegyetlen megtorlást hajtottak végre, és törvénybe iktatták a jobbágyok örökös röghöz kötését."},
            {"type": "narration", "text": "A mély belső társadalmi szakadék miatt az ország képtelen volt egységesen felkészülni a közeledő oszmán támadásra."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs-01-meggyengult.json", story_01)

    story_02 = {
        "id": "story.b1.mohacs.02",
        "title": "Szulejmán szultán és Nándorfehérvár eleste",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In 1520, the ambitious young Sultan Suleiman the Magnificent came to power in Istanbul. In 1521, the key southern stronghold Nándorfehérvár fell, leaving the Hungarian heartland completely exposed.",
        "characters": [],
        "location": "Nándorfehérvár (Belgrád), Konstantinápoly",
        "grammar": ["temporal-clauses"],
        "vocabularyTopics": ["I. Szulejmán szultán", "Nándorfehérvár eleste 1521", "Oszmán előrenyomulás"],
        "paragraphs": [
            {"type": "narration", "text": "1520-ban I. Szulejmán lett az Oszmán Birodalom uralkodója, aki világbirodalmi terjeszkedést tervezett Európa felé."},
            {"type": "narration", "text": "1521 nyarán a török fősereg ostrom alá vette Nándorfehérvárt, a Magyar Királyság legfontosabb déli kapuját."},
            {"type": "narration", "text": "A csekély létszámú várvédők hősiesen ellenálltak, de felmentő sereg hiányában a vár augusztus végén elesett."},
            {"type": "narration", "text": "Nándorfehérvár elvesztése után a török hadak előtt megnyílt a közvetlen út az Alföld és Buda felé."},
            {"type": "narration", "text": "A magyar udvar hiába kért pénzügyi és katonai segítséget a pápatól és a nyugat-európai uralkodóktól, Magyarország magára maradt."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs-02-elorenyomulas.json", story_02)

    story_03 = {
        "id": "story.b1.mohacs.03",
        "title": "A tragikus ütközet 1526. augusztus 29-én",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "On August 29, 1526, on the plains south of Mohács, King Louis II's 25,000 soldiers confronted Sultan Suleiman's 60,000-strong army. Despite a valiant cavalry assault, the Hungarian lines were pulverized by Ottoman cannons within two hours.",
        "characters": [],
        "location": "Mohácsi sík",
        "grammar": ["rapid-sequence"],
        "vocabularyTopics": ["Mohácsi csata 1526", "Tomori Pál", "Lovasroham és tüzérség"],
        "paragraphs": [
            {"type": "narration", "text": "1526 augusztusában II. Lajos király és Tomori Pál kalocsai érsek mintegy 25 ezer fős sereggel vonult Mohács mellé."},
            {"type": "narration", "text": "A török szultán serege legalább 60 ezer jól képzett katonából és háromszáz modern ágyúból állt."},
            {"type": "narration", "text": "Augusztus 29-én délután a magyar nehézlovasság bátor rohamot indított az oszmán vonalak ellen."},
            {"type": "narration", "text": "Alighogy áttörték az első védelmi vonalat, a janicsárok pusztító puskasorozata és az ágyútűz megtörte a támadást."},
            {"type": "narration", "text": "Alig két óra leforgása alatt a magyar sereg felbomlott, a csata véres katasztrófává és megfutamodássá vált."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs-03-csata.json", story_03)

    story_04 = {
        "id": "story.b1.mohacs.04",
        "title": "II. Lajos tragédiája a Csele-patakban",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "While escaping the battlefield in the stormy dusk, the twenty-year-old King Louis II drowned in the flooded Csele brook when his armored horse stumbled, extinguishing the royal line and throwing Hungary into civil strife.",
        "characters": [],
        "location": "Csele-patak, Duna-mellék",
        "grammar": ["participles-tragedy"],
        "vocabularyTopics": ["II. Lajos halála", "Csele-patak", "Dinasztikus válság"],
        "paragraphs": [
            {"type": "narration", "text": "A csatavesztés után a húszéves II. Lajos király néhány hűséges kísérőjével észak felé menekült a viharos szürkületben."},
            {"type": "narration", "text": "Amikor a megáradt Csele-patak meredek partjához értek, a király nehéz csataméne megcsúszott a vizes sárban."},
            {"type": "narration", "text": "A király és lova a mély vízbe zuhant; a súlyos fém páncélzat miatt az uralkodó nem tudott kimenekülni, és megfulladt."},
            {"type": "narration", "text": "Holttestét csak hetekkel később találták meg és temették el Székesfehérváron."},
            {"type": "narration", "text": "Mivel Lajos király gyermektelenül halt meg, a magyar trónért véres harc indult Szapolyai János és Habsburg Ferdinánd között."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs-04-kiralyhalala.json", story_04)

    story_05 = {
        "id": "story.b1.mohacs.05",
        "title": "Több is veszett Mohácsnál: A nemzeti emlékezet",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The disaster at Mohács in 1526 ended medieval Hungarian great-power status and led to the 150-year Ottoman occupation. It permanently entered national consciousness as the supreme benchmark of tragedy and resilience.",
        "characters": [],
        "location": "Mohácsi Nemzeti Emlékhely, Magyarország",
        "grammar": ["proverb-fatalism"],
        "vocabularyTopics": ["Korszakhatár 1526", "Több is veszett Mohácsnál", "Nemzeti emlékezet"],
        "paragraphs": [
            {"type": "narration", "text": "1526. augusztus 29-e a magyar nemzet történelmének legfontosabb és legtragikusabb korszakhatára."},
            {"type": "narration", "text": "A mohácsi vereséggel véget ért a virágzó középkori független Magyar Királyság négyszáz éves nagyhatalmi korszaka."},
            {"type": "narration", "text": "A csatavesztés megnyitotta az utat Buda 1541-es elfoglalása és az ország három részre szakadása előtt."},
            {"type": "narration", "text": "A nép ajkán született szólás — „Több is veszett Mohácsnál” — arra emlékeztet, hogy még a legsúlyosabb csapás után is talpra kell állni."},
            {"type": "narration", "text": "A mohácsi csatatéren létesített nemzeti emlékhely ma a hősök tiszteletének és a nemzeti megmaradásnak szentelt hely."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs-05-fontossag.json", story_05)

    story_combined = {
        "id": "story.b1.mohacs",
        "title": "A mohácsi csata és a középkori Magyarország bukása",
        "level": "B1",
        "order": 9,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The catastrophic collapse of medieval Hungary at the Battle of Mohács (August 29, 1526): internal disunity after 1514, the rise of Suleiman I and fall of Nándorfehérvár, the two-hour collapse against Ottoman artillery, the drowning of King Louis II in the Csele brook, and the enduring cultural memory encapsulated in 'Több is veszett Mohácsnál'.",
        "characters": [],
        "location": "Buda, Nándorfehérvár, Mohács, Csele-patak",
        "grammar": ["causality-preconditions", "temporal-clauses", "rapid-sequence", "participles-tragedy", "proverb-fatalism"],
        "vocabularyTopics": ["Mohácsi csata 1526", "II. Lajos", "Szulejmán szultán", "Tomori Pál", "Nemzeti sorsforduló"],
        "paragraphs": [
            {"type": "narration", "text": "Hunyadi Mátyás 1490-es halála után a fekete sereg feloszlott, a királyi kincstár kiürült, a pártoskodó nemesség pedig meggyengítette az államot. Az 1514-es Dózsa-féle parasztfelkelés brutális megtorlása a társadalmat végzetesen megosztotta."},
            {"type": "narration", "text": "1520-ban I. Szulejmán szultán került az Oszmán Birodalom élére. 1521-ben csapatai elfoglalták az ország legfontosabb déli védőbástyáját, Nándorfehérvárt. A segélykérések süket fülekre találtak Európában, így a Magyar Királyság magára maradt."},
            {"type": "narration", "text": "1526. augusztus 29-én Mohács mezején a Tomori Pál érsek vezette 25 ezer fős magyar sereg megütközött a szultán 60 ezer katonájával. Bár a bátor lovasroham kezdetben sikeresnek tűnt, az oszmán ágyúk és puskások tüze alig két óra alatt szétzúzta a magyar hadrendet."},
            {"type": "narration", "text": "A menekülő húszéves II. Lajos király csataménjével a megáradt Csele-patakba zuhant, ahol nehéz páncéljában a vízbe fulladt. Az ifjú uralkodó gyermektelen halála az Árpádok és Anjouk utáni független királyság végét és véres trónviszályt jelentett."},
            {"type": "narration", "text": "A mohácsi csata után az ország három részre szakadt és másfél évszázados török hódoltság alá került. A 'Több is veszett Mohácsnál' közmondás mindmáig a nemzeti sorstragédiára és a legsötétebb időkben is szükséges kitartásra figyelmezteti a magyarokat."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-mohacs.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-mohacs-01",
        "exercises": [
            {
                "id": "b1-mohacs-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["meggyengült", "weakened"],
                    ["belső viszály", "internal strife"],
                    ["parasztfelkelés", "peasant revolt"],
                    ["jobbágyság", "serfdom / peasantry"]
                ]
            },
            {
                "id": "b1-mohacs-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["megtorlás", "retaliation / reprisal"],
                    ["kincstár", "royal treasury"],
                    ["zsoldoshiány", "shortage of mercenaries"],
                    ["széthúzás", "discord / disunity"]
                ]
            },
            {
                "id": "b1-mohacs-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi történt a fekete sereggel Mátyás király 1490-es halála után?",
                "options": [
                    "A fekete sereget feloszlatták a pénzhiány és a nemesi érdekek miatt.",
                    "A sereg elfoglalta Konstantinápolyt.",
                    "A sereg megduplázta a létszámát."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben tört ki a nagy parasztfelkelés Dózsa György vezetésével?",
                "options": ["1514-ben.", "1456-ban.", "1526-ban."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik utónévvel fejezzük ki a közvetlen okot: „A nemesi széthúzás ______ az ország hadereje meggyengült.”?",
                "options": ["miatt", "felé", "helyett"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felkelés megtorlásának ____ a jobbágyok elvesztették szabad költözési jogukat. (as a consequence of)",
                "answer": "következtében"
            },
            {
                "id": "b1-mohacs-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan hatott az 1514-es felkelés leverése a magyar társadalomra?",
                "options": [
                    "Mély társadalmi szakadékot és ellenségeskedést teremtett a nemesek és a jobbágyok között.",
                    "Egyesítette az összes társadalmi réteget a király mögött.",
                    "Gazdasági virágzást és bőséges kincstári adóbevételeket hozott."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik uralkodóház tagjai voltak Magyarország királyai a mohácsi csatát közvetlenül megelőző évtizedekben?",
                "options": ["A Jagelló-ház.", "Az Árpád-ház.", "A Habsburg-ház."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi jellemezte a királyi kincstár állapotát a mohácsi vész előtt?",
                "options": [
                    "A kincstár üres volt, ezért nem tudtak elegendő zsoldoshadsereget fizetni.",
                    "A kincstárban felhalmozódott aranyból új várakat építettek.",
                    "A király feleslegesen sok külföldi katonát vásárolt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-mohacs-02",
        "exercises": [
            {
                "id": "b1-mohacs-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szultán", "sultan"],
                    ["hadjárat", "military campaign"],
                    ["déli végvár", "southern border fortress"],
                    ["ostrom", "siege"]
                ]
            },
            {
                "id": "b1-mohacs-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["ágyú", "cannon / artillery"],
                    ["túlerő", "numerical superiority"],
                    ["segítségkérés", "plea for help"],
                    ["elszigeteltség", "isolation"]
                ]
            },
            {
                "id": "b1-mohacs-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik fontos végvár esett el 1521-ben az oszmán ostrom során?",
                "options": ["Nándorfehérvár (Belgrád).", "Eger vára.", "Kőszeg."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki vezette az Oszmán Birodalom hadseregét Nándorfehérvár és Mohács idején?",
                "options": ["I. Szulejmán szultán.", "II. Mehmed szultán.", "Murád szultán."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki az időbeli utólagosságot: „______ Szulejmán trónra lépett, azonnal hadjáratot indított.”?",
                "options": ["Miután", "Habár", "Minthogy"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nándorfehérvár elesett, ____ a királyi felmentő sereg megérkezhetett volna. (before)",
                "answer": "mielőtt"
            },
            {
                "id": "b1-mohacs-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért volt katasztrófa Nándorfehérvár 1521-es elvesztése Magyarország számára?",
                "options": [
                    "Mert Nándorfehérvár volt a Magyar Királyság legfontosabb déli kapuja, és utána szabaddá vált az út Buda felé.",
                    "Mert ott őrizték a Szent Koronát.",
                    "Mert az volt a királyi székhely és a főváros."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kapott-e érdemi katonai segítséget Magyarország a nyugat-európai államoktól 1526 előtt?",
                "options": [
                    "Nem, a segélykérések eredménytelenek maradtak, és az ország lényegében magára maradt.",
                    "Igen, hatalmas francia és spanyol zsoldoshadsereg érkezett Budára.",
                    "Igen, az összes szomszédos ország közösen hadba lépett."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen haditechnikai fölényben voltak a törökök a magyar sereggel szemben?",
                "options": [
                    "Jelentős létszámbeli fölényben voltak, és korszerű tüzérséggel (sok ágyúval) rendelkeztek.",
                    "Csak lovasságuk volt tüzérség nélkül.",
                    "Kisebb volt a hadseregük, de gyorsabbak voltak a hajóik."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-mohacs-03",
        "exercises": [
            {
                "id": "b1-mohacs-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hadrend", "battle order"],
                    ["roham", "charge / assault"],
                    ["lovasság", "cavalry"],
                    ["tüzérségi tűz", "artillery fire"]
                ]
            },
            {
                "id": "b1-mohacs-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["megfutamodás", "rout / disorderly flight"],
                    ["mocsár", "marsh / swamp"],
                    ["fővezér", "commander-in-chief"],
                    ["taktika", "tactics"]
                ]
            },
            {
                "id": "b1-mohacs-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikor zajlott le a mohácsi csata?",
                "options": ["1526. augusztus 29-én.", "1456. július 22-én.", "1490. április 6-án."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt a magyar fősereg fővezére a mohácsi csatában?",
                "options": ["Tomori Pál kalocsai érsek.", "Hunyadi János.", "Zrínyi Miklós."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejezi ki a gyors egymásutániságot: „______ elindult a roham, máris ágyútűz fogadta.”?",
                "options": ["Alighogy", "Mivelhogy", "Jóllehet"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-03.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Rövid ____ alatt a magyar sereg felbomlott a túlerővel szemben. (time)",
                "answer": "idő"
            },
            {
                "id": "b1-mohacs-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Körülbelül hány katona harcolt a két oldalon a mohácsi csatában?",
                "options": [
                    "Körülbelül 25 ezer magyar állt szemben legalább 60 ezer fős oszmán sereggel.",
                    "Egyenlő létszámú, 50-50 ezer fős hadak csaptak össze.",
                    "10 ezer török harcolt 100 ezer magyar lovassal."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Körülbelül mennyi ideig tartott maga az ütközet Mohácsnál?",
                "options": [
                    "Nagyon rövid ideig, mindössze másfél-két óra alatt véget ért.",
                    "Három napon keresztül tartott a véres ostrom.",
                    "Két hétig tartó állóháború alakult ki."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi történt Tomori Pál fővezérrel a mohácsi ütközetben?",
                "options": [
                    "Hősiesen harcolva életét vesztette a csatatéren.",
                    "Sikeresen visszavonult Bécsbe.",
                    "Török fogságba esett és Konstantinápolyba hurcolták."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-mohacs-04",
        "exercises": [
            {
                "id": "b1-mohacs-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["II. Lajos", "King Louis II of Hungary"],
                    ["Csele-patak", "Csele brook"],
                    ["nehéz páncél", "heavy armor"],
                    ["fulladás", "drowning / suffocation"]
                ]
            },
            {
                "id": "b1-mohacs-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["holttest", "corpse / body"],
                    ["menekülés", "flight / escape"],
                    ["trónörökös", "heir to the throne"],
                    ["dinasztikus válság", "dynastic crisis"]
                ]
            },
            {
                "id": "b1-mohacs-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan vesztette életét II. Lajos magyar király a mohácsi csata után?",
                "options": [
                    "Menekülés közben nehéz páncéljában a megáradt Csele-patakba fulladt.",
                    "A csatamezőn janicsárok nyilaitól esett el.",
                    "Túlélte a csatát és Budán halt meg idős korban."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hány éves volt II. Lajos király halálakor?",
                "options": ["Alig húszéves volt.", "Negyvenöt éves volt.", "Hatvan éves volt."],
                "correct": 0
            },
            {
                "id": "b1-mohacs-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik befejezett melléknévi igenév illik a mondatba: „A vízbe ______ király holttestét hetekkel később találták meg.”?",
                "options": ["fulladt", "fulladó", "fulladni"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A súlyos vas ____ miatt a fiatal király nem tudott kimászni a sáros patakból. (armor)",
                "answer": "páncél"
            },
            {
                "id": "b1-mohacs-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért okozott súlyos dinasztikus és politikai válságot II. Lajos halála?",
                "options": [
                    "Mert nem hagyott hátra trónörököst, így két királyt is megválasztottak (Szapolyai Jánost és Habsburg Ferdinándot).",
                    "Mert nem volt senki, aki eltemette volna.",
                    "Mert azonnal véget ért a háború."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hol temették el végül a megtalált II. Lajos királyt?",
                "options": [
                    "Székesfehérváron, a királyi bazilikában.",
                    "Visegrádon.",
                    "Esztergomban."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik dinasztia magyarországi uralma ért véget II. Lajos király halálával?",
                "options": [
                    "A Jagelló-dinasztia.",
                    "A Hunyadi-család.",
                    "Az Anjou-ház."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-mohacs-05",
        "exercises": [
            {
                "id": "b1-mohacs-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fordulópont", "turning point"],
                    ["korszakhatár", "era boundary / watershed"],
                    ["nemzeti emlékezet", "national memory"],
                    ["közmondás", "proverb / adage"]
                ]
            },
            {
                "id": "b1-mohacs-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["történelmi tanulság", "historical lesson"],
                    ["emlékhely", "memorial site"],
                    ["megmaradás", "national survival / persistence"],
                    ["gyász", "national mourning"]
                ]
            },
            {
                "id": "b1-mohacs-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a híres magyar szólás: „Több is veszett Mohácsnál”?",
                "options": [
                    "Bármilyen baj ér bennünket, a nemzet túlélt egy még nagyobb katasztrófát is, ezért nem szabad elcsüggedni.",
                    "Azt, hogy Mohácsnál senki sem halt meg.",
                    "Azt, hogy Mohács győzelmet hozott az országnak."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen korszak vette kezdetét Magyarországon a mohácsi csatavesztést követően?",
                "options": [
                    "A 150 éves török hódoltság és az ország három részre szakadása.",
                    "Az ipari forradalom korszaka.",
                    "A reneszánsz aranykor kezdete."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igealak szerepel a közmondásban: „Több is ______ Mohácsnál.”?",
                "options": ["veszett", "veszne", "veszítene"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1526. augusztus 29-e a magyar történelem legnagyobb ____. (turning point)",
                "answer": "fordulópontja"
            },
            {
                "id": "b1-mohacs-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért tekinti a magyar történetírás 1526-ot a középkor végének Magyarországon?",
                "options": [
                    "Mert Mohácsnál elbukott az önálló középkori Magyar Királyság, és az ország elveszítette egységét.",
                    "Mert ekkor vezették be a forintot mint pénznemet.",
                    "Mert ekkor koronázták meg Szent Istvánt."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen intézmény őrzi ma a csata és az áldozatok emlékét a helyszínen?",
                "options": [
                    "A Mohácsi Nemzeti Emlékhely a tömegsírokkal és faemlékművekkel.",
                    "A Parlament kupolacsarnoka.",
                    "A Budavári Palota Nemzeti Galériája."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen üzenetet hordoz Mohács a mai magyar nemzeti tudatban?",
                "options": [
                    "Az áldozatok iránti tiszteletet, a nemzeti összetartozás fontosságát és a nehézségek utáni talpra állást.",
                    "Azt, hogy a diplomácia soha nem segít.",
                    "Azt, hogy a hadsereget teljesen fel kell számolni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-mohacs-consolidation",
        "exercises": [
            {
                "id": "b1-mohacs-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["meggyengült", "weakened"],
                    ["parasztfelkelés", "peasant revolt"],
                    ["kincstár", "treasury"],
                    ["megtorlás", "reprisal / retaliation"]
                ]
            },
            {
                "id": "b1-mohacs-consolidation.ex02",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szultán", "sultan"],
                    ["ágyú", "cannon / artillery"],
                    ["túlerő", "numerical superiority"],
                    ["déli végvár", "southern border fortress"]
                ]
            },
            {
                "id": "b1-mohacs-consolidation.ex03",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hadrend", "battle order"],
                    ["roham", "charge"],
                    ["megfutamodás", "rout / flight"],
                    ["fővezér", "commander-in-chief"]
                ]
            },
            {
                "id": "b1-mohacs-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Csele-patak", "Csele brook"],
                    ["páncél", "armor"],
                    ["fordulópont", "turning point"],
                    ["emlékhely", "memorial site"]
                ]
            },
            {
                "id": "b1-mohacs-consolidation.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évszámhoz kötődik a mohácsi csata?",
                "options": ["1526", "1456", "1490", "1541"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt a török hadak vezetője a mohácsi csatában?",
                "options": ["I. Szulejmán szultán", "II. Mehmed szultán", "Ibrahim pasa", "Murád szultán"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki vezette a magyar sereget fővezérként Mohácsnál?",
                "options": ["Tomori Pál kalocsai érsek", "Hunyadi János", "Zrínyi Miklós", "Dózsa György"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol és hogyan halt meg a fiatal II. Lajos király?",
                "options": [
                    "A megáradt Csele-patakba fulladt nehéz páncéljában.",
                    "A csatamezőn érte ágyúgolyó.",
                    "Török fogságban halt meg Isztambulban.",
                    "Budán halt meg mérgezésben."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex09",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a következményt?",
                "options": [
                    "A belső viszályok következtében az ország nem tudott felkészülni a háborúra.",
                    "A belső viszályok általában az ország nem tudott.",
                    "A belső viszályok felett az ország nem tudott."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex10",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A közmondás szerint: „Több is ____ Mohácsnál.” (was lost)",
                "answer": "veszett"
            },
            {
                "id": "b1-mohacs-consolidation.ex11",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A királyi haderő a nemesi széthúzás ____ gyengült meg. (because of)",
                "answer": "miatt"
            },
            {
                "id": "b1-mohacs-consolidation.ex12",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Alighogy megindult a magyar roham, ____ pusztító ágyútűzbe ütközött. (already)",
                "answer": "máris"
            },
            {
                "id": "b1-mohacs-consolidation.ex13",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vízbe ____ II. Lajos király holttestét csak hetekkel később találták meg. (drowned)",
                "answer": "fulladt"
            },
            {
                "id": "b1-mohacs-consolidation.ex14",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik várat hívták a középkori Magyar Királyság kulcsának, amely 1521-ben elesett?",
                "options": ["Nándorfehérvárt (Belgrád)", "Eger várát", "Buda várát", "Pozsony várát"],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex15",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mihez vezetett II. Lajos gyermektelen halála a csata után?",
                "options": [
                    "Kettős királyválasztáshoz és dinasztikus polgárháborúhoz Szapolyai János és Habsburg Ferdinánd között.",
                    "A Magyar Köztársaság kikiáltásához.",
                    "A török seregek azonnali békés kivonulásához.",
                    "Egy lengyel király békés megválasztásához."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex16",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen geopolitikai következménye lett a mohácsi vereségnek a 16. században?",
                "options": [
                    "Az ország három részre szakadt: a Királyi Magyarországra, az Erdélyi Fejedelemségre és a Török Hódoltságra.",
                    "Magyarország azonnal elfoglalta Bécset.",
                    "Az Oszmán Birodalom teljesen összeomlott.",
                    "Magyarország beolvadt Lengyelországba."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex17",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen társadalmi feszültség előzte meg Mohácsot 1514-ben?",
                "options": [
                    "A Dózsa György-féle parasztfelkelés és annak véres megtorlása.",
                    "A budai céhek sztrájkja.",
                    "A reformáció kezdete Debrecenben.",
                    "A bányászok felkelése Selmecbányán."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex18",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit fejez ki a magyar kultúrában a „Több is veszett Mohácsnál” kifejezés használata?",
                "options": [
                    "Vigasztalást és kitartást nehéz helyzetekben, emlékeztetve a nemzet túlélő képességére.",
                    "A katonai harc folytatását minden áron.",
                    "A történelem elfelejtésének szükségességét.",
                    "Kizárólag anyagi javak elvesztését."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex19",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik csatával egyenértékű nemzeti sorstragédia a magyar történelemben az 1526-os mohácsi vereség?",
                "options": [
                    "Az önálló középkori magyar nagyhatalmi államiság lezárulásával és az ország feldarabolódásával.",
                    "A tatárjárás utáni azonnali békével.",
                    "A honfoglalás befejezésével.",
                    "Az aranybulla kiadásával."
                ],
                "correct": 0
            },
            {
                "id": "b1-mohacs-consolidation.ex20",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol található ma a csata emlékére kialakított Nemzeti Emlékhely?",
                "options": [
                    "Mohács mellett, Sátorhely közelében.",
                    "Budapesten a Hősök terén.",
                    "A Hortobágyon.",
                    "Esztergomban a Bazilikánál."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mohacs-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.mohacs-01",
        "title": "A meggyengült királyság (The Weakened Kingdom)",
        "level": "B1",
        "grammar": "Causality & Preconditions: miatt, következtében, eredményeképpen",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the domestic political and financial crisis in Hungary after King Matthias's death.",
                    "I can explain the impact of the 1514 Dózsa peasant revolt on social unity.",
                    "I can express complex historical causes using postpositions: miatt, következtében, eredményeképpen.",
                    "I can master eight new vocabulary items related to internal strife and feudal discord."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-mohacs-01-meggyengult.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-mohacs-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-mohacs-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-mohacs-01-ex.json", "exerciseRefs": [
                "b1-mohacs-01.ex01", "b1-mohacs-01.ex01b", "b1-mohacs-01.ex02", "b1-mohacs-01.ex03",
                "b1-mohacs-01.ex04", "b1-mohacs-01.ex05", "b1-mohacs-01.ex06", "b1-mohacs-01.ex07", "b1-mohacs-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the domestic political and financial crisis in Hungary after King Matthias's death.",
                    "I can explain the impact of the 1514 Dózsa peasant revolt on social unity.",
                    "I can express complex historical causes using postpositions: miatt, következtében, eredményeképpen.",
                    "I can master eight new vocabulary items related to internal strife and feudal discord."
                ]
            }
        ],
        "goal": [
            "I can describe the domestic political and financial crisis in Hungary after King Matthias's death.",
            "I can explain the impact of the 1514 Dózsa peasant revolt on social unity.",
            "I can express complex historical causes using postpositions: miatt, következtében, eredményeképpen.",
            "I can master eight new vocabulary items related to internal strife and feudal discord."
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.mohacs-02",
        "title": "Az oszmán előrenyomulás (The Ottoman Advance)",
        "level": "B1",
        "grammar": "Temporal Conjunctions: amikor, miután, mielőtt",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the rise of Sultan Suleiman I and his military offensive against Hungary.",
                    "I can explain the strategic catastrophe of the fall of Nándorfehérvár in 1521.",
                    "I can construct chronological military narratives using amikor, miután, and mielőtt.",
                    "I can use eight new vocabulary items related to siegecraft and Ottoman expansion."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-mohacs-02-elorenyomulas.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-mohacs-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-mohacs-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-mohacs-02-ex.json", "exerciseRefs": [
                "b1-mohacs-02.ex01", "b1-mohacs-02.ex01b", "b1-mohacs-02.ex02", "b1-mohacs-02.ex03",
                "b1-mohacs-02.ex04", "b1-mohacs-02.ex05", "b1-mohacs-02.ex06", "b1-mohacs-02.ex07", "b1-mohacs-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the rise of Sultan Suleiman I and his military offensive against Hungary.",
                    "I can explain the strategic catastrophe of the fall of Nándorfehérvár in 1521.",
                    "I can construct chronological military narratives using amikor, miután, and mielőtt.",
                    "I can use eight new vocabulary items related to siegecraft and Ottoman expansion."
                ]
            }
        ],
        "goal": [
            "I can describe the rise of Sultan Suleiman I and his military offensive against Hungary.",
            "I can explain the strategic catastrophe of the fall of Nándorfehérvár in 1521.",
            "I can construct chronological military narratives using amikor, miután, and mielőtt.",
            "I can use eight new vocabulary items related to siegecraft and Ottoman expansion."
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.mohacs-03",
        "title": "A csata lefolyása (The Battle of Mohács)",
        "level": "B1",
        "grammar": "Rapid Succession & Tactical Sequence: alighogy... máris, rövid idő alatt",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can recount the course of the Battle of Mohács on August 29, 1526.",
                    "I can identify Archbishop Pál Tomori and his tactical choices during the battle.",
                    "I can express rapid sequences and tactical shifts using alighogy... máris and hirtelen.",
                    "I can utilize eight new vocabulary items concerning battlefield orders and cavalry charges."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-mohacs-03-csata.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-mohacs-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-mohacs-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-mohacs-03-ex.json", "exerciseRefs": [
                "b1-mohacs-03.ex01", "b1-mohacs-03.ex01b", "b1-mohacs-03.ex02", "b1-mohacs-03.ex03",
                "b1-mohacs-03.ex04", "b1-mohacs-03.ex05", "b1-mohacs-03.ex06", "b1-mohacs-03.ex07", "b1-mohacs-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can recount the course of the Battle of Mohács on August 29, 1526.",
                    "I can identify Archbishop Pál Tomori and his tactical choices during the battle.",
                    "I can express rapid sequences and tactical shifts using alighogy... máris and hirtelen.",
                    "I can utilize eight new vocabulary items concerning battlefield orders and cavalry charges."
                ]
            }
        ],
        "goal": [
            "I can recount the course of the Battle of Mohács on August 29, 1526.",
            "I can identify Archbishop Pál Tomori and his tactical choices during the battle.",
            "I can express rapid sequences and tactical shifts using alighogy... máris and hirtelen.",
            "I can utilize eight new vocabulary items concerning battlefield orders and cavalry charges."
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.mohacs-04",
        "title": "A király halála (The King's Death)",
        "level": "B1",
        "grammar": "Past Participles in Tragedy: megfulladt, elhunyt, menekülő",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can narrate the tragedy of King Louis II in the swollen Csele brook.",
                    "I can explain the dynastic crisis and double king election caused by his childless demise.",
                    "I can use attributive and predicative past participles to describe historical events.",
                    "I can deploy eight new vocabulary items regarding royal demise and political succession."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-mohacs-04-kiralyhalala.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-mohacs-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-mohacs-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-mohacs-04-ex.json", "exerciseRefs": [
                "b1-mohacs-04.ex01", "b1-mohacs-04.ex01b", "b1-mohacs-04.ex02", "b1-mohacs-04.ex03",
                "b1-mohacs-04.ex04", "b1-mohacs-04.ex05", "b1-mohacs-04.ex06", "b1-mohacs-04.ex07", "b1-mohacs-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the tragedy of King Louis II in the swollen Csele brook.",
                    "I can explain the dynastic crisis and double king election caused by his childless demise.",
                    "I can use attributive and predicative past participles to describe historical events.",
                    "I can deploy eight new vocabulary items regarding royal demise and political succession."
                ]
            }
        ],
        "goal": [
            "I can narrate the tragedy of King Louis II in the swollen Csele brook.",
            "I can explain the dynastic crisis and double king election caused by his childless demise.",
            "I can use attributive and predicative past participles to describe historical events.",
            "I can deploy eight new vocabulary items regarding royal demise and political succession."
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.mohacs-05",
        "title": "Miért fontos Mohács ma is? (Why Mohács Matters Today)",
        "level": "B1",
        "grammar": "Proverbs & Fatalism: Több is veszett Mohácsnál",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the cultural meaning and usage of 'Több is veszett Mohácsnál'.",
                    "I can articulate why August 29, 1526, is seen as the end of the medieval Hungarian state.",
                    "I can discuss the Mohács National Memorial Site (Mohácsi Nemzeti Emlékhely).",
                    "I can answer citizenship interview questions about Mohács with high historical accuracy."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-mohacs-05-fontossag.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-mohacs-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-mohacs-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-mohacs-05-ex.json", "exerciseRefs": [
                "b1-mohacs-05.ex01", "b1-mohacs-05.ex01b", "b1-mohacs-05.ex02", "b1-mohacs-05.ex03",
                "b1-mohacs-05.ex04", "b1-mohacs-05.ex05", "b1-mohacs-05.ex06", "b1-mohacs-05.ex07", "b1-mohacs-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain the cultural meaning and usage of 'Több is veszett Mohácsnál'.",
                    "I can articulate why August 29, 1526, is seen as the end of the medieval Hungarian state.",
                    "I can discuss the Mohács National Memorial Site (Mohácsi Nemzeti Emlékhely).",
                    "I can answer citizenship interview questions about Mohács with high historical accuracy."
                ]
            }
        ],
        "goal": [
            "I can explain the cultural meaning and usage of 'Több is veszett Mohácsnál'.",
            "I can articulate why August 29, 1526, is seen as the end of the medieval Hungarian state.",
            "I can discuss the Mohács National Memorial Site (Mohácsi Nemzeti Emlékhely).",
            "I can answer citizenship interview questions about Mohács with high historical accuracy."
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.mohacs-consolidation",
        "title": "Unit 9 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can summarize the causes, events, and consequences of the Battle of Mohács (1526).",
                    "I can explain the strategic loss of Nándorfehérvár, the tactics at Mohács, and King Louis II's death.",
                    "I can analyze the cultural impact and proverb 'Több is veszett Mohácsnál'.",
                    "I can answer all citizenship examination questions on the 1526 turning point fluently."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-mohacs-consolidation-ex.json", "exerciseRefs": [
                "b1-mohacs-consolidation.ex01", "b1-mohacs-consolidation.ex02", "b1-mohacs-consolidation.ex03", "b1-mohacs-consolidation.ex04",
                "b1-mohacs-consolidation.ex05", "b1-mohacs-consolidation.ex06", "b1-mohacs-consolidation.ex07", "b1-mohacs-consolidation.ex08",
                "b1-mohacs-consolidation.ex09", "b1-mohacs-consolidation.ex10", "b1-mohacs-consolidation.ex11", "b1-mohacs-consolidation.ex12",
                "b1-mohacs-consolidation.ex13", "b1-mohacs-consolidation.ex14", "b1-mohacs-consolidation.ex15", "b1-mohacs-consolidation.ex16",
                "b1-mohacs-consolidation.ex17", "b1-mohacs-consolidation.ex18", "b1-mohacs-consolidation.ex19", "b1-mohacs-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can summarize the causes, events, and consequences of the Battle of Mohács (1526).",
                    "I can explain the strategic loss of Nándorfehérvár, the tactics at Mohács, and King Louis II's death.",
                    "I can analyze the cultural impact and proverb 'Több is veszett Mohácsnál'.",
                    "I can answer all citizenship examination questions on the 1526 turning point fluently."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-mohacs-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_9_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 9 (b1-mohacs)!")
