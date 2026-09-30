#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 36: Being a Hungarian Citizen: Rights, Duties & the Oath (b1-allampolgarsag)."""

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

def build_unit_36_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total - Pacing Target)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.allampolgarsag.01",
        "lesson": "b1-allampolgarsag-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "magyar állampolgár", "translation": "Hungarian citizen (subject of the Hungarian state)", "pos": "noun"},
            {"lemma": "állampolgársági bizonyítvány", "translation": "citizenship certificate (official proof of legal citizenship)", "pos": "noun"},
            {"lemma": "vérségi elv", "translation": "jus sanguinis / principle of descent (Hungarian citizenship acquired by birth to Hungarian parents)", "pos": "noun"},
            {"lemma": "honosítási okirat", "translation": "naturalization document / certificate of naturalization", "pos": "noun"},
            {"lemma": "kettős állampolgárság", "translation": "dual citizenship (permitted and recognized under Hungarian law)", "pos": "noun"},
            {"lemma": "jogállás", "translation": "legal status, statutory condition", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allampolgarsag-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.allampolgarsag.02",
        "lesson": "b1-allampolgarsag-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "választójog", "translation": "right to vote, suffrage", "pos": "noun"},
            {"lemma": "aktív választójog", "translation": "active voting right (right to cast a ballot in elections)", "pos": "noun"},
            {"lemma": "passzív választójog", "translation": "passive voting right (eligibility to stand as a candidate)", "pos": "noun"},
            {"lemma": "petíciós jog", "translation": "right of petition (right to address complaints to state bodies)", "pos": "noun"},
            {"lemma": "gyülekezési jog", "translation": "freedom of peaceful assembly", "pos": "noun"},
            {"lemma": "egyenlő méltóság", "translation": "equal human dignity of all citizens", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allampolgarsag-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.allampolgarsag.03",
        "lesson": "b1-allampolgarsag-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "állampolgári kötelesség", "translation": "civic duty, constitutional obligation of citizens", "pos": "noun"},
            {"lemma": "honvédelmi kötelezettség", "translation": "national defense duty (obligation to protect the homeland)", "pos": "noun"},
            {"lemma": "közteherviselés", "translation": "bearing of public burdens (paying taxes and contributions according to capacity)", "pos": "noun"},
            {"lemma": "tankötelezettség", "translation": "compulsory school attendance (mandatory education up to age 16)", "pos": "noun"},
            {"lemma": "környezetvédelem", "translation": "protection of the natural environment and resources", "pos": "noun"},
            {"lemma": "törvénytisztelet", "translation": "respect for the rule of law and statutory statutes", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allampolgarsag-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.allampolgarsag.04",
        "lesson": "b1-allampolgarsag-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "állampolgársági eskü", "translation": "Citizenship Oath (solemn oath taken before God and the nation)", "pos": "noun"},
            {"lemma": "állampolgársági fogadalom", "translation": "Citizenship Pledge (solemn secular alternative to the oath)", "pos": "noun"},
            {"lemma": "hazaszeretet", "translation": "patriotism, love of the homeland", "pos": "noun"},
            {"lemma": "ünnepélyes ceremónia", "translation": "solemn ceremony (held in the presence of the mayor)", "pos": "noun"},
            {"lemma": "hűség", "translation": "fidelity, loyalty to Hungary and the Fundamental Law", "pos": "noun"},
            {"lemma": "polgármesteri hivatal", "translation": "mayor's office (venue where citizenship oaths are administered)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allampolgarsag-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.allampolgarsag.05",
        "lesson": "b1-allampolgarsag-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "demokratikus részvétel", "translation": "democratic civic participation in public affairs", "pos": "noun"},
            {"lemma": "társadalmi szolidaritás", "translation": "social solidarity, mutual support among citizens", "pos": "noun"},
            {"lemma": "közösségi szerepvállalás", "translation": "community engagement, civic contribution", "pos": "noun"},
            {"lemma": "alkotmányos alapismeretek", "translation": "constitutional basics (curriculum tested in the citizenship examination)", "pos": "noun"},
            {"lemma": "állampolgársági vizsga", "translation": "citizenship examination (written and oral test on Hungarian history and law)", "pos": "noun"},
            {"lemma": "nemzeti elköteleződés", "translation": "national commitment, dedicated devotion to the homeland", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allampolgarsag-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per regular lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.allampolgarsag.01.citizenship-acquisition",
        "title": "Legal Status & Acquisition Valencies: Származás útján, részesül",
        "sections": [
            {
                "type": "text",
                "title": "Acquiring Citizenship",
                "content": "In Hungarian nationality law, citizenship is primarily acquired through descent (*leszármazás útján / vérségi elv alapján*): *A gyermek születésével magyar állampolgárrá válik, ha legalább egyik szülője magyar állampolgár.* For naturalization, Hungarian uses the construction *honosításban részesül* (is granted naturalization)."
            },
            {
                "type": "examples",
                "title": "Acquisition examples",
                "items": [
                    {"spanish": "A magyar állampolgárság a vérségi elv alapján, születéssel keletkezik.", "english": "Hungarian citizenship originates at birth on the basis of the principle of descent."},
                    {"spanish": "A kérelmező kedvezményes honosítási eljárásban részesülhet.", "english": "The applicant may be granted preferential naturalization."},
                    {"spanish": "A magyar jogszabályok teljes mértékben elismerik a kettős állampolgárságot.", "english": "Hungarian statutory statutes fully recognize dual citizenship."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allampolgarsag-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.allampolgarsag.02.fundamental-rights-syntax",
        "title": "Constitutional Entitlement Syntax: Joga van vmihez & Megilleti",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Constitutional Rights",
                "content": "To express basic political and civil rights, Hungarian law pairs verbal predicates with the allative case (*joga van vmihez*) or transitive verbs of entitlement (*megillet vkit*): *Minden nagykorú magyar állampolgárt megillet a választójog.*"
            },
            {
                "type": "examples",
                "title": "Rights syntax examples",
                "items": [
                    {"spanish": "Minden magyar állampolgárnak joga van részt venni az országgyűlési választásokon.", "english": "Every Hungarian citizen has the right to participate in parliamentary elections."},
                    {"spanish": "Az állampolgárokat megilleti a békés gyülekezés és a véleménynyilvánítás szabadsága.", "english": "Citizens are entitled to the freedom of peaceful assembly and expression of opinion."},
                    {"spanish": "Mindenkinek joga van ahhoz, hogy kérelmével a hatóságokhoz forduljon.", "english": "Everyone has the right to address petitions to the authorities."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allampolgarsag-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.allampolgarsag.03.civic-duties-syntax",
        "title": "Civic Duty & Obligation Syntax: Kötelessége [Infinitivus], Tartozik",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Constitutional Duties",
                "content": "Constitutional obligations are expressed using impersonal dative predicates: *minden állampolgár kötelessége [főnévi igenév]* (it is the duty of every citizen to...), or *felelősséggel tartozik a társadalomnak* (owes responsibility to society)."
            },
            {
                "type": "examples",
                "title": "Duty syntax examples",
                "items": [
                    {"spanish": "Minden állampolgár kötelessége hozzájárulni a közös szükségletek fedezéséhez.", "english": "It is the duty of every citizen to contribute to covering common public needs."},
                    {"spanish": "A szülők kötelesek gondoskodni kiskorú gyermekeik taníttatásáról.", "english": "Parents are obliged to ensure the schooling of their minor children."},
                    {"spanish": "Mindenki felelősséggel tartozik a természeti környezet megóvásáért.", "english": "Everyone bears responsibility for preserving the natural environment."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allampolgarsag-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.allampolgarsag.04.solemn-oath-formulas",
        "title": "The Oath Formula: Esküszöm / Fogadom, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "The Text of the Hungarian Citizenship Oath",
                "content": "The Hungarian Citizenship Oath follows a sacred statutory text: *„Esküszöm, hogy Magyarországot hazámnak tekintem. Magyarországnak hű állampolgára leszek, az Alaptörvényt és a jogszabályokat tiszteletben tartom és megtartom; a hazát erőmhöz mérten megvédem, tehetségem szerint szolgálom. Isten engem úgy segéljen!”* (The secular pledge ends with: *„Becsületemre és lelkiismeretemre fogadom...”*)."
            },
            {
                "type": "examples",
                "title": "Oath formula examples",
                "items": [
                    {"spanish": "Esküszöm, hogy Magyarországot hazámnak tekintem.", "english": "I swear that I consider Hungary my homeland."},
                    {"spanish": "Magyarországnak hű állampolgára leszek, az Alaptörvényt tiszteletben tartom.", "english": "I will be a faithful citizen of Hungary, and I will respect the Fundamental Law."},
                    {"spanish": "A hazát erőmhöz mérten megvédem, és tehetségem szerint szolgálom.", "english": "I will defend the homeland according to my strength, and serve it according to my talents."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allampolgarsag-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.allampolgarsag.05.civic-participation-synthesis",
        "title": "Grand Synthesis of Civic Competence: Felkészült, tisztában van vele",
        "sections": [
            {
                "type": "text",
                "title": "Demonstrating Constitutional Fluency",
                "content": "Graduating through the Hungarian citizenship curriculum signifies full readiness for the exam: *tisztában van a magyar történelem és államszervezet alapjaival* (is aware of the basics of Hungarian history and state organization), *büszkén vállalja az állampolgári felelősséget* (proudly assumes civic responsibility)."
            },
            {
                "type": "examples",
                "title": "Synthesis examples",
                "items": [
                    {"spanish": "A vizsgázó felkészült az alkotmányos alapismeretek sikeres letételére.", "english": "The candidate is prepared for successfully passing the constitutional basics exam."},
                    {"spanish": "Teljes mértékben tisztában vagyok a magyar állampolgárok jogaival és kötelességeivel.", "english": "I am fully aware of the rights and duties of Hungarian citizens."},
                    {"spanish": "Büszkén és felkészülten állok a magyar állampolgársági ceremónia előtt.", "english": "I stand proud and prepared before the Hungarian citizenship ceremony."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allampolgarsag-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized World Stories (5 segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.allampolgarsag.01",
        "title": "A magyar állampolgárság megszerzése és jogi alapjai",
        "level": "B1",
        "lesson": 1,
        "order": 36,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The legal foundation of Hungarian citizenship: the principle of descent (jus sanguinis), naturalization paths, proof of ancestry, and dual citizenship status recognized under Hungarian law.",
        "characters": [],
        "location": "Budapest, Kormányhivatal",
        "grammar": ["Legal Status & Acquisition Valencies: Származás útján, részesül"],
        "vocabularyTopics": ["citizenship", "law", "status"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az állampolgárság a személy és az állam közötti legszorosabb, kölcsönös jogokon és kötelezettségeken alapuló jogi és érzelmi kötelék. Magyarországon az állampolgárságot a törvény a nemzet legfőbb megtartó erejének tekinti."
            },
            {
                "type": "narration",
                "text": "A magyar jogrendszerben a vérségi elv – a jus sanguinis – uralkodik: a gyermek születésével automatikusan magyar állampolgárrá válik, ha születése pillanatában legalább az egyik szülője magyar állampolgár volt, függetlenül attól, hogy a világ melyik pontján jött a világra."
            },
            {
                "type": "narration",
                "text": "Azok számára, akik nem születéssel szerezték meg a köteléket, a jogrendszer a honosítás útját biztosítja. A rendes honosítás mellett az egyszerűsített honosítás lehetővé teszi a magyar származású emberek számára a kedvezményes állampolgárság felvételét."
            },
            {
                "type": "narration",
                "text": "A magyar jogszabályok nem követelik meg a korábbi állampolgárságról való lemondást: Magyarország elismeri és támogatja a kettős vagy többes állampolgárság intézményét."
            },
            {
                "type": "narration",
                "text": "Az állampolgárság megszerzését a köztársasági elnök által aláírt honosítási okirat tanúsítja, amely megnyitja a kaput az új hazába való teljes jogú beilleszkedés előtt."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag-01-megszerzese.json", story_01)

    story_02 = {
        "id": "story.b1.allampolgarsag.02",
        "title": "Alapvető jogok: Választójog, szabadságjogok és emberi méltóság",
        "level": "B1",
        "lesson": 2,
        "order": 36,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Exploring the fundamental constitutional rights of Hungarian citizens: the right to vote in national and European elections, freedoms of speech and assembly, petition rights, and consular protection abroad.",
        "characters": [],
        "location": "Országház és bíróságok",
        "grammar": ["Constitutional Entitlement Syntax: Joga van vmihez & Megilleti"],
        "vocabularyTopics": ["voting", "human_rights", "dignity"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar állampolgárság birtokosát az Alaptörvény által garantált alapvető jogok és szabadságok teljes köre megilleti. Ezek közül kiemelkedik a demokratikus közhatalom gyakorlásában való részvétel joga: a választójog."
            },
            {
                "type": "narration",
                "text": "Minden nagykorú magyar állampolgárnak joga van arra, hogy szavazzon az országgyűlési választásokon, a helyi önkormányzati választásokon, valamint az Európai Parlament képviselőinek megválasztásakor (aktív választójog), és ő maga is jelöltként indulhasson (passzív választójog)."
            },
            {
                "type": "narration",
                "text": "A polgárokat megilleti a véleménynyilvánítás szabadsága, a lelkiismereti és vallásszabadság, valamint a békés gyülekezési és egyesülési jog, amely biztosítja a társadalmi önszerveződést."
            },
            {
                "type": "narration",
                "text": "A polgárok petíciós jogukkal élve egyénileg vagy közösen kérelemmel, panasszal fordulhatnak bármely állami szervhez, és biztosak lehetnek abban, hogy ügyüket méltányosan kivizsgálják."
            },
            {
                "type": "narration",
                "text": "Ha egy magyar állampolgár külföldre utazik, a világ bármely országában számíthat a magyar állam diplomáciai és konzuli védelmére, hiszen a haza nem hagyja magára polgárait."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag-02-jogok.json", story_02)

    story_03 = {
        "id": "story.b1.allampolgarsag.03",
        "title": "Állampolgári kötelességek: A haza védelme és a közös teherviselés",
        "level": "B1",
        "lesson": 3,
        "order": 36,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Understanding constitutional civic duties: paying taxes in proportion to capacity (közteherviselés), national defense obligations, mandatory schooling for children, environmental protection, and obedience to the law.",
        "characters": [],
        "location": "Magyarország",
        "grammar": ["Civic Duty & Obligation Syntax: Kötelessége [Infinitivus], Tartozik"],
        "vocabularyTopics": ["duties", "taxation", "defense"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A jogok és a kötelességek elválaszthatatlan egységet alkotnak egy működő jogállamban. Az állampolgárság nemcsak kiváltságokat, hanem közös felelősségvállalást is jelent a haza és a nemzet jövőjéért."
            },
            {
                "type": "narration",
                "text": "Az egyik legfontosabb polgári kötelesség a közteherviselés: minden állampolgár köteles jövedelmi és vagyoni viszonyaihoz mérten adók és járulékok fizetésével hozzájárulni a közös társadalmi szükségletekhez, mint az egészségügy, oktatás és közbiztonság."
            },
            {
                "type": "narration",
                "text": "A haza védelme minden magyar állampolgár szent kötelessége. Bár békeidőben önkéntes honvédség működik, rendkívüli állapot vagy hadiállapot idején a törvényben meghatározott honvédelmi kötelezettség lép életbe."
            },
            {
                "type": "narration",
                "text": "A társadalom fejlődésének alapja a tankötelezettség: a szülők kötelesek gondoskodni arról, hogy gyermekeik legalább tizenhat éves korukig iskolába járjanak, és művelt, felelős felnőtté váljanak."
            },
            {
                "type": "narration",
                "text": "Végül az Alaptörvény rögzíti a természeti és kulturális értékek megóvásának kötelezettségét, hogy a jövő nemzedékek is tiszta, élhető és szép magyar hazában élhessenek."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag-03-kotelessegek.json", story_03)

    story_04 = {
        "id": "story.b1.allampolgarsag.04",
        "title": "Az állampolgársági eskü és a ceremónia magasztossága",
        "level": "B1",
        "lesson": 4,
        "order": 36,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The emotional pinnacle of naturalization: the solemn citizenship oath administered by the mayor, pledging loyalty to Hungary and the Fundamental Law before the national tricolor while singing the Himnusz.",
        "characters": [],
        "location": "Városháza, Díszterem",
        "grammar": ["The Oath Formula: Esküszöm / Fogadom, hogy..."],
        "vocabularyTopics": ["oath", "ceremony", "loyalty"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A honosítási eljárás legszebb, felejthetetlen pillanata az ünnepélyes állampolgársági eskü vagy fogadalom letétele. A ceremóniára a polgármesteri hivatal dísztermében vagy a magyar külképviseleteken kerül sor."
            },
            {
                "type": "narration",
                "text": "Az eskütétel napján a teremben a piros-fehér-zöld nemzeti lobogó és a Szent Koronával díszített magyar címer fogadja az új polgárokat, ünnepi méltóságot adva a pillanatnak."
            },
            {
                "type": "narration",
                "text": "A polgármester előtt állva a honosított polgárok felemelt kézzel mondják utána a törvényben meghatározott szavakat: „Esküszöm, hogy Magyarországot hazámnak tekintem. Magyarországnak hű állampolgára leszek, az Alaptörvényt és a jogszabályokat tiszteletben tartom és megtartom; a hazát erőmhöz mérten megvédem, tehetségem szerint szolgálom. Isten engem úgy segéljen!”"
            },
            {
                "type": "narration",
                "text": "Az eskü után a jelenlévők közösen éneklik el Kölcsey és Erkel Himnuszát. Ezen a ponton az új állampolgárok átveszik a honosítási okiratot, és a jelenlévők meleg kézfogással gratulálnak nekik."
            },
            {
                "type": "narration",
                "text": "Ettől a szent pillanattól kezdve a kérelmező már nem vendég, hanem a magyar nemzet teljes jogú, büszke tagja, akinek szívében és tetteiben tovább él a magyar hazaszeretet."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag-04-esku.json", story_04)

    story_05 = {
        "id": "story.b1.allampolgarsag.05",
        "title": "A nemzet polgáraként: Felkészülés az állampolgársági vizsgára",
        "level": "B1",
        "lesson": 5,
        "order": 36,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Culminating preparation for the constitutional basics citizenship exam: mastering Hungarian history, institutions, symbols, and culture, and looking forward to an active civic life as a proud Hungarian.",
        "characters": [],
        "location": "Budapest, Vizsgaközpont",
        "grammar": ["Grand Synthesis of Civic Competence: Felkészült, tisztában van vele"],
        "vocabularyTopics": ["exam", "graduation", "civic_life"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar állampolgársági vizsga az alkotmányos alapismeretek alapos elsajátítását követeli meg minden jelölttől. Ez a vizsga nem puszta formaság, hanem annak bizonyítéka, hogy az új polgár érti, tiszteli és magáénak vallja Magyarország értékeit."
            },
            {
                "type": "narration",
                "text": "A kurzus harminchat egységén keresztül a tanuló megismerte a magyar történelem sorsfordító állomásait: a honfoglalást, Szent István államalapítását, a mohácsi vészt, az 1848-as szabadságharcot, az 1956-os forradalmat és a rendszerváltást."
            },
            {
                "type": "narration",
                "text": "Emellett elsajátította az államszervezet felépítését: az Országgyűlés munkáját, a köztársasági elnök szerepét, a Kormány működését, a bíróságok függetlenségét és a helyi önkormányzatok világát."
            },
            {
                "type": "narration",
                "text": "Megtanulta a nemzeti jelképek – a Szent Korona, a címer, a Himnusz és a trikolór – szent jelentését, és tisztában van a magyar tudomány és kultúra világhírű értékeivel."
            },
            {
                "type": "narration",
                "text": "A vizsgabizottság előtt álló polgár most már büszkén és magabiztosan mondhatja el magyarul: készen állok arra, hogy a magyar hazát hűséggel, szorgalommal és szeretettel szolgáljam egy életen át!"
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag-05-vizsga.json", story_05)

    story_combined = {
        "id": "story.b1.allampolgarsag",
        "title": "Állampolgárság, alkotmányos jogok és az állampolgársági eskü",
        "level": "B1",
        "order": 36,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "The ultimate grand compendium of the Hungarian Citizenship curriculum: legal bases of citizenship, constitutional rights and duties, the solemn text of the citizenship oath, and full readiness for the citizenship exam.",
        "characters": [],
        "location": "Magyarország",
        "grammar": [
            "Legal Status & Acquisition Valencies: Származás útján, részesül",
            "Constitutional Entitlement Syntax: Joga van vmihez & Megilleti",
            "Civic Duty & Obligation Syntax: Kötelessége [Infinitivus], Tartozik",
            "The Oath Formula: Esküszöm / Fogadom, hogy...",
            "Grand Synthesis of Civic Competence: Felkészült, tisztában van vele"
        ],
        "vocabularyTopics": [
            "citizenship",
            "rights",
            "duties",
            "oath",
            "constitution"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A magyar állampolgárság megszerzése és megélése a legmagasztosabb kötelék az egyén és a magyar nemzet között. Magyarország Alaptörvénye és törvényei szilárd jogi keretet és otthont biztosítanak minden polgárnak."
            },
            {
                "type": "narration",
                "text": "A vérségi elv és a honosítási eljárások révén a nemzet kapui nyitva állnak azok előtt, akik származásuk, házasságuk vagy elköteleződésük révén a magyarság nagy családjához kívánnak tartozni."
            },
            {
                "type": "narration",
                "text": "Az állampolgárokat megilleti a választójog, a szólásszabadság, a gyülekezési jog és az emberi méltóság sérthetetlensége, miközben a közteherviselés, a honvédelem és a környezetvédelem kötelessége biztosítja a közösség fennmaradását."
            },
            {
                "type": "narration",
                "text": "Az ünnepélyes állampolgársági eskü szavai: „Esküszöm, hogy Magyarországot hazámnak tekintem...” egy életre szóló szent ígéretet jelentenek a hűségre, a törvénytiszteletre és a haza szolgálatára."
            },
            {
                "type": "narration",
                "text": "A B1-es tananyag és az alkotmányos alapismeretek sikeres elsajátításával a tanuló készen áll arra, hogy a vizsgabizottság előtt letegye a vizsgát, megkapja a magyar állampolgárságot, és büszkén éljen az új, szabad magyar hazában."
            }
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allampolgarsag.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-allampolgarsag-01",
        "exercises": [
            {
                "id": "b1-allampolgarsag-01.ex01",
                "type": "multiple-choice",
                "category": "law",
                "question": "Melyik elv alapján keletkezik a magyar állampolgárság születéssel?",
                "options": [
                    "A vérségi elv (jus sanguinis) alapján: ha legalább az egyik szülő magyar",
                    "Kizárólag a terület elve alapján: csak annak jár, aki Magyarországon született",
                    "A születési kórház vezetőjének egyedi döntése alapján"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kérelmező kedvezményes honosítás_____ részesülhet. (in naturalization - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-allampolgarsag-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "jog", "elismeri", "a", "kettős", "állampolgárságot."],
                "solution": ["A", "magyar", "jog", "elismeri", "a", "kettős", "állampolgárságot."]
            },
            {
                "id": "b1-allampolgarsag-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik hivatalos okirat tanúsítja a sikeres honosítást?",
                "options": [
                    "A honosítási okirat",
                    "A lakcímkártya",
                    "A gépjárművezetői engedély"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A felmenők magyar származásá_____ hivatalos dokumentumokkal kell igazolni. (ancestry - t)",
                "answer": "t"
            },
            {
                "id": "b1-allampolgarsag-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Ki írja alá a honosítási okiratot Magyarországon?",
                "options": [
                    "A köztársasági elnök",
                    "A helyi rendőrkapitány",
                    "A legfelsőbb bíró"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "állampolgársági", "bizonyítvány", "igazolja", "a", "jogállást."],
                "solution": ["Az", "állampolgársági", "bizonyítvány", "igazolja", "a", "jogállást."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-allampolgarsag-02",
        "exercises": [
            {
                "id": "b1-allampolgarsag-02.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelent az 'aktív választójog'?",
                "options": [
                    "A választásokon való szavazás jogát",
                    "A sportegyesületi tagságot",
                    "A választásokon jelöltként való indulást"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden nagykorú magyar állampolgárt megill_____ a választójog. (is entitled - eti)",
                "answer": "eti"
            },
            {
                "id": "b1-allampolgarsag-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "polgároknak", "joguk", "van", "a", "békés", "gyülekezéshez."],
                "solution": ["A", "polgároknak", "joguk", "van", "a", "békés", "gyülekezéshez."]
            },
            {
                "id": "b1-allampolgarsag-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen jogot biztosít a petíciós jog a polgárok számára?",
                "options": [
                    "Kérelemmel vagy panasszal fordulhatnak az állami hatóságokhoz",
                    "Ingyenes utazást az ország egész területén",
                    "Mentességet a szabálysértési bírságok alól"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az emberi méltóság sérthetetlen minden ember számá_____. (for - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-allampolgarsag-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kik szavazhatnak az Európai Parlament magyar képviselőire?",
                "options": [
                    "A választójoggal rendelkező magyar állampolgárok és az EU Magyarországon élő polgárai",
                    "Kizárólag az egyetemi tanárok",
                    "Csak azok, akik Brüsszelben dolgoznak"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "véleménynyilvánítás", "szabadsága", "alapvető", "alkotmányos", "jog."],
                "solution": ["A", "véleménynyilvánítás", "szabadsága", "alapvető", "alkotmányos", "jog."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-allampolgarsag-03",
        "exercises": [
            {
                "id": "b1-allampolgarsag-03.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelent a 'közteherviselés' alkotmányos kötelezettsége?",
                "options": [
                    "Adók és járulékok fizetését a jövedelmi viszonyoknak megfelelően",
                    "A közösségi közlekedési eszközök takarítását",
                    "A szomszédok csomagjainak kötelező cipelését"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden állampolgár kötelessége a természeti környezet megóvás_____. (preservation - a)",
                "answer": "a"
            },
            {
                "id": "b1-allampolgarsag-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "haza", "védelme", "minden", "magyar", "állampolgár", "kötelessége."],
                "solution": ["A", "haza", "védelme", "minden", "magyar", "állampolgár", "kötelessége."]
            },
            {
                "id": "b1-allampolgarsag-03.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Hány éves korig tart a kötelező iskoláztatás (tankötelezettség) Magyarországon?",
                "options": [
                    "16 éves korig",
                    "12 éves korig",
                    "21 éves korig"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A jogszabályok betartása és a törvénytisztelet elengedhetet_____. (indispensable - len)",
                "answer": "len"
            },
            {
                "id": "b1-allampolgarsag-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mire kötelezi a szülőket az Alaptörvény a gyermekeikkel kapcsolatban?",
                "options": [
                    "Gondoskodniuk kell kiskorú gyermekeik neveléséről és taníttatásáról",
                    "Minden gyermeknek zenei pályát kell választania",
                    "A gyermekeknek 14 évesen munkába kell állniuk"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "jogok", "és", "a", "kötelességek", "egyensúlyban", "vannak."],
                "solution": ["A", "jogok", "és", "a", "kötelességek", "egyensúlyban", "vannak."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-allampolgarsag-04",
        "exercises": [
            {
                "id": "b1-allampolgarsag-04.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan kezdődik az ünnepélyes magyar állampolgársági eskü?",
                "options": [
                    "Esküszöm, hogy Magyarországot hazámnak tekintem...",
                    "Ígérem, hogy sokat fogok utazni...",
                    "Kijelentem, hogy tetszik a magyar időjárás..."
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Magyarországnak hű állampolgára lesz_____, az Alaptörvényt tiszteletben tartom. (I will be - ek)",
                "answer": "ek"
            },
            {
                "id": "b1-allampolgarsag-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hazát", "erőmhöz", "mérten", "megvédem,", "tehetségem", "szerint", "szolgálom."],
                "solution": ["A", "hazát", "erőmhöz", "mérten", "megvédem,", "tehetségem", "szerint", "szolgálom."]
            },
            {
                "id": "b1-allampolgarsag-04.ex04",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hol tehető le a magyar állampolgársági eskü?",
                "options": [
                    "A polgármesteri hivatalban a polgármester előtt, vagy a magyar külképviseleteken",
                    "A postahivatalban a postáskisasszony előtt",
                    "Online videojátékon keresztül"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az ünnepélyes ceremónián eléneklik a magyar nemzeti Himnusz_____. (Anthem - t)",
                "answer": "t"
            },
            {
                "id": "b1-allampolgarsag-04.ex06",
                "type": "multiple-choice",
                "category": "law",
                "question": "Miben különbözik az állampolgársági fogadalom az eskütől?",
                "options": [
                    "A fogadalom világi szövegű, és nem tartalmazza az 'Isten engem úgy segéljen' záradékot",
                    "A fogadalom után kevesebb adót kell fizetni",
                    "A fogadalmat csak gyerekek tehetik le"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-04.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hazaszeretet", "és", "a", "hűség", "összeköti", "a", "nemzetet."],
                "solution": ["A", "hazaszeretet", "és", "a", "hűség", "összeköti", "a", "nemzetet."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-allampolgarsag-05",
        "exercises": [
            {
                "id": "b1-allampolgarsag-05.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit mér fel az állampolgársági vizsga alkotmányos alapismeretek része?",
                "options": [
                    "A magyar történelem, államszervezet, jelképek és Alaptörvény ismeretét",
                    "A magyar labdarúgó-bajnokság eredményeit",
                    "A budapesti metróállomások mélységét méterben"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vizsgázó felkészült az állampolgársági vizsga sikeres letételé_____. (taking - re)",
                "answer": "re"
            },
            {
                "id": "b1-allampolgarsag-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Büszkén", "vállalom", "az", "állampolgári", "felelősséget", "és", "kötelezettségeket."],
                "solution": ["Büszkén", "vállalom", "az", "állampolgári", "felelősséget", "és", "kötelezettségeket."]
            },
            {
                "id": "b1-allampolgarsag-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'demokratikus részvétel' a gyakorlatban?",
                "options": [
                    "Részvételt a választásokon, a civil szervezetekben és a közügyek alakításában",
                    "Kizárólag a televíziós hírek megtekintését",
                    "A politikai témák teljes elkerülését"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A társadalmi szolidaritás erősíti az összetartozás érzés_____. (feeling - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-allampolgarsag-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik állítás fejezi ki a sikeres B1 és állampolgársági kurzus befejezését?",
                "options": [
                    "Magyarország hű polgáraként büszkén beszélem a nyelvet és ismerem a nemzet történelmét!",
                    "Csak véletlenül jártam ezen az órán.",
                    "Semmit sem értek az államszervezetből."
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magyar", "nemzet", "közössége", "szeretettel", "fogadja", "új", "polgárait."],
                "solution": ["A", "magyar", "nemzet", "közössége", "szeretettel", "fogadja", "új", "polgárait."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-allampolgarsag-consolidation",
        "exercises": [
            {
                "id": "b1-allampolgarsag-consolidation.ex01",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik mondat idézi pontosan az állampolgársági eskü központi kötelezettségvállalását?",
                "options": [
                    "„...az Alaptörvényt és a jogszabályokat tiszteletben tartom és megtartom; a hazát erőmhöz mérten megvédem...”",
                    "„...ígérem, hogy mindig egyetértek a kormánnyal mindenben...”",
                    "„...soha többé nem utazom külföldre...”"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A sikeres állampolgársági eskü után átveszem a honosítási okirat_____. (document - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Esküszöm,", "hogy", "Magyarországot", "hazámnak", "tekintem."],
                "solution": ["Esküszöm,", "hogy", "Magyarországot", "hazámnak", "tekintem."]
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex04",
                "type": "multiple-choice",
                "category": "law",
                "question": "Milyen jogok illetik meg a magyar állampolgárokat?",
                "options": [
                    "Választójog, gyülekezési jog, petíciós jog, véleménynyilvánítás szabadsága és konzuli védelem",
                    "Kizárólag a magyar zászló használatának joga",
                    "Csak adófizetési jogok jogorvoslat nélkül"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az alkotmányos alapismeretek elsajátítása a sikeres vizsga alapj_____. (its basis - a)",
                "answer": "a"
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelképez a Szent István király által megalapozott ezeréves magyar államiság?",
                "options": [
                    "A magyar nemzet európai, keresztény és demokratikus történelmi folytonosságát",
                    "Egy rövid, jelentéktelen korszakot",
                    "Kizárólag egy régi pénzérme nevét"
                ],
                "correct": 0
            },
            {
                "id": "b1-allampolgarsag-consolidation.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Isten", "áldd", "meg", "a", "magyart", "jó", "kedvvel,", "bőséggel!"],
                "solution": ["Isten", "áldd", "meg", "a", "magyart", "jó", "kedvvel,", "bőséggel!"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allampolgarsag-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.allampolgarsag-01",
        "unit": 36,
        "title": "A magyar állampolgárság megszerzése és jogi alapjai",
        "level": "B1",
        "grammar": "Legal Status & Acquisition Valencies: Származás útján, részesül",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain how Hungarian citizenship is acquired by birth (jus sanguinis) and naturalization.",
                    "I can use legal acquisition valencies like származás útján and honosításban részesül.",
                    "I can master 6 essential terms for citizenship certificate, status, and dual nationality.",
                    "I can read the world story about the legal foundations of Hungarian citizenship."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-allampolgarsag-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-allampolgarsag-01-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag-01-megszerzese.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-allampolgarsag-01-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-01.ex01",
                    "b1-allampolgarsag-01.ex02",
                    "b1-allampolgarsag-01.ex03",
                    "b1-allampolgarsag-01.ex04",
                    "b1-allampolgarsag-01.ex05",
                    "b1-allampolgarsag-01.ex06",
                    "b1-allampolgarsag-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.allampolgarsag-02",
        "unit": 36,
        "title": "Alapvető jogok: Választójog, szabadságjogok és emberi méltóság",
        "level": "B1",
        "grammar": "Constitutional Entitlement Syntax: Joga van vmihez & Megilleti",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can articulate fundamental constitutional rights (voting, petition, peaceful assembly).",
                    "I can construct entitlement sentences using joga van vmihez and megilleti a szabadság.",
                    "I can learn 6 words for suffrage, democratic petitioning, and human dignity.",
                    "I can understand the active and passive voting rights of Hungarian citizens."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-allampolgarsag-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-allampolgarsag-02-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag-02-jogok.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-allampolgarsag-02-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-02.ex01",
                    "b1-allampolgarsag-02.ex02",
                    "b1-allampolgarsag-02.ex03",
                    "b1-allampolgarsag-02.ex04",
                    "b1-allampolgarsag-02.ex05",
                    "b1-allampolgarsag-02.ex06",
                    "b1-allampolgarsag-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.allampolgarsag-03",
        "unit": 36,
        "title": "Állampolgári kötelességek: A haza védelme és a közös teherviselés",
        "level": "B1",
        "grammar": "Civic Duty & Obligation Syntax: Kötelessége [Infinitivus], Tartozik",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain constitutional duties: public taxation (közteherviselés), defense, and schooling.",
                    "I can express legal obligations using kötelessége [infinitivus] and felelősséggel tartozik.",
                    "I can acquire 6 vocabulary terms for civic responsibilities and respect for the law.",
                    "I can discuss environmental protection and parental duties under the Fundamental Law."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-allampolgarsag-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-allampolgarsag-03-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag-03-kotelessegek.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-allampolgarsag-03-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-03.ex01",
                    "b1-allampolgarsag-03.ex02",
                    "b1-allampolgarsag-03.ex03",
                    "b1-allampolgarsag-03.ex04",
                    "b1-allampolgarsag-03.ex05",
                    "b1-allampolgarsag-03.ex06",
                    "b1-allampolgarsag-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.allampolgarsag-04",
        "unit": 36,
        "title": "Az állampolgársági eskü és a ceremónia magasztossága",
        "level": "B1",
        "grammar": "The Oath Formula: Esküszöm / Fogadom, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can recite and comprehend the solemn text of the Hungarian Citizenship Oath.",
                    "I can distinguish between the oath (eskü) and the pledge (fogadalom).",
                    "I can master 6 words for solemn ceremonies, loyalty, and mayoral administration.",
                    "I can experience the emotional solemnity of the naturalization ceremony."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-allampolgarsag-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-allampolgarsag-04-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag-04-esku.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-allampolgarsag-04-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-04.ex01",
                    "b1-allampolgarsag-04.ex02",
                    "b1-allampolgarsag-04.ex03",
                    "b1-allampolgarsag-04.ex04",
                    "b1-allampolgarsag-04.ex05",
                    "b1-allampolgarsag-04.ex06",
                    "b1-allampolgarsag-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.allampolgarsag-05",
        "unit": 36,
        "title": "A nemzet polgáraként: Felkészülés az állampolgársági vizsgára",
        "level": "B1",
        "grammar": "Grand Synthesis of Civic Competence: Felkészült, tisztában van vele",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can synthesize all constitutional basics required for the Hungarian citizenship exam.",
                    "I can express full civic readiness using felkészült and tisztában van vele.",
                    "I can acquire 6 words for democratic participation, solidarity, and civic commitment.",
                    "I can look forward with confidence to life as a naturalized Hungarian citizen."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-allampolgarsag-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-allampolgarsag-05-gr.json"},
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag-05-vizsga.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-allampolgarsag-05-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-05.ex01",
                    "b1-allampolgarsag-05.ex02",
                    "b1-allampolgarsag-05.ex03",
                    "b1-allampolgarsag-05.ex04",
                    "b1-allampolgarsag-05.ex05",
                    "b1-allampolgarsag-05.ex06",
                    "b1-allampolgarsag-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.allampolgarsag-consolidation",
        "unit": 36,
        "title": "B1 Citizenship Capstone: Állampolgárság és alkotmányos alapismeretek",
        "level": "B1",
        "grammar": "Grand capstone synthesis of the entire 36-unit Hungarian citizenship curriculum",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Consolidate all 30 capstone vocabulary items on citizenship, constitutional rights, duties, and the oath.",
                    "Synthesize all historical, institutional, and constitutional knowledge across Units 1–36.",
                    "Read the grand compendium on Hungarian citizenship and the solemn oath.",
                    "Graduate with honors from the Hungarian B1 Citizenship Curriculum, fully prepared for the citizenship exam!"
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-allampolgarsag.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-allampolgarsag-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-allampolgarsag-consolidation.ex01",
                    "b1-allampolgarsag-consolidation.ex02",
                    "b1-allampolgarsag-consolidation.ex03",
                    "b1-allampolgarsag-consolidation.ex04",
                    "b1-allampolgarsag-consolidation.ex05",
                    "b1-allampolgarsag-consolidation.ex06",
                    "b1-allampolgarsag-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allampolgarsag-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_36_citizenship()
