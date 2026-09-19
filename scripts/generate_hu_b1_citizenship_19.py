#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 19: Austria-Hungary & the Belle Époque (b1-monarchia)."""

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

def build_unit_19_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.monarchia.01",
        "lesson": "b1-monarchia-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "dualista államrendszer", "translation": "dual state system (two states, one monarch)", "pos": "noun"},
            {"lemma": "közös hadsereg", "translation": "common army (k.u.k. joint imperial-royal army)", "pos": "noun"},
            {"lemma": "külpolitika", "translation": "foreign policy and international relations", "pos": "noun"},
            {"lemma": "közös minisztériumok", "translation": "joint ministries (war, foreign affairs, finance)", "pos": "noun"},
            {"lemma": "delegációk", "translation": "parliamentary delegations (60-60 representatives)", "pos": "noun"},
            {"lemma": "Osztrák-Magyar Bank", "translation": "Austro-Hungarian Bank (shared central bank)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-monarchia-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.monarchia.02",
        "lesson": "b1-monarchia-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "millenniumi ünnepségek", "translation": "Millennium celebrations of 1896", "pos": "noun"},
            {"lemma": "honfoglalás emlékezete", "translation": "commemoration of the 896 Hungarian Conquest", "pos": "noun"},
            {"lemma": "Hősök tere", "translation": "Heroes' Square (monumental millennial plaza)", "pos": "noun"},
            {"lemma": "Millenniumi Földalatti", "translation": "Millennium Underground Railway (continental Europe's first)", "pos": "noun"},
            {"lemma": "Vajdahunyad vára", "translation": "Vajdahunyad Castle in the City Park", "pos": "noun"},
            {"lemma": "Iparcsarnok", "translation": "Industrial Exhibition Hall in the City Park", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-monarchia-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.monarchia.03",
        "lesson": "b1-monarchia-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "metropolisz", "translation": "world metropolis (Budapest's rapid rise)", "pos": "noun"},
            {"lemma": "Nagykörút", "translation": "Grand Boulevard of Budapest", "pos": "noun"},
            {"lemma": "Országház építése", "translation": "construction of the Parliament building (Steindl Imre)", "pos": "noun"},
            {"lemma": "kávéházi kultúra", "translation": "urban coffeehouse culture (New York, Pilvax, Gerbeaud)", "pos": "noun"},
            {"lemma": "polgárosodás", "translation": "bourgeois development, civic modernization", "pos": "noun"},
            {"lemma": "Dunaparti korzó", "translation": "Danube promenade in Pest", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-monarchia-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.monarchia.04",
        "lesson": "b1-monarchia-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "malomipar", "translation": "milling industry (Budapest as world grain capital)", "pos": "noun"},
            {"lemma": "Ganz gyár", "translation": "Ganz engineering works (turbines, locomotives, electrical engines)", "pos": "noun"},
            {"lemma": "vasúti hálózat", "translation": "dense national railway network", "pos": "noun"},
            {"lemma": "gabonaexport", "translation": "grain and flour export to European markets", "pos": "noun"},
            {"lemma": "folyószabályozás", "translation": "river regulation (Tisza flood control, Danube navigable paths)", "pos": "noun"},
            {"lemma": "technikai újítás", "translation": "technical innovation and patent engineering", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-monarchia-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.monarchia.05",
        "lesson": "b1-monarchia-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "boldog békeidők", "translation": "'Happy Peacetime' (the Belle Époque era, 1867–1914)", "pos": "noun"},
            {"lemma": "nemzetiségi kérdés", "translation": "nationalities question (ethnic minorities in Hungary)", "pos": "noun"},
            {"lemma": "társadalmi feszültség", "translation": "social tension and agrarian hardship", "pos": "noun"},
            {"lemma": "kivándorlás", "translation": "emigration waves across the Atlantic to America", "pos": "noun"},
            {"lemma": "századforduló", "translation": "turn of the 20th century (fin de siècle)", "pos": "noun"},
            {"lemma": "történelmi örökség", "translation": "historical legacy and architecture of the Dual Monarchy", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-monarchia-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.monarchia.01.dual-statehood",
        "title": "Dual Structures: mindkét állam, egyrészt... másrészt...",
        "sections": [
            {
                "type": "text",
                "title": "Describing Complex Power Sharing",
                "content": "To explain the dual power balance between Vienna and Budapest: *egyrészt... másrészt...* ('on the one hand... on the other hand...'), *mindkét fél számára* ('for both parties'): *A dualista államrendszer egyrészt megőrizte a magyar önállóságot, másrészt biztosította a birodalom nagyhatalmi erejét.*"
            },
            {
                "type": "examples",
                "title": "Dual statehood syntax",
                "items": [
                    {
                        "spanish": "A közös minisztériumok mindkét parlamentnek elszámolással tartoztak.",
                        "english": "The joint ministries were accountable to both parliaments."
                    },
                    {
                        "spanish": "A közös hadsereg felett az uralkodó gyakorolta a legfőbb parancsnoki jogot.",
                        "english": "Over the common army, the monarch exercised supreme command."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-monarchia-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.monarchia.02.celebratory-commemorative",
        "title": "Commemorative & Monumental Discourse: emlékére, tiszteletére",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Dedication and Memorials",
                "content": "Postpositions *emlékére* ('in memory of') and *tiszteletére* ('in honor of') take a noun in the nominative/possessive: *A honfoglalás ezeréves évfordulójának emlékére épült a Hősök tere.* ('Heroes' Square was built in memory of the thousand-year anniversary of the Conquest.')."
            },
            {
                "type": "examples",
                "title": "Monumental formulas",
                "items": [
                    {
                        "spanish": "A millenniumi ünnepségek alkalmából adták át a kontinens első földalatti vasútját.",
                        "english": "On the occasion of the Millennium celebrations, the continent's first underground railway was inaugurated."
                    },
                    {
                        "spanish": "A magyar nemzet tiszteletére grandiózus kiállítást rendeztek a Városligetben.",
                        "english": "In honor of the Hungarian nation, a grandiose exhibition was organized in the City Park."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-monarchia-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.monarchia.03.urban-transformation",
        "title": "Urban Development Verbs: kiépül, átalakul, létrejön",
        "sections": [
            {
                "type": "text",
                "title": "Verbs with Prefixes of Completion in Urban History",
                "content": "Prefixes *ki-*, *át-*, and *létre-* denote comprehensive urban transformations: *kiépül a sugárút* (the avenue is fully built out), *világvárossá alakul át a főváros* (the capital transforms into a world metropolis), *létrejön az egységes Budapest* (unified Budapest comes into existence)."
            },
            {
                "type": "examples",
                "title": "Urban growth expressions",
                "items": [
                    {
                        "spanish": "Néhány évtized alatt modern metropolisz épült ki a Duna két partján.",
                        "english": "Within a few decades, a modern metropolis was built out on both banks of the Danube."
                    },
                    {
                        "spanish": "A kávéházakban pezsgő szellemi és irodalmi élet alakult ki.",
                        "english": "A vibrant intellectual and literary life developed in the coffeehouses."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-monarchia-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.monarchia.04.superlatives-scale",
        "title": "Superlatives of Innovation: a legkorszerűbb, világviszonylatban is",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Industrial Preeminence",
                "content": "Describing world-class achievements: *világviszonylatban is a legmodernebb* ('the most modern even in global terms'), *európai szinten kiemelkedő* ('outstanding at the European level'): *A budapesti malomipar világviszonylatban is vezető szerepet töltött be.*"
            },
            {
                "type": "examples",
                "title": "Superlative industrial descriptors",
                "items": [
                    {
                        "spanish": "A Ganz gyár technikai újításai a világ legfejlettebb elektromos gépei közé tartoztak.",
                        "english": "The Ganz factory's technical innovations ranked among the world's most advanced electrical machines."
                    },
                    {
                        "spanish": "A sűrű vasúti hálózat gyors összeköttetést biztosított a kontinens nagyvárosaival.",
                        "english": "The dense railway network provided rapid connections with the continent's great cities."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-monarchia-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.monarchia.05.historical-evaluation",
        "title": "Contrasting Historical Perspective: Miközben..., aközben...",
        "sections": [
            {
                "type": "text",
                "title": "Simultaneous Realities and Historical Tensions",
                "content": "Balancing the splendor and structural flaws of the Dual Monarchy: *Miközben a főváros látványosan gazdagodott, a vidéki szegénység miatt százezrek vándoroltak ki.* ('While the capital was spectacularly growing wealthy, hundreds of thousands emigrated due to rural poverty.')."
            },
            {
                "type": "examples",
                "title": "Dual perspectives on history",
                "items": [
                    {
                        "spanish": "A boldog békeidők korszaka egyszerre volt a kulturális aranykor és a növekvő feszültségek ideje.",
                        "english": "The era of the Happy Peacetime was simultaneously a cultural golden age and a time of growing tensions."
                    },
                    {
                        "spanish": "A dualizmus kora a mai napig meghatározza a magyar városok építészeti és kulturális örökségét.",
                        "english": "The Dualist era continues to this day to define the architectural and cultural heritage of Hungarian cities."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-monarchia-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (Rest is History Style, 5 lessons + combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.monarchia.01",
        "title": "A kétfejű sas és a Szent Korona",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "In Rest is History style, we explore the extraordinary bureaucratic and military machinery of the Austro-Hungarian Empire: two sovereign states under one emperor-king, three joint ministries, and a sprawling multinational army speaking a dozen languages.",
        "characters": [
            "Bécsi miniszter",
            "Pesti képviselő",
            "Közös hadsereg ezredese"
        ],
        "location": "Bécs, Ballhausplatz & Budapest, Sándor-palota",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1867 után a világ térképeire egy különös, 50 milliós óriásbirodalom rajzolódott fel: az Osztrák–Magyar Monarchia. A dualista államrendszer egy valódi politikai bűvészmutatvány volt, ahol a kétfejű sas fejei ugyanazt az aranykoronát viselték, de két külön testet irányítottak."
            },
            {
                "type": "narration",
                "text": "Magyarországnak független parlamentje és önálló kormánya lett Pesten, de három kulcsfontosságú terület közös maradt: a hadügy, a külpolitika és az ezek költségeit fedező közös minisztériumok."
            },
            {
                "type": "dialogue",
                "speaker": "Pesti képviselő",
                "text": "Uraim, a magyar szuverenitást megvédtük! Csak ott működünk együtt Béccsel, ahol a birodalom nagysága elengedhetetlenül megkívánja!"
            },
            {
                "type": "narration",
                "text": "A költségvetésről nem egyetlen közös parlament döntött, hanem a hatvan-hatvan fős delegációk, amelyek felváltva Bécsben és Pesten üléseztek – ráadásul soha nem vitatkoztak egy szobában, csupán írásos jegyzékeket küldtek egymásnak!"
            },
            {
                "type": "narration",
                "text": "A gazdaság vérkeringését a közös valuta, a korona, és a közös jegybank, az Osztrák-Magyar Bank biztosította, miközben a közös hadsereg tizenegy nyelven vezényelt ezredei a császár és a magyar király nevében álltak őrt a határokon."
            },
            {
                "type": "dialogue",
                "speaker": "Közös hadsereg ezredese",
                "text": "Ebben a seregben magyar huszárok, bécsi tüzérek és tiroli vadászok szolgálnak egymás mellett. A korona köti össze a népeket!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia-01-ketsas.json", story_01)

    story_02 = {
        "id": "story.b1.monarchia.02",
        "title": "1896: A birodalom csúcsán – A Millennium",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Budapest throws the party of the century in 1896 to celebrate the 1000th anniversary of the Hungarian Conquest. From the monumental Heroes' Square to Europe's first underground railway, the kingdom demonstrates its pride and dizzying progress to the world.",
        "characters": [
            "Ferenc József király",
            "Ybl Miklós és Steindl Imre építészek",
            "A budapesti polgárok"
        ],
        "location": "Budapest, Városliget és Andrássy út",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1896 tavaszán Budapest úgy ragyogott, mint még soha. A millenniumi ünnepségek alkalmából a nemzet az Árpád vezér általi honfoglalás emlékezete előtt hajtott fejet, mégpedig olyan pompával, ami egész Európát elkápráztatta."
            },
            {
                "type": "narration",
                "text": "A Városliget kapujában felépült a gigantikus Hősök tere a Millenniumi Emlékművel és a magyar történelem legnagyobb királyainak szobraival. A liget közepén tündérmeseként magasodott Alpár Ignác remekműve, a Vajdahunyad vára."
            },
            {
                "type": "dialogue",
                "speaker": "Ferenc József király",
                "text": "Örömmel látom ezeréves Magyarországunk páratlan virágzását és tehetségét. A jövő fényes kapui nyíltak meg ezen a földön!"
            },
            {
                "type": "narration",
                "text": "Az elegáns Andrássy út alatt a világ legkorszerűbb mérnöki csodája zúgott: a Millenniumi Földalatti Vasút, amely a kontinensen elsőként szállította az utasokat villamos hajtással."
            },
            {
                "type": "narration",
                "text": "A ligetben elhelyezkedő monumentális Iparcsarnok csarnokaiban a magyar gépgyártás, borászat és textilipar legkiválóbb termékeit állították ki, bizonyítva, hogy a magyar nemzet a modern világ élvonalába érkezett."
            },
            {
                "type": "dialogue",
                "speaker": "A budapesti polgárok",
                "text": "Ezer év küzdelem után végre felvirradt a magyar dicsőség napja! Nézzétek a palotákat és a sugárutakat: Budapest igazi világváros lett!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia-02-millennium.json", story_02)

    story_03 = {
        "id": "story.b1.monarchia.03",
        "title": "A kávéházak és paloták városa",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How Pest, Buda and Óbuda merged to become one of the fastest-growing world metropolises. The construction of the Parliament, the sweep of the Grand Boulevard, and the rich coffeehouse culture where literature, journalism and romance flourished.",
        "characters": [
            "Krúdy Gyula író",
            "Főpincér a New York kávéházban",
            "Steindl Imre építész"
        ],
        "location": "Budapest, New York Kávéház, Nagykörút, Duna-part",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Alig harminc év alatt a poros Duna-parti mezővárosból lenyűgöző metropolisz született. A századfordulóra Budapest lakossága megközelítette az egymillió főt, növekedési üteme még Chicagóéval is vetekedett."
            },
            {
                "type": "narration",
                "text": "A Duna partján lassan emelkedtek az Országház építése során kifaragott neogótikus tornyok és a hatalmas kupola, miközben a város körül félkörívben fényárban úszott a széles Nagykörút a maga kávéházaival és színházaival."
            },
            {
                "type": "dialogue",
                "speaker": "Steindl Imre",
                "text": "A magyar Országház nem csupán egy épület: a nemzet szívverése és a polgári szabadság kőbe vésett emlékműve a Duna partján!"
            },
            {
                "type": "narration",
                "text": "A pest-budai polgárosodás igazi központjai azonban a kávéházak voltak. A híres kávéházi kultúra falai között költők, hírlapírók és bankárok vitatták meg a nap híreit feketekávé és friss újságok mellett."
            },
            {
                "type": "narration",
                "text": "Délutánonként az elegáns dámák és urak a Dunaparti korzó sétányain mutatták be legújabb párizsi toalettjeiket, a gőzhajók kürtje pedig a nyüzsgő dunai kereskedelem ritmusát diktálta."
            },
            {
                "type": "dialogue",
                "speaker": "Krúdy Gyula író",
                "text": "Pest kávéházaiban mindig szólt a halk hegedűszó, a pincérek ezüst tálcákon hordták az álmot, és a szavaknak nagyobb súlya volt, mint az aranynak."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia-03-vilagvaros.json", story_03)

    story_04 = {
        "id": "story.b1.monarchia.04",
        "title": "A gőzmalmok és vasutak országa",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Behind the glamorous coffeehouses lay industrial might: Budapest was the flour milling capital of the globe, Ganz engineering powered locomotives and European power grids, and an immense railway boom transformed the Hungarian plains into a breadbasket.",
        "characters": [
            "Mechwart András mérnök",
            "Ganz Ábrahám örökösei",
            "Alföldi gabonakereskedő"
        ],
        "location": "Budapest, Ganz gyár & Ferencvárosi malmok",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Kevesen tudják, de a 19. század végén Budapest volt a Föld második legnagyobb malomipari központja Minneapolis után. A hatalmas hengermalmok ontották magukból a legfinomabb fehér búzalisztet, amit egész Nyugat-Európa rajongva vásárolt."
            },
            {
                "type": "narration",
                "text": "A siker kulcsa egy zseniális technikai újítás volt: Mechwart András kéregöntésű hengerszékei forradalmasították az őrlést. A budapesti malomipar és a hatalmas gabonaexport aranyat hozott az országnak."
            },
            {
                "type": "dialogue",
                "speaker": "Mechwart András mérnök",
                "text": "A precíz acél és a fizika törvényei nem ismernek határokat! A Ganz gyár gépei és transzformátorai a világ bármely pontján megállják a helyüket!"
            },
            {
                "type": "narration",
                "text": "A budai Ganz gyár műhelyeiben Kandó Kálmán megalkotta az első modern villanymozdonyokat, míg Zipernowsky, Déri és Bláthy kifejlesztette a modern zárt vasmagú transzformátort, ami nélkül ma nem létezne elektromos hálózat."
            },
            {
                "type": "narration",
                "text": "Eközben a Kárpát-medencében kiépült a sűrű vasúti hálózat, és a hatalmas folyószabályozás révén százezer hektárnyi termékeny szántóföld szabadult fel a Tisza és a Duna áradásai alól."
            },
            {
                "type": "dialogue",
                "speaker": "Alföldi gabonakereskedő",
                "text": "A gőzmozdony reggel felveszi a búzát a dél-alföldi tanyán, este pedig már a pesti gőzmalomban őrlik! Ez a gyorsaság maga a modern kor!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia-04-ipar.json", story_04)

    story_05 = {
        "id": "story.b1.monarchia.05",
        "title": "A boldog békeidők alkonya",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "As the turn of the century arrived, the golden age of the Belle Époque began to reveal profound tensions. Rural poverty drove hundreds of thousands to emigrate to America, ethnic minorities demanded autonomy, and Europe's old order drifted toward the catastrophe of 1914.",
        "characters": [
            "Fiumei kikötőtiszt",
            "Kivándorló magyar parasztlegény",
            "Budapesti újságíró"
        ],
        "location": "Fiume kikötője, Kassa, Budapest",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A nosztalgikus emlékezet úgy hívja ezt a korszakot: boldog békeidők. És valóban, közel ötven éven át nem dörögtek ágyúk a határokon, az életszínvonal növekedett, a kultúra virágzott a századforduló éveiben."
            },
            {
                "type": "narration",
                "text": "Ám a ragyogó felszín alatt komoly mélyreható feszültségek húzódtak. A földbirtokos rendszer miatt a zsellérek és a szegényparasztok élete kilátástalan maradt, és az egyre élesebb társadalmi feszültség robbanással fenyegetett."
            },
            {
                "type": "dialogue",
                "speaker": "Kivándorló magyar parasztlegény",
                "text": "Isten veled, szülőföldem! Nincs itt föld, nincs kenyér a gyerekeimnek. Amerikában, a pittsburghi acélgyárakban próbálok új életet teremteni a családomnak!"
            },
            {
                "type": "narration",
                "text": "Fiume kikötőjéből hétről hétre indultak a nagy óceánjárók New York felé: a tömeges kivándorlás során több mint másfél millió ember hagyta el a történelmi Magyarországot."
            },
            {
                "type": "narration",
                "text": "Ugyanakkor a soknemzetiségű országban a nemzetiségi kérdés megoldatlansága – a szlovákok, románok, délszlávok jogkövetelései – állandó politikai viharokat szított, miközben az európai nagyhatalmak fegyverkezési versenybe kezdtek."
            },
            {
                "type": "dialogue",
                "speaker": "Budapesti újságíró",
                "text": "A Monarchia olyan volt, mint egy gyönyörű kristálycsillár a bálteremben: ragyogott és elvakított, de elég volt egyetlen lökés, hogy darabjaira hulljon."
            },
            {
                "type": "narration",
                "text": "A Monarchia 1918-ban felbomlott, de a korszak épületei, hídjai, szellemi alkotásai és gazdag történelmi öröksége a mai napig elevenen él a magyar városok utcáin."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia-05-bekeidok.json", story_05)

    # Combined story for consolidation
    story_combined = {
        "id": "story.b1.monarchia.combined",
        "title": "Az Osztrák–Magyar Monarchia kora (1867–1914)",
        "level": "B1",
        "order": 19,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive Rest is History narrative tracing the dual monarchy from the power-sharing compromise to the 1896 Millennium mega-celebration, Budapest's golden age of coffeehouses and heavy industry, and the poignant sunset of the Belle Époque.",
        "characters": [
            "Ferenc József uralkodó",
            "Andrássy Gyula és Tisza Kálmán miniszterelnökök",
            "Mechwart András és Steindl Imre alkotók",
            "A korszak magyar népe"
        ],
        "location": "Bécs, Budapest, Fiume, Kárpát-medence",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1867-ben az 1848-as forradalom leverése után közel két évtizeddel a magyar nemzet és a Habsburg-dinasztia történelmi kiegyezést kötött. Létrejött az Osztrák–Magyar Monarchia: egy sokszínű, lenyűgöző birodalom."
            },
            {
                "type": "narration",
                "text": "A dualista államrendszer két független kormányra és három közös területre – külpolitika, közös hadsereg és pénzügy – épült. A közös minisztériumok munkáját az évenként ülésező parlamenti delegációk felügyelték, miközben az Osztrák-Magyar Bank kibocsátotta az aranyfedezetű koronát."
            },
            {
                "type": "narration",
                "text": "1896-ban a millenniumi ünnepségek keretében az ország megünnepelte az ezeréves honfoglalás emlékezete pillanatát. Megszületett a monumentális Hősök tere, a mesés Vajdahunyad vára, és megindult a kontinens első villamos földalattija, a Millenniumi Földalatti."
            },
            {
                "type": "narration",
                "text": "Budapest villámgyorsan világméretű metropolisz lett. A Duna partján felépült a monumentális Országház, a Nagykörút mentén pezsgett a polgárosodás, a kávéházi kultúra pedig a modern irodalom bölcsőjévé vált."
            },
            {
                "type": "narration",
                "text": "A gazdaságban a Mechwart-féle hengerszékeknek köszönhetően a budapesti malomipar és a gabonaexport a világranglista élére tört. A Ganz gyár elektrotechnikai csodái, a sűrű vasúti hálózat és a kiterjedt folyószabályozás átformálta az egész Kárpát-medencét."
            },
            {
                "type": "narration",
                "text": "Bár a boldog békeidők csillogása máig elbűvöli az utókort, a mélyben a nemzetiségi kérdés és a társadalmi feszültség éleződött, ami tömeges tengerentúli kivándorláshoz vezetett a századforduló után."
            },
            {
                "type": "narration",
                "text": "A Monarchia fél évszázados korszaka Magyarország történelmének leglátványosabb modernizációs ugrását jelentette, melynek történelmi öröksége ma is látható Budapest és az ország minden szegletében."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-monarchia.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-monarchia-{padded}",
            "exercises": [
                {
                    "id": f"b1-monarchia-{padded}.ex01",
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
                    "id": f"b1-monarchia-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen az Osztrák–Magyar Monarchia történelmi viszonyait? (Lesson {i})",
                    "options": [
                        "A dualista államrendszer egyrészt önállóságot biztosított, másrészt közös hadsereget tartott fenn.",
                        "A közös minisztériumok mert nem beszélnek soha delegációk egymással.",
                        "Mivel Millennium volt 1896-ban ezért tilos volt vasutat építeni."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-monarchia-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "1896-ban az ezeréves honfoglalás emlékére nagyszabású ____ ünnepségeket tartottak. (Millennium)",
                    "answer": "millenniumi"
                },
                {
                    "id": f"b1-monarchia-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A nemzet nagy királyainak tisztelet____ emelték a szobrokat a Hősök terén. (in honor of -ére/-ére)",
                    "answer": "ére"
                },
                {
                    "id": f"b1-monarchia-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Melyik világelső közlekedési eszköz indult el Budapesten 1896-ban?",
                    "options": [
                        "A kontinens első villamos hajtású földalatti vasútja (Millenniumi Földalatti).",
                        "A világ legelső gőzmeghajtású űrrakétája.",
                        "Egy óriási hőlégballon-flotta menetrend szerinti járata."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-monarchia-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Néhány évtized alatt virágzó világvárossá alakult ____ Budapest. (transformed into - verbal prefix át-)",
                    "answer": "át"
                },
                {
                    "id": f"b1-monarchia-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "budapesti", "kávéházi", "kultúra", "és", "a", "polgárosodás", "meghatározta", "a", "boldog", "békeidők", "hangulatát."],
                    "solution": ["A", "budapesti", "kávéházi", "kultúra", "és", "a", "polgárosodás", "meghatározta", "a", "boldog", "békeidők", "hangulatát."]
                },
                {
                    "id": f"b1-monarchia-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik magyar gyár mérnökei fejlesztették ki a modern zárt vasmagú transzformátort?",
                    "options": [
                        "A Ganz gyár kiváló mérnökei (Zipernowsky, Déri és Bláthy).",
                        "Egy bécsi sörfőzde szerelői.",
                        "Egy angol pamutszövő manufaktúra munkásai."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-monarchia-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-monarchia-consolidation",
        "exercises": [
            {
                "id": "b1-monarchia-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["dualista államrendszer", "dual state system"],
                    ["millenniumi ünnepségek", "Millennium celebrations"],
                    ["boldog békeidők", "'Happy Peacetime'"],
                    ["Ganz gyár", "Ganz engineering works"]
                ]
            },
            {
                "id": "b1-monarchia-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás jellemzi a leghitelesebben a Monarchia korszakának mérlegét?",
                "options": [
                    "Páratlan gazdasági és kulturális fejlődést hozott, miközben mély nemzetiségi és társadalmi feszültségek maradtak fenn.",
                    "Teljes gazdasági elszigetelődést és a városok elnéptelenedését eredményezte.",
                    "Magyarország azonnal beolvadt Ausztria tartományai közé önállóság nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-monarchia-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Duna partján felépült Steindl Imre tervei alapján a magyar ____ épülete. (Parliament - Országház)",
                "answer": "Országház"
            },
            {
                "id": "b1-monarchia-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Kárpát-medence szántóföldjeit a folyószabályozás révén mentették ____ az árvizektől. (rescued/saved - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-monarchia-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "századforduló", "építészeti", "és", "kulturális", "öröksége", "máig", "meghatározza", "a", "magyar", "nemzet", "önképét."],
                "solution": ["A", "századforduló", "építészeti", "és", "kulturális", "öröksége", "máig", "meghatározza", "a", "magyar", "nemzet", "önképét."]
            },
            {
                "id": "b1-monarchia-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'boldog békeidők' történelmi kifejezés?",
                "options": [
                    "Az 1867 és 1914 közötti virágzó, viszonylag békés időszakot a Monarchiában.",
                    "A középkori tatárjárás utáni éveket.",
                    "A második világháborút követő újjáépítés első három napját."
                ],
                "correct": 0
            },
            {
                "id": "b1-monarchia-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szegénység elől a századfordulón több mint egymillió ember döntött az Amerikába való ____ mellett. (emigration)",
                "answer": "kivándorlás"
            },
            {
                "id": "b1-monarchia-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik téren található az ezeréves honfoglalás tiszteletére emelt monumentális emlékmű Budapesten?",
                "options": [
                    "A Hősök terén a Városliget bejáratánál.",
                    "A Déli pályaudvar előtt egy kis parkban.",
                    "A Gellért-hegy legtetején lévő barlangban."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-monarchia-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("A kétfejű sas és a Szent Korona", "The Double-Headed Eagle & the Crown"),
        "02": ("A Millennium éve (1896)", "The Millennium Year 1896"),
        "03": ("Budapest világvárossá válik", "Budapest Becomes a World Metropolis"),
        "04": ("Gyárak, gőzmalmok és vasutak", "Mills, Iron & Rails"),
        "05": ("A boldog békeidők és a századforduló", "The Belle Époque & Its Shadows")
    }

    story_refs = {
        "01": "stories/world/b1/b1-monarchia-01-ketsas.json",
        "02": "stories/world/b1/b1-monarchia-02-millennium.json",
        "03": "stories/world/b1/b1-monarchia-03-vilagvaros.json",
        "04": "stories/world/b1/b1-monarchia-04-ipar.json",
        "05": "stories/world/b1/b1-monarchia-05-bekeidok.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.monarchia-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Dual State Structures, Commemorative Postpositions & Urban Innovation Verbs",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events, institutions and societal changes of {en_t}.",
                        "I can use commemorative formulas and urban transformation verbs in Hungarian.",
                        "I can answer citizenship interview questions about Austria-Hungary and the Millennium.",
                        "I can master six new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-monarchia-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-monarchia-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-monarchia-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-monarchia-{padded}.ex01",
                        f"b1-monarchia-{padded}.ex02",
                        f"b1-monarchia-{padded}.ex03",
                        f"b1-monarchia-{padded}.ex04",
                        f"b1-monarchia-{padded}.ex05",
                        f"b1-monarchia-{padded}.ex06",
                        f"b1-monarchia-{padded}.ex07",
                        f"b1-monarchia-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-monarchia-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.monarchia-consolidation",
        "title": "Összefoglalás: Az Osztrák–Magyar Monarchia (Austria-Hungary Consolidation)",
        "level": "B1",
        "grammar": "Consolidation of the Austro-Hungarian Dual Monarchy & the Belle Époque",
        "sections": [
            {
                "type": "story",
                "ref": "stories/world/b1/b1-monarchia.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-monarchia-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-monarchia-consolidation.ex01",
                    "b1-monarchia-consolidation.ex02",
                    "b1-monarchia-consolidation.ex03",
                    "b1-monarchia-consolidation.ex04",
                    "b1-monarchia-consolidation.ex05",
                    "b1-monarchia-consolidation.ex06",
                    "b1-monarchia-consolidation.ex07",
                    "b1-monarchia-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-monarchia-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 19 (b1-monarchia)!")

if __name__ == "__main__":
    build_unit_19_citizenship()
