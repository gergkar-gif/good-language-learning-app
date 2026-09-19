#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 22: The Interwar Years (b1-horthykorszak)."""

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

def build_unit_22_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.horthykorszak.01",
        "lesson": "b1-horthykorszak-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kormányzó", "translation": "Regent (head of state of Hungary 1920–1944)", "pos": "noun"},
            {"lemma": "király nélküli királyság", "translation": "kingdom without a king (constitutional status)", "pos": "noun"},
            {"lemma": "tengernagy", "translation": "admiral (Horthy's former Austro-Hungarian naval rank)", "pos": "noun"},
            {"lemma": "restauráció", "translation": "royal restoration (attempts by King Charles IV to reclaim the throne)", "pos": "noun"},
            {"lemma": "trónfosztás", "translation": "dethronement of the Habsburg dynasty (1921)", "pos": "noun"},
            {"lemma": "jogkör", "translation": "scope of constitutional authority / executive prerogative", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-horthykorszak-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.horthykorszak.02",
        "lesson": "b1-horthykorszak-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Bethlen István", "translation": "Count István Bethlen (prime minister 1921–1931)", "pos": "noun"},
            {"lemma": "konszolidáció", "translation": "political and economic consolidation / stabilization", "pos": "noun"},
            {"lemma": "Népszövetség", "translation": "League of Nations (provided vital stabilization loan in 1924)", "pos": "noun"},
            {"lemma": "pengő", "translation": "pengő (stable new national currency introduced in 1927)", "pos": "noun"},
            {"lemma": "Nemzeti Bank", "translation": "Magyar Nemzeti Bank (Hungarian Central Bank, founded 1924)", "pos": "noun"},
            {"lemma": "Bethlen-Peyer paktum", "translation": "Bethlen-Peyer pact (agreement between government and Social Democrats)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-horthykorszak-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.horthykorszak.03",
        "lesson": "b1-horthykorszak-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Klebelsberg Kuno", "translation": "Count Kuno Klebelsberg (Minister of Religion and Education 1922–1931)", "pos": "noun"},
            {"lemma": "kultúrfölény", "translation": "cultural superiority / cultural elevation doctrine", "pos": "noun"},
            {"lemma": "népiskola", "translation": "rural folk elementary school (nationwide school construction campaign)", "pos": "noun"},
            {"lemma": "Szegedi Tudományegyetem", "translation": "University of Szeged (refugee university from Kolozsvár)", "pos": "noun"},
            {"lemma": "Szent-Györgyi Albert", "translation": "Albert Szent-Györgyi (Nobel laureate, isolated Vitamin C from paprika)", "pos": "noun"},
            {"lemma": "Collegium Hungaricum", "translation": "Collegium Hungaricum (Hungarian cultural institutes in Vienna, Berlin, Rome)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-horthykorszak-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.horthykorszak.04",
        "lesson": "b1-horthykorszak-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "úri középosztály", "translation": "'gentlemanly' middle class (civil servants, officers, professionals)", "pos": "noun"},
            {"lemma": "dzsentri", "translation": "gentry (impoverished historic nobility serving in bureaucracy)", "pos": "noun"},
            {"lemma": "hárommillió koldus", "translation": "'three million beggars' (contemporary term for landless agrarian poor)", "pos": "noun"},
            {"lemma": "nagybirtokrendszer", "translation": "large landed estate system (feudal land distribution)", "pos": "noun"},
            {"lemma": "kávéházi kultúra", "translation": "vibrant urban coffeehouse culture and literary life of Budapest", "pos": "noun"},
            {"lemma": "társadalmi mobilitás", "translation": "social mobility (restricted movement between social strata)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-horthykorszak-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.horthykorszak.05",
        "lesson": "b1-horthykorszak-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "revíziós politika", "translation": "territorial revisionist foreign policy", "pos": "noun"},
            {"lemma": "olasz-magyar barátsági szerződés", "translation": "Italian-Hungarian Treaty of Friendship (1927, breaking diplomatic isolation)", "pos": "noun"},
            {"lemma": "tengelyhatalmak", "translation": "Axis Powers (Rome-Berlin-Tokyo axis alignment)", "pos": "noun"},
            {"lemma": "első bécsi döntés", "translation": "First Vienna Award (Nov 2, 1938: return of ethnic Hungarian southern Slovakia)", "pos": "noun"},
            {"lemma": "fegyveres semlegesség", "translation": "armed neutrality (Teleki Pál's strategic diplomatic aim)", "pos": "noun"},
            {"lemma": "revíziós eufória", "translation": "revision euphoria (public celebration of peaceful territorial returns)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-horthykorszak-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.horthykorszak.01.future-participle",
        "title": "The Obligatory Future Participle: -andó / -endő",
        "sections": [
            {
                "type": "text",
                "title": "Formation and Meaning of -andó / -endő",
                "content": "In formal legal, historical, and administrative Hungarian, the participle *-andó / -endő* expresses necessity, obligation, or an action to be performed: *megoldandó feladat* ('a task to be solved'), *követendő példa* ('an example to be followed'), *elvégzendő munka* ('work that must be carried out')."
            },
            {
                "type": "examples",
                "title": "Historical and Legal Usage",
                "items": [
                    {
                        "spanish": "Az ország újjáépítése az 1920-as években sürgősen megoldandó feladat volt.",
                        "english": "The reconstruction of the country in the 1920s was an urgently to-be-solved task."
                    },
                    {
                        "spanish": "A miniszterelnök kijelölte a kormány által követendő politikai irányvonalat.",
                        "english": "The Prime Minister indicated the political guideline to be followed by the government."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-horthykorszak-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.horthykorszak.02.instrumental-subordination",
        "title": "Institutional Instrumentality: révén, útján, által",
        "sections": [
            {
                "type": "text",
                "title": "Postpositions of Means and Agency",
                "content": "Historical narratives describe political and financial instruments using postpositions: *a Népszövetség kölcsöne révén* ('by means of the League of Nations loan'), *törvényes úton* ('by lawful means'), *a minisztérium által* ('by the ministry'). These structures are indispensable for formal citizenship examination essays."
            },
            {
                "type": "examples",
                "title": "Administrative discourse",
                "items": [
                    {
                        "spanish": "A gazdasági stabilitást a Nemzeti Bank felállítása és a pengő bevezetése révén érték el.",
                        "english": "Economic stability was achieved by means of establishing the National Bank and introducing the pengő."
                    },
                    {
                        "spanish": "A reformokat parlamenti szavazás útján emelték törvényerőre.",
                        "english": "The reforms were enacted into law by means of a parliamentary vote."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-horthykorszak-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.horthykorszak.03.purpose-clauses",
        "title": "Complex Purpose Clauses: azzal a céllal, annak érdekében hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Grand Policy Objectives",
                "content": "To explain the ideological aims of reforms, Hungarian uses: *azzal a céllal, hogy...* ('with the goal that...'), *annak érdekében, hogy...* ('in the interest of / so that...'), followed by the imperative-subjunctive (*hogy fellendítse*, *hogy megteremtse*)."
            },
            {
                "type": "examples",
                "title": "Educational reform goals",
                "items": [
                    {
                        "spanish": "Klebelsberg Kuno ötezer népiskolát építtetett azzal a céllal, hogy felszámolja az analfabétizmust.",
                        "english": "Kuno Klebelsberg had 5,000 folk schools built with the aim of eradicating illiteracy."
                    },
                    {
                        "spanish": "A kormány modern kutatóhelyeket támogatott annak érdekében, hogy a magyar tudomány világszínvonalra emelkedjen.",
                        "english": "The government supported modern research centers so that Hungarian science would rise to world standards."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-horthykorszak-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.horthykorszak.04.honorific-hierarchy",
        "title": "Social Honorifics and Bureaucratic Registers: Méltóságos úr, Kegyelmes úr",
        "sections": [
            {
                "type": "text",
                "title": "Interwar Protocol and Titles",
                "content": "The interwar period was known as the 'úri Magyarország' (gentlemanly Hungary), characterized by strict honorific forms of address in public life: *Kegyelmes úr* (for ministers), *Méltóságos úr* (for high civil servants, generals), *Nagyságos úr* (for middle-ranking officials)."
            },
            {
                "type": "examples",
                "title": "Historical titles in context",
                "items": [
                    {
                        "spanish": "A hivatalokban a legapróbb részletekig tiszteletben tartották az udvarias megszólítási formákat.",
                        "english": "In government offices, polite forms of address were respected down to the smallest detail."
                    },
                    {
                        "spanish": "A kávéházi társalgások során az írók gyakran gúnyosan ábrázolták a merev társadalmi szokásokat.",
                        "english": "During coffeehouse conversations, writers often satirized rigid social customs."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-horthykorszak-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.horthykorszak.05.temporal-geopolitics",
        "title": "Temporal Connectors in Geopolitical History: miután, párhuzamosan azzal hogy",
        "sections": [
            {
                "type": "text",
                "title": "Sequencing Diplomatic Shifts",
                "content": "Describing foreign policy changes requires exact chronological subordinators: *miután* ('after / once'), *mielőtt* ('before'), *párhuzamosan azzal, hogy...* ('in parallel with the fact that...'), *aminek következtében* ('as a consequence of which')."
            },
            {
                "type": "examples",
                "title": "Diplomatic timelines",
                "items": [
                    {
                        "spanish": "Miután az európai nagyhatalmak aláírták a müncheni egyezményt, megnyílt az út a magyar revízió előtt.",
                        "english": "After the European great powers signed the Munich Agreement, the way opened for Hungarian revision."
                    },
                    {
                        "spanish": "Párhuzamosan a területi sikerekkel megnőtt a német gazdasági és katonai befolyás is.",
                        "english": "In parallel with territorial successes, German economic and military influence also grew."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-horthykorszak-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Stories (World / Rest-is-History Style)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.horthykorszak.01",
        "lesson": 1,
        "order": 1,
        "title": "A király nélküli királyság: Horthy Miklós megválasztása",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Following the collapse of 1918 and the turmoil of the Soviet Republic, Hungary restored its constitutional form as a kingdom. On March 1, 1920, the National Assembly elected former Austro-Hungarian admiral Miklós Horthy as Regent (kormányzó), establishing a unique political system: a kingdom without a king.",
        "characters": [
            "Horthy Miklós, kormányzó",
            "Országgyűlési képviselő",
            "Budapesti polgár"
        ],
        "location": "Budapest, Országház és a Gellért Szálló",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1920 kora tavaszán a háborúban megtépázott és idegen csapatok által megszállt Magyarország a politikai túlélésért küzdött. Az Országgyűlés úgy döntött, hogy fenntartja az ezeréves államformát, a királyságot, ám az üres trónra nem hívtak meg új uralkodót."
            },
            {
                "type": "narration",
                "text": "Március 1-jén a parlament elsöprő többséggel kormányzóvá választotta Horthy Miklóst, a Monarchia egykori kiváló tengernagyát. Ezzel létrejött a 20. század egyik legkülönösebb alkotmányos berendezkedése: a király nélküli királyság, amelyet egy flotta nélküli tengernagy vezetett."
            },
            {
                "type": "dialogue",
                "speaker": "Országgyűlési képviselő",
                "text": "Horthy kormányzó úr személye garancia a rendre és az alkotmányos folytonosságra. Az ország megmentése most mindenek felett álló, sürgősen megoldandó feladat!"
            },
            {
                "type": "narration",
                "text": "Az utolsó Habsburg uralkodó, IV. Károly király kétszer is megpróbált visszatérni a magyar trónra 1921-ben. A szomszédos államok fegyveres beavatkozással fenyegettek, ezért Horthy kormánya kénytelen volt meghozni a Habsburg-ház trónfosztását kimondó törvényt."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti polgár",
                "text": "A király visszatérése újabb háborút jelentett volna. Bármennyire fájdalmas volt is, a kormányzó józan döntése megvédte az ország maradékát a teljes pusztulástól."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak-01-kormanyzo.json", story_01)

    story_02 = {
        "id": "story.b1.horthykorszak.02",
        "lesson": 2,
        "order": 2,
        "title": "A bethleni konszolidáció és a pengő sikere",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Count István Bethlen assumed the prime ministership in 1921, launching an extraordinary decade of political and financial stabilization. Through a major League of Nations loan, he established the National Bank and introduced the pengő, rescuing the nation from runaway inflation.",
        "characters": [
            "Gróf Bethlen István, miniszterelnök",
            "Peyer Károly, szociáldemokrata vezető",
            "Pénzügyi szakember"
        ],
        "location": "Budapest, Sándor-palota és a Magyar Nemzeti Bank",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1921-ben gróf Bethlen István került a miniszterelnöki székbe. Híres jelmondata – 'Konszolidálni kell!' – egy évtizedre meghatározta a magyar belpolitikát. Célja a politikai béke helyreállítása és a romokban heverő gazdaság talpra állítása volt."
            },
            {
                "type": "narration",
                "text": "Bethlen megkötötte a kompromisszumot a baloldallal: a Bethlen-Peyer paktum révén a Szociáldemokrata Párt legálisan működhetett a parlamentben, cserébe garantálta a mezőgazdasági sztrájkok elkerülését."
            },
            {
                "type": "dialogue",
                "speaker": "Gróf Bethlen István",
                "text": "A rombolás korszaka véget ért. Most a higgadt munka, a pénzügyi rend és az építkezés ideje jött el. Ha megbízhatóságot mutatunk, a világ újra hinni fog Magyarországban."
            },
            {
                "type": "narration",
                "text": "A legfontosabb áttörést a Népszövetség által nyújtott 250 millió aranykoronás stabilizációs kölcsön jelentette 1924-ben. Ebből megalapították a Magyar Nemzeti Bankot, megfékezték az inflációt, és 1927-ben bevezették az új, stabil nemzeti valutát: a pengőt."
            },
            {
                "type": "dialogue",
                "speaker": "Pénzügyi szakember",
                "text": "A pengő Európa egyik legstabilabb valutájává vált. A boltok polcain újra van áru, a munkások végre értékálló fizetést kapnak, s a gazdaság vérkeringése megindult!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak-02-bethlen.json", story_02)

    story_03 = {
        "id": "story.b1.horthykorszak.03",
        "lesson": 3,
        "order": 3,
        "title": "Klebelsberg Kuno és a kultúrfölény programja",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Count Kuno Klebelsberg, minister of education, launched a legendary cultural renaissance. Believing that Hungary could regain its international respect through knowledge and intellectual excellence ('kultúrfölény'), he built 5,000 rural elementary schools, relocated universities to Szeged and Debrecen, and established Collegium Hungaricum institutes across Europe.",
        "characters": [
            "Gróf Klebelsberg Kuno, kultuszminiszter",
            "Szent-Györgyi Albert, kutatóorvos",
            "Tanyasi tanító Csongrád vármegyében"
        ],
        "location": "Szeged, Dóm tér és egy alföldi tanyasi népiskola",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A trianoni határok közé szorított Magyarország vezetői tudták: a fegyveres revízió lehetetlen. Gróf Klebelsberg Kuno vallás- és közoktatásügyi miniszter meghirdette a 'kultúrfölény' doktrínáját: a nemzet felemelkedésének egyetlen biztos záloga az oktatás és a tudomány."
            },
            {
                "type": "dialogue",
                "speaker": "Gróf Klebelsberg Kuno",
                "text": "Katonailag legyőztek bennünket, de a szellem, a kultúra és a tudomány terén nem győzhetnek le! Minden tanyasi gyermek számára meg kell nyitnunk az iskola kapuját!"
            },
            {
                "type": "narration",
                "text": "Klebelsberg gigantikus iskolaépítési programot indított: néhány év leforgása alatt ötezer tantermet és tanítói lakást húztak fel a vidéki tanyavilágban. Az elcsatolt Kolozsvár egyetemét Szegedre költöztette, ahol felépült a monumentális Dóm tér és a modern laboratóriumok sora."
            },
            {
                "type": "dialogue",
                "speaker": "Szent-Györgyi Albert",
                "text": "Klebelsberg személyesen hívott vissza Angliából Szegedre. Itt, az új egyetemi intézetben tudtam izolálni a C-vitamint a szegedi fűszerpaprikából, amiért 1937-ben orvosi Nobel-díjjal jutalmaztak!"
            },
            {
                "type": "narration",
                "text": "Bécsben, Berlinben és Rómában megalapították a Collegium Hungaricum intézeteket, hogy a tehetséges magyar egyetemisták a legkiválóbb európai professzoroktól tanulhassanak, hazatérve pedig modern európai tudással gyarapítsák hazájukat."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak-03-klebelsberg.json", story_03)

    story_04 = {
        "id": "story.b1.horthykorszak.04",
        "lesson": 4,
        "order": 4,
        "title": "A két háború közötti társadalom: Fények és árnyak",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungarian society between the wars was a study in contrasts. While Budapest flourished with world-class coffeehouses, cinema, and literary magazines like 'Nyugat', the rural countryside was burdened by rigid landed estates and millions of struggling agrarian laborers.",
        "characters": [
            "Budapesti újságíró a New York kávéházban",
            "Falukutató szociográfus",
            "Vidéki zsellérlegény"
        ],
        "location": "Budapest, New York Kávéház és a dél-alföldi falu",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A két világháború közötti Magyarországot mély társadalmi szakadékok jellemezték. A fővárosban virágzott az elegáns kávéházi kultúra: a New York kávéház márványasztalai körül írták remekműveiket a 'Nyugat' írói és költői, s a mozikban már a magyar hangosfilm legújabb slágereit énekelték."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti újságíró",
                "text": "Budapest igazi világváros! A körutakon pezseg az élet, az elegáns kávéházakban a modern irodalom és a színház a fő téma. Ám elég néhány kilométert utazni vidékre, hogy egy egészen más világba csöppenjünk."
            },
            {
                "type": "narration",
                "text": "A vidéki Magyarországon a konzervatív nagybirtokrendszer uralta a tájat. A mezőgazdasági népesség jelentős része, mintegy hárommillió ember – akiket a szociográfusok 'hárommillió koldusnak' neveztek – föld és vagyon nélkül, napszámból és idénymunkából tengődött."
            },
            {
                "type": "dialogue",
                "speaker": "Falukutató szociográfus",
                "text": "A népi írók és szociográfusok feladata, hogy megmutassák a valóságot. Nem elég az úri középosztály eleganciája: átfogó földreform és a szegényparasztság felemelése nélkül nincs jövője a nemzetnek!"
            },
            {
                "type": "narration",
                "text": "A merev társadalmi hierarchia ellenére az iparosodás, az oktatás elterjedése és a városiasodás lassan megnyitotta az utat a társadalmi mobilitás előtt."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak-04-tarsadalom.json", story_04)

    story_05 = {
        "id": "story.b1.horthykorszak.05",
        "lesson": 5,
        "order": 5,
        "title": "A revíziós sikerek és az első bécsi döntés (1938)",
        "level": "B1",
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary pursued peaceful territorial revision throughout the interwar years. Following the Munich conference, the First Vienna Award on November 2, 1938, returned predominantly ethnic Hungarian areas of southern Slovakia (Felvidék) to Hungary, triggering national euphoria but deepening diplomatic dependence on the Axis powers.",
        "characters": [
            "Kassai magyar tanító",
            "Budapesti diplomata",
            "Horthy Miklós kormányzó fehér lovon"
        ],
        "location": "Bécs, Belvedere kastély és Kassa főtere",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A trianoni trauma után a magyar külpolitika legfőbb célja a határrevízió volt. Magyarország először Olaszországgal kötött barátsági szerződést 1927-ben, hogy kitörjön a diplomáciai elszigeteltségből, majd a harmincas években fokozatosan a tengelyhatalmak befolyási övezetébe sodródott."
            },
            {
                "type": "narration",
                "text": "1938 őszén, a müncheni egyezmény után a német és az olasz külügyminiszter a bécsi Belvedere kastélyban hirdette ki az első bécsi döntést: a Felvidék túlnyomórészt magyarok lakta déli sávját, mintegy 12 000 négyzetkilométert visszacsatoltak Magyarországhoz."
            },
            {
                "type": "dialogue",
                "speaker": "Kassai magyar tanító",
                "text": "Húsz éven át vártunk erre a napra! Amikor a magyar honvédek bevonultak a feldíszített kassai dóm elé, sírtunk a boldogságtól. Újra szabadon tanulhatnak a gyermekeink a szülőföldjükön!"
            },
            {
                "type": "narration",
                "text": "Horthy Miklós fehér lován vonult be Komáromba és Kassára a lakosság határtalan ujjongása közepette. Az országban revíziós eufória uralkodott: a határok békés módosítása igazolni látszott a kormány politikáját."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti diplomata",
                "text": "A területi revízió óriási öröm az egész nemzetnek, de a politikai ára rettentő súlyos. Végzetesen leköteleztük magunkat a tengelyhatalmak mellett, s a közeledő viharban rendkívül nehéz lesz megőrizni a fegyveres semlegességet."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak-05-revizio.json", story_05)

    # Combined comprehensive story for consolidation
    story_combined = {
        "id": "story.b1.horthykorszak.combined",
        "title": "A Horthy-korszak története: Konszolidáció, kultúra és revízió (1920–1939)",
        "level": "B1",
        "order": 22,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A complete historical synthesis of interwar Hungary: the election of Regent Miklós Horthy in 1920, Count Bethlen's monetary and political consolidation with the pengő, Count Klebelsberg's cultural and educational breakthrough (Szent-Györgyi's Nobel Prize), social realities of 'úri Magyarország', and the diplomatic revisionism leading to the First Vienna Award in 1938.",
        "characters": [
            "Horthy Miklós kormányzó",
            "Gróf Bethlen István és Gróf Klebelsberg Kuno",
            "Szent-Györgyi Albert Nobel-díjas tudós",
            "A korszak polgárai és parasztsága"
        ],
        "location": "Budapest, Szeged, Kassa és az Alföld",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az első világháború és Trianon után Magyarország a szakadék szélén állt. 1920. március 1-jén az Országgyűlés Horthy Miklóst választotta meg kormányzóvá, s az államforma király nélküli királyság maradt. A Habsburg restaurációs kísérletek kudarca után a nemzet az önálló talpra állás útjára lépett."
            },
            {
                "type": "narration",
                "text": "A húszas években gróf Bethlen István miniszterelnök vezetésével megvalósult a történelmi konszolidáció. A Népszövetségi kölcsön segítségével 1924-ben megalapították a Nemzeti Bankot, és 1927-ben megszületett a korszak szilárd fizetőeszköze, a pengő."
            },
            {
                "type": "narration",
                "text": "A gazdasági rend megteremtésével párhuzamosan Klebelsberg Kuno kultuszminiszter a kultúrfölény eszméjére építve megújította az oktatást: 5000 népiskolai tantermet építtetett, felvirágoztatta a Szegedi Tudományegyetemet – ahol Szent-Györgyi Albert C-vitaminos kutatásait Nobel-díjjal koronázták –, és megalapította a külföldi Collegium Hungaricumokat."
            },
            {
                "type": "narration",
                "text": "Társadalmilag az úri középosztály tekintélye uralkodott, miközben az irodalom a budapesti kávéházakban virágzott. Ugyanakkor a szegényparasztság 'hárommillió koldusa' mély nélkülözésben élt, felhívva a népi írók és szociográfusok figyelmét a halaszthatatlan szociális reformok szükségességére."
            },
            {
                "type": "narration",
                "text": "A harmincas évek végén a nemzetközi események sodrásában Magyarország elérte első nagy külpolitikai sikerét: az 1938-as első bécsi döntéssel visszatért a Felvidék túlnyomórészt magyarok lakta része. A revíziós mámor azonban előrevetítette a második világháborúba való végzetes sodródás veszélyét is."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-horthykorszak.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        ex_data = {
            "lesson": f"b1-horthykorszak-{padded}",
            "exercises": [
                {
                    "id": f"b1-horthykorszak-{padded}.ex01",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen tisztséget töltött be Horthy Miklós 1920 és 1944 között?",
                    "options": [
                        "Kormányzó volt a király nélküli királyság államfőjeként.",
                        "Magyarország megkoronázott királya volt.",
                        "A Szociáldemokrata Párt elnöke és pénzügyminiszter."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az ország gazdasági újjáépítése sürgősen megol_____ feladat volt a világháború után. (to be solved - dandó)",
                    "answer": "dandó"
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1927-ben vezették be a korszak új, értékálló valutáját, a _____. (new currency - pengőt)",
                    "answer": "pengőt"
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex04",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "kormány", "a", "Népszövetség", "kölcsöne", "révén", "állította", "helyre", "a", "pénzügyi", "egyensúlyt."],
                    "solution": ["A", "kormány", "a", "Népszövetség", "kölcsöne", "révén", "állította", "helyre", "a", "pénzügyi", "egyensúlyt."]
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi jellemezte Klebelsberg Kuno kultúrpolitikáját?",
                    "options": [
                        "A 'kultúrfölény' eszméje: az iskolák, egyetemek és a kutatás kiemelt támogatása.",
                        "Minden vidéki iskola azonnali bezárása költségtakarékosságból.",
                        "Kizárólag a katonai hadfelszerelés fejlesztése az oktatás helyett."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Ötezer népiskolát építettek azzal a céllal, _____ felszámolják az analfabétizmust. (that - hogy)",
                    "answer": "hogy"
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Szent-Györgyi", "Albert", "Szegeden", "izolálta", "a", "paprikából", "a", "C-vitamint."],
                    "solution": ["Szent-Györgyi", "Albert", "Szegeden", "izolálta", "a", "paprikából", "a", "C-vitamint."]
                },
                {
                    "id": f"b1-horthykorszak-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen eredményt hozott az 1938-as első bécsi döntés?",
                    "options": [
                        "Visszacsatolták Magyarországhoz a Felvidék túlnyomórészt magyarok lakta déli területeit.",
                        "Magyarország teljes egészében kilépett a Népszövetségből.",
                        "Új királyt választottak a magyar trónra a Habsburg-házból."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-horthykorszak-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-horthykorszak-consolidation",
        "exercises": [
            {
                "id": "b1-horthykorszak-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Horthy Miklós", "kormányzó (1920–1944)"],
                    ["Bethlen István", "konszolidáció és a pengő"],
                    ["Klebelsberg Kuno", "kultúrfölény és népiskolák"],
                    ["Szent-Györgyi Albert", "orvosi Nobel-díj (1937)"]
                ]
            },
            {
                "id": "b1-horthykorszak-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás foglalja össze legpontosabban a két világháború közötti Magyarország államformáját?",
                "options": [
                    "Királyság volt betöltetlen trónnal, amelynek élén a kormányzó állt államfőként.",
                    "Demokratikus köztársaság volt közvetlenül választott köztársasági elnökkel.",
                    "Katonai diktatúra volt alkotmány és parlamentáris választások nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-horthykorszak-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A történelmi Habsburg-dinasztia trón_____át 1921-ben rögzítette a magyar törvényhozás. (dethronement - fosztás)",
                "answer": "fosztás"
            },
            {
                "id": "b1-horthykorszak-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar külpolitika a békés revízió követ_____ példáját igyekezett felmutatni. (to be followed - endő)",
                "answer": "endő"
            },
            {
                "id": "b1-horthykorszak-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "konszolidáció", "révén", "Magyarország", "visszanyerte", "nemzetközi", "pénzügyi", "hitelképességét."],
                "solution": ["A", "konszolidáció", "révén", "Magyarország", "visszanyerte", "nemzetközi", "pénzügyi", "hitelképességét."]
            },
            {
                "id": "b1-horthykorszak-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kikre utalt a korabeli szociográfiában a 'hárommillió koldus' kifejezés?",
                "options": [
                    "A földtelen és szegény mezőgazdasági cselédségre és parasztságra.",
                    "A külföldre emigrált bankárokra és gyárosokra.",
                    "A budapesti egyetemek külföldi ösztöndíjas diákjaira."
                ],
                "correct": 0
            },
            {
                "id": "b1-horthykorszak-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A magyar honvédség komáromi bevonulásakor országszerte revíziós _____ tört ki. (euphoria - eufória)",
                "answer": "eufória"
            },
            {
                "id": "b1-horthykorszak-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan értékelik a történészek Szent-Györgyi Albert szegedi tudományos munkásságát?",
                "options": [
                    "A modern magyar természettudomány csúcsteljesítménye, amelyet hazai kutatásért tüntettek ki Nobel-díjjal.",
                    "Egy sikertelen kísérletsorozat, amely elpazarolta az egyetem kutatási forrásait.",
                    "Kizárólag külföldi laboratóriumokban elért, Magyarországtól független felfedezés."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-horthykorszak-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Horthy Miklós és a kormányzóság", "The Regency & the Kingdom without a King"),
        "02": ("Bethlen István és a konszolidáció", "Stabilization, League of Nations & Pengő"),
        "03": ("Klebelsberg Kuno és a kultúrfölény", "Education Reform & Nobel Prize"),
        "04": ("A Horthy-korszak társadalma", "Gentry, Coffeehouses & Rural Realities"),
        "05": ("Külpolitikai sodródás és a revízió", "Revisionism & the First Vienna Award")
    }

    story_refs = {
        "01": "stories/world/b1/b1-horthykorszak-01-kormanyzo.json",
        "02": "stories/world/b1/b1-horthykorszak-02-bethlen.json",
        "03": "stories/world/b1/b1-horthykorszak-03-klebelsberg.json",
        "04": "stories/world/b1/b1-horthykorszak-04-tarsadalom.json",
        "05": "stories/world/b1/b1-horthykorszak-05-revizio.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.horthykorszak-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Institutional Participles (-andó/-endő), Instrumentality Connectors & Historical Discourse",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in interwar Hungarian history.",
                        "I can use formal historical participles and instrumentality connectors in Hungarian.",
                        "I can answer essential citizenship interview questions regarding the Horthy era and cultural achievements.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-horthykorszak-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-horthykorszak-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-horthykorszak-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-horthykorszak-{padded}.ex01",
                        f"b1-horthykorszak-{padded}.ex02",
                        f"b1-horthykorszak-{padded}.ex03",
                        f"b1-horthykorszak-{padded}.ex04",
                        f"b1-horthykorszak-{padded}.ex05",
                        f"b1-horthykorszak-{padded}.ex06",
                        f"b1-horthykorszak-{padded}.ex07",
                        f"b1-horthykorszak-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-horthykorszak-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.horthykorszak-consolidation",
        "title": "Összefoglalás: A két világháború közötti időszak (The Interwar Years Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of the Interwar Regency, Cultural Reforms & Territorial Revisionism",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-horthykorszak.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-horthykorszak-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-horthykorszak-consolidation.ex01",
                    "b1-horthykorszak-consolidation.ex02",
                    "b1-horthykorszak-consolidation.ex03",
                    "b1-horthykorszak-consolidation.ex04",
                    "b1-horthykorszak-consolidation.ex05",
                    "b1-horthykorszak-consolidation.ex06",
                    "b1-horthykorszak-consolidation.ex07",
                    "b1-horthykorszak-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-horthykorszak-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 22 (b1-horthykorszak)!")

if __name__ == "__main__":
    build_unit_22_citizenship()
