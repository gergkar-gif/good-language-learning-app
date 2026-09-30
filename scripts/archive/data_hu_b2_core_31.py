"""
Hungarian B2 Core Track Unit 31:
  b2-31: Gastronomy, Conviviality & Cultural Rituals
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_31 = {
    "unit_num": 31,
    "title": "Gastronomy, Conviviality & Cultural Rituals",
    "grammar_summary": "Resultative sublative phrases denoting culinary end states (pirosra süti, ropogósra pirítja, sűrűre főzi) and hypothetical sensory comparisons with mintha + conditional.",
    "grammar_skill": "b2-resultative-similes",
    "vocab_skill": "b2-31-vocab",
    "theme": "Gastronomy, conviviality and cultural rituals",
    "intro_body": [
        "A gasztronómia a magyar kultúrában nem csupán a táplálkozásról szól, hanem az együttlét, a családi és baráti kötelékek megerősítésének, valamint az érzéki emlékezetnek a szentélye. A Krúdy Gyula által oly finoman megörökített vasárnapi húslevesek és kockás abroszos vendéglők világa mélyen gyökerezik a nemzeti önképben.",
        "Ebben a fejezetben elsajátíthatja a célállapotot kifejező eredményhatározói kifejezéseket (pirosra süti, ropogósra pirítja, puhára párolja), a finom érzéki hasonlatokat és feltételes szerkezeteket (mintha csak most vették volna ki a kemencéből), valamint az ízek, textúrák, asztali rituálék és étteremkritikák választékos B2-es szókincsét.",
    ],
    "classic_story": {
        "slug": "szindbad",
        "author": "Krúdy Gyula",
        "work": "Szindbád: Ínyesmesék (1911)",
        "title": "A velős csont és a vasárnapi húsleves emlékezete",
        "summary": "Szindbád egy csendes óbudai kiskocsmában a gőzölgő marhahúsleves és a forró velős csont szertartásos elfogyasztása közben a múlt emlékeit, az ízek múlandóságát és az élet apró gyönyöreit idézi fel.",
        "characters": ["Szindbád", "A vendéglős"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Az óbudai kiskocsma sarkában, a kockás abrosz mellett Szindbád csendesen várta a vasárnapi levest. Az ablaküvegen sűrű pára gyöngyözött, kinn az őszi eső mosta a macskaköveket, idebent pedig a fokhagymás pirítós és a forró zsíros gőz édes, meleg otthonosságot teremtett.",
            },
            {
                "type": "dialogue",
                "speaker": "A vendéglős",
                "text": "Szindbád uram, a húsleves több mint három órán át gyöngyözött a sparhelten lábszárral és sárgarépával. A velős csontot éppen most emeltük ki a fazékból; olyan forró, hogy puszta kézzel hozzá sem lehetne érni.",
            },
            {
                "type": "dialogue",
                "speaker": "Szindbád",
                "text": "Köszönöm, kedves mesterem. A velős pirítós nem csupán étel, hanem szertartás. Ha az ember a forró velőt a fokhagymával megkent kenyérre simítja, mintha a fiatalságát kapná vissza egyetlen falattal.",
            },
            {
                "type": "narration",
                "text": "Szindbád lassú, kimért mozdulatokkal kocogtatta a hosszú csontot a kistányér széléhez, míg a reszketeg, puha velő ki nem csusszant a frissen pirított kenyérre. Sóval hintette meg, durvára őrölt fekete borssal szórta be, majd lehunyt szemmel kóstolta meg a falatot.",
            },
            {
                "type": "dialogue",
                "speaker": "Szindbád",
                "text": "Nézze csak ezt az aranysárga színt! Olyan tiszta ez a lé, mintha hegyi forrásvizet szűrtünk volna át a sáfrányon. A marhahús pedig puhára párolódott, szinte szétolvad az ember nyelvén.",
            },
            {
                "type": "dialogue",
                "speaker": "A vendéglős",
                "text": "Jól tudjuk errefelé, mi jár a törzsvendégnek. Egy kis pohár száraz somlói juhfarkat készítettem ki mellé, mert a bor finom savai pompásan ellensúlyozzák a velő gazdagságát.",
            },
            {
                "type": "narration",
                "text": "Szindbád elmerengett. A húsleves illatfelhőjében felselettek a hajdani kisvárosi vasárnapok emlékei: fehér csipketerítők, távoli csengettyűszó a templomból, és a hölgyek, akiknek pillantása éppoly melegséggel töltötte el a szívét, mint a forró fűszeres lé.",
            },
            {
                "type": "narration",
                "text": "Végül letette az ezüstkanalat, és megelégedetten dőlt hátra a kopott székben. A jóllakottság békéje töltötte el lelkét; tudta, hogy a világ zaklatottan változik odakint, de amíg akad egy csendes vendéglő gőzölgő levessel és jó borral, addig az élet elviselhető marad.",
            },
        ],
        "reading_questions": [
            {
                "question": "Hogyan fogyasztja el Szindbád a velős csontot a leírás szerint?",
                "options": [
                    "Kimért mozdulatokkal kiüti a velőt a fokhagymás pirítósra, sózza, borsozza, és lehunyt szemmel ízleli meg.",
                    "Gyorsan belekeveri a levesbe, mielőtt az teljesen kihűlne az asztalon.",
                    "Villával darabokra vágja a tányérján, és kenyér nélkül eszi meg.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen asszociációkat ébreszt Szindbádban a forró húsleves és a velő elfogyasztása?",
                "options": [
                    "A hajdani kisvárosi vasárnapok békéjét, fehér csipketerítőket és a letűnt ifjúság emlékeit idézi fel.",
                    "A külföldi utazások során szerzett keserű csalódásokra emlékezteti.",
                    "Kizárólag a konyhai alapanyagok árára és a vendéglő számlájára gondol.",
                ],
                "correct": 0,
            },
            {
                "question": "Miért kínál a vendéglős száraz somlói bort az étel mellé?",
                "options": [
                    "Mert a bor élénk savai kiválóan ellensúlyozzák a velő zsíros gazdagságát.",
                    "Mert a vendéglőben nem volt semmilyen más ital raktáron aznap.",
                    "Mert a húslevesbe szokás beleönteni egy egész pohár bort a tálalás előtt.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Resultative Sublative Phrases (pirosra süti, ropogósra pirítja)",
            "grammar_label": "Resultative sublative phrases denoting final states (-ra/-re: pirosra süti, ropogósra pirítja, puhára párolja)",
            "goals": [
                "I can use resultative sublative phrases (-ra/-re) to describe the final state of culinary transformations",
                "I can distinguish between ongoing culinary actions and target end states (pirosra süt, puhára párol)",
                "I can apply precise gastronomic cooking adjectives in resultative structures",
            ],
            "grammar_doc": {
                "slug": "resultative-sublative-phrases-cooking",
                "title": "Resultative Sublative Phrases: pirosra süt, ropogósra pirít, puhára párol",
                "text1_title": "Expressing Resulting State with the Sublative (-ra/-re)",
                "text1": "In Hungarian, the sublative case (-ra/-re) attached to an adjective frequently functions as an adverbial of result (eredményhatározó). It denotes the final physical state, texture, or color attained by the object as a direct consequence of a culinary process. Instead of using a subordinate clause ('addig süti, amíg piros nem lesz'), Hungarian encapsulates the transformation succinctly: 'pirosra süti a húst' (browns/fries the meat until red/crispy).",
                "text2_title": "Common Culinary Verb-Adjective Collocations",
                "text2": "Common collocations include 'ropogósra pirít' (to toast until crispy), 'puhára párol' (to braise until tender), 'aranybarnára süt' (to bake until golden brown), 'sűrűre főz' (to reduce/cook until thick), 'finomra aprít' (to chop finely), and 'készre süt' (to bake until fully done). Note that the adjective always takes the sublative suffix harmonizing with its vowels (-ra after back vowels, -re after front vowels).",
                "table_title": "Frequent Resultative Sublative Combinations",
                "table_rows": [
                    ["ropogósra pirít", "A kenyérszeleteket ropogósra pirítjuk a serpenyőben. (Toast until crispy.)"],
                    ["puhára párol", "A hagymát és a zöldségeket puhára pároljuk fedő alatt. (Braise until tender.)"],
                    ["aranybarnára süt", "A sütemény tetejét aranybarnára sütjük a sütőben. (Bake until golden brown.)"],
                    ["sűrűre főz", "A gyümölcslevet lassan sűrűre főzzük a lekvárhoz. (Boil down until thick.)"],
                ],
                "examples": [
                    {
                        "spanish": "A szakács pirosra sütötte a kacsacombokat a forró kemencében.",
                        "english": "The chef roasted the duck legs until crisp and brown in the hot oven.",
                    },
                    {
                        "spanish": "A vöröshagymát lassú tűzön üvegesre pároljuk, mielőtt hozzáadnánk a fűszerpaprikát.",
                        "english": "We sweat the onion until translucent over low heat before adding the paprika.",
                    },
                    {
                        "spanish": "A mártást addig forralták, amíg sűrűre nem főtt.",
                        "english": "They boiled the sauce until it was reduced to a thick consistency.",
                    },
                    {
                        "spanish": "A petrezselymet finomra aprítva szórjuk a gőzölgő húsleves tetejére.",
                        "english": "We sprinkle the parsley finely chopped onto the top of the steaming broth.",
                    },
                ],
                "tip": "Do not confuse the manner adverbial (-an/-on/-en: 'ropogósan tálalja') with the resultative sublative (-ra/-re: 'ropogósra pirítja'). The sublative specifies the outcome reached through the cooking process.",
            },
            "words": [
                {"lemma": "ropogósra pirít", "translation": "to toast / fry until crispy", "pos": "expression"},
                {"lemma": "puhára párol", "translation": "to braise / steam until tender", "pos": "expression"},
                {"lemma": "aranybarna", "translation": "golden brown", "pos": "adjective"},
                {"lemma": "sűrűre főz", "translation": "to reduce / boil down until thick", "pos": "expression"},
                {"lemma": "finomra aprít", "translation": "to chop finely", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'ropogósra pirít' mean in culinary instructions?",
                        [
                            "to fry or toast an ingredient until it reaches a crispy texture",
                            "to boil vegetables in salted water until they lose color",
                            "to freeze dough overnight in the refrigerator",
                        ],
                        0,
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which phrase describes braising meat or vegetables until completely tender?",
                        ["puhára párol", "finomra aprít", "ropogósra pirít"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["ropogósra pirít", "to toast / fry until crispy"],
                            ["puhára párol", "to braise until tender"],
                            ["aranybarna", "golden brown"],
                            ["sűrűre főz", "to boil down until thick"],
                            ["finomra aprít", "to chop finely"],
                        ],
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case suffix forms resultative state phrases in 'A séf aranybarna____ sütötte a kalácsot'?",
                        ["-ra", "-ként", "-ul"],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct form for 'We cook the tomato sauce until thick':",
                        [
                            "A paradicsommártást sűrűre főzzük.",
                            "A paradicsommártást sűrűn főzzük.",
                            "A paradicsommártást sűrűből főzzük.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A fokhagymát egy éles késsel ____ aprítjuk a pörkölthöz. (finely)",
                        "finomra",
                        "We chop the garlic finely with a sharp knife for the stew.",
                        ["b2-resultative-similes"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A marhahúst lassú tűzön, fedő alatt ____ párolta a szakács. (until tender)",
                        "puhára",
                        "The cook braised the beef until tender over low heat under a lid.",
                        ["b2-resultative-similes"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "kenyérszeleteket", "forró", "serpenyőben", "ropogósra", "pirítjuk."],
                        ["A", "kenyérszeleteket", "forró", "serpenyőben", "ropogósra", "pirítjuk."],
                        "We toast the bread slices until crispy in a hot skillet.",
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A kelt tésztát addig sütjük a forró kemencében, míg szép ____ nem lesz a teteje. (golden brown)",
                        "aranybarna",
                        "We bake the yeast dough in the hot oven until its top turns a lovely golden brown.",
                        ["b2-31-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szilvalevet", "egész", "éjszaka", "sűrűre", "főzték", "a", "bográcsban."],
                        ["A", "szilvalevet", "egész", "éjszaka", "sűrűre", "főzték", "a", "bográcsban."],
                        "They boiled down the plum juice until thick all night in the cauldron.",
                        ["b2-31-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kezdő szakács", "text": "Hogyan érhetem el, hogy a kacsamell bőre igazán élvezetes legyen?"},
                            {"speaker": "Konyhafőnök", "text": "____"},
                        ],
                        [
                            "Először hideg serpenyőbe tedd zsiradék nélkül, és lassan pirítsd ropogósra a bőrét, majd a sütőben süsd készre.",
                            "Önts rá hideg vizet, és főzd szét teljesen tíz perc alatt.",
                            "A kacsamell bőrét mindig nyersen kell hagyni a tálaláskor.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Gasztronómiai riporter", "text": "Mi a titka a hagyományos magyar gulyásleves alapjának?"},
                            {"speaker": "Hagyományőrző szakács", "text": "____"},
                        ],
                        [
                            "A finomra aprított hagymát kíméletesen üvegesre pároljuk, nem szabad megégetni, mielőtt a hús belekerül.",
                            "A hagymát nyersen a levesbe dobjuk a főzés legvégén.",
                            "Kizárólag cukrot és ecetet forralunk sűrűre a fazékban.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a recipe instruction using 'puhára párol' with a direct object.",
                                "answer": "A kockára vágott marhalábszárat kevés vörösbor hozzáadásával fedő alatt puhára pároljuk.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'ropogósra pirít' to describe preparing garnish.",
                                "answer": "A tálalás előtt a füstölt szalonnát apró kockákra vágjuk, és serpenyőben ropogósra pirítjuk.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A mártást addig kevergette a tűzön, amíg kellemesen ____ nem főzte. (until thick)",
                        "sűrűre",
                        "He stirred the sauce over the fire until he boiled it down pleasantly thick.",
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes chopping herbs into minute pieces?",
                        ["finomra aprít", "puhára párol", "sűrűre főz"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Hypothetical Sensory Comparisons (mintha csak most vették volna ki)",
            "grammar_label": "Sensory similes with mintha + conditional (mintha csak most vették volna ki a kemencéből)",
            "goals": [
                "I can construct vivid sensory similes using mintha combined with the conditional mood",
                "I can evoke nostalgic or imaginary gustatory impressions in gastronomic discourse",
                "I can select between present and past conditional when formulating hypothetical comparisons",
            ],
            "grammar_doc": {
                "slug": "hypothetical-sensory-similes-mintha",
                "title": "Hypothetical Sensory Comparisons: mintha + Conditional",
                "text1_title": "Evoking Sensory Illusions with mintha",
                "text1": "In Hungarian literary gastronomy, complex taste impressions and aromas are frequently captured through hypothetical comparisons introduced by the conjunction 'mintha' (as if / as though). Because the comparison describes a subjective sensation or imaginary reality rather than a factual event, the subordinate clause requires the conditional mood (feltételes mód).",
                "text2_title": "Tense Distinctions in mintha Clauses",
                "text2": "When referring to a simultaneous hypothetical state, the present conditional is used: 'Olyan puha, mintha vaj lenne' (It is so soft, as if it were butter). When referring to an antecedent completed event or nostalgic memory, the past conditional is employed: 'Olyan friss a kenyér, mintha csak most vették volna ki a kemencéből' (The bread is so fresh, as if they had just taken it out of the oven). Adding particles like 'csak' or 'éppen' intensifies the freshness and immediacy of the sensation.",
                "table_title": "Comparative Structures with mintha",
                "table_rows": [
                    ["mintha ... lenne (present cond.)", "Úgy olvad a nyelven, mintha hópehely lenne. (Melts as if it were a snowflake.)"],
                    ["mintha ... vették volna ki (past cond.)", "Olyan forró a cipó, mintha most vették volna ki a sütőből. (As if just removed.)"],
                    ["olyan az illata, mintha ...", "Olyan az illata, mintha nagymamám konyhájában ülnénk. (Smells as if we were sitting in grandma's kitchen.)"],
                    ["mintha csak tegnap történt volna", "Az íz felidézi a gyerekkoromat, mintha tegnap lett volna. (As if it were yesterday.)"],
                ],
                "examples": [
                    {
                        "spanish": "A frissen sült kalács illata betöltötte a házat, mintha ünnepnapra ébredtünk volna.",
                        "english": "The aroma of freshly baked challah filled the house, as if we had awakened to a feast day.",
                    },
                    {
                        "spanish": "A libamájkrém olyan selymesen simult a kenyérre, mintha lágy tejszínhab volna.",
                        "english": "The goose liver pâté smoothed so silky onto the bread, as if it were soft whipped cream.",
                    },
                    {
                        "spanish": "Az első korty bor után úgy érezte, mintha a napfényes villányi domboldalon sétálna.",
                        "english": "After the first sip of wine, he felt as if he were strolling on the sunny slopes of Villány.",
                    },
                    {
                        "spanish": "A leves íze oly meghitt volt, mintha a szülői ház vasárnapi asztalához tért volna vissza.",
                        "english": "The soup's taste was so intimate, as if he had returned to the Sunday table of his childhood home.",
                    },
                ],
                "tip": "Always ensure the verb following 'mintha' is conjugated in the conditional (-na/-ne/-ná/-né in the present, or past participle + volna in the past). Using the indicative mood after 'mintha' in sensory descriptions sounds jarring and uneducated.",
            },
            "words": [
                {"lemma": "mintha", "translation": "as if / as though", "pos": "conjunction"},
                {"lemma": "ízlelőbimbó", "translation": "taste bud", "pos": "noun"},
                {"lemma": "illatfelhő", "translation": "cloud of aroma / fragrant cloud", "pos": "noun"},
                {"lemma": "felidéz", "translation": "to evoke / conjure up", "pos": "verb"},
                {"lemma": "érzéki csalódás", "translation": "sensory illusion", "pos": "expression"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which conjunction introduces hypothetical comparisons in Hungarian?",
                        ["mintha", "minthogy", "holott"],
                        0,
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the anatomical term for taste receptor structures on the tongue?",
                        ["ízlelőbimbó", "illatfelhő", "érzéki csalódás"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["mintha", "as if / as though"],
                            ["ízlelőbimbó", "taste bud"],
                            ["illatfelhő", "cloud of aroma"],
                            ["felidéz", "to evoke / conjure up"],
                            ["érzéki csalódás", "sensory illusion"],
                        ],
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which verb form correctly completes 'Olyan ropogós a kenyérhéj, mintha csak most ____ ki a kemencéből'?",
                        ["vették volna", "veszik", "vegyék"],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the correct sentence expressing a simultaneous sensory comparison:",
                        [
                            "A krém olyan lágy, mintha selyem lenne a nyelvemen.",
                            "A krém olyan lágy, mintha selyem van a nyelvemen.",
                            "A krém olyan lágy, mintha selyem volt a nyelvemen.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A forró fűszerek illata úgy lebegett a konyhában, ____ egy keleti bazárban sétáltunk volna. (as if)",
                        "mintha",
                        "The aroma of hot spices floated in the kitchen as if we had been strolling in an oriental bazaar.",
                        ["b2-resultative-similes"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A rétes tésztája olyan vékonyra sikerült, mintha szellő ____ azt. (had blown it)",
                        "fújta volna",
                        "The strudel pastry turned out so thin, as if a breeze had blown it.",
                        ["b2-resultative-similes"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Olyan", "az", "étel", "íze,", "mintha", "a", "nagymamám", "főzte", "volna."],
                        ["Olyan", "az", "étel", "íze,", "mintha", "a", "nagymamám", "főzte", "volna."],
                        "The food's taste is as if my grandmother had cooked it.",
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A friss mézeskalács illata azonnal ____ a gyermekkorom legszebb karácsonyi emlékeit. (evoked)",
                        "felidézte",
                        "The aroma of fresh gingerbread immediately evoked the fondest Christmas memories of my childhood.",
                        ["b2-31-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "sűrű", "illatfelhő", "azonnal", "elárasztotta", "az", "egész", "kocsmát."],
                        ["A", "sűrű", "illatfelhő", "azonnal", "elárasztotta", "az", "egész", "kocsmát."],
                        "The thick cloud of aroma immediately flooded the entire tavern.",
                        ["b2-31-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Étteremkritikus", "text": "Hogyan jellemezné ezt a különleges somlói galuskát?"},
                            {"speaker": "Gasztronómus", "text": "____"},
                        ],
                        [
                            "A csokoládéöntet és a dió harmóniája olyan tökéletes, mintha egy bécsi cukrászda műhelyében készítették volna.",
                            "Minden falat rágós, mintha köveket ennék a kavicsos udvaron.",
                            "A galuska egyáltalán nem édes, mert sót tettek a vaníliakrém helyett.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vendég", "text": "Miért van ilyen bódító illat ebben az öreg pincében?"},
                            {"speaker": "Borász", "text": "____"},
                        ],
                        [
                            "A tölgyfahordókban érlelődő aszú párolgása miatt olyan az illatfelhő, mintha sárgabaracklekvár főne a sparhelten.",
                            "Csak azért, mert nyitva hagytuk az ablakot az autópálya felé.",
                            "A boroshordókban ecet van, amit most öntöttünk ki a kútba.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'mintha' with the past conditional to describe the nostalgic taste of an authentic dish.",
                                "answer": "A füstölt kolbász és a friss parasztkenyér íze olyan nosztalgiát ébresztett bennem, mintha újra a falusi nagyszüleim konyhájában ültem volna.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'ízlelőbimbó' and a sensory comparison.",
                                "answer": "A pikáns fűszerezés úgy stimulálta az ízlelőbimbóimat, mintha apró szikrák pattogtak volna a nyelvemen.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A finom vadhús úgy szétomlott a szájban, mintha vajból ____ volna. (had been made)",
                        "készült",
                        "The delicate venison melted away in the mouth as if it had been made of butter.",
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which word describes the sensory stimulation that conjures past memories?",
                        ["felidéz", "elrejt", "megszüntet"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "Flavors, Aromas, and Sensory Memory",
            "grammar_label": "Describing gastronomic textures, aromas, and nostalgic gustatory experiences",
            "goals": [
                "I can describe complex gastronomic textures including omlós, selymes, and ropogós",
                "I can characterize aroma profiles and subtle aftertastes (utóíz, fanyar, zamatos)",
                "I can express nostalgic emotional connections triggered by gustatory sensory memory",
            ],
            "grammar_doc": {
                "slug": "gastronomic-textures-sensory-memory",
                "title": "Gastronomic Textures, Aromas, and Gustatory Memory",
                "text1_title": "Nuanced Adjectives for Food Textures and Flavors",
                "text1": "At the B2 level, describing food transcends simple evaluative terms like 'finom' or 'rossz'. Hungarian possesses a vivid descriptive vocabulary for textures and sensations: 'omlós' (tender, melting in the mouth, used for braised meats and crumbly pastries), 'selymes' (silky, smooth, used for emulsions and velvety soups), 'zamatos' (succulent, full-flavored, juicy), and 'fanyar' (astringent, pleasantly tart, typical of dry wines and certain wild berries).",
                "text2_title": "Describing the Temporal Progression of Tastes",
                "text2": "Gastronomic analysis pays close attention to the chronology of tasting: the initial impression (első benyomás / indítás), the core body (ízvilág / testesség), and the lingering finish (utóíz / lecsengés). A complex wine or mature cheese may start with fruity notes and end with a long, pleasantly bitter or mineral aftertaste ('hosszú, fanyar utóíz').",
                "table_title": "Key Flavor and Texture Descriptors",
                "table_rows": [
                    ["omlós", "A lassan sült marhapofa rendkívül omlós maradt. (Tender / melting.)"],
                    ["fanyar", "A feketeribizli fanyar íze jól illik a vadhúsokhoz. (Tart / astringent.)"],
                    ["zamatos", "A nyári szegedi őszibarack bámulatosan zamatos. (Succulent / juicy.)"],
                    ["utóíz", "A csokoládénak hosszan tartó, nemes utóíze van. (Pleasant aftertaste.)"],
                ],
                "examples": [
                    {
                        "spanish": "A mangalica tarja olyan omlósra sült, hogy alig kellett kést használni a felvágásához.",
                        "english": "The mangalica pork collar was roasted so tender that one hardly needed a knife to slice it.",
                    },
                    {
                        "spanish": "A tokaji furmint fanyar mineralitása tökéletesen kiegészíti a füstölt pisztráng gazdag zamatát.",
                        "english": "The tart minerality of the Tokaj Furmint perfectly complements the rich flavor of the smoked trout.",
                    },
                    {
                        "spanish": "A hagyományos magyar konyha ízvilága a paprika, a hagyma és a zsír ősi hármasára épül.",
                        "english": "The flavor profile of traditional Hungarian cuisine is built on the ancient triad of paprika, onion, and lard.",
                    },
                    {
                        "spanish": "A kávé kortyolása után kellemes pörkölt mogyorós utóíz maradt a szánkban.",
                        "english": "After sipping the coffee, a pleasant roasted hazelnut aftertaste remained in our mouth.",
                    },
                ],
                "tip": "Distinguish between 'savanyú' (plain sour, potentially unpleasant like spoiled milk) and 'fanyar' (astringent/tart, a sophisticated, desirable dry quality found in cranberries, quince, and tannins).",
            },
            "words": [
                {"lemma": "zamatos", "translation": "flavorful / succulent / juicy", "pos": "adjective"},
                {"lemma": "omlós", "translation": "tender / melt-in-the-mouth", "pos": "adjective"},
                {"lemma": "fanyar", "translation": "tart / astringent", "pos": "adjective"},
                {"lemma": "utóíz", "translation": "aftertaste", "pos": "noun"},
                {"lemma": "ízvilág", "translation": "flavor profile / culinary realm", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective describes meat that is so tender it literally melts in the mouth?",
                        ["omlós", "rágós", "kemény"],
                        0,
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'fanyar' describe in gastronomic sensory terminology?",
                        [
                            "pleasantly dry, tart, or astringent taste such as in cranberries or dry wine tannins",
                            "excessively sugary and cloying like cheap syrup",
                            "completely burnt and charcoal-flavored",
                        ],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["zamatos", "flavorful / succulent"],
                            ["omlós", "tender / melting"],
                            ["fanyar", "tart / astringent"],
                            ["utóíz", "aftertaste"],
                            ["ízvilág", "flavor profile"],
                        ],
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which resultative phrase correctly describes braising the duck until tender?",
                        [
                            "A kacsát omlósra párolta a séf.",
                            "A kacsát omlósan párolta a séf.",
                            "A kacsát omlóssal párolta a séf.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Complete the comparison: 'A desszert olyan selymes volt, mintha tejszín____'.",
                        ["volna", "lett", "lenne volna"],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A vadhúst addig párolták a vörösborban, amíg teljesen ____ nem puhult. (tender)",
                        "omlósra",
                        "They braised the venison in red wine until it softened completely tender.",
                        ["b2-resultative-similes"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A somlói galuska csokoládéöntete olyan gazdag volt, mintha tiszta kakaóbabból ____ volna. (had been brewed)",
                        "főzték",
                        "The chocolate sauce of the Somló sponge was so rich, as if it had been brewed from pure cacao beans.",
                        ["b2-resultative-similes"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "hosszú", "érlelés", "után", "a", "sajt", "íze", "különösen", "zamatos", "lett."],
                        ["A", "hosszú", "érlelés", "után", "a", "sajt", "íze", "különösen", "zamatos", "lett."],
                        "After the long aging, the taste of the cheese became exceptionally flavorful.",
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A prémium minőségű étcsokoládé elfogyasztása után hosszan tartó, kellemesen ____ íz maradt a szájban. (aftertaste)",
                        "utóíz",
                        "After consuming the premium dark chocolate, a long-lasting, pleasant aftertaste remained in the mouth.",
                        ["b2-31-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "magyar", "borkultúra", "egyedülálló", "ízvilágot", "képvisel", "Közép-Európában."],
                        ["A", "magyar", "borkultúra", "egyedülálló", "ízvilágot", "képvisel", "Közép-Európában."],
                        "Hungarian wine culture represents a unique flavor profile in Central Europe.",
                        ["b2-31-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Sommelier", "text": "Milyen jegyeket érez ki ebből az egri bikavérből a kóstolás során?"},
                            {"speaker": "Borkedvelő vendég", "text": "____"},
                        ],
                        [
                            "Kifejezetten zamatos szilvás aromákkal nyit, majd a korty végén kellemesen fanyar tölgyfás utóíz bontakozik ki.",
                            "A bor teljesen íztelen, mintha desztillált csapvizet töltene a poharamba.",
                            "Kizárólag ecetszagot érzek, mert a palackot harminc éve a napon felejtették.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vendég", "text": "Hogyan készítették el ezt a marhapofát, hogy ennyire vajpuha maradt?"},
                            {"speaker": "Főpincér", "text": "____"},
                        ],
                        [
                            "Tizenkét órán át sous-vide eljárással puhára pároltuk alacsony hőfokon, így őrizte meg omlós textúráját.",
                            "Nyersen hagytuk a fagyasztóban három hétig, majd hidegen tálaltuk.",
                            "Mikrohullámú sütőben melegítettük két másodpercig.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'omlós' and 'zamatos' to describe a meat dish.",
                                "answer": "A lassan sült báránycsülök kívül ropogósra pirult, belül pedig csodálatosan omlós és zamatos maradt.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence describing a wine's finish using 'fanyar' and 'utóíz'.",
                                "answer": "A száraz vörösbor kortyolását hosszan lecsengő, nemesen fanyar utóíz követte, amely harmonizált a vadhússal.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A séf a tésztát pirosra sütötte, a köretet pedig sűrűre ____ a hús mellé. (reduced / cooked)",
                        "főzte",
                        "The chef baked the pastry until golden red and reduced the sauce thick beside the meat.",
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the comprehensive sensory profile and character of a cuisine?",
                        ["ízvilág", "teríték", "étlap"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Hospitality, Etiquette, and the Ritual of the Meal",
            "grammar_label": "Social table manners, host-guest obligations, and toast etiquette",
            "goals": [
                "I can formulate polite formal toasts and expressions of hospitality (pohárköszöntő)",
                "I can describe Hungarian dining etiquette, seating rules, and host-guest customs",
                "I can use appropriate formal modals and resultative expressions in social dining contexts",
            ],
            "grammar_doc": {
                "slug": "hospitality-table-etiquette-toasts",
                "title": "Hungarian Hospitality, Dining Etiquette, and Toasts",
                "text1_title": "The Ritual and Ethics of Hungarian Hospitality",
                "text1": "Hungarian hospitality (vendéglátás) carries a profound cultural heritage where generosity and decorum are paramount. Offering food and drink to an arriving guest is an obligation; refusing the first offering flatly can be seen as impolite. Formal meals follow strict etiquette (asztali illem): the host indicates when to start, soup is traditionally the compulsory opening course of a ceremonial meal, and bread holds almost sacred symbolic respect.",
                "text2_title": "The Art of the Pohárköszöntő and Clinking Traditions",
                "text2": "At formal gatherings, banquets, and family celebrations, a designated host or honored guest delivers a toast ('pohárköszöntőt mond'). Unlike informal drinking, a formal toast requires rising, holding the glass at chest height, making eye contact, and expressing sincere wishes for health, prosperity, or remembrance. A famous historical custom: after the defeat of the 1848 revolution, Hungarians pledged not to clink beer glasses ('sörrel nem koccintunk') for 150 years; wine and pálinka clinking, however, is customary with direct eye contact ('Egészségedre!').",
                "table_title": "Key Etiquette and Hospitality Expressions",
                "table_rows": [
                    ["pohárköszöntőt mond", "A házigazda megható pohárköszöntőt mondott a jubileum alkalmából. (Gave a toast.)"],
                    ["illendő", "Illendő megvárni, míg a házigazda felemeli a poharát. (It is polite/proper.)"],
                    ["koccint (+ -val/-vel)", "Szemkontaktust tartva koccintottak a vendégekkel. (Clinked glasses.)"],
                    ["teríték", "A díszes teríték része volt az ezüst étkészlet és a kristálypohár. (Table setting.)"],
                ],
                "examples": [
                    {
                        "spanish": "A házigazda szívélyes vendéglátással fogadta a távolról érkezett rokonokat.",
                        "english": "The host welcomed the relatives who arrived from afar with cordial hospitality.",
                    },
                    {
                        "spanish": "Nem illendő elkezdeni az étkezést, amíg az asztaltársaság minden tagja nem kapta meg a tányérját.",
                        "english": "It is not polite to start eating until every member of the table party has received their plate.",
                    },
                    {
                        "spanish": "A díszvacsora kezdetén a dékán ünnepélyes pohárköszöntőben méltatta az elért eredményeket.",
                        "english": "At the beginning of the gala dinner, the dean praised the achievements in a solemn toast.",
                    },
                    {
                        "spanish": "A vendégek borral koccintottak az ifjú pár boldogságára a lakodalomban.",
                        "english": "The guests toasted with wine to the happiness of the newlyweds at the wedding.",
                    },
                ],
                "tip": "Remember: in Hungarian table culture, wishing 'Jó étvágyat!' before eating is standard and expected, but replying 'Köszönöm, viszont kívánom!' is equally necessary.",
            },
            "words": [
                {"lemma": "pohárköszöntő", "translation": "toast / dinner speech", "pos": "noun"},
                {"lemma": "vendéglátás", "translation": "hospitality / catering", "pos": "noun"},
                {"lemma": "illendő", "translation": "proper / polite / decorous", "pos": "adjective"},
                {"lemma": "koccint", "translation": "to clink glasses / toast", "pos": "verb"},
                {"lemma": "teríték", "translation": "table setting / place setting", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'pohárköszöntő' in formal social gatherings?",
                        [
                            "a formal speech or toast delivered before or during a ceremonial meal",
                            "a special discount voucher given at the entrance of a restaurant",
                            "a machine used for washing fine wine glasses in kitchens",
                        ],
                        0,
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective means socially appropriate, decorous, or polite?",
                        ["illendő", "illetéktelen", "ellenséges"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["pohárköszöntő", "toast / dinner speech"],
                            ["vendéglátás", "hospitality"],
                            ["illendő", "proper / polite"],
                            ["koccint", "to clink glasses"],
                            ["teríték", "table setting"],
                        ],
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence correctly expresses table etiquette with a resultative phrase?",
                        [
                            "A pék aranybarnára sütötte a friss kenyeret a díszes teríték mellé.",
                            "A pék aranybarnán sütötte a friss kenyeret a teríték mellé.",
                            "A pék aranybarnával sütötte a friss kenyeret a teríték mellé.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which verb form completes the sensory memory comparison: 'Úgy éreztük magunkat a vendégségben, mintha otthon ____'?",
                        ["lennénk", "voltunk", "leszünk"],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A házigazda poharat emelt, és a vendégek egészségére ____ a finom tokaji borral. (clinked glasses)",
                        "koccintott",
                        "The host raised a glass and toasted with the fine Tokaj wine to the health of the guests.",
                        ["b2-resultative-similes"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A díszvacsora előtt a pincérek makulátlanul tisztára csiszolták a poharakat, és pompásra ____ a terítéket. (arranged / set)",
                        "készítették",
                        "Before the gala dinner, the waiters polished the glasses spotless and set the table setting magnificently.",
                        ["b2-resultative-similes"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "díszvacsorán", "nem", "illendő", "a", "házigazda", "előtt", "felállni", "az", "asztaltól."],
                        ["A", "díszvacsorán", "nem", "illendő", "a", "házigazda", "előtt", "felállni", "az", "asztaltól."],
                        "At a gala dinner it is not polite to stand up from the table before the host.",
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A magyar vidéki ____ híres a bőséges adagokról és a szívélyes fogadtatásról. (hospitality)",
                        "vendéglátás",
                        "Hungarian rural hospitality is famous for generous portions and cordial reception.",
                        ["b2-31-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "családfő", "rövid", "pohárköszöntőt", "mondott", "a", "fiatalok", "tiszteletére."],
                        ["A", "családfő", "rövid", "pohárköszöntőt", "mondott", "a", "fiatalok", "tiszteletére."],
                        "The head of the family gave a brief toast in honor of the young couple.",
                        ["b2-31-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Külföldi diplomata", "text": "Milyen szabályokra kell ügyelnem egy hivatalos magyar vacsorán koccintáskor?"},
                            {"speaker": "Protokollfőnök", "text": "____"},
                        ],
                        [
                            "Mindig nézzen a másik fél szemébe, emelje meg a poharát, és mondja tisztán, hogy 'Egészségére!'.",
                            "Tilos ránézni a partnerre, és a bort azonnal ki kell önteni a szőnyegre.",
                            "Magyarországon csak sörrel szabad koccintani a protokoll szerint.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Házigazda", "text": "Parancsol még egy adag töltött káposztát? Kifejezetten a kedvéért készítettük!"},
                            {"speaker": "Vendég", "text": "____"},
                        ],
                        [
                            "Nagyon köszönöm a szívélyes vendéglátást, igazán fenséges volt, de sajnos már egyetlen falat sem férne belém.",
                            "Utálom a káposztát, miért nem rendelt inkább pizzát?",
                            "A vendéglátás tilos a törvény szerint, kérem hívja a rendőrséget.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a short formal toast ('pohárköszöntő') using 'koccint' and 'egészségére'.",
                                "answer": "Hölgyeim és Uraim, engedjék meg, hogy poharamat emeljem közös sikereinkre; koccintsunk mindannyiunk egészségére és a jövőbeli együttműködésre!",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'illendő' regarding table manners.",
                                "answer": "Hivatalos fogadásokon illendő megvárni, amíg az idős vendégek és a hölgyek helyet foglalnak az asztalnál.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A lakodalomban a vőfély olyan hangosan kiáltott, ____ a falu túlsó végén is meghallották volna. (as if)",
                        "mintha",
                        "At the wedding the best man shouted so loudly as if they would have heard it at the far end of the village.",
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "What is the term for the arrangement of plates, cutlery, and glasses for one diner?",
                        ["teríték", "étlap", "szervizdíj"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Food Writing and Restaurant Criticism",
            "grammar_label": "Writing an analytical gastronomic review (étteremkritika, textúra, ár-érték arány, szerviz)",
            "goals": [
                "I can write an analytical restaurant review evaluating culinary balance, ambience, and service",
                "I can critique culinary execution with nuanced stylistic and resultative terminology",
                "I can assess value for money (ár-érték arány) and overall conceptual coherence in dining",
            ],
            "grammar_doc": {
                "slug": "restaurant-criticism-food-writing",
                "title": "Gastronomic Journalism: Writing an Étteremkritika",
                "text1_title": "The Structure of an Analytical Restaurant Review",
                "text1": "Gastronomic journalism (gasztroújságírás) requires combining vivid sensory prose with objective critical standards. A well-constructed 'étteremkritika' evaluates four core pillars: the interior concept and atmosphere (hangulat / enteriőr), the attentiveness of service (szerviz / kiszolgálás), the technical execution and flavor harmony of individual courses (fogások / konyhatechnológia), and the final value-for-money verdict (ár-érték arány).",
                "text2_title": "Nuanced Critical Vocabulary: Between Praise and Restraint",
                "text2": "B2 food writing avoids hyperbolic clichés like 'szuper' or 'nagyon jó'. Instead, it uses precise evaluative terms: 'kifogástalan' (flawless, impeccable), 'kiegyensúlyozott' (balanced), 'túlgondolt' (over-conceived / trying too hard), 'félresikerült' (misguided / botched), and 'kulináris élmény' (culinary experience). Resultative sublative structures ('ropogósra sült', 'túlságosan sűrűre főzött') articulate exact technical successes or shortcomings.",
                "table_title": "Critical Review Assessment Vocabulary",
                "table_rows": [
                    ["kifogástalan", "A desszert tálalása és ízharmóniája egyszerűen kifogástalan volt. (Flawless.)"],
                    ["ár-érték arány", "Az étterem ár-érték aránya a belvárosban kifejezetten kedvező. (Value for money.)"],
                    ["kulináris élmény", "A kóstolómenü emlékezetes kulináris élményt nyújtott. (Culinary experience.)"],
                    ["fogás", "A hétfogásos degusztációs menü minden tétele meglepetést rejtett. (Course / dish.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az étteremkritika szerzője dicsérte az omlósra párolt marhát, de kifogásolta a lassú szervizt.",
                        "english": "The author of the restaurant review praised the beef braised tender, but criticized the slow service.",
                    },
                    {
                        "spanish": "A pincérek figyelmessége és szakmai felkészültsége az egész este folyamán kifogástalan maradt.",
                        "english": "The attentiveness and professional expertise of the waitstaff remained flawless throughout the evening.",
                    },
                    {
                        "spanish": "A magas árak ellenére a kimagasló minőség miatt az ár-érték arány teljesen indokolt.",
                        "english": "Despite the high prices, the value for money is completely justified due to the outstanding quality.",
                    },
                    {
                        "spanish": "A vacsora harmadik fogása, a füstölt pisztránghab igazi kulináris remekműnek bizonyult.",
                        "english": "The third course of the dinner, the smoked trout mousse, proved to be a true culinary masterpiece.",
                    },
                ],
                "tip": "In professional restaurant reviews, balance praise with constructive criticism. Even an outstanding meal rarely receives uncritical adoration; noting a slightly oversalted jus or a stiff bread roll demonstrates critical authority.",
            },
            "words": [
                {"lemma": "étteremkritika", "translation": "restaurant review / critique", "pos": "noun"},
                {"lemma": "kifogástalan", "translation": "impeccable / flawless", "pos": "adjective"},
                {"lemma": "ár-érték arány", "translation": "value for money / price-performance ratio", "pos": "expression"},
                {"lemma": "kulináris", "translation": "culinary", "pos": "adjective"},
                {"lemma": "fogás", "translation": "course / dish", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is the focus of an 'étteremkritika' in food journalism?",
                        [
                            "an analytical review evaluating food quality, service, and dining ambience",
                            "a municipal health inspection document that shuts down illegal kitchens",
                            "a simple grocery list written by the restaurant's purchasing manager",
                        ],
                        0,
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective means absolutely flawless, without any shortcomings?",
                        ["kifogástalan", "kifogásolható", "középszerű"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["étteremkritika", "restaurant review"],
                            ["kifogástalan", "impeccable / flawless"],
                            ["ár-érték arány", "value for money"],
                            ["kulináris", "culinary"],
                            ["fogás", "course / dish"],
                        ],
                        ["b2-31-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence uses a resultative sublative phrase appropriately in food criticism?",
                        [
                            "A séf a tőkehalat omlósra párolta, míg a zöldségeket ropogósra pirította.",
                            "A séf a tőkehalat omlósan párolt, míg a zöldségeket ropogósan pirított.",
                            "A séf a tőkehalat omlósból párolta a serpenyőbe.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Complete the simile: 'A leves olyan tiszta volt, mintha forrásvízből ____ volna'.",
                        ["szűrték", "szűrtek", "szűrni"],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A degusztációs menü minden egyes fogása úgy volt felépítve, ____ egy zenei szimfóniát hallgatnánk. (as if)",
                        "mintha",
                        "Every single course of the tasting menu was constructed as if we were listening to a musical symphony.",
                        ["b2-resultative-similes"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A desszertet alkotó csokoládégömböt aranybarnára ____ a mestercukrász. (baked / browned)",
                        "sütötte",
                        "The master pastry chef baked the chocolate sphere forming the dessert until golden brown.",
                        ["b2-resultative-similes"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "fogás", "ízharmóniája", "olyan", "tökéletes", "volt,", "mintha", "festmény", "lenne."],
                        ["A", "fogás", "ízharmóniája", "olyan", "tökéletes", "volt,", "mintha", "festmény", "lenne."],
                        "The flavor harmony of the course was so perfect, as if it were a painting.",
                        ["b2-resultative-similes"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A belvárosi bisztróban a figyelmes szerviz és a friss alapanyagok miatt az ____ kifejezetten kedvező. (value for money)",
                        "ár-érték arány",
                        "In the downtown bistro, due to attentive service and fresh ingredients, the value for money is exceptionally favorable.",
                        ["b2-31-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "szakíró", "részletes", "étteremkritikát", "publikált", "a", "gasztronómiai", "magazinban."],
                        ["A", "szakíró", "részletes", "étteremkritikát", "publikált", "a", "gasztronómiai", "magazinban."],
                        "The culinary writer published a detailed restaurant review in the gastronomic magazine.",
                        ["b2-31-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Főszerkesztő", "text": "Hogyan ítéled meg az új Michelin-csillagos étterem kóstolómenüjét a készülő kritikában?"},
                            {"speaker": "Gasztronómiai kritikus", "text": "____"},
                        ],
                        [
                            "A konyhatechnológia kifogástalan, a textúrák játéka lenyűgöző, bár az utolsó fogás talán kissé túlgondolt volt.",
                            "Minden étel ehetetlen volt, mert sós tengervízben mosták el a tányérokat.",
                            "Az étterem valójában egy garázs, ahol nem árulnak semmilyen ételt.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Vendég", "text": "Megéri kipróbálni az öt fogásos degusztációs vacsorát a hétvégén?"},
                            {"speaker": "Ínyenc barát", "text": "____"},
                        ],
                        [
                            "Feltétlenül! Az ár-érték arány ritka jó ebben a kategóriában, és igazi kulináris utazást kapsz a pénzedért.",
                            "Semmiképp, mert a pincérek megtagadják a vendégek kiszolgálását.",
                            "Csak akkor éri meg, ha otthonról viszel magaddal rántott húst a zsebedben.",
                        ],
                        0,
                        ["b2-resultative-similes"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a critical evaluation sentence praising an entrée using 'kifogástalan' and a resultative sublative phrase.",
                                "answer": "A ropogósra sült kacsacomb és a selymesre pürésített zellerkrém párosítása egyszerűen kifogástalan kulináris élményt nyújtott.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a concluding assessment in an 'étteremkritika' evaluating 'ár-érték arány'.",
                                "answer": "Bár az árszínvonal a prémium kategóriába tartozik, a hibátlan alapanyagok és a professzionális szerviz révén az ár-érték arány teljes mértékben meggyőző.",
                            }
                        ],
                        ["b2-resultative-similes"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A pincér olyan eleganciával szervírozta a bort, ____ a királyi udvarban szolgált volna. (as if)",
                        "mintha",
                        "The waiter served the wine with such elegance as if he had been serving in the royal court.",
                        ["b2-resultative-similes"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which phrase denotes the ratio between financial cost and received gastronomic quality?",
                        ["ár-érték arány", "haszonkulcs", "borravaló"],
                        0,
                        ["b2-31-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can confidently apply resultative sublative phrases (-ra/-re) in culinary and transformation contexts",
            "I can formulate nuanced hypothetical sensory comparisons using mintha and conditional verb forms",
            "I can synthesize gastronomic vocabulary to critique dining experiences, textures, and etiquette",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["ropogósra pirít", "to toast / fry until crispy"],
                    ["puhára párol", "to braise until tender"],
                    ["omlós", "tender / melting"],
                    ["pohárköszöntő", "toast / dinner speech"],
                    ["kifogástalan", "impeccable / flawless"],
                ],
                ["b2-31-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'fanyar' signify in tasting notes for Hungarian wines or fruits?",
                [
                    "a pleasantly dry, astringent, tannic sensation that cleanses the palate",
                    "an overly sweet, syrupy and cloying taste profile",
                    "a completely spoiled and vinegar-like acidity",
                ],
                0,
                ["b2-31-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly illustrates both a resultative sublative phrase and a hypothetical simile?",
                [
                    "A pék pirosra sütötte a kenyeret, amely olyan illatos volt, mintha most vették volna ki a kemencéből.",
                    "A pék pirosan sütötte a kenyeret, amely olyan illatos volt, mintha most veszik ki a kemencéből.",
                    "A pék pirosról sütötte a kenyeret, amely olyan illatos volt, mintha most venni a kemencéből.",
                ],
                0,
                ["b2-resultative-similes"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A degusztációs vacsora végén a vendégek elégedettek voltak, mert a prémium minőség mellett az ____ is kedvező maradt. (value for money)",
                "ár-érték arány",
                "At the end of the tasting dinner the guests were satisfied because alongside premium quality the value for money also remained favorable.",
                ["b2-31-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A séf a zöldségeket vajon kíméletesen ____ párolta a sült hal mellé. (until tender)",
                "puhára",
                "The chef gently braised the vegetables tender in butter beside the roasted fish.",
                ["b2-resultative-similes"],
            ),
            fb(
                "grammar",
                "recall",
                "A forró fokhagymás pirítós íze olyan nosztalgiát ébresztett benne, ____ gyermekkorában ült volna a konyhában. (as if)",
                "mintha",
                "The taste of hot garlic toast aroused such nostalgia in him as if he had been sitting in the kitchen during his childhood.",
                ["b2-resultative-similes"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is the sublative (-ra/-re) used instead of an adverbial (-an/-en) in 'ropogósra pirítja'?",
                [
                    "Because it designates the resulting end state achieved by the cooking process rather than the ongoing manner of action.",
                    "Because in Hungarian all verbs of motion must take a sublative suffix.",
                    "Because 'ropogós' cannot take any other suffix according to vowel harmony rules.",
                ],
                0,
                ["b2-resultative-similes"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Irodalomtörténész", "text": "Hogyan ábrázolja Krúdy Gyula a gasztronómia és az emberi emlékezet kapcsolatát a Szindbád-történetekben?"},
                    {"speaker": "Egyetemi oktató", "text": "____"},
                ],
                [
                    "Az ízek, a forró húsleves és a velős csont rituáléja Prousthoz hasonlóan a letűnt idők, szerelmek és ifjúság érzéki felidézésének eszköze.",
                    "Krúdy kizárólag a kalóriaszámítással és a dietetikai előírásokkal foglalkozott a regényeiben.",
                    "Szindbád valójában megvetette a magyar konyhát, és kizárólag száraz kenyeret evett.",
                ],
                0,
                ["b2-resultative-similes"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where the resultative sublative phrase is applied with stylistic elegance:",
                [
                    "A vadast lassan sűrűre főzték, a zsemlegombócot pedig puhára gőzölték a tálalás előtt.",
                    "A vadast lassan sűrűn főzték, a zsemlegombócot pedig puhán gőzölték a tálalás előtt.",
                    "A vadast lassan sűrűig főzték, a zsemlegombócot pedig puháig gőzölték a tálalás előtt.",
                ],
                0,
                ["b2-resultative-similes"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "szakács", "aranysárgára", "pirította", "a", "finom", "vajas", "galuskát."],
                ["A", "szakács", "aranysárgára", "pirította", "a", "finom", "vajas", "galuskát."],
                "The cook toasted the fine butter dumplings golden yellow.",
                ["b2-resultative-similes"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "pincér", "olyan", "udvariasan", "szólt,", "mintha", "főúri", "kastélyban", "lennénk."],
                ["A", "pincér", "olyan", "udvariasan", "szólt,", "mintha", "főúri", "kastélyban", "lennénk."],
                "The waiter spoke so politely as if we were in an aristocratic manor.",
                ["b2-resultative-similes"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a compound sentence combining a resultative sublative phrase ('ropogósra süt / puhára párol') and a sensory comparison with 'mintha'.",
                        "answer": "A konyhafőnök omlósra párolta a marhapofát és ropogósra pirította a köretet; az ételek harmóniája oly gazdag volt, mintha egy királyi lakomán vettünk volna részt.",
                    }
                ],
                ["b2-resultative-similes"],
            ),
        ],
    },
}
