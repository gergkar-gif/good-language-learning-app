#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 25: The 1956 Revolution (b1-otvenhat)."""

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

def build_unit_25_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.otvenhat.01",
        "lesson": "b1-otvenhat-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "október huszonharmadika", "translation": "October 23rd (outbreak of 1956 Revolution, national holiday)", "pos": "noun"},
            {"lemma": "egyetemista tüntetés", "translation": "university student demonstration (at Petőfi and Bem statues)", "pos": "noun"},
            {"lemma": "tizenhat pont", "translation": "16 points (revolutionary political and democratic demands)", "pos": "noun"},
            {"lemma": "Sztálin-szobor ledöntése", "translation": "toppling of the colossal bronze Stalin monument at City Park", "pos": "noun"},
            {"lemma": "Magyar Rádió ostroma", "translation": "siege of the Hungarian Radio on Bródy Sándor street", "pos": "noun"},
            {"lemma": "lyukas zászló", "translation": "flag with a hole (national tricolor with communist coat-of-arms cut out)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-otvenhat-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.otvenhat.02",
        "lesson": "b1-otvenhat-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "pesti srácok", "translation": "'boys of Pest' (young teenage street fighters confronting Soviet tanks)", "pos": "noun"},
            {"lemma": "Corvin köz", "translation": "Corvin passage (epicenter of armed resistance led by Gergely Pongrátz)", "pos": "noun"},
            {"lemma": "Molotov-koktél", "translation": "Molotov cocktail (gasoline bottles used to immobilize tanks)", "pos": "noun"},
            {"lemma": "szabadságharcos", "translation": "freedom fighter", "pos": "noun"},
            {"lemma": "fegyveres ellenállás", "translation": "armed resistance against invading armored columns", "pos": "noun"},
            {"lemma": "barikád", "translation": "street barricade erected from cobblestones and overturned tramcars", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-otvenhat-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.otvenhat.03",
        "lesson": "b1-otvenhat-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nagy Imre", "translation": "Imre Nagy (reform communist Prime Minister who sided with the people)", "pos": "noun"},
            {"lemma": "többpártrendszer", "translation": "multi-party democratic system restored on October 30", "pos": "noun"},
            {"lemma": "semlegesség", "translation": "declaration of Hungarian neutrality (November 1, 1956)", "pos": "noun"},
            {"lemma": "Varsói Szerződés felmondása", "translation": "renunciation and unilateral exit from the Warsaw Pact", "pos": "noun"},
            {"lemma": "Maléter Pál", "translation": "Pál Maléter (heroic colonel, appointed Minister of Defense)", "pos": "noun"},
            {"lemma": "nemzeti forradalom", "translation": "victorious national revolution for freedom and independence", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-otvenhat-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.otvenhat.04",
        "lesson": "b1-otvenhat-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szovjet invázió", "translation": "massive Soviet military invasion (dawn of November 4, 1956)", "pos": "noun"},
            {"lemma": "Forgószél hadművelet", "translation": "Operation Whirlwind (Khrushchev's crushing armored assault)", "pos": "noun"},
            {"lemma": "túlerő", "translation": "overwhelming military odds (hundreds of Soviet tanks and artillery)", "pos": "noun"},
            {"lemma": "Kádár János", "translation": "János Kádár (traitor installed as puppet head of government)", "pos": "noun"},
            {"lemma": "harc az utolsó töltényig", "translation": "fight to the last bullet (desperate defense of Csepel and hills)", "pos": "noun"},
            {"lemma": "segélykiáltás", "translation": "Imre Nagy's dramatic radio plea to the free world at 5:20 AM", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-otvenhat-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.otvenhat.05",
        "lesson": "b1-otvenhat-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "megtorlás", "translation": "brutal post-revolutionary retribution under Kádár", "pos": "noun"},
            {"lemma": "kivégzés", "translation": "execution (Imre Nagy, Pál Maléter, Miklós Gimes on June 16, 1958)", "pos": "noun"},
            {"lemma": "börtönbüntetés", "translation": "heavy prison sentences for tens of thousands of freedom fighters", "pos": "noun"},
            {"lemma": "emigráció", "translation": "mass emigration (200,000 Hungarians fleeing across the Austrian border)", "pos": "noun"},
            {"lemma": "nemzeti ünnep", "translation": "official national holiday (proclaimed on October 23, 1989)", "pos": "noun"},
            {"lemma": "újratemetés", "translation": "historic ceremonial reburial of the martyrs (June 16, 1989 on Hősök tere)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-otvenhat-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.otvenhat.01.insurgent-demands",
        "title": "Revolutionary Directives & Demands: követel, eltávolít",
        "sections": [
            {
                "type": "text",
                "title": "Formulating Demands of Freedom",
                "content": "Revolutionary manifestos use assertive imperative and cohortative structures: *követeli a szovjet csapatok kivonását* ('demands withdrawal of Soviet troops'), *eltávolítja a diktatúra jelképeit* ('removes symbols of dictatorship'), *szolidaritást vállal* ('declares solidarity')."
            },
            {
                "type": "examples",
                "title": "Revolutionary demands",
                "items": [
                    {
                        "spanish": "Az egyetemisták tizenhat pontban foglalták össze a nemzet demokratikus követeléseit.",
                        "english": "The university students summarized the nation's democratic demands in sixteen points."
                    },
                    {
                        "spanish": "A tüntetők kivágták a gyűlölt címert a nemzeti trikolórból.",
                        "english": "The demonstrators cut out the hated coat-of-arms from the national tricolor."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-otvenhat-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.otvenhat.02.insurgent-warfare",
        "title": "Asymmetric Resistance: szembeszáll a túlerővel, fegyvert ragad",
        "sections": [
            {
                "type": "text",
                "title": "Vocabulary of Heroic Defense",
                "content": "*Fegyvert ragad a szabadságért* ('takes up arms for freedom'), *szembeszáll a hatalmas túlerővel* ('confronts overwhelming odds'), *barikádokat emel* ('erects barricades')."
            },
            {
                "type": "examples",
                "title": "Armed resistance",
                "items": [
                    {
                        "spanish": "A pesti srácok Molotov-koktélokkal szálltak szembe a szovjet tankokkal.",
                        "english": "The boys of Pest confronted Soviet tanks with Molotov cocktails."
                    },
                    {
                        "spanish": "A Corvin köz harcosai napokon keresztül hősiesen védték a bázisukat.",
                        "english": "The fighters of Corvin passage heroically defended their base for days."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-otvenhat-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.otvenhat.03.constitutional-sovereignty",
        "title": "Sovereign Proclamations: kikiáltja a semlegességet, felmondja a szerződést",
        "sections": [
            {
                "type": "text",
                "title": "Official State Decisions of 1956",
                "content": "*Kikiáltja az ország örökös semlegességét* ('proclaims eternal neutrality of the country'), *felmondja a Varsói Szerződést* ('renounces the Warsaw Pact'), *visszaállítja a többpártrendszert* ('restores the multi-party system')."
            },
            {
                "type": "examples",
                "title": "Proclamation of sovereignty",
                "items": [
                    {
                        "spanish": "Nagy Imre kormánya kikiáltotta Magyarország katonai semlegességét.",
                        "english": "The government of Imre Nagy proclaimed Hungary's military neutrality."
                    },
                    {
                        "spanish": "A forradalom napjaiban újjáalakultak a történelmi demokratikus pártok.",
                        "english": "During the days of the revolution, the historic democratic parties reconstituted themselves."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-otvenhat-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.otvenhat.04.invasion-and-pleas",
        "title": "Invasion & Historical Pleas: hadüzenet nélkül megtámad, segélyt kér",
        "sections": [
            {
                "type": "text",
                "title": "Invasion Narrative",
                "content": "*Hadüzenet nélkül rátámad az országra* ('attacks the country without declaration of war'), *drámai segélykiáltást intéz a világhoz* ('addresses a dramatic cry for help to the world'), *hősiesen ellenáll* ('heroically resists')."
            },
            {
                "type": "examples",
                "title": "November 4th events",
                "items": [
                    {
                        "spanish": "1956. november 4-én hajnalban a szovjet hadsereg hadüzenet nélkül támadta meg Budapestet.",
                        "english": "At dawn on November 4, 1956, the Soviet army attacked Budapest without a declaration of war."
                    },
                    {
                        "spanish": "Nagy Imre híres rádióbeszédében tudatta a világgal: 'Csapataink harcban állnak!'",
                        "english": "In his famous radio speech, Imre Nagy announced to the world: 'Our troops are in combat!'"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-otvenhat-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.otvenhat.05.martyrdom-and-legacy",
        "title": "Martyrdom & Historical Memory: mártírhalált hal, örökségét őrzi",
        "sections": [
            {
                "type": "text",
                "title": "Commemoration Registers",
                "content": "*Mártírhalált hal a hazájáért* ('dies a martyr's death for his homeland'), *nemzeti ünneppé nyilvánít* ('declares a national holiday'), *fejet hajt az áldozatok emléke előtt* ('bows head before the memory of the victims')."
            },
            {
                "type": "examples",
                "title": "Remembering 1956",
                "items": [
                    {
                        "spanish": "Nagy Imre és mártírtársai 1989-es újratemetése a rendszerváltás jelképes kezdete volt.",
                        "english": "The 1989 reburial of Imre Nagy and fellow martyrs was the symbolic beginning of the regime change."
                    },
                    {
                        "spanish": "Október 23-án a nemzet tisztelettel adózik az 1956-os forradalmárok emlékének.",
                        "english": "On October 23rd, the nation pays respectful tribute to the memory of the 1956 revolutionaries."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-otvenhat-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Stories (World / Rest-is-History Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.otvenhat.01",
        "lesson": 1,
        "order": 1,
        "title": "1956. október 23.: A szabadság hajnala",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On October 23, 1956, tens of thousands of university students marched in Budapest, carrying national flags with the Stalinist emblem cut out. They gathered at the Bem statue and the Parliament, demanding free elections and Soviet troop withdrawal. By nightfall, the colossal bronze Stalin monument was toppled, and the first shots were fired at the Hungarian Radio.",
        "characters": [
            "Műegyetemi diák tüntető",
            "Idős budapesti polgár",
            "Rádió előtti felkelő"
        ],
        "location": "Budapest, Bem tér, Kossuth tér és a Bródy Sándor utca",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1956. október 23-án délután tiszta őszi napsütés borította Budapestet. A Műegyetem udvaráról indultak el a fiatalok, kezükben a forradalom jelképévé vált lyukas zászlóval: a nemzeti piros-fehér-zöld trikolórból ollóval vágták ki a gyűlölt kommunista címert."
            },
            {
                "type": "dialogue",
                "speaker": "Műegyetemi diák",
                "text": "Magyarok vagyunk, nem szovjet gyarmat! Követeljük a szovjet csapatok azonnali kivonását, a szabad választásokat és az alapvető emberi jogokat!"
            },
            {
                "type": "narration",
                "text": "A Bem-szobornál felolvasták a tizenhat pontot, s a tömeg békésen vonult a Parlament elé. Estére több mint kétszázezer ember töltötte meg a Kossuth teret, kialudt fények mellett gyújtva meg újságpapírból a szabadság fáklyáit."
            },
            {
                "type": "dialogue",
                "speaker": "Idős budapesti polgár",
                "text": "Évtizedek óta nem láttam ilyet! A félelem jeges fala egyetlen délután alatt elolvadt! Idegenek ölelték át egymást az utcán, s együtt énekeltük a Himnuszt!"
            },
            {
                "type": "narration",
                "text": "A Városligetben a felkelők hegesztőpisztolyokkal és acélsodronyokkal döntötték le a 25 méteres bronz Sztálin-szobrot, amelyből csak a csizmák maradtak a talapzaton. Amikor a Magyar Rádió épületénél az ÁVH fegyveresei tüzet nyitottak a fegyvertelen tömegre, a békés tüntetés fegyveres forradalommá vált."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat-01-kitores.json", story_01)

    story_02 = {
        "id": "story.b1.otvenhat.02",
        "lesson": 2,
        "order": 2,
        "title": "A pesti srácok és a Corvin köz hősei",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Young apprentices, students, and workers—immortalized as the 'boys of Pest'—became the legendary backbone of armed resistance. Stationed at strategic intersections like the Corvin passage and Széna tér, they used homemade Molotov cocktails to destroy dozens of heavily armored Soviet tanks.",
        "characters": [
            "Pongrátz Gergely, a Corvin köz legendás parancsnoka",
            "Tizenöt éves pesti srác",
            "Vöröskeresztes ápolónő"
        ],
        "location": "A Corvin mozi környéke és az Üllői út",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesti utcák sarkaiból, a kapualjakból és a háztetőkről fiatalok ezrei léptek elő fegyverrel a kezükben. Sokan közülük még alig töltötték be a tizenöt-tizenhat évet: ők voltak a halhatatlan 'pesti srácok', a szabadságharc legbátrabb harcosai."
            },
            {
                "type": "dialogue",
                "speaker": "Tizenöt éves pesti srác",
                "text": "Nem félünk a tankoktól! Ha befordul a T-34-es az Üllői útról, a sarok mögül dobjuk a benzines palackot egyenesen a motortérre! Dávid és Góliát harca ez!"
            },
            {
                "type": "narration",
                "text": "A legfontosabb ellenállási gócpont a Corvin köz lett, a félköríves mozi védett épülete. Pongrátz Gergely parancsnoksága alatt a corvinisták valóságos erőddé változtatták a környéket, és tucatnyi szovjet páncélost lőttek ki a pesti aszfalton."
            },
            {
                "type": "dialogue",
                "speaker": "Pongrátz Gergely parancsnok",
                "text": "Itt nem zsoldosok harcolnak, hanem a magyar nemzet tiszta lelkiismerete! Addig tartjuk a Corvin közt, amíg az utolsó orosz tank is el nem hagyja a fővárost!"
            },
            {
                "type": "narration",
                "text": "A harcok szünetében az ablakokból ételt, kenyeret és forró teát adtak le a felkelőknek. A budapesti nép egysége megtörhetetlennek bizonyult: a szovjet csapatok október végén kénytelenek voltak visszavonulni a fővárosból."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat-02-pestisracok.json", story_02)

    story_03 = {
        "id": "story.b1.otvenhat.03",
        "lesson": 3,
        "order": 3,
        "title": "A győzelem napjai: Nagy Imre és a semlegesség",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Between October 28 and November 3, Hungary tasted true freedom. Prime Minister Imre Nagy formed a democratic coalition government, dissolved the ÁVH, restored the multi-party system, and declared Hungary's perpetual neutrality, renouncing the Warsaw Pact.",
        "characters": [
            "Nagy Imre, miniszterelnök",
            "Maléter Pál, honvédelmi miniszter",
            "Szabad budapesti újságíró"
        ],
        "location": "Budapest, Parlament és a Kilián laktanya",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Október utolsó napjaiban a forradalom győzött. Nagy Imre miniszterelnök a Parlament erkélyéről bejelentette a tűzszünetet, az ÁVH feloszlatását és a szovjet csapatok kivonulását a fővárosból."
            },
            {
                "type": "dialogue",
                "speaker": "Szabad budapesti újságíró",
                "text": "Csodálatos napok voltak! Újra megjelentek a független újságok, újjáalakultak a régi pártok: a Kisgazdák, a Szociáldemokraták, a Parasztpárt! Az emberek virágot tűztek a nemzetőrök puskáira!"
            },
            {
                "type": "narration",
                "text": "A kormány honvédelmi miniszterévé a bátor Maléter Pál ezredest nevezték ki, aki a felkelők oldalára állt Kilián laktanya parancsnokaként. November 1-jén Nagy Imre megtette a történelmi lépést: kikiáltotta Magyarország örökös semlegességét, és felmondta a Varsói Szerződést."
            },
            {
                "type": "dialogue",
                "speaker": "Nagy Imre miniszterelnök",
                "text": "A magyar nemzet nem kíván senkinek az ellensége lenni. Barátságban akarunk élni szomszédainkkal, szabadon, függetlenül, mint Ausztria vagy Svájc!"
            },
            {
                "type": "narration",
                "text": "Az ENSZ-hez fordultak védelemért, ám Moszkvában Hruscsov és a szovjet vezetés már titokban kiadta a parancsot a véres revánsra: a szabadság tavasza alig néhány napig tarthatott."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat-03-gyozelem.json", story_03)

    story_04 = {
        "id": "story.b1.otvenhat.04",
        "lesson": 4,
        "order": 4,
        "title": "A Forgószél hadművelet és a segélykiáltás (November 4.)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "At dawn on November 4, 1956, Soviet forces launched Operation Whirlwind with 2,000 tanks, brutally crushing the revolution. At 5:20 AM, Imre Nagy delivered his immortal radio message to the nation and the world. Despite desperate armed resistance in Csepel and the hills, freedom was overwhelmed by brute force.",
        "characters": [
            "Nagy Imre, miniszterelnök a mikrofon előtt",
            "Csepeli gyári munkás felkelő",
            "Szabad Európa Rádió tudósítója"
        ],
        "location": "A Magyar Rádió ideiglenes stúdiója és a csepeli gyártelep",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1956. november 4-én vasárnap hajnalban ágyúdörgés rázta meg a fővárost. A szovjet hadsereg kétezer harckocsival, hadüzenet nélkül megindította a 'Forgószél' hadműveletet a békés és semleges Magyarország ellen."
            },
            {
                "type": "dialogue",
                "speaker": "Nagy Imre miniszterelnök",
                "text": "Itt Nagy Imre beszél, a Magyar Népköztársaság Minisztertanácsának elnöke. Ma hajnalban a szovjet csapatok támadást indítottak fővárosunk ellen azzal a nyilvánvaló szándékkal, hogy megdöntsék a törvényes magyar kormányt. Csapataink harcban állnak! A kormány a helyén van! Ezt közlöm az ország népével és a világ közvéleményével!"
            },
            {
                "type": "narration",
                "text": "A drámai segélykiáltást több világnyelven is megismételték a rádióban, de a nyugati nagyhatalmak – a szuezi válság árnyékában – tétlenek maradtak. Magyarország magára maradt a roppant túlerővel szemben."
            },
            {
                "type": "dialogue",
                "speaker": "Csepeli munkás felkelő",
                "text": "A vörös Csepel munkásai az utolsó töltényig védik a gyárakat! Lehet, hogy legyőznek minket fegyverrel, de a lelkünket soha nem tudják meghódítani!"
            },
            {
                "type": "narration",
                "text": "Csepel, Kőbánya és a budai hegyek még napokig tartották magukat. A szabadságharcot végül eltiporták, de a magyar nép hősiessége megrengette a világot és leleplezte a szovjet birodalom embertelen arcát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat-04-invazio.json", story_04)

    story_05 = {
        "id": "story.b1.otvenhat.05",
        "lesson": 5,
        "order": 5,
        "title": "A kádári megtorlás és a forradalom öröksége",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Following the defeat, the Moscow-installed puppet regime of János Kádár executed over 350 patriots—including Imre Nagy and Pál Maléter on June 16, 1958—and imprisoned tens of thousands. Over 200,000 Hungarians fled into exile. On June 16, 1989, their historic reburial sealed the collapse of communism, establishing October 23rd as the free Republic's national holiday.",
        "characters": [
            "Kivégzésre váró mártír",
            "Nyugatra menekülő fiatal mérnök az osztrák határon",
            "1989-es budapesti szónok a Hősök terén"
        ],
        "location": "A budapesti Kozma utcai börtön, az andaui híd és a Hősök tere",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A szabadságharc leverése után Kádár János bábkormánya kíméletlen megtorlást indított. Több mint 350 forradalmárt végeztek ki – köztük a tizennyolc éves Mansfeld Pétert és a miniszterelnök Nagy Imrét –, és mintegy húszezer embert vetettek börtönbe."
            },
            {
                "type": "dialogue",
                "speaker": "Menekülő mérnök az andaui hídnál",
                "text": "Kétszázezer magyar ember kényszerült elhagyni a hazáját az aknamezőkön át vágva utat Ausztria felé. Magunkkal vittük a szabad Magyarország álmát a világ minden tájára."
            },
            {
                "type": "narration",
                "text": "A mártírokat jeltelen sírokban, összedrótozott kézzel kaparták el a rákoskeresztúri 301-es parcellában. Harminchárom éven át tilos volt még csak kiejteni is a forradalom szót a hivatalos sajtóban."
            },
            {
                "type": "narration",
                "text": "1989. június 16-án azonban a történelem igazságot szolgáltatott: a Hősök terén háromszázezer ember jelenlétében újratemették Nagy Imrét és mártírtársait. Ez a nap jelentette a kommunizmus erkölcsi és politikai bukását Magyarországon."
            },
            {
                "type": "dialogue",
                "speaker": "1989-es szónok a Hősök terén",
                "text": "Az 1956-os forradalom nem bukás volt, hanem a jövő záloga! A pesti srácok vére nyitotta meg az utat a mai szabad, demokratikus Magyar Köztársaság előtt!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat-05-megtorlas.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.otvenhat.combined",
        "title": "Az 1956-os forradalom és szabadságharc története (1956–1989)",
        "level": "B1",
        "order": 25,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive Rest is History synthesis of the 1956 Hungarian Revolution: from the student outbreak on October 23rd with the flag with a hole and toppling of Stalin, to the fierce street fighting of the 'boys of Pest' at Corvin köz, Imre Nagy's declaration of neutrality, the crushing Soviet invasion on November 4th, Kádár's brutal retribution, and the triumphant moral resurrection of June 16, 1989.",
        "characters": [
            "Nagy Imre és Maléter Pál mártírok",
            "Pongrátz Gergely és a pesti srácok",
            "Az 1956-os emigráció és az 1989-es rendszerváltó nemzedék"
        ],
        "location": "Budapest, Bem tér, Corvin köz, Országház és a Hősök tere",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1956. október 23-án a magyar nép megmutatta a világnak, hogy a szabadság vágya erősebb a legkegyetlenebb diktatúránál is. A budapesti egyetemisták békés felvonulása a Bem-szobortól a Parlamentig indult, a nemzeti zászlóból kivágva a kommunista címert."
            },
            {
                "type": "narration",
                "text": "Az ÁVH fegyveres provokációja után fegyvert ragadott a nép: a 'pesti srácok' és a Corvin köz harcosai Molotov-koktélokkal és hihetetlen bátorsággal állították meg a szovjet tankokat, kivívva az első győzelmet."
            },
            {
                "type": "narration",
                "text": "A megalakult Nagy Imre-kormány feloszlatta az ÁVH-t, visszaállította a többpártrendszert, és november 1-jén kikiáltotta Magyarország örökös semlegességét, felmondva a Varsói Szerződést."
            },
            {
                "type": "narration",
                "text": "1956. november 4-én azonban a Szovjetunió hadüzenet nélkül, kétezer harckocsival támadta meg Budapestet. A Forgószél hadművelet vérbe fojtotta a szabadságharcot, miközben Nagy Imre drámai segélykiáltása visszhangzott a szabad világ rádióiban."
            },
            {
                "type": "narration",
                "text": "A Kádár-rezsim véres megtorlása után Nagy Imrét és társait kivégezték, kétszázezer magyar pedig emigrációba kényszerült. Ám a forradalom szelleme legyőzhetetlen maradt: 1989. június 16-i újratemetésük megpecsételte a kommunista rendszer sorsát, október 23-át pedig a szabad Magyar Köztársaság nemzeti ünnepévé avatta."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-otvenhat.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        ex_data = {
            "lesson": f"b1-otvenhat-{padded}",
            "exercises": [
                {
                    "id": f"b1-otvenhat-{padded}.ex01",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik történelmi esemény kezdődött 1956. október 23-án Magyarországon?",
                    "options": [
                        "Az 1956-os forradalom és szabadságharc kitörése a szovjet elnyomás ellen.",
                        "A trianoni békeszerződés aláírása.",
                        "Az első világháború lezárása."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az egyetemisták tizenhat pontban foglalták _____ a nemzet legfőbb követeléseit. (summarized - össze)",
                    "answer": "össze"
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A forradalom legfőbb jelképévé a lyukas _____ vált, amelyből kivágták a címert. (flag - zászló)",
                    "answer": "zászló"
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex04",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "pesti", "srácok", "Molotov-koktélokkal", "szálltak", "szembe", "a", "szovjet", "tankokkal."],
                    "solution": ["A", "pesti", "srácok", "Molotov-koktélokkal", "szálltak", "szembe", "a", "szovjet", "tankokkal."]
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik fontos külpolitikai lépést tette meg Nagy Imre kormánya 1956. november 1-jén?",
                    "options": [
                        "Kikiáltotta Magyarország örökös semlegességét és kilépett a Varsói Szerződésből.",
                        "Katonai szövetséget kötött a Szovjetunióval a NATO ellen.",
                        "Hadüzenetet küldött az ENSZ Biztonsági Tanácsának."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "1956. november 4-én a szovjet hadsereg hadüzenet _____ támadt Budapestre. (without - nélkül)",
                    "answer": "nélkül"
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Nagy", "Imre", "mártírhalált", "halt", "a", "magyar", "nemzet", "szabadságáért."],
                    "solution": ["Nagy", "Imre", "mártírhalált", "halt", "a", "magyar", "nemzet", "szabadságáért."]
                },
                {
                    "id": f"b1-otvenhat-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért számít 1989. június 16-a a magyar rendszerváltás döntő pillanatának?",
                    "options": [
                        "Mert Nagy Imre és mártírtársai budapesti újratemetése a kommunista diktatúra erkölcsi bukását jelentette.",
                        "Mert ekkor vezették be a magyar forintot a gazdaságban.",
                        "Mert ekkor nyitották meg a Lánchidat a forgalom előtt."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-otvenhat-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-otvenhat-consolidation",
        "exercises": [
            {
                "id": "b1-otvenhat-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["október 23.", "forradalom kitörése és nemzeti ünnep"],
                    ["Corvin köz", "fegyveres ellenállás legendás központja"],
                    ["Nagy Imre", "semlegességet hirdető mártír miniszterelnök"],
                    ["november 4.", "szovjet invázió (Forgószél hadművelet)"]
                ]
            },
            {
                "id": "b1-otvenhat-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki pontosan az 1956-os nemzeti összefogást?",
                "options": [
                    "A magyar társadalom pártállástól függetlenül egy emberként állt ki a szabadság mellett.",
                    "A forradalmat kizárólag külföldi zsoldosok vívták meg.",
                    "A lakosság passzív maradt és bezárkózott a lakásokba."
                ],
                "correct": 0
            },
            {
                "id": "b1-otvenhat-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A harcok során a felkelők szétzúzták a Városligetben álló hatalmas Sztálin-_____. (statue - szobrot)",
                "answer": "szobrot"
            },
            {
                "id": "b1-otvenhat-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nagy Imre miniszterelnök drámai segélykiáltást in_____ a szabad világ népeihez. (addressed - tézett)",
                "answer": "tézett"
            },
            {
                "id": "b1-otvenhat-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "forradalom", "leverése", "után", "kétszázezer", "magyar", "menekült", "Nyugatra."],
                "solution": ["A", "forradalom", "leverése", "után", "kétszázezer", "magyar", "menekült", "Nyugatra."]
            },
            {
                "id": "b1-otvenhat-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kik voltak a 'pesti srácok'?",
                "options": [
                    "Azok a bátor fiatalok és tizenévesek, akik életüket kockáztatva harcoltak a pesti utcákon.",
                    "A budapesti opera gyermekkórusának énekesei.",
                    "Egy korabeli népszerű labdarúgócsapat játékosai."
                ],
                "correct": 0
            },
            {
                "id": "b1-otvenhat-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Október 23-a Magyarország legfontosabb nemzeti ünnepeinek egyi_____ lett 1989-ben. (one of them - ke)",
                "answer": "ke"
            },
            {
                "id": "b1-otvenhat-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan él tovább az 1956-os forradalom emléke a modern magyar alkotmányban és államiságban?",
                "options": [
                    "A szabad, demokratikus és független Magyarország erkölcsi fundamentumaként.",
                    "Kizárólag egy vitatott, felejtésre ítélt katonai kudarcként.",
                    "Egyetlen budapesti múzeum zárt kiállítási anyagaként."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-otvenhat-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A forradalom kitörése (Október 23.)", "The Outbreak of the Revolution"),
        "02": ("A pesti srácok és a fegyveres ellenállás", "The Boys of Pest & Corvin Passage"),
        "03": ("A győzelem napjai és a semlegesség", "Days of Victory, Imre Nagy & Neutrality"),
        "04": ("A szovjet invázió (November 4.)", "Soviet Invasion & the Cry for Help"),
        "05": ("Megtorlás és a forradalom öröksége", "Retribution, Exile & Reburial (1989)")
    }

    story_refs = {
        "01": "stories/world/b1/b1-otvenhat-01-kitores.json",
        "02": "stories/world/b1/b1-otvenhat-02-pestisracok.json",
        "03": "stories/world/b1/b1-otvenhat-03-gyozelem.json",
        "04": "stories/world/b1/b1-otvenhat-04-invazio.json",
        "05": "stories/world/b1/b1-otvenhat-05-megtorlas.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.otvenhat-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Directives of Freedom, Asymmetric Warfare & Sovereign Historical Discourse",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in the 1956 Hungarian Revolution.",
                        "I can use sovereign and commemorative registers of resistance and martyrdom in Hungarian.",
                        "I can answer essential citizenship interview questions regarding 1956, Imre Nagy, and October 23rd.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-otvenhat-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-otvenhat-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-otvenhat-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-otvenhat-{padded}.ex01",
                        f"b1-otvenhat-{padded}.ex02",
                        f"b1-otvenhat-{padded}.ex03",
                        f"b1-otvenhat-{padded}.ex04",
                        f"b1-otvenhat-{padded}.ex05",
                        f"b1-otvenhat-{padded}.ex06",
                        f"b1-otvenhat-{padded}.ex07",
                        f"b1-otvenhat-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-otvenhat-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.otvenhat-consolidation",
        "title": "Összefoglalás: Az 1956-os forradalom és szabadságharc (1956 Revolution Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of 1956 Revolutionary Memory, October 23rd & Democratic Heritage",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-otvenhat.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-otvenhat-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-otvenhat-consolidation.ex01",
                    "b1-otvenhat-consolidation.ex02",
                    "b1-otvenhat-consolidation.ex03",
                    "b1-otvenhat-consolidation.ex04",
                    "b1-otvenhat-consolidation.ex05",
                    "b1-otvenhat-consolidation.ex06",
                    "b1-otvenhat-consolidation.ex07",
                    "b1-otvenhat-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-otvenhat-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 25 (b1-otvenhat)!")

if __name__ == "__main__":
    build_unit_25_citizenship()
