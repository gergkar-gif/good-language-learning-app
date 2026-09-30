"""
Hungarian B2 Core Track Unit 35:
  b2-35: Technology, Futurism & Human Agency
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_35 = {
    "unit_num": 35,
    "title": "Technology, Futurism & Human Agency",
    "grammar_summary": "Multi-layered speculative and counterfactual conditional architectures (feltéve, ha...; azzal a feltétellel, amennyiben; ha ... volna, akkor sem ...-hatott volna), future scenario modeling, tech ethics, and foresight discourse.",
    "grammar_skill": "b2-speculative-conditionals",
    "vocab_skill": "b2-35-vocab",
    "theme": "Technology, futurism and human agency",
    "intro_body": [
        "A 21. századi technológiai forradalom, a mesterséges intelligencia robbanásszerű fejlődése és a bioetikai dilemmák alapjaiban kérdőjelezik meg az emberi cselekvőképesség hagyományos határait. A jövőkutatás és a technológiai előrejelzés sajátos nyelvezetet igényel: a hipotézisek felállítása, a feltételes forgatókönyvek modellezése és a felelősség mérlegelése összetett nyelvtani szerkezetekre támaszkodik.",
        "Ebben a fejezetben elsajátíthatja a spekulatív és többágú feltételes mondatszerkezeteket (feltéve, ha...; azzal a feltétellel, amennyiben; még ha bekövetkezne is... akkor sem), elemezheti az automatizálás és a genetikai beavatkozások etikai dimenzióit, valamint megírhatja saját jövőkutatási elemzését. A fejezet végén Karinthy Frigyes zseniális utópiáján, az Utazás Faremidóbán keresztül találkozhat a szervetlen lények zenei világával és a technológiai fejlődés filozófiai paradoxonaival.",
    ],
    "classic_story": {
        "slug": "utazasfaremidoba",
        "author": "Karinthy Frigyes",
        "work": "Utazás Faremidóba (1916)",
        "title": "A szervetlen gépek és a tiszta zene világa",
        "summary": "Gulliver eljut a szervetlen lények különös szigetére, Faremidóba, ahol a fémből és kristályból épült géplények nem szavakkal, hanem tiszta zenei hangközökkel és harmonikus rezgésekkel beszélnek az emberi lét gyarlóságáról és a tiszta rációról.",
        "characters": ["Gulliver", "A szervetlen lény"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A repülőgép roncsai közül felocsúdva Gulliver egy olyan szigeten találta magát, amelyhez foghatót még soha nem látott a négy korábbi utazása során. Nem voltak fák, nem zöldellt fű, semmilyen szerves anyag nem borította a talajt: a hegyeket polírozott acél, a folyómedreket pedig higany és folyékony kristály alkotta.",
            },
            {
                "type": "narration",
                "text": "Hirtelen a magasból hatalmas, szárnyas alak ereszkedett alá, amelynek teste csillogó bronzból és finom fogaskerekekből állt. Amikor a lény megállt előtte, a levegő finoman megremegett, és szavak helyett csodálatos, tiszta zenei akkordok csendültek fel a szervetlen test belsejéből: fá-ré-mi-dó.",
            },
            {
                "type": "dialogue",
                "speaker": "Gulliver",
                "text": "Uram, miféle tünemény ez? Én ember vagyok Angliából, a szárazföldről jöttem, és a szavaidat zenei dallamként hallom, mégis megértem az értelmüket a lelkemben.",
            },
            {
                "type": "dialogue",
                "speaker": "A szervetlen lény",
                "text": "Mi vagyunk Faremidó lakói, a tiszta szervetlen értelem gyermekei. Ti, szerves lények, állandóan szenvedtek a testetek pusztulásától, a betegségektől és a hazugságoktól, mert a szavaitok zűrzavarosak és pontatlanok.",
            },
            {
                "type": "dialogue",
                "speaker": "Gulliver",
                "text": "De vajon képes volna-e egy szervetlen fémtest érezni a szeretetet, a művészetet és a könyörületet, amire mi, emberek oly büszkék vagyunk?",
            },
            {
                "type": "dialogue",
                "speaker": "A szervetlen lény",
                "text": "A mi szeretetünk maga a matematika és az egyetemes harmónia. Amennyiben a ti fajotok képes lett volna felülemelkedni az önpusztító háborúkon, talán megérthette volna a hangok törvényét, de ti a tudást pusztításra használtátok fel.",
            },
            {
                "type": "narration",
                "text": "Gulliver megrendülten hallgatta a dallamos rezgéseket. Rádöbbent, hogy az első világháború borzalmai elől menekülő Karinthy ebben a látomásban a technológia és az emberi erkölcs tragikus szakadékát ábrázolta: a gépek világa tökéletes és romolhatatlan, de vajon élhető-e az ember számára az érzések nélkül?",
            },
            {
                "type": "narration",
                "text": "Ahogy az óriási fémlény újra kitárta szárnyait és a zenei akkordok visszhangozva elhaltak a kristályhegyek között, Gulliver ott maradt a parton. Magányosan nézte a lemenő nap sugarait, és arra gondolt: bárcsak az emberi civilizáció is megtanulná a tisztaság és az értelem harmóniáját, mielőtt késő lenne.",
            },
        ],
        "reading_questions": [
            {
                "question": "Hogyan kommunikálnak Faremidó lakói a szöveg szerint?",
                "options": [
                    "Nem artikulált emberi szavakkal, hanem tiszta zenei akkordokkal és matematikai harmóniákkal.",
                    "Papírra vetett bonyolult matematikai egyenletek cseréjével.",
                    "Rejtjeles rádiójelekkel a levegőben.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen alapvető hibát lát a szervetlen lény az emberi fajban?",
                "options": [
                    "Hogy a szerves test törékenysége és a pontatlan szavak zűrzavara miatt önpusztító háborúkba sodródnak.",
                    "Hogy nem hajlandók fémből készült ruhákat hordani a hideg ellen.",
                    "Hogy nem tudnak repülőgépet építeni a tengeri utazásokhoz.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen mélyebb filozófiai üzenetet közvetít Karinthy utópiája az olvasónak?",
                "options": [
                    "A technológiai tökéletesség és az emberi etika közötti feszültséget a háborúk árnyékában.",
                    "A zeneoktatás azonnali eltörlésének szükségességét az iskolákban.",
                    "A fémkohászat kizárólagos fejlesztésének fontosságát a mezőgazdasággal szemben.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Speculative Conditional Hypotheses (feltéve, ha...; azzal a feltétellel, amennyiben)",
            "grammar_label": "Speculative conditional hypotheses in scientific framing (feltéve, ha...; azzal a feltétellel, amennyiben; feltéve, hogy)",
            "goals": [
                "I can frame complex speculative hypotheses using 'feltéve, ha' and 'amennyiben'",
                "I can express scientific conditions with 'azzal a feltétellel, hogy' and correlative clauses",
                "I can formulate probabilistic forecasts and policy prerequisites in academic discourse",
            ],
            "grammar_doc": {
                "slug": "speculative-conditional-hypotheses",
                "title": "Speculative Conditional Hypotheses: feltéve, ha...; azzal a feltétellel, amennyiben",
                "text1_title": "Correlative and Prerequisite Conditionals in Scientific Register",
                "text1": "Scientific speculation, technology assessment, and future forecasting require precise conditional markers beyond the basic 'ha' clause. The conjunction 'feltéve, ha' (provided that / supposing that) frames a speculative premise under which a future technological breakthrough or systemic risk may materialize. In high-register prose, 'azzal a feltétellel, hogy...' (on the condition that...) introduces formal prerequisites and regulatory boundaries.",
                "text2_title": "The Correlative Structure: amennyiben..., úgy / abban az esetben...",
                "text2": "The formal conjunction 'amennyiben' (insofar as, in the event that) pairs symmetrically with the apodosis correlatives 'úgy' or 'abban az esetben'. Unlike conversational 'ha', 'amennyiben' highlights institutional, procedural, or mathematical causality: 'Amennyiben a szimuláció igazolja a modellt, úgy megkezdődhet a kísérlet.' Speculative conditionals often take the conditional mood (-na/-ne) to indicate that the scenario remains theoretical.",
                "table_title": "Speculative and Formal Conditional Patterns",
                "table_rows": [
                    ["feltéve, ha...", "A technológia elterjedhet, feltéve, ha az energiaköltségek csökkennek. (Provided that energy costs fall.)"],
                    ["azzal a feltétellel, hogy...", "Engedélyezték a tesztet, azzal a feltétellel, hogy szigorúan felügyelik. (On the condition that it is supervised.)"],
                    ["amennyiben..., úgy...", "Amennyiben új adatok merülnek fel, úgy felülvizsgáljuk a hipotézist. (In the event that new data arises, we review.)"],
                    ["abban az esetben, ha...", "Abban az esetben, ha a rendszer meghibásodna, vészleállás lép életbe. (In the event that the system fails.)"],
                    ["feltéve, hogy...", "A projekt megvalósítható, feltéve, hogy elegendő forrás áll rendelkezésre. (Provided that sufficient funding exists.)"],
                ],
                "examples": [
                    {
                        "spanish": "Feltéve, ha sikerül csökkenteni a mikrocsipek energiafogyasztását, a kvantumszámítás hamarosan elérhetővé válhat.",
                        "english": "Provided that we succeed in reducing the power consumption of microchips, quantum computing may soon become accessible.",
                    },
                    {
                        "spanish": "A kutatócsoport azzal a feltétellel kapott támogatást, hogy eredményeit nyílt hozzáférésű folyóiratban publikálja.",
                        "english": "The research team received funding on the condition that it publishes its findings in an open-access journal.",
                    },
                    {
                        "spanish": "Amennyiben a mesterséges intelligencia autonóm döntéseket hoz, úgy tisztázni kell a jogi felelősség kérdését.",
                        "english": "In the event that artificial intelligence makes autonomous decisions, the issue of legal liability must be clarified.",
                    },
                    {
                        "spanish": "A szakértők szerint a klímavédelmi célok elérhetők, feltéve, hogy a gazdasági szereplők azonnal cselekszenek.",
                        "english": "According to experts, climate goals are attainable, provided that economic actors take immediate action.",
                    },
                ],
                "tip": "Distinguish between factual condition ('amennyiben bekövetkezik, úgy...') and hypothetical speculation ('amennyiben bekövetkezne, úgy...'). When drafting future tech scenarios, the conditional mood underscores epistemic uncertainty.",
            },
            "words": [
                {"lemma": "feltéve", "translation": "provided that / supposing that", "pos": "conjunction"},
                {"lemma": "amennyiben", "translation": "insofar as / in the event that / if", "pos": "conjunction"},
                {"lemma": "feltétel", "translation": "condition / prerequisite / requirement", "pos": "noun"},
                {"lemma": "hipotézis", "translation": "hypothesis / working assumption", "pos": "noun"},
                {"lemma": "előrejelzés", "translation": "forecast / projection / prediction", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'amennyiben' express in formal academic discourse?",
                        [
                            "in the event that / insofar as (introducing a formal condition or hypothetical clause)",
                            "an informal greeting exchanged between coworkers in a hallway",
                            "a strictly past-tense historical marker of time",
                        ],
                        0,
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which noun designates a scientific assumption or working premise that requires verification?",
                        ["hipotézis", "előrejelzés", "feltétel"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["feltéve", "provided that / supposing"],
                            ["amennyiben", "in the event that / insofar as"],
                            ["feltétel", "condition / prerequisite"],
                            ["hipotézis", "hypothesis / assumption"],
                            ["előrejelzés", "forecast / projection"],
                        ],
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which correlative word standardly introduces the main clause after 'Amennyiben...' in formal prose?",
                        ["úgy / abban az esetben", "pedig / de", "hiszen / ugyanis"],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence where 'feltéve, ha' introduces a speculative scientific hypothesis correctly:",
                        [
                            "Az autonóm járművek elterjedhetnek, feltéve, ha a jogi szabályozás garantálja a biztonságot.",
                            "Feltéve, ha tegnap megérkezett a villamos az állomásra háromkor.",
                            "A hipotézis feltéve ha megitta az összes tejet a hűtőszekrényből.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A kísérletet engedélyezték, azzal a ____, hogy a kutatók folyamatosan tájékoztatják az etikai bizottságot. (condition)",
                        "feltétellel",
                        "The experiment was authorized, on the condition that the researchers continuously inform the ethics committee.",
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "____ a számítógépes modell megbízhatónak bizonyul, úgy megkezdődhet a klinikai tesztelés. (In the event that / Insofar as)",
                        "Amennyiben",
                        "In the event that the computer model proves reliable, clinical testing may begin.",
                        ["b2-speculative-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "technológiai", "áttörés", "megvalósulhat,", "feltéve,", "ha", "elegendő", "támogatást", "kap", "a", "laboratórium."],
                        ["A", "technológiai", "áttörés", "megvalósulhat,", "feltéve,", "ha", "elegendő", "támogatást", "kap", "a", "laboratórium."],
                        "The technological breakthrough can be realized, provided that the laboratory receives sufficient funding.",
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A legfrissebb gazdasági ____ szerint a mesterséges intelligencia átalakítja az ipari termelést. (forecasts / projections)",
                        "előrejelzések",
                        "According to the latest economic forecasts, artificial intelligence will transform industrial production.",
                        ["b2-35-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "kutatók", "számos", "kísérlettel", "ellenőrizték", "az", "új", "tudományos", "hipotézist."],
                        ["A", "kutatók", "számos", "kísérlettel", "ellenőrizték", "az", "új", "tudományos", "hipotézist."],
                        "The researchers verified the new scientific hypothesis with numerous experiments.",
                        ["b2-35-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Futurológus", "text": "Mikor válhatnak az önvezető autók a mindennapi közlekedés általános részévé?"},
                            {"speaker": "Mérnök", "text": "____"},
                        ],
                        [
                            "Feltéve, ha a digitális infrastruktúra kellően fejletté válik, már a következő évtizedben elterjedhetnek.",
                            "Amennyiben a gépkocsi tegnap megevett egy almát a garázsban délután.",
                            "Ugyan már, a szervetlen lények nem engedik meg a közlekedést soha.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutató", "text": "Hogyan reagál a tudományos közösség erre a forradalmi elméletre?"},
                            {"speaker": "Professzor", "text": "____"},
                        ],
                        [
                            "A hipotézist izgalmasnak tartják, azzal a feltétellel, hogy független laboratóriumok is megerősítik az eredményeket.",
                            "Mindenki azonnal eldobja a számítógépét és Faremidóba költözik holnap.",
                            "A feltétel kizárólag a villamos menetrendjétől függ a belvárosban.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a formal sentence using 'amennyiben..., úgy...' framing a conditional technological regulation.",
                                "answer": "Amennyiben az algoritmus emberi beavatkozás nélkül hoz döntést, úgy a fejlesztő vállalatot terheli a jogi felelősség.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a speculative forecast sentence using 'feltéve, ha' concerning renewable energy.",
                                "answer": "A fosszilis tüzelőanyagok teljes kivezetése lehetségessé válik 2040-re, feltéve, ha az akkumulátoros energiatárolás hatékonysága megduplázódik.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "____ a teszt sikeres lesz, úgy haladéktalanul megindítjuk a sorozatgyártást. (In the event that / Insofar as)",
                        "Amennyiben",
                        "In the event that the test is successful, we will launch serial production without delay.",
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun means a prerequisite or necessary condition in formal Hungarian?",
                        ["feltétel", "hipotézis", "előrejelzés"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Multi-Clause Counterfactual Stacking in Scientific Dilemmas",
            "grammar_label": "Multi-clause counterfactual conditionals and concessive past stacking (ha ... volna, akkor sem ...-hatott volna; még ha ... is)",
            "goals": [
                "I can stack multiple counterfactual conditions across past and present scenarios",
                "I can use concessive counterfactuals with 'még ha ... is' to evaluate technological risks",
                "I can reconstruct alternative scientific histories and ethical turning points",
            ],
            "grammar_doc": {
                "slug": "counterfactual-stacking-scientific-dilemmas",
                "title": "Multi-Clause Counterfactual Stacking in Scientific Dilemmas",
                "text1_title": "Mechanics of Counterfactual Stacking (Többtagú ellenfaktikus szerkezetek)",
                "text1": "Counterfactual conditionals speculate about states of affairs that did not occur in the past or are impossible in the present. In scientific analysis, scholars frequently stack multiple conditional clauses to model chain reactions or alternative historical scenarios: 'Ha a kutatók nem fedezték volna fel az mRNS-technológiát, a világjárvány sokkal súlyosabb következményekkel járt volna, és ma nem tartanánk a rákkutatás jelenlegi szintjén.' Note how past conditional ('fedezték volna fel') links to present consequence ('nem tartanánk').",
                "text2_title": "Concessive Counterfactuals with 'Még ha... volna is'",
                "text2": "Concessive counterfactual constructions evaluate inevitable outcomes regardless of hypothetical interventions: 'Még ha a kormányzat betiltotta volna is a fejlesztést, a nemzetközi verseny akkor sem állt volna le.' The combination of 'még ha... is' with past conditional auxiliary 'volna' and modal potential suffix '-hatott volna' produces nuanced, resilient ethical argumentation.",
                "table_title": "Counterfactual Patterns in Scenario Modeling",
                "table_rows": [
                    ["ha ... volna, akkor ... volna", "Ha időben léptek volna, megelőzhető lett volna a hiba. (Had they acted, the error could have been prevented.)"],
                    ["még ha ... volna is, akkor sem...", "Még ha figyelmeztették volna is, akkor sem hitte volna el. (Even had they warned him, he would not have believed it.)"],
                    ["ha nem ... volna, ma nem...", "Ha nem építették volna meg, ma nem működhetne a hálózat. (Had they not built it, the network could not function today.)"],
                    ["amennyiben megvalósult volna...", "Amennyiben megvalósult volna, úgy átalakította volna a piacot. (Had it been realized, it would have transformed the market.)"],
                ],
                "examples": [
                    {
                        "spanish": "Ha a kibervédelmi szakemberek nem reagáltak volna percek alatt, az adatbázis megsemmisült volna.",
                        "english": "Had the cybersecurity specialists not reacted within minutes, the database would have been destroyed.",
                    },
                    {
                        "spanish": "Még ha a szimuláció pontos eredményt adott volna is, a laboratóriumi ellenőrzést akkor sem lehetett volna kihagyni.",
                        "english": "Even had the simulation yielded an accurate result, laboratory verification could not have been omitted anyway.",
                    },
                    {
                        "spanish": "A szakértők szerint a válság elkerülhető lett volna, ha a döntéshozók figyelembe veszik az előrejelzéseket.",
                        "english": "According to experts, the crisis could have been avoided had decision-makers taken the forecasts into account.",
                    },
                    {
                        "spanish": "Ha Neumann János nem fektette volna le az elméleti alapokat, a modern számítástechnika évtizedekkel később alakult volna ki.",
                        "english": "Had John von Neumann not laid the theoretical foundations, modern computing would have developed decades later.",
                    },
                ],
                "tip": "In Hungarian counterfactual conditionals, remember that 'volna' follows the past tense verb form in both protasis and apodosis: 'ha tudtam volna, eljöttem volna'. For potential modality, use '-hatott/-hetett volna': 'megelőzhető lett volna' or 'megelőzhették volna'.",
            },
            "words": [
                {"lemma": "szimuláció", "translation": "simulation / modeling", "pos": "noun"},
                {"lemma": "forgatókönyv", "translation": "scenario / roadmap / projection plan", "pos": "noun"},
                {"lemma": "kockázat", "translation": "risk / hazard", "pos": "noun"},
                {"lemma": "előre nem látható", "translation": "unforeseen / unpredictable", "pos": "adjective"},
                {"lemma": "következmény", "translation": "consequence / outcome / aftermath", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'forgatókönyv' in technology forecasting and risk management?",
                        [
                            "a structured scenario or hypothetical projection plan modeling possible future events",
                            "a physical receipt given to a customer at a grocery store",
                            "a medical prescription for antibiotics",
                        ],
                        0,
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective describes consequences that could not have been predicted in advance?",
                        ["előre nem látható", "szimuláció", "kockázat"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["szimuláció", "simulation / modeling"],
                            ["forgatókönyv", "scenario / projection plan"],
                            ["kockázat", "risk / hazard"],
                            ["előre nem látható", "unforeseen / unpredictable"],
                            ["következmény", "consequence / outcome"],
                        ],
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which grammatical auxiliary creates the past counterfactual conditional mood in Hungarian?",
                        ["volna", "lenne", "kellene"],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct concessive counterfactual construction:",
                        [
                            "Még ha a szimuláció pontos lett volna is, akkor sem küszöbölhette volna ki az emberi tényezőt.",
                            "Még ha a kockázat fut a vonaton holnap reggel.",
                            "A forgatókönyv még ha nem iszik vizet a pohárból.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Ha a mérnökök időben észrevették volna a hibát, a reaktor nem ____ le. (would not have shut down)",
                        "állt volna",
                        "Had the engineers noticed the defect in time, the reactor would not have shut down.",
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Még ha időben figyelmeztették volna is a közvéleményt, a pánikot akkor sem lehetett volna ____. (avoided / prevented)",
                        "elkerülni",
                        "Even had they warned the public in time, the panic could not have been avoided anyway.",
                        ["b2-speculative-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Ha", "nem", "végezték", "volna", "el", "a", "szimulációt,", "súlyos", "kockázatnak", "tették", "volna", "ki", "a", "rendszert."],
                        ["Ha", "nem", "végezték", "volna", "el", "a", "szimulációt,", "súlyos", "kockázatnak", "tették", "volna", "ki", "a", "rendszert."],
                        "Had they not carried out the simulation, they would have exposed the system to grave risk.",
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A kutatóintézet három különböző ____ dolgozott ki a globális energiaátmenet lehetséges kimeneteleire. (scenarios / roadmaps)",
                        "forgatókönyvet",
                        "The research institute developed three different scenarios for the possible outcomes of the global energy transition.",
                        ["b2-35-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "váratlan", "technológiai", "hiba", "számos", "előre", "nem", "látható", "következménnyel", "járt."],
                        ["A", "váratlan", "technológiai", "hiba", "számos", "előre", "nem", "látható", "következménnyel", "járt."],
                        "The unexpected technological glitch entailed numerous unforeseen consequences.",
                        ["b2-35-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Elemző", "text": "Megelőzhető lett volna a hatalmas szerverleállás a múlt héten?"},
                            {"speaker": "Rendszergazda", "text": "____"},
                        ],
                        [
                            "Igen, ha a tesztkörnyezetben elvégezték volna a terhelési szimulációt, a hiba azonnal kiderült volna.",
                            "Dehogyis, a gizgaz már tegnap megírta az egész szoftvert a gépen.",
                            "Még ha a limlom bevállalta volna is, a hercehurca nem engedte.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Milyen következményei lettek volna, ha az állam nem avatkozik be a válság idején?"},
                            {"speaker": "Közgazdász", "text": "____"},
                        ],
                        [
                            "Ha nem avatkoztak volna be, a bankrendszer összeomlott volna, és ma sokkal mélyebb recesszióban élnénk.",
                            "Mindenki azonnal Faremidóba utazott volna nyaralni a családdal.",
                            "A forgatókönyv azonnal megevett volna három csésze kávét.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a multi-clause counterfactual sentence evaluating a missed opportunity in scientific research.",
                                "answer": "Ha a laboratórium időben megkapta volna a kért támogatást, a kutatók már tavaly befejezhették volna az ígéretes gyógyszerkísérletet.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'még ha ... volna is, akkor sem' assessing technological risk.",
                                "answer": "Még ha a vállalat megduplázta volna is a biztonsági költségvetést, az emberi mulasztást akkor sem zárhatta volna ki teljesen.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Ha a katasztrófavédelem nem lépett volna közbe azonnal, a gátszakadás beláthatatlan ____ járt volna. (consequences)",
                        "következményekkel",
                        "Had disaster management not intervened immediately, the dam burst would have entailed incalculable consequences.",
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes the probability of adverse outcomes or hazard in technological design?",
                        ["kockázat", "szimuláció", "forgatókönyv"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Artificial Intelligence, Automation, and the Future of Work",
            "grammar_label": "Speculative modality and passive-avoidance in technology ethics (helyettesíthetné, felmerül, átalakításra kerül)",
            "goals": [
                "I can debate the societal and economic ramifications of artificial intelligence and automation",
                "I can use modal auxiliary verbs to express potential disruptions to the labor market",
                "I can discuss human agency versus algorithmic decision-making using high-register vocabulary",
            ],
            "grammar_doc": {
                "slug": "ai-automation-future-of-work",
                "title": "Artificial Intelligence, Automation, and the Future of Work",
                "text1_title": "Grammar of Agency and Human Oversight in Technological Discourse",
                "text1": "Discussions surrounding artificial intelligence (mesterséges intelligencia) and automation (automatizálás) involve acute grammatical choices regarding agency. While popular journalism often attributes active verbs to algorithms ('az MI elveszi a munkát'), formal academic and ethical registers prefer impersonal constructions or passive-avoidance strategies ('automatizálásra kerülnek a rutinfeladatok', 'átalakul a munkaerőpiac szerkezete') to emphasize human responsibility and policy choices.",
                "text2_title": "Human Agency (Cselekvőképesség) and Labor Market Disruption",
                "text2": "The concept of 'cselekvőképesség' (agency / capacity to act) lies at the heart of technological ethics: to what degree do human workers maintain autonomy when assisted by algorithmic decision-making? Mitigating the disruptive impact of automation requires lifelong retraining ('átképzés') and strategic economic planning across the entire labor market ('munkaerőpiac').",
                "table_title": "Key Terminology for AI and the Labor Market",
                "table_rows": [
                    ["mesterséges intelligencia", "A mesterséges intelligencia fejlődése új etikai szabályozást követel. (Demands new ethical rules.)"],
                    ["automatizálás", "Az ipari automatizálás növeli a termelékenységet, de munkahelyeket szüntet meg. (Increases productivity.)"],
                    ["munkaerőpiac", "A digitalizáció mélyrehatóan átformálja a hazai és globális munkaerőpiacot. (Transforms the labor market.)"],
                    ["átképzés", "Átfogó átképzési programokra van szükség a veszélyeztetett szakmákban. (Comprehensive reskilling programs.)"],
                    ["cselekvőképesség", "Meg kell őriznünk az emberi cselekvőképességet és döntési autonómiát. (Preserve human agency.)"],
                ],
                "examples": [
                    {
                        "spanish": "A mesterséges intelligencia nem helyettesítheti az emberi empátiát és a komplex erkölcsi mérlegelést.",
                        "english": "Artificial intelligence cannot substitute for human empathy and complex moral deliberation.",
                    },
                    {
                        "spanish": "A rutinszerű irodai feladatok automatizálása miatt a munkavállalók jelentős részének átképzésre lesz szüksége.",
                        "english": "Due to the automation of routine office tasks, a significant portion of employees will need retraining.",
                    },
                    {
                        "spanish": "A modern munkaerőpiac egyre inkább a kreatív problémamegoldó képességet és a rugalmasságot díjazza.",
                        "english": "The modern labor market increasingly rewards creative problem-solving ability and flexibility.",
                    },
                    {
                        "spanish": "Az autonóm fegyverrendszerek alkalmazása felveti a kérdést: kinek a cselekvőképessége érvényesül a harctéren?",
                        "english": "The deployment of autonomous weapons systems raises the question: whose agency prevails on the battlefield?",
                    },
                ],
                "tip": "When discussing technological developments, avoid deterministic statements ('a gépek elkerülhetetlenül átveszik a hatalmat'). Use epistemic hedging modals instead: 'valószínűsíthető, hogy...', 'mindez szükségessé teheti a...', 'felvetheti a kérdést, hogy...'.",
            },
            "words": [
                {"lemma": "mesterséges intelligencia", "translation": "artificial intelligence", "pos": "expression"},
                {"lemma": "automatizálás", "translation": "automation / computerization", "pos": "noun"},
                {"lemma": "munkaerőpiac", "translation": "labor market / job market", "pos": "noun"},
                {"lemma": "átképzés", "translation": "retraining / reskilling", "pos": "noun"},
                {"lemma": "cselekvőképesség", "translation": "agency / capacity to act / legal competence", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'cselekvőképesség' designate in technology ethics and social theory?",
                        [
                            "the capacity of an individual or agent to act autonomously and make meaningful decisions",
                            "the battery life of an electronic device in standby mode",
                            "the speed at which a computer downloads software updates",
                        ],
                        0,
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which compound noun refers to the process of training workers in new skills to adapt to tech changes?",
                        ["átképzés", "automatizálás", "munkaerőpiac"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["mesterséges intelligencia", "artificial intelligence"],
                            ["automatizálás", "automation"],
                            ["munkaerőpiac", "labor market"],
                            ["átképzés", "retraining / reskilling"],
                            ["cselekvőképesség", "agency / capacity to act"],
                        ],
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence uses appropriate epistemic hedging when discussing AI impacts on employment?",
                        [
                            "A mesterséges intelligencia elterjedése alapjaiban alakíthatja át a jövőbeli munkaerőpiaci elvárásokat.",
                            "A robotok holnap reggel azonnal kidobják az összes embert az ablakon.",
                            "Minden munkahely megszűnik három napon belül világszerte.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "What passive-avoidance nominalization replaces 'Az algoritmusok megvizsgálják az adatokat' in high formal style?",
                        [
                            "Az adatok algoritmusok általi vizsgálata megtörténik / folyamatban van.",
                            "A gizgaz megeszi az adatokat a monitoron.",
                            "A vizsgálat azonnal beugrik a gépbe tegnap.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Az ipari termelésben végbemenő gyors ____ következtében számos hagyományos munkakör megszűnt. (automation)",
                        "automatizálás",
                        "As a consequence of the rapid automation occurring in industrial production, numerous traditional jobs disappeared.",
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A kormányzat nagyszabású programot indított a dolgozók szakmai ____ elősegítésére. (retraining)",
                        "átképzésének",
                        "The government launched a large-scale program to facilitate the professional retraining of workers.",
                        ["b2-speculative-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "mesterséges", "intelligencia", "alkalmazása", "során", "meg", "kell", "őrizni", "az", "emberi", "felügyeletet."],
                        ["A", "mesterséges", "intelligencia", "alkalmazása", "során", "meg", "kell", "őrizni", "az", "emberi", "felügyeletet."],
                        "During the application of artificial intelligence, human oversight must be preserved.",
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A modern technológiák alkalmazása során sosem szabad csorbítani a felhasználók döntési ____. (agency / capacity to act)",
                        "cselekvőképességét",
                        "During the application of modern technologies, users' decision-making agency must never be impaired.",
                        ["b2-35-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "digitalizáció", "mélyreható", "változásokat", "idéz", "elő", "a", "hazai", "munkaerőpiacon."],
                        ["A", "digitalizáció", "mélyreható", "változásokat", "idéz", "elő", "a", "hazai", "munkaerőpiacon."],
                        "Digitalization induces profound changes in the domestic labor market.",
                        ["b2-35-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szociológus", "text": "Hogyan készíthetjük fel a társadalmat az automatizálás kihívásaira?"},
                            {"speaker": "Oktatási szakértő", "text": "____"},
                        ],
                        [
                            "Rugalmas átképzési programokkal, a digitális készségek fejlesztésével és a kritikus gondolkodás erősítésével.",
                            "Azonnal be kell tiltani minden számítógépet és vissza kell térni az ókorba.",
                            "Ugyan már, a mesterséges intelligencia sosem fogja megérteni a betűket.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Etikus", "text": "Nem félő, hogy az emberi cselekvőképesség háttérbe szorul az algoritmusok korában?"},
                            {"speaker": "Informatikus", "text": "____"},
                        ],
                        [
                            "Valós a kockázat, éppen ezért elengedhetetlen, hogy a végső döntés mindig az ember kezében maradjon.",
                            "Dehogyis, a gépek sokkal jobban tudnak verset írni a nagymamának.",
                            "A cselekvőképesség csak a virágoknak fontos a botanikus kertben.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a balanced sentence on the relationship between 'mesterséges intelligencia' and 'munkaerőpiac'.",
                                "answer": "Bár a mesterséges intelligencia elterjedése egyes szakmák megszűnéséhez vezethet, egyidejűleg új, magas hozzáadott értékű munkahelyeket is teremt a munkaerőpiacon.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence arguing for the preservation of human 'cselekvőképesség' in the workplace.",
                                "answer": "Az automatizált rendszerek bevezetésekor biztosítani kell, hogy a munkavállalók megtartsák cselekvőképességüket és ne váljanak csupán passzív végrehajtókká.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A technológiai fejlődés elkerülhetetlenül átformálja a globális ____ igényeit. (labor market)",
                        "munkaerőpiac",
                        "Technological advancement inevitably transforms the demands of the global labor market.",
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which multi-word phrase denotes computer systems capable of performing tasks requiring human intelligence?",
                        ["mesterséges intelligencia", "ökológiai lábnyom", "technológiai ugrás"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Bioethics, Genetics, and Ecological Boundaries",
            "grammar_label": "Normative modality and ethical boundary argumentation (megengedhető volna, gátat kell szabni, tiszteletben kell tartani)",
            "goals": [
                "I can articulate nuanced ethical positions on genetic engineering and bio-technologies",
                "I can evaluate human environmental impact through the concept of ecological boundaries",
                "I can balance scientific innovation against ethical precautionary principles",
            ],
            "grammar_doc": {
                "slug": "bioethics-genetics-ecological-boundaries",
                "title": "Bioethics, Genetics, and Ecological Boundaries",
                "text1_title": "Normative Modality in Bioethical Debates",
                "text1": "Bioethical argumentation operates with normative modality: evaluating what is permissible ('megengedhető'), what is strictly prohibited ('tilos / elfogadhatatlan'), and what limits must be imposed on scientific interference ('gátat kell szabni', 'határt kell vonni'). When discussing genetic modification (génmódosítás) and human enhancement, writers combine deontic verbs ('kell', 'szükséges') with the conditional mood ('megengedhető volna-e...', 'erkölcsileg igazolható lenne-e...') to explore hypothetical boundaries.",
                "text2_title": "Planetary Boundaries and Sustainable Coexistence",
                "text2": "The survival of civilization hinges on recognizing ecological boundaries ('ökológiai korlátok') and reducing our collective ecological footprint ('ökológiai lábnyom'). True sustainability ('fenntarthatóság') demands that technological interventions ('beavatkozások') align with natural regenerative cycles rather than treating nature as an infinite resource for exploitation.",
                "table_title": "Core Vocabulary for Bioethics and Ecology",
                "table_rows": [
                    ["bioetika", "A bioetika alapelvei irányítják a modern orvosbiológiai kutatásokat. (Principles of bioethics guide.)"],
                    ["génmódosítás", "A mezőgazdasági génmódosítás körül élénk társadalmi viták folynak. (Lively social debates.)"],
                    ["ökológiai lábnyom", "Minden polgárnak törekednie kell az ökológiai lábnyoma csökkentésére. (Reduce ecological footprint.)"],
                    ["fenntarthatóság", "A fenntarthatóság elve nélkül nem képzelhető el hosszú távú gazdasági fejlődés. (Principle of sustainability.)"],
                    ["beavatkozás", "Az emberi beavatkozás súlyos károkat okozhat a természetes ökoszisztémákban. (Intervention can cause harm.)"],
                ],
                "examples": [
                    {
                        "spanish": "Megengedhető volna-e a humán génmódosítás alkalmazása nem örökletes betegségek megelőzésére?",
                        "english": "Would the application of human gene editing be permissible for the prevention of non-hereditary diseases?",
                    },
                    {
                        "spanish": "A bioetikai bizottság határozottan kimondta, hogy az emberi méltóság határait minden körülmények között tiszteletben kell tartani.",
                        "english": "The bioethics committee firmly stated that the boundaries of human dignity must be respected under all circumstances.",
                    },
                    {
                        "spanish": "Az ökológiai lábnyom mérséklése érdekében elengedhetetlen a megújuló energiaforrások elterjesztése.",
                        "english": "In order to reduce our ecological footprint, the widespread adoption of renewable energy sources is indispensable.",
                    },
                    {
                        "spanish": "Minden drasztikus környezeti beavatkozás előtt alapos hatásvizsgálatot kell végezni.",
                        "english": "Before every drastic environmental intervention, a thorough impact assessment must be conducted.",
                    },
                ],
                "tip": "Use the structure 'kérdéses, hogy... megengedhető-e' to frame ethical dilemmas neutrally before taking a firm personal stance in an essay.",
            },
            "words": [
                {"lemma": "bioetika", "translation": "bioethics", "pos": "noun"},
                {"lemma": "génmódosítás", "translation": "genetic modification / gene editing", "pos": "noun"},
                {"lemma": "ökológiai lábnyom", "translation": "ecological footprint", "pos": "expression"},
                {"lemma": "fenntarthatóság", "translation": "sustainability", "pos": "noun"},
                {"lemma": "beavatkozás", "translation": "intervention / interference", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'bioetika' primarily concerned with?",
                        [
                            "the ethical, philosophical, and legal dilemmas arising from biomedical and genetic sciences",
                            "the design of computer software for accounting firms",
                            "the historical architecture of medieval cathedrals",
                        ],
                        0,
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which expression denotes the total environmental resource demand imposed by human activity?",
                        ["ökológiai lábnyom", "génmódosítás", "beavatkozás"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["bioetika", "bioethics"],
                            ["génmódosítás", "genetic modification"],
                            ["ökológiai lábnyom", "ecological footprint"],
                            ["fenntarthatóság", "sustainability"],
                            ["beavatkozás", "intervention / interference"],
                        ],
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence correctly articulates a normative ethical boundary conditional?",
                        [
                            "Erkölcsileg megengedhető volna-e a genetikai beavatkozás, ha azzal súlyos örökletes betegségeket előznénk meg?",
                            "A fenntarthatóság elment a piacra és vásárolt három almát.",
                            "Gátat kell szabni a bioetikának, mert túl sokat alszik délután.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the postposition that commonly pairs with 'érdekében' in sustainability discourse:",
                        ["a fenntarthatóság érdekében (in the interest of sustainability)", "a fenntarthatóság nélkül", "a fenntarthatóság helyett"],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A tudománynak szigorú etikai korlátokat kell felállítania a felelőtlen emberi ____ megelőzése végett. (intervention)",
                        "beavatkozás",
                        "Science must establish strict ethical limits in order to prevent irresponsible human intervention.",
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A jövő nemzedékek érdekeit szem előtt tartva gátat kell ____ a természet kizsákmányolásának. (to set / impose a limit)",
                        "szabni",
                        "Keeping in mind the interests of future generations, limits must be set on the exploitation of nature.",
                        ["b2-speculative-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "génmódosítás", "alkalmazása", "során", "kiemelt", "figyelmet", "kell", "fordítani", "a", "bioetikai", "elvekre."],
                        ["A", "génmódosítás", "alkalmazása", "során", "kiemelt", "figyelmet", "kell", "fordítani", "a", "bioetikai", "elvekre."],
                        "During the application of genetic modification, priority attention must be paid to bioethical principles.",
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az energiahatékony technológiák révén jelentősen csökkenthetjük intézményünk ____. (ecological footprint)",
                        "ökológiai lábnyomát",
                        "Through energy-efficient technologies, we can significantly reduce our institution's ecological footprint.",
                        ["b2-35-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "valódi", "fenntarthatóság", "megköveteli", "a", "természeti", "erőforrások", "felelősségteljes", "használatát."],
                        ["A", "valódi", "fenntarthatóság", "megköveteli", "a", "természeti", "erőforrások", "felelősségteljes", "használatát."],
                        "Genuine sustainability demands the responsible use of natural resources.",
                        ["b2-35-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Biológus", "text": "Szabadna-e módosítani az emberi embriók génállományát a betegségek kiküszöbölésére?"},
                            {"speaker": "Bioetikus", "text": "____"},
                        ],
                        [
                            "Ez rendkívül kényes kérdés: megengedhető volna gyógyítási célból, de gátat kell szabni az embertervezés kísértésének.",
                            "Persze, a szervetlen gépek már holnap mindenkinek új lábat szerelnek.",
                            "Ugyan már, a DNS csak egyszerű limlom a mikroszkóp alatt.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Környezetvédő", "text": "Hogyan mérhető reálisan a gazdasági növekedés környezeti terhelése?"},
                            {"speaker": "Ökológus", "text": "____"},
                        ],
                        [
                            "Az ökológiai lábnyom számításával, amely világosan megmutatja, túlléptük-e a bolygó regenerációs határait.",
                            "A gizgaz magasságának napi mérésével a repülőtér mellett.",
                            "Dehogyis, a gazdaság sosem érintkezik a természettel semmilyen formában.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence arguing for ethical caution regarding 'génmódosítás'.",
                                "answer": "Bár a génmódosítás forradalmasíthatja a gyógyászatot, az eljárás előre nem látható kockázatai miatt szigorú bioetikai felügyelet szükséges.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence linking 'ökológiai lábnyom' with 'fenntarthatóság'.",
                                "answer": "A hosszú távú fenntarthatóság megvalósításának alapvető feltétele az ipari társadalmak túlzott ökológiai lábnyomának drasztikus mérséklése.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A környezeti katasztrófák elkerülése végett szigorú korlátok közé kell szorítani a természetbe való emberi ____. (intervention)",
                        "beavatkozást",
                        "In order to avoid environmental catastrophes, human intervention into nature must be kept within strict limits.",
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes the discipline examining ethical dilemmas of biological and medical advancements?",
                        ["bioetika", "fenntarthatóság", "génmódosítás"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Designing a Scenario: Tech Forecast Essay",
            "grammar_label": "Discourse markers and structural synthesis in technological forecast essays (kiindulási alapként feltételezve, mindent egybevetve)",
            "goals": [
                "I can structure an analytical futurist essay outlining multi-decade technological scenarios",
                "I can integrate speculative conditionals, empirical data, and normative conclusions",
                "I can synthesize technological optimism and critical risk analysis in formal Hungarian",
            ],
            "grammar_doc": {
                "slug": "designing-scenario-tech-forecast",
                "title": "Designing a Scenario: Tech Forecast Essay",
                "text1_title": "Discourse Architecture of a Technology Forecast Essay",
                "text1": "A futurology or technology assessment essay in Hungarian requires a disciplined rhetorical architecture. The introduction posits an empirical baseline and working assumptions ('kiindulási alapként feltételezve, hogy...'). The body develops alternative branches (optimistic, baseline, and disruptive scenarios) linked by conditional chains ('amennyiben... úgy...', 'ha ez a tendencia folytatódik, akkor...'). The synthesis weighs benefits against systemic risks before formulating policy recommendations.",
                "text2_title": "Vocabulary of Paradigm Shifts and Institutional Adaptation",
                "text2": "Describing long-term transformations draws on high-register conceptual tools: 'jövőkutatás' (futurology / futures studies), 'technológiai ugrás' (technological leap), 'társadalmi hatás' (societal impact), and 'paradigmaváltás' (paradigm shift). Regulatory frameworks ('szabályozás') must be drafted proactively rather than reactively to safeguard human well-being.",
                "table_title": "Advanced Discourse Formulae for Futurist Essays",
                "table_rows": [
                    ["kiindulási alapként feltételezve", "Kiindulási alapként feltételezve a digitális infrastruktúra bővülését... (Assuming as baseline...)"],
                    ["technológiai ugrás", "A kvantumszámítás olyan technológiai ugrást jelent, amely mindent megváltoztat. (Technological leap.)"],
                    ["társadalmi hatás", "Minden technológiai fejlesztés társadalmi hatását alaposan fel kell mérni. (Societal impact.)"],
                    ["paradigmaváltás", "A megújuló energiák térnyerése valódi paradigmaváltást hozott. (Genuine paradigm shift.)"],
                    ["mindent egybevetve", "Mindent egybevetve a felelős szabályozás jelenti a jövő zálogát. (All things considered.)"],
                ],
                "examples": [
                    {
                        "spanish": "A modern jövőkutatás célja nem a jövő megjósolása, hanem a lehetséges forgatókönyvek körültekintő modellezése.",
                        "english": "The goal of modern futures studies is not to predict the future, but to carefully model possible scenarios.",
                    },
                    {
                        "spanish": "A fúziós energia megvalósulása olyan korszakos technológiai ugrást hozna, amely megoldaná a globális energiaválságot.",
                        "english": "The realization of fusion energy would bring about an epochal technological leap that would solve the global energy crisis.",
                    },
                    {
                        "spanish": "A digitális platformok elterjedésének mélyreható társadalmi hatásait még csak most kezdjük igazán megérteni.",
                        "english": "We are only now truly beginning to understand the profound societal impacts of the proliferation of digital platforms.",
                    },
                    {
                        "spanish": "Mindent egybevetve elmondható, hogy az innováció sebességének lépést kell tartania az etikai szabályozással.",
                        "english": "All things considered, it can be stated that the speed of innovation must keep pace with ethical regulation.",
                    },
                ],
                "tip": "In your concluding paragraph, avoid simplistic utopian or dystopian cliches. Balance technological potential with pragmatic risk governance, using the conclusive marker 'mindent egybevetve' or 'összegzésképpen megállapítható'." ,
            },
            "words": [
                {"lemma": "jövőkutatás", "translation": "futurology / futures studies", "pos": "noun"},
                {"lemma": "technológiai ugrás", "translation": "technological leap / breakthrough", "pos": "expression"},
                {"lemma": "társadalmi hatás", "translation": "social impact / societal consequence", "pos": "expression"},
                {"lemma": "szabályozás", "translation": "regulation / legal framework", "pos": "noun"},
                {"lemma": "paradigmaváltás", "translation": "paradigm shift", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'paradigmaváltás' in scientific and technological history?",
                        [
                            "a fundamental transformation in basic concepts and experimental practices of a scientific discipline",
                            "a minor bug fix in an existing software application",
                            "an annual maintenance check on factory equipment",
                        ],
                        0,
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the academic field focused on systematic study of the future and scenario planning?",
                        ["jövőkutatás", "szabályozás", "technológiai ugrás"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["jövőkutatás", "futurology / futures studies"],
                            ["technológiai ugrás", "technological leap"],
                            ["társadalmi hatás", "social impact"],
                            ["szabályozás", "regulation / framework"],
                            ["paradigmaváltás", "paradigm shift"],
                        ],
                        ["b2-35-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which discourse phrase best serves to establish a baseline assumption in an academic futurist essay?",
                        [
                            "Kiindulási alapként feltételezve, hogy...",
                            "Mindenki tudja a faluban, hogy...",
                            "Ugyan már, dehogyis...",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence demonstrating proper conditional synthesis in scenario analysis:",
                        [
                            "Amennyiben a szabályozás lépést tart a fejlesztésekkel, a technológiai ugrás nem veszélyezteti a társadalmi kohéziót.",
                            "A jövőkutatás felugrott az asztalra és kinyitotta az ablakot tegnap.",
                            "Ha a paradigmaváltás nem eszik levest, akkor kiakad a villamos.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A megújuló energiaforrások elterjedése valódi ____ hozott a globális gazdaságban. (paradigm shift)",
                        "paradigmaváltást",
                        "The proliferation of renewable energy sources brought about a genuine paradigm shift in the global economy.",
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Mindent ____, a jövő sikere a felelős innováció és a szigorú etikai kontroll egyensúlyán múlik. (considering all things / all in all)",
                        "egybevetve",
                        "All things considered, the success of the future hinges on the balance between responsible innovation and strict ethical control.",
                        ["b2-speculative-conditionals"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "mesterséges", "intelligencia", "fejlődése", "olyan", "technológiai", "ugrást", "jelent,", "amelyre", "fel", "kell", "készülnünk."],
                        ["A", "mesterséges", "intelligencia", "fejlődése", "olyan", "technológiai", "ugrást", "jelent,", "amelyre", "fel", "kell", "készülnünk."],
                        "The advancement of artificial intelligence represents a technological leap for which we must prepare.",
                        ["b2-speculative-conditionals"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az új autonóm rendszerek bevezetése előtt alaposan elemezni kell azok hosszú távú ____. (social impacts)",
                        "társadalmi hatásait",
                        "Before introducing new autonomous systems, their long-term social impacts must be analyzed thoroughly.",
                        ["b2-35-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "korszerű", "jövőkutatás", "fontos", "szerepet", "játszik", "a", "kormányzati", "döntéshozatalban."],
                        ["A", "korszerű", "jövőkutatás", "fontos", "szerepet", "játszik", "a", "kormányzati", "döntéshozatalban."],
                        "Modern futures studies plays an important role in governmental decision-making.",
                        ["b2-35-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Politikus", "text": "Hogyan kellene szabályoznunk a gyorsan fejlődő technológiákat?"},
                            {"speaker": "Technológiai szakértő", "text": "____"},
                        ],
                        [
                            "Olyan rugalmas szabályozási keretre van szükség, amely támogatja az innovációt, de megvédi a polgárok alapvető jogait.",
                            "Azonnal zárjuk be az összes egyetemet és tiltsuk be az internetet örökre.",
                            "Ugyan már, a gépek sosem fognak elektromos áramot használni.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Diák", "text": "Milyen módszerekkel dolgozik egy professzionális futurológus?"},
                            {"speaker": "Előadó", "text": "____"},
                        ],
                        [
                            "Statisztikai adatokra támaszkodva alternatív forgatókönyveket épít, és a társadalmi hatások szimulációjával segít a tervezésben.",
                            "Kristálygömbből jósolja meg a jövő heti lottószámokat a tévében.",
                            "Minden nap kidobja a számítógépes limlomot a folyóba.",
                        ],
                        0,
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a thesis sentence for a tech forecast essay introducing a 'paradigmaváltás'.",
                                "answer": "A kvantumszámítástechnika és a mesterséges intelligencia fúziója olyan mértékű paradigmaváltást vetít előre, amely alapjaiban alakítja át a tudományos megismerés határait.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a concluding sentence using 'mindent egybevetve' regarding responsible technology regulation.",
                                "answer": "Mindent egybevetve kijelenthető, hogy a technológiai fejlődés valódi sikere nem csupán a gépek teljesítményén, hanem az emberközpontú szabályozás bölcsességén múlik.",
                            }
                        ],
                        ["b2-speculative-conditionals"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A pénzügyi szektorban a digitális fizetési rendszerek megjelenése valódi ____ idézett elő. (technological leap)",
                        "technológiai ugrást",
                        "In the financial sector, the emergence of digital payment systems induced a genuine technological leap.",
                        ["b2-speculative-conditionals"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun refers to the legislative or administrative framework governing an industry?",
                        ["szabályozás", "jövőkutatás", "paradigmaváltás"],
                        0,
                        ["b2-35-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can formulate complex speculative hypotheses and counterfactual scenarios in academic Hungarian",
            "I can debate ethical and economic dilemmas of artificial intelligence, genetics, and ecology",
            "I can author an analytical futures forecast essay integrating high-register discourse markers",
        ],
        "exercises": [
            # 1..3 Recognize
            mc(
                "vocabulary",
                "recognize",
                "What does 'ökológiai lábnyom' measure in environmental science?",
                [
                    "the total human demand on ecological assets and natural resource capacity",
                    "the depth of soil erosion caused by winter frost",
                    "the physical footprints left by animals in a national park",
                ],
                0,
                ["b2-35-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "Which phrase denotes a profound, historic shift in fundamental scientific concepts?",
                ["paradigmaváltás", "szimuláció", "hipotézis"],
                0,
                ["b2-35-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence displays correct multi-clause counterfactual syntax in Hungarian?",
                [
                    "Ha a döntéshozók időben reagáltak volna, a környezeti katasztrófa megelőzhető lett volna, és ma nem fenyegetné a térséget az ivóvízhiány.",
                    "Ha a szimuláció tegnap futott volna, akkor a villamos holnap megérkezik időben.",
                    "Amennyiben a robot megitta a kávét, úgy azonnal elment a moziba este.",
                ],
                0,
                ["b2-speculative-conditionals"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A gazdasági elemzők három különböző ____ vázoltak fel a munkaerőpiac várható alakulására. (scenarios / projections)",
                "forgatókönyvet",
                "The economic analysts outlined three different scenarios for the expected development of the labor market.",
                ["b2-35-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "Még ha a vállalat minden biztonsági előírást betartott ____ is, a váratlan kibertámadást akkor sem lehetett volna teljesen kivédeni. (would have - counterfactual auxiliary)",
                "volna",
                "Even had the company complied with every security protocol, the unexpected cyberattack could not have been completely repelled anyway.",
                ["b2-speculative-conditionals"],
            ),
            fb(
                "grammar",
                "recall",
                "____ a kutatás megbízható eredményt hoz, úgy sor kerülhet a nemzetközi szabadalom bejegyzésére. (In the event that / Insofar as)",
                "Amennyiben",
                "In the event that the research yields a reliable result, registration of the international patent can take place.",
                ["b2-speculative-conditionals"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'amennyiben..., úgy...' preferred in official policy forecasts over conversational 'ha'?",
                [
                    "Because it conveys formal procedural causality, institutional authority, and clear legal conditioning.",
                    "Because 'ha' cannot be used with future verbs in written Hungarian.",
                    "Because 'amennyiben' was invented in 2020 specifically for computer algorithms.",
                ],
                0,
                ["b2-speculative-conditionals"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Egyetemi hallgató", "text": "Miért olyan fontos az etikai szabályozás a mesterséges intelligencia fejlesztésekor?"},
                    {"speaker": "Professzor", "text": "____"},
                ],
                [
                    "Mert ha az algoritmusok felelősségvállalás nélkül hoznának döntéseket, súlyosan sérülne az emberi méltóság és cselekvőképesség.",
                    "Mert a gépek azonnal elfelejtik a magyar nyelvtant, ha nem kapnak süteményt.",
                    "Dehogyis fontos, a forgatókönyv már 1916-ban megoldott minden problémát Faremidóban.",
                ],
                0,
                ["b2-speculative-conditionals"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where normative modality is applied appropriately to environmental boundaries:",
                [
                    "A természeti erőforrások kimerülése miatt határozott gátat kell szabni a féktelen ipari terjeszkedésnek.",
                    "A természet tegnap este engedélyezte a fák kivágását a városi parkban.",
                    "A bolygó regenerációja azonnal megírta a tiltakozó levelet a hivatalnak.",
                ],
                0,
                ["b2-speculative-conditionals"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "tudományos", "innováció", "megvalósulhat,", "feltéve,", "ha", "a", "társadalom", "biztosítja", "a", "szükséges", "forrásokat."],
                ["A", "tudományos", "innováció", "megvalósulhat,", "feltéve,", "ha", "a", "társadalom", "biztosítja", "a", "szükséges", "forrásokat."],
                "Scientific innovation can be realized, provided that society provides the necessary resources.",
                ["b2-speculative-conditionals"],
            ),
            sb(
                "grammar",
                "produce",
                ["Ha", "a", "kutatók", "nem", "ismerték", "volna", "fel", "a", "kockázatokat,", "beláthatatlan", "környezeti", "károk", "keletkeztek", "volna."],
                ["Ha", "a", "kutatók", "nem", "ismerték", "volna", "fel", "a", "kockázatokat,", "beláthatatlan", "környezeti", "károk", "keletkeztek", "volna."],
                "Had the researchers not recognized the risks, incalculable environmental damage would have occurred.",
                ["b2-speculative-conditionals"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause future forecast essay excerpt linking 'technológiai ugrás', speculative conditionals ('amennyiben..., úgy...'), and human 'cselekvőképesség'.",
                        "answer": "Bár a mesterséges intelligencia ugrásszerű fejlődése történelmi technológiai ugrást hoz a termelékenységben, amennyiben az algoritmusok felügyelet nélkül döntenek emberi sorsokról, úgy helyrehozhatatlan csorbát szenved az egyéni cselekvőképesség; éppen ezért a társadalomnak már ma szigorú etikai és jogi garanciákat kell teremtenie a jövő technológiái köré.",
                    }
                ],
                ["b2-speculative-conditionals"],
            ),
        ],
    },
}
