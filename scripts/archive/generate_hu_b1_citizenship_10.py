#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 10: Three Parts of Hungary (b1-haromresz)."""

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

def build_unit_10_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.haromresz.01",
        "lesson": "b1-haromresz-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Királyi Magyarország", "translation": "Royal Hungary (Habsburg-ruled north & west)", "pos": "noun"},
            {"lemma": "Habsburg-kormányzat", "translation": "Habsburg administration", "pos": "noun"},
            {"lemma": "Pozsony", "translation": "Pozsony (Bratislava, coronation capital)", "pos": "noun"},
            {"lemma": "kancellária", "translation": "chancellery", "pos": "noun"},
            {"lemma": "nádor", "translation": "palatine (highest kingdom dignitary)", "pos": "noun"},
            {"lemma": "rendi gyűlés", "translation": "diet of estates, parliament", "pos": "noun"},
            {"lemma": "végvárvonal", "translation": "border fortress line", "pos": "noun"},
            {"lemma": "határvédelem", "translation": "border defense", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-haromresz-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.haromresz.02",
        "lesson": "b1-haromresz-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Török Hódoltság", "translation": "Ottoman-ruled central Hungary (1541–1699)", "pos": "noun"},
            {"lemma": "vilajet", "translation": "vilayet (Ottoman administrative province)", "pos": "noun"},
            {"lemma": "budai pasa", "translation": "pasha of Buda", "pos": "noun"},
            {"lemma": "defterdár", "translation": "defterdar (Ottoman tax official)", "pos": "noun"},
            {"lemma": "dzsámi", "translation": "mosque", "pos": "noun"},
            {"lemma": "minaret", "translation": "minaret", "pos": "noun"},
            {"lemma": "törökfürdő", "translation": "Turkish thermal bath", "pos": "noun"},
            {"lemma": "kettős adóztatás", "translation": "double taxation (to Turks and Hungarian nobles)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-haromresz-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.haromresz.03",
        "lesson": "b1-haromresz-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Erdélyi Fejedelemség", "translation": "Principality of Transylvania", "pos": "noun"},
            {"lemma": "fejedelem", "translation": "ruling prince of Transylvania", "pos": "noun"},
            {"lemma": "Gyulafehérvár", "translation": "Gyulafehérvár (Alba Iulia, princely seat)", "pos": "noun"},
            {"lemma": "vallásszabadság", "translation": "religious freedom (1568 Diet of Torda)", "pos": "noun"},
            {"lemma": "adófizetés", "translation": "tribute payment (haradzs to the Sultan)", "pos": "noun"},
            {"lemma": "anyanyelvi kultúra", "translation": "vernacular / Hungarian-language culture", "pos": "noun"},
            {"lemma": "reformáció", "translation": "Reformation", "pos": "noun"},
            {"lemma": "közvetítő szerep", "translation": "mediating role (between East and West)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-haromresz-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.haromresz.04",
        "lesson": "b1-haromresz-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "végvári vitéz", "translation": "border fortress soldier / hero", "pos": "noun"},
            {"lemma": "bajvívás", "translation": "single combat / duel between champions", "pos": "noun"},
            {"lemma": "portya", "translation": "cavalry raid, foray", "pos": "noun"},
            {"lemma": "mezőváros", "translation": "market town (oppidum)", "pos": "noun"},
            {"lemma": "marhakereskedelem", "translation": "cattle trade (grey cattle driving to the West)", "pos": "noun"},
            {"lemma": "elnéptelenedés", "translation": "depopulation", "pos": "noun"},
            {"lemma": "paraszti ellenállás", "translation": "peasant resilience / resistance", "pos": "noun"},
            {"lemma": "együttélés", "translation": "coexistence", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-haromresz-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.haromresz.05",
        "lesson": "b1-haromresz-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "megosztottság", "translation": "division, tripartite partition", "pos": "noun"},
            {"lemma": "másfél évszázad", "translation": "century and a half (150 years)", "pos": "noun"},
            {"lemma": "nemzeti egység", "translation": "national unity", "pos": "noun"},
            {"lemma": "túlélés", "translation": "survival", "pos": "noun"},
            {"lemma": "rombolás", "translation": "destruction, devastation", "pos": "noun"},
            {"lemma": "folytonosság", "translation": "continuity (of Hungarian law and statehood)", "pos": "noun"},
            {"lemma": "visszafoglalás", "translation": "reconquest (expulsion of Ottomans)", "pos": "noun"},
            {"lemma": "újjáépítés", "translation": "rebuilding, reconstruction", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-haromresz-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.haromresz.01.administrative-framing",
        "title": "Administrative Framing & Capital Seats: Pozsony székhellyel, központként",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Administrative Status and Institutional Seats",
                "content": "In historical and legal descriptions, administrative centers use the sociative construction *valamilyen székhellyel* ('with ... as seat/capital') or the essive-formal suffix *-ként* (*fővárosként, központként* = 'as a capital, as a center')."
            },
            {
                "type": "examples",
                "title": "Administrative framing examples",
                "items": [
                    {
                        "spanish": "A Királyi Magyarország Pozsony székhellyel működött, mint a Habsburg-kormányzat központja.",
                        "english": "Royal Hungary operated with Pozsony as its seat, as the center of the Habsburg administration."
                    },
                    {
                        "spanish": "A magyar rendi gyűlések színhelyeként Pozsony a politikai élet központjává vált.",
                        "english": "As the venue for Hungarian diets of estates, Pozsony became the center of political life."
                    },
                    {
                        "spanish": "A nádor a király után a legmagasabb méltóságként vezette az ország ügyeit.",
                        "english": "As the highest dignitary after the king, the palatine directed the kingdom's affairs."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-haromresz-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.haromresz.02.ottoman-terminology",
        "title": "Ottoman Terminology & Complex Administrative Systems in Hungarian",
        "sections": [
            {
                "type": "text",
                "title": "Historical Terminology and Subordinate Systems",
                "content": "Discussing the Ottoman occupation (*Török Hódoltság*) involves integrating historical loanwords into Hungarian morphology (*vilajet, vilajetben, vilajetekre; budai pasa, pasaság; defterdár*). Notice compound nouns like *kettős adóztatás* (double taxation)."
            },
            {
                "type": "examples",
                "title": "Ottoman occupation terminology examples",
                "items": [
                    {
                        "spanish": "Buda 1541-es cseles elfoglalása után az oszmánok vilajetekre osztották a meghódított területeket.",
                        "english": "After the cunning capture of Buda in 1541, the Ottomans divided the conquered lands into vilayets."
                    },
                    {
                        "spanish": "A budai pasa a szultán közvetlen képviselőjeként irányította a hódoltsági közigazgatást.",
                        "english": "As the sultan's direct representative, the pasha of Buda administered the occupied territory's governance."
                    },
                    {
                        "spanish": "A magyar jobbágyok kettős adóztatás alá estek: a töröknek és a magyar nemeseknek is fizettek.",
                        "english": "Hungarian serfs fell under double taxation: they paid both to the Turks and to Hungarian nobles."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-haromresz-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.haromresz.03.concessive-clauses",
        "title": "Diplomatic Balance & Concession: noha, bár, jóllehet, ugyanakkor",
        "sections": [
            {
                "type": "text",
                "title": "Concessive Clauses in Geopolitical History",
                "content": "Narrating Transylvania's balancing act between two empires requires concessive conjunctions: *bár / noha / jóllehet* ('although, even though') and contrasting adverbs like *ugyanakkor* ('at the same time') and *mindazonáltal* ('nonetheless')."
            },
            {
                "type": "examples",
                "title": "Diplomatic balance examples",
                "items": [
                    {
                        "spanish": "Noha Erdély adót fizetett a szultánnak, belső önállóságát és magyar kultúráját megőrizte.",
                        "english": "Although Transylvania paid tribute to the sultan, it preserved its internal autonomy and Hungarian culture."
                    },
                    {
                        "spanish": "Bár a fejedelemség két hatalmas birodalom között lavírozott, virágzó kulturális központtá fejlődött.",
                        "english": "Although the principality balanced between two giant empires, it developed into a thriving cultural center."
                    },
                    {
                        "spanish": "Az 1568-as tordai országgyűlésen törvénybe iktatták a vallásszabadságot, ami Európában egyedülálló volt.",
                        "english": "At the 1568 Diet of Torda, religious freedom was enacted into law, which was unique in Europe."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-haromresz-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.haromresz.04.historical-routines",
        "title": "Describing Historical Routines & Habitual Past: rendszeresen, gyakran, szokás volt",
        "sections": [
            {
                "type": "text",
                "title": "Habitual Life and Border Warfare Routines",
                "content": "To depict habitual life along the frontier, Hungarian uses frequency adverbs (*rendszeresen* = regularly, *gyakran* = often, *folyamatosan* = continuously) and impersonal expressions like *szokás volt* (+ infinitive: 'it was customary to...')."
            },
            {
                "type": "examples",
                "title": "Habitual historical routine examples",
                "items": [
                    {
                        "spanish": "A végvári vitézek rendszeresen portyáztak a határvidéken, hogy megvédjék a falvakat.",
                        "english": "Border fortress warriors regularly raided the borderlands to protect the villages."
                    },
                    {
                        "spanish": "A két sereg bajnokai között szokás volt a bajvívás a várak falai előtt.",
                        "english": "Between the champions of the two armies, it was customary to engage in single combat before the fortress walls."
                    },
                    {
                        "spanish": "A mezővárosok kereskedői százezrével hajtották a szürkemarhát a nyugati piacokra.",
                        "english": "Merchants from market towns drove grey cattle by the hundreds of thousands to western markets."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-haromresz-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.haromresz.05.temporal-durations",
        "title": "Long-Duration Historical Expressions: másfél évszázadon át, évtizedekig",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Long Historical Durations and Continuity",
                "content": "To measure extended historical periods, use postpositions and adverbial case suffixes: *másfél évszázadon keresztül / át* (across a century and a half), *évtizedekig tartó* (lasting for decades), and *végig* (throughout)."
            },
            {
                "type": "examples",
                "title": "Extended duration examples",
                "items": [
                    {
                        "spanish": "Magyarország másfél évszázadon keresztül három részre szakadva létezett.",
                        "english": "Hungary existed partitioned into three parts across a century and a half."
                    },
                    {
                        "spanish": "A megosztottság ellenére a magyar jog és nemzeti öntudat folytonossága fennmaradt.",
                        "english": "Despite the division, the continuity of Hungarian law and national consciousness survived."
                    },
                    {
                        "spanish": "Buda 1686-os visszafoglalása után megindult a lerombolt ország újjáépítése.",
                        "english": "After the reconquest of Buda in 1686, the reconstruction of the devastated country began."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-haromresz-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.haromresz.01",
        "title": "A Királyi Magyarország és Pozsony",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Following Mohács and the fall of Buda, the northern and western parts of Hungary came under Habsburg rule as Royal Hungary, with Pozsony (Bratislava) serving as the kingdom's coronation capital and administrative center.",
        "characters": [],
        "location": "Pozsony, Bécs, Észak- és Nyugat-Magyarország",
        "grammar": ["administrative-framing"],
        "vocabularyTopics": ["Királyi Magyarország", "Pozsony főváros", "Habsburg-kormányzat"],
        "paragraphs": [
            {"type": "narration", "text": "A mohácsi csata után a Habsburg-házi I. Ferdinándot is magyar királlyá választották."},
            {"type": "narration", "text": "Az ország északi és nyugati területeiből alakult ki a Királyi Magyarország, amely a Habsburg Birodalom részévé vált."},
            {"type": "narration", "text": "Mivel Buda török kézre került, a Magyar Királyság új fővárosa és koronázó városa Pozsony lett."},
            {"type": "narration", "text": "Pozsonyban működött a magyar kancellária és a kamara, és a Szent Márton-dómban koronázták meg a magyar királyokat."},
            {"type": "narration", "text": "A magyar rendek a pozsonyi országgyűléseken küzdöttek az alkotmányos jogokért és a végvárrendszer fenntartásáért."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz-01-kiralyi.json", story_01)

    story_02 = {
        "id": "story.b1.haromresz.02",
        "title": "Buda 1541-es elfoglalása és a Hódoltság",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "On August 29, 1541, Sultan Suleiman captured Buda Castle through trickery without firing a shot, establishing the Ottoman-ruled territory (Hódoltság) across the heart of Hungary for 150 years.",
        "characters": [],
        "location": "Buda vára, Alföld, Duna-kanyar",
        "grammar": ["ottoman-terminology"],
        "vocabularyTopics": ["Buda elfoglalása 1541", "Török Hódoltság", "Vilajetek és pasák"],
        "paragraphs": [
            {"type": "narration", "text": "1541. augusztus 29-én, pontosan tizenöt évvel a mohácsi csata után Szulejmán szultán hatalmas sereggel érkezett Buda alá."},
            {"type": "narration", "text": "A török katonák barátként, békésen sétáltak be a várba, majd egy adott jelre kardot rántottak és elfoglalták az erődöt."},
            {"type": "narration", "text": "Ezzel a csellel megkezdődött az ország középső területeit magában foglaló, 150 évig tartó Török Hódoltság korszaka."},
            {"type": "narration", "text": "Buda vilajetközponttá vált, a budai pasa irányította a tartományt, a keresztény templomokat pedig dzsámikká alakították át."},
            {"type": "narration", "text": "A lakosság kettős adóztatástól szenvedett, de a török kor emlékei — mint a gyógyfürdők és minaretek — máig láthatók Magyarországon."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz-02-hodoltsag.json", story_02)

    story_03 = {
        "id": "story.b1.haromresz.03",
        "title": "Erdély: A magyar kultúra és a vallásszabadság bástyája",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In the east, the Principality of Transylvania arose under John Sigismund and later princes. Headquartered in Gyulafehérvár, Transylvania preserved Hungarian language and enacted Europe's first law on religious tolerance in 1568.",
        "characters": [],
        "location": "Gyulafehérvár, Torda, Kolozsvár",
        "grammar": ["concessive-clauses"],
        "vocabularyTopics": ["Erdélyi Fejedelemség", "1568 Tordai ediktum", "Vallásszabadság"],
        "paragraphs": [
            {"type": "narration", "text": "A Kárpátok keleti hegyei között létrejött az Erdélyi Fejedelemség Szapolyai János fia, János Zsigmond vezetésével."},
            {"type": "narration", "text": "Bár Erdély a török szultán hűbérese volt és éves adót fizetett Isztambulnak, belső függetlenséget élvezett."},
            {"type": "narration", "text": "Gyulafehérvár lett a fejedelmi székhely, ahol a reformáció eszméi termékeny talajra találtak, és virágzott a magyar nyelvű irodalom."},
            {"type": "narration", "text": "1568-ban a tordai országgyűlésen a világon legelőször iktatták törvénybe a vallásszabadságot négy keresztény felekezet számára."},
            {"type": "narration", "text": "Erdély évszázadokon át a magyar önállóság, az anyanyelvi műveltség és a diplomáciai egyensúlyozás jelképévé vált."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz-03-erdely.json", story_03)

    story_04 = {
        "id": "story.b1.haromresz.04",
        "title": "Végvári élet és mezővárosi virágzás a határokon",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Along the border fortress chain (Eger, Szigetvár, Győr), heroic border warriors fought daily skirmishes. Concurrently, the agricultural market towns of the Great Plain grew wealthy trading Hungarian grey cattle to western Europe.",
        "characters": [],
        "location": "Eger, Szigetvár, Debrecen, Kecskemét",
        "grammar": ["historical-routines"],
        "vocabularyTopics": ["Végvári élet", "Mezővárosok", "Szürkemarha kereskedelem"],
        "paragraphs": [
            {"type": "narration", "text": "A három országrész határán több száz kilométer hosszan kiépült a híres magyar végvárvonal."},
            {"type": "narration", "text": "Eger, Győr, Kanizsa és Szigetvár falainál a végvári vitézek mindennapos harcokban, bajvívásokban és portyákban védték a hazát."},
            {"type": "narration", "text": "Ugyanakkor a háborús pusztítás közepette az alföldi mezővárosok — mint Kecskemét, Nagykőrös és Debrecen — megerősödtek."},
            {"type": "narration", "text": "A tőzsérek évente több tízezer magyar szürkemarhát hajtottak lábon a bécsi, nürnbergi és velencei piacokra."},
            {"type": "narration", "text": "A kereskedelemből származó jövedelem segített a lakosságnak túlélni a nehéz évtizedeket és fenntartani a református iskolákat."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz-04-veghazak.json", story_04)

    story_05 = {
        "id": "story.b1.haromresz.05",
        "title": "Másfél évszázad megosztottságban",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Between 1541 and 1699, Hungary endured 150 years of tripartite division. Despite widespread destruction, the legal unity of the Hungarian crown, culture, and language endured until Buda's liberation in 1686.",
        "characters": [],
        "location": "Buda, Magyarország",
        "grammar": ["temporal-durations"],
        "vocabularyTopics": ["150 éves török kor", "Buda visszafoglalása 1686", "Nemzeti megmaradás"],
        "paragraphs": [
            {"type": "narration", "text": "Magyarország másfél évszázadon keresztül, 1541-től 1699-ig három részre szakadva harcolt a túlélésért."},
            {"type": "narration", "text": "A folyamatos harcok miatt a déli és középső országrészek falvai elnéptelenedtek, virágzó szántóföldek váltak pusztává."},
            {"type": "narration", "text": "A nemzet azonban a tragikus szétszakítottság ellenére sem veszítette el kulturális és jogi egységét."},
            {"type": "narration", "text": "1686-ban az egyesült európai keresztény seregek véres ostromban visszafoglalták Budát a törököktől."},
            {"type": "narration", "text": "Az 1699-es karlócai békével lezárult a hódoltság korszaka, és megkezdődött a szétrombolt ország hatalmas újjáépítése."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz-05-megosztottsag.json", story_05)

    story_combined = {
        "id": "story.b1.haromresz",
        "title": "A három részre szakadt Magyarország (1541–1699)",
        "level": "B1",
        "order": 10,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The dramatic 150-year era of the tripartite partition of Hungary (1541–1699): Royal Hungary under Habsburg rule with Pozsony as capital, the Ottoman Hódoltság centered in Buda, the autonomous Principality of Transylvania championing religious freedom, heroic border fortress defense, cattle trade, and the eventual liberation of Buda in 1686.",
        "characters": [],
        "location": "Pozsony, Buda, Gyulafehérvár, Eger, Bécs",
        "grammar": ["administrative-framing", "ottoman-terminology", "concessive-clauses", "historical-routines", "temporal-durations"],
        "vocabularyTopics": ["Három részre szakadt ország", "Királyi Magyarország", "Török Hódoltság", "Erdélyi Fejedelemség", "Buda visszafoglalása"],
        "paragraphs": [
            {"type": "narration", "text": "Buda 1541-es oszmán elfoglalásával a középkori Magyar Királyság másfél évszázadra három részre szakadt. Északon és nyugaton a Habsburg-kormányzat alatt álló Királyi Magyarország működött, amelynek Pozsony lett az új fővárosa és koronázó székhelye."},
            {"type": "narration", "text": "Az ország középső harmada, az Alföld és a Duna-Tisza köze a Török Hódoltság része lett. A budai pasa által irányított vilajetek lakói kettős adóztatás alatt éltek, miközben Budán és a hódoltsági városokban török fürdők, dzsámik és minaretek épültek."},
            {"type": "narration", "text": "Keleten megalakult az önálló Erdélyi Fejedelemség Gyulafehérvár székhellyel. Noha Erdély adót fizetett a szultánnak, a fejedelmek megőrizték belső önállóságukat, és az 1568-as tordai országgyűlésen a világon elsőként iktatták törvénybe a vallásszabadságot."},
            {"type": "narration", "text": "A határokon több száz kilométeren át húzódott a végvárvonal, ahol Eger, Kanizsa és Szigetvár végvári vitézei hősiesen védték az országot. Az alföldi mezővárosok eközben hatalmas szürkemarha-kereskedelmet folytattak Nyugat-Európával, fenntartva a gazdasági életet."},
            {"type": "narration", "text": "A másfél évszázados megosztottság és pusztulás után 1686-ban az egyesült keresztény hadak felszabadították Budát. Az 1699-es karlócai béke végleg felszámolta az oszmán uralmat, és megkezdődött a sok sebből vérző ország történelmi újjáépítése."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-haromresz.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-haromresz-01",
        "exercises": [
            {
                "id": "b1-haromresz-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Királyi Magyarország", "Royal Hungary"],
                    ["Habsburg-kormányzat", "Habsburg administration"],
                    ["Pozsony", "Pozsony (Bratislava)"],
                    ["kancellária", "chancellery"]
                ]
            },
            {
                "id": "b1-haromresz-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nádor", "palatine (highest kingdom dignitary)"],
                    ["rendi gyűlés", "diet of estates"],
                    ["végvárvonal", "border fortress line"],
                    ["határvédelem", "border defense"]
                ]
            },
            {
                "id": "b1-haromresz-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik város lett a Királyi Magyarország fővárosa és koronázó városa Buda török kézre kerülése után?",
                "options": ["Pozsony", "Kolozsvár", "Debrecen"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik uralkodóház tagjai voltak a Királyi Magyarország királyai a 16. században?",
                "options": ["A Habsburg-ház", "A Jagelló-ház", "Az Anjou-ház"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik ragos szerkezet fejezi ki az adminisztratív központot: „A Királyi Magyarország Pozsony ______ működött.”?",
                "options": ["székhellyel", "székhelyből", "székhelyre"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A király után a legfontosabb világi méltóság a ____ volt, aki az országgyűlést vezette. (palatine)",
                "answer": "nádor"
            },
            {
                "id": "b1-haromresz-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen fő feladat hárult a Királyi Magyarországra a 16–17. században?",
                "options": [
                    "A végvárrendszer fenntartása és Bécs, valamint a keresztény Európa védelme a törökkel szemben.",
                    "Hadsereg küldése Amerikába.",
                    "A Dunai hajózás teljes betiltása."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hol koronázták meg a magyar királyokat a török hódoltság évszázadaiban?",
                "options": [
                    "A pozsonyi Szent Márton-dómban.",
                    "A budavári Mátyás-templomban.",
                    "Az esztergomi bazilikában."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol ülésezett a magyar rendi országgyűlés a török korban?",
                "options": [
                    "Pozsonyban.",
                    "Visegrádon.",
                    "Székesfehérváron."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-haromresz-02",
        "exercises": [
            {
                "id": "b1-haromresz-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Török Hódoltság", "Ottoman-ruled territory"],
                    ["vilajet", "vilayet (province)"],
                    ["budai pasa", "pasha of Buda"],
                    ["defterdár", "defterdar (tax keeper)"]
                ]
            },
            {
                "id": "b1-haromresz-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["dzsámi", "mosque"],
                    ["minaret", "minaret"],
                    ["törökfürdő", "Turkish thermal bath"],
                    ["kettős adóztatás", "double taxation"]
                ]
            },
            {
                "id": "b1-haromresz-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben foglalta el Szulejmán szultán csellel Buda várát?",
                "options": ["1541-ben (augusztus 29-én).", "1526-ban.", "1456-ban."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt a török közigazgatás legfőbb vezetője a Hódoltság területén?",
                "options": ["A budai pasa.", "A pozsonyi nádor.", "Az egri várkapitány."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti a török adóösszeíró tisztviselőt?",
                "options": ["defterdár", "janicsár", "spahi"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A hódoltsági jobbágyok ____ adóztatástól szenvedtek: a szultánnak és a magyar földesúrnak is fizettek. (double)",
                "answer": "kettős"
            },
            {
                "id": "b1-haromresz-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen kulturális és építészeti emlékek maradtak fenn a török hódoltság korából Magyarországon?",
                "options": [
                    "Gyógyfürdők (pl. Rudas, Király), minaretek (Eger, Pécs) és Gül Baba türbéje Budán.",
                    "Gótikus katedrálisok a Dunakanyarban.",
                    "Barokk kastélyok az Alföldön."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan foglalta el Szulejmán szultán Budát 1541-ben?",
                "options": [
                    "Csellel: a janicsárok békés látogatóként sétáltak be a várba, majd megszállták a kapukat harc nélkül.",
                    "Egy éven át tartó véres ostrommal és ágyúzással.",
                    "A magyar rendek önként átadták a kulcsokat."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi az a 'vilajet' az oszmán közigazgatásban?",
                "options": [
                    "A legnagyobb oszmán tartományi közigazgatási egység, élén a pasával.",
                    "Egy kis falu a határ mellett.",
                    "A janicsárok különleges fegyvere."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-haromresz-03",
        "exercises": [
            {
                "id": "b1-haromresz-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Erdélyi Fejedelemség", "Principality of Transylvania"],
                    ["fejedelem", "ruling prince"],
                    ["Gyulafehérvár", "Gyulafehérvár (princely capital)"],
                    ["vallásszabadság", "freedom of religion"]
                ]
            },
            {
                "id": "b1-haromresz-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["adófizetés", "paying tribute (haradzs)"],
                    ["anyanyelvi kultúra", "mother-tongue culture"],
                    ["reformáció", "Reformation"],
                    ["közvetítő szerep", "mediating role"]
                ]
            },
            {
                "id": "b1-haromresz-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik város volt az Erdélyi Fejedelemség székhelye és kulturális központja?",
                "options": ["Gyulafehérvár", "Pozsony", "Buda"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik híres országgyűlésen iktatták törvénybe a vallásszabadságot 1568-ban?",
                "options": ["A tordai országgyűlésen.", "A pozsonyi diétán.", "A rákosi mezőn."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik megengedő kötőszó illik a mondatba: „______ Erdély adót fizetett a töröknek, belső önállóságát megőrizte.”?",
                "options": ["Noha", "Mert", "Mintha"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-03.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az 1568-as tordai ediktum a világon elsőként biztosította a ____ a négy keresztény felekezet számára. (religious freedom)",
                "answer": "vallásszabadságot"
            },
            {
                "id": "b1-haromresz-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért számított Európában egyedülállónak az 1568-as tordai vallásbéke?",
                "options": [
                    "Mert a vallásháborúk korában békésen egyenrangúnak nyilvánította a katolikus, lutheránus, kálvinista és unitárius vallást.",
                    "Mert betiltotta az összes vallást.",
                    "Mert kötelezővé tette az iszlámot."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen szerepet töltött be Erdély a magyar kultúra és nyelv történetében?",
                "options": [
                    "A magyar nyelvű oktatás, könyvnyomtatás és anyanyelvi kultúra bástyája volt a reformáció idején.",
                    "Teljesen feladta a magyar nyelvet a latin javára.",
                    "Nem működtek iskolák és nyomdák Erdélyben."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen külpolitikai helyzetben volt az Erdélyi Fejedelemség?",
                "options": [
                    "Két hatalmas birodalom (a Habsburg és az Oszmán) között egyensúlyozott ügyes diplomáciával.",
                    "Csak Oroszországgal tartott kapcsolatot.",
                    "Teljesen el volt vágva a külvilágtól."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-haromresz-04",
        "exercises": [
            {
                "id": "b1-haromresz-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["végvári vitéz", "border fortress warrior"],
                    ["bajvívás", "single combat / duel"],
                    ["portya", "cavalry raid"],
                    ["mezőváros", "market town"]
                ]
            },
            {
                "id": "b1-haromresz-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["marhakereskedelem", "cattle trade"],
                    ["elnéptelenedés", "depopulation"],
                    ["paraszti ellenállás", "peasant resilience"],
                    ["együttélés", "coexistence"]
                ]
            },
            {
                "id": "b1-haromresz-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mely híres magyar végvárak védték az országot az oszmán hadakkal szemben?",
                "options": ["Eger, Szigetvár, Győr, Kanizsa", "Bécs, Prága, Pozsony", "Szeged, Debrecen, Kecskemét"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen árucikkel folytattak hatalmas volumenű kereskedelmet a magyar mezővárosok Nyugat-Európa felé?",
                "options": ["Magyar szürkemarhával.", "Selyemmel és fűszerekkel.", "Kőszénnel és vassal."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés utal a múltbeli szokásos cselekvésre: „A két sereg bajnokai között ______ volt a bajvívás.”?",
                "options": ["szokás", "ritka", "lehetetlen"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A végvári vitézek rendszeresen ____ indultak az ellenséges portyázók feltartóztatására. (on a raid)",
                "answer": "portyára"
            },
            {
                "id": "b1-haromresz-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan tudtak az alföldi mezővárosok (pl. Kecskemét, Nagykőrös, Cegléd) túlélni a Hódoltságban?",
                "options": [
                    "Közvetlenül a szultánnak fizettek adót (khász városok voltak), így nagyobb önrendelkezést élveztek.",
                    "Fegyverrel elűzték az összes törököt a határról.",
                    "Feladták a keresztény vallást."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen életforma jellemezte a végvári katonaságot a 16–17. században?",
                "options": [
                    "Állandó készültség, önfeláldozó hazaszeretet, a zsold hiánya miatt portyázás és a bajtársi szolidaritás.",
                    "Kényelmes udvari élet zsoldoshadsereg nélkül.",
                    "Kizárólag békés mezőgazdasági munka a váron belül."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hová hajtották a tőzsérek a magyar szürkemarhákat?",
                "options": [
                    "Bécs, Nürnberg, Velence és más nagy nyugat-európai városok piacaira.",
                    "Csak a szomszédos falvakba.",
                    "Konstantinápolyba a szultánnak."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-haromresz-05",
        "exercises": [
            {
                "id": "b1-haromresz-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["megosztottság", "division / partition"],
                    ["másfél évszázad", "century and a half (150 yrs)"],
                    ["nemzeti egység", "national unity"],
                    ["túlélés", "survival"]
                ]
            },
            {
                "id": "b1-haromresz-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rombolás", "destruction / devastation"],
                    ["folytonosság", "continuity of statehood"],
                    ["visszafoglalás", "reconquest / liberation"],
                    ["újjáépítés", "rebuilding / reconstruction"]
                ]
            },
            {
                "id": "b1-haromresz-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben foglalták vissza a keresztény szövetséges hadak Buda várát a töröktől?",
                "options": ["1686-ban.", "1541-ben.", "1699-ben."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik békeszerződés zárta le hivatalosan a magyarországi oszmán hódoltságot 1699-ben?",
                "options": ["A karlócai béke.", "A pozsonyi béke.", "A tordai ediktum."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik névutó fejezi ki a tartósságot: „Magyarország másfél évszázadon ______ három részre szakadva élt.”?",
                "options": ["keresztül", "ellenére", "helyett"],
                "correct": 0
            },
            {
                "id": "b1-haromresz-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A karlócai béke után megkezdődött a súlyosan elnéptelenedett ország ____. (reconstruction / rebuilding)",
                "answer": "újjáépítése"
            },
            {
                "id": "b1-haromresz-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Körülbelül hány évig tartott a török hódoltság korszaka Magyarországon (1541–1686/1699)?",
                "options": [
                    "Körülbelül másfél évszázadig (150 évig).",
                    "Mindössze tíz évig.",
                    "Háromszáz évig."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen demográfiai következményekkel járt a 150 éves török háborúskodás az Alföldön és a déli végeken?",
                "options": [
                    "Súlyos népességfogyással, falvak százainak elpusztulásával és az etnikai arányok megváltozásával a későbbi betelepítések miatt.",
                    "A lakosság megháromszorozódásával.",
                    "Semmilyen hatással nem volt a népességre."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan maradhatott fenn a magyar nemzeti egység a három országrészben a megosztottság idején?",
                "options": [
                    "A közös magyar nyelv, a protestáns és katolikus anyanyelvi iskolák, a Szent Korona-eszme és a közös joghagyomány révén.",
                    "Egyetlen közös közigazgatási hivatal működésével Budán.",
                    "Mert a török szultán kötelezővé tette a magyar nyelvet."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-haromresz-consolidation",
        "exercises": [
            {
                "id": "b1-haromresz-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Királyi Magyarország", "Royal Hungary"],
                    ["Török Hódoltság", "Ottoman occupation territory"],
                    ["Erdélyi Fejedelemség", "Principality of Transylvania"],
                    ["Pozsony", "Pozsony (coronation capital)"]
                ]
            },
            {
                "id": "b1-haromresz-consolidation.ex02",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["budai pasa", "pasha of Buda"],
                    ["vilajet", "vilayet (Ottoman province)"],
                    ["Gyulafehérvár", "princely seat of Transylvania"],
                    ["nádor", "palatine"]
                ]
            },
            {
                "id": "b1-haromresz-consolidation.ex03",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vallásszabadság", "religious freedom"],
                    ["végvári vitéz", "border warrior"],
                    ["mezőváros", "market town"],
                    ["marhakereskedelem", "cattle trade"]
                ]
            },
            {
                "id": "b1-haromresz-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["másfél évszázad", "150 years (century and a half)"],
                    ["kettős adóztatás", "double taxation"],
                    ["visszafoglalás", "reconquest"],
                    ["újjáépítés", "rebuilding"]
                ]
            },
            {
                "id": "b1-haromresz-consolidation.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mely három részre szakadt a középkori Magyarország 1541 után?",
                "options": [
                    "Királyi Magyarországra, Török Hódoltságra és Erdélyi Fejedelemségre.",
                    "Ausztriára, Poroszországra és Lengyelországra.",
                    "Dunántúlra, Alföldre és Felvidékre külön királyokkal."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben esett el Buda, megpecsételve az ország három részre szakadását?",
                "options": ["1541-ben.", "1526-ban.", "1490-ben.", "1686-ban."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik városban működött az Erdélyi Fejedelemség székhelye?",
                "options": ["Gyulafehérváron.", "Pozsonyban.", "Budán.", "Egerben."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben foglalták vissza Budát a szövetséges keresztény seregek?",
                "options": ["1686-ban.", "1541-ben.", "1526-ban.", "1703-ban."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex09",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a diplomáciai ellentétet?",
                "options": [
                    "Bár Erdély adót fizetett a szultánnak, belső önállóságát sikerrel megőrizte.",
                    "Bár Erdély adót fizetett a szultánnak, mert belső önállóságát nem őrizte.",
                    "Bár Erdély adót fizetett a szultánnak általában önálló volt."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex10",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az 1568-as tordai országgyűlésen a világon elsőként mondták ki a ____. (religious freedom)",
                "answer": "vallásszabadságot"
            },
            {
                "id": "b1-haromresz-consolidation.ex11",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A török hódoltság ideje alatt Pozsony volt a Királyi Magyarország koronázó ____. (city / capital)",
                "answer": "városa"
            },
            {
                "id": "b1-haromresz-consolidation.ex12",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A hódoltsági parasztok ____ adóztatástól szenvedtek a két hatalom felé. (double)",
                "answer": "kettős"
            },
            {
                "id": "b1-haromresz-consolidation.ex13",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A török uralom ____ évszázadon keresztül nehezedett Magyarországra. (century and a half)",
                "answer": "másfél"
            },
            {
                "id": "b1-haromresz-consolidation.ex14",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen békével zárult le végleg a török hódoltság korszaka 1699-ben?",
                "options": ["A karlócai békével.", "A pozsonyi békével.", "A bécsi békével.", "A tordai ediktummal."],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex15",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelentett a 'kettős adóztatás' a török hódoltságban élők számára?",
                "options": [
                    "A magyar jobbágyok a török hatóságoknak és az elmenekült magyar nemeseknek is adóztak.",
                    "Két különböző pénznemben fizették a béreket.",
                    "Csak az egyháznak és a királynak fizettek adót.",
                    "Egyáltalán nem kellett adót fizetniük."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex16",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik állítás igaz az Erdélyi Fejedelemség kultúrájára a 16–17. században?",
                "options": [
                    "A magyar nyelvű reformáció, a bibliafordítások és az anyanyelvi iskolák kiemelkedő központja volt.",
                    "Teljesen átvette az oszmán nyelvet és szokásokat.",
                    "Minden iskolát és nyomdát bezártak a fejedelmek.",
                    "Kizárólag görög nyelven folyt az oktatás."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex17",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Kik voltak a végvári vitézek?",
                "options": [
                    "A határvédő magyar erődökben szolgáló harcosok, akik nap mint nap küzdöttek az oszmán betörések ellen.",
                    "Kizárólag külföldi osztrák zsoldosok.",
                    "A földeken dolgozó jobbágyok.",
                    "A budai pasa testőrei."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex18",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen gazdasági ágazat virágzott a hódoltsági mezővárosokban a háborús idők ellenére?",
                "options": [
                    "A szürkemarha-kereskedelem és állattenyésztés Nyugat-Európa felé.",
                    "A gépgyártás és vasútépítés.",
                    "A selyemhernyó-tenyésztés.",
                    "A tengeri halászat."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex19",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen építészeti hagyatékot hagyott hátra az oszmán hódoltság Budapesten és más magyar városokban?",
                "options": [
                    "Gyógyfürdőket (pl. Rudas, Király), minareteket és sírkápolnákat (Gül Baba türbéje).",
                    "Csak kőhidakat.",
                    "Gótikus harangtornyokat.",
                    "Barokk színházakat."
                ],
                "correct": 0
            },
            {
                "id": "b1-haromresz-consolidation.ex20",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért tekint a magyar történettudomány büszkeséggel a 150 éves hódoltság korára a borzalmas pusztítás ellenére?",
                "options": [
                    "Mert a nemzet a kettős birodalmi nyomás és a feldaraboltság ellenére is megőrizte nyelvét, kultúráját és államiságának folytonosságát.",
                    "Mert Magyarország ekkor gyarmatosította a szomszédos országokat.",
                    "Mert ekkor vezették be a modern alkotmányt.",
                    "Mert a harcok azonnali békét eredményeztek."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-haromresz-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.haromresz-01",
        "title": "Királyi Magyarország (Royal Hungary)",
        "level": "B1",
        "grammar": "Administrative Framing: Pozsony székhellyel, központként",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the governance of Royal Hungary under the Habsburg monarchs.",
                    "I can explain why Pozsony (Bratislava) became the coronation capital and diet seat.",
                    "I can use administrative sociative and essive expressions (székhellyel, központként).",
                    "I can master eight new vocabulary items related to early modern kingdom administration."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-haromresz-01-kiralyi.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-haromresz-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-haromresz-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-haromresz-01-ex.json", "exerciseRefs": [
                "b1-haromresz-01.ex01", "b1-haromresz-01.ex01b", "b1-haromresz-01.ex02", "b1-haromresz-01.ex03",
                "b1-haromresz-01.ex04", "b1-haromresz-01.ex05", "b1-haromresz-01.ex06", "b1-haromresz-01.ex07", "b1-haromresz-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the governance of Royal Hungary under the Habsburg monarchs.",
                    "I can explain why Pozsony (Bratislava) became the coronation capital and diet seat.",
                    "I can use administrative sociative and essive expressions (székhellyel, központként).",
                    "I can master eight new vocabulary items related to early modern kingdom administration."
                ]
            }
        ],
        "goal": [
            "I can describe the governance of Royal Hungary under the Habsburg monarchs.",
            "I can explain why Pozsony (Bratislava) became the coronation capital and diet seat.",
            "I can use administrative sociative and essive expressions (székhellyel, központként).",
            "I can master eight new vocabulary items related to early modern kingdom administration."
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.haromresz-02",
        "title": "A török hódoltság (The Ottoman Occupation)",
        "level": "B1",
        "grammar": "Ottoman Loanwords & Administrative Terminology: vilajet, pasa, kettős adóztatás",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can narrate the fall of Buda Castle on August 29, 1541.",
                    "I can describe the Ottoman administrative system (vilajets, pasas, defterdars) in central Hungary.",
                    "I can explain double taxation (kettős adóztatás) experienced by Hungarian peasants.",
                    "I can use eight new vocabulary items related to Ottoman-era Hungary and architecture."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-haromresz-02-hodoltsag.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-haromresz-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-haromresz-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-haromresz-02-ex.json", "exerciseRefs": [
                "b1-haromresz-02.ex01", "b1-haromresz-02.ex01b", "b1-haromresz-02.ex02", "b1-haromresz-02.ex03",
                "b1-haromresz-02.ex04", "b1-haromresz-02.ex05", "b1-haromresz-02.ex06", "b1-haromresz-02.ex07", "b1-haromresz-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the fall of Buda Castle on August 29, 1541.",
                    "I can describe the Ottoman administrative system (vilajets, pasas, defterdars) in central Hungary.",
                    "I can explain double taxation (kettős adóztatás) experienced by Hungarian peasants.",
                    "I can use eight new vocabulary items related to Ottoman-era Hungary and architecture."
                ]
            }
        ],
        "goal": [
            "I can narrate the fall of Buda Castle on August 29, 1541.",
            "I can describe the Ottoman administrative system (vilajets, pasas, defterdars) in central Hungary.",
            "I can explain double taxation (kettős adóztatás) experienced by Hungarian peasants.",
            "I can use eight new vocabulary items related to Ottoman-era Hungary and architecture."
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.haromresz-03",
        "title": "Az Erdélyi Fejedelemség (The Principality of Transylvania)",
        "level": "B1",
        "grammar": "Concessive Clauses & Diplomatic Balancing: noha, bár, jóllehet",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can outline the founding and autonomy of the Principality of Transylvania.",
                    "I can explain the European significance of the 1568 Diet of Torda and religious tolerance.",
                    "I can construct diplomatic balancing arguments using noha, bár, and jóllehet.",
                    "I can deploy eight new vocabulary items concerning Transylvanian statehood and culture."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-haromresz-03-erdely.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-haromresz-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-haromresz-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-haromresz-03-ex.json", "exerciseRefs": [
                "b1-haromresz-03.ex01", "b1-haromresz-03.ex01b", "b1-haromresz-03.ex02", "b1-haromresz-03.ex03",
                "b1-haromresz-03.ex04", "b1-haromresz-03.ex05", "b1-haromresz-03.ex06", "b1-haromresz-03.ex07", "b1-haromresz-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can outline the founding and autonomy of the Principality of Transylvania.",
                    "I can explain the European significance of the 1568 Diet of Torda and religious tolerance.",
                    "I can construct diplomatic balancing arguments using noha, bár, and jóllehet.",
                    "I can deploy eight new vocabulary items concerning Transylvanian statehood and culture."
                ]
            }
        ],
        "goal": [
            "I can outline the founding and autonomy of the Principality of Transylvania.",
            "I can explain the European significance of the 1568 Diet of Torda and religious tolerance.",
            "I can construct diplomatic balancing arguments using noha, bár, and jóllehet.",
            "I can deploy eight new vocabulary items concerning Transylvanian statehood and culture."
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.haromresz-04",
        "title": "Élet három határon (Life Across Three Borders)",
        "level": "B1",
        "grammar": "Habitual Historical Routines: rendszeresen, gyakran, szokás volt",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the daily life, skirmishes (portya), and single combat (bajvívás) of border warriors.",
                    "I can explain how market towns (mezővárosok) thrived through the western cattle trade.",
                    "I can describe historical customs using habitual expressions like szokás volt.",
                    "I can use eight new vocabulary items concerning border fortresses and trade routes."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-haromresz-04-veghazak.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-haromresz-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-haromresz-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-haromresz-04-ex.json", "exerciseRefs": [
                "b1-haromresz-04.ex01", "b1-haromresz-04.ex01b", "b1-haromresz-04.ex02", "b1-haromresz-04.ex03",
                "b1-haromresz-04.ex04", "b1-haromresz-04.ex05", "b1-haromresz-04.ex06", "b1-haromresz-04.ex07", "b1-haromresz-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the daily life, skirmishes (portya), and single combat (bajvívás) of border warriors.",
                    "I can explain how market towns (mezővárosok) thrived through the western cattle trade.",
                    "I can describe historical customs using habitual expressions like szokás volt.",
                    "I can use eight new vocabulary items concerning border fortresses and trade routes."
                ]
            }
        ],
        "goal": [
            "I can describe the daily life, skirmishes (portya), and single combat (bajvívás) of border warriors.",
            "I can explain how market towns (mezővárosok) thrived through the western cattle trade.",
            "I can describe historical customs using habitual expressions like szokás volt.",
            "I can use eight new vocabulary items concerning border fortresses and trade routes."
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.haromresz-05",
        "title": "Egy megosztott évszázad (A Divided Century and a Half)",
        "level": "B1",
        "grammar": "Long-Duration Historical Expressions: másfél évszázadon át, évtizedekig",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can summarize the 150-year era of Hungarian partition from 1541 to 1699.",
                    "I can explain the liberation of Buda in 1686 and the 1699 Peace of Karlowitz.",
                    "I can discuss how Hungarian national identity, law, and culture survived this period.",
                    "I can answer all citizenship exam questions on the tripartite division with total precision."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-haromresz-05-megosztottsag.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-haromresz-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-haromresz-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-haromresz-05-ex.json", "exerciseRefs": [
                "b1-haromresz-05.ex01", "b1-haromresz-05.ex01b", "b1-haromresz-05.ex02", "b1-haromresz-05.ex03",
                "b1-haromresz-05.ex04", "b1-haromresz-05.ex05", "b1-haromresz-05.ex06", "b1-haromresz-05.ex07", "b1-haromresz-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can summarize the 150-year era of Hungarian partition from 1541 to 1699.",
                    "I can explain the liberation of Buda in 1686 and the 1699 Peace of Karlowitz.",
                    "I can discuss how Hungarian national identity, law, and culture survived this period.",
                    "I can answer all citizenship exam questions on the tripartite division with total precision."
                ]
            }
        ],
        "goal": [
            "I can summarize the 150-year era of Hungarian partition from 1541 to 1699.",
            "I can explain the liberation of Buda in 1686 and the 1699 Peace of Karlowitz.",
            "I can discuss how Hungarian national identity, law, and culture survived this period.",
            "I can answer all citizenship exam questions on the tripartite division with total precision."
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.haromresz-consolidation",
        "title": "Unit 10 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can explain the tripartite division of Hungary: Royal Hungary, Ottoman Hódoltság, and Transylvania.",
                    "I can describe Buda's capture in 1541, the 1568 Diet of Torda, and Buda's reconquest in 1686.",
                    "I can discuss the border fortress system, single combat, double taxation, and cattle trade.",
                    "I can confidently pass Hungarian citizenship interview questions on the 150-year Ottoman era."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-haromresz-consolidation-ex.json", "exerciseRefs": [
                "b1-haromresz-consolidation.ex01", "b1-haromresz-consolidation.ex02", "b1-haromresz-consolidation.ex03", "b1-haromresz-consolidation.ex04",
                "b1-haromresz-consolidation.ex05", "b1-haromresz-consolidation.ex06", "b1-haromresz-consolidation.ex07", "b1-haromresz-consolidation.ex08",
                "b1-haromresz-consolidation.ex09", "b1-haromresz-consolidation.ex10", "b1-haromresz-consolidation.ex11", "b1-haromresz-consolidation.ex12",
                "b1-haromresz-consolidation.ex13", "b1-haromresz-consolidation.ex14", "b1-haromresz-consolidation.ex15", "b1-haromresz-consolidation.ex16",
                "b1-haromresz-consolidation.ex17", "b1-haromresz-consolidation.ex18", "b1-haromresz-consolidation.ex19", "b1-haromresz-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can explain the tripartite division of Hungary: Royal Hungary, Ottoman Hódoltság, and Transylvania.",
                    "I can describe Buda's capture in 1541, the 1568 Diet of Torda, and Buda's reconquest in 1686.",
                    "I can discuss the border fortress system, single combat, double taxation, and cattle trade.",
                    "I can confidently pass Hungarian citizenship interview questions on the 150-year Ottoman era."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-haromresz-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_10_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 10 (b1-haromresz)!")
