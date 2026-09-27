"""
Hungarian B2 Core Track Unit 32:
  b2-32: Competition, Mastery & Peak Performance
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_32 = {
    "unit_num": 32,
    "title": "Competition, Mastery & Peak Performance",
    "grammar_summary": "Consecutive clauses of degree and result (olyannyira ..., hogy; oly mértékben ..., hogy) and preverbs of dynamic athletic action (lefut, átvesz, kicselez, belő).",
    "grammar_skill": "b2-consecutive-degree",
    "vocab_skill": "b2-32-vocab",
    "theme": "Competition, mastery and peak performance",
    "intro_body": [
        "A sport és a versengés világa az emberi teljesítőképesség határait kutatja, ahol a fizikai erőnlét a pszichológiai állóképességgel és a taktikai intelligenciával fonódik össze. A magyar kultúrában az olimpiai sikerek, a labdarúgás legendás pillanatai és a sportirodalom – Esterházy Pétertől Mándy Ivánig – kiemelt helyet foglalnak el.",
        "Ebben a fejezetben megismerkedhet az intenzív fok- és következményhatározói mellékmondatokkal (olyannyira ..., hogy; oly mértékben ..., hogy), a dinamikus sportbeli cselekvést kifejező igekötőkkel (lefut, átvesz, kicselez, belő), valamint a csapatszellem, a taktikai fegyelem, a kudarckezelés és az élő mérkőzésközvetítés választékos szókincsével.",
    ],
    "classic_story": {
        "slug": "utazasatizenhatos",
        "author": "Esterházy Péter",
        "work": "Utazás a tizenhatos mélyére (2006)",
        "title": "A labda íve és a pálya geometriája",
        "summary": "Esterházy Péter és a rutinos kapus a büntetőterület különös geometriájáról, a kapus magányáról és a labda röppályájának kiszámíthatatlan szépségéről elmélkednek az üres stadionban.",
        "characters": ["Esterházy Péter", "A kapus"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kora esti órákban a néptelen stadionban a frissen nyírt fű illata keveredett a hűvösödő széllel. Esterházy Péter a tizenhatos mészvonalán állva a fehér kapufát nézte; a futball számára soha nem puszta sport volt, hanem a létezés geometriája, a test és a nyelv közös játéka.",
            },
            {
                "type": "dialogue",
                "speaker": "A kapus",
                "text": "Péter, az ember azt hinné, hogy a tizenhatoson belül a kapus az úr, de a valóságban ez a legmagányosabb hely a világon. Amikor a csatár feléd robog, a másodperc törtrésze alatt kell döntened, miközben a tér összezsugorodik körülötted.",
            },
            {
                "type": "dialogue",
                "speaker": "Esterházy Péter",
                "text": "A kapus magánya valóban metafizikai természetű. A csatár hibázhat tízszer is, ha a tizenegyedik lövést belövi; a kapus viszont, ha egyszer vét, máris bűnbakká válik a lelátó szemében. A labda íve pedig könyörtelen, nem ismer kompromisszumot.",
            },
            {
                "type": "narration",
                "text": "A kapus elmosolyodott, felkapta a kopott bőrlabdát, és könnyedén feldobta a levegőbe. Évtizedes reflexek mozdultak az ujjaiban; olyannyira megszokta a labda súlyát és röppályáját, hogy behunyt szemmel is pontosan meg tudta volna mondani, hol ér majd földet a zöld gyepen.",
            },
            {
                "type": "dialogue",
                "speaker": "Esterházy Péter",
                "text": "Nézd, ahogy a gyors szélső lefutja a védőt, vagy ahogy az irányító egyetlen finom érintéssel átveszi az indítást és azonnal kicselezi a kapust! Ez nem csupán izommunka; ez tiszta gondolkodás, geometriai intuíció és költészet.",
            },
            {
                "type": "dialogue",
                "speaker": "A kapus",
                "text": "Valóban, a csúcsteljesítményhez nem elég a puszta állóképesség. Oly mértékben kell összpontosítani a kilencven perc során, hogy a külvilág zaja teljesen elnémuljon. Csak a labda létezik, a társak mozgása és az üres terek ritmusa.",
            },
            {
                "type": "narration",
                "text": "Az alkony lassan árnyékba borította a lelátókat. A két férfi némán figyelte a pálya közepén heverő labdát; a sport és az irodalom ebben a pillanatban egymásra talált a mozdulatok fegyelmében és a vereség utáni talpra állás méltóságában.",
            },
            {
                "type": "narration",
                "text": "Esterházy zsebre dugta a kezét, és lassan megindult az öltözőfolyosó felé. Tudta, hogy a mérkőzés lezárulhat sípszóval, a tabella rögzítheti a pontokat, de a játék igazi titka – a mozdulat tökéletessége és az emberi küzdelem szépsége – megfoghatatlan marad mindörökre.",
            },
        ],
        "reading_questions": [
            {
                "question": "Hogyan értelmezi Esterházy Péter a futballpályát és a játékot a szövegben?",
                "options": [
                    "A létezés geometriájaként, ahol a fizikai mozgás, a gondolkodás és a költészet találkozik.",
                    "Pusztán gazdasági vállalkozásként, amely a televíziós jogdíjakból él.",
                    "Szabálytalan harcként, ahol csak a nyers fizikai erőszak számít.",
                ],
                "correct": 0,
            },
            {
                "question": "Miért tekinti a kapus a büntetőterületet a legmagányosabb helynek a világon?",
                "options": [
                    "Mert egyetlen hibája azonnal gólt eredményez, míg a csatárnak több rontás is megbocsátható.",
                    "Mert a kapusnak tilos beszélnie a csapattársaival a szabályok szerint.",
                    "Mert a kapus soha nem kap fizetést a klubvezetéstől.",
                ],
                "correct": 0,
            },
            {
                "question": "Mit tartanak a szereplők elengedhetetlennek a csúcsteljesítmény eléréséhez?",
                "options": [
                    "Az abszolút mentális fókuszt és geometriai intuíciót, amely kizárja a külvilág zaját.",
                    "A folyamatos veszekedést a játékvezetővel a döntések megváltoztatása érdekében.",
                    "A meccs előtti nehéz, zsíros ételek bőséges fogyasztását.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Degree and Result Clauses (olyannyira ..., hogy; oly mértékben ..., hogy)",
            "grammar_label": "Consecutive clauses of degree and extreme extent (olyannyira ..., hogy; oly mértékben ..., hogy)",
            "goals": [
                "I can form consecutive clauses of extreme degree using olyannyira ..., hogy",
                "I can construct formal result sentences measuring extent with oly mértékben ..., hogy",
                "I can express intense athletic fatigue, endurance, and performance limits",
            ],
            "grammar_doc": {
                "slug": "consecutive-degree-clauses-intensity",
                "title": "Consecutive Clauses of Degree: olyannyira ..., hogy & oly mértékben ..., hogy",
                "text1_title": "Expressing Extreme Extent and Result",
                "text1": "In Hungarian complex sentences, consecutive clauses (következményes mellékmondatok) link a cause of extreme intensity in the main clause to its resulting effect in the subordinate clause introduced by 'hogy'. At the B2 level, conversational 'annyira ..., hogy' is elevated to formal demonstrative correlatives: 'olyannyira ..., hogy' (so very much that) and 'oly mértékben ..., hogy' (to such an extent / in such degree that).",
                "text2_title": "Syntactic Position and Emphasis",
                "text2": "The correlatives 'olyannyira' and 'oly mértékben' typically precede the focused verb or adjective in the main clause: 'A futó olyannyira kimerült a maraton végére, hogy alig tudott talpon maradni' (The runner was exhausted to such an extent that he could barely stay on his feet). In formal academic and journalistic texts, 'oly mértékben ..., hogy' is preferred when quantifying sociological, athletic, or physiological phenomena.",
                "table_title": "Consecutive Correlatives Matrix",
                "table_rows": [
                    ["olyannyira ..., hogy", "Olyannyira gyors volt a támadás, hogy a védelem nem tudott reagálni. (So fast that... )"],
                    ["oly mértékben ..., hogy", "Oly mértékben növelték az intenzitást, hogy minden rekord megdőlt. (To such an extent that... )"],
                    ["olyan fokon ..., hogy", "Olyan fokon sajátította el a technikát, hogy hibátlanul játszott. (At such a level that... )"],
                    ["annyira ..., hogy (neutral)", "Annyira elfáradt az edzésen, hogy azonnal elaludt. (So tired that... )"],
                ],
                "examples": [
                    {
                        "spanish": "A mérkőzés hajrájában a játékosok olyannyira kimerültek, hogy mindkét csapat a védekezésre rendezkedett be.",
                        "english": "In the final stretch of the match, the players were so exhausted that both teams settled into defending.",
                    },
                    {
                        "spanish": "Az edző oly mértékben bízott a fiatal tehetségben, hogy a döntőben is a kezdőcsapatba állította.",
                        "english": "The coach trusted the young talent to such an extent that he placed him in the starting lineup in the final as well.",
                    },
                    {
                        "spanish": "A sportoló állóképessége olyannyira kimagasló volt, hogy az utolsó kilométeren könnyedén lehagyta ellenfeleit.",
                        "english": "The athlete's endurance was so outstanding that on the final kilometer he easily outpaced his rivals.",
                    },
                    {
                        "spanish": "A felkészülés során a terhelés oly mértékben megnőtt, hogy külön orvosi stábra volt szükség a regenerációhoz.",
                        "english": "During preparation, the physical load increased to such an extent that a dedicated medical staff was needed for recovery.",
                    },
                ],
                "tip": "Always write 'olyannyira' as a single compound word. Do not place a comma between 'oly' and 'annyira', but always place a comma before the conjunction 'hogy'.",
            },
            "words": [
                {"lemma": "olyannyira", "translation": "so much / to such an extent", "pos": "adverb"},
                {"lemma": "oly mértékben", "translation": "to such an extent / in such degree", "pos": "expression"},
                {"lemma": "kimerültség", "translation": "exhaustion / fatigue", "pos": "noun"},
                {"lemma": "csúcsteljesítmény", "translation": "peak performance", "pos": "noun"},
                {"lemma": "állóképesség", "translation": "endurance / stamina", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'olyannyira' express in complex sentence structures?",
                        [
                            "an extreme degree or extent that produces a specific consequence",
                            "a vague and uncertain temporal delay",
                            "a total denial or contradiction of a prior claim",
                        ],
                        0,
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun denotes maximum athletic output and physical excellence?",
                        ["csúcsteljesítmény", "kimerültség", "szabálytalanság"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["olyannyira", "so much / to such an extent"],
                            ["oly mértékben", "to such an extent / degree"],
                            ["kimerültség", "exhaustion / fatigue"],
                            ["csúcsteljesítmény", "peak performance"],
                            ["állóképesség", "endurance / stamina"],
                        ],
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which correlative pair forms a consecutive sentence: 'A ritmus ____ felgyorsult, ____ a nézők alig győzték követni'?",
                        ["olyannyira ... hogy", "bár ... de", "nemcsak ... hanem"],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence correctly punctuated and structured with 'oly mértékben ..., hogy':",
                        [
                            "A sportoló oly mértékben összpontosított, hogy a közönség moraját sem hallotta.",
                            "A sportoló oly mértékben összpontosított hogy, a közönség moraját sem hallotta.",
                            "A sportoló oly, mértékben összpontosított hogy a közönség moraját sem hallotta.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A maratonfutó ____ kimerült a célvonal előtt, hogy az orvosoknak kellett felsegíteniük. (to such an extent)",
                        "olyannyira",
                        "The marathon runner was exhausted to such an extent before the finish line that doctors had to help him up.",
                        ["b2-consecutive-degree"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A bajnokság döntőjében a csapatok ____ mértékben küzdöttek a győzelemért, hogy több játékos megsérült. (in such)",
                        "oly",
                        "In the championship final the teams fought for victory in such degree that several players got injured.",
                        ["b2-consecutive-degree"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "versenyző", "olyannyira", "felgyorsított,", "hogy", "világcsúcsot", "döntött", "a", "döntőben."],
                        ["A", "versenyző", "olyannyira", "felgyorsított,", "hogy", "világcsúcsot", "döntött", "a", "döntőben."],
                        "The competitor accelerated to such an extent that he broke the world record in the final.",
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A hegyi terepfutáshoz nemcsak gyorsaság, hanem rendkívüli fizikai ____ is szükséges. (endurance)",
                        "állóképesség",
                        "For mountain trail running not only speed but also extraordinary physical endurance is required.",
                        ["b2-32-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szigorú", "diéta", "és", "edzésmunka", "eredményeként", "csúcsteljesítményt", "ért", "el."],
                        ["A", "szigorú", "diéta", "és", "edzésmunka", "eredményeként", "csúcsteljesítményt", "ért", "el."],
                        "As a result of the strict diet and training work, he achieved peak performance.",
                        ["b2-32-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Sportriporter", "text": "Hogyan bírta az olimpikon az utolsó száz métert a döntőben?"},
                            {"speaker": "Edző", "text": "____"},
                        ],
                        [
                            "Olyannyira hatalmas volt benne a győzni akarás, hogy a fizikai kimerültség ellenére is meg tudta előzni a riválisát.",
                            "Azonnal feladta a versenyt a rajt után, mert elfáradt a cipőfűzésben.",
                            "Nem indult el a döntőben, mert inkább elment fagyizni a belvárosba.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Sportorvos", "text": "Milyen hatással van a túledzettség az élsportolók szervezetére?"},
                            {"speaker": "Fiziológus", "text": "____"},
                        ],
                        [
                            "A regeneráció hiánya oly mértékben rontja az állóképességet, hogy a sérülésveszély drasztikusan megugrik.",
                            "A sportolóknak soha nincs szükségük alvásra vagy pihenésre a tudomány szerint.",
                            "A kimerültség csupán képzeletbeli illúzió, amit vitaminokkal meg lehet szüntetni tíz másodperc alatt.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a consecutive sentence using 'olyannyira ..., hogy' describing athletic stamina.",
                                "answer": "A triatlonista állóképessége olyannyira legendás volt, hogy az embert próbáló verseny után sem látszott rajta a kimerültség.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'oly mértékben ..., hogy' to explain tactical discipline.",
                                "answer": "A védők oly mértékben tartották a taktikai fegyelmet, hogy az ellenfél egyetlen kapura lövést sem tudott felmutatni.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A kapus reakcióideje ____ gyors volt, hogy a közeli fejest is szögletre tudta tolni. (so much)",
                        "olyannyira",
                        "The goalkeeper's reaction time was so fast that he was able to tip even the close-range header for a corner.",
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which word describes the profound physical and mental depletion following extreme exertion?",
                        ["kimerültség", "frissesség", "állóképesség"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Preverb Aspect in Dynamic Action (lefut, átvesz, kicselez, belő)",
            "grammar_label": "Rapid aspectual shifts and directional verbal prefixes in athletics (lefut, átvesz, kicselez, belő)",
            "goals": [
                "I can describe rapid athletic maneuvers using dynamic aspectual preverbs (lefut, átvesz, kicselez, belő)",
                "I can distinguish continuous motion from sudden perfective actions on the field",
                "I can narrate fast-paced sports sequences with accurate preverb placement",
            ],
            "grammar_doc": {
                "slug": "dynamic-preverb-aspect-athletics",
                "title": "Dynamic Verbal Prefixes in Sports: lefut, átvesz, kicselez, belő",
                "text1_title": "Aspectual Shifts in High-Speed Athletics",
                "text1": "Hungarian sports narration relies heavily on verbal prefixes (igekötők) to capture rapid transitions, directional changes, and the decisive culmination of motion. The base verbs (fut, vesz, cselez, lő) denote ongoing, imperfective physical activities; adding preverbs instantaneously shifts them into telic, perfective events where a specific spatial obstacle or defensive barrier is conquered.",
                "text2_title": "Core Dynamic Preverb Collocations in Sports",
                "text2": "Key collocations include: 'lefutja a védőt' (outruns the defender, where 'le-' emphasizes leaving behind or conquering in a sprint); 'átveszi a labdát' (receives/controls the ball, crossing from sender to recipient); 'kicselezi a kapust' (dribbles past / tricks out the goalkeeper, where 'ki-' expresses evasion); 'belövi a labdát a hálóba' (shoots the ball into the net); and 'felgyorsít' (accelerates). When an auxiliary or modal verb is present, the preverb detaches according to Hungarian word order rules ('át tudta venni', 'nem cselezte ki').",
                "table_title": "Dynamic Preverb Contrasts in Athletics",
                "table_rows": [
                    ["lefut", "A gyors szélső könnyedén lefutotta a nehézkes középhátvédet. (Outran the defender.)"],
                    ["átvesz", "Mellre vette a negyvenméteres indítást, és tisztán átvette. (Controlled the pass.)"],
                    ["kicselez", "Egyetlen testcsellel kicselezte a rátámadó bekkeket. (Outmaneuvered the backs.)"],
                    ["belő", "Hidegvérrel belőtte a tizenegyest a jobb alsó sarokba. (Shot in the penalty.)"],
                ],
                "examples": [
                    {
                        "spanish": "A csatár lefutotta az egész védelmet, kicselezte a kifutó kapust, és higgadtan belőtte a labdát az üres kapuba.",
                        "english": "The striker outran the entire defense, dribbled past the onrushing goalkeeper, and calmly slotted the ball into the empty net.",
                    },
                    {
                        "spanish": "A középpályás kiváló ütemben vette át a passzt, majd azonnal felgyorsított a kapu felé.",
                        "english": "The midfielder received the pass in excellent rhythm, then immediately accelerated toward the goal.",
                    },
                    {
                        "spanish": "Nem volt könnyű átvenni a lepattanó labdát a csúszós, vizes füvön.",
                        "english": "It was not easy to control the bouncing ball on the slippery, wet grass.",
                    },
                    {
                        "spanish": "A tehetséges szélső olyannyira felgyorsított a szélen, hogy senki sem tudta feltartóztatni.",
                        "english": "The talented winger accelerated so much on the flank that nobody could hold him back.",
                    },
                ],
                "tip": "Observe transitivity: 'fut' (to run) is intransitive, but 'lefut vkit' (to outrun someone) is transitive and takes a direct object in the accusative ('lefutotta a védőt'). Similarly, 'cselez' is intransitive, but 'kicselez vkit' takes an accusative object ('kicselezte a kapust').",
            },
            "words": [
                {"lemma": "lefut", "translation": "to outrun / sprint past", "pos": "verb"},
                {"lemma": "átvesz", "translation": "to receive / control (a ball/lead)", "pos": "verb"},
                {"lemma": "kicselez", "translation": "to outmaneuver / dribble past", "pos": "verb"},
                {"lemma": "belő", "translation": "to shoot in / score", "pos": "verb"},
                {"lemma": "felgyorsít", "translation": "to accelerate / speed up", "pos": "verb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which verb means to outpace or outrun an opponent on the athletic field?",
                        ["lefut", "átvesz", "belő"],
                        0,
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'kicselez' mean when a striker faces a goalkeeper?",
                        [
                            "to outmaneuver or dribble past the goalkeeper using deceptive body motion",
                            "to kick the ball out of the stadium intentionally",
                            "to ask the referee for permission to leave the pitch",
                        ],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["lefut", "to outrun / sprint past"],
                            ["átvesz", "to receive / control"],
                            ["kicselez", "to outmaneuver / dribble past"],
                            ["belő", "to shoot in / score"],
                            ["felgyorsít", "to accelerate"],
                        ],
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Where does the preverb move in negative sentences with dynamic verbs: 'A csatár nem ____ a kapust'?",
                        ["cselezte ki", "kicselezte", "ki nem cselezte"],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence demonstrating correct consecutive degree with athletic motion:",
                        [
                            "A szélső olyannyira felgyorsított, hogy könnyedén lefutotta a védőjét.",
                            "A szélső olyannyira felgyorsított hogy könnyedén lefutott a védőjét.",
                            "A szélső olyannyira felgyorsított, hogy könnyedén lefut a védőjét.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A támadó egy pontos passzt kapott, és a tizenhatos vonaláról a hálóba ____ a labdát. (shot in)",
                        "belőtte",
                        "The attacker received an accurate pass and shot the ball into the net from the eighteen-yard line.",
                        ["b2-consecutive-degree"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A villámgyors futó az utolsó kanyarban teljesen ____ a mezőnyt. (outran / left behind)",
                        "lefutotta",
                        "The lightning-fast runner completely outran the field in the final bend.",
                        ["b2-consecutive-degree"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "középpályás", "hibátlanul", "átvette", "a", "hosszú", "keresztpasszt."],
                        ["A", "középpályás", "hibátlanul", "átvette", "a", "hosszú", "keresztpasszt."],
                        "The midfielder received the long cross pass faultlessly.",
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A csatár a büntetőterületen belül két védőt is ügyesen ____, mielőtt kapura lőtt volna. (dribbled past)",
                        "kicselezett",
                        "Inside the penalty box the striker skillfully dribbled past two defenders before shooting on goal.",
                        ["b2-32-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "sprinter", "hirtelen", "felgyorsított", "a", "célegyenesben."],
                        ["A", "sprinter", "hirtelen", "felgyorsított", "a", "célegyenesben."],
                        "The sprinter suddenly accelerated in the home straight.",
                        ["b2-32-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kommentátor", "text": "Hogyan született meg a mérkőzést eldöntő győztes gól a hosszabbításban?"},
                            {"speaker": "Szakértő", "text": "____"},
                        ],
                        [
                            "A cserecsatár lefutotta a fáradó védőt, pazar mozdulattal átvette az indítást, majd hidegvérrel belőtte a hosszú sarokba.",
                            "A kapus saját kezébe vette a labdát, és behajította a lelátóra a nézők közé.",
                            "A játékvezető úgy döntött, hogy gól helyett inkább lefújja a meccset a harmincadik percben.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Edző", "text": "Miért nem tudtad kicselezni a hátvédet az egy az egy elleni szituációban?"},
                            {"speaker": "Szélső", "text": "____"},
                        ],
                        [
                            "Olyannyira szorosan rám tapadt a védő, hogy nem maradt elég területem felgyorsítani a labdával.",
                            "Mert elfelejtettem felvenni a futballcipőmet a mérkőzés előtt.",
                            "A pálya túl zöld volt, ami elvonta a figyelmemet a labdáról.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'átvesz' and 'kicselez' to describe an offensive football action.",
                                "answer": "A támadó egyetlen finom mozdulattal átvette a mélységi indítást, majd villámgyorsan kicselezte a kifutó kapust.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'lefut' and 'belő' with consecutive degree.",
                                "answer": "A szélső olyannyira könnyedén lefutotta a védelmét, hogy a kapus mellett ziccerből belőtte a vezető gólt.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A tehetséges játékos a döntő pillanatban elegánsan ____ a kapust. (dribbled past)",
                        "kicselezte",
                        "The talented player elegantly dribbled past the goalkeeper at the decisive moment.",
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which verb describes increasing running speed dramatically in a sprint?",
                        ["felgyorsít", "lelassít", "megtorpan"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Tactics, Psychology, and Team Dynamics",
            "grammar_label": "Analyzing athletic strategy, role distribution, and team coherence",
            "goals": [
                "I can analyze team strategy and tactical coordination in competitive sports",
                "I can discuss psychological dynamics, cohesion, and role division within a team",
                "I can articulate defensive and pressing strategies using formal sports vocabulary",
            ],
            "grammar_doc": {
                "slug": "tactics-psychology-team-dynamics",
                "title": "Tactics, Psychology, and Team Cohesion in Sports",
                "text1_title": "Strategic Structure and Tactical Discipline",
                "text1": "Modern sports analysis at the B2 level requires moving beyond raw physical attributes to analyze systemic organization. A successful team operates on 'taktikai fegyelem' (tactical discipline), clear 'szerepmegosztás' (division of roles), and proactive 'letámadás' (pressing / high press). When tactics break down, space opens up for the opposition and structural coherence is lost.",
                "text2_title": "Psychological Synergy and Team Spirit",
                "text2": "Individual mastery (egyéni virtuozitás) achieves nothing without 'csapatszellem' (team spirit) and 'összjáték' (fluid team play / combination passing). Psychological dynamics often outweigh physical superiority: a squad with superior chemistry and mutual trust will dismantle an uncoordinated ensemble of superstars. Consecutive degree structures frequently explain this synergy: 'A játékosok oly mértékben bíztak egymásban, hogy...' (The players trusted each other to such an extent that...).",
                "table_title": "Tactical and Psychological Terms",
                "table_rows": [
                    ["taktika", "A mester alaposan kidolgozta a győztes taktika részleteit. (Tactics / strategy.)"],
                    ["összjáték", "A csapat gyors és pontos összjátékkal bontotta meg a védelmet. (Team play / passing.)"],
                    ["csapatszellem", "A nehéz helyzetekben a kiváló csapatszellem segített a túlélésben. (Team spirit.)"],
                    ["letámadás", "A magas letámadás miatt az ellenfél nem tudott labdát kihozni. (Pressing / high press.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az edző által megkövetelt szigorú taktikai fegyelem meghozta gyümölcsét a nemzetközi kupamérkőzésen.",
                        "english": "The strict tactical discipline demanded by the coach bore fruit in the international cup match.",
                    },
                    {
                        "spanish": "A csapat összjátéka olyannyira gördülékeny volt, hogy a rivális védelem szinte tehetetlennek bizonyult.",
                        "english": "The team's collective play was so fluid that the rival defense proved virtually helpless.",
                    },
                    {
                        "spanish": "A precíz szerepmegosztásnak köszönhetően minden játékos pontosan ismerte a feladatát a pályán.",
                        "english": "Thanks to the precise division of roles, every player knew their exact duty on the pitch.",
                    },
                    {
                        "spanish": "Az agresszív letámadás oly mértékben megzavarta az ellenfelet, hogy sorozatos hibákat követtek el saját térfelükön.",
                        "english": "The aggressive pressing disrupted the opponent to such an extent that they committed successive errors in their own half.",
                    },
                ],
                "tip": "Distinguish between 'stratégia' (long-term overarching plan for a season or tournament) and 'taktika' (specific operational adaptations chosen for a single match or opponent).",
            },
            "words": [
                {"lemma": "taktika", "translation": "tactics / strategy", "pos": "noun"},
                {"lemma": "összjáték", "translation": "team play / combination passing", "pos": "noun"},
                {"lemma": "csapatszellem", "translation": "team spirit", "pos": "noun"},
                {"lemma": "letámadás", "translation": "pressing / high press", "pos": "noun"},
                {"lemma": "szerepmegosztás", "translation": "division of roles", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'letámadás' signify in modern football tactics?",
                        [
                            "an aggressive defensive pressing system aimed at regaining the ball in the opponent's half",
                            "a physical assault on the referee after a contested decision",
                            "leaving the field before the final whistle to protest against rain",
                        ],
                        0,
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the shared psychological bond and mutual trust among teammates?",
                        ["csapatszellem", "egyéni ambíció", "mérkőzésdíj"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["taktika", "tactics / strategy"],
                            ["összjáték", "team play / combination"],
                            ["csapatszellem", "team spirit"],
                            ["letámadás", "pressing / high press"],
                            ["szerepmegosztás", "division of roles"],
                        ],
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence using consecutive degree to describe team coordination:",
                        [
                            "A játékosok oly mértékben betartották a taktikát, hogy az ellenfél nem talált rést a védelmen.",
                            "A játékosok oly mértékben betartották a taktikát mert az ellenfél nem talált rést.",
                            "A játékosok oly mértékben betartották a taktikát ha az ellenfél nem talált rést.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence correctly incorporates preverbs of athletic action into tactical analysis?",
                        [
                            "Amint a középpályás átvette a labdát, azonnal felgyorsított és kicselezte a védőt.",
                            "Amint a középpályás labdát vett át, gyorsított fel és cselezte ki a védőt.",
                            "Amint a középpályás vette át a labdát, felgyorsított és ki cselezte a védőt.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A csapat összjátéka ____ tökéletes volt, hogy a közönség felállva tapsolt a lelátón. (so much)",
                        "olyannyira",
                        "The team's passing combination was so perfect that the audience applauded standing up in the stands.",
                        ["b2-consecutive-degree"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A védelem fegyelmezettsége ____ mértékben javult a szünet után, hogy nem kaptak több gólt. (in such)",
                        "oly",
                        "The defense's discipline improved to such an extent after the break that they conceded no further goals.",
                        ["b2-consecutive-degree"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "tudatos", "letámadás", "miatt", "az", "ellenfél", "nem", "tudott", "helyzetet", "kialakítani."],
                        ["A", "tudatos", "letámadás", "miatt", "az", "ellenfél", "nem", "tudott", "helyzetet", "kialakítani."],
                        "Due to the deliberate pressing, the opponent could not create a scoring chance.",
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A bajnokcsapat sikerének kulcsa a megkérdőjelezhetetlen ____ és az önfeláldozás volt. (team spirit)",
                        "csapatszellem",
                        "The key to the champion team's success was unquestionable team spirit and self-sacrifice.",
                        ["b2-32-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "keretben", "kialakított", "világos", "szerepmegosztás", "megelőzte", "a", "belső", "konfliktusokat."],
                        ["A", "keretben", "kialakított", "világos", "szerepmegosztás", "megelőzte", "a", "belső", "konfliktusokat."],
                        "The clear division of roles established in the squad prevented internal conflicts.",
                        ["b2-32-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Taktikai elemző", "text": "Hogyan tudta megnyerni a mérkőzést az esélytelenebbnek tartott csapat?"},
                            {"speaker": "Vezetőedző", "text": "____"},
                        ],
                        [
                            "A játékosok olyannyira fegyelmezetten követték a megbeszélt taktikát és az agresszív letámadást, hogy teljesen semlegesítették az ellenfél sztárjait.",
                            "Kizárólag a véletlennek köszönhető, mert a játékosok behunyt szemmel rugdosták a labdát.",
                            "Az ellenfél nem jelent meg a mérkőzésen, így játék nélkül kaptuk meg a győzelmet.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Miért fontosabb a csapatszellem az egyéni képességeknél a csapatsportokban?"},
                            {"speaker": "Csapatkapitány", "text": "____"},
                        ],
                        [
                            "Mert a kiváló összjáték és a kölcsönös bizalom oly mértékben megsokszorozza az erőt, hogy a legnagyobb egyéniségeket is le lehet győzni.",
                            "A csapatszellem egyáltalán nem számít, elég ha egyetlen játékos tud futni a pályán.",
                            "Mindenki csak magáért küzd, a többiek jelenléte csupán zavaró tényező.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an analytical sentence using 'letámadás' and 'taktika' with consecutive degree.",
                                "answer": "Az edző olyannyira precízen kidolgozta a letámadás taktikáját, hogy a rivális egyetlen tiszta passzt sem tudott megvalósítani a saját térfelén.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'összjáték' and 'csapatszellem' to explain a victory.",
                                "answer": "A győzelem nem az egyéni villanásoknak, hanem a lenyűgöző csapatszellemnek és a fegyelmezett összjátéknak volt köszönhető.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A játékosok fizikai felkészültsége ____ mértékben növekedett, hogy a hosszabbításban is ők domináltak. (in such)",
                        "oly",
                        "The physical preparedness of the players increased in such degree that they dominated in extra time as well.",
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term describes the harmonious combination of passes and movement between teammates?",
                        ["összjáték", "magányosság", "szabálytalanság"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Overcoming Defeat, Enduring Pressure",
            "grammar_label": "Mental resilience, psychological endurance, and sportsmanship (kudarc, talpra állás, sportszerűség)",
            "goals": [
                "I can discuss psychological pressure and mental endurance under competitive conditions",
                "I can describe strategies for coping with defeat and rebounding from setbacks (talpra állás)",
                "I can articulate principles of fair play and sportsmanship in athletic competitions",
            ],
            "grammar_doc": {
                "slug": "resilience-pressure-sportsmanship",
                "title": "Mental Resilience: Overcoming Defeat and Enduring Pressure",
                "text1_title": "The Psychology of High-Stakes Defeat",
                "text1": "At the elite level, athletic competition is determined as much by mental toughness (mentális állóképesség) as by biomechanics. Experiencing 'kudarc' (defeat / failure) is an inevitable facet of sport. True mastery is defined not by the absence of defeat, but by 'talpra állás' (the ability to rebound / stand back on one's feet). Athletes must withstand immense 'lélektani nyomás' (psychological pressure) from expectations, media, and fans.",
                "text2_title": "Sportsmanship and the Ethos of Fair Play",
                "text2": "'Sportszerűség' (sportsmanship / fair play) represents the moral benchmark of athletics: acknowledging the victor with grace, accepting defeat without bitterness, and refusing to compromise integrity for victory. Consecutive degree constructions describe how intense pressure affects mental fortitude: 'A lélektani nyomás olyannyira rányomta a bélyegét a mérkőzésre, hogy...' (Psychological pressure left its mark on the match to such an extent that...).",
                "table_title": "Resilience and Ethical Descriptors",
                "table_rows": [
                    ["kudarc", "A súlyos kudarc után a sportoló új edzésmódszerekhez folyamodott. (Failure / defeat.)"],
                    ["talpra állás", "A bravúros talpra állás a csapat rendkívüli erejét bizonyította. (Rebound / recovery.)"],
                    ["sportszerűség", "A vesztes tapsolva gratulált ellenfelének a sportszerűség jegyében. (Sportsmanship.)"],
                    ["küzdőszellem", "A fáradhatatlan küzdőszellem átsegítette a mélypontokon. (Fighting spirit.)"],
                ],
                "examples": [
                    {
                        "spanish": "A bajnok olyannyira erős mentális állóképességgel rendelkezett, hogy a legsúlyosabb kudarc után is képes volt a talpra állásra.",
                        "english": "The champion possessed such strong mental stamina that he was capable of rebounding even after the gravest defeat.",
                    },
                    {
                        "spanish": "A döntőben a lélektani nyomás oly mértékben fokozódott, hogy a legkisebb hiba is végzetesnek bizonyult.",
                        "english": "In the final, the psychological pressure escalated to such an extent that the slightest error proved fatal.",
                    },
                    {
                        "spanish": "A sportszerűség azt kívánja, hogy a győztes tisztelettel bánjon a legyőzöttel a küzdelem lezárása után.",
                        "english": "Sportsmanship requires that the victor treat the defeated with respect after the conclusion of the contest.",
                    },
                    {
                        "spanish": "A csapat küzdőszelleme olyannyira magával ragadta a közönséget, hogy a vereség ellenére állva ünnepelték őket.",
                        "english": "The team's fighting spirit captivated the audience to such an extent that despite the defeat they celebrated them standing.",
                    },
                ],
                "tip": "'Kudarc' takes the inessive (-ban/-ben) when talking about lessons drawn from defeat ('a kudarcban rejlő tanulság'), but sublative (-ra/-re) with verbs of condemnation ('kudarcra van ítélve' = doomed to fail).",
            },
            "words": [
                {"lemma": "kudarc", "translation": "failure / defeat", "pos": "noun"},
                {"lemma": "sportszerűség", "translation": "sportsmanship / fair play", "pos": "noun"},
                {"lemma": "talpra állás", "translation": "rebound / recovery from setback", "pos": "expression"},
                {"lemma": "lélektani nyomás", "translation": "psychological pressure", "pos": "expression"},
                {"lemma": "küzdőszellem", "translation": "fighting spirit / competitive drive", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'talpra állás' in athletic psychology?",
                        [
                            "the ability to recover and rebound mentally and physically after a severe defeat or injury",
                            "a mandatory stretching exercise performed exclusively on one foot",
                            "standing up to argue with the referee during half-time",
                        ],
                        0,
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase denotes fair play, ethical respect, and honesty in sports?",
                        ["sportszerűség", "kudarc", "lélektani nyomás"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["kudarc", "failure / defeat"],
                            ["sportszerűség", "sportsmanship / fair play"],
                            ["talpra állás", "rebound / recovery"],
                            ["lélektani nyomás", "psychological pressure"],
                            ["küzdőszellem", "fighting spirit"],
                        ],
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which consecutive sentence describes pressure on an athlete correctly?",
                        [
                            "A lélektani nyomás olyannyira bénító volt, hogy a bajnok nem tudta megismételni a selejtezőbeli idejét.",
                            "A lélektani nyomás olyannyira bénító volt mert a bajnok nem tudta megismételni az idejét.",
                            "A lélektani nyomás olyannyira bénító volt ha a bajnok nem tudta megismételni az idejét.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Complete the consecutive clause: 'A küzdőszellem oly mértékben fűtötte a csapatot, ____ a hátrányt is ledolgozták'.",
                        ["hogy", "minthogy", "holott"],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A vereség súlya ____ nehezedett a játékosok vállára, hogy alig tudtak megszólalni a sajtótájékoztatón. (so much)",
                        "olyannyira",
                        "The weight of defeat pressed on the players' shoulders so much that they could barely speak at the press conference.",
                        ["b2-consecutive-degree"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A közönség füttye ____ mértékben zavarta a büntetőt végrehajtó játékost, hogy mellé lőtte a labdát. (in such)",
                        "oly",
                        "The crowd's whistling disturbed the player taking the penalty in such degree that he shot the ball wide.",
                        ["b2-consecutive-degree"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "sportoló", "nem", "tört", "meg", "a", "kudarc", "után,", "hanem", "azonnal", "újrakezdte."],
                        ["A", "sportoló", "nem", "tört", "meg", "a", "kudarc", "után,", "hanem", "azonnal", "újrakezdte."],
                        "The athlete did not break after defeat, but immediately restarted.",
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A döntő pillanatban tapasztalható hatalmas ____ miatt a tapasztalt veteránoknak kellett vállalniuk a felelősséget. (psychological pressure)",
                        "lélektani nyomás",
                        "Due to the immense psychological pressure felt at the decisive moment, the experienced veterans had to take responsibility.",
                        ["b2-32-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "sportszerűség", "szellemében", "a", "két", "versenyző", "összeölelkezett", "a", "célvonalon."],
                        ["A", "sportszerűség", "szellemében", "a", "két", "versenyző", "összeölelkezett", "a", "célvonalon."],
                        "In the spirit of sportsmanship the two competitors embraced at the finish line.",
                        ["b2-32-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Sportpszichológus", "text": "Hogyan segíthet a mentális felkészülés a kudarcok feldolgozásában?"},
                            {"speaker": "Élsportoló", "text": "____"},
                        ],
                        [
                            "A vereség nem a végállomás, hanem visszajelzés; a gyors talpra álláshoz meg kell tanulni kezelni a lélektani nyomást és a kételyeket.",
                            "A kudarcot azonnal el kell felejteni, és a bírót kell hibáztatni minden egyes hiba miatt.",
                            "Ha valaki veszít egy meccsen, azonnal abba kell hagynia az élsportot örökre.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Mit jelentett számodra a riválisod gesztusa, amikor felsegített a bukás után?"},
                            {"speaker": "Bajnok", "text": "____"},
                        ],
                        [
                            "Ez a tiszta sportszerűség pillanata volt, amely megmutatta, hogy az emberi méltóság és a tisztelet fontosabb bármilyen aranyéremnél.",
                            "Nagyon dühös voltam, mert szerettem volna a földön aludni még fél órát.",
                            "Azt hittem, hogy meg akar támadni, ezért elszaladtam a stadionból.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'talpra állás' and 'küzdőszellem' with consecutive degree.",
                                "answer": "A bajnokcsapat küzdőszelleme olyannyira törhetetlen maradt, hogy a bravúros talpra állás után megnyerte a döntőt.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an ethical reflection using 'sportszerűség' and 'lélektani nyomás'.",
                                "answer": "Bár a döntőben a lélektani nyomás szinte elviselhetetlen volt, a versenyzők végig megőrizték a példamutató sportszerűséget.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A csalódottság ____ mértékben uralkodott el a csapaton, hogy hetekbe telt a motiváció visszaszerzése. (in such)",
                        "oly",
                        "Disappointment prevailed over the team in such degree that it took weeks to regain motivation.",
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term represents the relentless inner drive to fight against all odds?",
                        ["küzdőszellem", "közömbösség", "fáradtság"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Sports Journalism, Live Commentary, and Post-Match Analysis",
            "grammar_label": "Delivering live commentary and writing analytical match reports (élő közvetítés, mérkőzéselemzés, bravúr)",
            "goals": [
                "I can deliver or follow rapid live sports commentary with vivid aspectual narration",
                "I can write an analytical post-match report dissecting key turning points (fordulópont)",
                "I can evaluate individual brilliant athletic achievements (bravúr) in context",
            ],
            "grammar_doc": {
                "slug": "sports-journalism-live-commentary",
                "title": "Sports Journalism: Live Commentary and Match Reports",
                "text1_title": "The Linguistic Rhythm of Live Commentary",
                "text1": "Hungarian sports commentary (élő közvetítés) is renowned for its explosive tempo and dramatic aspectual verbs. A live commentator alternates between ongoing scene setting (imperfective present: 'készül a lövésre, lendül a láb') and sudden, telegraphic perfective declarations (perfective past or historical present: 'és belövi! micsoda gól!'). Preverbs are foregrounded to create suspense and immediacy.",
                "text2_title": "Structure of an Analytical Match Report",
                "text2": "An analytical match report (mérkőzéselemzés) dissects the tactical phases: the opening approach, the decisive 'fordulópont' (turning point / pivotal momentum shift), key saves and individual feats ('bravúr'), and the final outcome (győzelem, vereség, or 'döntetlen' = draw/tie). Consecutive degree clauses provide analytical weight: 'A kapus bravúrjai olyannyira demoralizálták a támadókat, hogy...' (The goalkeeper's saves demoralized the attackers to such an extent that...).",
                "table_title": "Sports Commentary Descriptors",
                "table_rows": [
                    ["élő közvetítés", "Az élő közvetítés során a riporter minden apró részletre kitért. (Live commentary.)"],
                    ["mérkőzéselemzés", "A szakértő részletes mérkőzéselemzésben tárta fel a taktikai hibákat. (Match analysis.)"],
                    ["fordulópont", "A kiállítás jelentette a meccs igazi fordulópontját. (Turning point.)"],
                    ["bravúr", "A kapus elképesztő bravúrral mentett a gólvonalról. (Masterful save / feat.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az élő közvetítésben a kommentátor hangja megremegett az izgalomtól, amikor a csatár a hosszabbításban belőtte a győztes gólt.",
                        "english": "In the live broadcast the commentator's voice trembled with excitement when the striker scored the winning goal in stoppage time.",
                    },
                    {
                        "spanish": "A mérkőzéselemzés rámutatott, hogy a korai csere bizonyult a találkozó legfőbb fordulópontjának.",
                        "english": "The match analysis pointed out that the early substitution proved to be the match's main turning point.",
                    },
                    {
                        "spanish": "A vendégek hálóőre egymás után három olyan bravúrt mutatott be, hogy a hazai szurkolók is megtapsolták.",
                        "english": "The visitors' goalkeeper produced three consecutive saves of such brilliance that the home fans applauded him as well.",
                    },
                    {
                        "spanish": "Bár a hazaiak végig rohamoztak, a találkozó végül igazságos döntetlennel zárult a sípszó pillanatában.",
                        "english": "Although the home team attacked throughout, the encounter ultimately ended in a fair draw at the final whistle.",
                    },
                ],
                "tip": "In sports reporting, avoid repetitive generic verbs like 'rúg' or 'fut'. Use expressive verbs of motion and placement: 'ível' (curves/lobs), 'csúsztat' (glances/slides), 'bombáz' (thunders a shot), 'hárít' (parries/saves).",
            },
            "words": [
                {"lemma": "élő közvetítés", "translation": "live broadcast / live commentary", "pos": "expression"},
                {"lemma": "mérkőzéselemzés", "translation": "match analysis", "pos": "noun"},
                {"lemma": "fordulópont", "translation": "turning point / pivotal moment", "pos": "noun"},
                {"lemma": "bravúr", "translation": "masterful feat / spectacular save", "pos": "noun"},
                {"lemma": "döntetlen", "translation": "draw / tie", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'fordulópont' in sports journalism?",
                        [
                            "a decisive moment or critical event that completely alters the momentum of the game",
                            "the painted center circle where kickoff takes place",
                            "the turnstile at the stadium gate where tickets are scanned",
                        ],
                        0,
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes a spectacular, extraordinary athletic save or accomplishment?",
                        ["bravúr", "szabálytalanság", "vereség"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["élő közvetítés", "live broadcast"],
                            ["mérkőzéselemzés", "match analysis"],
                            ["fordulópont", "turning point"],
                            ["bravúr", "masterful feat / save"],
                            ["döntetlen", "draw / tie"],
                        ],
                        ["b2-32-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence using consecutive degree in match analysis:",
                        [
                            "A kapus bravúrjai olyannyira elbizonytalanították a csatárokat, hogy nem mertek kapura lőni.",
                            "A kapus bravúrjai olyannyira elbizonytalanították a csatárokat mert nem mertek lőni.",
                            "A kapus bravúrjai olyannyira elbizonytalanították a csatárokat ha nem mertek lőni.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Complete the live commentary sentence: 'A védő lefutotta a támadót, majd ____ a labdát a kapu elől'.",
                        ["kicsúsztatta", "csúsztatott ki", "ki kicsúsztatta"],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A riporter hangja ____ felgyorsult a hajrában, hogy a nézők alig győzték követni az eseményeket. (so much)",
                        "olyannyira",
                        "The reporter's voice accelerated so much in the final minutes that the viewers could barely keep up with the events.",
                        ["b2-consecutive-degree"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A mérkőzés irama ____ mértékben fokozódott, hogy mindkét gárda teljesen feladta a védelmi óvatosságot. (in such)",
                        "oly",
                        "The tempo of the match escalated in such degree that both sides completely abandoned defensive caution.",
                        ["b2-consecutive-degree"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "kapus", "hatalmas", "bravúrral", "hárította", "a", "felső", "sarokba", "tartó", "lövést."],
                        ["A", "kapus", "hatalmas", "bravúrral", "hárította", "a", "felső", "sarokba", "tartó", "lövést."],
                        "The goalkeeper parried the shot heading for the top corner with an enormous save.",
                        ["b2-consecutive-degree"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A televíziós ____ milliók kísérték figyelemmel a magyar válogatott történelmi győzelmét. (live broadcast)",
                        "élő közvetítésben",
                        "In the live broadcast millions followed with attention the historic victory of the Hungarian national team.",
                        ["b2-32-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kiállítás", "jelentette", "a", "találkozó", "legfontosabb", "fordulópontját."],
                        ["A", "kiállítás", "jelentette", "a", "találkozó", "legfontosabb", "fordulópontját."],
                        "The red card represented the most important turning point of the encounter.",
                        ["b2-32-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szerkesztő", "text": "Hogyan foglalnád össze a mai derbi tanulságait az esti mérkőzéselemzésben?"},
                            {"speaker": "Szakkommentátor", "text": "____"},
                        ],
                        [
                            "A találkozó igazi fordulópontja a második félidő elején jött el, és bár a vége döntetlen lett, a kapusok bravúrjai emlékezetesek maradnak.",
                            "A meccs elmaradt, mert senki sem talált labdát az egész városban.",
                            "Nem érdemes elemezni a mérkőzést, mert a futballisták csak beszélgettek a kezdőkörben.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szurkoló", "text": "Igazságosnak tartod a mai döntetlen eredményt a sípszó után?"},
                            {"speaker": "Tudósító", "text": "____"},
                        ],
                        [
                            "Feltétlenül! Mindkét csapat oly mértékben kitette a szívét a pályára, hogy egyik fél sem érdemelt volna vereséget.",
                            "Egyáltalán nem, mert a mérkőzésen nem szabad döntetlennek lennie a szabályok szerint.",
                            "A döntetlen csak a kosárlabdában megengedett, a futballban tilos.",
                        ],
                        0,
                        ["b2-consecutive-degree"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a dramatic sentence for an 'élő közvetítés' using dynamic preverb verbs (pl. 'átvesz', 'belő').",
                                "answer": "Itt a kontra: a csatár mellre veszi a labdát, egyetlen csellel kicselezi a bekkeket, és védhetetlenül belövi a bal felsőbe!",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an analytical sentence for a 'mérkőzéselemzés' using 'fordulópont' and 'bravúr'.",
                                "answer": "A mérkőzés legfőbb fordulópontját a büntető jelentette, amelyet a kapus elképesztő bravúrral tolt a lécre, megőrizve a döntetlent.",
                            }
                        ],
                        ["b2-consecutive-degree"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A döntő kimenetele ____ bizonytalan volt, hogy az utolsó másodpercig senki sem mert győztest hirdetni. (so much)",
                        "olyannyira",
                        "The outcome of the final was so uncertain that until the final second nobody dared declare a winner.",
                        ["b2-consecutive-degree"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which word describes a match concluding with equal score for both opponents?",
                        ["döntetlen", "győzelem", "vereség"],
                        0,
                        ["b2-32-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can formulate complex consecutive degree clauses with olyannyira ..., hogy and oly mértékben ..., hogy",
            "I can utilize dynamic aspectual preverbs (lefut, átvesz, kicselez, belő) in high-speed sports narratives",
            "I can synthesize analytical sports terminology to critique tactics, resilience, and journalism",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["csúcsteljesítmény", "peak performance"],
                    ["állóképesség", "endurance / stamina"],
                    ["kicselez", "to outmaneuver / dribble past"],
                    ["csapatszellem", "team spirit"],
                    ["fordulópont", "turning point"],
                ],
                ["b2-32-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'bravúr' designate in sports journalism?",
                [
                    "a remarkable, extraordinary athletic feat or spectacular goalkeeping save",
                    "a serious foul leading to immediate expulsion",
                    "a regular scheduled pause for water during hot weather",
                ],
                0,
                ["b2-32-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly combines a consecutive clause of degree with dynamic athletic action?",
                [
                    "A csatár olyannyira felgyorsított a szélen, hogy könnyedén lefutotta a védőjét és belőtte a győztes gólt.",
                    "A csatár olyannyira felgyorsított a szélen mert lefutott a védőjét és belőtt a gólt.",
                    "A csatár olyannyira felgyorsított a szélen ha lefutná a védőjét és belőné a gólt.",
                ],
                0,
                ["b2-consecutive-degree"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A sportolónak rendkívüli mentális erőre volt szüksége a súlyos vereség utáni ____ eléréséhez. (rebound / recovery)",
                "talpra állás",
                "The athlete needed extraordinary mental strength to achieve the rebound after the heavy defeat.",
                ["b2-32-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A döntőben a lélektani nyomás ____ mértékben nehezedett a játékosokra, hogy sorozatos technikai hibákat vétettek. (in such)",
                "oly",
                "In the final the psychological pressure weighed on the players in such degree that they committed successive technical errors.",
                ["b2-consecutive-degree"],
            ),
            fb(
                "grammar",
                "recall",
                "A villámgyors szélső egy váratlan testcsellel elegánsan ____ a kapujából kifutó hálóőrt. (dribbled past)",
                "kicselezte",
                "The lightning-fast winger elegantly dribbled past the goalkeeper running out of his goal with an unexpected body feint.",
                ["b2-consecutive-degree"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'lefutotta a védőt' preferred over 'futott a védő mellett' in sports commentary?",
                [
                    "Because 'lefut' is a telic, perfective verb denoting the decisive act of outpacing and overcoming the opponent.",
                    "Because 'futott' cannot be used in the past tense in Hungarian grammar.",
                    "Because 'lefut' only applies when running downhill.",
                ],
                0,
                ["b2-consecutive-degree"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Irodalomkritikus", "text": "Hogyan köti össze Esterházy Péter a futballt és az írást az 'Utazás a tizenhatos mélyére' című művében?"},
                    {"speaker": "Egyetemi tanár", "text": "____"},
                ],
                [
                    "A futballpályát a létezés és a nyelv tereként értelmezi, ahol a tizenhatos geometriája, a kapus magánya és a labda íve esztétikai mélységet kap.",
                    "Kizárólag statisztikai táblázatokat és a játékosok fizetését közli mindenféle irodalmi gondolat nélkül.",
                    "Esterházy szerint a futball tilos minden gondolkodó ember számára.",
                ],
                0,
                ["b2-consecutive-degree"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where consecutive degree is used with impeccable stylistic register:",
                [
                    "A hazai csapat oly mértékben uralta a középpályát, hogy az ellenfél nem jutott el a kapuig.",
                    "A hazai csapat oly mértékben uralta a középpályát hogy az ellenfél nem jutna el a kapuig.",
                    "A hazai csapat oly mértékben uralta a középpályát de az ellenfél nem jutott el a kapuig.",
                ],
                0,
                ["b2-consecutive-degree"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "csatár", "olyannyira", "pontosan", "célzott,", "hogy", "a", "labda", "a", "kapufáról", "pattant", "be."],
                ["A", "csatár", "olyannyira", "pontosan", "célzott,", "hogy", "a", "labda", "a", "kapufáról", "pattant", "be."],
                "The striker aimed so accurately that the ball bounced in off the goalpost.",
                ["b2-consecutive-degree"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "védő", "hatalmas", "sprinttel", "beérte", "és", "lefutotta", "a", "támadót."],
                ["A", "védő", "hatalmas", "sprinttel", "beérte", "és", "lefutotta", "a", "támadót."],
                "The defender caught up with a huge sprint and outran the attacker.",
                ["b2-consecutive-degree"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a post-match commentary paragraph combining consecutive degree ('olyannyira ..., hogy') with dynamic action verbs ('átvesz', 'belő').",
                        "answer": "A mérkőzés ráadásában a szélső olyannyira felgyorsított, hogy könnyedén lefutotta védőjét; ezt követően a csatár pazarul átvette a beadást, és kíméletlenül belőtte a győztes gólt a hálóba.",
                    }
                ],
                ["b2-consecutive-degree"],
            ),
        ],
    },
}
