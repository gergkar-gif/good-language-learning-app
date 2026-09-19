#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 23: World War II in Hungary (b1-masodikvh)."""

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

def build_unit_23_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.masodikvh.01",
        "lesson": "b1-masodikvh-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hadba lépés", "translation": "entry into war (June 1941)", "pos": "noun"},
            {"lemma": "Kassa bombázása", "translation": "bombing of Kassa (unclarified air raid of June 26, 1941)", "pos": "noun"},
            {"lemma": "Bárdossy László", "translation": "László Bárdossy (Prime Minister who declared war)", "pos": "noun"},
            {"lemma": "hadüzenet", "translation": "declaration of war", "pos": "noun"},
            {"lemma": "keleti front", "translation": "Eastern Front", "pos": "noun"},
            {"lemma": "hadjárat", "translation": "military campaign", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-masodikvh-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.masodikvh.02",
        "lesson": "b1-masodikvh-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "doni katasztrófa", "translation": "catastrophe at the River Don (January 1943)", "pos": "noun"},
            {"lemma": "második magyar hadsereg", "translation": "Second Hungarian Army (nearly 100,000 casualties)", "pos": "noun"},
            {"lemma": "Jány Gusztáv", "translation": "General Gusztáv Jány (army commander at the Don)", "pos": "noun"},
            {"lemma": "fagyhalál", "translation": "freezing to death (in extreme minus 35-degree winter)", "pos": "noun"},
            {"lemma": "munkaszolgálat", "translation": "forced labor service (unarmed Jewish and political recruits)", "pos": "noun"},
            {"lemma": "hátországi gyász", "translation": "mourning and shock on the home front", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-masodikvh-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.masodikvh.03",
        "lesson": "b1-masodikvh-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "német megszállás", "translation": "German military occupation (March 19, 1944)", "pos": "noun"},
            {"lemma": "Margarethe hadművelet", "translation": "Operation Margarethe (Wehrmacht takeover of Hungary)", "pos": "noun"},
            {"lemma": "holokauszt", "translation": "Holocaust in Hungary (destruction of over 400,000 Hungarian Jews)", "pos": "noun"},
            {"lemma": "deportálás", "translation": "mass deportation to Auschwitz death camp", "pos": "noun"},
            {"lemma": "Raoul Wallenberg", "translation": "Raoul Wallenberg (Swedish diplomat and rescuer)", "pos": "noun"},
            {"lemma": "embermentők", "translation": "righteous rescuers (Wallenberg, Carl Lutz, Salkaházi Sára)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-masodikvh-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.masodikvh.04",
        "lesson": "b1-masodikvh-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kiugrási kísérlet", "translation": "breakout / armistice attempt (October 15, 1944)", "pos": "noun"},
            {"lemma": "rádióproklamáció", "translation": "Horthy's broadcast radio proclamation of armistice", "pos": "noun"},
            {"lemma": "nyilas hatalomátvétel", "translation": "Arrow Cross fascist coup backed by Nazi Germany", "pos": "noun"},
            {"lemma": "Szálasi Ferenc", "translation": "Ferenc Szálasi (Arrow Cross 'Leader of the Nation')", "pos": "noun"},
            {"lemma": "nyilas terror", "translation": "Arrow Cross terror and street massacres", "pos": "noun"},
            {"lemma": "Duna-parti cipők", "translation": "Shoes on the Danube Bank memorial", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-masodikvh-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.masodikvh.05",
        "lesson": "b1-masodikvh-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Budapest ostroma", "translation": "Siege of Budapest (102-day brutal urban battle)", "pos": "noun"},
            {"lemma": "romváros", "translation": "city reduced to ruins and rubble", "pos": "noun"},
            {"lemma": "hidak felrobbantása", "translation": "blowing up of Danube bridges by retreating German troops", "pos": "noun"},
            {"lemma": "Várnegyed", "translation": "Buda Castle District (final redoubt of the siege)", "pos": "noun"},
            {"lemma": "szovjet megszállás", "translation": "Soviet Red Army occupation of Hungary", "pos": "noun"},
            {"lemma": "málenkij robot", "translation": "'malenkiy robot' (forced labor deportation of civilians to USSR)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-masodikvh-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.masodikvh.01.causal-precipitating",
        "title": "Precipitating Causes: ürügyén, hatására, következtében",
        "sections": [
            {
                "type": "text",
                "title": "Casus Belli Formulations",
                "content": "To explain the triggers of historical events: *valaminek az ürügyén* ('under the pretext of sth'), *a provokáció hatására* ('under the impact of provocation'), *annak következtében, hogy...* ('as a consequence of the fact that...')."
            },
            {
                "type": "examples",
                "title": "Triggers of war",
                "items": [
                    {
                        "spanish": "Kassa máig tisztázatlan bombázásának ürügyén a kormány bejelentette a hadiállapotot.",
                        "english": "Under the pretext of the still-unclarified bombing of Kassa, the government announced a state of war."
                    },
                    {
                        "spanish": "A német nyomás hatására Magyarország belépett a Szovjetunió elleni hadjáratba.",
                        "english": "Under the impact of German pressure, Hungary entered the campaign against the Soviet Union."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-masodikvh-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.masodikvh.02.passive-catastrophe",
        "title": "Expressions of Catastrophe and Loss: áldozatul esik, pusztulásra van ítélve",
        "sections": [
            {
                "type": "text",
                "title": "Describing Tragic Collective Fates",
                "content": "Formal historical descriptions of catastrophe: *áldozatul esik* ('falls victim to'), *pusztulásra volt ítélve* ('was doomed to destruction'), *hiányos felszerelés következtében* ('due to deficient equipment')."
            },
            {
                "type": "examples",
                "title": "The Don disaster in memory",
                "items": [
                    {
                        "spanish": "A hiányosan felszerelt 2. magyar hadsereg tízezrei estek áldozatul a dermesztő orosz télben.",
                        "english": "Tens of thousands of the inadequately equipped 2nd Hungarian Army fell victim in the freezing Russian winter."
                    },
                    {
                        "spanish": "A doni katasztrófa a magyar hadtörténet egyik legsúlyosabb tragédiája maradt.",
                        "english": "The catastrophe at the Don remained one of the gravest tragedies in Hungarian military history."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-masodikvh-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.masodikvh.03.persecution-and-rescue",
        "title": "Persecution vs. Resistance: üldöztetés ellenére, életét kockáztatva",
        "sections": [
            {
                "type": "text",
                "title": "Concessive Participles of Heroism",
                "content": "Describing heroic resistance and moral choices: *életét kockáztatva* ('risking one's life'), *a deportálások ellenére* ('in spite of deportations'), *védelmet nyújtott üldözöttek ezreinek* ('provided shelter to thousands of persecuted people')."
            },
            {
                "type": "examples",
                "title": "Rescuers in the Holocaust",
                "items": [
                    {
                        "spanish": "Raoul Wallenberg svéd diplomata a saját életét kockáztatva mentett meg több tízezer embert.",
                        "english": "Swedish diplomat Raoul Wallenberg, risking his own life, saved tens of thousands of people."
                    },
                    {
                        "spanish": "Az embermentők bátor kiállása az emberiesség örök példája a sötétség idején.",
                        "english": "The courageous stance of the rescuers is an eternal example of humanity in a time of darkness."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-masodikvh-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.masodikvh.04.abortive-actions",
        "title": "Abortive Attempts: kísérletet tesz vmire, meghiúsul",
        "sections": [
            {
                "type": "text",
                "title": "Failed Coups and Crises",
                "content": "*Kísérletet tesz vmire* ('makes an attempt at sth'), *meghiúsul a terv* ('the plan is thwarted / fails'), *puccs útján magához ragadja a hatalmat* ('seizes power by means of a coup')."
            },
            {
                "type": "examples",
                "title": "The failed breakout",
                "items": [
                    {
                        "spanish": "Horthy kormányzó kísérletet tett a háborúból való kiugrásra, de a terv meghiúsult.",
                        "english": "Regent Horthy made an attempt to break out of the war, but the plan was thwarted."
                    },
                    {
                        "spanish": "A nyilasok német segítséggel ragadták magukhoz a hatalmat 1944 októberében.",
                        "english": "The Arrow Cross seized power with German assistance in October 1944."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-masodikvh-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.masodikvh.05.destruction-and-liberation",
        "title": "Rupture & Aftermath: romhalmazzá válik, megszállás alá kerül",
        "sections": [
            {
                "type": "text",
                "title": "Describing Devastating Destruction",
                "content": "*Romhalmazzá válik* ('turns into a pile of rubble'), *megszállás alá kerül* ('falls under occupation'), *kiszolgáltatott helyzetben* ('in a defenseless position')."
            },
            {
                "type": "examples",
                "title": "Post-siege conditions",
                "items": [
                    {
                        "spanish": "A hónapokig tartó véres ostrom során a gyönyörű főváros szinte romhalmazzá vált.",
                        "english": "During the months-long bloody siege, the beautiful capital turned almost entirely into a pile of rubble."
                    },
                    {
                        "spanish": "A lakosság tízezreit hurcolták el 'málenkij robotra' a Szovjetunió lágereibe.",
                        "english": "Tens of thousands of the population were dragged off for 'malenkiy robot' into the camps of the Soviet Union."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-masodikvh-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Stories (World / Rest-is-History Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.masodikvh.01",
        "lesson": 1,
        "order": 1,
        "title": "A hadba lépés tragédiája: Kassa bombázása (1941)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On June 26, 1941, unidentified aircraft bombed the city of Kassa. Within hours, Prime Minister László Bárdossy announced in Parliament that a state of war existed between Hungary and the Soviet Union, dragging the nation into the catastrophic vortex of World War II against Teleki Pál's desperate warnings.",
        "characters": [
            "Bárdossy László, miniszterelnök",
            "Kassai postatisztviselő",
            "Országgyűlési képviselő"
        ],
        "location": "Kassa főutcája és a budapesti Országház",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1941. június 26-án kora délután békés nyári napnak indult Kassán. Hirtelen ismeretlen felségjelzésű bombázók jelentek meg a felhők között, és halálos bombazáport zúdítottak a postapalotára és a lakónegyedekre."
            },
            {
                "type": "dialogue",
                "speaker": "Kassai postatisztviselő",
                "text": "Az ablakok darabokra törtek, a füst és a lángok elborították az utcát! Senki sem értette, kik voltak a támadók, és miért dobtak bombát a békés városra!"
            },
            {
                "type": "narration",
                "text": "Bár a gépek hovatartozása mindmáig a történettudomány egyik legnagyobb rejtélye, a magyar katonai vezetés azonnal a Szovjetuniót vádolta. Bárdossy László miniszterelnök még aznap bejelentette a parlamentben a hadiállapot beálltát."
            },
            {
                "type": "dialogue",
                "speaker": "Országgyűlési képviselő",
                "text": "Nem volt parlamenti vita, nem volt körültekintő vizsgálat! Néhány óra leforgása alatt Magyarország hadviselő féllé vált a világ legnagyobb szárazföldi háborújában!"
            },
            {
                "type": "narration",
                "text": "Teleki Pál volt miniszterelnök tragikus öngyilkossága és figyelmeztetése – 'bűnösök lettünk mások háborújában' – sajnos valóra vált: a magyar hadsereg megindult a keleti front felé, a katasztrófa útjára lépve."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh-01-hadbalepes.json", story_01)

    story_02 = {
        "id": "story.b1.masodikvh.02",
        "lesson": 2,
        "order": 2,
        "title": "A doni katasztrófa: Dermesztő pokol a Don-kanyarnál (1943)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In January 1943, the Soviet Red Army launched a massive winter offensive at the Don bend. The 200,000-strong 2nd Hungarian Army, strung out along a 200-kilometer front without adequate winter clothing or heavy anti-tank weapons, was obliterated in minus 35-degree cold.",
        "characters": [
            "Honvéd tizedes a Don-kanyarnál",
            "Munkaszolgálatos orvos",
            "Gyászoló édesanya a hátországban"
        ],
        "location": "A Don-kanyar hófúvásai és egy alföldi falu",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1943 januárjában a Don folyó partján a hőmérséklet mínusz 35 fok alá süllyedt. A 2. magyar hadsereg katonái vékony posztóköpenyben, fagytól elgémberedett ujjakkal próbálták tartani a hatalmas, kétszáz kilométeres védelmi vonalat."
            },
            {
                "type": "dialogue",
                "speaker": "Honvéd tizedes",
                "text": "A puskák zárszerkezete belefagyott a géppisztolyba, a motorok olaja jéggé dermedt! Amikor a szovjet T-34-es harckocsik áttörték a vonalat Urivnál, nem volt mivel megállítani őket!"
            },
            {
                "type": "narration",
                "text": "A doni áttörés napjaiban százezren haltak meg, sebesültek meg vagy estek szovjet hadifogságba. Velük együtt pusztultak el a fegyvertelen zsidó munkaszolgálatosok tízezrei is, akiket embertelen körülmények között vezényeltek aknaszedésre."
            },
            {
                "type": "dialogue",
                "speaker": "Munkaszolgálatos orvos",
                "text": "A hóviharban nem volt különbség katona és munkaszolgálatos között: a fehér halál mindannyiunkat egyformán fenyegetett. Csak az egymásba kapaszkodó emberiesség maradt meg."
            },
            {
                "type": "narration",
                "text": "A doni katasztrófa híre mély fekete gyászba borította a magyar családokat. Nem volt olyan falu vagy város, ahol ne sirattak volna apát, fiút vagy testvért. A Don neve örökre a magyar nemzet egyik legfájóbb Golgotájává vált."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh-02-doni.json", story_02)

    story_03 = {
        "id": "story.b1.masodikvh.03",
        "lesson": 3,
        "order": 3,
        "title": "A német megszállás és az embermentők helytállása (1944)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On March 19, 1944, Hitler launched Operation Margarethe, occupying Hungary. Under the direction of Adolf Eichmann, over 430,000 rural Hungarian Jews were deported to Auschwitz within weeks. Amidst this dark abyss, brave rescuers like Raoul Wallenberg, Carl Lutz, and Sára Salkaházi risked their lives to save tens of thousands.",
        "characters": [
            "Raoul Wallenberg, svéd diplomata",
            "Budapesti védett ház lakója",
            "Salkaházi Sára nővér"
        ],
        "location": "Budapest, Svéd Nagykövetség és a nemzetközi gettó",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1944. március 19-én reggel a budapestiek arra ébredtek, hogy a hidakon és a pályaudvarokon német Wehrmacht-katonák és páncélosok állnak őrt. Megkezdődött a Margarethe-hadművelet: Magyarország elveszítette szuverenitását."
            },
            {
                "type": "narration",
                "text": "A náci megszállókkal együtt megérkezett Adolf Eichmann különítménye. A kollaboráns magyar hatóságok segítségével alig néhány hét alatt több mint 430 000 vidéki magyar zsidó honfitársunkat vagonírozták be és deportálták az auschwitzi haláltáborba."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti védett ház lakója",
                "text": "A sárga csillag kötelezővé vált, a gettó falai bezárultak. Minden nap rettegésben telt: mikor jönnek a nyilasok vagy a Gestapo, hogy elhurcoljanak?"
            },
            {
                "type": "narration",
                "text": "A legsötétebb órákban felragyogott a tiszta emberiesség fénye. Raoul Wallenberg svéd diplomata svéd védőleveleket (Schutzpass) osztott, menedékházakat hozott létre, és személyesen rángatott le embereket a halálvonatokról."
            },
            {
                "type": "dialogue",
                "speaker": "Raoul Wallenberg",
                "text": "Számomra nem létezik más választás: amíg egyetlen embert is meg tudok menteni, addig itt maradok Budapesten! Az emberi méltóság védelme nem ismer nemzeti vagy diplomáciai határokat!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh-03-megszallas.json", story_03)

    story_04 = {
        "id": "story.b1.masodikvh.04",
        "lesson": 4,
        "order": 4,
        "title": "A kiugrási kísérlet és a nyilas rémuralom (1944. október)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On October 15, 1944, Regent Miklós Horthy broadcast a dramatic radio proclamation announcing an armistice with the Soviet Union. However, the German SS kidnapped his son, backed an Arrow Cross fascist coup led by Ferenc Szálasi, and unleashed a reign of terror culminating in Danube bank massacres.",
        "characters": [
            "Rádióbemondó a Magyar Rádiónál",
            "Nyilas keretlegény",
            "Üldözött pesti diák"
        ],
        "location": "Budapest, Magyar Rádió (Bródy Sándor utca) és a Duna-part",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1944. október 15-én délután egy órakor megállt a szívverés Budapesten. A Magyar Rádió adását megszakították, és felhangzott Horthy Miklós kormányzó megrázó proklamációja: 'A mai napon fegyverszünetet kértem az ellenfeleinktől... a háborút elvesztettük!'"
            },
            {
                "type": "dialogue",
                "speaker": "Üldözött pesti diák",
                "text": "Amikor meghallottuk a bejelentést, sírtunk a megkönnyebbüléstől. Azt hittük, vége a mészárlásnak, a békés jövő kapujában állunk!"
            },
            {
                "type": "narration",
                "text": "A remény azonban alig néhány óráig élt. A német titkosszolgálat elrabolta a kormányzó fiát, Horthyt zsarolással lemondatták, és a hatalmat a Szálasi Ferenc vezette Nyilaskeresztes Párt vette át. Budapest utcáit elárasztotta a zöldinges nyilas terror."
            },
            {
                "type": "dialogue",
                "speaker": "Rádióbemondó",
                "text": "Néhány órával később már a nyilas parancsokat kellett beolvasnunk: a harcot az utolsó töltényig folytatni kell! A város egyetlen pillanat alatt a pokol tornácára került."
            },
            {
                "type": "narration",
                "text": "A nyilas banditák ezreket lőttek a jeges Duna habjaiba a pesti alsó rakparton. A parton hagyott üres vascipők – a ma világszerte ismert megrázó emlékmű – az ártatlan áldozatok örök mementójaként hirdetik a fasiszta őrület pusztítását."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh-04-nyilas.json", story_04)

    story_05 = {
        "id": "story.b1.masodikvh.05",
        "lesson": 5,
        "order": 5,
        "title": "Budapest ostroma és a háború vége (1944–1945)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The Siege of Budapest was one of the deadliest urban battles of WWII, lasting 102 days. The city was pulverized, all historic Danube bridges were blown up by retreating German forces, and hundreds of thousands hid in basements. Liberation from fascism was immediately followed by Soviet occupation and deportations to forced labor camps.",
        "characters": [
            "Budai óvóhelyen rejtőzködő anya",
            "Műegyetemi mérnökhallgató",
            "Visszatérő budapesti lakos a romok között"
        ],
        "location": "A Gellért-hegy barlangjai, Lánchíd romjai és a Várnegyed",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1944 karácsonyán a Vörös Hadsereg teljesen bekerítette Budapestet. Hitler parancsára a fővárost erőddé (Festung Budapest) nyilvánították: házról házra, emeletről emeletre folyt a kíméletlen harc a romok között."
            },
            {
                "type": "dialogue",
                "speaker": "Budai óvóhelyen rejtőzködő anya",
                "text": "Ötven napon át éltünk a sötét pincében villany, fűtés és víz nélkül. Odafenn éjjel-nappal robbantak a bombák és a tüzérségi lövedékek. A gyermekemnek hólevet olvasztottam, hogy ne haljon szomjan."
            },
            {
                "type": "narration",
                "text": "1945 januárjában a visszavonuló német csapatok sorra a levegőbe repítették a főváros büszkeségeit: a Lánchidat, az Erzsébet hidat, a Margit hidat és a Széchenyi-emlékeket. A Duna partján fekete acélcsonkok meredtek a jégtáblák közé."
            },
            {
                "type": "dialogue",
                "speaker": "Műegyetemi mérnökhallgató",
                "text": "Amikor végre feljöttünk az óvóhelyről, rá sem ismertünk a szülővárosunkra. A Várnegyed füstölgő romhalmaz volt, a pesti körút romokban hevert, a halottakat a parkokban kellett eltemetni."
            },
            {
                "type": "narration",
                "text": "A náci elnyomás alóli felszabadulás azonban nem hozott valódi szabadságot. A szovjet hatóságok civilek tízezreit hurcolták el 'málenkij robotra' (kis munkára) a távoli gulág-táborokba. Magyarországon véget ért a háború, de megkezdődött a szovjet megszállás nehéz korszaka."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh-05-ostrom.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.masodikvh.combined",
        "title": "Magyarország a második világháborúban: Hadba lépés, holokauszt és ostrom (1941–1945)",
        "level": "B1",
        "order": 23,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive Rest is History narrative synthesizing Hungary's tragedy in World War II: entry into the war following the bombing of Kassa, the catastrophic freezing defeat of the 2nd Army at the Don, German military occupation (March 1944) and the Holocaust, the failed October armistice attempt followed by Arrow Cross terror, and the apocalyptic 102-day Siege of Budapest.",
        "characters": [
            "Bárdossy László és Teleki Pál miniszterelnökök",
            "A doni katasztrófa honvédei és munkaszolgálatosai",
            "Raoul Wallenberg és az embermentők",
            "Budapest ostromának civil túlélői"
        ],
        "location": "Kassa, a Don-kanyar, Auschwitz és Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország a második világháborúban a 20. század legsúlyosabb nemzeti és emberi katasztrófáját szenvedte el. Bár Teleki Pál kormánya igyekezett megőrizni a fegyveres semlegességet, 1941 júniusában, Kassa máig tisztázatlan bombázása után az ország belépett a Szovjetunió elleni hadjáratba."
            },
            {
                "type": "narration",
                "text": "1943 januárjában a Don-kanyarnál bekövetkezett a nemzeti tragédia: a felkészületlen, hiányos felszerelésű 2. magyar hadsereg megsemmisült a mínusz 35 fokos fagyban és a szovjet áttörésben, több mint százezer ember halálát vagy fogságát okozva."
            },
            {
                "type": "narration",
                "text": "1944. március 19-én a náci Németország megszállta Magyarországot. Néhány hónap alatt több mint 430 ezer vidéki magyar zsidót deportáltak Auschwitzba. Ebben a sötétségben Raoul Wallenberg, Carl Lutz és magyar segítőik ezrek életét mentették meg védőlevelekkel és bátor kiállással."
            },
            {
                "type": "narration",
                "text": "1944. október 15-én Horthy kormányzó kiugrási kísérlete meghiúsult. A hatalmat a nyilasok vették át, akik tomboló terrort zúdítottak a fővárosra, védtelen áldozatok ezreit lőve a Duna hullámaiba a pesti rakparton."
            },
            {
                "type": "narration",
                "text": "A 102 napos budapesti ostromban a Dunába robbantott hidakkal a gyönyörű főváros romhalmazzá vált. A náci rémuralom véget ért, ám a szovjet megszállás és a málenkij robotra hurcolt ártatlanok tragédiája egy új, elnyomó korszak kezdetét jelezte."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-masodikvh.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        ex_data = {
            "lesson": f"b1-masodikvh-{padded}",
            "exercises": [
                {
                    "id": f"b1-masodikvh-{padded}.ex01",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik esemény szolgált közvetlen ürügyül Magyarország 1941-es hadba lépéséhez?",
                    "options": [
                        "Kassa máig tisztázatlan bombázása 1941. június 26-án.",
                        "A versailles-i békekonferencia megnyitása.",
                        "A budapesti metró építésének leállítása."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A provokáció hatás_____ a miniszterelnök bejelentette a hadiállapot beálltát. (under the impact of - ára)",
                    "answer": "ára"
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1943 januárjában a Don-kanyarnál tízezrek estek fagy_____ áldozatául. (freezing death - halál)",
                    "answer": "halál"
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex04",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "doni", "katasztrófa", "a", "magyar", "hadtörténet", "egyik", "legsúlyosabb", "tragédiája."],
                    "solution": ["A", "doni", "katasztrófa", "a", "magyar", "hadtörténet", "egyik", "legsúlyosabb", "tragédiája."]
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Ki volt Raoul Wallenberg a második világháború alatt Budapesten?",
                    "options": [
                        "Svéd diplomata, aki saját életét kockáztatva zsidók tízezreit mentette meg.",
                        "A német megszálló hadsereg főparancsnoka.",
                        "A szovjet Vörös Hadsereg tüzérségi tábornoka."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Horthy kormányzó kiugrási kísérlete a német túlerő miatt sajnos meghiú_____. (was thwarted / failed - sult)",
                    "answer": "sult"
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "Duna-parti", "cipők", "emlékműve", "a", "nyilas", "terror", "áldozataira", "emlékeztet."],
                    "solution": ["A", "Duna-parti", "cipők", "emlékműve", "a", "nyilas", "terror", "áldozataira", "emlékeztet."]
                },
                {
                    "id": f"b1-masodikvh-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hány napig tartott Budapest ostroma a második világháború végén?",
                    "options": [
                        "102 napig tartott a véres ostrom a romvárossá vált fővárosban.",
                        "Mindössze három nap alatt ért véget harcok nélkül.",
                        "Több mint öt évig folyamatosan bombázták a várost."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-masodikvh-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-masodikvh-consolidation",
        "exercises": [
            {
                "id": "b1-masodikvh-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Kassa bombázása", "1941. június 26."],
                    ["doni katasztrófa", "1943. január"],
                    ["német megszállás", "1944. március 19."],
                    ["kiugrási kísérlet", "1944. október 15."]
                ]
            },
            {
                "id": "b1-masodikvh-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás foglalja össze legpontosabban a 2. magyar hadsereg doni katasztrófáját?",
                "options": [
                    "A hiányos felszerelésű hadsereg megsemmisült a dermesztő orosz télben és a szovjet áttörésben.",
                    "A magyar hadsereg döntő és gyors győzelmet aratott Moszkva alatt.",
                    "A katonák harc nélkül visszavonultak a Dunántúlra pihenni."
                ],
                "correct": 0
            },
            {
                "id": "b1-masodikvh-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1944 tavaszán több mint 430 ezer vidéki magyar zsidót depor_____ az auschwitzi lágerekbe. (deported - táltak)",
                "answer": "táltak"
            },
            {
                "id": "b1-masodikvh-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Saját életét kockáz____ mentette az üldözötteket Raoul Wallenberg. (risking - tatva)",
                "answer": "tatva"
            },
            {
                "id": "b1-masodikvh-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "visszavonuló", "német", "csapatok", "felrobbantották", "a", "budapesti", "Duna-hidakat."],
                "solution": ["A", "visszavonuló", "német", "csapatok", "felrobbantották", "a", "budapesti", "Duna-hidakat."]
            },
            {
                "id": "b1-masodikvh-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelentett a 'málenkij robot' a háború végén?",
                "options": [
                    "Magyar civilek tízezreinek kényszermunkára hurcolását a Szovjetunió munkatáboraiba.",
                    "Egy új típusú szovjet aratógép bemutatóját.",
                    "A budapesti gyárakban végzett önkéntes vasárnapi műszakot."
                ],
                "correct": 0
            },
            {
                "id": "b1-masodikvh-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hónapokig tartó ostrom során Budapest szinte rom_____ vált. (pile of ruins - halmazzá)",
                "answer": "halmazzá"
            },
            {
                "id": "b1-masodikvh-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan értékeli a modern magyar történetírás Magyarország második világháborús szereplését?",
                "options": [
                    "Nemzeti tragédiaként, amelyben az ország szuverenitását elveszítve hatalmas emberi és anyagi áldozatot hozott.",
                    "Kizárólag dicsőséges és sikeres katonai vállalkozásként.",
                    "Jelentéktelen helyi konfliktusként Európa peremén."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-masodikvh-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A hadba lépés tragédiája", "Entry into War & Bombing of Kassa (1941)"),
        "02": ("A doni katasztrófa", "The Don Catastrophe & Forced Labor (1943)"),
        "03": ("A német megszállás és a holokauszt", "German Occupation & Rescuers (1944)"),
        "04": ("Kiugrási kísérlet és nyilas terror", "Failed Armistice & Arrow Cross Terror"),
        "05": ("Budapest ostroma és a háború vége", "Siege of Budapest & Soviet Occupation")
    }

    story_refs = {
        "01": "stories/world/b1/b1-masodikvh-01-hadbalepes.json",
        "02": "stories/world/b1/b1-masodikvh-02-doni.json",
        "03": "stories/world/b1/b1-masodikvh-03-megszallas.json",
        "04": "stories/world/b1/b1-masodikvh-04-nyilas.json",
        "05": "stories/world/b1/b1-masodikvh-05-ostrom.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.masodikvh-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Causal Triggers, Tragedy Descriptors & Historical Memorial Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungary's WWII history.",
                        "I can use historical connectors of causality, catastrophe, and resistance in Hungarian.",
                        "I can answer essential citizenship interview questions regarding WWII, the Holocaust, and Budapest's siege.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-masodikvh-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-masodikvh-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-masodikvh-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-masodikvh-{padded}.ex01",
                        f"b1-masodikvh-{padded}.ex02",
                        f"b1-masodikvh-{padded}.ex03",
                        f"b1-masodikvh-{padded}.ex04",
                        f"b1-masodikvh-{padded}.ex05",
                        f"b1-masodikvh-{padded}.ex06",
                        f"b1-masodikvh-{padded}.ex07",
                        f"b1-masodikvh-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-masodikvh-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.masodikvh-consolidation",
        "title": "Összefoglalás: A második világháború Magyarországon (World War II in Hungary Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of WWII Historical Memory, the Holocaust & the Siege of Budapest",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-masodikvh.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-masodikvh-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-masodikvh-consolidation.ex01",
                    "b1-masodikvh-consolidation.ex02",
                    "b1-masodikvh-consolidation.ex03",
                    "b1-masodikvh-consolidation.ex04",
                    "b1-masodikvh-consolidation.ex05",
                    "b1-masodikvh-consolidation.ex06",
                    "b1-masodikvh-consolidation.ex07",
                    "b1-masodikvh-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-masodikvh-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 23 (b1-masodikvh)!")

if __name__ == "__main__":
    build_unit_23_citizenship()
