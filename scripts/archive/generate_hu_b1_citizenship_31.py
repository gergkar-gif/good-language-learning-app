#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 31: The Constitution: Alaptörvény (b1-alaptorveny)."""

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

def build_unit_31_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.alaptorveny.01",
        "lesson": "b1-alaptorveny-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Alaptörvény", "translation": "Fundamental Law (Hungary's constitution)", "pos": "noun"},
            {"lemma": "alkotmányos rend", "translation": "constitutional order", "pos": "noun"},
            {"lemma": "történeti alkotmány", "translation": "historical constitution (uncodified customary constitutional heritage)", "pos": "noun"},
            {"lemma": "húsvéti alkotmány", "translation": "Easter Constitution (adopted on Easter Monday, 25 April 2011)", "pos": "noun"},
            {"lemma": "preambulum", "translation": "preamble, solemn introductory statement", "pos": "noun"},
            {"lemma": "hatálybalépés", "translation": "entry into force (1 January 2012)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-alaptorveny-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.alaptorveny.02",
        "lesson": "b1-alaptorveny-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Nemzeti hitvallás", "translation": "National Avowal (creed opening the Fundamental Law)", "pos": "noun"},
            {"lemma": "Szent István állama", "translation": "Saint Stephen's state, foundational Christian kingdom", "pos": "noun"},
            {"lemma": "nemzeti örökség", "translation": "national heritage, historical legacy", "pos": "noun"},
            {"lemma": "kereszténység megtartó ereje", "translation": "preserving power of Christianity", "pos": "noun"},
            {"lemma": "történelmi hűség", "translation": "historical loyalty, fidelity to ancestral roots", "pos": "noun"},
            {"lemma": "nemzeti önazonosság", "translation": "national identity, self-definition as Hungarians", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-alaptorveny-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.alaptorveny.03",
        "lesson": "b1-alaptorveny-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Alapvetés", "translation": "Foundations (first chapter of the Fundamental Law)", "pos": "noun"},
            {"lemma": "Szabadság és felelősség", "translation": "Freedom and Responsibility (bill of rights chapter)", "pos": "noun"},
            {"lemma": "emberi méltóság", "translation": "human dignity, supreme inviolable value", "pos": "noun"},
            {"lemma": "sérthetetlenség", "translation": "inviolability, immunity from infringement", "pos": "noun"},
            {"lemma": "egyenjogúság", "translation": "equality of rights, equal legal status", "pos": "noun"},
            {"lemma": "véleménynyilvánítás szabadsága", "translation": "freedom of expression and opinion", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-alaptorveny-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.alaptorveny.04",
        "lesson": "b1-alaptorveny-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Állam fejezete", "translation": "The State chapter (defining institutional structure)", "pos": "noun"},
            {"lemma": "közjó", "translation": "the common good, public welfare", "pos": "noun"},
            {"lemma": "jogbiztonság", "translation": "legal certainty, predictability of the law", "pos": "noun"},
            {"lemma": "hatalmi ágak megosztása", "translation": "separation of branches of power", "pos": "noun"},
            {"lemma": "közteherviselés", "translation": "bearing of public burdens, proportional taxation", "pos": "noun"},
            {"lemma": "haza védelme", "translation": "defense of the homeland, civic military duty", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-alaptorveny-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.alaptorveny.05",
        "lesson": "b1-alaptorveny-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Alkotmánybíróság", "translation": "Constitutional Court of Hungary", "pos": "noun"},
            {"lemma": "alaptörvény-ellenesség", "translation": "unconstitutionality, contrariety to Fundamental Law", "pos": "noun"},
            {"lemma": "normakontroll", "translation": "constitutional review (abstract or concrete norm control)", "pos": "noun"},
            {"lemma": "alapvető jogok biztosa", "translation": "Commissioner for Fundamental Rights (Ombudsman)", "pos": "noun"},
            {"lemma": "jogállami garancia", "translation": "rule-of-law guarantee, legal safeguard", "pos": "noun"},
            {"lemma": "sarkalatos törvény", "translation": "cardinal law (requiring two-thirds parliamentary majority)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-alaptorveny-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.alaptorveny.01.promulgation",
        "title": "Founding Constitutional Promulgation: Hatályba lép & Rögzít",
        "sections": [
            {
                "type": "text",
                "title": "Promulgation Verbs",
                "content": "Hungarian constitutional discourse employs precise legal verbs: *kihirdet* (promulgates), *hatályba lép* (enters into force), and *rögzít* (enshrines, lays down). These formal verbs govern direct objects or inessive complements."
            },
            {
                "type": "examples",
                "title": "Promulgation examples",
                "items": [
                    {"spanish": "Az Országgyűlés 2011 húsvéthétfőjén fogadta el az Alaptörvényt.", "english": "The National Assembly adopted the Fundamental Law on Easter Monday 2011."},
                    {"spanish": "Magyarország Alaptörvénye 2012. január 1-jén lépett hatályba.", "english": "Hungary's Fundamental Law entered into force on 1 January 2012."},
                    {"spanish": "Az Alaptörvény Magyarország jogrendszerének az alapja.", "english": "The Fundamental Law is the foundation of Hungary's legal system."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-alaptorveny-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.alaptorveny.02.national-avowal",
        "title": "Solemn Declarative Registers: Valljuk, hogy... & Elismerjük",
        "sections": [
            {
                "type": "text",
                "title": "Solemn Declarative Verbs",
                "content": "The preamble 'Nemzeti hitvallás' (National Avowal) uses first-person plural solemn declarative verbs: *valljuk, hogy...* (we profess that), *elismerjük* (we recognize), and *tiszteletben tartjuk* (we hold in respect), expressing collective national commitment."
            },
            {
                "type": "examples",
                "title": "Avowal examples",
                "items": [
                    {"spanish": "Valljuk, hogy a kereszténységnek nemzetmegtartó szerepe van.", "english": "We profess that Christianity has a nation-preserving role."},
                    {"spanish": "Elismerjük Szent István király államalapító művét.", "english": "We recognize the state-founding work of King Saint Stephen."},
                    {"spanish": "Tiszteletben tartjuk hazánk történeti alkotmányának vívmányait.", "english": "We respect the achievements of our country's historical constitution."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-alaptorveny-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.alaptorveny.03.fundamental-rights",
        "title": "Constitutional Rights & Entitlements: Mindenkinek joga van a...-hoz",
        "sections": [
            {
                "type": "text",
                "title": "Rights Formulations",
                "content": "Human rights are codified using the dative-allative pattern: *mindenkinek joga van a [valamihez]* (everyone has the right to sth) and absolute predicative adjectives: *az emberi méltóság sérthetetlen* (human dignity is inviolable)."
            },
            {
                "type": "examples",
                "title": "Rights examples",
                "items": [
                    {"spanish": "Az emberi méltóság sérthetetlen és elidegeníthetetlen.", "english": "Human dignity is inviolable and inalienable."},
                    {"spanish": "Mindenkinek joga van az élethez és a szabadsághoz.", "english": "Everyone has the right to life and freedom."},
                    {"spanish": "A törvény előtt minden ember egyenlő, megkülönböztetés nélkül.", "english": "All persons are equal before the law, without discrimination."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-alaptorveny-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.alaptorveny.04.civic-duties",
        "title": "Civic Obligations: Kötelessége hozzájárulni & Felelősséggel tartozik",
        "sections": [
            {
                "type": "text",
                "title": "Duty and Responsibility Formulations",
                "content": "The Fundamental Law balances rights with civic responsibilities using *kötelessége [infinitívusz]* (it is one's duty to do sth) and *felelősséggel tartozik* (bears responsibility for)."
            },
            {
                "type": "examples",
                "title": "Duty examples",
                "items": [
                    {"spanish": "Minden állampolgár kötelessége hozzájárulni a közteherviseléshez.", "english": "Every citizen has the duty to contribute to public burden-bearing."},
                    {"spanish": "A haza védelme minden magyar állampolgár szent kötelessége.", "english": "The defense of the homeland is a sacred duty of every Hungarian citizen."},
                    {"spanish": "Mindenki felelősséggel tartozik önmagáért és a közösségért.", "english": "Everyone bears responsibility for themselves and for the community."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-alaptorveny-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.alaptorveny.05.cardinal-review",
        "title": "Cardinal Laws & Constitutional Review: Sarkalatos törvény & Megsemmisít",
        "sections": [
            {
                "type": "text",
                "title": "Cardinal Majority and Annulment",
                "content": "Crucial institutional laws (*sarkalatos törvények*) require a two-thirds majority of MPs present (*a jelen lévő képviselők kétharmadának szavazata*). The Constitutional Court examines laws for unconstitutionality and may annul them (*megsemmisíti az alaptörvény-ellenes jogszabályt*)."
            },
            {
                "type": "examples",
                "title": "Cardinal law examples",
                "items": [
                    {"spanish": "A sarkalatos törvény elfogadásához kétharmados többség szükséges.", "english": "A two-thirds majority is required to adopt a cardinal law."},
                    {"spanish": "Az Alkotmánybíróság megsemmisíti a jogszabályt, ha az alaptörvény-ellenes.", "english": "The Constitutional Court annuls the legal regulation if it is unconstitutional."},
                    {"spanish": "Az alapvető jogok biztosa védi az állampolgárok alkotmányos jogait.", "english": "The Commissioner for Fundamental Rights protects the constitutional rights of citizens."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-alaptorveny-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (5 segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.alaptorveny.01",
        "title": "Az Alaptörvény születése és a magyar alkotmányosság",
        "level": "B1",
        "lesson": 1,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The history and adoption of Hungary's Fundamental Law on Easter Monday 2011, replacing the amended 1949 constitution.",
        "characters": [],
        "location": "Budapest, Országház",
        "grammar": ["grammar.b1.alaptorveny.01.promulgation"],
        "vocabularyTopics": ["Alaptörvény", "alkotmányos rend", "hatálybalépés"],
        "paragraphs": [
            {"type": "narration", "text": "Magyarország évszázadokon át íratlan, úgynevezett történeti alkotmánnyal rendelkezett, amelyet a szokásjog, a királyi dekrétumok és az Aranybulla alkotott."},
            {"type": "narration", "text": "A szovjet típusú 1949-es alkotmányt az 1989-es rendszerváltoztatáskor alaposan módosították, de a nemzet képviselői egy teljesen új alaptörvény megalkotását tervezték."},
            {"type": "narration", "text": "A magyar Országgyűlés 2011. április 25-én, húsvéthétfőn fogadta el az új Alaptörvényt, amelyet Schmitt Pál köztársasági elnök írt alá."},
            {"type": "narration", "text": "Az Alaptörvény ünnepélyes hatálybalépésére 2012. január 1-jén került sor az Operaházban tartott díszelőadáson."},
            {"type": "narration", "text": "Az új Alaptörvény egyszerre tükrözi Magyarország ezeréves keresztény államiságát és a modern európai jogállam legmagasabb követelményeit."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny-01-szuletese.json", story_01)

    story_02 = {
        "id": "story.b1.alaptorveny.02",
        "title": "A Nemzeti hitvallás: a nemzet közös értékei",
        "level": "B1",
        "lesson": 2,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The preamble of the Fundamental Law, the National Avowal, which honors Saint Stephen and affirms national identity.",
        "characters": [],
        "location": "Budapest, Nemzeti Emlékhely",
        "grammar": ["grammar.b1.alaptorveny.02.national-avowal"],
        "vocabularyTopics": ["Nemzeti hitvallás", "nemzeti önazonosság", "Szent István állama"],
        "paragraphs": [
            {"type": "narration", "text": "Az Alaptörvény a 'Nemzeti hitvallás' című ünnepélyes preambulummal kezdődik, amely a magyar Himnusz első sorát idézi: 'ISTEN, ÁLDD MEG A MAGYART!'"},
            {"type": "narration", "text": "A hitvallás büszkén vallja, hogy Szent István király ezer évvel ezelőtt szilárd alapokra helyezte a magyar államot, és hazánkat a keresztény Európa részévé tette."},
            {"type": "narration", "text": "A szöveg kinyilvánítja a nemzeti önazonosság védelmét, a magyar nyelv ápolását és a hazánkban élő nemzetiségek értékeinek megbecsülését."},
            {"type": "narration", "text": "Ugyancsak elismeri a határon túli magyarsággal való szellemi és lelki összetartozást, amely határokon átívelő egységet képez."},
            {"type": "narration", "text": "A Nemzeti hitvallás erkölcsi iránytűként szolgál a jogalkotók és minden felelős magyar állampolgár számára."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny-02-hitvallas.json", story_02)

    story_03 = {
        "id": "story.b1.alaptorveny.03",
        "title": "Szabadság és felelősség: az alapvető jogok védelme",
        "level": "B1",
        "lesson": 3,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The bill of rights in the Fundamental Law, guaranteeing human dignity, personal freedom, and civic equality.",
        "characters": [],
        "location": "Budapest",
        "grammar": ["grammar.b1.alaptorveny.03.fundamental-rights"],
        "vocabularyTopics": ["emberi méltóság", "egyenjogúság", "sérthetetlenség"],
        "paragraphs": [
            {"type": "narration", "text": "Az Alaptörvény második nagy fejezete a 'Szabadság és felelősség' címet viseli, amely részletesen felsorolja az alapvető emberi jogokat."},
            {"type": "narration", "text": "A fejezet első és legfontosabb tétele kimondja, hogy az emberi méltóság sérthetetlen, és mindenkinek veleszületett joga van az élethez."},
            {"type": "narration", "text": "Garantálja a gondolat, a lelkiismeret és a vallás szabadságát, valamint a békés gyülekezési és véleménynyilvánítási szabadságot."},
            {"type": "narration", "text": "A törvény előtt minden ember egyenlő: az Alaptörvény szigorúan tiltja a faji, vallási vagy egyéb megkülönböztetést."},
            {"type": "narration", "text": "Ezek az alkotmányos jogok mindenkit megilletnek Magyarország területén, biztosítva a szabad és méltóságteljes életet."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny-03-jogok.json", story_03)

    story_04 = {
        "id": "story.b1.alaptorveny.04",
        "title": "Az állami berendezkedés és a közösség érdeke",
        "level": "B1",
        "lesson": 4,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The organization of the state, the principle of separation of powers, and the civic obligations of citizens.",
        "characters": [],
        "location": "Budapest",
        "grammar": ["grammar.b1.alaptorveny.04.civic-duties"],
        "vocabularyTopics": ["hatalmi ágak megosztása", "közjó", "közteherviselés"],
        "paragraphs": [
            {"type": "narration", "text": "Az Alaptörvény 'Az Állam' fejezete szabályozza a legfőbb állami szervek működését a klasszikus hatalommegosztás elve alapján."},
            {"type": "narration", "text": "A törvényhozó hatalom az Országgyűlés, a végrehajtó hatalom a Kormány, az igazságszolgáltatást pedig a független bíróságok gyakorolják."},
            {"type": "narration", "text": "Az állam célja a közjó szolgálata, a jogbiztonság megteremtése és a nemzeti vagyon védelme."},
            {"type": "narration", "text": "A jogok mellett a polgárok kötelezettségei is rögzítve vannak: a közteherviselés (adófizetés), a tanulás és a haza fegyveres vagy fegyver nélküli védelme."},
            {"type": "narration", "text": "A jogok és kötelességek egyensúlya garantálja a társadalom harmonikus és biztonságos működését."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny-04-allam.json", story_04)

    story_05 = {
        "id": "story.b1.alaptorveny.05",
        "title": "Az Alkotmánybíróság és a sarkalatos törvények garanciája",
        "level": "B1",
        "lesson": 5,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The role of the Constitutional Court, the Commissioner for Fundamental Rights, and cardinal laws in safeguarding democracy.",
        "characters": [],
        "location": "Budapest, Alkotmánybíróság",
        "grammar": ["grammar.b1.alaptorveny.05.cardinal-review"],
        "vocabularyTopics": ["Alkotmánybíróság", "sarkalatos törvény", "alapvető jogok biztosa"],
        "paragraphs": [
            {"type": "narration", "text": "Az alkotmányos rend legfőbb védelmezője az Alkotmánybíróság, amely a többi hatalmi ágtól függetlenül működik."},
            {"type": "narration", "text": "Ha egy törvény vagy kormányrendelet sérti az Alaptörvény rendelkezéseit, az Alkotmánybíróság megsemmisíti azt."},
            {"type": "narration", "text": "Bármely állampolgár alkotmányjogi panasszal fordulhat a testülethez, ha úgy érzi, hogy egy bírósági ítélet sértette az alkotmányos jogait."},
            {"type": "narration", "text": "Az alapvető jogok biztosa (az ombudsman) felügyeli a hatóságok eljárásait, és fellép a jogtalanságok ellen."},
            {"type": "narration", "text": "A legfontosabb társadalmi intézményekről szóló sarkalatos törvények kétharmados konszenzust igényelnek, megakadályozva az egyoldalú módosításokat."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny-05-garanciak.json", story_05)

    story_combined = {
        "id": "story.b1.alaptorveny",
        "title": "Az Alaptörvény: Magyarország alkotmányos rendje",
        "level": "B1",
        "lesson": 31,
        "order": 31,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive overview of Hungary's Fundamental Law: its historical background, the National Avowal, fundamental rights, state structure, and constitutional safeguards.",
        "characters": [],
        "location": "Magyarország, Országház és Alkotmánybíróság",
        "grammar": [
            "grammar.b1.alaptorveny.01.promulgation",
            "grammar.b1.alaptorveny.02.national-avowal",
            "grammar.b1.alaptorveny.03.fundamental-rights",
            "grammar.b1.alaptorveny.04.civic-duties",
            "grammar.b1.alaptorveny.05.cardinal-review"
        ],
        "vocabularyTopics": [
            "Alaptörvény",
            "Nemzeti hitvallás",
            "emberi méltóság",
            "hatalmi ágak megosztása",
            "Alkotmánybíróság",
            "sarkalatos törvény"
        ],
        "paragraphs": [
            {"type": "narration", "text": "Magyarország íratlan történeti alkotmánya évszázadokon át védte a nemzet szabadságát. A rendszerváltoztatás után az Országgyűlés 2011 húsvéthétfőjén fogadta el az új Alaptörvényt, amely 2012. január 1-jén lépett hatályba mint a nemzet legfőbb jogi fundamentuma."},
            {"type": "narration", "text": "Az Alaptörvény ünnepélyes nyitánya, a Nemzeti hitvallás tisztelettel adózik Szent István király ezeréves államalapító műve és a keresztény hagyomány előtt, miközben elismeri a nemzetiségek gazdag kultúráját és a határon túli magyarok egységét."},
            {"type": "narration", "text": "A 'Szabadság és felelősség' fejezet sérthetetlen értékként deklarálja az emberi méltóságot, az egyenlőséget, valamint a vallás, a szólás és a gyülekezés szabadságát, amely minden embert egyformán megillet."},
            {"type": "narration", "text": "Az államszervezet a hatalommegosztás elvére épül: a népképviseleti Országgyűlésre, a végrehajtó Kormányra és a független bíróságokra. A jogok mellett az Alaptörvény hangsúlyozza az állampolgári felelősséget, a közteherviselést és a haza védelmét."},
            {"type": "narration", "text": "A jogállamiság garanciáját az Alkotmánybíróság, az alapvető jogok biztosa és a kétharmados többséggel elfogadott sarkalatos törvények biztosítják, védve Magyarország demokratikus és szilárd jövőjét."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-alaptorveny.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercises Files (8 exercises per lesson x 5 + consolidation = 6 files)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-alaptorveny-01",
        "exercises": [
            {
                "id": "b1-alaptorveny-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mikor lépett hatályba Magyarország Alaptörvénye?",
                "options": [
                    "2012. január 1-jén.",
                    "1989. október 23-án.",
                    "2004. május 1-jén."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az Alaptörvény 2012. január elsején lépett hatály_____. (into force - ba)",
                "answer": "ba"
            },
            {
                "id": "b1-alaptorveny-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "Alaptörvény", "Magyarország", "jogrendszerének", "a", "legfőbb", "alapja."],
                "solution": ["Az", "Alaptörvény", "Magyarország", "jogrendszerének", "a", "legfőbb", "alapja."]
            },
            {
                "id": "b1-alaptorveny-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'történeti alkotmány' kifejezés a magyar jogtörténetben?",
                "options": [
                    "Az évszázadok során kialakult szokásjog és törvények íratlan, de kötelező összességét.",
                    "Egy ókori görög törvénykönyv másolatát.",
                    "A mai napilapok jogi rovatát."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az Országgyűlés 2011 húsvéthétfőjén fogadta el az új Alaptörvény_____. (the Fundamental Law - t)",
                "answer": "t"
            },
            {
                "id": "b1-alaptorveny-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'preambulum'?",
                "options": [
                    "Egy törvény vagy alkotmány ünnepélyes, értékeket megfogalmazó bevezetője.",
                    "Egy pénzügyi táblázat az adóhivatalban.",
                    "Egy katonai díszszemle menete."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársasági elnök ünnepélyesen kihirdet_____ az Alaptörvényt. (promulgated it - te)",
                "answer": "te"
            },
            {
                "id": "b1-alaptorveny-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "alkotmányos", "rend", "védi", "a", "demokráciát", "és", "a", "jogállamot."],
                "solution": ["Az", "alkotmányos", "rend", "védi", "a", "demokráciát", "és", "a", "jogállamot."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-alaptorveny-02",
        "exercises": [
            {
                "id": "b1-alaptorveny-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik híres idézettel kezdődik a Nemzeti hitvallás?",
                "options": [
                    "'ISTEN, ÁLDD MEG A MAGYART!'",
                    "'Talpra magyar, hí a haza!'",
                    "'Hazádnak rendületlenül légy híve, ó magyar!'"
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Valljuk, hogy a kereszténységnek nemzetmegtartó szerepe van a történelmünk_____. (in our history - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-alaptorveny-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Elismerjük", "Szent", "István", "király", "ezeréves", "államalapító", "művét."],
                "solution": ["Elismerjük", "Szent", "István", "király", "ezeréves", "államalapító", "művét."]
            },
            {
                "id": "b1-alaptorveny-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezi ki a Nemzeti hitvallás a közös értékelköteleződést?",
                "options": [
                    "Többes szám első személyű ünnepélyes igékkel: 'valljuk', 'elismerjük', 'tiszteletben tartjuk'.",
                    "Kérdő mondatokkal a bizonytalanság kifejezésére.",
                    "Feltételes múlt idejű tagadásokkal."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Nemzeti hitvallás védi a magyar nemzeti önazonosság_____. (its identity - t)",
                "answer": "t"
            },
            {
                "id": "b1-alaptorveny-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit ismer el az Alaptörvény a hazánkban élő nemzetiségekkel kapcsolatban?",
                "options": [
                    "Hogy a velünk élő nemzetiségek a magyar politikai közösség részei és államalkotó tényezők.",
                    "Hogy csak vendégek Magyarországon.",
                    "Hogy nem beszélhetik a saját anyanyelvüket."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Tiszteletben tartjuk hazánk kulturális örökség_____. (its heritage - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-alaptorveny-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magyar", "nemzet", "összetartozása", "határokon", "átívelő", "valóság."],
                "solution": ["A", "magyar", "nemzet", "összetartozása", "határokon", "átívelő", "valóság."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-alaptorveny-03",
        "exercises": [
            {
                "id": "b1-alaptorveny-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az Alaptörvény szerint az emberi jogok legfőbb fundamentuma?",
                "options": [
                    "Az emberi méltóság sérthetetlensége.",
                    "A pénzügyi vagyon nagysága.",
                    "A származási bizonyítvány megléte."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindenkinek joga van az élethez és az emberi méltóság_____. (to dignity - hoz)",
                "answer": "hoz"
            },
            {
                "id": "b1-alaptorveny-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "törvény", "előtt", "minden", "ember", "egyenlő,", "megkülönböztetés", "nélkül."],
                "solution": ["A", "törvény", "előtt", "minden", "ember", "egyenlő,", "megkülönböztetés", "nélkül."]
            },
            {
                "id": "b1-alaptorveny-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás fejezi ki helyesen a véleménynyilvánítás szabadságát?",
                "options": [
                    "Mindenkinek joga van a véleménynyilvánítás szabadságához.",
                    "Mindenkinek tilos véleményt nyilvánítani nyilvánosan.",
                    "A vélemény csak otthon szabad a szobában."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az emberi méltóság sérthetetlen és elidegeníthetetlen érték az alkotmány_____. (in constitution - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-alaptorveny-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'egyenjogúság' elve?",
                "options": [
                    "Hogy minden polgárt ugyanazok a jogok és kötelezettségek illetnek meg a törvény előtt.",
                    "Hogy mindenkinek pontosan ugyanannyi pénze van.",
                    "Hogy mindenki azonos foglalkozást választ."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az Alaptörvény garantálja a vallásszabadság_____ minden lakos számára. (its freedom - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-alaptorveny-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szabadság", "és", "a", "felelősség", "elválaszthatatlanul", "összetartozik."],
                "solution": ["A", "szabadság", "és", "a", "felelősség", "elválaszthatatlanul", "összetartozik."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-alaptorveny-04",
        "exercises": [
            {
                "id": "b1-alaptorveny-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik elv alapján oszlik meg a magyar állami főhatalom?",
                "options": [
                    "A hatalmi ágak megosztásának elve alapján (törvényhozás, végrehajtás, igazságszolgáltatás).",
                    "Egyetlen uralkodó korlátlan parancsa alapján.",
                    "A polgármesterek sorsolása alapján."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden állampolgár kötelessége hozzájárulni a közteherviselés_____. (to public burdens - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-alaptorveny-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "haza", "védelme", "minden", "magyar", "állampolgár", "szent", "kötelessége."],
                "solution": ["A", "haza", "védelme", "minden", "magyar", "állampolgár", "szent", "kötelessége."]
            },
            {
                "id": "b1-alaptorveny-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'jogbiztonság' az állampolgárok szemszögéből?",
                "options": [
                    "Hogy a törvények egyértelműek, kiszámíthatók és mindenki számára megismerhetők.",
                    "Hogy minden épület előtt rendőr áll.",
                    "Hogy nem szabad fellebbezni semmilyen döntés ellen."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az állami szervek működésének legfőbb célja a közjó szolgálat_____. (its service - a)",
                "answer": "a"
            },
            {
                "id": "b1-alaptorveny-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit nevezünk 'közteherviselésnek'?",
                "options": [
                    "Az adók és járulékok fizetését a közös kiadások és közszolgáltatások fedezésére.",
                    "Nehéz csomagok közös cipelését az állomáson.",
                    "A közösségi közlekedés ingyenességét."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden ember felelősséggel tartozik a környezet megóvásá_____. (for its protection - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-alaptorveny-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "törvényes", "rend", "és", "a", "közjó", "biztosítja", "a", "társadalom", "békéjét."],
                "solution": ["A", "törvényes", "rend", "és", "a", "közjó", "biztosítja", "a", "társadalom", "békéjét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-alaptorveny-05",
        "exercises": [
            {
                "id": "b1-alaptorveny-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az Alkotmánybíróság legfontosabb feladata?",
                "options": [
                    "Az Alaptörvény védelme és az alaptörvény-ellenes jogszabályok megsemmisítése.",
                    "A parlamenti képviselők fizetésének átutalása.",
                    "A rendőrség napi járőrszolgálatának irányítása."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A sarkalatos törvény elfogadásához kétharmados többség szükség_____. (necessary - es)",
                "answer": "es"
            },
            {
                "id": "b1-alaptorveny-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "Alkotmánybíróság", "megsemmisíti", "az", "alaptörvény-ellenes", "jogszabályokat."],
                "solution": ["Az", "Alkotmánybíróság", "megsemmisíti", "az", "alaptörvény-ellenes", "jogszabályokat."]
            },
            {
                "id": "b1-alaptorveny-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen törvényeket nevezünk 'sarkalatos törvényeknek'?",
                "options": [
                    "Olyan kiemelkedő fontosságú törvényeket, amelyek elfogadásához a jelen lévő képviselők kétharmadának szavazata szükséges.",
                    "Olyan rendeleteket, amelyeket csak télen alkalmaznak.",
                    "A sarkvidéki kutatásokról szóló megállapodásokat."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az alapvető jogok biztos_____ védi az állampolgárok alkotmányos jogait. (its commissioner - a)",
                "answer": "a"
            },
            {
                "id": "b1-alaptorveny-05.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kihez fordulhat az az állampolgár, aki a hatóságok jogsértő eljárását tapasztalja?",
                "options": [
                    "Az alapvető jogok biztosához (ombudsmanhoz) vagy alkotmányjogi panasszal az Alkotmánybírósághoz.",
                    "A legközelebbi vasútállomás pénztárához.",
                    "Csak külföldi nagykövetségekhez."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A jogállamiság garanciái biztosítják a polgárok biztonság_____. (their safety - át)",
                "answer": "át"
            },
            {
                "id": "b1-alaptorveny-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "független", "intézmények", "a", "demokratikus", "jogállam", "legfőbb", "garanciái."],
                "solution": ["A", "független", "intézmények", "a", "demokratikus", "jogállam", "legfőbb", "garanciái."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-alaptorveny-consolidation",
        "exercises": [
            {
                "id": "b1-alaptorveny-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hányadikán lépett hatályba Magyarország mai Alaptörvénye?",
                "options": [
                    "2012. január 1-jén.",
                    "2010. május 29-én.",
                    "2011. március 15-én."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az emberi méltóság sérthetetlen és elidegeníthetetlen érték az alkotmányunk_____. (in our constitution - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-alaptorveny-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "Alaptörvény", "Magyarország", "alkotmányos", "rendjének", "a", "szilárd", "alapja."],
                "solution": ["Az", "Alaptörvény", "Magyarország", "alkotmányos", "rendjének", "a", "szilárd", "alapja."]
            },
            {
                "id": "b1-alaptorveny-consolidation.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit garantál az Alkotmánybíróság döntése a jogrendszer számára?",
                "options": [
                    "Hogy egyetlen jogszabály sem lehet ellentétes az Alaptörvény rendelkezéseivel és szellemével.",
                    "Hogy minden törvényt évente újra kell írni.",
                    "Hogy a bíróságok nem hozhatnak ítéletet."
                ],
                "correct": 0
            },
            {
                "id": "b1-alaptorveny-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A sarkalatos törvények kétharmados többséget igényel_____ a parlamentben. (require - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-alaptorveny-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "Nemzeti", "hitvallás", "összeköti", "a", "múltat,", "a", "jelent", "és", "a", "jövőt."],
                "solution": ["A", "Nemzeti", "hitvallás", "összeköti", "a", "múltat,", "a", "jelent", "és", "a", "jövőt."]
            },
            {
                "id": "b1-alaptorveny-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden állampolgár felelősséggel tartozik a közösség sorsá_____. (for its fate - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-alaptorveny-consolidation.ex08",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mely három hatalmi ágra oszlik a demokratikus magyar államszervezet?",
                "options": [
                    "Törvényhozás (Országgyűlés), végrehajtás (Kormány) és igazságszolgáltatás (Bíróságok).",
                    "Rendőrség, posta és vasút.",
                    "Egyház, sajtó és egyetemek."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-alaptorveny-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Az Alaptörvény születése és hatálybalépése", "The Birth & Promulgation of the Fundamental Law"),
        "02": ("A Nemzeti hitvallás és a történelmi örökség", "The National Avowal & Historical Heritage"),
        "03": ("Szabadság és felelősség: alapvető jogok", "Freedom & Responsibility: Fundamental Rights"),
        "04": ("Az állami berendezkedés és a közteherviselés", "State Organization & Civic Responsibilities"),
        "05": ("Az Alkotmánybíróság és a jogállami garanciák", "The Constitutional Court & Democratic Safeguards")
    }

    story_refs = {
        "01": "stories/world/b1/b1-alaptorveny-01-szuletese.json",
        "02": "stories/world/b1/b1-alaptorveny-02-hitvallas.json",
        "03": "stories/world/b1/b1-alaptorveny-03-jogok.json",
        "04": "stories/world/b1/b1-alaptorveny-04-allam.json",
        "05": "stories/world/b1/b1-alaptorveny-05-garanciak.json"
    }

    grammar_refs = {
        "01": "grammar/b1/b1-alaptorveny-01-gr.json",
        "02": "grammar/b1/b1-alaptorveny-02-gr.json",
        "03": "grammar/b1/b1-alaptorveny-03-gr.json",
        "04": "grammar/b1/b1-alaptorveny-04-gr.json",
        "05": "grammar/b1/b1-alaptorveny-05-gr.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.alaptorveny-{padded}",
            "unit": 31,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Constitutional Regimes, Rights Guarantees & Legal Terminology in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungarian.",
                        "I can use constitutional terms (Alaptörvény, Nemzeti hitvallás, emberi méltóság, sarkalatos törvény).",
                        "I can explain fundamental human rights and civic duties as tested in the Hungarian citizenship examination.",
                        "I can read and analyze the serialized historical story on Hungary's constitutional order."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-alaptorveny-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded]},
                {
                    "type": "story",
                    "title": hu_t,
                    "ref": story_refs[padded]
                },
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-alaptorveny-{padded}-ex.json",
                    "exerciseRefs": [f"b1-alaptorveny-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-alaptorveny-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.alaptorveny-consolidation",
        "unit": 31,
        "title": "Unit 31 Consolidation (Az Alaptörvény)",
        "level": "B1",
        "grammar": "Consolidation of Hungarian Constitutional Knowledge, Fundamental Rights & Alaptörvény",
        "sections": [
            {
                "type": "story",
                "title": "Az Alaptörvény: Magyarország alkotmányos rendje",
                "ref": "stories/world/b1/b1-alaptorveny.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-alaptorveny-consolidation-ex.json",
                "exerciseRefs": [f"b1-alaptorveny-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-alaptorveny-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Citizenship Unit 31 (b1-alaptorveny)!")

if __name__ == "__main__":
    build_unit_31_citizenship()
