#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 22, 23, and 24 (b2-22, b2-23, b2-24)
using build_core_unit from b2_unit_builder_helper.py.
"""
import sys
from pathlib import Path

sys.path.insert(
    0,
    r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch",
)
from b2_unit_builder_helper import build_core_unit


# ==============================================================================
# Exercise Builder Helpers
# ==============================================================================

def mc(cat, stage, question, options, correct, teaches=None):
    res = {
        "type": "multiple-choice",
        "category": cat,
        "stage": stage,
        "question": question,
        "options": options,
        "correct": correct,
    }
    if teaches:
        res["teaches"] = teaches
    return res


def match(cat, stage, pairs, teaches):
    return {
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    return {
        "type": "fill-blank",
        "category": cat,
        "stage": stage,
        "sentence": sentence,
        "answer": answer,
        "english": english,
        "teaches": teaches,
    }


def sb(cat, stage, tiles, solution, english, teaches):
    return {
        "type": "sentence-builder",
        "category": cat,
        "stage": stage,
        "tiles": tiles,
        "solution": solution,
        "english": english,
        "teaches": teaches,
    }


def dc(stage, prompt, options, correct, teaches):
    return {
        "type": "dialogue-complete",
        "category": "dialogue",
        "stage": stage,
        "prompt": prompt,
        "options": options,
        "correct": correct,
        "teaches": teaches,
    }


def sw(stage, template, teaches):
    return {
        "type": "structured-writing",
        "category": "writing",
        "stage": stage,
        "template": template,
        "teaches": teaches,
    }


# ==============================================================================
# UNIT 22: Demographics, Generations & the Life Course
# ==============================================================================

UNIT_22 = {
    "unit_num": 22,
    "title": "Demographics, Generations & the Life Course",
    "grammar_summary": "Temporal framing postpositions across the life course (folyamán, során, múltával, küszöbén), anteriority temporal clauses with mire and perfective preverbs, and generational perspectives.",
    "grammar_skill": "b2-temporal-framing",
    "vocab_skill": "b2-22-vocab",
    "theme": "Demographics, generations and the life course",
    "intro_body": [
        "A társadalmi struktúrák alakulása és az emberi életút szakaszai elválaszthatatlanok az idő múlásától. Akár a demográfiai folyamatok makroszintű elemzéséről, akár az egyes generációk közötti szolidaritásról van szó, a modern magyar nyelv kifinomult nyelvtani eszközökkel fejezi ki az időbeli keretezést és az egymást követő életszakaszok viszonyát.",
        "Ebben a fejezetben elsajátíthatja a formális időhatározói névutókat (folyamán, során, múltával, küszöbén), a 'mire' kötőszóval bevezetett előidejűségi mellékmondatok szerkesztését, valamint az életkori sajátosságokat kifejező idiómákat (gyerekkorában, öregségére, fiatalként). Szabó Magda megrázó regénye, 'Az ajtó' segítségével pedig a generációk közötti bizalom és függetlenség határait vizsgálhatja meg.",
    ],
    "classic_story": {
        "slug": "azajto",
        "author": "Szabó Magda",
        "work": "Az ajtó (1987)",
        "title": "Emerenc és a bizalom határai",
        "summary": "Az idős, rejtélyes házvezetőnő, Emerenc és a fiatal írónő kapcsolatának kibontakozása, amelyben a szeretet, a méltóság és a generációk közötti távolság kérdései feszülnek egymásnak.",
        "characters": ["Emerenc", "Az írónő"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A rideg téli délelőttön az írónő dolgozószobájában a csendet csak az írógép kopogása törte meg. Emerenc seprűvel a kezében állt meg a küszöbön; tekintete tiszta volt, kemény, mint a bazalt, mégis ott bujkált benne évtizedek megpróbáltatásainak nehéz tapasztalata.",
            },
            {
                "type": "dialogue",
                "speaker": "Emerenc",
                "text": "Maga csak írjon, kedvesem, a szavak nem kopnak el. De az élet folyamán az ember megtanulja, hogy a valódi hűséget nem a mondatok, hanem a néma cselekedetek mérik. Mire az ember megérti ezt, addigra sokszor már késő bocsánatot kérni.",
            },
            {
                "type": "narration",
                "text": "Az írónő letette a tollat, és elgondolkodva nézett az idős asszonyra. Tudta jól, hogy Emerenc lakásának ajtaja mindenki előtt zárva áll; senki sem léphette át azt a titokzatos küszöböt, amely mögött a múlt sebeit és emlékeit őrizte.",
            },
            {
                "type": "dialogue",
                "speaker": "Az írónő",
                "text": "Emerenc, én tisztelem a maga függetlenségét, mégis aggódom magáért. Öregségére egyedül van azokkal a terhekkel, amelyeket évtizedek során hordozott. Nem fél attól, hogy mire segítségre szorulna, már senki sem lesz a közelben?",
            },
            {
                "type": "dialogue",
                "speaker": "Emerenc",
                "text": "Fiatalként az ember azt hiszi, mindent kibír egyedül, és igaza is van. De a magány nem büntetés, hanem tisztaság. Az én ajtóm mögé csak akkor léphet be valaki, ha már nincs szükség magyarázatokra. Magának pedig még sokat kell tanulnia az emberi lélekről, mire felnő ehhez a feladathoz.",
            },
            {
                "type": "narration",
                "text": "A szavak súlyosan nehezedtek a szobára. Emerenc mozdulatai pontosak és kimértek voltak; minden gesztusa azt a méltóságot árasztotta, amelyet sem a háborúk, sem a szegénység nem tudott megtörni élete folyamán.",
            },
            {
                "type": "dialogue",
                "speaker": "Az írónő",
                "text": "Megértettem, Emerenc. A bizalom nem követelhető, hanem csak kiérdemelhető az évek múltával. Ígérem, hogy soha nem fogom erőszakkal átlépni a határait, bármennyire féltem is magát.",
            },
            {
                "type": "narration",
                "text": "Az idős asszony arcán halvány, szinte észrevehetetlen mosoly suhant át, majd bólintott, és csendben visszatért a folyosó takarításához. A bizalom törékeny hídja megépült kettejük között, de mindketten érezték: az igazi próbatételek még hátravannak.",
            },
        ],
        "reading_questions": [
            {
                "question": "Milyen alapvető elvet fogalmaz meg Emerenc a hűséggel kapcsolatban?",
                "options": [
                    "A valódi hűséget a tettek és nem a szavak mérik.",
                    "A hűséget csak nyilvános ígéretekkel lehet bizonyítani.",
                    "A hűség a fiatalság kiváltsága, amely öregségre elmúlik.",
                ],
                "correct": 0,
            },
            {
                "question": "Miért tartotta Emerenc zárva a lakása ajtaját a külvilág elől?",
                "options": [
                    "Mert a múlt emlékeit és belső függetlenségét védte a kéretlen beavatkozástól.",
                    "Mert félt a betörőktől és a városi zajártalomtól.",
                    "Mert el akarta adni az értékes bútorait anélkül, hogy mások megtudnák.",
                ],
                "correct": 0,
            },
            {
                "question": "Mit ígért az írónő Emerencnek a beszélgetés végén?",
                "options": [
                    "Hogy tiszteletben tartja a határait, és soha nem lépi át erőszakkal a bizalom küszöbét.",
                    "Hogy minden héten orvost hív hozzá a házhoz.",
                    "Hogy könyvet ír a titkairól az engedélye nélkül.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Over the Course Of, With the Passing Of (folyamán, múltával)",
            "grammar_label": "Temporal framing postpositions (folyamán, során, múltával, küszöbén)",
            "goals": [
                "I can frame extended processes and periods using folyamán and során",
                "I can express the lapse of time and milestones using múltával",
                "I can describe being on the brink of life transitions with küszöbén",
            ],
            "grammar_doc": {
                "slug": "temporal-framing-postpositions",
                "title": "Temporal Framing Postpositions: folyamán, során, múltával, küszöbén",
                "text1_title": "Extended Processes and Durations: folyamán and során",
                "text1": "In formal Hungarian narrative and expository discourse, extended processes unfolding across time are framed with the postpositions 'folyamán' and 'során'. Both require the preceding noun to take a possessive suffix: 'az elmúlt évek folyamán' ('over the course of past years'), 'a demográfiai felmérés során' ('in the course of the demographic survey'). While 'folyamán' emphasizes continuous duration within a temporal frame, 'során' focuses on occurrences occurring throughout a procedural or life sequence ('életútja során').",
                "text2_title": "Lapse of Time and Threshold Milestones: múltával and küszöbén",
                "text2": "'Múltával' expresses an elapsed interval or passage of time after which a new situation emerges ('évek múltával' - with the passing of years, 'a krízis múltával' - with the passing of the crisis). 'Küszöbén' (literally 'on the threshold of') marks being on the very verge of entering a decisive life phase or historic transition ('a felnőttkor küszöbén' - on the threshold of adulthood, 'egy demográfiai fordulat küszöbén' - on the brink of a demographic turning point).",
                "table_title": "Key Temporal Framing Postpositions",
                "table_rows": [
                    ["folyamán (+ possessive)", "az évszázad folyamán (over the course of the century)"],
                    ["során (+ possessive)", "az élete során (in the course of his/her life)"],
                    ["múltával (+ possessive)", "hónapok múltával (after the passing of months)"],
                    ["küszöbén (+ possessive)", "a nyugdíjazás küszöbén (on the threshold of retirement)"],
                ],
                "examples": [
                    {
                        "spanish": "Az elmúlt évtizedek folyamán a magyar társadalom korfája jelentősen átalakult.",
                        "english": "Over the course of recent decades, Hungarian society's population pyramid transformed significantly.",
                    },
                    {
                        "spanish": "A vizsgálat során a kutatók részletesen elemezték a születésszám alakulását.",
                        "english": "In the course of the investigation, researchers analyzed the trend in birth numbers in detail.",
                    },
                    {
                        "spanish": "Hosszú évek múltával a családok felismerték a generációk közötti támogatás fontosságát.",
                        "english": "With the passing of long years, families recognized the importance of intergenerational support.",
                    },
                    {
                        "spanish": "A fiatal egyetemisták a felnőttkor küszöbén állva tervezik a jövőjüket.",
                        "english": "Standing on the threshold of adulthood, young university students plan their future.",
                    },
                ],
                "tip": "Notice the possessive suffix required on the noun before 'folyamán', 'során', and 'küszöbén' (e.g. 'az élet folyamán', 'a kutatás során', 'a változás küszöbén').",
            },
            "words": [
                {"lemma": "folyamán", "translation": "in the course of / during", "pos": "postposition"},
                {"lemma": "során", "translation": "in the course of / throughout", "pos": "postposition"},
                {"lemma": "múltával", "translation": "after the passing of / with the lapse of", "pos": "postposition"},
                {"lemma": "küszöbén", "translation": "on the threshold of / on the brink of", "pos": "postposition"},
                {"lemma": "életút", "translation": "life course / life path", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'életút' mean in sociological and demographic contexts?",
                        [
                            "an individual's life course or life trajectory across different life stages",
                            "a legal document registering changes of residential address",
                            "a brief tourist trip taken across national borders",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which postposition conveys 'with the passing of' or 'after the lapse of' time?",
                        ["múltával", "helyett", "ellenére"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["folyamán", "in the course of / during"],
                            ["során", "throughout / during"],
                            ["múltával", "after the passing of"],
                            ["küszöbén", "on the threshold of"],
                            ["életút", "life course / trajectory"],
                        ],
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which postposition best completes: 'Az elmúlt évszázad ____ gyökeresen megváltozott a családok felépítése'?",
                        ["folyamán", "helyett", "nélkül"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the correct phrase expressing being on the brink of entering adulthood:",
                        ["a felnőttkor küszöbén", "a felnőttkor múltával", "a felnőttkor helyett"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A hosszú tárgyalások ____ a felek végre megállapodásra jutottak. (in the course of)",
                        "során",
                        "In the course of the long negotiations, the parties finally reached an agreement.",
                        ["b2-temporal-framing"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Évtizedek ____ ismerték csak fel a demográfiai változások valódi súlyát. (after the passing of)",
                        "múltával",
                        "Only after the passing of decades did they recognize the true weight of the demographic changes.",
                        ["b2-temporal-framing"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Az", "év", "folyamán", "több", "generációs", "találkozót", "szerveztek."],
                        ["Az", "év", "folyamán", "több", "generációs", "találkozót", "szerveztek."],
                        "Over the course of the year, they organized several generational meetings.",
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A szociológus az emberi ____ különböző szakaszait elemezte a tanulmányában. (life course)",
                        "életút",
                        "The sociologist analyzed the different stages of the human life course in his study.",
                        ["b2-22-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "fiatalok", "az", "önálló", "élet", "küszöbén", "állnak."],
                        ["A", "fiatalok", "az", "önálló", "élet", "küszöbén", "állnak."],
                        "The young people stand on the threshold of independent life.",
                        ["b2-22-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szociológus", "text": "Hogyan értékelné a családpolitikai intézkedések hatását?"},
                            {"speaker": "Kutató", "text": "____"},
                        ],
                        [
                            "A felmérés során világossá vált, hogy az évtizedek folyamán a családi struktúrák teljesen átalakultak.",
                            "A felmérés helyett nem beszélünk a családokról semmit.",
                            "Mivel a felmérés tegnap volt, ezért mindenki fiatal maradt.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Pályaválasztási tanácsadó", "text": "Milyen kihívásokkal szembesülnek ma a fiatal diplomások?"},
                            {"speaker": "Egyetemi oktató", "text": "____"},
                        ],
                        [
                            "A felnőttkor küszöbén állva sokan bizonytalanok a munkaerőpiaci elvárások miatt.",
                            "A felnőttkor múltával már senki sem akar dolgozni.",
                            "A küszöbön állva csak a lépcsőt takarítják a bérházban.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'folyamán' to describe economic shifts over past decades.",
                                "answer": "Az elmúlt évtizedek folyamán jelentősen megváltoztak a munkavállalási szokások.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'múltával' to describe understanding arriving after long years.",
                                "answer": "Hosszú évek múltával az ember jobban értékeli a családi kötelékeket.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Egy új technológiai korszak ____ állva fel kell készülnünk a kihívásokra. (on the threshold of)",
                        "küszöbén",
                        "Standing on the threshold of a new technological era, we must prepare for the challenges.",
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun refers to the full trajectory of a person's life across time?",
                        ["életút", "járda", "ösvény"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "By the Time That (mire + perfective preverbs)",
            "grammar_label": "Anteriority temporal clauses with mire and matrix adverbs (addigra, már)",
            "goals": [
                "I can form anterior temporal subordinate clauses using mire with perfective verbs",
                "I can correlate mire clauses with matrix adverbs such as már and addigra",
                "I can contrast actions completed by a temporal horizon with ongoing states",
            ],
            "grammar_doc": {
                "slug": "mire-anteriority-clauses",
                "title": "Anteriority Temporal Clauses: mire + Perfective Verbs",
                "text1_title": "Temporal Subordination with mire",
                "text1": "The temporal conjunction 'mire' introduces an anteriority clause meaning 'by the time that'. The subordinate clause typically contains a verb with a perfective verbal prefix (preverb: fel-, meg-, el-, ki-) denoting an action that reaches completion: 'Mire felnőtt...' ('By the time he grew up...'), 'Mire a törvényjavaslatot elfogadták...' ('By the time the bill was passed...').",
                "text2_title": "Matrix Clause Correlation: már and addigra",
                "text2": "The matrix clause governed by a 'mire' clause almost universally employs correlating temporal adverbs, predominantly 'már' ('already') or 'addigra' ('by that time'). This structure establishes a sharp contrast between the reference point marked by 'mire' and the prior completion of the main event: 'Mire hazaért, addigra a család már megvacsorázott' ('By the time he arrived home, by that time the family had already had dinner').",
                "table_title": "Correlating mire Clauses with Matrix Adverbs",
                "table_rows": [
                    ["mire + past perfective", "Mire felébredt, már kisütött a nap."],
                    ["addigra correlation", "Mire a segély megérkezett, addigra felépült a ház."],
                    ["mire + present perfective", "Mire megérkezel, már készen lesz az ebéd."],
                    ["contrast of states", "Mire nyugdíjba ment, megváltozott a társadalom."],
                ],
                "examples": [
                    {
                        "spanish": "Mire a fiatal generáció felnőtt, a munkaerőpiaci viszonyok teljesen átalakultak.",
                        "english": "By the time the young generation grew up, labor market conditions had completely transformed.",
                    },
                    {
                        "spanish": "Mire a nagyszülők nyugdíjba vonultak, addigra a gyermekeik már önálló egzisztenciát teremtettek.",
                        "english": "By the time the grandparents retired, by then their children had already established an independent livelihood.",
                    },
                    {
                        "spanish": "Mire a demográfiai intézkedések hatni kezdtek, már jelentősen megnőtt az idős korosztály aránya.",
                        "english": "By the time the demographic measures began to take effect, the proportion of the elderly cohort had already grown significantly.",
                    },
                    {
                        "spanish": "Mire a reformokat bevezették, addigra a költségvetési hiány már tarthatatlanná vált.",
                        "english": "By the time the reforms were introduced, by then the budget deficit had already become unsustainable.",
                    },
                ],
                "tip": "Always ensure the verb in the 'mire' clause carries the appropriate perfective preverb (meg-, fel-, el-) when signaling that the milestone has been fully reached.",
            },
            "words": [
                {"lemma": "mire", "translation": "by the time that", "pos": "conjunction"},
                {"lemma": "addigra", "translation": "by that time / by then", "pos": "adverb"},
                {"lemma": "felnő", "translation": "to grow up / mature", "pos": "verb"},
                {"lemma": "nyugdíjba vonul", "translation": "to retire", "pos": "expression"},
                {"lemma": "idősödés", "translation": "aging / senescence", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the meaning of the expression 'nyugdíjba vonul'?",
                        [
                            "to retire from active professional employment",
                            "to enroll in an academic degree program",
                            "to move to another city for work",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adverb correlates with 'mire' to mean 'by that time / by then'?",
                        ["addigra", "eddig", "mindig"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["mire", "by the time that"],
                            ["addigra", "by that time / by then"],
                            ["felnő", "to grow up / mature"],
                            ["nyugdíjba vonul", "to retire"],
                            ["idősödés", "aging / senescence"],
                        ],
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which conjunction introduces anteriority in: '____ a gyermekek felnőttek, a szülők már idős korba léptek'?",
                        ["Mire", "Mivel", "Noha"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correlating adverb that best fits: 'Mire megérkezett a segítség, ____ a kárt felszámolták':",
                        ["addigra", "ezért", "holott"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "____ a kutatók befejezték a felmérést, már új demográfiai adatok láttak napvilágot. (By the time that)",
                        "Mire",
                        "By the time the researchers finished the survey, new demographic data had already come to light.",
                        ["b2-temporal-framing"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Mire az orvos nyugdíjba ment, ____ több generáció nőtt fel a keze alatt. (by then)",
                        "addigra",
                        "By the time the doctor retired, by then several generations had grown up under his care.",
                        ["b2-temporal-framing"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Mire", "a", "gyerekek", "felnőttek,", "már", "megváltozott", "a", "világ."],
                        ["Mire", "a", "gyerekek", "felnőttek,", "már", "megváltozott", "a", "világ."],
                        "By the time the children grew up, the world had already changed.",
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A professzor negyven év tanítás után úgy döntött, hogy jövőre ____. (to retire)",
                        "nyugdíjba vonul",
                        "After forty years of teaching, the professor decided to retire next year.",
                        ["b2-22-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "társadalom", "idősödése", "új", "szociális", "kihívásokat", "teremt."],
                        ["A", "társadalom", "idősödése", "új", "szociális", "kihívásokat", "teremt."],
                        "The aging of society creates new social challenges.",
                        ["b2-22-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kolléga", "text": "Mikor kezdődik a szakmai nyugdíjas búcsúztató?"},
                            {"speaker": "Titkár", "text": "____"},
                        ],
                        [
                            "Mire az igazgató úr megérkezik, addigra minden vendég elfoglalja a helyét a teremben.",
                            "Mivel senki sem jött el, ezért elmarad az egész ünnepség.",
                            "Mire felnövünk, addigra elfelejtjük az egészet.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Családkutató", "text": "Hogyan élik meg a családok a szülők idősödését?"},
                            {"speaker": "Pszichológus", "text": "____"},
                        ],
                        [
                            "Mire a felnőtt gyermekek észreveszik a gondozás szükségességét, addigra a szülők már sok segítséget igényelnek.",
                            "Mire a szülők fiatalok, már nincsenek gyerekeik.",
                            "Addigra mindenki elment, mert senki sem akart beszélgetni.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'Mire..., addigra már...' describing generational shifts upon retirement.",
                                "answer": "Mire az idősebb generáció nyugdíjba vonult, addigra már a fiatalok vették át a gazdaság irányítását.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'Mire..., már...' about children growing up before parents realize it.",
                                "answer": "Mire a szülők feleszméltek, már fel is nőttek a gyermekeik.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "____ a reformtervezet a parlament elé került, a gazdasági helyzet már rosszabbodott. (By the time that)",
                        "Mire",
                        "By the time the reform proposal reached parliament, the economic situation had already worsened.",
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the demographic process of a population's average age increasing?",
                        ["idősödés", "felnövés", "születésszám"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Generational Expectations and Care",
            "grammar_label": "Life-stage idioms (gyerekkorában, öregségére, fiatalként, idős korára)",
            "goals": [
                "I can use temporal life-stage expressions (gyerekkorában, öregségére, fiatalként)",
                "I can discuss intergenerational care obligations and family expectations",
                "I can express changes in perspective across different generational cohorts",
            ],
            "grammar_doc": {
                "slug": "generational-expectations-care",
                "title": "Age Idioms & Life-Stage Framing: gyerekkorában, öregségére, fiatalként",
                "text1_title": "Inessive and Sublative Life-Stage Expressions",
                "text1": "Hungarian frames stages of life using crystallized case-marked nouns. Inessive forms with possessive suffixes ('gyerekkorában' - in his/her childhood, 'fiatalkorában' - in his/her youth) describe static periods of life during which formative experiences occurred. In contrast, the sublative form 'öregségére' (or 'idős korára') indicates looking forward toward the twilight years or state arrived at in old age: 'Öregségére egyedül maradt a faluban' ('For his old age, he remained alone in the village').",
                "text2_title": "Essive-Formal fiatalként and Intergenerational Responsibility",
                "text2": "The essive-formal suffix -ként ('fiatalként' - as a youth, 'szülőként' - as a parent, 'gondozóként' - as a caregiver) expresses the societal role or subjective identity held during a particular life phase. In discussions of intergenerational solidarity ('nemzedékek közötti szolidaritás'), these idioms provide the nuance needed to analyze how expectations shift as children become caregivers to their aging parents.",
                "table_title": "Life-Stage Idiomatic Expressions",
                "table_rows": [
                    ["gyerekkorában (inessive)", "Gyerekkorában sokat tanult a nagyszüleitől."],
                    ["öregségére (sublative)", "Öregségére békés otthonra vágyott."],
                    ["fiatalként (essive-formal)", "Fiatalként még nem látta át a családi felelősséget."],
                    ["idős korára (sublative)", "Idős korára támaszra szorult a mindennapokban."],
                ],
                "examples": [
                    {
                        "spanish": "Gyerekkorában még több generáció élt együtt ugyanabban a vidéki házban.",
                        "english": "In his childhood, multiple generations still lived together in the same rural house.",
                    },
                    {
                        "spanish": "Az idős asszony öregségére sem veszítette el szellemi frissességét és humorát.",
                        "english": "Even in her old age, the elderly woman did not lose her mental acuity and sense of humor.",
                    },
                    {
                        "spanish": "Fiatalként az ember hajlamos azt hinni, hogy a szülei mindig erősek és önállóak maradnak.",
                        "english": "As a young person, one tends to believe that one's parents will always remain strong and independent.",
                    },
                    {
                        "spanish": "A nemzedékek közötti gondoskodás nemcsak erkölcsi kötelesség, hanem társadalmi alapérték.",
                        "english": "Intergenerational care is not only a moral duty, but also a fundamental societal value.",
                    },
                ],
                "tip": "Distinguish 'időskorában' (in his old age, static time) from 'idős korára' / 'öregségére' (for his old age, reaching that stage).",
            },
            "words": [
                {"lemma": "öregségére", "translation": "in one's old age / for one's twilight years", "pos": "adverb"},
                {"lemma": "nemzedék", "translation": "generation", "pos": "noun"},
                {"lemma": "gondoskodás", "translation": "care / providing care", "pos": "noun"},
                {"lemma": "elvárás", "translation": "expectation", "pos": "noun"},
                {"lemma": "fiatalként", "translation": "as a young person / as a youth", "pos": "adverb"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is meant by 'nemzedék' in demographic and social discourse?",
                        [
                            "a generational cohort born and living in roughly the same time period",
                            "an official government pension fund division",
                            "a legal contract determining child support payments",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which word means 'in one's old age / for one's twilight years' in Hungarian?",
                        ["öregségére", "gyerekkorában", "fiatalként"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["öregségére", "in one's old age"],
                            ["nemzedék", "generation"],
                            ["gondoskodás", "care / caregiving"],
                            ["elvárás", "expectation"],
                            ["fiatalként", "as a young person"],
                        ],
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct sublative form: 'A gazda ____ csendes, vidéki nyugalomra vágyott':",
                        ["öregségére", "gyerekkorában", "fiatalként"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which form expressing subjective role means 'as a young person'?",
                        ["fiatalként", "fiatalsága", "fiatalonként"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Nagyapám ____ sokat dolgozott a földeken, és korán megtanulta a munka értékét. (in his childhood)",
                        "gyerekkorában",
                        "In his childhood, my grandfather worked hard in the fields and learned the value of work early.",
                        ["b2-temporal-framing"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Nem könnyű feladat ____ helytállni a családban és a munkahelyen egyszerre. (as a young person)",
                        "fiatalként",
                        "It is not an easy task to stand one's ground as a young person in the family and at the workplace at the same time.",
                        ["b2-temporal-framing"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Öregségére", "minden", "ember", "szeretetre", "és", "tiszteletre", "vágyik."],
                        ["Öregségére", "minden", "ember", "szeretetre", "és", "tiszteletre", "vágyik."],
                        "In one's old age, every human longs for love and respect.",
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A családi ____ sokszor feszültséget okoznak a fiatal és az idős korosztály között. (expectations)",
                        "elvárások",
                        "Family expectations often cause tension between the young and old cohorts.",
                        ["b2-22-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["Az", "idősekről", "való", "gondoskodás", "közös", "társadalmi", "kötelességünk."],
                        ["Az", "idősekről", "való", "gondoskodás", "közös", "társadalmi", "kötelességünk."],
                        "Caring for the elderly is our shared social duty.",
                        ["b2-22-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Unoka", "text": "Hogyan tudjuk legjobban támogatni a nagymamát most, hogy egyedül maradt?"},
                            {"speaker": "Édesanya", "text": "____"},
                        ],
                        [
                            "Öregségére megérdemli a folyamatos gondoskodást; fiatalként ő is mindent megadott nekünk.",
                            "Gyerekkorában elköltözött, tehát nem kell törődnünk vele.",
                            "Nemzedék helyett inkább senki se menjen hozzá látogatóba.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Szociális munkás", "text": "Milyen elvárásokat fogalmaznak meg a hozzátartozók az idősotthonnal szemben?"},
                            {"speaker": "Intézményvezető", "text": "____"},
                        ],
                        [
                            "A családok elvárása az, hogy a lakók idős korukra méltóságteljes és biztonságos környezetben élhessenek.",
                            "A lakók gyerekkorában nincsenek elvárások, mert mindenki alszik.",
                            "Fiatalként nem kell ételt adni senkinek az intézményben.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'öregségére' about someone wanting peace and security in their twilight years.",
                                "answer": "Öregségére békés környezetre és a családja támogatására vágyott.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'fiatalként' contrasting youth perspectives with later responsibilities.",
                                "answer": "Fiatalként az ember még nem látja át, milyen sok áldozatot követel a család fenntartása.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A híres festő ____ sok nélkülözést tapasztalt, de sosem adta fel a művészetet. (in his childhood)",
                        "gyerekkorában",
                        "In his childhood, the famous painter experienced much deprivation, but never gave up on art.",
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes providing attention, assistance, and physical help to dependent family members?",
                        ["gondoskodás", "elvárás", "nemzedék"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Interpreting Demographic Data",
            "grammar_label": "Demographic trend discourse and quantitative framing (korfa, arányszám, népességfogyás)",
            "goals": [
                "I can interpret and describe demographic shifts and fertility rates",
                "I can discuss the ratio of active workers to pensioners using quantitative framing",
                "I can analyze population decline and migration trends in professional prose",
            ],
            "grammar_doc": {
                "slug": "demographic-data-trends",
                "title": "Analyzing Demographic Shifts: Cohorts, Pyramids & Rates",
                "text1_title": "Expressing Quantitative Demographic Change",
                "text1": "When reporting demographic findings, Hungarian employs specific compound nouns and nominal predicates. The aging of society is captured by 'korfa' (population age pyramid), whose distortion reflects shrinking birth rates ('születésszám csökkenése') and lengthening life expectancy. Sociological prose uses terms such as 'termékenységi arányszám' (total fertility rate) and 'népességfogyás' (depopulation / demographic contraction) combined with postpositional temporal clauses.",
                "text2_title": "The Dependency Ratio and Labor Market Pressures",
                "text2": "The economic balance between generations is quantified through the 'eltartottsági ráta' (dependency ratio), which compares the economically inactive population (children and pensioners) to active contributors. Formal texts connect demographic cause and effect using adverbial participles and temporal phrases: 'A születésszám mérséklődésével párhuzamosan a társadalom korfája fokozatosan elöregszik'.",
                "table_title": "Key Demographic Concepts and Vocabulary",
                "table_rows": [
                    ["termékenységi arányszám", "A termékenységi arányszám elmarad a reprodukciós szinttől."],
                    ["korfa", "A korfa felső rétege jelentősen kiszélesedett."],
                    ["népességfogyás", "A népességfogyás lassítására új intézkedéseket hoztak."],
                    ["eltartottsági ráta", "Az eltartottsági ráta növekedése terheli a gazdaságot."],
                ],
                "examples": [
                    {
                        "spanish": "A statisztikai hivatal legfrissebb jelentése szerint a születésszám kismértékben emelkedett a tavalyi év folyamán.",
                        "english": "According to the statistical office's latest report, the birth rate increased slightly in the course of last year.",
                    },
                    {
                        "spanish": "A tartósan alacsony termékenységi arányszám következtében a népességfogyás folyamata felgyorsult.",
                        "english": "As a consequence of the persistently low fertility rate, the process of population decline accelerated.",
                    },
                    {
                        "spanish": "A magyar korfa alakja egyre inkább egy urnára hasonlít, ami az idősödő társadalom tipikus jele.",
                        "english": "The shape of the Hungarian age pyramid increasingly resembles an urn, which is a typical sign of an aging society.",
                    },
                    {
                        "spanish": "Az emelkedő eltartottsági ráta komoly kihívás elé állítja a nyugdíjrendszert és az egészségügyet.",
                        "english": "The rising dependency ratio poses a serious challenge to the pension system and healthcare.",
                    },
                ],
                "tip": "When describing numbers in demographics, verbs of movement and shift (emelkedik, mérséklődik, eltolódik, szűkül) commonly take adverbial modifiers like 'fokozatosan' (gradually) and 'számottevően' (significantly).",
            },
            "words": [
                {"lemma": "születésszám", "translation": "birth rate / number of births", "pos": "noun"},
                {"lemma": "termékenységi arányszám", "translation": "total fertility rate", "pos": "noun"},
                {"lemma": "korfa", "translation": "population pyramid / age structure", "pos": "noun"},
                {"lemma": "népességfogyás", "translation": "depopulation / population decline", "pos": "noun"},
                {"lemma": "eltartottsági ráta", "translation": "dependency ratio", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'korfa' in demographic science?",
                        [
                            "a graphical diagram illustrating the age and sex distribution of a population",
                            "a family genealogical tree recording noble ancestors",
                            "a forestry register cataloguing protected ancient trees",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the ratio of economically dependent persons to the working-age population?",
                        ["eltartottsági ráta", "születésszám", "népességfogyás"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["születésszám", "number of births"],
                            ["termékenységi arányszám", "total fertility rate"],
                            ["korfa", "population pyramid"],
                            ["népességfogyás", "population decline"],
                            ["eltartottsági ráta", "dependency ratio"],
                        ],
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which postposition fits best: 'A demográfiai kutatás ____ a szakemberek több ezer családot kérdeztek meg'?",
                        ["során", "múltával", "küszöbén"],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the sentence correctly combining temporal framing with demographic trend description:",
                        [
                            "Az elmúlt évtizedek folyamán a termékenységi arányszám jelentősen mérséklődött.",
                            "Az elmúlt évtizedek helyett a termékenységi arányszám nem létezik.",
                            "Mire a termékenységi arányszám, addigra mindenki elment vidékre.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A népességadatok alapos elemzése ____ kiderült, hogy a fiatalok aránya csökken. (in the course of)",
                        "során",
                        "In the course of thorough analysis of population data, it turned out that the proportion of young people is falling.",
                        ["b2-temporal-framing"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A válságos évek ____ a születésszám fokozatosan helyreállt. (after the passing of)",
                        "múltával",
                        "With the passing of the crisis years, the birth rate gradually recovered.",
                        ["b2-temporal-framing"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "demográfiai", "átalakulás", "folyamán", "megváltozott", "a", "korfa", "alakja."],
                        ["A", "demográfiai", "átalakulás", "folyamán", "megváltozott", "a", "korfa", "alakja."],
                        "In the course of the demographic transition, the shape of the age pyramid changed.",
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A tartós ____ megállítása a gazdaságpolitika egyik legfontosabb célkitűzése. (population decline)",
                        "népességfogyás",
                        "Halting persistent population decline is one of the most important objectives of economic policy.",
                        ["b2-22-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "magas", "eltartottsági", "ráta", "túlterheli", "az", "állami", "költségvetést."],
                        ["A", "magas", "eltartottsági", "ráta", "túlterheli", "az", "állami", "költségvetést."],
                        "The high dependency ratio overburdens the state budget.",
                        ["b2-22-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Demográfus", "text": "Milyen következtetéseket vonhatunk le az idei népszámlálásból?"},
                            {"speaker": "Közgazdász", "text": "____"},
                        ],
                        [
                            "A vizsgálat során beigazolódott, hogy a születésszám elmarad a várakozásoktól, miközben az eltartottsági ráta emelkedik.",
                            "Semmit sem tudunk meg a számokból, mert a korfa csak egy egyszerű fa az erdőben.",
                            "Múltával senki sem számolja a lakosságot, mert minek.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Mivel magyarázható a hazai korfa eltolódása?"},
                            {"speaker": "Egyetemi tanár", "text": "____"},
                        ],
                        [
                            "Az elmúlt évtizedek folyamán a várható élettartam nőtt, miközben a termékenységi arányszám alacsony maradt.",
                            "Mire a korfa megmozdult, már senki sem lakott a városokban.",
                            "Azért tolódott el, mert a naptárak hibásak voltak.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'során' and 'termékenységi arányszám' analyzing statistical findings.",
                                "answer": "A kutatás során kiderült, hogy a termékenységi arányszám elmarad a kívánt szinttől.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'folyamán' and 'népességfogyás' discussing long-term demographic challenges.",
                                "answer": "Az elmúlt fél évszázad folyamán a népességfogyás tartós jelenséggé vált a régióban.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Egy történelmi demográfiai fordulat ____ állva új családtámogatási rendszert dolgoztak ki. (on the threshold of)",
                        "küszöbén",
                        "Standing on the threshold of a historic demographic turning point, they developed a new family support system.",
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes the average number of children born to a woman over her childbearing years?",
                        ["termékenységi arányszám", "eltartottsági ráta", "korfa"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Debating Social Policy for an Aging Society",
            "grammar_label": "Integrating temporal framing postpositions into demographic policy debate",
            "goals": [
                "I can synthesize temporal framing connectors into policy recommendations",
                "I can articulate arguments concerning pension sustainability and healthcare infrastructure",
                "I can debate public policies aimed at intergenerational solidarity",
            ],
            "grammar_doc": {
                "slug": "aging-society-policy-debate",
                "title": "Debating Social Policy & Intergenerational Solidarity",
                "text1_title": "Synthesizing Temporal Framing into Policy Arguments",
                "text1": "Policy debate concerning an aging society requires weaving temporal framing postpositions ('folyamán', 'során', 'küszöbén') together with socio-economic arguments. When discussing the sustainability ('fenntarthatóság') of the pension system ('nyugdíjrendszer'), speakers must articulate how changes in the ratio of active workers ('járulékfizetők') to retirees over decades necessitate structural interventions before critical demographic thresholds are crossed.",
                "text2_title": "Institutional Welfare and Intergenerational Solidarity",
                "text2": "Discourse around public welfare ('társadalombiztosítás') balances state support with familial obligations. Argumentative connectors and modal constructions allow participants to weigh fiscal prudence against human dignity: 'Nemzedékek közötti szolidaritásra van szükség, amelynek során a fiatalabb korosztályok méltó gondoskodást biztosítanak az idősek számára'.",
                "table_title": "Socio-Demographic Policy Discourse",
                "table_rows": [
                    ["fenntarthatóság", "A nyugdíjrendszer hosszú távú fenntarthatósága kiemelt cél."],
                    ["járulékfizető", "A járulékfizetők arányának csökkenése reformokat sürget."],
                    ["társadalombiztosítás", "A társadalombiztosítás rendszere átfogó felülvizsgálatra szorul."],
                    ["nemzedékek közötti", "A nemzedékek közötti szolidaritás a társadalom alapköve."],
                ],
                "examples": [
                    {
                        "spanish": "A nyugdíjrendszer fenntarthatósága érdekében az elkövetkező évek folyamán átfogó reformokat kell bevezetni.",
                        "english": "In the interest of the pension system's sustainability, comprehensive reforms must be introduced over the course of coming years.",
                    },
                    {
                        "spanish": "Mire a nagy létszámú korosztályok elérik a nyugdíjkorhatárt, a társadalombiztosítás terhei jelentősen megnőnek.",
                        "english": "By the time large demographic cohorts reach retirement age, social security burdens will grow significantly.",
                    },
                    {
                        "spanish": "A vita során a szakértők rámutattak, hogy a járulékfizetők számának csökkenése azonnali lépéseket kíván.",
                        "english": "During the debate, experts pointed out that the decline in the number of contribution payers demands immediate steps.",
                    },
                    {
                        "spanish": "A nemzedékek közötti együttműködés megőrzése a modern jóléti állam fennmaradásának záloga.",
                        "english": "Preserving intergenerational cooperation is the guarantee of the modern welfare state's survival.",
                    },
                ],
                "tip": "In high-register policy debates, prefer formal compound nominals ('járulékfizetői bázis', 'nyugdíjkorhatár-emelés') linked with temporal postpositions ('az elkövetkező évtizedek folyamán').",
            },
            "words": [
                {"lemma": "nyugdíjrendszer", "translation": "pension system", "pos": "noun"},
                {"lemma": "fenntarthatóság", "translation": "sustainability", "pos": "noun"},
                {"lemma": "társadalombiztosítás", "translation": "social security", "pos": "noun"},
                {"lemma": "járulékfizető", "translation": "taxpayer / contribution payer", "pos": "noun"},
                {"lemma": "nemzedékek közötti", "translation": "intergenerational", "pos": "adjective"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'fenntarthatóság' in the context of pension and welfare systems?",
                        [
                            "the capacity of a system to maintain financial and operational equilibrium over the long term",
                            "a temporary emergency grant awarded to distressed families",
                            "a mandatory annual audit performed by tax authorities",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Who is a 'járulékfizető' in the social security framework?",
                        [
                            "an employed individual who pays mandatory statutory contributions into the state fund",
                            "a child receiving educational allowances from municipal funds",
                            "a tourist paying local commercial accommodation taxes",
                        ],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["nyugdíjrendszer", "pension system"],
                            ["fenntarthatóság", "sustainability"],
                            ["társadalombiztosítás", "social security"],
                            ["járulékfizető", "contribution payer"],
                            ["nemzedékek közötti", "intergenerational"],
                        ],
                        ["b2-22-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence best synthesizes temporal framing with policy debate?",
                        [
                            "A parlamenti vita során nyilvánvalóvá vált, hogy a nyugdíjrendszer azonnali átalakításra szorul.",
                            "A vita helyett senki sem ment be a parlamentbe, mert esett az eső.",
                            "Múltával nem fizet senki járulékot, mert nincs pénz.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence using anteriority to warn of fiscal pressure:",
                        [
                            "Mire a baby-boom nemzedék nyugdíjba vonul, a költségvetési terhek megduplázódnak.",
                            "Mivel a baby-boom nemzedék fiatal, ezért nincsenek nyugdíjak.",
                            "Addigra mindenki elment külföldre, mert nem volt más választás.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Az elkövetkező évtizedek ____ garantálni kell a nyugdíjak reálértékének megőrzését. (in the course of)",
                        "folyamán",
                        "Over the course of the coming decades, the preservation of the real value of pensions must be guaranteed.",
                        ["b2-temporal-framing"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A gazdasági válság ____ az állam felülvizsgálta a társadalombiztosítás kiadásait. (in the course of)",
                        "során",
                        "In the course of the economic crisis, the state reviewed social security expenditures.",
                        ["b2-temporal-framing"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Egy", "új", "társadalmi", "szerződés", "küszöbén", "áll", "az", "ország."],
                        ["Egy", "új", "társadalmi", "szerződés", "küszöbén", "áll", "az", "ország."],
                        "The country stands on the threshold of a new social contract.",
                        ["b2-temporal-framing"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A reformok célja a hazai ____ hosszú távú stabilitásának biztosítása. (pension system)",
                        "nyugdíjrendszer",
                        "The aim of the reforms is ensuring the long-term stability of the domestic pension system.",
                        ["b2-22-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "nemzedékek", "közötti", "szolidaritás", "erősítése", "közös", "célunk."],
                        ["A", "nemzedékek", "közötti", "szolidaritás", "erősítése", "közös", "célunk."],
                        "Strengthening intergenerational solidarity is our shared goal.",
                        ["b2-22-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Miniszter", "text": "Hogyan tartható fenn a társadalombiztosítás egyensúlya?"},
                            {"speaker": "Közgazdász", "text": "____"},
                        ],
                        [
                            "A viták során kiderült: ha a járulékfizetők száma csökken, az elkövetkező évek folyamán növelni kell a hatékonyságot.",
                            "Mire a miniszter megkérdezte, már bezárták a parlamentet.",
                            "Nemzedékek közötti szolidaritás helyett mindenki csak magára gondoljon.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ellenzéki képviselő", "text": "Nem tart attól, hogy a reformok hátrányosan érintik az időseket?"},
                            {"speaker": "Kormánypárti képviselő", "text": "____"},
                        ],
                        [
                            "Éppen ellenkezőleg: a tervezett intézkedések célja, hogy öregségükre mindenki méltó ellátásban részesüljön.",
                            "Gyerekkorában senki sem kap nyugdíjat, tehát nem értem a kérdést.",
                            "A küszöbön állva nem lehet beszélni a nyugdíjakról.",
                        ],
                        0,
                        ["b2-temporal-framing"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'folyamán' and 'fenntarthatóság' arguing for long-term welfare reform.",
                                "answer": "Az elkövetkező évek folyamán meg kell teremteni a nyugdíjrendszer pénzügyi fenntarthatóságát.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'nemzedékek közötti' and 'szolidaritás' highlighting social responsibility.",
                                "answer": "A nemzedékek közötti szolidaritás nélkül egyetlen modern társadalom sem maradhat fenn tartósan.",
                            }
                        ],
                        ["b2-temporal-framing"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Mire a törvény hatályba lép, ____ az érintett intézmények felkészülnek a végrehajtásra. (by then)",
                        "addigra",
                        "By the time the law takes effect, by then the affected institutions will be prepared for implementation.",
                        ["b2-temporal-framing"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which compound adjective expresses mutual relations and support across age cohorts?",
                        ["nemzedékek közötti", "járulékfizető", "nyugdíjrendszer"],
                        0,
                        ["b2-22-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can confidently apply temporal framing postpositions (folyamán, során, múltával, küszöbén)",
            "I can formulate anterior temporal clauses using mire and correlating matrix adverbs",
            "I can discuss demographic trends, cohort shifts, and intergenerational welfare policy",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["életút", "life course / trajectory"],
                    ["korfa", "population pyramid"],
                    ["nyugdíjrendszer", "pension system"],
                    ["fenntarthatóság", "sustainability"],
                    ["nemzedék", "generation"],
                ],
                ["b2-22-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'eltartottsági ráta' measure in demographic statistics?",
                [
                    "the ratio of economically inactive dependents to the active working-age population",
                    "the percentage of citizens owning residential real estate",
                    "the proportion of foreign workers employed in national factories",
                ],
                0,
                ["b2-22-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates anteriority using 'mire' and 'addigra'?",
                [
                    "Mire a konferencia elkezdődött, addigra minden szakértő megérkezett a terembe.",
                    "Mire a konferencia elkezdődött, mivel senki sem érkezett meg.",
                    "Addigra a konferencia elkezdődött, holott senki sem beszélt.",
                ],
                0,
                ["b2-temporal-framing"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A tartósan alacsony ____ miatt a népesség természetes fogyása tovább folytatódik. (total fertility rate)",
                "termékenységi arányszám",
                "Due to the persistently low total fertility rate, the natural decline of the population continues.",
                ["b2-22-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "Hosszú évek ____ az orvosok felismerték a megelőzés döntő fontosságát. (after the passing of)",
                "múltával",
                "With the passing of long years, doctors recognized the decisive importance of prevention.",
                ["b2-temporal-framing"],
            ),
            fb(
                "grammar",
                "recall",
                "A nyugdíjkorhatár ____ állva az ember visszatekint az elvégzett munkájára. (on the threshold of)",
                "küszöbén",
                "Standing on the threshold of retirement age, a person looks back upon the work accomplished.",
                ["b2-temporal-framing"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'folyamán' correctly frames an extended duration:",
                [
                    "Az elmúlt két évtized folyamán alapvetően átalakult a családpolitikai támogatások rendszere.",
                    "Az elmúlt két évtized folyamán nem volt tegnap este.",
                    "A folyamán az elnök beszélt három percet.",
                ],
                0,
                ["b2-temporal-framing"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Gazdaságpolitikus", "text": "Hogyan biztosítható a nyugdíjak fedezete a jövőben?"},
                    {"speaker": "Kutatóintézeti vezető", "text": "____"},
                ],
                [
                    "A felmérések során bebizonyosodott, hogy a járulékfizetők bázisát kell szélesíteni az elkövetkező évek folyamán.",
                    "Mire a pénz elfogyott, már senki sem akart fizetni semmit.",
                    "Nemzedékek közötti szolidaritás helyett inkább zárjuk be az intézményeket.",
                ],
                0,
                ["b2-temporal-framing"],
            ),
            mc(
                "grammar",
                "in-context",
                "Why is 'öregségére' preferred over 'gyerekkorában' in: 'Az idős író ____ sem hagyta abba az alkotást'?",
                [
                    "Because it specifically references reaching and being in the advanced years of one's life.",
                    "Because it is an accusative form required by the verb.",
                    "Because 'gyerekkorában' can only be used with past tense passive verbs.",
                ],
                0,
                ["b2-temporal-framing"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["Mire", "a", "segély", "megérkezett,", "addigra", "már", "újjáépítették", "a", "falut."],
                ["Mire", "a", "segély", "megérkezett,", "addigra", "már", "újjáépítették", "a", "falut."],
                "By the time the aid arrived, by then they had already rebuilt the village.",
                ["b2-temporal-framing"],
            ),
            sb(
                "grammar",
                "produce",
                ["Az", "életút", "során", "minden", "generáció", "értékes", "tapasztalatokat", "szerez."],
                ["Az", "életút", "során", "minden", "generáció", "értékes", "tapasztalatokat", "szerez."],
                "In the course of the life path, every generation acquires valuable experiences.",
                ["b2-temporal-framing"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause demographic analysis using 'folyamán' (duration), 'mire' (anteriority), and 'addigra' (correlation).",
                        "answer": "Az elmúlt évtizedek folyamán folyamatosan csökkent a születésszám; és mire a szakpolitikusok felismerték a veszélyt, addigra már jelentősen elöregedett a társadalom korfája.",
                    }
                ],
                ["b2-temporal-framing"],
            ),
],
},
}
# ==============================================================================
# UNIT 23: Urban Space, Architecture & Coexistence
# ==============================================================================
UNIT_23 = {
"unit_num": 23,
"title": "Urban Space, Architecture & Coexistence",
"grammar_summary": "Relative clauses governed by spatial and causal postpositions (amely mellett, amely által, akihez képest) and nested possessive relative chains (amelynek a tetején, akiknek segítségével).",
"grammar_skill": "b2-relative-postpositions",
"vocab_skill": "b2-23-vocab",
"theme": "Urban space, architecture and coexistence",
"intro_body": [
"A közép-európai nagyvárosok, különösen Budapest építészeti öröksége sajátos térbeli és társadalmi viszonyokat teremtett. A körfolyosós bérházak belső udvarai, a Duna-hidak látványa és a műemléki védelem alatt álló homlokzatok nem csupán esztétikai formák, hanem az emberi együttélés történelmi színterei is.",
"Ebben a fejezetben elsajátíthatja a névutókkal álló vonatkozó névmások kifinomult használatát (amely mellett, amely által, akik között), valamint a balra ágazó birtokos vonatkozó szerkezeteket (amelynek a tetején, akiknek segítségével). Ottlik Géza 'Buda' című remekműve segítségével pedig felfedezheti a városi terek rejtett geometriáját és a kőbe zárt emlékezetet.",
],
"classic_story": {
"slug": "buda",
"author": "Ottlik Géza",
"work": "Buda (1993)",
"title": "Hidak, bérházak és budai udvarok",
"summary": "Bébé és Medve Gábor a budai hegyoldal és a Duna-part zegzugos utcáit járva a városi terek rejtett geometriájáról, a bérházak körfolyosóiról és a múló idő kőbe vésett nyomairól beszélgetnek.",
"characters": ["Bébé", "Medve Gábor"],
"paragraphs": [
{
"type": "narration",
"text": "A budai alkonyat hűvös párája lassan ellepte a Duna felett átívelő hidakat. Bébé és Medve Gábor a vár alatti csendes macskaköves utcákon lépkedtek, ahol a sárga gázlámpák fénye megvilágította a régi bérházak omladozó homlokzatát.",
},
{
"type": "dialogue",
"speaker": "Bébé",
"text": "Nézd ezt az épületet, Medve! Egy olyan bérház, amely mellett százszor elmentünk gyerekkorunkban, mégsem vettük észre a rejtett arányait. A körfolyosó, amely a belső udvar fölé magasodik, szinte lebeg a térben.",
},
{
"type": "dialogue",
"speaker": "Medve Gábor",
"text": "A budai tereknek sajátos törvényeik vannak, Bébé. Nem pusztán kőből és habarcsból épültek, hanem az emberi pillantásokból, amelyek által értelmet nyernek. Az a kapualj ott, amely felé most tartunk, évszázadok történetét rejti a falai között.",
},
{
"type": "narration",
"text": "Beléptek a boltíves kapun, és megálltak a szűk, négyszögletű belső udvaron. A csend itt más minőségű volt, mint az utcán: a lakóközösség mindennapi életének halk visszhangjai verődtek vissza a gangok korlátjairól.",
},
{
"type": "dialogue",
"speaker": "Bébé",
"text": "Mindig csodáltam azokat az embereket, akik ezekben a házakban élnek, és akiknek a sorsa összefonódik a közös lépcsőházak homályában. Olyan világ ez, amelynek udvarán a múlt és a jelen egymásba ér, és amelynek ritmusát nem a modern sietség határozza meg.",
},
{
"type": "dialogue",
"speaker": "Medve Gábor",
"text": "Ez a városkép lényege: a megmaradás. Lehet hidakat robbantani és falakat rombolni, de a belső terek geometriája, amelyhez képest az emberi élet mulandó, változatlan marad. A műemlékvédelem nem csupán téglák védelme, hanem az emlékezet őrzése.",
},
{
"type": "narration",
"text": "Felnéztek az ég felé, amelyet a bérház négyszögletes tetővonala keretezett. Egy magányos csillag ragyogott fel a kémények felett, miközben a Dunáról felszálló köd lassan elérte a várhegy lejtőit.",
},
{
"type": "dialogue",
"speaker": "Bébé",
"text": "Igazad van, Medve. Amíg ezek az udvarok állnak, és amíg van kivel megosztani ezt a csendet, addig a város nem veszítheti el a lelkét.",
},
],
"reading_questions": [
{
"question": "Milyen sajátosságot emel ki Bébé a régi budai bérházzal kapcsolatban?",
"options": [
"A rejtett arányait és a belső udvar fölé magasodó körfolyosóját.",
"A modern lift és a fényes üvegfelületek jelenlétét.",
"Az épület lebontására vonatkozó hatósági rendeletet.",
],
"correct": 0,
},
{
"question": "Hogyan értelmezi Medve Gábor a műemlékvédelmet és a városi tereket?",
"options": [
"Nem csupán téglák védelmeként, hanem az emberi emlékezet és belső geometria őrzéseként.",
"Kizárólag pénzügyi és turisztikai hasznot hozó beruházásként.",
"Olyan feladatként, amely gátolja a modern közlekedésfejlesztést.",
],
"correct": 0,
},
{
"question": "Milyen hangulat uralkodik a bérház belső udvarán?",
"options": [
"A külvilágtól védett, a múlt és jelen összefonódását tükröző mély csend.",
"Rendkívül hangos és zavaró utcai lárma.",
"Elhagyatott, teljesen romos és veszélyes pusztulás.",
],
"correct": 0,
},
],
},
"lessons": [
# Lesson 1
{
"num": 1,
"title": "Relative Pronouns with Postpositions (amely mellett, amely által)",
"grammar_label": "Governed relative pronouns with postpositions (amely mellett, amely által, akik között, ami felé)",
"goals": [
"I can connect clauses using relative pronouns governed by postpositions (amely mellett, amely által)",
"I can select the correct relative pronoun form (amely, ami, aki) based on humanness and antecedents",
"I can form elegant spatial and relational descriptions in architectural discourse",
],
"grammar_doc": {
"slug": "relative-pronouns-postpositions",
"title": "Relative Pronouns Governed by Postpositions",
"text1_title": "Spatial and Instrumental Postpositions with amely",
"text1": "In formal Hungarian, relative pronouns (amely, ami, aki) readily combine with postpositions to express spatial, causal, and instrumental relationships. In non-human reference, amely is the standard literary relative pronoun: 'A bérház, amely mellett elsétáltunk...' ('The apartment building next to which we walked...'), 'A felújítási program, amely által megmentették a homlokzatot...' ('The renovation program through which they saved the facade...').",
"text2_title": "Selecting Between aki, amely, and ami with Postpositions",
"text2": "Aki is reserved for human antecedents and takes postpositions directly: 'A szomszédok, akik között felnőtt...' ('The neighbours among whom he grew up...'). Amely refers to specific antecedent nouns (singular or plural), while ami refers to whole propositions or indefinite pronouns (minden, semmi): 'A körfolyosót helyreállították, ami után a lakók visszaköltözhettek' ('The balcony corridor was restored, after which the residents could move back').",
"table_title": "Relative Pronouns with Postpositions",
"table_rows": [
["amely mellett (spatial)", "A régi bérház, amely mellett egy új park épült."],
["amely által (instrumental)", "A pályázat, amely által megújult a homlokzat."],
["akik között (human plural)", "A lakók, akik között mély barátság szövődött."],
["ami felé (clausal reference)", "A városvezetés zöldít, ami felé a polgárok is nyitottak."],
],
"examples": [
{
"spanish": "A régi bérház, amely mellett naponta eljárok, a tizenkilencedik század végén épült.",
"english": "The old apartment building next to which I walk daily was built at the end of the nineteenth century.",
},
{
"spanish": "Elfogadták az új építészeti koncepciót, amely által megőrizhető a történelmi városkép.",
"english": "They accepted the new architectural concept through which the historic cityscape can be preserved.",
},
{
"spanish": "Azok a szomszédok, akik között gyermekkoromat töltöttem, mindig összetartottak.",
"english": "Those neighbours among whom I spent my childhood always stuck together.",
},
{
"spanish": "A belső udvar felé nyílik a körfolyosó, amely felől kellemes hűvös árad be a lakásokba.",
"english": "The balcony corridor opens toward the inner courtyard, from which pleasant cool air flows into the apartments.",
},
],
"tip": "In literary and formal Hungarian, prefer 'amely' over 'ami' when referring back to a specific concrete or abstract noun (e.g. 'az épület, amely mellett', NOT 'az épület, ami mellett').",
},
"words": [
{"lemma": "amely mellett", "translation": "next to which / beside which", "pos": "expression"},
{"lemma": "amely által", "translation": "by means of which / through which", "pos": "expression"},
{"lemma": "bérház", "translation": "tenement / apartment building", "pos": "noun"},
{"lemma": "körfolyosó", "translation": "open courtyard corridor / gangway", "pos": "noun"},
{"lemma": "homlokzat", "translation": "facade / building front", "pos": "noun"},
],
"exercises": {
"intro": [
mc(
"vocabulary",
"introduce",
"What is a traditional 'bérház' in Budapest urban architecture?",
[
"a multi-story historic tenement or apartment building often built around a central courtyard with open corridors",
"a modern single-family detached villa in the suburban hills",
"a commercial warehouse exclusively storing industrial freight",
],
0,
["b2-23-vocab"],
),
mc(
"vocabulary",
"introduce",
"Which postpositional expression means 'through which / by means of which' in formal Hungarian?",
["amely által", "amely nélkül", "amely helyett"],
0,
["b2-23-vocab"],
),
],
"controlled": [
match(
"vocabulary",
"controlled",
[
["amely mellett", "next to which"],
["amely által", "by means of which"],
["bérház", "tenement / apartment building"],
["körfolyosó", "open courtyard corridor"],
["homlokzat", "facade"],
],
["b2-23-vocab"],
),
mc(
"grammar",
"controlled",
"Select the relative phrase for a non-human antecedent meaning 'next to which':",
["amely mellett", "aki mellett", "amihez képest"],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"controlled",
"Choose the correct relative pronoun for a human plural antecedent: 'A lakók, ____ békés kapcsolat alakult ki':",
["akik között", "amelyek között", "amik között"],
0,
["b2-relative-postpositions"],
),
fb(
"grammar",
"controlled",
"Kidolgoztak egy tervet, ____ megvalósítható a gangok biztonságos felújítása. (by means of which)",
"amely által",
"They elaborated a plan through which the safe renovation of the gangways can be implemented.",
["b2-relative-postpositions"],
),
],
"practice": [
fb(
"grammar",
"practice",
"A Duna-parti fasor, ____ a villamos halad, a város egyik legszebb része. (beside which)",
"amely mellett",
"The Danube tree-lined promenade next to which the tram travels is one of the most beautiful parts of the city.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"practice",
["A", "bérház,", "amely", "mellett", "elsétáltunk,", "felújítás", "alatt", "áll."],
["A", "bérház,", "amely", "mellett", "elsétáltunk,", "felújítás", "alatt", "áll."],
"The apartment building next to which we walked is under renovation.",
["b2-relative-postpositions"],
),
fb(
"vocabulary",
"practice",
"A belső udvarra néző ____ a lakók kedvenc találkozóhelye volt nyaranta. (open corridor)",
"körfolyosó",
"The open corridor overlooking the inner courtyard was the residents' favorite meeting place in summers.",
["b2-23-vocab"],
),
sb(
"vocabulary",
"practice",
["A", "felújított", "homlokzat", "díszíti", "a", "történelmi", "utcát."],
["A", "felújított", "homlokzat", "díszíti", "a", "történelmi", "utcát."],
"The renovated facade decorates the historic street.",
["b2-23-vocab"],
),
],
"dialogue": [
dc(
"dialogue",
[
{"speaker": "Építész", "text": "Hogyan értékeled a belső udvar revitalizációját?"},
{"speaker": "Várostervező", "text": "____"},
],
[
"Ez egy kiváló koncepció, amely által a lakóközösség egy valódi közösségi kerthez jutott.",
"Nem tetszik a dolog, mert a bérházakban nincsenek ablakok.",
"Amely nélkül nem lehet téglát vásárolni a boltban.",
],
0,
["b2-relative-postpositions"],
),
dc(
"dialogue",
[
{"speaker": "Idegenvezető", "text": "Miért olyan különleges ez a budai bérház?"},
{"speaker": "Történész", "text": "____"},
],
[
"Ez az az épület, amely mellett száz éven át generációk nőttek fel a körfolyosók védelmében.",
"Mert nincs ajtaja és senki sem mehet be a kapun.",
"Akik között nincsenek falak a szobákban.",
],
0,
["b2-relative-postpositions"],
),
],
"writing": [
sw(
"production",
[
{
"prompt": "Write a sentence using 'amely mellett' describing an iconic architectural structure.",
"answer": "A régi Duna-parti palota, amely mellett naponta elsétálok, műemléki védelem alatt áll.",
}
],
["b2-relative-postpositions"],
),
sw(
"production",
[
{
"prompt": "Write a sentence using 'amely által' explaining how an urban renewal step improves living conditions.",
"answer": "Olyan felújítási programot indítottak, amely által a lakók modern és energiatakarékos otthonokhoz jutnak.",
}
],
["b2-relative-postpositions"],
),
],
"check": [
fb(
"grammar",
"check",
"A Clark Ádám tér az a pont, ____ a budai hegyek alagútja vezet. (toward which)",
"amely felé",
"Clark Ádám Square is the point toward which the Buda hill tunnel leads.",
["b2-relative-postpositions"],
),
mc(
"vocabulary",
"check",
"Which architectural term denotes the open corridor running around an inner courtyard?",
["körfolyosó", "homlokzat", "alagsor"],
0,
["b2-23-vocab"],
),
],
},
},
# Lesson 2
{
"num": 2,
"title": "Possessive Relative Chains (amelynek a tetején)",
"grammar_label": "Left-branching possessive relative clauses (amelynek udvarán, akiknek segítségével, amelynek révén)",
"goals": [
"I can construct complex possessive relative phrases (amelynek a tetején, amelynek udvarán)",
"I can use plural possessive relative pronouns with human antecedents (akiknek a részvételével)",
"I can maintain structural clarity across nested possessive relative clauses",
],
"grammar_doc": {
"slug": "possessive-relative-chains",
"title": "Possessive Relative Chains: amelynek a tetején",
"text1_title": "Left-Branching Possessive Relatives",
"text1": "Hungarian relative clauses frequently embed possessive constructions governed by postpositions or inflected locative nouns. In these structures, the relative pronoun takes the dative/genitive suffix -nek (amelynek, akiknek), followed by a possessed noun carrying its possessive suffix: 'A bérház, amelynek a tetején teraszkertet alakítottak ki...' ('The apartment building on the roof of which a terrace garden was created...').",
"text2_title": "Abstract Relational Idioms: amelynek révén, segítségével",
"text2": "Beyond physical locations, possessive relative chains commonly express instrumental means and causation in formal civic prose: 'amelynek révén' ('thanks to which / through the agency of which'), 'amelynek segítségével' ('with the help of which'), 'akiknek a közreműködésével' ('with whose participation'). This recursive left-branching is a hallmark of sophisticated B2-C1 Hungarian syntax.",
"table_title": "Possessive Relative Chains",
"table_rows": [
["amelynek udvarán", "A bérház, amelynek udvarán szökőkút áll."],
["amelynek révén", "A beruházás, amelynek révén felújították az utcát."],
["akiknek segítségével", "A szomszédok, akiknek segítségével rendbe hoztuk a kertet."],
["amelynek következtében", "A forgalomkorlátozás, amelynek következtében tisztább lett a levegő."],
],
"examples": [
{
"spanish": "Megcsodáltuk a palotát, amelynek tetején zöld rézkupola magasodik.",
"english": "We admired the palace, on top of which rises a green copper dome.",
},
{
"spanish": "Egy olyan társasházban lakom, amelynek udvarán százéves gesztenyefa lombosodik.",
"english": "I live in a condominium in the courtyard of which a hundred-year-old chestnut tree blossoms.",
},
{
"spanish": "Pályázatot nyert a lakóközösség, amelynek révén korszerűsítik az egész fűtésrendszert.",
"english": "The residential community won a grant, thanks to which they will modernize the entire heating system.",
},
{
"spanish": "Köszönetet mondtak a restaurátoroknak, akiknek szakértelme nélkül elveszett volna a freskó.",
"english": "They expressed thanks to the restorers, without whose expertise the fresco would have been lost.",
},
],
"tip": "Remember the possessive suffix on the noun: in 'amelynek udvarán', 'udvar' must carry the 3rd person possessive -a/-e ('udvara') plus the superessive case -n ('udvarán').",
},
"words": [
{"lemma": "amelynek révén", "translation": "thanks to which / by means of which", "pos": "expression"},
{"lemma": "lakóközösség", "translation": "residential community / co-op members", "pos": "noun"},
{"lemma": "udvar", "translation": "courtyard", "pos": "noun"},
{"lemma": "műemlékvédelem", "translation": "historic preservation / monument protection", "pos": "noun"},
{"lemma": "térrendezés", "translation": "spatial planning / landscaping", "pos": "noun"},
],
"exercises": {
"intro": [
mc(
"vocabulary",
"introduce",
"What does 'lakóközösség' refer to in condominium administration?",
[
"the collective body of residents and property owners within an apartment building",
"a municipal police department responsible for public order",
"a construction company building suburban shopping centers",
],
0,
["b2-23-vocab"],
),
mc(
"vocabulary",
"introduce",
"Which idiom means 'thanks to which / by means of which'?",
["amelynek révén", "amely helyett", "amely nélkül"],
0,
["b2-23-vocab"],
),
],
"controlled": [
match(
"vocabulary",
"controlled",
[
["amelynek révén", "thanks to which"],
["lakóközösség", "residential community"],
["udvar", "courtyard"],
["műemlékvédelem", "monument protection"],
["térrendezés", "spatial planning"],
],
["b2-23-vocab"],
),
mc(
"grammar",
"controlled",
"Select the correct possessive relative phrase: 'Ez az az épület, ____ szoborpark található':",
["amelynek udvarán", "amely udvarán", "ami udvarán"],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"controlled",
"Which form refers to plural human possessors in a relative clause?",
["akiknek a segítségével", "amelyeknek a segítségével", "amiknek a segítségével"],
0,
["b2-relative-postpositions"],
),
fb(
"grammar",
"controlled",
"Meglátogattuk a várat, ____ kilátó nyílik az egész budai völgyre. (on top of which)",
"amelynek tetején",
"We visited the castle, on top of which a lookout terrace opens onto the whole Buda valley.",
["b2-relative-postpositions"],
),
],
"practice": [
fb(
"grammar",
"practice",
"Olyan pályázatot nyertünk, ____ felújíthatjuk a ház belső udvarát. (thanks to which)",
"amelynek révén",
"We won a grant, thanks to which we can renovate the building's inner courtyard.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"practice",
["A", "bérház,", "amelynek", "udvarán", "szökőkút", "áll,", "műemléki", "védettséget", "élvez."],
["A", "bérház,", "amelynek", "udvarán", "szökőkút", "áll,", "műemléki", "védettséget", "élvez."],
"The apartment building in whose courtyard a fountain stands enjoys monument protection.",
["b2-relative-postpositions"],
),
fb(
"vocabulary",
"practice",
"A szigorú ____ megakadályozta, hogy az épület eredeti stílusát átalakítsák. (historic preservation)",
"műemlékvédelem",
"Strict historic preservation prevented the building's original style from being transformed.",
["b2-23-vocab"],
),
sb(
"vocabulary",
"practice",
["A", "korszerű", "térrendezés", "új", "zöldterületeket", "hoz", "létre", "a", "lakóknak."],
["A", "korszerű", "térrendezés", "új", "zöldterületeket", "hoz", "létre", "a", "lakóknak."],
"Modern spatial planning creates new green areas for residents.",
["b2-23-vocab"],
),
],
"dialogue": [
dc(
"dialogue",
[
{"speaker": "Közös képviselő", "text": "Hogyan sikerült finanszírozni a gangok megerősítését?"},
{"speaker": "Számvizsgáló", "text": "____"},
],
[
"Olyan fővárosi támogatást kaptunk, amelynek segítségével a lakóközösség önerőből is el tudta végezni a munkát.",
"Nem tudom, mert nem lakik senki a házban.",
"Akiknek a tetején nem volt fűtés, azok elmentek.",
],
0,
["b2-relative-postpositions"],
),
dc(
"dialogue",
[
{"speaker": "Restaurátor", "text": "Miért fontos a belső udvar eredeti kövezésének megóvása?"},
{"speaker": "Művészettörténész", "text": "____"},
],
[
"Mert ez az a tér, amelynek révén átélhetjük a tizenkilencedik századi polgári életforma hangulatát.",
"Mivel a kövek túl nehezek a szállításhoz.",
"Műemlékvédelem helyett betonozzunk le mindent.",
],
0,
["b2-relative-postpositions"],
),
],
"writing": [
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelynek udvarán' describing a community courtyard.",
"answer": "Olyan bérházban élünk, amelynek udvarán régi szökőkút és zöld növények teremtenek békét.",
}
],
["b2-relative-postpositions"],
),
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelynek révén' explaining civic development.",
"answer": "A kerület támogatást kapott, amelynek révén akadálymentesítették az összes középületet.",
}
],
["b2-relative-postpositions"],
),
],
"check": [
fb(
"grammar",
"check",
"Elkészült az új közlekedési rend, ____ csökkent a belvárosi utcák zajterhelése. (as a consequence of which)",
"amelynek következtében",
"The new traffic plan was completed, as a consequence of which noise pollution in downtown streets decreased.",
["b2-relative-postpositions"],
),
mc(
"vocabulary",
"check",
"Which term refers to state regulations safeguarding historical buildings?",
["műemlékvédelem", "térrendezés", "lakóközösség"],
0,
["b2-23-vocab"],
),
],
},
},
# Lesson 3
{
"num": 3,
"title": "Historic Preservation vs. Modern Development",
"grammar_label": "Spatial relations in city architecture and heritage discourse (városkép, műemlék, átépítés)",
"goals": [
"I can discuss the tension between historic preservation and contemporary urban development",
"I can describe architectural styles and structural restorations with relative postpositions",
"I can evaluate urban zoning regulations and heritage designations",
],
"grammar_doc": {
"slug": "historic-preservation-modernization",
"title": "Architectural Tension: Historic Preservation vs. Modernization",
"text1_title": "Cityscapes and Heritage Protection",
"text1": "The architectural fabric of Central European cities balances the preservation of historical character ('városkép megőrzése') with contemporary demands. Protected heritage monuments ('műemlékek') require specialized restoration techniques. When discussing renovations ('felújítás') and reconstructions ('átépítés'), relative clauses describe architectural elements in relation to protected cityscapes.",
"text2_title": "Zoning and Structural Intervention",
"text2": "Municipal zoning classifications ('övezeti besorolás') regulate height limits, facade materials, and density. Professional debates evaluate structural interventions: 'Egy olyan védett épületről van szó, amelynek homlokzata eredeti formájában maradt meg, de amelyben korszerű irodákat alakítottak ki'.",
"table_title": "Urban Architecture Vocabulary & Syntactic Patterns",
"table_rows": [
["városkép", "A történelmi városkép védelme szigorú szabályokat kíván."],
["műemlék", "A tizenkilencedik századi palota védett műemlék."],
["átépítés", "Az átépítés során ügyeltek a régi boltívekre."],
["övezeti besorolás", "Az új övezeti besorolás korlátozza az épületmagasságot."],
],
"examples": [
{
"spanish": "A városkép védelme érdekében szigorúan korlátozzák a magasházak építését a Duna mentén.",
"english": "In the interest of protecting the cityscape, the construction of high-rises along the Danube is strictly restricted.",
},
{
"spanish": "Az az épület, amelyben a múzeum működik, kiemelt jelentőségű műemlék.",
"english": "That building in which the museum operates is a monument of prominent significance.",
},
{
"spanish": "A műemlékvédelmi hivatal csak olyan átépítést engedélyez, amely tiszteletben tartja a homlokzat arányait.",
"english": "The monument protection office only authorizes remodeling that respects the proportions of the facade.",
},
{
"spanish": "A kerület új övezeti besorolása megtiltja a nehézgépjárművek behajtását a lakóövezetbe.",
"english": "The district's new zoning classification prohibits heavy vehicles from entering the residential zone.",
},
],
"tip": "When describing architectural transformations, use contrastive relative clauses ('amely egykor gyár volt, ma viszont...') to highlight historical transitions.",
},
"words": [
{"lemma": "városkép", "translation": "cityscape / townscape", "pos": "noun"},
{"lemma": "felújítás", "translation": "renovation / refurbishment", "pos": "noun"},
{"lemma": "átépítés", "translation": "reconstruction / remodeling", "pos": "noun"},
{"lemma": "műemlék", "translation": "historic monument / listed building", "pos": "noun"},
{"lemma": "övezeti besorolás", "translation": "zoning classification", "pos": "noun"},
],
"exercises": {
"intro": [
mc(
"vocabulary",
"introduce",
"What is a 'műemlék' under Hungarian cultural heritage legislation?",
[
"a legally listed and protected historic building or structure of architectural significance",
"a temporary scaffolding erected around modern construction sites",
"a newly constructed prefabricated apartment block",
],
0,
["b2-23-vocab"],
),
mc(
"vocabulary",
"introduce",
"Which noun denotes the overall visual and aesthetic appearance of an urban landscape?",
["városkép", "átépítés", "övezeti besorolás"],
0,
["b2-23-vocab"],
),
],
"controlled": [
match(
"vocabulary",
"controlled",
[
["városkép", "cityscape"],
["felújítás", "renovation"],
["átépítés", "remodeling"],
["műemlék", "historic monument"],
["övezeti besorolás", "zoning classification"],
],
["b2-23-vocab"],
),
mc(
"grammar",
"controlled",
"Select the relative phrase with postposition meaning 'compared to which':",
["amelyhez képest", "amely által", "amely nélkül"],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"controlled",
"Which connector completes: 'Olyan műemléki felújítást végeztek, ____ a belső terek modern funkciót kaptak'?",
["amely által", "akik által", "amihez képest"],
0,
["b2-relative-postpositions"],
),
fb(
"grammar",
"controlled",
"Léteznek olyan történelmi terek, ____ elképzelhetetlen a magyar főváros identitása. (without which)",
"amelyek nélkül",
"There exist historical squares without which the Hungarian capital's identity is unimaginable.",
["b2-relative-postpositions"],
),
],
"practice": [
fb(
"grammar",
"practice",
"A rakpart felújítása volt az a beruházás, ____ közelebb került a Duna a gyalogosokhoz. (by means of which)",
"amely által",
"The renovation of the embankment was the investment through which the Danube came closer to pedestrians.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"practice",
["A", "védett", "műemlék,", "amelynek", "homlokzatát", "helyreállították,", "a", "város", "büszkesége."],
["A", "védett", "műemlék,", "amelynek", "homlokzatát", "helyreállították,", "a", "város", "büszkesége."],
"The protected monument whose facade was restored is the pride of the city.",
["b2-relative-postpositions"],
),
fb(
"vocabulary",
"practice",
"A színház teljes körű ____ során megnövelték a nézőtér befogadóképességét. (remodeling [possessive])",
"átépítése",
"In the course of the theater's comprehensive remodeling, they increased the auditorium's seating capacity.",
["b2-23-vocab"],
),
sb(
"vocabulary",
"practice",
["Az", "új", "övezeti", "besorolás", "szigorúan", "szabályozza", "a", "belvárosi", "építkezéseket."],
["Az", "új", "övezeti", "besorolás", "szigorúan", "szabályozza", "a", "belvárosi", "építkezéseket."],
"The new zoning classification strictly regulates downtown construction projects.",
["b2-23-vocab"],
),
],
"dialogue": [
dc(
"dialogue",
[
{"speaker": "Főépítész", "text": "Hogyan egyeztethető össze a modern irodaház a történelmi környezettel?"},
{"speaker": "Műemléki szakértő", "text": "____"},
],
[
"Csak olyan tervezési kompromisszum fogadható el, amely mentén a védett városkép harmóniája nem sérül.",
"Nem kell foglalkozni a régi falakkal, mindent el kell bontani.",
"Akik között nincsenek ablakok, azok nem látják a várost.",
],
0,
["b2-relative-postpositions"],
),
dc(
"dialogue",
[
{"speaker": "Ingatlanfejlesztő", "text": "Miért olyan szigorú az új övezeti besorolás ebben a kerületben?"},
{"speaker": "Polgármester", "text": "____"},
],
[
"Mert ez az a történelmi negyed, amelyhez képest a modern lakóparkok idegen testnek hatnának.",
"Mert senki sem szeret építkezni a nyáron.",
"Amely mellett nem folyik a Duna, ott nincs szabály.",
],
0,
["b2-relative-postpositions"],
),
],
"writing": [
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelynek felújítása' arguing for architectural preservation.",
"answer": "Meg kell mentenünk a régi vámházat, amelynek felújítása révén új kulturális központ jöhetne létre.",
}
],
["b2-relative-postpositions"],
),
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelyek nélkül' describing irreplaceable historic landmarks.",
"answer": "Vannak olyan épületek, amelyek nélkül a budai várnegyed elveszítené történelmi varázsát.",
}
],
["b2-relative-postpositions"],
),
],
"check": [
fb(
"grammar",
"check",
"A Duna az az elem, ____ a két városrész, Buda és Pest évszázadok óta igazodik. (to which / toward which)",
"amelyhez",
"The Danube is the element to which the two parts of the city, Buda and Pest, have aligned for centuries.",
["b2-relative-postpositions"],
),
mc(
"vocabulary",
"check",
"Which term defines the legal classification determining permissible land use and building heights?",
["övezeti besorolás", "városkép", "felújítás"],
0,
["b2-23-vocab"],
),
],
},
},
# Lesson 4
{
"num": 4,
"title": "Life in Shared Urban Spaces",
"grammar_label": "Neighbourhood dynamics, coexistence, and human relative postpositions (akikkel, akik között, akikért)",
"goals": [
"I can express social interactions and civic coexistence in dense urban environments",
"I can use relative clauses with inflected postpositions referring to neighbours and cohabitants",
"I can discuss community spaces, noise ordinances, and shared courtyard traditions",
],
"grammar_doc": {
"slug": "shared-urban-spaces-coexistence",
"title": "Urban Coexistence & Shared Spaces: akikkel együtt élünk",
"text1_title": "The Grammar of Courtyard Coexistence",
"text1": "Living in traditional multi-story residential blocks (the classic Budapest bérház) creates a dense web of human interactions. Shared open corridors (körfolyosó) and courtyards require explicit rules of coexistence ('együttélési szabályok'). Clauses describing neighbours take governed relative forms: 'A lakók, akikkel nap mint nap találkozunk a lépcsőházban...' ('The residents with whom we meet daily in the stairwell...').",
"text2_title": "Regulating the Common Sphere: házirend and zajártalom",
"text2": "Every condominium operates under house rules ('házirend') addressing shared courtyard spaces ('közösségi tér') and noise disturbances ('zajártalom'). Expressing community grievances and agreements calls for precise interpersonal and spatial relative structures: 'Olyan házirendre van szükség, amelynek betartásával elkerülhetők a lakók közötti feszültségek'.",
"table_title": "Neighbourhood & Coexistence Terms",
"table_rows": [
["együttélés", "A békés együttélés alapja a kölcsönös figyelem."],
["szomszédság", "A szomszédság összefogott a belső kert csinosítására."],
["házirend", "A társasház házirendje tiltja az éjszakai zajongást."],
["zajártalom", "A belvárosi forgalom komoly zajártalmat okoz a lakóknak."],
],
"examples": [
{
"spanish": "A szomszédok, akikkel a körfolyosón megosztjuk a mindennapokat, sokat segítenek egymásnak.",
"english": "The neighbours with whom we share everyday life on the open corridor help each other a lot.",
},
{
"spanish": "A békés együttélés érdekében a lakóközösség szigorú házirendet léptetett életbe.",
"english": "In the interest of peaceful coexistence, the residential community put strict house rules into effect.",
},
{
"spanish": "A belső udvar közösségi térré alakult, ahol a gyerekek biztonságban játszhatnak.",
"english": "The inner courtyard was transformed into a community space where children can play safely.",
},
{
"spanish": "A belvárosi szórakozóhelyek által okozott zajártalom ellen közösen léptek fel a lakók.",
"english": "Residents took joint action against the noise pollution caused by downtown entertainment venues.",
},
],
"tip": "With plural human antecedents, ensure relative pronoun case agreement: 'akikkel együtt lakunk' (comitative), 'akikre számíthatunk' (sublative), 'akiknek a nyugalma' (dative possessor).",
},
"words": [
{"lemma": "együttélés", "translation": "coexistence / living together", "pos": "noun"},
{"lemma": "szomszédság", "translation": "neighbourhood / neighbours", "pos": "noun"},
{"lemma": "közösségi tér", "translation": "community space", "pos": "noun"},
{"lemma": "házirend", "translation": "house rules / condominium regulations", "pos": "noun"},
{"lemma": "zajártalom", "translation": "noise pollution / noise nuisance", "pos": "noun"},
],
"exercises": {
"intro": [
mc(
"vocabulary",
"introduce",
"What is the function of a 'házirend' in an apartment block?",
[
"a set of internal regulations establishing mandatory rules of conduct for residents",
"a catalog listing real estate prices across municipal districts",
"a daily chore checklist assigned to professional cleaners",
],
0,
["b2-23-vocab"],
),
mc(
"vocabulary",
"introduce",
"Which noun denotes harmful or disruptive noise affecting urban residents?",
["zajártalom", "együttélés", "közösségi tér"],
0,
["b2-23-vocab"],
),
],
"controlled": [
match(
"vocabulary",
"controlled",
[
["együttélés", "coexistence"],
["szomszédság", "neighbourhood"],
["közösségi tér", "community space"],
["házirend", "house rules"],
["zajártalom", "noise pollution"],
],
["b2-23-vocab"],
),
mc(
"grammar",
"controlled",
"Choose the correct relative pronoun form: 'A szomszédok, ____ együtt élünk, tiszteletben tartják a csendet':",
["akikkel", "amelyekkel", "amikkel"],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"controlled",
"Select the relative phrase for plural human antecedents meaning 'among whom':",
["akik között", "amelyek között", "akikért"],
0,
["b2-relative-postpositions"],
),
fb(
"grammar",
"controlled",
"A lakók, ____ felelősséget érzünk a társasházban, megbíznak a közös képviselőben. (for whom)",
"akikért",
"The residents for whom we feel responsibility in the condominium trust the representative.",
["b2-relative-postpositions"],
),
],
"practice": [
fb(
"grammar",
"practice",
"Olyan barátságos lakók költöztek a házba, ____ bármikor számíthatunk segítségre. (on whom)",
"akikre",
"Such friendly residents moved into the building, on whom we can count for help at any time.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"practice",
["A", "szomszédok,", "akikkel", "naponta", "találkozunk,", "segítőkészek", "és", "figyelmesek."],
["A", "szomszédok,", "akikkel", "naponta", "találkozunk,", "segítőkészek", "és", "figyelmesek."],
"The neighbours with whom we meet daily are helpful and attentive.",
["b2-relative-postpositions"],
),
fb(
"vocabulary",
"practice",
"Az éjszakai szórakozóhelyek miatt a lakók folyamatos ____ panaszkodnak. (noise pollution [sublative])",
"zajártalomra",
"Due to night entertainment venues, residents continuously complain about noise pollution.",
["b2-23-vocab"],
),
sb(
"vocabulary",
"practice",
["A", "lakóközösség", "új", "házirendet", "fogadott", "el", "a", "nyugalom", "érdekében."],
["A", "lakóközösség", "új", "házirendet", "fogadott", "el", "a", "nyugalom", "érdekében."],
"The residential community adopted new house rules in the interest of peace.",
["b2-23-vocab"],
),
],
"dialogue": [
dc(
"dialogue",
[
{"speaker": "Új lakó", "text": "Hogyan működik a közös udvar használata ebben a bérházban?"},
{"speaker": "Régi lakó", "text": "____"},
],
[
"A házirend szabályozza, hogy mikor játszhatnak a gyerekek, ami által elkerülhető a felesleges zajártalom.",
"Senki sem mehet le a lépcsőn, mert tilos a járkálás.",
"Akikkel nincsenek ablakok, azok nem beszélnek egymással.",
],
0,
["b2-relative-postpositions"],
),
dc(
"dialogue",
[
{"speaker": "Közös képviselő", "text": "Sikerült megállapodni a szomszédokkal a felújítás időpontjáról?"},
{"speaker": "Gondnok", "text": "____"},
],
[
"Igen, azokkal a családokkal, akikkel közvetlenül egyeztettünk, teljes az egyetértés.",
"Nem, mert a bérházakban tilos a felújítás.",
"Amely mellett nem volt senki otthon tegnap.",
],
0,
["b2-relative-postpositions"],
),
],
"writing": [
sw(
"production",
[
{
"prompt": "Write a sentence using 'akikkel együtt élünk' describing community relationships.",
"answer": "A szomszédok, akikkel együtt élünk a lépcsőházban, mindig figyelnek egymás nyugalmára.",
}
],
["b2-relative-postpositions"],
),
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelynek betartásával' describing adherence to house rules.",
"answer": "Közös házirendet alkottunk, amelynek betartásával megelőzhetők a felesleges viták.",
}
],
["b2-relative-postpositions"],
),
],
"check": [
fb(
"grammar",
"check",
"A lépcsőház lakói, ____ a békéje mindannyiunk felelőssége, támogatják a házirend szigorítását. (whose)",
"akiknek",
"The residents of the stairwell, whose peace is the responsibility of us all, support tightening the house rules.",
["b2-relative-postpositions"],
),
mc(
"vocabulary",
"check",
"Which concept denotes the state of people living peacefully together in shared space?",
["együttélés", "zajártalom", "övezeti besorolás"],
0,
["b2-23-vocab"],
),
],
},
},
# Lesson 5
{
"num": 5,
"title": "Proposing an Urban Renewal Plan",
"grammar_label": "Presenting urban renewal strategies with complex relative clauses and spatial postpositions",
"goals": [
"I can present an urban regeneration proposal using layered relative clauses",
"I can defend infrastructure decisions balancing public transit, green zones, and housing",
"I can synthesize architectural critique and civic stakeholder perspectives",
],
"grammar_doc": {
"slug": "urban-renewal-plan-proposal",
"title": "Proposing Urban Regeneration: Complex Spatial Synthesis",
"text1_title": "Structuring an Urban Renewal Strategy",
"text1": "Presenting an urban rehabilitation plan ('városrehabilitációs terv') requires synthesizing spatial postpositions, relative clauses, and policy vocabulary. Urban planners must justify expanding pedestrian zones ('gyalogosövezet') and green areas ('zöldfelület') while maintaining livability ('élhetőség') and viable public transport development ('közlekedésfejlesztés').",
"text2_title": "Layered Relative Justifications",
"text2": "High-register proposals articulate multi-layered causal and spatial justifications: 'Olyan átfogó koncepciót javaslunk, amelynek központjában a közösségi terek revitalizációja áll, és amely által a belvárosi lakókörnyezet jelentősen javulni fog'.",
"table_title": "Urban Planning Key Concepts",
"table_rows": [
["városrehabilitáció", "A kerület sikeres városrehabilitációt hajtott végre."],
["zöldfelület", "A zöldfelületek növelése csökkenti a hőszigethatást."],
["gyalogosövezet", "A történelmi magban új gyalogosövezetet hoztak létre."],
["élhetőség", "A város élhetősége a tiszta tereken és parkokon múlik."],
],
"examples": [
{
"spanish": "Olyan átfogó városrehabilitációt javaslunk, amelynek keretében zöldövezetté alakítják a forgalmas sugárutat.",
"english": "We propose a comprehensive urban rehabilitation within the framework of which the busy boulevard will be turned into a green zone.",
},
{
"spanish": "A gyalogosövezet kibővítése az a lépés, amely által visszaadjuk a belvárost a járókelőknek.",
"english": "Expanding the pedestrian zone is the step through which we give downtown back to pedestrians.",
},
{
"spanish": "A város élhetősége nagyban függ azoktól a zöldfelületektől, amelyek mentén pihenőparkokat létesítenek.",
"english": "The livability of the city depends greatly on those green areas along which they establish recreation parks.",
},
{
"spanish": "A fenntartható közlekedésfejlesztés révén csökken a légszennyezettség és gyorsul a forgalom.",
"english": "Through sustainable transportation development, air pollution decreases and traffic accelerates.",
},
],
"tip": "When proposing civic plans, chain possessive relative clauses smoothly to avoid sentence clutter: 'egy olyan projekt, amelynek megvalósítása révén a lakók...'.",
},
"words": [
{"lemma": "városrehabilitáció", "translation": "urban rehabilitation / urban renewal", "pos": "noun"},
{"lemma": "zöldfelület", "translation": "green area / green space", "pos": "noun"},
{"lemma": "gyalogosövezet", "translation": "pedestrian zone", "pos": "noun"},
{"lemma": "élhetőség", "translation": "livability", "pos": "noun"},
{"lemma": "közlekedésfejlesztés", "translation": "transportation development", "pos": "noun"},
],
"exercises": {
"intro": [
mc(
"vocabulary",
"introduce",
"What does 'városrehabilitáció' signify in municipal planning?",
[
"the comprehensive renewal, renovation, and social revitalisation of run-down urban areas",
"the complete demolition of historic districts to construct motorways",
"a routine repaving of suburban side streets",
],
0,
["b2-23-vocab"],
),
mc(
"vocabulary",
"introduce",
"Which term denotes the overall quality of life and comfort in an urban environment?",
["élhetőség", "közlekedésfejlesztés", "övezeti besorolás"],
0,
["b2-23-vocab"],
),
],
"controlled": [
match(
"vocabulary",
"controlled",
[
["városrehabilitáció", "urban rehabilitation"],
["zöldfelület", "green area"],
["gyalogosövezet", "pedestrian zone"],
["élhetőség", "livability"],
["közlekedésfejlesztés", "transportation development"],
],
["b2-23-vocab"],
),
mc(
"grammar",
"controlled",
"Select the relative clause expressing institutional framework: 'Olyan tervet nyújtottak be, ____ megújulnak a terek':",
["amelynek keretében", "amely helyett", "amely nélkül"],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"controlled",
"Choose the sentence formulating an urban development proposal with a relative postposition:",
[
"Olyan zöldfelületeket kell kialakítani, amelyek mentén a családok nyugodtan pihenhetnek.",
"A zöldfelület helyett betonozzunk le mindent, mert az egyszerűbb.",
"Amely által nincsenek fák a parkokban.",
],
0,
["b2-relative-postpositions"],
),
fb(
"grammar",
"controlled",
"A körút felújítása az a projekt, ____ büszkék lehetnek a kerület lakói. (on which / upon which)",
"amelyre",
"The renovation of the boulevard is the project of which district residents can be proud.",
["b2-relative-postpositions"],
),
],
"practice": [
fb(
"grammar",
"practice",
"Korszerű villamoshálózatot építenek, ____ gyorsabbá és környezetkímélőbbé válik a közlekedés. (by means of which)",
"amely révén",
"They are building a modern tram network, thanks to which transportation becomes faster and more eco-friendly.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"practice",
["A", "városrehabilitáció,", "amelynek", "során", "parkok", "épültek,", "növelte", "az", "élhetőséget."],
["A", "városrehabilitáció,", "amelynek", "során", "parkok", "épültek,", "növelte", "az", "élhetőséget."],
"The urban rehabilitation during which parks were built increased livability.",
["b2-relative-postpositions"],
),
fb(
"vocabulary",
"practice",
"A történelmi belvárosban kijelölt új ____ teljesen kitiltotta a gépjárműforgalmat. (pedestrian zone)",
"gyalogosövezet",
"The new pedestrian zone designated in the historic city center completely banned motor vehicle traffic.",
["b2-23-vocab"],
),
sb(
"vocabulary",
"practice",
["A", "zöldfelületek", "bővítése", "jelentősen", "javítja", "a", "belváros", "levegőminőségét."],
["A", "zöldfelületek", "bővítése", "jelentősen", "javítja", "a", "belváros", "levegőminőségét."],
"Expanding green areas significantly improves downtown air quality.",
["b2-23-vocab"],
),
],
"dialogue": [
dc(
"dialogue",
[
{"speaker": "Várostervező", "text": "Hogyan fogadják a polgárok a gépkocsiforgalom korlátozását?"},
{"speaker": "Polgármester", "text": "____"},
],
[
"Az új gyalogosövezet, amely által csendesebbé vált a belváros, osztatlan sikert aratott a lakók körében.",
"Nem támogatják, mert mindenki a járdán akar parkolni.",
"Amely nélkül nem lehet repülővel közlekedni az utcákon.",
],
0,
["b2-relative-postpositions"],
),
dc(
"dialogue",
[
{"speaker": "Környezetvédő", "text": "Miért van szükség a zöldfelületek radikális növelésére?"},
{"speaker": "Ökológus", "text": "____"},
],
[
"Olyan mikroklímát kell teremtenünk, amelynek segítségével elviselhetővé válnak a nyári kánikulák a bérházakban.",
"Mert nincs más színű festék a városban.",
"Akikkel nincsenek parkok, azok nem mennek ki az utcára.",
],
0,
["b2-relative-postpositions"],
),
],
"writing": [
sw(
"production",
[
{
"prompt": "Write a sentence using 'amelynek központjában' formulating an urban renewal objective.",
"answer": "Olyan városfejlesztési programot javaslunk, amelynek központjában az élhetőség és a zöldfelületek bővítése áll.",
}
],
["b2-relative-postpositions"],
),
sw(
"production",
[
{
"prompt": "Write a sentence using 'amely által' defending public transport modernisation.",
"answer": "Korszerűsítettük a villamoshálózatot, amely által jelentősen csökkent a belvárosi károsanyag-kibocsátás.",
}
],
["b2-relative-postpositions"],
),
],
"check": [
fb(
"grammar",
"check",
"Kijelölték a kerékpárutakat, ____ a zöld parkok könnyen és biztonságosan elérhetők. (along which)",
"amelyek mentén",
"They designated the bike paths, along which green parks are easily and safely accessible.",
["b2-relative-postpositions"],
),
mc(
"vocabulary",
"check",
"Which compound noun denotes systemic investments into public transit infrastructure?",
["közlekedésfejlesztés", "zajártalom", "homlokzat"],
0,
["b2-23-vocab"],
),
],
},
},
],
"consolidation": {
"goals": [
"I can connect clauses using governed relative pronouns and postpositions (amely mellett, amely által, akik között)",
"I can construct recursive possessive relative phrases (amelynek udvarán, akiknek segítségével, amelynek révén)",
"I can articulate architectural evaluations, heritage preservation debates, and urban renewal proposals",
],
"exercises": [
# 1..3 Recognize
match(
"vocabulary",
"recognize",
[
["bérház", "tenement / apartment building"],
["műemlék", "historic monument"],
["együttélés", "coexistence"],
["városrehabilitáció", "urban renewal"],
["körfolyosó", "open corridor"],
],
["b2-23-vocab"],
),
mc(
"vocabulary",
"recognize",
"What does 'városkép' represent in architectural urban planning?",
[
"the unified visual aesthetic and historical character of an urban environment",
"a printed administrative map distributed to tourists at stations",
"a municipal tax levied on commercial property facades",
],
0,
["b2-23-vocab"],
),
mc(
"grammar",
"recognize",
"Which sentence demonstrates proper use of a spatial postposition with a non-human relative pronoun?",
[
"Megtekintettük a budai palotát, amely mellett egy lenyűgöző teraszkert húzódik.",
"Megtekintettük a budai palotát, aki mellett egy lenyűgöző teraszkert húzódik.",
"Megtekintettük a budai palotát, amely nélkül mindenki otthon maradt tegnap.",
],
0,
["b2-relative-postpositions"],
),
# 4..6 Recall
fb(
"vocabulary",
"recall",
"A történelmi belvárosban a szigorú ____ védi a régi bérházak homlokzatát. (monument protection)",
"műemlékvédelem",
"In the historic downtown, strict monument protection guards the facades of old apartment buildings.",
["b2-23-vocab"],
),
fb(
"grammar",
"recall",
"Az a lakóközösség nyert támogatást, ____ újították fel a belső körfolyosót. (thanks to which)",
"amelynek révén",
"That residential community won support, thanks to which they renovated the inner open corridor.",
["b2-relative-postpositions"],
),
fb(
"grammar",
"recall",
"A budai szomszédok, ____ évtizedek óta barátságban élünk, megbecsülik egymást. (with whom)",
"akikkel",
"The Buda neighbours with whom we have lived in friendship for decades cherish each other.",
["b2-relative-postpositions"],
),
# 7..9 In Context
mc(
"grammar",
"in-context",
"Select the sentence using 'amely által' to express civic instrumental achievement:",
[
"Megvalósult az a felújítási program, amely által a lakók modern és csendes otthonokhoz jutottak.",
"Megvalósult az a felújítási program, amely mellett nem volt pénz a festésre.",
"Megvalósult az a program, aki által mindenki elköltözött.",
],
0,
["b2-relative-postpositions"],
),
dc(
"in-context",
[
{"speaker": "Fővárosi főépítész", "text": "Mi a legnagyobb eredménye az új gyalogosövezet kialakításának?"},
{"speaker": "Kerületi polgármester", "text": "____"},
],
[
"Létrejött egy olyan élhető közösségi tér, amelynek köszönhetően a történelmi belváros visszanyerte békés polgári hangulatát.",
"Az, hogy mostantól senki sem sétálhat az utcákon sötétedés után.",
"Akikkel nincsenek padok a téren, azok nem tudnak leülni.",
],
0,
["b2-relative-postpositions"],
),
mc(
"grammar",
"in-context",
"Why is 'amely mellett' required instead of 'ami mellett' in 'A bérház, amely mellett elsétáltunk...'?",
[
"Because the antecedent is a specific, definite concrete noun ('a bérház'), requiring the literary relative pronoun 'amely'.",
"Because 'ami' cannot be followed by postpositions under any circumstances.",
"Because 'bérház' is an irregular plural noun in literary Hungarian.",
],
0,
["b2-relative-postpositions"],
),
# 10..12 Produce
sb(
"grammar",
"produce",
["A", "történelmi", "bérház,", "amelynek", "udvarán", "szökőkút", "áll,", "védett", "műemlék."],
["A", "történelmi", "bérház,", "amelynek", "udvarán", "szökőkút", "áll,", "védett", "műemlék."],
"The historic apartment building in whose courtyard a fountain stands is a protected monument.",
["b2-relative-postpositions"],
),
sb(
"grammar",
"produce",
["A", "lakók,", "akikkel", "együtt", "élünk,", "valódi", "összetartó", "közösséget", "alkotnak."],
["A", "lakók,", "akikkel", "együtt", "élünk,", "valódi", "összetartó", "közösséget", "alkotnak."],
"The residents with whom we live together form a genuinely cohesive community.",
["b2-relative-postpositions"],
),
sw(
"produce",
[
{
"prompt": "Write a three-clause urban renewal proposal combining 'amelynek keretében', 'amely által', and 'amelynek köszönhetően'.",
"answer": "Olyan átfogó városrehabilitációs tervet fogadtak el, amelynek keretében megújítják a bérházak homlokzatát; egy új gyalogosövezetet hoznak létre, amely által csökken a belvárosi forgalom; és amelynek köszönhetően az egész kerület élhetősége számottevően javulni fog.",
}
],
["b2-relative-postpositions"],
),
],
},
}


# ==============================================================================
# UNIT 24: Ecology, Infrastructure & Stewardship
# ==============================================================================

UNIT_24 = {
    "unit_num": 24,
    "title": "Ecology, Infrastructure & Stewardship",
    "grammar_summary": "Formal causal and purposive postpositional structures in Hungarian (elkerülése végett, megóvása érdekében, következtében, hatására, eredményeképpen).",
    "grammar_skill": "b2-causal-purposive-chains",
    "vocab_skill": "b2-24-vocab",
    "theme": "Ecology, infrastructure and stewardship",
    "intro_body": [
        "A Kárpát-medence természeti tájai, a Kis-Balaton védett lápvilága, valamint a Tisza és a Duna vízrendszere az ember és természet törékeny együttélésének tanúi. Az ökológiai egyensúly fenntartása, a nagyszabású infrastrukturális beruházások és a biodiverzitás megőrzése a modern magyar társadalom kiemelt felelőssége.",
        "Ebben a fejezetben elsajátíthatja a formális célhatározói névutós szerkezeteket (elkerülése végett, megóvása érdekében, céljából), valamint az ok-okozati láncokat kifejező névutókat (következtében, hatására, eredményeképpen, folytán). Fekete István klasszikus regénye, a 'Tüskevár' révén pedig megelevenedik Matula bácsi ősi természeti bölcsessége és a vadvilág tisztelete.",
    ],
    "classic_story": {
        "slug": "tuskevar",
        "author": "Fekete István",
        "work": "Tüskevár (1957)",
        "title": "A Kis-Balaton nádasa és Matula bácsi bölcsessége",
        "summary": "Tutajos és az öreg pákász, Matula bácsi a Kis-Balaton sűrű nádasában csónakázva a természet belső törvényeiről, a vadvilág tiszteletéről és az emberi beavatkozás határairól beszélgetnek.",
        "characters": ["Tutajos (Gyula)", "Matula bácsi"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A hajnali pára lassan szállt fel a Kis-Balaton végtelen nádasáról. A ladik szinte hangtalanul siklott a sötét vízen, miközben Tutajos óvatosan húzta az evezőt, ügyelve arra, hogy meg ne riassza a part mentén fészkelő kócsagokat.",
            },
            {
                "type": "dialogue",
                "speaker": "Matula bácsi",
                "text": "Lassan húzd, fiam! A természetben semmit sem szabad kapkodva csinálni. A vadak megóvása érdekében a csend az első szabály, amit az embernek meg kell tanulnia a berekben. Aki zajt csap, az nem lát meg semmit.",
            },
            {
                "type": "dialogue",
                "speaker": "Tutajos (Gyula)",
                "text": "Olyan hatalmas és érintetlen ez a nádas, Matula bácsi! Néha úgy érzem, mintha a városi világ és a gyárak zaja egy másik bolygón létezne. Miért kellett a folyókat szabályozni, ha a természet magától is ilyen tökéletesen működik?",
            },
            {
                "type": "narration",
                "text": "Az öreg pákász letette a pipáját a ladik deszkájára, és a távolba révedt, ahol a Zala folyó torkolata beleveszett a zöld sűrűségbe. Ismerte a láp minden rezdülését, és látta azokat a változásokat is, amelyeket az emberi beavatkozás idézett elő az évtizedek során.",
            },
            {
                "type": "dialogue",
                "speaker": "Matula bácsi",
                "text": "A folyamszabályozás folytán sok szántóföld nyert teret, csakhogy a vizes élőhelyek pusztulásának elkerülése végett most mégis vissza kell engedni a vizet a berekbe. Az ember azt hiszi, okosabb a természetnél, de a hibák következtében előbb-utóbb kénytelen visszakozni.",
            },
            {
                "type": "dialogue",
                "speaker": "Tutajos (Gyula)",
                "text": "Tehát a gátak és csatornák építése nem jelent mindig valódi haladást? Egyensúlyt kell teremteni a gazdaság és az ökoszisztéma között, különben elpusztul mindaz, amiért érdemes élni.",
            },
            {
                "type": "narration",
                "text": "A nádas felett egy rétisas körözött méltóságteljesen a reggeli napsütésben. Matula bácsi elégedetten bólintott; örült, hogy a fiú nemcsak horgászni tanult meg a nyáron, hanem megértette a táj és az élővilág iránti felelősséget is.",
            },
            {
                "type": "dialogue",
                "speaker": "Matula bácsi",
                "text": "Jól mondod, Tutajos. A vízgazdálkodás céljából lehet mérnököket hívni, de a táj tisztelete a szívben dől el. Jegyezd meg ezt, ha egyszer visszatérsz a nagyvárosba!",
            },
        ],
        "reading_questions": [
            {
                "question": "Miért inti csendre Matula bácsi Tutajost a csónakázás során?",
                "options": [
                    "Mert a vadvilág megóvása és megfigyelése érdekében a csend az elsődleges szabály a berekben.",
                    "Mert fél, hogy a halőrök észreveszik a ladikot.",
                    "Mert a motoros hajók zajától nem hallaná a szavait.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen tanulságot von le Matula bácsi a korábbi folyamszabályozásokról?",
                "options": [
                    "Bár szántókat nyertek, a hibák következtében most a vizes élőhelyek megóvása végett vissza kell engedni a vizet.",
                    "Hogy a természetet teljesen be kell betonozni a mezőgazdaság fejlesztése céljából.",
                    "Hogy a Kis-Balatont le kell csapolni új gyárak építése érdekében.",
                ],
                "correct": 0,
            },
            {
                "question": "Mit tart Matula bácsi a táj tisztelete szempontjából a legfontosabbnak?",
                "options": [
                    "Hogy a természet iránti felelősség nem csupán mérnöki számítás, hanem belső tisztelet kérdése.",
                    "Hogy minél több halat kell fogni a nyári szünidő alatt.",
                    "Hogy a fiataloknak a nagyvárosban kell maradniuk.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "For the Purpose of Avoiding (elkerülése végett, megóvása érdekében)",
            "grammar_label": "Purposive nominal compounds and postpositions (végett, érdekében, céljából)",
            "goals": [
                "I can express purpose and formal intentionality using végett, érdekében, and céljából",
                "I can correctly attach possessive suffixes to action nouns preceding purposive postpositions",
                "I can formulate environmental and technical policies in standard administrative style",
            ],
            "grammar_doc": {
                "slug": "purposive-postpositions",
                "title": "Purposive Postpositions: végett, érdekében, céljából",
                "text1_title": "Formal Purposive Postpositions with Possessive Nouns",
                "text1": "In formal, administrative, and ecological Hungarian, intentions and objectives are expressed with purposive postpositions governed by nouns with a 3rd person possessive suffix. 'Végett' ('for the purpose of / in order to') is traditionally paired with deverbal action nouns: 'a félreértések elkerülése végett' ('in order to avoid misunderstandings'), 'a természeti értékek megóvása végett' ('for the purpose of protecting natural values').",
                "text2_title": "Distinguishing érdekében and céljából",
                "text2": "'Érdekében' (literally 'in the interest of') highlights beneficial outcomes or public welfare: 'a biológiai sokféleség megőrzése érdekében' ('in the interest of preserving biodiversity'). 'Céljából' ('with the goal/purpose of') emphasizes institutional or statutory intent: 'monitoring vizsgálatok lefolytatása céljából' ('with the purpose of conducting monitoring investigations').",
                "table_title": "Purposive Postpositions in Hungarian",
                "table_rows": [
                    ["elkerülése végett", "A környezeti katasztrófák elkerülése végett szigorították a szabályokat."],
                    ["megóvása érdekében", "A ritka madárfajok megóvása érdekében lezárták a lápvidéket."],
                    ["fejlesztése céljából", "Az öntözőrendszerek korszerűsítése céljából pályázatot írtak ki."],
                    ["biztosítása végett", "A tiszta ivóvíz biztosítása végett új víztisztító művet építettek."],
                ],
                "examples": [
                    {
                        "spanish": "A természeti értékek megóvása érdekében szigorúan korlátozzák a látogatók számát a nemzeti parkban.",
                        "english": "In the interest of safeguarding natural values, they strictly limit the number of visitors in the national park.",
                    },
                    {
                        "spanish": "A talaj eróziójának elkerülése végett védőerdőket telepítettek a domboldalakra.",
                        "english": "In order to avoid soil erosion, they planted shelterbelts on the hillsides.",
                    },
                    {
                        "spanish": "A vizes élőhelyek helyreállítása céljából a kormány új vízgazdálkodási programot indított.",
                        "english": "With the purpose of restoring wetland habitats, the government launched a new water management program.",
                    },
                    {
                        "spanish": "A konfliktusok elkerülése végett a beruházó lakossági fórumot hívott össze a tervekről.",
                        "english": "In order to avoid conflicts, the developer called a civic forum regarding the plans.",
                    },
                ],
                "tip": "The preceding action noun must carry the appropriate possessive suffix (-a/-e, -ja/-je) before 'végett', 'érdekében', or 'céljából' (e.g. 'elkerülés' -> 'elkerülése végett').",
            },
            "words": [
                {"lemma": "végett", "translation": "for the purpose of / in order to", "pos": "postposition"},
                {"lemma": "érdekében", "translation": "in the interest of / for the sake of", "pos": "postposition"},
                {"lemma": "céljából", "translation": "with the purpose of / with the aim of", "pos": "postposition"},
                {"lemma": "megóvás", "translation": "preservation / safeguarding", "pos": "noun"},
                {"lemma": "elkerülés", "translation": "avoidance / prevention", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'megóvás' in ecological and environmental contexts?",
                        [
                            "the preservation, safeguarding, and protection of natural species and habitats",
                            "the industrial processing of raw timber into paper pulp",
                            "the construction of artificial drainage canals",
                        ],
                        0,
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which postposition is traditionally combined with action nouns to mean 'in order to / for the purpose of'?",
                        ["végett", "ellen", "alatt"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["végett", "for the purpose of / in order to"],
                            ["érdekében", "in the interest of"],
                            ["céljából", "with the aim of"],
                            ["megóvás", "preservation / safeguarding"],
                            ["elkerülés", "avoidance / prevention"],
                        ],
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct purposive construction expressing beneficial aim: 'A ritka fészkelőmadarak ____':",
                        ["megóvása érdekében", "megóvása miatt", "megóvása nélkül"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which phrase properly expresses preventive purpose: 'A súlyosabb károk ____ azonnal leállították a szivattyúzást'?",
                        ["elkerülése végett", "elkerülésével", "elkerülése során"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A lápvidék természetes ökoszisztémájának ____ új vízkormányzási rendszert építettek ki. (with the purpose of restoring [possessive])",
                        "helyreállítása céljából",
                        "With the purpose of restoring the marshland's natural ecosystem, they built a new water steering system.",
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A félreértések ____ a szakértők részletes magyarázatot fűztek a hatástanulmányhoz. (in order to avoid [possessive])",
                        "elkerülése végett",
                        "In order to avoid misunderstandings, the experts attached a detailed explanation to the impact study.",
                        ["b2-causal-purposive-chains"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "természeti", "értékek", "megóvása", "érdekében", "természetvédelmi", "területet", "létesítettek."],
                        ["A", "természeti", "értékek", "megóvása", "érdekében", "természetvédelmi", "területet", "létesítettek."],
                        "In the interest of preserving natural values, they established a protected nature area.",
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A környezeti katasztrófák tudatos ____ alapvető feladata minden felelős döntéshozónak. (avoidance / prevention [possessive])",
                        "elkerülése",
                        "Conscious avoidance of environmental disasters is a fundamental duty of every responsible decision-maker.",
                        ["b2-24-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "ritka", "élőhelyek", "megóvása", "közös", "társadalmi", "kötelességünk."],
                        ["A", "ritka", "élőhelyek", "megóvása", "közös", "társadalmi", "kötelességünk."],
                        "Preserving rare habitats is our shared social duty.",
                        ["b2-24-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Természetvédelmi őr", "text": "Miért zárták le a turisták elől a Kis-Balaton belső övezetét?"},
                            {"speaker": "Főigazgató", "text": "____"},
                        ],
                        [
                            "A ritka vízimadarak zavartalan költésének megóvása érdekében ideiglenes látogatási tilalmat rendeltünk el.",
                            "Mert elfogyott a benzin a csónakokból.",
                            "Végett nem lehet halászni a vízparton.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Környezetvédő mérnök", "text": "Miért van szükség a gátak átépítésére ezen a szakaszon?"},
                            {"speaker": "Vízügyi szakértő", "text": "____"},
                        ],
                        [
                            "A tavaszi villámárvizek elkerülése végett árapasztó csatornákat alakítunk ki.",
                            "Mert a gátak túl szépek a folyó partján.",
                            "Érdekében nem folyik a víz a mederben.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'megóvása érdekében' stating a concrete conservation policy.",
                                "answer": "A tiszta ivóvízbázisok megóvása érdekében szigorúan megtiltották a vegyszeres permetezést a védőövezetben.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'elkerülése végett' describing an environmental prevention measure.",
                                "answer": "A talajszennyezés elkerülése végett a gyár zárt rendszerű hulladéktárolót köteles üzemeltetni.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A vízminőség rendszeres ellenőrzése ____ a kutatók heti rendszerességgel vettek mintát a tóból. (with the purpose of [possessive])",
                        "céljából",
                        "With the purpose of regular checking of water quality, researchers took samples from the lake on a weekly basis.",
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes safeguarding or protecting natural values from destruction?",
                        ["megóvás", "elkerülés", "beruházás"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Long-Chain Cause and Consequence (következtében, hatására)",
            "grammar_label": "Causal postpositions and explanatory chains (következtében, hatására, eredményeképpen, folytán)",
            "goals": [
                "I can trace environmental cause-and-effect chains using következtében and hatására",
                "I can distinguish between intentional purpose (érdekében) and objective consequence (következtében)",
                "I can use eredményeképpen and folytán to report scientific findings",
            ],
            "grammar_doc": {
                "slug": "causal-chains-postpositions",
                "title": "Causal Postpositions: következtében, hatására, eredményeképpen",
                "text1_title": "Objective Causality: következtében and hatására",
                "text1": "Whereas purposive postpositions look forward to an intended goal, causal postpositions describe objective effects. 'Következtében' ('as a consequence of') introduces inevitable outcomes, frequently adverse: 'a szárazság következtében kiszáradtak a tavak' ('as a consequence of the drought, lakes dried up'). 'Hatására' ('under the influence / effect of') describes biological, physical, or climatic influence: 'a globális felmelegedés hatására' ('under the effect of global warming').",
                "text2_title": "Scientific Synthesis: eredményeképpen and folytán",
                "text2": "'Eredményeképpen' ('as a result of') marks culmination of long-term processes, often positive: 'a természetvédelmi intézkedések eredményeképpen visszatértek a vándormadarak'. 'Folytán' ('owing to / by virtue of') appears in elevated explanatory register: 'a folyamszabályozás folytán átalakult a vízrendszer'.",
                "table_title": "Causal Postpositions in Environmental Discourse",
                "table_rows": [
                    ["következtében", "A talajszennyezés következtében csökkent a terméshozam."],
                    ["hatására", "A klímaváltozás hatására gyakoribbá váltak a villámárvizek."],
                    ["eredményeképpen", "A védelmi program eredményeképpen megerősödött a vidraállomány."],
                    ["folytán", "A heves esőzések folytán megáradt a Zala folyó."],
                ],
                "examples": [
                    {
                        "spanish": "Az ipari szennyezés következtében pusztulásnak indult a folyami halállomány.",
                        "english": "As a consequence of industrial pollution, the river fish population began to perish.",
                    },
                    {
                        "spanish": "Az éghajlatváltozás hatására drasztikusan megváltozott a Kárpát-medence csapadékeloszlása.",
                        "english": "Under the influence of climate change, the precipitation distribution of the Carpathian Basin changed drastically.",
                    },
                    {
                        "spanish": "Az évtizedes élőhely-rekonstrukció eredményeképpen ismét megjelent a fekete gólya a berekben.",
                        "english": "As a result of decades of habitat reconstruction, the black stork reappeared in the wetland.",
                    },
                    {
                        "spanish": "A rosszul tervezett lecsapolás folytán a szomszédos területeken kiszáradt a talaj.",
                        "english": "Owing to poorly planned drainage, the soil dried out in neighboring areas.",
                    },
                ],
                "tip": "Do not confuse purpose ('érdekében') with cause ('következtében'): 'érdekében' is an intentional goal, while 'következtében' is an objective result.",
            },
            "words": [
                {"lemma": "következtében", "translation": "as a consequence of", "pos": "postposition"},
                {"lemma": "hatására", "translation": "under the effect of / influenced by", "pos": "postposition"},
                {"lemma": "eredményeképpen", "translation": "as a result of", "pos": "postposition"},
                {"lemma": "folytán", "translation": "owing to / as a result of", "pos": "postposition"},
                {"lemma": "éghajlatváltozás", "translation": "climate change", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is 'éghajlatváltozás' in modern scientific environmental discourse?",
                        [
                            "long-term shifts in global or regional climate patterns, temperatures, and precipitation",
                            "a daily meteorological weather forecast broadcast on television",
                            "the seasonal migration pattern of swallows in autumn",
                        ],
                        0,
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which causal postposition means 'as a consequence of'?",
                        ["következtében", "érdekében", "céljából"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["következtében", "as a consequence of"],
                            ["hatására", "under the effect of"],
                            ["eredményeképpen", "as a result of"],
                            ["folytán", "owing to"],
                            ["éghajlatváltozás", "climate change"],
                        ],
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the postposition introducing an adverse causal consequence: 'A vegyszerszivárgás ____ halpusztulás történt':",
                        ["következtében", "céljából", "érdekében"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which postposition describes biological influence or physical impact: 'A felmelegedés ____ korábban virágoznak a fák'?",
                        ["hatására", "folyamán", "végett"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A következetes természetvédelmi intézkedések ____ újra megtelepedtek a ritka vízimadarak. (as a result of)",
                        "eredményeképpen",
                        "As a result of consistent conservation measures, rare waterfowl settled again.",
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A heves nyári esőzések ____ sárlavina keletkezett a domboldalon. (owing to)",
                        "folytán",
                        "Owing to the heavy summer rains, a mudslide occurred on the hillside.",
                        ["b2-causal-purposive-chains"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "globális", "éghajlatváltozás", "hatására", "gyakoribbá", "válnak", "a", "rendkívüli", "aszályok."],
                        ["A", "globális", "éghajlatváltozás", "hatására", "gyakoribbá", "válnak", "a", "rendkívüli", "aszályok."],
                        "Under the effect of global climate change, extraordinary droughts are becoming more frequent.",
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A globális ____ közvetlen hatással van a Kárpát-medence természetes vízkészletére. (climate change)",
                        "éghajlatváltozás",
                        "Global climate change has a direct impact on the Carpathian Basin's natural water resources.",
                        ["b2-24-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "talaj", "szennyeződése", "következtében", "csökkent", "a", "mezőgazdasági", "terméshozam."],
                        ["A", "talaj", "szennyeződése", "következtében", "csökkent", "a", "mezőgazdasági", "terméshozam."],
                        "As a consequence of soil contamination, agricultural yield decreased.",
                        ["b2-24-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Meteorológus", "text": "Hogyan befolyásolja az éghajlatváltozás a hazai folyókat?"},
                            {"speaker": "Hidrológus", "text": "____"},
                        ],
                        [
                            "A magasabb hőmérséklet hatására a párolgás fokozódik, aminek következtében a nyári vízszintek drámaian lecsökkennek.",
                            "Nem befolyásolja, mert a folyókban nincsen víz.",
                            "Céljából nem esik az eső egész évben.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Biológus", "text": "Milyen eredménnyel zárult a védett vidrák visszatelepítési programja?"},
                            {"speaker": "Parkigazgató", "text": "____"},
                        ],
                        [
                            "A szakemberek kitartó munkájának eredményeképpen a populáció stabilizálódott a Kis-Balaton térségében.",
                            "Minden állat elment, mert nem szerették a vizet.",
                            "Végett nincsenek halak a tóban.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'hatására' describing climatic effects on vegetation.",
                                "answer": "A szokatlanul enyhe tél hatására a növények már februárban rügyezni kezdtek.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'következtében' explaining an ecological consequence of drought.",
                                "answer": "A hosszan tartó aszály következtében a sekély tavak teljesen kiszáradtak a térségben.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A növekvő ipari károsanyag-kibocsátás ____ romlott a folyami ökoszisztéma állapota. (under the effect of)",
                        "hatására",
                        "Under the effect of growing industrial pollutant emissions, the state of the river ecosystem deteriorated.",
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes broad long-term transformations of weather and climatic equilibrium?",
                        ["éghajlatváltozás", "megóvás", "elkerülés"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Balancing Infrastructure and Ecosystems",
            "grammar_label": "Environmental protection discourse and purposive-causal coordination (élőhely, ökoszisztéma, vízgazdálkodás)",
            "goals": [
                "I can analyze ecological trade-offs of large infrastructure projects",
                "I can formulate arguments for biodiversity protection using causal-purposive structures",
                "I can discuss wetland conservation and habitat restoration",
            ],
            "grammar_doc": {
                "slug": "ecosystem-stewardship-water",
                "title": "Ecosystem Stewardship & Water Management",
                "text1_title": "Wetland Conservation and Biodiversity",
                "text1": "Preserving fragile natural habitats ('élőhelyek') and complex ecosystems ('ökoszisztémák') is a fundamental pillar of environmental stewardship. In the Carpathian Basin, water management ('vízgazdálkodás') plays a decisive role in balancing agriculture with nature reserves ('természetvédelmi területek') to maintain biological diversity ('biológiai sokféleség').",
                "text2_title": "Causal-Purposive Articulation in Conservation",
                "text2": "Environmental scientists connect purpose and cause when formulating conservation protocols: 'A vizes élőhelyek rehabilitációja céljából vízkormányzási rendszert építettek ki, amelynek hatására helyreállt a lápvidék természetes ökoszisztémája'.",
                "table_title": "Ecology & Habitat Vocabulary",
                "table_rows": [
                    ["élőhely", "A nádas létfontosságú költő- és élőhely a vízimadarak számára."],
                    ["ökoszisztéma", "A folyami ökoszisztéma érzékenyen reagál az ipari beavatkozásokra."],
                    ["vízgazdálkodás", "A fenntartható vízgazdálkodás megakadályozza a talaj kiszáradását."],
                    ["biológiai sokféleség", "A természetvédelmi terület megőrzi a táj biológiai sokféleségét."],
                ],
                "examples": [
                    {
                        "spanish": "A vizes élőhelyek megőrzése céljából szigorú korlátozásokat vezettek be a Kis-Balaton védett zónájában.",
                        "english": "With the purpose of preserving wetland habitats, they introduced strict restrictions in the protected zone of the Kis-Balaton.",
                    },
                    {
                        "spanish": "A helyes vízgazdálkodás révén megakadályozható a lápvidék kiszáradása és a talaj pusztulása.",
                        "english": "Through sound water management, the drying out of the marshland and the destruction of soil can be prevented.",
                    },
                    {
                        "spanish": "A természetvédelmi terület kiterjesztése alapvető lépés a ritka madárfajok megóvása érdekében.",
                        "english": "Expanding the nature reserve is a fundamental step in the interest of safeguarding rare bird species.",
                    },
                    {
                        "spanish": "Az ökoszisztéma stabilitása nagymértékben függ az ott élő fajok biológiai sokféleségétől.",
                        "english": "The stability of an ecosystem depends to a great extent on the biological diversity of species living there.",
                    },
                ],
                "tip": "Compound nouns like 'vízgazdálkodás' and 'élőhelyvédelem' frequently govern purposive postpositions: 'a hatékony vízgazdálkodás megvalósítása céljából'.",
            },
            "words": [
                {"lemma": "élőhely", "translation": "habitat", "pos": "noun"},
                {"lemma": "ökoszisztéma", "translation": "ecosystem", "pos": "noun"},
                {"lemma": "vízgazdálkodás", "translation": "water management", "pos": "noun"},
                {"lemma": "természetvédelmi terület", "translation": "nature reserve / protected natural area", "pos": "noun"},
                {"lemma": "biológiai sokféleség", "translation": "biodiversity / biological diversity", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is an 'ökoszisztéma' in ecological science?",
                        [
                            "a complex community of living organisms interacting with their physical and abiotic environment",
                            "an artificial glasshouse dedicated exclusively to tropical flower propagation",
                            "a municipal waste processing facility in suburban zones",
                        ],
                        0,
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase denotes the variety of all living species within an ecosystem?",
                        ["biológiai sokféleség", "vízgazdálkodás", "hatásvizsgálat"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["élőhely", "habitat"],
                            ["ökoszisztéma", "ecosystem"],
                            ["vízgazdálkodás", "water management"],
                            ["természetvédelmi terület", "nature reserve"],
                            ["biológiai sokféleség", "biodiversity"],
                        ],
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the purposive phrase expressing the goal of wetland restoration: 'A lápvidék ____ vízkormányzási gátakat építettek':",
                        ["megőrzése céljából", "következtében", "folytán"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the sentence linking ecosystem preservation with purpose:",
                        [
                            "A biológiai sokféleség fenntartása érdekében védett övezeteket jelöltek ki a folyó mentén.",
                            "A biológiai sokféleség helyett betoncsatornákat építsünk mindenhova.",
                            "Múltával nem él semmilyen madár a nádasban.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A felelőtlen emberi beavatkozások ____ felborult a vizes élőhelyek természetes egyensúlya. (as a consequence of)",
                        "következtében",
                        "As a consequence of irresponsible human interventions, the natural balance of wetland habitats was upset.",
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A sérülékeny folyami ökoszisztéma ____ szigorúan ellenőrzik az ipari szennyvízkibocsátást. (in the interest of protecting [possessive])",
                        "védelme érdekében",
                        "In the interest of protecting the vulnerable river ecosystem, they strictly monitor industrial wastewater discharge.",
                        ["b2-causal-purposive-chains"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "vizes", "élőhelyek", "megőrzése", "céljából", "korlátozzák", "az", "ipari", "tevékenységet."],
                        ["A", "vizes", "élőhelyek", "megőrzése", "céljából", "korlátozzák", "az", "ipari", "tevékenységet."],
                        "With the purpose of preserving wetland habitats, they restrict industrial activity.",
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A szakszerű ____ nélkül a Kis-Balaton vize nem lenne képes megszűrni a Zala folyó hordalékát. (water management)",
                        "vízgazdálkodás",
                        "Without professional water management, the Kis-Balaton's water would not be capable of filtering the Zala river sediment.",
                        ["b2-24-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "természetvédelmi", "terület", "megóvja", "a", "vidék", "gazdag", "biológiai", "sokféleségét."],
                        ["A", "természetvédelmi", "terület", "megóvja", "a", "vidék", "gazdag", "biológiai", "sokféleségét."],
                        "The nature reserve safeguards the region's rich biological diversity.",
                        ["b2-24-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Ökológus", "text": "Miért olyan érzékeny a Kis-Balaton ökoszisztémája?"},
                            {"speaker": "Természetvédelmi szakember", "text": "____"},
                        ],
                        [
                            "Mert a sekély víz és a nádas egyensúlya könnyen felborul a tápanyag-túlterhelés következtében; megőrzése céljából állandó monitoring szükséges.",
                            "Mert nincs benne víz, csak száraz homok.",
                            "Érdekében nem él semmilyen hal a tóban.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gazdálkodó", "text": "Hogyan egyeztethető össze az öntözés a folyó védelmével?"},
                            {"speaker": "Vízügyi felügyelő", "text": "____"},
                        ],
                        [
                            "Olyan fenntartható vízgazdálkodásra van szükség, amelynek eredményeképpen a termés is biztonságban van és az élőhely sem károsodik.",
                            "Úgy, hogy lecsapoljuk az egész folyót szántóföldnek.",
                            "Végett nem szabad növényeket termeszteni a falu körül.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'ökoszisztéma megóvása érdekében' articulating an environmental goal.",
                                "answer": "A folyami ökoszisztéma megóvása érdekében elengedhetetlen a szennyvíztisztító telepek korszerűsítése.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'vízgazdálkodás fejlesztése céljából' proposing water infrastructure improvement.",
                                "answer": "A hatékonyabb vízgazdálkodás fejlesztése céljából új tározórendszert építettek ki a folyó mentén.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A természetes élőhelyek szűkülése ____ számos őshonos madárfaj veszélybe került. (as a consequence of)",
                        "következtében",
                        "As a consequence of the narrowing of natural habitats, numerous native bird species became endangered.",
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the natural environmental territory in which a species typically lives?",
                        ["élőhely", "ökoszisztéma", "hatásvizsgálat"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Environmental Impact Assessment",
            "grammar_label": "Environmental impact assessment, threshold compliance, and consequence reporting (hatásvizsgálat, határérték, kibocsátás)",
            "goals": [
                "I can interpret and articulate findings of an Environmental Impact Assessment (hatásvizsgálat)",
                "I can report pollution levels, emissions, and ecological thresholds",
                "I can construct conditional and causal arguments regarding project approval",
            ],
            "grammar_doc": {
                "slug": "environmental-impact-assessment",
                "title": "Environmental Impact Assessment: Thresholds & Risk Analysis",
                "text1_title": "Evaluating Technical vs. Ecological Impacts",
                "text1": "Before authorizing any industrial or transportation development, law requires an Environmental Impact Assessment ('hatásvizsgálat'). Experts analyze pollutant emissions ('károsanyag-kibocsátás'), potential soil contamination ('talajszennyezés'), and compare projected levels against legal threshold limits ('határértékek').",
                "text2_title": "Reporting Violations and Environmental Damage",
                "text2": "When thresholds are breached, reports document environmental destruction ('környezetkárosítás'). Syntactic constructions employ causal postpositions to attribute damage: 'A megengedett határérték túllépése következtében a hatóság felfüggesztette a gyár működési engedélyét'.",
                "table_title": "Environmental Assessment Vocabulary",
                "table_rows": [
                    ["hatásvizsgálat", "A környezeti hatásvizsgálat feltárta a beruházás kockázatait."],
                    ["károsanyag-kibocsátás", "A szigorúbb előírások csökkentik a gyárak károsanyag-kibocsátását."],
                    ["talajszennyezés", "A vegyi hulladék elszivárgása súlyos talajszennyezést idézett elő."],
                    ["határérték", "A mért nehézfém-koncentráció jóval meghaladta az egészségügyi határértéket."],
                ],
                "examples": [
                    {
                        "spanish": "A független környezeti hatásvizsgálat megállapította, hogy a tervezett autópálya kettévágná a védett élőhelyeket.",
                        "english": "The independent environmental impact assessment established that the planned motorway would bisect protected habitats.",
                    },
                    {
                        "spanish": "A megengedett határérték túllépése következtében a hatóság azonnal felfüggesztette az üzem engedélyét.",
                        "english": "As a consequence of exceeding the permissible threshold, the authority immediately suspended the plant's license.",
                    },
                    {
                        "spanish": "A gyár korszerűsítésének eredményeképpen a károsanyag-kibocsátás a felére csökkent.",
                        "english": "As a result of modernizing the factory, pollutant emissions were cut in half.",
                    },
                    {
                        "spanish": "A talajszennyezés elkerülése végett szigorú védőréteggel bélelték ki az új hulladéktárolót.",
                        "english": "In order to avoid soil contamination, they lined the new waste storage with a strict protective barrier.",
                    },
                ],
                "tip": "In environmental reports, use past participle attributive phrases ('a hatásvizsgálat során feltárt hiányosságok') before drawing legal conclusions.",
            },
            "words": [
                {"lemma": "hatásvizsgálat", "translation": "impact assessment / environmental review", "pos": "noun"},
                {"lemma": "károsanyag-kibocsátás", "translation": "pollutant emissions", "pos": "noun"},
                {"lemma": "talajszennyezés", "translation": "soil contamination", "pos": "noun"},
                {"lemma": "határérték", "translation": "threshold value / permissible limit", "pos": "noun"},
                {"lemma": "környezetkárosítás", "translation": "environmental damage / harm", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'hatásvizsgálat' in public infrastructure planning?",
                        [
                            "a statutory scientific investigation assessing the environmental impacts of a proposed development",
                            "a financial accounting statement calculating expected project profits",
                            "a municipal permit granting permission to erect temporary market stalls",
                        ],
                        0,
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes the legally permissible ceiling value for pollutant concentrations?",
                        ["határérték", "talajszennyezés", "élőhely"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["hatásvizsgálat", "impact assessment"],
                            ["károsanyag-kibocsátás", "pollutant emissions"],
                            ["talajszennyezés", "soil contamination"],
                            ["határérték", "threshold limit"],
                            ["környezetkárosítás", "environmental damage"],
                        ],
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the postposition expressing cause in: 'A kibocsátási határértékek túllépése ____ bírságot szabtak ki':",
                        ["következtében", "céljából", "végett"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the purposive phrase expressing intention to avert pollution:",
                        ["a talajszennyezés megelőzése céljából", "a talajszennyezés hatására", "a talajszennyezés folytán"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A részletes hatásvizsgálat ____ megállapították, hogy a projekt veszélyezteti a talajvizet. (in the course of)",
                        "során",
                        "In the course of the detailed impact assessment, they established that the project endangers groundwater.",
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A súlyos környezetkárosítás ____ az üzemeltető köteles helyreállítani az eredeti állapotot. (in order to avoid [possessive])",
                        "elkerülése végett",
                        "In order to avoid severe environmental damage, the operator is obligated to restore the original state.",
                        ["b2-causal-purposive-chains"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "környezeti", "hatásvizsgálat", "lefolytatása", "céljából", "független", "szakértői", "bizottságot", "hoztak", "létre."],
                        ["A", "környezeti", "hatásvizsgálat", "lefolytatása", "céljából", "független", "szakértői", "bizottságot", "hoztak", "létre."],
                        "With the purpose of conducting an environmental impact assessment, they established an independent expert committee.",
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A mérgező nehézfémek kiszivárgása évtizedekre kiterjedő ____ okozott a térségben. (soil contamination)",
                        "talajszennyezést",
                        "The leakage of toxic heavy metals caused soil contamination extending across decades in the region.",
                        ["b2-24-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "gyár", "károsanyag-kibocsátása", "jóval", "a", "megengedett", "határérték", "alatt", "maradt."],
                        ["A", "gyár", "károsanyag-kibocsátása", "jóval", "a", "megengedett", "határérték", "alatt", "maradt."],
                        "The factory's pollutant emissions remained well below the permissible threshold limit.",
                        ["b2-24-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Hatósági ellenőr", "text": "Miért kellett leállítani az ipari létesítmény próbaüzemét?"},
                            {"speaker": "Környezetvédelmi jogász", "text": "____"},
                        ],
                        [
                            "A károsanyag-kibocsátási határértékek többszöri túllépése következtében a hatóság nem adhatta meg a működési engedélyt.",
                            "Mert a munkások nem akartak dolgozni a hétvégén.",
                            "Végett nincsenek falak a gyárépületen.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Civil aktivista", "text": "Hogyan biztosítható, hogy ne történjen környezetkárosítás a beruházás során?"},
                            {"speaker": "Projektvezető", "text": "____"},
                        ],
                        [
                            "A szennyezések megelőzése céljából folyamatos online mérőállomásokat telepítünk a folyó mentén.",
                            "Úgy, hogy nem mérünk semmit, és akkor nincs probléma.",
                            "Érdekében nem engedünk senkit beszélni a lakógyűlésen.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'határérték túllépése következtében' reporting an environmental violation.",
                                "answer": "A megengedett zajkibocsátási határérték túllépése következtében a bíróság felfüggesztette az építkezést.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'környezetkárosítás elkerülése végett' proposing a precautionary step.",
                                "answer": "A környezetkárosítás elkerülése végett a beruházó köteles független monitoring rendszert működtetni.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A szigorúbb környezetvédelmi szabályozás ____ harmadával csökkent a gyár károsanyag-kibocsátása. (under the effect of)",
                        "hatására",
                        "Under the effect of stricter environmental regulation, the factory's pollutant emissions decreased by a third.",
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the volume of pollutants released into the atmosphere or water?",
                        ["károsanyag-kibocsátás", "talajszennyezés", "hatásvizsgálat"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Debating a Major Infrastructure Project",
            "grammar_label": "Writing a balanced ecological assessment with causal and purposive postpositional chains",
            "goals": [
                "I can present a balanced debate on major infrastructure developments (dams, motorways, railways)",
                "I can integrate multiple causal and purposive postpositional chains in sustained debate",
                "I can formulate policy recommendations reconciling economic growth with ecological stewardship",
            ],
            "grammar_doc": {
                "slug": "infrastructure-project-debate",
                "title": "Debating Large-Scale Infrastructure Projects",
                "text1_title": "Reconciling Economic Growth and Ecological Protection",
                "text1": "Major capital investment projects ('beruházások')—such as motorways, high-speed rail lines, and hydroelectric dams—often create sharp conflict between economic development and landscape preservation ('tájrendezés'). Public hearings ('közmeghallgatás') provide a civic arena where citizens, developers, and green groups debate environmental consciousness ('környezettudatosság') and the adoption of renewable energy ('megújuló energia').",
                "text2_title": "Complex Causal-Purposive Chains in Debate",
                "text2": "In public debate, debaters combine multiple causal and purposive postpositions within single balanced arguments: 'Bár a vasútvonal kiépítése a gazdasági növekedés elősegítése céljából történik, a védett erdők pusztulásának elkerülése végett elkerülő nyomvonal kijelölése szükséges'.",
                "table_title": "Infrastructure & Ecological Debate Discourse",
                "table_rows": [
                    ["beruházás", "A nagyszabású infrastrukturális beruházás megosztotta a közvéleményt."],
                    ["tájrendezés", "A bányászat befejezése után kötelező a tájrendezés és rekultiváció."],
                    ["megújuló energia", "A szél- és napenergia mint megújuló energiaforrás támogatandó."],
                    ["közmeghallgatás", "A viharos közmeghallgatáson a helyi lakosok tiltakoztak az építkezés ellen."],
                ],
                "examples": [
                    {
                        "spanish": "A beruházás megvalósítása céljából benyújtott terveket a lakosság környezettudatos része hevesen bírálta.",
                        "english": "The plans submitted with the aim of implementing the investment were sharply criticized by the environmentally conscious part of the public.",
                    },
                    {
                        "spanish": "A közmeghallgatás során kiderült, hogy a tájrombolás elkerülése végett módosítani kell az autópálya nyomvonalát.",
                        "english": "During the public hearing, it turned out that in order to avoid landscape destruction, the motorway route must be modified.",
                    },
                    {
                        "spanish": "A megújuló energiaforrások elterjedése következtében csökkenthető az ország fosszilis energiafüggősége.",
                        "english": "As a consequence of the proliferation of renewable energy sources, the country's fossil energy dependency can be reduced.",
                    },
                    {
                        "spanish": "A gondos tájrendezés eredményeképpen a bezárt kavicsbánya helyén vonzó pihenőtó létesült.",
                        "english": "As a result of careful landscape restoration, an attractive recreational lake was established on the site of the closed gravel pit.",
                    },
                ],
                "tip": "Chain contrasting postpositions when presenting concession and compromise: 'bár X megvalósítása céljából... mindazonáltal Y elkerülése végett...'.",
            },
            "words": [
                {"lemma": "beruházás", "translation": "investment project / capital development", "pos": "noun"},
                {"lemma": "tájrendezés", "translation": "landscape planning / restoration", "pos": "noun"},
                {"lemma": "megújuló energia", "translation": "renewable energy", "pos": "noun"},
                {"lemma": "környezettudatosság", "translation": "environmental consciousness", "pos": "noun"},
                {"lemma": "közmeghallgatás", "translation": "public hearing", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'közmeghallgatás' in environmental administrative procedures?",
                        [
                            "a mandatory public hearing where citizens and experts express concerns regarding large investment projects",
                            "a private shareholders' meeting allocating annual dividend payouts",
                            "a courtroom trial sentencing individuals for criminal infractions",
                        ],
                        0,
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes ecological mindfulness and responsible societal attitude toward nature?",
                        ["környezettudatosság", "beruházás", "tájrendezés"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["beruházás", "investment project"],
                            ["tájrendezés", "landscape planning"],
                            ["megújuló energia", "renewable energy"],
                            ["környezettudatosság", "environmental consciousness"],
                            ["közmeghallgatás", "public hearing"],
                        ],
                        ["b2-24-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the purposive construction introducing project implementation:",
                        ["a beruházás megvalósítása céljából", "a beruházás következtében", "a beruházás hatására"],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Choose the sentence expressing an aim to avoid environmental damage:",
                        [
                            "A természetkárosítás elkerülése végett a vasútvonal alagútban halad a nemzeti park alatt.",
                            "A természetkárosítás helyett minden fát vágjunk ki azonnal.",
                            "Következtében nem épül semmilyen vasút sehol.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A helyi lakosság tiltakozásának ____ a beruházó beleegyezett a nyomvonal módosításába. (under the effect of / influenced by)",
                        "hatására",
                        "Influenced by the protest of the local population, the developer agreed to modify the route.",
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A táj természeti egyensúlyának ____ a bányászat után átfogó rekultivációt hajtottak végre. (in the interest of restoring [possessive])",
                        "helyreállítása érdekében",
                        "In the interest of restoring the landscape's natural balance, comprehensive reclamation was carried out after mining.",
                        ["b2-causal-purposive-chains"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "nagyszabású", "beruházás", "megvalósítása", "céljából", "közmeghallgatást", "hívtak", "össze", "a", "faluban."],
                        ["A", "nagyszabású", "beruházás", "megvalósítása", "céljából", "közmeghallgatást", "hívtak", "össze", "a", "faluban."],
                        "With the purpose of implementing the large-scale investment, they called a public hearing in the village.",
                        ["b2-causal-purposive-chains"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "Az ipari övezet bezárása után megkezdődött a terület ökológiai célú ____. (landscape planning [possessive])",
                        "tájrendezése",
                        "After the closure of the industrial zone, the ecological landscape restoration of the area began.",
                        ["b2-24-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "megújuló", "energiaforrások", "használata", "erősíti", "a", "társadalom", "környezettudatosságát."],
                        ["A", "megújuló", "energiaforrások", "használata", "erősíti", "a", "társadalom", "környezettudatosságát."],
                        "Using renewable energy sources strengthens society's environmental consciousness.",
                        ["b2-24-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Civil szervezet elnöke", "text": "Miért tiltakoznak a lakosok a tervezett logisztikai központ ellen?"},
                            {"speaker": "Helyi képviselő", "text": "____"},
                        ],
                        [
                            "A zöldterületek elvesztésének elkerülése végett alternatív helyszínt követelünk az önkormányzattól.",
                            "Mert a raktárakban nincsenek asztalok és székek.",
                            "Hatására nem szabad semmit sem építeni a megyében.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gazdasági miniszter", "text": "Hogyan értékeli a megújuló energiaparkok fejlesztését?"},
                            {"speaker": "Energetikai szakértő", "text": "____"},
                        ],
                        [
                            "A beruházások eredményeképpen jelentősen csökken az üvegházhatású gázok kibocsátása, miközben nő az energiabiztonság.",
                            "Nagyon rosszul, mert a napenergia túl fényes a madaraknak.",
                            "Végett nem lehet villanyt kapcsolni a házakban.",
                        ],
                        0,
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence combining 'megvalósítása céljából' with 'elkerülése végett' in an infrastructure compromise.",
                                "answer": "A vasútvonal korszerűsítése céljából új hidat építenek, de a nádas pusztulásának elkerülése végett elkerülik a védett öblöt.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'eredményeképpen' describing an environmental cleanup success.",
                                "answer": "A sikeres tájrendezés eredményeképpen a korábbi ipari területen új közpark nyílt a városlakók számára.",
                            }
                        ],
                        ["b2-causal-purposive-chains"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A lakossági összefogás ____ a hatóság elrendelte a környezeti hatásvizsgálat megismétlését. (as a result of)",
                        "eredményeképpen",
                        "As a result of citizen solidarity, the authority ordered the repetition of the environmental impact assessment.",
                        ["b2-causal-purposive-chains"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the public forum held to debate major infrastructure developments?",
                        ["közmeghallgatás", "beruházás", "tájrendezés"],
                        0,
                        ["b2-24-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can use purposive postpositions (végett, érdekében, céljából) with correct possessive governance",
            "I can connect cause and effect in environmental prose using következtében, hatására, and eredményeképpen",
            "I can formulate balanced ecological arguments evaluating technical infrastructure and nature stewardship",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["élőhely", "habitat"],
                    ["ökoszisztéma", "ecosystem"],
                    ["hatásvizsgálat", "impact assessment"],
                    ["tájrendezés", "landscape restoration"],
                    ["környezettudatosság", "environmental awareness"],
                ],
                ["b2-24-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What is the primary function of an Environmental Impact Assessment (hatásvizsgálat)?",
                [
                    "to scientifically forecast, evaluate, and mitigate the ecological consequences of an infrastructure project",
                    "to assess the aesthetic taste of private residential garden decorations",
                    "to determine the commercial retail prices of agricultural produce",
                ],
                0,
                ["b2-24-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly distinguishes intentional purpose from objective consequence?",
                [
                    "A ritka fajok megóvása érdekében korlátozták a forgalmat, aminek következtében regenerálódott a növényzet.",
                    "A ritka fajok következtében korlátozták a forgalmat, aminek érdekében pusztult el minden.",
                    "Végett nem történt semmi a természetvédelmi területen tegnap.",
                ],
                0,
                ["b2-causal-purposive-chains"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A Kárpát-medence gazdag természeti kincse a lenyűgöző ____, amelyet óvnunk kell. (biological diversity)",
                "biológiai sokféleség",
                "The rich natural treasure of the Carpathian Basin is its stunning biological diversity, which we must protect.",
                ["b2-24-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A talajvíz elszennyeződésének ____ szigorú monitoring rendszert vezettek be az ipari park körül. (in order to avoid [possessive])",
                "elkerülése végett",
                "In order to avoid contamination of groundwater, they introduced a strict monitoring system around the industrial park.",
                ["b2-causal-purposive-chains"],
            ),
            fb(
                "grammar",
                "recall",
                "A súlyos szárazság ____ drámai mértékben leapadt a Zala folyó vízszintje. (as a consequence of)",
                "következtében",
                "As a consequence of the severe drought, the Zala river's water level dropped dramatically.",
                ["b2-causal-purposive-chains"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Select the sentence using 'céljából' to express administrative and institutional intent:",
                [
                    "A Kis-Balaton vizes élőhelyeinek rehabilitációja céljából nagyszabású európai uniós projekt indult.",
                    "A rehabilitáció következtében senki sem indított semmilyen projektet.",
                    "Céljából nem volt víz a csatornákban a nyár folyamán.",
                ],
                0,
                ["b2-causal-purposive-chains"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Főépítész", "text": "Hogyan reagált a közvélemény a gátépítési tervekre a közmeghallgatáson?"},
                    {"speaker": "Jegyző", "text": "____"},
                ],
                [
                    "A lakosság határozott fellépésének hatására a beruházó visszavonta az eredeti tervet az élőhelyek megóvása érdekében.",
                    "Senki sem jött el, mert a gátak nem érdekelnek senkit a városban.",
                    "Következtében tilos beszélni a vizekről a városházán.",
                ],
                0,
                ["b2-causal-purposive-chains"],
            ),
            mc(
                "grammar",
                "in-context",
                "Why is 'elkerülése végett' preferred over 'elkerülése miatt' in policy recommendations?",
                [
                    "Because 'végett' denotes forward-looking intention and purpose, whereas 'miatt' denotes backward-looking reason or cause.",
                    "Because 'miatt' can never be preceded by a possessive noun in Hungarian.",
                    "Because 'végett' is exclusively used for informal spoken language.",
                ],
                0,
                ["b2-causal-purposive-chains"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "védett", "élőhelyek", "megóvása", "érdekében", "a", "hatóság", "felfüggesztette", "a", "beruházást."],
                ["A", "védett", "élőhelyek", "megóvása", "érdekében", "a", "hatóság", "felfüggesztette", "a", "beruházást."],
                "In the interest of preserving protected habitats, the authority suspended the investment.",
                ["b2-causal-purposive-chains"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "szigorúbb", "előírások", "hatására", "jelentősen", "csökkent", "a", "környező", "talajszennyezés."],
                ["A", "szigorúbb", "előírások", "hatására", "jelentősen", "csökkent", "a", "környező", "talajszennyezés."],
                "Under the effect of stricter regulations, surrounding soil contamination decreased significantly.",
                ["b2-causal-purposive-chains"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a three-clause environmental policy argument combining 'fejlesztése céljából', 'következtében', and 'elkerülése végett'.",
                        "answer": "Bár a zöld infrastruktúra fejlesztése céljából új tározókat létesítenek, a korábbi hibák következtében fellépő vízhiány intő jel marad; ezért a további természetkárosítás elkerülése végett minden egyes lépést független hatásvizsgálatnak kell alávetni.",
                    }
                ],
                ["b2-causal-purposive-chains"],
            ),
        ],
    },
}


def main():
    for spec in (UNIT_22, UNIT_23, UNIT_24):
        build_core_unit(spec)


if __name__ == "__main__":
    main()


