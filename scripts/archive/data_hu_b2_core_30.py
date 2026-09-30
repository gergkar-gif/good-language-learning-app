"""
Hungarian B2 Core Track Unit 30:
  b2-30: Civic Participation, Advocacy & Public Institutions
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_30 = {
    "unit_num": 30,
    "title": "Civic Participation, Advocacy & Public Institutions",
    "grammar_summary": "Abstract case government in institutional and civic Hungarian (-hoz/-hez/-höz, -tól/-től, -ra/-re, -ról/-ről, ellen), official complaint procedures, public inquiries, and advocacy rhetoric.",
    "grammar_skill": "b2-abstract-case-government",
    "vocab_skill": "b2-30-vocab",
    "theme": "Civic participation, advocacy and public institutions",
    "intro_body": [
        "A demokratikus jogállamban a polgárok és a közintézmények kapcsolata a precíz, formalizált nyelvezeten alapul. Az állampolgári érdekérvényesítés, az ombudsmani beadványok és a civil petíciók megfogalmazásakor elengedhetetlen a hivatalos stílus és az elvont igevonzatok magabiztos használata.",
        "Ebben a fejezetben részletesen elsajátíthatja a közigazgatásban leggyakoribb elvont vonzatos igéket (hozzájárul vmihez, ragaszkodik vmihez, eltekint vmitől, tartózkodik vmitől, hivatkozik vmire, kitér vmire, beszámol vmiről, meggyőződik vmiről), megtanulhat hivatalos panaszt és fellebbezést írni, valamint nyilvános vitát vezetni. Mikszáth Kálmán 'Különös házasság' című remekműve pedig a jogi és intézményi önkénnyel szembeni küzdelem örök dilemmáit mutatja be.",
    ],
    "classic_story": {
        "slug": "kulonoshazassag",
        "author": "Mikszáth Kálmán",
        "work": "Különös házasság (1900)",
        "title": "Buttler János pere az intézményi önkény ellen",
        "summary": "Buttler János gróf az egyházi és világi hatóságok cinkosságával ráerőszakolt házasság érvénytelenítéséért küzd, miközben ügyvédjével a jogi eljárás és a hivatali közöny buktatóit mérlegelik.",
        "characters": ["Buttler János gróf", "Az ügyvéd"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesti ügyvédi iroda poros polcain törvénykönyvek és periratok sorakoztak a mennyezetig. Buttler János gróf feszülten ült a kopott bőrfotelben; fiatal arcán a megaláztatás fájdalma és a dacos elszántság küzdött egymással a délutáni homályban.",
            },
            {
                "type": "dialogue",
                "speaker": "Az ügyvéd",
                "text": "Gróf úr, az egyházi törvényszék ismét elutasította a perújítási kérelmünket. Ragaszkodnak a formai előírásokhoz, és makacsul eltekintenek a kényszerítés egyértelmű tanúvallomásaitól.",
            },
            {
                "type": "dialogue",
                "speaker": "Buttler János gróf",
                "text": "Hogyan tekinthetnek el a nyilvánvaló bűnténytől? Engem fegyveres pandúrokkal vonszoltak az oltár elé! Nem fogok belenyugodni ebbe a gyalázatba; ragaszkodom a jogaimhoz, és fellebbezni fogunk a legfelsőbb világi bírósághoz!",
            },
            {
                "type": "narration",
                "text": "Az ügyvéd levette ezüstkeretes szemüvegét, és komoran sóhajtott. Jól tudta, hogy a hatalmas Dőry báró összeköttetései és az intézményi hálózat cinkossága szinte áthatolhatatlan falat képez az egyszerű jogkereső ember előtt.",
            },
            {
                "type": "dialogue",
                "speaker": "Az ügyvéd",
                "text": "A fellebbezés során kénytelenek leszünk szigorúan a törvény betűjére hivatkozni, és részletesen beszámolni a vizsgálóbiztos eljárási visszaéléseiről. Ám fel kell készülnie arra, hogy a hatóságok megpróbálják elhúzni az ügyet, amíg csak bele nem fárad.",
            },
            {
                "type": "dialogue",
                "speaker": "Buttler János gróf",
                "text": "Semmitől sem tartózkodom, ami az igazságomat bizonyítja. Meggyőződtem arról, hogy a hatalom csak akkor hátrál meg, ha a nyilvánosság erejével kényszerítjük rá a jogszerű eljárásra.",
            },
            {
                "type": "narration",
                "text": "A lemenő nap fénye megvilágította az asztalon heverő hivatalos pecséteket és a grófi címeres papírokat. Az ügyvéd tollat ragadott, és gondosan szerkesztett mondatokkal látott munkához, ügyelve arra, hogy a beadvány minden egyes szava kikezdhetetlen legyen a jogászok előtt.",
            },
            {
                "type": "narration",
                "text": "Buttler felállt, és kinézett az ablakon a Duna felé. Megértette, hogy magányos küzdelme már nem pusztán egy szerencsétlen házasságról szólt, hanem az állampolgári méltóság és az intézményi önkény örök háborújáról.",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért utasította el az egyházi bíróság Buttler János kérelmét a szöveg szerint?",
                "options": [
                    "Mert mereven ragaszkodtak a formai előírásokhoz, és eltekintettek a kényszerítés vizsgálatától.",
                    "Mert Buttler elmulasztotta befizetni az illetéket a határidő lejárta előtt.",
                    "Mert a gróf ügyvédje elfelejtette benyújtani a tanúk listáját a bíróságnak.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen jogorvoslati stratégiát javasol az ügyvéd a további lépésekre?",
                "options": [
                    "A törvény betűjére hivatkoznak, és részletesen beszámolnak az eljárási visszaélésekről.",
                    "Azonnal feladják a küzdelmet, és elfogadják a házasság érvényességét.",
                    "Elhagyják az országot, és soha többé nem fordulnak semmilyen bírósághoz.",
                ],
                "correct": 0,
            },
            {
                "question": "Mire döbbent rá Buttler gróf a per elhúzódása során?",
                "options": [
                    "Hogy a hatalommal szemben a kitartó küzdelem és a nyilvánosság ereje hozhat jogszerű döntést.",
                    "Hogy az egyházi intézmények mindig a leggyorsabban és legigazságosabban járnak el.",
                    "Hogy egy ügyvéd felfogadása teljesen felesleges pénzkidobás.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "High-Frequency Abstract Verbs + -hoz/-hez/-höz and -tól/-től",
            "grammar_label": "Verbal government: hozzájárul (-hoz), ragaszkodik (-hoz), eltekint (-tól), tartózkodik (-tól)",
            "goals": [
                "I can use allative-governing verbs like hozzájárul and ragaszkodik in institutional contexts",
                "I can use ablative-governing verbs like eltekint and tartózkodik to express abstention and waiver",
                "I can discuss legal remedy (jogorvoslat) using precise formal case governance",
            ],
            "grammar_doc": {
                "slug": "abstract-verbs-allative-ablative",
                "title": "Abstract Verbs Governing Allative (-hoz/-hez/-höz) and Ablative (-tól/-től)",
                "text1_title": "Attachment and Insistence: hozzájárul and ragaszkodik (+ -hoz/-hez/-höz)",
                "text1": "In Hungarian public and legal administration, verbs expressing adherence, assent, or contribution require the allative case suffix (-hoz/-hez/-höz). 'Ragaszkodik vmihez' denotes unyielding insistence on rights, rules, or standards: 'Ragaszkodik a törvényes eljáráshoz' (He insists on lawful procedure). 'Hozzájárul vmihez' signifies providing official consent or contributing to a collective outcome: 'A hatóság hozzájárul a kérelem teljesítéséhez.'",
                "text2_title": "Separation, Waiver, and Abstention: eltekint and tartózkodik (+ -tól/-től)",
                "text2": "Conversely, verbs denoting procedural waiver, omission, or self-restraint govern the ablative case (-tól/-től). 'Eltekint vmitől' expresses formally waiving a penalty, requirement, or formal defect: 'A hivatal eltekint a bírság kiszabásától' (The office waives the imposition of the fine). 'Tartózkodik vmitől' signifies abstaining from an action, statement, or voting: 'A képviselő tartózkodott a szavazástól' (The representative abstained from the vote).",
                "table_title": "Allative vs. Ablative Government Matrix",
                "table_rows": [
                    ["ragaszkodik (+ -hoz/-hez/-höz)", "Ragaszkodnak a határidőkhöz. (They insist on the deadlines.)"],
                    ["hozzájárul (+ -hoz/-hez/-höz)", "Nem járul hozzá az adatai kezeléséhez. (Does not consent to data processing.)"],
                    ["eltekint (+ -tól/-től)", "Eltekintenek a pótdíj megfizetésétől. (They waive payment of the surcharge.)"],
                    ["tartózkodik (+ -tól/-től)", "Tartózkodik a politikai véleménynyilvánítástól. (Refrains from political statements.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az állampolgár határozottan ragaszkodik az alaptörvényben biztosított jogaihoz.",
                        "english": "The citizen firmly insists on his rights guaranteed in the constitution.",
                    },
                    {
                        "spanish": "A polgármesteri hivatal nem járult hozzá a zöldterület átminősítéséhez.",
                        "english": "The mayor's office did not consent to the reclassification of the green area.",
                    },
                    {
                        "spanish": "Méltányosságból a hatóság eltekintett az eljárási illeték beszedésétől.",
                        "english": "Out of equity, the authority waived collection of the procedural fee.",
                    },
                    {
                        "spanish": "A vizsgálat lezárultáig a tisztségviselők kötelesek tartózkodni minden nyilvános nyilatkozattól.",
                        "english": "Until the conclusion of the inquiry, officials are obliged to refrain from any public statement.",
                    },
                ],
                "tip": "When a governed verb introduces a subordinate clause, use the correlating demonstrative: 'Ragaszkodik ahhoz, hogy...', 'Eltekint attól, hogy...'.",
            },
            "words": [
                {"lemma": "hozzájárul", "translation": "to contribute to / consent to (-hoz/-hez/-höz)", "pos": "verb"},
                {"lemma": "ragaszkodik", "translation": "to insist on / cling to (-hoz/-hez/-höz)", "pos": "verb"},
                {"lemma": "eltekint", "translation": "to disregard / waive (-tól/-től)", "pos": "verb"},
                {"lemma": "tartózkodik", "translation": "to refrain from / abstain (-tól/-től)", "pos": "verb"},
                {"lemma": "jogorvoslat", "translation": "legal remedy / redress", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which case suffix is governed by 'ragaszkodik' in formal Hungarian?",
                        ["allative (-hoz/-hez/-höz)", "sublative (-ra/-re)", "ablative (-tól/-től)"],
                        0,
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'jogorvoslat' in legal and administrative disputes?",
                        [
                            "the legal right and procedure to challenge an unlawful or contested authority decision",
                            "a medical prescription provided to elderly court witnesses",
                            "a formal apology issued by a defendant in criminal court",
                        ],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["hozzájárul", "to consent / contribute to (-hoz)"],
                            ["ragaszkodik", "to insist on (-hoz)"],
                            ["eltekint", "to waive / disregard (-tól)"],
                            ["tartózkodik", "to abstain / refrain from (-tól)"],
                            ["jogorvoslat", "legal remedy / redress"],
                        ],
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix governed by 'eltekint': 'A hatóság méltányosságból eltekintett a bírság____.'",
                        ["-tól", "-hoz", "-re"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix completes 'ragaszkodik': 'Az ügyfél ragaszkodott a jegyzőkönyv felvételé____'?",
                        ["-hez", "-től", "-ért"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A képviselő-testület több tagja ____ a szavazástól a személyi kérdésben. (abstained)",
                        "tartózkodott",
                        "Several members of the municipal council abstained from voting on the personnel question.",
                        ["b2-abstract-case-government"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A minisztérium nem járult ____ a vitatott beruházás környezetvédelmi engedélyéhez. (did not consent)",
                        "hozzá",
                        "The ministry did not consent to the environmental permit of the contested investment.",
                        ["b2-abstract-case-government"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "polgár", "jogosult", "a", "hatékony", "jogorvoslat", "igénybevételére."],
                        ["A", "polgár", "jogosult", "a", "hatékony", "jogorvoslat", "igénybevételére."],
                        "The citizen is entitled to the use of effective legal remedy.",
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az állampolgár határozottan ____ a törvényes eljárás betartásához. (insists)",
                        "ragaszkodik",
                        "The citizen firmly insists on the observance of lawful procedure.",
                        ["b2-30-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "bíróság", "eltekintett", "az", "eljárási", "költségek", "megfizetésétől."],
                        ["A", "bíróság", "eltekintett", "az", "eljárási", "költségek", "megfizetésétől."],
                        "The court waived payment of the procedural costs.",
                        ["b2-30-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyfél", "text": "Kérhetem-e, hogy tekintsenek el a késedelmi pótlék megfizetésétől?"},
                            {"speaker": "Hivatali ügyintéző", "text": "____"},
                        ],
                        [
                            "Igen, méltányossági kérelmet nyújthat be, és a hivatal eltekinthet a pótléktól, ha igazolja a rendkívüli körülményeket.",
                            "A hivatalban tilos eltekinteni bármitől, ezért azonnal börtönbe kell vonulnia.",
                            "Nem tudjuk, mit jelent az eltekintés, mert nincs nálunk szótár.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Civil aktivista", "text": "Mi a teendő, ha a hatóság nem járul hozzá a közérdekű adatok kiadásához?"},
                            {"speaker": "Jogvédő", "text": "____"},
                        ],
                        [
                            "Ragaszkodnunk kell a jogainkhoz, és jogorvoslattal élve pert indíthatunk az adatok közzétételéért.",
                            "Nyugodjunk bele a döntésbe, és soha többé ne kérdezzünk semmit az intézményektől.",
                            "A hozzájárulás automatikus mindenhol a világon, nem kell semmit tenni.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'ragaszkodik' (+ -hoz/-hez/-höz) to assert a citizen's procedural right.",
                                "answer": "A panaszos határozottan ragaszkodik ahhoz, hogy a hatóság írásban indokolja meg a döntését.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'eltekint' (+ -tól/-től) in an official administrative context.",
                                "answer": "A hatóság a körülmények alapos mérlegelése után eltekintett a szabálysértési bírság kiszabásától.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A tisztviselők kötelesek ____ minden olyan tevékenységtől, amely összeférhetetlen a hivatali eskükkel. (to refrain)",
                        "tartózkodni",
                        "Officials are obliged to refrain from any activity that is incompatible with their official oath.",
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which verb requires the ablative case (-tól/-től) to express waiving a requirement?",
                        ["eltekint", "ragaszkodik", "hozzájárul"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "High-Frequency Abstract Verbs + -ra/-re and -ról/-ről",
            "grammar_label": "Verbal government: hivatkozik (-ra), kitér (-ra), beszámol (-ról), meggyőződik (-ról)",
            "goals": [
                "I can use sublative-governing verbs like hivatkozik and kitér to cite regulations and touch upon issues",
                "I can use delative-governing verbs like beszámol and meggyőződik to report on and verify facts",
                "I can draft an administrative petition (beadvány) applying these governed verbs correctly",
            ],
            "grammar_doc": {
                "slug": "abstract-verbs-sublative-delative",
                "title": "Abstract Verbs Governing Sublative (-ra/-re) and Delative (-ról/-ről)",
                "text1_title": "Citation and Focus: hivatkozik and kitér (+ -ra/-re)",
                "text1": "Verbs pointing towards an authority, legal precedent, statutory article, or specific sub-topic govern the sublative case (-ra/-re). 'Hivatkozik vmire' (to refer to / cite / invoke) grounds claims in established law: 'A kérelmező az eljárási törvény 15. szakaszára hivatkozik.' 'Kitér vmire' (to touch upon / address) directs focus toward an issue: 'A jelentés külön kitért a környezeti kockázatokra.'",
                "text2_title": "Reporting and Verification: beszámol and meggyőződik (+ -ról/-ről)",
                "text2": "Conversely, verbs dealing with comprehensive accounts of events or empirical verification govern the delative case (-ról/-ről). 'Beszámol vmiről' denotes rendering a structured official report: 'Az ombudsman beszámolt a vizsgálat megállapításairól.' 'Meggyőződik vmiről' denotes verifying facts firsthand to arrive at certainty: 'A felügyelő a helyszínen győződött meg a szabályok betartásáról.'",
                "table_title": "Sublative vs. Delative Government Matrix",
                "table_rows": [
                    ["hivatkozik (+ -ra/-re)", "A jogszabályra hivatkozik. (Invokes the statute.)"],
                    ["kitér (+ -ra/-re)", "Kitért a panasz részleteire. (Touched upon complaint details.)"],
                    ["beszámol (+ -ról/-ről)", "Beszámolt a vizsgálat eredményéről. (Reported on the investigation.)"],
                    ["meggyőződik (+ -ról/-ről)", "Meggyőződött a tényekről. (Convinced oneself of / verified facts.)"],
                ],
                "examples": [
                    {
                        "spanish": "A beadvány megfogalmazásakor a jogász a legfrissebb bírósági határozatokra hivatkozott.",
                        "english": "When formulating the petition, the lawyer cited the most recent court rulings.",
                    },
                    {
                        "spanish": "Az éves közmeghallgatáson a polgármester részletesen kitért a költségvetés hiányára.",
                        "english": "At the annual public hearing, the mayor touched in detail upon the budget deficit.",
                    },
                    {
                        "spanish": "A bizottság elnöke a sajtótájékoztatón számolt be a feltárt szabálytalanságokról.",
                        "english": "The committee chair reported on the uncovered irregularities at the press conference.",
                    },
                    {
                        "spanish": "A hatóság képviselője személyesen győződött meg az intézmény akadálymentesítéséről.",
                        "english": "The authority's representative personally made sure of the institution's accessibility.",
                    },
                ],
                "tip": "Watch the correlating demonstrative forms: 'Hivatkozik arra, hogy...' (-ra), versus 'Meggyőződik arról, hogy...' (-ról).",
            },
            "words": [
                {"lemma": "hivatkozik", "translation": "to refer to / cite (-ra/-re)", "pos": "verb"},
                {"lemma": "kitér", "translation": "to touch upon / mention (-ra/-re)", "pos": "verb"},
                {"lemma": "beszámol", "translation": "to report on / give account of (-ról/-ről)", "pos": "verb"},
                {"lemma": "meggyőződik", "translation": "to make sure of / verify (-ról/-ről)", "pos": "verb"},
                {"lemma": "beadvány", "translation": "petition / submission / application", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which case is governed by the verb 'hivatkozik'?",
                        ["sublative (-ra/-re)", "delative (-ról/-ről)", "dative (-nak/-nek)"],
                        0,
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'beadvány' in administrative and legal procedures?",
                        [
                            "a formal written petition, application, or pleading submitted to a public authority",
                            "a receipt issued when purchasing stationery supplies",
                            "an identity badge worn by civil servants inside ministry buildings",
                        ],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["hivatkozik", "to cite / refer to (-ra/-re)"],
                            ["kitér", "to touch upon (-ra/-re)"],
                            ["beszámol", "to report on (-ról/-ről)"],
                            ["meggyőződik", "to make sure of (-ról/-ről)"],
                            ["beadvány", "petition / submission"],
                        ],
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix governed by 'beszámol': 'A miniszter beszámolt az elvégzett munka____.'",
                        ["-ról", "-ra", "-val"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix completes 'meggyőződik': 'Szeretnék személyesen meggyőződni az adatok hitelességé____'?",
                        ["-ről", "-re", "-hez"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A beadvány szerzője az Alaptörvény védelmet garantáló passzusaira ____. (referred / cited)",
                        "hivatkozott",
                        "The author of the petition cited the passages of the Fundamental Law that guarantee protection.",
                        ["b2-abstract-case-government"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A vizsgálóbiztos a jelentésében külön ____ a lakossági panaszok megalapozottságára. (touched upon)",
                        "kitért",
                        "In his report, the inquiry commissioner specifically touched upon the groundedness of public complaints.",
                        ["b2-abstract-case-government"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "jogász", "a", "beadványban", "a", "vonatkozó", "jogszabályokra", "hivatkozott."],
                        ["A", "jogász", "a", "beadványban", "a", "vonatkozó", "jogszabályokra", "hivatkozott."],
                        "The lawyer cited the relevant regulations in the petition.",
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az ombudsman éves jelentésében részletesen ____ a gyermekjogok helyzetéről. (reported on)",
                        "beszámolt",
                        "The ombudsman reported in detail in his annual report on the situation of children's rights.",
                        ["b2-30-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "ellenőrök", "a", "helyszínen", "győződtek", "meg", "a", "tényekről."],
                        ["Az", "ellenőrök", "a", "helyszínen", "győződtek", "meg", "a", "tényekről."],
                        "The inspectors made sure of the facts on site.",
                        ["b2-30-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Állampolgár", "text": "Hogyan indokoljam meg a beadványomat a hivatal felé?"},
                            {"speaker": "Ügyvéd", "text": "____"},
                        ],
                        [
                            "Hivatkozzon a vonatkozó jogszabályi helyekre, és részletesen számoljon be a sérelmet okozó eseményekről.",
                            "Ne hivatkozzon semmire, csak követeljen pénzt udvariatlan szavakkal.",
                            "A beadványokat kizárólag énekelve szabad előadni a hivatal portáján.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Bizottsági elnök", "text": "Mire terjedt ki a hatósági ellenőrzés?"},
                            {"speaker": "Főfelügyelő", "text": "____"},
                        ],
                        [
                            "A felügyelők személyesen győződtek meg a biztonsági előírások betartásáról, és a jelentés külön kitért a hiányosságokra.",
                            "Nem ellenőriztünk semmit, mert elment az áram az épületben.",
                            "A tényekről nem szabad meggyőződni a törvény szerint.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hivatkozik' (+ -ra/-re) citing a law in an administrative context.",
                                "answer": "A fellebbezésében az ügyfél az általános közigazgatási rendtartásról szóló törvényre hivatkozott.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'meggyőződik' (+ -ról/-ről) verifying factual accuracy.",
                                "answer": "A döntés meghozatala előtt a hivatalvezető személyesen győződött meg a benyújtott dokumentumok valódiságáról.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A polgármester beszédében nem ____ a lakossági tiltakozást kiváltó beruházásra. (did not touch upon)",
                        "tért ki",
                        "In his speech, the mayor did not touch upon the investment that elicited public protest.",
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which verb requires the delative case (-ról/-ről) to express delivering an official report?",
                        ["beszámol", "hivatkozik", "kitér"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Holding Institutions Accountable",
            "grammar_label": "Institutional accountability, ombudsman procedures, and access to public data (átláthatóság, elszámoltathatóság)",
            "goals": [
                "I can discuss public sector transparency (átláthatóság) and institutional accountability (elszámoltathatóság)",
                "I can formulate inquiries to the parliamentary commissioner / ombudsman",
                "I can request public interest data (közérdekű adat) using formal institutional grammar",
            ],
            "grammar_doc": {
                "slug": "institutional-accountability-ombudsman",
                "title": "Holding Institutions Accountable: átláthatóság és ombudsman",
                "text1_title": "Pillars of Democratic Accountability",
                "text1": "Public sector integrity rests upon 'átláthatóság' (transparency) and 'elszámoltathatóság' (accountability). When institutions fail to adhere to administrative norms, citizens have the constitutional right to initiate an official 'kivizsgálás' (inquiry / investigation) through independent oversight bodies.",
                "text2_title": "Ombudsman Petitions and Freedom of Information Requests",
                "text2": "The parliamentary commissioner for fundamental rights ('ombudsman') investigates maladministration and systemic rights violations. Concurrently, citizens may file access requests for 'közérdekű adat' (public interest data). These petitions synthesize complex case-governed verbs: 'hivatkozik az információszabadságról szóló törvényre', 'ragaszkodik az adatok kiadásához', 'beszámol a hatósági mulasztásokról'.",
                "table_title": "Accountability and Oversight Vocabulary",
                "table_rows": [
                    ["átláthatóság", "A közpénzek elköltése során alapkövetelmény az átláthatóság. (Transparency.)"],
                    ["elszámoltathatóság", "Az intézményi elszámoltathatóság erősíti a társadalmi bizalmat. (Accountability.)"],
                    ["ombudsman", "Az állampolgár az ombudsmanhoz fordult panasszal. (Ombudsman.)"],
                    ["közérdekű adat", "Közérdekű adatigénylést nyújtott be az önkormányzathoz. (Public interest data.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az ombudsman átfogó kivizsgálást indított a szociális otthonokban tapasztalt jogsértések miatt.",
                        "english": "The ombudsman launched a comprehensive inquiry into the rights violations experienced in social care homes.",
                    },
                    {
                        "spanish": "A civil szervezetek az állami beruházások teljes átláthatóságáért küzdenek.",
                        "english": "Civil organizations fight for the complete transparency of state investments.",
                    },
                    {
                        "spanish": "A közérdekű adatok megismerésére irányuló kérelmet a minisztérium határidőre teljesítette.",
                        "english": "The ministry fulfilled the request directed at accessing public interest data within the deadline.",
                    },
                    {
                        "spanish": "A választott képviselők elszámoltathatósága a demokrácia működésének elengedhetetlen feltétele.",
                        "english": "The accountability of elected representatives is an indispensable condition for the functioning of democracy.",
                    },
                ],
                "tip": "Note that 'ombudsman' is typically used with the allative case when turning to that official for help: 'az ombudsmanhoz fordul segítségért'.",
            },
            "words": [
                {"lemma": "átláthatóság", "translation": "transparency", "pos": "noun"},
                {"lemma": "elszámoltathatóság", "translation": "accountability", "pos": "noun"},
                {"lemma": "ombudsman", "translation": "ombudsman / parliamentary commissioner", "pos": "noun"},
                {"lemma": "közérdekű adat", "translation": "public interest data / freedom of information", "pos": "expression"},
                {"lemma": "kivizsgálás", "translation": "investigation / inquiry", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the official role of the 'ombudsman' in Hungary?",
                        [
                            "an independent parliamentary commissioner who investigates fundamental rights violations and maladministration",
                            "a judge who issues traffic fines at regional road intersections",
                            "a bank manager in charge of national currency reserves",
                        ],
                        0,
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes institutional transparency in governance and spending?",
                        ["átláthatóság", "száműzetés", "határozat"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["átláthatóság", "transparency"],
                            ["elszámoltathatóság", "accountability"],
                            ["ombudsman", "parliamentary commissioner"],
                            ["közérdekű adat", "public interest data"],
                            ["kivizsgálás", "inquiry / investigation"],
                        ],
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix for turning to the ombudsman: 'A panaszos az ombudsman____ fordult segítségért.'",
                        ["-hoz", "-nak", "-ban"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which verb correctly pairs with 'vizsgálat' in 'Az ombudsman hivatalból átfogó vizsgálatot ____'?",
                        ["indított", "tért", "kötött"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A civil szervezet keresetet indított a bíróságon a megtagadott közérdekű adatok kiadása ____. (for / regarding)",
                        "iránt",
                        "The civil organization launched a lawsuit in court for the release of refused public interest data.",
                        ["b2-abstract-case-government"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A közintézmények kötelesek biztosítani a költségvetési gazdálkodás teljes ____. (transparency)",
                        "átláthatóságát",
                        "Public institutions are obliged to ensure the full transparency of budget management.",
                        ["b2-abstract-case-government"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Az", "ombudsman", "független", "kivizsgálást", "rendelt", "el", "az", "ügyben."],
                        ["Az", "ombudsman", "független", "kivizsgálást", "rendelt", "el", "az", "ügyben."],
                        "The ombudsman ordered an independent investigation in the case.",
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A korrupció visszaszorításának leghatékonyabb eszköze a döntéshozók intézményi ____. (accountability)",
                        "elszámoltathatósága",
                        "The most effective instrument for curbing corruption is the institutional accountability of decision-makers.",
                        ["b2-30-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Minden", "állampolgárnak", "joga", "van", "a", "közérdekű", "adatok", "megismeréséhez."],
                        ["Minden", "állampolgárnak", "joga", "van", "a", "közérdekű", "adatok", "megismeréséhez."],
                        "Every citizen has the right to access public interest data.",
                        ["b2-30-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Mit tehetünk, ha a minisztérium megtagadja a szerződések nyilvánosságra hozatalát?"},
                            {"speaker": "Jogvédő jogász", "text": "____"},
                        ],
                        [
                            "Közérdekű adatigénylési pert indíthatunk, és az ombudsmanhoz fordulhatunk az átláthatóság érvényesítése végett.",
                            "Semmit sem tehetünk, mert az állami pénzek elköltése titkos információ.",
                            "Töröljük le a számítógépről a cikket, és hagyjuk abba a munkát.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Panaszos", "text": "Mikor avatkozhat be az ombudsman az eljárásba?"},
                            {"speaker": "Hivatali tanácsadó", "text": "____"},
                        ],
                        [
                            "Akkor, ha a hatóság tevékenysége vagy mulasztása alapvető jogokat sért, és a jogorvoslati lehetőségeket már kimerítették.",
                            "Bármikor, amikor a postás késik a levelek kézbesítésével.",
                            "Csak akkor avatkozhat be, ha a bíróság engedélyt ad neki rá.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'közérdekű adat' asserting access to information.",
                                "answer": "Az önkormányzat köteles harminc napon belül kiadni a polgárok által kért közérdekű adatokat.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'elszámoltathatóság' in the context of democratic governance.",
                                "answer": "A tisztségviselők elszámoltathatósága és a közpénzek átlátható felhasználása a jogállam legfontosabb sarokköve.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A független hatóság alapos ____ indított a rendőri intézkedések jogszerűségének felülvizsgálatára. (inquiry / investigation)",
                        "kivizsgálást",
                        "The independent authority launched a thorough inquiry to review the legality of police measures.",
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase designates government-held information accessible to the public by law?",
                        ["közérdekű adat", "személyi titok", "hivatali eskü"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Writing an Official Complaint or Proposal",
            "grammar_label": "Administrative appeals and official complaints (fellebbez -ellen, panasszal él, eljárási hiba)",
            "goals": [
                "I can lodge an official appeal against a ruling using fellebbez (-ellen)",
                "I can formulate a formal complaint using panasszal él with postpositional government",
                "I can identify procedural errors (eljárási hiba) and petition for equity (méltányosság)",
            ],
            "grammar_doc": {
                "slug": "administrative-complaints-and-appeals",
                "title": "Official Complaints, Appeals, and Equity: fellebbez és panasszal él",
                "text1_title": "Appeals and Objections: fellebbez (+ ellen) and panasszal él",
                "text1": "In Hungarian administrative law, challenging an authoritative decree or resolution ('határozat') requires precise governance formulas. 'Fellebbez vmi ellen' governs the postposition 'ellen': 'Fellebbez a határozat ellen' (Appeals against the resolution). When lodging an official objection, the idiom 'panasszal él' (literally 'lives with a complaint' = formally files a complaint) is paired with 'szemben' or takes a dative-infinitive complement.",
                "text2_title": "Procedural Errors and Equity Petitions",
                "text2": "Appeals typically allege an 'eljárási hiba' (procedural defect or due process violation) or petition for 'méltányosság' (administrative equity / leniency) based on exceptional personal hardship. Precision in technical legal register is required: 'határozatot hoz' (issues a decree), 'méltányossági kérelmet terjeszt elő' (submits an equity petition).",
                "table_title": "Legal Appeals and Complaint Lexicon",
                "table_rows": [
                    ["fellebbez (ellen)", "Fellebbeztek az elsőfokú ítélet ellen. (Appealed against the first-instance verdict.)"],
                    ["panasszal él", "Az ügyfél panasszal élt a szabálytalan bánásmód miatt. (Lodged a complaint.)"],
                    ["határozat", "A kormányhivatal elutasító határozatot hozott. (Issued a rejecting resolution.)"],
                    ["méltányosság", "Méltányossági kérelem benyújtására van lehetőség. (Equity petition.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az ügyfél a kézhezvételtől számított tizenöt napon belül fellebbezett az elutasító határozat ellen.",
                        "english": "The client appealed against the rejecting resolution within fifteen days of receipt.",
                    },
                    {
                        "spanish": "A polgár hivatalos panasszal élt a vizsgálat során elkövetett súlyos eljárási hiba miatt.",
                        "english": "The citizen lodged an official complaint due to a grave procedural error committed during the inquiry.",
                    },
                    {
                        "spanish": "A minisztérium hatályon kívül helyezte a határozatot, és új eljárás lefolytatását rendelte el.",
                        "english": "The ministry annulled the resolution and ordered the conduct of a new proceeding.",
                    },
                    {
                        "spanish": "A súlyos egészségi állapotra tekintettel a hivatal méltányosságból csökkentette a kiszabott bírságot.",
                        "english": "In view of the grave health condition, the office reduced the imposed fine out of equity.",
                    },
                ],
                "tip": "Remember: 'fellebbez' governs 'ellen' ('fellebbez a döntés ellen'), NOT the accusative or dative!",
            },
            "words": [
                {"lemma": "fellebbez", "translation": "to appeal (against: -ellen)", "pos": "verb"},
                {"lemma": "panasszal él", "translation": "to lodge a complaint", "pos": "expression"},
                {"lemma": "határozat", "translation": "formal decision / resolution", "pos": "noun"},
                {"lemma": "eljárási hiba", "translation": "procedural error", "pos": "expression"},
                {"lemma": "méltányosság", "translation": "equity / fairness / leniency", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which postposition is governed by 'fellebbez' when challenging a decision?",
                        ["ellen", "mellett", "nélkül"],
                        0,
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'határozat' in Hungarian administrative terminology?",
                        [
                            "a formal, legally binding resolution or decree issued by a public authority",
                            "an informal telephone inquiry between two municipal clerks",
                            "a temporary pass giving access to the town hall cafeteria",
                        ],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["fellebbez", "to appeal against (-ellen)"],
                            ["panasszal él", "to lodge a complaint"],
                            ["határozat", "resolution / formal decision"],
                            ["eljárási hiba", "procedural error"],
                            ["méltányosság", "equity / leniency"],
                        ],
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct phrasing for lodging an administrative complaint: 'Az állampolgár hivatalos ____ a hivatalvezetőnél.'",
                        ["panasszal élt", "panaszt tett tönkre", "panaszkodott tegnap este"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the correct postposition: 'A kérelmező az elutasító határozat ____ nyújtott be fellebbezést.'",
                        ["ellen", "iránt", "által"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A bíróság megállapította, hogy a hatóság súlyos ____ követett el az ügyben. (procedural error)",
                        "eljárási hibát",
                        "The court determined that the authority had committed a grave procedural error in the case.",
                        ["b2-abstract-case-government"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A panaszos határidőn belül ____ az építési hatóság elmarasztaló határozata ellen. (appealed)",
                        "fellebbezett",
                        "The complainant appealed within the deadline against the construction authority's adverse decision.",
                        ["b2-abstract-case-government"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "hivatal", "méltányosságból", "engedélyezte", "a", "részletfizetést", "a", "kérelmezőnek."],
                        ["A", "hivatal", "méltányosságból", "engedélyezte", "a", "részletfizetést", "a", "kérelmezőnek."],
                        "The office permitted installment payments to the applicant out of equity.",
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A sérelmet szenvedett vállalkozó hivatalos ____ élt a jegyző törvénysértő eljárása miatt. (complaint)",
                        "panasszal",
                        "The aggrieved entrepreneur lodged an official complaint due to the notary's unlawful procedure.",
                        ["b2-30-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kormányhivatal", "másodfokon", "megsemmisítette", "a", "törvénysértő", "határozatot."],
                        ["A", "kormányhivatal", "másodfokon", "megsemmisítette", "a", "törvénysértő", "határozatot."],
                        "The government office annulled the unlawful resolution on second instance.",
                        ["b2-30-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyfél", "text": "Mit tehetek, ha úgy érzem, a hivatal igazságtalan határozatot hozott?"},
                            {"speaker": "Ügyvéd", "text": "____"},
                        ],
                        [
                            "Tizenöt napon belül fellebbezhet a határozat ellen a felettes szervnél, vagy méltányossági kérelmet terjeszthet elő.",
                            "Semmit, mert a hivatal határozatai megváltoztathatatlanok az örökkévalóságig.",
                            "Tépje szét a határozatot, és dobja ki a kukába.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Hivatali ellenőr", "text": "Milyen indok alapján semmisítették meg a határozatot?"},
                            {"speaker": "Jegyző", "text": "____"},
                        ],
                        [
                            "A vizsgálat során kiderült, hogy súlyos eljárási hiba történt, mert az ügyfélnek nem adtak lehetőséget a nyilatkozattételre.",
                            "Mert a bíró elfelejtette aláírni a dokumentumot, és elvesztette a pecsétjét.",
                            "A határozatokat minden hónapban automatikusan megsemmisítik.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'fellebbez' (+ ellen) challenging an administrative decree.",
                                "answer": "A kérelmező jogi képviselője útján fellebbezett az elsőfokú környezetvédelmi határozat ellen.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'eljárási hiba' and 'panasszal él'.",
                                "answer": "A felperes panasszal élt az eljárási hiba miatt, amely megfosztotta őt a bizonyítás lehetőségétől.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Az állampolgárok jogosultak a törvénysértő közigazgatási döntések ____ fellebbezést benyújtani. (against)",
                        "ellen",
                        "Citizens are entitled to submit an appeal against unlawful administrative decisions.",
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes lodging an official grievance in administrative law?",
                        ["panasszal él", "határozatot hoz", "fellebbezést megtagad"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Leading a Public Consultation",
            "grammar_label": "Synthesizing case-governed verbs in civic advocacy and democratic assembly",
            "goals": [
                "I can moderate or participate in a public consultation (társadalmi egyeztetés)",
                "I can advocate for community interests at a public hearing (közmeghallgatás)",
                "I can analyze environmental and social impact assessments (hatásvizsgálat) using governed verbs",
            ],
            "grammar_doc": {
                "slug": "leading-public-consultations",
                "title": "Public Consultation, Civic Advocacy, and Assembly: érdekérvényesítés",
                "text1_title": "Mechanisms of Participatory Democracy",
                "text1": "Democratic legitimacy relies on robust 'állampolgári részvétel' (civic participation) mediated through institutional channels: 'társadalmi egyeztetés' (public consultation) and statutory 'közmeghallgatás' (public hearing). At these forums, local residents and interest groups engage in structured 'érdekérvényesítés' (advocacy / interest representation) before major urban or infrastructural decisions are finalized.",
                "text2_title": "Impact Assessments and Rhetorical Synthesis",
                "text2": "Proposals and debates evaluate the conclusions of an independent 'hatásvizsgálat' (impact assessment). Advocacy discourse brings together the full inventory of case-governed abstract verbs: 'ragaszkodnak a környezet megóvásához' (-hoz), 'eltekintenek az önkényes módosításoktól' (-tól), 'hivatkoznak a hatástanulmány adataira' (-ra), and 'beszámolnak a lakossági észrevételekről' (-ról).",
                "table_title": "Civic Advocacy Lexicon",
                "table_rows": [
                    ["társadalmi egyeztetés", "A törvénytervezetet társadalmi egyeztetésre bocsátották. (Public consultation.)"],
                    ["állampolgári részvétel", "A részvételi költségvetés erősíti az állampolgári részvételt. (Civic participation.)"],
                    ["közmeghallgatás", "A lakosság aktívan felszólalt a közmeghallgatáson. (Public hearing.)"],
                    ["hatásvizsgálat", "Független környezeti hatásvizsgálat elvégzését követelik. (Impact assessment.)"],
                ],
                "examples": [
                    {
                        "spanish": "A városvezetés társadalmi egyeztetést kezdeményezett a belvárosi forgalomcsillapítás tervéről.",
                        "english": "The city leadership initiated a public consultation on the downtown traffic calming plan.",
                    },
                    {
                        "spanish": "Az aktív állampolgári részvétel nélkülözhetetlen egy élhető és fenntartható település kialakításához.",
                        "english": "Active civic participation is indispensable for creating a livable and sustainable settlement.",
                    },
                    {
                        "spanish": "A feszült hangulatú közmeghallgatáson a lakosok élesen bírálták a tervezett akkumulátorgyár beruházását.",
                        "english": "At the tense public hearing, residents sharply criticized the planned battery factory investment.",
                    },
                    {
                        "spanish": "A civil szervezetek ragaszkodnak ahhoz, hogy a beruházás előtt készüljön részletes társadalmi hatásvizsgálat.",
                        "english": "Civil organizations insist that a detailed social impact assessment be prepared prior to the investment.",
                    },
                ],
                "tip": "Synthesizing case governments in oral advocacy: practice transitioning between '-hoz' (ragaszkodik hozzá), '-ra' (hivatkozik rá), and '-ról' (beszámol róla).",
            },
            "words": [
                {"lemma": "társadalmi egyeztetés", "translation": "public consultation", "pos": "expression"},
                {"lemma": "állampolgári részvétel", "translation": "civic participation", "pos": "expression"},
                {"lemma": "közmeghallgatás", "translation": "public hearing", "pos": "noun"},
                {"lemma": "érdekérvényesítés", "translation": "advocacy / interest representation", "pos": "noun"},
                {"lemma": "hatásvizsgálat", "translation": "impact assessment", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'közmeghallgatás' in local municipal governance?",
                        [
                            "an open public hearing where citizens can voice opinions directly to elected officials",
                            "a mandatory hearing test administered to school children",
                            "an opera concert organized in the town square for pensioners",
                        ],
                        0,
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term designates the organized representation of citizens' social or legal interests?",
                        ["érdekérvényesítés", "eljárási hiba", "kivándorlás"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["társadalmi egyeztetés", "public consultation"],
                            ["állampolgári részvétel", "civic participation"],
                            ["közmeghallgatás", "public hearing"],
                            ["érdekérvényesítés", "advocacy / interest representation"],
                            ["hatásvizsgálat", "impact assessment"],
                        ],
                        ["b2-30-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which governed verb fits best: 'A lakosok a hatásvizsgálat eredményei____ hivatkoztak a vita során'?",
                        ["-re", "-hez", "-ből"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct case suffix: 'A civil közösség ragaszkodik a környezet védelmé____.'",
                        ["-hez", "-től", "-ben"],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A polgármester a közmeghallgatáson részletesen beszámolt a beruházás várható gazdasági ____. (effects)",
                        "hatásairól",
                        "At the public hearing, the mayor reported in detail on the expected economic effects of the investment.",
                        ["b2-abstract-case-government"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A törvénytervezetet széles körű társadalmi ____ kell bocsátani a parlamenti vita előtt. (consultation)",
                        "egyeztetésre",
                        "The draft bill must be submitted to broad public consultation before the parliamentary debate.",
                        ["b2-abstract-case-government"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Az", "állampolgári", "részvétel", "erősíti", "a", "helyi", "közösségek", "összetartozását."],
                        ["Az", "állampolgári", "részvétel", "erősíti", "a", "helyi", "közösségek", "összetartozását."],
                        "Civic participation strengthens the cohesion of local communities.",
                        ["b2-abstract-case-government"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A civil szervezetek hatékony ____ révén elérték a védett erdőterület megóvását. (advocacy)",
                        "érdekérvényesítés",
                        "Through effective advocacy, civil organizations achieved the preservation of the protected forest area.",
                        ["b2-30-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "független", "hatásvizsgálat", "súlyos", "környezeti", "kockázatokra", "figyelmeztetett."],
                        ["A", "független", "hatásvizsgálat", "súlyos", "környezeti", "kockázatokra", "figyelmeztetett."],
                        "The independent impact assessment warned of severe environmental risks.",
                        ["b2-30-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Önkormányzati képviselő", "text": "Hogyan növelhetjük a lakosság bizalmát a városfejlesztési tervek iránt?"},
                            {"speaker": "Civil koordinátor", "text": "____"},
                        ],
                        [
                            "Társadalmi egyeztetést kell szervezni, ahol a lakosok hozzászólhatnak a hatásvizsgálatokhoz a közmeghallgatáson.",
                            "Tartsuk titokban a terveket az utolsó pillanatig, hogy senki se tiltakozhasson.",
                            "A lakossági vélemények feleslegesek, mert a polgárok nem értenek az építkezéshez.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Helyi lakos", "text": "Érdemes elmenni a holnapi közmeghallgatásra?"},
                            {"speaker": "Környezetvédő", "text": "____"},
                        ],
                        [
                            "Feltétlenül, hiszen az állampolgári részvétel és az érdekérvényesítés révén közvetlenül befolyásolhatjuk a képviselő-testület döntését.",
                            "Nem érdemes, mert a törvény tiltja a polgárok felszólalását a meghallgatásokon.",
                            "A meghallgatáson csak a képviselők beszélhetnek egymással zárt ajtók mögött.",
                        ],
                        0,
                        ["b2-abstract-case-government"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'társadalmi egyeztetés' in a legislative reform context.",
                                "answer": "A kormány az új oktatási törvény elfogadása előtt széles körű társadalmi egyeztetést ígért a szakmai szervezetekkel.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'közmeghallgatás' and 'hatásvizsgálat'.",
                                "answer": "A közmeghallgatáson a lakosok részletesen elemezték a környezeti hatásvizsgálat aggasztó megállapításait.",
                            }
                        ],
                        ["b2-abstract-case-government"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A civil mozgalom határozottan ragaszkodott ahhoz, hogy a beruházás előtt tartsanak nyilvános ____. (public hearing)",
                        "közmeghallgatást",
                        "The civic movement firmly insisted that a public hearing be held prior to the investment.",
                        ["b2-abstract-case-government"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes an assessment analyzing the future consequences of a proposed policy or project?",
                        ["hatásvizsgálat", "beadvány", "jogorvoslat"],
                        0,
                        ["b2-30-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can confidently apply allative and ablative abstract verb case governments (ragaszkodik -hoz, eltekint -tól)",
            "I can master sublative and delative verb case governments (hivatkozik -ra, beszámol -ról, meggyőződik -ról)",
            "I can draft petitions, administrative appeals, and participate in civic consultations in sophisticated B2 Hungarian",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["jogorvoslat", "legal remedy / redress"],
                    ["beadvány", "petition / submission"],
                    ["átláthatóság", "transparency"],
                    ["fellebbez", "to appeal against (-ellen)"],
                    ["közmeghallgatás", "public hearing"],
                ],
                ["b2-30-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'panasszal él' signify in formal administrative disputes?",
                [
                    "formally exercising the legal right to submit a grievance against an institutional action or defect",
                    "complaining verbally to neighbors over morning coffee",
                    "filing a medical claim for chronic fatigue at a workplace clinic",
                ],
                0,
                ["b2-30-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates abstract verb case government for both 'ragaszkodik' and 'eltekint'?",
                [
                    "A felperes ragaszkodott a határidőkhöz, de a bíróság méltányosságból eltekintett a bírságtól.",
                    "A felperes ragaszkodott a határidőktől, de a bíróság eltekintett a bírsághoz.",
                    "A felperes ragaszkodik a határidőkre, és eltekint a bírságban.",
                ],
                0,
                ["b2-abstract-case-government"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A döntéshozók intézményi ____ elengedhetetlen a demokrácia átlátható működéséhez. (accountability)",
                "elszámoltathatósága",
                "The institutional accountability of decision-makers is indispensable for the transparent functioning of democracy.",
                ["b2-30-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "Az ügyfél a kézhezvételtől számított tizenöt napon belül ____ az elsőfokú határozat ellen. (appealed)",
                "fellebbezett",
                "The client appealed against the first-instance resolution within fifteen days of receipt.",
                ["b2-abstract-case-government"],
            ),
            fb(
                "grammar",
                "recall",
                "A beadvány benyújtásakor az ügyvéd a törvény pontos szövegére ____ a panasz alátámasztására. (referred / cited)",
                "hivatkozott",
                "When submitting the petition, the lawyer cited the exact text of the law to support the complaint.",
                ["b2-abstract-case-government"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'fellebbez a határozat ellen' the only correct phrasing in administrative law?",
                [
                    "Because 'fellebbez' strictly governs the postposition 'ellen' to denote challenging an authority ruling.",
                    "Because 'határozat' cannot take any grammatical case suffixes in Hungarian.",
                    "Because 'ellen' is used only with past tense verbs in formal registers.",
                ],
                0,
                ["b2-abstract-case-government"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Irodalomtörténész", "text": "Hogyan jelenik meg az intézményi önkény Mikszáth Különös házasságában?"},
                    {"speaker": "Egyetemi hallgató", "text": "____"},
                ],
                [
                    "A hatóságok ragaszkodnak a formaságokhoz, eltekintenek az igazságtól, és az áldozat hiába fellebbez a döntések ellen.",
                    "Mindenki azonnal igazságot szolgáltat Buttler grófnak, mert a törvények tökéletesen működnek.",
                    "A regényben nincsenek hatóságok, csupán egy békés falusi esküvőről szól a történet.",
                ],
                0,
                ["b2-abstract-case-government"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'meggyőződik' is used with its correct grammatical case government:",
                [
                    "A vizsgálóbiztos a helyszínen győződött meg a tények valódiságáról.",
                    "A vizsgálóbiztos a tényekre győződött meg a helyszínen.",
                    "A vizsgálóbiztos meggyőződött a tényekhez a vizsgálat után.",
                ],
                0,
                ["b2-abstract-case-government"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["Az", "állampolgár", "határozottan", "ragaszkodik", "a", "törvényben", "biztosított", "jogaihoz."],
                ["Az", "állampolgár", "határozottan", "ragaszkodik", "a", "törvényben", "biztosított", "jogaihoz."],
                "The citizen firmly insists on his rights guaranteed in the law.",
                ["b2-abstract-case-government"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "közmeghallgatáson", "a", "szakértők", "részletesen", "beszámoltak", "a", "hatásvizsgálat", "eredményeiről."],
                ["A", "közmeghallgatáson", "a", "szakértők", "részletesen", "beszámoltak", "a", "hatásvizsgálat", "eredményeiről."],
                "At the public hearing, the experts reported in detail on the results of the impact assessment.",
                ["b2-abstract-case-government"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause administrative argument using 'ragaszkodik' (-hoz), 'hivatkozik' (-ra), and 'fellebbez' (ellen).",
                        "answer": "Mivel a panaszos határozottan ragaszkodik az alaptörvényben rögzített jogaihoz, a beadványában a vonatkozó közigazgatási jogszabályokra hivatkozott; és amennyiben a kérelem elutasításra kerülne, határidőn belül fellebbezni fog az elmarasztaló határozat ellen.",
                    }
                ],
                ["b2-abstract-case-government"],
            ),
        ],
    },
}
