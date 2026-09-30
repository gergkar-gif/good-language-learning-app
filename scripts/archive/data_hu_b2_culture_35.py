# -*- coding: utf-8 -*-
"""
Hungarian B2 Culture Track Unit 35:
Hungary in the 21st-Century Knowledge Economy (b2-tudomanyjovo)
"""
from helpers_hu_b2_exercises import dc, fb, match, mc, sb, sw

VOCAB_SKILL = "b2-tudomanyjovo-vocab"
GRAMMAR_SKILL = "b2-speculative-conditionals"

UNIT_35_TUDOMANYJOVO = {
    "unit_num": 35,
    "slug": "tudomanyjovo",
    "title": "Hungary in the 21st-Century Knowledge Economy",
    "grammar_skill": GRAMMAR_SKILL,
    "vocab_skill": VOCAB_SKILL,
    "theme": "21st-century Hungarian science, knowledge economy and future technologies",
    "location": "Szeged (ELI-ALPS), Budapest (MTA, BME), Garching és Debrecen",
    "intro_body": [
        "A magyar tudományosság a huszonegyedik században is a globális kutatási élvonalban képviselteti magát, folytatva a tizenkilencedik és huszadik század nagy újítóinak örökségét. Krausz Ferenc 2023-as fizikai Nobel-díja az attoszekundumos fizika megalapozásáért, valamint a szegedi ELI-ALPS lézeres kutatóközpont megépülése bizonyítja, hogy a Kárpát-medence stratégiai csomóponttá válhat a nemzetközi élvonalbeli fizikai és fotonikai infrastruktúrában.",
        "Ezzel párhuzamosan a hazai kutatóintézetek és egyetemek az információs társadalom kulcskérdéseire keresnek választ: a mesterséges intelligencia és a magyar nyelvtechnológia megőrzésére, a tiszta technológiák és az akkumulátorgyártás mérnöki kihívásaira, valamint a közepes méretű nemzeti nyelvek digitális jövőjére a gépi tanulás korában.",
        "Nyelvtanilag az összetett hipotetikus és spekulatív feltételes szerkezeteket (feltéve, ha...; azzal a feltétellel, hogy...; amennyiben; hacsak nem...; abban az esetben, ha...) és az ellenfaktuális múltbeli mondathalmozást (ha létrejött volna..., akkor megvalósulhatott volna) sajátítjuk el, amelyek elengedhetetlenek a tudományos érvelés és jövőkutatás B2 szintű megfogalmazásához."
    ],
    "combined_story_title": "Attoszekundumok és mesterséges intelligencia: A 21. századi magyar tudomány",
    "combined_story_summary": "Hungary's position in global science and innovation in the 21st century: Ferenc Krausz and attosecond physics (2023 Nobel Prize), ELI-ALPS laser research center in Szeged, AI and natural language processing in Hungarian, clean tech, and the future of medium-sized languages.",
    "lessons": [
        {
            "num": 1,
            "title": "Ferenc Krausz and Attosecond Physics: Peering Inside the Electron",
            "grammar_label": "Complex speculative conditions with *feltéve, ha...* and *azzal a feltétellel, hogy...*",
            "goals": [
                "I can explain Ferenc Krausz's Nobel Prize-winning research on attosecond physics and electronic motion.",
                "I can construct complex speculative conditional clauses using *feltéve, ha...* and *azzal a feltétellel, hogy...*",
                "I can discuss future medical diagnostics using infrared molecular fingerprinting."
            ],
            "story_segment": {
                "seg_slug": "krauszferenc",
                "title": "Krausz Ferenc és az elektronok világa: Az attoszekundumos fizika",
                "summary": "In 2023, Ferenc Krausz won the Nobel Prize in Physics for pioneering attosecond light pulses (10^-18 seconds), enabling scientists to track electron movement in real time and discover medical biomarkers.",
                "location": "Mór, Budapest, Bécs és Garching (2001–2023)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "2023 őszén a világ tudományos közvéleménye Magyarországra és a magyar kutatókra figyelt, amikor Krausz Ferenc fizikus – Pierre Agostinivel és Anne L'Huillier-vel megosztva – elnyerte a fizikai Nobel-díjat. A móri születésű, az Eötvös Loránd Tudományegyetemen és a Budapesti Műszaki Egyetemen diplomázott tudós olyan kísérleti módszereket dolgozott ki, amelyek lehetővé tették az atomi léptékű elektronmozgások valós idejű megfigyelését."
                    },
                    {
                        "type": "narration",
                        "text": "Az attoszekundumos fizika a másodperc egymilliárd-milliárdod részének (10^-18 másodperc) világába enged bepillantást. Ahogyan egy ultragyors vaku kimerevíti a száguldó kolibri szárnycsapását, úgy a Krausz Ferenc által előállított fényimpulzusok kimerevítették az atommag körül keringő elektronok korábban láthatatlannak hitt mozgását."
                    },
                    {
                        "type": "narration",
                        "text": "Krausz professzor a bécsi egyetemen és a müncheni Max Planck Kvantumoptikai Intézetben végzett úttörő kísérletei során mindig szoros kapcsolatot ápolt a hazai tudományos élettel. Meggyőződése szerint a legelvontabb alapkutatásnak is társadalmi hasznot kell hajtania, ezért figyelmét hamar az orvostudományi alkalmazások felé fordította."
                    },
                    {
                        "type": "narration",
                        "text": "Az általa vezetett nemzetközi kutatócsoport kifejlesztette a molekuláris ujjlenyomat-vétel módszerét: infravörös lézerimpulzusok segítségével az emberi vérplazma molekuláris összetételét vizsgálják. Ez a technológia a jövőben lehetővé teheti a daganatos megbetegedések és krónikus kórok korai felismerését még azelőtt, hogy a klinikai tünetek megjelennének."
                    },
                    {
                        "type": "narration",
                        "text": "Krausz Ferenc Nobel-díja hatalmas lendületet adott a magyar tudománynak. Személyes példája bizonyítja, hogy az alapos hazai mérnöki és elméleti képzésre építve, nemzetközi együttműködések hálózatában a legmagasabb globális tudományos csúcsok is meghódíthatók."
                    }
                ]
            },
            "words": [
                {"lemma": "attoszekundumos fizika", "translation": "attosecond physics", "pos": "expression"},
                {"lemma": "elektronmozgás", "translation": "electron movement / dynamics", "pos": "noun"},
                {"lemma": "lézerimpulzus", "translation": "laser pulse", "pos": "noun"},
                {"lemma": "molekuláris ujjlenyomat", "translation": "molecular fingerprint", "pos": "expression"},
                {"lemma": "Nobel-díj", "translation": "Nobel Prize", "pos": "noun"},
                {"lemma": "kutatás-fejlesztés", "translation": "research and development (R&D)", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "speculative-conditionals-felteve",
                "title": "Speculative Conditions: Feltéve, ha... and Azzal a feltétellel, hogy...",
                "text1_title": "Expressing Scientific Hypotheses with Feltéve, ha...",
                "text1": "In formal academic discourse, speculative hypotheses are introduced using complex conditional conjunctions. The compound phrase 'feltéve, ha...' (provided that / assuming that) sets up a strict preliminary premise under which a theoretical model or physical prediction holds true: 'A modell érvényes, feltéve, ha az elektronok energiája nem haladja meg a határértéket.'",
                "text2_title": "Contractual and Methodological Prerequisites: Azzal a feltétellel, hogy...",
                "text2": "When stating a necessary precondition or experimental boundary, Hungarian uses 'azzal a feltétellel, hogy...' (on condition that...). The subordinate clause takes the conditional mood (feltételes mód) when speculative, or the subjunctive (felszólító mód) when expressing an administrative or procedural constraint.",
                "table_title": "Speculative Conditional Formulas in Academic Hungarian",
                "table_rows": [
                    ["A kísérlet megismételhető, feltéve, ha a vákuum stabil marad.", "The experiment is repeatable, provided that the vacuum remains stable."],
                    ["A támogatást megítélik, azzal a feltétellel, hogy publikálják az eredményeket.", "The funding is granted, on condition that they publish the findings."],
                    ["Feltéve, ha időben felismerik a sejtelváltozást, a betegség gyógyítható.", "Assuming that the cellular alteration is recognized in time, the disease is curable."]
                ],
                "examples": [
                    {"spanish": "A lézerimpulzusok pontosan mérhetők, feltéve, ha a detektorok érzékenysége eléri a kívánt szintet.", "english": "The laser pulses can be accurately measured, provided that the detectors' sensitivity reaches the desired level."},
                    {"spanish": "A kutatócsoport engedélyt kapott a tesztekre, azzal a feltétellel, hogy szigorú etikai normákat követnek.", "english": "The research group obtained permission for the tests, on condition that they follow strict ethical standards."},
                    {"spanish": "A molekuláris ujjlenyomat megbízható diagnózist ad, feltéve, ha elegendő mintát elemeznek.", "english": "The molecular fingerprint yields a reliable diagnosis, assuming that they analyze sufficient samples."}
                ],
                "tip": "Observe word order: when 'feltéve, ha...' introduces the main premise, the conditional subclause is set off by commas: 'Feltéve, ha a mérések helytállóak, a hipotézis igazoltnak tekinthető.'"
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["attoszekundumos fizika", "attosecond physics"],
                        ["elektronmozgás", "electron movement"],
                        ["lézerimpulzus", "laser pulse"],
                        ["molekuláris ujjlenyomat", "molecular fingerprint"],
                        ["Nobel-díj", "Nobel Prize"],
                        ["kutatás-fejlesztés", "research and development"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Milyen korszakalkotó eredményért ítélték oda Krausz Ferencnek a 2023-as fizikai Nobel-díjat?",
                    [
                        "Az elektronok mozgásának vizsgálatára szolgáló attoszekundumos fényimpulzusok előállításáért.",
                        "A Mars bolygón talált folyékony víz és kőzetek geológiai feltárásáért.",
                        "Az első magyar gyártmányú gőzgép és vasúti sínrendszer megtervezéséért."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A magyar kutatócsoport infravörös lézerrel vizsgálja a vérplazmát, hogy megalkossa a betegségek korai felismerésére szolgáló _____ .",
                    "molekuláris ujjlenyomatot",
                    "The Hungarian research group examines blood plasma with infrared lasers to create a molecular fingerprint for early disease detection.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik kötőszó fejezi ki legszabatosabban a tudományos feltételt az alábbi mondatban? 'Az új elmélet igazolható, _____ a kísérleti mérések megismételhetők azonos körülmények között.'",
                    ["feltéve, ha", "noha", "minthogy", "jóllehet"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "Az egyetem kutatási támogatást kapott a minisztériumtól, _____ a feltétellel, hogy nemzetközi szabadalmat nyújtanak be.",
                    "azzal",
                    "The university received research funding from the ministry, on condition that they file an international patent.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "diagnózis", "megbízható", "lesz,", "feltéve,", "ha", "elegendő", "vérmintát", "elemeznek."],
                    ["A", "diagnózis", "megbízható", "lesz,", "feltéve,", "ha", "elegendő", "vérmintát", "elemeznek."],
                    "The diagnosis will be reliable, provided that they analyze sufficient blood samples.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Fizikus", "text": "Alkalmazható-e az attoszekundumos technológia a mindennapi orvosi diagnosztikában?"},
                        {"speaker": "Kutatóorvos", "text": "_____"}
                    ],
                    [
                        "Igen, feltéve, ha sikerül kompakt és megfizethető lézerforrásokat fejleszteni a kórházak számára.",
                        "Nem, mert az elektronok mozgását tilos orvosi célokra felhasználni az Európai Unióban.",
                        "Kizárólag akkor, ha a betegek maguk kezelik a laboratóriumi műszereket otthon."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Miért forradalmi jelentőségű az elektronok mozgásának megfigyelése az anyagtudományban?",
                    [
                        "Mert az elektronmozgás irányítja az összes kémiai kötés kialakulását és a biológiai folyamatokat.",
                        "Mert segítségével meg lehet állítani a Föld forgását és szabályozni a napsütést.",
                        "Mert feleslegessé teszi az összes kórházi laboratóriumot és orvosi képzést."
                    ],
                    0
                )
            ]
        },
        {
            "num": 2,
            "title": "ELI-ALPS Szeged: European Research Infrastructure in the South",
            "grammar_label": "Restrictive and concessive conditions with *amennyiben* and *hacsak nem...*",
            "goals": [
                "I can describe the ELI-ALPS laser research center in Szeged as part of European research infrastructure.",
                "I can employ formal restrictive conditional connectors (*amennyiben, hacsak nem*) in scientific discourse.",
                "I can analyze how international research facilities stimulate regional economies and knowledge transfer."
            ],
            "story_segment": {
                "seg_slug": "elialpsszeged",
                "title": "ELI-ALPS Szeged: Nemzetközi lézerinfrastruktúra a Dél-Alföldön",
                "summary": "The ELI-ALPS research center in Szeged is one of the world's most advanced laser research institutes, attracting international physicists and creating a vibrant biomedical and photonic cluster.",
                "location": "Szeged, ELI-ALPS Kutatóközpont",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A Tisza partján, a nagy egyetemi hagyományokkal rendelkező Szeged északi peremén emelkedik Közép-Európa egyik legmodernebb tudományos létesítménye: az ELI-ALPS (Extreme Light Infrastructure Attosecond Light Pulse Source) lézeres kutatóközpont. Az Európai Unió támogatásával felépült gigantikus kutatási infrastruktúra a kontinens legjelentősebb tudományos beruházásai közé tartozik."
                    },
                    {
                        "type": "narration",
                        "text": "A szegedi intézmény a páneurópai ELI projekt három pillérének egyike, amely Prága és Bukarest mellett az ultrarövid fényimpulzusok és az attoszekundumos technológia kutatására szakosodott. A laboratóriumokban található csúcsteljesítményű lézerek olyan elképesztő fénysűrűséget és sebességet hoznak létre, amely a csillagok belsejében uralkodó fizikai viszonyokat idézi meg a Földön."
                    },
                    {
                        "type": "narration",
                        "text": "Az ELI-ALPS épülete önmagában is mérnöki csoda. A lézerek rendkívüli érzékenysége miatt a kísérleti csarnokokat olyan rezgésmentes alapzatokra és szigorú tiszta terekbe helyezték, ahol a külső forgalom, a földrengések vagy akár a hőmérséklet tizedfokos ingadozása sem zavarhatja meg a precíziós méréseket."
                    },
                    {
                        "type": "narration",
                        "text": "A kutatóközpont a világ minden tájáról vonzza a vendégkutatókat, fizikusokat, kémikusokat és anyagtudósokat. A nyílt hozzáférésű nemzetközi konzorcium keretében a kutatók versenyképes pályázatok révén kaphatnak mérési időt, ami felbecsülhetetlen értékű tudástranszfert és nemzetközi együttműködési hálózatot teremt Magyarországon."
                    },
                    {
                        "type": "narration",
                        "text": "Szeged városa számára az ELI-ALPS jóval több egyszerű tudományos bázisnál: a lézerközpont körül létrejövő Science Park egy dinamikus innovációs ökoszisztémát táplál, ahol a biotechnológiai cégek, szoftverfejlesztők és startupok közvetlenül hasznosíthatják a legfrissebb tudományos felfedezéseket."
                    }
                ]
            },
            "words": [
                {"lemma": "kutatóközpont", "translation": "research center / institute", "pos": "noun"},
                {"lemma": "lézerinfrastruktúra", "translation": "laser infrastructure", "pos": "noun"},
                {"lemma": "fotonika", "translation": "photonics", "pos": "noun"},
                {"lemma": "nemzetközi konzorcium", "translation": "international consortium", "pos": "expression"},
                {"lemma": "tiszta tér", "translation": "cleanroom / clean space", "pos": "expression"},
                {"lemma": "innovációs ökoszisztéma", "translation": "innovation ecosystem", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "restrictive-conditionals-amennyiben",
                "title": "Restrictive and Concessive Conditions: Amennyiben and Hacsak nem...",
                "text1_title": "Formal Conditional Provisos with Amennyiben",
                "text1": "In high-register administrative, technical, and scientific prose, 'amennyiben' replaces everyday 'ha'. It signals an objective, institutional contingency: 'Amennyiben a pályázat megfelel a követelményeknek, a bizottság mérési időt biztosít az ELI laboratóriumában.'",
                "text2_title": "Negative Restrictive Clauses: Hacsak nem...",
                "text2": "'Hacsak nem...' (unless / except if) introduces the sole mitigating circumstance that can reverse an otherwise inevitable outcome. It is followed by an indicative or conditional verb depending on whether the exception is factual or hypothetical: 'A beruházás sikeres lesz, hacsak nem lépnek fel váratlan hálózati zavarok.'",
                "table_title": "Restrictive Condition Markers in Technical Contexts",
                "table_rows": [
                    ["Amennyiben hiba lép fel, a rendszer leáll.", "In the event that an error occurs, the system shuts down."],
                    ["A mérést elvégzik, hacsak nem romlik el a lézer.", "The measurement will be carried out, unless the laser breaks down."],
                    ["Amennyiben szükséges, további forrásokat biztosítanak.", "If necessary, additional resources will be provided."]
                ],
                "examples": [
                    {"spanish": "Amennyiben a konzorcium jóváhagyja a tervezetet, a szegedi kutatók azonnal megkezdhetik a teszteket.", "english": "In the event that the consortium approves the draft, the Szeged researchers may begin tests immediately."},
                    {"spanish": "A kísérletet holnap reggel befejezik, hacsak nem tapasztalnak váratlan rezgéseket az alapzatban.", "english": "The experiment will be concluded tomorrow morning, unless they experience unexpected vibrations in the foundation."},
                    {"spanish": "Amennyiben elegendő nemzetközi kutató érkezik, a létesítmény kapacitását tovább bővítik.", "english": "Provided that sufficient international researchers arrive, the facility's capacity will be further expanded."}
                ],
                "tip": "Avoid double negatives: 'hacsak nem' already contains negation, so the verb that follows must not take a redundant 'nem': write 'hacsak nem történik hiba' (unless an error happens), never 'hacsak nem nem történik hiba'."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["kutatóközpont", "research center"],
                        ["lézerinfrastruktúra", "laser infrastructure"],
                        ["fotonika", "photonics"],
                        ["nemzetközi konzorcium", "international consortium"],
                        ["tiszta tér", "cleanroom"],
                        ["innovációs ökoszisztéma", "innovation ecosystem"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Milyen speciális kutatási területre szakosodott a Szegeden felépült ELI-ALPS nemzetközi kutatóközpont?",
                    [
                        "Az ultrarövid fényimpulzusok és az attoszekundumos lézertechnológia kutatására.",
                        "A mezőgazdasági műtrágyák és nehézgépek tömeggyártására.",
                        "A mélytengeri korallzátonyok és tengeralattjárók tesztelésére."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A precíziós lézerek védelme érdekében a kísérleti berendezéseket szigorúan ellenőrzött pormentes _____ helyezték el.",
                    "tiszta terekben",
                    "In order to protect the precision lasers, the experimental apparatus was placed in strictly controlled dust-free cleanrooms.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik kötőszó fejezi ki a hivatalos, emelkedett feltételességet az alábbi mondatban? '_____ a pályázat elnyeri a bizottság támogatását, a kutatócsoport megkezdheti a kísérleteket.'",
                    ["Amennyiben", "Bár", "Minthogy", "Ámbár"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A kísérletet a tervek szerint befejezik holnapra, _____ nem lép fel váratlan hiba a hűtőrendszerben.",
                    "hacsak",
                    "The experiment will be concluded by tomorrow according to plan, unless an unexpected fault occurs in the cooling system.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["Amennyiben", "a", "mérések", "sikeresek,", "új", "tudományos", "közleményt", "adnak", "ki."],
                    ["Amennyiben", "a", "mérések", "sikeresek,", "új", "tudományos", "közleményt", "adnak", "ki."],
                    "In the event that the measurements are successful, they will publish a new scientific paper.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Egyetemi hallgató", "text": "Hogyan juthatnak be a külföldi kutatók a szegedi ELI-ALPS laboratóriumaiba?"},
                        {"speaker": "Intézetvezető", "text": "_____"}
                    ],
                    [
                        "Nemzetközi pályázatok útján igényelhetnek mérési időt, amennyiben a projektjük megfelel a legmagasabb minőségi követelményeknek.",
                        "Bárki szabadon besétálhat az utcáról és kipróbálhatja a nagy teljesítményű lézereket.",
                        "Kizárólag a szegedi születésű lakosok kaphatnak belépőkártyát az épületbe."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Milyen gazdasági hatást gyakorol az ELI-ALPS létesítmény Szeged és a Dél-Alföld fejlődésére?",
                    [
                        "Science Parkot és innovációs ökoszisztémát hoz létre, vonzva a biotechnológiai cégeket és magasan képzett szakembereket.",
                        "Megtiltja a magánvállalkozások működését és bezáratja az egyetem tanszékeit.",
                        "Kizárólag bányászati munkásokat alkalmaz a Tisza medrében."
                    ],
                    0
                )
            ]
        },
        {
            "num": 3,
            "title": "Hungarian AI: Large Language Models and Computational Linguistics",
            "grammar_label": "Counterfactual condition stacking in scientific deduction (*ha lett volna... volna*)",
            "goals": [
                "I can explain the unique computational challenges Hungarian grammar poses for AI and large language models.",
                "I can formulate multi-clause counterfactual conditions in the past conditional mood (*ha lett volna..., akkor...*).",
                "I can debate digital sovereignty and the importance of national NLP resources."
            ],
            "story_segment": {
                "seg_slug": "magyarmestintelligencia",
                "title": "Magyar mesterséges intelligencia és nyelvtechnológia",
                "summary": "Hungarian computational linguists at NYTK and BME are developing sovereign Hungarian LLMs (like PULI), tackling the intricate challenges of agglutinative morphology and word order.",
                "location": "Budapest (Nyelvtudományi Kutatóközpont, BME)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A mesterséges intelligencia és a nagy nyelvi modellek korszakában a nyelvek túlélése és digitális életképessége alapvetően azon múlik, hogy rendelkeznek-e korszerű számítógépes nyelvtechnológiával. A Nyelvtudományi Kutatóközpont (NYTK) és a Budapesti Műszaki Egyetem kutatói évtizedek óta dolgoznak azon, hogy a magyar nyelv ne szoruljon a technológiai perifériára."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar nyelv feldolgozása egyedülálló kihívások elé állítja a gépi tanulási algoritmusokat. Míg az angol nyelvben a szavak alakja viszonylag merev, a magyar agglutináló szerkezet miatt egyetlen igetőből vagy főnévből több száz ragozott szóalak hozható létre. E gazdag morfológiai sokféleség elemzéséhez kifinomult tokenizálókra és szabályalapú morfológiai elemzőkre van szükség."
                    },
                    {
                        "type": "narration",
                        "text": "További nehézséget jelent a szabadnak nevezett, ám valójában szigorú pragmatikai és fókuszszabályok által vezérelt magyar szórend. Ha a mondat elején áll a fókusz, az teljesen megváltoztatja az állítás jelentését és intonációját, amit a statisztikai modellek csak hatalmas méretű, gondosan annotált magyar szövegkorpuszok segítségével képesek megbízhatóan megtanulni."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar kutatók válasza a kihívásra a PULI és más nemzeti nyelvi modellek kifejlesztése volt. Ezek a modellek garantálják a nemzeti digitális szuverenitást, lehetővé téve, hogy a hazai közigazgatás, egészségügy és oktatás saját, biztonságos és a magyar kulturális kontextust pontosan értő algoritmusokra támaszkodhasson a globális techóriások kizárólagos függősége helyett."
                    },
                    {
                        "type": "narration",
                        "text": "A számítógépes nyelvészet magyarországi sikerei bizonyítják, hogy az anyanyelv védelme ma már nem csupán szótárak írását jelenti, hanem szuperszámítógépeken futó neuronális hálók betanítását. Ha a nyelvészek nem fektettek volna ekkora energiát a digitális korpuszok építésébe, a magyar nyelv ma komoly digitális hátrányt szenvedne."
                    }
                ]
            },
            "words": [
                {"lemma": "mesterséges intelligencia", "translation": "artificial intelligence", "pos": "expression"},
                {"lemma": "nyelvtechnológia", "translation": "language technology / NLP", "pos": "noun"},
                {"lemma": "nagy nyelvi modell", "translation": "large language model (LLM)", "pos": "expression"},
                {"lemma": "morfológiai elemző", "translation": "morphological analyzer", "pos": "expression"},
                {"lemma": "számítógépes nyelvészet", "translation": "computational linguistics", "pos": "expression"},
                {"lemma": "digitális szuverenitás", "translation": "digital sovereignty", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "counterfactual-stacking-ha-volna",
                "title": "Counterfactual Stacking in the Past Conditional: Ha... volna, akkor... lett volna",
                "text1_title": "Forming Past Counterfactual Hypotheses",
                "text1": "Counterfactual conditionals describe hypothetical events in the past that did not occur, along with their deduced unreal consequences. In Hungarian, the past conditional is formed by placing the particle 'volna' after a past-tense verb: 'Ha a kutatók korábban kezdték volna el a projektet, a modell már tavaly elkészült volna.'",
                "text2_title": "Stacking Clauses and Deductive Sequences",
                "text2": "In complex scientific discourse, counterfactual conditions often stack across multiple subclauses, demonstrating chains of cause and effect: 'Ha nem fejlesztették volna ki a morfológiai elemzőt, a rendszer nem lett volna képes kezelni a magyar ragokat, és a modell félreértette volna a fókuszos szerkezeteket.'",
                "table_title": "Past Counterfactual Formations in Hungarian",
                "table_rows": [
                    ["Ha több adat állt volna rendelkezésre, a modell pontosabb lett volna.", "If more data had been available, the model would have been more accurate."],
                    ["Ha nem építettek volna digitális korpuszt, a nyelv lemaradt volna.", "If they had not built a digital corpus, the language would have lagged behind."],
                    ["Megoldották volna a feladatot, ha ismerték volna az algoritmust.", "They would have solved the problem if they had known the algorithm."]
                ],
                "examples": [
                    {"spanish": "Ha a nyelvészek nem digitalizálták volna a szövegeket, ma nem lennének magyar nyelvi modellek.", "english": "If linguists had not digitized the texts, there would not be Hungarian language models today."},
                    {"spanish": "A rendszer sokkal lassabban tanult volna, ha nem használtak volna grafikus processzorokat.", "english": "The system would have learned much more slowly if they had not used graphics processing units."},
                    {"spanish": "Ha elkerülték volna a morfológiai hibákat, a fordítóprogram tökéletes eredményt adott volna.", "english": "If they had avoided morphological errors, the translation program would have produced a perfect result."}
                ],
                "tip": "Remember: 'volna' never attaches as a suffix; it is an invariant particle. In negative past conditional clauses, 'nem' precedes the verb and 'volna' follows: 'nem vett volna észre' (would not have noticed)."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["mesterséges intelligencia", "artificial intelligence"],
                        ["nyelvtechnológia", "language technology"],
                        ["nagy nyelvi modell", "large language model"],
                        ["morfológiai elemző", "morphological analyzer"],
                        ["számítógépes nyelvészet", "computational linguistics"],
                        ["digitális szuverenitás", "digital sovereignty"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Miért jelent különleges számítástechnikai kihívást a magyar nyelv feldolgozása a nagy nyelvi modellek számára?",
                    [
                        "A gazdag ragozási rendszer (agglutináció) és a fókusz által vezérelt rugalmas szórend miatt.",
                        "Mert a magyar nyelvben nincsenek magánhangzók és tilos írásjeleket használni.",
                        "Mert a számítógépek csak latin betűs szavakat képesek bináris kódra fordítani."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A saját nemzeti mesterséges intelligencia fejlesztése elengedhetetlen Magyarország _____ megőrzéséhez a digitális korban.",
                    "digitális szuverenitásának",
                    "Developing proprietary national artificial intelligence is essential for preserving Hungary's digital sovereignty in the digital age.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik mondat fejezi ki helyesen a múltbeli meg nem valósult (ellenfaktuális) feltételt?",
                    [
                        "Ha a mérnökök nem hoztak volna létre magyar korpuszt, a modell nem lett volna képes tanulni.",
                        "Ha a mérnökök nem hoznak létre magyar korpuszt, a modell nem lenne képes tanulni.",
                        "Ha a mérnökök nem hoznának létre magyar korpuszt, a modell nem fog tanulni.",
                        "Ha a mérnökök nem hoztak létre volna magyar korpuszt, a modell nem volna lett képes."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A számítógépes nyelvészek hamarabb befejezték _____ a projektet, ha nagyobb szerverkapacitással rendelkeztek volna.",
                    "volna",
                    "The computational linguists would have finished the project sooner if they had had larger server capacity.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["Ha", "nem", "fejlesztettek", "volna", "modelleket,", "a", "nyelv", "lemaradt", "volna."],
                    ["Ha", "nem", "fejlesztettek", "volna", "modelleket,", "a", "nyelv", "lemaradt", "volna."],
                    "If they had not developed models, the language would have lagged behind.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Informatikus", "text": "Miért fontos, hogy Magyarország saját nagy nyelvi modellel rendelkezzen?"},
                        {"speaker": "Kutató", "text": "_____"}
                    ],
                    [
                        "Mert ha nem fejlesztenénk saját modellt, teljesen kiszolgáltatottá válnánk a globális techcégek algoritmusainak és adatkezelésének.",
                        "Mert a külföldi szoftverek használatát törvényben tiltja a nemzetközi postaegyezmény.",
                        "Mert a mesterséges intelligencia csak magyar billentyűzeten keresztül képes működni."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Hogyan járulnak hozzá a szabályalapú morfológiai elemzők a magyar nyelvi modellek sikeréhez?",
                    [
                        "Segítenek a gazdag ragozott szóalakok felbontásában és a nyelvtani viszonyok pontos feltárásában.",
                        "Kitörlik az összes nehéz szót a szótárakból, hogy egyszerűbb legyen a programozás.",
                        "Átírják az összes magyar szöveget angol nyelvtanra a feldolgozás előtt."
                    ],
                    0
                )
            ]
        },
        {
            "num": 4,
            "title": "Green Energy Transition, Battery Technology, and Engineering Hubs",
            "grammar_label": "Multi-layered speculative conditionals with *abban az esetben, ha...* and *azzal a kikötéssel*",
            "goals": [
                "I can discuss the opportunities and environmental debates surrounding Hungary's battery manufacturing hubs.",
                "I can frame complex policy trade-offs using *abban az esetben, ha...* and *azzal a kikötéssel, hogy...*",
                "I can evaluate green energy transitions, solar grid balance, and water resource management."
            ],
            "story_segment": {
                "seg_slug": "zoldenergia",
                "title": "Zöld átállás és akkumulátorgyárak: Magyarország ipari átalakulása",
                "summary": "Debrecen and other hubs are becoming central to Europe's EV battery production. This brings massive investment but raises critical ecological, water-management, and energy-grid dilemmas.",
                "location": "Debrecen, Komárom és a Tisza-völgy",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszonegyedik század harmadik évtizedében Magyarország a globális zöld átállás és az elektromos mobilitás egyik legfontosabb európai központjává lépett elő. Az ázsiai és európai autóipari óriások hatalmas tőkeberuházásokkal létesítettek akkumulátorgyárakat Debrecenben, Komáromban, Iváncsán és Gödön, alapjaiban alakítva át a hazai gazdaság szerkezetét."
                    },
                    {
                        "type": "narration",
                        "text": "Ezek a beruházások rendkívüli gazdasági növekedést, új munkahelyeket és mérnöki innovációt ígérnek a régióban. Debrecen városa köré például olyan integrált ipari övezet épül ki, ahol az elektromos járművek teljes ellátási lánca – az alapanyagok finomításától a cellagyártáson át az összeszerelésig – egyetlen földrajzi térben koncentrálódik."
                    },
                    {
                        "type": "narration",
                        "text": "Ugyanakkor az akkumulátoripar gigantikus méretei komoly társadalmi vitákat és környezeti aggodalmakat váltottak ki. A gyárak működése hatalmas mennyiségű villamos energiát és ipari vizet igényel, ami az aszályok által sújtott Alföldön és a Tisza vízgyűjtő területén sürgető kérdéseket vet fel a fenntartható vízgazdálkodás és a talajvíz védelme kapcsán."
                    },
                    {
                        "type": "narration",
                        "text": "A zöld átállás másik kulcseleme a napenergia robbanásszerű elterjedése. Magyarországon a háztartási és ipari napelem-kapacitás néhány év alatt elérte az országos csúcsfogyasztás szintjét, ami óriási kihívás elé állítja az energiahálózatot: a megtermelt tiszta áram tárolása és kiegyenlítése korszerű akkumulátoros energiatárolókat és okos hálózatokat igényel."
                    },
                    {
                        "type": "narration",
                        "text": "A jövő kulcskérdése, hogy a gazdasági előnyök és a környezeti terhelés közötti egyensúly fenntartható-e hosszú távon. A magyar mérnökök és környezetvédők feladata, hogy szigorú ellenőrzéssel és technológiai újításokkal biztosítsák az ipari fejlődés és a természeti erőforrások harmonikus együttélését."
                    }
                ]
            },
            "words": [
                {"lemma": "zöld átállás", "translation": "green transition", "pos": "expression"},
                {"lemma": "akkumulátorgyártás", "translation": "battery manufacturing", "pos": "noun"},
                {"lemma": "energiahálózat", "translation": "energy grid / power distribution network", "pos": "noun"},
                {"lemma": "megújuló energia", "translation": "renewable energy", "pos": "expression"},
                {"lemma": "ipari beruházás", "translation": "industrial investment", "pos": "expression"},
                {"lemma": "környezeti terhelés", "translation": "environmental impact / footprint", "pos": "expression"}
            ],
            "grammar_doc": {
                "slug": "multi-layered-speculative-kikotes",
                "title": "Multi-Layered Speculative Conditionals: Abban az esetben, ha... and Azzal a kikötéssel, hogy...",
                "text1_title": "Categorical Scenarios with Abban az esetben, ha...",
                "text1": "'Abban az esetben, ha...' (in the event that / in the case that) sets up a clearly delineated case study or regulatory scenario in policy, economics, and environmental analysis: 'Abban az esetben, ha a vízkészletek apadnak, a gyárnak vissza kell fognia a termelést.'",
                "text2_title": "Contractual Stipulations with Azzal a kikötéssel, hogy...",
                "text2": "'Azzal a kikötéssel, hogy...' (with the proviso / stipulation that...) attaches an explicit condition or environmental safeguard to an approval. The following subordinate clause takes the subjunctive (felszólító mód) when expressing a normative rule: 'Engedélyezték a gyárépítést, azzal a kikötéssel, hogy zárt láncú vízgazdálkodást valósítsanak meg.'",
                "table_title": "Complex Condition Stipulations in Environmental Policy",
                "table_rows": [
                    ["Abban az esetben, ha túllépik a határértéket, bírságot szabnak ki.", "In the event that they exceed the threshold, a fine will be imposed."],
                    ["Támogatást kapnak, azzal a kikötéssel, hogy csökkentik a kibocsátást.", "They receive funding, with the stipulation that they reduce emissions."],
                    ["Abban az esetben, ha süt a nap, a hálózat napenergiát tárol.", "In the event that the sun shines, the grid stores solar energy."]
                ],
                "examples": [
                    {"spanish": "Abban az esetben, ha az ipari beruházás nem veszélyezteti a talajvizet, a hatóság kiadja az engedélyt.", "english": "In the event that the industrial investment does not endanger groundwater, the authority issues the permit."},
                    {"spanish": "A város hozzájárult a bővítéshez, azzal a kikötéssel, hogy folyamatos online monitoringot biztosítsanak.", "english": "The city consented to the expansion, with the stipulation that they provide continuous online monitoring."},
                    {"spanish": "Abban az esetben, ha megnő a villamosenergia-fogyasztás, a gázerőművek segítik a hálózatot.", "english": "In the event that electricity consumption increases, gas power plants support the grid."}
                ],
                "tip": "Distinguish indicative from subjunctive: 'azzal a feltétellel, hogy megcsinálja' (factual/conditional) vs. 'azzal a kikötéssel, hogy megcsinálja / megcsinálhassa' (normative requirement)."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["zöld átállás", "green transition"],
                        ["akkumulátorgyártás", "battery manufacturing"],
                        ["energiahálózat", "energy grid"],
                        ["megújuló energia", "renewable energy"],
                        ["ipari beruházás", "industrial investment"],
                        ["környezeti terhelés", "environmental impact"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Milyen környezeti aggályok merültek fel a nagyszabású magyarországi akkumulátorgyárak építése kapcsán?",
                    [
                        "A hatalmas ipari vízigény és a talajvízkészletek esetleges elszennyeződésének kockázata.",
                        "A gyárak miatt hirtelen beköszöntő sarki fagyok és hóviharok veszélye.",
                        "A napelemek által kibocsátott láthatatlan rádióhullámok elterjedése."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A megújuló napenergia terjedése miatt modernizálni kell az országos villamos _____, hogy kezelni lehessen a csúcsokat.",
                    "energiahálózatot",
                    "Due to the expansion of renewable solar energy, the national electricity grid must be modernized to manage peaks.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik kötőszó fejezi ki legpontosabban a szigorú hatósági előírást? 'A hatóság jóváhagyta a beruházást, _____ a kikötéssel, hogy zárt víztisztító rendszert építenek ki.'",
                    ["azzal", "annak", "ebben", "arról"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "_____ az esetben, ha a gyár túllépi a kibocsátási határértéket, a termelést azonnal fel kell függeszteni.",
                    "Abban",
                    "In the event that the factory exceeds the emission threshold, production must be suspended immediately.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "beruházást", "jóváhagyták,", "azzal", "a", "kikötéssel,", "hogy", "óvják", "a", "vizeket."],
                    ["A", "beruházást", "jóváhagyták,", "azzal", "a", "kikötéssel,", "hogy", "óvják", "a", "vizeket."],
                    "The investment was approved, with the stipulation that they protect the waters.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Környezetvédő", "text": "Hogyan egyeztethető össze az ipari növekedés a természeti kincsek védelmével Debrecenben?"},
                        {"speaker": "Mérnök", "text": "_____"}
                    ],
                    [
                        "Csak úgy, ha a gyárak a legszigorúbb zárt technológiákat alkalmazzák, azzal a kikötéssel, hogy a lakosság folyamatosan ellenőrizheti a mérési adatokat.",
                        "Sehogy, a törvények szerint a gyárakban nem szabad semmilyen környezetvédelmi szűrőt felszerelni.",
                        "A környezetvédelem automatikusan megoldódik, ha több autót adnak el külföldön."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Miért jelent komoly mérnöki feladatot a napenergia hálózati integrációja Magyarországon?",
                    [
                        "Mert a napsütéses időszakban megtermelt áramfelesleget hatékonyan kell tárolni és elosztani a fogyasztók között.",
                        "Mert a napelemek meggátolják a felhők képződését és elállítják az esőt a mezőgazdaság elől.",
                        "Mert a napenergiát tilos villanyvezetékeken szállítani az európai szabványok szerint."
                    ],
                    0
                )
            ]
        },
        {
            "num": 5,
            "title": "The Future of Medium-Sized Languages in the Digital Age",
            "grammar_label": "Synthesis of speculative conditionals in future linguistic foresight",
            "goals": [
                "I can discuss the future viability of medium-sized European languages like Hungarian in a digitized world.",
                "I can synthesize speculative conditional clauses with confidence across hypothetical arguments.",
                "I can advocate for mother-tongue scientific education and digital language corpus expansion."
            ],
            "story_segment": {
                "seg_slug": "kozepesnyelvekjovoje",
                "title": "A közepes méretű nyelvek jövője a digitális korban",
                "summary": "Will Hungarian thrive in the era of multimodal AI? Linguists argue that maintaining Hungarian scientific and technical vocabulary is vital for democratic thought and cultural autonomy.",
                "location": "Budapest (MTA Székház) és nemzetközi kutatóműhelyek",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A digitális forradalom és az angol nyelvű globális technológiai dominancia korában alapvető kérdéssé vált a világ közepes méretű nyelveinek – köztük a mintegy tizenhárom-tizennégymillió ember által beszélt magyarnak – a jövője. A jövőkutatók és nyelvészek figyelmeztetnek: a digitális kihalás veszélye nem pusztán a kis törzsi nyelveket fenyegeti, hanem azokat a nyelveket is, amelyek nem képesek megjelenni a modern digitális térben."
                    },
                    {
                        "type": "narration",
                        "text": "Ha egy nyelv nem rendelkezik megfelelő digitális infrastruktúrával, nagy méretű szövegkorpuszokkal és mesterséges intelligencia eszközökkel, fokozatosan elveszítheti funkcióit. Előbb a tudományos publikációk, majd a technológiai fejlesztések, végül a mindennapi ügyintézés szférájából is kiszorulhat, visszaszorulva a tisztán családi és folklórhasználatra."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar tudományos közösség és a Magyar Tudományos Akadémia határozottan küzd e folyamat ellen. A hazai egyetemeken és kutatóintézetekben tudatos nyelvstratégia érvényesül: a legújabb technológiai vívmányoknak azonnal megalkotják a pontos és elegáns magyar megfelelőit, elkerülve a szolgalelkű idegennyelv-használatot."
                    },
                    {
                        "type": "narration",
                        "text": "Az anyanyelvi tudományosság megőrzése a demokratikus társadalom alapfeltétele. Feltéve, ha a polgárok a saját anyanyelvükön érthetik meg a mesterséges intelligencia, a géntechnológia és a klímaváltozás kérdéseit, érdemben részt vehetnek a jövőjüket formáló társadalmi döntésekben."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar nyelv évezredeken át bizonyította rendkívüli életképességét és megújulási erejét. Ha a mai nemzedékek is elkötelezetten bővítik a digitális korpuszokat és ápolják az anyanyelvi műveltséget, a magyar nyelv a huszonegyedik század technológiai környezetében is virágzó, teljes értékű európai kultúrnyelv marad."
                    }
                ]
            },
            "words": [
                {"lemma": "nyelvi vitalitás", "translation": "linguistic vitality", "pos": "expression"},
                {"lemma": "digitális nyelvmegőrzés", "translation": "digital language preservation", "pos": "expression"},
                {"lemma": "nyelvtechnológiai hátrány", "translation": "language technology deficit / gap", "pos": "expression"},
                {"lemma": "digitális korpusz", "translation": "digital corpus", "pos": "expression"},
                {"lemma": "anyanyelvi műveltség", "translation": "mother-tongue literacy / cultural literacy", "pos": "expression"},
                {"lemma": "jövőkutatás", "translation": "futurology / foresight studies", "pos": "noun"}
            ],
            "grammar_doc": {
                "slug": "speculative-synthesis-foresight",
                "title": "Synthesizing Speculative and Hypothetical Conditional Structures",
                "text1_title": "Multi-Tiered Conditional Stacking in Futurology",
                "text1": "Foresight analysis synthesizes multiple conditional layers to weigh alternative scenarios. By combining 'feltéve, ha...', 'amennyiben...', 'hacsak nem...', and counterfactual reflections, an author evaluates complex probabilistic futures without asserting dogmatic certainty.",
                "text2_title": "Integrating the Past Counterfactual with Future Speculation",
                "text2": "Advanced B2 discourse weaves historical counterfactual lessons directly into forward-looking speculation: 'Ha korábban nem hozták volna létre az akadémiai szótárakat, a nyelv mára elveszítette volna rugalmasságát; feltéve viszont, ha most fektetünk be az MI-be, a nyelv virágozni fog.'",
                "table_title": "Comprehensive Speculative Conditional Connectors",
                "table_rows": [
                    ["feltéve, ha...", "assuming that / provided that..."],
                    ["azzal a feltétellel, hogy...", "on condition that..."],
                    ["amennyiben...", "in the event that... / insofar as..."],
                    ["hacsak nem...", "unless / except if..."],
                    ["abban az esetben, ha...", "in the case that / should it happen that..."]
                ],
                "examples": [
                    {"spanish": "A közepes méretű nyelvek fennmaradnak, feltéve, ha a digitális korban is biztosítják a technológiai hátterüket.", "english": "Medium-sized languages will survive, provided that their technological backing is ensured in the digital age as well."},
                    {"spanish": "A nyelv visszaszorulhat, hacsak nem fordítanak kellő figyelmet az anyanyelvi oktatásra és a korpuszépítésre.", "english": "The language may recede, unless they pay sufficient attention to mother-tongue education and corpus building."},
                    {"spanish": "Amennyiben megőrizzük a magyar szakkifejezéseket, a társadalmi párbeszéd nyitott és demokratikus marad.", "english": "Insofar as we preserve Hungarian technical terms, public dialogue will remain open and democratic."}
                ],
                "tip": "Mastering the interplay between real conditionals (jelen idejű feltétel), hypothetical conditionals (feltételes jelen), and counterfactuals (feltételes múlt) marks the transition from B2 competence to C1 mastery."
            },
            "exercises": [
                match(
                    "vocabulary",
                    "introduce",
                    [
                        ["nyelvi vitalitás", "linguistic vitality"],
                        ["digitális nyelvmegőrzés", "digital language preservation"],
                        ["nyelvtechnológiai hátrány", "language technology gap"],
                        ["digitális korpusz", "digital corpus"],
                        ["anyanyelvi műveltség", "mother-tongue literacy"],
                        ["jövőkutatás", "futurology"]
                    ],
                    [VOCAB_SKILL]
                ),
                mc(
                    "vocabulary",
                    "controlled",
                    "Mi fenyegeti leginkább a közepes méretű nemzeti nyelveket a 21. századi digitális korban?",
                    [
                        "A digitális hátrány és funkcióvesztés, ha nem alakítanak ki saját nyelvtechnológiai eszközöket.",
                        "Az, hogy a könyvtárakból eltűnnek a papír alapú enciklopédiák.",
                        "Az, hogy az internetes szerverek kizárólag angol ábécével képesek adatot tárolni."
                    ],
                    0,
                    [VOCAB_SKILL]
                ),
                fb(
                    "vocabulary",
                    "controlled",
                    "A magyar nyelv kutatásához és a mesterséges intelligencia fejlesztéséhez hatalmas méretű szövegeket tartalmazó _____ van szükség.",
                    "digitális korpuszra",
                    "For the research of the Hungarian language and development of artificial intelligence, a digital corpus containing huge texts is needed.",
                    [VOCAB_SKILL]
                ),
                mc(
                    "grammar",
                    "controlled",
                    "Melyik összetett feltételes kifejezés illik leginkább a jövőbeli tudományos előrejelzésbe? 'A magyar nyelv digitálisan életképes marad, _____ elegendő forrást biztosítanak a nyelvtechnológiai kutatásokra.'",
                    ["feltéve, ha", "habár", "jóllehet", "minthogy"],
                    0,
                    [GRAMMAR_SKILL]
                ),
                fb(
                    "grammar",
                    "practice",
                    "A szakemberek szerint a nyelv elveszítheti technológiai funkcióit, _____ nem fektetnek be a nemzeti nyelvi modellekbe.",
                    "hacsak",
                    "According to experts, the language may lose its technological functions, unless they invest in national language models.",
                    [GRAMMAR_SKILL]
                ),
                sb(
                    "grammar",
                    "practice",
                    ["A", "nyelv", "virágozni", "fog,", "feltéve,", "ha", "ápoljuk", "az", "anyanyelvi", "műveltséget."],
                    ["A", "nyelv", "virágozni", "fog,", "feltéve,", "ha", "ápoljuk", "az", "anyanyelvi", "műveltséget."],
                    "The language will flourish, provided that we cultivate mother-tongue literacy.",
                    [GRAMMAR_SKILL]
                ),
                dc(
                    "dialogue",
                    [
                        {"speaker": "Egyetemista", "text": "Miért nem elegendő, ha minden tudományos cikket közvetlenül angolul írunk meg?"},
                        {"speaker": "Nyelvészprofesszor", "text": "_____"}
                    ],
                    [
                        "Mert ha feladjuk a magyar szókincset a tudományban, a társadalom többsége nem fogja érteni a saját jövőjét érintő döntéseket.",
                        "Mert a nemzetközi folyóiratok szigorúan büntetik a túl jó angol nyelvtudást.",
                        "Mert a magyar törvények kizárólag a latin nyelvű orvosi könyveket ismerik el."
                    ],
                    0,
                    [GRAMMAR_SKILL]
                ),
                mc(
                    "reading",
                    "reading",
                    "Miért tekinti a Magyar Tudományos Akadémia a magyar szakkifejezések megalkotását nemzeti prioritásnak?",
                    [
                        "Mert így a magyar nyelv az élet minden területén teljes értékű, önálló kultúrnyelv marad.",
                        "Mert ezzel teljesen ki lehet szorítani az internetet a Kárpát-medencéből.",
                        "Mert a külföldi kutatóknak tilos magyar szavakat tanulniuk."
                    ],
                    0
                )
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can synthesize the trajectory of 21st-century Hungarian science from attosecond physics to large language models.",
            "I can effortlessly deploy multi-layered speculative and counterfactual conditionals across complex technical topics.",
            "I can articulate arguments concerning digital language preservation, green transition, and national innovation clusters."
        ],
        "exercises": [
            match(
                "vocabulary",
                "recognize",
                [
                    ["attoszekundumos fizika", "attosecond physics"],
                    ["lézerinfrastruktúra", "laser infrastructure"],
                    ["mesterséges intelligencia", "artificial intelligence"],
                    ["nagy nyelvi modell", "large language model"],
                    ["zöld átállás", "green transition"],
                    ["digitális korpusz", "digital corpus"]
                ],
                [VOCAB_SKILL]
            ),
            mc(
                "vocabulary",
                "recognize",
                "Melyik kutatóintézet képviseli Magyarországon a legmagasabb szintű ultrarövid lézeres kutatási infrastruktúrát?",
                ["ELI-ALPS Szeged", "Nemzeti Színház", "Országos Széchényi Könyvtár", "Fekete Lyuk Klub"],
                0,
                [VOCAB_SKILL]
            ),
            fb(
                "vocabulary",
                "recognize",
                "A magyar nyelv számítógépes feldolgozásához elengedhetetlen a szabályalapú _____ alkalmazása a szavak felbontásához.",
                "morfológiai elemzők",
                "For computational processing of the Hungarian language, applying morphological analyzers is indispensable for decomposing words.",
                [VOCAB_SKILL]
            ),
            mc(
                "grammar",
                "recall",
                "Melyik mondat fejezi ki helyesen a 'feltéve, ha' szerkezetet tudományos összefüggésben?",
                [
                    "A daganatos sejtek korán kimutathatók, feltéve, ha a lézeres vizsgálat kellően érzékeny.",
                    "A daganatos sejtek korán kimutathatók, jóllehet a lézeres vizsgálat kellően érzékeny.",
                    "A daganatos sejtek korán kimutathatók, noha a lézeres vizsgálat kellően érzékeny.",
                    "A daganatos sejtek korán kimutathatók, minthogy a lézeres vizsgálat kellően érzékeny."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            fb(
                "grammar",
                "recall",
                "Amennyiben a nemzetközi konzorcium támogatja a projektet, a kísérleti méréseket jövő hónapban megkezdik a szegedi _____ .",
                "laboratóriumokban",
                "In the event that the international consortium supports the project, experimental measurements will begin next month in the Szeged laboratories.",
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Fizikus", "text": "Hogyan értékeled Krausz Ferenc Nobel-díjának jelentőségét a hazai kutatókra nézve?"},
                    {"speaker": "Kutató", "text": "_____"}
                ],
                [
                    "Hatalmas inspirációt jelent, hiszen bebizonyította, hogy a hazai alapokra építve a legmagasabb globális tudományos csúcsok is elérhetők.",
                    "Semmilyen hatása sincs, mert a fizikai kísérletek nem kapcsolódnak a magyar kultúrához.",
                    "Csak annyit jelent, hogy a jövőben tilos lesz fizikát tanítani a középiskolákban."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Környezetvédő", "text": "Hogyan védhetők meg a természeti erőforrások az akkumulátorgyárak építése során?"},
                    {"speaker": "Szakértő", "text": "_____"}
                ],
                [
                    "Abban az esetben, ha a hatóságok a legszigorúbb monitoringot írják elő, a környezeti kockázatok hatékonyan minimalizálhatók.",
                    "Kizárólag úgy, ha minden ipari termelést végleg beszüntetünk az egész kontinensen.",
                    "A gyáraknak nincs semmilyen hatása a környezetre, ezért felesleges vizsgálatokat végezni."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            mc(
                "grammar",
                "in-context",
                "Melyik kötőszó fejezi ki a legpontosabban a kivételt vagy korlátozást az alábbi mondatban? 'A villamosenergia-hálózat stabil marad, _____ nem következik be hirtelen üzemzavar az egyik erőműben.'",
                ["hacsak", "bár", "minthogy", "jóllehet"],
                0,
                [GRAMMAR_SKILL]
            ),
            dc(
                "dialogue",
                [
                    {"speaker": "Újságíró", "text": "Miért van szükség saját magyar nagy nyelvi modellre a mesterséges intelligencia korában?"},
                    {"speaker": "Informatikus", "text": "_____"}
                ],
                [
                    "Mert a magyar nyelv digitális szuverenitása garantálja, hogy kulturális értékeink és anyanyelvünk a jövő technológiáiban is megmaradjanak.",
                    "Mert az amerikai modellek törvényben tiltják a magyar szövegek lefordítását.",
                    "Mert a számítógépek csak akkor működnek, ha kizárólag magyar fejlesztésű chipek vannak bennük."
                ],
                0,
                [GRAMMAR_SKILL]
            ),
            sb(
                "grammar",
                "produce",
                ["A", "kutatás", "sikeres", "lesz,", "feltéve,", "ha", "biztosítják", "a", "megfelelő", "finanszírozást."],
                ["A", "kutatás", "sikeres", "lesz,", "feltéve,", "ha", "biztosítják", "a", "megfelelő", "finanszírozást."],
                "The research will be successful, provided that they ensure appropriate financing.",
                [GRAMMAR_SKILL]
            ),
            sb(
                "grammar",
                "produce",
                ["Ha", "nem", "fektettek", "volna", "a", "lézerekbe,", "Szeged", "nem", "vált", "volna", "központtá."],
                ["Ha", "nem", "fektettek", "volna", "a", "lézerekbe,", "Szeged", "nem", "vált", "volna", "központtá."],
                "If they had not invested in lasers, Szeged would not have become a hub.",
                [GRAMMAR_SKILL]
            ),
            sw(
                "produce",
                [
                    {
                        "prompt": "Write a sentence using 'feltéve, ha...' or 'azzal a feltétellel, hogy...' discussing a scientific hypothesis or research project.",
                        "answer": "A kísérlet eredményei megbízhatónak tekinthetők, feltéve, ha a laboratóriumi méréseket független kutatócsoportok is meg tudják ismételni."
                    },
                    {
                        "prompt": "Write a sentence formulating a counterfactual condition in the past (using 'ha... volna, akkor... lett volna') regarding linguistic or technological development.",
                        "answer": "Ha a magyar kutatók nem fektettek volna ekkora energiát a digitális korpuszok építésébe, a hazai nyelvtechnológia mára menthetetlenül lemaradt volna a nemzetközi élmezőnytől."
                    }
                ],
                [GRAMMAR_SKILL]
            )
        ]
    }
}
