#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 35: Hungarians Across the World & International Relations (b1-magyarsag)."""

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

def build_unit_35_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.magyarsag.01",
        "lesson": "b1-magyarsag-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "határon túli magyarság", "translation": "cross-border Hungarians, Hungarian communities outside Hungary", "pos": "noun"},
            {"lemma": "Kárpát-medence", "translation": "Carpathian Basin (historic homeland of the Hungarian nation)", "pos": "noun"},
            {"lemma": "nemzetpolitika", "translation": "national policy, kin-state policy supporting Hungarian minorities", "pos": "noun"},
            {"lemma": "anyanemzet", "translation": "mother nation, kin state (Hungary)", "pos": "noun"},
            {"lemma": "kisebbségi jogok", "translation": "minority rights (cultural, linguistic, and educational entitlements)", "pos": "noun"},
            {"lemma": "anyanyelvhasználat", "translation": "use of the mother tongue (native language rights in education and public life)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-magyarsag-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.magyarsag.02",
        "lesson": "b1-magyarsag-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "történelmi közösség", "translation": "historic community, autochthonous native community", "pos": "noun"},
            {"lemma": "Erdély", "translation": "Transylvania (historic region in modern Romania with large Hungarian population)", "pos": "noun"},
            {"lemma": "Felvidék", "translation": "Upper Hungary (historic region in modern Slovakia)", "pos": "noun"},
            {"lemma": "Vajdaság", "translation": "Vojvodina (historic region in modern Serbia)", "pos": "noun"},
            {"lemma": "Kárpátalja", "translation": "Transcarpathia (historic region in modern western Ukraine)", "pos": "noun"},
            {"lemma": "kulturális autonómia", "translation": "cultural autonomy, self-determination in educational and linguistic matters", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-magyarsag-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.magyarsag.03",
        "lesson": "b1-magyarsag-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "diaszpóra", "translation": "diaspora (Hungarians living across Western Europe, the Americas, and Australia)", "pos": "noun"},
            {"lemma": "kivándorlás", "translation": "emigration, moving abroad", "pos": "noun"},
            {"lemma": "magyar ház", "translation": "Hungarian community center abroad", "pos": "noun"},
            {"lemma": "hétvégi iskola", "translation": "weekend heritage school (teaching Hungarian language and history abroad)", "pos": "noun"},
            {"lemma": "hagyományápolás", "translation": "nurturing traditions, cultural preservation", "pos": "noun"},
            {"lemma": "összetartozás", "translation": "togetherness, belonging together across borders", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-magyarsag-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.magyarsag.04",
        "lesson": "b1-magyarsag-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Visegrádi Négyek", "translation": "Visegrád Four / V4 (alliance of Hungary, Poland, Czechia, and Slovakia)", "pos": "noun"},
            {"lemma": "közép-európai együttműködés", "translation": "Central European regional cooperation", "pos": "noun"},
            {"lemma": "Európai Unió", "translation": "European Union (joined by Hungary on May 1, 2004)", "pos": "noun"},
            {"lemma": "schengeni övezet", "translation": "Schengen area (passport-free European travel zone)", "pos": "noun"},
            {"lemma": "határmenti kapcsolat", "translation": "cross-border regional relations and infrastructure", "pos": "noun"},
            {"lemma": "érdekképviselet", "translation": "advocacy of interests, diplomatic representation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-magyarsag-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.magyarsag.05",
        "lesson": "b1-magyarsag-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "egyszerűsített honosítás", "translation": "simplified naturalization (preferential citizenship based on Hungarian ancestry)", "pos": "noun"},
            {"lemma": "Nemzeti Összetartozás Napja", "translation": "Day of National Togetherness (June 4, commemorating Trianon in solidarity)", "pos": "noun"},
            {"lemma": "Rákóczi Szövetség", "translation": "Rákóczi Association (civil organization connecting youth across the Carpathian Basin)", "pos": "noun"},
            {"lemma": "Kőrösi Csoma Sándor Program", "translation": "Kőrösi Csoma Sándor Program (internship supporting diaspora communities)", "pos": "noun"},
            {"lemma": "diplomáciai védelem", "translation": "diplomatic and consular protection granted to all citizens abroad", "pos": "noun"},
            {"lemma": "konzuli szolgálat", "translation": "consular service of Hungary", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-magyarsag-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.magyarsag.01.transnational-responsibility",
        "title": "Constitutional Responsibility Valencies: Felelősséget visel & Támogatja",
        "sections": [
            {
                "type": "text",
                "title": "Article D of the Fundamental Law",
                "content": "The Hungarian Fundamental Law codifies the kin-state principle: *Magyarország felelősséget visel a határain kívül élő magyarok sorsáért* (Hungary bears responsibility for the fate of Hungarians living beyond its borders). The verbal expression *felelősséget visel vmiért* takes the causal-final case (*-ért*)."
            },
            {
                "type": "examples",
                "title": "Responsibility valency examples",
                "items": [
                    {"spanish": "Magyarország felelősséget visel a határon túli magyar közösségek sorsáért.", "english": "Hungary bears responsibility for the fate of cross-border Hungarian communities."},
                    {"spanish": "Az állam támogatja a határon túli magyarság anyanyelvi kultúrájának megőrzését.", "english": "The state supports the preservation of cross-border Hungarians' native language culture."},
                    {"spanish": "A törvény garantálja a nemzeti összetartozás intézményes védelmét.", "english": "The law guarantees institutional protection for national togetherness."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-magyarsag-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.magyarsag.02.regional-locatives",
        "title": "Historic Regional Locatives: Erdélyben, Felvidéken, Kárpátalján",
        "sections": [
            {
                "type": "text",
                "title": "Locative Suffix Harmony for Historical Regions",
                "content": "Designating geographic regions in the Carpathian Basin requires specific locative suffixes: *Erdélyben* (-ban/-ben, inessive), *a Vajdaságban* (-ban/-ben), but *a Felvidéken* (-on/-en/-ön, superessive), *Kárpátalján* (-on/-en/-ön), and *az Őrvidéken / Burgenlandban*."
            },
            {
                "type": "examples",
                "title": "Regional locative examples",
                "items": [
                    {"spanish": "Jelentős magyar közösség él Erdélyben és a Partiumban.", "english": "A significant Hungarian community lives in Transylvania and the Partium."},
                    {"spanish": "A Felvidéken sok településen magyar tannyelvű iskolák működnek.", "english": "In Upper Hungary, Hungarian-language schools operate in many settlements."},
                    {"spanish": "Kárpátalján a nehéz körülmények ellenére kitartanak a magyar családok.", "english": "In Transcarpathia, Hungarian families persevere despite challenging circumstances."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-magyarsag-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.magyarsag.03.diaspora-preservation",
        "title": "Diaspora Preservation Syntax: Ápolja a kapcsolatot & Megőrzi az identitást",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Collocations of Cultural Heritage",
                "content": "To describe the activities of diaspora communities, Hungarian pairs transitive verbs of preservation with abstract cultural objects: *ápolja a kapcsolatot* (nurtures ties), *megőrzi a nyelvet / hagyományt* (preserves the language / tradition), *erősíti a kötődést* (strengthens attachment)."
            },
            {
                "type": "examples",
                "title": "Diaspora preservation examples",
                "items": [
                    {"spanish": "A nyugati diaszpórában élő magyarok hűen ápolják a nemzeti hagyományokat.", "english": "Hungarians living in the western diaspora faithfully nurture national traditions."},
                    {"spanish": "A hétvégi magyar iskolák segítik a gyermekek anyanyelvi fejlődését.", "english": "Weekend Hungarian schools assist children's native language development."},
                    {"spanish": "A diaszpóra közösségei szoros kapcsolatot tartanak fenn az anyaországgal.", "english": "Diaspora communities maintain close ties with the mother country."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-magyarsag-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.magyarsag.04.diplomatic-coordination",
        "title": "Regional Cooperation Formulas: Együttműködik, álláspontot egyeztet",
        "sections": [
            {
                "type": "text",
                "title": "Diplomatic & European Registers",
                "content": "When discussing the Visegrád Four (V4) and European integration, formal Hungarian uses reciprocal and collaborative verbal structures: *együttműködik vmivel* (cooperates with), *álláspontot egyeztet* (coordinates positions), *érdeket képvisel* (represents interests)."
            },
            {
                "type": "examples",
                "title": "Diplomatic coordination examples",
                "items": [
                    {"spanish": "A Visegrádi Négyek szorosan együttműködnek a gazdaság és a biztonság területén.", "english": "The Visegrád Four closely cooperate in the areas of economy and security."},
                    {"spanish": "A közép-európai partnerek rendszeresen egyeztetik álláspontjukat az Európai Unióban.", "english": "Central European partners regularly coordinate their positions in the European Union."},
                    {"spanish": "A schengeni övezet biztosítja a határok szabad átjárhatóságát a régióban.", "english": "The Schengen zone ensures free border crossing in the region."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-magyarsag-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.magyarsag.05.civic-kinship",
        "title": "Preferential Naturalization & Kinship: Honosításban részesül, igazolja a származást",
        "sections": [
            {
                "type": "text",
                "title": "Legal Framework of Naturalization",
                "content": "To explain the acquisition of citizenship by descent, Hungarian uses legal administrative verbs: *kedvezményes honosításban részesül* (is granted simplified naturalization), *igazolja a magyar származást* (proves Hungarian ancestry), and *állampolgársági esküt tesz* (takes the citizenship oath)."
            },
            {
                "type": "examples",
                "title": "Civic kinship examples",
                "items": [
                    {"spanish": "A határon túli magyarok egyszerűsített honosítási eljárásban kérhetik az állampolgárságot.", "english": "Cross-border Hungarians can apply for citizenship in a simplified naturalization procedure."},
                    {"spanish": "A kérelmezőnek igazolnia kell magyar származását és nyelvtudását.", "english": "The applicant must certify their Hungarian ancestry and language proficiency."},
                    {"spanish": "A sikeres eljárás után az új állampolgár ünnepélyes esküt tesz a magyar zászló előtt.", "english": "Following the successful procedure, the new citizen takes a solemn oath before the Hungarian flag."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-magyarsag-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized World Stories (5 segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.magyarsag.01",
        "title": "A nemzet határok nélkül: A Kárpát-medence magyarsága",
        "level": "B1",
        "lesson": 1,
        "order": 35,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The historical and emotional unity of the Hungarian nation beyond state borders. Exploring Article D of the Fundamental Law and the historic reality of cross-border Hungarian communities in neighboring countries.",
        "characters": [],
        "location": "Kárpát-medence",
        "grammar": ["Constitutional Responsibility Valencies: Felelősséget visel & Támogatja"],
        "vocabularyTopics": ["cross_border", "constitution", "national_policy"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar történelem viharai és a 20. századi határmódosítások következtében a magyar nemzet egy jelentős része ma Magyarország államhatárain kívül, a szomszédos országok területén él."
            },
            {
                "type": "narration",
                "text": "Ezek a közösségek nem emigránsok: ők nem hagyták el szülőföldjüket, hanem a határok mozdultak el a fejük felett. Évszázadok óta őrzik őseik nyelvét, hitét, kultúráját és szokásait a szülőföldjükön."
            },
            {
                "type": "narration",
                "text": "Magyarország Alaptörvényének D) cikke világosan rögzíti ezt a történelmi köteléket: „Magyarország az egységes magyar nemzet eszméjétől vezérelve felelősséget visel a határain kívül élő magyarok sorsáért”."
            },
            {
                "type": "narration",
                "text": "A magyar állam nemzetpolitikájának középpontjában a szülőföldön való megmaradás és boldogulás áll. Ez magában foglalja az anyanyelvű oktatás, a kulturális intézmények és a gazdasági fejlesztések támogatását."
            },
            {
                "type": "narration",
                "text": "A határon túli magyarság nemcsak a múlt öröksége, hanem az egyetemes magyar nemzet élő és elválaszthatatlan része, amely gazdagítja az egész Kárpát-medence kultúráját."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag-01-hatarontul.json", story_01)

    story_02 = {
        "id": "story.b1.magyarsag.02",
        "title": "Történelmi régiók: Erdély, Felvidék, Vajdaság és Kárpátalja",
        "level": "B1",
        "lesson": 2,
        "order": 35,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "A journey across the historic regions of the Carpathian Basin: the vibrant Székelyföld in Transylvania, Csallóköz in Upper Hungary, the plains of Vojvodina, and the courageous communities of Transcarpathia.",
        "characters": [],
        "location": "Kolozsvár, Dunaszerdahely, Szabadka és Beregszász",
        "grammar": ["Historic Regional Locatives: Erdélyben, Felvidéken, Kárpátalján"],
        "vocabularyTopics": ["regions", "autonomy", "cultural_life"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Kárpát-medence történelmi régiói sajátos színnel gazdagítják a magyar kultúrát. A legnagyobb lélekszámú közösség Erdélyben és a Partiumban él, Románia területén, több mint egymillió emberrel."
            },
            {
                "type": "narration",
                "text": "A Székelyföld – Csík, Háromszék, Udvarhely és Marosszék – szívében a magyar lakosság többséget alkot. Városaikban, mint Csíkszeredában vagy Kolozsvárott, pezsgő magyar szellemi élet és egyetemi oktatás működik."
            },
            {
                "type": "narration",
                "text": "Északon, a Felvidéken – a mai Szlovákia déli sávjában – a Csallóköz és a Bodrogköz magyarjai őrzik anyanyelvüket. Komáromban a Selye János Egyetem biztosítja a teljes körű magyar nyelvű felsőoktatást."
            },
            {
                "type": "narration",
                "text": "Délen, a Vajdaságban – Szerbiában – a magyar közösség Szabadka és Zenta környékén él. Itt a kulturális autonómia és a többnyelvű feliratok a mindennapi élet természetes részét képezik."
            },
            {
                "type": "narration",
                "text": "Kárpátalján, a mai Ukrajna területén a beregszászi és ungi magyarok példamutató hűséggel tartanak ki szülőföldjükön a nehéz történelmi próbatételek és háborús megpróbáltatások közepette is."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag-02-regiok.json", story_02)

    story_03 = {
        "id": "story.b1.magyarsag.03",
        "title": "A magyar diaszpóra a világban: Nyugattól a tengerentúlig",
        "level": "B1",
        "lesson": 3,
        "order": 35,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Exploring the Hungarian diaspora around the globe: heritage communities in North America, Western Europe, and Australia, preserved through Hungarian clubs, scout troops, and weekend heritage schools.",
        "characters": [],
        "location": "Bécs, Cleveland, Toronto és Sydney",
        "grammar": ["Diaspora Preservation Syntax: Ápolja a kapcsolatot & Megőrzi az identitást"],
        "vocabularyTopics": ["diaspora", "emigration", "scouting"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A szomszédos országok őshonos magyar közösségei mellett több százezer magyar él a világ távolabbi országaiban: Nyugat-Európában, Észak- és Dél-Amerikában, valamint Ausztráliában."
            },
            {
                "type": "narration",
                "text": "A kivándorlás több hullámban zajlott: a 19. század végi gazdasági kivándorlást követte az 1945 utáni politikai menekültek sora, majd az 1956-os forradalom leverése után közel kétszázezer magyar hagyta el a hazát."
            },
            {
                "type": "narration",
                "text": "A tengerentúlon olyan városokban alakultak ki erős magyar központok, mint az amerikai Cleveland, a kanadai Toronto vagy az ausztráliai Melbourne. Itt templomok, Magyar Házak és cserkészcsapatok jöttek létre."
            },
            {
                "type": "narration",
                "text": "A diaszpórában a hétvégi magyar iskolák és néptáncegyüttesek játszanak kulcsszerepet abban, hogy a harmad- és negyedízigleni fiatalok is megtanulják őseik nyelvét és büszkék legyenek magyar gyökereikre."
            },
            {
                "type": "narration",
                "text": "A modern kommunikáció és a kulturális programok révén a világban élő magyarság ma szorosabb kapcsolatot ápol az anyaországgal, mint bármikor korábban a történelemben."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag-03-diaszpora.json", story_03)

    story_04 = {
        "id": "story.b1.magyarsag.04",
        "title": "Közép-európai szövetség: A Visegrádi Négyek és az Európai Unió",
        "level": "B1",
        "lesson": 4,
        "order": 35,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Hungary's role in the international community: the historic Visegrád alliance with Poland, Czechia, and Slovakia, and participation in the European Union's internal market and Schengen borders.",
        "characters": [],
        "location": "Visegrád és Brüsszel",
        "grammar": ["Regional Cooperation Formulas: Együttműködik, álláspontot egyeztet"],
        "vocabularyTopics": ["v4", "european_union", "diplomacy"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Magyarország külpolitikájának egyik legfontosabb sarokköve a közép-európai térség stabilitása és a szomszédos népekkel való szoros, kölcsönös tiszteleten alapuló együttműködés."
            },
            {
                "type": "narration",
                "text": "A Visegrádi Csoport – a V4 – a Károly Róbert magyar király által 1335-ben összehívott történelmi királytalálkozó hagyományát folytatja. Magyarország, Lengyelország, Csehország és Szlovákia közösen képviselik a térség stratégiai érdekeit."
            },
            {
                "type": "narration",
                "text": "A négy ország nemcsak gazdaságilag van ezer szálon összekötve, hanem közös történelmi sorsuk – a kommunizmus alóli felszabadulás és az euroatlanti integráció – is mély szolidaritást teremt közöttük."
            },
            {
                "type": "narration",
                "text": "2004. május elsején Magyarország a térség államaival együtt az Európai Unió teljes jogú tagjává vált. Az uniós tagság megnyitotta a határokat, biztosította az áruk és a személyek szabad mozgását."
            },
            {
                "type": "narration",
                "text": "A schengeni övezetbe való belépés révén a történelmi határok átjárhatóvá váltak, ami újra összekapcsolta a Kárpát-medencében élő magyar közösségeket, megszüntetve az évtizedes fizikai elszigeteltséget."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag-04-eu.json", story_04)

    story_05 = {
        "id": "story.b1.magyarsag.05",
        "title": "A nemzetpolitika intézményei és a honosítás",
        "level": "B1",
        "lesson": 5,
        "order": 35,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The practical and legal bonds uniting the nation: the simplified naturalization law enacted in 2010, the June 4 Day of National Togetherness, and youth programs led by the Rákóczi Association and Kőrösi Csoma Program.",
        "characters": [],
        "location": "Budapest, Országház",
        "grammar": ["Preferential Naturalization & Kinship: Honosításban részesül, igazolja a származást"],
        "vocabularyTopics": ["citizenship", "naturalization", "solidarity"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "2010-ben a magyar Országgyűlés döntő lépést tett a nemzeti egység jogi megerősítésére: szinte egyhangúlag megszavazta az egyszerűsített honosítási eljárást."
            },
            {
                "type": "narration",
                "text": "Ennek értelmében minden olyan személy, akinek felmenője magyar állampolgár volt, és aki igazolja magyar nyelvtudását, kérelmezheti a magyar állampolgárságot anélkül, hogy Magyarországra kellene költöznie."
            },
            {
                "type": "narration",
                "text": "Az elmúlt másfél évtizedben több mint 1,1 millió határon túli és diaszpórában élő magyar kapta meg a magyar állampolgárságot és tette le a megható állampolgársági esküt, újra jogilag is a nemzet részévé válva."
            },
            {
                "type": "narration",
                "text": "A törvényhozás június 4-ét, a trianoni békeszerződés évfordulóját a Nemzeti Összetartozás Napjává nyilvánította, a gyász helyett az összetartozás életerejét állítva a figyelem középpontjába."
            },
            {
                "type": "narration",
                "text": "Olyan programok, mint a Rákóczi Szövetség diákutaztatásai és a Kőrösi Csoma Sándor Program ösztöndíjasai naponta építik a hidakat az anyaország és a világ magyarsága között, biztosítva a nemzet jövőjét."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag-05-honositas.json", story_05)

    story_combined = {
        "id": "story.b1.magyarsag",
        "title": "Magyarság a világban és nemzetközi kapcsolatok",
        "level": "B1",
        "order": 35,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive compendium on the Hungarian nation across borders: historical roots in the Carpathian Basin, global diaspora communities, Central European V4 alliance, and constitutional responsibility through simplified naturalization.",
        "characters": [],
        "location": "Kárpát-medence és a világ",
        "grammar": [
            "Constitutional Responsibility Valencies: Felelősséget visel & Támogatja",
            "Historic Regional Locatives: Erdélyben, Felvidéken, Kárpátalján",
            "Diaspora Preservation Syntax: Ápolja a kapcsolatot & Megőrzi az identitást",
            "Regional Cooperation Formulas: Együttműködik, álláspontot egyeztet",
            "Preferential Naturalization & Kinship: Honosításban részesül, igazolja a származást"
        ],
        "vocabularyTopics": [
            "cross_border",
            "diaspora",
            "regions",
            "v4",
            "naturalization"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar nemzet fogalma és valósága jóval tágabb, mint Magyarország jelenlegi államhatárai. A határon túli közösségek és a világban élő diaszpóra tagjai évszázadok óta hordozzák magukban a magyar kultúra értékeit."
            },
            {
                "type": "narration",
                "text": "Az Alaptörvény kimondja, hogy Magyarország felelősséget visel minden magyarért, éljen Erdély hegyei között, a Felvidék síkjain, a Vajdaságban vagy Kárpátalja megpróbáltatásokkal küzdő falvaiban."
            },
            {
                "type": "narration",
                "text": "A tengerentúli diaszpóra tagjai Amerikától Ausztráliáig Magyar Házakban, cserkészcsapatokban és hétvégi iskolákban adják át a nyelvet az új generációknak, ápolva az elszakíthatatlan lelki kötődést."
            },
            {
                "type": "narration",
                "text": "A nemzetközi színtéren Magyarország a Visegrádi Négyekkel összefogva védi a közép-európai térség értékeit, míg az Európai Unió és a schengeni rendszer biztosítja a fizikai határok nélküli szabad kapcsolattartást."
            },
            {
                "type": "narration",
                "text": "A 2010-ben bevezetett egyszerűsített honosítás történelmi igazságtételt jelentett: több mint egymillió határon túli testvérünk kapta vissza magyar állampolgárságát, megerősítve, hogy a nemzet határoktól függetlenül egy és oszthatatlan."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-magyarsag.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-magyarsag-01",
        "exercises": [
            {
                "id": "b1-magyarsag-01.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit mond ki az Alaptörvény D) cikke a határon kívül élő magyarokról?",
                "options": [
                    "Magyarország felelősséget visel a határain kívül élő magyarok sorsáért",
                    "A magyar államnak semmilyen kötelezettsége nincs feléjük",
                    "Mindenkinek kötelező Magyarországra költöznie"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Magyarország felelősséget visel a nemzet tagjai_____ sorsáért. (for members - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-magyarsag-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "állam", "támogatja", "a", "kisebbségi", "jogok", "védelmét."],
                "solution": ["A", "magyar", "állam", "támogatja", "a", "kisebbségi", "jogok", "védelmét."]
            },
            {
                "id": "b1-magyarsag-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kiket nevezünk 'határon túli magyarságnak'?",
                "options": [
                    "A szomszédos országok területén őshonosként élő magyar közösségeket",
                    "A külföldi nyaraláson tartózkodó turistákat",
                    "A külföldi állampolgárokat, akik nem beszélnek magyarul"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A nemzetpolitika célja az anyanyelvhasználat biztosítás_____. (ensuring - a)",
                "answer": "a"
            },
            {
                "id": "b1-magyarsag-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik földrajzi térségben él a magyar történelmi közösségek túlnyomó része?",
                "options": [
                    "A Kárpát-medencében",
                    "A Skandináv-félszigeten",
                    "Az Ibériai-félszigeten"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "anyanyelv", "a", "nemzeti", "megmaradás", "legfőbb", "záloga."],
                "solution": ["Az", "anyanyelv", "a", "nemzeti", "megmaradás", "legfőbb", "záloga."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-magyarsag-02",
        "exercises": [
            {
                "id": "b1-magyarsag-02.ex01",
                "type": "multiple-choice",
                "category": "geography",
                "question": "Melyik szomszédos ország területén található a Székelyföld és Kolozsvár?",
                "options": [
                    "Romániában (Erdélyben)",
                    "Szlovákiában (Felvidéken)",
                    "Szerbiában (Vajdaságban)"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Sok magyar család él a Felvidék_____. (in Upper Hungary - en)",
                "answer": "en"
            },
            {
                "id": "b1-magyarsag-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Erdélyben", "több", "mint", "egymillió", "magyar", "ember", "él."],
                "solution": ["Erdélyben", "több", "mint", "egymillió", "magyar", "ember", "él."]
            },
            {
                "id": "b1-magyarsag-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kulturális autonómia' egy nemzeti kisebbség életében?",
                "options": [
                    "Önálló döntéshozatali jogot az oktatás és a kulturális intézmények területén",
                    "A határok teljes lezárását a szomszédok elől",
                    "Egy különálló pénznem bevezetését"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Vajdaság_____ a magyar nyelv hivatalos használata biztosított. (in Vojvodina - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-magyarsag-02.ex06",
                "type": "multiple-choice",
                "category": "geography",
                "question": "Melyik egyetem nyújt magyar nyelvű felsőoktatást Komáromban?",
                "options": [
                    "Selye János Egyetem",
                    "Babeș–Bolyai Tudományegyetem",
                    "II. Rákóczi Ferenc Főiskola"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Kárpátalján", "a", "közösségek", "hűen", "őrzik", "hagyományaikat."],
                "solution": ["Kárpátalján", "a", "közösségek", "hűen", "őrzik", "hagyományaikat."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-magyarsag-03",
        "exercises": [
            {
                "id": "b1-magyarsag-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit értünk a 'magyar diaszpóra' alatt?",
                "options": [
                    "A Kárpát-medencén kívül, a világ távoli országaiban élő magyarságot",
                    "A budapesti lakosok összességét",
                    "A Dunántúlon élő nemzetiségeket"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A diaszpóra tagjai hűen ápolják a nemzeti kapcsolat_____ az anyaországgal. (ties - okat)",
                "answer": "okat"
            },
            {
                "id": "b1-magyarsag-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hétvégi", "magyar", "iskolák", "segítik", "a", "nyelvtanulást."],
                "solution": ["A", "hétvégi", "magyar", "iskolák", "segítik", "a", "nyelvtanulást."]
            },
            {
                "id": "b1-magyarsag-03.ex04",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik történelmi esemény után menekült közel 200 ezer magyar nyugatra?",
                "options": [
                    "Az 1956-os forradalom leverése után",
                    "Az 1848-as szabadságharc kezdetén",
                    "A millennium évében, 1896-ban"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A cserkészet fontos szerepet játszik a hagyományápolás_____. (in tradition preservation - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-magyarsag-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen intézmények fogják össze a diaszpórában élő magyarok kulturális életét?",
                "options": [
                    "Magyar Házak és egyesületek",
                    "Kizárólag külföldi nagykövetségek",
                    "Kereskedelmi bankfiókok"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "összetartozás", "érzése", "áthidalja", "a", "hatalmas", "távolságokat."],
                "solution": ["Az", "összetartozás", "érzése", "áthidalja", "a", "hatalmas", "távolságokat."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-magyarsag-04",
        "exercises": [
            {
                "id": "b1-magyarsag-04.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mely országok alkotják a Visegrádi Négyek (V4) szövetségét?",
                "options": [
                    "Magyarország, Lengyelország, Csehország és Szlovákia",
                    "Magyarország, Ausztria, Németország és Svájc",
                    "Magyarország, Románia, Szerbia és Horvátország"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A V4-országok szorosan együttműköd_____ a közös érdekek védelmében. (cooperate - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-magyarsag-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["2004-ben", "Magyarország", "belépett", "az", "Európai", "Unióba."],
                "solution": ["2004-ben", "Magyarország", "belépett", "az", "Európai", "Unióba."]
            },
            {
                "id": "b1-magyarsag-04.ex04",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen előnyt jelent a schengeni övezet a Kárpát-medencei lakosok számára?",
                "options": [
                    "A belső határokon nincs állandó határellenőrzés, szabad az átjárás",
                    "Minden országban ingyenes a tömegközlekedés",
                    "Mindenhol kötelező ugyanazt az adót fizetni"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tagállamok rendszeresen egyeztetik álláspontjukat a diplomáciai érdekképviselet_____ során. (advocacy - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-magyarsag-04.ex06",
                "type": "multiple-choice",
                "category": "history",
                "question": "Melyik évszázadban zajlott az első történelmi visegrádi királytalálkozó Károly Róbert vezetésével?",
                "options": [
                    "A 14. században (1335-ben)",
                    "A 19. században (1848-ban)",
                    "A 11. században (1000-ben)"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-04.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "közép-európai", "együttműködés", "erősíti", "a", "térség", "biztonságát."],
                "solution": ["A", "közép-európai", "együttműködés", "erősíti", "a", "térség", "biztonságát."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-magyarsag-05",
        "exercises": [
            {
                "id": "b1-magyarsag-05.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Ki jogosult egyszerűsített honosításra Magyarországon 2010 óta?",
                "options": [
                    "Aki igazolja magyar származását (magyar felmenőjét) és nyelvtudását",
                    "Bárki, aki ingatlant vásárol Magyarországon",
                    "Kizárólag az, aki már 10 éve folyamatosan Budapesten él"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A sikeres eljárás után az új állampolgárok esküt tesz_____ a zászló előtt. (take oath - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-magyarsag-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Június", "negyedike", "a", "Nemzeti", "Összetartozás", "Napja."],
                "solution": ["Június", "negyedike", "a", "Nemzeti", "Összetartozás", "Napja."]
            },
            {
                "id": "b1-magyarsag-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik civil szervezet segíti a Kárpát-medencei magyar diákok utaztatását és kapcsolatait?",
                "options": [
                    "Rákóczi Szövetség",
                    "Magyar Tudományos Akadémia",
                    "Magyar Posta"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A külföldön tartózkodó magyar állampolgárok diplomáciai védelmet élvez_____. (enjoy - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-magyarsag-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen program küld ösztöndíjasokat a diaszpórába a magyar közösségek támogatására?",
                "options": [
                    "Kőrösi Csoma Sándor Program",
                    "Erasmus Program",
                    "Széchenyi Terv"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "konzuli", "szolgálat", "segíti", "az", "állampolgárok", "ügyintézését."],
                "solution": ["A", "konzuli", "szolgálat", "segíti", "az", "állampolgárok", "ügyintézését."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-magyarsag-consolidation",
        "exercises": [
            {
                "id": "b1-magyarsag-consolidation.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hány határon túli és diaszpórában élő magyar kapta vissza állampolgárságát 2010 óta?",
                "options": [
                    "Több mint 1,1 millió ember",
                    "Körülbelül 50 ezer ember",
                    "Több mint 10 millió ember"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A határon túli közösségek szoros kapcsolatot ápol_____ az anyaországgal. (maintain - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-magyarsag-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "V4", "szövetség", "együttműködik", "az", "európai", "színtéren."],
                "solution": ["A", "V4", "szövetség", "együttműködik", "az", "európai", "színtéren."]
            },
            {
                "id": "b1-magyarsag-consolidation.ex04",
                "type": "multiple-choice",
                "category": "geography",
                "question": "Melyik térségben élnek a csángók és a székelyek?",
                "options": [
                    "Erdélyben és Moldvában (Románia)",
                    "A Felvidéken (Szlovákia)",
                    "A Vajdaságban (Szerbia)"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szülőföldön való megmaradás a nemzetpolitika kulcsfontosságú célj_____. (its goal - a)",
                "answer": "a"
            },
            {
                "id": "b1-magyarsag-consolidation.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit ünnepel a magyarság június 4-én, a Nemzeti Összetartozás Napján?",
                "options": [
                    "A nemzet lelki és kulturális egységét a trianoni határok felett",
                    "A parlament tavaszi ülésszakának lezárását",
                    "Az első magyar műhold fellövését"
                ],
                "correct": 0
            },
            {
                "id": "b1-magyarsag-consolidation.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "egységes", "magyar", "nemzet", "eszméje", "összeköt", "bennünket."],
                "solution": ["Az", "egységes", "magyar", "nemzet", "eszméje", "összeköt", "bennünket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-magyarsag-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.magyarsag-01",
        "unit": 35,
        "title": "A nemzet határok nélkül: A Kárpát-medence magyarsága",
        "level": "B1",
        "grammar": "Constitutional Responsibility Valencies: Felelősséget visel & Támogatja",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can understand the concept of the unified Hungarian nation beyond state borders.",
                    "I can use constitutional valency verbs like felelősséget visel and támogatja.",
                    "I can master 6 key terms for kin-state policy, minority rights, and mother tongue usage.",
                    "I can read about Article D of the Fundamental Law."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-magyarsag-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-magyarsag-01-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag-01-hatarontul.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-magyarsag-01-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-01.ex01",
                    "b1-magyarsag-01.ex02",
                    "b1-magyarsag-01.ex03",
                    "b1-magyarsag-01.ex04",
                    "b1-magyarsag-01.ex05",
                    "b1-magyarsag-01.ex06",
                    "b1-magyarsag-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.magyarsag-02",
        "unit": 35,
        "title": "Történelmi régiók: Erdély, Felvidék, Vajdaság és Kárpátalja",
        "level": "B1",
        "grammar": "Historic Regional Locatives: Erdélyben, Felvidéken, Kárpátalján",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can identify the historic regions of the Carpathian Basin and their Hungarian communities.",
                    "I can apply correct locative case suffixes for regions (Erdélyben, Felvidéken, Kárpátalján).",
                    "I can learn 6 essential terms for historical regions and cultural autonomy.",
                    "I can discuss educational and linguistic rights in neighboring states."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-magyarsag-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-magyarsag-02-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag-02-regiok.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-magyarsag-02-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-02.ex01",
                    "b1-magyarsag-02.ex02",
                    "b1-magyarsag-02.ex03",
                    "b1-magyarsag-02.ex04",
                    "b1-magyarsag-02.ex05",
                    "b1-magyarsag-02.ex06",
                    "b1-magyarsag-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.magyarsag-03",
        "unit": 35,
        "title": "A magyar diaszpóra a világban: Nyugattól a tengerentúlig",
        "level": "B1",
        "grammar": "Diaspora Preservation Syntax: Ápolja a kapcsolatot & Megőrzi az identitást",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe Hungarian diaspora communities across Europe, the Americas, and Australia.",
                    "I can use preservation collocations like ápolja a kapcsolatot and megőrzi a nyelvet.",
                    "I can acquire 6 vocabulary words for emigration, diaspora institutions, and scouting.",
                    "I can understand how weekend schools and Hungarian Clubs preserve national identity."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-magyarsag-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-magyarsag-03-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag-03-diaszpora.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-magyarsag-03-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-03.ex01",
                    "b1-magyarsag-03.ex02",
                    "b1-magyarsag-03.ex03",
                    "b1-magyarsag-03.ex04",
                    "b1-magyarsag-03.ex05",
                    "b1-magyarsag-03.ex06",
                    "b1-magyarsag-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.magyarsag-04",
        "unit": 35,
        "title": "Közép-európai szövetség: A Visegrádi Négyek és az Európai Unió",
        "level": "B1",
        "grammar": "Regional Cooperation Formulas: Együttműködik, álláspontot egyeztet",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the Visegrád Four (V4) alliance and Central European cooperation.",
                    "I can use formal diplomatic coordination verbs in Hungarian.",
                    "I can acquire 6 terms for regional diplomacy, the EU, and the Schengen zone.",
                    "I can appreciate how European integration enables seamless cross-border ties."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-magyarsag-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-magyarsag-04-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag-04-eu.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-magyarsag-04-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-04.ex01",
                    "b1-magyarsag-04.ex02",
                    "b1-magyarsag-04.ex03",
                    "b1-magyarsag-04.ex04",
                    "b1-magyarsag-04.ex05",
                    "b1-magyarsag-04.ex06",
                    "b1-magyarsag-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.magyarsag-05",
        "unit": 35,
        "title": "A nemzetpolitika intézményei és a honosítás",
        "level": "B1",
        "grammar": "Preferential Naturalization & Kinship: Honosításban részesül, igazolja a származást",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can understand the legal process of simplified naturalization for people of Hungarian ancestry.",
                    "I can use administrative naturalization terminology and civic kinship formulas.",
                    "I can learn 6 words for national togetherness, civil programs, and consular protection.",
                    "I can explain the significance of the June 4 Day of National Togetherness."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-magyarsag-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-magyarsag-05-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag-05-honositas.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-magyarsag-05-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-05.ex01",
                    "b1-magyarsag-05.ex02",
                    "b1-magyarsag-05.ex03",
                    "b1-magyarsag-05.ex04",
                    "b1-magyarsag-05.ex05",
                    "b1-magyarsag-05.ex06",
                    "b1-magyarsag-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.magyarsag-consolidation",
        "unit": 35,
        "title": "Magyarság a világban és nemzetközi kapcsolatok (Consolidation)",
        "level": "B1",
        "grammar": "Comprehensive review of cross-border Hungarian communities, diaspora, and international ties",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Consolidate all 30 vocabulary items on cross-border communities, diaspora, V4, and naturalization.",
                    "Review constitutional responsibility clauses, regional locatives, and diplomatic coordination verbs.",
                    "Read the full compendium on the worldwide Hungarian nation and its international position.",
                    "Demonstrate readiness for the Hungarian citizenship examination questions on national policy."
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-magyarsag.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-magyarsag-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-magyarsag-consolidation.ex01",
                    "b1-magyarsag-consolidation.ex02",
                    "b1-magyarsag-consolidation.ex03",
                    "b1-magyarsag-consolidation.ex04",
                    "b1-magyarsag-consolidation.ex05",
                    "b1-magyarsag-consolidation.ex06",
                    "b1-magyarsag-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-magyarsag-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_35_citizenship()
