#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 20: World War I & Collapse (b1-vilaghaboru)."""

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

def build_unit_20_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.vilaghaboru.01",
        "lesson": "b1-vilaghaboru-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szarajevói merénylet", "translation": "Sarajevo assassination (June 28, 1914)", "pos": "noun"},
            {"lemma": "hadüzenet", "translation": "declaration of war", "pos": "noun"},
            {"lemma": "mozgósítás", "translation": "military mobilization of troops", "pos": "noun"},
            {"lemma": "lelkesedés", "translation": "initial patriotic war enthusiasm", "pos": "noun"},
            {"lemma": "frontvonal", "translation": "front line, military combat zone", "pos": "noun"},
            {"lemma": "lövészárok", "translation": "combat trench (trench warfare)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-vilaghaboru-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.vilaghaboru.02",
        "lesson": "b1-vilaghaboru-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hátország", "translation": "home front (civilian population supporting the war)", "pos": "noun"},
            {"lemma": "jegyrendszer", "translation": "rationing system (food and supply cards)", "pos": "noun"},
            {"lemma": "hadigazdaság", "translation": "war economy (production geared for combat)", "pos": "noun"},
            {"lemma": "hadikölcsön", "translation": "war loan / war bond subscriptions", "pos": "noun"},
            {"lemma": "áruhiány", "translation": "shortage of consumer goods and food", "pos": "noun"},
            {"lemma": "női munkaerő", "translation": "female workforce replacing mobilized men", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-vilaghaboru-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.vilaghaboru.03",
        "lesson": "b1-vilaghaboru-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Doberdó-fennsík", "translation": "Doberdò plateau (infamous Italian karst front)", "pos": "noun"},
            {"lemma": "Isonzó-csata", "translation": "Battles of the Isonzo (twelve brutal clashes)", "pos": "noun"},
            {"lemma": "hősi halott", "translation": "heroic war dead (fallen soldiers)", "pos": "noun"},
            {"lemma": "hadifogság", "translation": "captivity as prisoner of war (POW in Russia/Italy)", "pos": "noun"},
            {"lemma": "sebesülés", "translation": "battlefield wound, combat injury", "pos": "noun"},
            {"lemma": "veszteséglista", "translation": "casualty list of dead, wounded and missing", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-vilaghaboru-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.vilaghaboru.04",
        "lesson": "b1-vilaghaboru-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "őszirózsás forradalom", "translation": "Aster Revolution of October 31, 1918", "pos": "noun"},
            {"lemma": "Károlyi Mihály", "translation": "Count Mihály Károlyi (prime minister, president)", "pos": "noun"},
            {"lemma": "katonatanács", "translation": "soldiers' council (mutinous revolutionary body)", "pos": "noun"},
            {"lemma": "köztársaság kikiáltása", "translation": "proclamation of the People's Republic (Nov 16, 1918)", "pos": "noun"},
            {"lemma": "fegyverszünet", "translation": "armistice, ceasefire agreement (Padua / Belgrade)", "pos": "noun"},
            {"lemma": "lemondás", "translation": "abdication / renunciation of state power (Charles IV)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-vilaghaboru-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.vilaghaboru.05",
        "lesson": "b1-vilaghaboru-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "történelmi összeomlás", "translation": "historical collapse of the Austro-Hungarian Empire", "pos": "noun"},
            {"lemma": "nemzetiségi elszakadás", "translation": "secession of non-Hungarian nationalities", "pos": "noun"},
            {"lemma": "demarkációs vonal", "translation": "demarcation line (allied advance borders)", "pos": "noun"},
            {"lemma": "bizonytalanság", "translation": "political and social uncertainty / chaos", "pos": "noun"},
            {"lemma": "nemzeti önrendelkezés", "translation": "national self-determination (Wilson's 14 Points)", "pos": "noun"},
            {"lemma": "történelmi korszakhatár", "translation": "epochal historical turning point (end of historical Hungary)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-vilaghaboru-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.vilaghaboru.01.past-counterfactual-history",
        "title": "Past Conditional in Historical Analysis: Ha nem történt volna meg a merénylet...",
        "sections": [
            {
                "type": "text",
                "title": "Analyzing Historical Alternatives with volna",
                "content": "To examine critical turning points in history: *Ha Tisza István meg tudta volna akadályozni a háborút, a Monarchia nem sodródott volna katasztrófába.* ('If István Tisza had been able to prevent the war, the Monarchy would not have drifted into catastrophe.')."
            },
            {
                "type": "examples",
                "title": "Counterfactual historical syntax",
                "items": [
                    {
                        "spanish": "Ha a trónörökös nem utazott volna Szarajevóba, elkerülhető lett volna a háború.",
                        "english": "If the heir to the throne had not travelled to Sarajevo, the war might have been avoidable."
                    },
                    {
                        "spanish": "Tisza István miniszterelnök kezdetben ellenezte a hadüzenetet a szerbeknek.",
                        "english": "Prime Minister István Tisza initially opposed the declaration of war against the Serbs."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-vilaghaboru-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.vilaghaboru.02.homefront-necessity",
        "title": "War Economy & Systemic Obligation: bevezetésre került, kénytelenek voltak",
        "sections": [
            {
                "type": "text",
                "title": "Describing Collective Hardships on the Home Front",
                "content": "Formal historical constructions for wartime rationing: *kénytelen volt + inf.* ('was forced to...'), *bevezetésre került* ('was instituted'): *A növekvő áruhiány miatt a kormány kénytelen volt bevezetni a szigorú jegyrendszert.*"
            },
            {
                "type": "examples",
                "title": "Home front expressions",
                "items": [
                    {
                        "spanish": "A hátország lakossága kénytelen volt nélkülözni a legalapvetőbb élelmiszereket is.",
                        "english": "The population of the home front was forced to do without even the most basic foodstuffs."
                    },
                    {
                        "spanish": "A gyárakban és a közlekedésben a női munkaerő vette át a bevonult férfiak helyét.",
                        "english": "In factories and transport, female labor took over the places of mobilized men."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-vilaghaboru-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.vilaghaboru.03.commemorating-sacrifice",
        "title": "Commemorating Sacrifice: életét áldozta, hadifogságba esett",
        "sections": [
            {
                "type": "text",
                "title": "Formulas for Wartime Remembrance",
                "content": "Respectful military and commemorative phrasing: *életét áldozta a hazáért* ('sacrificed one's life for the homeland'), *hadifogságba esett* ('fell into captivity as POW'), *súlyos sebesülést szenvedett* ('suffered a severe combat wound')."
            },
            {
                "type": "examples",
                "title": "Remembrance expressions",
                "items": [
                    {
                        "spanish": "Több mint hatszázezer magyar katona esett el a frontvonalakon hősi halottként.",
                        "english": "More than six hundred thousand Hungarian soldiers fell on the frontlines as heroic war dead."
                    },
                    {
                        "spanish": "A Doberdó szikláin a honvédek hősiesen védték a rájuk bízott állásokat.",
                        "english": "On the rocks of Doberdò, the Hungarian soldiers heroically defended the positions entrusted to them."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-vilaghaboru-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.vilaghaboru.04.proclamation-register",
        "title": "Revolutionary & Proclamation Syntax: kikiáltották a köztársaságot",
        "sections": [
            {
                "type": "text",
                "title": "Proclamations and Regime Change",
                "content": "Verbs of political rupture in 1918: *kikiáltják a független köztársaságot* ('proclaim the independent republic'), *megtagadja az engedelmességet* ('refuses obedience'), *fegyverszünetet köt* ('concludes an armistice')."
            },
            {
                "type": "examples",
                "title": "Revolutionary proclamation sentences",
                "items": [
                    {
                        "spanish": "1918. október 31-én az őszirózsás forradalom győzelmével Károlyi Mihály alakított kormányt.",
                        "english": "On October 31, 1918, with the victory of the Aster Revolution, Mihály Károlyi formed a government."
                    },
                    {
                        "spanish": "A katonák letépték a sapkájukról a császári címert, és őszirózsát tűztek a helyére.",
                        "english": "Soldiers ripped the imperial emblem from their caps and pinned an aster in its place."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-vilaghaboru-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.vilaghaboru.05.epochal-change",
        "title": "Epochal Rupture Connectors: megszűnt létezni, kezdetét vette",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Epochal Historical Ruptures",
                "content": "Describing the end of historical eras: *végérvényesen megszűnt létezni* ('definitively ceased to exist'), *új, tragikus fejezet vette kezdetét* ('a new, tragic chapter commenced'), *ennek következtében felbomlott a birodalom* ('consequently the empire dissolved')."
            },
            {
                "type": "examples",
                "title": "Epochal transformation syntax",
                "items": [
                    {
                        "spanish": "Az első világháború végén a történelmi Magyarország integritása végzetesen megrendült.",
                        "english": "At the end of the First World War, the integrity of historical Hungary was fatally shaken."
                    },
                    {
                        "spanish": "A nemzetiségek sorra kimondták az elszakadást és a csatlakozást a szomszédos államokhoz.",
                        "english": "The national minorities declared secession one after another and union with neighboring states."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-vilaghaboru-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Style, 5 lessons + combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.vilaghaboru.01",
        "title": "1914: A szarajevói lövés és a háborús láz",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In dramatic Rest is History style, we revisit June 28, 1914. Gavrilo Princip's shots in Sarajevo shatter European peace. While Vienna clamors for vengeance, Hungarian Prime Minister István Tisza initially resists the madness, before imperial momentum sweeps the nation into mobilization.",
        "characters": [
            "Tisza István miniszterelnök",
            "Ferenc József császár és király",
            "A pesti tömeg"
        ],
        "location": "Szarajevó, Bécs és Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1914. június 28-án délelőtt Szarajevóban két pisztolylövés dördült el. Ferenc Ferdinánd trónörökös meggyilkolásával a 20. század egyik legborzalmasabb gépezete indult be: a szarajevói merénylet lángra lobbantotta a puskaporos hordót."
            },
            {
                "type": "narration",
                "text": "Bécsben a katonai vezetés azonnal háborút követelt Szerbia ellen. Egyetlen ember mert nyíltan ellentmondani a császári udvarban: a magyar miniszterelnök, gróf Tisza István."
            },
            {
                "type": "dialogue",
                "speaker": "Tisza István miniszterelnök",
                "text": "Felség, nem szabad elhamarkodott döntést hoznunk! Egy Szerbia elleni támadás egész Európát lángba borítja, és Magyarországnak nincs mit nyernie egy világégésben!"
            },
            {
                "type": "narration",
                "text": "Ám a német császár feltétlen támogatása és a bécsi nyomás végül sarokba szorította Tiszát. Július 28-án megszületett a hadüzenet, és másnap Magyarországon is megkezdődött az általános mozgósítás."
            },
            {
                "type": "narration",
                "text": "A budapesti utcákon különös, szinte hisztérikus lelkesedés uralkodott. Fiatal diákok és munkások virágokkal díszített vonatokra szálltak, meggyőződve arról, hogy mire a falevelek lehullanak, győztesen térnek haza."
            },
            {
                "type": "dialogue",
                "speaker": "A pesti tömeg",
                "text": "Éljen a király! Megállj, megállj, kutya Szerbia! Néhány hét alatt rendet teszünk a Balkánon!"
            },
            {
                "type": "narration",
                "text": "Senki sem sejtette, hogy a vidám dalok nem a gyors győzelembe, hanem a modern történelem legvéresebb vágóhídjára, a frontvonal és a fagyos lövészárok poklába vezetik a nemzet ifjúságát."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru-01-hadbaindulas.json", story_01)

    story_02 = {
        "id": "story.b1.vilaghaboru.02",
        "lesson": 2,
        "order": 2,
        "title": "Élet a hátországban: jegyrendszer és hadikölcsön",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The reality of total war strikes civilian life. As the conflict drags on into 1916, Budapest faces severe rationing, shortages of flour and coal, and propaganda urging families to empty their pockets for war bonds while women sustain the city's factories and tramways.",
        "characters": [
            "Pesti háziasszony",
            "Banktisztviselő",
            "Villamosvezetőnő"
        ],
        "location": "Budapest, Nagykörút és a központi vásárcsarnok",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1916 telére a kezdeti naiv lelkesedésnek már nyoma sem maradt. A frontokon elakadtak a hadseregek, a küzdelem elhúzódott, és a háború kegyetlen terhei közvetlenül rászakadtak a hátország lakosságára."
            },
            {
                "type": "narration",
                "text": "A magyar ipart és mezőgazdaságot teljesen alárendelték a hadsereg szükségleteinek: megszületett a hadigazdaság. A boltok polcai kiürültek, és a kormány kénytelen volt bevezetni a szigorú jegyrendszer szabályait."
            },
            {
                "type": "dialogue",
                "speaker": "Pesti háziasszony",
                "text": "Hajnali négy óra óta állok sorban a fagyban a vásárcsarnok előtt, és a jegyemre csak fél kiló kukoricakenyeret és kevés zsírt kaphatok! Nincs szén, nincs cipő, már a rézkilincseket is be kellett szolgáltatnunk ágyúnak!"
            },
            {
                "type": "narration",
                "text": "A mindennapos áruhiány és a növekvő infláció ellenére a bankok és az újságok folyamatosan újabb és újabb hadikölcsön jegyzésére szólították fel a polgárokat, hogy a birodalom fedezni tudja a napi milliókba kerülő háborút."
            },
            {
                "type": "narration",
                "text": "A város képe gyökeresen átalakult: a bevonult férfiak helyét az üzemekben, a vasútnál és a kórházakban a bátor női munkaerő vette át. Nők vezették a villamosokat a Nagykörúton és szerelték a fegyvereket a csepeli gyárakban."
            },
            {
                "type": "dialogue",
                "speaker": "Villamosvezetőnő",
                "text": "A férjem a keleti fronton fagyoskodik, a kisfiam otthon éhes. Munkába álltam a villamosnál, mert a várost működtetni kell, és valakinek haza kell vinnie a kenyeret."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru-02-hatorszag.json", story_02)

    story_03 = {
        "id": "story.b1.vilaghaboru.03",
        "lesson": 3,
        "order": 3,
        "title": "Doberdó és az Isonzó pokla",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "On the brutal karst cliffs above the turquoise Isonzo River, Hungarian soldiers endure relentless artillery bombardments in the summer heat and winter ice. A poignant account of the Doberdò plateau, where hundreds of thousands sacrificed their lives.",
        "characters": [
            "Szegedi honvédtiszt",
            "Közkatona az Alföldről",
            "Tábori lelkész"
        ],
        "location": "Doberdó-fennsík és az Isonzó völgye, Olasz front",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Amikor Olaszország 1915-ben belépett a háborúba a Monarchia ellen, a déli határvidéken megnyílt a történelem egyik legvéresebb hadszíntere. Az Isonzó-csata tizenkét felvonásban tombolt az alpesi sziklák között."
            },
            {
                "type": "narration",
                "text": "A legfélelmetesebb helyszín a karszti Doberdó-fennsík volt. A kőkemény sziklákba nem lehetett árkokat ásni: az olasz tüzérségi gránátok felrobbantották magát a kőzetet, és a szétrepülő éles kőszilánkok borzalmas sebesüléseket okoztak."
            },
            {
                "type": "dialogue",
                "speaker": "Szegedi honvédtiszt",
                "text": "Kitartani, fiúk! A negyvenhatos szegedi bakák sosem hátrálnak meg! Ha elveszítjük ezt a fennsíkot, az ellenség közvetlenül Trieszt és a hazánk felé törhet előre!"
            },
            {
                "type": "narration",
                "text": "A katonák hetekig éltek víz nélkül a perzselő karszti hőségben, barakkok helyett barlangokban meghúzódva. A szörnyű küzdelemben minden magyar falu adott egy-egy hősi halottat, akinek neve ma is ott áll a helyi emlékműveken."
            },
            {
                "type": "narration",
                "text": "Sokan hadifogságba estek és Szibéria távoli lágereibe kerültek, míg otthon a családok rettegve nyitották ki az újságokat, ahol oldalakat töltött meg a végeláthatatlan veszteséglista."
            },
            {
                "type": "dialogue",
                "speaker": "Közkatona az Alföldről",
                "text": "Kimegyek a doberdói harctérre, feltekintek a csillagos nagy égre... Istenem, csak még egyszer láthassam a Tiszát és a szülőfalum harangtornyát!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru-03-doberdo.json", story_03)

    story_04 = {
        "id": "story.b1.vilaghaboru.04",
        "lesson": 4,
        "order": 4,
        "title": "1918 ősze: Az őszirózsás forradalom",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "October 1918 brings exhaustion and mutiny. As the front collapses, soldiers return to Budapest, ripping off imperial rosettes and pinning autumn asters to their caps. Crowds surge around Hotel Astoria, Károlyi Mihály forms a government, and Hungary declares a republic.",
        "characters": [
            "Károlyi Mihály",
            "Frontról visszatért katona",
            "Pesti egyetemista leány"
        ],
        "location": "Budapest, Astoria Szálló és az Országház tér",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1918 októberének végén a frontok végleg összeomlottak. A Monarchia katonailag vereséget szenvedett, a katonák százezrei hagyták el az állásokat, és indultak haza a kimerült, éhező birodalomba."
            },
            {
                "type": "narration",
                "text": "Budapesten az elégedetlenség forradalommá érlelődött. Október 30-án éjszaka a felkelő munkások és a megalakult katonatanács fegyveresei elfoglalták a város stratégiai pontjait: győzött az őszirózsás forradalom."
            },
            {
                "type": "dialogue",
                "speaker": "Frontról visszatért katona",
                "text": "Elég volt a vérontásból! Le a császári címerrel a sapkánkról! Tűzzetek a helyére fehér őszirózsát: békét és kenyeret akarunk!"
            },
            {
                "type": "narration",
                "text": "Az Astoria Szálló előtt tízezres tömeg ünnepelte gróf Károlyi Mihályt, akit a nép a béke és a polgári megújulás vezérének tartott. Károlyi kormánya azonnal megkötötte a fegyverszünet egyezményét, bízva a wilsoni igazságos békében."
            },
            {
                "type": "narration",
                "text": "1918. november közepén IV. Károly király eckartsaui nyilatkozatában bejelentette lemondását az államügyek intézéséről. Néhány nap múlva a Parlament előtt százezres tömeg éljenzése közepette megtörtént az első független köztársaság kikiáltása."
            },
            {
                "type": "dialogue",
                "speaker": "Károlyi Mihály",
                "text": "Polgárok! Négy év szenvedés után levetettük a háború bilincseit. Szabad, független és demokratikus Magyarországot építünk!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru-04-oszirozsa.json", story_04)

    story_05 = {
        "id": "story.b1.vilaghaboru.05",
        "lesson": 5,
        "order": 5,
        "title": "A birodalom alkonya és a széthullás",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The euphoria of peace quickly turns to dismay. Instead of Wilsonian self-determination, foreign armies cross the demarcation lines. The historical Kingdom of Hungary fractures as Romanians, Czechs, and Serbs take control of border territories, heralding an epochal turning point.",
        "characters": [
            "Magyar diplomata",
            "Erdélyi menekült tanár",
            "Kassai polgár"
        ],
        "location": "Kolozsvár, Kassa, Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A köztársaság kikiáltásának öröme tragikusan rövid ideig tartott. Az Osztrák–Magyar Monarchia történelmi összeomlása után nem a békés jólét, hanem a geopolitikai káosz időszaka köszöntött a Kárpát-medencére."
            },
            {
                "type": "narration",
                "text": "A nemzetiségi önrendelkezés elvére hivatkozva a szomszédos államok seregei átlépték a belgrádi fegyverszünet által kijelölt demarkációs vonalat. Román csapatok nyomultak Erdélybe, cseh légiók vonultak be a Felvidékre, szerb erők szállták meg a Délvidéket."
            },
            {
                "type": "dialogue",
                "speaker": "Erdélyi menekült tanár",
                "text": "El kellett hagynunk a kolozsvári otthonunkat. Egy marhavagonban érkeztünk Pestre. Nem hittük volna, hogy a háború vége a szülőföldünk elvesztését jelenti!"
            },
            {
                "type": "narration",
                "text": "A magyar hadsereg a forradalom után szétzilálódott, az ország védtelen maradt, és a gazdasági blokád miatt az egész társadalmat fojtogatta a kilátástalanság és a bizonytalanság."
            },
            {
                "type": "narration",
                "text": "A nemzetiségi elszakadás visszafordíthatatlan ténnyé vált. Ezeréves határok omlottak össze néhány hét leforgása alatt, kijelölve az utat a trianoni békediktátum felé."
            },
            {
                "type": "dialogue",
                "speaker": "Magyar diplomata",
                "text": "Ez a pillanat valódi történelmi korszakhatár. A régi Magyarország elenyészett a háború tüzében, és a nemzetnek a romokból kell újjáépítenie a jövőjét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru-05-osszeomlas.json", story_05)

    # Combined story for consolidation
    story_combined = {
        "id": "story.b1.vilaghaboru.combined",
        "title": "Az első világháború és a történelmi Magyarország széthullása",
        "level": "B1",
        "order": 20,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A gripping Rest is History narrative sweeping through 1914 to 1918: the fatal assassination in Sarajevo, the July crisis, the bloody trenches of Doberdò, the hardships of the home front, the Aster Revolution, and the dramatic collapse of the Dual Monarchy.",
        "characters": [
            "Tisza István és Károlyi Mihály miniszterelnökök",
            "Ferenc József és IV. Károly uralkodók",
            "A magyar honvédek és a hátország népe"
        ],
        "location": "Szarajevó, Bécs, Doberdó, Budapest, Kárpát-medence",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1914. június 28-án a szarajevói merénylet véget vetett a boldog békeidők korszakának. Bár Tisza István miniszterelnök hetekig küzdött a háború elkerüléséért, a Monarchia hadüzenetet küldött Szerbiának, és megindult az általános mozgósítás."
            },
            {
                "type": "narration",
                "text": "A kezdeti nemzeti lelkesedés hamar a rideg valóságba torkollott. A frontvonal merevvé vált, a katonák a lövészárok fagyos sarában rekedtek, miközben a hátországban a hadigazdaság és a szigorú jegyrendszer mindennapos áruhiányt és nélkülözést hozott."
            },
            {
                "type": "narration",
                "text": "A déli fronton a Doberdó-fennsík és az Isonzó-csata neve a borzalom szinonimájává vált: a sziklák között több százezer magyar katona vált hősi halottá, vagy került embertelen hadifogságba."
            },
            {
                "type": "narration",
                "text": "1918 őszén a kimerült frontok összeomlottak. Budapesten győzött a vértelen őszirózsás forradalom, Károlyi Mihály vezetésével kikiáltották a köztársaságot, míg az uralkodó, IV. Károly lemondott az államügyek intézéséről."
            },
            {
                "type": "narration",
                "text": "A megkötött fegyverszünet azonban nem hozott megnyugvást: a szomszédos államok csapatai átlépték a demarkációs vonalakat. A nemzetiségi elszakadás és a történelmi összeomlás nyomán a történelmi Magyarország korszaka végérvényesen lezárult."
            },
            {
                "type": "narration",
                "text": "Ez a négy esztendő alapjaiban formálta át Közép-Európa térképét és a magyar nemzet sorsát, megteremtve a modern 20. század máig ható történelmi kérdéseit."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-vilaghaboru.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-vilaghaboru-{padded}",
            "exercises": [
                {
                    "id": f"b1-vilaghaboru-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [
                        [curr_voc["words"][0]["lemma"], curr_voc["words"][0]["translation"]],
                        [curr_voc["words"][1]["lemma"], curr_voc["words"][1]["translation"]],
                        [curr_voc["words"][2]["lemma"], curr_voc["words"][2]["translation"]],
                        [curr_voc["words"][3]["lemma"], curr_voc["words"][3]["translation"]]
                    ]
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat elemzi helyesen az első világháborús eseményeket? (Lesson {i})",
                    "options": [
                        "Ha nem történt volna meg a merénylet, a Monarchia talán elkerülhette volna az összeomlást.",
                        "Ha nem merénylet lett volt, ezért nem háború van volt.",
                        "Mivel hadüzenet történt volna ezért tilos volt a katonáknak harcolni."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1914 júliusában az Osztrák–Magyar Monarchia ____ küldött Szerbiának. (declaration of war -t)",
                    "answer": "hadüzenetet"
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Ha Tisza István meg tudta volna akadályozni a háborút, nem veszett ____ annyi magyar honvéd. (would have - volna)",
                    "answer": "volna"
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelentett a jegyrendszer bevezetése a hátországban?",
                    "options": [
                        "Az élelmiszerek és alapvető áruk fejadagjának hatósági korlátozását és jegyekkel való elosztását.",
                        "Ingyenes színházjegyek biztosítását minden budapesti polgár számára.",
                        "A vasúti menetjegyek kötelező megvásárlását minden reggel."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "1918. október 31-én győzött az őszirózsás ____. (revolution)",
                    "answer": "forradalom"
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "Doberdó", "szikláin", "harcoló", "katonák", "hősies", "áldozatára", "örökre", "emlékezik", "a", "nemzet."],
                    "solution": ["A", "Doberdó", "szikláin", "harcoló", "katonák", "hősies", "áldozatára", "örökre", "emlékezik", "a", "nemzet."]
                },
                {
                    "id": f"b1-vilaghaboru-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik virág vált az 1918. október végi budapesti forradalom jelképévé?",
                    "options": [
                        "Az őszirózsa, amit a katonák a sapkájukra tűztek a császári címer helyett.",
                        "A piros tulipán, amit a városháza előtt osztogattak.",
                        "A fehér liliom, amit a miniszterelnök viselt a gomblyukában."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-vilaghaboru-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-vilaghaboru-consolidation",
        "exercises": [
            {
                "id": "b1-vilaghaboru-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szarajevói merénylet", "Sarajevo assassination"],
                    ["hátország", "home front"],
                    ["őszirózsás forradalom", "Aster Revolution"],
                    ["történelmi összeomlás", "historical collapse"]
                ]
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás összegzi hitelesen az első világháború következményeit Magyarország számára?",
                "options": [
                    "A háborús vereség a Monarchia felbomlásához és a történelmi Magyarország széthullásához vezetett.",
                    "Magyarország újabb területeket csatolt magához a Balkánon és Ausztriában.",
                    "A gazdaság gyorsabban virágzott a háború alatt, mint valaha a békeidőkben."
                ],
                "correct": 0
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A frontvonalon elesett katonákat tisztelettel ____ halottnak nevezi a történetírás. (heroic - hősi)",
                "answer": "hősi"
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársaság kikiáltása után a király lemondott az államügyek ____. (from directing - intézéséről)",
                "answer": "intézéséről"
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "első", "világháború", "tragikus", "történelmi", "korszakhatárt", "jelentett", "Magyarország", "életében."],
                "solution": ["Az", "első", "világháború", "tragikus", "történelmi", "korszakhatárt", "jelentett", "Magyarország", "életében."]
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki alakított kormányt 1918. október 31-én, a forradalom győzelmekor?",
                "options": [
                    "Gróf Károlyi Mihály",
                    "Tisza István",
                    "Horthy Miklós"
                ],
                "correct": 0
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szomszédos államok seregei átlépték a kijelölt ____ vonalakat. (demarcation - demarkációs)",
                "answer": "demarkációs"
            },
            {
                "id": "b1-vilaghaboru-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért kiemelkedő állampolgársági vizsgatéma az első világháború és az 1918-as összeomlás?",
                "options": [
                    "Mert közvetlenül megmagyarázza a Monarchia felbomlását és a trianoni békeszerződéshez vezető folyamatokat.",
                    "Mert ekkor vezették be az általános gépjárművezetési vizsgát Pesten.",
                    "Mert ekkor rendezték meg az első budapesti nemzetközi virágkiállítást."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-vilaghaboru-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Hadba indul a nemzet (1914)", "Hungary Goes to War"),
        "02": ("A hátország terhei és a mindennapok", "The Home Front"),
        "03": ("Doberdó és az Isonzó pokla", "Defeat & The Carnage"),
        "04": ("Az őszirózsás forradalom (1918)", "Revolution in Budapest"),
        "05": ("A birodalom felbomlása és a széthullás", "A Monarchy Ends")
    }

    story_refs = {
        "01": "stories/world/b1/b1-vilaghaboru-01-hadbaindulas.json",
        "02": "stories/world/b1/b1-vilaghaboru-02-hatorszag.json",
        "03": "stories/world/b1/b1-vilaghaboru-03-doberdo.json",
        "04": "stories/world/b1/b1-vilaghaboru-04-oszirozsa.json",
        "05": "stories/world/b1/b1-vilaghaboru-05-osszeomlas.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.vilaghaboru-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Past Conditional Volna in Historical Context, War Obligation & Epochal Connectors",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events, sacrifices and societal impacts of {en_t}.",
                        "I can analyze historical events using the past conditional (volna) in Hungarian.",
                        "I can answer citizenship exam questions about World War I and the collapse of the Monarchy.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-vilaghaboru-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-vilaghaboru-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-vilaghaboru-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-vilaghaboru-{padded}.ex01",
                        f"b1-vilaghaboru-{padded}.ex02",
                        f"b1-vilaghaboru-{padded}.ex03",
                        f"b1-vilaghaboru-{padded}.ex04",
                        f"b1-vilaghaboru-{padded}.ex05",
                        f"b1-vilaghaboru-{padded}.ex06",
                        f"b1-vilaghaboru-{padded}.ex07",
                        f"b1-vilaghaboru-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-vilaghaboru-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.vilaghaboru-consolidation",
        "title": "Összefoglalás: Az első világháború és a széthullás (World War I & Collapse Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of World War I History, the 1918 Aster Revolution & Empire Collapse",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-vilaghaboru.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-vilaghaboru-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-vilaghaboru-consolidation.ex01",
                    "b1-vilaghaboru-consolidation.ex02",
                    "b1-vilaghaboru-consolidation.ex03",
                    "b1-vilaghaboru-consolidation.ex04",
                    "b1-vilaghaboru-consolidation.ex05",
                    "b1-vilaghaboru-consolidation.ex06",
                    "b1-vilaghaboru-consolidation.ex07",
                    "b1-vilaghaboru-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-vilaghaboru-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 20 (b1-vilaghaboru)!")

if __name__ == "__main__":
    build_unit_20_citizenship()
