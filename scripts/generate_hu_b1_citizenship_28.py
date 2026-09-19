#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 28: Modern Democratic Hungary & Euro-Atlantic Integration (b1-demokracia)."""

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

def build_unit_28_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.demokracia.01",
        "lesson": "b1-demokracia-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Alaptörvény", "translation": "Fundamental Law of Hungary (constitutional supreme legal code)", "pos": "noun"},
            {"lemma": "jogállamiság", "translation": "rule of law (governance based on legal certainty and equal justice)", "pos": "noun"},
            {"lemma": "hatalommegosztás", "translation": "separation of powers (legislative, executive, and judicial branches)", "pos": "noun"},
            {"lemma": "Alkotmánybíróság", "translation": "Constitutional Court (guardian of constitutional conformity)", "pos": "noun"},
            {"lemma": "alapvető jogok", "translation": "fundamental human and civil rights guaranteed by law", "pos": "noun"},
            {"lemma": "független igazságszolgáltatás", "translation": "independent judiciary and court system", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-demokracia-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.demokracia.02",
        "lesson": "b1-demokracia-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Országgyűlés", "translation": "National Assembly (Hungary's unicameral 199-member parliament)", "pos": "noun"},
            {"lemma": "köztársasági elnök", "translation": "President of the Republic (head of state expressing national unity)", "pos": "noun"},
            {"lemma": "miniszterelnök", "translation": "Prime Minister (head of government leading the executive)", "pos": "noun"},
            {"lemma": "helyi önkormányzat", "translation": "local municipal self-government managing communities", "pos": "noun"},
            {"lemma": "népszavazás", "translation": "popular referendum (direct democratic expression of sovereign will)", "pos": "noun"},
            {"lemma": "parlamenti képviselő", "translation": "Member of Parliament elected for a four-year mandate", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-demokracia-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.demokracia.03",
        "lesson": "b1-demokracia-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "NATO-csatlakozás", "translation": "accession to NATO (March 12, 1999, securing national defense)", "pos": "noun"},
            {"lemma": "kollektív védelem", "translation": "collective defense under Article 5 (an attack on one is an attack on all)", "pos": "noun"},
            {"lemma": "Észak-atlanti Szerződés", "translation": "North Atlantic Treaty guaranteeing democratic transatlantic security", "pos": "noun"},
            {"lemma": "szövetségi hűség", "translation": "fidelity to alliance commitments and partners", "pos": "noun"},
            {"lemma": "nemzetközi békemisszió", "translation": "international peacekeeping mission of Hungarian soldiers", "pos": "noun"},
            {"lemma": "Magyar Honvédség", "translation": "Hungarian Defense Forces safeguarding national sovereignty", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-demokracia-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.demokracia.04",
        "lesson": "b1-demokracia-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Európai Uniós csatlakozás", "translation": "accession to the European Union (May 1, 2004)", "pos": "noun"},
            {"lemma": "schengeni övezet", "translation": "Schengen area (borderless travel zone entered in December 2007)", "pos": "noun"},
            {"lemma": "négy szabadságjog", "translation": "four EU freedoms: free movement of goods, capital, services, and persons", "pos": "noun"},
            {"lemma": "európai integráció", "translation": "European integration and peaceful partnership of sovereign nations", "pos": "noun"},
            {"lemma": "határok nélküli Európa", "translation": "borderless Europe enabling unhindered contact across borders", "pos": "expression"},
            {"lemma": "uniós források", "translation": "European Union development funds modernizing infrastructure", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-demokracia-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.demokracia.05",
        "lesson": "b1-demokracia-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "határon túli magyarság", "translation": "Hungarians living across national borders in the Carpathian Basin", "pos": "noun"},
            {"lemma": "nemzetpolitika", "translation": "national policy supporting Hungarian identity and heritage abroad", "pos": "noun"},
            {"lemma": "kettős állampolgárság", "translation": "dual citizenship for ethnic Hungarians across the borders", "pos": "noun"},
            {"lemma": "egyszerűsített honosítás", "translation": "simplified naturalization process established in 2010", "pos": "noun"},
            {"lemma": "Nemzeti Összetartozás Napja", "translation": "Day of National Cohesion (commemorated annually on June 4th)", "pos": "noun"},
            {"lemma": "Kárpát-medence", "translation": "Carpathian Basin (shared geographic and cultural sphere of Hungarians)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-demokracia-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.demokracia.01.constitutional-principles",
        "title": "Constitutional Guarantees: biztosítja az alapjogokat, nyugszik",
        "sections": [
            {
                "type": "text",
                "title": "Constitutional Syntax and Prepositional Verbs",
                "content": "Constitutional discourse in Hungarian employs specific governing structures: *Magyarország Alaptörvénye rögzíti/biztosítja...* ('The Fundamental Law enshrines/guarantees...'), *a hatalommegosztás elvén nyugszik* ('rests on the principle of the separation of powers' - superessive *-on/-en/-ön*)."
            },
            {
                "type": "examples",
                "title": "Constitutional examples",
                "items": [
                    {
                        "spanish": "Az Alaptörvény biztosítja minden ember sérthetetlen és elidegeníthetetlen alapvető jogait.",
                        "english": "The Fundamental Law guarantees the inviolable and inalienable fundamental rights of every person."
                    },
                    {
                        "spanish": "A demokratikus jogállam a törvények uralmán és a hatalmi ágak szétválasztásán nyugszik.",
                        "english": "The democratic state governed by the rule of law rests on the rule of laws and the separation of powers."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-demokracia-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.demokracia.02.state-institutional-roles",
        "title": "Institutional Mandates and Functions: feladata, hatásköre, felelős",
        "sections": [
            {
                "type": "text",
                "title": "Describing Powers of State Bodies",
                "content": "*A köztársasági elnök kifejezi a nemzet egységét* ('The President of the Republic expresses the unity of the nation'), *az Országgyűlés törvényeket alkot* ('The National Assembly creates laws'), *a Kormány felelős az Országgyűlésnek* ('The Government is accountable to the National Assembly' - dative *-nak/-nek*)."
            },
            {
                "type": "examples",
                "title": "State function examples",
                "items": [
                    {
                        "spanish": "Az Országgyűlés a legfőbb népképviseleti és törvényhozó szerv Magyarországon.",
                        "english": "The National Assembly is the supreme organ of popular representation and legislation in Hungary."
                    },
                    {
                        "spanish": "A miniszterelnököt az Országgyűlés választja meg a köztársasági elnök javaslatára.",
                        "english": "The Prime Minister is elected by the National Assembly upon the proposal of the President of the Republic."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-demokracia-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.demokracia.03.treaty-commitments",
        "title": "Alliance Commitments: kollektív védelem, kötelezettséget vállal",
        "sections": [
            {
                "type": "text",
                "title": "International Security Grammar",
                "content": "*Csatlakozik a szövetséghez* ('joins the alliance' - allative *-hoz/-hez/-höz*), *garantálja a biztonságot* ('guarantees security'), *kötelezettséget vállal a kollektív védelemre* ('undertakes commitment to collective defense' - sublative *-ra/-re*)."
            },
            {
                "type": "examples",
                "title": "NATO alliance examples",
                "items": [
                    {
                        "spanish": "1999. március 12-én Magyarország hivatalosan a NATO teljes jogú tagjává vált.",
                        "english": "On March 12, 1999, Hungary officially became a full member of NATO."
                    },
                    {
                        "spanish": "A kollektív védelem elve alapján egy tagállam megtámadása az egész szövetség elleni támadásnak minősül.",
                        "english": "Under the principle of collective defense, an attack on one member state qualifies as an attack on the entire alliance."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-demokracia-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.demokracia.04.supranational-integration",
        "title": "European Integration & Free Movement: jogot biztosít, csatlakozik",
        "sections": [
            {
                "type": "text",
                "title": "Phrasing Transnational Rights and Freedoms",
                "content": "*Szabadon utazhat és munkát vállalhat* ('can travel and work freely'), *része a schengeni övezetnek* ('is part of the Schengen zone'), *hozzájárul a fejlődéshez* ('contributes to development' - allative *-hoz/-hez/-höz*)."
            },
            {
                "type": "examples",
                "title": "EU integration examples",
                "items": [
                    {
                        "spanish": "2004. május 1-jén Magyarország kilenc másik országgal együtt csatlakozott az Európai Unióhoz.",
                        "english": "On May 1, 2004, Hungary joined the European Union together with nine other countries."
                    },
                    {
                        "spanish": "A schengeni övezethez való csatlakozás megszüntette a belső határellenőrzést a szomszédos uniós államok felé.",
                        "english": "Accession to the Schengen zone eliminated internal border controls toward neighboring EU states."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-demokracia-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.demokracia.05.kin-state-responsibility",
        "title": "Kin-State Responsibility: felelősséget visel, támogatja a megmaradást",
        "sections": [
            {
                "type": "text",
                "title": "Constitutional Care for Cross-Border Hungarians",
                "content": "Article D of Hungary's Fundamental Law states: *'Magyarország az egységes magyar nemzet eszméjétől vezérelve felelősséget visel a határain kívül élő magyarok sorsáért...'* Governed by *felelősséget visel vmiért* and *támogatja a szülőföldön való boldogulást*."
            },
            {
                "type": "examples",
                "title": "National cohesion examples",
                "items": [
                    {
                        "spanish": "Magyarország támogatja a határon túli magyar közösségek identitásának megőrzését és anyanyelvi kultúráját.",
                        "english": "Hungary supports the preservation of identity and mother-tongue culture of Hungarian communities across borders."
                    },
                    {
                        "spanish": "Az egyszerűsített honosítás révén több mint egymillió határon túli magyar szerzett magyar állampolgárságot.",
                        "english": "Through simplified naturalization, over one million cross-border Hungarians acquired Hungarian citizenship."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-demokracia-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Story Files (5 regular lesson stories + 1 combined omnibus story)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.demokracia.01",
        "lesson": 1,
        "order": 1,
        "title": "Az alkotmányos rend és a jogállamiság fundamentuma",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Modern Hungary is a democratic state governed by the rule of law. The Fundamental Law (Alaptörvény) guarantees fundamental human rights and establishes the separation of powers between legislative, executive, and judicial branches. The Constitutional Court and the independent judiciary ensure that state authority never exceeds its lawful limits, protecting citizens' freedom.",
        "characters": [
            "Alkotmánybíróság bírája",
            "Fiatal ügyvéd Budapesten",
            "Alapvető jogok biztosa"
        ],
        "location": "Budapest, az Alkotmánybíróság Donáti utcai épülete és a Kúria",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A modern Magyarország demokratikus jogállam. Az állami működés legfőbb zsinórmértéke Magyarország Alaptörvénye, amely a nemzeti örökségre és az egyetemes emberi jogokra épül."
            },
            {
                "type": "dialogue",
                "speaker": "Alkotmánybíróság bírája",
                "text": "A demokrácia lényege a hatalommegosztás. Egyetlen személy vagy intézmény sem gyakorolhatja a hatalmat ellenőrizetlenül! A törvényhozás, a végrehajtó hatalom és a független bíróságok egymást ellensúlyozzák."
            },
            {
                "type": "narration",
                "text": "Az Alkotmánybíróság feladata, hogy megvizsgálja a parlament által hozott törvényeket: amennyiben bármelyik jogszabály sérti az Alaptörvényt és a polgárok alapjogait, a testület megsemmisíti azt."
            },
            {
                "type": "dialogue",
                "speaker": "Alapvető jogok biztosa (ombudsman)",
                "text": "A hivatalunkhoz bármelyik polgár fordulhat, ha úgy érzi, hogy a hatóságok megsértették alapvető emberi jogait, a szólásszabadságot, a vallásszabadságot vagy a méltóságát."
            },
            {
                "type": "narration",
                "text": "A független bíróságok és a jogállami garanciák biztosítják, hogy a magyar állampolgárok biztonságban, a jog védelme alatt élhessenek hazájukban."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia-01-alkotmany.json", story_01)

    story_02 = {
        "id": "story.b1.demokracia.02",
        "lesson": 2,
        "order": 2,
        "title": "A magyar államszervezet és a parlamentáris demokrácia",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary's political system is a parliamentary representative democracy. The 199 Members of the National Assembly are elected every four years. The President of the Republic in the Sándor Palace acts as head of state, symbolizing the nation's unity, while the Prime Minister leads the executive Government, accountable to Parliament. Local municipalities govern towns and villages.",
        "characters": [
            "Parlamenti képviselő az Országházban",
            "Falusi polgármester a Dunakanyarban",
            "Köztársasági elnök protokollfőnöke"
        ],
        "location": "Budapest, Országház, a budavári Sándor-palota és egy Pest vármegyei községháza",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar parlamentáris demokrácia szíve az Országház, Steindl Imre neogótikus mesterműve a Duna partján. Itt ülésezik a 199 országgyűlési képviselő, akiket a nép választ meg négy évre szabad, titkos és közvetlen választásokon."
            },
            {
                "type": "dialogue",
                "speaker": "Országgyűlési képviselő",
                "text": "Az Országgyűlés vitatja meg a törvényjavaslatokat, elfogadja az állami költségvetést, és megválasztja a miniszterelnököt. A kormány minden lépéséért felelősséggel tartozik a választott parlamentnek!"
            },
            {
                "type": "narration",
                "text": "Az államfő a köztársasági elnök, akinek székhelye a budavári Sándor-palota. Ő fejezi ki a nemzet egységét, őrködik az államszervezet demokratikus működése felett, és képviseli Magyarországot nemzetközi szinten."
            },
            {
                "type": "dialogue",
                "speaker": "Falusi polgármester",
                "text": "A helyi önkormányzatok a demokrácia közvetlen pillérei. Mi magunk döntünk az iskolákról, az óvodákról, a helyi utakról és a faluközösség kulturális életéről a helyi polgárok bevonásával."
            },
            {
                "type": "narration",
                "text": "A közvetlen demokrácia legfontosabb eszköze az országos népszavazás, amellyel a választópolgárok a leglényegesebb sorskérdésekben közvetlenül fejezhetik ki akaratukat."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia-02-allamszervezet.json", story_02)

    story_03 = {
        "id": "story.b1.demokracia.03",
        "lesson": 3,
        "order": 3,
        "title": "A NATO-csatlakozás (1999) és Magyarország biztonsága",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Following an overwhelming 85% majority in the November 1997 referendum, Hungary officially joined the North Atlantic Treaty Organization (NATO) on March 12, 1999 in Independence, Missouri, alongside Poland and the Czech Republic. Article 5 of the Washington Treaty guaranteed collective defense, integrating Hungary into the democratic transatlantic security community.",
        "characters": [
            "Martonyi János külügyminiszter",
            "Magyar Honvédség vadászpilótája Kecskeméten",
            "Taszári bázisparancsnok"
        ],
        "location": "Independence (Missouri), Kecskeméti légibázis és Taszár",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A vasfüggöny leomlása után Magyarország legfőbb biztonságpolitikai célja az észak-atlanti szövetséghez való csatlakozás volt. Az 1997-es népszavazáson a magyar választók 85 százaléka mondott igent a NATO-tagságra."
            },
            {
                "type": "dialogue",
                "speaker": "Martonyi János külügyminiszter (1999. március 12-én)",
                "text": "Magyarország végleg visszatért természetes szövetségesei közé! A NATO nem pusztán katonai szövetség, hanem a szabadság, a demokrácia és a közös nyugati értékek védőbástyája!"
            },
            {
                "type": "narration",
                "text": "A csatlakozási okmányok letétbe helyezésével a washingtoni szerződés híres 5. cikkelye Magyarország védelmét is szavatolta: a kollektív védelem elve értelmében bármely tagállam megtámadása valamennyi szövetséges elleni agressziónak minősül."
            },
            {
                "type": "dialogue",
                "speaker": "Kecskeméti Gripen-pilóta",
                "text": "Ma már a Magyar Honvédség korszerű vadászgépei védik Magyarország és a szomszédos szövetségesek légterét, katonáink pedig a békét védik a világ számos pontján, a Balkántól a Közel-Keletig."
            },
            {
                "type": "narration",
                "text": "A NATO-tagság évszázadok óta nem látott szilárd biztonsági garanciát nyújtott a magyar nemzet számára, megelőzve a háborús konfliktusokat a térségben."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia-03-nato.json", story_03)

    story_04 = {
        "id": "story.b1.demokracia.04",
        "lesson": 4,
        "order": 4,
        "title": "Csatlakozás az Európai Unióhoz (2004) és a schengeni határok",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On May 1, 2004, Hungary fulfilled a historic ambition by officially joining the European Union. At Budapest's City Park, the massive Time Wheel turned to mark the historic hour. Accession brought the four EU freedoms—free movement of goods, services, capital, and persons. In December 2007, joining the Schengen Area physically erased the border barriers separating Hungarians from Austria and Slovakia.",
        "characters": [
            "Medgyessy Péter miniszterelnök",
            "Magyar egyetemi hallgató Erasmus-ösztöndíjjal",
            "Északi határmenti gazdálkodó Ipolyságnál"
        ],
        "location": "Budapest, Városliget (Időkerék) és a szlovák-magyar határ az Ipoly partján",
        "paragraphs": [
            {
                "type": "narration",
                "text": "2004. május 1-jének éjjelén a budapesti Hősök tere mellett megfordították a világ legnagyobb Időkerekét: Magyarország kilenc másik közép- és kelet-európai állammal együtt az Európai Unió tagjává vált."
            },
            {
                "type": "dialogue",
                "speaker": "Medgyessy Péter miniszterelnök",
                "text": "István király ezer évvel ezelőtt Európához kapcsolta nemzetünket. Ma ez a kapocs végleg megerősödött: teljes jogú tagként veszünk részt az egységesülő Európa építésében!"
            },
            {
                "type": "narration",
                "text": "Az uniós csatlakozás megnyitotta a négy szabadságjogot: a magyar polgárok szabadon utazhatnak, tanulhatnak és vállalhatnak munkát az unió országaiban, az egyetemeket összeköti az Erasmus-program, a gazdaság fejlesztését pedig uniós források segítik."
            },
            {
                "type": "dialogue",
                "speaker": "Ipoly menti gazdálkodó (2007 decembere)",
                "text": "Amikor beléptünk a schengeni övezetbe, felnyitották a sorompókat a szlovák határon! Nyolcvan év után újra megállás nélkül látogathatjuk meg a túlparton élő felvidéki rokonainkat!"
            },
            {
                "type": "narration",
                "text": "A schengeni határok lebontása révén a történelmi határok elválasztó jellege megszűnt: a Kárpát-medencei magyarok újra akadálytalanul találkozhatnak egymással a közös európai térben."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia-04-eu.json", story_04)

    story_05 = {
        "id": "story.b1.demokracia.05",
        "lesson": 5,
        "order": 5,
        "title": "A nemzetpolitika és a határon túli magyarság összetartozása",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The 1920 Trianon Treaty severed one-third of ethnic Hungarians into neighboring states. Under the Fundamental Law, the Hungarian state bears constitutional responsibility for cross-border communities in Transylvania, Upper Hungary, Vojvodina, and Transcarpathia. The 2010 simplified naturalization law enabled over one million kin-state Hungarians to regain citizenship, while June 4th was proclaimed the Day of National Cohesion.",
        "characters": [
            "Kolozsvári erdélyi magyar egyetemi tanár",
            "Szabadkai vajdasági középiskolás",
            "Budapesti nemzetpolitikai államtitkár"
        ],
        "location": "Kolozsvár, Szabadka, a Parlament Főrendiházi terme és a Nemzeti Összetartozás Emlékhelye",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar nemzet határai nem esnek egybe a Magyar Állam határaival: a szomszédos országokban – Erdélyben, a Felvidéken, a Vajdaságban és Kárpátalján – több millió magyar él őshonos közösségekben."
            },
            {
                "type": "dialogue",
                "speaker": "Nemzetpolitikai államtitkár",
                "text": "Az Alaptörvény kimondja: Magyarország felelősséget visel a határain kívül élő magyarok sorsáért! Támogatjuk az anyanyelvi iskolákat, a magyar kultúrát és a gazdasági talpra állást, hogy mindenki a szülőföldjén maradhasson meg magyarként!"
            },
            {
                "type": "narration",
                "text": "2010-ben az Országgyűlés elsöprő többséggel elfogadta az egyszerűsített honosítási törvényt. Ennek révén több mint egymillió határon túli magyar testvérünk vehette fel a magyar állampolgárságot, visszakapva közjogi kapcsolatát az anyaországgal."
            },
            {
                "type": "dialogue",
                "speaker": "Kolozsvári tanár",
                "text": "Amikor letettem az állampolgársági esküt, a nagyapámra gondoltam. Nem elköltözni akarunk Erdélyből, hanem itt, szülőföldünkön akarunk emelt fővel élni a magyar nemzet megbecsült tagjaiként!"
            },
            {
                "type": "narration",
                "text": "Június 4-e a Nemzeti Összetartozás Napja: a trianoni békediktátum gyásza helyett a megmaradás, a nemzeti szolidaritás és a határokon átívelő egység ünnepévé emelkedett."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia-05-nemzetpolitika.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.demokracia.combined",
        "title": "A modern demokratikus Magyarország és az euroatlanti integráció",
        "level": "B1",
        "order": 28,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "A comprehensive panoramic chronicle of modern democratic Hungary. From the constitutional framework of the rule of law, the separation of powers, and the Fundamental Law; the institutional workings of the National Assembly, the President of the Republic, and local self-governments; the historic security guarantee of NATO accession in 1999; EU membership in 2004 and the Schengen borderless zone in 2007; to modern kin-state policy supporting cross-border Hungarians through dual citizenship and national cohesion.",
        "characters": [
            "Köztársasági elnök",
            "Országgyűlési képviselő",
            "Határon túli magyar tanár",
            "NATO-tiszt"
        ],
        "location": "Budapest, Országház, Sándor-palota és a Kárpát-medence",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A rendszerváltoztatás óta eltelt évtizedekben Magyarország a modern demokratikus jogállam szilárd alapjaira építette újjá államiságát. Az Alaptörvényben rögzített hatalommegosztás elve biztosítja, hogy a törvényhozás, a végrehajtás és a független igazságszolgáltatás a polgárok szabadságát szolgálja."
            },
            {
                "type": "narration",
                "text": "Az 1999-es NATO-csatlakozással és a 2004-es Európai Uniós tagsággal Magyarország visszatért természetes civilizációs otthonába, a szabad nyugati nemzetek közösségébe. A schengeni övezethez való csatlakozás megnyitotta a határokat, lehetővé téve az emberek és eszmék szabad áramlását."
            },
            {
                "type": "narration",
                "text": "A modern magyar állam kiemelt alkotmányos felelősséget visel a Kárpát-medencében és a diaszpórában élő határon túli magyarságért. Az egyszerűsített honosítás és a kettős állampolgárság révén több mint egymillió határon túli testvérünk vált újra a nemzet közjogi tagjává."
            },
            {
                "type": "narration",
                "text": "Magyarország ma szuverén, demokratikus nemzetállamként, szilárd szövetségi rendszerek részeként és a Kárpát-medencei magyarság felelős anyaországaként tekint a 21. század jövőjébe."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-demokracia.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-demokracia-01",
        "exercises": [
            {
                "id": "b1-demokracia-01.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mi Magyarország legfelsőbb szintű, alkotmányos jogi alapdokumentuma?",
                "options": [
                    "Magyarország Alaptörvénye.",
                    "A Polgári Törvénykönyv.",
                    "A Közlekedési Szabályzat."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A demokratikus állam a hatalommegosztás elvén nyug_____. (rests on - szik)",
                "answer": "szik"
            },
            {
                "id": "b1-demokracia-01.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "Alkotmánybíróság", "őrködik", "a", "jogszabályok", "alkotmányossága", "felett."],
                "solution": ["Az", "Alkotmánybíróság", "őrködik", "a", "jogszabályok", "alkotmányossága", "felett."]
            },
            {
                "id": "b1-demokracia-01.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Mely három hatalmi ágra oszlik a modern államhatalom a jogállamiság elve szerint?",
                "options": [
                    "A törvényhozó, a végrehajtó és az igazságszolgáltató hatalomra.",
                    "A bankokra, az iskolákra és a kórházakra.",
                    "A rendőrségre, a tűzoltóságra és a mentőkre."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az Alaptörvény rögzíti az állampolgárok elidegeníthetetlen alapjogai_____. (their rights - t)",
                "answer": "t"
            },
            {
                "id": "b1-demokracia-01.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi az alapvető jogok biztosának (ombudsman) legfőbb feladata?",
                "options": [
                    "A polgárok alapvető jogainak védelme a hatóságok esetleges jogsértéseivel szemben.",
                    "A költségvetési adók beszedése.",
                    "A parlamenti ülések levezetése."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bírák függetlenek, és kizárólag a törvényeknek vannak alárendel_____. (subordinated - ve)",
                "answer": "ve"
            },
            {
                "id": "b1-demokracia-01.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Magyarország", "független", "és", "demokratikus", "jogállam."],
                "solution": ["Magyarország", "független", "és", "demokratikus", "jogállam."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-demokracia-02",
        "exercises": [
            {
                "id": "b1-demokracia-02.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hány képviselőből áll a magyar Országgyűlés?",
                "options": [
                    "199 országgyűlési képviselőből.",
                    "386 képviselőből.",
                    "100 képviselőből."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársasági elnök kifejezi a nemzet egység_____. (its unity - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-demokracia-02.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kormány", "felelősséggel", "tartozik", "az", "Országgyűlésnek."],
                "solution": ["A", "kormány", "felelősséggel", "tartozik", "az", "Országgyűlésnek."]
            },
            {
                "id": "b1-demokracia-02.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Hol található a köztársasági elnök hivatalos székhelye?",
                "options": [
                    "A budavári Sándor-palotában.",
                    "A Parlament kupolatermében.",
                    "A debreceni Nagytemplomban."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A választópolgárok országos népszavazás útján közvetlenül fejezhetik ki akaratu_____. (their will - kat)",
                "answer": "kat"
            },
            {
                "id": "b1-demokracia-02.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen időközönként tartanak parlamenti választásokat Magyarországon?",
                "options": [
                    "Négyévente.",
                    "Minden évben.",
                    "Hétévente."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A miniszterelnököt az Országgyűlés választja meg a köztársasági elnök javaslatá_____. (upon his proposal - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-demokracia-02.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "helyi", "önkormányzatok", "önállóan", "irányítják", "a", "településeket."],
                "solution": ["A", "helyi", "önkormányzatok", "önállóan", "irányítják", "a", "településeket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-demokracia-03",
        "exercises": [
            {
                "id": "b1-demokracia-03.ex01",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik évben csatlakozott Magyarország hivatalosan a NATO-hoz?",
                "options": [
                    "1999-ben.",
                    "1990-ben.",
                    "2010-ben."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1999. március 12-én Magyarország a NATO teljes jogú tagjává vál_____. (became - t)",
                "answer": "t"
            },
            {
                "id": "b1-demokracia-03.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kollektív", "védelem", "garantálja", "hazánk", "katonai", "biztonságát."],
                "solution": ["A", "kollektív", "védelem", "garantálja", "hazánk", "katonai", "biztonságát."]
            },
            {
                "id": "b1-demokracia-03.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mit mond ki a NATO washingtoni szerződésének 5. cikkelye?",
                "options": [
                    "Egyetlen szövetséges megtámadása valamennyi tagállam elleni támadásnak minősül (kollektív védelem).",
                    "Minden tagnak kötelező azonos egyenruhát viselnie.",
                    "A tagállamoknak fel kell oszlatniuk a nemzeti hadseregüket."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Magyar Honvédség aktívan részt vesz a nemzetközi békemissziók_____. (inessive - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-demokracia-03.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan döntött a magyar lakosság a NATO-csatlakozásról az 1997-es népszavazáson?",
                "options": [
                    "Elsöprő, mintegy 85 százalékos többséggel támogatta a csatlakozást.",
                    "A szavazók többsége elutasította a tagságot.",
                    "A népszavazás érvénytelen volt a csekély részvétel miatt."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szövetségesi hűség alapvető érték az Észak-atlanti Szerződés_____. (inessive - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-demokracia-03.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "NATO-tagság", "megvédi", "Magyarországot", "a", "külső", "támadásoktól."],
                "solution": ["A", "NATO-tagság", "megvédi", "Magyarországot", "a", "külső", "támadásoktól."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-demokracia-04",
        "exercises": [
            {
                "id": "b1-demokracia-04.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik napon csatlakozott Magyarország az Európai Unióhoz?",
                "options": [
                    "2004. május 1-jén.",
                    "1999. március 12-én.",
                    "2011. január 1-jén."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "2004-ben Magyarország az Európai Unió tagjává vál_____. (became - t)",
                "answer": "t"
            },
            {
                "id": "b1-demokracia-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "schengeni", "övezet", "biztosítja", "a", "határok", "nélküli", "szabad", "utazást."],
                "solution": ["A", "schengeni", "övezet", "biztosítja", "a", "határok", "nélküli", "szabad", "utazást."]
            },
            {
                "id": "b1-demokracia-04.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Melyek az Európai Unió belső piacának úgynevezett 'négy szabadságjoga'?",
                "options": [
                    "Az áruk, a személyek, a szolgáltatások és a tőke szabad áramlása.",
                    "A halászat, a bányászat, a repülés és a hajózás szabadsága.",
                    "A négynapos munkahét és a szabad hétvége."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az uniós források nagymértékben hozzájárulnak az infrastruktúra fejlesztésé_____. (allative - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-demokracia-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen közvetlen előnyt jelentett a határon élők számára a 2007-es schengeni csatlakozás?",
                "options": [
                    "Megszűnt az állandó határellenőrzés a szomszédos Ausztria és Szlovákia felé.",
                    "Ingyen vonatjegyet kapott minden utas.",
                    "A határon kötelezővé tették a vízumváltást."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar diákok az Erasmus-program révén külföldi egyetemeken tanulhat_____. (can study - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-demokracia-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "európai", "integráció", "békét", "és", "gazdasági", "fejlődést", "teremtett."],
                "solution": ["Az", "európai", "integráció", "békét", "és", "gazdasági", "fejlődést", "teremtett."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-demokracia-05",
        "exercises": [
            {
                "id": "b1-demokracia-05.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Melyik napot nyilvánította a parlament a Nemzeti Összetartozás Napjává?",
                "options": [
                    "Június 4-ét (a trianoni békediktátum aláírásának napját).",
                    "Március 15-ét.",
                    "Október 23-át."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Magyarország felelősséget visel a határain kívül élő magyarok sorsá_____. (for their fate - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-demokracia-05.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "egyszerűsített", "honosítás", "lehetővé", "tette", "a", "kettős", "állampolgárságot."],
                "solution": ["Az", "egyszerűsített", "honosítás", "lehetővé", "tette", "a", "kettős", "állampolgárságot."]
            },
            {
                "id": "b1-demokracia-05.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Hány határon túli magyar szerezte meg a magyar állampolgárságot a 2010-es egyszerűsített honosítási törvény révén?",
                "options": [
                    "Több mint egymillió határon túli magyar ember.",
                    "Alig néhány ezer ember.",
                    "Tízmillió külföldi állampolgár."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Kárpát-medencei nemzetpolitika támogatja a szülőföldön való megmaradás_____. (its remaining - t)",
                "answer": "t"
            },
            {
                "id": "b1-demokracia-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi a legfontosabb célja a magyar nemzetpolitikának a szomszédos országokban?",
                "options": [
                    "Az őshonos magyar közösségek anyanyelvének, oktatásának, gazdaságának és identitásának megőrzése szülőföldjükön.",
                    "A határon túli magyarok azonnali áttelepítése Budapestre.",
                    "A határok katonai erőszakkal való megváltoztatása."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Bethlen Gábor Alap támogatásokat nyújt az anyanyelvi kultúra ápolásá_____. (allative - hoz)",
                "answer": "hoz"
            },
            {
                "id": "b1-demokracia-05.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "nemzet", "határokon", "átívelő", "lelki", "és", "kulturális", "közösség."],
                "solution": ["A", "magyar", "nemzet", "határokon", "átívelő", "lelki", "és", "kulturális", "közösség."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-demokracia-consolidation",
        "exercises": [
            {
                "id": "b1-demokracia-consolidation.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Milyen államforma Magyarország a hatályos Alaptörvény szerint?",
                "options": [
                    "Független, demokratikus jogállam és köztársaság.",
                    "Alkotmányos monarchia.",
                    "Népköztársaság."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-consolidation.ex02",
                "type": "fill-blank",
                "category": "history",
                "sentence": "Magyarország 1999-ben lépett be a NATO-ba, és 2004-ben az Európai Unió_____. (illative - ba)",
                "answer": "ba"
            },
            {
                "id": "b1-demokracia-consolidation.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "Alaptörvény", "a", "magyar", "jogrendszer", "legmagasabb", "szintű", "fundamentuma."],
                "solution": ["Az", "Alaptörvény", "a", "magyar", "jogrendszer", "legmagasabb", "szintű", "fundamentuma."]
            },
            {
                "id": "b1-demokracia-consolidation.ex04",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Kik jogosultak egyszerűsített honosítással magyar állampolgárságot kérelmezni?",
                "options": [
                    "Azok a határon túli vagy diaszpórában élő személyek, akiknek felmenője magyar állampolgár volt, és igazolják magyar nyelvtudásukat.",
                    "Bárki a világon, aki Magyarországon vásárol repülőjegyet.",
                    "Kizárólag a profi sportolók."
                ],
                "correct": 0
            },
            {
                "id": "b1-demokracia-consolidation.ex05",
                "type": "fill-blank",
                "category": "law",
                "sentence": "A hatalommegosztás elve biztosítja a fékek és egyensúlyok rendszer_____. (its system - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-demokracia-consolidation.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "schengeni", "övezetben", "szabadon", "járhatunk", "át", "a", "határokon."],
                "solution": ["A", "schengeni", "övezetben", "szabadon", "járhatunk", "át", "a", "határokon."]
            },
            {
                "id": "b1-demokracia-consolidation.ex07",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "Június 4-e a Nemzeti Összetartozás Nap_____. (its day - ja)",
                "answer": "ja"
            },
            {
                "id": "b1-demokracia-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért alapvető fontosságú Magyarország számára az euroatlanti integráció?",
                "options": [
                    "Mert garantálja az ország katonai biztonságát (NATO) és biztosítja gazdasági, társadalmi és emberi jogi fejlődését (EU).",
                    "Mert kötelezővé tette az angol nyelv kizárólagos használatát.",
                    "Mert megszüntette a magyar nemzeti szimbólumokat."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-demokracia-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Az alkotmányos rend és a jogállamiság", "Constitutional Order & Rule of Law"),
        "02": ("A parlamentáris demokrácia és az államszervezet", "State Structure & Parliamentary Democracy"),
        "03": ("A NATO-csatlakozás és hazánk biztonsága", "NATO Accession & Collective Defense"),
        "04": ("Csatlakozás az Európai Unióhoz és a Schengeni övezethez", "EU Accession & the Schengen Borderless Zone"),
        "05": ("Nemzetpolitika és a határon túli magyarság", "Kin-State Policy & Cross-Border Hungarians")
    }

    story_refs = {
        "01": "stories/world/b1/b1-demokracia-01-alkotmany.json",
        "02": "stories/world/b1/b1-demokracia-02-allamszervezet.json",
        "03": "stories/world/b1/b1-demokracia-03-nato.json",
        "04": "stories/world/b1/b1-demokracia-04-eu.json",
        "05": "stories/world/b1/b1-demokracia-05-nemzetpolitika.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.demokracia-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Constitutional Guarantees, Supranational Integration & Kin-State Registers in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in modern Hungary.",
                        "I can use constitutional, institutional, and civic vocabulary in Hungarian.",
                        "I can answer essential citizenship exam questions regarding the Fundamental Law, NATO, the EU, and national cohesion.",
                        "I can master six target vocabulary items in authentic civic and historical context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-demokracia-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-demokracia-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-demokracia-{padded}-ex.json",
                    "exerciseRefs": [f"b1-demokracia-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-demokracia-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.demokracia-consolidation",
        "title": "Összefoglalás: A modern Magyarország és az integráció (Modern Hungary Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of Democratic Governance, European Integration & National Cohesion",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-demokracia.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-demokracia-consolidation-ex.json",
                "exerciseRefs": [f"b1-demokracia-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-demokracia-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 28 (b1-demokracia)!")

if __name__ == "__main__":
    build_unit_28_citizenship()
