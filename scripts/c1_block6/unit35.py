#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 35 Generator:
  - Track 1 (Core): Unit 35 — "Information Theory, Digital Ethics & Algorithmic Society" (c1-35)
  - Track 2 (Discourse): Unit 35 — "The Pegasus Surveillance Scandal & State Cyber-Espionage" (c1-megfigyeles)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_35():
    print("=== Generating C1 Unit 35 ===")
    
    new_skills = {
        "c1-35-vocab": {"kind": "vocabulary"},
        "c1-megfigyeles-vocab": {"kind": "vocabulary"},
        "c1-adv-information-entropy-cybernetics": {"kind": "grammar"},
        "c1-participle-algorithmic-determinism": {"kind": "grammar"},
        "c1-modal-deontic-digital-privacy-ethics": {"kind": "grammar"},
        "c1-adv-comparative-cybernetic-cognition": {"kind": "grammar"},
        "c1-syntax-von-neumann-technological-synthesis": {"kind": "grammar"},
        "c1-discourse-cyber-surveillance-scandal-framing": {"kind": "grammar"},
        "c1-adv-unconstrained-wiretap-authorization-critique": {"kind": "grammar"},
        "c1-modal-deontic-journalistic-source-protection": {"kind": "grammar"},
        "c1-adv-proportional-cyber-secrecy-erosion": {"kind": "grammar"},
        "c1-adv-conclusive-digital-privacy-restitution": {"kind": "grammar"},
    }
    new_titles = {
        "c1-35-vocab": "reading",
        "c1-megfigyeles-vocab": "reading",
        "c1-adv-information-entropy-cybernetics": "evaluative adverbials formulating information entropy and algorithmic computational theory",
        "c1-participle-algorithmic-determinism": "participial clauses analyzing algorithmic determinism and digital surveillance apparatus",
        "c1-modal-deontic-digital-privacy-ethics": "deontic modal structures asserting digital privacy and technological ethics",
        "c1-adv-comparative-cybernetic-cognition": "scalar comparative adverbials comparing machine intelligence and human cognition",
        "c1-syntax-von-neumann-technological-synthesis": "evaluative correlative syntax structuring john von neumann technological vision",
        "c1-discourse-cyber-surveillance-scandal-framing": "discourse markers diagnosing illegal state cyber espionage and surveillance",
        "c1-adv-unconstrained-wiretap-authorization-critique": "critical evaluative adverbials exposing unconstrained ministerial wiretap authorization",
        "c1-modal-deontic-journalistic-source-protection": "deontic modal structures asserting journalistic duty of confidential source protection",
        "c1-adv-proportional-cyber-secrecy-erosion": "proportional correlative structures mapping national security classification against democratic oversight",
        "c1-adv-conclusive-digital-privacy-restitution": "evaluative conclusive particles asserting inalienability of digital constitutional privacy",
    }
    
    core_title = "Information Theory, Digital Ethics & Algorithmic Society"
    core_stems = [f"c1-35-0{i}" for i in range(1, 6)] + ["c1-35-consolidation"]
    disc_title = "The Pegasus Surveillance Scandal & State Cyber-Espionage"
    slug = "megfigyeles"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(35, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-35)
    # ----------------------------------------------------
    core_intro = [
        "The digital revolution and algorithmic society present unprecedented philosophical challenges concerning consciousness, information entropy, digital autonomy, and human dignity.",
        "In this unit, centered on John von Neumann's (Neumann János) pioneering work 'A számológép és az agy' (The Computer and the Brain, 1958) and his ethical warnings on technological progress, you will master the elevated academic register of cybernetics, algorithmic determinism, machine cognition, and digital ethics at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-35-01",
            "title": "Information Theory, Entropy & Cybernetics",
            "grammar_title": "Evaluative Adverbials Formulating Information Entropy and Algorithmic Computational Theory",
            "grammar_skill": "c1-adv-information-entropy-cybernetics",
            "goals": [
                "I can analyze information entropy, cybernetic feedback loops, and algorithmic complexity (*információelmélet, Shannon-entrópia, kibernetikai visszacsatolás, algoritmikus komplexitás*).",
                "I can deploy elevated evaluative adverbials formulating cybernetic computation (*kibernetikailag modellezve, információelméleti szempontból vizsgálva, algoritmikusan leképezve a valószínűségeket*).",
                "I can critique determinism in information systems and digital modeling."
            ],
            "vocab": [
                {"lemma": "információelmélet", "translation": "information theory", "pos": "noun"},
                {"lemma": "információs entrópia", "translation": "information entropy", "pos": "expression"},
                {"lemma": "kibernetikai visszacsatolás", "translation": "cybernetic feedback loop", "pos": "expression"},
                {"lemma": "algoritmikus komplexitás", "translation": "algorithmic complexity", "pos": "expression"},
                {"lemma": "valószínűségszámítás", "translation": "probability calculus", "pos": "noun"},
                {"lemma": "digitális jelfeldolgozás", "translation": "digital signal processing", "pos": "expression"},
                {"lemma": "zaj és redundancia", "translation": "noise and redundancy", "pos": "expression"},
                {"lemma": "rendszerelmélet", "translation": "systems theory", "pos": "noun"}
            ],
            "gr_text1": "Evaluative adverbials in cybernetics and computation formulate mathematical and systemic perspectives: `kibernetikailag modellezve` (modeled cybernetically), `információelméleti szempontból vizsgálva` (examined from an information theory perspective), `algoritmikusan leképezve a neurális folyamatokat` (algorithmically mapping neural processes), `az entrópia csökkentésének szigorú logikáját követve` (following the strict logic of entropy reduction).",
            "gr_text2": "Example: `A neurális hálózatokat kibernetikailag modellezve és információelméleti szempontból vizsgálva a gépi tanulás nem más, mint a statisztikai entrópia szisztematikus minimalizálása`.",
            "gr_table": [
                ["A rendszert kibernetikailag modellezve feltárulnak az önszabályozó mechanizmusok.", "Modeling the system cybernetically self-regulating mechanisms are revealed."],
                ["Az adatfolyamot információelméleti szempontból vizsgálva kiszűrhető a zaj.", "Examining data flow from an information theory perspective noise can be filtered."],
                ["Algoritmikusan leképezve a neuronok működését új számítási modellek születnek.", "Mapping the operation of neurons algorithmically new computational models are born."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az információs entrópia Shannon elméletében?", [
                    "Egy üzenet vagy rendszer bizonytalanságának és információtartalmának mértékét: minél nagyobb az entrópia, annál nagyobb a kiszámíthatatlanság.",
                    "A számítógépek túlmelegedésének fizikai hőfokát.",
                    "Az internetes kábelek hosszának összegét."
                ], 0, ["c1-35-vocab"]),
                fb("grammar", "controlled", "A biológiai folyamatokat kibernetikailag _____ világossá válik az idegrendszer kódolási mechanizmusa. (modeling / modellezve)", "modellezve", "Modeling biological processes cybernetically the nervous system's coding mechanism becomes clear.", ["c1-adv-information-entropy-cybernetics"]),
                match("vocabulary", "controlled", [
                    ["információs entrópia", "a rendszer bizonytalanságának és információtartalmának mértéke"],
                    ["kibernetikai visszacsatolás", "az önszabályozó rendszerek működését vezérlő hurok"],
                    ["algoritmikus komplexitás", "a számítási feladat megoldásához szükséges lépések száma"],
                    ["zaj és redundancia", "az átviteli csatorna hibái és a biztonsági jeltöbblet"]
                ], ["c1-35-vocab"]),
                fb("grammar", "practice", "Az adatokat információelméleti szempontból _____ új törvényszerűségek mutathatók ki. (examining / vizsgálva)", "vizsgálva", "Examining the data from an information theory perspective new regularities can be shown.", ["c1-adv-information-entropy-cybernetics"]),
                sb("grammar", "practice", ["A", "folyamatokat", "kibernetikailag", "modellezve", "minimalizálható", "az", "információs", "zaj."], ["A", "folyamatokat", "kibernetikailag", "modellezve", "minimalizálható", "az", "információs", "zaj."], "Modeling processes cybernetically information noise can be minimized.", ["c1-adv-information-entropy-cybernetics"]),
                dc("dialogue", [
                    {"speaker": "Adattudós", "text": "Hogyan képes a mesterséges intelligencia felismerni az emberi hangot?"},
                    {"speaker": "Kibernetikus", "text": "Úgy, hogy algoritmikusan leképezve a hanghullámokat csökkenti a rendszerben lévő _____."},
                    {"speaker": "Adattudós", "text": "Ez a valószínűségi modellezés diadala."}
                ], ["entrópiát", "időt", "pénzt"], 0, ["c1-adv-information-entropy-cybernetics"]),
                sw("production", [{"prompt": "Write a sentence analyzing digital systems using a cybernetic evaluative adverbial.", "answer": "Az emberi agy és a számítógépek működését kibernetikailag modellezve és információelméleti szempontból vizsgálva nyilvánvalóvá válik, hogy mindkét struktúra a valószínűségi statisztika és az entrópia törvényeit követi."}], ["c1-adv-information-entropy-cybernetics"]),
                mc("grammar", "check", "Melyik határozói kifejezés fogalmazza meg a digitális információelméletet a legszakszerűbben?", [
                    "kibernetikailag modellezve / információelméleti szempontból vizsgálva",
                    "nagyon gyorsan gépelve a billentyűzeten",
                    "amikor a képernyő fényesen világít este"
                ], 0, ["c1-adv-information-entropy-cybernetics"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-35-02",
            "title": "Algorithmic Determinism & Digital Surveillance",
            "grammar_title": "Participial Clauses Analyzing Algorithmic Determinism and Digital Surveillance Apparatus",
            "grammar_skill": "c1-participle-algorithmic-determinism",
            "goals": [
                "I can analyze algorithmic determinism, profiling, surveillance capitalism, and behavioral prediction (*algoritmikus determinizmus, digitális megfigyelés, profilozás, megfigyelési kapitalizmus, prediktív analitika*).",
                "I can construct participial clauses analyzing data extraction and behavioral control (*a felhasználói viselkedést szisztematikusan profilozva, az egyéni autonómiát algoritmikus kontroll alá vonva, a privátszférát kíméletlenül felszámolva*).",
                "I can critique Shoshana Zuboff's surveillance capitalism in sociotechnical context."
            ],
            "vocab": [
                {"lemma": "algoritmikus determinizmus", "translation": "algorithmic determinism", "pos": "expression"},
                {"lemma": "megfigyelési kapitalizmus", "translation": "surveillance capitalism (Zuboff concept)", "pos": "expression"},
                {"lemma": "felhasználói profilozás", "translation": "user profiling / behavioral tracking", "pos": "expression"},
                {"lemma": "prediktív analitika", "translation": "predictive analytics", "pos": "expression"},
                {"lemma": "digitális lábnyom", "translation": "digital footprint", "pos": "expression"},
                {"lemma": "viselkedési többlet", "translation": "behavioral surplus (data extraction)", "pos": "expression"},
                {"lemma": "adathalászat és kémkedés", "translation": "data mining and espionage", "pos": "expression"},
                {"lemma": "platform-monopólium", "translation": "platform monopoly", "pos": "expression"}
            ],
            "gr_text1": "Participial clauses in critical digital studies dissect how algorithms restrict human liberty: `a polgárok minden lépését láthatatlanul monitorozva` (invisibly monitoring every step of citizens), `a személyes adatokat viselkedési többletként kisajátítva` (appropriating personal data as behavioral surplus), `az emberi önrendelkezést prediktív buborékokba zárva` (confining human self-determination into predictive bubbles).",
            "gr_text2": "Example: `A technológiai óriáscégek a digitális lábnyomokat szisztematikusan profilozva és az egyént algoritmikus determinizmus alá vonva számolják fel a szabad akarat illúzióját`.",
            "gr_table": [
                ["A felhasználói adatokat gátlástalanul kinyerve a platformok manipulálják a közvéleményt.", "Extracting user data without scruples platforms manipulate public opinion."],
                ["Az egyéni döntéseket algoritmusok alá rendelve elvész a polgári autonómia.", "Subordinating individual decisions to algorithms civic autonomy is lost."],
                ["A magánszférát folyamatosan monitorozva épül ki a megfigyelő állam.", "Continuously monitoring privacy the surveillance state is constructed."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez Shoshana Zuboff 'megfigyelési kapitalizmusnak'?", [
                    "Azt a gazdasági rendszert, amely az emberi viselkedést és személyes tapasztalatot ingyenes nyersanyagként sajátítja ki, hogy viselkedési többletet állítson elő és prediktív algoritmusokkal manipulálja a döntéseinket.",
                    "A biztonsági kamerák gyártását a plázák számára.",
                    "Amikor a bankok kamatot számítanak fel a hitelkártyákra."
                ], 0, ["c1-35-vocab"]),
                fb("grammar", "controlled", "A digitális szokásokat szisztematikusan _____ a rendszerek előre látják a reakcióinkat. (profiling / profilozva)", "profilozva", "Systematically profiling digital habits systems foresee our reactions.", ["c1-participle-algorithmic-determinism"]),
                match("vocabulary", "controlled", [
                    ["algoritmikus determinizmus", "a szabad akarat felváltása a gépi döntéshozatal korlátaival"],
                    ["megfigyelési kapitalizmus", "az emberi adatok haszonszerzési célú totális kizsákmányolása"],
                    ["viselkedési többlet", "a működéshez nem szükséges, megfigyelésre használt adatfölösleg"],
                    ["prediktív analitika", "a jövőbeli emberi cselekvések valószínűségi kiszámítása"]
                ], ["c1-35-vocab"]),
                fb("grammar", "practice", "A magánszférát kíméletlenül _____ a digitális platformok aláássák a demokráciát. (eroding / felszámolva)", "felszámolva", "Ruthlessly eroding privacy digital platforms undermine democracy.", ["c1-participle-algorithmic-determinism"]),
                sb("grammar", "practice", ["A", "platformok", "az", "adatokat", "profilozva", "manipulálják", "a", "társadalmat."], ["A", "platformok", "az", "adatokat", "profilozva", "manipulálják", "a", "társadalmat."], "Profiling data platforms manipulate society.", ["c1-participle-algorithmic-determinism"]),
                dc("dialogue", [
                    {"speaker": "Szociológus", "text": "Hogyan hat a közösségi média az egyéni autonómiára?"},
                    {"speaker": "Médiaetikus", "text": "Úgy, hogy a felhasználói viselkedést szüntelenül monitorozva és prediktív buborékokba _____ megfosztja az embert a valódi választás szabadságától."},
                    {"speaker": "Szociológus", "text": "Ez a modern rabság legkifinomultabb formája."}
                ], ["zárva", "dobva", "kérve"], 0, ["c1-participle-algorithmic-determinism"]),
                sw("production", [{"prompt": "Write a critique of algorithmic determinism using a participial clause.", "answer": "A digitális óriásvállalatok a felhasználók minden rezdülését szisztematikusan profilozva és az egyéni autonómiát algoritmikus determinizmus alá hajtva olyan megfigyelési kapitalizmust hoztak létre, amely felszámolja a polgári szabadság alapjait."}], ["c1-participle-algorithmic-determinism"]),
                mc("grammar", "check", "Melyik szerkezet leplezi le az algoritmikus kontrollt a legpontosabban?", [
                    "a digitális lábnyomokat szisztematikusan profilozva és az autonómiát korlátozva",
                    "új fényképeket feltöltve a profiloldalra délután",
                    "ha valaki sokat nyomkodja a telefonját a vonaton"
                ], 0, ["c1-participle-algorithmic-determinism"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-35-03",
            "title": "Digital Privacy & Technological Ethics",
            "grammar_title": "Deontic Modal Structures Asserting Digital Privacy and Technological Ethics",
            "grammar_skill": "c1-modal-deontic-digital-privacy-ethics",
            "goals": [
                "I can analyze digital constitutionalism, cryptographic privacy, data sovereignty, and AI ethics (*digitális alkotmányosság, kriptográfiai védelem, adatszuverenitás, mesterséges intelligencia etikája*).",
                "I can deploy deontic modal structures asserting digital privacy and technological ethics (*a jogalkotónak kötelessége korlátoznia a digitális megfigyelést, megalkuvást nem ismerve kell védeni az egyén adatszuverenitását, nem engedhető meg az emberi méltóság algoritmusok általi lealacsonyítása*).",
                "I can debate the EU General Data Protection Regulation (GDPR) and the AI Act."
            ],
            "vocab": [
                {"lemma": "digitális alkotmányosság", "translation": "digital constitutionalism", "pos": "expression"},
                {"lemma": "adatszuverenitás", "translation": "data sovereignty", "pos": "noun"},
                {"lemma": "kriptográfiai védelem", "translation": "cryptographic protection / encryption", "pos": "expression"},
                {"lemma": "információs önrendelkezés", "translation": "informational self-determination", "pos": "expression"},
                {"lemma": "etikus mesterséges intelligencia", "translation": "ethical artificial intelligence", "pos": "expression"},
                {"lemma": "adatvédelmi garancia", "translation": "data protection guarantee", "pos": "expression"},
                {"lemma": "algoritmikus elszámoltathatóság", "translation": "algorithmic accountability", "pos": "expression"},
                {"lemma": "privátszféra szentsége", "translation": "sanctity of privacy", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate the uncompromising constitutional demand for digital privacy: `a demokratikus államnak kötelessége garantálnia az információs önrendelkezést` (it is the duty of the democratic state to guarantee informational self-determination), `megalkuvást nem ismerve kell védeni a polgárok titkosított kommunikációját` (citizens' encrypted communication must be defended without compromise), `nem engedhető meg az autonóm fegyverek és az átláthatatlan fekete doboz algoritmusok kontrollálatlan alkalmazása` (uncontrolled application of autonomous weapons and opaque black-box algorithms cannot be permitted).",
            "gr_text2": "Example: `A társadalomnak feltétlen kötelessége kordában tartania a technológiai hatalmat, hiszen a magánszféra védelme az emberi méltóság digitális kiterjesztése`.",
            "gr_table": [
                ["Az államnak kötelessége tiszteletben tartani a levelezés és a digitális adatok titkosságát.", "The state has a duty to respect the secrecy of correspondence and digital data."],
                ["Elengedhetetlen az algoritmikus rendszerek feletti szigorú emberi kontroll.", "Strict human oversight over algorithmic systems is indispensable."],
                ["Megalkuvást nem ismerve kell fellépni a tömeges lehallgatási kísérletekkel szemben.", "One must take action against mass wiretapping attempts without compromise."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi az 'információs önrendelkezési jog' lényege az alkotmányjogban?", [
                    "Minden ember elidegeníthetetlen joga arra, hogy maga döntsön személyes adatainak kiszolgáltatásáról, kezeléséről és felhasználásáról az állami és piaci szereplőkkel szemben.",
                    "A jog arra, hogy mindenki ingyen internetet kapjon a lakásában.",
                    "A közösségi médiás profilképek naponta történő cseréjének joga."
                ], 0, ["c1-35-vocab"]),
                fb("grammar", "controlled", "A jogállamnak alkotmányos _____ megvédeni a polgárok digitális magánszféráját. (duty / kötelessége)", "kötelessége", "It is the constitutional duty of the rule of law to protect citizens' digital privacy.", ["c1-modal-deontic-digital-privacy-ethics"]),
                match("vocabulary", "controlled", [
                    ["információs önrendelkezés", "a személyes adatok feletti kizárólagos rendelkezés joga"],
                    ["kriptográfiai védelem", "a kommunikáció titkosítása a lehallgatás ellen"],
                    ["algoritmikus elszámoltathatóság", "a gépi döntéshozatal átláthatósága és számonkérhetősége"],
                    ["digitális alkotmányosság", "az alapjogok érvényesítése a virtuális térben"]
                ], ["c1-35-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ az etikai normák érvényesülését a technológiában. (enforce / kikényszeríteni)", "kikényszeríteni", "Without compromise one must enforce ethical norms in technology.", ["c1-modal-deontic-digital-privacy-ethics"]),
                sb("grammar", "practice", ["A", "demokráciának", "kötelessége", "védeni", "a", "polgárok", "digitális", "szabadságát."], ["A", "demokráciának", "kötelessége", "védeni", "a", "polgárok", "digitális", "szabadságát."], "Democracy has a duty to defend citizens' digital freedom.", ["c1-modal-deontic-digital-privacy-ethics"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Hogyan korlátozható a mesterséges intelligencia túlhatalma?"},
                    {"speaker": "Informatikai etikus", "text": "Úgy, hogy kötelességünk szigorú törvényi korlátokat szabni, és nem engedhető meg a polgárok megfigyelése megfelelő bírói _____ nélkül."},
                    {"speaker": "Jogvédő", "text": "Az emberi méltóság a digitális korban is érinthetetlen."}
                ], ["kontroll", "szerződés", "számla"], 0, ["c1-modal-deontic-digital-privacy-ethics"]),
                sw("production", [{"prompt": "Write a sentence declaring the duty of digital privacy using a deontic modal.", "answer": "A modern jogállamnak alkotmányos kötelessége garantálni a polgárok információs önrendelkezését, és megalkuvást nem ismerve kell kikényszerítenie a technológiai cégektől és állami szervektől a privátszféra szentségének tiszteletben tartását."}], ["c1-modal-deontic-digital-privacy-ethics"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fogalmazza meg a digitális etika követelményét a leghatározottabban?", [
                    "kötelessége garantálni az önrendelkezést / megalkuvást nem ismerve kell védeni a magánszférát",
                    "jó lenne ha a cégek néha elolvasnák az adatvédelmi nyilatkozatot",
                    "a számítógépeket érdemes lekapcsolni este villanyoltás előtt"
                ], 0, ["c1-modal-deontic-digital-privacy-ethics"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-35-04",
            "title": "Machine Intelligence & Human Cognition",
            "grammar_title": "Scalar Comparative Adverbials Comparing Machine Intelligence and Human Cognition",
            "grammar_skill": "c1-adv-comparative-cybernetic-cognition",
            "goals": [
                "I can analyze the comparison between computer architectures and human neural cognition (*Neumann-architektúra, analóg vs. digitális agy, neurális hálózatok, gépi intelligencia korlátai*).",
                "I can deploy scalar comparative adverbials comparing biological cognition with computation (*sokkal rugalmasabban adaptálódva az ismeretlen környezethez, lényegesen mélyebb szemantikai értést felmutatva, felülmúlhatatlanul gazdagabb érzelmi intuícióval rendelkezve*).",
                "I can discuss John von Neumann's posthumous lectures in 'The Computer and the Brain'."
            ],
            "vocab": [
                {"lemma": "Neumann-architektúra", "translation": "Von Neumann computer architecture", "pos": "expression"},
                {"lemma": "analóg és digitális agy", "translation": "analog and digital brain", "pos": "expression"},
                {"lemma": "gépi tanulás", "translation": "machine learning", "pos": "expression"},
                {"lemma": "szemantikai megértés", "translation": "semantic understanding / intentionality", "pos": "expression"},
                {"lemma": "neurális plaszticitás", "translation": "neural plasticity", "pos": "expression"},
                {"lemma": "számítási kapacitás", "translation": "computational capacity", "pos": "expression"},
                {"lemma": "szintaktikai feldolgozás", "translation": "syntactic processing", "pos": "expression"},
                {"lemma": "emberi egyediség", "translation": "human uniqueness / consciousness", "pos": "expression"}
            ],
            "gr_text1": "Scalar comparative adverbials calibrate the qualitative differences between electronic computers and the human mind: `lényegesen alacsonyabb energiafogyasztással, mégis sokkal komplexebb asszociációkat képezve` (with substantially lower energy consumption, yet forming much more complex associations), `sokkal rugalmasabban alkalmazkodva az etikai dilemmákhoz, mint a merev algoritmusok` (adapting to ethical dilemmas much more flexibly than rigid algorithms), `felülmúlhatatlanul mélyebb szemantikai megértést tanúsítva` (demonstrating insurpassably deeper semantic understanding).",
            "gr_text2": "Example: `Neumann János kimutatta, hogy az emberi agy statisztikai és analóg jellege révén lényegesen hatékonyabban kezeli a bizonytalanságot, sokkal mélyebbre hatolva a valóság megértésében, mint a digitális gépek merev logikája`.",
            "gr_table": [
                ["Az emberi elme sokkal rugalmasabban reagál a váratlan helyzetekre, mint a számítógép.", "The human mind reacts much more flexibly to unexpected situations than the computer."],
                ["Az agy lényegesen kevesebb energiával végez komplex gondolati asszociációkat.", "The brain performs complex thought associations with substantially less energy."],
                ["A gép felülmúlhatatlanul gyorsabb a számolásban, de képtelen a morális mérlegelésre.", "The machine is insurpassably faster at computation, but incapable of moral balancing."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen alapvető különbséget tárt fel Neumann János a számítógép és az emberi agy működése között?", [
                    "A számítógép pontos digitális aritmetikát használ nagy sebességgel, míg az agy alacsony pontosságú, analóg és statisztikai jelzésekkel, párhuzamosan és elképesztő energiahatékonysággal gondolkodik.",
                    "A számítógépeknek nincs memóriájuk, míg az ember mindent megjegyez.",
                    "Nincs különbség, az emberi agy pontosan olyan, mint egy laptop."
                ], 0, ["c1-35-vocab"]),
                fb("grammar", "controlled", "Az agy sokkal rugalmasabban _____ a hibákhoz, mint a digitális áramkörök. (adapted / alkalmazkodott)", "alkalmazkodott", "The brain adapted much more flexibly to errors than digital circuits.", ["c1-adv-comparative-cybernetic-cognition"]),
                match("vocabulary", "controlled", [
                    ["Neumann-architektúra", "a tárolt programú digitális számítógép klasszikus felépítése"],
                    ["analóg és digitális agy", "Neumann összehasonlítása az idegrendszer és a gépek működéséről"],
                    ["szemantikai megértés", "a jelek mögötti valódi tartalom és jelentés felfogása"],
                    ["neurális plaszticitás", "az agysejtek képessége a tanulás útján való átrendeződésre"]
                ], ["c1-35-vocab"]),
                fb("grammar", "practice", "A mesterséges intelligencia lényegesen gyorsabban _____ adatokat, mint az ember. (processes / dolgoz fel)", "dolgoz fel", "Artificial intelligence processes data substantially faster than humans.", ["c1-adv-comparative-cybernetic-cognition"]),
                sb("grammar", "practice", ["Az", "emberi", "elme", "sokkal", "mélyebb", "szemantikai", "megértést", "tanúsít."], ["Az", "emberi", "elme", "sokkal", "mélyebb", "szemantikai", "megértést", "tanúsít."], "The human mind demonstrates much deeper semantic understanding.", ["c1-adv-comparative-cybernetic-cognition"]),
                dc("dialogue", [
                    {"speaker": "Kognitív kutató", "text": "Képes lesz-e a számítógép valaha valódi tudatra ébredni?"},
                    {"speaker": "Neumann-kutató", "text": "Neumann szerint a gép szintaktikailag dolgozza fel a jeleket, míg az ember felülmúlhatatlanul mélyebb morális és érzelmi _____ rendelkezik."},
                    {"speaker": "Kognitív kutató", "text": "Ezért az emberi felelősség nem ruházható át a gépekre."}
                ], ["tudással", "pénzzel", "idővel"], 0, ["c1-adv-comparative-cybernetic-cognition"]),
                sw("production", [{"prompt": "Write a comparative analysis of human vs. machine intelligence using a scalar comparative adverbial.", "answer": "Bár a modern szuperszámítógépek felülmúlhatatlanul gyorsabbak az adatok puszta kalkulációjában, az emberi elme a neurális plaszticitás révén sokkal rugalmasabban adaptálódik a komplex etikai helyzetekhez és lényegesen mélyebb szemantikai megértést tanúsít."}], ["c1-adv-comparative-cybernetic-cognition"]),
                mc("grammar", "check", "Melyik fokozó hasonlító határozói forma állítja szembe az elmét és a gépet a legpontosabban?", [
                    "sokkal rugalmasabban alkalmazkodva / lényegesen mélyebb szemantikai megértést tanúsítva",
                    "több áramot használva a szobában mint a lámpa",
                    "gyorsabban kattintva az egérrel a monitoron"
                ], 0, ["c1-adv-comparative-cybernetic-cognition"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-35-05",
            "title": "John von Neumann: Technological Vision & Ethical Limits",
            "grammar_title": "Evaluative Correlative Syntax Structuring John von Neumann Technological Vision",
            "grammar_skill": "c1-syntax-von-neumann-technological-synthesis",
            "goals": [
                "I can analyze John von Neumann's (Neumann János) technological vision, atomic game theory, and 'Can We Survive Technology?' manifesto (*Neumann János, A számológép és az agy, technológiai szingularitás, etikai korlátok*).",
                "I can construct evaluative correlative syntax structuring technological prognosis (*ahogyan a számítástechnika exponenciálisan kitágítja az emberi hatalom határait, úgy sokszorozódik meg a felelősségünk a technológia békés és etikus megőrzéséért*).",
                "I can synthesize the humanist responsibility of the scientist in the nuclear and digital age."
            ],
            "vocab": [
                {"lemma": "Neumann János", "translation": "John von Neumann (polymath and computer pioneer)", "pos": "noun"},
                {"lemma": "A számológép és az agy", "translation": "The Computer and the Brain (Neumann 1958)", "pos": "expression"},
                {"lemma": "technológiai szingularitás", "translation": "technological singularity", "pos": "expression"},
                {"lemma": "etikai korlátok", "translation": "ethical limits / boundaries", "pos": "expression"},
                {"lemma": "játékelmélet", "translation": "game theory (Von Neumann & Morgenstern)", "pos": "noun"},
                {"lemma": "exponenciális fejlődés", "translation": "exponential technological growth", "pos": "expression"},
                {"lemma": "emberi túlélés", "translation": "human survival (in the technological age)", "pos": "expression"},
                {"lemma": "felelősségvállalás", "translation": "assumption of moral responsibility", "pos": "noun"}
            ],
            "gr_text1": "Evaluative correlative syntax pairs scientific acceleration with moral vigilance: `ahogyan a technológiai fejlődés exponenciálisan növekszik, úgy válik mind sürgetőbbé az etikai korlátok meghúzása` (as technological progress grows exponentially, so drawing ethical boundaries becomes ever more urgent), `amennyire hatalmas erőt ad a számítógép a kezünkbe, annyira megkérdőjelezhetetlen a felelősségünk annak békés felhasználásáért` (as much as the computer puts immense power into our hands, so unquestionable is our responsibility for its peaceful use).",
            "gr_text2": "Example: `Ahogyan Neumann János megjósolta a számítási kapacitás robbanásszerű növekedését, úgy figyelmeztetett arra is, hogy a túlélés záloga az emberi erkölcs érettségében gyökerezik`.",
            "gr_table": [
                ["Ahogyan a gépek egyre okosabbá válnak, úgy kell az embernek mind bölcsebbé lennie.", "As machines become smarter, so must humanity become all the wiser."],
                ["Amennyire kitágul a digitális hatalom, annyira létfontosságú az etikai kontroll.", "As much as digital power expands, so vital is ethical control."],
                ["Ahogyan Neumann látta a jövőt, úgy nézünk ma szembe a mesterséges intelligenciával.", "As Neumann saw the future, so do we face artificial intelligence today."]
            ],
            "classic_story": {
                "slug": "neumann-szamologep-es-az-agy",
                "title": "Neumann János: A számológép és az agy – A technológia határai",
                "author": "Neumann János",
                "work": "A számológép és az agy (1958) / Túlélhetjük-e a technikát? (1955)",
                "summary": "Neumann János (1903–1957) magyar származású matematikus, fizikus, a modern számítógép-architektúra, a játékelmélet és a kvantummechanika matematikai alapjainak megteremtője, az egyetemes tudománytörténet egyik legnagyobb lángelméje. Élete utolsó művében, a halálos ágyán diktált 'A számológép és az agy' című könyvében a digitális számítógépek és az emberi idegrendszer működésének mély hasonlóságait és lényegi különbségeit vizsgálta. 'Túlélhetjük-e a technikát?' című prófétai esszéjében arra figyelmeztetett: a technológiai fejlődés sebessége hamarosan eléri azt a pontot, ahol az emberiség puszta túlélése kizárólag erkölcsi érettségén és a szabadság intézményes védelmén múlik.",
                "characters": ["Neumann János, a modern kor géniusza"],
                "paragraphs": [
                    {"type": "narration", "text": "A huszadik század közepén az emberiség olyan eszközök birtokába jutott, amelyek alapjaiban változtatták meg a történelem menetét: a maghasadás energiájához és az elektronikus számítási kapacitáshoz. E két forradalom középpontjában egyetlen zseniális elme állt: Neumann János."},
                    {"type": "dialogue", "speaker": "Neumann János", "text": "A technológiai fejlődés felgyorsulása olyan ponthoz közeledik, amely után az emberi létezés formái gyökeresen átalakulnak. Ahogyan a gépi számítás exponenciálisan kitágítja a lehetőségeinket, úgy kell felismernünk: a technika önmagában semleges, de a szabadság és az erkölcsi józanság nélkül a legpusztítóbb elnyomás eszközévé válhat."},
                    {"type": "narration", "text": "Neumann rámutatott, hogy a számítógép és az agy összehasonlítása nem technokrata gőg, hanem az emberi természet legmélyebb megértésének kísérlete. Az agy alacsony pontosságú, analóg és statisztikai nyelven beszél, mégis képes az önreflexióra, a szeretetre és az igazság keresésére – mindarra, amire a legbonyolultabb szilíciumáramkör sem lesz képes soha."},
                    {"type": "narration", "text": "Neumann János öröksége ma aktuálisabb, mint valaha. Megtanította a világnak, hogy a digitális jövőt nem a technológia vak imádatával, hanem szigorú intellektuális fegyelemmel, az emberi jogok feltétlen tiszteletével és a szabadság védelmével kell felépítenünk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen prófétai figyelmeztetést fogalmazott meg Neumann János 'Túlélhetjük-e a technikát?' című esszéjében?", [
                    "A technológiai fejlődés exponenciális sebessége hamarosan meghaladja a korábbi politikai intézmények kereteit, így a túlélés egyetlen záloga az emberiség morális érettsége és az együttműködés lesz.",
                    "Azt, hogy 2000-re minden számítógépet le kell kapcsolni.",
                    "Hogy a tudósoknak nem szabad matematikai cikkeket írniuk."
                ], 0, ["c1-35-vocab"]),
                fb("grammar", "controlled", "Ahogyan növekszik a mesterséges intelligencia ereje, _____ válik fontosabbá a humánus etika. (so / úgy)", "úgy", "As the power of artificial intelligence grows, so does humane ethics become more important.", ["c1-syntax-von-neumann-technological-synthesis"]),
                match("vocabulary", "controlled", [
                    ["Neumann János", "a digitális számítógép és a modern játékelmélet atyja"],
                    ["technológiai szingularitás", "a technikai fejlődés visszafordíthatatlan, robbanásszerű pontja"],
                    ["A számológép és az agy", "Neumann utolsó műve az elme és a számítógép párhuzamairól"],
                    ["emberi túlélés", "a civilizáció megmaradásának erkölcsi imperatívusza"]
                ], [f"c1-35-vocab"]),
                fb("grammar", "practice", "Amennyire kitágul a gépi kapacitás, _____ elengedhetetlen a humánus kontroll. (as much / annyira)", "annyira", "As much as machine capacity expands, so much is humane control indispensable.", ["c1-syntax-von-neumann-technological-synthesis"]),
                sb("grammar", "practice", ["Ahogyan", "fejlődik", "a", "technika,", "úgy", "sokszorozódik", "meg", "az", "emberi", "felelősség."], ["Ahogyan", "fejlődik", "a", "technika,", "úgy", "sokszorozódik", "meg", "az", "emberi", "felelősség."], "As technology develops, so human responsibility multiplies.", ["c1-syntax-von-neumann-technological-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Kiberfilozófus", "text": "Hogyan értékelhető Neumann technológiai hagyatéka ma?"},
                    {"speaker": "Professzor", "text": "Úgy, hogy ahogyan ő előre látta a gépek hatalmát, úgy kell ma is védenünk az emberi méltóság etikai _____."},
                    {"speaker": "Kiberfilozófus", "text": "A technika az embert szolgálja, nem az ember a technikát."}
                ], ["korlátait", "árait", "adatait"], 0, ["c1-syntax-von-neumann-technological-synthesis"]),
                sw("production", [{"prompt": "Write an evaluative synthesis of technological progress using correlative syntax.", "answer": "Ahogyan a digitális számítástechnika és a mesterséges intelligencia exponenciálisan kitágítja az emberi hatalom határait, úgy sokszorozódik meg a civilizáció felelőssége azért, hogy az innováció az egyetemes humánumot és ne a pusztítást szolgálja."}], ["c1-syntax-von-neumann-technological-synthesis"]),
                mc("grammar", "check", "Melyik páros szerkezet fogalmazza meg a technológiai felelősséget a legpontosabban?", [
                    "ahogyan növekszik a számítási kapacitás, úgy válik mind sürgetőbbé az etikai korlátok megvonása",
                    "amikor új telefont veszünk a boltban, örülünk a jó kamerának",
                    "ha sok gép van a szobában, meleg lesz a levegő"
                ], 0, ["c1-syntax-von-neumann-technological-synthesis"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(35, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        35,
        "core",
        "c1-35-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of information theory, cybernetics, algorithmic determinism, and digital ethics.",
            "I can employ cybernetic evaluative adverbials, participial profiling clauses, and deontic modal structures of digital privacy.",
            "I can synthesize John von Neumann's technological vision and compare machine computation with human cognition."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés elemzi a kiberrendszerek belső logikáját a legszakszerűbben?", [
                "kibernetikailag modellezve / információelméleti szempontból vizsgálva",
                "hogyha valaki jól ért a számítógépes játékokhoz",
                "amikor új szoftvert töltenek le az internetről"
            ], 0, ["c1-adv-information-entropy-cybernetics"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhető le az algoritmikus determinizmus a leghitelesebben?", [
                "a felhasználói szokásokat szisztematikusan profilozva és az autonómiát korlátozva",
                "amikor sok reklám jelenik meg az oldalon",
                "ha a gép hamar lemerül és tölteni kell"
            ], 0, ["c1-participle-algorithmic-determinism"]),
            match("vocabulary", "recognize", [
                ["információs entrópia", "a rendszerben rejlő bizonytalanság és információtartalom mértéke"],
                ["megfigyelési kapitalizmus", "a személyes viselkedési adatok profitcélú totális kisajátítása"],
                ["információs önrendelkezés", "a személyes adatok feletti kizárólagos egyéni rendelkezési jog"],
                ["Neumann János", "a modern számítógép-architektúra és kiber-etika megteremtője"]
            ], ["c1-35-vocab"]),
            fb("vocabulary", "recall", "A polgárok magánszférájának védelme az információs _____ elidegeníthetetlen része. (self-determination / önrendelkezés)", "önrendelkezés", "Defense of citizens' privacy is an inalienable part of informational self-determination.", ["c1-35-vocab"]),
            fb("vocabulary", "recall", "A technológia exponenciális fejlődése etikai _____ követel az emberiségtől. (boundaries / korlátokat)", "korlátokat", "Exponential development of technology demands ethical boundaries from humanity.", ["c1-35-vocab"]),
            fb("grammar", "recall", "A folyamatokat kibernetikailag _____ minimalizálható az entrópia. (modeling / modellezve)", "modellezve", "Modeling processes cybernetically entropy can be minimized.", ["c1-adv-information-entropy-cybernetics"]),
            fb("grammar", "context", "Az államnak kötelessége _____ a polgárok kommunikációjának titkosságát. (guarantee / garantálnia)", "garantálnia", "The state has a duty to guarantee the secrecy of citizens' communication.", ["c1-modal-deontic-digital-privacy-ethics"]),
            fb("grammar", "context", "Ahogyan terjed a technológia hatalma, _____ növekszik az etikai felelősség. (so / úgy)", "úgy", "As the power of technology spreads, so does ethical responsibility grow.", ["c1-syntax-von-neumann-technological-synthesis"]),
            mc("grammar", "context", "Mi Neumann János szerint a technológiai fejlődés legfőbb erkölcsi tanulsága?", [
                "A technika gyorsulása miatt az emberiség túlélése nem a gépek hatalmán, hanem a szabadság és az erkölcs intézményes védelmén múlik.",
                "Minden matematikusnak abba kell hagynia a kutatást.",
                "A számítógépek mindent maguktól megoldanak az ember helyett."
            ], 0, ["c1-syntax-von-neumann-technological-synthesis"]),
            sb("grammar", "produce", ["A", "digitális", "magánszféra", "védelme", "az", "emberi", "méltóság", "alapja."], ["A", "digitális", "magánszféra", "védelme", "az", "emberi", "méltóság", "alapja."], "Defense of digital privacy is the basis of human dignity.", ["c1-modal-deontic-digital-privacy-ethics"]),
            sw("production", [{"prompt": "Write a critical evaluation of surveillance capitalism using a participial clause.", "answer": "A digitális óriásvállalatok a polgárok minden rezdülését szisztematikusan profilozva és a viselkedési többletet kisajátítva olyan algoritmikus determinizmust kényszerítenek a társadalomra, amely aláássa a demokratikus önrendelkezést."}], ["c1-participle-algorithmic-determinism"]),
            sw("production", [{"prompt": "Synthesize John von Neumann's technological vision using correlative syntax.", "answer": "Ahogyan a számítástechnika és az algoritmusok exponenciálisan átalakítják az emberi civilizációt, úgy bizonyosodik be Neumann jóslata: a túlélés záloga az emberi méltóság és a szabadság megingathatatlan védelmében rejlik."}], ["c1-syntax-von-neumann-technological-synthesis"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-megfigyeles)
    # ----------------------------------------------------
    disc_intro = [
        "In 2021, the international Pegasus project unmasked the Hungarian state's illegal deployment of military-grade cyber-espionage weapons against investigative journalists, media executives, lawyers, and opposition figures.",
        "In this unit, following the investigative revelations of the Pegasus scandal, the rubber-stamp ministerial wiretap authorizations under Varga Judit and Völner Pál, the chilling intimidation of independent civil society, and the 50-year parliamentary cover-up, you will master the elevated critical discourse of state cyber-espionage, secret service abuses, and digital human rights defense at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Pegasus Revelation & State Cyber-Espionage",
            "grammar_title": "Discourse Markers Diagnosing Illegal State Cyber Espionage and Surveillance",
            "grammar_skill": "c1-discourse-cyber-surveillance-scandal-framing",
            "goals": [
                "I can analyze the 2021 Pegasus spyware scandal in Hungary, military cyber-weapons, and the targeting of journalists (*Pegasus-botrány, izraeli NSO Group kémszoftver, Panyi Szabolcs megfigyelése, független újságírók lehallgatása*).",
                "I can deploy discourse markers diagnosing illegal state cyber-espionage (*az állami kiberkémkedés botrányos bizonyítékaként értékelve, a jogállamiság fundamentumainak felrúgásaként aposztrofálva, a hatalmi paranoiát leplezve*).",
                "I can evaluate Amnesty International's forensic evidence exposing smartphone infection."
            ],
            "vocab": [
                {"lemma": "Pegasus kémszoftver", "translation": "Pegasus spyware (NSO Group cyber-weapon)", "pos": "expression"},
                {"lemma": "állami kiberkémkedés", "translation": "state cyber-espionage", "pos": "expression"},
                {"lemma": "tényfeltáró újságíró", "translation": "investigative journalist", "pos": "expression"},
                {"lemma": "okostelefon feltörése", "translation": "zero-click smartphone hacking", "pos": "expression"},
                {"lemma": "titkos megfigyelés", "translation": "clandestine surveillance", "pos": "expression"},
                {"lemma": "forrásvédelem sérelme", "translation": "breach of source confidentiality", "pos": "expression"},
                {"lemma": "NSO Group", "translation": "NSO Group (Israeli cyber-arms firm)", "pos": "noun"},
                {"lemma": "nemzetközi tényfeltárás", "translation": "international investigative consortium", "pos": "expression"}
            ],
            "gr_text1": "Discourse markers expose unlawful state cyber-espionage against democratic watchdogs: `az államilag vezényelt kiberkémkedés iskolapéldájaként értékelve` (evaluated as a textbook case of state-directed cyber-espionage), `a független sajtó elleni illegális hadüzenetként aposztrofálva` (characterized as an illegal declaration of war against independent press), `a tekintélyelvű rezsimekre jellemző paranoia jegyében` (in the spirit of paranoia characteristic of authoritarian regimes).",
            "gr_text2": "Example: `A magyar kormányzat Pegasus kémszoftverrel folytatott akcióit a nemzetközi közvélemény a legsúlyosabb állami kiberkémkedésként értékelve egyhangúlag elítélte`.",
            "gr_table": [
                ["Az újságírók megfigyelését állami bűncselekményként értékelve indult vizsgálat.", "Evaluating the surveillance of journalists as a state crime an investigation was launched."],
                ["A kémszoftver bevetését a sajtószabadság elleni merényletként aposztrofálták.", "They characterized the deployment of the spyware as an assassination attempt against press freedom."],
                ["A nemzetbiztonsági célok ürügyén hallgatták le a kritikus médiát.", "Critical media were wiretapped under the pretext of national security goals."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-01-pegasus-botrany-ujsagirok",
                "title": "A zsebre vágott kém: A Pegasus-botrány kirobbanása",
                "summary": "2021 júliusában a Forbidden Stories és a Direkt36 leleplezte, hogy a magyar titkosszolgálatok katonai kiberfegyvert, az izraeli Pegasus szoftvert vetették be független tényfeltáró újságírók és laptulajdonosok telefonjai ellen.",
                "paragraphs": [
                    {"type": "narration", "text": "2021 forró nyarán az évszázad legsúlyosabb megfigyelési botránya robbant ki: tizenhét nemzetközi szerkesztőség, köztük a magyar Direkt36 tényfeltáró központ és az Amnesty International nyilvánosságra hozta a Pegasus-projekt leleplező adatait."},
                    {"type": "dialogue", "speaker": "Panyi Szabolcs", "text": "Amikor kiderült, hogy a telefonomat heteken át hekkelték a katonai kémszoftverrel, világossá vált: a hatalom a legintimebb magánéletünket és a forrásainkat hallgatta le. Az állami kiberkémkedés nyílt bizonyítékaként értékelve az esetet ez nemcsak ellenem, hanem a szabad sajtó egésze ellen elkövetett merénylet volt."},
                    {"type": "narration", "text": "A technikai elemzések igazolták, hogy a Pegasus láthatatlanul törte fel a telefonokat: bekapcsolta a mikrofont, a kamerát, hozzáférést szerzett a titkosított üzenetekhez, fényképekhez és a tartózkodási helyhez. A megfigyeltek listáján nem terroristák, hanem újságírók, médiavállalkozók, ügyvédek és ellenzéki politikusok szerepeltek."},
                    {"type": "narration", "text": "A leleplezés sokkolta az európai közvéleményt: kiderült, hogy az Európai Unió határain belül egy tagállam kormánya terrorizmus elleni fegyvereket fordít a saját polgárai ellen."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért robbantott ki nemzetközi botrányt a Pegasus kémszoftver magyarországi alkalmazása?", [
                    "Mert a kormány a terrorizmus elleni katonai kiberfegyvert illegálisan, független tényfeltáró újságírók, médiavezetők, ügyvédek és politikai ellenfelek lehallgatására használta fel.",
                    "Mert a szoftver túl drága volt a költségvetésnek.",
                    "Mert az izraeli cég elfelejtette elküldeni a számlát a minisztériumnak."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A lehallgatást állami kiberkémkedésként _____ a nemzetközi sajtó azonnali vizsgálatot követelt. (evaluating / értékelve)", "értékelve", "Evaluating the wiretapping as state cyber-espionage the international press demanded an immediate investigation.", ["c1-discourse-cyber-surveillance-scandal-framing"]),
                match("vocabulary", "controlled", [
                    ["Pegasus kémszoftver", "az izraeli NSO Group katonai fokozatú telefonfeltörő fegyvere"],
                    ["állami kiberkémkedés", "a titkosszolgálatok törvénytelen digitális behatolása a polgárok eszközeibe"],
                    ["forrásvédelem sérelme", "az újságírói informátorok leleplezése a lehallgatások által"],
                    ["tényfeltáró újságíró", "a hatalmi visszaéléseket feltáró független sajtómunkás"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A megfigyelést a sajtószabadság elleni támadásként _____ a civil szervezetek tiltakoztak. (characterizing / aposztrofálva)", "aposztrofálva", "Characterizing the surveillance as an attack against press freedom civil organizations protested.", ["c1-discourse-cyber-surveillance-scandal-framing"]),
                sb("grammar", "practice", ["A", "hatalom", "katonai", "kémszoftvert", "vetett", "be", "az", "újságírók", "ellen."], ["A", "hatalom", "katonai", "kémszoftvert", "vetett", "be", "az", "újságírók", "ellen."], "Power deployed military spyware against journalists.", ["c1-discourse-cyber-surveillance-scandal-framing"]),
                dc("dialogue", [
                    {"speaker": "Médiajogász", "text": "Mi a legsúlyosabb következménye az újságírók Pegasus-megfigyelésének?"},
                    {"speaker": "Főszerkesztő", "text": "Az, hogy a forrásvédelem durva felrúgásaként eljárva megbénítja a hatalmi korrupciót leleplező _____ munkáját."},
                    {"speaker": "Médiajogász", "text": "Az informátorok többé nem mernek beszélni a sajtóval."}
                ], ["tényfeltárók", "festők", "szakácsok"], 0, ["c1-discourse-cyber-surveillance-scandal-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of the Pegasus scandal using a discourse marker.", "answer": "A Pegasus kémszoftver független újságírók elleni bevetését az államilag vezényelt illegális kiberkémkedés iskolapéldájaként értékelve a nemzetközi közösség elítélte a magyar titkosszolgálatok jogsértő eljárását."}], ["c1-discourse-cyber-surveillance-scandal-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a Pegasus-lehallgatásokat a legpontosabban?", [
                    "az állami kiberkémkedés botrányaként értékelve / a sajtószabadság durva felrúgásaként aposztrofálva",
                    "amikor új szoftvert telepítenek a mobilra az üzletben",
                    "hogyha valaki elfelejti a telefonja pin-kódját"
                ], 0, ["c1-discourse-cyber-surveillance-scandal-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Ministerial Rubber-Stamping & Absence of Judicial Oversight",
            "grammar_title": "Critical Evaluative Adverbials Exposing Unconstrained Ministerial Wiretap Authorization",
            "grammar_skill": "c1-adv-unconstrained-wiretap-authorization-critique",
            "goals": [
                "I can analyze the lack of independent judicial oversight, ministerial rubber-stamping, and Varga Judit delegating powers to Völner Pál (*igazságügyi pecsét, külső bírói kontroll hiánya, Varga Judit és Völner Pál, biankó megfigyelési engedélyek*).",
                "I can deploy critical evaluative adverbials exposing arbitrary executive surveillance (*önkényesen pecsételve le a lehallgatásokat, a bírói kontrollt teljesen kiiktatva, felhatalmazás nélkül delegálva a jogköröket lojális politikusoknak*).",
                "I can critique European Court of Human Rights judgments on Hungarian secret surveillance (Szabó and Vissy v. Hungary)."
            ],
            "vocab": [
                {"lemma": "bírói kontroll hiánya", "translation": "absence of judicial control / oversight", "pos": "expression"},
                {"lemma": "miniszteri engedélyezés", "translation": "ministerial wiretap authorization", "pos": "expression"},
                {"lemma": "biankó engedély", "translation": "blanket / rubber-stamp authorization", "pos": "expression"},
                {"lemma": "igazságügyi pecsét", "translation": "ministerial rubber stamp", "pos": "expression"},
                {"lemma": "jogállami garanciák hiánya", "translation": "lack of rule of law safeguards", "pos": "expression"},
                {"lemma": "Völner-ügy", "translation": "Völner corruption case (state secretary wiretapper)", "pos": "expression"},
                {"lemma": "titkos információgyűjtés", "translation": "clandestine intelligence gathering", "pos": "expression"},
                {"lemma": "EJEB elmarasztalás", "translation": "ECtHR condemnation (Strasbourg ruling)", "pos": "expression"}
            ],
            "gr_text1": "Critical evaluative adverbials expose the arbitrary executive monopoly over wiretap authorizations: `a független bírói kontrollt szándékosan kiiktatva` (deliberately eliminating independent judicial oversight), `önkényesen és futószalagon pecsételve le a titkos megfigyeléseket` (arbitrarily and assembly-line rubber-stamping secret surveillance), `átláthatatlan módon átruházva a döntést a korrupcióba keveredett államtitkárra` (untransparently delegating the decision to the state secretary entangled in corruption).",
            "gr_text2": "Example: `A minisztérium a külső bírói felügyeletet teljesen kiiktatva és biankó engedélyeket kiadva tette lehetővé a politikai ellenfelek törvénytelen lehallgatását`.",
            "gr_table": [
                ["A tárca a bírói felügyeletet kiiktatva hagyta jóvá a titkosszolgálati kéréseket.", "Eliminating judicial oversight the ministry approved intelligence requests."],
                ["Futószalagon pecsételve le az engedélyeket a miniszter nem vizsgálta a megalapozottságot.", "Rubber-stamping approvals on an assembly line the minister did not examine substantiation."],
                ["Átláthatatlan módon eljárva adtak zöld utat a Pegasus bevetésének.", "Acting in an untransparent manner they gave green light to the deployment of Pegasus."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-02-igazsagugyi-pecset-varga-judit",
                "title": "A futószalagon adott engedélyek: A minisztériumi pecsét",
                "summary": "Magyarországon a nemzetbiztonsági célú megfigyeléseket nem független bíró, hanem az igazságügyi miniszter engedélyezi. Varga Judit miniszter a feladatot a később súlyos korrupcióval megvádolt Völner Pálra bízta, aki kérdés nélkül pecsételt le mindent.",
                "paragraphs": [
                    {"type": "narration", "text": "A demokratikus jogállamokban alapvető garancia, hogy a polgárok titkos lehallgatását kizárólag független bíró engedélyezheti, szigorú és alapos indokolás mellett. Magyarországon azonban a nemzetbiztonsági törvény az igazságügyi miniszter egyszemélyi kezébe adta ezt a hatalmat."},
                    {"type": "dialogue", "speaker": "Alkotmányjogász", "text": "A független bírói kontrollt teljesen kiiktatva a rendszer a végrehajtó hatalom önkényére bízta a magánszféra sorsát. Varga Judit igazságügyi miniszter ráadásul átruházta az engedélyezési jogkört államtitkárára, Völner Pálra, aki futószalagon, évi több mint ezer esetben pecsételte le a titkosszolgálatok kérelmeit."},
                    {"type": "narration", "text": "A groteszk fordulat akkor következett be, amikor Völner Pált hivatali vesztegetés elfogadásával gyanúsították meg: kiderült, hogy az az ember döntött a magyar állampolgárok és újságírók lehallgatásáról, aki maga is egy bűnözői hálózat kulcsfigurája volt."},
                    {"type": "narration", "text": "A strasbourgi Emberi Jogok Európai Bírósága a Szabó és Vissy kontra Magyarország ügyben már korábban kimondta: a külső bírói kontroll nélküli miniszteri engedélyezés önmagában sérti az Emberi Jogok Európai Egyezményét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelent súlyos jogállami torzulást a magyarországi lehallgatások miniszteri engedélyezési rendszere?", [
                    "Mert nincs független bírói kontroll: a politikai kormányzat tagja (az igazságügyi miniszter vagy államtitkára) egymaga, fellebbezési lehetőség és külső felügyelet nélkül pecsételi le a titkos megfigyeléseket.",
                    "Mert a pecsétek tintája túl drága az államkincstárnak.",
                    "Mert a miniszterek nem tudnak gyorsan aláírni."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A független bírói kontrollt teljesen _____ a kormányzat ellenőrizetlen hatalmat adott a szolgálatoknak. (eliminating / kiiktatva)", "kiiktatva", "Completely eliminating independent judicial control the government gave unchecked power to the services.", ["c1-adv-unconstrained-wiretap-authorization-critique"]),
                match("vocabulary", "controlled", [
                    ["bírói kontroll hiánya", "a megfigyelések feletti független jogi garancia hiánya"],
                    ["miniszteri engedélyezés", "a végrehajtó hatalom politikai aláírása a lehallgatásokhoz"],
                    ["biankó engedély", "automatikus, érdemi vizsgálat nélküli hatósági jóváhagyás"],
                    ["Völner-ügy", "a megfigyeléseket pecsételő államtitkár korrupciós botránya"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Futószalagon _____ le az engedélyeket a minisztérium nem ellenőrizte a jogszerűséget. (rubber-stamping / pecsételve)", "pecsételve", "Rubber-stamping authorizations on an assembly line the ministry did not verify legality.", ["c1-adv-unconstrained-wiretap-authorization-critique"]),
                sb("grammar", "practice", ["A", "minisztérium", "bírói", "kontroll", "nélkül", "engedélyezte", "a", "lehallgatásokat."], ["A", "minisztérium", "bírói", "kontroll", "nélkül", "engedélyezte", "a", "lehallgatásokat."], "The ministry authorized wiretaps without judicial control.", ["c1-adv-unconstrained-wiretap-authorization-critique"]),
                dc("dialogue", [
                    {"speaker": "Ügyvéd", "text": "Hogyan történhetett meg, hogy újságírókat hallgattak le nemzetbiztonsági kockázatra hivatkozva?"},
                    {"speaker": "Vizsgálóbizottsági tag", "text": "Úgy, hogy a minisztérium kérdések nélkül, futószalagon pecsételve adta ki a biankó _____ a titkosszolgálatnak."},
                    {"speaker": "Ügyvéd", "text": "Ez a hatalommal való nyílt visszaélés volt."}
                ], ["engedélyeket", "könyveket", "leveleket"], 0, ["c1-adv-unconstrained-wiretap-authorization-critique"]),
                sw("production", [{"prompt": "Write a critical evaluation of ministerial wiretap authorization using an evaluative adverbial.", "answer": "A külső és független bírói kontrollt szándékosan kiiktatva és a titkos megfigyeléseket futószalagon pecsételve le az igazságügyi tárca megfosztotta a polgárokat a jogállami garanciáktól és zöld utat adott a törvénytelen kiberkémkedésnek."}], ["c1-adv-unconstrained-wiretap-authorization-critique"]),
                mc("grammar", "check", "Melyik szerkezet leplezi le a miniszteri engedélyezés önkényét a leghitelesebben?", [
                    "a bírói felügyeletet kiiktatva / futószalagon pecsételve le a biankó engedélyeket",
                    "amikor a miniszter új tollal írja alá a papírt az asztalnál",
                    "hogyha a postás délben viszi a leveleket a hivatalba"
                ], 0, ["c1-adv-unconstrained-wiretap-authorization-critique"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Chilling Effect & Secret Service Intimidation",
            "grammar_title": "Deontic Modal Structures Asserting Journalistic Duty of Confidential Source Protection",
            "grammar_skill": "c1-modal-deontic-journalistic-source-protection",
            "goals": [
                "I can analyze the 'chilling effect' of state surveillance, psychological intimidation, and secret service pressure on civil society (*dermesztő hatás / chilling effect, forrásvédelem, titkosszolgálati megfélemlítés, civil társadalom autonómiája*).",
                "I can deploy deontic modal structures asserting the sacred duty of journalistic source protection (*az újságírónak kötelessége minden körülmények között megvédenie az informátorok kilétét, megalkuvást nem ismerve kell védeni a sajtótitkot a szolgálatokkal szemben, nem engedhető meg a források állami kiszolgáltatása*).",
                "I can evaluate the European Court of Human Rights jurisprudence on investigative reporting."
            ],
            "vocab": [
                {"lemma": "dermesztő hatás", "translation": "chilling effect (self-censorship caused by fear)", "pos": "expression"},
                {"lemma": "forrásvédelem szentsége", "translation": "sanctity of journalistic source confidentiality", "pos": "expression"},
                {"lemma": "megfélemlítés", "translation": "intimidation / harassment", "pos": "noun"},
                {"lemma": "sajtótitok", "translation": "press secrecy / confidentiality", "pos": "noun"},
                {"lemma": "öncenzúra", "translation": "self-censorship", "pos": "noun"},
                {"lemma": "civil ellenállás", "translation": "civil resistance", "pos": "expression"},
                {"lemma": "titkosszolgálati zsarolás", "translation": "secret service blackmail / pressure", "pos": "expression"},
                {"lemma": "szakmai szolidaritás", "translation": "professional solidarity", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures formulate the ethical imperative of investigative journalists to resist intimidation: `a sajtómunkásnak kötelessége a végsőkig védeni az informátorai anonimitását` (it is the duty of the press worker to protect the anonymity of informants to the end), `megalkuvást nem ismerve kell szembeszállni a titkosszolgálati megfélemlítési kísérletekkel` (one must resist secret service intimidation attempts without compromise), `nem engedhető meg, hogy a félelem dermesztő hatása elhallgattassa a korrupciót leleplező hangokat` (it cannot be permitted that the chilling effect of fear silence voices exposing corruption).",
            "gr_text2": "Example: `A tényfeltáró újságíróknak etikai kötelességük megvédeni a forrásaikat, még akkor is, ha az állam katonai kémszoftverekkel vadászik a leleplező dokumentumokra`.",
            "gr_table": [
                ["Az újságírónak kötelessége megőriznie a sajtótitkot minden hatósági nyomás ellenére.", "It is the journalist's duty to preserve press secrecy despite all official pressure."],
                ["Elengedhetetlen a forrásvédelem szigorú törvényi és technológiai biztosítása.", "Strict legal and technological provision of source protection is indispensable."],
                ["Megalkuvást nem ismerve kell elutasítani a titkosszolgálati együttműködést.", "One must reject secret service cooperation without compromise."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-03-titkosszolgalati-felelemkeltes",
                "title": "A dermesztő hatás: Félelemkeltés és a források védelme",
                "summary": "A Pegasus bevetésének legsúlyosabb társadalmi következménye a 'dermesztő hatás' lett: a lehallgatások célja nem pusztán információgyűjtés volt, hanem a kritikus újságírók és informátoraik pszichológiai megfélemlítése.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy államban nyilvánvalóvá válik, hogy a hatóságok a legfejlettebb kiberfegyverekkel figyelik a kormányzatot bíráló polgárokat, a társadalomban eluralkodik a gyanakvás és a félelem. A jogtudomány ezt nevezi 'dermesztő hatásnak' (chilling effect)."},
                    {"type": "dialogue", "speaker": "Oknyomozó riporter", "text": "A Pegasus bevetése után az informátorok, minisztériumi tisztviselők és szakértők rettegni kezdtek a telefonos beszélgetésektől. Kötelességünk volt azonnal titkosított csatornákra, analóg módszerekre és személyes találkozókra váltani: a forrásvédelem szent kötelesség, amelyet semmilyen titkosszolgálati nyomásra nem adhatunk fel."},
                    {"type": "narration", "text": "A megfélemlítés célja a csend kikényszerítése volt. Ha a közpénzek ellopásáról értesülő források nem mernek az újságírókhoz fordulni, a korrupció láthatatlanná és számonkérhetetlenné válik."},
                    {"type": "narration", "text": "A független magyar szerkesztőségek azonban nem hátráltak meg. Új digitális biztonsági protokollokat vezettek be, megerősítették a forrásvédelmet, bizonyítva: a szabad sajtó bátorságát még a katonai kémszoftverek sem képesek megtörni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a médiajog 'dermesztő hatásnak' (chilling effect) a megfigyelések kontextusában?", [
                    "Azt a pszichológiai állapotot és öncenzúrát, amikor a polgárok és informátorok a lehallgatástól és retorziótól való félelmükben nem mernek beszélni a sajtóval vagy bírálni a hatalmat.",
                    "A hideg téli időjárás miatti telefonos akkumulátor-lemerülést.",
                    "A számítógépes ventilátorok hangos zúgását a szerverszobában."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A sajtómunkásnak etikai _____ megvédeni a bizalmas források anonimitását. (duty / kötelessége)", "kötelessége", "It is the press worker's ethical duty to protect the anonymity of confidential sources.", ["c1-modal-deontic-journalistic-source-protection"]),
                match("vocabulary", "controlled", [
                    ["dermesztő hatás", "a megfigyeléstől való félelem szülte bénultság és öncenzúra"],
                    ["forrásvédelem szentsége", "az újságírói informátorok kilétének feltétlen védelme"],
                    ["sajtótitok", "a hivatás gyakorlása során megismert adatok kötelező megőrzése"],
                    ["titkosszolgálati megfélemlítés", "a hatóságok nyomásgyakorlása a kritikus hangok elnémítására"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ a sajtótitok sérthetetlensége mellett. (stand / kiállni)", "kiállni", "Without compromise one must stand up for the inviolability of press secrecy.", ["c1-modal-deontic-journalistic-source-protection"]),
                sb("grammar", "practice", ["Az", "újságírónak", "kötelessége", "megvédeni", "a", "forrásai", "biztonságát."], ["Az", "újságírónak", "kötelessége", "megvédeni", "a", "forrásai", "biztonságát."], "It is the duty of the journalist to protect the security of their sources.", ["c1-modal-deontic-journalistic-source-protection"]),
                dc("dialogue", [
                    {"speaker": "Tényfeltáró", "text": "Hogyan tarthatjuk meg az informátorok bizalmát a Pegasus-botrány után?"},
                    {"speaker": "Főszerkesztő", "text": "Úgy, hogy kötelességünk a legszigorúbb biztonsági intézkedésekkel garantálni a forrásvédelem _____."},
                    {"speaker": "Tényfeltáró", "text": "A forrásaink védelme a hitelünk alapköve."}
                ], ["szentségét", "árát", "méretét"], 0, ["c1-modal-deontic-journalistic-source-protection"]),
                sw("production", [{"prompt": "Write a declaration of journalistic source protection using a deontic modal.", "answer": "A tényfeltáró újságíróknak megalkuvást nem ismerve kötelességük megvédeni az informátorok titkosságát, és nem engedhető meg, hogy a titkosszolgálati lehallgatások dermesztő hatása elhallgattassa a szabad sajtót."}], ["c1-modal-deontic-journalistic-source-protection"]),
                mc("grammar", "check", "Melyik deontikus szerkezet fogalmazza meg a forrásvédelem kötelezettségét a leghatározottabban?", [
                    "kötelessége megvédeni az informátorokat / megalkuvást nem ismerve kell őrizni a sajtótitkot",
                    "jó lenne ha az újságírók néha kikapcsolnák a telefonjukat",
                    "a riporterek beszélgethetnek a forrásokkal a kávézóban"
                ], 0, ["c1-modal-deontic-journalistic-source-protection"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Parliamentary Cover-Up & The 50-Year Classification",
            "grammar_title": "Proportional Correlative Structures Mapping National Security Classification Against Democratic Oversight",
            "grammar_skill": "c1-adv-proportional-cyber-secrecy-erosion",
            "goals": [
                "I can analyze the parliamentary cover-up of the Pegasus scandal, the 2070 classification, and the European Parliament PEGA Committee inquiry (*Nemzetbiztonsági Bizottság, 2070-ig titkosított akták, elszámoltathatóság megkerülése, EP PEGA-bizottság jelentése*).",
                "I can construct proportional correlative structures mapping classification to democratic erosion (*minél agresszívabban titkosítja a kormányzat a lehallgatási iratokat, annál nyilvánvalóbbá válik a hatalommal való visszaélés mértéke*).",
                "I can critique parliamentary committee sabotage in illiberal democracies."
            ],
            "vocab": [
                {"lemma": "Nemzetbiztonsági Bizottság", "translation": "National Security Parliamentary Committee", "pos": "expression"},
                {"lemma": "50 évre titkosítva", "translation": "classified for 50 years (until 2070)", "pos": "expression"},
                {"lemma": "parlamenti eltussolás", "translation": "parliamentary cover-up", "pos": "expression"},
                {"lemma": "PEGA-bizottság", "translation": "EP PEGA Committee of Inquiry", "pos": "noun"},
                {"lemma": "elszámoltathatóság", "translation": "accountability", "pos": "noun"},
                {"lemma": "bizottsági szabotázs", "translation": "committee sabotage / boycotting quorum", "pos": "expression"},
                {"lemma": "államtitok", "translation": "state secret", "pos": "noun"},
                {"lemma": "visszaélés gyanúja", "translation": "suspicion of abuse of power", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures chart how government classification directly correlates with the erosion of democratic scrutiny: `minél mélyebbre próbálja rejteni a hatalom a Pegasus-aktákat, annál egyértelműbb a politikai bűnrészesség` (the deeper power tries to hide Pegasus files, the clearer political complicity is), `amilyen mértékben blokkolja a kormánypárti többség a parlamenti vizsgálatot, olyan mértékben erősödik az európai felháborodás` (to the extent the ruling majority blocks the parliamentary probe, to that extent European outrage strengthens).",
            "gr_text2": "Example: `Minél hisztérikusabban próbálta a kormányzat ötven évre titkosítani a megfigyelési jegyzőkönyveket, annál élesebb elmarasztaló jelentést fogalmazott meg az Európai Parlament PEGA-bizottsága`.",
            "gr_table": [
                ["Minél tovább titkolják az iratokat, annál mélyebbé válik a bizalmatlanság.", "The longer files are kept secret, the deeper distrust becomes."],
                ["Amilyen mértékben szabotálják a bizottságot, olyan mértékben sérül a demokrácia.", "To the extent they sabotage the committee, to that extent democracy is harmed."],
                ["Minél inkább hivatkoznak államtitokra, annál gyanúsabb a hatalmi eljárás.", "The more they invoke state secrets, the more suspicious the power procedure is."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-04-nemzetbiztonsagi-bizottsag-eltitkolas",
                "title": "Ötven évre eltemetve: A parlamenti eltussolás és a PEGA-bizottság",
                "summary": "A magyar kormányzat ahelyett, hogy tisztázta volna a Pegasus-botrányt, 2070-ig titkosította a vizsgálóbizottsági ülések jegyzőkönyveit. Az Európai Parlament PEGA-bizottsága Budapestre látogatva a jogállamiság súlyos megsértését állapította meg.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az ellenzéki képviselők kezdeményezték a parlament Nemzetbiztonsági Bizottságának rendkívüli ülését a Pegasus-lehallgatások kivizsgálására, a kormánypárti többség heteken át bojkottálta az üléseket, megakadályozva a határozatképességet."},
                    {"type": "dialogue", "speaker": "Ellenzéki bizottsági tag", "text": "Amikor végül kénytelenek voltak meghallgatni a szolgálatok vezetőit, a hatalom döbbenetes döntést hozott: a vizsgálati jegyzőkönyveket ötven évre, 2070-ig minősítették államtitokká. Minél hisztérikusabban titkolóznak, annál nyilvánvalóbb, hogy a legsúlyosabb törvénysértéseket próbálják elfedni."},
                    {"type": "narration", "text": "Az ügyet azonban nem lehetett a szőnyeg alá söpörni. Az Európai Parlament felállította a PEGA vizsgálóbizottságot, amely Budapestre utazott, hogy meghallgassa az áldozatokat és a minisztériumokat. Varga Judit miniszter egyszerűen megtagadta a találkozót az európai képviselőkkel."},
                    {"type": "narration", "text": "A PEGA-bizottság zárójelentése megsemmisítő erejű volt: kimondta, hogy Magyarországon a kémszoftvert a hatalom megtartására és a kritikus nyilvánosság megfélemlítésére használták, s a demokratikus felügyelet teljes hiánya rendszerszintű fenyegetést jelent."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan próbálta meg a magyar kormányzat elfedni a Pegasus-vizsgálat eredményeit a parlamentben?", [
                    "Bojkottálta a bizottsági üléseket, majd a vizsgálat jegyzőkönyveit ötven évre, egészen 2070-ig titkosította a nyilvánosság elől.",
                    "Nyilvános tévévitát rendezett a parlament plenáris ülésén.",
                    "Azonnal felmondta a szerződést az izraeli céggel és kártérítést fizetett."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Minél jobban titkolózik a kormányzat, _____ nyilvánvalóbb a politikai felelősség. (the / annál)", "annál", "The more the government conceals, the more obvious political responsibility is.", ["c1-adv-proportional-cyber-secrecy-erosion"]),
                match("vocabulary", "controlled", [
                    ["Nemzetbiztonsági Bizottság", "a titkosszolgálatokat ellenőrizni hivatott parlamenti testület"],
                    ["50 évre titkosítva", "az iratok elzárása a nyilvánosság elől 2070-ig"],
                    ["PEGA-bizottság", "az Európai Parlament kémszoftver-visszaéléseket vizsgáló testülete"],
                    ["parlamenti eltussolás", "a törvényhozási vizsgálatok szándékos megakadályozása"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben korlátozzák a nyilvánosságot, _____ mértékben nő a gyanú a visszaélésekre. (such / olyan)", "olyan", "To such an extent as publicity is restricted, to that extent suspicion of abuses grows.", ["c1-adv-proportional-cyber-secrecy-erosion"]),
                sb("grammar", "practice", ["Minél", "mélyebb", "a", "titkolózás,", "annál", "súlyosabb", "a", "politikai", "válság."], ["Minél", "mélyebb", "a", "titkolózás,", "annál", "súlyosabb", "a", "politikai", "válság."], "The deeper the secrecy, the more severe the political crisis.", ["c1-adv-proportional-cyber-secrecy-erosion"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Miért minősítették a Pegasus-jegyzőkönyveket 2070-ig államtitokká?"},
                    {"speaker": "Parlamenti tudósító", "text": "Mert minél tovább tudják elzárni a bizonyítékokat, annál inkább remélik a politikai következmények _____."},
                    {"speaker": "Újságíró", "text": "De a nemzetközi tényfeltárást nem lehet titkosítani."}
                ], ["elkerülését", "növelését", "árát"], 0, ["c1-adv-proportional-cyber-secrecy-erosion"]),
                sw("production", [{"prompt": "Write a proportional sentence mapping secrecy against accountability.", "answer": "Minél agresszívabban próbálta a hatalom ötven évre titkosítani a Pegasus-vizsgálat jegyzőkönyveit, annál nyilvánvalóbbá vált a független nyilvánosság és az európai intézmények előtt a jogsértések súlyossága és a parlamenti felügyelet teljes kudarca."}], ["c1-adv-proportional-cyber-secrecy-erosion"]),
                mc("grammar", "check", "Melyik páros kötőszó fejezi ki a titkolózás és a bűnrészesség összefüggését a legpontosabban?", [
                    "minél mélyebbre titkosítják az iratokat, annál nyilvánvalóbb a visszaélés",
                    "bár bezárták az ajtót, mégis beszélgetnek a folyosón",
                    "ha a képviselők fáradtak, korán hazamennek"
                ], 0, ["c1-adv-proportional-cyber-secrecy-erosion"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Restitution of Digital Rights & Constitutional Oversight",
            "grammar_title": "Evaluative Conclusive Particles Asserting Inalienability of Digital Constitutional Privacy",
            "grammar_skill": "c1-adv-conclusive-digital-privacy-restitution",
            "goals": [
                "I can analyze the democratic restitution of digital human rights, independent judicial warrants, and secret service reform (*digitális jogállam, külső bírói kontroll visszaállítása, titkosszolgálati reform, polgári szabadság védelme*).",
                "I can deploy conclusive evaluative particles asserting digital privacy (*értelemszerűen elengedhetetlen, fundamentálisan megdönthetetlen, kétséget kizáróan létfontosságú, végső soron elidegeníthetetlen*).",
                "I can debate the constitutional limits of state cyber-surveillance in 21st-century democracies."
            ],
            "vocab": [
                {"lemma": "digitális jogállam", "translation": "digital rule of law", "pos": "expression"},
                {"lemma": "külső bírói kontroll", "translation": "external judicial oversight / warrant", "pos": "expression"},
                {"lemma": "titkosszolgálati reform", "translation": "intelligence agency reform", "pos": "expression"},
                {"lemma": "visszaélések kivizsgálása", "translation": "investigation of surveillance abuses", "pos": "expression"},
                {"lemma": "alkotmányos védelem", "translation": "constitutional protection of privacy", "pos": "expression"},
                {"lemma": "független felügyelet", "translation": "independent oversight body", "pos": "expression"},
                {"lemma": "digitális emberi jogok", "translation": "digital human rights", "pos": "expression"},
                {"lemma": "társadalmi katarzis", "translation": "societal catharsis / reckoning", "pos": "expression"}
            ],
            "gr_text1": "Conclusive evaluative particles assert the non-negotiable imperative of restoring constitutional safeguards over surveillance: `értelemszerűen elengedhetetlen a független bírói kontroll bevezetése minden lehallgatásnál` (introducing independent judicial control for every wiretap is naturally indispensable), `fundamentálisan megdönthetetlen az információs önrendelkezés elve` (the principle of informational self-determination is fundamentally unshakeable), `végső soron elidegeníthetetlen a polgárok joga a megfigyelésmentes magánélethez` (ultimately citizens' right to surveillance-free private life is inalienable).",
            "gr_text2": "Example: `A Pegasus-botrány tanulsága szerint a digitális jogállam helyreállításához értelemszerűen elengedhetetlen és fundamentálisan megdönthetetlen a titkosszolgálatok szigorú demokratikus elszámoltathatósága`.",
            "gr_table": [
                ["A külső bírói engedélyezés értelemszerűen elengedhetetlen egy jogállamban.", "External judicial authorization is naturally indispensable in a state governed by rule of law."],
                ["A magánszféra védelme fundamentálisan megdönthetetlen alkotmányos alapjog.", "Defense of privacy is a fundamentally unshakeable constitutional right."],
                ["Végső soron elidegeníthetetlen a társadalom joga az állami önkény korlátozására.", "Ultimately society's right to limit state autocracy is inalienable."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-05-digitalis-jogallam-vedelme",
                "title": "A digitális szabadság védelmében: A jogállami helyreállítás",
                "summary": "A Pegasus-botrány történelmi vízválasztó: megmutatta, hogy a digitális korban a demokrácia védelme a kiberfegyverek szigorú jogi és alkotmányos korlátozásán múlik. A jövő záloga a független bírói garanciák és a titkosszolgálatok demokratikus kontrollja.",
                "paragraphs": [
                    {"type": "narration", "text": "A Pegasus kémszoftver visszaélései leleplezték a magyar autoriter államgépezet legsötétebb arcát. A botrány azonban a társadalmi felébredés katalizátorává is vált: a polgárok megértették, hogy a digitális magánszféra nem kényelmi kérdés, hanem a politikai szabadság legvégső bástyája."},
                    {"type": "dialogue", "speaker": "Társaság a Szabadságjogokért (TASZ) jogásza", "text": "Fundamentálisan megdönthetetlen igazság, hogy senkit sem lehet pusztán a véleménye vagy újságírói munkája miatt katonai kiberfegyverekkel megfigyelni. Értelemszerűen elengedhetetlen a nemzetbiztonsági törvény teljes körű reformja: minden titkos megfigyelést kötelező, független bírói engedélyhez kell kötni."},
                    {"type": "narration", "text": "A jogvédő szervezetek hazai és nemzetközi bíróságok elé vitték a lehallgatott újságírók ügyét, s az Európai Unióban megkezdődött a szigorúbb kiberbiztonsági és megfigyelés-ellenes jogszabályok kidolgozása."},
                    {"type": "narration", "text": "A digitális jogállam nem veszhet el. A jövő szabad Magyarországán a titkosszolgálatok a nemzet védelmét, és nem a mindenkori hatalom félelmeit és politikai érdekeit fogják szolgálni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen elengedhetetlen garanciák szükségesek a digitális jogállam helyreállításához a Pegasus-botrány után?", [
                    "A titkosszolgálatok politikai függetlenítése, a miniszteri önkény helyett kötelező külső bírói engedélyezés bevezetése, és a törvénytelen megfigyelések áldozatainak hatékony jogorvoslata.",
                    "Minden okostelefon állami elkobzása a lakosságtól.",
                    "A titkosszolgálati költségvetés titkos megduplázása."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A független bírói engedélyezés bevezetése értelemszerűen _____ a jogállamban. (indispensable / elengedhetetlen)", "elengedhetetlen", "Introducing independent judicial authorization is naturally indispensable in a state governed by rule of law.", ["c1-adv-conclusive-digital-privacy-restitution"]),
                match("vocabulary", "controlled", [
                    ["digitális jogállam", "az alkotmányos alapjogok és a magánszféra védelme a virtuális térben"],
                    ["külső bírói kontroll", "független bírói végzéshez kötött titkos megfigyelés"],
                    ["titkosszolgálati reform", "a nemzetbiztonsági szervek szigorú demokratikus elszámoltatása"],
                    ["digitális emberi jogok", "a kommunikáció és a személyes adatok sérthetetlensége"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Az információs önrendelkezés fundamentálisan _____ alapérték. (unshakeable / megdönthetetlen)", "megdönthetetlen", "Informational self-determination is a fundamentally unshakeable core value.", ["c1-adv-conclusive-digital-privacy-restitution"]),
                sb("grammar", "practice", ["A", "külső", "bírói", "kontroll", "értelemszerűen", "elengedhetetlen", "a", "demokráciában."], ["A", "külső", "bírói", "kontroll", "értelemszerűen", "elengedhetetlen", "a", "demokráciában."], "External judicial control is naturally indispensable in democracy.", ["c1-adv-conclusive-digital-privacy-restitution"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Hogyan zárható ki végleg a Pegasushoz hasonló visszaélések megismétlődése?"},
                    {"speaker": "Alkotmánybíró", "text": "Úgy, hogy végső soron elidegeníthetetlen a magánélet védelme, és fundamentálisan megdönthetetlen a titkosszolgálatok szigorú parlamenti és bírói _____."},
                    {"speaker": "Jogvédő", "text": "A szabadság a digitális térben sem alku tárgya."}
                ], ["kontrollja", "ára", "neve"], 0, ["c1-adv-conclusive-digital-privacy-restitution"]),
                sw("production", [{"prompt": "Write a conclusive synthesis on digital human rights using an evaluative particle.", "answer": "A digitális jogállam helyreállítása és a független bírói kontroll megteremtése értelemszerűen elengedhetetlen és fundamentálisan megdönthetetlen, hiszen a polgárok magánszférájának tiszteletben tartása a modern demokrácia legfőbb alkotmányos fundamentuma."}], ["c1-adv-conclusive-digital-privacy-restitution"]),
                mc("grammar", "check", "Melyik konkluzív kifejezés szintetizálja a digitális magánszféra helyreállítását a legerőteljesebben?", [
                    "értelemszerűen elengedhetetlen / fundamentálisan megdönthetetlen / végső soron elidegeníthetetlen",
                    "reméljük a kémek nem figyelnek minket többé",
                    "jó lenne ha mindenki venne egy új telefont jövőre"
                ], 0, ["c1-adv-conclusive-digital-privacy-restitution"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(35, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-pegasus-kiberkemkedes-jogallam.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A Pegasus-botrány: Állami kiberkémkedés és a digitális jogállam védelme",
            "level": "C1",
            "lesson": 5,
            "order": 35,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-digital-privacy-restitution"],
            "summary": "Átfogó krónika a 2021-es magyar Pegasus-botrányról: a katonai kémszoftver tényfeltáró újságírók, médiavezetők és ügyvédek elleni bevetéséről, a minisztériumi futószalag-engedélyezésről és a Völner-ügyről, a dermesztő hatásról és forrásvédelemről, a vizsgálati akták 2070-ig tartó eltitkolásáról és az EP PEGA-bizottság vizsgálatáról, valamint a digitális jogállam helyreállításának elengedhetetlen garanciáiról.",
            "vocabularyTopics": [
                "The Pegasus Surveillance Scandal & State Cyber-Espionage",
                "Restitution of Digital Rights & Constitutional Oversight"
            ],
            "paragraphs": [
                {"type": "narration", "text": "2021 júliusában a modern magyar politikatörténet legsúlyosabb megfigyelési botránya robbant ki: a Forbidden Stories nemzetközi tényfeltáró konzorcium és a Direkt36 leleplezte, hogy a magyar állam az izraeli NSO Group katonai fokozatú Pegasus kémszoftverét vetette be saját polgárai ellen."},
                {"type": "narration", "text": "A célpontok nem terroristák vagy bűnözők voltak, hanem hatalmi korrupciót kutató független újságírók – köztük Panyi Szabolcs –, független médiatulajdonosok, sztárügyvédek és ellenzéki politikusok. A kémszoftver láthatatlanul törte fel az okostelefonokat, korlátlan hozzáférést biztosítva a privát üzenetekhez, fényképekhez, mikrofonhoz és kamerához."},
                {"type": "narration", "text": "A leleplezések fényt derítettek a magyar lehallgatási rendszer súlyos strukturális hiányosságaira: a törvények nem írtak elő független bírói kontrollt. A megfigyeléseket az igazságügyi minisztérium nevében Völner Pál államtitkár pecsételte le biankó módon, aki később maga is súlyos korrupciós botrányba keveredett."},
                {"type": "narration", "text": "A hatalom ahelyett, hogy felelősséget vállalt volna, 2070-ig minősítette államtitokká a parlamenti vizsgálat jegyzőkönyveit. Az Európai Parlament PEGA-bizottsága azonban Budapestre látogatva megsemmisítő ítéletet mondott: kimondta, hogy Magyarországon a kémszoftvert a független nyilvánosság elnyomására és a hatalom védelmére használták."},
                {"type": "narration", "text": "A botrány végső tanulsága fundamentálisan megdönthetetlen: a digitális korban a szabadság nem maradhat a politikai önkény kiszolgáltatottja. A bírói engedélyhez kötött megfigyelés és az információs önrendelkezés garanciái értelemszerűen nélkülözhetetlenek a szabad társadalom megmaradásához."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        35,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can master the critical discourse of state cyber-espionage, Pegasus surveillance, and ministerial rubber-stamping.",
            "I can employ discourse markers of clandestine surveillance, critical evaluative adverbials, and deontic modal structures of source protection.",
            "I can construct proportional correlative structures and conclusive evaluative syntheses on digital constitutionalism."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés diagnosztizálja a Pegasus-lehallgatásokat a legpontosabban?", [
                "az állami kiberkémkedés botrányaként értékelve / a jogállamiság fundamentumainak felrúgásaként aposztrofálva",
                "hogyha valaki új alkalmazást tölt le a telefonjára",
                "amikor az internet sebessége lelassul este"
            ], 0, ["c1-discourse-cyber-surveillance-scandal-framing"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhető le a miniszteri engedélyezési önkény a leghitelesebben?", [
                "a független bírói kontrollt kiiktatva és futószalagon pecsételve le a biankó engedélyeket",
                "egy szép hivatalos levelet küldve a minisztériumból",
                "amikor a hivatalnokok kávészünetet tartanak délben"
            ], 0, ["c1-adv-unconstrained-wiretap-authorization-critique"]),
            match("vocabulary", "recognize", [
                ["Pegasus kémszoftver", "izraeli katonai kiberfegyver újságírók lehallgatására"],
                ["bírói kontroll hiánya", "a megfigyelések feletti független ellenőrzés hiánya Magyarországon"],
                ["dermesztő hatás", "a megfigyeléstől való félelem szülte öncenzúra a sajtóban"],
                ["PEGA-bizottság", "az Európai Parlament lehallgatásokat kivizsgáló különbizottsága"]
            ], [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A megfigyelés legsúlyosabb következménye a sajtó munkáját megbénító _____ . (chilling effect / dermesztő hatás)", "dermesztő hatás", "The most severe consequence of surveillance is the chilling effect paralyzing the press.", [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A telefonok törvénytelen feltörése az állami _____ példátlan esete. (cyber-espionage / kiberkémkedés)", "kiberkémkedés", "Unlawful hacking of phones is an unprecedented case of state cyber-espionage.", [f"c1-{slug}-vocab"]),
            fb("grammar", "recall", "A lépést állami bűncselekményként _____ a nemzetközi sajtó tiltakozott. (evaluating / értékelve)", "értékelve", "Evaluating the step as a state crime the international press protested.", ["c1-discourse-cyber-surveillance-scandal-framing"]),
            fb("grammar", "context", "Minél mélyebbre titkosítják az iratokat, _____ nyilvánvalóbb a hatalmi bűnrészesség. (the / annál)", "annál", "The deeper files are classified, the more obvious power complicity is.", ["c1-adv-proportional-cyber-secrecy-erosion"]),
            fb("grammar", "context", "A külső bírói engedélyezés értelemszerűen _____ a jogállamban. (indispensable / elengedhetetlen)", "elengedhetetlen", "External judicial authorization is naturally indispensable in a state governed by rule of law.", ["c1-adv-conclusive-digital-privacy-restitution"]),
            mc("grammar", "context", "Mi az újságírók legfőbb deontikus etikai kötelessége a titkosszolgálati lehallgatásokkal szemben?", [
                "Az informátorok anonimitásának feltétlen megvédése, a sajtótitok őrzése és a megfélemlítésnek való ellenállás.",
                "A telefonok átadása a rendőrségnek kérdés nélkül.",
                "A cikkek publikálásának leállítása a nyugalom érdekében."
            ], 0, ["c1-modal-deontic-journalistic-source-protection"]),
            sb("grammar", "produce", ["A", "digitális", "jogállam", "védelme", "fundamentálisan", "megdönthetetlen", "alapérték."], ["A", "digitális", "jogállam", "védelme", "fundamentálisan", "megdönthetetlen", "alapérték."], "Defense of the digital rule of law is a fundamentally unshakeable core value.", ["c1-adv-conclusive-digital-privacy-restitution"]),
            sw("production", [{"prompt": "Write a critical evaluation of secrecy vs. accountability using a proportional correlative structure.", "answer": "Minél agresszívabban próbálta a hatalom ötven évre titkosítani a Pegasus-megfigyelések iratait, annál egyértelműbbé vált az európai és a hazai nyilvánosság előtt a politikai visszaélések súlyossága és a független bírói kontroll elengedhetetlensége."}], ["c1-adv-proportional-cyber-secrecy-erosion"]),
            sw("production", [{"prompt": "Synthesize the restoration of digital privacy using an evaluative conclusive particle.", "answer": "A digitális jogállam megteremtése és a független bírói garanciák bevezetése értelemszerűen elengedhetetlen és fundamentálisan megdönthetetlen, hiszen a polgárok megfigyelésmentes szabadsága a demokratikus társadalom legfőbb fundamentuma."}], ["c1-adv-conclusive-digital-privacy-restitution"])
        ]
    )

    print("=== Finished C1 Unit 35 ===")


if __name__ == "__main__":
    generate_unit_35()
