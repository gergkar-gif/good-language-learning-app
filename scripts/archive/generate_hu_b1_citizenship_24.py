#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 24: The Communist Takeover & Rákosi Era (b1-rakosikorszak)."""

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

def build_unit_24_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.rakosikorszak.01",
        "lesson": "b1-rakosikorszak-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szalámitaktika", "translation": "'salami tactics' (slicing away democratic opposition parties one by one)", "pos": "noun"},
            {"lemma": "Magyar Kommunista Párt", "translation": "Hungarian Communist Party (MKP)", "pos": "noun"},
            {"lemma": "kékcédulás választások", "translation": "'blue slip' fraudulent elections (August 31, 1947)", "pos": "noun"},
            {"lemma": "koalíciós kormány", "translation": "coalition government (1945–1948)", "pos": "noun"},
            {"lemma": "államosítás", "translation": "nationalization of private banks, industries, and schools", "pos": "noun"},
            {"lemma": "Független Kisgazdapárt", "translation": "Independent Smallholders' Party (winner of 1945 free elections, crushed by 1948)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakosikorszak-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.rakosikorszak.02",
        "lesson": "b1-rakosikorszak-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Rákosi Mátyás", "translation": "Mátyás Rákosi (Stalinist dictator of Hungary, General Secretary)", "pos": "noun"},
            {"lemma": "személyi kultusz", "translation": "cult of personality ('Stalin's best Hungarian disciple')", "pos": "noun"},
            {"lemma": "pártállam", "translation": "one-party state / totalitarian party-state apparatus", "pos": "noun"},
            {"lemma": "Magyar Dolgozók Pártja", "translation": "Hungarian Working People's Party (MDP - monopoly party formed 1948)", "pos": "noun"},
            {"lemma": "sztálini alkotmány", "translation": "Stalinist Constitution of 1949 (Act XX of 1949, People's Republic)", "pos": "noun"},
            {"lemma": "ötéves terv", "translation": "Five-Year Plan (forced industrial development quotas)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakosikorszak-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.rakosikorszak.03",
        "lesson": "b1-rakosikorszak-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Államvédelmi Hatóság", "translation": "State Protection Authority (ÁVH - dreaded secret police)", "pos": "noun"},
            {"lemma": "Péter Gábor", "translation": "Gábor Péter (notorious chief of the ÁVH secret police)", "pos": "noun"},
            {"lemma": "Andrássy út 60", "translation": "60 Andrássy Avenue (headquarters of terror, torture, and interrogation)", "pos": "noun"},
            {"lemma": "fekete autó", "translation": "'black car' (Pobeda cars arriving for midnight arrests)", "pos": "noun"},
            {"lemma": "kitelepítés", "translation": "forced deportation of 'class-alien' families from cities to countryside", "pos": "noun"},
            {"lemma": "Recski kényszermunkatábor", "translation": "Recsk forced labor camp (the 'Hungarian Gulag' quarry, 1950–1953)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakosikorszak-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.rakosikorszak.04",
        "lesson": "b1-rakosikorszak-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "koncepciós per", "translation": "show trial / staged political trial with fabricated charges", "pos": "noun"},
            {"lemma": "Rajk László", "translation": "László Rajk (interior minister purged and executed in 1949)", "pos": "noun"},
            {"lemma": "Mindszenty József", "translation": "Cardinal József Mindszenty (Prince Primate sentenced in show trial)", "pos": "noun"},
            {"lemma": "kicsikart vallomás", "translation": "extorted confession under physical and psychological torture", "pos": "noun"},
            {"lemma": "ellenségkép", "translation": "manufactured image of internal enemy / 'imperialist agent'", "pos": "noun"},
            {"lemma": "rehabilitáció", "translation": "posthumous political rehabilitation of innocent purge victims", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakosikorszak-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.rakosikorszak.05",
        "lesson": "b1-rakosikorszak-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kuláküldözés", "translation": "persecution of 'kulaks' (peasant landowners branded class enemies)", "pos": "noun"},
            {"lemma": "padlássöprés", "translation": "'sweeping the attics' (ruthless total requisitioning of peasant grain and lard)", "pos": "noun"},
            {"lemma": "beszolgáltatás", "translation": "compulsory agricultural delivery quotas to the state", "pos": "noun"},
            {"lemma": "termelőszövetkezet", "translation": "agricultural collective / cooperative farm (téesz)", "pos": "noun"},
            {"lemma": "a vas és acél országa", "translation": "'country of iron and steel' (unrealistic heavy industrial dogma)", "pos": "noun"},
            {"lemma": "Sztálinváros", "translation": "Sztálinváros (showcase socialist steel town, today Dunaújváros)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakosikorszak-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.rakosikorszak.01.authoritarian-takeover",
        "title": "Authoritarian Mechanics: felszámol, lépésről lépésre ellehetetlenít",
        "sections": [
            {
                "type": "text",
                "title": "Describing Systematic Erosion of Democracy",
                "content": "To express how institutions are systematically dismantled: *lépésről lépésre felszámol* ('dismantles step by step'), *ellehetetleníti a működést* ('makes operation impossible'), *hatalma alá von* ('brings under its power')."
            },
            {
                "type": "examples",
                "title": "Political takeover phrases",
                "items": [
                    {
                        "spanish": "A kommunista párt szalámitaktikával számolta fel a demokratikus ellenzéket.",
                        "english": "The Communist Party dismantled democratic opposition using salami tactics."
                    },
                    {
                        "spanish": "Az államosítás során minden nagyobb gyárat és magánbankot állami tulajdonba vettek.",
                        "english": "During nationalization, every larger factory and private bank was taken into state ownership."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakosikorszak-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.rakosikorszak.02.totalitarian-discourse",
        "title": "Totalitarian Propaganda Discourse: kötelezővé tesz, hűséget követel",
        "sections": [
            {
                "type": "text",
                "title": "Language of Forced Adulation",
                "content": "*Kötelezővé teszi a személyi kultuszt* ('makes cult of personality mandatory'), *feltétlen hűséget követel* ('demands unconditional loyalty'), *rendelet útján kormányoz* ('governs by decree')."
            },
            {
                "type": "examples",
                "title": "Propaganda slogans and analysis",
                "items": [
                    {
                        "spanish": "Rákosi Mátyást a propaganda 'népünk bölcs vezérének' nevezte.",
                        "english": "Propaganda hailed Mátyás Rákosi as 'the wise leader of our people'."
                    },
                    {
                        "spanish": "Az 1949-es szovjet mintájú alkotmány rögzítette a kommunista pártállam egyeduralmát.",
                        "english": "The 1949 Soviet-model constitution codified the absolute monopoly of the communist party-state."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakosikorszak-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.rakosikorszak.03.coercion-and-internment",
        "title": "State Terror Registers: kényszermunkára ítél, éj leple alatt elhurcol",
        "sections": [
            {
                "type": "text",
                "title": "Vocabulary of Lawless Coercion",
                "content": "*Bírósági ítélet nélkül internál* ('interns without judicial verdict'), *éj leple alatt hurcol el* ('drags off under cover of night'), *kényszermunkára kényszerít* ('forces into hard labor')."
            },
            {
                "type": "examples",
                "title": "Documenting terror",
                "items": [
                    {
                        "spanish": "Az ÁVH rettegett fekete autói éjszaka érkeztek a gyanútlan családok otthonába.",
                        "english": "The feared black cars of the ÁVH arrived at night at the homes of unsuspecting families."
                    },
                    {
                        "spanish": "Recskre bírósági ítélet nélkül hurcolták el a rendszer politikai ellenfeleit.",
                        "english": "The regime's political opponents were dragged off to Recsk without any judicial verdict."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakosikorszak-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.rakosikorszak.04.show-trial-accusations",
        "title": "Show Trial Fabrications: koholt vádak alapján, vallomást kényszerít ki",
        "sections": [
            {
                "type": "text",
                "title": "Dissecting Judicial Fabrications",
                "content": "*Koholt vádak alapján* ('on the basis of fabricated charges'), *kicsikarja a beismerő vallomást* ('extorts the confession'), *elrettentés céljából kivégez* ('executes for the purpose of deterrence')."
            },
            {
                "type": "examples",
                "title": "Show trial discourse",
                "items": [
                    {
                        "spanish": "Rajk Lászlót és Mindszenty Józsefet koholt vádak alapján állították bíróság elé.",
                        "english": "László Rajk and József Mindszenty were put on trial on the basis of fabricated charges."
                    },
                    {
                        "spanish": "A kihallgatások során fizikai és lelki kínzással csikartak ki hamis vallomásokat.",
                        "english": "During interrogations, false confessions were extorted through physical and psychological torture."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakosikorszak-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.rakosikorszak.05.command-economy-dogma",
        "title": "Command Economy Directives: tervutasításos rendszer, beszolgáltatásra kötelez",
        "sections": [
            {
                "type": "text",
                "title": "Economic Directives",
                "content": "*Tervutasításos rendszerben működik* ('operates in a command economy system'), *kötelező beszolgáltatást ír elő* ('prescribes compulsory delivery quotas'), *erőszakkal kényszerít a téeszbe* ('forces into the collective by coercion')."
            },
            {
                "type": "examples",
                "title": "Agrarian crisis phrases",
                "items": [
                    {
                        "spanish": "A padlássöprések során a parasztok utolsó vetőmagját is elvitték az állami raktárakba.",
                        "english": "During the attic-sweepings, even the peasants' last seed grain was taken to state warehouses."
                    },
                    {
                        "spanish": "A vas és acél országa jelszóval a gazdasági realitásoktól elrugaszkodott nehézipart erőltettek.",
                        "english": "With the slogan 'country of iron and steel', heavy industry divorced from economic reality was forced."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakosikorszak-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Stories (World / Rest-is-History Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.rakosikorszak.01",
        "lesson": 1,
        "order": 1,
        "title": "A szalámitaktika és a kékcédulás választások (1945–1948)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In 1945, Hungary held free democratic elections in which the Independent Smallholders won 57% of the vote. Backed by Soviet occupation forces, Communist leader Mátyás Rákosi systematically sliced away opposing political parties one by one—a strategy he famously coined 'salami tactics'—culminating in the fraudulent blue-slip elections of 1947.",
        "characters": [
            "Rákosi Mátyás, a kommunista párt főtitkára",
            "Kisgazda országgyűlési képviselő",
            "Budapesti választópolgár"
        ],
        "location": "Budapest, Országház és a szavazóhelyiségek",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1945 őszén a romokból ébredő Magyarországon szabad választásokat tartottak. A választók elsöprő, 57 százalékos többséggel a polgári Független Kisgazdapártra szavaztak, míg a kommunisták mindössze 17 százalékot szereztek."
            },
            {
                "type": "dialogue",
                "speaker": "Kisgazda képviselő",
                "text": "A nép akarata világos: békét, földet, demokráciát és nyugati típusú szabadságot akarunk! Senki sem kényszerítheti ránk az egypártrendszert!"
            },
            {
                "type": "narration",
                "text": "Ám a szovjet hadsereg fegyverei a Magyar Kommunista Párt mögött álltak. Rákosi Mátyás kidolgozta a hírhedt 'szalámitaktikát': nem egyszerre támadták meg a demokráciát, hanem szeletenként, egymás ellen kijátszva és megzsarolva semmisítették meg az ellenzéki pártokat."
            },
            {
                "type": "narration",
                "text": "1947. augusztus 31-én sor került a szégyenteljes 'kékcédulás' választásra. A kommunista aktivisták teherautókkal járták az országot, és hamis kék színű igazolásokkal több tízezer illegális szavazatot adtak le."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti választópolgár",
                "text": "Saját szememmel láttam, hogy ugyanazok a bőrfejű fiatalok három különböző kerületben dobtak be szavazócédulát! A demokrácia utolsó maradványát is eltiporták!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak-01-szalami.json", story_01)

    story_02 = {
        "id": "story.b1.rakosikorszak.02",
        "lesson": 2,
        "order": 2,
        "title": "A pártállam és Rákosi személyi kultusza",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "By 1949, Hungary was transformed into a totalitarian Stalinist people's republic under the new constitution. Mátyás Rákosi erected a suffocating cult of personality: giant portraits in classrooms and factories, compulsory praise in song and poetry, and total control over every aspect of private and public life.",
        "characters": [
            "Iskolai tanítónő Budapesten",
            "Csepeli vasmunkás",
            "Pártfunkcionárius"
        ],
        "location": "A csepeli Rákosi Mátyás Művek és az iskolai tanterem",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1949-ben hatályba lépett a szovjet mintára megfogalmazott új alkotmány. Az ezeréves királyi címer helyére a vörös csillagos Rákosi-címer került, s az ország hivatalos neve Magyar Népköztársaság lett."
            },
            {
                "type": "narration",
                "text": "Kezdetét vette a tomboló személyi kultusz. Rákosi Mátyás arcképe ott lógott minden irodában, gyárban, iskolában és vasútállomáson. A sajtó 'Sztálin legjobb magyar tanítványaként' és 'népünk atyjaként' magasztalta a rettegett diktátort."
            },
            {
                "type": "dialogue",
                "speaker": "Pártfunkcionárius",
                "text": "Rákosi elvtárs hatvanadik születésnapjára az egész országnak felajánlást kell tennie! Minden gyár dolgozzon túlórát, minden költő írjon ódát a bölcs vezérről!"
            },
            {
                "type": "dialogue",
                "speaker": "Iskolai tanítónő",
                "text": "Reggel a Himnusz helyett szovjet indulókat és Rákosi-dalokat kellett énekeltetnem a kisiskolásokkal. Ha egyetlen gyermek elhibázta a szavakat, rettegtem, hogy feljelentenek."
            },
            {
                "type": "narration",
                "text": "A látszat mögött azonban nyomasztó szegénység és félelem uralkodott. Az ötéves tervek elérhetetlen normákat követeltek, a boltok polcain állandósult a hiány, miközben a hivatalos sajtó a szocializmus virágzásáról hazudott."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak-02-szemelyikultusz.json", story_02)

    story_03 = {
        "id": "story.b1.rakosikorszak.03",
        "lesson": 3,
        "order": 3,
        "title": "Az ÁVH réme: Andrássy út 60. és a recski tábor",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The cornerstone of Rákosi's totalitarian control was the ÁVH secret police, led by Gábor Péter. Operating out of Andrássy Avenue 60, midnight 'black cars' swept up citizens without trial, deporting bourgeois families to Hortobágy and political dissidents to the brutal secret quarry at Recsk.",
        "characters": [
            "Péter Gábor, az ÁVH rettegett vezetője",
            "Recski kényszermunkás (egykori mérnök)",
            "Kitelepített budapesti polgárasszony"
        ],
        "location": "Budapest, Andrássy út 60. és a recski kőbánya",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A budapesti Andrássy út 60. alatti neoreneszánsz palota pincéje a rettegés központjává vált. Az Államvédelmi Hatóság (ÁVH) kékparfás tisztjei előtt nem létezett törvény: a gyanúsítottakat heteken át verték és kínozták a sötét cellákban."
            },
            {
                "type": "dialogue",
                "speaker": "Kitelepített polgárasszony",
                "text": "Éjfélkor dörömböltek az ajtón. Egyetlen órát kaptunk, hogy egy bőröndbe pakoljunk. Másnap már marhavagonban vittek minket a hortobágyi puszta egyik elhagyatott birkahodályába."
            },
            {
                "type": "narration",
                "text": "1950 és 1953 között a Mátra hegyei között működött a legtitkosabb haláltábor: a recski kényszermunkatábor. Ide bírósági ítélet nélkül hurcolták el az egykori politikusokat, tudósokat, arisztokratákat és szociáldemokratákat."
            },
            {
                "type": "dialogue",
                "speaker": "Recski kényszermunkás",
                "text": "Napi tizenhat órát törtük a bazaltot a kőbányában csákánnyal, éhezve, vékony rabruhában a fagyban. A külvilág nem is tudta, hogy létezünk: Recsket szigorú szögesdrót és géppuskafészkek zárták el a világtól."
            },
            {
                "type": "narration",
                "text": "Faludy György költő és sorstársai azonban a legmélyebb pokolban is megőrizték emberi méltóságukat: fejből mondták fel a világirodalom remekeit a barakkokban, bizonyítva, hogy a szellem szabadságát a fegyveres terror sem törheti meg."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak-03-avh.json", story_03)

    story_04 = {
        "id": "story.b1.rakosikorszak.04",
        "lesson": 4,
        "order": 4,
        "title": "Koncepciós perek: Rajk László és Mindszenty bíboros",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "To eliminate every potential rival and intimidate the population, Rákosi staged show trials with pre-scripted verdicts. In 1948, Cardinal József Mindszenty was drugged and sentenced to life imprisonment; in 1949, former interior minister László Rajk was executed as a fabricated 'Titoist spy'.",
        "characters": [
            "Rajk László, a vádolt egykori belügyminiszter",
            "Mindszenty József, bíboros hercegprímás",
            "Bírósági ülnök a koncepciós perben"
        ],
        "location": "A Markó utcai bíróság díszterme, Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A sztálini típusú diktatúra legördögibb eszköze a koncepciós per volt: a vádiratot és az ítéletet előre megírták a pártközpontban, a bírósági tárgyalás csupán megfélemlítő propagandaszínházként szolgált."
            },
            {
                "type": "dialogue",
                "speaker": "Mindszenty József bíboros",
                "text": "A magyar katolikus egyház és a hívők lelkiismerete nem eladó! Bármit kényszerítenek rám a börtön falai között, tudják: az erőszak alatt aláírt vallomás érvénytelen Isten és a nemzet színe előtt!"
            },
            {
                "type": "narration",
                "text": "Mindszenty hercegprímást életfogytiglani börtönre ítélték. Nem sokkal később a párt belső tisztogatást indított: 1949-ben bíróság elé állították Rajk László belügyminisztert, akit abszurd vádakkal 'amerikai és jugoszláv imperialista kémkedéssel' vádoltak meg."
            },
            {
                "type": "dialogue",
                "speaker": "Bírósági ülnök",
                "text": "Mindenki tudta, hogy a vádak koholtak. De a teremben ülő ÁVH-s tisztek szeme előtt a bírák szolgaian olvasták fel a halálos ítéletet. Senki sem volt biztonságban: a forradalom saját gyermekeit falta fel."
            },
            {
                "type": "narration",
                "text": "Rajk Lászlót kivégezték, de 1956 őszén a mártírok újratemetése több százezer ember néma tüntetésévé vált, megnyitva az utat a szabadságharc kitörése előtt."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak-04-koncepcio.json", story_04)

    story_05 = {
        "id": "story.b1.rakosikorszak.05",
        "lesson": 5,
        "order": 5,
        "title": "Padlássöprés és a vas országa: Gazdasági zsákutca",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Rákosi's economic dogma wreaked havoc on Hungary. In the countryside, 'sweeping the attics' robbed peasants of their last grain to force them into collective farms (téesz). In industry, the regime poured all resources into unviable heavy steel plants ('the country of iron and steel') while food shortages crippled everyday life.",
        "characters": [
            "Alföldi gazda a falu határában",
            "Begyűjtési biztos",
            "Sztálinvárosi kohászsegéd"
        ],
        "location": "Békési falu és Sztálinváros (Dunaújváros)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A mezőgazdaságban a kommunista hatalom kíméletlen háborút indított a hagyományos parasztság ellen. A módosabb gazdákat megbélyegezték: ők lettek a 'kulákok', a falu belső ellenségei, akiket különadókkal és megaláztatásokkal sújtottak."
            },
            {
                "type": "dialogue",
                "speaker": "Begyűjtési biztos",
                "text": "Gazda, ne rejtegessen semmit! A pártnak gabona kell a városi munkások és a baráti Szovjetunió ellátására! Ha a padláson egyetlen szem búza marad, börtönbe kerül!"
            },
            {
                "type": "narration",
                "text": "Megkezdődött a gyalázatos 'padlássöprés'. A felügyelők a padlások deszkáit is felbontották, és elvitték az utolsó zsák búzát, a füstölt szalonnát és még a jövő évi vetőmagot is. A cél az önálló paraszti lét megtörése és a kollektivizálás, a termelőszövetkezetekbe (téesz) való kényszerítés volt."
            },
            {
                "type": "dialogue",
                "speaker": "Alföldi gazda",
                "text": "A föld a vérünk, a kenyerünk volt generációkon át. Most elvették az igáslovunkat, a búzánkat, s még minket neveznek kizsákmányolónak a saját szülőföldünkön!"
            },
            {
                "type": "narration",
                "text": "Ezzel párhuzamosan épült a puszta közepén Sztálinváros és a hatalmas Dunai Vasmű. 'A vas és acél országa leszünk!' – hangoztatta a jelszó, miközben Magyarországnak sem vasérce, sem kokszolható szene nem volt. A gazdaság a szakadék szélére sodródott, megalapozva az 1956-os népharagot."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak-05-kulak.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.rakosikorszak.combined",
        "title": "A Rákosi-korszak története: Diktatúra, ÁVH-terror és gazdasági összeomlás (1945–1956)",
        "level": "B1",
        "order": 24,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive Rest is History synthesis of post-WWII Hungary under Stalinism: the liquidation of democracy through 'salami tactics' and fraudulent 1947 elections, Mátyás Rákosi's suffocating cult of personality and one-party state, ÁVH secret police terror at Andrássy út 60 and Recsk, fabricated show trials (Rajk, Mindszenty), and agrarian devastation through padlássöprés and heavy industrial dogma.",
        "characters": [
            "Rákosi Mátyás diktátor és Péter Gábor ÁVH-vezér",
            "Mindszenty József bíboros és Rajk László",
            "A diktatúra üldözöttei: parasztok, polgárok és recski rabok"
        ],
        "location": "Budapest, Andrássy út 60., Recsk és az Alföld",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A második világháború után Magyarország a szovjet megszállási övezetbe került. Bár az 1945-ös szabad választásokon a polgári Kisgazdapárt győzött, a szovjet tankok támogatását élvező Magyar Kommunista Párt Rákosi Mátyás vezetésével 'szalámitaktikával' és az 1947-es kékcédulás választási csalással felszámolta a többpártrendszert."
            },
            {
                "type": "narration",
                "text": "1949-ben megszületett a szovjet mintájú sztálini alkotmány, s kiépült a totális pártállam. Rákosi körül nyomasztó személyi kultusz bontakozott ki, miközben a gazdaságot az értelmetlen 'vas és acél országa' dogmának rendelték alá."
            },
            {
                "type": "narration",
                "text": "A rendszer védelmét az Államvédelmi Hatóság (ÁVH) kegyetlen terrorja biztosította. Az Andrássy út 60. alatti börtönben ezreket kínoztak meg, polgári családok tömegeit telepítették ki a fővárosból, a politikai ellenfeleket pedig bírósági ítélet nélkül hurcolták a recski kényszermunkatáborba."
            },
            {
                "type": "narration",
                "text": "Koncepciós perek sorozatával tiporták el az egyházakat és a független gondolkodókat: Mindszenty József bíborost életfogytiglanra ítélték, a párt belső tisztogatásában pedig még a korábbi belügyminisztert, Rajk Lászlót is kivégezték koholt vádak alapján."
            },
            {
                "type": "narration",
                "text": "A vidéki társadalmat a kuláküldözés, az erőszakos téeszesítés és a megalázó 'padlássöprések' döntötték nyomorba. A félelemre és hazugságra épülő sztálini diktatúra elviselhetetlenné vált: a felgyülemlett keserűség egyenesen vezetett az 1956-os forradalom és szabadságharc lángjaihoz."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-rakosikorszak.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        ex_data = {
            "lesson": f"b1-rakosikorszak-{padded}",
            "exercises": [
                {
                    "id": f"b1-rakosikorszak-{padded}.ex01",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelentett a 'szalámitaktika' a kommunista hatalomátvétel idején?",
                    "options": [
                        "A demokratikus ellenzéki pártok módszeres, szeletenkénti felszámolását.",
                        "A szalámigyárak államosításának gazdasági programját.",
                        "Egy új élelmiszerjegy-rendszer bevezetését."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A kommunista párt lépésről lépésre számolta _____ a demokratikus intézményeket. (dismantled - fel)",
                    "answer": "fel"
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1949-ben rögzítette a szovjet mintájú alkotmány a párt_____ egyeduralmát. (one-party state - állam)",
                    "answer": "állam"
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex04",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Az", "ÁVH", "rettegett", "fekete", "autói", "éjjel", "hurcolták", "el", "az", "embereket."],
                    "solution": ["Az", "ÁVH", "rettegett", "fekete", "autói", "éjjel", "hurcolták", "el", "az", "embereket."]
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt a recski tábor 1950 és 1953 között?",
                    "options": [
                        "Titkos kényszermunkatábor a Mátra hegyei között bírósági ítélet nélkül elhurcolt foglyoknak.",
                        "Egy ifjúsági úttörőtábor nyári pihenésre.",
                        "A Nemzeti Bank aranytartalékának földalatti raktára."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Rajk Lászlót koholt vádak alap_____ ítélték halálra a kirakatperben. (on the basis of - ján)",
                    "answer": "ján"
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "padlássöprések", "során", "az", "utolsó", "zsák", "búzát", "is", "elrekvirálták."],
                    "solution": ["A", "padlássöprések", "során", "az", "utolsó", "zsák", "búzát", "is", "elrekvirálták."]
                },
                {
                    "id": f"b1-rakosikorszak-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen irreális iparpolitikai jelszót erőltetett a Rákosi-rezsim a gazdaságban?",
                    "options": [
                        "'A vas és acél országa leszünk!' – nyersanyagok nélküli erőltetett nehézipart építve.",
                        "'A tiszta digitális technológia úttörői vagyunk!'",
                        "'Minden falunak önálló szélmalmot és napkollektort!'"
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-rakosikorszak-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-rakosikorszak-consolidation",
        "exercises": [
            {
                "id": "b1-rakosikorszak-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szalámitaktika", "demokrácia szeletenkénti felszámolása"],
                    ["Andrássy út 60", "ÁVH kihallgató és kínzóközpontja"],
                    ["Mindszenty József", "életfogytiglanra ítélt bíboros"],
                    ["padlássöprés", "paraszti gabona erőszakos elvétele"]
                ]
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás jellemzi a koncepciós pereket a Rákosi-diktatúrában?",
                "options": [
                    "A vádiratot és az ítéletet előre megírták a pártban, a vallomásokat kínzással csikarták ki.",
                    "A vádlottak szabadon választhattak nemzetközi ügyvédeket a független bíróság előtt.",
                    "A tárgyalások mindig nyilvános televíziós élő adásban zajlottak."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A rettegett Államvédelmi Hatóságot a korabeli köznyelvben _____ néven emlegették. (ÁVH - ÁVH)",
                "answer": "ÁVH"
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A diktatúra feltétlen hűséget köve_____ minden állampolgártól. (demanded - telt)",
                "answer": "telt"
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kitelepített", "családokat", "marhavagonokban", "szállították", "a", "hortobágyi", "pusztába."],
                "solution": ["A", "kitelepített", "családokat", "marhavagonokban", "szállították", "a", "hortobágyi", "pusztába."]
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kiket bélyegeztek 'kuláknak' a falvakban?",
                "options": [
                    "A tehetősebb, földdel rendelkező gazdákat, akiket osztályellenségnek nyilvánítottak.",
                    "A városból érkező fiatal pedagógusokat.",
                    "A postagalambokat tenyésztő hobbistákat."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Rákosi Mátyás körül nyomasztó személyi _____ alakult ki a kommunista médiában. (cult - kultusz)",
                "answer": "kultusz"
            },
            {
                "id": "b1-rakosikorszak-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan értékelik a történészek a Rákosi-korszak következményeit Magyarországon?",
                "options": [
                    "Totális terroron alapuló, a gazdaságot romlásba döntő korszaknak, amely elkerülhetetlenné tette az 1956-os forradalmat.",
                    "A magyar mezőgazdaság és ipar legsikeresebb aranykorának.",
                    "Egy békés és demokratikus jóléti társadalom mintapéldájának."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakosikorszak-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Szalámitaktika és kékcédulás választások", "Liquidation of Democracy (1945–1948)"),
        "02": ("A pártállam és a személyi kultusz", "Totalitarian State & Cult of Personality"),
        "03": ("Az ÁVH és a megfélemlítés", "Secret Police, Andrássy út 60 & Recsk"),
        "04": ("Koncepciós perek és kirakatperek", "Show Trials: Mindszenty and Rajk"),
        "05": ("Padlássöprés és a vas országa", "Attic Sweeping & Command Economy")
    }

    story_refs = {
        "01": "stories/world/b1/b1-rakosikorszak-01-szalami.json",
        "02": "stories/world/b1/b1-rakosikorszak-02-szemelyikultusz.json",
        "03": "stories/world/b1/b1-rakosikorszak-03-avh.json",
        "04": "stories/world/b1/b1-rakosikorszak-04-koncepcio.json",
        "05": "stories/world/b1/b1-rakosikorszak-05-kulak.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.rakosikorszak-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Authoritarian Mechanics, Totalitarian Discourse & State Terror Register",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungary's communist history.",
                        "I can analyze the mechanisms of dictatorship, show trials, and command economy in Hungarian.",
                        "I can answer essential citizenship interview questions regarding the Rákosi era and totalitarian terror.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-rakosikorszak-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-rakosikorszak-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-rakosikorszak-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-rakosikorszak-{padded}.ex01",
                        f"b1-rakosikorszak-{padded}.ex02",
                        f"b1-rakosikorszak-{padded}.ex03",
                        f"b1-rakosikorszak-{padded}.ex04",
                        f"b1-rakosikorszak-{padded}.ex05",
                        f"b1-rakosikorszak-{padded}.ex06",
                        f"b1-rakosikorszak-{padded}.ex07",
                        f"b1-rakosikorszak-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-rakosikorszak-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.rakosikorszak-consolidation",
        "title": "Összefoglalás: A kommunista diktatúra és a Rákosi-korszak (The Rákosi Era Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of Totalitarian History, ÁVH State Terror & Show Trials",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-rakosikorszak.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-rakosikorszak-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-rakosikorszak-consolidation.ex01",
                    "b1-rakosikorszak-consolidation.ex02",
                    "b1-rakosikorszak-consolidation.ex03",
                    "b1-rakosikorszak-consolidation.ex04",
                    "b1-rakosikorszak-consolidation.ex05",
                    "b1-rakosikorszak-consolidation.ex06",
                    "b1-rakosikorszak-consolidation.ex07",
                    "b1-rakosikorszak-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-rakosikorszak-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 24 (b1-rakosikorszak)!")

if __name__ == "__main__":
    build_unit_24_citizenship()
