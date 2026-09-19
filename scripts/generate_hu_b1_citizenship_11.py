#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 11: Transylvania's Golden Age (b1-erdelyaranykora)."""

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

def build_unit_11_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.erdelyaranykora.01",
        "lesson": "b1-erdelyaranykora-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fejedelemség", "translation": "principality", "pos": "noun"},
            {"lemma": "hűbérúr", "translation": "suzerain, feudal overlord", "pos": "noun"},
            {"lemma": "belső önállóság", "translation": "internal autonomy, self-government", "pos": "noun"},
            {"lemma": "fejedelmi székhely", "translation": "princely seat, capital (Gyulafehérvár)", "pos": "noun"},
            {"lemma": "rendi országgyűlés", "translation": "diet of the three estates", "pos": "noun"},
            {"lemma": "kiváltság", "translation": "privilege, constitutional right", "pos": "noun"},
            {"lemma": "külpolitika", "translation": "foreign policy", "pos": "noun"},
            {"lemma": "békés építkezés", "translation": "peaceful state-building", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-erdelyaranykora-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.erdelyaranykora.02",
        "lesson": "b1-erdelyaranykora-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vallásszabadság", "translation": "freedom of religion", "pos": "noun"},
            {"lemma": "tordai ediktum", "translation": "1568 Edict of Torda (religious patent)", "pos": "noun"},
            {"lemma": "bevett vallás", "translation": "officially recognized denomination", "pos": "noun"},
            {"lemma": "katolikus", "translation": "Roman Catholic", "pos": "adjective"},
            {"lemma": "lutheránus", "translation": "Lutheran (Evangelical)", "pos": "adjective"},
            {"lemma": "református", "translation": "Calvinist (Reformed)", "pos": "adjective"},
            {"lemma": "unitárius", "translation": "Unitarian", "pos": "adjective"},
            {"lemma": "felekezeti béke", "translation": "denominational / inter-faith peace", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-erdelyaranykora-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.erdelyaranykora.03",
        "lesson": "b1-erdelyaranykora-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Bethlen Gábor", "translation": "Gábor Bethlen (Prince of Transylvania 1613–1629)", "pos": "noun"},
            {"lemma": "aranykor", "translation": "golden age, heyday", "pos": "noun"},
            {"lemma": "merkantilizmus", "translation": "mercantilism, state trade monopolies", "pos": "noun"},
            {"lemma": "bányászat", "translation": "mining (precious metals, salt)", "pos": "noun"},
            {"lemma": "nemesfém-kivitel", "translation": "precious metal export", "pos": "noun"},
            {"lemma": "fejedelmi kollégium", "translation": "princely college / academy", "pos": "noun"},
            {"lemma": "mecénás", "translation": "patron of the arts, benefactor", "pos": "noun"},
            {"lemma": "gazdasági fellendülés", "translation": "economic upswing / boom", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-erdelyaranykora-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.erdelyaranykora.04",
        "lesson": "b1-erdelyaranykora-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "harmincéves háború", "translation": "Thirty Years' War (1618–1648)", "pos": "noun"},
            {"lemma": "szövetséges", "translation": "ally", "pos": "noun"},
            {"lemma": "protestáns liga", "translation": "Protestant league", "pos": "noun"},
            {"lemma": "hadjárat", "translation": "military campaign", "pos": "noun"},
            {"lemma": "békeszerződés", "translation": "peace treaty (1621 Peace of Nikolsburg)", "pos": "noun"},
            {"lemma": "diplomácia", "translation": "diplomacy", "pos": "noun"},
            {"lemma": "egyensúlyozás", "translation": "balancing act between superpowers", "pos": "noun"},
            {"lemma": "nemzetközi elismertség", "translation": "international recognition", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-erdelyaranykora-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.erdelyaranykora.05",
        "lesson": "b1-erdelyaranykora-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "műveltség", "translation": "culture, erudition, learning", "pos": "noun"},
            {"lemma": "bibliafordítás", "translation": "Bible translation (Károli Gáspár Vizsoly Bible)", "pos": "noun"},
            {"lemma": "nyomdászat", "translation": "book printing", "pos": "noun"},
            {"lemma": "anyanyelvi oktatás", "translation": "mother-tongue education", "pos": "noun"},
            {"lemma": "zsoltáréneklés", "translation": "psalm singing (Szenczi Molnár Albert)", "pos": "noun"},
            {"lemma": "történelmi hagyaték", "translation": "historical heritage / legacy", "pos": "noun"},
            {"lemma": "nemzeti tudat", "translation": "national consciousness", "pos": "noun"},
            {"lemma": "bástya", "translation": "bastion, stronghold, bulwark", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-erdelyaranykora-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.erdelyaranykora.01.essive-formal-kent",
        "title": "The Essive-Formal Suffix: -ként (Acting as, In the Role of)",
        "sections": [
            {
                "type": "text",
                "title": "Designating Status, Function, and Character in History",
                "content": "The essive-formal suffix *-ként* expresses the capacity or role in which someone or something acts ('as a...'): *fejedelemként* (as a prince), *székhelyként* (as a capital/seat), *önálló államként* (as an independent state), *védelmezőként* (as a protector)."
            },
            {
                "type": "examples",
                "title": "The -ként suffix examples",
                "items": [
                    {
                        "spanish": "Erdély önálló fejedelemségként működött több mint egy évszázadon át.",
                        "english": "Transylvania operated as an independent principality for more than a century."
                    },
                    {
                        "spanish": "Gyulafehérvár a fejedelmek székhelyeként a magyar reneszánsz és reformáció központja lett.",
                        "english": "As the seat of the princes, Gyulafehérvár became the center of Hungarian Renaissance and Reformation."
                    },
                    {
                        "spanish": "A fejedelem a nemzet védelmezőjeként lépett fel a Habsburg központosítással szemben.",
                        "english": "The prince stepped forward as the protector of the nation against Habsburg centralization."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-erdelyaranykora-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.erdelyaranykora.02.statutory-decrees",
        "title": "Reporting Historic Laws & Religious Decrees: törvénybe iktat, kimondja, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Legal and Declarative Framing in Historical Hungarian",
                "content": "To narrate the enactment of landmark civil statutes, Hungarian uses verbal expressions like *törvénybe iktat* ('enact into law'), *kinyilvánít* ('proclaim'), and *kimondja, hogy...* ('decrees/declares that...')."
            },
            {
                "type": "examples",
                "title": "Statutory decree examples",
                "items": [
                    {
                        "spanish": "Az 1568-as tordai országgyűlés a világon elsőként iktatta törvénybe a vallásszabadságot.",
                        "english": "The 1568 Diet of Torda was the first in the world to enact religious freedom into law."
                    },
                    {
                        "spanish": "A híres törvény kimondta, hogy a hitért senkit sem szabad bántalmazni vagy fogságba vetni.",
                        "english": "The famous law declared that no one may be harmed or imprisoned for their faith."
                    },
                    {
                        "spanish": "Négy felekezetet ismertek el egyenrangú bevett vallásként: a katolikus, lutheránus, református és unitárius egyházat.",
                        "english": "Four denominations were recognized as equal recognized religions: the Catholic, Lutheran, Reformed, and Unitarian churches."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-erdelyaranykora-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.erdelyaranykora.03.economic-boom",
        "title": "Narrating Economic Flourishing: virágzásnak indult, fellendült",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Economic and Cultural Upswing in B1 Hungarian",
                "content": "To describe golden ages and prosperity, Hungarian uses inchoative and perfective verbal expressions: *virágzásnak indult* (began to flourish), *fellendült a kereskedelem* (trade boomed/surged), and *megteremtette az alapjait* (laid the foundations of)."
            },
            {
                "type": "examples",
                "title": "Economic boom examples",
                "items": [
                    {
                        "spanish": "Bethlen Gábor uralkodása alatt Erdély gazdasága és kultúrája páratlan virágzásnak indult.",
                        "english": "Under the reign of Gábor Bethlen, Transylvania's economy and culture began an unprecedented flourishing."
                    },
                    {
                        "spanish": "A fejedelmi merkantilista politika révén fellendült a bányászat és a külkereskedelem.",
                        "english": "Through princely mercantilist policies, mining and foreign trade surged."
                    },
                    {
                        "spanish": "A fejedelem nagylelkű mecénásként külföldi tudósokat és építészeket hívott az udvarába.",
                        "english": "As a generous patron, the prince invited foreign scholars and architects to his court."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-erdelyaranykora-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.erdelyaranykora.04.diplomatic-intentions",
        "title": "Diplomatic Intentions & Alliances: annak érdekében, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Expressing High-Level Political and Strategic Aims",
                "content": "Formal diplomacy and military alliances utilize the complex purpose conjunction *annak érdekében, hogy...* ('in order that... / with the aim of...') followed by the subjunctive mood (*-jon / -jen*)."
            },
            {
                "type": "examples",
                "title": "Diplomatic intent examples",
                "items": [
                    {
                        "spanish": "Bethlen Gábor hadjáratokat indított annak érdekében, hogy megvédje a magyar rendi jogokat és a vallásszabadságot.",
                        "english": "Gábor Bethlen launched campaigns in order to defend Hungarian constitutional rights and religious freedom."
                    },
                    {
                        "spanish": "Erdély bekapcsolódott a harmincéves háborúba a protestáns hatalmak szövetségeseként.",
                        "english": "Transylvania entered the Thirty Years' War as an ally of the Protestant powers."
                    },
                    {
                        "spanish": "Az 1621-es nikolsburgi béke nemzetközi elismertséget és hét felső-magyarországi vármegyét biztosított a fejedelemnek.",
                        "english": "The 1621 Peace of Nikolsburg secured international recognition and seven Upper Hungarian counties for the prince."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-erdelyaranykora-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.erdelyaranykora.05.metaphorical-stronghold",
        "title": "Metaphorical Roles in National Identity: a kultúra bástyája, menedékként",
        "sections": [
            {
                "type": "text",
                "title": "Describing Cultural Sanctuaries and Historic Bulwarks",
                "content": "Hungarian cultural memory characterizes Transylvania through symbolic metaphors: *a magyar kultúra és nyelv bástyája* (the bulwark of Hungarian culture and language), *menedékként szolgált* (served as a haven/refuge), and *őrizte a folytonosságot* (preserved continuity)."
            },
            {
                "type": "examples",
                "title": "Cultural bulwark examples",
                "items": [
                    {
                        "spanish": "A három részre szakadt ország legnehezebb évszázadában Erdély a magyar nyelv és műveltség igazi bástyájaként szolgált.",
                        "english": "In the most difficult century of the partitioned country, Transylvania served as a true bastion of Hungarian language and culture."
                    },
                    {
                        "spanish": "A vizsolyi biblia kinyomtatása és a debreceni meg gyulafehérvári kollégiumok megalapítása biztosította a nemzeti megmaradást.",
                        "english": "The printing of the Vizsoly Bible and the founding of colleges in Debrecen and Gyulafehérvár ensured national survival."
                    },
                    {
                        "spanish": "Az erdélyi aranykor öröksége mindmáig a nemzeti büszkeség és az európai nyitottság szimbóluma.",
                        "english": "The legacy of Transylvania's Golden Age remains a symbol of national pride and European openness to this day."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-erdelyaranykora-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.erdelyaranykora.01",
        "title": "A fejedelemség megszületése",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Following Buda's fall in 1541, Queen Isabella and her infant son John Sigismund established the autonomous Principality of Transylvania in Gyulafehérvár, paying tribute to the sultan while maintaining internal Hungarian statehood.",
        "characters": [],
        "location": "Gyulafehérvár, Erdély",
        "grammar": ["essive-formal-kent"],
        "vocabularyTopics": ["Erdélyi Fejedelemség", "Belső önállóság", "Gyulafehérvári székhely"],
        "paragraphs": [
            {"type": "narration", "text": "Buda 1541-es eleste után Fráter György és Izabella királyné a keleti országrészbe vonult vissza a csecsemő János Zsigmonddal."},
            {"type": "narration", "text": "A Kárpátok védelmében kialakult az Erdélyi Fejedelemség, amely a szultán hűbéreseként, de belső ügyeiben önállóan létezett."},
            {"type": "narration", "text": "A fejedelmi székhely a gyönyörű fekvésű Gyulafehérvár lett, ahol a magyar, székely és szász rendek közösen tanácskoztak."},
            {"type": "narration", "text": "Az új állam feladata az volt, hogy a Habsburg és az Oszmán Birodalom között lavírozva megőrizze a magyar államiság folytonosságát."},
            {"type": "narration", "text": "Az erdélyi fejedelmek határozott külpolitikájukkal békés éveket és gazdasági stabilitást teremtettek a határokon belül."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora-01-onallo.json", story_01)

    story_02 = {
        "id": "story.b1.erdelyaranykora.02",
        "title": "A tordai vallásbéke (1568)",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "At the 1568 Diet of Torda, Transylvania enacted Europe's first law on universal religious tolerance, granting equal legal protection to Catholic, Lutheran, Reformed, and Unitarian believers amid bloody religious wars across the continent.",
        "characters": [],
        "location": "Torda, Kolozsvár",
        "grammar": ["statutory-decrees"],
        "vocabularyTopics": ["Tordai ediktum 1568", "Vallásszabadság", "Bevett vallások"],
        "paragraphs": [
            {"type": "narration", "text": "A 16. században Európát véres vallásháborúk szaggatták szét a reformáció és az ellenreformáció összecsapásai miatt."},
            {"type": "narration", "text": "Ezzel éles ellentétben Erdélyben 1568 januárjában, a tordai katolikus templomban rendkívüli országgyűlés ült össze."},
            {"type": "narration", "text": "János Zsigmond fejedelem és Dávid Ferenc prédikátor javaslatára a rendek kinyilvánították: 'a hit Isten ajándéka'."},
            {"type": "narration", "text": "A tordai ediktum a világon legelőször garantálta négy keresztény felekezet (katolikus, evangélikus, református, unitárius) szabad vallásgyakorlatát."},
            {"type": "narration", "text": "Ez a páratlan bölcsesség és türelem évszázadokra megmentette Erdélyt a belső felekezeti háborúk pusztításától."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora-02-vallasbeke.json", story_02)

    story_03 = {
        "id": "story.b1.erdelyaranykora.03",
        "title": "Bethlen Gábor és a gazdasági felvirágzás",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Prince Gábor Bethlen (1613–1629) ushered in Transylvania's Golden Age through state monopolies on salt and mining, attracting skilled foreign craftsmen and founding the illustrious princely academy in Gyulafehérvár.",
        "characters": [],
        "location": "Gyulafehérvár, Kolozsvár, Nagyszeben",
        "grammar": ["economic-boom"],
        "vocabularyTopics": ["Bethlen Gábor", "Erdély aranykora", "Gazdasági reformok", "Akadémia"],
        "paragraphs": [
            {"type": "narration", "text": "1613-ban a tehetséges diplomata és kiváló hadvezér, Bethlen Gábor lépett az Erdélyi Fejedelemség trónjára."},
            {"type": "narration", "text": "Uralkodása alatt Erdély gazdasága páratlan virágzásnak indult: a fejedelem modern merkantilista gazdaságpolitikát vezetett be."},
            {"type": "narration", "text": "Állami monopóliummá tette a nemesfémek, a marha és a só kivitelét, és felvidéki német bányászokat telepített be a termelés növelésére."},
            {"type": "narration", "text": "Gyulafehérváron hatalmas fejedelmi palotát építtetett és híres protestáns akadémiát alapított európai hírű professzorokkal."},
            {"type": "narration", "text": "Bethlen kincstára megtelt arannyal, így erős zsoldoshadsereget tudott fenntartani és bőkezű mecénásként támogatta a tehetséges diákokat."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora-03-bethlen.json", story_03)

    story_04 = {
        "id": "story.b1.erdelyaranykora.04",
        "title": "Erdély a harmincéves háborúban",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "During the Thirty Years' War, Bethlen Gábor allied with Protestant European powers against the Habsburg Emperor, capturing Upper Hungary and securing constitutional freedoms in the 1621 Peace of Nikolsburg.",
        "characters": [],
        "location": "Pozsony, Bécs, Kassa, Nikolsburg",
        "grammar": ["diplomatic-intentions"],
        "vocabularyTopics": ["Harmincéves háború", "Nikolsburgi béke 1621", "Európai diplomácia"],
        "paragraphs": [
            {"type": "narration", "text": "Amikor 1618-ban kitört a harmincéves háború, Bethlen Gábor felismerte a történelmi lehetőséget a magyar nemzeti jogok védelmére."},
            {"type": "narration", "text": "A fejedelem a cseh és protestáns szövetségesek oldalán hadjáratot indított a Habsburgok ellen, és csapataival még Bécset is ostrom alá vette."},
            {"type": "narration", "text": "1620-ban a besztercebányai országgyűlésen a rendek magyar királlyá választották Bethlent, de ő nem koronáztatta meg magát a Szent Koronával."},
            {"type": "narration", "text": "Az 1621-es nikolsburgi békében megerősítette a Királyi Magyarország rendi jogait, és Erdélyhez csatolt hét felső-magyarországi vármegyét."},
            {"type": "narration", "text": "Sikerei révén az Erdélyi Fejedelemség Európa-szerte elismert tényezővé vált a nemzetközi diplomáciában."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora-04-europa.json", story_04)

    story_05 = {
        "id": "story.b1.erdelyaranykora.05",
        "title": "A magyar nyelv és kultúra menedéke",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "While the central plains suffered Ottoman devastation, Transylvania flourished as the sanctuary of Hungarian literature, vernacular education, and psalm translation, cementing the enduring foundation of modern national consciousness.",
        "characters": [],
        "location": "Debrecen, Vizsoly, Gyulafehérvár, Kolozsvár",
        "grammar": ["metaphorical-stronghold"],
        "vocabularyTopics": ["Magyar műveltség", "Vizsolyi biblia", "Nemzeti megmaradás"],
        "paragraphs": [
            {"type": "narration", "text": "A hódoltság másfél évszázada alatt, amikor az ország szíve romokban hevert, Erdély a magyar anyanyelv és műveltség menedékévé vált."},
            {"type": "narration", "text": "Itt működtek a leghíresebb nyomdák, ahol Károli Gáspár első teljes magyar nyelvű Bibliája (1590) és Szenczi Molnár Albert zsoltárai megjelentek."},
            {"type": "narration", "text": "A fejedelmek által bőkezűen támogatott kollégiumokból nemzedékek sora került ki, akik a magyar nyelvet tudományos és irodalmi szintre emelték."},
            {"type": "narration", "text": "Erdély nem csupán politikai bástya volt, hanem a magyar szellem és öntudat őrzője a legsötétebb történelmi viharok közepette."},
            {"type": "narration", "text": "Ez az aranykor mindmáig a nemzeti összetartozás, a szabadságvágy és az intellektuális büszkeség örök példája."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora-05-hagyatek.json", story_05)

    story_combined = {
        "id": "story.b1.erdelyaranykora",
        "title": "Erdély aranykora és történelmi öröksége",
        "level": "B1",
        "order": 11,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The glorious golden age of the Principality of Transylvania: its establishment after Buda's fall in 1541, the revolutionary 1568 Diet of Torda proclaiming universal religious freedom, Prince Gábor Bethlen's mercantilist economic boom and academic patronage, participation in the Thirty Years' War, and its enduring role as the cultural sanctuary of the Hungarian language.",
        "characters": [],
        "location": "Gyulafehérvár, Torda, Kolozsvár, Kassa, Bécs",
        "grammar": ["essive-formal-kent", "statutory-decrees", "economic-boom", "diplomatic-intentions", "metaphorical-stronghold"],
        "vocabularyTopics": ["Erdély aranykora", "Bethlen Gábor", "Tordai ediktum 1568", "Vallásszabadság", "Kulturális örökség"],
        "paragraphs": [
            {"type": "narration", "text": "Buda 1541-es oszmán megszállása után a keleti hegyek között létrejött az Erdélyi Fejedelemség Gyulafehérvár székhellyel. Noha a fejedelmek adót fizettek a szultánnak, belső önállóságukat és a magyar államiság folytonosságát sikerrel megőrizték."},
            {"type": "narration", "text": "Miközben Nyugat-Európában véres vallásháborúk dúltak, az 1568-as tordai országgyűlésen a világon elsőként iktatták törvénybe a vallásszabadságot. A katolikus, evangélikus, református és unitárius felekezetek békés egymás mellett élése évszázadokra biztosította a belső nyugalmat."},
            {"type": "narration", "text": "A fejedelemség legfényesebb korszakát Bethlen Gábor (1613–1629) uralkodása hozta el. A fejedelem merkantilista reformjaival fellendítette a bányászatot és a külkereskedelmet, megtöltötte a kincstárat, és európai hírű tudományos kollégiumot alapított Gyulafehérváron."},
            {"type": "narration", "text": "A harmincéves háború idején Bethlen a protestáns szövetségesek oldalán sikeres hadjáratokat vezetett a Habsburg császár ellen. Az 1621-es nikolsburgi béke nemzetközi szinten is elismert európai hatalommá emelte Erdélyt, és biztosította a rendi jogokat."},
            {"type": "narration", "text": "A nehéz évszázadokban Erdély nemcsak katonai erősség, hanem a magyar anyanyelv, irodalom és könyvnyomtatás szentélye volt. Az erdélyi aranykor öröksége máig a szabadságszeretet, a vallási türelem és a kulturális büszkeség szimbóluma."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-erdelyaranykora.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-erdelyaranykora-01",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fejedelemség", "principality"],
                    ["hűbérúr", "suzerain / overlord"],
                    ["belső önállóság", "internal autonomy"],
                    ["fejedelmi székhely", "princely seat"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rendi országgyűlés", "diet of estates"],
                    ["kiváltság", "privilege / right"],
                    ["külpolitika", "foreign policy"],
                    ["békés építkezés", "peaceful state-building"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik város volt az Erdélyi Fejedelemség politikai és kulturális székhelye?",
                "options": ["Gyulafehérvár", "Pozsony", "Buda"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen jogi kapcsolatban állt az Erdélyi Fejedelemség az Oszmán Birodalommal?",
                "options": [
                    "A török szultán hűbérese volt és éves adót fizetett, de belső ügyeiben önálló volt.",
                    "Közvetlen török katonai megszállás alatt állt pashákkal.",
                    "Semmilyen kapcsolata nem volt a törökökkel."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik rag fejezi ki a szerepet/státuszt a mondatban: „Erdély önálló állam______ működött.”?",
                "options": ["ként", "ban", "tól"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Gyulafehérvár a fejedelmek székhelye____ a magyar kultúra központjává vált. (as its seat - essive: ként)",
                "answer": "ként"
            },
            {
                "id": "b1-erdelyaranykora-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kik alkották az erdélyi rendi országgyűlés három nemzetét (három rendjét)?",
                "options": [
                    "A magyar nemesek, a székelyek és az erdélyi szászok.",
                    "Csak a budai polgárok.",
                    "A bécsi udvar és a török janicsárok."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért volt történelmi jelentősége az önálló Erdélyi Fejedelemség létezésének a török korban?",
                "options": [
                    "Mert megőrizte a magyar államiság, jogrendszer és anyanyelvi kultúra folytonosságát.",
                    "Mert azonnal egyesítette egész Közép-Európát.",
                    "Mert felszámolta az összes adót."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt az első fejedelme az alakuló Erdélyi Fejedelemségnek?",
                "options": [
                    "János Zsigmond (Szapolyai János fia).",
                    "Mátyás király.",
                    "Szent István."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-erdelyaranykora-02",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vallásszabadság", "freedom of religion"],
                    ["tordai ediktum", "1568 Edict of Torda"],
                    ["bevett vallás", "recognized religion"],
                    ["felekezeti béke", "inter-faith peace"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["katolikus", "Catholic"],
                    ["lutheránus", "Lutheran"],
                    ["református", "Calvinist"],
                    ["unitárius", "Unitarian"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben és melyik városban hirdették ki a híres vallási türelmi ediktumot?",
                "options": ["1568-ban Tordán.", "1526-ban Mohácson.", "1541-ben Budán."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hány vallást ismert el egyenrangú bevett vallásként a tordai ediktum?",
                "options": ["Négyet (katolikus, lutheránus, református, unitárius).", "Csak egyet.", "Tizenkettőt."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik jogi igei kifejezés jelenti a törvénybe foglalást: „Az országgyűlés törvénybe ______ a szabad vallásgyakorlatot.”?",
                "options": ["iktatta", "utalta", "vonta"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tordai törvény kimondta, hogy a hit Isten ajándéka, ezért senkit sem szabad hitéért ____ vetni. (into captivity: fogságba)",
                "answer": "fogságba"
            },
            {
                "id": "b1-erdelyaranykora-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért számított világtörténelmi jelentőségűnek az 1568-as tordai vallásbéke?",
                "options": [
                    "Mert Európában elsőként törvényesítette az állam a felekezeti türelmet és a szabad lelkészválasztást a vallásháborúk korában.",
                    "Mert betiltotta a kereszténységet.",
                    "Mert az összes egyházat a király alá rendelte."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen felekezet született és terjedt el Erdélyben Dávid Ferenc vezetésével a 16. században?",
                "options": [
                    "Az unitárius egyház.",
                    "Az anglikán egyház.",
                    "Az ortodox egyház."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan hatott a vallásbéke Erdély mindennapi életére?",
                "options": [
                    "Megakadályozta a vallási polgárháborúkat, így a lakosság békében és szellemi virágzásban élhetett.",
                    "Minden falu elpusztult.",
                    "A lakosság elmenekült külföldre."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-erdelyaranykora-03",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Bethlen Gábor", "Gábor Bethlen (Prince)"],
                    ["aranykor", "golden age"],
                    ["merkantilizmus", "mercantilism"],
                    ["bányászat", "mining"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemesfém-kivitel", "precious metal export"],
                    ["fejedelmi kollégium", "princely college / academy"],
                    ["mecénás", "patron of arts"],
                    ["gazdasági fellendülés", "economic upswing"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik fejedelem uralkodását nevezzük Erdély aranykorának (1613–1629)?",
                "options": ["Bethlen Gáborét", "Báthory Istvánét", "Rákóczi Ferencét"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen intézményt alapított Bethlen Gábor Gyulafehérváron a tudományok és a műveltség támogatására?",
                "options": [
                    "Híres fejedelmi kollégiumot (akadémiát) gazdag könyvtárral.",
                    "Csak egy katonai börtönt.",
                    "Egy nagy pénzverő gépet tanárok nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igei szerkezet fejezi ki a virágzás kezdetét: „Bethlen alatt az ország gazdasága páratlan ______ indult.”?",
                "options": ["virágzásnak", "virágzásból", "virágzásra"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-03.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fejedelem nagylelkű ____ támogatta a tehetséges magyar diákok külföldi egyetemi tanulmányait. (patron: mecénásként)",
                "answer": "mecénásként"
            },
            {
                "id": "b1-erdelyaranykora-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan növelte Bethlen Gábor a fejedelmi kincstár bevételeit?",
                "options": [
                    "Állami monopóliumot vezetett be a nemesfémek, a szarvasmarha és a só kereskedelmére, és fejlesztette a bányászatot.",
                    "Minden földet eladott a török szultánnak.",
                    "Megszüntette a kereskedelmet."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kiket telepített be Bethlen a bányászat és a kézműipar fejlesztésére Erdélybe?",
                "options": [
                    "Szakképzett felvidéki német bányászokat és külföldi mesterembereket.",
                    "Csak spanyol katonákat.",
                    "Senkit sem engedett be az országba."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen építkezések jellemezték Gyulafehérvárt Bethlen korában?",
                "options": [
                    "Reneszánsz fejedelmi palota épült díszes kertekkel és gazdag könyvtárral.",
                    "Csak fa barakkok épültek.",
                    "Semmilyen építkezés nem folyt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-erdelyaranykora-04",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["harmincéves háború", "Thirty Years' War"],
                    ["szövetséges", "ally"],
                    ["protestáns liga", "Protestant league"],
                    ["hadjárat", "campaign"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["békeszerződés", "peace treaty"],
                    ["diplomácia", "diplomacy"],
                    ["egyensúlyozás", "balancing"],
                    ["nemzetközi elismertség", "international recognition"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik nagy európai háborúba kapcsolódott be Bethlen Gábor a protestáns hatalmak oldalán?",
                "options": ["A harmincéves háborúba (1618–1648).", "A százéves háborúba.", "A napóleoni háborúkba."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik békével zárult le Bethlen Gábor hadjárata 1621-ben a Habsburg császárral szemben?",
                "options": ["A nikolsburgi békével.", "A karlócai békével.", "A szatmári békével."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki a politikai célt: „Bethlen hadba lépett annak ______ , hogy megvédje a vallásszabadságot.”?",
                "options": ["érdekében", "helyett", "nyomán"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nikolsburgi béke révén a fejedelem hét felső-magyarországi vármegyét kapott Erdély ____. (territory: területéhez)",
                "answer": "területéhez"
            },
            {
                "id": "b1-erdelyaranykora-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen címet ajánlottak fel a magyar rendek Bethlen Gábornak az 1620-as besztercebányai országgyűlésen?",
                "options": [
                    "Magyar királlyá választották, de ő nem koronáztatta meg magát a Szent Koronával politikai megfontoltságból.",
                    "Római pápává választották.",
                    "Megfosztották minden címétől."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen nemzetközi szerepet töltött be Erdély a 17. század első felében?",
                "options": [
                    "A protestáns európai koalíció megbecsült szövetségese és az európai nagypolitika elismert szereplője volt.",
                    "Teljesen elszigetelt, elfeledett kis tartomány maradt.",
                    "Ázsia felé indított hódító háborúkat."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Kikkel kötött szövetséget Bethlen Gábor a harmincéves háború idején?",
                "options": [
                    "A cseh rendekkel, valamint Hollandia, Anglia és a protestáns német fejedelmek ligájával.",
                    "Kizárólag a spanyol királlyal.",
                    "A római pápával."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-erdelyaranykora-05",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["műveltség", "culture / erudition"],
                    ["bibliafordítás", "Bible translation"],
                    ["nyomdászat", "printing"],
                    ["anyanyelvi oktatás", "mother-tongue education"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["zsoltáréneklés", "psalm singing"],
                    ["történelmi hagyaték", "historical legacy"],
                    ["nemzeti tudat", "national consciousness"],
                    ["bástya", "bastion / bulwark"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki készítette el az első teljes magyar nyelvű bibliafordítást (a vizsolyi Bibliát 1590-ben)?",
                "options": ["Károli Gáspár.", "Pázmány Péter.", "Balassi Bálint."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki fordította le a genfi zsoltárokat magyar nyelvre, megteremtve a protestáns énekkultúrát?",
                "options": ["Szenczi Molnár Albert.", "Tinódi Lantos Sebestyén.", "Zrinyi Miklós."],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés írja le képletesen Erdély védelmi szerepét: „Erdély a magyar kultúra ______ volt.”?",
                "options": ["bástyája", "romja", "ága"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A reformáció korában az anyanyelvi ____ tette lehetővé a széles rétegek művelődését. (education: oktatás)",
                "answer": "oktatás"
            },
            {
                "id": "b1-erdelyaranykora-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért hívják Debrecent a 'kálvinista Rómának'?",
                "options": [
                    "Mert a Református Kollégium és a Nagytemplom révén a magyar reformáció és szellemi élet legfőbb fellegvára lett.",
                    "Mert a pápa személyesen ott székelt.",
                    "Mert ott épült a legnagyobb katolikus bazilika."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan járult hozzá az erdélyi fejedelmek mecénási politikája a magyar nyelv túléléséhez?",
                "options": [
                    "Nyomdákat létesítettek, támogatták a magyar nyelvű könyvkiadást és ösztöndíjakat adtak a diákoknak.",
                    "Kizárólag latin nyelven engedték a könyvnyomtatást.",
                    "Bezárták az iskolákat a pénzhiány miatt."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent az erdélyi aranykor öröksége a mai magyar nemzeti tudatban?",
                "options": [
                    "A vallási türelem, az autonómia, a tudománytisztelet és az anyanyelvi kultúra csúcsteljesítményét.",
                    "A katonai terjeszkedés végét.",
                    "A gazdasági elszegényedést."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-erdelyaranykora-consolidation",
        "exercises": [
            {
                "id": "b1-erdelyaranykora-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fejedelemség", "principality"],
                    ["belső önállóság", "internal autonomy"],
                    ["fejedelmi székhely", "princely seat"],
                    ["Gyulafehérvár", "Gyulafehérvár"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex02",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vallásszabadság", "freedom of religion"],
                    ["tordai ediktum", "Edict of Torda"],
                    ["bevett vallás", "recognized denomination"],
                    ["felekezeti béke", "denominational peace"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex03",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Bethlen Gábor", "Gábor Bethlen"],
                    ["aranykor", "golden age"],
                    ["merkantilizmus", "mercantilism"],
                    ["mecénás", "patron of arts"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["harmincéves háború", "Thirty Years' War"],
                    ["nikolsburgi béke", "Peace of Nikolsburg"],
                    ["bibliafordítás", "Bible translation"],
                    ["bástya", "bastion / bulwark"]
                ]
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben hozták a tordai vallási ediktumot?",
                "options": ["1568-ban", "1526-ban", "1541-ben", "1686-ban"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik város volt az Erdélyi Fejedelemség állandó székhelye?",
                "options": ["Gyulafehérvár", "Kolozsvár", "Pozsony", "Debrecen"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt Erdély fejedelme a fejedelemség gazdasági és kulturális aranykorában (1613–1629)?",
                "options": ["Bethlen Gábor", "Báthory Zsigmond", "II. Rákóczi Ferenc", "Hunyadi János"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki fordította le az első teljes magyar nyelvű Bibliát Vizsolyban?",
                "options": ["Károli Gáspár", "Szenczi Molnár Albert", "Dávid Ferenc", "Pázmány Péter"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex09",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban szerepel helyesen a -ként essivus-formalis rag?",
                "options": [
                    "Erdély a magyar műveltség bástyájaként védte a nemzeti nyelvet.",
                    "Erdély a magyar műveltség bástyájával védte a nemzeti nyelvet.",
                    "Erdély a magyar műveltség bástyáért védte a nemzeti nyelvet."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex10",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az 1568-as tordai országgyűlés törvénybe iktatta a ____. (religious freedom)",
                "answer": "vallásszabadságot"
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex11",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bethlen Gábor gazdaságpolitikájának köszönhetően az ország gazdasága gyors virágzásnak ____. (began / indult)",
                "answer": "indult"
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex12",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fejedelem hadjáratot indított annak ____, hogy védje a rendi szabadságjogokat. (in order that / érdekében)",
                "answer": "érdekében"
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex13",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Gyulafehérvár a fejedelemség székhelye____ Európa-szerte ismertté vált. (as its seat: ként)",
                "answer": "ként"
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex14",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik négy vallást ismerte el a tordai ediktum?",
                "options": [
                    "A katolikus, lutheránus, református és unitárius vallást.",
                    "A katolikus, ortodox, zsidó és iszlám vallást.",
                    "Csak a református felekezetet.",
                    "Minden nem keresztény vallást."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex15",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan egyensúlyozott az Erdélyi Fejedelemség a két nagyhatalom között?",
                "options": [
                    "Ügyes diplomáciával adót fizetett az Oszmán Birodalomnak, miközben a Habsburgokkal szemben megvédte a magyar rendi és vallási szabadságot.",
                    "Mindkét birodalmat azonnal elfoglalta.",
                    "Kizárólag Franciaország védelme alatt állt hadsereg nélkül.",
                    "Önként beolvadt a török birodalomba."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex16",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen békével ért véget Bethlen Gábor harmincéves háborús hadjárata a császárral 1621-ben?",
                "options": ["A nikolsburgi békével", "A tordai ediktummal", "A pozsonyi békével", "A karlócai békével"],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex17",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen gazdasági rendszert épített ki Bethlen Gábor Erdélyben?",
                "options": [
                    "Merkantilista állami monopóliumokat a bányászatra, a szarvasmarhára és a sóra, ami megtöltötte a kincstárat.",
                    "Teljes szabadpiacot vámok nélkül.",
                    "Minden magántulajdont elkobzott és megsemmisített.",
                    "Kizárólag külföldi segélyekből élt."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex18",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt a 'három nemzet uniója' az erdélyi rendi berendezkedésben?",
                "options": [
                    "A magyar nemesek, a székely lófők és a szász polgárok szövetsége a rendi jogok védelmére.",
                    "Magyarország, Lengyelország és Csehország katonai szövetsége.",
                    "A bécsi udvar, a pápa és a szultán megállapodása.",
                    "A parasztok és jobbágyok szakszervezete."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex19",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen kulturális örökséget hagyott hátra az Erdélyi Fejedelemség aranykora?",
                "options": [
                    "A magyar nyelvű irodalom, a bibliafordítások, a híres kollégiumi hálózat és az európai szintű tudományosság felvirágzását.",
                    "Csak török nyelvű feljegyzéseket.",
                    "A latin nyelv kizárólagos kötelezővé tételét.",
                    "Minden iskola bezárását."
                ],
                "correct": 0
            },
            {
                "id": "b1-erdelyaranykora-consolidation.ex20",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért büszke a mai magyar nemzet az 1568-as tordai vallásbékére az állampolgársági vizsgán?",
                "options": [
                    "Mert a hitbeli szabadság és tolerancia legelső törvénybe iktatása volt a világon, jóval megelőzve a nyugati államokat.",
                    "Mert véget vetett az összes adófizetésnek.",
                    "Mert ekkor vezették be a magyar forintot.",
                    "Mert ekkor koronázták meg Mátyás királyt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-erdelyaranykora-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.erdelyaranykora-01",
        "title": "Önálló fejedelemség (An Independent Principality)",
        "level": "B1",
        "grammar": "Essive-Formal Suffix: -ként (székhelyként, államként, védelmezőként)",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe how the Principality of Transylvania was established after Buda's fall.",
                    "I can explain Gyulafehérvár's role as the princely seat and political hub.",
                    "I can use the essive-formal suffix -ként to express capacities and institutional roles.",
                    "I can master eight new vocabulary items related to early modern Transylvanian statehood."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-erdelyaranykora-01-onallo.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-erdelyaranykora-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-erdelyaranykora-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-erdelyaranykora-01-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-01.ex01", "b1-erdelyaranykora-01.ex01b", "b1-erdelyaranykora-01.ex02", "b1-erdelyaranykora-01.ex03",
                "b1-erdelyaranykora-01.ex04", "b1-erdelyaranykora-01.ex05", "b1-erdelyaranykora-01.ex06", "b1-erdelyaranykora-01.ex07", "b1-erdelyaranykora-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe how the Principality of Transylvania was established after Buda's fall.",
                    "I can explain Gyulafehérvár's role as the princely seat and political hub.",
                    "I can use the essive-formal suffix -ként to express capacities and institutional roles.",
                    "I can master eight new vocabulary items related to early modern Transylvanian statehood."
                ]
            }
        ],
        "goal": [
            "I can describe how the Principality of Transylvania was established after Buda's fall.",
            "I can explain Gyulafehérvár's role as the princely seat and political hub.",
            "I can use the essive-formal suffix -ként to express capacities and institutional roles.",
            "I can master eight new vocabulary items related to early modern Transylvanian statehood."
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.erdelyaranykora-02",
        "title": "Vallási türelem (Religious Tolerance)",
        "level": "B1",
        "grammar": "Statutory Decrees: törvénybe iktat, kimondja, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the European significance of the 1568 Diet of Torda.",
                    "I can list the four officially recognized Christian denominations in Transylvania.",
                    "I can cite historic legal decrees using törvénybe iktat and kinyilvánít.",
                    "I can use eight new vocabulary items concerning religious tolerance and denominations."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-erdelyaranykora-02-vallasbeke.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-erdelyaranykora-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-erdelyaranykora-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-erdelyaranykora-02-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-02.ex01", "b1-erdelyaranykora-02.ex01b", "b1-erdelyaranykora-02.ex02", "b1-erdelyaranykora-02.ex03",
                "b1-erdelyaranykora-02.ex04", "b1-erdelyaranykora-02.ex05", "b1-erdelyaranykora-02.ex06", "b1-erdelyaranykora-02.ex07", "b1-erdelyaranykora-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain the European significance of the 1568 Diet of Torda.",
                    "I can list the four officially recognized Christian denominations in Transylvania.",
                    "I can cite historic legal decrees using törvénybe iktat and kinyilvánít.",
                    "I can use eight new vocabulary items concerning religious tolerance and denominations."
                ]
            }
        ],
        "goal": [
            "I can explain the European significance of the 1568 Diet of Torda.",
            "I can list the four officially recognized Christian denominations in Transylvania.",
            "I can cite historic legal decrees using törvénybe iktat and kinyilvánít.",
            "I can use eight new vocabulary items concerning religious tolerance and denominations."
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.erdelyaranykora-03",
        "title": "Bethlen Gábor (Prince Gábor Bethlen)",
        "level": "B1",
        "grammar": "Economic Boom & Prosperity: virágzásnak indult, fellendült",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the reign of Prince Gábor Bethlen (1613–1629) and Transylvania's Golden Age.",
                    "I can explain Bethlen's mercantilist reforms, mining monopolies, and collegiate patronage.",
                    "I can express economic surge and cultural blooming (virágzásnak indult, fellendült).",
                    "I can deploy eight new vocabulary items regarding early modern economy and patronage."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-erdelyaranykora-03-bethlen.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-erdelyaranykora-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-erdelyaranykora-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-erdelyaranykora-03-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-03.ex01", "b1-erdelyaranykora-03.ex01b", "b1-erdelyaranykora-03.ex02", "b1-erdelyaranykora-03.ex03",
                "b1-erdelyaranykora-03.ex04", "b1-erdelyaranykora-03.ex05", "b1-erdelyaranykora-03.ex06", "b1-erdelyaranykora-03.ex07", "b1-erdelyaranykora-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the reign of Prince Gábor Bethlen (1613–1629) and Transylvania's Golden Age.",
                    "I can explain Bethlen's mercantilist reforms, mining monopolies, and collegiate patronage.",
                    "I can express economic surge and cultural blooming (virágzásnak indult, fellendült).",
                    "I can deploy eight new vocabulary items regarding early modern economy and patronage."
                ]
            }
        ],
        "goal": [
            "I can describe the reign of Prince Gábor Bethlen (1613–1629) and Transylvania's Golden Age.",
            "I can explain Bethlen's mercantilist reforms, mining monopolies, and collegiate patronage.",
            "I can express economic surge and cultural blooming (virágzásnak indult, fellendült).",
            "I can deploy eight new vocabulary items regarding early modern economy and patronage."
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.erdelyaranykora-04",
        "title": "Transylvania & Europe (Erdély és Európa)",
        "level": "B1",
        "grammar": "Diplomatic Purpose Clauses: annak érdekében, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can recount Transylvania's participation in the Thirty Years' War.",
                    "I can explain the diplomatic terms of the 1621 Peace of Nikolsburg.",
                    "I can formulate high-level strategic aims using annak érdekében, hogy...",
                    "I can use eight new vocabulary items concerning international treaties and alliances."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-erdelyaranykora-04-europa.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-erdelyaranykora-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-erdelyaranykora-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-erdelyaranykora-04-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-04.ex01", "b1-erdelyaranykora-04.ex01b", "b1-erdelyaranykora-04.ex02", "b1-erdelyaranykora-04.ex03",
                "b1-erdelyaranykora-04.ex04", "b1-erdelyaranykora-04.ex05", "b1-erdelyaranykora-04.ex06", "b1-erdelyaranykora-04.ex07", "b1-erdelyaranykora-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can recount Transylvania's participation in the Thirty Years' War.",
                    "I can explain the diplomatic terms of the 1621 Peace of Nikolsburg.",
                    "I can formulate high-level strategic aims using annak érdekében, hogy...",
                    "I can use eight new vocabulary items concerning international treaties and alliances."
                ]
            }
        ],
        "goal": [
            "I can recount Transylvania's participation in the Thirty Years' War.",
            "I can explain the diplomatic terms of the 1621 Peace of Nikolsburg.",
            "I can formulate high-level strategic aims using annak érdekében, hogy...",
            "I can use eight new vocabulary items concerning international treaties and alliances."
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.erdelyaranykora-05",
        "title": "A Different Kind of Hungary (Egy sajátos magyar világ)",
        "level": "B1",
        "grammar": "National Metaphors & Sanctuaries: a kultúra bástyája, menedékként",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain how Transylvania preserved Hungarian language, printing, and education.",
                    "I can discuss Károli Gáspár's Vizsoly Bible and Albert Szenczi Molnár's psalm translations.",
                    "I can describe the metaphorical role of Transylvania as a bulwark of national consciousness.",
                    "I can answer citizenship interview questions about Transylvania's Golden Age with full confidence."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-erdelyaranykora-05-hagyatek.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-erdelyaranykora-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-erdelyaranykora-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-erdelyaranykora-05-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-05.ex01", "b1-erdelyaranykora-05.ex01b", "b1-erdelyaranykora-05.ex02", "b1-erdelyaranykora-05.ex03",
                "b1-erdelyaranykora-05.ex04", "b1-erdelyaranykora-05.ex05", "b1-erdelyaranykora-05.ex06", "b1-erdelyaranykora-05.ex07", "b1-erdelyaranykora-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain how Transylvania preserved Hungarian language, printing, and education.",
                    "I can discuss Károli Gáspár's Vizsoly Bible and Albert Szenczi Molnár's psalm translations.",
                    "I can describe the metaphorical role of Transylvania as a bulwark of national consciousness.",
                    "I can answer citizenship interview questions about Transylvania's Golden Age with full confidence."
                ]
            }
        ],
        "goal": [
            "I can explain how Transylvania preserved Hungarian language, printing, and education.",
            "I can discuss Károli Gáspár's Vizsoly Bible and Albert Szenczi Molnár's psalm translations.",
            "I can describe the metaphorical role of Transylvania as a bulwark of national consciousness.",
            "I can answer citizenship interview questions about Transylvania's Golden Age with full confidence."
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.erdelyaranykora-consolidation",
        "title": "Unit 11 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can summarize the founding, autonomy, and golden age of the Principality of Transylvania.",
                    "I can explain the 1568 Diet of Torda, Gábor Bethlen's rule, and the Thirty Years' War.",
                    "I can discuss the preservation of Hungarian vernacular literature, colleges, and printing.",
                    "I can answer all citizenship interview questions on Transylvania's Golden Age flawlessly."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-erdelyaranykora-consolidation-ex.json", "exerciseRefs": [
                "b1-erdelyaranykora-consolidation.ex01", "b1-erdelyaranykora-consolidation.ex02", "b1-erdelyaranykora-consolidation.ex03", "b1-erdelyaranykora-consolidation.ex04",
                "b1-erdelyaranykora-consolidation.ex05", "b1-erdelyaranykora-consolidation.ex06", "b1-erdelyaranykora-consolidation.ex07", "b1-erdelyaranykora-consolidation.ex08",
                "b1-erdelyaranykora-consolidation.ex09", "b1-erdelyaranykora-consolidation.ex10", "b1-erdelyaranykora-consolidation.ex11", "b1-erdelyaranykora-consolidation.ex12",
                "b1-erdelyaranykora-consolidation.ex13", "b1-erdelyaranykora-consolidation.ex14", "b1-erdelyaranykora-consolidation.ex15", "b1-erdelyaranykora-consolidation.ex16",
                "b1-erdelyaranykora-consolidation.ex17", "b1-erdelyaranykora-consolidation.ex18", "b1-erdelyaranykora-consolidation.ex19", "b1-erdelyaranykora-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can summarize the founding, autonomy, and golden age of the Principality of Transylvania.",
                    "I can explain the 1568 Diet of Torda, Gábor Bethlen's rule, and the Thirty Years' War.",
                    "I can discuss the preservation of Hungarian vernacular literature, colleges, and printing.",
                    "I can answer all citizenship interview questions on Transylvania's Golden Age flawlessly."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-erdelyaranykora-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_11_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 11 (b1-erdelyaranykora)!")
