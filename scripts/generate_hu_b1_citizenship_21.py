#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 21: The Treaty of Trianon (b1-trianon)."""

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

def build_unit_21_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.trianon.01",
        "lesson": "b1-trianon-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "békedelegáció", "translation": "peace delegation (Hungarian mission to Neuilly/Paris)", "pos": "noun"},
            {"lemma": "Apponyi Albert", "translation": "Count Albert Apponyi (leader of the peace delegation)", "pos": "noun"},
            {"lemma": "vörös térkép", "translation": "'Red Map' (Teleki Pál's ethnographic map of Hungarians)", "pos": "noun"},
            {"lemma": "etnikai elv", "translation": "ethnic principle / self-determination principle", "pos": "noun"},
            {"lemma": "történelmi érv", "translation": "historical argument / geocultural unity", "pos": "noun"},
            {"lemma": "békediktátum", "translation": "peace diktat (treaty imposed without mutual negotiation)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-trianon-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.trianon.02",
        "lesson": "b1-trianon-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nagy Trianon kastély", "translation": "Grand Trianon Palace at Versailles", "pos": "noun"},
            {"lemma": "aláírás", "translation": "signing of the peace treaty (June 4, 1920)", "pos": "noun"},
            {"lemma": "területelcsatolás", "translation": "annexation / detachment of historical territories", "pos": "noun"},
            {"lemma": "új államhatárok", "translation": "new state borders partitioning the Carpathian Basin", "pos": "noun"},
            {"lemma": "gyászharang", "translation": "mourning bell (tolled across Hungary at 16:32)", "pos": "noun"},
            {"lemma": "nemzeti tragédia", "translation": "national tragedy", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-trianon-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.trianon.03",
        "lesson": "b1-trianon-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "határon túli magyarok", "translation": "Hungarians beyond the borders (transborder communities)", "pos": "noun"},
            {"lemma": "kisebbségi sors", "translation": "minority fate / existence in successor states", "pos": "noun"},
            {"lemma": "anyanyelvhasználat", "translation": "right to use one's native mother tongue", "pos": "noun"},
            {"lemma": "kettős identitás", "translation": "dual identity (Hungarian cultural & state civic identity)", "pos": "noun"},
            {"lemma": "magyar iskola", "translation": "native-language Hungarian schooling institution", "pos": "noun"},
            {"lemma": "nemzetiségi elnyomás", "translation": "ethnic discrimination and minority rights restrictions", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-trianon-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.trianon.04",
        "lesson": "b1-trianon-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vagonlakók", "translation": "'wagon dwellers' (refugee families living in rail cars)", "pos": "noun"},
            {"lemma": "menekülthullám", "translation": "refugee wave (civil servants, teachers fleeing to rump Hungary)", "pos": "noun"},
            {"lemma": "trauma", "translation": "collective historical trauma and grief", "pos": "noun"},
            {"lemma": "revízió", "translation": "territorial revision (peaceful border correction policy)", "pos": "noun"},
            {"lemma": "irredentizmus", "translation": "irredentism ('Nem, nem, soha!' movement)", "pos": "noun"},
            {"lemma": "országgyarapítás", "translation": "territorial regain (brief re-annexations 1938–41)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-trianon-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.trianon.05",
        "lesson": "b1-trianon-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nemzeti Összetartozás Napja", "translation": "Day of National Unity (memorialized on June 4th since 2010)", "pos": "noun"},
            {"lemma": "összetartozás", "translation": "solidarity / sense of belonging to one undivided nation", "pos": "noun"},
            {"lemma": "történelmi emlékezet", "translation": "historical memory and dignified commemoration", "pos": "noun"},
            {"lemma": "kulturális egység", "translation": "cultural unity transcending geopolitical state borders", "pos": "noun"},
            {"lemma": "megbékélés", "translation": "reconciliation and mutual respect among neighboring nations", "pos": "noun"},
            {"lemma": "Kárpát-medencei együttműködés", "translation": "Carpathian Basin regional cooperation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-trianon-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.trianon.01.causal-consequence-treaty",
        "title": "Cause, Result & Treaty Arguments: emiatt, abból a célból, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Explaining Historical Negotiations",
                "content": "In presenting diplomatic cases: *emiatt* ('due to this'), *annak érdekében, hogy...* ('in order that...'): *Apponyi Albert azért beszélt három világnyelven, hogy a győztes hatalmak megértsék a magyar érveket.*"
            },
            {
                "type": "examples",
                "title": "Diplomatic argumentation syntax",
                "items": [
                    {
                        "spanish": "Teleki Pál vörös térképe pontosan bemutatta a Kárpát-medence nemzetiségi arányait.",
                        "english": "Pál Teleki's Red Map accurately demonstrated the ethnic proportions of the Carpathian Basin."
                    },
                    {
                        "spanish": "A békedelegáció történelmi és gazdasági érvekkel próbálta meggyőzni a döntéshozókat.",
                        "english": "The peace delegation attempted to convince decision-makers with historical and economic arguments."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-trianon-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.trianon.02.passive-avoidance-treaty",
        "title": "Formal Treaty Register: elcsatolásra került, kötelezték Magyarországot",
        "sections": [
            {
                "type": "text",
                "title": "Official Decisions and Impositions",
                "content": "Historical decisions imposed on a state: *kötelezték Magyarországot arra, hogy...* ('they obligated Hungary to...'), *elcsatolásra került az ország kétharmada* ('two-thirds of the country was annexed/detached')."
            },
            {
                "type": "examples",
                "title": "Treaty register examples",
                "items": [
                    {
                        "spanish": "1920. június 4-én írták alá a trianoni békediktátumot a versailles-i kastélyban.",
                        "english": "On June 4, 1920, the Trianon peace diktat was signed in the palace at Versailles."
                    },
                    {
                        "spanish": "A szerződés értelmében több mint hárommillió magyar került idegen fennhatóság alá.",
                        "english": "Under the terms of the treaty, more than three million Hungarians came under foreign rule."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-trianon-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.trianon.03.minority-rights-discourse",
        "title": "Discourse of Rights & Belonging: joga van hozzá, hogy..., megilleti a jog",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Fundamental Minority Rights",
                "content": "Citizenship interview discourse regarding transborder communities: *minden közösséget megillet a jog, hogy anyanyelvén tanuljon* ('every community is entitled to the right to study in its mother tongue')."
            },
            {
                "type": "examples",
                "title": "Rights and identity phrases",
                "items": [
                    {
                        "spanish": "A határon túli magyarok évszázados szülőföldjükön őrzik anyanyelvüket és kultúrájukat.",
                        "english": "Hungarians beyond the borders preserve their native language and culture in their ancestral homeland."
                    },
                    {
                        "spanish": "A kettős identitás lehetővé teszi a hűséget a szülőföldhöz és a magyar nemzethez.",
                        "english": "Dual identity enables loyalty both to the homeland of birth and to the Hungarian nation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-trianon-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.trianon.04.emotional-historical-register",
        "title": "Emotional Memory Register: mély nyomot hagyott, nemzedékeken át",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Enduring National Memory",
                "content": "Phrases for collective historical processing: *mély sebet ejtett* ('inflicted a deep wound'), *nemzedékeken át érezhető maradt* ('remained palpable across generations'), *nehéz körülmények között kényszerült élni* ('was forced to live amidst difficult conditions')."
            },
            {
                "type": "examples",
                "title": "Memory phrases in context",
                "items": [
                    {
                        "spanish": "A trianoni döntés mély traumát okozott a magyar társadalom egészében.",
                        "english": "The Trianon decision caused deep trauma across the whole of Hungarian society."
                    },
                    {
                        "spanish": "Több százezer menekült érkezett vagonlakóként Budapestre az elcsatolt területekről.",
                        "english": "Hundreds of thousands of refugees arrived as railcar dwellers in Budapest from the annexed territories."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-trianon-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.trianon.05.unity-across-borders",
        "title": "Transnational Belonging: határoktól függetlenül, egységes egészként",
        "sections": [
            {
                "type": "text",
                "title": "Modern Constitutional Concept of the Nation",
                "content": "Formulations in the Hungarian Fundamental Law (*Alaptörvény*): *Magyarország felelősséget visel a határain kívül élő magyarok sorsáért.* ('Hungary bears responsibility for the fate of Hungarians living beyond its borders.'). *Határoktól függetlenül* ('irrespective of state borders')."
            },
            {
                "type": "examples",
                "title": "National unity phrasing",
                "items": [
                    {
                        "spanish": "Június 4-e a Nemzeti Összetartozás Napja, amely a kulturális egységet hirdeti.",
                        "english": "June 4th is the Day of National Unity, which proclaims cultural unity."
                    },
                    {
                        "spanish": "A megbékélés és az együttműködés a békés közép-európai jövő záloga.",
                        "english": "Reconciliation and cooperation are the pledge of a peaceful Central European future."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-trianon-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Style, 5 lessons + combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.trianon.01",
        "title": "A békedelegáció Párizsban és Apponyi beszéde",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In January 1920, the Hungarian peace delegation arrives in Paris, confined to the Château de Madrid in Neuilly. On January 16, Count Albert Apponyi delivers his legendary, multilingual defense of Hungary's thousand-year territorial and cultural integrity.",
        "characters": [
            "Gróf Apponyi Albert",
            "Gróf Teleki Pál geográfus",
            "Georges Clemenceau francia miniszterelnök"
        ],
        "location": "Párizs, Neuilly (Château de Madrid), Quai d'Orsay",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1920 fagyos januárjában egy elszánt magyar békedelegáció érkezett Párizsba. A küldöttséget a hetvenhárom éves gróf Apponyi Albert vezette, akit a franciák a Neuilly-sur-Seine-i Château de Madrid szállodába internáltak: a magyar diplomaták még a szálloda kertjét sem hagyhatták el engedély nélkül."
            },
            {
                "type": "narration",
                "text": "Január 16-án a Quai d'Orsay selyemtapétás termében a győztes nagyhatalmak vezetői előtt Apponyi felállt, hogy előadja Magyarország védőbeszédét. A teremben Clemenceau, Lloyd George és az olasz Nitti miniszterelnökök ültek a hatalmas zöld posztós asztalnál."
            },
            {
                "type": "dialogue",
                "speaker": "Gróf Apponyi Albert",
                "text": "Uraim! Ha Magyarország olyan helyzetbe kerülne, hogy választania kellene e békének az aláírása vagy visszautasítása között, úgy tulajdonképpen abban a kérdésben kellene döntenie: helyes-e öngyilkossággal megmenekülni a halál elől?"
            },
            {
                "type": "narration",
                "text": "Apponyi hibátlan, elegáns franciasággal kezdte, majd tolmács nélkül váltott át angolra és olaszra. A delegáció tagja, Teleki Pál kiterítette az asztalra híres alkotását: a vörös térkép részletesen, vörös színnel mutatta be a magyarság tömbjeit a Kárpát-medencében."
            },
            {
                "type": "narration",
                "text": "Apponyi nem kiváltságokat követelt, hanem népszavazást az etnikai elv és a wilsoni önrendelkezés alapján. A győztesek csendben hallgatták a lenyűgöző szónoklatot, de a geopolitikai döntések már régen megszülettek: a szerződés valódi békediktátum volt."
            },
            {
                "type": "dialogue",
                "speaker": "Gróf Apponyi Albert",
                "text": "Kérdezzék meg a népeket, hová akarnak tartozni! Mi készek vagyunk meghajolni a népszavazás döntése előtt, mert bízunk az igazságban!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon-01-apponyi.json", story_01)

    story_02 = {
        "id": "story.b1.trianon.02",
        "lesson": 2,
        "order": 2,
        "title": "1920. június 4.: A békediktátum aláírása",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "At 16:32 on June 4, 1920, inside the Grand Trianon Palace at Versailles, two reluctant Hungarian envoys sign the treaty that dismembers the thousand-year-old kingdom. In Budapest, streetcars halt, shops close, and mourning bells toll across the grieving nation.",
        "characters": [
            "Drasche-Lázár Alfréd államtitkár",
            "Benárd Ágost miniszter",
            "A budapesti polgárok"
        ],
        "location": "Versailles (Nagy Trianon kastély) és Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1920. június 4-én délután a versailles-i parkban csend telepedett a márványoszlopokra. A Nagy Trianon kastély Cotelle-galériájában összegyűltek a szövetséges hatalmak képviselői a történelmi aktusra."
            },
            {
                "type": "narration",
                "text": "Magyarország részéről a kormány két tagja, Benárd Ágost népjóléti miniszter és Drasche-Lázár Alfréd rendkívüli követ lépett az asztalhoz. Mindketten fekete díszmagyarban voltak, arcuk sápadt volt a történelmi felelősség súlya alatt."
            },
            {
                "type": "dialogue",
                "speaker": "Benárd Ágost",
                "text": "Tudjuk, hogy mit írunk alá: a nemzettest megcsonkítását. De azért tesszük, hogy a megmaradt csonka ország legalább lélegezni tudjon és megkezdhesse az újjáépítést."
            },
            {
                "type": "narration",
                "text": "Pontosan 16 óra 32 perckor a toll sercegése pecsételte meg a döntést: a területelcsatolás révén Magyarország elveszítette területének több mint kétharmadát és lakosságának felét, miközben az új államhatárok több mint hárommillió magyart zártak a határokon kívülre."
            },
            {
                "type": "narration",
                "text": "Ugyanebben a percben Budapesten megállt az élet: a villamosok tíz percre leállították motorjaikat, a boltok bezártak, az iskolákban megszólalt a gyászharang. Az egész ország fekete zászlókba öltözött: ez volt a modern magyar történelem legnagyobb nemzeti tragédiája."
            },
            {
                "type": "dialogue",
                "speaker": "A budapesti polgárok",
                "text": "Elvették Kolozsvárt, Pozsonyt és Kassát... de a szívünket nem vehetik el! Amíg él magyar ember, a nemzet lelke egy és oszthatatlan marad!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon-02-alairas.json", story_02)

    story_03 = {
        "id": "story.b1.trianon.03",
        "lesson": 3,
        "order": 3,
        "title": "Határon túli magyarság és a kisebbségi sors",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Overnight, over three million Hungarians find themselves citizens of foreign successor states without ever leaving their homes. We explore their resilience in Transylvania, Upper Hungary, and the Vojvodina, protecting their native schools, churches, and dual identity.",
        "characters": [
            "Kós Károly építész és író",
            "Felvidéki magyar tanító",
            "Vajdasági gazda"
        ],
        "location": "Sztána (Erdély), Kassa (Csehszlovákia), Szabadka (Szerb-Horvát-Szlovén Királyság)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A trianoni határhúzás legfájdalmasabb következménye az emberi sorsokban mutatkozott meg. Több mint hárommillió magyar ember ébredt fel úgy egyik napról a másikra, hogy anélkül, hogy elhagyta volna szülőházát, egy idegen ország alattvalójává vált."
            },
            {
                "type": "narration",
                "text": "Romániában, Csehszlovákiában és a délszláv államban azonnal megkezdődött a közigazgatás átalakítása. A határon túli magyarok számára kezdetét vette a nehéz kisebbségi sors: az anyanyelvhasználat korlátozása és a magyar tisztviselők elbocsátása."
            },
            {
                "type": "dialogue",
                "speaker": "Kós Károly építész és író",
                "text": "Kiáltom a szót! Nem szabad feladnunk a szülőföldünket! Itt kell élnünk, itt kell dolgoznunk, új alapokra kell helyeznünk erdélyi magyar életünket!"
            },
            {
                "type": "narration",
                "text": "A magyarság békés, kulturális ellenállással válaszolt: önálló magyar iskola hálózatot szerveztek, magyar nyelvű lapokat és színházakat tartottak fenn a történelmi egyházak segítségével."
            },
            {
                "type": "narration",
                "text": "Kialakult a sajátos kettős identitás: az állampolgári lojalitás a lakóhely szerinti államhoz, miközben a szív, a nyelv és a kultúra az ezeréves magyar nemzethez kapcsolta őket."
            },
            {
                "type": "dialogue",
                "speaker": "Felvidéki magyar tanító",
                "text": "Ha a hivatalban nem is szólhatunk magyarul, az iskolában és a családi asztalnál a magyar anyanyelv a legdrágább örökségünk marad!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon-03-kisebbseg.json", story_03)

    story_04 = {
        "id": "story.b1.trianon.04",
        "lesson": 4,
        "order": 4,
        "title": "A vagonlakók és a nemzeti trauma",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Between 1918 and 1924, nearly 400,000 refugees arrive in truncated Hungary. With housing destroyed or unavailable, entire families live in unheated freight train cars on Budapest railway sidings, fueling the deep interwar trauma and the passionate cry for revision.",
        "characters": [
            "Menekült kolozsvári jogász",
            "Pályaudvari segélymunkás",
            "Budapesti diák"
        ],
        "location": "Budapest, Nyugati pályaudvar rendezőpályaudvara",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az elcsatolt országrészekből a háború után hatalmas menekülthullám indult el: bírák, tanárok, vasutasok és gazdák százezrei kényszerültek elhagyni otthonukat, mert megtagadták az új államokra tett hűségesküt."
            },
            {
                "type": "narration",
                "text": "Közel négyszázezer menekült érkezett a romokban heverő csonka Magyarországra. Mivel a fővárosban nem volt szabad lakás, megszületett a vagonlakók szívszorító jelensége: családok ezrei éltek éveken át a pályaudvarok mellékvágányain veszteglő fagyos marhavagonokban."
            },
            {
                "type": "dialogue",
                "speaker": "Menekült kolozsvári jogász",
                "text": "Egyetlen kofferrel menekültünk el a családommal. A kályhát magunk szereltük a vagon közepére, de a gyermekeim kabátban alszanak a szalmán. És mégis: itt legalább magyar szót hallunk az állomáson!"
            },
            {
                "type": "narration",
                "text": "A megalázó nélkülözés és az ország feldarabolása mély kollektív traumát vésett a nemzet tudatába. Az iskolákban minden reggel a Trianon-imát mondták, a köztereken felállították a revízió emlékműveit, és az 'irredentizmus' a hivatalos állampolitika vezérfonalává vált."
            },
            {
                "type": "narration",
                "text": "A 'Nem, nem, soha!' jelszava két évtizeden át határozta meg a magyar közéletet, megalapozva azt a külpolitikai irányt, amely később a határok békés vagy fegyveres módosítását, az országgyarapítás lehetőségét kereste."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti diák",
                "text": "Nem a bosszú vezérel minket, hanem az igazságérzet. Egy nemzetet nem lehet örökre bezárni a mesterségesen meghúzott határok közé!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon-04-trauma.json", story_04)

    story_05 = {
        "id": "story.b1.trianon.05",
        "lesson": 5,
        "order": 5,
        "title": "A Nemzeti Összetartozás Napja: Múltból a jövőbe",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "A century later, June 4th transforms from a day of bitter grievance into the Day of National Unity. Reflecting modern European values, the Hungarian nation celebrates cultural unity transcending borders, educational ties, and fraternal cooperation in the Carpathian Basin.",
        "characters": [
            "Budapesti középiskolás",
            "Kassai magyar diák",
            "Határon túli civil vezető"
        ],
        "location": "Budapest, Kossuth tér (Nemzeti Összetartozás Emlékhelye) és Csíksomlyó",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Egy évszázaddal a trianoni békediktátum után a történelmi trauma helyét fokozatosan az érett történelmi emlékezet és a méltóságteljes összetartozás eszméje vette át."
            },
            {
                "type": "narration",
                "text": "A magyar Országgyűlés 2010-ben június 4-ét hivatalosan a Nemzeti Összetartozás Napja emlékévévé nyilvánította. Ez a törvény kimondja, hogy a világban élő minden magyar ember része az egységes magyar nemzetnek, függetlenül attól, hogy melyik állam területén él."
            },
            {
                "type": "dialogue",
                "speaker": "Határon túli civil vezető",
                "text": "A 21. században már nem határok átrajzolásáról beszélünk, hanem a határok légiessé válásáról. Az Európai Unió tagjaiként szabadon járhatunk át a határokon, és a kulturális egység erősebb, mint valaha!"
            },
            {
                "type": "narration",
                "text": "A 'Határtalanul!' program keretében magyarországi iskolások tízezrei látogatják meg évről évre Erdély, a Felvidék, Kárpátalja és a Vajdaság magyar iskoláit, életre szóló barátságokat kötve a határon túli fiatalokkal."
            },
            {
                "type": "narration",
                "text": "A megbékélés a szomszédos népekkel és a Kárpát-medencei együttműködés a modern magyar külpolitika sarokköve lett. A közös történelem sebei lassan gyógyulnak, miközben a közös jövő az egymás iránti tiszteleten épül."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti középiskolás",
                "text": "Amikor Csíksomlyón több százezer emberrel együtt énekeljük a Himnuszt, megértem: a nemzet nem négyzetkilométerekben mérhető, hanem a közös nyelvben, a dalokban és az összetartozás érzésében él!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon-05-osszetartozas.json", story_05)

    # Combined story for consolidation
    story_combined = {
        "id": "story.b1.trianon.combined",
        "title": "A trianoni békediktátum és a nemzeti összetartozás (1920–napjainkig)",
        "level": "B1",
        "order": 21,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive Rest is History narrative exploring the tragedy and legacy of Trianon: Apponyi's speech in Paris, the signing at Versailles on June 4, 1920, the struggle of transborder Hungarian communities, the refugee crisis, and the modern transformation into the Day of National Unity.",
        "characters": [
            "Gróf Apponyi Albert és Teleki Pál",
            "Benárd Ágost és Drasche-Lázár Alfréd aláírók",
            "A határon túli magyarság és a mai nemzedékek"
        ],
        "location": "Párizs, Versailles, Kolozsvár, Kassa, Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1920 januárjában a párizsi békekonferencián gróf Apponyi Albert vezetésével megjelent a magyar békedelegáció. Bár Apponyi három nyelven elmondott beszéde és a Teleki Pál által készített vörös térkép lenyűgözte a jelenlévőket, az etnikai elv helyett a győztes szövetségesek stratégiai érdekei győztek."
            },
            {
                "type": "narration",
                "text": "1920. június 4-én a Nagy Trianon kastély galériájában megtörtént az aláírás: megszületett a trianoni békediktátum. A területelcsatolás során Magyarország elveszítette történelmi területének kétharmadát, miközben országszerte megkondult a gyászharang a példátlan nemzeti tragédia emlékére."
            },
            {
                "type": "narration",
                "text": "Több mint hárommillió határon túli magyar került egyik napról a másikra idegen impérium alá. A kisebbségi sors évtizedeiben az anyanyelvhasználat és a magyar iskola fenntartása a megmaradás zálogává vált az elcsatolt országrészekben."
            },
            {
                "type": "narration",
                "text": "A csonka országba menekülthullám zúdult: a budapesti pályaudvarokon vagonlakók ezrei éltek évekig, és a mély trauma miatt a két világháború közötti Magyarországot az irredentizmus és a revízió követelése fűtötte."
            },
            {
                "type": "narration",
                "text": "A 21. században június 4-e új jelentést kapott: a Nemzeti Összetartozás Napja lett. Ma már nem a keserűség, hanem a kulturális egység, a határokon átívelő szolidaritás és a békés Kárpát-medencei együttműködés határozza meg a megemlékezést."
            },
            {
                "type": "narration",
                "text": "A trianoni békediktátum a modern magyar történelem legnagyobb sorsfordító eseménye, amelynek mély és sokrétű ismerete az állampolgársági felkészülés legfontosabb sarokköve."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-trianon.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-trianon-{padded}",
            "exercises": [
                {
                    "id": f"b1-trianon-{padded}.ex01",
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
                    "id": f"b1-trianon-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen a trianoni békeszerződés történelmi körülményeit? (Lesson {i})",
                    "options": [
                        "A békedelegáció azért terjesztette elő a vörös térképet, hogy bemutassa a valós etnikai határokat.",
                        "A békedelegáció mert térkép elvinni ezért békét nem ír alá.",
                        "Mivel Trianon aláírás volt ezért azonnal minden ember elköltözni volt."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-trianon-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1920. június 4-én délután írták alá a versailles-i Nagy Trianon kastélyban a ____. (peace treaty / diktat - békediktátumot)",
                    "answer": "békediktátumot"
                },
                {
                    "id": f"b1-trianon-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A trianoni döntés következtében több mint hárommillió magyar került idegen államhatárok ____. (beyond / outside - túl / közé / mögé -> közé)",
                    "answer": "közé"
                },
                {
                    "id": f"b1-trianon-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit nevezünk a 'vörös térképnek' a békekonferenciával kapcsolatban?",
                    "options": [
                        "Teleki Pál híres etnikai térképét, amely vörös színnel jelölte a magyar lakosságot.",
                        "A francia hadsereg titkos katonai haditervét.",
                        "Budapest belvárosának közlekedési hálózati rajzát."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-trianon-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Magyarország felelősséget visel a határain kívül élő magyarok sorsá____. (for their fate - ért)",
                    "answer": "ért"
                },
                {
                    "id": f"b1-trianon-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "Nemzeti", "Összetartozás", "Napja", "a", "határokon", "átívelő", "kulturális", "egységet", "hirdeti."],
                    "solution": ["A", "Nemzeti", "Összetartozás", "Napja", "a", "határokon", "átívelő", "kulturális", "egységet", "hirdeti."]
                },
                {
                    "id": f"b1-trianon-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik napot nyilvánította a magyar Országgyűlés a Nemzeti Összetartozás Napjává?",
                    "options": [
                        "Június 4-ét, a trianoni békeszerződés aláírásának emléknapját.",
                        "Március 15-ét, a forradalom napját.",
                        "Október 23-át, az 1956-os szabadságharc kezdetét."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-trianon-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-trianon-consolidation",
        "exercises": [
            {
                "id": "b1-trianon-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Apponyi Albert", "head of peace delegation"],
                    ["vörös térkép", "ethnic map by Teleki"],
                    ["határon túli magyarok", "Hungarians beyond borders"],
                    ["Nemzeti Összetartozás Napja", "Day of National Unity"]
                ]
            },
            {
                "id": "b1-trianon-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás foglalja össze a legpontosabban az 1920-as trianoni döntés következményeit?",
                "options": [
                    "Magyarország elveszítette területének kétharmadát, és több mint hárommillió magyar került kisebbségi sorba.",
                    "Magyarország területe kétszeresére növekedett a győztes hatalmak jóvoltából.",
                    "A békeszerződés azonnal helyreállította az Osztrák–Magyar Monarchia határait."
                ],
                "correct": 0
            },
            {
                "id": "b1-trianon-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A békedelegáció vezetője, gróf Apponyi Albert három nyelven tartotta meg híres védő____. (speech / defense - beszédét)",
                "answer": "beszédét"
            },
            {
                "id": "b1-trianon-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1920. június 4-én 16 óra 32 perckor az egész országban megszólaltak a gyász____. (bells - harangok)",
                "answer": "harangok"
            },
            {
                "id": "b1-trianon-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "határon", "túli", "magyarság", "megőrizte", "anyanyelvét", "és", "nemzeti", "önazonosságát."],
                "solution": ["A", "határon", "túli", "magyarság", "megőrizte", "anyanyelvét", "és", "nemzeti", "önazonosságát."]
            },
            {
                "id": "b1-trianon-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kisebbségi sors' fogalma a magyar történelemben?",
                "options": [
                    "Az elcsatolt területeken élő magyarság megváltozott jogi, kulturális és társadalmi helyzetét.",
                    "Egy ritka középkori vallási rendhez való tartozást.",
                    "A külföldi egyetemi ösztöndíjasok ideiglenes tanulmányi szerződését."
                ],
                "correct": 0
            },
            {
                "id": "b1-trianon-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A határon túli magyar iskolák és egyházak a nemzeti kultúra bástyái ____. (remained - maradtak)",
                "answer": "maradtak"
            },
            {
                "id": "b1-trianon-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan fogalmazza meg a magyar Alaptörvény a határon túli magyarok iránti elkötelezettséget?",
                "options": [
                    "Magyarország felelősséget visel a határain kívül élő magyarok sorsáért, és támogatja közösségeik megmaradását.",
                    "A magyar állam teljesen lemondott minden külföldön élő magyar támogatásáról.",
                    "A határon túli magyaroknak tilos kapcsolatot tartaniuk Magyarországgal."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-trianon-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A békedelegáció és Apponyi beszéde", "Negotiating the Peace"),
        "02": ("A trianoni békediktátum (1920. június 4.)", "What Trianon Changed"),
        "03": ("Határon túli magyarság és kisebbségi sors", "Hungarians Beyond the Border"),
        "04": ("Menekülthullám és nemzeti trauma", "National Trauma & Memory"),
        "05": ("A Nemzeti Összetartozás Napja", "Day of National Unity")
    }

    story_refs = {
        "01": "stories/world/b1/b1-trianon-01-apponyi.json",
        "02": "stories/world/b1/b1-trianon-02-alairas.json",
        "03": "stories/world/b1/b1-trianon-03-kisebbseg.json",
        "04": "stories/world/b1/b1-trianon-04-trauma.json",
        "05": "stories/world/b1/b1-trianon-05-osszetartozas.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.trianon-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Causal-Consequence Discourse, Treaty Formulations & Transnational Identity Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} and its historic consequences.",
                        "I can use causal treaty connectors and discuss minority rights in Hungarian.",
                        "I can answer essential citizenship interview questions regarding Trianon and National Unity.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-trianon-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-trianon-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-trianon-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-trianon-{padded}.ex01",
                        f"b1-trianon-{padded}.ex02",
                        f"b1-trianon-{padded}.ex03",
                        f"b1-trianon-{padded}.ex04",
                        f"b1-trianon-{padded}.ex05",
                        f"b1-trianon-{padded}.ex06",
                        f"b1-trianon-{padded}.ex07",
                        f"b1-trianon-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-trianon-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.trianon-consolidation",
        "title": "Összefoglalás: A trianoni békeszerződés (The Treaty of Trianon Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of Trianon, Transborder Minorities & the Day of National Unity",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-trianon.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-trianon-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-trianon-consolidation.ex01",
                    "b1-trianon-consolidation.ex02",
                    "b1-trianon-consolidation.ex03",
                    "b1-trianon-consolidation.ex04",
                    "b1-trianon-consolidation.ex05",
                    "b1-trianon-consolidation.ex06",
                    "b1-trianon-consolidation.ex07",
                    "b1-trianon-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-trianon-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 21 (b1-trianon)!")

if __name__ == "__main__":
    build_unit_21_citizenship()
