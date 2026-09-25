#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 7, 8, and 9:
  - Unit 7: b2-marslakok ("The 'Martians' of Budapest: Physics & Computing")
  - Unit 8: b2-semmelweis ("Semmelweis, Szent-Györgyi & Medical Pioneers")
  - Unit 9: b2-matematikasakk ("Non-Euclidean Worlds: Hungarian Mathematics & Chess")
"""
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
from b2_unit_builder_helper import build_culture_unit


# ============================================================================
# CULTURE UNIT 7: b2-marslakok
# ============================================================================
UNIT_7_MARSLAKOK = {
    "unit_num": 7,
    "slug": "marslakok",
    "title": "The 'Martians' of Budapest: Physics & Computing",
    "grammar_skill": "b2-proportional-correlatives",
    "vocab_skill": "b2-marslakok-vocab",
    "theme": "The Martians of Budapest: Physics and computing",
    "location": "Budapest, Göttingen, Princeton és Los Alamos",
    "combined_story_title": "A marslakók már itt vannak: Neumann, Szilárd és a 20. század",
    "combined_story_summary": "How a legendary generation of Budapest-born scientists—János Neumann, Leó Szilárd, Jenő Wigner, Ede Teller, and Tódor Kármán—shaped modern computer architecture, game theory, and nuclear physics.",
    "intro_body": [
        "Between 1881 and 1908, a single central European city—Budapest—produced a cluster of theoretical physicists, mathematicians, and engineers who permanently altered the trajectory of the twentieth century: Tódor Kármán, Leó Szilárd, Jenő Wigner, János Neumann (John von Neumann), and Ede Teller.",
        "In this unit, you will explore the intellectual origins, scientific breakthroughs, and moral dilemmas of the 'Martians' while mastering B2 proportional correlatives (minél ... annál ...) and formal conditional conjunctions (amennyiben, feltéve, hogy, abban az esetben, ha)."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "Who Were the 'Martians'?",
            "grammar_label": "Proportional correlatives: minél + comparative ..., annál + comparative ...",
            "goals": [
                "I can explain the origin of the 'Martians of Budapest' anecdote attributed to Enrico Fermi and Leó Szilárd.",
                "I can express proportional variation using minél + comparative ..., annál + comparative ....",
                "I can use B2 vocabulary related to theoretical physics, emigration, and scientific collaboration."
            ],
            "story_segment": {
                "seg_slug": "kikvoltakamarslakok",
                "title": "Kik voltak a marslakók?",
                "summary": "At Los Alamos, when Enrico Fermi asked where extraterrestrial civilizations were hiding, Leó Szilárd dryly replied that they were already among us—they just called themselves Hungarians.",
                "location": "Los Alamos és Budapest",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század közepén az amerikai kutatóintézetek folyosóin különös legenda terjedt el. Amikor Enrico Fermi, a Nobel-díjas olasz fizikus egy ebéd közben felvetette a híres kérdést, hogy amennyiben a világegyetem tele van lakható bolygókkal, mégis hol vannak a földönkívüliek, Szilárd Leó huncut mosollyal azonnal válaszolt. Szerinte a földönkívüliek már rég itt élnek közöttünk, csakhogy óvatosságból magyaroknak nevezik magukat."
                    },
                    {
                        "type": "narration",
                        "text": "A tréfás elnevezés — a „marslakók” — nem volt teljesen alaptalan. Az amerikai kollégák számára valóban megmagyarázhatatlannak tűnt, miként lehetséges, hogy Közép-Európa egyetlen városa, Budapest néhány évtized alatt olyan zseniket adott a világnak, mint Kármán Tódor, Szilárd Leó, Wigner Jenő, Neumann János és Teller Ede. Minél mélyebben vizsgálták a modern fizika és a számítástechnika alapjait, annál gyakrabban bukkantak budapesti születésű tudósok nevére."
                    },
                    {
                        "type": "narration",
                        "text": "Ezeket a kutatókat számos közös vonás kötötte össze. Mindannyian a századforduló polgári Budapestjén nőttek fel, kiváló gimnáziumokba jártak, majd a húszas években Németország — elsősorban Berlin és Göttingen — egyetemein csiszolták tovább tudásukat. Amikor azonban Európában megerősödött a fasizmus és az antiszemitizmus, egymás után kényszerültek elhagyni a kontinenst."
                    },
                    {
                        "type": "narration",
                        "text": "Az Egyesült Államokban is megőrizték jellegzetes, erősen hangsúlyos angol kiejtésüket és szokatlan gondolkodásmódjukat. A princetoni és los alamosi laboratóriumokban gyakran váltottak át anyanyelvükre a táblák előtt, amit a kívülállók úgy hallgattak, mintha egy távoli bolygó titkos kódnyelvét beszélnék. Minél összetettebbé vált egy elméleti probléma, annál gyorsabban záporoztak közöttük a magyar szavak."
                    },
                    {
                        "type": "narration",
                        "text": "A „marslakók” azonban nem pusztán különc elméleti tudósok voltak. Mindannyian élesen érzékelték a történelmi veszélyeket: pontosan tudták, hogy amennyiben a totális diktatúrák jutnak először új típusú fegyverekhez, a szabad világ léte kerülhet veszélybe."
                    }
                ]
            },
            "words": [
                {"lemma": "földönkívüli", "translation": "extraterrestrial / alien", "pos": "noun"},
                {"lemma": "kutatóintézet", "translation": "research institute", "pos": "noun"},
                {"lemma": "kivándorlás", "translation": "emigration", "pos": "noun"},
                {"lemma": "elméleti fizika", "translation": "theoretical physics", "pos": "noun"},
                {"lemma": "minél ... annál ...", "translation": "the more ... the more ...", "pos": "expression"},
                {"lemma": "különc", "translation": "eccentric / unconventional person", "pos": "adjective"}
            ],
            "grammar_doc": {
                "slug": "proportional-correlatives-minel-annal",
                "title": "Proportional Correlatives: minél ... annál ...",
                "text1_title": "Building Proportional Relationships",
                "text1": "To express how one process or quality changes in direct proportion to another ('the more ..., the more ...'), Hungarian pairs the relative pronoun form minél ('by how much') in the subordinate clause with the demonstrative correlative annál ('by that much') in the main clause. Both words MUST be immediately followed by a comparative adjective or adverb (-bb / -ban / -ben).",
                "text2_title": "Word Order and Preverb Behavior",
                "text2": "Because minél + [comparative] and annál + [comparative] occupy the focus position of their respective clauses, any separable verbal prefix (preverb) in either clause must invert and stand AFTER the finite verb (e.g., Minél tovább kutatták a kérdést, annál több összefüggést fedeztek fel).",
                "table_title": "Proportional Correlative Patterns",
                "table_rows": [
                    ["Minél mélyebben vizsgálták a problémát, annál több kérdés merült fel.", "The more deeply they examined the problem, the more questions arose."],
                    ["Minél összetettebb a feladat, annál fontosabb az együttműködés.", "The more complex the task is, the more important collaboration becomes."],
                    ["Minél korábban felismerték a veszélyt, annál gyorsabban cselekedtek.", "The earlier they recognized the danger, the faster they acted."]
                ],
                "examples": [
                    {
                        "spanish": "Minél mélyebben vizsgálták a modern fizika alapjait, annál gyakrabban bukkantak budapesti tudósok nevére.",
                        "english": "The more deeply they examined the foundations of modern physics, the more frequently they came across the names of Budapest scientists."
                    },
                    {
                        "spanish": "Minél bonyolultabbá vált egy egyenlet, annál szívesebben váltottak át magyar nyelvre.",
                        "english": "The more complicated an equation became, the more gladly they switched to Hungarian."
                    },
                    {
                        "spanish": "Minél súlyosabbnak látták az európai helyzetet, annál sürgősebbnek tartották az amerikai kutatásokat.",
                        "english": "The graver they saw the European situation to be, the more urgent they considered American research."
                    }
                ],
                "tip": "Never use the base (positive) degree after minél or annál! Write Minél gyorsabban dolgoztak, annál jobb eredményt értek el (not *Minél gyorsan ... annál jó ...)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'elméleti fizika' kifejezés a tudományos életben?",
                    "options": [
                        "A fizikának azt az ágát, amely matematikai modellekkel és elméleti törvényszerűségekkel írja le a természet jelenségeit.",
                        "Kizárólag ipari gyárakban végzett gépjavítási munkát.",
                        "Csillagászati távcsövek lencséinek kézi csiszolását."
                    ],
                    "correct": 0,
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A harmincas években számos közép-európai tudós számára a _____ jelentette az egyetlen menekülési utat. (emigration)",
                    "answer": "kivándorlás",
                    "english": "In the 1930s, emigration meant the only path of escape for numerous Central European scientists.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Minél mélyebben vizsgálták a kérdést, _____ több bizonyítékot találtak a budapesti iskolák kiválóságára. (the more)",
                    "answer": "annál",
                    "english": "The more deeply they examined the question, the more evidence they found for the excellence of Budapest schools.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat használja nyelvtanilag helyesen a 'minél ... annál ...' párost?",
                    "options": [
                        "Minél összetettebb volt a számítás, annál gyorsabban oldotta meg Neumann János.",
                        "Minél összetett volt a számítás, annál gyorsan oldotta meg Neumann János.",
                        "Minél összetettebb volt a számítás, annyira gyorsabban meg-oldotta Neumann János."
                    ],
                    "correct": 0,
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Minél", "tovább", "kutatták", "a", "jelenséget,", "annál", "újabb", "összefüggéseket", "fedeztek", "fel."],
                    "solution": ["Minél", "tovább", "kutatták", "a", "jelenséget,", "annál", "újabb", "összefüggéseket", "fedeztek", "fel."],
                    "english": "The longer they researched the phenomenon, the newer interconnections they discovered.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan válaszolt Szilárd Leó Enrico Fermi kérdésére a földönkívüli civilizációk létezéséről?",
                    "options": [
                        "Azt felelte, hogy a földönkívüliek már itt vannak közöttünk, csak magyaroknak nevezik magukat.",
                        "Azt állította, hogy a Marson soha nem alakulhatott ki értelmes élet.",
                        "Azt javasolta, hogy építsenek rádiótávcsövet a sivatag közepén."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "princetoni", "kutatóintézet", "a", "világ", "legkiválóbb", "elméleti", "fizikusait", "fogadta", "be."],
                    "solution": ["A", "princetoni", "kutatóintézet", "a", "világ", "legkiválóbb", "elméleti", "fizikusait", "fogadta", "be."],
                    "english": "The Princeton research institute welcomed the world's most outstanding theoretical physicists.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a proportional sentence about how the more complex a problem became, the faster the Hungarian scientists switched to their native tongue.",
                            "answer": "Minél összetettebbé vált egy elméleti probléma, annál gyorsabban váltottak át a tudósok az anyanyelvükre."
                        },
                        {
                            "prompt": "Express that the more we study 20th-century physics, the clearer the role of the Budapest scientists becomes.",
                            "answer": "Minél alaposabban tanulmányozzuk a huszadik századi fizikát, annál világosabbá válik a budapesti tudósok szerepe."
                        }
                    ],
                    "teaches": ["b2-proportional-correlatives"]
                }
            ]
        },
        {
            "num": 2,
            "title": "Neumann János: Game Theory and Computer Architecture",
            "grammar_label": "Formal conditional conjunctions: amennyiben and abban az esetben, ha",
            "goals": [
                "I can explain John von Neumann's contributions to stored-program computer architecture and game theory.",
                "I can formulate precise logical conditions using amennyiben ('insofar as / provided that') and abban az esetben, ha ('in the event that').",
                "I can discuss computing memory, algorithms, and strategic decision-making in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "neumannjanos",
                "title": "Neumann János: Játékelmélet és számítógép-architektúra",
                "summary": "Born in Budapest in 1903, János Neumann revolutionized quantum mechanics, founded mathematical game theory, and designed the stored-program architecture still used in virtually every modern computer.",
                "location": "Budapest és Princeton",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Neumann János, aki 1903-ban született Budapesten, kortársai szerint még a „marslakók” között is egyedülálló szellemi képességekkel rendelkezett. Wigner Jenő később úgy emlékezett vissza rá, hogy sok kiváló tudóst ismert életében, de egyedül Neumann agya működött olyan sebességgel és pontossággal, mintha egy magasabb rendű gépezet lett volna. Hatéves korában már nyolcjegyű számokat osztott fejben, és ógörögül társalgott az édesapjával."
                    },
                    {
                        "type": "narration",
                        "text": "Neumann tudományos érdeklődése szinte minden területet átfogott. A húszas években megalapozta a kvantummechanika szigorú matematikai elméletét, majd Oskar Morgenstern közgazdásszal közösen megalkotta a játékelméletet. Felismerték, hogy amennyiben a szereplők döntései kölcsönösen függenek egymástól, a stratégiai viselkedés pontos matematikai egyenletekkel írható le — legyen szó sakkjátszmáról, piaci versenyről vagy diplomáciai válságról."
                    },
                    {
                        "type": "narration",
                        "text": "A második világháború végén figyelme az elektronikus számológépek felé fordult. A korai gépek, mint az ENIAC, csak úgy tudtak új feladatot elvégezni, ha a mérnökök napokon át kézzel átkábelezték az áramköröket. Neumann 1945-ös híres jelentésében, az EDVAC-tervezetben radikális újítást javasolt: a gép csak abban az esetben válhat valóban univerzálissá, ha a program utasításait ugyanabban a memóriában tárolja, mint a feldolgozandó adatokat."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a „Neumann-elv” — a központi vezérlőegység, az aritmetikai-logikai egység, a memória és a bemeneti-kimeneti eszközök szétválasztása — vált minden modern számítógép, okostelefon és szerver alaprajzává. Amennyiben ma megnyitunk egy szövegszerkesztőt vagy elindítunk egy keresést az interneten, a háttérben ugyanaz a logikai felépítés dolgozik, amelyet Neumann papírra vetett."
                    },
                    {
                        "type": "narration",
                        "text": "Élete utolsó éveiben már a mesterséges önreprodukáló automaták elméletével és az emberi agy ideghálózatának matematikai modellezésével foglalkozott, évtizedekkel megelőzve a modern mesterséges intelligencia kutatóit."
                    }
                ]
            },
            "words": [
                {"lemma": "játékelmélet", "translation": "game theory", "pos": "noun"},
                {"lemma": "memória", "translation": "memory (computing / cognitive)", "pos": "noun"},
                {"lemma": "utasítás", "translation": "instruction / command", "pos": "noun"},
                {"lemma": "vezérlőegység", "translation": "control unit", "pos": "noun"},
                {"lemma": "amennyiben", "translation": "insofar as / provided that / if (formal)", "pos": "expression"},
                {"lemma": "áramkör", "translation": "electrical circuit", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "formal-conditionals-amennyiben",
                "title": "Formal Conditional Conjunctions: amennyiben and abban az esetben, ha",
                "text1_title": "Academic and Legal Precision with amennyiben",
                "text1": "While everyday Hungarian uses ha ('if') for all conditions, B2 scientific, technical, and legal prose strongly prefers amennyiben ('if / insofar as / in the case that'). Amennyiben signals a precise logical prerequisite or boundary condition (e.g., Amennyiben a programot a memóriában tároljuk, a gép átkábelezés nélkül is újraprogramozható).",
                "text2_title": "Explicit Case Restriction: abban az esetben, ha",
                "text2": "To restrict a statement to a specific scenario ('in the event that / only in the case that'), Hungarian uses the demonstrative correlative phrase abban az esetben, ha ... (often preceded by csak for 'only if'). Notice the mandatory comma before ha.",
                "table_title": "Formal Conditional Structures",
                "table_rows": [
                    ["Amennyiben a feltételek teljesülnek, az egyenlet megoldható.", "Provided that the conditions are met, the equation is solvable."],
                    ["A gép csak abban az esetben univerzális, ha a program is a memóriában van.", "The machine is universal only in the event that the program is also in memory."],
                    ["Amennyiben a két fél nem működik együtt, mindketten veszítenek.", "Insofar as the two parties do not cooperate, both lose."]
                ],
                "examples": [
                    {
                        "spanish": "Amennyiben a szereplők döntései kölcsönösen függenek egymástól, a helyzet játékelmélettel írható le.",
                        "english": "Insofar as the participants' decisions mutually depend on one another, the situation can be described with game theory."
                    },
                    {
                        "spanish": "A számológép csak abban az esetben válhatott univerzálissá, ha az utasításokat is a memóriában tárolta.",
                        "english": "The calculating machine could become universal only in the case that it stored the instructions in memory as well."
                    },
                    {
                        "spanish": "Amennyiben ma elindítunk egy programot, a Neumann-féle architektúra lép működésbe.",
                        "english": "If we launch a program today, the von Neumann architecture goes into operation."
                    }
                ],
                "tip": "Amennyiben works in both indicative real conditions (Amennyiben ez igaz, ...) and conditional counterfactual clauses (Amennyiben másképp döntöttek volna, ...)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt a Neumann-elv legfontosabb újítása a korai elektronikus számológépekhez képest?",
                    "options": [
                        "A program utasításait ugyanabban a memóriában kell tárolni, mint a feldolgozandó adatokat.",
                        "A számítógépet gőzgéppel kell meghajtani az elektromos áram helyett.",
                        "Minden számítást kizárólag papírszalagra nyomtatva szabad elvégezni."
                    ],
                    "correct": 0,
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Neumann János és Oskar Morgenstern közösen dolgozták ki a stratégiai döntéseket vizsgáló _____ alapjait. (game theory)",
                    "answer": "játékelmélet",
                    "english": "János Neumann and Oskar Morgenstern jointly developed the foundations of game theory, which examines strategic decisions.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "_____ a gép a memóriában tárolja a programot, nincs szükség az áramkörök kézi átkábelezésére. (Provided that / If - formal)",
                    "answer": "Amennyiben",
                    "english": "Provided that the machine stores the program in memory, there is no need for manual rewiring of the circuits.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik kötőszó illik legjobban a tudományos szövegbe? 'A stratégiai egyensúly csak _____ jön létre, ha egyik félnek sem érdemes egyoldalúan változtatnia.'",
                    "options": [
                        "abban az esetben",
                        "annál inkább",
                        "minél tovább"
                    ],
                    "correct": 0,
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Amennyiben", "az", "adatok", "és", "az", "utasítások", "egy", "memóriában", "vannak,", "a", "számítógép", "univerzális."],
                    "solution": ["Amennyiben", "az", "adatok", "és", "az", "utasítások", "egy", "memóriában", "vannak,", "a", "számítógép", "univerzális."],
                    "english": "Provided that the data and the instructions are in one memory, the computer is universal.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért volt rendkívül lassú az ENIAC típusú korai gépek átállítása egy új feladatra?",
                    "options": [
                        "Mert a mérnököknek napokon keresztül kézzel kellett átkábelezniük az áramköröket.",
                        "Mert a gép csak télen tudott működni a nagy hőség miatt.",
                        "Mert nem létezett még az összeadás művelete."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "központi", "vezérlőegység", "olvassa", "be", "a", "memóriában", "tárolt", "utasításokat."],
                    "solution": ["A", "központi", "vezérlőegység", "olvassa", "be", "a", "memóriában", "tárolt", "utasításokat."],
                    "english": "The central control unit reads in the instructions stored in the memory.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain the core condition of game theory using 'Amennyiben a szereplők döntései...'.",
                            "answer": "Amennyiben a szereplők döntései kölcsönösen függenek egymástól, a stratégiai helyzet matematikai modellel írható le."
                        },
                        {
                            "prompt": "State when a computer becomes truly flexible using 'csak abban az esetben, ha'.",
                            "answer": "Egy számítógép csak abban az esetben válik igazán rugalmassá, ha a programot is a belső memóriában tárolja."
                        }
                    ],
                    "teaches": ["b2-proportional-correlatives"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Leó Szilárd: Chain Reaction and Moral Conscience",
            "grammar_label": "Stipulative conditionals: feltéve, hogy and azzal a feltétellel, hogy",
            "goals": [
                "I can recount Leó Szilárd's realization of the nuclear chain reaction in London and the Einstein–Szilárd letter.",
                "I can express stipulations and ethical conditions using feltéve, hogy and azzal a feltétellel, hogy.",
                "I can discuss patents, nuclear physics, and scientific responsibility in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szilardleo",
                "title": "Szilárd Leó: A láncreakció és a tudományos lelkiismeret",
                "summary": "Walking across a London intersection in 1933, Leó Szilárd conceived the nuclear chain reaction; later, having initiated the Einstein letter to Roosevelt, he fought passionately against using the atomic bomb on cities.",
                "location": "London, New York és Chicago",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Szilárd Leó életművében a fizikai zsenialitás és a mély erkölcsi felelősségtudat elválaszthatatlanul összefonódott. 1933 őszén, miután Berlinből Londonba menekült a náci hatalomátvétel elől, egy borús reggelen a Southampton Row jelzőlámpájánál várakozott. Ahogy a lámpa zöldre váltott, és ő lelépett a járdáról, hirtelen villámcsapásként hasított belé a felismerés: feltéve, hogy létezik egy olyan kémiai elem, amelynek atommagja egyetlen neutron becsapódására meghasad és közben két újabb neutront bocsát ki, önfenntartó nukleáris láncreakció jöhet létre."
                    },
                    {
                        "type": "narration",
                        "text": "Szilárd azonnal szabadalmaztatta a láncreakció gondolatát, ám a szabadalmat azzal a feltétellel engedte át a brit Admiralitásnak, hogy azt szigorúan titkosítják. Attól tartott ugyanis, hogy ha a felfedezés nyilvánosságra kerül, a német fizikusok fegyvert kovácsolhatnak belőle. Amikor 1938 végén Berlinben valóban felfedezték az uránhasadást, Szilárd világosan látta, hogy a fizika elméleti korszaka véget ért."
                    },
                    {
                        "type": "narration",
                        "text": "1939 nyarán két másik „marslakóval”, Wigner Jenővel és Teller Edével együtt felkereste egykori berlini tanárát és barátját, Albert Einsteint Long Island-i nyaralójában. Szilárd fogalmazta meg azt a történelmi levelet, amelyet Einstein írt alá Franklin D. Roosevelt elnöknek, figyelmeztetve az amerikai kormányt az uránbomba megépítésének lehetőségére. Ez a levél vezetett végül a Manhattan-terv elindításához, valamint az első atomreaktor megépítéséhez Chicagóban, amelyet Fermi és Szilárd közösen tervezett."
                    },
                    {
                        "type": "narration",
                        "text": "Szilárd azonban csak azzal a feltétellel támogatta a fegyverkutatást, hogy az kizárólag a hitleri Németország elrettentésére szolgál. Amikor 1945 tavaszán Németország kapitulált, és kiderült, hogy nincs német atombomba, Szilárd minden erejével tiltakozni kezdett a bomba japán városok elleni bevetése ellen."
                    },
                    {
                        "type": "narration",
                        "text": "Petíciót fogalmazott meg a tudósok körében, amelyben amellett érvelt, hogy a tudomány eredményeit nem szabad előzetes figyelmeztetés nélkül civil lakosság ellen felhasználni. A háború után felhagyott a magfizikával, és a molekuláris biológiának, valamint a nemzetközi leszerelés ügyének szentelte életét."
                    }
                ]
            },
            "words": [
                {"lemma": "láncreakció", "translation": "chain reaction", "pos": "noun"},
                {"lemma": "szabadalom", "translation": "patent", "pos": "noun"},
                {"lemma": "atommag", "translation": "atomic nucleus", "pos": "noun"},
                {"lemma": "felelősségtudat", "translation": "sense of responsibility / conscience", "pos": "noun"},
                {"lemma": "feltéve, hogy", "translation": "provided that / assuming that", "pos": "expression"},
                {"lemma": "elrettentés", "translation": "deterrence", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "stipulative-conditionals-felteve-hogy",
                "title": "Stipulative Conditionals: feltéve, hogy and azzal a feltétellel, hogy",
                "text1_title": "Theoretical Assumptions with feltéve, hogy",
                "text1": "In scientific reasoning and ethical argumentation, feltéve, hogy ('assuming that / provided that') introduces a necessary premise upon which a hypothesis or agreement rests. Morphologically, feltéve is the adverbial participle (-va/-ve) of feltesz ('to suppose / assume').",
                "text2_title": "Explicit Stipulations with azzal a feltétellel, hogy",
                "text2": "When an action is performed strictly under a negotiated or moral condition ('on the condition that'), Hungarian uses the correlative frame azzal a feltétellel (+ verb), hogy .... Because azzal a feltétellel often stands immediately before the verb as a manner/condition focus, any preverb on the main verb inverts behind it (e.g., A szabadalmat azzal a feltétellel adta át, hogy titkosítják).",
                "table_title": "Stipulative & Premise Conjunctions",
                "table_rows": [
                    ["Feltéve, hogy egy elem két neutront bocsát ki, láncreakció indul el.", "Assuming that an element emits two neutrons, a chain reaction begins."],
                    ["A szabadalmat azzal a feltétellel adta át, hogy titkosítják.", "He handed over the patent on the condition that they classify it."],
                    ["Csak azzal a feltétellel vett részt a tervben, hogy az az elrettentést szolgálja.", "He participated in the project only on the condition that it serve deterrence."]
                ],
                "examples": [
                    {
                        "spanish": "Feltéve, hogy létezik ilyen kémiai elem, önfenntartó nukleáris láncreakció jöhet létre.",
                        "english": "Provided that such a chemical element exists, a self-sustaining nuclear chain reaction can come about."
                    },
                    {
                        "spanish": "Szilárd a szabadalmat azzal a feltétellel engedte át a brit Admiralitásnak, hogy azt titokban tartják.",
                        "english": "Szilárd transferred the patent to the British Admiralty on the condition that they keep it secret."
                    },
                    {
                        "spanish": "A tudósok csak azzal a feltétellel támogatták a kutatást, hogy megelőzik vele a diktatúrát.",
                        "english": "The scientists supported the research only on the condition that they forestall the dictatorship with it."
                    }
                ],
                "tip": "Notice the word order when azzal a feltétellel precedes a prefixed verb: átengedte -> azzal a feltétellel engedte át, hogy..."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Miért adta át Szilárd Leó az 1930-as években a láncreakció szabadalmát a brit Admiralitásnak?",
                    "options": [
                        "Hogy titkosítsák a felfedezést, és a náci Németország fizikusai ne építhessenek belőle fegyvert.",
                        "Hogy nagy összegű kereskedelmi jutalékot kapjon az erőművektől.",
                        "Mert nem érdekelte többé a fizika."
                    ],
                    "correct": 0,
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Amikor egy neutron meghasítja az urán atommagját, önfenntartó nukleáris _____ indulhat el. (chain reaction)",
                    "answer": "láncreakció",
                    "english": "When a neutron splits the uranium nucleus, a self-sustaining nuclear chain reaction can start.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "_____ létezik egy két neutront kibocsátó elem, az atomenergia felszabadítható. (Assuming that / Provided that — two words with comma)",
                    "answer": "Feltéve, hogy",
                    "english": "Provided that an element emitting two neutrons exists, atomic energy can be released.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat szórendje helyes az 'azzal a feltétellel' szerkezettel?",
                    "options": [
                        "Szilárd a szabadalmat azzal a feltétellel adta át, hogy szigorúan titkosítják.",
                        "Szilárd a szabadalmat azzal a feltétellel átadta, hogy szigorúan titkosítják.",
                        "Szilárd a szabadalmat feltétellel azzal átadta, hogy szigorúan titkosítják."
                    ],
                    "correct": 0,
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "kutatók", "csak", "azzal", "a", "feltétellel", "írták", "alá", "a", "levelet,", "hogy", "megelőzik", "a", "veszélyt."],
                    "solution": ["A", "kutatók", "csak", "azzal", "a", "feltétellel", "írták", "alá", "a", "levelet,", "hogy", "megelőzik", "a", "veszélyt."],
                    "english": "The researchers signed the letter only on the condition that they prevent the danger.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan viszonyult Szilárd Leó az atombomba bevetéséhez 1945 tavaszán, Németország legyőzése után?",
                    "options": [
                        "Petícióban tiltakozott az ellen, hogy a bombát figyelmeztetés nélkül japán városok ellen vessék be.",
                        "Követelte, hogy azonnal dobják le a bombát több nagyvárosra is.",
                        "Visszaköltözött Berlinbe oktatni."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "tudományos", "felfedezéseket", "mindig", "mély", "erkölcsi", "felelősségtudatnak", "kell", "kísérnie."],
                    "solution": ["A", "tudományos", "felfedezéseket", "mindig", "mély", "erkölcsi", "felelősségtudatnak", "kell", "kísérnie."],
                    "english": "Scientific discoveries must always be accompanied by a deep sense of moral responsibility.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "State Szilárd's scientific hypothesis in 1933 using 'Feltéve, hogy...'.",
                            "answer": "Feltéve, hogy egy atommag hasadásakor két újabb neutron szabadul fel, önfenntartó láncreakció jöhet létre."
                        },
                        {
                            "prompt": "Explain under what condition Szilárd supported the Manhattan Project using 'csak azzal a feltétellel..., hogy'.",
                            "answer": "Szilárd csak azzal a feltétellel támogatta a kutatást, hogy a fegyver kizárólag az elrettentést szolgálja."
                        }
                    ],
                    "teaches": ["b2-proportional-correlatives"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Wigner, Kármán, and Theoretical Breakthroughs",
            "grammar_label": "Degree and consequence correlatives: annyira ..., hogy and olyan mértékben ..., hogy",
            "goals": [
                "I can describe Jenő Wigner's work on symmetry principles and Tódor Kármán's leadership in supersonic aerodynamics.",
                "I can construct high-register degree-and-consequence clauses using annyira ..., hogy and olyan mértékben ..., hogy.",
                "I can use academic terminology for symmetry, aerodynamics, and engineering design."
            ],
            "story_segment": {
                "seg_slug": "wignerkarman",
                "title": "Wigner Jenő, Kármán Tódor és az elméleti áttörések",
                "summary": "While Nobel laureate Jenő Wigner uncovered the mathematical symmetries of quantum physics and engineered the first industrial nuclear reactors, Tódor Kármán laid the foundations of supersonic flight and space exploration.",
                "location": "Göttingen, Princeton és Pasadena",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Míg Szilárd Leó a szellemi szikrák embere volt, addig Wigner Jenő a csendes, módszeres alaposságot képviselte a „marslakók” körében. Édesapja bőrgyári igazgató volt, és azt szerette volna, ha fia vegyészmérnöknek tanul, hogy átvehesse a családi üzemet. Wigner engedelmeskedett, és Berlinben vegyészmérnöki diplomát szerzett, ám a kvantummechanika olyan mértékben magával ragadta, hogy szabadidejében a fizikai intézet szemináriumait látogatta."
                    },
                    {
                        "type": "narration",
                        "text": "Wigner legnagyobb elméleti felfedezése az volt, hogy a csoportelmélet és a szimmetriaelvek segítségével írta le az elemi részecskék és az atommagok viselkedését. Ez a felismerés annyira alapvetőnek bizonyult, hogy 1963-ban fizikai Nobel-díjjal jutalmazták érte. Ugyanakkor vegyészmérnöki tudása sem veszett kárba: ő tervezte meg a világ első nagy teljesítményű atomreaktorait, így joggal tekintik a világ első reaktormérnökének."
                    },
                    {
                        "type": "narration",
                        "text": "A generáció legidősebb tagja, az 1881-ben született Kármán Tódor egy másik tudományágat, a modern repüléstudományt és az űrhajózást forradalmasította. Már göttingeni évei alatt leírta az áramló folyadékokban és gázokban keletkező szabályos örvénysort, amelyet ma is Kármán-féle örvénysornak neveznek. Felismerte, hogy a repülőgépek szárnyának rezgése csak abban az esetben előzhető meg, ha a mérnökök pontosan kiszámítják ezeket a légörvényeket."
                    },
                    {
                        "type": "narration",
                        "text": "Az Egyesült Államokban Kármán a kaliforniai Műszaki Egyetem (Caltech) professzoraként megszervezte a Sugárhajtási Laboratóriumot, a mai NASA JPL elődjét. Kutatásai olyan mértékben meghatározták a hangsebesség feletti repülést, hogy az űrrepülés nemzetközi szervezete később róla nevezte el a Föld légköre és a világűr közötti határt: a száz kilométeres magasságban húzódó Kármán-vonalat."
                    },
                    {
                        "type": "narration",
                        "text": "Wigner és Kármán életműve közös tanulságot hordoz: minél szorosabban kapcsolódik össze a legmagasabb szintű matematikai elmélet a gyakorlati mérnöki tudással, annál maradandóbb technológiai áttörések születnek."
                    }
                ]
            },
            "words": [
                {"lemma": "szimmetriaelv", "translation": "symmetry principle", "pos": "noun"},
                {"lemma": "örvénysor", "translation": "vortex street (aerodynamics)", "pos": "noun"},
                {"lemma": "hangsebesség", "translation": "speed of sound", "pos": "noun"},
                {"lemma": "vegyészmérnök", "translation": "chemical engineer", "pos": "noun"},
                {"lemma": "olyan mértékben ..., hogy", "translation": "to such an extent ..., that", "pos": "expression"},
                {"lemma": "sugárhajtás", "translation": "jet propulsion", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "degree-consequence-correlatives",
                "title": "Degree and Consequence Correlatives: annyira ..., hogy and olyan mértékben ..., hogy",
                "text1_title": "Quantifying Impact with olyan mértékben ..., hogy",
                "text1": "In B2 academic writing, simple 'so ... that' (olyan ..., hogy) is frequently elevated to olyan mértékben + [verb], hogy ... ('to such a degree/extent ..., that ...') or annyira + [adjective/verb], hogy ... to describe how a scientific discovery transformed an entire field.",
                "text2_title": "Combining Correlatives in Analytical Prose",
                "text2": "Notice how Hungarian writers combine proportional correlatives (minél ... annál ...) and degree correlatives (olyan mértékben ..., hogy) within the same paragraph to build cumulative arguments: the first shows dynamic covariation, while the second states the historical threshold reached.",
                "table_title": "Degree and Consequence Patterns",
                "table_rows": [
                    ["A fizika olyan mértékben magával ragadta, hogy pályát módosított.", "Physics captivated him to such an extent that he changed careers."],
                    ["A felismerés annyira alapvetőnek bizonyult, hogy Nobel-díjat kapott érte.", "The insight proved so fundamental that he received a Nobel Prize for it."],
                    ["Kármán kutatásai olyan mértékben meghatározták az űrkutatást, hogy róla nevezték el a világűr határát.", "Kármán's research shaped space exploration to such a degree that the boundary of space was named after him."]
                ],
                "examples": [
                    {
                        "spanish": "A kvantummechanika olyan mértékben magával ragadta Wignert, hogy minden szabadidejét a fizikai szemináriumokon töltötte.",
                        "english": "Quantum mechanics captivated Wigner to such an extent that he spent all his free time in physics seminars."
                    },
                    {
                        "spanish": "A szimmetriaelvek annyira fontosnak bizonyultak, hogy 1963-ban Nobel-díjjal ismerték el a munkásságát.",
                        "english": "Symmetry principles proved so important that his work was recognized with a Nobel Prize in 1963."
                    },
                    {
                        "spanish": "Minél szorosabban kapcsolódik össze az elmélet és a gyakorlat, annál maradandóbb áttörések születnek.",
                        "english": "The more closely theory and practice are linked, the more enduring breakthroughs are born."
                    }
                ],
                "tip": "When annyira modifies an adjective with -nak/-nek + bizonyul ('proves to be'), place annyira immediately before the adjective: annyira alapvetőnek bizonyult, hogy..."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelöl a Kármán Tódorról elnevezett 'Kármán-vonal'?",
                    "options": [
                        "A Föld légköre és a világűr közötti nemzetközileg elfogadott határt száz kilométeres magasságban.",
                        "A Budapestet és Bécset összekötő első vasútvonalat.",
                        "Az atommag belsejében ható erők hatósugarát."
                    ],
                    "correct": 0,
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Wigner Jenő a kvantummechanikai _____ kidolgozásáért kapott fizikai Nobel-díjat 1963-ban. (symmetry principle)",
                    "answer": "szimmetriaelv",
                    "english": "Jenő Wigner received the Nobel Prize in Physics in 1963 for working out the quantum-mechanical symmetry principle.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Kármán kutatásai olyan _____ meghatározták a modern repüléstudományt, hogy róla nevezték el a világűr határát. (to such an extent)",
                    "answer": "mértékben",
                    "english": "Kármán's research shaped modern aeronautics to such an extent that the boundary of space was named after him.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen a következményes összefüggést?",
                    "options": [
                        "Wigner felfedezése annyira alapvetőnek bizonyult, hogy a modern részecskefizika ma is erre épül.",
                        "Wigner felfedezése minél alapvetőnek bizonyult, hogy a modern részecskefizika ma is erre épül.",
                        "Wigner felfedezése amennyiben alapvetőnek bizonyult, annál a modern fizika erre épül."
                    ],
                    "correct": 0,
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Minél", "szorosabban", "kapcsolódik", "össze", "az", "elmélet", "és", "a", "gyakorlat,", "annál", "maradandóbb", "eredmény", "születik."],
                    "solution": ["Minél", "szorosabban", "kapcsolódik", "össze", "az", "elmélet", "és", "a", "gyakorlat,", "annál", "maradandóbb", "eredmény", "születik."],
                    "english": "The more closely theory and practice are connected, the more enduring a result is born.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan hasznosította Wigner Jenő az eredeti vegyészmérnöki diplomáját a második világháború idején?",
                    "options": [
                        "Ő tervezte meg a világ első nagy teljesítményű, ipari méretű atomreaktorait.",
                        "Bőrgyárat alapított Princeton belvárosában.",
                        "Üzemanyagot gyártott a korai gőzmozdonyok számára."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Kármán", "Tódor", "kutatásai", "megnyitották", "az", "utat", "a", "hangsebesség", "feletti", "repülés", "előtt."],
                    "solution": ["Kármán", "Tódor", "kutatásai", "megnyitották", "az", "utat", "a", "hangsebesség", "feletti", "repülés", "előtt."],
                    "english": "Tódor Kármán's research opened the way for flight above the speed of sound.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe how deeply quantum mechanics captivated Jenő Wigner using 'olyan mértékben ..., hogy'.",
                            "answer": "A kvantummechanika olyan mértékben magával ragadta Wigner Jenőt, hogy a vegyészmérnöki pálya mellett a fizikának szentelte életét."
                        },
                        {
                            "prompt": "Write a proportional statement linking mathematical theory and engineering practice using 'Minél ... annál ...'.",
                            "answer": "Minél szorosabban működnek együtt az elméleti matematikusok és a mérnökök, annál sikeresebbek a technológiai újítások."
                        }
                    ],
                    "teaches": ["b2-proportional-correlatives"]
                }
            ]
        },
        {
            "num": 5,
            "title": "The Secret of Budapest's Intellectual Ecosystem",
            "grammar_label": "Synthesizing proportional and conditional correlatives in historical explanation",
            "goals": [
                "I can analyze why turn-of-the-century Budapest secondary schools (Fasori, Minta, Reál) produced so many world-class scientists.",
                "I can combine minél ... annál ..., amennyiben, and feltéve, hogy in structured analytical essays.",
                "I can discuss pedagogy, secondary education (gimnázium), and intellectual talent development."
            ],
            "story_segment": {
                "seg_slug": "budapestititok",
                "title": "A budapesti szellemi műhely titka",
                "summary": "Historians of science agree that the 'Martians' were not a genetic miracle but the product of Budapest's extraordinary secondary schools, legendary teachers like László Rátz, and a culture that prized problem-solving.",
                "location": "Budapest (Fasori Evangélikus Gimnázium és Minta Gimnázium)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A tudománytörténészek évtizedek óta keresik a választ arra a kérdésre, hogy mi volt a századfordulós Budapest szellemi ökoszisztémájának titka. Hogyan lehetséges, hogy egyetlen város néhány négyzetkilométeres belvárosi negyedéből került ki a huszadik század annyi meghatározó fizikusa és matematikusa? A válasz nem valamilyen rejtélyes biológiai csodában, hanem a korabeli magyar oktatási rendszerben és polgári kultúrában rejlik."
                    },
                    {
                        "type": "narration",
                        "text": "A „marslakók” szinte mindannyian három legendás pesti középiskola valamelyikébe jártak: a Fasori Evangélikus Gimnáziumba (ahol Wigner Jenő és Neumann János tanult), a Kármán Mór által alapított Minta Gimnáziumba (ahová Kármán Tódor és Teller Ede járt), vagy a VI. kerületi Főreáliskolába (Szilárd Leó egykori iskolájába). Ezekben az intézményekben egyetemi színvonalú tanárok tanítottak, akik nem magolást, hanem önálló gondolkodást vártak el."
                    },
                    {
                        "type": "narration",
                        "text": "A Fasori Gimnázium matematikatanára, Rátz László például azonnal felismerte a tizenegy éves Neumann János rendkívüli tehetségét. Amennyiben egy diák kiemelkedő képességeket mutatott, a tanárok nem hagyták unatkozni az órákon: Rátz professzor egyetemi matematikusokat kért fel, hogy külön foglalkozzanak a fiatal Neumann-nal, miközben egyetlen fillért sem fogadott el a családjától. Minél nagyobb szabadságot kaptak a diákok a kérdezésben, annál bátrabban lépték át a tankönyvek határait."
                    },
                    {
                        "type": "narration",
                        "text": "Ugyanilyen fontos szerepet játszott a Eötvös Loránd Fizikai és Matematikai Társulat által 1894-ben indított középiskolai verseny, valamint a KöMaL folyóirat. Itt nem a gyors képletbehelyettesítés számított: a diákok csak abban az esetben nyerhettek díjat, ha eredeti, kreatív gondolatmenettel oldották meg a szokatlan feladatokat. Szilárd Leó és Wigner Jenő egyaránt e versenyek díjazottjai között tűntek fel először."
                    },
                    {
                        "type": "narration",
                        "text": "A budapesti „marslakók” története így a ma embere számára is érvényes tanulsággal zárul. Egy társadalom szellemi ereje mindig azon múlik, hogy mennyire becsüli meg a tanárait és az alapkutatást — feltéve, hogy a tehetség mellé nyitott szellemi légkör és emberi felelősségérzet is társul."
                    }
                ]
            },
            "words": [
                {"lemma": "gimnázium", "translation": "academic secondary school / grammar school", "pos": "noun"},
                {"lemma": "tehetséggondozás", "translation": "talent nurturing / gifted education", "pos": "noun"},
                {"lemma": "tanulmányi verseny", "translation": "academic competition", "pos": "noun"},
                {"lemma": "gondolatmenet", "translation": "line of reasoning / train of thought", "pos": "noun"},
                {"lemma": "alapkutatás", "translation": "basic / fundamental research", "pos": "noun"},
                {"lemma": "magolás", "translation": "rote memorization / cramming", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "synthesizing-correlatives-in-argumentation",
                "title": "Synthesizing Proportional and Conditional Correlatives in Argumentation",
                "text1_title": "Building Multi-Layered Historical Explanations",
                "text1": "In B2 essay writing, proportional and conditional correlatives work together to explain complex historical phenomena. You can state a general law with minél ... annál ..., specify institutional prerequisites with amennyiben or abban az esetben, ha, and conclude with a forward-looking caveat using feltéve, hogy.",
                "text2_title": "Checklist of B2 Correlative Punctuation and Word Order",
                "text2": "1. Always place a comma between the minél-clause and the annál-clause. 2. Remember that both minél + comparative and annál + comparative trigger preverb inversion (e.g., annál bátrabban lépték át). 3. Always place a comma before ha in abban az esetben, ha and before hogy in feltéve, hogy.",
                "table_title": "Full B2 Correlative Toolkit",
                "table_rows": [
                    ["Minél nagyobb szabadságot kaptak, annál bátrabban kérdeztek.", "Proportional covariation (the more ..., the more ...)"],
                    ["Amennyiben egy diák tehetséges volt, külön foglalkoztak vele.", "Formal prerequisite (provided that / insofar as)"],
                    ["Csak abban az esetben nyertek, ha eredeti megoldást találtak.", "Strict condition (only in the case that)"],
                    ["A tehetség kibontakozik, feltéve, hogy nyitott a szellemi légkör.", "Stipulative caveat (assuming that / provided that)"]
                ],
                "examples": [
                    {
                        "spanish": "Amennyiben egy diák kiemelkedő képességeket mutatott, a tanárok külön foglalkoztak vele.",
                        "english": "Provided that a student showed outstanding abilities, the teachers worked with them individually."
                    },
                    {
                        "spanish": "Minél nagyobb szabadságot kaptak a diákok a kérdezésben, annál bátrabban lépték át a tankönyvek határait.",
                        "english": "The greater freedom the students received in questioning, the more boldly they stepped beyond the boundaries of textbooks."
                    },
                    {
                        "spanish": "Egy nemzet tudománya virágozni fog, feltéve, hogy társadalma megbecsüli a tanárokat és az alapkutatást.",
                        "english": "A nation's science will flourish, provided that its society esteems teachers and basic research."
                    }
                ],
                "tip": "When writing B2 essays, avoid repeating ha in every sentence; alternating between amennyiben, feltéve, hogy, and minél ... annál ... immediately marks C1-approaching stylistic maturity."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen oktatási módszer jellemezte a századforduló kiemelkedő budapesti gimnáziumait?",
                    "options": [
                        "A gépies magolás helyett az önálló gondolkodást, a kérdezést és az egyéni tehetséggondozást támogatták.",
                        "Kizárólag latin szótárak szó szerinti bemagolását követelték meg.",
                        "Minden fizikai és matematikai órát megszüntettek."
                    ],
                    "correct": 0,
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Az Eötvös-versenyen nem a kész képletek bemagolása, hanem az eredeti _____ számított. (line of reasoning)",
                    "answer": "gondolatmenet",
                    "english": "In the Eötvös competition, what mattered was not memorizing ready-made formulas, but an original line of reasoning.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Minél nagyobb szabadságot kaptak a diákok, annál bátrabban _____ át a tankönyvek határait. (stepped across — preverb inversion!)",
                    "answer": "lépték",
                    "english": "The greater freedom the students received, the more boldly they stepped across the boundaries of the textbooks.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Válaszd ki a nyelvtanilag és stilisztikailag helyes mondatot!",
                    "options": [
                        "A tehetségek csak abban az esetben bontakozhatnak ki, ha az iskola támogatja az önálló gondolkodást.",
                        "A tehetségek csak abban az esetben kibontakozhatnak, amennyiben hogy az iskola támogatja.",
                        "Minél az iskola támogatja a diákokat, feltéve, hogy kibontakoznak."
                    ],
                    "correct": 0,
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "tudomány", "fejlődik,", "feltéve,", "hogy", "a", "társadalom", "megbecsüli", "a", "tanárokat", "és", "az", "alapkutatást."],
                    "solution": ["A", "tudomány", "fejlődik,", "feltéve,", "hogy", "a", "társadalom", "megbecsüli", "a", "tanárokat", "és", "az", "alapkutatást."],
                    "english": "Science develops, provided that society values teachers and basic research.",
                    "teaches": ["b2-proportional-correlatives"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit tett Rátz László, amikor felismerte a tizenegy éves Neumann János kivételes matematikai tehetségét?",
                    "options": [
                        "Egyetemi matematikusokat kért fel, hogy külön foglalkozzanak vele, és ezért semmilyen díjazást nem fogadott el.",
                        "Elküldte az iskolából, mert túl nehéz kérdéseket tett fel.",
                        "Kötelezte, hogy csak a nyolcadikos tankönyv példáit gyakorolja."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "Fasori", "Gimnáziumban", "a", "magolás", "helyett", "a", "módszeres", "tehetséggondozás", "állt", "a", "középpontban."],
                    "solution": ["A", "Fasori", "Gimnáziumban", "a", "magolás", "helyett", "a", "módszeres", "tehetséggondozás", "állt", "a", "középpontban."],
                    "english": "At the Fasori Gymnasium, methodical talent nurturing rather than rote memorization stood at the center.",
                    "teaches": ["b2-marslakok-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Summarize the role of teachers like László Rátz using 'Amennyiben egy diák...'.",
                            "answer": "Amennyiben egy diák rendkívüli képességeket mutatott, a tanárok egyéni tehetséggondozással segítették a fejlődését."
                        },
                        {
                            "prompt": "Conclude why Budapest's schools succeeded using 'Minél inkább ..., annál ...'.",
                            "answer": "Minél inkább az önálló gondolatmenetet jutalmazták a magolás helyett, annál több világhírű kutató került ki a padsorokból."
                        }
                    ],
                    "teaches": ["b2-proportional-correlatives"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can synthesize the biographies and scientific contributions of János Neumann, Leó Szilárd, Jenő Wigner, and Tódor Kármán.",
            "I can accurately use proportional correlatives (minél ... annál ...) with comparative forms and preverb inversion.",
            "I can deploy formal conditional and stipulative conjunctions (amennyiben, abban az esetben, ha, feltéve, hogy, azzal a feltétellel, hogy)."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban helyes a fokozás és az igekötő szórendje a 'minél ... annál ...' szerkezetben?",
                "options": [
                    "Minél pontosabban írták le a folyamatot, annál több gyakorlati alkalmazást fedeztek fel.",
                    "Minél pontosan írták le a folyamatot, annál többet felfedeztek.",
                    "Minél pontosabban leírták a folyamatot, annál több alkalmazást felfedeztek."
                ],
                "correct": 0,
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik fogalom kapcsolódik közvetlenül Neumann János 1945-ös EDVAC-jelentéséhez?",
                "options": [
                    "A tárolt programú számítógép-architektúra, ahol az adatok és az utasítások közös memóriában vannak.",
                    "A hangsebesség feletti légörvények matematikai leírása.",
                    "A klórvizes kézmosás bevezetése a szülészeti klinikákon."
                ],
                "correct": 0,
                "teaches": ["b2-marslakok-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés helyettesítheti a 'ha' kötőszót hivatalos, tudományos regiszterben?",
                "options": [
                    "amennyiben",
                    "annál inkább",
                    "viszont"
                ],
                "correct": 0,
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minél összetettebb volt egy matematikai probléma, _____ gyorsabban oldotta meg Neumann János. (the faster)",
                "answer": "annál",
                "english": "The more complex a mathematical problem was, the faster János Neumann solved it.",
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Szilárd Leó londoni sétája közben ismerte fel az önfenntartó nukleáris _____ elméleti lehetőségét. (chain reaction)",
                "answer": "láncreakció",
                "english": "During his walk in London, Leó Szilárd recognized the theoretical possibility of a self-sustaining nuclear chain reaction.",
                "teaches": ["b2-marslakok-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szilárd a szabadalmat csak azzal a _____ adta át, hogy azt szigorúan titkosítják. (on the condition)",
                "answer": "feltétellel",
                "english": "Szilárd handed over the patent only on the condition that it be strictly classified.",
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Amennyiben", "a", "program", "a", "memóriában", "van,", "a", "gép", "átkábelezés", "nélkül", "is", "működik."],
                "solution": ["Amennyiben", "a", "program", "a", "memóriában", "van,", "a", "gép", "átkábelezés", "nélkül", "is", "működik."],
                "english": "Provided that the program is in memory, the machine operates even without rewiring.",
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "budapesti", "gimnáziumokban", "a", "magolás", "helyett", "a", "kreatív", "gondolatmenetet", "értékelték."],
                "solution": ["A", "budapesti", "gimnáziumokban", "a", "magolás", "helyett", "a", "kreatív", "gondolatmenetet", "értékelték."],
                "english": "In Budapest grammar schools, creative reasoning was valued instead of rote memorization.",
                "teaches": ["b2-marslakok-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejez ki előfeltételt ('assuming that / provided that')?",
                "options": [
                    "Az elmélet helyesnek bizonyul, feltéve, hogy a kísérleti mérések is alátámasztják.",
                    "Az elmélet annyira helyesnek bizonyul, minél a mérések alátámasztják.",
                    "Az elmélet helyesnek bizonyul, annál inkább a mérések alátámasztják."
                ],
                "correct": 0,
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Minél", "többet", "tudunk", "a", "marslakókról,", "annál", "jobban", "értjük", "a", "huszadik", "századot."],
                "solution": ["Minél", "többet", "tudunk", "a", "marslakókról,", "annál", "jobban", "értjük", "a", "huszadik", "századot."],
                "english": "The more we know about the Martians, the better we understand the twentieth century.",
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Explain why the 'Martians' had such an impact on computing and physics using 'Minél ... annál ...'.",
                        "answer": "Minél szorosabban kapcsolták össze a matematikai elméletet a gyakorlati problémákkal, annál nagyobb hatást gyakoroltak a modern tudományra."
                    }
                ],
                "teaches": ["b2-proportional-correlatives"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "State a lesson from Leó Szilárd's life using 'feltéve, hogy' or 'amennyiben'.",
                        "answer": "A tudományos felfedezések csak akkor szolgálják az emberiség javát, amennyiben a kutatókat mély erkölcsi felelősségtudat vezérli."
                    }
                ],
                "teaches": ["b2-proportional-correlatives"]
            }
        ]
    }
}

# ============================================================================
# CULTURE UNIT 8: b2-semmelweis
# ============================================================================
UNIT_8_SEMMELWEIS = {
    "unit_num": 8,
    "slug": "semmelweis",
    "title": "Semmelweis, Szent-Györgyi & Medical Pioneers",
    "grammar_skill": "b2-past-modals",
    "vocab_skill": "b2-semmelweis-vocab",
    "theme": "Hungarian medical pioneers from Semmelweis to Karikó",
    "location": "Bécs, Pest, Szeged és Philadelphia",
    "combined_story_title": "Klórvíz, paprika és mRNS: Magyar orvosi sorsok",
    "combined_story_summary": "Three centuries of Hungarian medical breakthroughs and struggles against institutional skepticism: Ignác Semmelweis, Albert Szent-Györgyi, and Katalin Karikó.",
    "intro_body": [
        "From Ignác Semmelweis's 1847 discovery of antiseptic handwashing in Vienna to Albert Szent-Györgyi's isolation of vitamin C in Szeged and Katalin Karikó's decades-long persistence with mRNA in Philadelphia, Hungarian medical pioneers have repeatedly challenged medical orthodoxy.",
        "In this unit, you will explore these dramatic scientific biographies while mastering B2 past deontic and epistemic modals (kellett volna + infinitive, lehetett volna + infinitive, and verb + -hatott/-hetett volna) to evaluate historical decisions, missed opportunities, and counterfactual outcomes."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "Semmelweis and the Mystery of Childbed Fever",
            "grammar_label": "Past counterfactual obligation and possibility: kellett volna and lehetett volna",
            "goals": [
                "I can recount how Ignác Semmelweis solved the mystery of puerperal (childbed) fever in Vienna in 1847.",
                "I can express past unfulfilled obligation and missed possibility using kellett volna and lehetett volna + infinitive.",
                "I can use medical and historical vocabulary related to obstetrics, infection, and disinfection."
            ],
            "story_segment": {
                "seg_slug": "gyermekagyilaz",
                "title": "Semmelweis és a gyermekágyi láz rejtélye",
                "summary": "In 1847 at the Vienna General Hospital, young Buda-born physician Ignác Semmelweis realized that doctors themselves were carrying fatal 'cadaverous particles' from the autopsy room to maternity patients.",
                "location": "Bécs (Közkórház) és Buda",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1840-es évek közepén a bécsi Közkórház szülészeti klinikáján megdöbbentő kettősség uralkodott. Az intézmény két osztályra oszlott: az első osztályon orvosok és orvostanhallgatók vezették a szüléseket, a másodikon viszont bábák, azaz szülésznők dolgoztak. Míg a bábák osztályán a gyermekágyi láz okozta halálozás alig érte el a két-három százalékot, addig az orvosok osztályán a kismamák tíz-tizenöt százaléka vesztette életét. Sok kétségbeesett asszony térden állva könyörgött a felvételnél, hogy ne az első osztályra osszák be, mert tudták, hogy a tragédiát el lehetett volna kerülni."
                    },
                    {
                        "type": "narration",
                        "text": "A budai születésű fiatal tanársegéd, Semmelweis Ignác nem tudott belenyugodni abba a korabeli magyarázatba, hogy a járványt „kozmoszi-tellurikus” légköri hatások vagy a kismamák félelme okozza. Minden reggel a boncteremben kezdte a napját, ahol az elhunyt anyák holttestét vizsgálta, ám hónapokig nem találta a döntő különbséget a két osztály között. A fordulópontot 1847 tavaszán egy megrázó tragédia hozta el: barátja és kollégája, Jakob Kolletschka professzor boncolás közben megvágta az ujját egy szikével, és néhány nap múlva vérmérgezésben meghalt."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Semmelweis elolvasta Kolletschka boncolási jegyzőkönyvét, megdöbbenve látta, hogy a professzor belső szerveiben pontosan ugyanazok az elváltozások alakultak ki, mint a gyermekágyi lázban elhunyt édesanyáknál. Ekkor világosodott meg előtte az igazság: az orvosoknak és a diákoknak nem lett volna szabad a boncteremből közvetlenül, alapos fertőtlenítés nélkül átmenniük a szülőszobába, mert a kezükre tapadt „hullarészecskékkel” maguk vitték át a halálos kórt."
                    },
                    {
                        "type": "narration",
                        "text": "1847 májusában Semmelweis szigorú rendeletet vezetett be: minden orvosnak és medikusnak klórmészoldatban kellett kezet mosnia, mielőtt bármelyik beteget megvizsgálta volna. Az egyszerű szappanos víz nem volt elég, csak a klórvíz tudta elpusztítani a láthatatlan fertőző anyagot. Az eredmény szinte azonnali és drámai volt: néhány héten belül a halálozási arány az első osztályon is egy százalék alá zuhant."
                    },
                    {
                        "type": "narration",
                        "text": "Semmelweis ezzel a lépéssel évekkel Louis Pasteur és Joseph Lister munkássága előtt felfedezte az aszepszis, vagyis a kórokozóktól való mentesség gyakorlati elvét. Bebizonyította, hogy egyetlen fegyelmezett higiéniai intézkedéssel édesanyák ezreinek az életét lehetett volna megmenteni szerte Európában."
                    }
                ]
            },
            "words": [
                {"lemma": "gyermekágyi láz", "translation": "childbed fever / puerperal fever", "pos": "noun"},
                {"lemma": "boncolás", "translation": "autopsy / dissection", "pos": "noun"},
                {"lemma": "fertőtlenítés", "translation": "disinfection / sterilization", "pos": "noun"},
                {"lemma": "halálozási arány", "translation": "mortality rate", "pos": "noun"},
                {"lemma": "klórvíz", "translation": "chlorinated lime solution / chlorine water", "pos": "noun"},
                {"lemma": "kellett volna", "translation": "should have (past unfulfilled obligation)", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "past-modals-kellett-lehetett-volna",
                "title": "Past Deontic & Dynamic Modals: kellett volna and lehetett volna",
                "text1_title": "Unfulfilled Past Obligation with kellett volna + Infinitive",
                "text1": "To state what someone should have done (or what should not have been allowed) in the past, Hungarian uses the past tense of the impersonal modal verb (kellett / szabadott) followed by the conditional particle volna and the infinitive (-ni). When a specific person bears the obligation, that person appears in the Dative case (-nak/-nek): Az orvosoknak kezet kellett volna mosniuk ('The doctors should have washed their hands').",
                "text2_title": "Missed Past Possibility with lehetett volna + Infinitive",
                "text2": "To express that a tragedy could have been prevented or a problem could have been solved ('it would have been possible to...'), Hungarian uses lehetett volna + infinitive. Notice that if the infinitive has a separable preverb (e.g., elkerülni, megmenteni), the preverb frequently climbs in front of lehetett volna in neutral focus: A tragédiát el lehetett volna kerülni ('The tragedy could have been avoided').",
                "table_title": "Core Past Modal Constructions",
                "table_rows": [
                    ["Az orvosoknak kezet kellett volna mosniuk.", "The doctors should have washed their hands."],
                    ["Nem lett volna szabad fertőtlenítés nélkül vizsgálni.", "They should not have been allowed to examine without disinfection."],
                    ["A tragédiát el lehetett volna kerülni.", "The tragedy could have been avoided (preverb climbing)."],
                    ["Édesanyák ezreit lehetett volna megmenteni.", "Thousands of mothers could have been saved."]
                ],
                "examples": [
                    {
                        "spanish": "Az orvosoknak nem lett volna szabad a boncteremből közvetlenül átmenniük a szülőszobába.",
                        "english": "The doctors should not have gone directly from the autopsy room into the delivery room."
                    },
                    {
                        "spanish": "A gyermekágyi láz áldozatainak többségét meg lehetett volna menteni klórvizes kézmosással.",
                        "english": "The majority of the victims of childbed fever could have been saved with chlorinated handwashing."
                    },
                    {
                        "spanish": "A klinika vezetésének azonnal támogatnia kellett volna Semmelweis rendeletét.",
                        "english": "The clinic's leadership should have immediately supported Semmelweis's decree."
                    }
                ],
                "tip": "When a preverb climbs before lehetett volna or kellett volna, write it as a separate word before the modal: meg lehetett volna menteni (never *meglehetett volna menteni)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi okozta Semmelweis Ignác felismerése szerint a gyermekágyi láz járványos terjedését az első osztályon?",
                    "options": [
                        "Az orvosok és medikusok a boncteremből a kezükön vitték át a fertőző anyagokat a kismamákra.",
                        "A kórház ablakait túl gyakran nyitották ki tavasszal.",
                        "A szülésznők túl sok klórvizet használtak a második osztályon."
                    ],
                    "correct": 0,
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A klórvizes kézmosás bevezetése után a _____ néhány hét alatt egy százalék alá csökkent. (mortality rate — two words)",
                    "answer": "halálozási arány",
                    "english": "After the introduction of chlorinated handwashing, the mortality rate dropped below one percent within a few weeks.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az orvosoknak minden vizsgálat előtt alaposan kezet _____ volna mosniuk. (should have)",
                    "answer": "kellett",
                    "english": "The doctors should have washed their hands thoroughly before every examination.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen: 'The tragedy could have been avoided'?",
                    "options": [
                        "A tragédiát el lehetett volna kerülni.",
                        "A tragédiát lehetett volna elkerülte.",
                        "A tragédiát elkerülni volna lehetett."
                    ],
                    "correct": 0,
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Édesanyák", "ezreinek", "az", "életét", "meg", "lehetett", "volna", "menteni", "a", "fertőtlenítéssel."],
                    "solution": ["Édesanyák", "ezreinek", "az", "életét", "meg", "lehetett", "volna", "menteni", "a", "fertőtlenítéssel."],
                    "english": "The lives of thousands of mothers could have been saved with disinfection.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik tragikus esemény vezette rá Semmelweist a gyermekágyi láz valódi okára 1847 tavaszán?",
                    "options": [
                        "Barátja, Kolletschka professzor boncolás közben megvágta az ujját, és a gyermekágyi lázzal azonos tünetekkel halt meg.",
                        "Leégett a bécsi Közkórház régi könyvtára.",
                        "Louis Pasteur személyesen látogatta meg a budai klinikát."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "szappanos", "víz", "helyett", "csak", "a", "klórvíz", "biztosított", "teljes", "fertőtlenítést."],
                    "solution": ["A", "szappanos", "víz", "helyett", "csak", "a", "klórvíz", "biztosított", "teljes", "fertőtlenítést."],
                    "english": "Instead of soapy water, only chlorine water ensured complete disinfection.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "State what doctors should not have done after autopsies using 'nem lett volna szabad'.",
                            "answer": "Az orvosoknak nem lett volna szabad fertőtlenítés nélkül a boncteremből a szülőszobába menniük."
                        },
                        {
                            "prompt": "Express how many lives could have been saved using 'meg lehetett volna menteni'.",
                            "answer": "A klórvizes kézmosás általános bevezetésével kismamák tízezreit meg lehetett volna menteni Európában."
                        }
                    ],
                    "teaches": ["b2-past-modals"]
                }
            ]
        },
        {
            "num": 2,
            "title": "Why the Medical Establishment Refused to Listen",
            "grammar_label": "Potential suffix in past conditional: verb + -hatott/-hetett volna",
            "goals": [
                "I can explain the psychological and institutional reasons behind the Semmelweis reflex—why 19th-century physicians rejected Semmelweis's evidence.",
                "I can form and use the inflected past conditional potential (-hatott/-hetett volna) for both missed agency and counterfactual outcomes.",
                "I can discuss institutional inertia, clinical statistics, and medical orthodoxy in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szakmaiellenallas",
                "title": "Miért utasította el a szakma az igazságot?",
                "summary": "Despite irrefutable statistical proof, senior European obstetricians rejected Semmelweis's discovery because accepting it meant admitting their own unwashed hands had caused the deaths of their patients.",
                "location": "Bécs és Pest (Szent Rókus Kórház)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Logikusnak tűnt volna, hogy Semmelweis drámai statisztikai eredményei láttán Európa összes szülészeti klinikája azonnal átvegye a klórvizes kézmosást. A valóságban azonban éppen az ellenkezője történt. A bécsi klinika konzervatív vezetője, Johann Klein professzor — aki maga is a régi elméletek híve volt — gyanakvással figyelte magyar beosztottját, és 1849-ben nem hosszabbította meg Semmelweis tanársegédi szerződését. Pedig ha a korabeli orvosi kar nyitottabban fogadja az adatokat, a kórházi fertőzések történetét évtizedekkel korábban átírhatták volna."
                    },
                    {
                        "type": "narration",
                        "text": "Miért álltak ellen olyan makacsul a kor tekintélyes professzorai? Egyrészt a mikrobiológia korszaka előtt az orvosok nehezen tudták elképzelni, hogy láthatatlan részecskék okozhatnak halálos betegséget. Másrészt — és ez volt a súlyosabb lélektani akadály — Semmelweis elmélete kimondta, hogy maguk a tiszteletre méltó doktorok hordozták a halált a kezükön. Sok főorvos egyszerűen nem volt képes szembenézni a gondolattal, hogy saját mulasztása miatt halhattak meg a rá bízott betegek."
                    },
                    {
                        "type": "narration",
                        "text": "Semmelweis maga is hozzájárult a késedelemhez azzal, hogy több mint tíz éven át halogatta eredményei részletes, könyv alakban történő megjelentetését. Ha már 1848-ban megírja fő művét, és nyugodt, tárgyszerű hangnemben válaszol a kétkedőknek, talán könnyebben meggyőzhette volna a nemzetközi tudományos közvéleményt. Amikor végül 1861-ben megjelent nagy könyve, A gyermekágyi láz kóroktana, a szakmai elutasítás annyira elkeserítette, hogy nyílt leveleiben már „orvosi Néróknak” és gyilkosoknak nevezte bírálóit."
                    },
                    {
                        "type": "narration",
                        "text": "Pestre visszatérve a Szent Rókus Kórházban, majd a pesti egyetemi klinikán ismét bebizonyította igazát: a halálozást itt is egy százalék alá szorította le. Ám a szakmai elszigeteltség és a folyamatos küzdelem felőrölte az idegrendszerét. 1865 nyarán elmegyógyintézetbe zárták Bécs mellett, ahol két héttel később — tragikus iróniával éppen egy elfertőződött seb következtében, vérmérgezésben — meghalt."
                    },
                    {
                        "type": "narration",
                        "text": "A tudománytörténet ma „Semmelweis-reflexnek” nevezi azt a jelenséget, amikor egy intézményrendszer automatikusan, a bizonyítékok mérlegelése nélkül elutasít egy új felfedezést, pusztán azért, mert az ellentmond a fennálló dogmáknak."
                    }
                ]
            },
            "words": [
                {"lemma": "kóroktan", "translation": "etiology (study of the causes of disease)", "pos": "noun"},
                {"lemma": "vérmérgezés", "translation": "sepsis / blood poisoning", "pos": "noun"},
                {"lemma": "mulasztás", "translation": "negligence / omission", "pos": "noun"},
                {"lemma": "statisztikai bizonyíték", "translation": "statistical evidence", "pos": "noun"},
                {"lemma": "dogma", "translation": "dogma / entrenched orthodoxy", "pos": "noun"},
                {"lemma": "meggyőzhetett volna", "translation": "could have convinced", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "past-potential-hatott-hetett-volna",
                "title": "Inflected Past Potential Modals: Verb + -hatott/-hetett volna",
                "text1_title": "Personal Agency vs. Impersonal Possibility",
                "text1": "Whereas lehetett volna + infinitive is impersonal ('one could have / it could have been done'), attaching the potential suffix -hat/-het directly to the verb in the past conditional (verb + -hatott/-hetett + personal ending + volna) attributes the missed capability or opportunity to a specific grammatical subject: Semmelweis hamarabb is publikálhatta volna az eredményeit ('Semmelweis could have published his results earlier').",
                "text2_title": "Definite vs. Indefinite Conjugation in Past Modals",
                "text2": "Because verb + -hatott/-hetett volna is a fully inflected finite verb, it obeys standard Hungarian transitivity agreement! Use the indefinite forms (tanulhattam volna, segíthetett volna) when there is no definite object, and the definite forms (meggyőzhette volna a kollégáit, átírhatták volna a történelmet) when there is a definite direct object.",
                "table_title": "Past Potential (-hat/-het + Past + volna) Paradigm",
                "table_rows": [
                    ["Semmelweis korábban is megírhatta volna a könyvét. (Def.)", "Semmelweis could have written his book earlier."],
                    ["A professzorok ellenőrizhették volna az adatokat. (Def.)", "The professors could have verified the data."],
                    ["A betegek életben maradhattak volna. (Indef.)", "The patients could have remained alive."],
                    ["Miért halhattak meg annyian? (Epistemic past)", "Why might so many have died?"]
                ],
                "examples": [
                    {
                        "spanish": "Ha a korabeli orvosi kar nyitottabban fogadja az adatokat, évtizedekkel korábban átírhatták volna a kórházak történetét.",
                        "english": "If the contemporary medical faculty had received the data more openly, they could have rewritten the history of hospitals decades earlier."
                    },
                    {
                        "spanish": "Ha Semmelweis nyugodt hangnemben válaszol a kétkedőknek, könnyebben meggyőzhette volna a nemzetközi közvéleményt.",
                        "english": "If Semmelweis had answered the skeptics in a calm tone, he could have convinced international opinion more easily."
                    },
                    {
                        "spanish": "Sok főorvos nem tudott szembenézni azzal, hogy saját mulasztása miatt halhattak meg a betegek.",
                        "english": "Many chief physicians could not face the thought that the patients might have died because of their own negligence."
                    }
                ],
                "tip": "In Hungarian counterfactual if-clauses (If X had done Y, Z could have happened), the ha-clause can use either the past conditional (Ha megírta volna...) or, in vivid B2 historical narrative, the present indicative (Ha már 1848-ban megírja fő művét, meggyőzhette volna őket)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit nevez a modern tudományfilozófia és pszichológia 'Semmelweis-reflexnek'?",
                    "options": [
                        "Azt a jelenséget, amikor a szakmai közösség a bizonyítékok ellenére automatikusan elutasít egy új felismerést, mert az sérti a megszokott dogmákat.",
                        "A klórvíz hatására fellépő allergiás bőrpírt.",
                        "Azt a sebészeti eljárást, amellyel a csonttöréseket gyógyították."
                    ],
                    "correct": 0,
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Semmelweis 1861-ben megjelent fő műve a gyermekágyi láz _____ címet viselte. (etiology / study of causes of disease)",
                    "answer": "kóroktana",
                    "english": "Semmelweis's magnum opus published in 1861 bore the title 'The Etiology of Childbed Fever'.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Ha Semmelweis korábban kiadja a könyvét, könnyebben _____ volna a külföldi orvosokat. (could have convinced — definite 3sg)",
                    "answer": "meggyőzhette",
                    "english": "If Semmelweis had published his book earlier, he could have convinced foreign doctors more easily.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban helyes a határozott ragozású múlt idejű ható igealak?",
                    "options": [
                        "A bécsi professzorok maguk is ellenőrizhették volna a statisztikai adatokat.",
                        "A bécsi professzorok maguk is ellenőrizhettek volna a statisztikai adatokat.",
                        "A bécsi professzorok maguk is ellenőrizni lehetett volna az adatokat."
                    ],
                    "correct": 0,
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "kórházak", "már", "1848-ban", "bevezethették", "volna", "a", "kötelező", "kézfertőtlenítést."],
                    "solution": ["A", "kórházak", "már", "1848-ban", "bevezethették", "volna", "a", "kötelező", "kézfertőtlenítést."],
                    "english": "Hospitals could have introduced mandatory hand disinfection as early as 1848.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mi volt a legfőbb lélektani oka annak, hogy a vezető főorvosok elutasították Semmelweis elméletét?",
                    "options": [
                        "Az elmélet elfogadása egyet jelentett volna azzal a beismeréssel, hogy saját mosdatlan kezükkel ők maguk okozták a betegek halálát.",
                        "A klórmész túl drága volt a tizenkilencedik századi Ausztriában.",
                        "Semmelweis nem tudott semmilyen statisztikai adatot felmutatni."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "szakmai", "dogmák", "és", "a", "súlyos", "mulasztás", "ezrek", "életébe", "került."],
                    "solution": ["A", "szakmai", "dogmák", "és", "a", "súlyos", "mulasztás", "ezrek", "életébe", "került."],
                    "english": "Professional dogmas and grave negligence cost thousands of lives.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain what the Vienna hospital directors could have done in 1848 using 'átvehették volna'.",
                            "answer": "A bécsi kórházigazgatók már 1848-ban átvehették volna Semmelweis életmentő módszerét."
                        },
                        {
                            "prompt": "Reflect on how Semmelweis could have communicated differently using 'meggyőzhette volna'.",
                            "answer": "Ha Semmelweis korábban és higgadtabban publikál, talán gyorsabban meggyőzhette volna a kétkedő tudósokat."
                        }
                    ],
                    "teaches": ["b2-past-modals"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Szent-Györgyi Albert and the Szeged Laboratory",
            "grammar_label": "Epistemic past deduction: kellett, hogy + subjunctive and biztosan -hatott/-hetett",
            "goals": [
                "I can narrate how Albert Szent-Györgyi isolated vitamin C from Szeged paprika and won the 1937 Nobel Prize.",
                "I can express logical deduction about the past using epistemic modals (-hatott/-hetett, kellett, hogy + subjunctive).",
                "I can discuss biochemistry, cellular respiration, and scientific intuition in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szentgyorgyiszeged",
                "title": "Szent-Györgyi Albert és a szegedi paprika",
                "summary": "Returning to Hungary in 1930 to chair the biochemistry department at the University of Szeged, Albert Szent-Györgyi discovered that the local red pepper was a treasure trove of vitamin C, earning the 1937 Nobel Prize in Physiology or Medicine.",
                "location": "Cambridge és Szeged",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Szent-Györgyi Albert életútja merőben eltért Semmelweis tragikus sorsától, jóllehet a tudományos kételkedéssel neki is meg kellett küzdenie. Az 1920-as években Hollandiában és Cambridge-ben a sejtlégzés biokémiai folyamatait vizsgálta, és sikerült kivonnia a mellékveséből egy ismeretlen, erősen redukáló hatású vegyületet, a hexuronsavat. Amikor első cikkében tréfásan „ignóznak” (nem tudom milyen cukornak) nevezte el az anyagot, a tekintélyes biokémiai folyóirat szerkesztője visszadobta a nevet, mondván, hogy komoly tudós nem viccelődhet a szakirodalomban."
                    },
                    {
                        "type": "narration",
                        "text": "A cambridge-i laboratóriumban azonban alig néhány grammnyi hexuronsavat tudott előállítani, így nem igazolhatta volna egyértelműen, hogy ez az anyag azonos a skorbutot gyógyító C-vitaminnal. A fordulatot az hozta el, amikor Klebelsberg Kuno kultuszminiszter meghívására 1930-ban hazatért Magyarországra, és átvette a szegedi egyetem orvosi vegytani intézetének vezetését. Szegednek különleges természeti kincse volt: a világhírű fűszerpaprika."
                    },
                    {
                        "type": "narration",
                        "text": "A híres anekdota szerint egy őszi estén Szent-Györgyi felesége friss paprikasalátát tett a vacsoraasztalra. A professzornak nem volt kedve megenni a paprikát, ám hirtelen eszébe jutott, hogy ezt a növényt még soha nem vizsgálta meg a laboratóriumban. Még azon az éjszakán elemzésnek vetette alá a zöldséget, és döbbenten tapasztalta, hogy a szegedi paprika valóságos C-vitamin-bánya: egyetlen hét alatt több kilónyi tiszta kristályos aszkorbinsavat tudtak kivonni belőle, mint korábban évek alatt."
                    },
                    {
                        "type": "narration",
                        "text": "Szent-Györgyi azonnal szétküldte a szegedi aszkorbinsavat a világ vezető laboratóriumaiba, hogy a kollégák is elvégezhessék a kísérleteket. 1937-ben a Svéd Királyi Tudományos Akadémia neki ítélte az orvosi-élettani Nobel-díjat a biológiai égésfolyamatok, különösen a C-vitamin és a fumársav-katalízis szerepének felfedezéséért — ő volt az egyetlen magyar tudós, aki hazai egyetemen végzett kutatásáért vette át a díjat."
                    },
                    {
                        "type": "narration",
                        "text": "A szegedi laboratórium szellemi pezsgése ezzel nem ért véget: Szent-Györgyi és fiatal munkatársa, Straub F. Brunó itt fedezték fel az izom-összehúzódás alapvető fehérjéit, az aktint és a miozint is. Szent-Györgyi hitvallása az volt, hogy a felfedezés lényege „látni azt, amit mindenki lát, és gondolni azt, amit még senki sem gondolt”."
                    }
                ]
            },
            "words": [
                {"lemma": "biokémia", "translation": "biochemistry", "pos": "noun"},
                {"lemma": "sejtlégzés", "translation": "cellular respiration", "pos": "noun"},
                {"lemma": "aszkorbinsav", "translation": "ascorbic acid (vitamin C)", "pos": "noun"},
                {"lemma": "vegyület", "translation": "chemical compound", "pos": "noun"},
                {"lemma": "kivon", "translation": "to extract / isolate", "pos": "verb"},
                {"lemma": "skorbut", "translation": "scurvy", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "epistemic-past-deduction",
                "title": "Epistemic Past Modals and Counterfactual Prerequisites",
                "text1_title": "Epistemic Deduction with -hatott/-hetett (Without volna)",
                "text1": "Carefully distinguish between -hatott/-hetett VOLNA ('could have done [but didn't]') and -hatott/-hetett WITHOUT volna ('must/may have done [logical probability about the past]'). For example: Szent-Györgyi óriási izgalmat érezhetett azon az éjszakán ('Szent-Györgyi must have felt enormous excitement that night') expresses high probability about what actually happened.",
                "text2_title": "Counterfactual Negation: nem igazolhatta volna",
                "text2": "When describing what a scientist could NOT have achieved without a specific breakthrough, Hungarian combines a negative condition (a szegedi paprika nélkül...) with the negative past conditional modal (nem tudta volna kivonni / nem igazolhatta volna).",
                "table_title": "Epistemic Probability vs. Counterfactual Modality",
                "table_rows": [
                    ["Szent-Györgyi nagy meglepetést érezhetett. (No volna = probability)", "Szent-Györgyi must/may have felt great surprise."],
                    ["Paprika nélkül nem állíthatott volna elő több kilót. (With volna = counterfactual)", "Without paprika he could not have produced several kilos."],
                    ["Cambridge-ben évekig kellett volna dolgoznia ugyanazért a mennyiségért.", "In Cambridge he would have had to work for years for the same quantity."]
                ],
                "examples": [
                    {
                        "spanish": "A szegedi fűszerpaprika nélkül Szent-Györgyi nem tudott volna néhány nap alatt több kilónyi tiszta C-vitamint előállítani.",
                        "english": "Without Szeged paprika, Szent-Györgyi could not have produced several kilos of pure vitamin C within a few days."
                    },
                    {
                        "spanish": "Micsoda örömöt érezhettek a szegedi kutatók, amikor meglátták a kristályos aszkorbinsavat!",
                        "english": "What joy the Szeged researchers must have felt when they saw the crystalline ascorbic acid!"
                    },
                    {
                        "spanish": "Klebelsberg Kuno támogatása nélkül a szegedi egyetem nem válhatott volna világszínvonalú biokémiai központtá.",
                        "english": "Without Kuno Klebelsberg's support, the University of Szeged could not have become a world-class biochemical center."
                    }
                ],
                "tip": "Pay close attention to volna: érezhetett = 'he probably felt' (real past deduction); érezhetett volna = 'he could have felt' (unreal counterfactual)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Miért jelentett óriási áttörést a szegedi paprika vizsgálata Szent-Györgyi Albert kutatásában?",
                    "options": [
                        "Mert a paprikából néhány nap alatt több kilónyi tiszta aszkorbinsavat (C-vitamint) tudtak kivonni.",
                        "Mert a paprika csípőssége meggyógyította a gyermekágyi lázat.",
                        "Mert a paprikából vonták ki először a penicillint."
                    ],
                    "correct": 0,
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A C-vitamin tudományos neve _____, amely megelőzi és gyógyítja a skorbutot. (ascorbic acid)",
                    "answer": "aszkorbinsav",
                    "english": "The scientific name of vitamin C is ascorbic acid, which prevents and cures scurvy.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A szegedi paprika nélkül Szent-Györgyi nem _____ volna elegendő C-vitamint küldeni a külföldi laboratóriumoknak. (could [not] have been able — tudott)",
                    "answer": "tudott",
                    "english": "Without Szeged paprika, Szent-Györgyi could not have sent enough vitamin C to foreign laboratories.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Mi a jelentésbeli különbség az 'érezhetett' és az 'érezhetett volna' között?",
                    "options": [
                        "Az 'érezhetett' múltbeli valószínűséget (bizonyára érzett), az 'érezhetett volna' pedig meg nem valósult lehetőséget fejez ki.",
                        "Mindkettő jövő idejű parancsot fejez ki.",
                        "Az 'érezhetett volna' azt jelenti, hogy biztosan megtörtént az esemény."
                    ],
                    "correct": 0,
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "szegedi", "laboratórium", "nélkül", "ez", "a", "felfedezés", "éveket", "késhetett", "volna."],
                    "solution": ["A", "szegedi", "laboratórium", "nélkül", "ez", "a", "felfedezés", "éveket", "késhetett", "volna."],
                    "english": "Without the Szeged laboratory, this discovery could have been delayed by years.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen másik alapvető biokémiai felfedezés született Szent-Györgyi szegedi intézetében Straub F. Brunóval közösen?",
                    "options": [
                        "Az izom-összehúzódásért felelős fehérjék, az aktin és a miozin felfedezése.",
                        "A DNS kettős spiráljának röntgensugaras lefényképezése.",
                        "Az első elektronikus mikroszkóp megépítése."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Szent-Györgyi", "Albert", "a", "sejtlégzés", "és", "a", "C-vitamin", "kutatásáért", "kapott", "Nobel-díjat."],
                    "solution": ["Szent-Györgyi", "Albert", "a", "sejtlégzés", "és", "a", "C-vitamin", "kutatásáért", "kapott", "Nobel-díjat."],
                    "english": "Albert Szent-Györgyi received the Nobel Prize for his research on cellular respiration and vitamin C.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "State what Szent-Györgyi could not have done in Cambridge without Szeged paprika using 'nem tudott volna'.",
                            "answer": "A szegedi paprika nélkül Szent-Györgyi Cambridge-ben nem tudott volna néhány nap alatt több kilónyi aszkorbinsavat kivonni."
                        },
                        {
                            "prompt": "Express a deduction about how surprised Szent-Györgyi must have been that evening using '-hatott/-hetett' (without volna).",
                            "answer": "Szent-Györgyi óriási meglepetést érezhetett, amikor az éjszakai kísérlet során kimutatta a paprikában a rengeteg C-vitamint."
                        }
                    ],
                    "teaches": ["b2-past-modals"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Katalin Karikó: Persistence Against Skepticism",
            "grammar_label": "Counterfactual persistence: feladhatta volna, de ... and ha nem + past, nem + past conditional",
            "goals": [
                "I can trace Katalin Karikó's journey from Szeged to the University of Pennsylvania and the 2023 Nobel Prize.",
                "I can contrast counterfactual surrender with actual perseverance using feladhatta volna, de ... and counterfactual conditionals.",
                "I can discuss mRNA technology, immune response, and research funding in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "karikokatalin",
                "title": "Karikó Katalin: Kitartás a kételkedéssel szemben",
                "summary": "Trained at the Biological Research Centre in Szeged, biochemist Katalin Karikó endured rejected grants and university demotion in the 1990s before solving the inflammatory bottleneck of mRNA with Drew Weissman.",
                "location": "Kisújszállás, Szeged és Philadelphia",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A szegedi biokémiai hagyomány fél évszázaddal Szent-Györgyi Albert után újabb világtörténelmi áttörés kiindulópontjává vált. A Kisújszálláson felnőtt Karikó Katalin a szegedi József Attila Tudományegyetemen szerzett biológusi diplomát, majd a Szegedi Biológiai Központban kezdte meg kutatásait a hírvivő ribonukleinsav, azaz az mRNS területén. Amikor 1985-ben férjével és kislányával az Egyesült Államokba indult, minden megtakarításukat — a régi autójuk árából kapott alig ezer fontot — a kislánya játékmackójába varrva vitték magukkal."
                    },
                    {
                        "type": "narration",
                        "text": "A kilencvenes években a Pennsylvaniai Egyetemen Karikó szinte teljesen magára maradt azzal a meggyőződésével, hogy az mRNS segítségével az emberi sejteket gyógyító fehérjék előállítására lehetne megtanítani. A pályázati bizottságok sorra elutasították a kérelmeit, mert a molekulát túlságosan bomlékonynak és veszélyesen gyulladáskeltőnek tartották. 1995-ben az egyetem vezetése válaszút elé állította: vagy felhagy az mRNS-kutatással, vagy visszaminősítik az állásában és csökkentik a fizetését. Sok más kutató ebben a helyzetben feladhatta volna az álmát, Karikó azonban a laboratóriumi munkát választotta a rang helyett."
                    },
                    {
                        "type": "narration",
                        "text": "A sorsfordító találkozásra 1997-ben, az egyetemi fénymásoló gép mellett került sor, ahol megismerkedett Drew Weissman immunológussal. Ha azon a napon nem elegyednek beszélgetésbe a fénymásolónál, talán évekkel később találják csak meg a megoldást az mRNS legnagyobb rejtélyére: miért vált ki a mesterségesen előállított mRNS heves immunreakciót a szervezetben?"
                    },
                    {
                        "type": "narration",
                        "text": "Évekig tartó módszeres kísérletezéssel rájöttek, hogy amennyiben az mRNS egyik építőkövét, az uridint egy módosított változatra, pszeudouridinra cserélik, a molekula észrevétlenül, gyulladás kiváltása nélkül jut be a sejtekbe, és ott nagy mennyiségű fehérjét termel. Amikor 2005-ben beküldték sorsdöntő cikküket a Nature folyóiratnak, a szerkesztők huszonnégy órán belül elutasították, mert „nem tartották elég jelentősnek”."
                    },
                    {
                        "type": "narration",
                        "text": "Tizenöt évvel később, a 2020-as világjárvány idején pontosan ez a nukleozid-módosítási eljárás tette lehetővé a modern mRNS-alapú védőoltások rekordidő alatti kifejlesztését. 2023-ban Karikó Katalin és Drew Weissman átvehette az orvosi-élettani Nobel-díjat — igazolva, hogy a valódi tudományos kíváncsiság erősebb minden intézményi akadálytalanításnál és kételkedésnél."
                    }
                ]
            },
            "words": [
                {"lemma": "hírvivő RNS", "translation": "messenger RNA (mRNA)", "pos": "noun"},
                {"lemma": "immunreakció", "translation": "immune response", "pos": "noun"},
                {"lemma": "gyulladáskeltő", "translation": "inflammatory", "pos": "adjective"},
                {"lemma": "pályázat", "translation": "research grant application / tender", "pos": "noun"},
                {"lemma": "védőoltás", "translation": "vaccine", "pos": "noun"},
                {"lemma": "feladhatta volna", "translation": "could have given it up", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "counterfactual-persistence-modals",
                "title": "Contrasting Counterfactual Surrender with Real Action: -hatott volna, de ...",
                "text1_title": "Rhetorical Contrast: What Could Have Happened vs. What Did Happen",
                "text1": "In biographical and historical narratives, B2 speakers often highlight a protagonist's moral courage by stating the easy path they *could have taken* (verb + -hatott/-hetett volna) and immediately contrasting it with their actual past indicative choice after de or azonban: Karikó feladhatta volna a kutatást, ő azonban tovább dolgozott ('Karikó could have given up the research, yet she worked on').",
                "text2_title": "Negative Counterfactual Chains: Ha nem + Past ..., nem + Past Conditional",
                "text2": "To emphasize that a historical turning point was indispensable ('Had X not happened, Y could not have occurred'), pair a negative ha-clause with a past modal in the main clause: Ha Karikó és Weissman nem módosítják az uridint, nem készülhettek volna el időben az mRNS-alapú védőoltások.",
                "table_title": "Biographical Counterfactual Contrasts",
                "table_rows": [
                    ["Sok más kutató feladhatta volna az álmát, ő azonban kitartott.", "Many other researchers might have given up their dream, but she persevered."],
                    ["Választhatta volna a biztos karriert, de az alapkutatást választotta.", "She could have chosen a safe career, but chose basic research."],
                    ["Ha 2005-ben nem publikálják az eljárást, 2020-ban nem készülhetett volna el a vakcina.", "Had they not published the method in 2005, the vaccine could not have been made in 2020."]
                ],
                "examples": [
                    {
                        "spanish": "Sok más kutató ebben a helyzetben feladhatta volna a kísérleteket, Karikó Katalin azonban tovább dolgozott.",
                        "english": "Many other researchers in this situation might have given up the experiments, yet Katalin Karikó continued working."
                    },
                    {
                        "spanish": "Ha nem cserélik ki az uridint pszeudouridinra, az mRNS nem juthatott volna be gyulladás nélkül a sejtekbe.",
                        "english": "Had they not replaced uridine with pseudouridine, the mRNA could not have entered the cells without inflammation."
                    },
                    {
                        "spanish": "A pályázati bizottságoknak már a kilencvenes években támogatniuk kellett volna az mRNS-kutatást.",
                        "english": "The grant committees should have supported mRNA research back in the 1990s."
                    }
                ],
                "tip": "Notice the definite object agreement on feladhatta volna (because az álmát / a kutatást is definite) vs. indefinite lemondhatott volna a rangról (because -ról/-ről is an oblique case, not a direct object)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt az a kulcsfontosságú biokémiai felfedezés, amelyet Karikó Katalin és Drew Weissman 2005-ben publikált?",
                    "options": [
                        "Az uridin kicserélése pszeudouridinra megszünteti a mesterséges mRNS súlyos gyulladáskeltő immunreakcióját.",
                        "A C-vitamin nagy mennyiségben található meg a szegedi paprikában.",
                        "A klórvíz elpusztítja a boncteremből származó baktériumokat."
                    ],
                    "correct": 0,
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A kilencvenes években a bírálók azért utasították el a _____ kérelmeket, mert az mRNS-t túl bomlékonynak tartották. (grant application)",
                    "answer": "pályázati",
                    "english": "In the nineties, reviewers rejected the grant applications because they considered mRNA too unstable.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Sok más kutató _____ volna a munkát a visszaminősítés után, Karikó azonban kitartott. (could have given it up — definite 3sg)",
                    "answer": "feladhatta",
                    "english": "Many other researchers could have given up the work after the demotion, yet Karikó persevered.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Válaszd ki a helyes múlt idejű feltételes mondatot!",
                    "options": [
                        "Ha Karikó nem tart ki az elmélete mellett, a modern mRNS-védőoltások nem készülhettek volna el 2020-ban.",
                        "Ha Karikó nem tart ki az elmélete mellett, a modern védőoltások nem készültek el volna.",
                        "Ha Karikó nem tartott ki, a védőoltások nem lehetett elkészülni."
                    ],
                    "correct": 0,
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Választhatta", "volna", "a", "könnyebb", "utat,", "ő", "azonban", "hű", "maradt", "a", "kutatáshoz."],
                    "solution": ["Választhatta", "volna", "a", "könnyebb", "utat,", "ő", "azonban", "hű", "maradt", "a", "kutatáshoz."],
                    "english": "She could have chosen the easier path, yet she remained faithful to her research.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan reagált a Nature folyóirat szerkesztősége 2005-ben Karikó és Weissman sorsdöntő kéziratára?",
                    "options": [
                        "Huszonnégy órán belül elutasították, mert akkoriban nem tartották elég jelentősnek az eredményt.",
                        "Azonnal a címlapon közölték, és nemzetközi sajtótájékoztatót hívtak össze.",
                        "Kérték, hogy fordítsák le a cikket latin nyelvre."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "módosított", "hírvivő", "RNS", "nem", "váltott", "ki", "káros", "immunreakciót", "a", "sejtekben."],
                    "solution": ["A", "módosított", "hírvivő", "RNS", "nem", "váltott", "ki", "káros", "immunreakciót", "a", "sejtekben."],
                    "english": "The modified messenger RNA did not trigger a harmful immune response in the cells.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Contrast what Karikó could have done in 1995 with what she actually did using 'feladhatta volna..., de'.",
                            "answer": "Karikó Katalin 1995-ben feladhatta volna az mRNS-kutatást a visszaminősítés miatt, de ő a laboratóriumi munkát választotta."
                        },
                        {
                            "prompt": "Explain why the 2005 discovery was essential using 'Ha nem fedezik fel..., nem készülhettek volna el...'.",
                            "answer": "Ha nem fedezik fel a nukleozid-módosítást, nem készülhettek volna el rekordidő alatt az életmentő védőoltások."
                        }
                    ],
                    "teaches": ["b2-past-modals"]
                }
            ]
        },
        {
            "num": 5,
            "title": "Science, Ethics, and Public Trust",
            "grammar_label": "Synthesizing past modals in historical and bioethical evaluation",
            "goals": [
                "I can compare the historical trajectories of Semmelweis, Szent-Györgyi, and Karikó regarding institutional trust and peer review.",
                "I can combine kellett volna, lehetett volna, and -hatott/-hetett volna to evaluate past policies and ethical responsibilities.",
                "I can discuss peer review, public health communication, and scientific humility in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "orvosietika",
                "title": "Tudomány, etika és közbizalom",
                "summary": "Comparing the fates of Semmelweis, Szent-Györgyi, and Karikó reveals a timeless lesson for medical ethics: institutions must balance rigorous verification with intellectual humility so life-saving ideas are not silenced.",
                "location": "Budapest, Szeged és a nemzetközi tudományos élet",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ha egymás mellé állítjuk Semmelweis Ignác, Szent-Györgyi Albert és Karikó Katalin életútját, közel kétszáz év magyar és egyetemes orvostörténete rajzolódik ki előttünk. Mindhárman olyan problémával szembesültek, amelyet a korabeli fősodor vagy megoldhatatlannak, vagy érdemtelennek tartott a vizsgálatra. A történelem visszapillantó tükrében ma már világosan látjuk, mit kellett volna másképp tenniük a korabeli intézményeknek, és hogyan lehetett volna elkerülni az évtizedes késedelmeket."
                    },
                    {
                        "type": "narration",
                        "text": "Semmelweis esetében a szakmai gőg és a tekintélyelvűség szó szerint emberéletek tízezreibe került. A tizenkilencedik századi klinikaigazgatóknak félre kellett volna tenniük a személyes hiúságukat, és pusztán a kísérleti számok alapján el kellett volna rendelniük a fertőtlenítést. Ugyanakkor Semmelweis tragédiája arra is figyelmeztet, hogy a tudományos igazság önmagában nem mindig elég: a felfedezőnek türelmes érveléssel és pontos publikációkkal kell hidat építenie a kétkedő közösség felé."
                    },
                    {
                        "type": "narration",
                        "text": "Szent-Györgyi Albert és Karikó Katalin példája egy másik intézményi tanulságot világít meg: a tudományos finanszírozás rövidlátását. A pályázati rendszerek gyakran csak azokat a kutatásokat támogatják, amelyek gyors és kiszámítható hasznot ígérnek. Ha a tudománypolitika kizárólag a pillanatnyi divatokra hallgat, a legfontosabb alapkutatások elsorvadhatnak. A bírálóknak látniuk kellett volna, hogy a látszólag sikertelen kísérletek is értékes tudást halmoznak fel."
                    },
                    {
                        "type": "narration",
                        "text": "A huszonegyedik században az orvostudománynak egy új kihívással is szembe kell néznie: a társadalmi közbizalom megőrzésével. Egy életmentő eljárás vagy védőoltás csak akkor érheti el a célját, ha az orvosok és a kutatók őszintén, közérthetően és alázattal kommunikálnak a nyilvánossággal. Sok félreértést meg lehetett volna előzni, ha a tudományos intézmények mindig nyíltan elmagyarázzák, hogyan működik a kísérleti bizonyítás folyamata."
                    },
                    {
                        "type": "narration",
                        "text": "A klórvizes mosdótáltól a szegedi paprikán át a módosított mRNS-ig ívelő történet végső üzenete közös: a tudomány igazi motorja a rendíthetetlen kíváncsiság és az emberi élet védelme iránti elkötelezettség."
                    }
                ]
            },
            "words": [
                {"lemma": "közbizalom", "translation": "public trust", "pos": "noun"},
                {"lemma": "tekintélyelvűség", "translation": "authoritarianism / reliance on authority", "pos": "noun"},
                {"lemma": "alázat", "translation": "humility", "pos": "noun"},
                {"lemma": "rövidlátás", "translation": "short-sightedness / myopia", "pos": "noun"},
                {"lemma": "fősodor", "translation": "mainstream", "pos": "noun"},
                {"lemma": "meg lehetett volna előzni", "translation": "could have been prevented", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "synthesizing-past-modals-in-evaluation",
                "title": "Synthesizing Past Modals in Historical and Bioethical Evaluation",
                "text1_title": "Choosing the Right Past Modal for the Nuance",
                "text1": "When evaluating historical episodes at B2 level, you have three complementary tools: (1) Dative + kellett volna + infinitive for moral/professional duty (A vezetőknek félre kellett volna tenniük a hiúságukat); (2) lehetett volna + infinitive for general systemic feasibility (Sok félreértést meg lehetett volna előzni); and (3) Subject + -hatott/-hetett volna for personal agency or counterfactual consequence (A kutatások elsorvadhattak volna).",
                "text2_title": "Preverb Climbing with Multi-Word Infinitives",
                "text2": "Remember that separable preverbs (félre-, el-, meg-, be-) climb in front of kellett volna and lehetett volna in neutral affirmative sentences: félre kellett volna tenniük ('they should have set aside'), meg lehetett volna előzni ('it could have been prevented'). In negative sentences, however, nem takes the focus slot and the preverb stays attached to the infinitive: nem lehetett volna megelőzni.",
                "table_title": "Affirmative vs. Negative Preverb Placement with Past Modals",
                "table_rows": [
                    ["A tragédiát meg lehetett volna előzni. (Affirmative: preverb climbs)", "The tragedy could have been prevented."],
                    ["A tragédiát nem lehetett volna megelőzni. (Negative: nem is in focus)", "The tragedy could not have been prevented."],
                    ["Félre kellett volna tenniük a hiúságukat. (Affirmative: preverb climbs)", "They should have set aside their vanity."],
                    ["Nem lett volna szabad elutasítaniuk az adatokat. (Negative: nem is in focus)", "They should not have rejected the data."]
                ],
                "examples": [
                    {
                        "spanish": "A klinikaigazgatóknak félre kellett volna tenniük a személyes hiúságukat, és el kellett volna rendelniük a fertőtlenítést.",
                        "english": "The clinic directors should have set aside their personal vanity and ordered disinfection."
                    },
                    {
                        "spanish": "Sok félreértést meg lehetett volna előzni őszinte és közérthető tájékoztatással.",
                        "english": "Many misunderstandings could have been prevented with honest and accessible communication."
                    },
                    {
                        "spanish": "A bírálóknak látniuk kellett volna, hogy az alapkutatás hosszú távon felbecsülhetetlen értéket teremt.",
                        "english": "The reviewers should have seen that basic research creates inestimable value in the long run."
                    }
                ],
                "tip": "Master the contrast between affirmative meg lehetett volna előzni (preverb climbs) and negative nem lehetett volna megelőzni (nem blocks preverb climbing)!"
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen veszélyre figyelmeztet Karikó Katalin korai pályafutása a tudományfinanszírozással kapcsolatban?",
                    "options": [
                        "A pályázati rövidlátásra, amely gyakran elutasítja a merész, hosszú távú alapkutatásokat a gyors haszon reményében.",
                        "Arra, hogy a kutatóknak túl sok szabadidőt adnak az egyetemeken.",
                        "Arra, hogy a biokémiai kísérletekhez nincs szükség laboratóriumokra."
                    ],
                    "correct": 0,
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Az orvostudomány eredményeinek elfogadásához nélkülözhetetlen a társadalmi _____ és a nyílt kommunikáció. (public trust)",
                    "answer": "közbizalom",
                    "english": "Social public trust and open communication are indispensable for the acceptance of medical science's results.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A professzoroknak _____ kellett volna tenniük a szakmai gőgöt, és meg kellett volna vizsgálniuk a számokat. (aside — félretesz preverb climbing)",
                    "answer": "félre",
                    "english": "The professors should have set aside their professional arrogance and examined the numbers.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat szórendje helyes tagadás esetén?",
                    "options": [
                        "A klórvíz nélkül a járványt nem lehetett volna megállítani.",
                        "A klórvíz nélkül a járványt meg nem lehetett volna állítani.",
                        "A klórvíz nélkül a járványt nem megállítani lehetett volna."
                    ],
                    "correct": 0,
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Sok", "félreértést", "meg", "lehetett", "volna", "előzni", "őszinte", "tájékoztatással."],
                    "solution": ["Sok", "félreértést", "meg", "lehetett", "volna", "előzni", "őszinte", "tájékoztatással."],
                    "english": "Many misunderstandings could have been prevented with honest information.",
                    "teaches": ["b2-past-modals"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mi a közös vonás Semmelweis Ignác, Szent-Györgyi Albert és Karikó Katalin történetében a szöveg szerint?",
                    "options": [
                        "Mindhárman olyan úttörő felismerésért küzdöttek, amelyet a korabeli szakmai fősodor kezdetben kétkedéssel vagy elutasítással fogadott.",
                        "Mindhárman ugyanabban az évben születtek Budapesten.",
                        "Mindhárman a fizikai Nobel-díjat vették át Stockholmban."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "szakmai", "alázat", "és", "a", "kíváncsiság", "a", "tudományos", "haladás", "alapja."],
                    "solution": ["A", "szakmai", "alázat", "és", "a", "kíváncsiság", "a", "tudományos", "haladás", "alapja."],
                    "english": "Professional humility and curiosity are the foundation of scientific progress.",
                    "teaches": ["b2-semmelweis-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Evaluate what 19th-century clinic directors should have done using 'félre kellett volna tenniük'.",
                            "answer": "A tizenkilencedik századi klinikaigazgatóknak félre kellett volna tenniük a személyes hiúságukat a betegek védelmében."
                        },
                        {
                            "prompt": "State how many misunderstandings could have been prevented using 'meg lehetett volna előzni'.",
                            "answer": "A nyílt és közérthető tudományos párbeszéddel számos társadalmi félreértést meg lehetett volna előzni."
                        }
                    ],
                    "teaches": ["b2-past-modals"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can discuss the breakthroughs and institutional struggles of Ignác Semmelweis, Albert Szent-Györgyi, and Katalin Karikó.",
            "I can accurately form and use past deontic and dynamic modals (kellett volna, lehetett volna) including preverb climbing and negation.",
            "I can distinguish between counterfactual past potentials (-hatott/-hetett volna) and epistemic past deductions (-hatott/-hetett)."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban helyes az igekötő helye a múlt idejű 'lehetett volna' szerkezetben?",
                "options": [
                    "A fertőzést egyszerű klórvizes kézmosással meg lehetett volna előzni.",
                    "A fertőzést egyszerű klórvizes kézmosással lehetett volna megelőzni.",
                    "A fertőzést egyszerű klórvizes kézmosással megelőzni volna lehetett."
                ],
                "correct": 0,
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik magyar kutató kapott 1937-ben Nobel-díjat a C-vitamin és a sejtlégzés vizsgálatáért?",
                "options": [
                    "Szent-Györgyi Albert",
                    "Semmelweis Ignác",
                    "Wigner Jenő"
                ],
                "correct": 0,
                "teaches": ["b2-semmelweis-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igealak fejez ki múltbeli valószínűséget (és NEM meg nem történt lehetőséget)?",
                "options": [
                    "Szent-Györgyi hatalmas örömöt érezhetett a szegedi laboratóriumban.",
                    "Szent-Györgyi hatalmas örömöt érezhetett volna, ha kap paprikát.",
                    "Szent-Györgyinek örülnie kellett volna."
                ],
                "correct": 0,
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az orvosoknak minden vizsgálat előtt klórvízben _____ volna kezet mosniuk. (should have)",
                "answer": "kellett",
                "english": "The doctors should have washed their hands in chlorine water before every examination.",
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Semmelweis felismerte, hogy a boncteremből áthurcolt anyagok okozzák a halálos _____. (blood poisoning / sepsis — accusative)",
                "answer": "vérmérgezést",
                "english": "Semmelweis realized that substances carried over from the autopsy room caused the fatal blood poisoning.",
                "teaches": ["b2-semmelweis-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Karikó Katalin a visszaminősítés után _____ volna a kutatást, de ő tovább dolgozott. (could have given it up — definite 3sg)",
                "answer": "feladhatta",
                "english": "Katalin Karikó could have given up the research after the demotion, but she kept working.",
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bécsi", "klinikán", "édesanyák", "ezreit", "meg", "lehetett", "volna", "menteni."],
                "solution": ["A", "bécsi", "klinikán", "édesanyák", "ezreit", "meg", "lehetett", "volna", "menteni."],
                    "english": "At the Vienna clinic, thousands of mothers could have been saved.",
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "módosított", "hírvivő", "RNS", "alapozta", "meg", "az", "új", "védőoltásokat."],
                "solution": ["A", "módosított", "hírvivő", "RNS", "alapozta", "meg", "az", "új", "védőoltásokat."],
                "english": "Modified messenger RNA laid the foundation for the new vaccines.",
                "teaches": ["b2-semmelweis-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a tagadó múlt idejű lehetőséget?",
                "options": [
                    "A nukleozid-módosítás nélkül a vakcinát nem lehetett volna ilyen gyorsan kifejleszteni.",
                    "A nukleozid-módosítás nélkül a vakcinát ki nem lehetett volna fejleszteni.",
                    "A nukleozid-módosítás nélkül a vakcinát nem kifejleszteni lehetett volna."
                ],
                "correct": 0,
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bírálóknak", "már", "korábban", "támogatniuk", "kellett", "volna", "az", "alapkutatást."],
                "solution": ["A", "bírálóknak", "már", "korábban", "támogatniuk", "kellett", "volna", "az", "alapkutatást."],
                "english": "The reviewers should have supported basic research much earlier.",
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Reflect on Semmelweis's struggle using 'kellett volna' and 'meg lehetett volna menteni'.",
                        "answer": "Az orvosi karnak el kellett volna fogadnia Semmelweis statisztikáit, mert így édesanyák ezreit meg lehetett volna menteni."
                    }
                ],
                "teaches": ["b2-past-modals"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Compare Szent-Györgyi and Karikó's perseverance using '-hatott/-hetett volna'.",
                        "answer": "Mindketten feladhatták volna a kutatást a nehézségek láttán, kitartásukkal azonban megváltoztatták a modern orvostudományt."
                    }
                ],
                "teaches": ["b2-past-modals"]
            }
        ]
    }
}

# ============================================================================
# CULTURE UNIT 9: b2-matematikasakk
# ============================================================================
UNIT_9_MATEMATIKASAKK = {
    "unit_num": 9,
    "slug": "matematikasakk",
    "title": "Non-Euclidean Worlds: Hungarian Mathematics & Chess",
    "grammar_skill": "b2-concessive-indefinites",
    "vocab_skill": "b2-matematikasakk-vocab",
    "theme": "Hungarian mathematics, Bolyai, Erdős and chess",
    "location": "Marosvásárhely, Budapest és a nemzetközi versenytermek",
    "combined_story_title": "Semmiből egy új világot: Bolyaitól Erdősig és a Polgár lányokig",
    "combined_story_summary": "How János Bolyai's non-Euclidean geometry, the KöMaL problem-solving journal, Paul Erdős's collaborative mathematics, and Judit Polgár's chess mastery made Hungary a superpower of abstract thought.",
    "intro_body": [
        "Why has a relatively small Central European country produced such an extraordinary lineage of pure mathematicians and chess grandmasters—from János Bolyai's non-Euclidean geometry in the 1820s to Pál Erdős's global network of collaborators and Judit Polgár's historic triumphs over world champions?",
        "In this unit, you will explore Hungary's culture of abstract reasoning while mastering B2 universal and concessive indefinites (bárki, akárhogyan is, bármennyire ... is, akár ... akár ...) that allow speakers to generalize across all possible cases and concede extreme conditions."
    ],
    "lessons": [
        {
            "num": 1,
            "title": "János Bolyai: 'Out of Nothing I Have Created a Strange New Universe'",
            "grammar_label": "Concessive free-choice clauses: bármennyire (... is) and akárhogyan (... is)",
            "goals": [
                "I can explain how János Bolyai resolved the two-thousand-year-old problem of Euclid's parallel postulate.",
                "I can construct concessive scalar and manner clauses using bármennyire (... is) and akárhogyan (... is).",
                "I can use B2 vocabulary related to geometry, axioms, and spatial concepts."
            ],
            "story_segment": {
                "seg_slug": "bolyaijanos",
                "title": "Bolyai János: „Semmiből egy új, más világot teremtettem”",
                "summary": "Despite his father Farkas Bolyai's desperate warnings not to waste his life on Euclid's fifth postulate, young military engineer János Bolyai discovered hyperbolic geometry in 1823, laying the mathematical groundwork for Einstein's general relativity.",
                "location": "Marosvásárhely és Temesvár",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Kétezer éven keresztül a világ matematikusai egyetlen makacs kérdéssel viaskodtak: vajon levezethető-e Euklidesz híres ötödik posztulátuma, a párhuzamosok axiómája a többi geometriai alapigazságból? Bolyai Farkas, a marosvásárhelyi református kollégium kiváló professzora évtizedeket áldozott erre a problémára, ám bármennyire igyekezett is, minden bizonyítási kísérlete zsákutcába jutott. Amikor látta, hogy rendkívül tehetséges fia, a bécsi hadmérnöki akadémián tanuló Bolyai János is ugyanezzel a rejtéllyel foglalkozik, kétségbeesett levélben kérlelte: „Az Istenért kérlek, hagyj fel vele!”"
                    },
                    {
                        "type": "narration",
                        "text": "A fiatal Bolyai János azonban nem hátrált meg. Felismerte, hogy akárhogyan próbálják is a párhuzamosok axiómáját a többiből levezetni, az azért lehetetlen, mert az állítás független a többi axiómától. Mi történik akkor — tette fel a forradalmi kérdést —, ha feltételezzük, hogy egy adott egyeneshez egy külső ponton át nem egyetlen, hanem végtelen sok párhuzamos húzható? A várakozásokkal ellentétben nem keletkezett logikai ellentmondás: ehelyett egy teljesen új, önmagában ellentmondásmentes geometriai rendszer, a hiperbolikus geometria bontakozott ki előtte."
                    },
                    {
                        "type": "narration",
                        "text": "1823. november 3-án Temesvárról írta meg édesapjának a tudománytörténet egyik legszebb magyar mondatát: „Semmiből egy új, más világot teremtettem.” Felfedezését 1832-ben apja nagy matematikai tankönyvének függelékeként, a híres Appendixben jelentette meg. Ez a mindössze huszonhat oldalas latin nyelvű értekezés a modern matematika egyik legtömörebb remekműve."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor Bolyai Farkas elküldte az Appendixet fiatalkori barátjának, a „matematikusok fejedelmének” nevezett Carl Friedrich Gaussnak, a válasz egyszerre volt elismerő és lesújtó. Gauss azt írta, hogy nem dicsérheti meg János munkáját, mert azzal saját magát dicsérné, hiszen ő maga is évekkel korábban ugyanerre az eredményre jutott, csak nem merte publikálni a kortársak értetlenségétől tartva."
                    },
                    {
                        "type": "narration",
                        "text": "Bármennyire fájt is a fiatal Bolyainak a nemzetközi visszhang elmaradása, műve halhatatlannak bizonyult: közel száz évvel később Albert Einstein pontosan a nemeuklideszi geometria eszköztárát használta fel az általános relativitáselmélet és a görbült téridő leírására."
                    }
                ]
            },
            "words": [
                {"lemma": "axióma", "translation": "axiom / fundamental postulate", "pos": "noun"},
                {"lemma": "párhuzamos", "translation": "parallel (line)", "pos": "noun"},
                {"lemma": "ellentmondásmentes", "translation": "consistent / free of contradiction", "pos": "adjective"},
                {"lemma": "értekezés", "translation": "treatise / dissertation", "pos": "noun"},
                {"lemma": "bármennyire ... is", "translation": "however much / no matter how much", "pos": "expression"},
                {"lemma": "téridő", "translation": "spacetime", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "concessive-clauses-barmennyire-akarhogyan",
                "title": "Universal Concessive Clauses: bármennyire (... is) and akárhogyan (... is)",
                "text1_title": "Forming Concessive Indefinites with bár- and akár-",
                "text1": "Hungarian forms universal free-choice and concessive pronouns/adverbs by prefixing bár- or akár- to interrogative stems (ki -> bárki/akárki, hogyan -> bárhogyan/akárhogyan, mennyire -> bármennyire/akármennyire). When combined with the concessive particle is after the verb or adjective ('no matter how...'), they introduce a subordinate clause whose extreme condition fails to prevent the main clause from holding true.",
                "text2_title": "Position of the Particle 'is' and Preverb Inversion",
                "text2": "In a concessive clause headed by bármennyire or akárhogyan, the word immediately precedes the verb (or modified adjective/adverb) in the focus slot, and the particle is stands immediately after that focused element or verb: Bármennyire igyekezett is Bolyai Farkas... ('However hard Farkas Bolyai tried...'). If the verb has a separable preverb, it inverts behind the verb!",
                "table_title": "Concessive Indefinite Patterns",
                "table_rows": [
                    ["Bármennyire igyekezett is, nem találta a bizonyítást.", "However hard he tried, he did not find the proof."],
                    ["Akárhogyan próbálták is levezetni, mindig zsákutcába jutottak.", "No matter how they tried to derive it, they always hit a dead end."],
                    ["Bármilyen nehéz volt is a feladat, Bolyai nem hátrált meg.", "However difficult the task was, Bolyai did not back down."]
                ],
                "examples": [
                    {
                        "spanish": "Bármennyire igyekezett is Bolyai Farkas, minden bizonyítási kísérlete zsákutcába jutott.",
                        "english": "However hard Farkas Bolyai tried, every attempt at proof reached a dead end."
                    },
                    {
                        "spanish": "Akárhogyan próbálják is az ötödik posztulátumot a többiből levezetni, az független marad tőlük.",
                        "english": "No matter how they try to derive the fifth postulate from the others, it remains independent of them."
                    },
                    {
                        "spanish": "Bármennyire fájt is Jánosnak Gauss válasza, az Appendix megváltoztatta a matematika történetét.",
                        "english": "However much Gauss's reply hurt János, the Appendix changed the history of mathematics."
                    }
                ],
                "tip": "Place the concessive particle is right after the verb (Bármennyire igyekezett is) or right after the adjective (Bármilyen rövid volt is az értekezés)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az, hogy Bolyai János új geometriai rendszere 'ellentmondásmentes' volt?",
                    "options": [
                        "A rendszer belső szabályai logikailag összhangban álltak egymással, és nem vezettek önellentmondásra.",
                        "Minden kortárs professzor azonnal egyetértett vele.",
                        "Csak egyetlen egyenes létezett benne."
                    ],
                    "correct": 0,
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Bolyai János 1832-ben megjelent, huszonhat oldalas latin nyelvű _____ az Appendix címet viselte. (treatise / dissertation)",
                    "answer": "értekezése",
                    "english": "János Bolyai's twenty-six-page Latin treatise published in 1832 bore the title Appendix.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "_____ igyekezett is Bolyai Farkas, nem tudta levezetni a párhuzamosok axiómáját. (However much / No matter how hard)",
                    "answer": "Bármennyire",
                    "english": "However hard Farkas Bolyai tried, he could not derive the parallel postulate.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat használja helyesen a megengedő 'akárhogyan ... is' szerkezetet?",
                    "options": [
                        "Akárhogyan próbálták is bizonyítani az axiómát, minden kísérlet sikertelen maradt.",
                        "Akárhogyan bizonyítani próbálták az axiómát, vagy sikertelen maradt.",
                        "Is akárhogyan próbálták bizonyítani az axiómát, sikertelen maradt."
                    ],
                    "correct": 0,
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Bármilyen", "rövid", "volt", "is", "az", "Appendix,", "új", "világot", "nyitott", "a", "matematikában."],
                    "solution": ["Bármilyen", "rövid", "volt", "is", "az", "Appendix,", "új", "világot", "nyitott", "a", "matematikában."],
                    "english": "However short the Appendix was, it opened a new world in mathematics.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik huszadik századi fizikai elmélet használta fel Bolyai nemeuklideszi geometriáját a görbült téridő leírására?",
                    "options": [
                        "Albert Einstein általános relativitáselmélete.",
                        "Semmelweis Ignác fertőtlenítési elmélete.",
                        "Az első gőzgépek hőelmélete."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "párhuzamosok", "axiómája", "függetlennek", "bizonyult", "a", "többi", "geometriai", "alapigazságtól."],
                    "solution": ["A", "párhuzamosok", "axiómája", "függetlennek", "bizonyult", "a", "többi", "geometriai", "alapigazságtól."],
                    "english": "The parallel postulate proved independent of the other geometric fundamental truths.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe Farkas Bolyai's warnings using 'Bármennyire óvta is a fiát...'.",
                            "answer": "Bármennyire óvta is a fiát Bolyai Farkas a párhuzamosok problémájától, János nem adta fel a kutatást."
                        },
                        {
                            "prompt": "State that no matter how strange the new geometry seemed, it was free of contradiction using 'Bármilyen különösnek tűnt is...'.",
                            "answer": "Bármilyen különösnek tűnt is az új geometria a kortársak számára, a rendszer teljesen ellentmondásmentes volt."
                        }
                    ],
                    "teaches": ["b2-concessive-indefinites"]
                }
            ]
        },
        {
            "num": 2,
            "title": "The KöMaL Tradition and Problem-Solving Culture",
            "grammar_label": "Free-choice universal pronouns: bárki, akárki, bárhonnan, bármelyik",
            "goals": [
                "I can explain the role of the high-school journal KöMaL (1894) in discovering mathematical talent across Hungary.",
                "I can use universal free-choice pronouns (bárki, akárki, bárhonnan, bármelyik) in affirmative and negative contexts.",
                "I can discuss mathematical proof, monthly problem sets, and meritocracy in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "komalhagyomany",
                "title": "A KöMaL-hagyomány és a problémamegoldás kultúrája",
                "summary": "Founded in 1894 by Dániel Arany, the High School Mathematics and Physics Journal (KöMaL) created a nationwide meritocracy where any student from any village could send in proofs and see their name in print.",
                "location": "Győr és Budapest",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1894-ben egy győri reáliskolai tanár, Arany Dániel olyan kezdeményezést indított útjára, amely alapjaiban változtatta meg a magyar természettudományos oktatást: megalapította a Középiskolai Matematikai Lapokat, közismert nevén a KöMaL-t. A világ egyik legrégebbi, ma is megjelenő matematikai-fizikai diáklapja egyszerű, mégis forradalmi elvre épült. A szerkesztőség minden hónapban kitűzött egy sor gondolkodtató feladatot, amelyekre az ország bármelyik középiskolájából bárki beküldhette a saját megoldását."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a rendszer valódi szellemi demokráciát teremtett. Bárhonnan érkezett is a levél — akár egy nagyvárosi elit gimnáziumból, akár egy távoli kisváros vagy falu iskolájából —, a szerkesztők kizárólag a bizonyítás pontosságát és eleganciáját pontozták. A következő lapszámokban név szerint közölték a helyes megoldók névsorát, a legszebb gondolatmeneteket pedig nyomtatásban is megjelentették."
                    },
                    {
                        "type": "narration",
                        "text": "Egy tizenöt éves diák számára óriási büszkeséget jelentett, ha a neve megjelent a KöMaL hasábjain, sőt az év végi összesítésben a legjobbak arcképét is közzétették. Ha ma fellapozzuk a huszadik század első évtizedeinek évfolyamait, a sikeres megoldók között szinte az összes későbbi világhírű magyar tudóst megtaláljuk: Kármán Tódort, Haar Alfrédot, Riesz Marcellt, Szegő Gábort, Wigner Jenőt, Teller Edét és Erdős Pált."
                    },
                    {
                        "type": "narration",
                        "text": "A KöMaL feladatai megtanították a fiatalokat arra, hogy a matematika nem kész receptek bemagolása, hanem szellemi kaland. Akárki próbálkozott is a kitűzött példákkal, hamar rájött, hogy egy-egy nehezebb feladaton napokig, sőt hetekig érdemes töprengeni, miközben az ember séta közben vagy a villamoson is a bizonyítás lépéseit forgatja a fejében."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a hagyomány több mint százharminc éve töretlenül él tovább: a nyomtatott füzetek és az internetes pontverseny révén ma is középiskolások ezrei mérik össze tudásukat hónapról hónapra."
                    }
                ]
            },
            "words": [
                {"lemma": "bizonyítás", "translation": "mathematical proof / demonstration", "pos": "noun"},
                {"lemma": "pontverseny", "translation": "points competition / league", "pos": "noun"},
                {"lemma": "kitűz", "translation": "to set / pose (a problem or goal)", "pos": "verb"},
                {"lemma": "elegancia", "translation": "elegance (of a proof)", "pos": "noun"},
                {"lemma": "bárhonnan", "translation": "from anywhere / no matter from where", "pos": "adverb"},
                {"lemma": "töpreng", "translation": "to ponder / mull over deeply", "pos": "verb"}
            ],
            "grammar_doc": {
                "slug": "free-choice-pronouns-barki-akarki",
                "title": "Universal Free-Choice Pronouns: bárki, akárki, bármelyik, bárhonnan",
                "text1_title": "Bár- vs. Akár- in Free-Choice Generalizations",
                "text1": "Both bár- (bárki 'anyone', bármi 'anything', bármelyik 'any one of them', bárhonnan 'from anywhere') and akár- (akárki, akármi, akármelyik, akárhonnan) express universal free choice. In refined B2 written prose, bár- forms are slightly more neutral and formal in affirmative permissions (Az ország bármelyik iskolájából bárki beküldhette a megoldását), whereas akár- often carries a stronger emphatic or colloquial ring ('just anyone at all', e.g., Nem akárki tudta megoldani a feladatot = 'Not just anyone could solve the problem').",
                "text2_title": "Case Inflection on Free-Choice Pronouns",
                "text2": "Free-choice pronouns take all regular Hungarian case suffixes on their second element: bárkit (accusative), bárkinek (dative), bármelyikből (elative), bármiről (delative). Remember that they NEVER co-occur with double negation (senki nem); use them in affirmative clauses, modals, or concessive clauses.",
                "table_title": "Common Free-Choice Series",
                "table_rows": [
                    ["bárki / akárki (bárkit, bárkinek)", "anyone / whoever (acc., dat.)"],
                    ["bármelyik iskolából", "from any school whatsoever"],
                    ["bárhonnan érkezett is a levél", "no matter where the letter arrived from"],
                    ["Nem akárki nyerhette meg a versenyt.", "Not just anyone could win the competition."]
                ],
                "examples": [
                    {
                        "spanish": "Az ország bármelyik középiskolájából bárki beküldhette a saját matematikai megoldását.",
                        "english": "Anyone from any secondary school in the country could send in their own mathematical solution."
                    },
                    {
                        "spanish": "Bárhonnan érkezett is a pályamunka, a szerkesztők csak a bizonyítás pontosságát nézték.",
                        "english": "No matter where the entry arrived from, the editors looked only at the accuracy of the proof."
                    },
                    {
                        "spanish": "A legnehezebb feladatokat nem akárki tudta hibátlanul megoldani.",
                        "english": "Not just anyone was able to solve the hardest problems flawlessly."
                    }
                ],
                "tip": "Pay attention to the idiom 'nem akárki' ('not just anybody' = someone extraordinary): A nyertes diák nem akárki volt, hanem a fiatal Erdős Pál!"
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt az 1894-ben alapított KöMaL folyóirat legfontosabb pedagógiai újítása?",
                    "options": [
                        "Hónapról hónapra nyílt pontversenyben tűzött ki gondolkodtató feladatokat, amelyekre bárki beküldhette a bizonyítását.",
                        "Csak az egyetemi professzorok publikálhattak benne latin nyelven.",
                        "Betiltotta a geometriai ábrák használatát a középiskolákban."
                    ],
                    "correct": 0,
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A szerkesztők nemcsak a végeredményt, hanem a matematikai _____ logikai tisztaságát és eleganciáját is pontozták. (proof / demonstration)",
                    "answer": "bizonyítás",
                    "english": "The editors scored not only the final result, but also the logical clarity and elegance of the mathematical proof.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az ország _____ középiskolájából bárki beküldhette a megoldását a szerkesztőségnek. (from any [one] of them)",
                    "answer": "bármelyik",
                    "english": "Anyone from any secondary school in the country could submit their solution to the editorial office.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Mit jelent a magyar nyelvben a 'Nem akárki tudta megoldani ezt a feladatot' mondat?",
                    "options": [
                        "Csak rendkívül felkészült, kivételes képességű ember tudta megoldani a feladatot.",
                        "Senki a világon nem tudta megoldani a feladatot.",
                        "Mindenki könnyedén megoldotta a feladatot."
                    ],
                    "correct": 0,
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Bárhonnan", "érkezett", "is", "a", "levél,", "a", "szerkesztők", "minden", "megoldást", "elolvastak."],
                    "solution": ["Bárhonnan", "érkezett", "is", "a", "levél,", "a", "szerkesztők", "minden", "megoldást", "elolvastak."],
                    "english": "No matter where the letter arrived from, the editors read every solution.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Kiknek a nevével találkozhatunk a KöMaL huszadik század eleji sikeres feladatmegoldói között?",
                    "options": [
                        "Olyan későbbi világhírű tudósokéval, mint Kármán Tódor, Wigner Jenő, Teller Ede és Erdős Pál.",
                        "Kizárólag külföldi politikusokéval.",
                        "Csak általános iskolai rajztanárokéval."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "diákok", "hetekig", "töprengtek", "a", "folyóiratban", "kitűzött", "nehéz", "feladatokon."],
                    "solution": ["A", "diákok", "hetekig", "töprengtek", "a", "folyóiratban", "kitűzött", "nehéz", "feladatokon."],
                    "english": "The students pondered for weeks over the difficult problems posed in the journal.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain the democratic openness of KöMaL using 'bárki' and 'bármelyik iskolából'.",
                            "answer": "A KöMaL pontversenyébe bárki bekapcsolódhatott az ország bármelyik iskolájából."
                        },
                        {
                            "prompt": "Use 'Bárhonnan érkezett is...' to describe how the editors evaluated students' proofs.",
                            "answer": "Bárhonnan érkezett is a beküldött dolgozat, a bírálók kizárólag a bizonyítás eleganciáját értékelték."
                        }
                    ],
                    "teaches": ["b2-concessive-indefinites"]
                }
            ]
        },
        {
            "num": 3,
            "title": "Pál Erdős: Mathematics as a Social Art",
            "grammar_label": "Disjunctive concessive correlatives: akár ... akár ... and legyen szó ...-ról vagy ...-ról",
            "goals": [
                "I can describe Pál Erdős's nomadic lifestyle, unique vocabulary, and the concept of the Erdős number.",
                "I can build disjunctive concessive clauses using akár ... akár ... ('whether ... or ...') and legyen szó X-ről vagy Y-ról.",
                "I can discuss number theory, combinatorics, and collaborative research in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "erdospal",
                "title": "Erdős Pál: A matematika mint társas művészet",
                "summary": "Traveling the world with a single half-empty suitcase, Pál Erdős turned mathematics into a global social art, co-authoring over 1,500 papers and inspiring the famous 'Erdős number'.",
                "location": "Budapest és a világ egyetemei",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik századi matematika legkülönösebb és legtermékenyebb alakja kétségkívül az 1913-ban Budapesten született Erdős Pál volt. Szülei mindketten matematikatanárok voltak, így a kis Pál már hároméves korában fejben kiszámolta, hány másodpercet élt addig egy-egy vendégük, négyévesen pedig önállóan felfedezte a negatív számok tulajdonságait. Húszévesen, még egyetemi hallgatóként olyan egyszerű és elegáns bizonyítást adott Csebisev prímszámokra vonatkozó tételére, hogy neve egyetlen csapásra ismertté vált a világ matematikusai előtt."
                    },
                    {
                        "type": "narration",
                        "text": "Erdős egész felnőtt életét vándorló tudósként élte le: nem volt állandó lakása, bankszámlája vagy autója. Egyetlen kopott bőrönddel járta a világot, egyik egyetemről a másikra utazva. Amikor megérkezett egy kollégája házához, ezzel a legendás mondattal lépett be az ajtón: „Az agyam nyitva áll!” Akár Párizsban, akár Princetonban, akár Sydney-ben vagy Budapesten járt, néhány napig éjjel-nappal közösen gondolkodott a házigazdájával, majd amikor a cikk elkészült, már indult is a következő városba."
                    },
                    {
                        "type": "narration",
                        "text": "Különös, játékos magánnyelvet is alkotott magának. A gyerekeket „epszilonoknak” nevezte (a matematikában a tetszőlegesen kicsi mennyiség jele után), az előadásokat „prédikációnak”, a zenét „zajnak”. Legszebb elméleti látomása pedig „A Könyv” volt: hite szerint létezik egy képzeletbeli égi könyv, amelyben minden matematikai tételnek a lehető legtökéletesebb, legelegánsabb bizonyítása szerepel. Amikor egy kollégája különösen szép megoldást talált, Erdős legnagyobb dicsérete így szólt: „Ez egyenesen A Könyvből való!”"
                    },
                    {
                        "type": "narration",
                        "text": "Erdős Pál több mint ezerötszáz tudományos cikket írt, és több mint ötszáz társszerzővel dolgozott együtt — többen, mint bárki más a matematika történetében. Ebből a páratlan együttműködési hálózatból született meg a tréfás, mégis komolyan vett „Erdős-szám” fogalma. Erdős saját száma 0; akivel közös cikket írt, annak az Erdős-száma 1; aki pedig egy ilyen társszerzővel publikált közösen, azé 2."
                    },
                    {
                        "type": "narration",
                        "text": "Legyen szó számelméletről, kombinatorikáról vagy gráfelméletről, Erdős bebizonyította, hogy a legelvontabb tudomány sem magányos elefántcsonttorony, hanem határokon átívelő, élő emberi közösség."
                    }
                ]
            },
            "words": [
                {"lemma": "prímszám", "translation": "prime number", "pos": "noun"},
                {"lemma": "társszerző", "translation": "co-author", "pos": "noun"},
                {"lemma": "gráfelmélet", "translation": "graph theory", "pos": "noun"},
                {"lemma": "kombinatorika", "translation": "combinatorics", "pos": "noun"},
                {"lemma": "akár ... akár ...", "translation": "whether ... or ...", "pos": "expression"},
                {"lemma": "elefántcsonttorony", "translation": "ivory tower", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "disjunctive-concessives-akar-akar",
                "title": "Disjunctive Concessives: akár ... akár ... and legyen szó ...-ról",
                "text1_title": "Exhaustive Alternatives with akár ... akár ...",
                "text1": "To state that a conclusion holds true regardless of which of two or more alternatives is chosen ('whether X or Y'), Hungarian repeats akár before each alternative: Akár Párizsban, akár Budapesten járt, mindig a matematikáról beszélt ('Whether he was in Paris or in Budapest, he always spoke about mathematics'). It can join phrases (Akár esik, akár fúj) or full finite clauses.",
                "text2_title": "Academic Scope-Setting: legyen szó X-ről vagy Y-ról",
                "text2": "A hallmark of B2/C1 Hungarian essay prose is the subjunctive-imperative idiom legyen szó + [-ról/-ről] ... vagy + [-ról/-ről] ('be it a matter of X or Y / whether it concerns X or Y'). It elegantly lists domains to which a principle applies: Legyen szó számelméletről vagy gráfelméletről, Erdős új utakat nyitott.",
                "table_title": "Disjunctive Concessive Frames",
                "table_rows": [
                    ["Akár Európában, akár Amerikában járt, mindenhol társszerzők várták.", "Whether he traveled in Europe or America, co-authors awaited him everywhere."],
                    ["Akár fiatal diákkal, akár híres professzorral dolgozott, egyenrangú félként kezelte.", "Whether he worked with a young student or a famous professor, he treated them as an equal."],
                    ["Legyen szó számelméletről vagy kombinatorikáról, maradandót alkotott.", "Whether it was number theory or combinatorics, he created lasting work."]
                ],
                "examples": [
                    {
                        "spanish": "Akár Párizsban, akár Princetonban, akár Budapesten járt, Erdős azonnal munkához látott.",
                        "english": "Whether he was in Paris, Princeton, or Budapest, Erdős immediately got down to work."
                    },
                    {
                        "spanish": "Legyen szó számelméletről, kombinatorikáról vagy gráfelméletről, Erdős a közös gondolkodásban hitt.",
                        "english": "Be it number theory, combinatorics, or graph theory, Erdős believed in shared thinking."
                    },
                    {
                        "spanish": "Akárki nyitott is ajtót neki, Erdős ezzel a mondattal köszönt: „Az agyam nyitva áll!”",
                        "english": "Whoever opened the door for him, Erdős greeted them with this sentence: 'My brain is open!'."
                    }
                ],
                "tip": "Never confuse vagy ... vagy ... ('either ... or ...' — mutually exclusive choice) with akár ... akár ... ('whether ... or ...' — both cases lead to the same outcome)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit fejez ki a nemzetközi tudományos életben az 'Erdős-szám'?",
                    "options": [
                        "Azt, hogy egy kutató hány lépésnyi közös publikációs (társszerzői) távolságra van Erdős Páltól.",
                        "Azt, hogy hány prímszámot tud valaki egy perc alatt felsorolni.",
                        "Azt, hogy hány bőrönddel utazott Erdős Pál."
                    ],
                    "correct": 0,
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Erdős Pál több mint ötszáz _____ dolgozott együtt, így a matematika történetének legtermékenyebb kutatója lett. (with co-authors — instrumental -val/-vel)",
                    "answer": "társszerzővel",
                    "english": "Pál Erdős worked together with more than five hundred co-authors, thus becoming the most prolific researcher in the history of mathematics.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "_____ Európában, akár a tengerentúlon járt, Erdős mindenhol új matematikai problémákat vetett fel. (Whether ... [or])",
                    "answer": "Akár",
                    "english": "Whether he was in Europe or overseas, Erdős posed new mathematical problems everywhere.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik szerkezet illik a mondatba? '_____ számelméletről vagy gráfelméletről, Erdős minden területen maradandót alkotott.'",
                    "options": [
                        "Legyen szó",
                        "Minél inkább",
                        "Kellett volna"
                    ],
                    "correct": 0,
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Akár", "diákkal,", "akár", "professzorral", "beszélgetett,", "mindig", "egyenrangú", "társként", "kezelte", "őket."],
                    "solution": ["Akár", "diákkal,", "akár", "professzorral", "beszélgetett,", "mindig", "egyenrangú", "társként", "kezelte", "őket."],
                    "english": "Whether he was conversing with a student or a professor, he always treated them as equal partners.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit értett Erdős Pál azon, amikor egy matematikai levezetésről azt mondta, hogy 'A Könyvből való'?",
                    "options": [
                        "Azt, hogy a bizonyítás annyira tökéletes, tiszta és elegáns, mintha egy képzeletbeli égi gyűjteményből származna.",
                        "Azt, hogy a megoldást egy középiskolai tankönyvből másolták ki.",
                        "Azt, hogy a bizonyítás túl hosszú és unalmas."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["A", "kombinatorika", "és", "a", "gráfelmélet", "a", "modern", "számítástechnika", "alapjává", "vált."],
                    "solution": ["A", "kombinatorika", "és", "a", "gráfelmélet", "a", "modern", "számítástechnika", "alapjává", "vált."],
                    "english": "Combinatorics and graph theory became the foundation of modern computer science.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe Erdős's global way of working using 'Akár ..., akár ...'.",
                            "answer": "Akár egyetemi szemináriumon, akár egy barátja nappalijában ült, Erdős Pál mindig új bizonyításokon dolgozott."
                        },
                        {
                            "prompt": "Summarize the breadth of Erdős's work using 'Legyen szó ...-ról vagy ...-ról'.",
                            "answer": "Legyen szó prímszámokról vagy gráfelméletről, Erdős Pál a közös gondolkodás művészetévé tette a matematikát."
                        }
                    ],
                    "teaches": ["b2-concessive-indefinites"]
                }
            ]
        },
        {
            "num": 4,
            "title": "Judit Polgár and the Experiment in Genius",
            "grammar_label": "Emphatic universal concessives with bárki + subjunctive/indicative and bármilyen + noun",
            "goals": [
                "I can explain László and Klára Polgár's pedagogical thesis ('geniuses are made, not born') and Judit Polgár's historic chess career.",
                "I can use universal concessive structures with bármilyen + noun and bárki ellen + verb.",
                "I can discuss chess strategy, grandmaster tournaments, and gender stereotypes in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "polgarjudit",
                "title": "Polgár Judit és a zseninevelés kísérlete",
                "summary": "Raised in Budapest by educators László and Klára Polgár to prove that extraordinary achievement comes from early, joyful specialization, Judit Polgár broke Bobby Fischer's grandmaster record at fifteen and defeated eleven world champions.",
                "location": "Budapest és a nemzetközi sakkversenyek",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1960-as évek végén egy fiatal budapesti pedagógus és pszichológus, Polgár László merész elmélettel állt elő: miután több száz történelmi zseni — köztük Mozart és Gauss — életrajzát tanulmányozta, arra a következtetésre jutott, hogy a zseninek nem születni kell, hanem a zsenit nevelni lehet. Feleségével, Klárával elhatározták, hogy saját gyermekeik nevelésével bizonyítják be az elméletet, és ehhez a legobjektívebben mérhető szellemi sportot, a sakkot választották."
                    },
                    {
                        "type": "narration",
                        "text": "A három Polgár lány — Zsuzsa, Zsófia és a legfiatalabb, 1976-ban született Judit — nem járt hagyományos iskolába: szüleik otthon tanították őket, miközben a lakás falait több ezer sakkjátszma kartotékjai borították. Bármilyen szkeptikusan fogadták is kezdetben a hatóságok és a szakemberek ezt a kísérletet, az eredmények minden várakozást felülmúltak. 1988-ban a szaloniki sakkolimpián a három Polgár nővér Mádl Ildikóval kiegészülve megszerezte Magyarország számára az aranyérmet a verhetetlennek hitt szovjet válogatott előtt."
                    },
                    {
                        "type": "narration",
                        "text": "Polgár Judit pályafutása még a nővérei sikerein is túlmutatott. Ő már a kezdetektől fogva kizárólag a nyílt — vagyis a férfiak által uralt — mezőnyben indult, mert be akarta bizonyítani, hogy a sakktábla mellett nincs különbség férfi és női gondolkodás között. 1991 decemberében, mindössze tizenöt évesen és négy hónaposan megszerezte a nemzetközi nagymesteri címet, megdöntve ezzel az amerikai világbajnok, Bobby Fischer addigi világcsúcsát."
                    },
                    {
                        "type": "narration",
                        "text": "Bárki ült is vele szemben a sakktábla túloldalán, Judit félelmet nem ismerő, támadó kombinációs stílusával mindenkit zavarba hozott. Negyed évszázadon keresztül megszakítás nélkül vezette a női világranglistát, az abszolút (férfi és női közös) világranglistán pedig a nyolcadik helyig jutott — amire sem előtte, sem azóta nem volt képes más női sakkozó."
                    },
                    {
                        "type": "narration",
                        "text": "Pályafutása során összesen tizenegy regnáló vagy egykori világbajnokot — köztük Garri Kaszparovot, Anatolij Karpovot, Visuvanathan Anandot és Magnus Carlsent — győzött le, végleg lebontva az évszázados előítéleteket."
                    }
                ]
            },
            "words": [
                {"lemma": "nagymester", "translation": "grandmaster (chess)", "pos": "noun"},
                {"lemma": "világranglista", "translation": "world ranking list", "pos": "noun"},
                {"lemma": "előítélet", "translation": "prejudice / preconception", "pos": "noun"},
                {"lemma": "sakktábla", "translation": "chessboard", "pos": "noun"},
                {"lemma": "bárki ült is", "translation": "whoever sat / no matter who sat", "pos": "expression"},
                {"lemma": "kombinációs készség", "translation": "combinational / tactical skill", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "concessive-pronouns-barki-barmilyen",
                "title": "Concessive Relative Clauses with bárki (... is) and bármilyen (... is)",
                "text1_title": "Subject and Oblique Concessive Clauses: Bárki ült is vele szemben...",
                "text1": "When bárki or akárki introduces a concessive subordinate clause ('whoever / no matter who...'), the pronoun stands at the head of the clause, immediately followed by the finite verb and the particle is: Bárki ült is vele szemben a sakktáblánál, Judit győzelemre tört ('Whoever sat across from her at the chessboard, Judit strove for victory').",
                "text2_title": "Adjectival Concessives: Bármilyen + Adjective/Adverb + Verb + is",
                "text2": "Similarly, bármilyen ('no matter what kind of / however...') modifies an adjective or adverb right before the verb, with is placed right after the verb: Bármilyen szkeptikusan fogadták is a kísérletet, az eredmények igazolták a szülőket ('However skeptically they received the experiment, the results vindicated the parents').",
                "table_title": "Concessive Clause Templates",
                "table_rows": [
                    ["Bárki ült is vele szemben, bátran támadott.", "Whoever sat across from her, she attacked boldly."],
                    ["Bármilyen erős volt is az ellenfél, nem hátrált meg.", "However strong the opponent was, she did not retreat."],
                    ["Bármilyen szkeptikusan fogadták is a tervet, sikeres lett.", "However skeptically they received the plan, it became successful."]
                ],
                "examples": [
                    {
                        "spanish": "Bárki ült is vele szemben a sakktábla túloldalán, Polgár Judit támadó stílusban játszott.",
                        "english": "Whoever sat across from her on the other side of the chessboard, Judit Polgár played in an attacking style."
                    },
                    {
                        "spanish": "Bármilyen szkeptikusan fogadták is kezdetben a pedagógiai kísérletet, a három lány sikere mindenkit meggyőzött.",
                        "english": "However skeptically the pedagogical experiment was initially received, the three daughters' success convinced everyone."
                    },
                    {
                        "spanish": "Bármelyik világbajnokkal mérkőzött is meg, egyenrangú ellenfélnek bizonyult.",
                        "english": "Whichever world champion she competed against, she proved to be an equal opponent."
                    }
                ],
                "tip": "Notice how any preverb on the verb inside a bárki/bármelyik ... is clause must invert after the particle is: Bármelyik világbajnokkal mérkőzött is meg (from megmérkőzik)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt Polgár László pedagógiai kísérletének alapvető tételmondata?",
                    "options": [
                        "A zseninek nem születni kell, hanem korai, örömteli és céltudatos neveléssel a zseni kinevelhető.",
                        "A sakkot csak húszéves kor felett szabad elkezdeni tanulni.",
                        "A matematikai és sakktehetség kizárólag genetikai öröklődés útján adható át."
                    ],
                    "correct": 0,
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Polgár Judit tizenöt évesen szerezte meg a nemzetközi _____ címet, megdöntve Bobby Fischer rekordját. (grandmaster — adjectival form nagymesteri)",
                    "answer": "nagymesteri",
                    "english": "Judit Polgár earned the international grandmaster title at age fifteen, breaking Bobby Fischer's record.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "_____ ült is vele szemben a sakktáblánál, Polgár Judit mindig győzelemre játszott. (Whoever / No matter who)",
                    "answer": "Bárki",
                    "english": "Whoever sat across from her at the chessboard, Judit Polgár always played for victory.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban helyes az igekötő és az 'is' szócska sorrendje?",
                    "options": [
                        "Bármelyik világbajnokkal mérkőzött is meg, képes volt legyőzni őt.",
                        "Bármelyik világbajnokkal megmérkőzött is, képes volt legyőzni őt.",
                        "Is bármelyik világbajnokkal megmérkőzött, képes volt legyőzni őt."
                    ],
                    "correct": 0,
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Bármilyen", "szkeptikusan", "fogadták", "is", "a", "kísérletet,", "az", "eredmények", "önmagukért", "beszéltek."],
                    "solution": ["Bármilyen", "szkeptikusan", "fogadták", "is", "a", "kísérletet,", "az", "eredmények", "önmagukért", "beszéltek."],
                    "english": "However skeptically they received the experiment, the results spoke for themselves.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért indult Polgár Judit pályafutása során következetesen a nyílt (férfiak által uralt) versenyeken?",
                    "options": [
                        "Hogy bebizonyítsa: a szellemi sportokban és a sakktábla mellett nincs különbség férfi és női teljesítmény között.",
                        "Mert Magyarországon nem rendeztek női sakkversenyeket.",
                        "Mert a női versenyeken tilos volt a támadó játék."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Polgár", "Judit", "sikerei", "végleg", "lebontották", "a", "régi", "társadalmi", "előítéleteket."],
                    "solution": ["Polgár", "Judit", "sikerei", "végleg", "lebontották", "a", "régi", "társadalmi", "előítéleteket."],
                    "english": "Judit Polgár's successes permanently dismantled the old social prejudices.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Describe Judit Polgár's courage against world champions using 'Bárki ült is vele szemben...'.",
                            "answer": "Bárki ült is vele szemben a sakktábla túloldalán, Polgár Judit félelem nélkül, támadó szellemben sakkozott."
                        },
                        {
                            "prompt": "State that however strong the prejudices were, her results overcame them using 'Bármilyen erősek voltak is...'.",
                            "answer": "Bármilyen erősek voltak is az előítéletek a női sakkozókkal szemben, Polgár Judit győzelmei minden kétkedőt meggyőztek."
                        }
                    ],
                    "teaches": ["b2-concessive-indefinites"]
                }
            ]
        },
        {
            "num": 5,
            "title": "Why Small Nations Excel in Abstract Disciplines",
            "grammar_label": "Synthesizing universal and concessive indefinites in cultural analysis",
            "goals": [
                "I can explain the sociological and historical reasons why Hungary excelled in low-capital abstract fields like mathematics, chess, and theoretical physics.",
                "I can synthesize bár-/akár- pronouns, concessive clauses (... is), and disjunctive correlatives (akár ... akár ...) in B2 essays.",
                "I can discuss research infrastructure, intellectual capital, and abstract disciplines in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "elvonttudomanyok",
                "title": "Miért jeleskednek a kis nemzetek az elvont tudományokban?",
                "summary": "Needing only paper, a pencil, or a chessboard rather than billion-dollar particle accelerators, mathematics, theoretical physics, and chess allowed Hungarian thinkers to compete at the global frontier regardless of economic constraints.",
                "location": "Budapest és a nemzetközi tudományos közösség",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Ha végigtekintünk Bolyai János, a KöMaL-iskola, Erdős Pál, a budapesti „marslakók” vagy a Polgár nővérek történetén, óhatatlanul felmerül egy mélyebb kultúrtörténeti kérdés: miért éppen a legelvontabb szellemi területeken — a tiszta matematikában, az elméleti fizikában és a sakkban — vált Magyarország világhatalommá? A válasz egyszerre gazdasági, társadalmi és kulturális természetű."
                    },
                    {
                        "type": "narration",
                        "text": "A tizenkilencedik és a huszadik században egy közép-európai kis országnak ritkán állt rendelkezésére annyi tőke, hogy óriási tengeri flottákat, drága részecskegyorsítókat vagy hatalmas ipari kutatólaboratóriumokat építsen. A matematikához és a sakkhoz azonban nincs szükség milliárdos berendezésekre: bármilyen szerény körülmények között él is egy tehetséges fiatal, egyetlen ceruza, néhány ív papír és egy sakktábla elegendő ahhoz, hogy a világ élvonalába kerüljön."
                    },
                    {
                        "type": "narration",
                        "text": "Ugyanakkor a tőke hiánya önmagában nem teremt tudományt. Ahhoz, hogy a papíron és ceruzán megszülessenek a nagy gondolatok, olyan szellemi közegre volt szükség, amely társadalmi rangot adott az észnek. Magyarországon a gimnáziumi tanárok, a matematikai versenyek és a sakk-klubok olyan hagyományt építettek fel, amelyben a szellemi teljesítményt bárki elismerte, függetlenül a családi háttértől."
                    },
                    {
                        "type": "narration",
                        "text": "Ráadásul a matematika és a sakk egyetemes nyelv: akár tud valaki angolul vagy németül, akár csak most tanulja a világnyelveket, egy elegáns egyenletet vagy egy huszárlépést a Föld bármelyik pontján azonnal megértenek. Ez az egyetemesség tette lehetővé, hogy a történelmi viharok idején is fennmaradjon a magyar szellemi jelenlét a nemzetközi életben."
                    },
                    {
                        "type": "narration",
                        "text": "Bárhogyan alakul is a huszonegyedik század technológiája — a mesterséges intelligenciától a kvantumszámítógépekig —, az elvont, fegyelmezett és mégis játékos gondolkodás művészete továbbra is a magyar kultúra egyik legértékesebb öröksége marad."
                    }
                ]
            },
            "words": [
                {"lemma": "elvont", "translation": "abstract", "pos": "adjective"},
                {"lemma": "szellemi tőke", "translation": "intellectual capital", "pos": "noun"},
                {"lemma": "részecskegyorsító", "translation": "particle accelerator", "pos": "noun"},
                {"lemma": "élvonal", "translation": "forefront / vanguard / world elite", "pos": "noun"},
                {"lemma": "bárhogyan alakul is", "translation": "no matter how it develops / turns out", "pos": "expression"},
                {"lemma": "örökség", "translation": "heritage / legacy", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "synthesizing-concessive-indefinites",
                "title": "Synthesizing Universal and Concessive Indefinites in Cultural Analysis",
                "text1_title": "Summary of the B2 Concessive & Universal System",
                "text1": "Across Unit 9, you have mastered four high-register ways to generalize and concede in Hungarian: (1) Scalar/Manner Concessives: Bármennyire / bármilyen / bárhogyan + verb + is ('However much / no matter how...'); (2) Nominal Concessives: Bárki + verb + is ('Whoever...'); (3) Disjunctive Correlatives: Akár ... akár ... / legyen szó ...-ról ('Whether ... or ...'); and (4) Universal Free-Choice Pronouns: bárki, bármelyik, bárhonnan in affirmative and modal clauses.",
                "text2_title": "Avoiding Common Learner Pitfalls",
                "text2": "1. Do not omit 'is' in finite concessive clauses (*Bárhogyan alakul a jövő -> Bárhogyan alakul is a jövő). 2. Do not put 'is' directly after bár-/akár- (*Bárhogyan is alakul is preferred in speech, but in classical B2/C1 written prose, placing 'is' right after the verb or adjective—Bárhogyan alakul is / Bármilyen szerény volt is—is the gold standard). 3. Invert separable preverbs behind 'is'.",
                "table_title": "Master Synthesis Table",
                "table_rows": [
                    ["Bármilyen szerény körülmények között él is valaki...", "No matter how modest circumstances someone lives in..."],
                    ["Bárhogyan alakul is a jövő technológiája...", "However the technology of the future turns out..."],
                    ["A Föld bármelyik pontján azonnal megértik.", "At any point on Earth they immediately understand it."],
                    ["Akár a matematikát, akár a sakkot nézzük...", "Whether we look at mathematics or chess..."]
                ],
                "examples": [
                    {
                        "spanish": "Bármilyen szerény körülmények között él is egy tehetséges diák, egy ceruza és egy papír elegendő a matematikához.",
                        "english": "No matter how modest circumstances a talented student lives in, a pencil and paper suffice for mathematics."
                    },
                    {
                        "spanish": "Akár a tiszta matematikát, akár a sakkot vizsgáljuk, mindkettő egyetemes nyelvet beszél.",
                        "english": "Whether we examine pure mathematics or chess, both speak a universal language."
                    },
                    {
                        "spanish": "Bárhogyan alakul is a huszonegyedik század technológiája, az elvont gondolkodás értékes örökség marad.",
                        "english": "However the technology of the twenty-first century develops, abstract thinking will remain a valuable legacy."
                    }
                ],
                "tip": "Using Bárhogyan alakul is... or Bármilyen nehéz volt is... in your concluding paragraph gives your Hungarian essays an unmistakable native B2/C1 cadence."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Miért tudott Magyarország különösen a tiszta matematikában és a sakkban a világ élvonalába kerülni a szöveg szerint?",
                    "options": [
                        "Mert ezekhez az elvont tudományokhoz nem drága ipari berendezésekre, hanem kiváló iskolákra, szellemi tőkére, papírra és sakktáblára volt szükség.",
                        "Mert Magyarországon volt a világ legtöbb részecskegyorsítója a tizenkilencedik században.",
                        "Mert minden más tantárgyat betiltottak a gimnáziumokban."
                    ],
                    "correct": 0,
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A matematika és a sakk kultúrája a magyar szellemi _____ egyik legértékesebb része. (heritage / legacy)",
                    "answer": "örökség",
                    "english": "The culture of mathematics and chess is one of the most valuable parts of Hungarian intellectual heritage.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Bárhogyan _____ is a jövő technológiája, az önálló gondolkodásra mindig szükség lesz. (turns out / develops — alakul)",
                    "answer": "alakul",
                    "english": "However the technology of the future develops, independent thinking will always be needed.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat foglalja össze helyesen a választó-megengedő ('whether ... or ...') viszonyt?",
                    "options": [
                        "Akár a matematikát, akár a sakkot vizsgáljuk, mindkettőben döntő szerepet játszott a tehetséggondozás.",
                        "Minél a matematikát, annál a sakkot vizsgáljuk, döntő szerepet játszott.",
                        "Bárki a matematikát, akárki a sakkot vizsgáljuk."
                    ],
                    "correct": 0,
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Bármilyen", "szerény", "körülmények", "között", "él", "is", "valaki,", "a", "tehetsége", "utat", "törhet."],
                    "solution": ["Bármilyen", "szerény", "körülmények", "között", "él", "is", "valaki,", "a", "tehetsége", "utat", "törhet."],
                    "english": "No matter how modest circumstances someone lives in, their talent can break through.",
                    "teaches": ["b2-concessive-indefinites"]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért nevezi a szöveg a matematikát és a sakkot 'egyetemes nyelvnek'?",
                    "options": [
                        "Mert egy elegáns matematikai bizonyítást vagy egy sakkjátszmát a Föld bármely pontján nyelvi akadályok nélkül megértenek.",
                        "Mert mindkettőt kizárólag eszperantó nyelven oktatják.",
                        "Mert egyikben sincsenek szabályok."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": ["Az", "elvont", "gondolkodás", "és", "a", "szellemi", "tőke", "a", "világ", "élvonalába", "emelte", "a", "kutatókat."],
                    "solution": ["Az", "elvont", "gondolkodás", "és", "a", "szellemi", "tőke", "a", "világ", "élvonalába", "emelte", "a", "kutatókat."],
                    "english": "Abstract thinking and intellectual capital raised the researchers into the forefront of the world.",
                    "teaches": ["b2-matematikasakk-vocab"]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Explain why young talents could succeed without expensive laboratories using 'Bármilyen szerény körülmények között...'.",
                            "answer": "Bármilyen szerény körülmények között tanult is egy diák, a matematikához elég volt a papír, a ceruza és a kitartás."
                        },
                        {
                            "prompt": "Write a concluding sentence about the future of abstract thought using 'Bárhogyan alakul is...'.",
                            "answer": "Bárhogyan alakul is a huszonegyedik század tudománya, a kreatív problémamegoldás örök érték marad."
                        }
                    ],
                    "teaches": ["b2-concessive-indefinites"]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can discuss the achievements of János Bolyai, the KöMaL tradition, Pál Erdős, and Judit Polgár.",
            "I can construct concessive clauses with bármennyire/bármilyen/bárhogyan/bárki ... is and correct preverb order.",
            "I can use free-choice pronouns (bárki, bármelyik, nem akárki) and disjunctive correlatives (akár ... akár ..., legyen szó ...-ról)."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban helyes a megengedő 'bármennyire ... is' szerkezet szórendje?",
                "options": [
                    "Bármennyire igyekezett is Bolyai Farkas, nem találta meg az ötödik posztulátum bizonyítását.",
                    "Bármennyire Bolyai Farkas igyekezett, nem találta is meg a bizonyítást.",
                    "Is bármennyire igyekezett Bolyai Farkas, nem találta meg."
                ],
                "correct": 0,
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Kinek a nevéhez fűződik a nemeuklideszi (hiperbolikus) geometria felfedezése és az 1832-es Appendix?",
                "options": [
                    "Bolyai Jánoséhoz",
                    "Semmelweis Ignácéhoz",
                    "Szent-Györgyi Albertéhez"
                ],
                "correct": 0,
                "teaches": ["b2-matematikasakk-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszópár fejezi ki a 'whether in Europe or in America' jelentést?",
                "options": [
                    "Akár Európában, akár Amerikában",
                    "Minél Európában, annál Amerikában",
                    "Sem Európában, vagy Amerikában"
                ],
                "correct": 0,
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A KöMaL pontversenyébe az ország _____ középiskolájából bárki beküldhette a megoldását. (any [one] of them)",
                "answer": "bármelyik",
                "english": "Anyone from any secondary school in the country could send in their solution to the KöMaL competition.",
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Erdős Pál több mint ötszáz _____ publikált közös matematikai cikket élete során. (with co-authors — társszerzővel)",
                "answer": "társszerzővel",
                "english": "Pál Erdős published joint mathematical papers with more than five hundred co-authors during his life.",
                "teaches": ["b2-matematikasakk-vocab"]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "_____ ült is vele szemben a sakktáblánál, Polgár Judit mindig bátor, támadó stílusban játszott. (Whoever)",
                "answer": "Bárki",
                "english": "Whoever sat across from her at the chessboard, Judit Polgár always played in a bold, attacking style.",
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Legyen", "szó", "számelméletről", "vagy", "gráfelméletről,", "Erdős", "Pál", "új", "utakat", "nyitott."],
                "solution": ["Legyen", "szó", "számelméletről", "vagy", "gráfelméletről,", "Erdős", "Pál", "új", "utakat", "nyitott."],
                "english": "Whether it was number theory or graph theory, Pál Erdős opened new paths.",
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Bolyai", "János", "felfedezte", "az", "ellentmondásmentes", "nemeuklideszi", "geometria", "törvényeit."],
                "solution": ["Bolyai", "János", "felfedezte", "az", "ellentmondásmentes", "nemeuklideszi", "geometria", "törvényeit."],
                "english": "János Bolyai discovered the laws of consistent non-Euclidean geometry.",
                "teaches": ["b2-matematikasakk-vocab"]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat tartalmazza helyesen a megengedő szerkezetet és az igekötő hátravetését?",
                "options": [
                    "Bármelyik világbajnokkal mérkőzött is meg Polgár Judit, méltó ellenfélnek bizonyult.",
                    "Bármelyik világbajnokkal megmérkőzött Polgár Judit, vagy méltó ellenfélnek bizonyult.",
                    "Akár világbajnokkal megmérkőzött is Polgár Judit."
                ],
                "correct": 0,
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bárhogyan", "alakul", "is", "a", "jövő,", "az", "elvont", "gondolkodás", "érték", "marad."],
                "solution": ["Bárhogyan", "alakul", "is", "a", "jövő,", "az", "elvont", "gondolkodás", "érték", "marad."],
                "english": "However the future turns out, abstract thinking will remain a value.",
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Summarize János Bolyai's breakthrough using 'Bármennyire óvta is az édesapja...'.",
                        "answer": "Bármennyire óvta is az édesapja a párhuzamosok problémájától, Bolyai János megalkotta a nemeuklideszi geometriát."
                    }
                ],
                "teaches": ["b2-concessive-indefinites"]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "template": [
                    {
                        "prompt": "Connect the stories of Erdős and Judit Polgár using 'Akár a matematikát, akár a sakkot nézzük...'.",
                        "answer": "Akár a matematikát, akár a sakkot nézzük, a magyar tehetségek a világ élvonalába emelték az elvont gondolkodás kultúráját."
                    }
                ],
                "teaches": ["b2-concessive-indefinites"]
            }
        ]
    }
}


def main():
    build_culture_unit(UNIT_7_MARSLAKOK)
    build_culture_unit(UNIT_8_SEMMELWEIS)
    build_culture_unit(UNIT_9_MATEMATIKASAKK)
    print("Successfully generated Hungarian B2 Culture Units 7, 8, and 9.")


if __name__ == "__main__":
    main()
