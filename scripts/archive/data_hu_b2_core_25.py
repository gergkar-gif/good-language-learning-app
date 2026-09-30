#!/usr/bin/env python3
"""
Hungarian B2 Core Unit 25: Law, Justice & Constitutional Principles
Grammar skill: b2-legal-normative-register
Vocab skill: b2-25-vocab
"""
from helpers_hu_b2_exercises import mc, match, fb, sb, dc, sw

UNIT_25 = {
    "unit_num": 25,
    "title": "Law, Justice & Constitutional Principles",
    "grammar_summary": "Formal legal syntax and normative constructions: based upon (alapján, értelmében), in accordance with (összhangban), procedural detriment and burden (sérelmére, terhére), normative rights and obligations (jogosult, köteles + infinitive), and future/obligatory participles (-andó/-endő).",
    "grammar_skill": "b2-legal-normative-register",
    "vocab_skill": "b2-25-vocab",
    "theme": "Law, justice and constitutional principles",
    "intro_body": [
        "A jogállamiság, az emberi jogok védelme és a hatalmi ágak elválasztása a modern alkotmányos demokráciák legfőbb sarokkövei. A jogi szaknyelv Magyarországon évszázados fejlődés eredménye: a feudális vármegyei szokásjogtól a 19. századi kodifikáción át a kortárs európai jogharmonizációig kifinomult szintaktikai és lexikai rendszert hozott létre.",
        "Ebben a fejezetben elsajátíthatja a formális jogi hivatkozások szerkesztését (alapján, összhangban vmivel, sérelmére, terhére), a normatív kötelezettségek és jogosultságok kifejezését (jogosult/köteles + főnévi igenév, beálló melléknévi igenév: -andó/-endő), valamint a jogértelmezés és a beadványszerkesztés magas szintű nyelvi fordulatait. Eötvös József halhatatlan regénye, 'A falu jegyzője' segítségével pedig a jog betűje és az igazság szelleme közötti örök konfliktus mélyére tekinthet.",
    ],
    "classic_story": {
        "slug": "afalujegyzoje",
        "author": "Eötvös József",
        "work": "A falu jegyzője (1845)",
        "title": "Törvény, igazság és vármegyei hatalom",
        "summary": "Tengelyi Jónás tiszaréti jegyző és a törvényen kívülivé lett Viola találkozása a nádas szélén: drámai vita a vármegyei nemesi önkényről, a törvények rideg betűjéről és az igazság valódi természetéről.",
        "characters": ["Tengelyi Jónás", "Viola"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A tiszaréti határban lassan alkonyodott; a Tisza menti nádas felett nehéz, szürke fellegek gyülekeztek. Tengelyi Jónás jegyző egyedül ballagott a gáton, kezében vándorbotjával, mélyen elmerülve a vármegyei igazságszolgáltatás nyomasztó állapotán való töprengésben.",
            },
            {
                "type": "dialogue",
                "speaker": "Viola",
                "text": "Jó estét kívánok, jegyző úr! Ne féljen, a fegyverem a föld felé néz. Tengelyi Jónásnak nincs mit tartania attól az embertől, akit a világ haramiának nevez, de aki jól tudja, hogy a faluban egyedül a jegyző úrnak van tiszta lelkiismerete.",
            },
            {
                "type": "dialogue",
                "speaker": "Tengelyi Jónás",
                "text": "Te vagy az, Viola? Miért kockáztatod az életedet azzal, hogy a falu határában ólálkodsz? A pandúrok a nyomodban járnak, és a vármegyei bíróság statáriális ítélettel fenyeget mindenkit, aki menedéket nyújt neked.",
            },
            {
                "type": "dialogue",
                "speaker": "Viola",
                "text": "Tudom én azt jól, jegyző úr. De mondja meg nekem Isten színe előtt: miféle törvény az, amely az ártatlan parasztot botbüntetésre ítéli, elrabolja a tehenét a földesúr parancsára, és amikor a becsületét védi, rablónak bélyegzi? A törvény nem az igazságot szolgálja, hanem a hatalmasok önkényét.",
            },
            {
                "type": "dialogue",
                "speaker": "Tengelyi Jónás",
                "text": "Nem tagadom a rendszer visszásságait, Viola; a vármegyei nemesi önkény mindannyiunk életét megmérgezi. De ha a törvényesség kereteit felrúgjuk, és ki-ki a maga puskájával szerez igazságot, akkor a társadalom a barbárság és a káosz örvényébe zuhan vissza.",
            },
            {
                "type": "dialogue",
                "speaker": "Viola",
                "text": "Könnyű a törvényt tisztelni annak, akit az úri jogok megvédenek! De engem megfosztottak az emberi méltóságomtól, a családomtól és a tisztességes eljárás jogától. A bíróság nem mérlegelt semmit, csupán a szolgabíró haragjának engedelmeskedett a szegény ember terhére.",
            },
            {
                "type": "dialogue",
                "speaker": "Tengelyi Jónás",
                "text": "Megértem a keserűségedet, de az igazi feladat nem a bosszú, hanem a jogrend reformja. Olyan alkotmányos rendre van szükség, amelyben a törvény előtt minden polgár egyenlő, és senki sem büntethető független bírói ítélet nélkül. Ígérem, amíg élek, a tisztességes eljárásért és az igazság szelleméért fogok küzdeni.",
            },
            {
                "type": "narration",
                "text": "Viola hallgatott, tekintetében fájdalmas beletörődés tükröződött, majd megemelte a kalapját, és nesztelen léptekkel eltűnt a sűrű nádasban. Tengelyi magára maradt a sötétedő pusztán, szívében azzal a szilárd elhatározással, hogy tollával és szavával az elnyomottak törvényes védelmére kél.",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért vált Viola törvényen kívülivé Eötvös József regényében?",
                "options": [
                    "Mert a vármegyei tisztviselők önkénye és az igazságtalan büntetés megfosztotta emberi méltóságától és jogaitól.",
                    "Mert anyagi haszonszerzés céljából ki akarta rabolni a vármegyei pénztárat.",
                    "Mert külföldre akart szökni, hogy katonaként szolgáljon egy idegen hadseregben.",
                ],
                "correct": 0,
            },
            {
                "question": "Hogyan látja Tengelyi Jónás a hatályos vármegyei igazságszolgáltatást és a törvény szerepét?",
                "options": [
                    "Felismeri a rendszer súlyos visszásságait, de úgy véli, hogy az önbíráskodás helyett a jogrend reformja és az egyenlőség a megoldás.",
                    "Tökéletesen igazságosnak tartja a nemesi kiváltságokon alapuló bírósági gyakorlatot.",
                    "Azt javasolja Violának, hogy fegyveres felkelést robbantson ki a vármegye ellen.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen alapvető konfliktust tár fel a jegyző és a szegénylegény párbeszéde?",
                "options": [
                    "A formális jogi hatalom önkénye és a morális igazságosság iránti elemi emberi igény feszültségét.",
                    "A Tisza menti falvak közötti halászati és legeltetési határvitát.",
                    "Egy örökösödési per lefolytatásának adminisztratív formaságait.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "In Accordance With, Pursuant To (alapján, összhangban)",
            "grammar_label": "Formal legal syntax (alapján, összhangban vmivel, sérelmére, terhére)",
            "goals": [
                "I can cite statutory bases and legal provisions using alapján and értelmében",
                "I can express conformity with regulations using összhangban vmivel",
                "I can state procedural prejudice and legal detriment using sérelmére and terhére",
            ],
            "grammar_doc": {
                "slug": "formal-legal-syntax",
                "title": "Formal Legal Syntax: alapján, összhangban, sérelmére, terhére",
                "text1_title": "Citing Legal Grounds: alapján and értelmében",
                "text1": "In Hungarian administrative and legal drafting, statutory authority and normative grounds are invoked using possessive postpositional constructions. 'Alapján' ('on the basis of / pursuant to') links an administrative decision or judicial ruling directly to an enabling act: 'A hatályos törvény alapján...' ('Pursuant to the statute in force...'). Similarly, 'értelmében' ('in the sense of / under the provisions of') specifies exact statutory definitions or regulatory articles: 'A rendelet 3. cikke értelmében...' ('Within the meaning of Article 3 of the decree...').",
                "text2_title": "Conformity and Detriment: összhangban, sérelmére, terhére",
                "text2": "To express legal compliance and hierarchical harmony between norms, Hungarian uses 'összhangban' followed by an instrumental complement (-val/-vel): 'összhangban az Alaptörvénnyel' ('in accordance with the Basic Law'). Conversely, procedural violations and financial burdens are expressed through 'sérelmére' ('to the detriment / injury of') and 'terhére' ('to the charge / detriment of'): 'a felperes jogainak sérelmére' ('in violation of the plaintiff's rights'), 'az alperes terhére rótt kötelezettség' ('the obligation imposed to the defendant's debit').",
                "table_title": "Key Legal Framing Postpositions",
                "table_rows": [
                    ["alapján (+ possessive)", "a jogszabály rendelkezései alapján (pursuant to statutory provisions)"],
                    ["összhangban (-val/-vel)", "összhangban az alkotmányos elvekkel (in conformity with constitutional principles)"],
                    ["sérelmére (+ possessive)", "az ügyfél jogainak sérelmére (to the detriment of the client's rights)"],
                    ["terhére (+ possessive)", "a jogsértő terhére megállapított kár (damages assessed to the tortfeasor's charge)"],
                ],
                "examples": [
                    {
                        "spanish": "A bíróság a benyújtott bizonyítékok alapján hozta meg a döntést.",
                        "english": "The court reached its decision on the basis of the submitted evidence.",
                    },
                    {
                        "spanish": "Az önkormányzati rendeletnek teljes összhangban kell állnia a törvénnyel.",
                        "english": "The municipal ordinance must be in full accordance with the statute.",
                    },
                    {
                        "spanish": "A hatóság intézkedése az érintett állampolgár alapvető jogainak sérelmére történt.",
                        "english": "The authority's measure occurred to the detriment of the citizen's fundamental rights.",
                    },
                    {
                        "spanish": "A perköltséget a bíróság a pervesztes fél terhére rótta ki.",
                        "english": "The court assessed the legal costs to the losing party's debit.",
                    },
                ],
                "tip": "Remember that 'összhangban' always governs the instrumental case (-val/-vel), while 'alapján', 'sérelmére', and 'terhére' require the preceding noun to take an explicit possessive agreement suffix (e.g. 'a törvény alapján', 'a fél jogainak sérelmére').",
            },
            "words": [
                {"lemma": "alapján", "translation": "on the basis of / pursuant to", "pos": "postposition"},
                {"lemma": "összhangban", "translation": "in accordance with / in harmony with", "pos": "postposition"},
                {"lemma": "sérelmére", "translation": "to the detriment of / in violation of", "pos": "postposition"},
                {"lemma": "jogszabály", "translation": "legal rule / statutory regulation", "pos": "noun"},
                {"lemma": "hatályos", "translation": "in force / legally effective", "pos": "adjective"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of 'jogszabály' in formal Hungarian legal discourse?",
                        [
                            "a binding legal rule, act, statute, or government regulation",
                            "an informal recommendation issued by a private club",
                            "a historical chronicle about ancient county disputes",
                        ],
                        0,
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term describes a law that is currently in force and legally effective?",
                        ["hatályos", "érvénytelen", "ideiglenes"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["alapján", "pursuant to / on the basis of"],
                            ["összhangban", "in accordance with"],
                            ["sérelmére", "to the detriment of"],
                            ["jogszabály", "statute / legal rule"],
                            ["hatályos", "in force / effective"],
                        ],
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase correctly completes: 'A hatóság a ____ törvény rendelkezései alapján járt el'?",
                        ["hatályos", "hatályosan", "hatálytalan"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the postposition expressing that an act violates someone's legal rights:",
                        ["sérelmére", "javára", "céljából"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A miniszteri rendeletnek teljes ____ kell állnia az uniós irányelvekkel. (in accordance with)",
                        "összhangban",
                        "The ministerial decree must be in full accordance with the EU directives.",
                        ["b2-legal-normative-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A bíróság a benyújtott szakvélemény ____ állapította meg a kártérítés összegét. (on the basis of)",
                        "alapján",
                        "The court determined the compensation amount on the basis of the submitted expert opinion.",
                        ["b2-legal-normative-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "határozat", "az", "ügyfél", "jogainak", "sérelmére", "született", "meg."],
                        ["A", "határozat", "az", "ügyfél", "jogainak", "sérelmére", "született", "meg."],
                        "The decision was adopted to the detriment of the client's rights.",
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A parlament által elfogadott új ____ a kihirdetését követő napon lép hatályba. (statute / legal rule)",
                        "jogszabály",
                        "The new statute passed by parliament enters into force on the day following its promulgation.",
                        ["b2-25-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "hatályos", "jogszabályok", "minden", "állampolgárra", "egyaránt", "vonatkoznak."],
                        ["A", "hatályos", "jogszabályok", "minden", "állampolgárra", "egyaránt", "vonatkoznak."],
                        "The statutes in force apply equally to all citizens.",
                        ["b2-25-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyvéd", "text": "Hogyan kívánja alátámasztani a felperes kártérítési követelését?"},
                            {"speaker": "Kolléga", "text": "____"},
                        ],
                        [
                            "A hatályos Polgári Törvénykönyv alapján terjesztjük elő, bemutatva a jogsértés sérelmére történt károkat.",
                            "Mivel nincs semmilyen jogszabály, ezért csak szóban kérünk elnézést a bírótól.",
                            "Összhangban a reggeli újságcikkekkel, nem törődünk a törvényekkel.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Jogtanácsos", "text": "Megfelel az új vállalati szabályzat az európai adatvédelmi normáknak?"},
                            {"speaker": "Adatvédelmi tisztviselő", "text": "____"},
                        ],
                        [
                            "Igen, a belső előírások teljes összhangban állnak a vonatkozó uniós rendeletekkel.",
                            "Nem, mert a szabályzatot senki sem olvasta el a cégnél.",
                            "A sérelmére írtunk mindent, hogy senki se értse meg a lényeget.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'alapján' to cite a statutory ground for judicial annulment.",
                                "answer": "A bíróság a hatályos jogszabály alapján megsemmisítette a jogellenes közigazgatási határozatot.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'összhangban' stating that local decrees must conform with the constitution.",
                                "answer": "Az önkormányzati döntéseknek minden esetben összhangban kell lenniük az alkotmányos alapelvekkel.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A szabálytalan eljárás az alperes eljárási jogainak súlyos ____ történt. (to the detriment of)",
                        "sérelmére",
                        "The irregular proceeding took place to the severe detriment of the defendant's procedural rights.",
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective indicates that a legal norm or contract is currently legally operative?",
                        ["hatályos", "korábbi", "feltételes"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Entitled and Obliged (jogosult, köteles + infinitive)",
            "grammar_label": "Normative obligation and rights (jogosult, köteles + inf, prescriptive -andó/-endő)",
            "goals": [
                "I can state legal rights and statutory authorizations using jogosult + infinitive",
                "I can specify binding obligations and duties using köteles + infinitive",
                "I can employ prescriptive future/obligatory participles ending in -andó/-endő",
            ],
            "grammar_doc": {
                "slug": "normative-obligation-and-rights",
                "title": "Normative Modality: jogosult, köteles, and -andó/-endő",
                "text1_title": "Expressing Rights and Duties: jogosult and köteles + Infinitive",
                "text1": "In Hungarian legislative drafting, civil codes, and employment contracts, normative entitlement and duty are formulated using the predicate adjectives 'jogosult' ('entitled / authorized') and 'köteles' ('obligated / duty-bound') followed directly by an infinitive: 'Az ügyfél jogosult megismerni az iratokat' ('The client is entitled to inspect the documents'); 'A munkáltató köteles biztosítani az egészséges feltételeket' ('The employer is obliged to ensure healthy conditions'). These constructions possess definitive legal force, contrasting with colloquial deontic verbs like 'lehet' or 'kell'.",
                "text2_title": "Prescriptive Future Participles: -andó / -endő",
                "text2": "The obligatory future participle (beálló melléknévi igenév) formed with '-andó / -endő' acts as a concise, highly formal passive-equivalent modifier conveying necessity: 'alkalmazandó jog' ('applicable law / law to be applied'), 'teljesítendő kötelezettség' ('obligation to be fulfilled'), 'fizetendő összeg' ('amount payable'). When functioning as a predicate adjective with 'van' or 'lesz', it denotes an unavoidable statutory requirement: 'Ez a szabály minden esetben követendő' ('This rule is to be followed in all cases').",
                "table_title": "Normative Predicates and Participles",
                "table_rows": [
                    ["jogosult + inf", "A fogyasztó jogosult elállni a szerződéstől. (The consumer is entitled to rescind the contract.)"],
                    ["köteles + inf", "A fél köteles jóhiszeműen eljárni. (The party is obligated to act in good faith.)"],
                    ["-andó / -endő (attributive)", "az alkalmazandó jogszabály (the statute to be applied / applicable law)"],
                    ["-andó / -endő (predicative)", "A határidő szigorúan betartandó. (The deadline is strictly to be observed.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az alperes jogosult fellebbezést benyújtani az elsőfokú ítélet ellen.",
                        "english": "The defendant is entitled to file an appeal against the first-instance judgment.",
                    },
                    {
                        "spanish": "A bérlő köteles a bérleti díjat minden hónap tizedik napjáig megfizetni.",
                        "english": "The tenant is obliged to pay the rent by the tenth day of each month.",
                    },
                    {
                        "spanish": "A vitás kérdések eldöntésére a magyar polgári jog szabályai alkalmazandók.",
                        "english": "For the resolution of disputed questions, the rules of Hungarian civil law are applicable.",
                    },
                    {
                        "spanish": "A szerződésben rögzített kötelezettségek késedelem nélkül teljesítendők.",
                        "english": "The obligations established in the contract are to be fulfilled without delay.",
                    },
                ],
                "tip": "Avoid substituting 'kell' for 'köteles' in formal legal pleadings or corporate bylaws; 'köteles + infinitive' pinpoints legal liability to a specific grammatical subject, whereas 'kell' creates an impersonal sentence.",
            },
            "words": [
                {"lemma": "jogosult", "translation": "entitled / authorized", "pos": "adjective"},
                {"lemma": "köteles", "translation": "obligated / duty-bound", "pos": "adjective"},
                {"lemma": "alkalmazandó", "translation": "to be applied / applicable", "pos": "adjective"},
                {"lemma": "teljesítendő", "translation": "to be fulfilled / to be performed", "pos": "adjective"},
                {"lemma": "kötelezettség", "translation": "obligation / statutory duty", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective indicates that a party has a formal legal right to take an action?",
                        ["jogosult", "köteles", "tiltott"],
                        0,
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of 'kötelezettség' in civil law?",
                        [
                            "a legally binding duty or obligation to perform or refrain from an act",
                            "an optional suggestion given during mediation",
                            "a ceremonial greeting spoken at the beginning of a trial",
                        ],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["jogosult", "entitled / authorized"],
                            ["köteles", "obligated / duty-bound"],
                            ["alkalmazandó", "applicable / to be applied"],
                            ["teljesítendő", "to be fulfilled"],
                            ["kötelezettség", "obligation / statutory duty"],
                        ],
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which form correctly completes: 'A munkavállaló ____ megismerni a rá vonatkozó nyilvántartást'?",
                        ["jogosult", "jogosultan", "jogosulni"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the prescriptive participle for: 'a határidőn belül ____ feladatok' (tasks to be fulfilled):",
                        ["teljesítendő", "teljesített", "teljesítő"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A szerződő felek ____ egymást haladéktalanul értesíteni a változásokról. (obligated / duty-bound)",
                        "kötelesek",
                        "The contracting parties are obligated to notify each other of changes without delay.",
                        ["b2-legal-normative-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A jelen jogvitában kizárólag a magyar polgári jog szabályai ____. (applicable / to be applied)",
                        "alkalmazandók",
                        "In the present dispute, exclusively the rules of Hungarian civil law are applicable.",
                        ["b2-legal-normative-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "panaszos", "jogosult", "jogi", "képviselőt", "igénybe", "venni."],
                        ["A", "panaszos", "jogosult", "jogi", "képviselőt", "igénybe", "venni."],
                        "The complainant is entitled to retain legal counsel.",
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A vállalkozó a szerződésben vállalt ____ hiánytalanul teljesítette. (statutory obligations / duties)",
                        "kötelezettségeit",
                        "The contractor fully performed the obligations undertaken in the contract.",
                        ["b2-25-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "törvényben", "előírt", "szabályok", "mindenki", "számára", "kötelezőek."],
                        ["A", "törvényben", "előírt", "szabályok", "mindenki", "számára", "kötelezőek."],
                        "The rules prescribed in the statute are binding for everyone.",
                        ["b2-25-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Bíró", "text": "Milyen jogcímen követeli a felperes a kártérítés megfizetését?"},
                            {"speaker": "Ügyvéd", "text": "____"},
                        ],
                        [
                            "Az alperes a szerződés alapján köteles volt a hibát elhárítani, így ügyfelem jogosult a kártérítésre.",
                            "Nem tudjuk a jogcímet, de nagyon szeretnénk pénzt kapni a tárgyalás után.",
                            "A felperes nem jogosult semmire, de azért beadtuk a keresetet.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Közjegyző", "text": "Tájékoztatta az örökösöket a hagyatéki eljárás menetéről?"},
                            {"speaker": "Asszisztens", "text": "____"},
                        ],
                        [
                            "Igen, részletesen ismertettem velük a benyújtandó okiratokat és a teljesítendő kötelezettségeket.",
                            "Nem volt rá időm, ezért elküldtem őket egy kávézóba várakozni.",
                            "A kötelezettség helyett inkább szabadságra ment mindenki az irodából.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a contractual clause using 'köteles' and 'biztosítani' regarding workplace safety.",
                                "answer": "A munkáltató köteles biztosítani a biztonságos és egészséget nem veszélyeztető munkafeltételeket.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence with 'alkalmazandó' specifying statutory rules in arbitration.",
                                "answer": "A választottbírósági eljárás során a felek megállapodása szerinti anyagi jogi normák alkalmazandók.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A sértett a nyomozati szakaszban is ____ másolatot kérni az ügy iratairól. (entitled)",
                        "jogosult",
                        "The victim is entitled to request a copy of the case files during the investigation phase as well.",
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which verbal noun denotes a legally enforceable duty or liability in civil relations?",
                        ["kötelezettség", "véletlen", "engedmény"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "The Letter vs. the Spirit of the Law",
            "grammar_label": "Legal reasoning and statutory interpretation (törvény betűje vs. szelleme)",
            "goals": [
                "I can contrast literal wording with teleological intent (a törvény betűje vs. szelleme)",
                "I can articulate statutory interpretation using teleological and grammatical principles",
                "I can evaluate judicial discretion and legal certainty (jogbiztonság, mérlegelés)",
            ],
            "grammar_doc": {
                "slug": "statutory-interpretation-and-equity",
                "title": "Statutory Interpretation: The Letter vs. the Spirit of the Law",
                "text1_title": "Textual vs. Teleological Interpretation: betűje vs. szelleme",
                "text1": "Juridical discourse distinguishes sharply between strict literal construction ('a törvény betűje' - the letter of the law) and purposeful, constitutional construction ('a törvény szelleme' - the spirit of the law). Hungarian jurisprudence emphasizes teleological interpretation (cél szerinti jogértelmezés), asserting that statutory text must always be read in light of its social purpose and constitutional values: 'A bíróság nem ragaszkodhat pusztán a törvény rideg betűjéhez, ha az ellentétes a jogalkotó szándékával' ('The court cannot merely cling to the rigid letter of the law if that conflicts with the legislator's intent').",
                "text2_title": "Judicial Discretion and Equity: mérlegelés, méltányosság, and jogbiztonság",
                "text2": "Where statutes exhibit gaps ('joghézag') or indeterminate legal concepts, courts exercise judicial deliberation ('bírói mérlegelés'). Deliberation must always be balanced against the principle of legal certainty ('jogbiztonság')—the constitutional requirement that laws be clear, predictable, and non-retroactive. In exceptional individual circumstances, judicial equity ('méltányosság') allows courts to mitigate undue harshness without undermining statutory coherence.",
                "table_title": "Concepts of Legal Reasoning",
                "table_rows": [
                    ["a törvény betűje", "a jogszabály szó szerinti szövege (the literal text of the statute)"],
                    ["a törvény szelleme", "a jogalkotói cél és alkotmányos értékrend (the legislative purpose and constitutional values)"],
                    ["mérlegelési jogkör", "a bíróság vagy hatóság döntési szabadsága (discretionary authority of court or agency)"],
                    ["jogbiztonság", "a jogrend kiszámíthatósága és stabilitása (predictability and stability of the legal order)"],
                ],
                "examples": [
                    {
                        "spanish": "A bíró nemcsak a törvény betűjét követte, hanem annak valódi szellemét is érvényre juttatta.",
                        "english": "The judge not only followed the letter of the law, but also gave effect to its true spirit.",
                    },
                    {
                        "spanish": "A jogbiztonság elve megköveteli, hogy a jogszabályok egyértelműek és kiszámíthatóak legyenek.",
                        "english": "The principle of legal certainty requires that statutes be unambiguous and predictable.",
                    },
                    {
                        "spanish": "A rendkívüli körülményekre tekintettel a hatóság méltányosságból elengedte a bírságot.",
                        "english": "In consideration of extraordinary circumstances, the authority remitted the fine out of equity.",
                    },
                    {
                        "spanish": "A joghézag kitöltése során a bíróság az Alaptörvény értékeivel összhangban járt el.",
                        "english": "In filling the statutory lacuna, the court acted in accordance with the values of the Basic Law.",
                    },
                ],
                "tip": "When contrasting literal text and legislative intent, use idiomatic antitheses such as 'nem pusztán a törvény betűje, hanem annak szelleme alapján' or 'a szó szerinti értelmezés helyett a teleologikus jogértelmezést részesítve előnyben'.",
            },
            "words": [
                {"lemma": "jogértelmezés", "translation": "statutory interpretation / legal interpretation", "pos": "noun"},
                {"lemma": "méltányosság", "translation": "equity / fairness", "pos": "noun"},
                {"lemma": "joghézag", "translation": "legal loophole / statutory lacuna", "pos": "noun"},
                {"lemma": "mérlegel", "translation": "to weigh / deliberate / exercise discretion", "pos": "verb"},
                {"lemma": "jogbiztonság", "translation": "legal certainty / rule of law stability", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'jogbiztonság' encompass in constitutional law?",
                        [
                            "the predictability, clarity, and stability of the entire legal order",
                            "the private security guards stationed in court hallways",
                            "the encrypted password used to log in to court databases",
                        ],
                        0,
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which concept describes a situation where statutory legislation has omitted a regulation?",
                        ["joghézag", "jogalap", "jogvita"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["jogértelmezés", "statutory interpretation"],
                            ["méltányosság", "equity / fairness"],
                            ["joghézag", "legal loophole / lacuna"],
                            ["mérlegel", "to weigh / deliberate"],
                            ["jogbiztonság", "legal certainty"],
                        ],
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase represents teleological interpretation over literal wording?",
                        ["a törvény szelleme", "a törvény betűje", "a törvény paragrafusa"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What is required of judicial deliberation ('bírói mérlegelés') in a constitutional democracy?",
                        [
                            "It must remain within statutory bounds and respect fundamental constitutional values.",
                            "It can be decided completely arbitrarily based on personal mood.",
                            "It must ignore all written statutes and previous precedents.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A bíróság nem csupán a törvény rideg betűjét, hanem annak alkotmányos ____ is követte. (spirit)",
                        "szellemét",
                        "The court followed not merely the rigid letter of the law, but also its constitutional spirit.",
                        ["b2-legal-normative-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Az ítélet meghozatala előtt a bírónak alaposan ____ kell az enyhítő és súlyosító körülményeket. (to weigh / deliberate)",
                        "mérlegelnie",
                        "Before handing down the judgment, the judge must thoroughly weigh the mitigating and aggravating circumstances.",
                        ["b2-legal-normative-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "jogbiztonság", "nélkül", "nem", "létezhet", "valódi", "jogállamiság."],
                        ["A", "jogbiztonság", "nélkül", "nem", "létezhet", "valódi", "jogállamiság."],
                        "Without legal certainty, true rule of law cannot exist.",
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A váratlan helyzet rávilágított egy korábban ismeretlen ____ fennállására. (legal loophole / statutory lacuna)",
                        "joghézag",
                        "The unexpected situation highlighted the existence of a previously unknown legal loophole.",
                        ["b2-25-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "hatóság", "különös", "méltányosságból", "engedélyezte", "a", "kérelmet."],
                        ["A", "hatóság", "különös", "méltányosságból", "engedélyezte", "a", "kérelmet."],
                        "The authority granted the request out of special equity.",
                        ["b2-25-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Jogtudós", "text": "Hogyan oldható fel az ellentét a törvény betűje és a társadalmi igazságosság között?"},
                            {"speaker": "Bíró", "text": "____"},
                        ],
                        [
                            "A cél szerinti jogértelmezés segítségével, amely a jogalkotó valós szándékát és az Alaptörvény értékeit követi.",
                            "Csak úgy, ha figyelmen kívül hagyjuk a jogszabályokat és sorsolással döntünk.",
                            "A törvény betűje mindig fontosabb, még akkor is, ha teljesen abszurd eredményre vezet.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Miért olyan fontos a jogbiztonság a polgárok számára?"},
                            {"speaker": "Alkotmányjogász", "text": "____"},
                        ],
                        [
                            "Mert a jogbiztonság garantálja, hogy a szabályok előre megismerhetők és a hatóságok nem alkalmazhatnak önkényt.",
                            "Mert a jogbiztonság azt jelenti, hogy soha többé nem hoznak új törvényeket.",
                            "A jogbiztonság csupán egy elméleti fogalom, aminek a gyakorlatban nincs semmi haszna.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence contrasting 'törvény betűje' with 'törvény szelleme' in statutory interpretation.",
                                "answer": "A döntéshozatal során a törvény szellemének kell érvényesülnie a rideg és formális betűvel szemben.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'jogbiztonság' and 'mérlegelés' describing judicial responsibility.",
                                "answer": "A bírói mérlegelés szabadsága soha nem sértheti a jogbiztonság alkotmányos követelményét.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A modern bírói gyakorlatban a nyelvtani mellett a teleologikus ____ is kiemelt szerepet kap. (statutory interpretation)",
                        "jogértelmezés",
                        "In modern judicial practice, teleological statutory interpretation plays a prominent role alongside grammatical interpretation.",
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes judicial fairness and mercy mitigating formal statutory strictness?",
                        ["méltányosság", "önkény", "szigorúság"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Analyzing a Legal Dilemma",
            "grammar_label": "Due process, fundamental rights, and balance of power",
            "goals": [
                "I can analyze constitutional tensions between public authority and civil liberties",
                "I can describe procedural guarantees and due process (tisztességes eljárás)",
                "I can evaluate proportional restrictions on fundamental rights using legal criteria",
            ],
            "grammar_doc": {
                "slug": "due-process-and-fundamental-rights",
                "title": "Due Process, Fundamental Rights, and the Separation of Powers",
                "text1_title": "The Right to Due Process: tisztességes eljárás and jogorvoslat",
                "text1": "Constitutional jurisprudence places the right to a fair procedure ('a tisztességes eljáráshoz való jog') at the core of judicial integrity. Due process guarantees that every party has the right to be heard ('meghallgatáshoz való jog'), access to an independent court ('független és pártatlan bíróság'), and effective legal recourse ('jogorvoslati lehetőség'). Any administrative action restricting civil liberties must remain strictly within designated statutory competence ('hatáskör').",
                "text2_title": "Proportionality and the Restriction of Fundamental Rights: alapjog and arányosság",
                "text2": "Fundamental rights ('alapjogok') may only be restricted when strictly necessary to achieve a legitimate public aim, and only to the extent proportional ('szükségességi és arányossági teszt'). If an administrative agency exceeds its statutory remit ('túllépi a hatáskörét') or infringes an individual's fundamental rights disproportionately, constitutional courts provide judicial annulment: 'Az alapjog korlátozása csak akkor jogszerű, ha arányban áll a védeni kívánt céllal' ('Restriction of a fundamental right is lawful only if it is proportionate to the legitimate aim sought to be protected').",
                "table_title": "Constitutional and Procedural Vocabulary",
                "table_rows": [
                    ["tisztességes eljárás", "az eljárási garanciák maradéktalan érvényesülése (full realization of procedural guarantees)"],
                    ["jogorvoslathoz való jog", "a határozat felettes szerv vagy bíróság előtti megtámadása (right of appeal / legal remedy)"],
                    ["arányosság elve", "a cél és az alkalmazott eszköz közötti egyensúly (balance between legitimate aim and means employed)"],
                    ["hatáskörtúllépés", "a törvény által kijelölt keretek megsértése (ultra vires / exceeding statutory jurisdiction)"],
                ],
                "examples": [
                    {
                        "spanish": "Mindenkinek joga van ahhoz, hogy ügyét a bíróság tisztességes eljárásban bírálja el.",
                        "english": "Everyone has the right to have their case adjudicated by a court in a fair proceeding.",
                    },
                    {
                        "spanish": "Az eljárási garanciák megsértése miatt az ügyfél élt a jogorvoslat lehetőségével.",
                        "english": "Due to the violation of procedural guarantees, the client exercised the option of legal remedy.",
                    },
                    {
                        "spanish": "Az alapjogok bármilyen korlátozásának meg kell felelnie a szükségesség és arányosság tesztjének.",
                        "english": "Any restriction of fundamental rights must satisfy the test of necessity and proportionality.",
                    },
                    {
                        "spanish": "A minisztérium hatáskör hiányában nem hozhatott volna érvényes döntést ebben a kérdésben.",
                        "english": "In the absence of jurisdiction, the ministry could not have made a valid decision on this matter.",
                    },
                ],
                "tip": "Distinguish between 'hatáskör' (subject-matter jurisdiction, e.g. what kind of cases an authority may handle) and 'illetékesség' (territorial jurisdiction, e.g. which geographic court has competence).",
            },
            "words": [
                {"lemma": "tisztességes eljárás", "translation": "due process / fair procedure", "pos": "expression"},
                {"lemma": "alapjog", "translation": "fundamental right", "pos": "noun"},
                {"lemma": "arányosság", "translation": "proportionality", "pos": "noun"},
                {"lemma": "hatáskör", "translation": "jurisdiction / scope of authority", "pos": "noun"},
                {"lemma": "jogorvoslat", "translation": "legal remedy / right of appeal", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'tisztességes eljárás' mean in constitutional and human rights law?",
                        [
                            "due process and the right to a fair and public trial before an impartial court",
                            "a polite way of addressing county dignitaries at public banquets",
                            "an informal negotiation where no records or protocols are kept",
                        ],
                        0,
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the constitutional right to appeal an adverse administrative or judicial decision?",
                        ["jogorvoslat", "jogalap", "jogszokás"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["tisztességes eljárás", "due process / fair trial"],
                            ["alapjog", "fundamental right"],
                            ["arányosság", "proportionality"],
                            ["hatáskör", "scope of authority / jurisdiction"],
                            ["jogorvoslat", "legal remedy / appeal"],
                        ],
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "When can a public authority lawfully restrict a citizen's fundamental right ('alapjog')?",
                        [
                            "Only if the restriction is strictly necessary, serves a legitimate aim, and satisfies proportionality.",
                            "Whenever an administrative official considers it convenient for tax collection.",
                            "Under no circumstances whatsoever, even in emergency civil defense.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What occurs when an administrative agency acts beyond its statutory competence?",
                        [
                            "It commits hatáskörtúllépés (exceeding its statutory jurisdiction), rendering its decision unlawful.",
                            "Its decision automatically becomes unchallengeable constitutional doctrine.",
                            "It receives an official award from the bar association.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A közigazgatási határozattal szemben az ügyfél harminc napon belül bírósági ____ élhet. (with legal remedy)",
                        "jogorvoslattal",
                        "Against the administrative decision, the client may seek legal remedy in court within thirty days.",
                        ["b2-legal-normative-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A hatósági beavatkozás mértéke nem sértette az alkotmányos ____ követelményét. (proportionality)",
                        "arányosság",
                        "The extent of the official intervention did not violate the requirement of constitutional proportionality.",
                        ["b2-legal-normative-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Minden", "állampolgárnak", "joga", "van", "a", "tisztességes", "eljáráshoz."],
                        ["Minden", "állampolgárnak", "joga", "van", "a", "tisztességes", "eljáráshoz."],
                        "Every citizen has the right to due process.",
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A véleménynyilvánítás szabadsága a demokratikus társadalmak egyik legfontosabb ____. (fundamental right)",
                        "alapjoga",
                        "Freedom of expression is one of the most important fundamental rights of democratic societies.",
                        ["b2-25-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "polgármesteri", "hivatal", "túllépte", "törvényes", "hatáskörét", "az", "ügyben."],
                        ["A", "polgármesteri", "hivatal", "túllépte", "törvényes", "hatáskörét", "az", "ügyben."],
                        "The mayor's office exceeded its statutory jurisdiction in the matter.",
                        ["b2-25-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Jogvédő", "text": "Miért fordultak az Alkotmánybírósághoz a vitatott törvény ügyében?"},
                            {"speaker": "Ügyvéd", "text": "____"},
                        ],
                        [
                            "Mert a jogszabály aránytalanul korlátozza az állampolgárok alapjogait és sérti a tisztességes eljárás elvét.",
                            "Mert nem tetszett a parlamenti vita hangneme, de jogi érvünk nincs.",
                            "A hatáskör hiányában mindenki elégedett volt a helyzettel.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Alperes", "text": "Van még lehetőségünk fellépni az elsőfokú döntés ellen?"},
                            {"speaker": "Jogtanácsos", "text": "____"},
                        ],
                        [
                            "Természetesen, a törvény biztosítja a jogorvoslat jogát, így tizenöt napon belül fellebbezést nyújtunk be.",
                            "Semmilyen lehetőség nincs, mert a bíró döntése ellen tilos beszélni.",
                            "Nem nyújtunk be semmit, mert az arányosság elve tiltja a fellebbezést.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'tisztességes eljárás' asserting procedural rights before an administrative tribunal.",
                                "answer": "Az eljárás alá vont személynek alapvető joga van a tisztességes eljáráshoz és a védelemhez.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'arányosság' and 'alapjog' regarding legislative limits.",
                                "answer": "Az állam kizárólag a szükségesség és arányosság alkotmányos elvével összhangban korlátozhat alapjogokat.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A felügyeleti szerv megállapította, hogy az alsóbb szintű hatóság túllépte törvényes ____. (scope of authority / jurisdiction)",
                        "hatáskörét",
                        "The supervisory body determined that the lower-level authority exceeded its statutory jurisdiction.",
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the constitutional mechanism by which aggrieved parties contest an administrative order?",
                        ["jogorvoslat", "jogerő", "jogviszony"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Drafting a Formal Petition or Legal Argument",
            "grammar_label": "Writing a structured legal plea or petition",
            "goals": [
                "I can structure formal legal pleadings and submissions (keresetlevél, beadvány)",
                "I can articulate factual background and statutory justification (tényállás, indokolás)",
                "I can formulate binding petitions and formal motions (indítványoz, kérelmez)",
            ],
            "grammar_doc": {
                "slug": "drafting-formal-legal-arguments",
                "title": "Drafting Formal Pleadings and Petitions: keresetlevél, tényállás, indokolás",
                "text1_title": "The Structural Anatomy of a Legal Plea: keresetlevél",
                "text1": "A formal Hungarian statement of claim ('keresetlevél') or administrative petition ('beadvány') follows a rigid three-part architecture: (1) identification of parties and jurisdiction; (2) the statement of facts ('tényállás'), presenting historical events chronologically without legal embellishment; and (3) the legal reasoning ('érdemi indokolás'), citing exact statutory provisions violated and linking evidence to statutory thresholds.",
                "text2_title": "Petitory Formulas and Legal Finality: indítványoz and jogerős",
                "text2": "The operative prayer for relief relies on prescriptive performative verbs such as 'indítványoz' ('petitions / motions') and 'kéri a bíróságtól' ('requests the court'). Once all appellate remedies are exhausted or deadlines lapse without challenge, a judicial ruling becomes final and legally binding ('jogerős'), acquiring the status of res judicata: 'A határozat fellebbezés hiányában jogerőre emelkedett' ('In the absence of an appeal, the decision became final and binding').",
                "table_title": "Key Procedural Terms in Pleadings",
                "table_rows": [
                    ["keresetlevél", "a bírósági eljárást megindító hivatalos irat (formal statement of claim initiating proceedings)"],
                    ["tényállás", "a releváns valós események pontos rögzítése (factual background / statement of facts)"],
                    ["indokolás", "a jogi érvek és jogszabályi hivatkozások kifejtése (statement of reasons / legal justification)"],
                    ["jogerős ítélet", "további rendes jogorvoslattal nem támadható döntés (final and non-appealable judgment)"],
                ],
                "examples": [
                    {
                        "spanish": "A felperes a keresetlevélben részletesen előadta a követelésének alapjául szolgáló tényállást.",
                        "english": "In the statement of claim, the plaintiff set forth in detail the facts serving as the basis for the claim.",
                    },
                    {
                        "spanish": "Az alperes ügyvédje a bizonyítékok elégtelenségére hivatkozva a per megszüntetését indítványozta.",
                        "english": "Citing insufficiency of evidence, the defendant's attorney motioned for dismissal of the lawsuit.",
                    },
                    {
                        "spanish": "A bíróság határozata az indokolásban részletesen kitér a felek jogi érveire.",
                        "english": "The court's decree addresses the parties' legal arguments in detail in its reasoning.",
                    },
                    {
                        "spanish": "A fellebbviteli bíróság helybenhagyta az elsőfokú döntést, így az ítélet jogerőssé vált.",
                        "english": "The appellate court affirmed the first-instance decision, thus the judgment became final and binding.",
                    },
                ],
                "tip": "In formal petitions, maintain passive or impersonal third-person register: write 'A felperes tisztelettel indítványozza...' ('The plaintiff respectfully motions...') rather than first-person colloquial expressions.",
            },
            "words": [
                {"lemma": "keresetlevél", "translation": "statement of claim / formal petition", "pos": "noun"},
                {"lemma": "tényállás", "translation": "statement of facts / factual circumstance", "pos": "noun"},
                {"lemma": "indokolás", "translation": "statement of reasons / legal grounds", "pos": "noun"},
                {"lemma": "indítványoz", "translation": "to petition / motion / formally request", "pos": "verb"},
                {"lemma": "jogerős", "translation": "final and binding / non-appealable", "pos": "adjective"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'keresetlevél' in civil judicial proceedings?",
                        [
                            "the formal statement of claim by which the plaintiff commences a lawsuit in court",
                            "an informal letter written to a newspaper editorial board",
                            "a receipt issued by a notary public confirming payment of fees",
                        ],
                        0,
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective describes a judicial decision that can no longer be challenged by regular appeal?",
                        ["jogerős", "ideiglenes", "fellebbezhető"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["keresetlevél", "statement of claim"],
                            ["tényállás", "statement of facts"],
                            ["indokolás", "statement of reasons"],
                            ["indítványoz", "to motion / petition"],
                            ["jogerős", "final and binding"],
                        ],
                        ["b2-25-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which section of a formal petition contains the chronological description of relevant events?",
                        ["a tényállás", "a záróformula", "a perköltség-jegyzék"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the formal performative verb for submitting an evidentiary motion to court:",
                        ["indítványoz", "remél", "gondol"],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A bíróság az eljárás megszüntetését ____ az alperes kérelmére. (formally ordered / decided; use verb: indítványozta)",
                        "indítványozta",
                        "The party motioned for the termination of the proceedings at the defendant's request.",
                        ["b2-legal-normative-register"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A fellebbezési határidő eredménytelen leteltét követően a határozat ____ emelkedett. (became final and binding)",
                        "jogerőre",
                        "Following the expiration of the appeal deadline without result, the decision became final and binding.",
                        ["b2-legal-normative-register"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "felperes", "a", "keresetlevélben", "részletesen", "bemutatta", "a", "tényállást."],
                        ["A", "felperes", "a", "keresetlevélben", "részletesen", "bemutatta", "a", "tényállást."],
                        "The plaintiff presented the statement of facts in detail in the statement of claim.",
                        ["b2-legal-normative-register"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A bírói döntés érdemi része az eljárásjogi és anyagi jogi ____ alapul. (statement of reasons / legal justification)",
                        "indokoláson",
                        "The substantive part of the judicial decision is grounded on procedural and substantive legal reasoning.",
                        ["b2-25-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "ítélet", "jogerőre", "emelkedése", "után", "megkezdődhet", "a", "végrehajtás."],
                        ["Az", "ítélet", "jogerőre", "emelkedése", "után", "megkezdődhet", "a", "végrehajtás."],
                        "After the judgment becomes final and binding, enforcement may begin.",
                        ["b2-25-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyvédjelölt", "text": "Hogyan építsük fel a bírósághoz benyújtandó beadványt?"},
                            {"speaker": "Vezető ügyvéd", "text": "____"},
                        ],
                        [
                            "Először rögzítsük pontosan a valós tényállást, majd fejtsük ki a jogszabályi indokolást, és indítványozzuk a kártérítést.",
                            "Csak a véleményünket írjuk le, a jogszabályok hivatkozásával nem érdemes vesződni.",
                            "A jogerős ítéletet küldjük el válaszként még a per megindítása előtt.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ügyfél", "text": "Mikor tekinthető véglegesnek a bíróság által hozott döntés?"},
                            {"speaker": "Jogtanácsos", "text": "____"},
                        ],
                        [
                            "Amikor az ítélet jogerőre emelkedik, és ellene rendes jogorvoslatnak már nincs helye.",
                            "Azonnal a tárgyalás első öt percében, függetlenül a bizonyítékoktól.",
                            "Csak akkor, ha a felek baráti kezet nyújtanak egymásnak a folyosón.",
                        ],
                        0,
                        ["b2-legal-normative-register"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal petitory clause using 'indítványoz' requesting witness testimony in court.",
                                "answer": "A felperes tisztelettel indítványozza a megjelölt tanúk bírósági meghallgatását a tényállás tisztázása céljából.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence with 'jogerős' describing the legal effect of an appellate decision.",
                                "answer": "A másodfokú bíróság határozatának kihirdetésével az ítélet jogerőssé és végrehajthatóvá vált.",
                            }
                        ],
                        ["b2-legal-normative-register"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A beadvány készítője a rendelkezésre álló iratok alapján vázolta fel a perbeli ____. (statement of facts)",
                        "tényállást",
                        "The author of the petition outlined the facts at issue in the lawsuit based on the available documents.",
                        ["b2-legal-normative-register"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which formal document serves to institute a civil contentious proceeding in court?",
                        ["keresetlevél", "jegyzőkönyv", "értesítés"],
                        0,
                        ["b2-25-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can confidently apply legal and normative syntax (alapján, összhangban, sérelmére, terhére)",
            "I can formulate statutory rights and obligations using jogosult, köteles, and -andó/-endő",
            "I can draft structured legal arguments integrating due process, statutory interpretation, and formal petitions",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["jogszabály", "statute / legal rule"],
                    ["hatályos", "in force / effective"],
                    ["jogbiztonság", "legal certainty"],
                    ["tisztességes eljárás", "due process"],
                    ["jogerős", "final and binding"],
                ],
                ["b2-25-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'joghézag' signify in jurisprudence?",
                [
                    "an unintentional gap in statutory legislation where a norm is required but absent",
                    "a spatial boundary dispute between neighboring municipalities",
                    "a typographical error in the official parliamentary gazette",
                ],
                0,
                ["b2-25-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates statutory obligation with a prescriptive participle?",
                [
                    "A szerződésben rögzített feltételek minden fél számára kötelezően betartandók.",
                    "A szerződésben rögzített feltételek ha betartotta volna tegnap.",
                    "Betartandó a szerződés mert senki sem akart olvasni semmit.",
                ],
                0,
                ["b2-legal-normative-register"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A közigazgatási határozat ellen a felperes harminc napon belül ____ terjesztett elő. (statement of claim / formal petition)",
                "keresetlevelet",
                "Against the administrative decision, the plaintiff filed a statement of claim within thirty days.",
                ["b2-25-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A hatósági intézkedés a jogszabály egyértelmű rendelkezései ____ történt. (on the basis of)",
                "alapján",
                "The official measure took place on the basis of the clear provisions of the statute.",
                ["b2-legal-normative-register"],
            ),
            fb(
                "grammar",
                "recall",
                "A munkáltató a törvény erejénél fogva ____ a biztonságos munkakörülmények garantálására. (obligated / duty-bound)",
                "köteles",
                "By virtue of law, the employer is obligated to guarantee safe working conditions.",
                ["b2-legal-normative-register"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'sérelmére' correctly denotes legal prejudice:",
                [
                    "Az egyoldalú szerződésmódosítás a fogyasztó törvényes jogainak sérelmére történt.",
                    "A törvény sérelmére mindenki vidáman ünnepelt a városházán tegnap.",
                    "A sérelmére megírtuk a leckét anélkül, hogy hibáztunk volna.",
                ],
                0,
                ["b2-legal-normative-register"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Alkotmánybíró", "text": "Hogyan ítéli meg a vitatott törvénymódosítás alkotmányosságát?"},
                    {"speaker": "Szakértő", "text": "____"},
                ],
                [
                    "A jogszabály sérti a jogbiztonság követelményét, mivel nem áll összhangban az Alaptörvény tisztességes eljárásra vonatkozó garanciáival.",
                    "Nem foglalkozunk a törvénnyel, mert a vármegyei jegyző már hazament a faluba.",
                    "Minden jogszabály tökéletes, függetlenül attól, hogy mit tartalmaz.",
                ],
                0,
                ["b2-legal-normative-register"],
            ),
            mc(
                "grammar",
                "in-context",
                "Why is 'jogosult + infinitive' preferred over 'kell' in statutory drafting?",
                [
                    "Because it explicitly assigns a subjective legal entitlement to an authorized party rather than stating an impersonal necessity.",
                    "Because 'kell' cannot be used with past tense verbs in Hungarian.",
                    "Because 'jogosult' is an archaic noun only found in 19th-century novels.",
                ],
                0,
                ["b2-legal-normative-register"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "rendeletnek", "teljes", "összhangban", "kell", "állnia", "az", "Alaptörvénnyel."],
                ["A", "rendeletnek", "teljes", "összhangban", "kell", "állnia", "az", "Alaptörvénnyel."],
                "The decree must stand in full accordance with the Basic Law.",
                ["b2-legal-normative-register"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "bírósági", "ítélet", "jogerőre", "emelkedése", "után", "megindult", "a", "végrehajtás."],
                ["A", "bírósági", "ítélet", "jogerőre", "emelkedése", "után", "megindult", "a", "végrehajtás."],
                "Following the judgment becoming final and binding, enforcement commenced.",
                ["b2-legal-normative-register"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause legal argument combining 'alapján' (statutory ground), 'köteles' (obligation), and 'jogerős' (binding judgment).",
                        "answer": "A hatályos jogszabály alapján az alperes köteles megtéríteni az okozott kárt; amennyiben a fellebbezési határidő letelt, a bíróság jogerős ítélete haladéktalanul végrehajthatóvá válik.",
                    }
                ],
                ["b2-legal-normative-register"],
            ),
        ],
    },
}
