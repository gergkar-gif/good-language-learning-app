"""
Hungarian B2 Core Track Unit 33:
  b2-33: Political Philosophy, Freedom & Historical Hysteria
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2_ex_helpers import mc, match, fb, sb, dc, sw

UNIT_33 = {
    "unit_num": 33,
    "title": "Political Philosophy, Freedom & Historical Hysteria",
    "grammar_summary": "Cleft identificational clauses and emphatic focus (az nem más, mint; éppen az, ami) and complex formal causal syntagms (abból adódóan, hogy; annak tulajdoníthatóan, hogy).",
    "grammar_skill": "b2-cleft-identification",
    "vocab_skill": "b2-33-vocab",
    "theme": "Political philosophy, freedom and historical hysteria",
    "intro_body": [
        "A politikai filozófia és az eszmetörténet legfontosabb kérdései a hatalom természetét, a szabadság intézményes garanciáit és a társadalmi fejlődés válságait vizsgálják. A 20. századi magyar gondolkodás egyik legnagyobb alakja, Bibó István páratlan mélységgel tárta fel a közép- és kelet-európai nemzetek kollektív félelmeit és a politikai hisztéria mechanizmusát.",
        "Ebben a fejezetben elsajátíthatja a filozófiai és akadémiai esszéstílus meghatározó szerkezeteit: a kiemelő azonosító mondatokat (az nem más, mint; éppen az, ami), az elvont oksági kapcsolatokat kifejező szintagmákat (abból adódóan, hogy; annak tulajdoníthatóan, hogy), valamint a jogállamiság, a demokratikus legitimitás, a bűnbakképzés és a fogalmi tisztázás B2-es szintű szókincsét.",
    ],
    "classic_story": {
        "slug": "kisallamoknyomorusage",
        "author": "Bibó István",
        "work": "A kelet-európai kisállamok nyomorúsága (1946)",
        "title": "Félelem, illúziók és a politikai hisztéria természete",
        "summary": "Bibó István és a vitapartner gondolkodó a közép- és kelet-európai nemzetek kollektív félelmeiről, a politikai hisztéria öngerjesztő mechanizmusáról és a demokratikus felelősségvállalás szükségességéről vitáznak a háború utáni romos Budapesten.",
        "characters": ["Bibó István", "A gondolkodó"],
        "paragraphs": [
            {
                "type": "narration",
                "text": "1946 borongós őszén, a háború utáni Budapest romos könyvtárszobájában Bibó István kéziratlapokat rendezgetett az íróasztalán. A kelet-európai történelem tragédiái, a határok folytonos változása és a nemzeti sérelmek terhe nehezedett a városra; Bibó a romok között a politikai gondolkodás tiszta erkölcsi alapjait kereste.",
            },
            {
                "type": "dialogue",
                "speaker": "A gondolkodó",
                "text": "István, sokan úgy vélik, hogy régiónk nyomorúsága a nagyhatalmak önzéséből és a balszerencsés földrajzi elhelyezkedésből fakad. Valóban ez volna a legfőbb magyarázat a történelmi kudarcainkra?",
            },
            {
                "type": "dialogue",
                "speaker": "Bibó István",
                "text": "Ez a magyarázat nem más, mint kényelmes önbecsapás. A kelet-európai népek alapvető tragédiája abból adódik, hogy az egzisztenciális félelem – a nemzethalál és a területvesztés rémképe – megbénította a józan valóságérzéket, és utat nyitott a politikai hisztériának.",
            },
            {
                "type": "narration",
                "text": "A vitapartner felállt, és a Dunára néző repedezett ablakhoz lépett. Felidézte a két világháború közötti évtizedek csalóka mítoszait: hogyan sodródott a társadalom a bűnbakképzés és az illúziók hálójába, miközben a valódi társadalmi reformok elmaradtak.",
            },
            {
                "type": "dialogue",
                "speaker": "A gondolkodó",
                "text": "De vajon hogyan lehet megkülönböztetni a valós veszélyeket a hisztérikus képzelgésektől? A politikai vezetők gyakran éppen a nemzet védelmére hivatkozva csorbítják a szabadságjogokat.",
            },
            {
                "type": "dialogue",
                "speaker": "Bibó István",
                "text": "Éppen az a valódi demokrata ismertetőjele, hogy nem fél. A félelem az, ami a tekintélyelvű kísértést táplálja; a demokrácia lényege viszont nem más, mint a fékek és egyensúlyok tisztelete, a jogállamiság és az állampolgári elszámoltathatóság.",
            },
            {
                "type": "narration",
                "text": "A délutáni fények megvilágították a sárguló könyvgerinceket. Bibó gondolatai kristálytiszta logikával metszették át a történelmi dogmákat; tudta, hogy a szabadság nem adottság, hanem mindennapi intellektuális és erkölcsi erőfeszítés, amely megköveteli a szembenézést a tényekkel.",
            },
            {
                "type": "narration",
                "text": "A beszélgetés végén csend telepedett a szobára. Mindketten érezték, hogy e sorok túlmutatnak az adott kor politikai válságán: a hisztéria elutasítása és az emberi szabadság feltétlen védelme örök érvényű iránytű maradt a közép-európai gondolkodás történetében.",
            },
        ],
        "reading_questions": [
            {
                "question": "Mi a kelet-európai népek nyomorúságának legfőbb belső oka Bibó István szerint?",
                "options": [
                    "Az egzisztenciális félelem, amely megbénítja a józan valóságérzéket és politikai hisztériát gerjeszt.",
                    "Kizárólag az ipari nyersanyagok és a termékeny termőföldek hiánya a Kárpát-medencében.",
                    "A külföldi utazási tilalmak és a diplomáciai kapcsolatok teljes hiánya.",
                ],
                "correct": 0,
            },
            {
                "question": "Hogyan határozza meg Bibó a valódi demokratát a dialógusban?",
                "options": [
                    "A demokrata legfőbb ismertetőjele az, hogy nem fél, és nem enged a tekintélyelvű kísértésnek.",
                    "Az a demokrata, aki minden választáson más pártra szavaz a változatosság kedvéért.",
                    "Az a személy, aki kizárólag a nagyhatalmak utasításait hajtja végre bírálat nélkül.",
                ],
                "correct": 0,
            },
            {
                "question": "Milyen következményekkel jár a bűnbakképzés és az illúziók hajszolása a társadalomban?",
                "options": [
                    "Önbecsapáshoz vezet, eltorzítja a valóságérzéket, és elodázza a szükséges társadalmi reformokat.",
                    "Azonnal fellendíti a nemzetközi kereskedelmet és a gazdasági növekedést.",
                    "Segít megerősíteni a szomszédos államokkal való harmonikus együttműködést.",
                ],
                "correct": 0,
            },
        ],
    },
    "lessons": [
        # Lesson 1
        {
            "num": 1,
            "title": "Cleft Identification and Emphatic Focus (az nem más, mint; éppen az, ami)",
            "grammar_label": "Cleft sentences and identificational focal structures (az nem más, mint; éppen az, ami)",
            "goals": [
                "I can construct emphatic cleft identification sentences using the formula az nem más, mint ...",
                "I can single out essential attributes and definitions with éppen az, ami ...",
                "I can deploy contrastive cleft structures to clarify philosophical propositions",
            ],
            "grammar_doc": {
                "slug": "cleft-identification-emphatic-focus",
                "title": "Cleft Identification and Emphatic Focus: az nem más, mint & éppen az, ami",
                "text1_title": "Identificational Cleft Constructions in Hungarian Prose",
                "text1": "In Hungarian academic, essayistic, and philosophical argumentation, complex ideas are frequently distilled through identificational cleft structures (azonosító kiemelő mondatok). Instead of a plain subject-predicate statement ('A szabadság a felelősség vállalása'), Hungarian foregrounds the demonstrative pronoun 'az' followed by the restrictive formula 'nem más, mint' (is none other than / is nothing other than): 'A szabadság az nem más, mint a személyes felelősség vállalása'.",
                "text2_title": "Precise Focus with 'éppen az, ami'",
                "text2": "When isolating an exact determining factor or distinguishing attribute, 'éppen az, ami' (precisely that which / the very thing that) is employed. This structure focuses attention exclusively on the crucial condition: 'Éppen az a garancia hiányzik, ami a hatalom korlátozásához szükséges' (Precisely that guarantee is missing which is necessary for constraining power). These cleft devices sharpen contrastive claims: 'Nem az a kérdés, hogy ..., hanem az, hogy ...' (The question is not whether ..., but rather that ...).",
                "table_title": "Core Cleft and Identificational Formulas",
                "table_rows": [
                    ["az nem más, mint ...", "A valódi szabadság nem más, mint félelemmentes cselekvés. (Is none other than... )"],
                    ["éppen az, ami ...", "Éppen az a felelősségtudat hiányzik, ami a demokráciát élteti. (Precisely that which... )"],
                    ["nem az ..., hanem az ...", "Nem az a lényeg, ki van hatalmon, hanem az, hogy korlátozott-e. (Not who, but... )"],
                    ["az az igazi ..., amely ...", "Az az igazi veszély, amely észrevétlenül bontja le a jogállamot. (The true danger is... )"],
                ],
                "examples": [
                    {
                        "spanish": "Bibó szerint a politikai hisztéria nem más, mint a valósággal való szembenézés képtelensége.",
                        "english": "According to Bibó, political hysteria is none other than the inability to face reality.",
                    },
                    {
                        "spanish": "Éppen az a kritikus gondolkodás hiányzott a korszakból, ami megelőzhette volna a társadalmi katasztrófát.",
                        "english": "Precisely that critical thinking was missing from the era which could have prevented the social catastrophe.",
                    },
                    {
                        "spanish": "A vita során nem az volt a döntő kérdés, hogy ki vezeti az intézményt, hanem az, hogy megmarad-e a függetlensége.",
                        "english": "During the debate, the decisive question was not who heads the institution, but whether its independence is preserved.",
                    },
                    {
                        "spanish": "Az igazi bátorság az nem más, mint a tények elismerése a kényelmes illúziókkal szemben.",
                        "english": "True courage is none other than the acknowledgment of facts in opposition to comforting illusions.",
                    },
                ],
                "tip": "In 'az nem más, mint...', always remember that 'mint' takes the same case as the preceding noun or pronoun: 'Ez nem másról szól, mint a szabadságról' (This is about nothing other than freedom).",
            },
            "words": [
                {"lemma": "nem más, mint", "translation": "none other than / nothing other than", "pos": "expression"},
                {"lemma": "éppen az", "translation": "precisely that / the very thing", "pos": "expression"},
                {"lemma": "lényegi", "translation": "essential / fundamental", "pos": "adjective"},
                {"lemma": "meghatározó", "translation": "defining / decisive", "pos": "adjective"},
                {"lemma": "félreértés", "translation": "misunderstanding / misconception", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What role does the formula 'nem más, mint' play in philosophical argumentation?",
                        [
                            "it identifies and equates an abstract concept with its essential definition",
                            "it expresses total numerical doubt about statistical figures",
                            "it concludes a casual greeting at the beginning of an informal phone call",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective means essential, core, or touching the deepest nature of a subject?",
                        ["lényegi", "másodlagos", "jelentéktelen"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["nem más, mint", "none other than"],
                            ["éppen az", "precisely that / the very thing"],
                            ["lényegi", "essential / fundamental"],
                            ["meghatározó", "defining / decisive"],
                            ["félreértés", "misunderstanding"],
                        ],
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence uses a cleft identificational structure with 'nem más, mint' correctly?",
                        [
                            "A demokrácia lényege az nem más, mint a polgári szabadság védelme.",
                            "A demokrácia lényege az nem más, hogy a polgári szabadság védelme.",
                            "A demokrácia lényege az nem más, mint ha polgári szabadság védelme.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence demonstrating focal cleft emphasis with 'éppen az':",
                        [
                            "Éppen az a valóságérzék hiányzik belőle, ami a felelős döntésekhez szükséges.",
                            "Éppen az a valóságérzék hiányzik belőle, mert a felelős döntésekhez szükséges.",
                            "Éppen az a valóságérzék hiányzik belőle, ha a felelős döntésekhez szükséges.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A filozófus szerint a zsarnokság az nem más, ____ az intézményesített félelem. (than)",
                        "mint",
                        "According to the philosopher, tyranny is nothing other than institutionalized fear.",
                        ["b2-cleft-identification"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Az igazi kérdés nem az, hogy mit ígérnek a vezetők, ____ az, hogy számonkérhetőek-e a döntéseik. (but rather)",
                        "hanem",
                        "The real question is not what leaders promise, but rather whether their decisions are accountable.",
                        ["b2-cleft-identification"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["Éppen", "az", "a", "bizalom", "veszett", "el,", "ami", "a", "társadalmi", "békét", "őrizte."],
                        ["Éppen", "az", "a", "bizalom", "veszett", "el,", "ami", "a", "társadalmi", "békét", "őrizte."],
                        "Precisely that trust was lost which preserved social peace.",
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A politikai vita során súlyos ____ keletkezett a hatalmi ágak elválasztásának fogalmát illetően. (misunderstanding)",
                        "félreértés",
                        "During the political debate a serious misunderstanding arose concerning the concept of separation of powers.",
                        ["b2-33-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "történelmi", "tapasztalat", "meghatározó", "szerepet", "játszik", "a", "kollektív", "tudatban."],
                        ["A", "történelmi", "tapasztalat", "meghatározó", "szerepet", "játszik", "a", "kollektív", "tudatban."],
                        "Historical experience plays a decisive role in the collective consciousness.",
                        ["b2-33-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Filozófushallgató", "text": "Hogyan határozná meg a modern jogállam lényegi tartalmát?"},
                            {"speaker": "Professzor", "text": "____"},
                        ],
                        [
                            "A jogállam az nem más, mint a hatalom önkényének korlátozása az egyén elidegeníthetetlen szabadságjogai javára.",
                            "A jogállam egy olyan épület a belvárosban, ahová tilos belépni hétvégén.",
                            "Kizárólag az uralkodó személyes akaratának feltétlen végrehajtását jelenti.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutató", "text": "Miért vallottak kudarcot a reformkísérletek a 20. század közepén?"},
                            {"speaker": "Politológus", "text": "____"},
                        ],
                        [
                            "Éppen az a társadalmi konszenzus hiányzott a döntéshozók mögül, ami nélkülözhetetlen lett volna az átalakuláshoz.",
                            "Mert a reformokhoz túl sok papírt kellett volna kinyomtatni a nyomdákban.",
                            "A kudarc oka az volt, hogy senki sem szeretett reggel korán felkelni.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a philosophical statement using the cleft identification formula 'az nem más, mint...'.",
                                "answer": "A valódi társadalmi fejlődés az nem más, mint az egyéni autonómia és a közösségi szolidaritás harmonikus kiteljesedése.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'éppen az, ami' to highlight an institutional safeguard.",
                                "answer": "A független bíróságok léte éppen az az intézményi fék, ami megakadályozza a politikai önkény elhatalmasodását.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A diktatúra lényege az nem más, mint a polgárok mindennapi életének teljes ____. (control / surveillance)",
                        "ellenőrzése",
                        "The essence of dictatorship is none other than the total surveillance of citizens' everyday lives.",
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which adjective describes an indispensable, foundational attribute of an idea?",
                        ["lényegi", "mellékes", "felszínes"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
            },
        },
        # Lesson 2
        {
            "num": 2,
            "title": "Abstract Causal Syntagms (abból adódóan, hogy; annak tulajdoníthatóan, hogy)",
            "grammar_label": "Complex formal causal constructions in academic argumentation (abból adódóan, hogy; annak tulajdoníthatóan, hogy)",
            "goals": [
                "I can express sophisticated causal deductions using abból adódóan, hogy ...",
                "I can attribute historical or political phenomena using annak tulajdoníthatóan, hogy ...",
                "I can analyze causal chains with complex academic connective syntagms",
            ],
            "grammar_doc": {
                "slug": "abstract-causal-syntagms-argumentation",
                "title": "Abstract Causal Syntagms: abból adódóan, hogy & annak tulajdoníthatóan, hogy",
                "text1_title": "Elevating Causal Links in Academic Prose",
                "text1": "While conversational Hungarian relies on simple causal conjunctions like 'mert' (because) or 'mivel' (since), formal political philosophy, historiography, and academic essays demand complex causal syntagms (elvont okhatározói szintagmák). These syntagms incorporate demonstrative pronouns in oblique cases combined with participles: 'abból adódóan, hogy...' (arising from the fact that...) and 'annak tulajdoníthatóan, hogy...' (attributable to the fact that...).",
                "text2_title": "Distinguishing Causation, Consequence, and Attribution",
                "text2": "'Abból adódóan, hogy...' stresses the structural or logical emergence of an outcome from an inherent circumstance. 'Annak tulajdoníthatóan, hogy...' focuses on attribution and explanatory responsibility, often indicating why a positive or negative development took place. Other essential formal causal phrases include 'annak következtében, hogy...' (as a consequence of...) and 'abból kiindulva, hogy...' (proceeding from the premise that...).",
                "table_title": "Formal Causal Syntagms",
                "table_rows": [
                    ["abból adódóan, hogy ...", "Abból adódóan, hogy hiányzott a bizalom, a tárgyalások megfeneklettek. (Arising from... )"],
                    ["annak tulajdoníthatóan, hogy ...", "Annak tulajdoníthatóan maradt fenn a béke, hogy kompromisszum született. (Attributable to... )"],
                    ["annak következtében, hogy ...", "Annak következtében vesztettek teret, hogy elzárkóztak a reformoktól. (In consequence of... )"],
                    ["abból kiindulva, hogy ...", "Abból kiindulva alkottak törvényt, hogy az egyén alapvetően szabad. (Proceeding from... )"],
                ],
                "examples": [
                    {
                        "spanish": "A térség politikai instabilitása nagyrészt abból adódott, hogy a határok kijelölésekor figyelmen kívül hagyták a helyi realitásokat.",
                        "english": "The political instability of the region largely arose from the fact that when demarcating borders local realities were ignored.",
                    },
                    {
                        "spanish": "A demokratikus átmenet békés jellege annak volt tulajdonítható, hogy a felek készek voltak a folyamatos dialógusra.",
                        "english": "The peaceful character of the democratic transition was attributable to the fact that the parties were ready for continuous dialogue.",
                    },
                    {
                        "spanish": "Annak következtében, hogy a sajtószabadságot korlátozták, a társadalmi kontroll szinte teljesen megszűnt a végrehajtó hatalom felett.",
                        "english": "As a consequence of the restriction of freedom of the press, social control over executive power ceased almost completely.",
                    },
                    {
                        "spanish": "A szerző abból a felismerésből kiindulva érvel, hogy a félelem a politikai hisztéria legfőbb táptalaja.",
                        "english": "The author argues proceeding from the insight that fear is the primary breeding ground of political hysteria.",
                    },
                ],
                "tip": "Pay close attention to case government: 'adódik' governs the elative (abból adódóan), whereas 'tulajdonítható' governs the dative (annak tulajdoníthatóan).",
            },
            "words": [
                {"lemma": "abból adódóan", "translation": "arising from the fact that / as a result of", "pos": "expression"},
                {"lemma": "annak tulajdoníthatóan", "translation": "attributable to the fact that", "pos": "expression"},
                {"lemma": "következtében", "translation": "as a consequence of", "pos": "postposition"},
                {"lemma": "oksági kapcsolat", "translation": "causal link / relationship", "pos": "expression"},
                {"lemma": "előfeltétel", "translation": "prerequisite / precondition", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which formal syntagm expresses that a result logically arises from a pre-existing fact?",
                        ["abból adódóan", "anélkül hogy", "olyannyira"],
                        0,
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is an 'előfeltétel' in philosophical and constitutional logic?",
                        [
                            "a necessary prerequisite or prior condition required before something can occur",
                            "a sudden retrospective cancellation of an existing treaty",
                            "an informal recommendation without any binding force",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["abból adódóan", "arising from the fact that"],
                            ["annak tulajdoníthatóan", "attributable to the fact that"],
                            ["következtében", "as a consequence of"],
                            ["oksági kapcsolat", "causal link"],
                            ["előfeltétel", "prerequisite / precondition"],
                        ],
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which case pronoun is governed by 'adódóan' in formal causal sentences?",
                        ["abból", "annak", "azzal"],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence correctly applying 'annak tulajdoníthatóan, hogy...':",
                        [
                            "A stabilitás annak volt tulajdonítható, hogy tiszteletben tartották az alkotmányt.",
                            "A stabilitás abból volt tulajdonítható, hogy tiszteletben tartották az alkotmányt.",
                            "A stabilitás azzal volt tulajdonítható, hogy tiszteletben tartották az alkotmányt.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A válság nagyrészt ____ adódóan alakult ki, hogy elodázták a gazdasági reformokat. (from that)",
                        "abból",
                        "The crisis developed largely arising from the fact that they postponed economic reforms.",
                        ["b2-cleft-identification"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A békés megállapodás ____ volt tulajdonítható, hogy a felek képesek voltak a kölcsönös engedményekre. (to that)",
                        "annak",
                        "The peaceful agreement was attributable to the fact that the parties were capable of mutual concessions.",
                        ["b2-cleft-identification"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "politikai", "hisztéria", "a", "félelem", "túlzott", "mértékéből", "adódott."],
                        ["A", "politikai", "hisztéria", "a", "félelem", "túlzott", "mértékéből", "adódott."],
                        "Political hysteria arose from the excessive degree of fear.",
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A jogállamiság működésének elengedhetetlen ____ a hatalmi ágak szigorú szétválasztása. (prerequisite)",
                        "előfeltétele",
                        "An indispensable prerequisite for the functioning of the rule of law is the strict separation of powers.",
                        ["b2-33-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "tanulmány", "világos", "oksági", "kapcsolatot", "mutatott", "ki", "a", "két", "jelenség", "között."],
                        ["A", "tanulmány", "világos", "oksági", "kapcsolatot", "mutatott", "ki", "a", "két", "jelenség", "között."],
                        "The study demonstrated a clear causal relationship between the two phenomena.",
                        ["b2-33-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi hallgató", "text": "Miből fakadt Bibó szerint a kelet-európai demokráciák törékenysége?"},
                            {"speaker": "Politikaelmélet-oktató", "text": "____"},
                        ],
                        [
                            "Főként abból adódóan, hogy a nemzeti egzisztenciát fenyegető félelmek miatt a társadalmak a szabadság helyett a tekintélyelvű vezetést választották.",
                            "Kizárólag abból adódóan, hogy nem volt elég kávéház a fővárosokban.",
                            "A törékenység annak volt tulajdonítható, hogy a parlamentben mindenki csak verseket szavalt.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Történész", "text": "Hogyan bizonyítható az oksági kapcsolat a gazdasági válság és a radikalizálódás között?"},
                            {"speaker": "Szociológus", "text": "____"},
                        ],
                        [
                            "Annak következtében, hogy a középosztály elveszítette megtakarításait, megnőtt a fogékonyság a demagóg ígéretek iránt.",
                            "Semmilyen oksági kapcsolat nincs, mert a történelemben minden puszta véletlen.",
                            "A radikalizálódás annak tulajdonítható, hogy megváltozott az időjárás a tavaszi hónapokban.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an academic causal sentence using 'abból adódóan, hogy...'.",
                                "answer": "A politikai polarizáció mélyülése abból adódott, hogy a szemben álló felek elutasították az érdemi társadalmi párbeszédet.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence using 'annak tulajdoníthatóan, hogy...' to explain institutional stability.",
                                "answer": "A demokratikus intézmények stabilitása annak volt tulajdonítható, hogy a jogállami fékek és egyensúlyok hatékonyan működtek.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A társadalmi feszültség enyhülése nagyrészt annak volt ____, hogy a kormány megnyitotta a tárgyalásokat. (attributable)",
                        "tulajdonítható",
                        "The easing of social tension was largely attributable to the fact that the government opened negotiations.",
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes the logical link connecting a cause directly to its inevitable effect?",
                        ["oksági kapcsolat", "személyi kultusz", "véletlen egybeesés"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
            },
        },
        # Lesson 3
        {
            "num": 3,
            "title": "The Psychology of Fear in Politics",
            "grammar_label": "Analyzing fear-driven politics, authoritarian traps, and democratic maturity (politikai hisztéria, valóságérzék, bűnbakképzés)",
            "goals": [
                "I can analyze Bibó István's diagnosis of collective fear and political hysteria in Central Europe",
                "I can evaluate psychological defense mechanisms in political discourse (bűnbakképzés, önbecsapás)",
                "I can discuss how existential anxiety undermines rational political judgment and reality sense",
            ],
            "grammar_doc": {
                "slug": "psychology-fear-political-hysteria",
                "title": "Bibó István: The Psychology of Fear and Political Hysteria",
                "text1_title": "The Mechanism of Political Hysteria",
                "text1": "In his seminal 1946 essay 'A kelet-európai kisállamok nyomorúsága', Bibó István diagnosed the central pathology of Central European public life as 'politikai hisztéria'. When a community suffers traumatic historic defeats or fears territorial extinction, its collective 'valóságérzék' (sense of reality) becomes severely compromised. Unable to bear real dilemmas, the community escapes into illusions, grandiosity, and profound 'önbecsapás' (self-deception).",
                "text2_title": "Scapegoating and the Authoritarian Reflex",
                "text2": "The inevitable symptom of hysterical politics is 'bűnbakképzés' (scapegoating): attributing complex internal failures entirely to external conspiracies or domestic minorities. The hysterical community constructs 'téveszmék' (delusions) that justify authoritarian centralization in the name of national defense. Overcoming this requires democratic maturity: the courage to discard historical victimhood and accept ethical agency.",
                "table_title": "Key Concepts in Bibó's Political Psychology",
                "table_rows": [
                    ["politikai hisztéria", "A politikai hisztéria megbénítja a józan kompromisszumkeresést. (Political hysteria.)"],
                    ["valóságérzék", "A félelem eltorzítja a nemzet egészséges valóságérzékét. (Sense of reality.)"],
                    ["bűnbakképzés", "A bűnbakképzés eltereli a figyelmet a valódi társadalmi bajokról. (Scapegoating.)"],
                    ["önbecsapás", "A dicső múlt mítosza kényelmes önbecsapássá vált. (Self-deception.)"],
                ],
                "examples": [
                    {
                        "spanish": "Bibó szerint a politikai hisztéria az a lelkiállapot, amelyben a félelem felülírja az erkölcsi gátlásokat és a józan észt.",
                        "english": "According to Bibó, political hysteria is the state of mind in which fear overrides moral inhibitions and common sense.",
                    },
                    {
                        "spanish": "A bűnbakképzés veszélyes mechanizmusa abból adódik, hogy a felelősséget kizárólag külső ellenségekre hárítja.",
                        "english": "The dangerous mechanism of scapegoating arises from the fact that it shifts responsibility exclusively onto external enemies.",
                    },
                    {
                        "spanish": "A valóságérzék elvesztése az nem más, mint a hisztérikus politikai vezetés legsúlyosabb következménye.",
                        "english": "The loss of the sense of reality is none other than the gravest consequence of hysterical political leadership.",
                    },
                    {
                        "spanish": "Az önbecsapás téveszméi évtizedeken át akadályozták a szomszédos népekkel való megbékélést.",
                        "english": "The delusions of self-deception prevented reconciliation with neighboring nations for decades.",
                    },
                ],
                "tip": "'Hisztéria' in political philosophy refers not to individual emotional volatility, but to a structural, collective pathology of public discourse where rational evaluation of threats is replaced by existential panic.",
            },
            "words": [
                {"lemma": "politikai hisztéria", "translation": "political hysteria", "pos": "expression"},
                {"lemma": "valóságérzék", "translation": "sense of reality", "pos": "noun"},
                {"lemma": "bűnbakképzés", "translation": "scapegoating", "pos": "noun"},
                {"lemma": "önbecsapás", "translation": "self-deception", "pos": "noun"},
                {"lemma": "téveszme", "translation": "delusion / false belief", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "How does Bibó István define 'politikai hisztéria'?",
                        [
                            "a collective pathology where existential fear distorts reality and leads to irrational politics",
                            "a loud argument between parliamentary delegates during a budget debate",
                            "a sudden psychological illness affecting solely military officers",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which term denotes blaming an innocent group or minority for systemic national failures?",
                        ["bűnbakképzés", "önkritika", "jogállamiság"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["politikai hisztéria", "political hysteria"],
                            ["valóságérzék", "sense of reality"],
                            ["bűnbakképzés", "scapegoating"],
                            ["önbecsapás", "self-deception"],
                            ["téveszme", "delusion / false belief"],
                        ],
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence using cleft identification to define political scapegoating:",
                        [
                            "A bűnbakképzés az nem más, mint a saját mulasztások másokra hárítása.",
                            "A bűnbakképzés az nem más hogy saját mulasztások hárítása.",
                            "A bűnbakképzés az nem más mint ha mulasztásokat hárítanánk.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence uses formal causal syntagms to explain the loss of reality sense?",
                        [
                            "A valóságérzék elvesztése abból adódott, hogy a társadalom elmenekült a szembenézés elől.",
                            "A valóságérzék elvesztése azzal adódott hogy a társadalom elmenekült.",
                            "A valóságérzék elvesztése annak adódott hogy a társadalom elmenekült.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Éppen az a józan ____ hiányzik a közéletből, ami megelőzhetné a téveszmék terjedését. (sense of reality)",
                        "valóságérzék",
                        "Precisely that sober sense of reality is missing from public life which could prevent the spread of delusions.",
                        ["b2-cleft-identification"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A politikai hisztéria mechanizmusa az nem más, mint a kollektív félelmek tudatos ____. (manipulation / exploitation)",
                        "kihasználása",
                        "The mechanism of political hysteria is none other than the conscious exploitation of collective fears.",
                        ["b2-cleft-identification"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "nemzeti", "önbecsapás", "megakadályozta", "a", "történelmi", "szembenézést."],
                        ["A", "nemzeti", "önbecsapás", "megakadályozta", "a", "történelmi", "szembenézést."],
                        "National self-deception prevented the historical confrontation with facts.",
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A propaganda veszélyes ____ ringatta a lakosságot ahelyett, hogy felkészítette volna a valóságra. (delusions)",
                        "téveszmékbe",
                        "The propaganda lulled the population into dangerous delusions instead of preparing them for reality.",
                        ["b2-33-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "politikai", "hisztéria", "állapotában", "a", "félelem", "felülírja", "az", "erkölcsi", "gátlásokat."],
                        ["A", "politikai", "hisztéria", "állapotában", "a", "félelem", "felülírja", "az", "erkölcsi", "gátlásokat."],
                        "In a state of political hysteria fear overrides moral inhibitions.",
                        ["b2-33-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Egyetemi hallgató", "text": "Hogyan lehet kigyógyítani egy társadalmat a politikai hisztériából Bibó szerint?"},
                            {"speaker": "Politikaelmélet-kutató", "text": "____"},
                        ],
                        [
                            "A gyógyulás az nem más, mint a félelem leküzdése, a józan valóságérzék visszaszerzése és a téveszmék bátor elvetése.",
                            "Újabb háborúkat kell indítani, hogy a társadalom elfelejtse a korábbi sérelmeit.",
                            "Be kell tiltani minden könyvolvasást és történelmi vitát az egyetemeken.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Újságíró", "text": "Miért olyan vonzó a politikai vezetés számára a bűnbakképzés módszere?"},
                            {"speaker": "Szociológus", "text": "____"},
                        ],
                        [
                            "Főként abból adódóan, hogy azonnali és egyszerű ellenségképet kínál, felmentve a hatalmat a saját hibáiért viselt felelősség alól.",
                            "Mert a törvények kötelezik a kormányokat arra, hogy bűnbakokat keressenek havonta.",
                            "A bűnbakképzés valójában a legtisztább demokratikus eljárás a világon.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence analyzing 'önbecsapás' using the cleft formula 'az nem más, mint...'.",
                                "answer": "A politikai önbecsapás az nem más, mint kényelmes menekülés a történelmi felelősségvállalás és a valóság elől.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an argumentative sentence explaining the root of 'politikai hisztéria' using 'abból adódóan, hogy...'.",
                                "answer": "A politikai hisztéria elhatalmasodása abból adódott, hogy az egzisztenciális félelem eltorzította a társadalom józan valóságérzékét.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Éppen az a kritikus gondolkodás az, ____ megvédheti a közösséget a demagóg téveszméktől. (which / that)",
                        "ami",
                        "Precisely that critical thinking is that which can protect the community from demagogic delusions.",
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes systematic self-delusion where reality is ignored in favor of comforting lies?",
                        ["önbecsapás", "önismeret", "jogállam"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
            },
        },
        # Lesson 4
        {
            "num": 4,
            "title": "Democratic Legitimacy vs. Authoritarian Temptation",
            "grammar_label": "Institutional checks and balances, political responsibility (demokratikus legitimitás, fékek és egyensúlyok, jogállamiság)",
            "goals": [
                "I can evaluate the foundations of democratic legitimacy and institutional checks and balances",
                "I can critique authoritarian temptations and populist shortcuts in constitutional governance",
                "I can articulate principles of institutional accountability (elszámoltathatóság) and rule of law",
            ],
            "grammar_doc": {
                "slug": "democratic-legitimacy-authoritarian-temptation",
                "title": "Democratic Legitimacy vs. Authoritarian Temptation",
                "text1_title": "The Institutional Architecture of Freedom",
                "text1": "Political philosophy distinguishes between raw electoral victory and genuine 'demokratikus legitimitás' (democratic legitimacy). A democracy is not merely majority rule; its legitimacy rests on the inviolability of human rights and the functioning of 'fékek és egyensúlyok' (checks and balances). Independent constitutional courts, media pluralism, and competitive parliamentary oversight constitute the safeguards of 'jogállamiság' (rule of law).",
                "text2_title": "The Authoritarian Temptation in Times of Crisis",
                "text2": "In times of severe socioeconomic crisis, societies face the 'tekintélyelvű' (authoritarian) temptation: the illusory promise that a decisive, unconstrained leader can resolve complex problems faster by bypassing constitutional procedures. Cleft constructions underline that genuine stability stems not from autocracy, but from 'elszámoltathatóság' (accountability): 'Az nem más, mint a jogállam garanciája, hogy senki sem áll a törvények felett' (It is none other than the guarantee of the rule of law that no one is above the law).",
                "table_title": "Constitutional and Philosophical Concepts",
                "table_rows": [
                    ["legitimitás", "A hatalom valódi legitimitása a törvények tiszteletéből fakad. (Democratic legitimacy.)"],
                    ["fékek és egyensúlyok", "A fékek és egyensúlyok rendszere megakadályozza a túlhatalmat. (Checks and balances.)"],
                    ["tekintélyelvű", "A tekintélyelvű rendszerek elnyomják az autonóm intézményeket. (Authoritarian.)"],
                    ["jogállamiság", "A jogállamiság csorbítása veszélyezteti az állampolgári jogokat. (Rule of law.)"],
                ],
                "examples": [
                    {
                        "spanish": "A demokratikus intézmények stabilitása abból adódik, hogy a hatalommegosztás elve érvényesül a gyakorlatban.",
                        "english": "The stability of democratic institutions arises from the fact that the principle of separation of powers prevails in practice.",
                    },
                    {
                        "spanish": "Éppen az a fékek és egyensúlyok rendszere védi meg a polgárokat, amit a tekintélyelvű kísértés le akar bontani.",
                        "english": "Precisely that system of checks and balances protects the citizens which the authoritarian temptation seeks to dismantle.",
                    },
                    {
                        "spanish": "A jogállamiság lényege az nem más, mint az intézmények kiszámíthatósága és az elszámoltathatóság garanciája.",
                        "english": "The essence of the rule of law is none other than the predictability of institutions and the guarantee of accountability.",
                    },
                    {
                        "spanish": "A kormányzat legitimitásának meggyengülése annak volt tulajdonítható, hogy figyelmen kívül hagyták az alkotmányos normákat.",
                        "english": "The weakening of the government's legitimacy was attributable to the fact that they ignored constitutional norms.",
                    },
                ],
                "tip": "Distinguish between 'tekintély' (earned moral authority / prestige) and 'tekintélyelvű' (authoritarian, imposing obedience through power and suppressing debate).",
            },
            "words": [
                {"lemma": "legitimitás", "translation": "legitimacy", "pos": "noun"},
                {"lemma": "fékek és egyensúlyok", "translation": "checks and balances", "pos": "expression"},
                {"lemma": "tekintélyelvű", "translation": "authoritarian", "pos": "adjective"},
                {"lemma": "jogállamiság", "translation": "rule of law", "pos": "noun"},
                {"lemma": "elszámoltathatóság", "translation": "accountability", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "What does 'fékek és egyensúlyok' refer to in constitutional theory?",
                        [
                            "the system of institutional separation of powers preventing any single branch from dominating",
                            "the mechanical maintenance manual of emergency vehicles",
                            "the balancing of state budget debts through currency devaluation",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "Which adjective describes governance based on unquestioned hierarchy and suppression of dissent?",
                        ["tekintélyelvű", "demokratikus", "pluralista"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["legitimitás", "legitimacy"],
                            ["fékek és egyensúlyok", "checks and balances"],
                            ["tekintélyelvű", "authoritarian"],
                            ["jogállamiság", "rule of law"],
                            ["elszámoltathatóság", "accountability"],
                        ],
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which sentence uses cleft identification to define the rule of law?",
                        [
                            "A jogállamiság az nem más, mint a törvény előtti teljes egyenlőség biztosítása.",
                            "A jogállamiság az nem más ha a törvény előtt mindenki egyenlő.",
                            "A jogállamiság az nem más mert a törvény előtt mindenki egyenlő.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence explaining authoritarian tendencies with formal causal syntagms:",
                        [
                            "A tekintélyelvű kísértés abból adódott, hogy a válságban gyors megoldásokat vártak a vezetőktől.",
                            "A tekintélyelvű kísértés azzal adódott hogy a válságban megoldásokat vártak.",
                            "A tekintélyelvű kísértés annak adódott hogy a válságban megoldásokat vártak.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "A demokratikus intézmények stabilitása ____ volt tulajdonítható, hogy a hatalommegosztás hatékonyan érvényesült. (to that)",
                        "annak",
                        "The stability of democratic institutions was attributable to the fact that the separation of powers prevailed effectively.",
                        ["b2-cleft-identification"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "Éppen az a független igazságszolgáltatás az, ____ garantálja az állampolgárok jogbiztonságát. (which / that)",
                        "ami",
                        "Precisely that independent judiciary is that which guarantees the legal certainty of citizens.",
                        ["b2-cleft-identification"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "demokratikus", "legitimitás", "alapja", "a", "szabad", "választások", "tisztasága."],
                        ["A", "demokratikus", "legitimitás", "alapja", "a", "szabad", "választások", "tisztasága."],
                        "The basis of democratic legitimacy is the integrity of free elections.",
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A modern közigazgatásban a vezetők nyilvános ____ megakadályozza a korrupció elterjedését. (accountability)",
                        "elszámoltathatósága",
                        "In modern public administration the public accountability of leaders prevents the spread of corruption.",
                        ["b2-33-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "fékek", "és", "egyensúlyok", "rendszere", "nélkülözhetetlen", "a", "jogállamban."],
                        ["A", "fékek", "és", "egyensúlyok", "rendszere", "nélkülözhetetlen", "a", "jogállamban."],
                        "The system of checks and balances is indispensable in a state governed by the rule of law.",
                        ["b2-33-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Alkotmányjogász", "text": "Miért elengedhetetlen a fékek és egyensúlyok rendszere egy érett demokráciában?"},
                            {"speaker": "Egyetemi dékán", "text": "____"},
                        ],
                        [
                            "Mert a hatalomkoncentráció megakadályozása az nem más, mint a polgári szabadságjogok megőrzésének legfőbb garanciája.",
                            "Csak azért, mert a képviselők szeretnek vitatkozni a parlament folyosóin.",
                            "A fékek és egyensúlyok tilosak a modern államokban, mert lelassítják a forgalmat.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Kutató", "text": "Hogyan alakulhat ki tekintélyelvű vezetés demokratikus választások után?"},
                            {"speaker": "Politikai elemző", "text": "____"},
                        ],
                        [
                            "Gyakran abból adódóan, hogy a választási győzelemre hivatkozva fokozatosan leépítik az intézményi elszámoltathatóságot és a fékeket.",
                            "Kizárólag akkor, ha a parlament épületét eladják egy külföldi befektetőnek.",
                            "A tekintélyelvűség magától megszűnik, ha senki sem néz televíziót.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a sentence defining 'jogállamiság' using 'az nem más, mint...'.",
                                "answer": "A jogállamiság az nem más, mint a hatalom alkotmányos korlátozottsága és a törvények mindenkire kötelező érvénye.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write a constitutional analysis using 'fékek és egyensúlyok' and 'elszámoltathatóság'.",
                                "answer": "A fékek és egyensúlyok rendszere biztosítja a kormányzati elszámoltathatóságot és megakadályozza a tekintélyelvű túlhatalmat.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "A tekintélyelvű rendszer veszélye az nem más, mint a polgári szabadságjogok fokozatos ____. (curtailment / restriction)",
                        "korlátozása",
                        "The danger of an authoritarian system is none other than the gradual restriction of civic liberties.",
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which term denotes institutional requirement for leaders to justify and take responsibility for actions?",
                        ["elszámoltathatóság", "titoktartás", "kiváltság"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
            },
        },
        # Lesson 5
        {
            "num": 5,
            "title": "Philosophical Argumentation and Conceptual Clarification",
            "grammar_label": "Constructing an argumentative philosophical essay (fogalmi tisztázás, érvelés, előfeltevés, szintézis)",
            "goals": [
                "I can write a structured philosophical exposition clarifying complex sociopolitical concepts",
                "I can dissect premises (előfeltevések) and deductive inferences in argumentative texts",
                "I can synthesize opposing philosophical perspectives into a coherent B2-level essay",
            ],
            "grammar_doc": {
                "slug": "philosophical-argumentation-conceptual-clarification",
                "title": "Philosophical Argumentation and Conceptual Clarification",
                "text1_title": "The Method of Conceptual Clarification",
                "text1": "Rigorous philosophical discourse begins with 'fogalmi tisztázás' (conceptual clarification). Many bitter public controversies arise not from genuine factual divergence, but from ambiguous terms used equivocally by opposing camps. Before constructing an argumentative position, the writer must explicitly define core categories, expose hidden 'előfeltevések' (presuppositions / axioms), and trace the logical coherence of the deduction.",
                "text2_title": "Structuring an Academic Philosophical Argument",
                "text2": "An analytical argument unfolds through distinct stages: the formulation of the thesis (tézis), the presentation of supporting evidence and causal chains (érvelés / gondolatmenet), the anticipation of counterarguments (ellenérvek cáfolata), and the higher-level synthesis ('szintézis'). Cleft identification clauses ('az nem más, mint...') formulate sharp definitional theses, while formal causal syntagms ('abból adódóan, hogy...') ground deduction.",
                "table_title": "Argumentative Philosophy Lexicon",
                "table_rows": [
                    ["fogalmi tisztázás", "A vita első lépése a fogalmi tisztázás volt. (Conceptual clarification.)"],
                    ["érvelés", "A logikus érvelés meggyőzte a hallgatóságot. (Argumentation / reasoning.)"],
                    ["előfeltevés", "Megkérdőjelezték a szerző rejtett előfeltevéseit. (Presupposition / premise.)"],
                    ["szintézis", "A tanulmány szintézist teremtett a két elmélet között. (Synthesis.)"],
                ],
                "examples": [
                    {
                        "spanish": "Az esszé szerzője alapos fogalmi tisztázással indított, hogy elkerülje a terminológiai félreértéseket.",
                        "english": "The author of the essay started with thorough conceptual clarification to avoid terminological misunderstandings.",
                    },
                    {
                        "spanish": "A filozófiai érvelés ereje abból adódik, hogy minden következtetés szigorúan levezethető az előfeltevésekből.",
                        "english": "The strength of philosophical argumentation arises from the fact that every conclusion is strictly deducible from the premises.",
                    },
                    {
                        "spanish": "A szintézis megalkotása az nem más, mint a látszólag ellentmondó álláspontok magasabb szintű integrálása.",
                        "english": "Creating a synthesis is none other than the higher-level integration of seemingly contradictory positions.",
                    },
                    {
                        "spanish": "A szerző gondolatmenete olyannyira koherens volt, hogy az ellenérvek képviselői sem találtak rajta logikai hibát.",
                        "english": "The author's line of reasoning was so coherent that even proponents of counterarguments found no logical flaw in it.",
                    },
                ],
                "tip": "In B2 academic writing, signal transitions clearly: 'Mindenekelőtt tisztázni szükséges...' (First of all it is necessary to clarify...), 'Ebből következően megállapíthatjuk...' (Consequently we can establish...), and 'Összegezve a fentieket...' (Summarizing the above...).",
            },
            "words": [
                {"lemma": "fogalmi tisztázás", "translation": "conceptual clarification", "pos": "expression"},
                {"lemma": "érvelés", "translation": "argumentation / reasoning", "pos": "noun"},
                {"lemma": "előfeltevés", "translation": "presupposition / premise", "pos": "noun"},
                {"lemma": "szintézis", "translation": "synthesis", "pos": "noun"},
                {"lemma": "gondolatmenet", "translation": "train of thought / line of reasoning", "pos": "noun"},
            ],
            "exercises": {
                "intro": [
                    mc(
                        "vocabulary",
                        "introduce",
                        "Why is 'fogalmi tisztázás' essential at the start of an academic essay?",
                        [
                            "it defines terms precisely to eliminate ambiguity and semantic confusion in argumentation",
                            "it provides a mandatory list of all grammatical errors made by previous authors",
                            "it translates the entire text into ancient Latin for archiving purposes",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "vocabulary",
                        "introduce",
                        "What is a 'szintézis' in philosophical methodology?",
                        [
                            "the higher-level unification and resolution of conflicting ideas or theses",
                            "the total physical destruction of all opponent manuscripts",
                            "a short break taken between academic lecture hours",
                        ],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
                "controlled": [
                    match(
                        "vocabulary",
                        "controlled",
                        [
                            ["fogalmi tisztázás", "conceptual clarification"],
                            ["érvelés", "argumentation / reasoning"],
                            ["előfeltevés", "presupposition / premise"],
                            ["szintézis", "synthesis"],
                            ["gondolatmenet", "line of reasoning"],
                        ],
                        ["b2-33-vocab"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Which cleft sentence defines philosophical synthesis with academic precision?",
                        [
                            "A szintézis az nem más, mint a tézis és az antitézis magasabb rendű egyesítése.",
                            "A szintézis az nem más hogy a tézis és antitézis egyesítése.",
                            "A szintézis az nem más mint ha tézist és antitézist egyesítenénk.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "grammar",
                        "controlled",
                        "Select the sentence using abstract causal syntagms in philosophical exposition:",
                        [
                            "A következtetés érvényessége abból adódott, hogy az előfeltevések igaznak bizonyultak.",
                            "A következtetés érvényessége azzal adódott hogy az előfeltevések igazak voltak.",
                            "A következtetés érvényessége annak adódott hogy az előfeltevések igazak voltak.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "grammar",
                        "controlled",
                        "Éppen az a koherens ____ hiányzott a vitapartner írásából, ami meggyőzhette volna a tudományos bizottságot. (line of reasoning)",
                        "gondolatmenet",
                        "Precisely that coherent line of reasoning was missing from the opponent's writing which could have convinced the scientific committee.",
                        ["b2-cleft-identification"],
                    ),
                ],
                "practice": [
                    fb(
                        "grammar",
                        "practice",
                        "A tanulmány ereje nagyrészt ____ volt tulajdonítható, hogy a szerző világos fogalmi tisztázással indított. (to that)",
                        "annak",
                        "The strength of the study was largely attributable to the fact that the author started with clear conceptual clarification.",
                        ["b2-cleft-identification"],
                    ),
                    sb(
                        "grammar",
                        "practice",
                        ["A", "logikus", "érvelés", "nélkülözhetetlen", "a", "filozófiai", "vitákban."],
                        ["A", "logikus", "érvelés", "nélkülözhetetlen", "a", "filozófiai", "vitákban."],
                        "Logical argumentation is indispensable in philosophical debates.",
                        ["b2-cleft-identification"],
                    ),
                    fb(
                        "vocabulary",
                        "practice",
                        "A kritikus rámutatott a tanulmány rejtett ____, amelyek megalapozatlanok voltak. (presuppositions / premises)",
                        "előfeltevéseire",
                        "The critic pointed out the hidden presuppositions of the study which were unfounded.",
                        ["b2-33-vocab"],
                    ),
                    sb(
                        "vocabulary",
                        "practice",
                        ["A", "két", "ellentétes", "elmélet", "között", "új", "szintézis", "jött", "létre."],
                        ["A", "két", "ellentétes", "elmélet", "között", "új", "szintézis", "jött", "létre."],
                        "A new synthesis was created between the two opposing theories.",
                        ["b2-33-vocab"],
                    ),
                ],
                "dialogue": [
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Konzulens", "text": "Hogyan érdemes felépíteni a szakdolgozat elméleti fejezetét?"},
                            {"speaker": "Diplomázó", "text": "____"},
                        ],
                        [
                            "Mindenekelőtt pontos fogalmi tisztázással kezdek, feltárom a kiinduló előfeltevéseket, majd logikus gondolatmenettel vezetem le a szintézist.",
                            "Kizárólag híres emberek fényképeit illesztem be szöveg nélkül a dolgozatba.",
                            "A szakdolgozatot véletlenszerű mondatokból másolom össze az internetről.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                    dc(
                        "dialogue",
                        [
                            {"speaker": "Opponens", "text": "Miért tartja gyengének a szerző érvelését a második alfejezetben?"},
                            {"speaker": "Recenzens", "text": "____"},
                        ],
                        [
                            "Főként abból adódóan, hogy a levont következtetések nincsenek összhangban a kiinduló előfeltevésekkel, és hiányzik a logikai szintézis.",
                            "Mert a szerző túl sok oldalt írt a megengedettnél.",
                            "A recenzióban csak a betűtípust bíráltam, a tartalommal nem foglalkoztam.",
                        ],
                        0,
                        ["b2-cleft-identification"],
                    ),
                ],
                "writing": [
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an opening thesis sentence for a philosophical essay using 'fogalmi tisztázás' and 'az nem más, mint...'.",
                                "answer": "A politikai filozófiai elemzés elsődleges feladata a fogalmi tisztázás, amely az nem más, mint a vitatott eszmék pontos elhatárolása a téveszméktől.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                    sw(
                        "production",
                        [
                            {
                                "prompt": "Write an academic sentence connecting 'előfeltevés' and 'érvelés' with 'abból adódóan, hogy...'.",
                                "answer": "A filozófiai érvelés megbízhatósága abból adódott, hogy a szerző szisztematikusan megvizsgálta és igazolta a kiinduló előfeltevéseit.",
                            }
                        ],
                        ["b2-cleft-identification"],
                    ),
                ],
                "check": [
                    fb(
                        "grammar",
                        "check",
                        "Az esszé legfőbb erénye az nem más, mint a rendkívül fegyelmezett és világos ____. (line of reasoning)",
                        "gondolatmenet",
                        "The primary virtue of the essay is none other than the exceptionally disciplined and clear line of reasoning.",
                        ["b2-cleft-identification"],
                    ),
                    mc(
                        "vocabulary",
                        "check",
                        "Which noun denotes an underlying premise or assumption taken as the starting point of an argument?",
                        ["előfeltevés", "utóíz", "döntetlen"],
                        0,
                        ["b2-33-vocab"],
                    ),
                ],
            },
        },
    ],
    "consolidation": {
        "goals": [
            "I can formulate authoritative cleft identificational sentences using az nem más, mint ... and éppen az, ami ...",
            "I can deploy complex formal causal syntagms (abból adódóan, hogy; annak tulajdoníthatóan, hogy) in academic prose",
            "I can synthesize political and philosophical terminology to analyze historical hysteria, freedom, and legitimacy",
        ],
        "exercises": [
            # 1..3 Recognize
            match(
                "vocabulary",
                "recognize",
                [
                    ["nem más, mint", "none other than"],
                    ["politikai hisztéria", "political hysteria"],
                    ["valóságérzék", "sense of reality"],
                    ["jogállamiság", "rule of law"],
                    ["fogalmi tisztázás", "conceptual clarification"],
                ],
                ["b2-33-vocab"],
            ),
            mc(
                "vocabulary",
                "recognize",
                "What does 'bűnbakképzés' designate in political analysis?",
                [
                    "the psychological and political scapegoating of a group to divert blame from systemic failures",
                    "an official legal process for pardoning convicted political prisoners",
                    "a statistical method used in demographic census analysis",
                ],
                0,
                ["b2-33-vocab"],
            ),
            mc(
                "grammar",
                "recognize",
                "Which sentence correctly combines cleft identification with an abstract causal syntagm?",
                [
                    "Bibó szerint a politikai hisztéria az nem más, mint kollektív önbecsapás, amely abból adódik, hogy a félelem megbénítja a józan észt.",
                    "Bibó szerint a politikai hisztéria az nem más hogy önbecsapás, amely azzal adódik ha a félelem bénít.",
                    "Bibó szerint a politikai hisztéria az nem más mint ha önbecsapás lenne, amely annak adódik mert a félelem bénít.",
                ],
                0,
                ["b2-cleft-identification"],
            ),
            # 4..6 Recall
            fb(
                "vocabulary",
                "recall",
                "A demokratikus intézmények stabilitásához elengedhetetlen a hatalom gyakorlóinak nyilvános ____ és felelősségvállalása. (accountability)",
                "elszámoltathatósága",
                "For the stability of democratic institutions, the public accountability and responsibility of powerholders is indispensable.",
                ["b2-33-vocab"],
            ),
            fb(
                "grammar",
                "recall",
                "A társadalmi polarizáció mélyülése nagyrészt abból ____, hogy hiányzott a párbeszéd a szemben álló felek között. (arose / stemmed)",
                "adódott",
                "The deepening of social polarization largely arose from the fact that dialogue was missing between the opposing parties.",
                ["b2-cleft-identification"],
            ),
            fb(
                "grammar",
                "recall",
                "A diktatúra lényege az nem más, ____ a polgárok mindennapi szabadságának teljes felszámolása. (than)",
                "mint",
                "The essence of dictatorship is none other than the total eradication of citizens' everyday liberty.",
                ["b2-cleft-identification"],
            ),
            # 7..9 In Context
            mc(
                "grammar",
                "in-context",
                "Why is 'az nem más, mint...' preferred over a simple copular sentence in philosophical definitions?",
                [
                    "Because it provides emphatic identificational focus, elevating the statement into an authoritative thesis.",
                    "Because Hungarian grammar does not allow copular verbs in the present tense under any circumstances.",
                    "Because 'mint' can only be used with demonstrative pronouns in academic texts.",
                ],
                0,
                ["b2-cleft-identification"],
            ),
            dc(
                "in-context",
                [
                    {"speaker": "Filozófiatanár", "text": "Hogyan foglalná össze Bibó István demokráciafelfogását egyetlen mondatban?"},
                    {"speaker": "Egyetemi hallgató", "text": "____"},
                ],
                [
                    "A demokrácia lényege az nem más, mint az emberi méltóság feltétlen tisztelete és a félelem nélküli élet intézményes biztosítása.",
                    "A demokrácia csupán felesleges fecsegés a parlamentben, amit a hadseregnek kell irányítania.",
                    "Bibó szerint a demokrácia tilos Közép-Európában a történelmi hagyományok miatt.",
                ],
                0,
                ["b2-cleft-identification"],
            ),
            mc(
                "grammar",
                "in-context",
                "Select the sentence where 'annak tulajdoníthatóan' is applied with syntactic and stylistic accuracy:",
                [
                    "A konszenzus létrejötte annak volt tulajdonítható, hogy a felek tiszteletben tartották az alkotmányos fékeket és egyensúlyokat.",
                    "A konszenzus létrejötte abból volt tulajdonítható, hogy a felek tiszteletben tartották a fékeket.",
                    "A konszenzus létrejötte azzal volt tulajdonítható, hogy a felek tiszteletben tartották a fékeket.",
                ],
                0,
                ["b2-cleft-identification"],
            ),
            # 10..12 Produce
            sb(
                "grammar",
                "produce",
                ["A", "valódi", "szabadság", "az", "nem", "más,", "mint", "félelemmentes", "felelősségvállalás."],
                ["A", "valódi", "szabadság", "az", "nem", "más,", "mint", "félelemmentes", "felelősségvállalás."],
                "True freedom is none other than fearless assumption of responsibility.",
                ["b2-cleft-identification"],
            ),
            sb(
                "grammar",
                "produce",
                ["A", "történelmi", "katasztrófa", "a", "józan", "valóságérzék", "elvesztéséből", "adódott."],
                ["A", "történelmi", "katasztrófa", "a", "józan", "valóságérzék", "elvesztéséből", "adódott."],
                "The historical catastrophe arose from the loss of a sober sense of reality.",
                ["b2-cleft-identification"],
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a philosophical paragraph synthesizing cleft identification ('az nem más, mint') and formal causal deduction ('abból adódóan, hogy').",
                        "answer": "A demokratikus érettség az nem más, mint a kollektív félelmek leküzdése; a történelmi hisztéria elkerülése abból adódik, hogy a polgárok a bűnbakképzés helyett az intézményes elszámoltathatóságot választják.",
                    }
                ],
                ["b2-cleft-identification"],
            ),
        ],
    },
}
