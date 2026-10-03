#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 33 Generator:
  - Track 1 (Core): Unit 33 — "Hungarian Literary Modernism, Poetic Semiotics & Textual Hermeneutics" (c1-33)
  - Track 2 (Discourse): Unit 33 — "The Battle for the Literary Canon: NAT, Textbooks & Blacklists" (c1-irodalmielet)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_33():
    print("=== Generating C1 Unit 33 ===")
    
    new_skills = {
        "c1-33-vocab": {"kind": "vocabulary"},
        "c1-irodalmielet-vocab": {"kind": "vocabulary"},
        "c1-adv-semiotic-literary-hermeneutics": {"kind": "grammar"},
        "c1-participle-polyphonic-textual-polysemy": {"kind": "grammar"},
        "c1-modal-deontic-aesthetic-humanism": {"kind": "grammar"},
        "c1-adv-comparative-intertextuality-scalar": {"kind": "grammar"},
        "c1-syntax-hermeneutic-canon-synthesis": {"kind": "grammar"},
        "c1-discourse-canon-indoctrination-framing": {"kind": "grammar"},
        "c1-adv-textbook-monopoly-critique": {"kind": "grammar"},
        "c1-modal-deontic-intellectual-dissent": {"kind": "grammar"},
        "c1-adv-proportional-cultural-patronage-polarization": {"kind": "grammar"},
        "c1-adv-conclusive-canon-pluralism": {"kind": "grammar"},
    }
    new_titles = {
        "c1-33-vocab": "reading",
        "c1-irodalmielet-vocab": "reading",
        "c1-adv-semiotic-literary-hermeneutics": "evaluative adverbials conducting semiotic analysis and textual literary hermeneutics",
        "c1-participle-polyphonic-textual-polysemy": "participial clauses analyzing polyphonic textual resonance and poetic polysemy",
        "c1-modal-deontic-aesthetic-humanism": "deontic modal structures asserting aesthetic duty of universal humanism",
        "c1-adv-comparative-intertextuality-scalar": "scalar comparative adverbials tracing european intertextual literary genealogy",
        "c1-syntax-hermeneutic-canon-synthesis": "evaluative correlative syntax formulating hermeneutic synthesis of world literary canons",
        "c1-discourse-canon-indoctrination-framing": "discourse framing markers diagnosing state ideological indoctrination through educational curricula",
        "c1-adv-textbook-monopoly-critique": "critical evaluative adverbials exposing state textbook monopolization and pedagogical regression",
        "c1-modal-deontic-intellectual-dissent": "deontic modal structures formulating writers duty of intellectual dissent",
        "c1-adv-proportional-cultural-patronage-polarization": "proportional correlative structures mapping political patronage against cultural polarization",
        "c1-adv-conclusive-canon-pluralism": "evaluative conclusive particles declaring irrepressible pluralism of autonomous literature",
    }
    
    core_title = "Hungarian Literary Modernism, Poetic Semiotics & Textual Hermeneutics"
    core_stems = [f"c1-33-0{i}" for i in range(1, 6)] + ["c1-33-consolidation"]
    disc_title = "The Battle for the Literary Canon: NAT, Textbooks & Blacklists"
    slug = "irodalmielet"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(33, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-33)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian literary modernism of the Nyugat generation represented an intellectual and artistic renaissance that bridged national poetry with universal European consciousness.",
        "In this unit, centered on Mihály Babits's monumental masterpiece 'Az európai irodalom története' (History of European Literature, 1934–1935), you will master the elevated academic register of poetic semiotics, textual hermeneutics, polyphonic textual analysis, aesthetic humanism, and comparative world literature at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-33-01",
            "title": "Poetic Semiotics & Hermeneutic Horizon",
            "grammar_title": "Evaluative Adverbials Conducting Semiotic Analysis and Textual Literary Hermeneutics",
            "grammar_skill": "c1-adv-semiotic-literary-hermeneutics",
            "goals": [
                "I can analyze poetic signs, semiotic decoding, and the hermeneutic horizon of literary modernism (*poétikai szemiotika, jelszerűség, hermeneutikai horizont, jelentésrétegek kibontása*).",
                "I can deploy elevated evaluative adverbials formulating textual hermeneutics (*szemiotikailag dekódolva, hermeneutikai szempontból vizsgálva, poétikailag szerves módon leképezve*).",
                "I can critique formalist vs. contextual interpretations of poetic imagery."
            ],
            "vocab": [
                {"lemma": "poétikai szemiotika", "translation": "poetic semiotics", "pos": "expression"},
                {"lemma": "hermeneutikai horizont", "translation": "hermeneutic horizon", "pos": "expression"},
                {"lemma": "jelentésréteg", "translation": "layer of meaning / textual strata", "pos": "noun"},
                {"lemma": "jelszerűség", "translation": "sign quality / semiotic nature", "pos": "noun"},
                {"lemma": "szimbolista poétika", "translation": "symbolist poetics", "pos": "expression"},
                {"lemma": "szövegszerűség", "translation": "textuality", "pos": "noun"},
                {"lemma": "értelmezési keret", "translation": "interpretive framework", "pos": "expression"},
                {"lemma": "esztétikai kód", "translation": "aesthetic code", "pos": "expression"}
            ],
            "gr_text1": "Evaluative adverbials in literary analysis formalize the methodological perspective through which poetic texts are dissected: `szemiotikailag dekódolva` (decoded semiotically), `hermeneutikai szempontból vizsgálva` (examined from a hermeneutic perspective), `poétikailag szerves módon megalkotva` (crafted in a poetically organic manner), `az esztétikai kódok finom hálóját feltárva` (uncovering the delicate web of aesthetic codes).",
            "gr_text2": "Example: `A vers szimbólumrendszerét szemiotikailag dekódolva és hermeneutikai szempontból vizsgálva a szöveg többszólamú metafizikai dimenziói tárulnak fel`.",
            "gr_table": [
                ["A költeményt hermeneutikai szempontból vizsgálva feltárul a szerzői én kettőssége.", "Examining the poem from a hermeneutic perspective the duality of the poetic self is revealed."],
                ["A metaforákat szemiotikailag dekódolva a szimbolista esztétika kulcsa válik láthatóvá.", "Decoding the metaphors semiotically the key to symbolist poetics becomes visible."],
                ["A vers poétikailag szerves módon ötvözi a ritmust a jelentéssel.", "Poetically the poem organically blends rhythm with meaning."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a hermeneutikai horizont lényege az irodalmi művek értelmezésében?", [
                    "Az az értelmezési keret és előzetes tudásrendszer, amelyben a befogadó és a szöveg történelmi jelentése párbeszédbe lép egymással.",
                    "A papír szélessége, amire a verset nyomtatták.",
                    "A könyvesbolt nyitvatartási ideje."
                ], 0, ["c1-33-vocab"]),
                fb("grammar", "controlled", "A szimbólumok hálóját szemiotikailag _____ világossá válik a költő rejtett szándéka. (decoding / dekódolva)", "dekódolva", "Decoding the network of symbols semiotically the poet's hidden intention becomes clear.", ["c1-adv-semiotic-literary-hermeneutics"]),
                match("vocabulary", "controlled", [
                    ["poétikai szemiotika", "a költői jelek és szimbólumok rendszerének tudományos vizsgálata"],
                    ["hermeneutikai horizont", "az értelmező és a szöveg találkozásának távlata"],
                    ["jelentésréteg", "a szövegben egymásra rakódó mélyebb értelmi szintek"],
                    ["esztétikai kód", "a művészi formanyelv közös kulturális szabályrendszere"]
                ], ["c1-33-vocab"]),
                fb("grammar", "practice", "A szöveget hermeneutikai szempontból _____ új jelentésrétegek bontakoznak ki. (examining / vizsgálva)", "vizsgálva", "Examining the text from a hermeneutic perspective new layers of meaning unfold.", ["c1-adv-semiotic-literary-hermeneutics"]),
                sb("grammar", "practice", ["A", "költeményt", "hermeneutikai", "szempontból", "vizsgálva", "feltárulnak", "a", "mélyebb", "jelentések."], ["A", "költeményt", "hermeneutikai", "szempontból", "vizsgálva", "feltárulnak", "a", "mélyebb", "jelentések."], "Examining the poem from a hermeneutic perspective the deeper meanings are revealed.", ["c1-adv-semiotic-literary-hermeneutics"]),
                dc("dialogue", [
                    {"speaker": "Irodalomtörténész", "text": "Hogyan érdemes közelíteni a Nyugat költőinek szimbólumaihoz?"},
                    {"speaker": "Kritikus", "text": "Mindenekelőtt szemiotikailag dekódolva a képeket, és a hermeneutikai _____ tágítva a szövegek felé."},
                    {"speaker": "Irodalomtörténész", "text": "Csak így érthetjük meg a modernség mélységét."}
                ], ["horizontot", "szobát", "ablakot"], 0, ["c1-adv-semiotic-literary-hermeneutics"]),
                sw("production", [{"prompt": "Write a sentence analyzing poetic signs using an evaluative adverbial.", "answer": "A modernista líra metaforáit szemiotikailag dekódolva és hermeneutikai szempontból vizsgálva a szövegek rejtett poétikai rétegei és ontológiai dilemmái tárulnak fel az olvasó előtt."}], ["c1-adv-semiotic-literary-hermeneutics"]),
                mc("grammar", "check", "Melyik határozói szerkezet fejezi ki a szakszerű irodalomelméleti elemzést?", [
                    "szemiotikailag dekódolva / hermeneutikai szempontból vizsgálva",
                    "a könyvet gyorsan átlapozva az ágyban",
                    "verseket mondogatva a folyosón"
                ], 0, ["c1-adv-semiotic-literary-hermeneutics"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-33-02",
            "title": "Polyphonic Resonance & Textual Polysemy",
            "grammar_title": "Participial Clauses Analyzing Polyphonic Textual Resonance and Poetic Polysemy",
            "grammar_skill": "c1-participle-polyphonic-textual-polysemy",
            "goals": [
                "I can analyze textual polyphony, ambivalence, and poetic polysemy (*polifónia, többszólamúság, poétikai többértelműség, ambivalencia*).",
                "I can construct participial clauses analyzing layered textual resonances (*egymásba fonódó motívumokat rétegezve, a szöveg belső ambivalenciáját felszínre hozva, polifonikus rezonanciát keltve*).",
                "I can critique Bakhtinian polyphony in modern Hungarian narrative and lyric poetry."
            ],
            "vocab": [
                {"lemma": "polifónia", "translation": "polyphony / multi-voicedness", "pos": "noun"},
                {"lemma": "többszólamúság", "translation": "polyphonic texture", "pos": "noun"},
                {"lemma": "poétikai többértelműség", "translation": "poetic polysemy / ambiguity", "pos": "expression"},
                {"lemma": "ambivalencia", "translation": "ambivalence", "pos": "noun"},
                {"lemma": "szövegi rezonancia", "translation": "textual resonance", "pos": "expression"},
                {"lemma": "motívumháló", "translation": "network of recurring motifs", "pos": "noun"},
                {"lemma": "szemantikai feszültség", "translation": "semantic tension", "pos": "expression"},
                {"lemma": "hangnemváltás", "translation": "shift of tone / modulation", "pos": "noun"}
            ],
            "gr_text1": "Participial clauses in textual analysis delineate how multiple voices and meanings coexist within modernist literature: `egymással feleselő hangokat megszólaltatva` (articulating voices in dialogue with one another), `a szöveg belső szemantikai feszültségeit kibontva` (unfolding the text's internal semantic tensions), `gazdag polifonikus rezonanciát keltve az olvasóban` (generating rich polyphonic resonance in the reader).",
            "gr_text2": "Example: `A regény a különböző narrátori nézőpontokat egymásra rétegezve és a poétikai többértelműséget fenntartva alkot megkerülhetetlen remekművet`.",
            "gr_table": [
                ["A szerző a különböző hangokat egymásba fonva hozza létre a polifóniát.", "Intertwining different voices the author creates polyphony."],
                ["A motívumokat rétegezve a költő gazdag jelentéshálót sző.", "Layering motifs the poet weaves a rich web of meaning."],
                ["A belső ambivalenciát felmutatva a mű ellenáll az egyszerűsítő olvasatoknak.", "Displaying internal ambivalence the work resists simplistic readings."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a poétikai többértelműség (poliszémia) a modernista lírában?", [
                    "Azt a jelenséget, amikor egy költői kép vagy kifejezés egyszerre több egymással összefüggő, olykor feszültségben álló jelentést hordoz anélkül, hogy egyetlen definícióra szűkíthető lenne.",
                    "Azt, hogy a költő nem tudta eldönteni a szavak helyesírását.",
                    "Amikor egy verset több nyelven egyszerre mondanak el a rádióban."
                ], 0, ["c1-33-vocab"]),
                fb("grammar", "controlled", "A szerző a motívumokat finoman egymásra _____ hozta létre a mű polifonikus mélységét. (layering / rétegezve)", "rétegezve", "Delicately layering motifs on top of one another the author created the work's polyphonic depth.", ["c1-participle-polyphonic-textual-polysemy"]),
                match("vocabulary", "controlled", [
                    ["polifónia", "különböző önálló szólamok és nézőpontok egyidejű jelenléte a műben"],
                    ["poétikai többértelműség", "egymásnak feszülő jelentések harmonikus együttélése"],
                    ["szemantikai feszültség", "az ellentétes fogalmak által gerjesztett költői energia"],
                    ["motívumháló", "a művön végigvonuló visszatérő gondolati elemek szövedéke"]
                ], ["c1-33-vocab"]),
                fb("grammar", "practice", "A belső ambivalenciát felszínre _____ a mű elkerüli a didaktikus leegyszerűsítést. (bringing / hozva)", "hozva", "Bringing internal ambivalence to the surface the work avoids didactic simplification.", ["c1-participle-polyphonic-textual-polysemy"]),
                sb("grammar", "practice", ["A", "szerző", "a", "motívumokat", "rétegezve", "polifonikus", "rezonanciát", "teremtett."], ["A", "szerző", "a", "motívumokat", "rétegezve", "polifonikus", "rezonanciát", "teremtett."], "Layering the motifs the author created polyphonic resonance.", ["c1-participle-polyphonic-textual-polysemy"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Mi teszi Babits líráját olyan utánozhatatlanul gazdaggá?"},
                    {"speaker": "Egyetemi oktató", "text": "Az, hogy az antik és keresztény mítoszokat egymásra _____ páratlan polifonikus mélységet teremt."},
                    {"speaker": "Kritikus", "text": "A szövegi rezonanciák szinte végtelenek."}
                ], ["rétegezve", "dobva", "írva"], 0, ["c1-participle-polyphonic-textual-polysemy"]),
                sw("production", [{"prompt": "Write a critical evaluation of textual polyphony using a participial clause.", "answer": "A szerző a különböző filozófiai nézőpontokat egymással dialógusba léptetve és a motívumokat szervesen rétegezve olyan polifonikus rezonanciát hoz létre, amely a modern ember egzisztenciális vívódásait tükrözi."}], ["c1-participle-polyphonic-textual-polysemy"]),
                mc("grammar", "check", "Melyik mondat alkalmaz helyesen melléknévi igeneves szerkezetet a többszólamúság kifejezésére?", [
                    "a költői hangokat egymásba fonva és a többértelműséget fenntartva mély rezonanciát kelt",
                    "a költő sok szót ír a papírra ceruzával",
                    "ha a könyv hosszú, sok idő elolvasni"
                ], 0, ["c1-participle-polyphonic-textual-polysemy"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-33-03",
            "title": "Aesthetic Duty & Universal Humanism",
            "grammar_title": "Deontic Modal Structures Asserting Aesthetic Duty of Universal Humanism",
            "grammar_skill": "c1-modal-deontic-aesthetic-humanism",
            "goals": [
                "I can analyze Babits's aesthetic humanism, moral duty of the intellectual, and anti-barbaric cultural commitment (*esztétikai humanizmus, írástudók árulása, erkölcsi imperatívusz, a szellem védelme*).",
                "I can deploy elevated deontic modal structures asserting intellectual and ethical duties (*a művésznek kötelessége a barbárság ellenében a szellem őrének lenni, megalkuvást nem ismerve kell hirdetni az egyetemes humánum értékeit, elengedhetetlen a morális autonómia megőrzése*).",
                "I can critique Julien Benda's 'La Trahison des Clercs' in Hungarian intellectual history."
            ],
            "vocab": [
                {"lemma": "esztétikai humanizmus", "translation": "aesthetic humanism", "pos": "expression"},
                {"lemma": "írástudók felelőssége", "translation": "responsibility of intellectuals (clerks)", "pos": "expression"},
                {"lemma": "erkölcsi imperatívusz", "translation": "moral imperative", "pos": "expression"},
                {"lemma": "a szellem védelme", "translation": "defense of the spirit / culture", "pos": "expression"},
                {"lemma": "egyetemes humánum", "translation": "universal humanism", "pos": "expression"},
                {"lemma": "kulturális barbarizmus", "translation": "cultural barbarism", "pos": "expression"},
                {"lemma": "szellemi arisztokratizmus", "translation": "intellectual aristocratic spirit", "pos": "expression"},
                {"lemma": "morális autonómia", "translation": "moral autonomy", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures in cultural philosophy establish the imperative duty of writers to stand against tyranny and moral degeneration: `az írástudónak szent kötelessége szót emelni a barbárság ellen` (it is the sacred duty of the intellectual to speak up against barbarism), `nem engedhető meg, hogy a művészet a politikai propaganda eszközévé alacsonyuljon` (it cannot be permitted that art degrade into a tool of political propaganda), `megalkuvást nem ismerve kell őrködni az egyetemes humánum felett` (one must watch over universal humanism without compromise).",
            "gr_text2": "Example: `Babits Mihály szerint az írástudónak kötelessége hűnek maradnia a szellem autonómiájához, még akkor is, ha a kor hisztériája a pusztulásba sodorja a világot`.",
            "gr_table": [
                ["Az alkotónak kötelessége ellenállnia a politikai megalkuvás kísértésének.", "It is the duty of the creator to resist the temptation of political compromise."],
                ["Elengedhetetlen az egyetemes emberi értékek védelme a barbarizmussal szemben.", "The defense of universal human values against barbarism is indispensable."],
                ["A költőnek megalkuvást nem ismerve kell őriznie a morális autonómiát.", "The poet must preserve moral autonomy without compromise."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'írástudók árulása' (Julien Benda és Babits szellemében)?", [
                    "Azt a morális züllést, amikor az értelmiségiek és művészek feladják az egyetemes igazság és humánum védelmét, és behódolnak a nacionalista vagy totalitárius politikai hatalomnak.",
                    "Amikor valaki elfelejt tollat vinni az írótalálkozóra.",
                    "Amikor egy szerző hibásan adja le a kéziratát a nyomdának."
                ], 0, ["c1-33-vocab"]),
                fb("grammar", "controlled", "Az alkotónak erkölcsi _____ a szellem tisztaságát védeni a totalitárius tébollyal szemben. (duty / kötelessége)", "kötelessége", "It is the moral duty of the creator to defend the purity of the spirit against totalitarian madness.", ["c1-modal-deontic-aesthetic-humanism"]),
                match("vocabulary", "controlled", [
                    ["esztétikai humanizmus", "a művészet és a morál elválaszthatatlan egységébe vetett hit"],
                    ["erkölcsi imperatívusz", "belső, feltétlen etikai parancs a jó cselekvésére"],
                    ["egyetemes humánum", "az emberi méltóság és szabadság határokon átívelő eszméje"],
                    ["a szellem védelme", "a kultúra autonómiájának megóvása a politikai önkénytől"]
                ], ["c1-33-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ a kultúra egyetemes értékei mellett. (stand / kiállni)", "kiállni", "Without compromise one must stand up for the universal values of culture.", ["c1-modal-deontic-aesthetic-humanism"]),
                sb("grammar", "practice", ["Az", "írástudónak", "kötelessége", "megvédeni", "az", "egyetemes", "humánum", "eszméjét."], ["Az", "írástudónak", "kötelessége", "megvédeni", "az", "egyetemes", "humánum", "eszméjét."], "It is the duty of the intellectual to defend the idea of universal humanism.", ["c1-modal-deontic-aesthetic-humanism"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Mi Babits 'Jónás könyve' című művének legfőbb erkölcsi tanítása?"},
                    {"speaker": "Irodalomtörténész", "text": "Az, hogy a prófétának, a költőnek kötelessége hirdetnie az igazságot, mert 'vétkesek közt cinkos, aki _____ '."},
                    {"speaker": "Filozófus", "text": "A hallgatás maga a bűnrészesség."}
                ], ["néma", "hangos", "gyors"], 0, ["c1-modal-deontic-aesthetic-humanism"]),
                sw("production", [{"prompt": "Write a philosophical assertion of the writer's duty using a deontic modal structure.", "answer": "Az írástudónak morális kötelessége ellenállni a barbár politikai ideológiák csábításának, és megalkuvást nem ismerve kell őrködnie az egyetemes humánum és az esztétikai autonómia megmaradása felett."}], ["c1-modal-deontic-aesthetic-humanism"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fejezi ki a szellemi ember erkölcsi felelősségét a legerőteljesebben?", [
                    "kötelessége a szellem őrének lenni / megalkuvást nem ismerve kell kiállni a humánum mellett",
                    "jó lenne ha mindenki elolvasna egy verset havonta",
                    "a költők néha találkozhatnak egy kávézóban beszélgetni"
                ], 0, ["c1-modal-deontic-aesthetic-humanism"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-33-04",
            "title": "Intertextuality & European Literary Genealogy",
            "grammar_title": "Scalar Comparative Adverbials Tracing European Intertextual Literary Genealogy",
            "grammar_skill": "c1-adv-comparative-intertextuality-scalar",
            "goals": [
                "I can analyze intertextual literary genealogy, translation poetics, and European cultural lineage (*intertextualitás, európai genealógia, műfordítás-poétika, kánonformálás*).",
                "I can deploy scalar comparative adverbials tracing literary lineage (*szervesebben kapcsolódva a dantei hagyományhoz, mélyrehatóbban merítve az antik forrásokból, felülmúlhatatlanul gazdagítva a nemzeti nyelvet*).",
                "I can discuss the Nyugat movement's translation philosophy (Babits: Dante Isteni színjátéka)."
            ],
            "vocab": [
                {"lemma": "intertextualitás", "translation": "intertextuality", "pos": "noun"},
                {"lemma": "műfordítás-poétika", "translation": "poetics of translation", "pos": "expression"},
                {"lemma": "európai genealógia", "translation": "European literary genealogy", "pos": "expression"},
                {"lemma": "dantei hagyomány", "translation": "Dantean tradition", "pos": "expression"},
                {"lemma": "kánonformálás", "translation": "canon formation", "pos": "noun"},
                {"lemma": "szellemi rokonság", "translation": "intellectual kinship / elective affinity", "pos": "expression"},
                {"lemma": "kulturális transzfer", "translation": "cultural transfer", "pos": "expression"},
                {"lemma": "klasszicizálódás", "translation": "classicization", "pos": "noun"}
            ],
            "gr_text1": "Scalar comparative adverbials establish the depth of a writer's integration into world literature: `szervesebben kapcsolódva az európai fősodorhoz` (more organically connecting to the European mainstream), `mélyrehatóbban merítve a klasszikus hagyományból, mint kortársai` (drawing more profoundly from classical tradition than his contemporaries), `felülmúlhatatlanul gazdagítva az anyanyelv kifejezőerejét` (insurpassably enriching the expressive power of the mother tongue).",
            "gr_text2": "Example: `Babits Mihály a Dante-fordítás révén szervesebben kapcsolódva az európai kánonhoz, felülmúlhatatlanul gazdagította a magyar nyelv poétikai határait`.",
            "gr_table": [
                ["Babits mélyrehatóbban merített a görög-római lírából, mint a legtöbb kortársa.", "Babits drew more profoundly from Greco-Roman lyric than most of his peers."],
                ["A műfordítás szervesebben kapcsolta a magyar irodalmat a világirodalmi kánonhoz.", "Translation connected Hungarian literature more organically to the world literary canon."],
                ["A dantei hatás felülmúlhatatlanul formálta át a költő kompozíciós készségét.", "The Dantean influence insurpassably transformed the poet's compositional skill."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető mérföldkőnek Babits Mihály Dante Isteni színjáték-fordítása?", [
                    "Mert nem egyszerű fordítás volt, hanem a magyar nyelv poétikai határainak kitágítása és a nemzeti irodalom szerves integrálása az európai klasszikus kánonba.",
                    "Mert ez volt az első könyv, amit bőrkötésben nyomtattak ki.",
                    "Mert a szerző ingyen osztogatta az utcán."
                ], 0, ["c1-33-vocab"]),
                fb("grammar", "controlled", "Babits sokkal szervesebben _____ az európai örökséghez, mint a provinciális szerzők. (connected / kapcsolódott)", "kapcsolódott", "Babits connected much more organically to European heritage than provincial authors.", ["c1-adv-comparative-intertextuality-scalar"]),
                match("vocabulary", "controlled", [
                    ["intertextualitás", "szövegek közötti tudatos vagy rejtett párbeszéd és utalásháló"],
                    ["műfordítás-poétika", "az idegen nyelvű remekművek anyanyelvi újrateremtésének művészete"],
                    ["európai genealógia", "a közös európai szellemi és irodalmi leszármazás vonala"],
                    ["kulturális transzfer", "eszmék és formák vándorlása nemzeti kultúrák között"]
                ], ["c1-33-vocab"]),
                fb("grammar", "practice", "A költő mélyrehatóbban _____ az antik hagyományból, mint kortársai. (drew / merített)", "merített", "The poet drew more profoundly from classical tradition than his contemporaries.", ["c1-adv-comparative-intertextuality-scalar"]),
                sb("grammar", "practice", ["Babits", "szervesebben", "kapcsolódott", "az", "európai", "kánonhoz,", "mint", "kortársai."], ["Babits", "szervesebben", "kapcsolódott", "az", "európai", "kánonhoz,", "mint", "kortársai."], "Babits connected more organically to the European canon than his contemporaries.", ["c1-adv-comparative-intertextuality-scalar"]),
                dc("dialogue", [
                    {"speaker": "Összehasonlító irodalmár", "text": "Hogyan határozta meg a Nyugat nemzedéke a világirodalomhoz való viszonyt?"},
                    {"speaker": "Babits-kutató", "text": "Úgy, hogy a világirodalmi kincsekből mélyrehatóbban merítve akarták megújítani a hazai _____."},
                    {"speaker": "Összehasonlító irodalmár", "text": "A provincializmus felszámolása volt a legfőbb céljuk."}
                ], ["líratörténetet", "mezőgazdaságot", "közlekedést"], 0, ["c1-adv-comparative-intertextuality-scalar"]),
                sw("production", [{"prompt": "Write a comparative analysis of literary lineage using a scalar comparative adverbial.", "answer": "Babits Mihály a világirodalom klasszikus kánonjához szervesebben kapcsolódva és az európai intertextuális hagyományból mélyrehatóbban merítve bizonyította be, hogy a nemzeti kultúra nagysága az egyetemes szellemmel való termékeny párbeszédben gyökerezik."}], ["c1-adv-comparative-intertextuality-scalar"]),
                mc("grammar", "check", "Melyik fokozó hasonlító határozói forma elemzi a világirodalmi kapcsolatokat a legpontosabban?", [
                    "szervesebben kapcsolódva a kánonhoz / mélyrehatóbban merítve az antik forrásokból",
                    "kicsit jobban olvasva a könyveket mint mások",
                    "több verset írva mint a szomszédai"
                ], 0, ["c1-adv-comparative-intertextuality-scalar"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-33-05",
            "title": "Mihály Babits: The History of European Literature",
            "grammar_title": "Evaluative Correlative Syntax Formulating Hermeneutic Synthesis of World Literary Canons",
            "grammar_skill": "c1-syntax-hermeneutic-canon-synthesis",
            "goals": [
                "I can analyze Babits Mihály's magnum opus 'Az európai irodalom története', literary canon formation, and the unity of European culture (*Az európai irodalom története, szerves egység, kánonszintézis, szellemi kontinuitás*).",
                "I can construct evaluative correlative syntax formulating hermeneutic synthesis (*ahogyan a görög tragédiák alapozták meg a lélek katarzisát, úgy ölt testet az európai szellem egysége a reneszánsz és a modernitás folyamatosságában*).",
                "I can synthesize the humanist manifesto of Hungarian literary modernism."
            ],
            "vocab": [
                {"lemma": "Az európai irodalom története", "translation": "History of European Literature (Babits masterpiece)", "pos": "expression"},
                {"lemma": "szerves egység", "translation": "organic unity", "pos": "expression"},
                {"lemma": "kánonszintézis", "translation": "canon synthesis", "pos": "noun"},
                {"lemma": "szellemi kontinuitás", "translation": "spiritual / intellectual continuity", "pos": "expression"},
                {"lemma": "közös emlékezet", "translation": "collective cultural memory", "pos": "expression"},
                {"lemma": "világirodalmi távlat", "translation": "world literary perspective", "pos": "expression"},
                {"lemma": "humanista hitvallás", "translation": "humanist creed / confession", "pos": "expression"},
                {"lemma": "szellemi világpolgárság", "translation": "intellectual cosmopolitanism", "pos": "expression"}
            ],
            "gr_text1": "Evaluative correlative syntax synthesizes universal cultural heritage across epochs: `ahogyan az antikvitás megteremtette a forma és a szabadság harmóniáját, úgy bontakozik ki az európai irodalom szerves egysége Babits szintézisében` (just as antiquity established the harmony of form and freedom, so unfolds the organic unity of European literature in Babits's synthesis), `amennyire fenyegeti a barbárság a kultúrát, annyira válik imperatívusszá a kánon megőrzése` (as much as barbarism threatens culture, so much does preserving the canon become an imperative).",
            "gr_text2": "Example: `Ahogyan Homérosz és Dante kijelölte a szellem útját, úgy fogja össze Babits monumentális műve az európai kontinuitás megbonthatatlan szövetségét`.",
            "gr_table": [
                ["Ahogyan a folyók a tengerbe ömlenek, úgy egyesül minden nemzeti irodalom az európai kánonban.", "As rivers flow into the sea, so every national literature unites in the European canon."],
                ["Amennyire pusztító a barbárság, annyira nélkülözhetetlen a szellemi kontinuitás védelme.", "As destructive as barbarism is, so indispensable is the defense of intellectual continuity."],
                ["Ahogyan Babits látta a világirodalmat, úgy tekintünk ma is a közös európai kultúrára.", "As Babits saw world literature, so do we look at common European culture today."]
            ],
            "classic_story": {
                "slug": "babits-europai-irodalom-tortenete",
                "title": "Babits Mihály: Az európai irodalom története",
                "author": "Babits Mihály",
                "work": "Az európai irodalom története (1934–1935)",
                "summary": "Babits Mihály (1883–1941) költő, regényíró, esszéista, műfordító, a Nyugat folyóirat főszerkesztője, a huszadik századi magyar irodalom szellemi fejedelme. Amikor Európában a fasizmus és a nácizmus barbarizmusa kezdte elborítani a kultúrát, Babits megírta monumentális szintézisét, 'Az európai irodalom történetét'. Műve nem száraz lexikon, hanem lángoló hitvallás: az európai kultúra nem egymással háborúzó nemzetek elszigetelt töredéke, hanem egyetlen élő, szerves szervezet, amely Homérosztól és a Bibliától Dantén, Shakespeare-en és Goethén át a modernségig a szellem és az emberi méltóság kontinuitását hordozza.",
                "characters": ["Babits Mihály, a szellem őre", "Európai költők és bölcsek"],
                "paragraphs": [
                    {"type": "narration", "text": "Az 1930-as évek derekán Európa felett sötét viharfelhők gyülekeztek: a totalitárius eszmék előretörése, a könyvégetések és a faji gőg azzal fenyegettek, hogy elpusztítják mindazt, amit a humanista civilizáció évezredek alatt felépített. Ebben a tragikus órában vonult vissza esztergomi magányába Babits Mihály, hogy megírja élete főművét."},
                    {"type": "dialogue", "speaker": "Babits Mihály", "text": "Az európai irodalom nem független nemzeti irodalmak mechanikus halmaza, hanem egyetlen élő test, egy közös szellem lélegzése. Ahogyan a vér kering a testben, úgy áramlik a gondolat Homérosztól Dantén át a mi korunkig: aki egyetlen nép kultúráját elszakítja ettől a szerves egységtől, az halálra ítéli a nemzet lelkét."},
                    {"type": "narration", "text": "Babits hatalmas tablóján megelevenedett a görög tragédiák katarzisa, a római jog és rend szelleme, a középkori kereszténység transzcendenciája és a reneszánsz emberközpontúsága. Minden korszak egy-egy újabb állomása volt az emberi szabadságért és az igazságért vívott küzdelemnek."},
                    {"type": "narration", "text": "Az európai irodalom története a magyar szellemtörténet legnagyszerűbb humanista kiáltványa maradt. Bebizonyította, hogy a magyarság nem a Nyugattól elzárt, provinciális sziget, hanem az európai szellemi kánon elválaszthatatlan és büszke örököse."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan fogta fel Babits Mihály az európai irodalom lényegét főművében?", [
                    "Egyetlen élő, szerves szellemi egységként, amelyben minden nemzet irodalma egy közös humanista örökség és folytonos párbeszéd része.",
                    "Különböző országok könyvtárainak leltári katalógusaként.",
                    "Egy olyan verseskötetként, amit csak latinul szabad olvasni."
                ], 0, ["c1-33-vocab"]),
                fb("grammar", "controlled", "Ahogyan az antikvitás megteremtette a formát, _____ teljesedett ki a reneszánsz szellemisége. (so / úgy)", "úgy", "As antiquity created the form, so was the spirit of the Renaissance fulfilled.", ["c1-syntax-hermeneutic-canon-synthesis"]),
                match("vocabulary", "controlled", [
                    ["Az európai irodalom története", "Babits monumentális, antifasiszta humanista kánonszintézise"],
                    ["szerves egység", "a kultúrák elválaszthatatlan belső összefonódása"],
                    ["szellemi kontinuitás", "az emberi értékek töretlen áthagyományozódása a korszakokon át"],
                    ["szellemi világpolgárság", "nyitottság az egyetemes kultúra minden kincsére a nemzeti gyökerekből kiindulva"]
                ], ["c1-33-vocab"]),
                fb("grammar", "practice", "Amennyire terjed a barbárság, _____ sürgetőbb a humanista kánon védelme. (as much / annyira)", "annyira", "As much as barbarism spreads, so much more urgent is the defense of the humanist canon.", ["c1-syntax-hermeneutic-canon-synthesis"]),
                sb("grammar", "practice", ["Ahogyan", "az", "európai", "szellem", "egységes,", "úgy", "marad", "fenn", "a", "kultúra."], ["Ahogyan", "az", "európai", "szellem", "egységes,", "úgy", "marad", "fenn", "a", "kultúra."], "As the European spirit is unified, so does culture endure.", ["c1-syntax-hermeneutic-canon-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi professzor", "text": "Mi Babits irodalomtörténetének legidőszerűbb üzenete ma?"},
                    {"speaker": "Doktorandusz", "text": "Az, hogy ahogyan a múltban a barbárság pusztított, úgy kell ma is őriznünk a szellemi kontinuitás _____."},
                    {"speaker": "Egyetemi professzor", "text": "A kultúra a legfőbb védőpajzsunk az elbutulással szemben."}
                ], ["fényét", "árát", "helyét"], 0, ["c1-syntax-hermeneutic-canon-synthesis"]),
                sw("production", [{"prompt": "Write a synthesis of the European literary canon using evaluative correlative syntax.", "answer": "Ahogyan az antikvitás és a reneszánsz megteremtette a polgári szabadság és a forma harmóniáját, úgy bizonyítja Babits Mihály remekműve, hogy a nemzeti kultúra kizárólag az egyetemes európai kánon szerves részeként töltheti be hivatását."}], ["c1-syntax-hermeneutic-canon-synthesis"]),
                mc("grammar", "check", "Melyik páros szerkezet valósítja meg a világirodalmi kánonszintézis kifejezését?", [
                    "ahogyan Homérosz és Dante kijelölte a szellem útját, úgy fogja össze a mű az európai kontinuitást",
                    "amikor a diák kinyitja a tankönyvet és elolvassa a fejezetet",
                    "ha sok könyvet vásárolunk, akkor betelik a polc"
                ], 0, ["c1-syntax-hermeneutic-canon-synthesis"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(33, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        33,
        "core",
        "c1-33-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of poetic semiotics, textual polyphony, and literary canon formation.",
            "I can employ semiotic evaluative adverbials, participial polysemy clauses, and deontic modal structures of humanism.",
            "I can synthesize Babits Mihály's History of European Literature and formulate the universal humanist ethos."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés elemzi a legszakszerűbben a költői szimbólumok jelentésrétegeit?", [
                "szemiotikailag dekódolva / hermeneutikai szempontból vizsgálva",
                "hogyha valaki szépen szaval az iskolai ünnepségen",
                "amikor a költő rímeket keres a szótárban"
            ], 0, ["c1-adv-semiotic-literary-hermeneutics"]),
            mc("grammar", "recognize", "Milyen szerkezettel mutatható fel a szövegi polifónia és többértelműség a leghitelesebben?", [
                "a motívumokat szervesen rétegezve és a belső ambivalenciát felszínre hozva",
                "amikor sok szereplő beszél egyszerre a színpadon",
                "ha a könyv nagyon vastag és sok fejezetből áll"
            ], 0, ["c1-participle-polyphonic-textual-polysemy"]),
            match("vocabulary", "recognize", [
                ["poétikai szemiotika", "a költői jelek és szimbólumok rendszerének elmélete"],
                ["polifónia", "több önálló gondolati szólam egyidejű költői jelenléte"],
                ["esztétikai humanizmus", "az alkotó morális hűsége az egyetemes emberi értékekhez"],
                ["kánonszintézis", "a világirodalmi remekművek szerves egységbe foglalása"]
            ], ["c1-33-vocab"]),
            fb("vocabulary", "recall", "Az írástudóknak kötelességük szót emelni a szellemi _____ ellen minden korban. (barbarism / barbarizmus)", "barbarizmus", "Intellectuals have a duty to speak up against spiritual barbarism in every era.", ["c1-33-vocab"]),
            fb("vocabulary", "recall", "Az európai irodalom nem elszigetelt művek halmaza, hanem egyetlen élő és _____ egység. (organic / szerves)", "szerves", "European literature is not a heap of isolated works but a single living and organic unity.", ["c1-33-vocab"]),
            fb("grammar", "recall", "A vers képeit szemiotikailag _____ a mélyebb rétegek tárulnak fel. (decoding / dekódolva)", "dekódolva", "Decoding the poem's images semiotically deeper strata are revealed.", ["c1-adv-semiotic-literary-hermeneutics"]),
            fb("grammar", "context", "Az alkotónak erkölcsi _____ a szellem szabadságát őrizni a hatalmi nyomással szemben. (duty / kötelessége)", "kötelessége", "It is the creator's moral duty to preserve the freedom of the spirit against power pressure.", ["c1-modal-deontic-aesthetic-humanism"]),
            fb("grammar", "context", "Ahogyan az antikvitás megteremtette az eszményt, _____ őrzi a kánon az örök értékeket. (so / úgy)", "úgy", "As antiquity created the ideal, so does the canon preserve eternal values.", ["c1-syntax-hermeneutic-canon-synthesis"]),
            mc("grammar", "context", "Mi Babits szerint az irodalmi kánon legfőbb hivatása válságos történelmi korszakokban?", [
                "A szellemi kontinuitás megőrzése és az egyetemes humánum felmutatása a politikai barbarizmussal és gyűlöletkeltéssel szemben.",
                "A könyvek árainak alacsonyan tartása a piacokon.",
                "A külföldi írók kitiltása a nemzeti könyvtárakból."
            ], 0, ["c1-syntax-hermeneutic-canon-synthesis"]),
            sb("grammar", "produce", ["A", "szellem", "autonómiájának", "megőrzése", "az", "írástudók", "szent", "kötelessége."], ["A", "szellem", "autonómiájának", "megőrzése", "az", "írástudók", "szent", "kötelessége."], "Preserving the autonomy of the spirit is the sacred duty of intellectuals.", ["c1-modal-deontic-aesthetic-humanism"]),
            sw("production", [{"prompt": "Write a critical evaluation of poetic polyphony using a participial clause.", "answer": "A költő a különböző kulturális és bibliai motívumokat egymásra rétegezve olyan polifonikus rezonanciát kelt a szövegben, amely megnyitja a művet a végtelen hermeneutikai értelmezés előtt."}], ["c1-participle-polyphonic-textual-polysemy"]),
            sw("production", [{"prompt": "Synthesize Babits's vision of European literature using evaluative correlative syntax.", "answer": "Ahogyan az európai kultúra évezredeken átívelő kontinuitása táplálja a nemzeti öntudatot, úgy bizonyítja Babits szintézise, hogy az egyetemes humánum védelme a magyar irodalom legnemesebb hivatása."}], ["c1-syntax-hermeneutic-canon-synthesis"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-irodalmielet)
    # ----------------------------------------------------
    disc_intro = [
        "In contemporary Hungary, literature and school curricula became ideological battlegrounds of the illiberal state, seeking to replace autonomous aesthetic value with nationalist propaganda, centralized textbooks, and state-directed cultural blacklists.",
        "In this unit, following the battles over the 2020 National Core Curriculum (NAT), the state publishing monopoly, political blacklisting under the Petőfi Literary Museum (PIM), and the courageous resistance of independent writers and teachers, you will master the critical discourse of canon wars, ideological indoctrination, and aesthetic pluralism at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The National Curriculum & Ideological Indoctrination",
            "grammar_title": "Discourse Framing Markers Diagnosing State Ideological Indoctrination Through Educational Curricula",
            "grammar_skill": "c1-discourse-canon-indoctrination-framing",
            "goals": [
                "I can analyze the 2020 National Core Curriculum (NAT), ideological canon restructuring, and political author favoritism (*Nemzeti Alaptanterv, ideológiai kánonátszabás, Wass Albert és Nyirő József kötelezővé tétele, Kertész Imre háttérbe szorítása*).",
                "I can deploy discourse framing markers diagnosing pedagogical indoctrination (*az állami indoktrináció szisztematikus kísérleteként értékelve, a kánon politikai átideologizálásaként aposztrofálva, a szakmai autonómia felszámolásának jegyében*).",
                "I can critique nationalist revisionism in literature education."
            ],
            "vocab": [
                {"lemma": "Nemzeti Alaptanterv", "translation": "National Core Curriculum (NAT)", "pos": "expression"},
                {"lemma": "kánonátszabás", "translation": "ideological restructuring of the literary canon", "pos": "noun"},
                {"lemma": "ideológiai indoktrináció", "translation": "ideological indoctrination", "pos": "expression"},
                {"lemma": "kötelező olvasmány", "translation": "compulsory reading", "pos": "expression"},
                {"lemma": "pedagógiai autonómia", "translation": "pedagogical autonomy", "pos": "expression"},
                {"lemma": "szélsőjobboldali szerzők", "translation": "far-right / nationalist authors", "pos": "expression"},
                {"lemma": "Nobel-díjas", "translation": "Nobel laureate (reference to Kertész Imre)", "pos": "noun"},
                {"lemma": "szakmai tiltakozás", "translation": "professional protest / backlash", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers expose state-directed ideological manipulation of school curricula: `az állami indoktrináció szisztematikus kísérleteként értékelve` (evaluated as a systematic attempt at state indoctrination), `a nemzeti kánon politikai célzatú átírásaként aposztrofálva` (characterized as politically motivated rewriting of the national canon), `a pedagógiai szabadság brutális megnyirbálásának jegyében` (in the name of brutally curtailing pedagogical freedom).",
            "gr_text2": "Example: `A 2020-as Nemzeti Alaptantervet a szakmai szervezetek nyílt politikai indoktrinációként értékelve tiltakoztak a szélsőjobboldali szerzők kötelezővé tétele ellen`.",
            "gr_table": [
                ["A reformot a tanterv politikai átideologizálásaként értékelve léptek fel a magyartanárok.", "Evaluating the reform as political ideologization of the curriculum Hungarian teachers took action."],
                ["A pedagógiai autonómia felszámolásaként aposztrofálták a központosított szerzői listát.", "They characterized the centralized author list as the elimination of pedagogical autonomy."],
                ["Az állami indoktrináció jegyében szorították háttérbe a modern világirodalmat.", "In the spirit of state indoctrination modern world literature was pushed to the background."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-01-nemzeti-alaptanterv-ideologia",
                "title": "A kánon átszabása: A 2020-as NAT és a nacionalista mítoszok",
                "summary": "2020 elején a kormányzat bevezette az új Nemzeti Alaptantervet, amely kötelezővé tette a Horthy-korszak antiszemita és nacionalista szerzőit, miközben háttérbe szorította az egyetemes értékeket képviselő kortárs alkotókat és a Nobel-díjas Kertész Imrét.",
                "paragraphs": [
                    {"type": "narration", "text": "2020 januárjában a magyar közoktatás történetének legmegosztóbb tantervi reformját hirdették ki. Az új Nemzeti Alaptanterv (NAT) irodalmi fejezete nem a szakmai konszenzust, hanem a kormányzó párt ideológiai elvárásait tükrözte."},
                    {"type": "dialogue", "speaker": "Magyartanár", "text": "A kánon politikai célzatú átszabásaként értékelve a reformot felháborító, hogy Wass Albertet és a nyilas szimpatizáns Nyirő Józsefet kötelező tananyaggá tették, miközben az egyetlen magyar irodalmi Nobel-díjas, Kertész Imre műveit vagy Ottlik Gézát a margóra száműzték."},
                    {"type": "narration", "text": "A Magyartanárok Egyesülete és a Magyar Tudományos Akadémia Irodalomtudományi Intézete példátlanul kemény nyilatkozatban ítélte el a tantervet: rávilágítottak, hogy a dokumentum az esztétikai minőség helyébe a nacionalista propagandát állítja."},
                    {"type": "narration", "text": "Tanárok és diákok országszerte sztrájkokkal és tiltakozó akciókkal álltak ki a pedagógiai szabadság mellett, megfogadva, hogy nem hajlandók a hatalmi indoktrináció eszközeivé válni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért váltott ki országos felháborodást a 2020-as Nemzeti Alaptanterv irodalmi része?", [
                    "Mert szakmai egyeztetés nélkül, politikai és nacionalista alapon írta át a kánont: kötelezővé tett szélsőjobboldali szerzőket, miközben háttérbe szorította a valódi esztétikai csúcsokat képviselő alkotókat.",
                    "Mert elrendelte, hogy minden verset fejből és énekelve kell elmondani.",
                    "Mert túl sok képregényt tett kötelezővé a diákoknak."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A lépést politikai indoktrinációként _____ a tanárok szövetsége elutasította az új tantervet. (evaluating / értékelve)", "értékelve", "Evaluating the step as political indoctrination the teachers' association rejected the new curriculum.", ["c1-discourse-canon-indoctrination-framing"]),
                match("vocabulary", "controlled", [
                    ["Nemzeti Alaptanterv", "az iskolai oktatás kötelező állami szabályozó dokumentuma"],
                    ["kánonátszabás", "a tanítandó szerzők politikai szempontú erőszakos lecserélése"],
                    ["pedagógiai autonómia", "a pedagógus joga a tanítási módszerek és művek szabad megválasztására"],
                    ["ideológiai indoktrináció", "a tanulók egyoldalú politikai befolyásolása az iskolában"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A kánon politikai átírásaként _____ a szakma keményen bírálta a döntést. (characterizing / aposztrofálva)", "aposztrofálva", "Characterizing the decision as political rewriting of the canon the profession harshly criticized it.", ["c1-discourse-canon-indoctrination-framing"]),
                sb("grammar", "practice", ["A", "kánon", "átszabása", "durván", "sértette", "a", "pedagógiai", "autonómiát."], ["A", "kánon", "átszabása", "durván", "sértette", "a", "pedagógiai", "autonómiát."], "The restructuring of the canon severely violated pedagogical autonomy.", ["c1-discourse-canon-indoctrination-framing"]),
                dc("dialogue", [
                    {"speaker": "Szülő", "text": "Mi a legnagyobb veszélye az új tantervi szabályozásnak?"},
                    {"speaker": "Irodalomtanár", "text": "Az, hogy az állami indoktrináció szisztematikus kísérleteként eljárva megfosztja a diákokat a kritikai _____ fejlesztésétől."},
                    {"speaker": "Szülő", "text": "A diákoknak szabadon kell gondolkodniuk."}
                ], ["gondolkodás", "öltözködés", "számolás"], 0, ["c1-discourse-canon-indoctrination-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of curriculum indoctrination using a discourse framing marker.", "answer": "A Nemzeti Alaptanterv irodalmi fejezetét a nyílt politikai indoktrináció szisztematikus kísérleteként értékelve a szakmai szervezetek rávilágítottak arra, hogy az esztétikai autonómia felszámolása súlyosan veszélyezteti az oktatás minőségét."}], ["c1-discourse-canon-indoctrination-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a tantervi politikai manipulációt a legpontosabban?", [
                    "az állami indoktrináció szisztematikus kísérleteként értékelve / a kánon átideologizálásaként aposztrofálva",
                    "amikor új tankönyvet nyomtatnak szép képekkel",
                    "hogyha a diákok korán reggel mennek az iskolába"
                ], 0, ["c1-discourse-canon-indoctrination-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Textbook Monopoly & Uniform Curriculum",
            "grammar_title": "Critical Evaluative Adverbials Exposing State Textbook Monopolization and Pedagogical Regression",
            "grammar_skill": "c1-adv-textbook-monopoly-critique",
            "goals": [
                "I can analyze the elimination of free textbook choice, the state publishing monopoly, and uniform textbooks (*tankönyvpiac államosítása, tankönyv-monopólium, egyentankönyv, a választás szabadságának felszámolása*).",
                "I can deploy critical evaluative adverbials exposing state educational monopolies (*önkényesen centralizálva a kiadást, a piaci versenyt erőszakosan felszámolva, pedagógiailag igénytelen módon homogenizálva a tananyagot*).",
                "I can assess pedagogical regression caused by forced ideological uniformity."
            ],
            "vocab": [
                {"lemma": "tankönyv-monopólium", "translation": "state textbook publishing monopoly", "pos": "expression"},
                {"lemma": "egyentankönyv", "translation": "uniform state textbook", "pos": "noun"},
                {"lemma": "tankönyvpiac államosítása", "translation": "nationalization of the textbook market", "pos": "expression"},
                {"lemma": "választási szabadság", "translation": "freedom of textbook choice", "pos": "expression"},
                {"lemma": "pedagógiai regresszió", "translation": "pedagogical regression", "pos": "expression"},
                {"lemma": "központosított terjesztés", "translation": "centralized textbook distribution", "pos": "expression"},
                {"lemma": "minőségromlás", "translation": "deterioration of quality", "pos": "noun"},
                {"lemma": "piaci verseny felszámolása", "translation": "elimination of market competition", "pos": "expression"}
            ],
            "gr_text1": "Critical evaluative adverbials expose state monopolization and arbitrary central control in textbook publishing: `önkényesen centralizálva a kiadási jogokat` (arbitrarily centralizing publishing rights), `a piaci és szakmai versenyt erőszakosan felszámolva` (violently abolishing market and professional competition), `pedagógiailag igénytelen módon homogenizálva a tananyagot` (homogenizing curriculum in a pedagogically shoddy manner).",
            "gr_text2": "Example: `A kormányzat a tankönyvpiacot erőszakosan államosítva és a választás szabadságát megszüntetve kötelező egyentankönyveket kényszerített az iskolákra`.",
            "gr_table": [
                ["A kiadást önkényesen centralizálva ellehetetlenítették a független műhelyeket.", "Arbitrarily centralizing publishing they made independent workshops impossible."],
                ["A tananyagot pedagógiailag igénytelen módon homogenizálva rontották az oktatás színvonalát.", "Homogenizing curriculum in a pedagogically shoddy manner they worsened educational standards."],
                ["A versenyt erőszakosan felszámolva hozták létre az állami tankönyvmonopóliumot.", "Abolishing competition aggressively they created the state textbook monopoly."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-02-tankonyv-monopolium-egyentankonyv",
                "title": "Az egyentankönyvek kora: A tankönyvpiac államosítása",
                "summary": "A kormányzat néhány év alatt teljesen felszámolta a szabad tankönyvválasztást és az önálló kiadókat. Létrehozta az állami tankönyvmonopóliumot, kötelező egyentankönyveket kényszerítve minden magyar iskolára.",
                "paragraphs": [
                    {"type": "narration", "text": "A magyar közoktatásban évtizedeken át magától értetődő alapelv volt, hogy a pedagógus szabadon választhatja meg, milyen tankönyvből tanítja diákjait. A kiadók közötti verseny folyamatos szakmai megújulást és magas színvonalat garantált."},
                    {"type": "dialogue", "speaker": "Független tankönyvszerző", "text": "A hatalom a tankönyvpiacot erőszakosan államosítva egyik napról a másikra tönkretette a nagy múltú szakmai műhelyeket. Önkényesen centralizálva a kiadást olyan egyentankönyveket kényszerítettek a tanárokra, amelyek hemzsegtek a tárgyi tévedésektől és a politikai elfogultságtól."},
                    {"type": "narration", "text": "Az állami könyvek nem a differenciált fejlesztést, hanem az egységes ideológiai igazodást szolgálták. A választási lehetőség hiánya közvetlen minőségromláshoz vezetett, ami a hátrányos helyzetű diákokat sújtotta leginkább."},
                    {"type": "narration", "text": "A pedagógusok kénytelenek voltak fénymásolt segédanyagokból, titokban tanítani a valódi irodalmat, bizonyítva, hogy a szellemi autonómiát még a legszigorúbb állami monopólium sem képes teljesen elfojtani."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen következményekkel járt a tankönyvpiac államosítása és az egyentankönyvek bevezetése?", [
                    "Megszűnt a tanárok szabad tankönyvválasztási joga, a független kiadók tönkrementek, és az oktatás minősége az ideológiailag vezérelt kötelező könyvek miatt drasztikusan leromlott.",
                    "Minden tankönyv ingyenessé és aranyozottá vált.",
                    "A diákoknak többé nem kellett házi feladatot írniuk."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A kiadást önkényesen _____ a kormányzat megszüntette a szakmai műhelyek sokszínűségét. (centralizing / centralizálva)", "centralizálva", "Centralizing publishing arbitrarily the government eliminated the diversity of professional workshops.", ["c1-adv-textbook-monopoly-critique"]),
                match("vocabulary", "controlled", [
                    ["tankönyv-monopólium", "a tankönyvkiadás kizárólagos állami ellenőrzése"],
                    ["egyentankönyv", "minden iskolára kötelezően ráerőltetett, egységesített tananyag"],
                    ["választási szabadság", "a pedagógus joga a legmegfelelőbb tankönyv kiválasztására"],
                    ["pedagógiai regresszió", "visszaesés a korszerű oktatási módszerekben az önkény miatt"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A tananyagot pedagógiailag igénytelen módon _____ súlyos minőségromlást idéztek elő. (homogenizing / homogenizálva)", "homogenizálva", "Homogenizing curriculum in a pedagogically shoddy manner they caused severe quality degradation.", ["c1-adv-textbook-monopoly-critique"]),
                sb("grammar", "practice", ["Az", "állam", "a", "tankönyvpiacot", "erőszakosan", "államosítva", "felszámolta", "a", "versenyt."], ["Az", "állam", "a", "tankönyvpiacot", "erőszakosan", "államosítva", "felszámolta", "a", "versenyt."], "Nationalizing the textbook market aggressively the state abolished competition.", ["c1-adv-textbook-monopoly-critique"]),
                dc("dialogue", [
                    {"speaker": "Gimnáziumi igazgató", "text": "Hogyan küzdenek a tanárok az egyentankönyvek szegényes színvonala ellen?"},
                    {"speaker": "Munkaközösség-vezető", "text": "Úgy, hogy a tananyagot önálló segédanyagokkal kiegészítve megőrzik a tanítás szakmai _____."},
                    {"speaker": "Gimnáziumi igazgató", "text": "A tanári kreativitást nem lehet államosítani."}
                ], ["méltóságát", "árát", "méretét"], 0, ["c1-adv-textbook-monopoly-critique"]),
                sw("production", [{"prompt": "Write a critical evaluation of the textbook monopoly using an evaluative adverbial.", "answer": "A tankönyvpiacot önkényesen centralizálva és a kiadói versenyt erőszakosan felszámolva a hatalom olyan egyentankönyveket kényszerített az iskolákra, amelyek mély pedagógiai regresszióhoz és az oktatás színvonalának romlásához vezettek."}], ["c1-adv-textbook-monopoly-critique"]),
                mc("grammar", "check", "Melyik szerkezet leplezi le a tankönyv-monopólium romboló hatását a leghitelesebben?", [
                    "a kiadást önkényesen centralizálva / pedagógiailag igénytelen módon homogenizálva a tananyagot",
                    "új nyomdagépeket állítva a csarnokba",
                    "ha a könyvek szépen sorakoznak a polcon"
                ], 0, ["c1-adv-textbook-monopoly-critique"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Cultural Blacklists & Patronage under PIM",
            "grammar_title": "Deontic Modal Structures Formulating Writers Duty of Intellectual Dissent",
            "grammar_skill": "c1-modal-deontic-intellectual-dissent",
            "goals": [
                "I can analyze political control of cultural institutions, Petőfi Literary Museum (PIM) under Demeter Szilárd, and literary blacklists (*Petőfi Irodalmi Múzeum, Demeter Szilárd, feketelisták, klientúra-építés, forrásmegvonás*).",
                "I can deploy deontic modal structures formulating the moral duty of intellectual dissent (*a független írónak kötelessége elutasítani a lojalitásért cserébe osztogatott állami pénzeket, megalkuvást nem ismerve kell szembeszállni a cenzúrával, nem engedhető meg a kultúra pártpolitikai alávetése*).",
                "I can critique authoritarian patronage networks in contemporary Central European arts."
            ],
            "vocab": [
                {"lemma": "Petőfi Irodalmi Múzeum", "translation": "Petőfi Literary Museum (PIM)", "pos": "expression"},
                {"lemma": "kulturális feketelista", "translation": "cultural / literary blacklist", "pos": "expression"},
                {"lemma": "politikai kegyenc", "translation": "political favorite / client", "pos": "noun"},
                {"lemma": "forrásmegvonás", "translation": "withdrawal / withholding of state funds", "pos": "noun"},
                {"lemma": "szellemi ellenállás", "translation": "intellectual resistance / dissent", "pos": "expression"},
                {"lemma": "kultúrharc", "translation": "culture war (Kulturkampf)", "pos": "noun"},
                {"lemma": "független folyóirat", "translation": "independent literary journal", "pos": "expression"},
                {"lemma": "erkölcsi integritás", "translation": "moral integrity", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate the uncompromising duty of writers and intellectuals to reject authoritarian patronage: `a hiteles alkotónak kötelessége visszautasítani a politikai hűbérúri logikát` (it is the duty of the authentic creator to reject political feudal logic), `megalkuvást nem ismerve kell kiállni a megbélyegzett kollégák mellett` (one must stand up for stigmatized colleagues without compromise), `nem engedhető meg a művészeti folyóiratok pénzügyi kivéreztetése` (the financial bleeding dry of artistic journals cannot be permitted).",
            "gr_text2": "Example: `A szellemi élet képviselőinek alkotmányos és erkölcsi kötelessége volt nyíltan szembeszállni a PIM élére állított politikai komisszár kulturális tisztogatásaival`.",
            "gr_table": [
                ["Az írónak kötelessége hűnek maradnia művészi lelkiismeretéhez a pénzosztókkal szemben.", "It is the duty of the writer to remain true to artistic conscience against dispensers of money."],
                ["Elengedhetetlen a cenzúrával sújtott független folyóiratok szolidáris támogatása.", "Solidarity support for independent journals struck by censorship is indispensable."],
                ["A művésznek megalkuvást nem ismerve kell elutasítania a hatalmi megrendeléseket.", "The artist must reject power commissions without compromise."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-03-fekete-es-feher-listak",
                "title": "A kultúrharc komisszárjai: A PIM és a feketelisták",
                "summary": "Demeter Szilárd kinevezése a Petőfi Irodalmi Múzeum élére a magyar kultúrharc új, agresszív szakaszát nyitotta meg: százmilliárdos pénzek feletti teljhatalmat kapott, miközben nyíltan fenyegette a független szerzőket és folyóiratokat.",
                "paragraphs": [
                    {"type": "narration", "text": "2018 végén a kormányzat a Petőfi Irodalmi Múzeum (PIM) főigazgatói székébe ültette Demeter Szilárdot, aki nem tudományos eredményeivel, hanem harcos pártpolitikai lojalitásával érdemelte ki a posztot. Rövid időn belül a teljes magyar irodalmi és könnyűzenei támogatási rendszer teljhatalmú urává tették."},
                    {"type": "dialogue", "speaker": "Független író", "text": "A hatalom nyílt fekete- és fehérlistákat hozott létre: aki behódolt és dicsérte a rendszert, az milliós ösztöndíjakat és állami kitüntetéseket kapott, míg a kritikus szerzők folyóirataitól megvonták a működési forrásokat. Alkotói kötelességünk volt elutasítani ezt a megalázó klientúra-rendszert."},
                    {"type": "narration", "text": "Demeter hírhedt publicisztikáiban a független értelmiséget Soros-hadseregnek és gázkamrák lakóinak nevezte, ami példátlan nemzetközi botrányt váltott ki. Írók és költők tucatjai léptek ki a Magyar Írószövetségből, tiltakozva a szellemi mélypont ellen."},
                    {"type": "narration", "text": "A független irodalmi élet bebizonyította: a valódi tehetséget és erkölcsi tartást nem lehet állami milliárdokkal megvásárolni, a hatalmi kegyencek művei pedig nyom nélkül hullanak ki az emlékezetből."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működött a politikai kliensrendszer a Petőfi Irodalmi Múzeum központosítása után?", [
                    "A lojális szerzőknek milliárdos támogatásokat és ösztöndíjakat juttattak, miközben a független és kritikus alkotókat és folyóiratokat forrásmegvonással és feketelistákkal próbálták ellehetetleníteni.",
                    "Minden magyar írónak ingyenes nyomdát biztosítottak otthon.",
                    "Kizárólag verseket fogadtak el a múzeum kapujában."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A független alkotóknak morális _____ volt visszautasítani a lojalitáshoz kötött támogatásokat. (duty / kötelességük)", "kötelességük", "It was the moral duty of independent creators to reject grants tied to loyalty.", ["c1-modal-deontic-intellectual-dissent"]),
                match("vocabulary", "controlled", [
                    ["Petőfi Irodalmi Múzeum", "a központosított állami kulturális forrásosztás intézménye"],
                    ["kulturális feketelista", "a kritikus művészek kirekesztése az állami támogatásokból"],
                    ["politikai kegyenc", "a tehetség helyett hűsége miatt jutalmazott alkotó"],
                    ["szellemi ellenállás", "az alkotói függetlenség és erkölcsi méltóság bátor védelme"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ a kulturális önkénnyel szemben. (resist / szembeszállni)", "szembeszállni", "Without compromise one must resist cultural autocracy.", ["c1-modal-deontic-intellectual-dissent"]),
                sb("grammar", "practice", ["Az", "íróknak", "kötelességük", "megőrizni", "a", "művészi", "függetlenség", "tisztaságát."], ["Az", "íróknak", "kötelességük", "megőrizni", "a", "művészi", "függetlenség", "tisztaságát."], "It is the duty of writers to preserve the purity of artistic independence.", ["c1-modal-deontic-intellectual-dissent"]),
                dc("dialogue", [
                    {"speaker": "Költő", "text": "Hogyan maradhat tiszta egy művész az állami kultúrharc közepette?"},
                    {"speaker": "Szerkesztő", "text": "Úgy, hogy erkölcsi kötelességünk elutasítani a klientúra-építést és szolidárisnak lenni a _____ kollégákkal."},
                    {"speaker": "Költő", "text": "A szolidaritás a túlélésünk egyetlen záloga."}
                ], ["meghurcolt", "gazdag", "boldog"], 0, ["c1-modal-deontic-intellectual-dissent"]),
                sw("production", [{"prompt": "Write a defense of artistic independence using a deontic modal structure.", "answer": "Az autentikus alkotóknak erkölcsi kötelességük szembeszállni a politikai kegyencrendszerrel, és megalkuvást nem ismerve kell védeniük a szellemi autonómiát a hatalom kulturális feketelistáival szemben."}], ["c1-modal-deontic-intellectual-dissent"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fogalmazza meg az írói szembeszegülést a legvilágosabban?", [
                    "kötelessége elutasítani a politikai függőséget / megalkuvást nem ismerve kell kiállni az autonómia mellett",
                    "érdemes elmenni egy díjátadóra ha meghívnak",
                    "a költőknek néha kellene találkozniuk a téren"
                ], 0, ["c1-modal-deontic-intellectual-dissent"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Resistance of the Independent Literary Sphere",
            "grammar_title": "Proportional Correlative Structures Mapping Political Patronage Against Cultural Polarization",
            "grammar_skill": "c1-adv-proportional-cultural-patronage-polarization",
            "goals": [
                "I can analyze the collective resistance of independent literary organizations (*Szépírók Társasága, Független Mentorhálózat, alternatív ösztöndíjak, független könyvkiadók szövetsége*).",
                "I can construct proportional correlative structures mapping state pressure to civic solidarity (*minél agresszívabban próbálja a hatalom kisajátítani a kultúrát, annál erősebbé válik a független alkotók szolidaritása*).",
                "I can evaluate grassroots civil patronage models sustaining uncensored literature."
            ],
            "vocab": [
                {"lemma": "Szépírók Társasága", "translation": "Society of Hungarian Authors (independent writers' union)", "pos": "expression"},
                {"lemma": "független könyvkiadás", "translation": "independent book publishing", "pos": "expression"},
                {"lemma": "közösségi finanszírozás", "translation": "crowdfunding / civic micro-donations", "pos": "expression"},
                {"lemma": "alternatív ösztöndíj", "translation": "alternative civic scholarship / grant", "pos": "expression"},
                {"lemma": "kulturális polarizáció", "translation": "cultural polarization", "pos": "expression"},
                {"lemma": "szolidaritási háló", "translation": "network of civic solidarity", "pos": "expression"},
                {"lemma": "cenzúramentes nyilvánosság", "translation": "censorship-free public sphere", "pos": "expression"},
                {"lemma": "szellemi szuverenitás", "translation": "intellectual sovereignty", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures chart the dynamic between authoritarian overreach and civil counter-organization: `minél gátlástalanabbul osztogat a rezsim forrásokat a lojális klientúrának, annál elmélyültebbé válik a kulturális polarizáció` (the more uninhibitedly the regime dispenses funds to the loyal clientele, the deeper cultural polarization becomes), `amilyen mértékben szorítják ki a független hangokat a hivatalos kánonból, olyan mértékben erősödik az alternatív nyilvánosság` (to the extent independent voices are squeezed out of the official canon, to that extent the alternative public sphere strengthens).",
            "gr_text2": "Example: `Minél durvábban próbálja a hatalom politikai pórázra fogni az irodalmat, annál szilárdabb szolidaritási hálózatokat hoz létre a független civil társadalom`.",
            "gr_table": [
                ["Minél agresszívabb a hatalmi kultúrharc, annál szorosabb a független írók összefogása.", "The more aggressive the power culture war, the tighter the solidarity of independent writers."],
                ["Amilyen mértékben vonják meg a pénzeket, olyan mértékben fordulnak a lapok a közösségi támogatáshoz.", "To the extent funds are withheld, to that extent journals turn to community crowdfunding."],
                ["Minél inkább erőltetik az egyenirányítást, annál inkább kivirágzik a szamizdat szellem.", "The more uniform direction is forced, the more the samizdat spirit blossoms."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-04-magyar-irodalmi-ellenallas",
                "title": "A szolidaritás hálói: A Szépírók Társasága és a civil mecenatúra",
                "summary": "A politikai tisztogatásokra a független magyar irodalom nem meghátrálással, hanem önszerveződéssel válaszolt. A Szépírók Társasága alternatív díjakat és közösségi ösztöndíjakat indított, megőrizve a szellemi szuverenitást.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az állami kultúrpolitika a kizárólagos hűségre épülő klientúra-rendszerré silányult, a magyar írótársadalom független része felismerte: a túlélés záloga az autonóm önszerveződés és a civil szolidaritás."},
                    {"type": "dialogue", "speaker": "Szépírók Társasága elnöke", "text": "Minél agresszívabban próbálta meg a hatalom megbélyegezni a szabad gondolatot, annál erősebbé vált a közösségünk összetartása. Létrehoztuk a Szépírók Díját és a Független Mentorhálózatot, hogy a fiatal tehetségek ne kényszerüljenek megalázó politikai kompromisszumokra."},
                    {"type": "narration", "text": "A független irodalmi lapok és könyvkiadók – mint a Jelenkor, a Kalligram vagy a Magvető körei – a közösségi finanszírozás felé fordultak. Olvasók ezrei adakoztak havonta mikroadományokkal, bebizonyítva, hogy a magyar társadalom igényli a minőségi, cenzúramentes irodalmat."},
                    {"type": "narration", "text": "Ez az ellenállás világossá tette: a diktatúrák elmúlnak, a politikai kegyencek elfelejtődnek, de a szolidaritásból és tehetségből született művek túlélik az elnyomás korszakát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan védte meg a Szépírók Társasága és a független szféra az irodalmi autonómiát?", [
                    "Alternatív közösségi ösztöndíjakat, független díjakat és olvasói mikrofinanszírozási hálózatokat hozott létre, függetlenítve az alkotókat az állami önkénytől.",
                    "Elfogadta a politikai iránymutatást és belépett a kormánypártba.",
                    "Bezárta az összes könyvesboltot az országban."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Minél durvább a forrásmegvonás, _____ elszántabbá válik az olvasói közösségi szolidaritás. (the / annál)", "annál", "The harsher the funding cuts, the more determined reader community solidarity becomes.", ["c1-adv-proportional-cultural-patronage-polarization"]),
                match("vocabulary", "controlled", [
                    ["Szépírók Társasága", "a demokratikus és autonóm magyar alkotók szakmai egyesülete"],
                    ["közösségi finanszírozás", "az olvasók közvetlen anyagi támogatása a lapok fenntartására"],
                    ["szolidaritási háló", "a megbélyegzett művészeket segítő civil összefogás"],
                    ["szellemi szuverenitás", "a hatalomtól és cenzúrától független szabad alkotókedv"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben szorítják vissza a független kultúrát, _____ mértékben növekszik a civil támogatás. (such / olyan)", "olyan", "To such an extent as independent culture is suppressed, to that extent civil support grows.", ["c1-adv-proportional-cultural-patronage-polarization"]),
                sb("grammar", "practice", ["Minél", "nagyobb", "a", "nyomás,", "annál", "erősebb", "a", "szakmai", "szolidaritás."], ["Minél", "nagyobb", "a", "nyomás,", "annál", "erősebb", "a", "szakmai", "szolidaritás."], "The greater the pressure, the stronger the professional solidarity.", ["c1-adv-proportional-cultural-patronage-polarization"]),
                dc("dialogue", [
                    {"speaker": "Kiadóvezető", "text": "Hogyan élheti túl a független könyvkiadás a politikai ellenszelet?"},
                    {"speaker": "Szerkesztő", "text": "Úgy, hogy minél agresszívabb a hatalom, annál hűségesebben állnak ki az olvasók a minőségi _____ mellett."},
                    {"speaker": "Kiadóvezető", "text": "A polgári öntudat a legfőbb támaszunk."}
                ], ["irodalom", "nyomda", "papír"], 0, ["c1-adv-proportional-cultural-patronage-polarization"]),
                sw("production", [{"prompt": "Write a proportional sentence linking political pressure to civil solidarity.", "answer": "Minél kíméletlenebbül próbálja a hatalom politikai klientúrává zülleszteni az irodalmat, annál szilárdabb szolidaritási hálózatot és alternatív nyilvánosságot épít ki a független civil társadalom az alkotói szabadság védelmében."}], ["c1-adv-proportional-cultural-patronage-polarization"]),
                mc("grammar", "check", "Melyik páros szerkezet fejezi ki a politikai nyomás és az ellenállás arányát a leghitelesebben?", [
                    "minél gátlástalanabb a politikai térfoglalás, annál erősebbé válik a szolidaritás",
                    "amikor a nyomda készen van a könyvekkel, kiteszik a kirakatba",
                    "bár süt a nap, az író mégis a szobájában dolgozik"
                ], 0, ["c1-adv-proportional-cultural-patronage-polarization"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "A Pluralistic Canon & The Horizon of Free Literature",
            "grammar_title": "Evaluative Conclusive Particles Declaring Irrepressible Pluralism of Autonomous Literature",
            "grammar_skill": "c1-adv-conclusive-canon-pluralism",
            "goals": [
                "I can analyze the irrepressible pluralism of autonomous Hungarian literature and the collapse of artificial ideological canons (*kánonpluralizmus, művészi szuverenitás, az esztétikai minőség elsőbbsége, a hatalmi kánon mulandósága*).",
                "I can deploy conclusive evaluative particles articulating the triumph of open literature (*értelemszerűen kikerülhetetlen, fundamentálisan megdönthetetlen, kétséget kizáróan bizonyított, végső soron elidegeníthetetlen*).",
                "I can synthesize the ongoing struggle for intellectual freedom in democratic Hungary."
            ],
            "vocab": [
                {"lemma": "kánonpluralizmus", "translation": "pluralism of literary canons", "pos": "noun"},
                {"lemma": "művészi szuverenitás", "translation": "artistic sovereignty", "pos": "expression"},
                {"lemma": "esztétikai minőség", "translation": "aesthetic quality / excellence", "pos": "expression"},
                {"lemma": "hatalmi kánon", "translation": "state-enforced authoritarian canon", "pos": "expression"},
                {"lemma": "szabad nyilvánosság", "translation": "free public sphere", "pos": "expression"},
                {"lemma": "szellemi sokszínűség", "translation": "intellectual diversity", "pos": "expression"},
                {"lemma": "maradandó érték", "translation": "enduring / lasting aesthetic value", "pos": "expression"},
                {"lemma": "jövő horizontja", "translation": "horizon of the future", "pos": "expression"}
            ],
            "gr_text1": "Conclusive evaluative particles assert the ultimate victory of artistic autonomy over temporary political tyranny: `értelemszerűen kikerülhetetlen a kánonok szabad sokszínűsége` (the free diversity of canons is naturally inescapable), `fundamentálisan megdönthetetlen az esztétikai minőség primátusa` (the primacy of aesthetic quality is fundamentally unshakeable), `végső soron elidegeníthetetlen az olvasó joga a cenzúrázatlan kultúrához` (ultimately the reader's right to uncensored culture is inalienable).",
            "gr_text2": "Example: `A történelem tanúsága szerint a politikai kánonok mulandóak, s végső soron elidegeníthetetlen és fundamentálisan megdönthetetlen az autonóm irodalom győzelme az ideológiai erőszak felett`.",
            "gr_table": [
                ["A művészi sokszínűség értelemszerűen kikerülhetetlen egy modern társadalomban.", "Artistic diversity is naturally inescapable in a modern society."],
                ["Az esztétikai autonómia fundamentálisan megdönthetetlen alapérték.", "Aesthetic autonomy is a fundamentally unshakeable core value."],
                ["Végső soron elidegeníthetetlen a nemzet joga a szabad irodalomhoz.", "Ultimately the nation's right to free literature is inalienable."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-05-szabad-irodalmi-kanon-jovo",
                "title": "A szellem győzelme: A szabad irodalom horizontja",
                "summary": "A magyar irodalom története bizonyítja, hogy sem a Rákosi-kor, sem a Kádár-rendszer, sem a modern illiberális kultúrharc nem tudta megtörni a valódi művészetet. A jövő az autonóm, sokszínű és európai kánoné.",
                "paragraphs": [
                    {"type": "narration", "text": "Bármilyen erőszakos eszközökkel próbálta is a mindenkori politikai hatalom saját ideológiájára formálni a kultúrát, a történelem ítélőszéke előtt az adminisztratív kánonok rendre elbuktak. A parancsra írt lojális művek elenyésztek, míg a független szellem remekművei a nemzet örök kincsévé váltak."},
                    {"type": "dialogue", "speaker": "Irodalomtudós", "text": "Fundamentálisan megdönthetetlen tétel, hogy az irodalmat nem a minisztériumok, hanem az olvasók és a művészi minőség teszi naggyá. Értelemszerűen kikerülhetetlen a sokszínűség: a magyar irodalom csak akkor virágozhat, ha minden hang szabadon megszólalhat benne."},
                    {"type": "narration", "text": "Babits Mihály, Pilinszky János, Kertész Imre, Esterházy Péter és Nádas Péter szellemi öröksége elpusztíthatatlan. Ők mutatták meg, hogy a magyar nyelv legmélyebb hivatása az emberi szabadság, a méltóság és az egyetemes európai humánum szolgálata."},
                    {"type": "narration", "text": "A jövő magyar irodalma nyitott, bátor és sokszínű marad. A kultúrharcok pora elül, de a szabad szó és az autonóm szellem fáklyája tovább világít a jövő nemzedékeinek."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért bukik el szükségszerűen minden erőszakos, politikai célú kánonátszabás a történelemben?", [
                    "Mert az irodalmi értéket nem a hatalmi rendeletek vagy a pénz, hanem az esztétikai minőség és a szabad olvasói közösség teremti meg, így a politikai kegyencek gyorsan feledésbe merülnek.",
                    "Mert a politikusok nem értenek a versek nyomtatásához.",
                    "Mert a könyvtárak nem engedik be az új könyveket."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A kultúra szellemi sokszínűsége értelemszerűen _____ egy szabad társadalomban. (inescapable / kikerülhetetlen)", "kikerülhetetlen", "The intellectual diversity of culture is naturally inescapable in a free society.", ["c1-adv-conclusive-canon-pluralism"]),
                match("vocabulary", "controlled", [
                    ["kánonpluralizmus", "a különböző esztétikai értékek békés és szabad együttélése"],
                    ["művészi szuverenitás", "a szerző függetlensége minden külső ideológiai elvárástól"],
                    ["esztétikai minőség", "a művészi formanyelv és gondolati mélység valódi rangja"],
                    ["maradandó érték", "az idő próbáját kiálló, korszakokon átívelő remekmű"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Az esztétikai autonómia elsőbbsége fundamentálisan _____ alapigazság. (unshakeable / megdönthetetlen)", "megdönthetetlen", "The primacy of aesthetic autonomy is a fundamentally unshakeable basic truth.", ["c1-adv-conclusive-canon-pluralism"]),
                sb("grammar", "practice", ["A", "kánonok", "sokszínűsége", "értelemszerűen", "kikerülhetetlen", "a", "demokratikus", "kultúrában."], ["A", "kánonok", "sokszínűsége", "értelemszerűen", "kikerülhetetlen", "a", "demokratikus", "kultúrában."], "The diversity of canons is naturally inescapable in democratic culture.", ["c1-adv-conclusive-canon-pluralism"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Hogyan foglalható össze a modern irodalmi küzdelmek végső tanulsága?"},
                    {"speaker": "Író", "text": "Úgy, hogy végső soron elidegeníthetetlen a társadalom joga a szabad és pluralista _____."},
                    {"speaker": "Kritikus", "text": "A hatalom mulandó, a művészet örök."}
                ], ["kultúrához", "épülethez", "autóhoz"], 0, ["c1-adv-conclusive-canon-pluralism"]),
                sw("production", [{"prompt": "Write a conclusive synthesis on the victory of literary pluralism using an evaluative particle.", "answer": "Az irodalmi kánon pluralizmusa és a művészi szuverenitás értelemszerűen kikerülhetetlen és fundamentálisan megdönthetetlen, hiszen a hatalmi kegyencek elfelejtődnek, de a szellemi szabadság remekművei örökre fennmaradnak."}], ["c1-adv-conclusive-canon-pluralism"]),
                mc("grammar", "check", "Melyik konkluzív kifejezés szintetizálja a szabad irodalom jövőjét a legerőteljesebben?", [
                    "értelemszerűen kikerülhetetlen / fundamentálisan megdönthetetlen / végső soron elidegeníthetetlen",
                    "reméljük a könyvek nem lesznek túl drágák holnap",
                    "jó lenne ha mindenki sokat olvasna hétvégén"
                ], 0, ["c1-adv-conclusive-canon-pluralism"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(33, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-kanonhaboru-irodalmi-szabadsag.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A kánonháború és a szabad magyar irodalom horizontja",
            "level": "C1",
            "lesson": 5,
            "order": 33,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-canon-pluralism"],
            "summary": "Átfogó krónika a 2010 utáni magyar irodalmi és oktatási kultúrharcról: a 2020-as Nemzeti Alaptanterv ideológiai kánonátszabásáról, az állami tankönyvmonopóliumról, a Petőfi Irodalmi Múzeum (PIM) alatti feketelistákról és klientúráról, a független írói szféra és a Szépírók Társasága szolidáris ellenállásáról, valamint a szabad, pluralista kultúra győzelméről.",
            "vocabularyTopics": [
                "The Battle for the Literary Canon: NAT, Textbooks & Blacklists",
                "A Pluralistic Canon & The Horizon of Free Literature"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A 2010 utáni évtizedben a magyar irodalom és közoktatás a tekintélyelvű államhatalom egyik legfőbb ideológiai csataterévé vált. A kétharmados törvényhozás és az állami kultúrpolitika célja a független szellemi műhelyek felszámolása és egy felülről vezérelt, nacionalista kánon megteremtése volt."},
                {"type": "narration", "text": "E törekvés csúcspontját a 2020-as Nemzeti Alaptanterv (NAT) és a tankönyvpiac erőszakos államosítása jelentette. A kormányzat kötelezővé tette a szélsőjobboldali, antiszemita nézeteket valló Wass Albertet és Nyirő Józsefet, miközben elsorvasztotta a tanári választási szabadságot, és egyentankönyveket kényszerített minden iskolára."},
                {"type": "narration", "text": "Ezzel párhuzamosan a Petőfi Irodalmi Múzeum (PIM) élére állított politikai komisszárok hatalmas állami forrásokat mozgósítva klientúra-rendszert építettek ki. A lojális szerzőket milliárdokkal jutalmazták, miközben a független irodalmi folyóiratokat forrásmegvonással és feketelistákkal próbálták elhallgattatni."},
                {"type": "narration", "text": "A magyar irodalmi élet azonban példátlan szolidaritással válaszolt az elnyomásra. A Szépírók Társasága, a független kiadók és az olvasók összefogásával közösségi finanszírozású ösztöndíjak és alternatív fórumok jöttek létre, biztosítva a cenzúramentes nyilvánosság túlélését."},
                {"type": "narration", "text": "A küzdelem végső tanulsága fundamentálisan megdönthetetlen: a hatalmi kánonok és a politikai kegyencek múlandóak, de a tehetség, az esztétikai minőség és a szabad szó autonómiája az egyetemes európai kultúra örök fundamentuma marad."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        33,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can master the critical discourse of curriculum indoctrination, state textbook monopoly, and cultural patronage.",
            "I can employ discourse framing markers of pedagogical capture, critical evaluative adverbials, and deontic modal structures of dissent.",
            "I can construct proportional correlative structures and conclusive evaluative syntheses on literary pluralism."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés diagnosztizálja a tantervi indoktrinációt a legpontosabban?", [
                "az állami indoktrináció szisztematikus kísérleteként értékelve / a kánon átideologizálásaként aposztrofálva",
                "hogyha a tanárok új krétát kapnak a táblához",
                "amikor a diákok elmennek színházba este"
            ], 0, ["c1-discourse-canon-indoctrination-framing"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhető le az állami tankönyvmonopólium a leghitelesebben?", [
                "a kiadást önkényesen centralizálva és a tananyagot pedagógiailag igénytelen módon homogenizálva",
                "egy szép könyvet ajándékozva az osztályfőnöknek",
                "amikor új asztalokat visznek az osztályterembe"
            ], 0, ["c1-adv-textbook-monopoly-critique"]),
            match("vocabulary", "recognize", [
                ["Nemzeti Alaptanterv", "az állami ideológiát ráerőltető kötelező tantervi szabályozás"],
                ["tankönyv-monopólium", "a tankönyvkiadás kizárólagos államosítása a választás elfojtásával"],
                ["Szépírók Társasága", "a független és autonóm magyar alkotók szolidaritási szervezete"],
                ["kánonpluralizmus", "a szabad és sokszínű irodalmi értékek megdönthetetlen elve"]
            ], [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A független lapok fenntartásához elengedhetetlenné vált az olvasói _____ . (crowdfunding / közösségi finanszírozás)", "közösségi finanszírozás", "For maintaining independent journals reader crowdfunding became indispensable.", [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "Az autonóm irodalom lényege a korlátozhatatlan művészi _____ . (sovereignty / szuverenitás)", "szuverenitás", "The essence of autonomous literature is unlimitable artistic sovereignty.", [f"c1-{slug}-vocab"]),
            fb("grammar", "recall", "A tantervet politikai indoktrinációként _____ a szakma egységesen tiltakozott. (evaluating / értékelve)", "értékelve", "Evaluating the curriculum as political indoctrination the profession protested unitedly.", ["c1-discourse-canon-indoctrination-framing"]),
            fb("grammar", "context", "Minél agresszívabb a hatalmi kultúrharc, _____ szorosabb a független alkotók szolidaritása. (the / annál)", "annál", "The more aggressive the power culture war, the tighter the solidarity of independent creators.", ["c1-adv-proportional-cultural-patronage-polarization"]),
            fb("grammar", "context", "A kánonok sokszínűsége értelemszerűen _____ a szabad kultúrában. (inescapable / kikerülhetetlen)", "kikerülhetetlen", "The diversity of canons is naturally inescapable in free culture.", ["c1-adv-conclusive-canon-pluralism"]),
            mc("grammar", "context", "Mi az írók erkölcsi kötelessége a politikai klientúrával és a feketelistákkal szemben?", [
                "A művészi integritás megőrzése, a megalázó hatalmi megrendelések elutasítása és a szolidaritás a megbélyegzett kollégákkal.",
                "A kormánydöntések feltétel nélküli ünneplése a nyilvánosság előtt.",
                "A könyvek azonnali elégetése a téren."
            ], 0, ["c1-modal-deontic-intellectual-dissent"]),
            sb("grammar", "produce", ["A", "szabad", "irodalom", "értékei", "fundamentálisan", "megdönthetetlenek", "minden", "korban."], ["A", "szabad", "irodalom", "értékei", "fundamentálisan", "megdönthetetlenek", "minden", "korban."], "The values of free literature are fundamentally unshakeable in every era.", ["c1-adv-conclusive-canon-pluralism"]),
            sw("production", [{"prompt": "Write a critical evaluation of cultural polarization using a proportional correlative structure.", "answer": "Minél agresszívabban próbálja a hatalom politikai klientúrára cserélni a független alkotókat, annál mélyebbé válik a kulturális polarizáció és annál elszántabbá válik a civil társadalom szolidaritása a szabad irodalom mellett."}], ["c1-adv-proportional-cultural-patronage-polarization"]),
            sw("production", [{"prompt": "Synthesize the triumph of literary autonomy using an evaluative conclusive particle.", "answer": "A kánonok pluralizmusa és a szellemi szuverenitás értelemszerűen kikerülhetetlen és fundamentálisan megdönthetetlen, hiszen a politikai önkény múlandó, de a szabad kultúra és az esztétikai minőség remekművei örökké fennmaradnak."}], ["c1-adv-conclusive-canon-pluralism"])
        ]
    )

    print("=== Finished C1 Unit 33 ===")


if __name__ == "__main__":
    generate_unit_33()
