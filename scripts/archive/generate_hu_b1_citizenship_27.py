#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 27: The Regime Change: From Communism to Democracy (b1-rendszervaltas)."""

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

def build_unit_27_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.rendszervaltas.01",
        "lesson": "b1-rendszervaltas-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Lakiteleki találkozó", "translation": "Lakitelek gathering (September 1987 birth of the democratic opposition)", "pos": "noun"},
            {"lemma": "Ellenzéki Kerekasztal", "translation": "Opposition Roundtable (EKA, united front of democratic groups in 1989)", "pos": "noun"},
            {"lemma": "Nemzeti Kerekasztal", "translation": "National Roundtable talks (tripartite negotiations shaping peaceful transition)", "pos": "noun"},
            {"lemma": "békés átmenet", "translation": "peaceful transition (negotiated path from dictatorship to democracy)", "pos": "noun"},
            {"lemma": "politikai pluralizmus", "translation": "political pluralism / multi-party system", "pos": "noun"},
            {"lemma": "Magyar Demokrata Fórum", "translation": "Hungarian Democratic Forum (MDF, leading center-right opposition party)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rendszervaltas-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.rendszervaltas.02",
        "lesson": "b1-rendszervaltas-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vasfüggöny lebontása", "translation": "dismantling of the Iron Curtain along the Austrian border (spring 1989)", "pos": "noun"},
            {"lemma": "Páneurópai piknik", "translation": "Pan-European Picnic (August 19, 1989 peace demonstration near Sopron)", "pos": "noun"},
            {"lemma": "határnyitás", "translation": "border opening (September 10/11, 1989, allowing East Germans to the West)", "pos": "noun"},
            {"lemma": "NDK-menekültek", "translation": "East German (GDR) refugees camping in Budapest church gardens", "pos": "noun"},
            {"lemma": "szögesdrót", "translation": "barbed wire dismantled at Hegyeshalom and Sopron", "pos": "noun"},
            {"lemma": "európai újraegyesítés", "translation": "European reunification triggered by Hungarian border opening", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rendszervaltas-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.rendszervaltas.03",
        "lesson": "b1-rendszervaltas-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nagy Imre újratemetése", "translation": "reburial of Imre Nagy and martyr comrades (June 16, 1989)", "pos": "noun"},
            {"lemma": "Hősök tere", "translation": "Heroes' Square (scene of the 300,000-strong historic memorial service)", "pos": "noun"},
            {"lemma": "301-es parcella", "translation": "Plot 301 in Rákoskeresztúr cemetery (burial ground of 1956 martyrs)", "pos": "noun"},
            {"lemma": "szovjet csapatkivonás", "translation": "withdrawal of Soviet occupation forces from Hungarian territory", "pos": "noun"},
            {"lemma": "mártírok rehabilitációja", "translation": "moral and political rehabilitation of the executed 1956 heroes", "pos": "noun"},
            {"lemma": "történelmi igazságtétel", "translation": "historical justice delivered through public remembrance", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rendszervaltas-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.rendszervaltas.04",
        "lesson": "b1-rendszervaltas-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Magyar Köztársaság kikiáltása", "translation": "proclamation of the Republic of Hungary (October 23, 1989)", "pos": "noun"},
            {"lemma": "Szűrös Mátyás", "translation": "Mátyás Szűrös (provisional president proclaiming the Republic)", "pos": "noun"},
            {"lemma": "október huszonharmadika", "translation": "October 23rd (connecting 1956 revolution with the 1989 free Republic)", "pos": "noun"},
            {"lemma": "alkotmánymódosítás", "translation": "comprehensive constitutional amendment replacing socialist tenets", "pos": "noun"},
            {"lemma": "népszuverenitás", "translation": "popular sovereignty / government derived from the people", "pos": "noun"},
            {"lemma": "demokratikus jogállam", "translation": "democratic state governed by the rule of law", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rendszervaltas-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.rendszervaltas.05",
        "lesson": "b1-rendszervaltas-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "első szabad választások", "translation": "first free democratic parliamentary elections (March-April 1990)", "pos": "noun"},
            {"lemma": "Antall József", "translation": "József Antall (first democratically elected Prime Minister)", "pos": "noun"},
            {"lemma": "Göncz Árpád", "translation": "Árpád Göncz (1956 prisoner elected first President of the Republic)", "pos": "noun"},
            {"lemma": "koalíciós kormány", "translation": "center-right coalition government led by MDF, FKgP, and KDNP", "pos": "noun"},
            {"lemma": "parlamenti demokrácia", "translation": "parliamentary democracy based on free elections and checks and balances", "pos": "noun"},
            {"lemma": "rendszerváltoztatás", "translation": "regime change / complete transformation of Hungary's political order", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rendszervaltas-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.rendszervaltas.01.roundtable-negotiations",
        "title": "Consensus and Political Negotiation: megállapodnak abban, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Formulas of Multi-Party Deliberation",
                "content": "Describing negotiated transitions uses verbs of multilateral accord: *megállapodnak abban, hogy...* ('agree on the fact that...'), *tárgyalóasztalhoz ül* ('sits down at the negotiating table'), *kompromisszumos megállapodást köt* ('strikes a compromise agreement')."
            },
            {
                "type": "examples",
                "title": "Roundtable examples",
                "items": [
                    {
                        "spanish": "Az Ellenzéki Kerekasztal pártjai megállapodtak abban, hogy egységesen lépnek fel a tárgyalásokon.",
                        "english": "The parties of the Opposition Roundtable agreed to act unitedly during the negotiations."
                    },
                    {
                        "spanish": "A Nemzeti Kerekasztal biztosította a békés átmenet jogi kereteit.",
                        "english": "The National Roundtable secured the legal framework for the peaceful transition."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rendszervaltas-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.rendszervaltas.02.border-opening-events",
        "title": "Decisive Historical Turning Points: utat nyit vmi előtt, lebont",
        "sections": [
            {
                "type": "text",
                "title": "Metaphors of Opening and Demolition",
                "content": "Key historical idioms: *utat nyit a szabadság előtt* ('opens the way to freedom'), *lebontja a vasfüggönyt* ('dismantles the Iron Curtain'), *áttöri a határt* ('breaks through the border')."
            },
            {
                "type": "examples",
                "title": "Border opening examples",
                "items": [
                    {
                        "spanish": "A magyar határnyitás megnyitotta az utat Németország és Európa újraegyesítése előtt.",
                        "english": "The Hungarian border opening opened the path toward the reunification of Germany and Europe."
                    },
                    {
                        "spanish": "A Páneurópai pikniken keletnémet családok százai jutottak át Ausztriába.",
                        "english": "At the Pan-European Picnic, hundreds of East German families crossed over into Austria."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rendszervaltas-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.rendszervaltas.03.commemoration-speeches",
        "title": "Public Demands and Solemn Oratory: követel, tiszteleg",
        "sections": [
            {
                "type": "text",
                "title": "High Commemorative and Political Register",
                "content": "Public remembrance combines solemn homage with explicit demands: *tiszteleg a mártírok emléke előtt* ('pays tribute before the memory of the martyrs'), *követeli a szovjet csapatok kivonását* ('demands the withdrawal of Soviet troops'), *igazságot szolgáltat* ('delivers justice')."
            },
            {
                "type": "examples",
                "title": "Commemoration examples",
                "items": [
                    {
                        "spanish": "1989. június 16-án háromszázezer ember tisztelgett Nagy Imre és társai koporsója előtt a Hősök terén.",
                        "english": "On June 16, 1989, three hundred thousand people paid tribute before the coffins of Imre Nagy and his companions at Heroes' Square."
                    },
                    {
                        "spanish": "A beszédben határozottan követelték a megszálló szovjet csapatok azonnali kivonását Magyarországról.",
                        "english": "In the speech, they firmly demanded the immediate withdrawal of occupying Soviet troops from Hungary."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rendszervaltas-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.rendszervaltas.04.proclamation-formulas",
        "title": "Constitutional Proclamations: kikiáltja a köztársaságot, hatályba lép",
        "sections": [
            {
                "type": "text",
                "title": "Juridical Formulas of Statehood",
                "content": "Key institutional verbs: *kikiáltja a köztársaságot* ('proclaims the Republic'), *hatályba lép az alkotmány* ('the constitution enters into effect'), *megszűnik a népköztársaság* ('the people's republic ceases to exist')."
            },
            {
                "type": "examples",
                "title": "Statehood examples",
                "items": [
                    {
                        "spanish": "1989. október 23-án a Parlament erkélyéről hivatalosan kikiáltották a független Magyar Köztársaságot.",
                        "english": "On October 23, 1989, from the balcony of Parliament, the independent Republic of Hungary was officially proclaimed."
                    },
                    {
                        "spanish": "Az új alkotmánymódosítás nyomán Magyarország demokratikus jogállammá vált.",
                        "english": "Following the new constitutional amendment, Hungary became a democratic state governed by the rule of law."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rendszervaltas-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.rendszervaltas.05.democratic-legitimacy",
        "title": "Electoral Mandates and Governance: bizalmat szavaz, kormányt alakít",
        "sections": [
            {
                "type": "text",
                "title": "Parliamentary Democracy Governance Syntax",
                "content": "*Kormányt alakít* ('forms a government'), *bizalmat kap a választóktól* ('receives the trust of the electorate'), *felesküszik a demokratikus alkotmányra* ('swears an oath on the democratic constitution')."
            },
            {
                "type": "examples",
                "title": "Democracy in practice",
                "items": [
                    {
                        "spanish": "Az 1990-es tavaszi választások nyomán Antall József vezetésével alakult meg az első szabad kormány.",
                        "english": "Following the spring 1990 elections, the first free government was formed under the leadership of József Antall."
                    },
                    {
                        "spanish": "Göncz Árpádot választotta meg a szabad parlament a Magyar Köztársaság elnökévé.",
                        "english": "The free parliament elected Árpád Göncz as President of the Republic of Hungary."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rendszervaltas-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Story Files (5 regular lesson stories + 1 combined omnibus story)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.rendszervaltas.01",
        "lesson": 1,
        "order": 1,
        "title": "Az Ellenzéki Kerekasztal és a békés átmenet",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In September 1987, patriotic writers and dissidents met in Lakitelek, creating the Hungarian Democratic Forum (MDF). By March 1989, eight democratic opposition parties and groups formed the Opposition Roundtable (EKA) to face the communist party united. At the National Roundtable talks, they negotiated the bloodless, peaceful transition from single-party rule to a multi-party constitutional democracy.",
        "characters": [
            "Pozsgay Imre, reformkommunista államminiszter",
            "Antall József, az Ellenzéki Kerekasztal vezető tárgyalója",
            "Fiatal jogász ellenzéki"
        ],
        "location": "Lakitelek és az Országház Vadászterme",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1987 őszén egy Bács-Kiskun megyei faluban, Lakitelken, Lezsák Sándor sátorkertjében gyűlt össze a magyar értelmiség színe-java. Megszületett a Magyar Demokrata Fórum (MDF), és elindult a demokratikus mozgalom feltartóztathatatlan hulláma."
            },
            {
                "type": "dialogue",
                "speaker": "Antall József ellenzéki vezető",
                "text": "Nem engedhetjük, hogy a pártállam megosszon bennünket! Ha a szabadságot akarjuk, egyetlen közös asztalhoz kell ülnünk, és egységes frontban kell fellépnünk!"
            },
            {
                "type": "narration",
                "text": "1989 márciusában megalakult az Ellenzéki Kerekasztal (EKA). Nyáron a Parlament Vadásztermében megkezdődtek a Nemzeti Kerekasztal-tárgyalások: a kommunista MSZMP és az ellenzék vezetői leültek egymással."
            },
            {
                "type": "dialogue",
                "speaker": "Fiatal ellenzéki jogász",
                "text": "Nincs több erőszak, nincs több fegyveres megtorlás! A jogállamot a jog és a tárgyalások erejével hozzuk létre, békés átmenettel!"
            },
            {
                "type": "narration",
                "text": "A kerekasztal-tárgyalások során megegyeztek a szabad választások feltételeiben, a többpártrendszerben és az alkotmány békés átírásában. Magyarország a vérontás nélküli forradalom példájává vált a világban."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas-01-kerekasztal.json", story_01)

    story_02 = {
        "id": "story.b1.rendszervaltas.02",
        "lesson": 2,
        "order": 2,
        "title": "A vasfüggöny lebontása és a határnyitás (1989)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In May 1989, Hungary began physically dismantling the barbed-wire electric fence along the Austrian border. On August 19, the Pan-European Picnic near Sopron allowed hundreds of East Germans to breach the border to the West. Finally, on September 10, 1989, the Hungarian government officially opened the western border, tearing the first brick from the Berlin Wall and uniting Europe.",
        "characters": [
            "Horn Gyula külügyminiszter",
            "Keletnémet apa a kislányával a zugligeti templomkertben",
            "Határőr tiszt Sopronnál"
        ],
        "location": "Hegyeshalom, a soproni határszél és a budapesti Zugliget",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1989 tavaszán a magyar határőrség megkezdte a rozsdás szögesdrót és az elektromos jelzőrendszer lebontását az osztrák határon. Horn Gyula magyar és Alois Mock osztrák külügyminiszter közösen vágta át a vasfüggönyt."
            },
            {
                "type": "narration",
                "text": "A hír villámgyorsan elterjedt Kelet-Németországban. Nyáron több tízezer NDK-állampolgár érkezett Budapestre, és a zugligeti templomkertben felvert sátrakban kértek menedéket Kozma Imre atya Máltai Szeretetszolgálatánál."
            },
            {
                "type": "dialogue",
                "speaker": "Keletnémet apa",
                "text": "Nem mehetünk vissza a Stasi elnyomásába! A gyermekeinknek szabad jövőt akarunk Nyugaton! Kérjük a magyarokat, engedjenek át minket a határon!"
            },
            {
                "type": "narration",
                "text": "Augusztus 19-én a Páneurópai pikniken Sopronnál áttörték a kaput a menekültek. Majd szeptember 10-én este a televízióban Horn Gyula bejelentette a történelmi döntést: Magyarország megnyitja határait a nyugatra távozni akaró NDK-polgárok előtt."
            },
            {
                "type": "dialogue",
                "speaker": "Horn Gyula külügyminiszter",
                "text": "Magyarország nem fegyverrel védi a határait más államok polgárai ellen. Ma éjféltől minden NDK-állampolgár szabadon átlépheti az osztrák határt!"
            },
            {
                "type": "narration",
                "text": "Ez a bátor döntés döntötte le az első dominót: alig két hónappal később leomlott a berlini fal, s megkezdődött Németország és Európa újraegyesítése."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas-02-hatarnyitas.json", story_02)

    story_03 = {
        "id": "story.b1.rendszervaltas.03",
        "lesson": 3,
        "order": 3,
        "title": "Nagy Imre újratemetése (1989. június 16.)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On June 16, 1989, thirty-one years after the execution of Imre Nagy and the martyrs of 1956, over 300,000 Hungarians gathered at Budapest's Heroes' Square. Six coffins stood on the steps of the Műcsarnok, including an empty sixth coffin for all unknown martyrs. The dramatic speech demanding the immediate withdrawal of Soviet troops broke thirty years of silence, marking the moral funeral of the communist system.",
        "characters": [
            "Rácz Sándor, 1956-os munkástanács-vezető",
            "Orbán Viktor, az ellenzéki ifjúság szónoka",
            "Gyászoló idős asszony virággal"
        ],
        "location": "Budapest, a Hősök tere és a Rákoskeresztúri új köztemető 301-es parcellája",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1989. június 16-án reggel fenséges és mély csend borult Budapestre. A Hősök terén, a Műcsarnok lépcsőin hat koporsó állt: Nagy Imre, Maléter Pál, Gimes Miklós, Losonczy Géza, Szilágyi József és a hatodik, üres koporsó a névtelen forradalmárokért."
            },
            {
                "type": "dialogue",
                "speaker": "Gyászoló idős asszony",
                "text": "Harminchárom évig nem tehettem egy szál virágot a fiam sírjára, mert még a nevét is tilos volt kiejteni. Ma végre szabadon sirathatjuk el a hőseinket!"
            },
            {
                "type": "narration",
                "text": "Háromszázezer ember állt a téren néma fegyelemben. A szónokok sorában egy huszonhat éves fiatalember, Orbán Viktor lépett a mikrofon elé, s szavai villámként járták be az országot."
            },
            {
                "type": "dialogue",
                "speaker": "Orbán Viktor szónok",
                "text": "Ha hiszünk a magunk erejében, képesek vagyunk véget vetni a kommunista diktatúrának! Követeljük a szovjet csapatok haladéktalan és teljes kivonását Magyarország területéről!"
            },
            {
                "type": "narration",
                "text": "A koporsókat délután a 301-es parcellában helyezték örök nyugalomra. Ezen a napon a kádárizmus erkölcsileg összeomlott: a magyar nép visszaszerezte a büszkeségét és az 1956-os forradalom tiszta örökségét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas-03-ujratemetes.json", story_03)

    story_04 = {
        "id": "story.b1.rendszervaltas.04",
        "lesson": 4,
        "order": 4,
        "title": "A Magyar Köztársaság kikiáltása (1989. október 23.)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On October 23, 1989—the 33rd anniversary of the 1956 Revolution—provisional President of the Republic Mátyás Szűrös stepped onto the balcony of the Parliament building overlooking Kossuth Square. Before an exultant crowd of 100,000 citizens, he proclaimed the birth of the free, independent, and democratic Republic of Hungary, consigning the socialist 'People's Republic' to history.",
        "characters": [
            "Szűrös Mátyás, ideiglenes köztársasági elnök",
            "Kossuth téri ünneplő egyetemi diák",
            "Idős 1956-os harcos"
        ],
        "location": "Budapest, a Parlament Kossuth téri erkélye és a tér",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1989. október 23-án, pontosan a forradalom harmincharmadik évfordulóján százezres tömeg gyűlt össze a budapesti Kossuth téren. A Parlament homlokzatáról már korábban levették a vörös csillagot."
            },
            {
                "type": "dialogue",
                "speaker": "Szűrös Mátyás ideiglenes köztársasági elnök",
                "text": "A mai naptól kezdve hazánk államformája és neve: Magyar Köztársaság! A népköztársaság korszaka lezárult. Hazánk szabad, demokratikus és független jogállam, amely a népszuverenitáson alapszik!"
            },
            {
                "type": "narration",
                "text": "A tömeg hatalmas éljenzésben tört ki. Zúgtak a harangok, kibontották a lyukas zászlókat, s az emberek a Himnuszt énekelték könnyeikkel küszködve."
            },
            {
                "type": "dialogue",
                "speaker": "Idős 1956-os harcos",
                "text": "Megértük! Harminchárom évvel ezelőtt ezen a téren lőttek ránk a gyilkosok. Ma pedig a szabad köztársaságot ünnepeljük! Nem volt hiábavaló a mártírok vére!"
            },
            {
                "type": "narration",
                "text": "A köztársaság kikiáltásával életbe lépett az átfogó alkotmánymódosítás: megszűnt az egypártrendszer, biztosították az emberi alapjogokat, s kitűzték az első szabad választások időpontját."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas-04-kikialtas.json", story_04)

    story_05 = {
        "id": "story.b1.rendszervaltas.05",
        "lesson": 5,
        "order": 5,
        "title": "Az első szabad választások és az Antall-kormány (1990)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In March and April 1990, Hungarians cast their votes in the first free democratic multi-party elections in over four decades. The Hungarian Democratic Forum (MDF) won a decisive victory. Historian József Antall formed a center-right coalition government, pledging to serve as 'Prime Minister of 15 million Hungarians in spirit'. The Parliament elected 1956 veteran Árpád Göncz as President, sealing the peaceful birth of the democratic third Republic.",
        "characters": [
            "Antall József miniszterelnök",
            "Göncz Árpád köztársasági elnök",
            "Első szavazó fiatal polgár"
        ],
        "location": "Budapest, Országház és egy budapesti szavazóhelyiség",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1990 tavaszán negyvenöt év kényszerű szünet után a magyar állampolgárok újra szabadon dönthettek a hazájuk sorsáról. Hosszú sorok kígyóztak a szavazókörök előtt: a választást a Magyar Demokrata Fórum (MDF) nyerte meg."
            },
            {
                "type": "dialogue",
                "speaker": "Antall József miniszterelnök",
                "text": "Közjogi értelemben a Magyar Köztársaság kormánya ennek az országnak a kormánya. De lélekben, érzésben tizenötmillió magyar miniszterelnöke kívánok lenni, a határokon túli testvéreinket is beleértve!"
            },
            {
                "type": "narration",
                "text": "Májusban megalakult az Antall-kormány, az MDF, a Kisgazdapárt és a Kereszténydemokraták koalíciója. A Parlament az 1956-os forradalom után életfogytiglanra ítélt írót és műfordítót, Göncz Árpádot választotta a köztársaság elnökévé."
            },
            {
                "type": "dialogue",
                "speaker": "Göncz Árpád köztársasági elnök",
                "text": "Ha szolgálni kívánok valakit, azokat kívánom szolgálni, akiknek nincsen szavuk: a védteleneket, a szegényeket és a szabadságra vágyókat!"
            },
            {
                "type": "narration",
                "text": "1991 júniusában az utolsó szovjet katona is elhagyta Magyarország területét. A békés rendszerváltoztatás befejeződött: Magyarország visszanyerte teljes nemzeti függetlenségét és szuverenitását."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas-05-valasztasok.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.rendszervaltas.combined",
        "title": "A magyar rendszerváltoztatás története (1988–1990)",
        "level": "B1",
        "order": 27,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "A comprehensive historical chronicle of Hungary's negotiated revolution between 1988 and 1990. From the dissident gatherings at Lakitelek and the Opposition Roundtable; the dismantling of the Iron Curtain and the border opening that helped reunify Germany; the cathartic reburial of Imre Nagy on June 16, 1989; the proclamation of the Republic on October 23, 1989; to the first free elections and the inauguration of Prime Minister József Antall and President Árpád Göncz.",
        "characters": [
            "Antall József miniszterelnök",
            "Göncz Árpád köztársasági elnök",
            "Szűrös Mátyás ideiglenes elnök",
            "Horn Gyula külügyminiszter"
        ],
        "location": "Budapest, Országház, Hősök tere és a soproni határszél",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kádári modell gazdasági és erkölcsi kimerülése után Magyarországon a társadalom békés úton vívta ki a szabadságot. 1987-ben Lakitelken zászlót bontott az ellenzék, s 1989 tavaszán az Ellenzéki Kerekasztal egységbe kovácsolta a demokráciáért küzdő pártokat."
            },
            {
                "type": "narration",
                "text": "Magyarország a vasfüggöny lebontásával és a nyugati határok 1989. szeptemberi megnyitásával történelmi szerepet játszott a kettéosztott Európa egyesítésében. 1989. június 16-án Nagy Imre és az 1956-os mártírok újratemetése a Hősök terén a kommunista diktatúra erkölcsi temetésévé vált."
            },
            {
                "type": "narration",
                "text": "1989. október 23-án Szűrös Mátyás kikiáltotta a Magyar Köztársaságot. 1990 tavaszán megtartották az első szabad választásokat: megalakult Antall József kormánya, Göncz Árpád lett a köztársasági elnök, s 1991 nyarára az utolsó szovjet katona is elhagyta az országot."
            },
            {
                "type": "narration",
                "text": "A magyar rendszerváltoztatás a békés, tárgyalásos átmenet nemzetközileg elismert mintájává vált: vérontás nélkül, a jog uralmára építve született újjá a demokratikus állam."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rendszervaltas.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-rendszervaltas-01",
        "exercises": [
            {
                "id": "b1-rendszervaltas-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi volt a célja az 1989 márciusában megalakult Ellenzéki Kerekasztalnak (EKA)?",
                "options": [
                    "Hogy a demokratikus ellenzéki erők egységesen tárgyaljanak az állampárttal a békés átmenetről.",
                    "Hogy új sportegyesületet hozzanak létre a diákoknak.",
                    "Hogy megszervezzék a szovjet hadsereg utánpótlását."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felek megállapodtak abban, hogy a változások békés úton men_____ végbe. (should proceed - jenek)",
                "answer": "jenek"
            },
            {
                "id": "b1-rendszervaltas-01.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "Nemzeti", "Kerekasztal", "kidolgozta", "a", "szabad", "választások", "szabályait."],
                "solution": ["A", "Nemzeti", "Kerekasztal", "kidolgozta", "a", "szabad", "választások", "szabályait."]
            },
            {
                "id": "b1-rendszervaltas-01.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Hol alakult meg 1987 szeptemberében a Magyar Demokrata Fórum (MDF)?",
                "options": [
                    "Lakitelken, Lezsák Sándor kertjében.",
                    "A moszkvai Kremlben.",
                    "A genfi ENSZ-palotában."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A politikai pluraliz_____ a többpártrendszer alapvető feltétele. (stem suffix - mus)",
                "answer": "mus"
            },
            {
                "id": "b1-rendszervaltas-01.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi jellemezte a magyar rendszerváltoztatás folyamatát európai összehasonlításban?",
                "options": [
                    "A vérontás nélküli, jogi alapokon nyugvó, tárgyalásos békés átmenet.",
                    "A polgárháború és a városok lerombolása.",
                    "A katonai junta hatalomátvétele."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tárgyalópartnerek közös nevezőre jut_____ a sarkalatos törvények ügyében. (they came - tak)",
                "answer": "tak"
            },
            {
                "id": "b1-rendszervaltas-01.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "békés", "átmenet", "biztosította", "a", "demokrácia", "győzelmét."],
                "solution": ["A", "békés", "átmenet", "biztosította", "a", "demokrácia", "győzelmét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-rendszervaltas-02",
        "exercises": [
            {
                "id": "b1-rendszervaltas-02.ex01",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik történelmi esemény történt 1989. augusztus 19-én Sopron közelében?",
                "options": [
                    "A Páneurópai piknik, ahol keletnémet menekültek százai jutottak át Ausztriába.",
                    "A varsói szerződés katonai hadgyakorlata.",
                    "A szovjet csapatok bevonulása."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar kormány megnyitotta a határt a menekültek előtt, ami utat nyi_____ Németország egyesülése előtt. (opened - tott)",
                "answer": "tott"
            },
            {
                "id": "b1-rendszervaltas-02.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "vasfüggöny", "lebontása", "az", "európai", "egység", "szimbóluma", "lett."],
                "solution": ["A", "vasfüggöny", "lebontása", "az", "európai", "egység", "szimbóluma", "lett."]
            },
            {
                "id": "b1-rendszervaltas-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kik nyújtottak menedéket a budapesti templomkertben sátorozó NDK-menekülteknek?",
                "options": [
                    "Kozma Imre atya és a Magyar Máltai Szeretetszolgálat.",
                    "A keletnémet nagykövetség katonái.",
                    "A szovjet csendőrség."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A határőrök átvágták a határon húzódó szögesdró_____. (accusative - tot)",
                "answer": "tot"
            },
            {
                "id": "b1-rendszervaltas-02.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan értékelte Helmut Kohl német kancellár Magyarország 1989-es határnyitását?",
                "options": [
                    "A magyarok ütötték ki az első téglát a berlini falból.",
                    "Magyarország elhibázott külpolitikát folytatott.",
                    "A határnyitás semmilyen hatással nem volt Németországra."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1989. szeptember 10-én Magyarország hivatalosan bejelentette a határnyitás_____. (its opening - t)",
                "answer": "t"
            },
            {
                "id": "b1-rendszervaltas-02.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Több", "tízezer", "NDK-állampolgár", "távozhatott", "szabadon", "Nyugatra."],
                "solution": ["Több", "tízezer", "NDK-állampolgár", "távozhatott", "szabadon", "Nyugatra."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-rendszervaltas-03",
        "exercises": [
            {
                "id": "b1-rendszervaltas-03.ex01",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik napon zajlott Nagy Imre és mártírtársai történelmi újratemetése a Hősök terén?",
                "options": [
                    "1989. június 16-án.",
                    "1956. október 23-án.",
                    "1990. május 1-jén."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szónokok követelték a szovjet csapatok haladéktalan kivonás_____. (its withdrawal - át)",
                "answer": "át"
            },
            {
                "id": "b1-rendszervaltas-03.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Háromszázezer", "ember", "tisztelgett", "a", "mártírok", "koporsója", "előtt."],
                "solution": ["Háromszázezer", "ember", "tisztelgett", "a", "mártírok", "koporsója", "előtt."]
            },
            {
                "id": "b1-rendszervaltas-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hol található a kádári megtorlás áldozatainak titkos temetkezési helye, a 301-es parcella?",
                "options": [
                    "A rákoskeresztúri Új köztemetőben.",
                    "A Margit-szigeten.",
                    "A budai Vár udvarán."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az újratemetés a történelmi igazságtétel döntő pillanata vol_____. (was - t)",
                "answer": "t"
            },
            {
                "id": "b1-rendszervaltas-03.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért volt sorsdöntő jelentősége az 1989. június 16-i megemlékezésnek?",
                "options": [
                    "Mert nyilvánvalóvá tette a kommunista rendszer erkölcsi bukását és a forradalom igazságát.",
                    "Mert elhalasztották a választásokat újabb tíz évre.",
                    "Mert új szovjet katonai támaszpontokat hoztak létre."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A mártírok rehabilitációja megnyitotta a kaput a demokrácia elő_____. (postposition - tt)",
                "answer": "tt"
            },
            {
                "id": "b1-rendszervaltas-03.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "nép", "visszaszerezte", "a", "múltját", "és", "büszkeségét."],
                "solution": ["A", "magyar", "nép", "visszaszerezte", "a", "múltját", "és", "büszkeségét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-rendszervaltas-04",
        "exercises": [
            {
                "id": "b1-rendszervaltas-04.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mikor kiáltották ki hivatalosan a harmadik Magyar Köztársaságot a Parlament erkélyéről?",
                "options": [
                    "1989. október 23-án.",
                    "1945. április 4-én.",
                    "1999. március 12-én."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szűrös Mátyás kikiáltotta a független Magyar Köztársaság_____. (accusative - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-rendszervaltas-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Magyarország", "független", "és", "demokratikus", "jogállam", "lett."],
                "solution": ["Magyarország", "független", "és", "demokratikus", "jogállam", "lett."]
            },
            {
                "id": "b1-rendszervaltas-04.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Ki kiáltotta ki a Magyar Köztársaságot 1989. október 23-án ideiglenes köztársasági elnökként?",
                "options": [
                    "Szűrös Mátyás.",
                    "Kádár János.",
                    "Nagy Imre."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az államhatalom forrása a népszuverenit_____ elve alapján a választópolgárok összessége. (stem suffix - ás)",
                "answer": "ás"
            },
            {
                "id": "b1-rendszervaltas-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért pont október 23-át választották a köztársaság kikiáltásának napjául?",
                "options": [
                    "Hogy szimbolikusan összekapcsolják az új köztársaságot az 1956-os forradalom örökségével.",
                    "Mert aznap volt a köztársasági elnök születésnapja.",
                    "Mert októberben mindig jó az idő Budapesten."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az átfogó alkotmánymódosítás felszámolta az egypártrendszer_____. (its system - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-rendszervaltas-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tömeg", "örömkönnyek", "között", "énekelte", "a", "nemzeti", "Himnuszt."],
                "solution": ["A", "tömeg", "örömkönnyek", "között", "énekelte", "a", "nemzeti", "Himnuszt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-rendszervaltas-05",
        "exercises": [
            {
                "id": "b1-rendszervaltas-05.ex01",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Ki lett a rendszerváltoztatás utáni első szabadon választott magyar miniszterelnök?",
                "options": [
                    "Antall József.",
                    "Horn Gyula.",
                    "Kossuth Lajos."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Antall József koalíciós kormányt alakí_____ az MDF vezetésével. (formed - tott)",
                "answer": "tott"
            },
            {
                "id": "b1-rendszervaltas-05.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "első", "szabad", "választásokat", "1990", "tavaszán", "tartották", "meg."],
                "solution": ["Az", "első", "szabad", "választásokat", "1990", "tavaszán", "tartották", "meg."]
            },
            {
                "id": "b1-rendszervaltas-05.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Kit választott meg az újonnan alakult szabad Parlament a köztársaság első elnökévé?",
                "options": [
                    "Göncz Árpádot, az 1956-os forradalom egykori elítéltjét.",
                    "Kádár Jánost.",
                    "Rákosi Mátyást."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1991 júniusában az utolsó szovjet katona is elhagyta Magyarorszá_____. (accusative - got)",
                "answer": "got"
            },
            {
                "id": "b1-rendszervaltas-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelentett Antall József híres mondata: 'lélekben tizenötmillió magyar miniszterelnöke kívánok lenni'?",
                "options": [
                    "Azt, hogy felelősséget érez a határokon kívül, a szomszédos országokban és a diaszpórában élő magyarok iránt is.",
                    "Azt, hogy tizenötmillió embert akart beköltöztetni Budapestre.",
                    "Azt, hogy tizenötezer forintot ad minden állampolgárnak."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szabad parlament visszaállította a jogállamiság intézményrendszer_____. (its institutional system - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-rendszervaltas-05.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Magyarország", "visszanyerte", "teljes", "nemzeti", "függetlenségét", "és", "szabadságát."],
                "solution": ["Magyarország", "visszanyerte", "teljes", "nemzeti", "függetlenségét", "és", "szabadságát."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-rendszervaltas-consolidation",
        "exercises": [
            {
                "id": "b1-rendszervaltas-consolidation.ex01",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik évszámhoz kötjük a magyarországi rendszerváltoztatást?",
                "options": [
                    "1989–1990.",
                    "1948–1949.",
                    "1914–1918."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex02",
                "type": "fill-blank",
                "category": "citizenship",
                "sentence": "1989. október 23-án kiáltották ki a Magyar Köztársaság_____. (accusative - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magyar", "rendszerváltoztatás", "békés", "és", "tárgyalásos", "úton", "zajlott."],
                "solution": ["A", "magyar", "rendszerváltoztatás", "békés", "és", "tárgyalásos", "úton", "zajlott."]
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex04",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen nemzetközi szerepet játszott Magyarország a vasfüggöny lebontásával 1989-ben?",
                "options": [
                    "Döntő lökést adott a berlini fal leomlásához és Németország újraegyesítéséhez.",
                    "Elszigetelte Közép-Európát a világ többi részétől.",
                    "Lezárta a nemzetközi kereskedelmi utakat."
                ],
                "correct": 0
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szabad választások biztosították a parlamentáris demokrácia működés_____. (its functioning - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Antall", "József", "vezetésével", "lépett", "hivatalba", "az", "első", "demokratikus", "kormány."],
                "solution": ["Antall", "József", "vezetésével", "lépett", "hivatalba", "az", "első", "demokratikus", "kormány."]
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Nemzeti Kerekasztal tárgyalásain dolgozták ki az átmenet sarkalatos törvénye_____. (its laws - it)",
                "answer": "it"
            },
            {
                "id": "b1-rendszervaltas-consolidation.ex08",
                "type": "multiple-choice",
                "category": "citizenship",
                "question": "Mikor hagyta el az utolsó szovjet katona Magyarországot, visszaállítva a teljes szuverenitást?",
                "options": [
                    "1991 júniusában.",
                    "1956 novemberében.",
                    "2004 májusában."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rendszervaltas-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Az Ellenzéki Kerekasztal és a békés átmenet", "Opposition Roundtable & Negotiated Transition"),
        "02": ("A vasfüggöny lebontása és a határnyitás", "Dismantling the Iron Curtain & Border Opening"),
        "03": ("Nagy Imre újratemetése (1989. június 16.)", "Reburial of Imre Nagy & Moral Renewal"),
        "04": ("A Magyar Köztársaság kikiáltása", "Proclamation of the Republic (October 23, 1989)"),
        "05": ("Az első szabad választások és az Antall-kormány", "First Free Elections & Democratic Governance")
    }

    story_refs = {
        "01": "stories/world/b1/b1-rendszervaltas-01-kerekasztal.json",
        "02": "stories/world/b1/b1-rendszervaltas-02-hatarnyitas.json",
        "03": "stories/world/b1/b1-rendszervaltas-03-ujratemetes.json",
        "04": "stories/world/b1/b1-rendszervaltas-04-kikialtas.json",
        "05": "stories/world/b1/b1-rendszervaltas-05-valasztasok.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.rendszervaltas-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Constitutional Proclamations, Negotiated Democracy & Sovereign Historical Registers",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} during Hungary's democratic transition.",
                        "I can use constitutional, political, and historical terminology of 1989-1990.",
                        "I can answer essential citizenship interview questions regarding the Republic, free elections, and national heroes.",
                        "I can master six target vocabulary items in authentic historical context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-rendszervaltas-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-rendszervaltas-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-rendszervaltas-{padded}-ex.json",
                    "exerciseRefs": [f"b1-rendszervaltas-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-rendszervaltas-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.rendszervaltas-consolidation",
        "title": "Összefoglalás: A rendszerváltoztatás évei (Regime Change Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of Regime Change Memory, Democratic Legitimacy & Sovereign Republic",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-rendszervaltas.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-rendszervaltas-consolidation-ex.json",
                "exerciseRefs": [f"b1-rendszervaltas-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-rendszervaltas-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 27 (b1-rendszervaltas)!")

if __name__ == "__main__":
    build_unit_27_citizenship()
