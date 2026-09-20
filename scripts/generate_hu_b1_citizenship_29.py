#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 29: National Symbols (b1-nemzetijelkepek)."""

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

def build_unit_29_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.nemzetijelkepek.01",
        "lesson": "b1-nemzetijelkepek-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nemzeti lobogó", "translation": "national flag / standard", "pos": "noun"},
            {"lemma": "trikolór", "translation": "tricolor (three horizontal stripes: red, white, green)", "pos": "noun"},
            {"lemma": "piros-fehér-zöld", "translation": "red-white-green (the national colors)", "pos": "adjective"},
            {"lemma": "erő", "translation": "strength (symbolized by the red stripe)", "pos": "noun"},
            {"lemma": "hűség", "translation": "fidelity / loyalty (symbolized by the white stripe)", "pos": "noun"},
            {"lemma": "remény", "translation": "hope (symbolized by the green stripe)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetijelkepek-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.nemzetijelkepek.02",
        "lesson": "b1-nemzetijelkepek-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Szent Korona", "translation": "Holy Crown of Hungary (supreme constitutional relic)", "pos": "noun"},
            {"lemma": "ferde kereszt", "translation": "tilted cross atop the Holy Crown", "pos": "noun"},
            {"lemma": "királyi jogar", "translation": "royal scepter (crystal-headed symbol of justice and authority)", "pos": "noun"},
            {"lemma": "országalma", "translation": "globus cruciger / royal orb (symbol of earthly dominion)", "pos": "noun"},
            {"lemma": "koronázási palást", "translation": "coronation mantle embroidered with gold thread (1031)", "pos": "noun"},
            {"lemma": "Szent Korona-tan", "translation": "Doctrine of the Holy Crown (historic source of constitutional sovereignty)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetijelkepek-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.nemzetijelkepek.03",
        "lesson": "b1-nemzetijelkepek-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Magyarország címere", "translation": "Coat of Arms of Hungary (crowned split shield)", "pos": "noun"},
            {"lemma": "kettős kereszt", "translation": "patriarchal / double cross (apostolic symbol on right field)", "pos": "noun"},
            {"lemma": "hármas halom", "translation": "triple mount (Tátra, Mátra, Fátra mountains beneath the cross)", "pos": "noun"},
            {"lemma": "Árpád-sávok", "translation": "Árpád stripes (four silver and four red horizontal bars on left field)", "pos": "noun"},
            {"lemma": "hasított pajzs", "translation": "vertically split shield forming the national arms", "pos": "noun"},
            {"lemma": "állami jelkép", "translation": "official state symbol enshrined in the Fundamental Law", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetijelkepek-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.nemzetijelkepek.04",
        "lesson": "b1-nemzetijelkepek-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nemzeti Himnusz", "translation": "National Anthem of Hungary ('Isten, áldd meg a magyart')", "pos": "noun"},
            {"lemma": "Kölcsey Ferenc", "translation": "Ferenc Kölcsey (author who wrote the Himnusz in Szatmárcseke in 1823)", "pos": "noun"},
            {"lemma": "Erkel Ferenc", "translation": "Ferenc Erkel (composer of the official Anthem music in 1844)", "pos": "noun"},
            {"lemma": "a magyar kultúra napja", "translation": "Day of Hungarian Culture (celebrated on January 22nd, birthday of Himnusz)", "pos": "noun"},
            {"lemma": "nemzeti ima", "translation": "national prayer (sung at all official ceremonies standing at attention)", "pos": "noun"},
            {"lemma": "Szatmárcseke", "translation": "Szatmárcseke (eastern village where Kölcsey composed the Himnusz)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetijelkepek-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.nemzetijelkepek.05",
        "lesson": "b1-nemzetijelkepek-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Szózat", "translation": "Szózat / The Appeal ('Hazádnak rendületlenül légy híve, ó magyar')", "pos": "noun"},
            {"lemma": "Vörösmarty Mihály", "translation": "Mihály Vörösmarty (poet who penned the Szózat in 1836)", "pos": "noun"},
            {"lemma": "Egressy Béni", "translation": "Béni Egressy (composer who set the Szózat to music in 1843)", "pos": "noun"},
            {"lemma": "Hazádnak rendületlenül", "translation": "'To your homeland be unwaveringly faithful' (immortal opening line)", "pos": "expression"},
            {"lemma": "második himnusz", "translation": "second national anthem (sung at the conclusion of celebrations)", "pos": "noun"},
            {"lemma": "nemzeti hűség", "translation": "fidelity to the Hungarian nation through all history", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-nemzetijelkepek-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.nemzetijelkepek.01.heraldic-symbolism",
        "title": "Heraldic Symbolism: szimbolizál, jelképez, kifejez",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Valencies in Symbolic Explanation",
                "content": "Describing national flags and emblems utilizes verbs of representation: *szimbolizál vmit* ('symbolizes sth'), *jelképezi az erőt* ('represents strength' - accusative), *kifejezi a nemzet hűségét* ('expresses the fidelity of the nation')."
            },
            {
                "type": "examples",
                "title": "Flag symbolism examples",
                "items": [
                    {
                        "spanish": "A magyar trikolór piros sávja az erőt, a fehér a hűséget, a zöld pedig a reményt jelképezi.",
                        "english": "The red stripe of the Hungarian tricolor represents strength, the white fidelity, and the green hope."
                    },
                    {
                        "spanish": "A három nemzeti szín hivatalos használatát az 1848-as törvények rögzítették először.",
                        "english": "The official use of the three national colors was first recorded by the laws of 1848."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetijelkepek-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.nemzetijelkepek.02.reverent-passive-doctrine",
        "title": "Reverent Constitutional Metaphors: a Szent Korona-tan",
        "sections": [
            {
                "type": "text",
                "title": "Constitutional Personification of the Crown",
                "content": "In Hungarian public law, the Holy Crown is personified: *megtestesíti az állam folytonosságát és egységét* ('embodies the continuity and unity of the state'), *a szuverenitás forrása* ('source of sovereignty'). Regalia items are governed by respectful verbs: *őriz* ('guards'), *koronázási jelvény* ('coronation insignia')."
            },
            {
                "type": "examples",
                "title": "Holy Crown doctrine examples",
                "items": [
                    {
                        "spanish": "A Szent Korona a magyar államiság folytonosságát és a nemzet egységét testesíti meg.",
                        "english": "The Holy Crown embodies the continuity of Hungarian statehood and the unity of the nation."
                    },
                    {
                        "spanish": "A koronázási jelvényeket az Országház kupolacsarnokában őrzi a Magyar Honvédség Koronaőrsége.",
                        "english": "The coronation insignia are guarded in the dome hall of the Parliament by the Crown Guard of the Hungarian Defense Forces."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetijelkepek-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.nemzetijelkepek.03.descriptive-essive-kent",
        "title": "Descriptive Essive Case: -ként / -képp",
        "sections": [
            {
                "type": "text",
                "title": "The Essive-Modal Suffix -ként",
                "content": "The suffix *-ként* expresses role, function, or capacity ('as / in the capacity of'): *nemzeti jelképként tisztel* ('reveres as a national symbol'), *történelmi ereklyeként őriz* ('preserves as a historical relic')."
            },
            {
                "type": "examples",
                "title": "Essive examples",
                "items": [
                    {
                        "spanish": "Magyarország címere a történelmi hagyományok hordozójaként jelenik meg az Alaptörvényben.",
                        "english": "The coat of arms of Hungary appears in the Fundamental Law as the bearer of historical traditions."
                    },
                    {
                        "spanish": "A kettős kereszt apostoli szimbólumként áll a hármas halom zöld csúcsán.",
                        "english": "The double cross stands as an apostolic symbol upon the green peak of the triple mount."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetijelkepek-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.nemzetijelkepek.04.poetic-and-prayer-syntax",
        "title": "Solemn and Poetic Register: áldd meg, nyújts feléje",
        "sections": [
            {
                "type": "text",
                "title": "Subjunctive / Imperative of Supplication in the Himnusz",
                "content": "The National Anthem is a poetic prayer to God. Supplication verbs take definite imperative/subjunctive forms: *Isten, áldd meg a magyart!* ('God, bless the Hungarian!'), *Nyújts feléje védő kart!* ('Extend toward him a shielding arm!')."
            },
            {
                "type": "examples",
                "title": "Anthem prayer examples",
                "items": [
                    {
                        "spanish": "A magyar Himnusz nem harci induló, hanem a nemzet közös imája a teremtő Istenhez.",
                        "english": "The Hungarian Anthem is not a battle march, but the collective prayer of the nation to Creator God."
                    },
                    {
                        "spanish": "Január 22-én, Kölcsey kéziratának befejezése napján ünnepeljük a magyar kultúra napját.",
                        "english": "On January 22nd, the day Kölcsey finished his manuscript, we celebrate the Day of Hungarian Culture."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetijelkepek-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.nemzetijelkepek.05.steadfast-adverbs",
        "title": "Steadfast Devotion & Adverbial Modifiers: rendületlenül, hűségesen",
        "sections": [
            {
                "type": "text",
                "title": "Manners of Patriotic Fidelity",
                "content": "Vörösmarty's *Szózat* immortalized steadfast adverbs: *rendületlenül* ('unwaveringly / steadfastly'), *hűen / hűségesen* ('faithfully'), *mindvégig* ('all the way to the end'): *Hazádnak rendületlenül légy híve, ó magyar!*"
            },
            {
                "type": "examples",
                "title": "Steadfast devotion examples",
                "items": [
                    {
                        "spanish": "A Szózat a magyar nemzet rendületlen hűségfogadalma a szülőföld és a hazai táj iránt.",
                        "english": "The Szózat is the Hungarian nation's steadfast pledge of fidelity toward the homeland and native landscape."
                    },
                    {
                        "spanish": "Ünnepi alkalmakkor a Himnusszal kezdjük és a Szózattal zárjuk a megemlékezéseket.",
                        "english": "On festive occasions, we begin commemorations with the Anthem and conclude them with the Szózat."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-nemzetijelkepek-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Story Files (5 regular lesson stories + 1 combined omnibus story)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.nemzetijelkepek.01",
        "lesson": 1,
        "order": 1,
        "title": "A magyar trikolór és nemzeti színeink története",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary's national flag is a horizontal tricolor of red, white, and green. Established during the Reform Era and codified by the 1848 revolutionary laws, its colors represent strength (red), fidelity (white), and hope (green). From the 1848 cockades to the flag with a cut-out hole in 1956, the tricolor symbolizes the nation's struggle for freedom and sovereignty.",
        "characters": [
            "Zászlóért felelős történész a Nemzeti Múzeumban",
            "Fiatal diák a márciusi ünnepségen"
        ],
        "location": "Budapest, Magyar Nemzeti Múzeum lépcsője",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország hivatalos zászlaja három egyenlő szélességű vízszintes sávból áll: felül piros, középen fehér, alul zöld. E három szín évszázados történelmi gyökerekkel rendelkezik."
            },
            {
                "type": "dialogue",
                "speaker": "Múzeumi történész",
                "text": "A színeknek mély szimbolikus jelentése van: a piros az erőt, a hazáért ontott vért, a fehér a tisztaságot és a hűséget, a zöld pedig a reményt és a virágzó magyar földet fejezi ki."
            },
            {
                "type": "narration",
                "text": "A reformkorban a francia forradalom mintájára született meg a magyar trikolór gondolata. 1848. március 15-én a forradalmi ifjúság piros-fehér-zöld kokárdát tűzött a kabátjára, s az áprilisi törvények hivatalos nemzeti jelképpé emelték a zászlót."
            },
            {
                "type": "dialogue",
                "speaker": "Fiatal diák",
                "text": "És 1956-ban a forradalmárok kivágták a zászló közepéből a szovjet mintájú kommunista címert! A lyukas zászló lett a szabadságharc szent jelképe a világ szemében!"
            },
            {
                "type": "narration",
                "text": "Ma a nemzeti trikolór méltósággal lobog a középületeken és a Parlament előtt, kifejezve a magyar nemzet egységét és szuverenitását."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek-01-zaszlo.json", story_01)

    story_02 = {
        "id": "story.b1.nemzetijelkepek.02",
        "lesson": 2,
        "order": 2,
        "title": "A Szent Korona és a koronázási jelvények misztériuma",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Holy Crown of Hungary is Europe's oldest surviving coronation crown. Comprising the Greek Crown (corona graeca) and the Latin Crown (corona latina), crowned with its famous tilted cross, it is not merely an ornament but the legal embodiment of Hungarian statehood through the historic Doctrine of the Holy Crown. Guarded in the Parliament with the scepter, orb, and mantle, it returned home from the US in 1978.",
        "characters": [
            "A Koronaőrség parancsnoka",
            "Látogató az Országház kupolacsarnokában"
        ],
        "location": "Budapest, az Országház kupolacsarnoka",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az Országház kupolacsarnokának félhomályában, golyóálló üveg alatt pihen Magyarország legféltettebb nemzeti kincse: a Szent Korona. Mellette látható a hegyikristály gombos jogar, az aranyozott országalma és a kard."
            },
            {
                "type": "dialogue",
                "speaker": "A Koronaőrség parancsnoka",
                "text": "A magyar jogfejlődésben egyedülálló módon a Szent Korona nem a király tulajdona volt, hanem maga az államhatalom és a szuverenitás szent megtestesítője. Ez a híres Szent Korona-tan alapja!"
            },
            {
                "type": "narration",
                "text": "A korona két fő részből áll: a bizánci stílusú alsó abroncsból és a latin feliratos felső keresztpántból. Tetején a jellegzetes ferde kereszt áll, amely egy 17. századi sérülés emlékét őrzi."
            },
            {
                "type": "dialogue",
                "speaker": "Látogató",
                "text": "A második világháború végén a koronaőrség kimenekítette a koronát, s évtizedekig a Fort Knox katonai bázison őrizték az Egyesült Államokban! Mekkora ünnep volt, amikor 1978-ban végre hazatérhetett Budapestre!"
            },
            {
                "type": "narration",
                "text": "2000 óta a Szent Korona az Országházban áll, ahol a díszegyenruhás honvédek karddal a kézben éjjel-nappal őrzik a magyar államiság ezeréves jelképét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek-02-szentkorona.json", story_02)

    story_03 = {
        "id": "story.b1.nemzetijelkepek.03",
        "lesson": 3,
        "order": 3,
        "title": "Magyarország címere: a kettős kereszt és az Árpád-sávok",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Coat of Arms of Hungary is an elegant vertically split shield crowned by the Holy Crown. The right field displays the silver apostolic patriarchal cross rising from a golden coronet atop three green hills (Tátra, Mátra, Fátra). The left field features the four silver and four red stripes of the founding Árpád Dynasty, representing Hungary's rivers (Duna, Tisza, Dráva, Száva).",
        "characters": [
            "Heraldikus és történész",
            "Középiskolai történelemtanár"
        ],
        "location": "Budapest, a Magyar Országos Levéltár várbeli kutatóterme",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország címere hegyes talpú, hasított pajzs, amelynek tetején a Szent Korona nyugszik. A heraldika szabályai szerint a címer két mezője a magyar történelem két legfontosabb korszakát egyesíti."
            },
            {
                "type": "dialogue",
                "speaker": "Heraldikus",
                "text": "A jobb oldali mezőben vörös alapon zöld hármas halom látható, középső csúcsán arany koronával, amelyből ezüst kettős kereszt emelkedik ki. Ez a keresztény királyság apostoli méltóságát szimbolizálja, a halmok pedig a Tátra, Mátra és Fátra hegyeit idézik."
            },
            {
                "type": "dialogue",
                "speaker": "Történelemtanár",
                "text": "A bal oldali mezőben a vörössel és ezüsttel hétszer vágott mező látható: az Árpád-sávok! A néphagyomány szerint a négy ezüst sáv Magyarország négy nagy történelmi folyóját – a Dunát, a Tiszát, a Drávát és a Szávát – jelképezi."
            },
            {
                "type": "narration",
                "text": "A kommunista évtizedekben a címert eltávolították és szovjet típusú emblémákkal helyettesítették. Ám 1990-ben a szabadon választott országgyűlés első törvényei között állította vissza a történelmi koronás címert."
            },
            {
                "type": "narration",
                "text": "A címer ma minden hivatalos okmányon, útlevélen és iskolai bizonyítványon ott áll, büszkén hirdetve a magyar nemzet ezeréves keresztény európai gyökereit."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek-03-cimer.json", story_03)

    story_04 = {
        "id": "story.b1.nemzetijelkepek.04",
        "lesson": 4,
        "order": 4,
        "title": "A Nemzeti Himnusz: Kölcsey imája és Erkel muzsikája",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary's National Anthem, 'Isten, áldd meg a magyart', is unique among world anthems: not a martial boast of military conquest, but a profound national prayer. Penned by poet Ferenc Kölcsey on January 22, 1823 in Szatmárcseke and set to immortal music by composer Ferenc Erkel in 1844, it surveys centuries of trials and blessings, asking God's protection for a people who have already suffered for past and future sins.",
        "characters": [
            "Kölcsey Ferenc költő szelleme",
            "Erkel Ferenc zeneszerző",
            "Szavaló diák a Szatmárcsekei emlékház udvarán"
        ],
        "location": "Szatmárcseke és a Nemzeti Színház Budapesten",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1823. január 22-én a szabolcsi csendben fekvő Szatmárcsekén Kölcsey Ferenc letette a tollat. Befejezte költeményét, amelynek ezt a címet adta: 'Hymnus, a Magyar nép zivataros századaiból'."
            },
            {
                "type": "dialogue",
                "speaker": "Kölcsey Ferenc",
                "text": "Nem a dicsőségünket akartam megénekelni, hanem a nemzet lelkiismeretét! A tatár pusztítását, a török rabigát és a belső viszályokat... Hogy bocsásson meg az Úr a vétkeinkért, mert ez a nép már megbűnhődte a múltat és jövendőt!"
            },
            {
                "type": "narration",
                "text": "1844-ben a Nemzeti Színház pályázatot írt ki a vers megzenésítésére. A győztes Erkel Ferenc lett, aki a magyar verbunkos és a mély egyházi zene motívumaiból komponált felemelő, himnikus dallamot."
            },
            {
                "type": "dialogue",
                "speaker": "Erkel Ferenc zeneszerző",
                "text": "A dallamnak egyszerre kellett áhítatosnak lennie, mint egy templomi zsoltár, és méltóságteljesnek, mint egy királyi fogadalom! Amikor felhangzik, mindenkinek megdobban a szíve!"
            },
            {
                "type": "narration",
                "text": "A Himnusz születésének napja, január 22-e 1989 óta a Magyar Kultúra Napja. Amikor a Himnuszt éneklik a magyarok bárhol a Földön, vigyázzban állva, csendes áhítattal hajtják meg fejüket."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek-04-himnusz.json", story_04)

    story_05 = {
        "id": "story.b1.nemzetijelkepek.05",
        "lesson": 5,
        "order": 5,
        "title": "A Szózat: Vörösmarty hűségfogadalma a hazához",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Regarded as Hungary's second national anthem, the Szózat ('The Appeal') was written by romantic poet Mihály Vörösmarty in 1836 and set to stirring music by Béni Egressy in 1843. Opening with the immortal imperative 'To your homeland be unwaveringly faithful', it proclaims that the soil of the motherland is the cradle and grave of every Hungarian, concluding ceremonies with an unbreakable pledge of fidelity.",
        "characters": [
            "Vörösmarty Mihály költő",
            "Egressy Béni zeneszerző",
            "Kórustag az ünnepi megemlékezésen"
        ],
        "location": "Székesfehérvár, a budapesti Nemzeti Színház és az Országház lépcsője",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1836-ban a reformkor lázában égő Magyarországon megjelent Vörösmarty Mihály költeménye, a Szózat. Az Auróra című zsebkönyvben napvilágot látott vers azonnal nemzeti hitvallássá vált."
            },
            {
                "type": "dialogue",
                "speaker": "Vörösmarty Mihály",
                "text": "Hazádnak rendületlenül légy híve, ó magyar! Bölcsőd az s majdan sírod is, mely ápol s eltakar! A nagyvilágon e kívül nincsen számodra hely; áldjon vagy verjen sors keze: itt élned, halnod kell!"
            },
            {
                "type": "narration",
                "text": "1843-ban Egressy Béni zenésítette meg a költeményt. Míg a Himnusz Istenhez szóló alázatos fohász, addig a Szózat a magyar emberhez intézett szigorú és felemelő felhívás a nemzeti hűségre."
            },
            {
                "type": "dialogue",
                "speaker": "Egressy Béni zeneszerző",
                "text": "Olyan zenét írtam, amely lüktet, mint a szívverés, és megrázza az ember lelkét! A Szózat nem engedi, hogy bárki elfelejtse, honnan jött és hová tartozik!"
            },
            {
                "type": "narration",
                "text": "A magyar hagyományban a nemzeti ünnepeket a Himnusz hangjaival nyitják meg, és a Szózattal zárják. E két költemény együtt alkotja a magyar nemzeti önazonosság örök fundamentumát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek-05-szozat.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.nemzetijelkepek.combined",
        "title": "Magyarország nemzeti jelképeinek története",
        "level": "B1",
        "order": 29,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "A comprehensive panoramic chronicle of Hungary's sacred national symbols enshrined in the Fundamental Law. From the red-white-green tricolor representing strength, fidelity, and hope; the historic Holy Crown and coronation regalia embodying millennial statehood; the crowned coat of arms uniting the apostolic double cross and the Árpád stripes; Kölcsey's Himnusz as the collective national prayer; to Vörösmarty's Szózat as the steadfast pledge of fidelity to the motherland.",
        "characters": [
            "Kölcsey Ferenc",
            "Vörösmarty Mihály",
            "A Koronaőrség tisztje",
            "Múzeumigazgató"
        ],
        "location": "Budapest, Országház és a Nemzeti Múzeum",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország Alaptörvénye kimondja: hazánk nemzeti jelképei a címer, a zászló és a Himnusz. E jelképek nem csupán hivatalos állami attribútumok, hanem a nemzet ezeréves küzdelmeinek, hitének és összetartozásának szent kifejezői."
            },
            {
                "type": "narration",
                "text": "A piros-fehér-zöld lobogó az 1848-as szabadságharcban és az 1956-os forradalomban a szabadság egyetemes szimbólumává vált: a piros az erő, a fehér a hűség, a zöld a remény színe. Az Országházban őrzött Szent Korona a legősibb európai koronázási ékszer, amely a Szent Korona-tan révén a magyar államiság folytonosságát testesíti meg."
            },
            {
                "type": "narration",
                "text": "Magyarország címere az Árpád-házi királyok sávjait és az apostoli kettős keresztet hordozza a Tátra, Mátra és Fátra hármas halmán, tetején a Szent Koronával. A két legfontosabb nemzeti költemény – Kölcsey Himnusza és Vörösmarty Szózata – imádságban és rendületlen hűségfogadalomban foglalja össze mindazt, amit a magyarság jelent."
            },
            {
                "type": "narration",
                "text": "E nemzeti jelképek ismerete és tisztelete minden magyar állampolgár közös büszkesége és a honosítási eskü erkölcsi alapja."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-nemzetijelkepek.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-nemzetijelkepek-01",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-01.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Milyen színekből áll a magyar nemzeti zászló fentről lefelé?",
                "options": [
                    "Piros, fehér és zöld vízszintes sávokból.",
                    "Kék, fehér és piros függőleges sávokból.",
                    "Fekete, piros és arany sávokból."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A piros szín az erőt, a fehér a hűséget, a zöld pedig a reményt jelképez_____. (symbolizes - i)",
                "answer": "i"
            },
            {
                "id": "b1-nemzetijelkepek-01.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nemzeti", "lobogó", "méltósággal", "leng", "az", "Országház", "előtt."],
                "solution": ["A", "nemzeti", "lobogó", "méltósággal", "leng", "az", "Országház", "előtt."]
            },
            {
                "id": "b1-nemzetijelkepek-01.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik történelmi esemény idején vált a 'lyukas zászló' a magyar szabadság jelképévé?",
                "options": [
                    "Az 1956-os forradalom idején, amikor kivágták a kommunista címert.",
                    "Az 1848-as forradalom idején.",
                    "A honfoglalás korában."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Március 15-én a magyarok piros-fehér-zöld kokárdá_____ tűznek a kabátjukra. (accusative - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetijelkepek-01.ex06",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mit jelent a zöld szín a magyar nemzeti trikolórban?",
                "options": [
                    "A reményt és a virágzó magyar szülőföldet.",
                    "A hadsereg erejét.",
                    "A tiszta tengereket."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemzeti trikolór hivatalos használatát az 1848-as törvények rögzítet_____. (recorded - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-nemzetijelkepek-01.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "három", "szín", "kifejezi", "a", "magyar", "nemzet", "összetartozását."],
                "solution": ["A", "három", "szín", "kifejezi", "a", "magyar", "nemzet", "összetartozását."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-nemzetijelkepek-02",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-02.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hol őrzik ma a Szent Koronát és a királyi koronázási jelvényeket?",
                "options": [
                    "Az Országház kupolacsarnokában Budapesten.",
                    "A Magyar Nemzeti Múzeum pincéjében.",
                    "A visegrádi vár tornyában."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Szent Korona a magyar államiság folytonosságát testesí_____ meg. (embodies - ti)",
                "answer": "ti"
            },
            {
                "id": "b1-nemzetijelkepek-02.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "koronázási", "jelvényeket", "a", "honvédség", "koronaőrei", "őrzik."],
                "solution": ["A", "koronázási", "jelvényeket", "a", "honvédség", "koronaőrei", "őrzik."]
            },
            {
                "id": "b1-nemzetijelkepek-02.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Milyen különleges jellegzetessége van a Szent Korona tetején álló keresztnek?",
                "options": [
                    "Ferde (meg van dőlve egy régi sérülés miatt).",
                    "Hiányzik róla.",
                    "Világít a sötétben."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A jogar gombja különleges hegyikristályból készül_____. (was made - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetijelkepek-02.ex06",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik évben tért haza a Szent Korona az Egyesült Államokból Magyarországra?",
                "options": [
                    "1978-ban.",
                    "1956-ban.",
                    "2004-ben."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Szent Korona-tan a történelmi alkotmány alapköveként szolgál_____. (served - t)",
                "answer": "t"
            },
            {
                "id": "b1-nemzetijelkepek-02.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "Szent", "Korona", "Európa", "egyik", "legrégebbi", "beavató", "koronája."],
                "solution": ["A", "Szent", "Korona", "Európa", "egyik", "legrégebbi", "beavató", "koronája."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-nemzetijelkepek-03",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-03.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mi látható Magyarország hivatalos címerének jobb oldali mezőjében?",
                "options": [
                    "Zöld hármas halom, arany korona és ezüst kettős kereszt.",
                    "Egy repülő turulmadár karddal.",
                    "Egy háromszínű zászló."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kettős kereszt apostoli szimbólum_____ áll a zöld hármas halmon. (as - ként)",
                "answer": "ként"
            },
            {
                "id": "b1-nemzetijelkepek-03.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "címer", "bal", "oldalán", "az", "Árpád-sávok", "láthatók."],
                "solution": ["A", "címer", "bal", "oldalán", "az", "Árpád-sávok", "láthatók."]
            },
            {
                "id": "b1-nemzetijelkepek-03.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hány ezüst és hány piros sávból állnak az Árpád-sávok a címerben?",
                "options": [
                    "Négy ezüst és négy piros sávból (összesen nyolc sáv).",
                    "Három piros és három zöld sávból.",
                    "Tíz fekete és fehér sávból."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A címerpajzs tetején a Szent Korona helyezkedik _____. (prefix - el)",
                "answer": "el"
            },
            {
                "id": "b1-nemzetijelkepek-03.ex06",
                "type": "multiple-choice",
                "category": "history",
                "question": "Mely három hegyet szimbolizálja a néphagyomány szerint a hármas halom?",
                "options": [
                    "A Tátrát, a Mátrát és a Fátrát.",
                    "A Gellért-hegyet, a Várhegyet és a János-hegyet.",
                    "Az Alpokat, a Kárpátokat és a Kaukázust."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az Alaptörvény Magyarország címereként határozza _____ ezt a pajzsot. (prefix - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-nemzetijelkepek-03.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "koronás", "címer", "Magyarország", "ezeréves", "államiságát", "hirdeti."],
                "solution": ["A", "koronás", "címer", "Magyarország", "ezeréves", "államiságát", "hirdeti."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-nemzetijelkepek-04",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-04.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Ki írta Magyarország Nemzeti Himnuszának szövegét?",
                "options": [
                    "Kölcsey Ferenc (1823-ban).",
                    "Petőfi Sándor.",
                    "Arany János."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Isten, áldd _____ a magyart jó kedvvel, bőséggel! (prefix - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-nemzetijelkepek-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "Himnusz", "zenéjét", "Erkel", "Ferenc", "szerezte", "1844-ben."],
                "solution": ["A", "Himnusz", "zenéjét", "Erkel", "Ferenc", "szerezte", "1844-ben."]
            },
            {
                "id": "b1-nemzetijelkepek-04.ex04",
                "type": "multiple-choice",
                "category": "culture",
                "question": "Melyik napon ünnepeljük a Magyar Kultúra Napját a Himnusz befejezésének emlékére?",
                "options": [
                    "Január 22-én.",
                    "Március 15-én.",
                    "Augusztus 20-án."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Himnusz a magyar nemzet közös imádságaként szólal _____. (prefix - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-nemzetijelkepek-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan viselkednek a résztvevők a Himnusz éneklése vagy hallgatása közben?",
                "options": [
                    "Vigyázzban állva, csendes méltósággal hallgatják vagy éneklik.",
                    "Tapsolnak és táncolnak a ritmusra.",
                    "Beszélgetnek a telefonjukon."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kölcsey Ferenc Szatmárcsekén fejezte _____ a Himnusz kéziratát. (prefix - be)",
                "answer": "be"
            },
            {
                "id": "b1-nemzetijelkepek-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "Himnusz", "egyedülálló", "és", "mély", "nemzeti", "ima."],
                "solution": ["A", "magyar", "Himnusz", "egyedülálló", "és", "mély", "nemzeti", "ima."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-nemzetijelkepek-05",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-05.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Ki írta a Szózat című költeményt, amelyet 'második himnuszunknak' is neveznek?",
                "options": [
                    "Vörösmarty Mihály (1836-ban).",
                    "Ady Endre.",
                    "József Attila."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Hazádnak rendületlenül légy híve, _____ magyar! (interjection - ó)",
                "answer": "ó"
            },
            {
                "id": "b1-nemzetijelkepek-05.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "Szózat", "zenéjét", "Egressy", "Béni", "komponálta."],
                "solution": ["A", "Szózat", "zenéjét", "Egressy", "Béni", "komponálta."]
            },
            {
                "id": "b1-nemzetijelkepek-05.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Hogyan kezdődik a Szózat legismertebb sora?",
                "options": [
                    "'Hazádnak rendületlenül légy híve, ó magyar...'",
                    "'Isten, áldd meg a magyart...'",
                    "'Talpra magyar, hí a haza...'"
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Szózat a szülőföld iránti rendületlen hűségre szólít _____. (prefix - fel)",
                "answer": "fel"
            },
            {
                "id": "b1-nemzetijelkepek-05.ex06",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Milyen szerepet tölt be a Szózat az ünnepi megemlékezéseken?",
                "options": [
                    "Az ünnepségek záróakkordjaként éneklik a Himnusz után.",
                    "Kizárólag sporteseményeken játsszák le.",
                    "Csak rádióműsorok szignáljaként használják."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nagyvilágon e kívül nincsen számodra hely: itt élned, halnod _____! (must - kell)",
                "answer": "kell"
            },
            {
                "id": "b1-nemzetijelkepek-05.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "Szózat", "a", "magyar", "hazafiság", "örök", "érvényű", "hitvallása."],
                "solution": ["A", "Szózat", "a", "magyar", "hazafiság", "örök", "érvényű", "hitvallása."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-nemzetijelkepek-consolidation",
        "exercises": [
            {
                "id": "b1-nemzetijelkepek-consolidation.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyek Magyarország hivatalos nemzeti jelképei az Alaptörvény szerint?",
                "options": [
                    "A címer, a zászló és a Himnusz.",
                    "A Parlament, a Lánchíd és a Halászbástya.",
                    "A gulyásleves, a tokaji bor és a paprika."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex02",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "A Himnuszt Kölcsey Ferenc írta, a Szózatot pedig Vörösmarty Mihály költöt_____. (composed - te)",
                "answer": "te"
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "Szent", "Korona", "a", "magyar", "államiság", "legősibb", "jelképe."],
                "solution": ["A", "Szent", "Korona", "a", "magyar", "államiság", "legősibb", "jelképe."]
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Miért kiemelkedő jelentőségű a Szent Korona a magyar jogtörténetben?",
                "options": [
                    "Mert a Szent Korona-tan szerint a korona a főhatalom és az állam egységének forrása.",
                    "Mert aranyból és gyémántból készült.",
                    "Mert csak egyetlen király viselte valaha."
                ],
                "correct": 0
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemzeti lobogó piros-fehér-zöld színeit a törvény pontosan meghatároz_____. (defines - za)",
                "answer": "za"
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "kultúra", "napját", "január", "22-én", "ünnepeljük."],
                "solution": ["A", "magyar", "kultúra", "napját", "január", "22-én", "ünnepeljük."]
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex07",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "A címerben látható négy ezüst sáv a Duna, Tisza, Dráva és Száva folyókat jelképez_____. (symbolizes - i)",
                "answer": "i"
            },
            {
                "id": "b1-nemzetijelkepek-consolidation.ex08",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mire tesz esküt az állampolgárságot szerző polgár a honosítási szertartáson?",
                "options": [
                    "Hogy Magyarországot hazájának tekinti, Alaptörvényét és jogszabályait betartja, és a hazát erejéhez mérten szolgálja.",
                    "Hogy minden évben elutazik a Balatonra.",
                    "Hogy csak magyar zenét fog hallgatni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-nemzetijelkepek-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A magyar zászló és a nemzeti színek", "The National Flag & Colors"),
        "02": ("A Szent Korona és a koronázási jelvények", "The Holy Crown & Coronation Regalia"),
        "03": ("Magyarország címere és szimbólumai", "The National Coat of Arms"),
        "04": ("A Nemzeti Himnusz: Kölcsey és Erkel műve", "The National Anthem (Himnusz)"),
        "05": ("A Szózat: Vörösmarty hűségfogadalma", "The Szózat (The Appeal)")
    }

    story_refs = {
        "01": "stories/world/b1/b1-nemzetijelkepek-01-zaszlo.json",
        "02": "stories/world/b1/b1-nemzetijelkepek-02-szentkorona.json",
        "03": "stories/world/b1/b1-nemzetijelkepek-03-cimer.json",
        "04": "stories/world/b1/b1-nemzetijelkepek-04-himnusz.json",
        "05": "stories/world/b1/b1-nemzetijelkepek-05-szozat.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.nemzetijelkepek-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Heraldic Symbolism, Constitutional Metaphors & Solemn Hymnic Registers",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and explain {en_t} in Hungarian.",
                        "I can use heraldic, symbolic, and reverent Hungarian vocabulary.",
                        "I can answer essential citizenship exam questions regarding the flag, coat of arms, Holy Crown, Himnusz, and Szózat.",
                        "I can master six target vocabulary items in authentic civic and cultural context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-nemzetijelkepek-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-nemzetijelkepek-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-nemzetijelkepek-{padded}-ex.json",
                    "exerciseRefs": [f"b1-nemzetijelkepek-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-nemzetijelkepek-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.nemzetijelkepek-consolidation",
        "title": "Összefoglalás: Nemzeti jelképek (National Symbols Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of National Symbols, Heraldic Heritage & Reverent Civic Identity",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-nemzetijelkepek.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-nemzetijelkepek-consolidation-ex.json",
                "exerciseRefs": [f"b1-nemzetijelkepek-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-nemzetijelkepek-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 29 (b1-nemzetijelkepek)!")

if __name__ == "__main__":
    build_unit_29_citizenship()
