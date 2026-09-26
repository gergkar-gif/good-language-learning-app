#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 22, 23, and 24:
  - Unit 22: b2-demografia (Demographics, Family Policy & Generational Shifts)
  - Unit 23: b2-lakhatas (Courtyards, Panel Estates & Urban Renewal)
  - Unit 24: b2-kornyezetpolitika (The Blue Danube: Ecology, Dams & Civic Awakening)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402


UNIT_22_DEMOGRAFIA = {   'unit_num': 22,
    'slug': 'demografia',
    'title': 'Demographics, Family Policy & Generational Shifts',
    'grammar_skill': 'b2-temporal-framing',
    'vocab_skill': 'b2-demografia-vocab',
    'theme': 'Demographics, family policy and intergenerational ties',
    'location': 'Budapest és a vidéki városok',
    'intro_body': [   'In the twentieth and twenty-first centuries, few subjects in Hungarian public discourse have '
                      'sparked such intense policy experimentation and demographic anxiety as birth rates, '
                      'generational succession, and the evolving structure of the family. From the drastic '
                      'administrative measures of the early 1950s to the pioneering introduction of child-care '
                      'allowances and contemporary tax incentives, the Hungarian state has repeatedly attempted to '
                      'steer demographic trends.',
                      'Across these five lessons, you will examine the socio-historical reality of the baby boom known '
                      'as the Ratkó era, explore the revolutionary social impact of GYES in 1967, analyze contemporary '
                      'family policies and housing subsidies, inspect the growing challenges of an aging society and '
                      'eldercare, and hear how young Hungarians navigate parenthood and career today. Grammatically, '
                      'you will master formal temporal framing postpositions (során, folyamán, múltával, elteltével) '
                      'and anteriority clauses introduced by mire.'],
    'combined_story_title': 'A Ratkó-korszaktól a 21. századi családokig',
    'combined_story_summary': "Hungary's demographic trajectory from the 1950s Ratkó generation and the 1967 "
                              'introduction of GYES to modern family policies, longevity, and changing household '
                              'patterns.',
    'lessons': [   {   'num': 1,
                       'title': 'The Ratkó Era and Generational Waves',
                       'grammar_label': "Temporal framing with során and folyamán ('during / in the course of')",
                       'goals': [   'I can explain the historical context and demographic consequences of the Ratkó '
                                    'era in 1950s Hungary.',
                                    'I can distinguish and properly use során and folyamán to frame historical '
                                    'processes and extended time spans.',
                                    'I can discuss baby booms, demographic cohorts, and state intervention using B2 '
                                    'Hungarian vocabulary.'],
                       'story_segment': {   'seg_slug': 'ratkokorszak',
                                            'title': 'A Ratkó-korszak demográfiai hullámai',
                                            'summary': 'Between 1950 and 1956, strict anti-abortion measures and a '
                                                       'childlessness tax introduced under Health Minister Anna Ratkó '
                                                       'generated a sudden baby boom whose generational waves rippled '
                                                       'through Hungarian society for decades.',
                                            'location': 'Budapest és az iparvárosok (1950–1956)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'Az 1950-es évek elején a Rákosi-korszak '
                                                                          'totalitárius hatalomgyakorlása a magánélet '
                                                                          'legszemélyesebb szférájába is drasztikusan '
                                                                          'beavatkozott. Ratkó Anna népjóléti, majd '
                                                                          'egészségügyi miniszter hivatali ideje alatt '
                                                                          'a kormány szigorúan betiltotta a '
                                                                          'terhességmegszakítást, és bevezette a '
                                                                          'gyermektelenségi adót a húsz év feletti '
                                                                          'egyedülállók és gyermektelen házaspárok '
                                                                          'számára.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Ezen adminisztratív kényszerintézkedések '
                                                                          'következtében a születések száma 1953 és '
                                                                          '1955 között példátlan mértékben megugrott: '
                                                                          'évente több mint kétszázezer gyermek jött a '
                                                                          'világra. A szülészeteken ágyhiány alakult '
                                                                          'ki, a folyosókon is újszülöttek feküdtek, '
                                                                          'és a korabeli propaganda a szocialista jövő '
                                                                          'diadalaként ünnepelte a népesedési '
                                                                          'rekordokat.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Az így született nemzedéket a köznyelv máig '
                                                                          '„Ratkó-gyerekekként” emlegeti. Amikor ez a '
                                                                          'rendkívül népes kohorsz az iskoláskorba '
                                                                          'lépett, az oktatási infrastruktúra nem '
                                                                          'bírta a terhelést: a tantermek túlzsúfolttá '
                                                                          'váltak, és sok általános iskolában '
                                                                          'délelőtti és délutáni váltásban '
                                                                          'kényszerültek tanítani a diákokat.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A demográfiai hullámverés a munkaerőpiacon '
                                                                          'és a lakásgazdálkodásban is éreztette '
                                                                          'hatását, amikor a fiatal felnőttek az '
                                                                          '1970-es években munkába álltak és önálló '
                                                                          'lakást kerestek. Az új szocialista '
                                                                          'iparvárosok, mint Dunaújváros és '
                                                                          'Kazincbarcika, valamint a felépülő panel '
                                                                          'lakótelepek nagyrészt ennek a hatalmas '
                                                                          'korosztálynak a letelepítését szolgálták.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A demográfusok elemzései kimutatták, hogy a '
                                                                          'mesterségesen előidézett születési csúcsot '
                                                                          'az 1970-es évek közepén egy újabb, kisebb '
                                                                          'hullám követte — a „Ratkó-unokák” korszaka '
                                                                          '—, ám az adminisztratív eszközökkel '
                                                                          'kikényszerített családpolitika hosszú távon '
                                                                          'nem tudta megállítani a modern '
                                                                          'urbanizációval járó népességfogyást.'}]},
                       'words': [   {   'lemma': 'demográfiai hullám',
                                        'translation': 'demographic wave / baby boom wave',
                                        'pos': 'noun'},
                                    {   'lemma': 'Ratkó-korszak',
                                        'translation': 'Ratkó era (1950–1956 Hungarian baby boom period)',
                                        'pos': 'noun'},
                                    {   'lemma': 'gyermekvállalás',
                                        'translation': 'childbearing / having children',
                                        'pos': 'noun'},
                                    {   'lemma': 'korfa',
                                        'translation': 'population pyramid / age structure',
                                        'pos': 'noun'},
                                    {   'lemma': 'termékenységi arányszám',
                                        'translation': 'total fertility rate',
                                        'pos': 'noun'},
                                    {   'lemma': 'népességfogyás',
                                        'translation': 'population decline / depopulation',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'soran-folyaman-framing',
                                          'title': "Temporal Framing with során and folyamán ('during / in the course "
                                                   "of')",
                                          'text1_title': 'Nuances of Process vs. Duration',
                                          'text1': 'In formal Hungarian historical and sociological prose, során and '
                                                   'folyamán replace the everyday prepositional postposition alatt. '
                                                   'While both govern noun phrases expressing extended temporal '
                                                   'phenomena, során emphasizes internal phases or actions within a '
                                                   'process (a népszámlálás során, a kutatás során), whereas folyamán '
                                                   'stresses continuous progress across a stretch of time (az '
                                                   'évtizedek folyamán, a korszak folyamán).',
                                          'text2_title': 'Word Order and Register',
                                          'text2': 'Both postpositions follow their noun without an intervening '
                                                   "article: 'A reformok során sok új bölcsőde nyílt.' When the noun "
                                                   'possesses an adjectival modifier or demonstrative, the '
                                                   "postposition still sits at the phrase boundary: 'Ezen intézkedések "
                                                   "során a születésszám hirtelen megugrott.'",
                                          'table_title': 'Temporal Contrast: során vs. folyamán',
                                          'table_rows': [   [   'Az 1950-es évek folyamán ugrásszerűen megnőtt a '
                                                                'születésszám.',
                                                                'In the course of the 1950s, the number of births '
                                                                'abruptly increased.'],
                                                            [   'A demográfiai vizsgálat során feltárták a korszak '
                                                                'torzulásait.',
                                                                'During the demographic investigation, they uncovered '
                                                                'the distortions of the era.'],
                                                            [   'Az évtizedek folyamán a magyar korfa alapvetően '
                                                                'elöregedett.',
                                                                'Over the course of the decades, the Hungarian age '
                                                                'pyramid fundamentally aged.']],
                                          'examples': [   {   'spanish': 'A Ratkó-korszak folyamán több mint félmillió '
                                                                         'gyermek született.',
                                                              'english': 'In the course of the Ratkó era, more than '
                                                                         'half a million children were born.'},
                                                          {   'spanish': 'A kórházi vizitek során az orvosok súlyos '
                                                                         'helyhiánnyal szembesültek.',
                                                              'english': 'During the hospital rounds, doctors faced '
                                                                         'severe shortages of space.'},
                                                          {   'spanish': 'A tárgyalások folyamán a kormányzat '
                                                                         'módosította a büntető törvénykönyvet.',
                                                              'english': 'Over the course of the negotiations, the '
                                                                         'government amended the penal code.'}],
                                          'tip': 'Use folyamán when emphasizing temporal lapse through calendar '
                                                 'periods (évek folyamán, század folyamán) and során when highlighting '
                                                 'procedural steps or human activities (vizsgálat során, építkezés '
                                                 'során).'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-demografia-vocab'],
                                            'pairs': [   ['demográfiai hullám', 'demographic baby boom wave'],
                                                         ['Ratkó-korszak', '1950–1956 Hungarian baby boom period'],
                                                         ['gyermekvállalás', 'childbearing / having children'],
                                                         ['korfa', 'population age structure pyramid'],
                                                         ['termékenységi arányszám', 'total fertility rate'],
                                                         ['népességfogyás', 'population decline']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'question': 'Mely intézkedések vezettek a születésszám hirtelen '
                                                        'megugrásához az 1950-es évek elején Magyarországon?',
                                            'options': [   'A terhességmegszakítás szigorú tiltása és a '
                                                           'gyermektelenségi adó bevezetése.',
                                                           'A modern bölcsődék és óvodák azonnali, tömeges felépítése.',
                                                           'A nyugdíjkorhatár drasztikus felemelése és a tandíjak '
                                                           'eltörlése.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'sentence': 'A demográfusok a nemzeti _____ alakjából pontosan le tudják '
                                                        'olvasni a korábbi évtizedek születési hullámait.',
                                            'answer': 'korfa',
                                            'english': 'Demographers can accurately read the birth waves of previous '
                                                       'decades from the shape of the national population pyramid.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-temporal-framing'],
                                            'question': 'Melyik névutó fejezi ki a legpontosabban a folyamatos időbeli '
                                                        "előrehaladást az alábbi mondatban? 'Az 1950-es évek ____ a "
                                                        "magyar társadalom szerkezete mélyrehatóan átalakult.'",
                                            'options': ['folyamán', 'helyett', 'gyanánt', 'végett'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'sentence': 'A részletes népszámlálás _____ a szakemberek megállapították '
                                                        'a születésszám növekedését.',
                                            'answer': 'során',
                                            'english': 'During the detailed census, specialists determined the '
                                                       'increase in the birth rate.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'tiles': [   'Az',
                                                         'évtizedek',
                                                         'folyamán',
                                                         'a',
                                                         'korfa',
                                                         'szerkezete',
                                                         'megváltozott.'],
                                            'solution': [   'Az',
                                                            'évtizedek',
                                                            'folyamán',
                                                            'a',
                                                            'korfa',
                                                            'szerkezete',
                                                            'megváltozott.'],
                                            'english': 'Over the course of the decades, the structure of the '
                                                       'population pyramid changed.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-temporal-framing'],
                                            'prompt': [   {   'speaker': 'Történész',
                                                              'text': 'Hogyan jellemezné a Ratkó-korszak hosszú távú '
                                                                      'demográfiai következményeit?'},
                                                          {'speaker': 'Demográfus', 'text': '_____'}],
                                            'options': [   'Az évtizedek folyamán a hirtelen születési hullám átmeneti '
                                                           'túlzsúfoltságot okozott az iskolákban, később pedig a '
                                                           'munkaerőpiacon.',
                                                           'A korszak folyamán senki sem akart családot alapítani a '
                                                           'falvakban.',
                                                           'A népesség száma felére csökkent a gyermektelenségi adó '
                                                           'miatt.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan oldották meg a túlzsúfolt általános iskolák a '
                                                        'Ratkó-gyerekek oktatását az 1960-as évek elején?',
                                            'options': [   'Délelőtti és délutáni váltásban tanították a diákokat a '
                                                           'tanteremhiány miatt.',
                                                           'Minden diákot azonnal egyetemre küldtek tanulni.',
                                                           'Kizárólag otthoni távoktatást vezettek be az egész '
                                                           'országban.'],
                                            'correct': 0}]},
                   {   'num': 2,
                       'title': 'Pioneering Parental Leave: The History of GYES',
                       'grammar_label': "Time-lapse and anteriority postpositions with múltával and elteltével ('after "
                                        "the lapse of')",
                       'goals': [   'I can explain the significance of the 1967 introduction of the child-care '
                                    'allowance (GYES) in Hungarian social history.',
                                    'I can use múltával and elteltével to express temporal lapse and deferred outcomes '
                                    'in formal Hungarian.',
                                    'I can describe maternity leave, employment security, and state family benefits '
                                    'using appropriate terms.'],
                       'story_segment': {   'seg_slug': 'gyestortenet',
                                            'title': 'A GYES forradalma: Otthon és munkahely között',
                                            'summary': "Introduced in 1967, Hungary's pioneering child-care allowance "
                                                       '(GYES) granted mothers a 3-year state-funded parental leave '
                                                       'with guaranteed job reinstatement, fundamentally altering '
                                                       'gender roles and maternal employment in Central Europe.',
                                            'location': 'Budapest és a gyárvárosok (1967–1985)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'Az 1960-as évek közepére a magyar nők '
                                                                          'foglalkoztatottsága az iparosítás '
                                                                          'következtében elérte a legmagasabb európai '
                                                                          'szintet, miközben a születésszám az 1962-es '
                                                                          'mélyponton aggasztó mértékben visszaesett. '
                                                                          'A bölcsődei férőhelyek elégtelensége és a '
                                                                          'dolgozó anyák kettős terhelése sürgető '
                                                                          'intézkedést kívánt a politikai vezetéstől.'},
                                                              {   'type': 'narration',
                                                                  'text': '1967 januárjában lépett életbe a '
                                                                          'gyermekgondozási segély, vagyis a GYES, '
                                                                          'amely nemzetközi összehasonlításban is '
                                                                          'forradalmi újításnak számított. A '
                                                                          'jogszabály lehetővé tette, hogy az '
                                                                          'édesanyák a gyermek hároméves koráig otthon '
                                                                          'maradjanak havi fix állami támogatás '
                                                                          'mellett, miközben a munkáltató köteles volt '
                                                                          'megőrizni munkahelyüket.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A társadalmi fogadtatás rendkívül kedvező '
                                                                          'volt: már az első években a jogosult nők '
                                                                          'több mint kétharmada élt a lehetőséggel. A '
                                                                          'GYES elterjedése enyhítette a '
                                                                          'csecsemőotthonok és bölcsődék '
                                                                          'túlterheltségét, és lehetőséget teremtett a '
                                                                          'közvetlen anya-gyermek kapcsolat '
                                                                          'elmélyítésére a legfogékonyabb korai '
                                                                          'életszakaszban.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A rendszer fejlődésének újabb '
                                                                          'mérföldköveként 1985-ben bevezették a '
                                                                          'gyermekgondozási díjat (GYED), amely már '
                                                                          'nem fix összegű segélyként, hanem a korábbi '
                                                                          'fizetéshez igazodó, keresetpótló '
                                                                          'juttatásként működött. Ez az intézkedés a '
                                                                          'magasabb végzettségű nők számára is '
                                                                          'vonzóbbá tette a gyermekvállalást a karrier '
                                                                          'feladása nélkül.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Bár a szociológusok elismerték a GYES '
                                                                          'vitathatatlan érdemeit a családok anyagi '
                                                                          'biztonságában, sokan rámutattak a '
                                                                          'visszásságokra is: a három év múltával '
                                                                          'esedékes visszatérés a munkaerőpiacra '
                                                                          'gyakran törést okozott a nők szakmai '
                                                                          'előmenetelében, és megerősítette a '
                                                                          'hagyományos nemi szerepmegosztást.'}]},
                       'words': [   {   'lemma': 'gyermekgondozási segély',
                                        'translation': 'childcare allowance (GYES, flat-rate parental benefit)',
                                        'pos': 'noun'},
                                    {'lemma': 'munkaerőpiac', 'translation': 'labor market', 'pos': 'noun'},
                                    {   'lemma': 'munkába állás',
                                        'translation': 'entering the workforce / return to work',
                                        'pos': 'noun'},
                                    {'lemma': 'keresetpótló', 'translation': 'income-replacing', 'pos': 'adjective'},
                                    {   'lemma': 'bölcsődei ellátás',
                                        'translation': 'crèche / infant day-care provision',
                                        'pos': 'noun'},
                                    {   'lemma': 'hivatástudat',
                                        'translation': 'professional vocation / career commitment',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'multaval-elteltevel-lapse',
                                          'title': "Expressing Elapsed Time with múltával and elteltével ('after the "
                                                   "lapse of')",
                                          'text1_title': 'High-Register Time-Lapse Postpositions',
                                          'text1': 'To express that an event or consequence occurs after a specified '
                                                   'period of time has elapsed, formal B2 Hungarian employs múltával '
                                                   '(derived from the verb múlik) and elteltével (from eltelik). Both '
                                                   'postpositions attach to a time expression with a possessive '
                                                   "suffix: 'három év múltával' (after the passage of three years), "
                                                   "'néhány hónap elteltével' (with the lapse of a few months).",
                                          'text2_title': 'Contrast with után',
                                          'text2': 'While the postposition után can follow any noun (az ebéd után, a '
                                                   'háború után), múltával and elteltével can ONLY be used with '
                                                   'expressions of quantified duration (napok, hetek, hónapok, évek). '
                                                   'They confer an elevated, precise tone essential for legal, '
                                                   'biographical, and demographic writing.',
                                          'table_title': 'Forming Time-Lapse Postpositions',
                                          'table_rows': [   [   'Három év múltával az anyák visszatérhettek '
                                                                'munkahelyükre.',
                                                                'With the passage of three years, mothers could return '
                                                                'to their workplace.'],
                                                            [   'Néhány hónap elteltével a kormány kiterjesztette a '
                                                                'jogosultak körét.',
                                                                'After the lapse of a few months, the government '
                                                                'expanded the circle of beneficiaries.'],
                                                            [   'Egy évtized múltával világossá váltak a rendszer '
                                                                'strukturális korlátai.',
                                                                'With the passage of a decade, the structural limits '
                                                                'of the system became clear.']],
                                          'examples': [   {   'spanish': 'A törvény életbe lépése után, egy év '
                                                                         'múltával megduplázódott az igénylők száma.',
                                                              'english': 'After the law entered into force, with the '
                                                                         'passage of one year the number of applicants '
                                                                         'doubled.'},
                                                          {   'spanish': 'A szülési szabadság elteltével a nők új '
                                                                         'készségekkel tértek vissza hivatásukhoz.',
                                                              'english': 'Upon the lapse of maternity leave, women '
                                                                         'returned to their vocation with new skills.'},
                                                          {   'spanish': 'Hosszú évek múltával a GYES a magyar '
                                                                         'szociálpolitika alapintézményévé vált.',
                                                              'english': 'With the passage of long years, GYES became '
                                                                         'a cornerstone of Hungarian social policy.'}],
                                          'tip': 'Remember: múltával and elteltével require a quantified time noun: '
                                                 "use 'három év múltával', never '*az ülés múltával'."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-demografia-vocab'],
                                            'pairs': [   ['gyermekgondozási segély', 'childcare allowance (GYES)'],
                                                         ['munkaerőpiac', 'labor market'],
                                                         ['munkába állás', 'returning to employment'],
                                                         ['keresetpótló', 'income-replacing'],
                                                         ['bölcsődei ellátás', 'infant nursery provision'],
                                                         ['hivatástudat', 'professional career vocation']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'question': 'Miben különbözött az 1985-ben bevezetett GYED az 1967-es '
                                                        'GYES-től?',
                                            'options': [   'A GYED a korábbi munkabérhez igazodó, keresetpótló '
                                                           'juttatásként működött a fix összegű segély helyett.',
                                                           'A GYED kizárólag a nagyszülők számára volt elérhető a '
                                                           'nyugdíj mellett.',
                                                           'A GYED-et csak azok a családok kaphatták meg, akik nem '
                                                           'rendelkeztek lakással.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'sentence': 'A kisgyermekes anyák számára a sikeres _____ komoly kihívást '
                                                        'jelentett a hosszú otthonlét után.',
                                            'answer': 'munkába állás',
                                            'english': 'For mothers with young children, a successful return to work '
                                                       'presented a serious challenge after prolonged leave.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-temporal-framing'],
                                            'question': 'Melyik kifejezés fejezi ki a legválasztékosabban az időbeli '
                                                        "eltelést? 'A gyermek hároméves kora után, a törvényes időszak "
                                                        "_____ az anyák visszatértek dolgozni.'",
                                            'options': ['múltával', 'következtében', 'alapján', 'ellenére'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'sentence': 'Három év _____ a munkáltató köteles volt visszavenni a '
                                                        'dolgozót az eredeti pozíciójába.',
                                            'answer': 'múltával',
                                            'english': 'With the passage of three years, the employer was obliged to '
                                                       'take back the worker into the original position.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'tiles': [   'Néhány',
                                                         'hónap',
                                                         'elteltével',
                                                         'újabb',
                                                         'támogatást',
                                                         'vezettek',
                                                         'be.'],
                                            'solution': [   'Néhány',
                                                            'hónap',
                                                            'elteltével',
                                                            'újabb',
                                                            'támogatást',
                                                            'vezettek',
                                                            'be.'],
                                            'english': 'With the lapse of a few months, they introduced further '
                                                       'support.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-temporal-framing'],
                                            'prompt': [   {   'speaker': 'Kutató',
                                                              'text': 'Hogyan értékelik a szociológusok a GYES '
                                                                      'bevezetését a női karrierek szempontjából?'},
                                                          {'speaker': 'Történész', 'text': '_____'}],
                                            'options': [   'Három év múltával sok nő nehezen illeszkedett vissza a '
                                                           'munkahelyi hierarchiába, jóllehet a rendszer kiváló anyagi '
                                                           'biztonságot nyújtott.',
                                                           'Az intézkedés azonnal megszüntette az összes bölcsődét és '
                                                           'gyárat.',
                                                           'A nők többsége soha többé nem akart visszatérni a '
                                                           'munkaerőpiacra.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Miért számított nemzetközi szinten is forradalminak az '
                                                        '1967-ben bevezetett GYES?',
                                            'options': [   'Mert három évig fizetett állami támogatást nyújtott az '
                                                           'anyáknak a munkahelyük kötelező megőrzése mellett.',
                                                           'Mert minden gyermeknek automatikusan lakást adományozott a '
                                                           'születésekor.',
                                                           'Mert betiltotta a női munkavállalást az iparban.'],
                                            'correct': 0}]},
                   {   'num': 3,
                       'title': 'Modern Family Policies and Public Debate',
                       'grammar_label': "Anteriority clauses with mire ('by the time that') and aspectual completion",
                       'goals': [   'I can debate the mechanisms and societal impacts of modern Hungarian family tax '
                                    'credits, CSOK subsidies, and loans.',
                                    'I can construct complex temporal sentences using mire with perfective verb '
                                    'aspects.',
                                    'I can discuss tax allowances, home-buying subsidies, and demographic incentives '
                                    'using nuanced B2 terms.'],
                       'story_segment': {   'seg_slug': 'csaladpolitika',
                                            'title': 'Családtámogatás és lakáspolitika a mérlegen',
                                            'summary': 'Since 2010, Hungary has pursued an ambitious pro-natalist '
                                                       'policy combining income tax allowances, prenatal loans '
                                                       '(babaváró hitel), and housing subsidies (CSOK), generating '
                                                       'vibrant debates over social equity and demographic efficacy.',
                                            'location': 'Budapest, Parlament és agglomeráció (2010–2024)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A 2010-es évektől kezdődően a magyar '
                                                                          'kormányzat a családpolitikát állami '
                                                                          'működésének stratégiai középpontjába '
                                                                          'emelte. A demográfiai jövőkép célja a '
                                                                          'termékenységi arányszám tartós emelése '
                                                                          'lett, amely a 2011-es történelmi mélyponton '
                                                                          'mindössze 1,23 gyermeket jelentett '
                                                                          'nőnként.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A korábbi univerzális segélyezés helyett a '
                                                                          'támogatásokat döntően a bejelentett '
                                                                          'munkaviszonyhoz és az adófizetéshez '
                                                                          'kötötték. A családi adókedvezmény '
                                                                          'bevezetése révén a több gyermeket nevelő '
                                                                          'szülők jelentős jövedelemadó-mentességet '
                                                                          'kaptak, miközben a négygyermekes anyákat '
                                                                          'élethosszig tartó '
                                                                          'személyijövedelemadó-mentesség illeti meg.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A lakhatási feltételek javítását célozta a '
                                                                          'Családi Otthonteremtési Kedvezmény (CSOK) '
                                                                          'és a kamattámogatott babaváró hitel. Mire a '
                                                                          'fiatal párok a harmincas éveik elejére '
                                                                          'értek, ezen pénzügyi ösztönzők '
                                                                          'igénybevételével sokan képesek voltak saját '
                                                                          'tulajdonú ingatlant vásárolni vagy családi '
                                                                          'házat építeni a nagyvárosok körüli '
                                                                          'agglomerációban.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A szakmai viták kereszttüzében azonban a '
                                                                          'programok társadalmi megoszlása és '
                                                                          'hatékonysága áll. Közgazdászok rámutattak, '
                                                                          'hogy mire a támogatási források megjelentek '
                                                                          'a piacon, az ingatlanárak olyan mértékben '
                                                                          'emelkedtek az építőipari kereslet nyomán, '
                                                                          'hogy a támogatás egy része beépült a '
                                                                          'lakásárakba.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Míg a kormány a termékenységi mutatók '
                                                                          'másfél körüli stabilizálódását az '
                                                                          'intézkedések sikerének tekinti, a '
                                                                          'szociológiai kutatások arra '
                                                                          'figyelmeztetnek, hogy az adókedvezmények '
                                                                          'elsősorban a jómódú középosztályt '
                                                                          'erősítették, miközben a leghátrányosabb '
                                                                          'helyzetű családok társadalmi mobilitása '
                                                                          'továbbra is korlátozott maradt.'}]},
                       'words': [   {   'lemma': 'adókedvezmény',
                                        'translation': 'tax allowance / tax relief',
                                        'pos': 'noun'},
                                    {   'lemma': 'otthonteremtés',
                                        'translation': 'home creation / housing acquisition',
                                        'pos': 'noun'},
                                    {   'lemma': 'babaváró hitel',
                                        'translation': 'prenatal baby-support loan',
                                        'pos': 'noun'},
                                    {'lemma': 'társadalmi mobilitás', 'translation': 'social mobility', 'pos': 'noun'},
                                    {'lemma': 'ösztönző', 'translation': 'incentive / stimulus', 'pos': 'noun'},
                                    {'lemma': 'fenntarthatóság', 'translation': 'sustainability', 'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'mire-clauses-aspect',
                                          'title': "Anteriority Clauses with mire ('by the time that') and Aspectual "
                                                   'Completion',
                                          'text1_title': 'Temporal Precedence with mire',
                                          'text1': 'The conjunction mire introduces a temporal subordinate clause '
                                                   "meaning 'by the time (that)'. It establishes an endpoint before or "
                                                   'by which the action of the main clause has already completed or '
                                                   'will complete. Unlike amikor (which denotes simultaneous or '
                                                   'consecutive moments), mire focuses squarely on anterior '
                                                   'completion.',
                                          'text2_title': 'Aspectual Matching and Verbal Prefixes',
                                          'text2': 'Because mire marks a deadline, verbs in the main clause typically '
                                                   'employ perfective verbal prefixes (meg-, fel-, el-, be-) to signal '
                                                   "culmination: 'Mire a gyermekek megszülettek, a szülők felépítették "
                                                   "a házat' (By the time the children were born, the parents had "
                                                   'built the house).',
                                          'table_title': 'Aspectual Completion with mire',
                                          'table_rows': [   [   'Mire a támogatás megérkezett, az ingatlanárak '
                                                                'megemelkedtek.',
                                                                'By the time the subsidy arrived, property prices had '
                                                                'risen.'],
                                                            [   'Mire a gyermekek iskolába mentek, a család '
                                                                'beköltözött az új otthonba.',
                                                                'By the time the children went to school, the family '
                                                                'had moved into the new home.'],
                                                            [   'Mire a vita véget ért, a parlament elfogadta a '
                                                                'törvénymódosítást.',
                                                                'By the time the debate ended, parliament had adopted '
                                                                'the amendment.']],
                                          'examples': [   {   'spanish': 'Mire a fiatalok betöltötték a harmincat, már '
                                                                         'önálló egzisztenciát teremtettek.',
                                                              'english': 'By the time the young adults reached thirty, '
                                                                         'they had already created an independent '
                                                                         'livelihood.'},
                                                          {   'spanish': 'Mire a népszámlálási adatokat közzétették, a '
                                                                         'demográfiai trend megerősítést nyert.',
                                                              'english': 'By the time the census data were published, '
                                                                         'the demographic trend had gained '
                                                                         'confirmation.'},
                                                          {   'spanish': 'Mire a bank jóváhagyta a hitelt, a '
                                                                         'szerződést előkészítették.',
                                                              'english': 'By the time the bank approved the loan, they '
                                                                         'had prepared the contract.'}],
                                          'tip': 'Always check verbal aspect: a completed event in the main clause '
                                                 'requires a perfective prefix (pl. felépült, beköltözött, '
                                                 'elfogadták).'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-demografia-vocab'],
                                            'pairs': [   ['adókedvezmény', 'tax allowance / tax relief'],
                                                         ['otthonteremtés', 'housing acquisition / home building'],
                                                         ['babaváró hitel', 'prenatal baby-support loan'],
                                                         ['társadalmi mobilitás', 'social mobility'],
                                                         ['ösztönző', 'financial incentive'],
                                                         ['fenntarthatóság', 'policy sustainability']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'question': 'Melyik társadalmi csoport részesült a legnagyobb mértékben a '
                                                        'modern magyar családi adókedvezményekből?',
                                            'options': [   'A bejelentett munkaviszonnyal rendelkező, magasabb '
                                                           'jövedelmű többgyermekes családok.',
                                                           'A munkanélküli egyedülállók és a pályakezdő egyetemisták.',
                                                           'Kizárólag a nyugdíjas korú állampolgárok.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'sentence': 'A lakáspiaci intézkedések elsődleges célja a fiatal párok '
                                                        'vidéki és agglomerációs _____ támogatása volt.',
                                            'answer': 'otthonteremtés',
                                            'english': 'The primary goal of the housing market measures was supporting '
                                                       'the home acquisition of young couples in rural and '
                                                       'agglomeration areas.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-temporal-framing'],
                                            'question': 'Melyik kötőszó fejezi ki, hogy a főmondat cselekvése egy '
                                                        "időbeli határidő előtt fejeződött be? '_____ az új "
                                                        'családpolitikai csomag hatályba lépett, a lakásárak '
                                                        "jelentősen megugrottak.'",
                                            'options': ['Mire', 'Jóllehet', 'Míg', 'Amennyiben'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'sentence': '_____ a bank jóváhagyta a babaváró kölcsönt, a házaspár már '
                                                        'kiválasztotta a leendő ingatlant.',
                                            'answer': 'Mire',
                                            'english': 'By the time the bank approved the baby loan, the married '
                                                       'couple had already selected the prospective property.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'tiles': [   'Mire',
                                                         'megérkezett',
                                                         'a',
                                                         'támogatás,',
                                                         'az',
                                                         'árak',
                                                         'már',
                                                         'felmentek.'],
                                            'solution': [   'Mire',
                                                            'megérkezett',
                                                            'a',
                                                            'támogatás,',
                                                            'az',
                                                            'árak',
                                                            'már',
                                                            'felmentek.'],
                                            'english': 'By the time the support arrived, prices had already gone up.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-temporal-framing'],
                                            'prompt': [   {   'speaker': 'Közgazdász',
                                                              'text': 'Hogyan befolyásolták a lakástámogatások az '
                                                                      'agglomerációs ingatlanpiacot?'},
                                                          {'speaker': 'Elemző', 'text': '_____'}],
                                            'options': [   'Mire a családok tömegesen megkapták a CSOK-ot, az '
                                                           'építőipari árak annyira felmentek, hogy a támogatás egy '
                                                           'része elveszítette reálértékét.',
                                                           'Mire a támogatás elindult, senki sem akart családi házat '
                                                           'vásárolni.',
                                                           'Az intézkedések következtében a nagyvárosok összes lakása '
                                                           'kiürült.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen bírálatot fogalmaztak meg szociológusok a munkához '
                                                        'kötött családi adókedvezményekkel kapcsolatban?',
                                            'options': [   'Azt, hogy a szegényebb, instabil munkaviszonnyal '
                                                           'rendelkező rétegek kimaradnak a támogatásokból, ami '
                                                           'gátolja a mobilitást.',
                                                           'Azt, hogy túl sok óvoda és iskola épült az országban.',
                                                           'Azt, hogy a támogatásokat kizárólag külföldi állampolgárok '
                                                           'vehették igénybe.'],
                                            'correct': 0}]},
                   {   'num': 4,
                       'title': 'Healthcare, Longevity, and the Care Economy',
                       'grammar_label': 'Formal temporal markers: idején, idejére, and huzamosabb időn keresztül',
                       'goals': [   'I can analyze the challenges of population aging, the pension system, and '
                                    'eldercare in Hungary.',
                                    'I can use idején, idejére, and temporal duration phrases accurately in formal '
                                    'sociological analysis.',
                                    'I can discuss longevity, multigenerational care, and healthcare infrastructure in '
                                    'B2 Hungarian.'],
                       'story_segment': {   'seg_slug': 'gondoskodasidosekrol',
                                            'title': 'Hosszabb élet, idősödő társadalom és gondoskodás',
                                            'summary': 'As life expectancy in Hungary increases and the demographic '
                                                       'pyramid shifts, the responsibility of elderly care falls '
                                                       "increasingly upon the informal care economy and the 'sandwich "
                                                       "generation', straining health institutions and family budgets.",
                                            'location': 'Magyarországi idősotthonok és családi otthonok (napjainkban)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A huszonegyedik századi Magyarország egyik '
                                                                          'legmélyrehatóbb demográfiai átalakulása a '
                                                                          'lakosság fokozatos idősödése. Az '
                                                                          'orvostudomány fejlődése és az '
                                                                          'életkörülmények javulása nyomán a '
                                                                          'születéskor várható élettartam jelentősen '
                                                                          'megemelkedett a rendszerváltás idejéhez '
                                                                          'képest, jóllehet az egészségben eltöltött '
                                                                          'életévek száma még elmarad az uniós '
                                                                          'átlagtól.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Az idősödő társadalom komoly strukturális '
                                                                          'próbatétel elé állítja az állami '
                                                                          'felosztó-kirovó nyugdíjrendszert és az '
                                                                          'egészségügyi ellátórendszert. Míg korábban '
                                                                          'több aktív kereső jutott egyetlen '
                                                                          'nyugdíjasra, a Ratkó-nemzedék nyugdíjba '
                                                                          'vonulásának idejére az eltartottsági ráta '
                                                                          'kritikussá vált, miközben a szakorvos- és '
                                                                          'ápolóhiány sújtja a kórházakat.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A hivatalos szociális infrastruktúra '
                                                                          'hiányosságait nagyrészt a láthatatlan '
                                                                          'gondoskodási gazdaság és a családi '
                                                                          'szolidaritás kompenzálja. A szociológusok '
                                                                          'által „szendvicsgenerációnak” nevezett '
                                                                          'középkorú felnőttek — különösen a '
                                                                          'negyvenes-ötvenes éveikben járó nők — '
                                                                          'egyszerre kényszerülnek nevelni növekvő '
                                                                          'gyermekeiket és ápolni idős, rászoruló '
                                                                          'szüleiket.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A férőhelyhiány miatt az állami '
                                                                          'idősotthonok várólistái gyakran többévesek, '
                                                                          'így a házi betegápolás és a magánellátás '
                                                                          'költségei huzamosabb időn keresztül súlyos '
                                                                          'anyagi terhet rónak a háztartásokra. Sokan '
                                                                          'önkéntes segítőkkel és egyházi karitatív '
                                                                          'hálózatokkal próbálják biztosítani a '
                                                                          'mindennapi meleg ételt és a társas '
                                                                          'támaszt.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Ugyanakkor az „aktív idősödés” szemlélete '
                                                                          'is teret hódít: a szenior akadémiák, a '
                                                                          'nyugdíjas klubok és az önkéntes programok '
                                                                          'bizonyítják, hogy az időskor nem a '
                                                                          'leépülés, hanem az élettapasztalat '
                                                                          'átadásának és a társadalmi hasznosságnak a '
                                                                          'korszaka, amely nélkülözhetetlen erőforrás '
                                                                          'a modern közösségek számára.'}]},
                       'words': [   {'lemma': 'idősödő társadalom', 'translation': 'aging society', 'pos': 'noun'},
                                    {'lemma': 'várható élettartam', 'translation': 'life expectancy', 'pos': 'noun'},
                                    {'lemma': 'nyugdíjrendszer', 'translation': 'pension system', 'pos': 'noun'},
                                    {   'lemma': 'idősgondozás',
                                        'translation': 'elderly care / geriatric care',
                                        'pos': 'noun'},
                                    {   'lemma': 'szendvicsgeneráció',
                                        'translation': 'sandwich generation',
                                        'pos': 'noun'},
                                    {   'lemma': 'nemzedéki szolidaritás',
                                        'translation': 'intergenerational solidarity',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'idejen-idejere-framing',
                                          'title': "Temporal Anchoring with idején ('at the time of') and idejére ('by "
                                                   "the time of')",
                                          'text1_title': 'Temporal Anchoring: idején vs. idejére',
                                          'text1': 'The postpositions idején and idejére attach to nouns denoting '
                                                   'epochs, life milestones, or events. idején anchors an action '
                                                   "simultaneously within that timeframe ('a rendszerváltás idején' = "
                                                   'at the time of the regime change), whereas idejére sets an '
                                                   "external deadline or prospective milestone ('időskoruk idejére' = "
                                                   'by the time of their old age).',
                                          'text2_title': 'Extended Duration with huzamosabb időn keresztül',
                                          'text2': 'To express prolonged continuous strain or enduring conditions in '
                                                   "formal prose, B2 Hungarian uses huzamosabb időn keresztül ('over "
                                                   "an extended period of time') or tartósan, replacing colloquial "
                                                   'sokáig.',
                                          'table_title': 'Using idején, idejére, and huzamosabb időn keresztül',
                                          'table_rows': [   [   'A gazdasági válság idején megnőtt a szociális '
                                                                'feszültség.',
                                                                'At the time of the economic crisis, social tension '
                                                                'grew.'],
                                                            [   'Nyugdíjba vonulásuk idejére a dolgozók biztos '
                                                                'egzisztenciát kívánnak.',
                                                                'By the time of their retirement, workers desire '
                                                                'secure livelihoods.'],
                                                            [   'A családok huzamosabb időn keresztül viselik a házi '
                                                                'gondozás terheit.',
                                                                'Families bear the burdens of home care over an '
                                                                'extended period of time.']],
                                          'examples': [   {   'spanish': 'A járvány idején az idősotthonok fokozott '
                                                                         'védelmet igényeltek.',
                                                              'english': 'At the time of the epidemic, nursing homes '
                                                                         'required heightened protection.'},
                                                          {   'spanish': 'A század közepének idejére a lakosság '
                                                                         'egyharmada hatvan év feletti lesz.',
                                                              'english': 'By the time of the middle of the century, '
                                                                         'one third of the population will be over '
                                                                         'sixty.'},
                                                          {   'spanish': 'Huzamosabb időn keresztül végzett gondozói '
                                                                         'munka után sok ápoló kimerül.',
                                                              'english': 'After caregiving work performed over an '
                                                                         'extended period, many nurses suffer '
                                                                         'exhaustion.'}],
                                          'tip': "Distinguish: 'valami idején' (simultaneous: during the time of X) "
                                                 "versus 'valami idejére' (prospective: by the target point of X)."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-demografia-vocab'],
                                            'pairs': [   ['idősödő társadalom', 'aging society'],
                                                         ['várható élettartam', 'life expectancy'],
                                                         ['nyugdíjrendszer', 'pension system'],
                                                         ['idősgondozás', 'eldercare'],
                                                         ['szendvicsgeneráció', 'sandwich generation'],
                                                         ['nemzedéki szolidaritás', 'intergenerational solidarity']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'question': "Kit nevez a szociológiai szakirodalom a 'szendvicsgeneráció' "
                                                        'tagjának?',
                                            'options': [   'Azon középkorú felnőtteket, akik egyszerre nevelik kiskorú '
                                                           'gyermekeiket és ápolják idősödő szüleiket.',
                                                           'Azon fiatal egyetemistákat, akik gyorséttermi '
                                                           'szendvicsbárokban vállalnak diákmunkát.',
                                                           'Azon nyugdíjasokat, akik három generációval élnek együtt '
                                                           'egyetlen lakásban.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'sentence': 'A modern orvostudománynak köszönhetően a születéskor _____ '
                                                        'folyamatosan emelkedett az elmúlt évtizedekben.',
                                            'answer': 'várható élettartam',
                                            'english': 'Thanks to modern medical science, life expectancy at birth has '
                                                       'continuously risen over past decades.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-temporal-framing'],
                                            'question': 'Melyik időhatározó jelöli az esemény bekövetkeztének '
                                                        "határidejét? 'A Ratkó-nemzedék nyugdíjba vonulásának _____ a "
                                                        "nyugdíjrendszer bevételei csökkenni kezdtek.'",
                                            'options': ['idejére', 'nélkül', 'gyanánt', 'ellenére'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'sentence': 'A rendszerváltás _____ az állami ellátórendszer számos '
                                                        'intézménye átalakult.',
                                            'answer': 'idején',
                                            'english': 'At the time of the regime change, numerous institutions of the '
                                                       'state care system transformed.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'tiles': [   'A',
                                                         'családok',
                                                         'huzamosabb',
                                                         'időn',
                                                         'keresztül',
                                                         'viselik',
                                                         'a',
                                                         'gondozás',
                                                         'terheit.'],
                                            'solution': [   'A',
                                                            'családok',
                                                            'huzamosabb',
                                                            'időn',
                                                            'keresztül',
                                                            'viselik',
                                                            'a',
                                                            'gondozás',
                                                            'terheit.'],
                                            'english': 'Families bear the burdens of care over an extended period of '
                                                       'time.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-temporal-framing'],
                                            'prompt': [   {   'speaker': 'Szociálpolitikus',
                                                              'text': 'Hogyan kezeli a magyar társadalom az '
                                                                      'idősellátás hiányosságait?'},
                                                          {'speaker': 'Kutató', 'text': '_____'}],
                                            'options': [   'A válságos időszakok idején a családok huzamosabb időn '
                                                           'keresztül saját erőből és anyagi áldozatokkal gondozzák '
                                                           'hozzátartozóikat.',
                                                           'A nyugdíjrendszer minden állampolgár számára azonnal '
                                                           'ingyenes luxusszállodát biztosít.',
                                                           'Az idősek többsége külföldre vándorol a nyugdíjba vonulás '
                                                           'idejére.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen pozitív társadalmi szemléletet mutatnak a szenior '
                                                        'akadémiák és önkéntes klubok a szöveg szerint?',
                                            'options': [   'Az aktív idősödés szemléletét, amely értékes '
                                                           'élettapasztalattal gazdagítja a helyi közösségeket.',
                                                           'Azt, hogy az időseknek tilos részt venniük a társadalom '
                                                           'kulturális életében.',
                                                           'Azt, hogy a nyugdíjasok nem igényelnek orvosi ellátást.'],
                                            'correct': 0}]},
                   {   'num': 5,
                       'title': 'How Young Hungarians Envision Family Today',
                       'grammar_label': 'Synthesizing temporal framing (során, folyamán, múltával, mire) in analytical '
                                        'discourse',
                       'goals': [   'I can summarize contemporary sociological findings on how young Hungarians '
                                    'balance education, career, and family planning.',
                                    'I can synthesize the full range of temporal framing postpositions and clauses in '
                                    'an analytical B2 essay.',
                                    'I can evaluate demographic prospects and shifting partnership models in '
                                    'Hungarian.'],
                       'story_segment': {   'seg_slug': 'fiatalokjovoje',
                                            'title': 'Családalapítás a 21. században: Tervek és valóság',
                                            'summary': 'Surveys reveal a persistent gap between the desired number of '
                                                       'children and realized fertility among young Hungarians, driven '
                                                       'by prolonged education, precarious housing, and evolving '
                                                       'gender roles.',
                                            'location': 'Budapesti egyetemek és kutatóintézetek (napjainkban)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A magyar ifjúságkutatások évtizedek óta '
                                                                          'megbízhatóan jelzik, hogy a fiatal '
                                                                          'felnőttek értékrendjében a család és a '
                                                                          'gyermekvállalás kiemelkedő helyet foglal '
                                                                          'el. A vágyott gyermekszám átlagosan két '
                                                                          'gyermek felett marad, ami elméletileg '
                                                                          'elegendő lenne a népesség természetes '
                                                                          'reprodukciójához.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A tervek és a valóság között azonban mély '
                                                                          'szakadék tátong: az első gyermek születése '
                                                                          'folyamatosan kitolódik. A kitolódó '
                                                                          'felnőttkor jelensége mögött a hosszabbá '
                                                                          'váló egyetemi tanulmányok, a munkaerőpiaci '
                                                                          'belépés bizonytalansága és a megfizethető '
                                                                          'lakhatás hiánya áll.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Mire a harmincas éveik közepére érnek, sok '
                                                                          'fiatal pár még mindig albérletben vagy '
                                                                          'szülői segítségre szorulva él, ami '
                                                                          'óvatosságra inti őket a családalapítás '
                                                                          'terén. A hagyományos házasságkötés mellett '
                                                                          'elterjedtté vált a tartós élettársi '
                                                                          'kapcsolat, és a gyermekek jelentős része ma '
                                                                          'már ilyen kötetlenebb együttélési formában '
                                                                          'születik meg.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A szociológiai interjúk során a fiatal '
                                                                          'anyák és apák egyaránt a munka és magánélet '
                                                                          'egyensúlyának megőrzését nevezik meg a '
                                                                          'legnagyobb kihívásnak. A rugalmas munkaidő, '
                                                                          'a távmunka lehetősége és a hozzáférhető '
                                                                          'bölcsődei hálózat sokkal meghatározóbb '
                                                                          'tényező a döntésükben, mint az egyszeri '
                                                                          'pénzügyi hitelek.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Az elkövetkező évtizedek folyamán a magyar '
                                                                          'társadalom jövője attól függ, hogy a '
                                                                          'szakpolitika képes lesz-e olyan '
                                                                          'kiszámítható környezetet teremteni, '
                                                                          'amelyben a fiatalok biztonságban '
                                                                          'vállalhatnak gyermeket anélkül, hogy fel '
                                                                          'kellene adniuk szakmai hivatásukat és '
                                                                          'személyes céljaikat.'}]},
                       'words': [   {   'lemma': 'családalapítás',
                                        'translation': 'family formation / starting a family',
                                        'pos': 'noun'},
                                    {   'lemma': 'élettársi kapcsolat',
                                        'translation': 'cohabitation / civil partnership',
                                        'pos': 'noun'},
                                    {   'lemma': 'vágyott gyermekszám',
                                        'translation': 'desired number of children',
                                        'pos': 'noun'},
                                    {   'lemma': 'kitolódó felnőttkor',
                                        'translation': 'delayed adulthood / prolonged youth',
                                        'pos': 'noun'},
                                    {   'lemma': 'munka-magánélet egyensúly',
                                        'translation': 'work-life balance',
                                        'pos': 'noun'},
                                    {   'lemma': 'demográfiai jövőkép',
                                        'translation': 'demographic outlook / future vision',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'temporal-synthesis',
                                          'title': 'Integrating Temporal Connectors and Postpositions in Sociological '
                                                   'Argumentation',
                                          'text1_title': 'Synthesizing Macro and Micro Temporal Scales',
                                          'text1': 'Advanced B2 essays integrate multiple temporal perspectives within '
                                                   'a coherent argument: macro-historical trends with folyamán (az '
                                                   'évtizedek folyamán), research processes with során (a vizsgálat '
                                                   'során), milestone conclusions with múltával (évek múltával), and '
                                                   'sequential turning points with mire (mire a fiatalok döntést '
                                                   'hoznak).',
                                          'text2_title': 'Cohesion and Variety',
                                          'text2': 'Alternating between temporal postpositions (során, folyamán) and '
                                                   'subordinating clauses (mire, amíg) prevents monotonous syntax and '
                                                   'allows precise calibration of cause, duration, and culmination.',
                                          'table_title': 'Synthesis of Temporal Framing Devices',
                                          'table_rows': [   [   'A felmérések során a kutatók a vágyott gyermekszámot '
                                                                'elemezték.',
                                                                'During the surveys, researchers analyzed the desired '
                                                                'number of children.'],
                                                            [   'Az évtizedek folyamán kitolódott a házasságkötések '
                                                                'átlagos életkora.',
                                                                'Over the course of the decades, the average age of '
                                                                'marriage was postponed.'],
                                                            [   'Mire a párok stabil egzisztenciát teremtenek, '
                                                                'elmúlnak harmincöt évesek.',
                                                                'By the time couples create a stable livelihood, they '
                                                                'pass thirty-five years of age.']],
                                          'examples': [   {   'spanish': 'A kutatások során kiderült, hogy a nők a '
                                                                         'rugalmas munkaidőt részesítik előnyben.',
                                                              'english': 'During the research, it turned out that '
                                                                         'women prefer flexible working hours.'},
                                                          {   'spanish': 'Hosszú évek múltával a demográfiai jövőkép a '
                                                                         'fiatalok döntésein áll vagy bukik.',
                                                              'english': 'With the passage of long years, the '
                                                                         'demographic future stands or falls on the '
                                                                         'decisions of youth.'},
                                                          {   'spanish': 'Mire a támogatások hatása megmutatkozott, új '
                                                                         'társadalmi kihívások keletkeztek.',
                                                              'english': 'By the time the impact of subsidies showed '
                                                                         'itself, new social challenges had arisen.'}],
                                          'tip': "In B2 writing, avoid relying solely on 'mikor' or 'után'; actively "
                                                 "employ 'során', 'folyamán', 'múltával', and 'mire' to demonstrate "
                                                 'syntactic sophistication.'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-demografia-vocab'],
                                            'pairs': [   ['családalapítás', 'starting a family / family formation'],
                                                         ['élettársi kapcsolat', 'cohabitation / civil partnership'],
                                                         ['vágyott gyermekszám', 'desired number of children'],
                                                         ['kitolódó felnőttkor', 'prolonged adulthood phenomenon'],
                                                         ['munka-magánélet egyensúly', 'work-life balance'],
                                                         ['demográfiai jövőkép', 'demographic future outlook']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'question': 'Mi a legfőbb oka annak, hogy a megvalósult születésszám '
                                                        'elmarad a fiatalok vágyott gyermekszámától?',
                                            'options': [   'A hosszabbá váló tanulmányok, a lakhatási bizonytalanság '
                                                           'és a munka-magánélet egyensúly hiánya.',
                                                           'A fiatalok teljes elfordulása a családi értékektől és a '
                                                           'házasságtól.',
                                                           'Az állam által bevezetett szigorú gyermektelenségi '
                                                           'büntetés.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-demografia-vocab'],
                                            'sentence': 'A fiatal munkavállalók körében a megfelelő _____ megléte a '
                                                        'gyermekvállalási hajlandóság kulcsfontosságú feltétele.',
                                            'answer': 'munka-magánélet egyensúly',
                                            'english': 'Among young employees, the existence of adequate work-life '
                                                       'balance is a key condition for the willingness to have '
                                                       'children.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-temporal-framing'],
                                            'question': "Melyik mondat alkalmazza hibátlanul a 'mire' kötőszót és a "
                                                        'befejezett igeszemléletet?',
                                            'options': [   'Mire a fiatal párok stabil állást találtak, a lakásárak '
                                                           'már megduplázódtak.',
                                                           'Mire a fiatal párok állást találni, a lakásárak dupláznak.',
                                                           'A lakásárak megduplázódtak mire párok keresnek állást.',
                                                           'Mire stabil állás nélkül a lakásárak duplázódtak.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'sentence': 'A kérdőíves felmérés _____ a válaszadók többsége két '
                                                        'gyermeket jelölt meg kívánatosnak.',
                                            'answer': 'során',
                                            'english': 'During the questionnaire survey, the majority of respondents '
                                                       'designated two children as desirable.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-temporal-framing'],
                                            'tiles': [   'Az',
                                                         'elkövetkező',
                                                         'évek',
                                                         'folyamán',
                                                         'eldől',
                                                         'a',
                                                         'demográfiai',
                                                         'jövőnk.'],
                                            'solution': [   'Az',
                                                            'elkövetkező',
                                                            'évek',
                                                            'folyamán',
                                                            'eldől',
                                                            'a',
                                                            'demográfiai',
                                                            'jövőnk.'],
                                            'english': 'Over the course of the coming years, our demographic future '
                                                       'will be decided.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-temporal-framing'],
                                            'prompt': [   {   'speaker': 'Egyetemi oktató',
                                                              'text': 'Hogyan látják a kutatók a mai huszonévesek '
                                                                      'családalapítási esélyeit?'},
                                                          {'speaker': 'Ifjúságszociológus', 'text': '_____'}],
                                            'options': [   'A vizsgálatok során kiderült, hogy mire a párok saját '
                                                           'lakáshoz jutnak, az életkoruk miatt gyakran lemondanak a '
                                                           'többedik gyermekről.',
                                                           'A fiatalok kivétel nélkül tizennyolc éves koruk előtt '
                                                           'megházasodnak.',
                                                           'Senki sem akar többé diplomát szerezni a munkaerőpiacon.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen tényezőket részesítenek előnyben a mai fiatal szülők '
                                                        'az egyszeri hiteleknél a szöveg szerint?',
                                            'options': [   'A rugalmas munkaidőt, a távmunka lehetőségét és a '
                                                           'megfizethető bölcsődéket.',
                                                           'A kötelező katonai szolgálatot és a gyermektelenségi adót.',
                                                           'A külföldi utazások teljes tilalmát.'],
                                            'correct': 0}]}],
    'consolidation': {   'goals': [   'I can recount the trajectory of Hungarian demographic history from the 1950s '
                                      'Ratkó era and 1967 GYES to contemporary family policy.',
                                      'I can properly employ temporal framing devices (során, folyamán, múltával, '
                                      'elteltével, idején, idejére, mire) in academic analysis.',
                                      'I can debate the socioeconomic factors shaping fertility, aging societies, and '
                                      'eldercare.',
                                      'I can accurately use 30 B2 demographic, sociological, and family-policy terms.'],
                         'exercises': [   {   'type': 'matching',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-demografia-vocab'],
                                              'pairs': [   ['demográfiai hullám', 'demographic baby boom wave'],
                                                           ['gyermekgondozási segély', 'childcare allowance (GYES)'],
                                                           ['otthonteremtés', 'housing acquisition / home building'],
                                                           ['idősödő társadalom', 'aging society'],
                                                           ['szendvicsgeneráció', 'sandwich generation'],
                                                           ['kitolódó felnőttkor', 'prolonged adulthood phenomenon']]},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'teaches': ['b2-temporal-framing'],
                                              'question': 'Which temporal marker specifically indicates continuous '
                                                          "duration over calendar spans ('over the course of decades') "
                                                          'rather than internal procedural steps?',
                                              'options': ['folyamán', 'során', 'helyett', 'végett'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-demografia-vocab'],
                                              'question': 'Melyik fogalom jelöli a női életkor alatt átlagosan '
                                                          'született gyermekek számát egy adott országban?',
                                              'options': [   'Termékenységi arányszám.',
                                                             'Eltartottsági ráta.',
                                                             'Korfa.',
                                                             'Munkaerőpiaci aktivitás.'],
                                              'correct': 0},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'teaches': ['b2-demografia-vocab'],
                                              'sentence': 'Az 1950-es évek elején érvényben lévő abortusztilalom miatt '
                                                          'kibontakozó időszakot a történelemírás _____ néven említi.',
                                              'answer': 'Ratkó-korszak',
                                              'english': 'Historiography refers to the period unfolding due to the '
                                                         'abortion ban in the early 1950s as the Ratkó era.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-temporal-framing'],
                                              'sentence': 'A szülési szabadság három évének _____ a munkavállaló '
                                                          'visszatérhet korábbi állásába.',
                                              'answer': 'múltával',
                                              'english': 'With the passage of the three years of maternity leave, the '
                                                         'employee may return to their former job.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-temporal-framing'],
                                              'sentence': '_____ a családpolitikai támogatások megérkeztek, az '
                                                          'ingatlanárak már jelentősen megemelkedtek.',
                                              'answer': 'Mire',
                                              'english': 'By the time the family policy subsidies arrived, property '
                                                         'prices had already risen significantly.'},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-temporal-framing'],
                                              'prompt': [   {   'speaker': 'Társadalomkutató',
                                                                'text': 'Hogyan értékeli a GYES és a GYED hatását a '
                                                                        'nők munkavállalására?'},
                                                            {'speaker': 'Szociológus', 'text': '_____'}],
                                              'options': [   'Az intézkedések bevezetése során a nők biztos jövedelmet '
                                                             'kaptak, ám az évek múltával a karrierépítés sokak '
                                                             'számára megnehezedett.',
                                                             'A törvény következtében a nők azonnal felmondtak minden '
                                                             'munkahelyen és soha nem tértek vissza.',
                                                             'A rendszer kizárólag a férfiak számára tette lehetővé a '
                                                             'gyermekgondozást 1967-ben.'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'teaches': ['b2-temporal-framing'],
                                              'question': "Which sentence demonstrates the idiomatic use of 'idejére' "
                                                          'to express a projected temporal milestone?',
                                              'options': [   'A népes nemzedék nyugdíjba vonulásának idejére a '
                                                             'társadalomnak fel kell készítenie az ellátórendszert.',
                                                             'Az ellátórendszer felkészült a nyugdíj idején idejére.',
                                                             'A nyugdíjba vonulás idején idejére a dolgozók pihennek.',
                                                             'A társadalom idejére vonult vissza a nemzedék idején.'],
                                              'correct': 0},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-temporal-framing'],
                                              'prompt': [   {   'speaker': 'Kérdező',
                                                                'text': 'Milyen strukturális feszültséget okoz az '
                                                                        'idősödő társadalom a felosztó-kirovó '
                                                                        'nyugdíjrendszerben?'},
                                                            {'speaker': 'Közgazdász', 'text': '_____'}],
                                              'options': [   'Az évtizedek folyamán megnőtt az inaktívak aránya, így '
                                                             'mire a Ratkó-nemzedék nyugdíjba vonult, kevesebb aktív '
                                                             'dolgozó járulékából kellett kigazdálkodni a '
                                                             'kifizetéseket.',
                                                             'A nyugdíjrendszerben egyetlen fillér hiány sem '
                                                             'keletkezett az elmúlt ötven évben.',
                                                             'Minden nyugdíjas visszatért a gyárakba három év múltával '
                                                             'dolgozni.'],
                                              'correct': 0},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-temporal-framing'],
                                              'tiles': [   'A',
                                                           'népszámlálás',
                                                           'során',
                                                           'részletesen',
                                                           'elemezték',
                                                           'a',
                                                           'korfa',
                                                           'alakulását.'],
                                              'solution': [   'A',
                                                              'népszámlálás',
                                                              'során',
                                                              'részletesen',
                                                              'elemezték',
                                                              'a',
                                                              'korfa',
                                                              'alakulását.'],
                                              'english': 'During the census, they analyzed in detail the evolution of '
                                                         'the population pyramid.'},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-temporal-framing'],
                                              'tiles': [   'Mire',
                                                           'felnőttek',
                                                           'a',
                                                           'gyerekek,',
                                                           'a',
                                                           'szülők',
                                                           'kifizették',
                                                           'a',
                                                           'hitelt.'],
                                              'solution': [   'Mire',
                                                              'felnőttek',
                                                              'a',
                                                              'gyerekek,',
                                                              'a',
                                                              'szülők',
                                                              'kifizették',
                                                              'a',
                                                              'hitelt.'],
                                              'english': 'By the time the children grew up, the parents had paid off '
                                                         'the loan.'},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'teaches': ['b2-temporal-framing'],
                                              'template': [   {   'prompt': 'Write a sentence explaining the '
                                                                            'demographic ripple effect of the 1950s '
                                                                            "baby boom (use 'az évtizedek folyamán' "
                                                                            "and 'során').",
                                                                  'answer': 'Az évtizedek folyamán a Ratkó-nemzedék '
                                                                            'belépése a munkaerőpiacra komoly '
                                                                            'lakáshiányt okozott, amelynek kezelése '
                                                                            'során hatalmas lakótelepek épültek fel.'},
                                                              {   'prompt': 'Write a sentence describing the timing of '
                                                                            'housing purchases for young families (use '
                                                                            "'mire' with a perfective verb prefix).",
                                                                  'answer': 'Mire a fiatal párok a harmincas éveik '
                                                                            'közepére értek, a családtámogatási '
                                                                            'kedvezmények segítségével felépítették '
                                                                            'saját otthonukat.'}]}]}}



UNIT_23_LAKHATAS = {   'unit_num': 23,
    'slug': 'lakhatas',
    'title': 'Courtyards, Panel Estates & Urban Renewal',
    'grammar_skill': 'b2-relative-postpositions',
    'vocab_skill': 'b2-lakhatas-vocab',
    'theme': 'Social history of housing: tenements, panels and ruin bars',
    'location': 'Budapest (Erzsébetváros, Óbuda, Kispest Wekerletelep)',
    'intro_body': [   'The built fabric of Budapest tells the story of how millions of Hungarians have lived, '
                      'struggled, and reinvented their urban spaces across the nineteenth, twentieth, and twenty-first '
                      'centuries. From the eclectic tenement buildings with ringing open courtyards to idyllic '
                      'garden-city suburbs, towering socialist housing estates, and the reinvention of decaying '
                      'Jewish-quarter courtyards into ruin bars, each architecture created its own distinct sociology '
                      'and community habits.',
                      'In this unit, you will step onto the gang of Pest tenements, wander the peaceful lime-tree '
                      'avenues of Wekerletelep, discover the daily realities of panel life in Óbuda and Újpalota, '
                      'trace the creative rebirth of the 7th District through ruin bars, and evaluate the modern '
                      'dilemmas of affordability and gentrification. Grammatically, you will master complex relative '
                      'clauses combining relative pronouns with postpositions (amely mellett, amelynek udvarán, '
                      'amellyel szemben, amelyeken keresztül).'],
    'combined_story_title': 'A körfolyosótól a tizedik emeletig: Hogyan lakunk?',
    'combined_story_summary': 'A social history of Hungarian housing: 19th-century courtyard tenements (gangos '
                              'bérházak), Wekerletelep garden suburb, 1970s panel concrete towers, ruin bars, and '
                              'inner-city renewal.',
    'lessons': [   {   'num': 1,
                       'title': "Sociology of the Pest 'Gangos' Courtyard",
                       'grammar_label': 'Relative pronouns with simple spatial postpositions (amely mellett, amely '
                                        'mögött, amely felett)',
                       'goals': [   'I can describe the architecture and social life of 19th-century Budapest '
                                    'courtyard tenement buildings (gangos bérházak).',
                                    'I can form relative clauses combining amely with spatial postpositions.',
                                    'I can discuss urban social stratification, caretaker cultures, and eclectic '
                                    'architecture in B2 Hungarian.'],
                       'story_segment': {   'seg_slug': 'gangosberhaz',
                                            'title': 'A gang világa: Élet a körfolyosón',
                                            'summary': 'The late 19th-century construction boom endowed Budapest with '
                                                       'thousands of eclectic courtyard tenements whose open circular '
                                                       'balconies (gangok) shaped an intensely communal and '
                                                       'acoustics-dominated urban sociology.',
                                            'location': 'Budapest, Erzsébetváros és Terézváros (1880–1910)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A kiegyezést követő évtizedekben Budapest a '
                                                                          'világ egyik leggyorsabban növekvő '
                                                                          'metropoliszává vált. A Nagykörút és a '
                                                                          'sugárutak mentén gomba módra szaporodtak a '
                                                                          'három-négy emeletes, eklektikus stílusú '
                                                                          'bérházak, amelyek sajátos építészeti '
                                                                          'megoldásukkal — a belső udvart körülölelő '
                                                                          'nyitott körfolyosóval, közismert nevén a '
                                                                          'ganggal — mélyen meghatározták a pesti '
                                                                          'lakókultúrát.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Ezekben az épületekben a társadalmi '
                                                                          'tagozódás függőlegesen és vízszintesen is '
                                                                          'kirajzolódott. Az utcára néző, tágas, '
                                                                          'stukkókkal díszített első emeleti '
                                                                          'nagypolgári lakásokban bankárok, orvosok és '
                                                                          'jómódú kereskedők laktak, miközben a belső '
                                                                          'udvar felé néző, sötétebb udvari lakásokban '
                                                                          'kisiparosok, cselédek és szegény bérlők '
                                                                          'osztoztak a szoba-konyhás helyiségeken.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A gangos udvar egyszerre volt akusztikai '
                                                                          'tér és társadalmi színpad. A kora reggeli '
                                                                          'porolástól a déli ebédillatokon át az esti '
                                                                          'zongoraszóig minden rezdülés visszhangzott '
                                                                          'a zárt kőfalak között, így a magánélet '
                                                                          'szinte elválaszthatatlanul összefonódott a '
                                                                          'szomszédság mindennapjaival.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A ház megkérdőjelezhetetlen ura a '
                                                                          'kapualjban lakó házmester volt, a kapu, '
                                                                          'amely mellett hivatali szobája állt, este '
                                                                          'tíz órakor kulcsra zárult. Aki ezután '
                                                                          'érkezett haza, annak kapupénzt kellett '
                                                                          'fizetnie, így a házmester nemcsak az épület '
                                                                          'tisztaságáért felelt, hanem szigorú '
                                                                          'erkölcsi és társadalmi felügyeletet is '
                                                                          'gyakorolt a lakóközösség felett.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A huszadik század viharaiban, különösen a '
                                                                          'háború utáni lakáshiány idején, a '
                                                                          'nagypolgári lakásokat gyakran felosztották, '
                                                                          'és létrejött a társbérlet intézménye, ahol '
                                                                          'idegen családok kényszerültek közös konyhát '
                                                                          'és fürdőszobát használni. A gangos bérház '
                                                                          'máig a pesti identitás és irodalom '
                                                                          'elmaradhatatlan toposza maradt.'}]},
                       'words': [   {   'lemma': 'körfolyosó',
                                        'translation': 'open access gallery / courtyard balcony / gang',
                                        'pos': 'noun'},
                                    {'lemma': 'bérház', 'translation': 'tenement / apartment building', 'pos': 'noun'},
                                    {   'lemma': 'házmester',
                                        'translation': 'concierge / residential building caretaker',
                                        'pos': 'noun'},
                                    {   'lemma': 'nagypolgári lakás',
                                        'translation': 'grand bourgeois apartment',
                                        'pos': 'noun'},
                                    {   'lemma': 'kapupénz',
                                        'translation': 'gate-opening fee (paid to the concierge at night)',
                                        'pos': 'noun'},
                                    {   'lemma': 'társbérlet',
                                        'translation': 'shared co-tenancy / divided subtenancy',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'amely-spatial-postpositions',
                                          'title': 'Relative Pronouns with Simple Spatial Postpositions (amely '
                                                   'mellett, amely mögött)',
                                          'text1_title': 'Positioning Relative Pronouns with Postpositions',
                                          'text1': 'In Hungarian, when a relative clause relates to a location '
                                                   'governed by a postposition, the relative pronoun amely (or ami in '
                                                   "informal speech) precedes the postposition directly: 'a gang, "
                                                   "amely felett virágok nyílnak' (the gallery above which flowers "
                                                   "bloom), 'a kapualj, amely mellett a házmester lakott' (the gateway "
                                                   'beside which the concierge lived).',
                                          'text2_title': 'Punctuation and Register',
                                          'text2': "A comma always precedes the relative pronoun: 'Az épület, amely "
                                                   "mögött kis kert húzódott, műemléki védelem alatt áll.' In formal "
                                                   'architectural and cultural essays, always prefer amely over ami '
                                                   'when referring to concrete feminine or masculine antecedents '
                                                   '(buildings, courtyards, structures).',
                                          'table_title': 'Spatial Postpositions with amely',
                                          'table_rows': [   [   'A kapualj, amely mellett a házmester lakott, sötét '
                                                                'volt.',
                                                                'The gateway beside which the caretaker lived was '
                                                                'dark.'],
                                                            [   'A körfolyosó, amely felett tetőablak nyílt, beázott.',
                                                                'The balcony above which a skylight opened suffered '
                                                                'leaks.'],
                                                            [   'A belső udvar, amely körül lakások sorakoztak, hangos '
                                                                'volt.',
                                                                'The inner courtyard around which apartments lined up '
                                                                'was loud.']],
                                          'examples': [   {   'spanish': 'A gang, amely mentén a szomszédok '
                                                                         'beszélgettek, reggelente megtelt élettel.',
                                                              'english': 'The gallery along which neighbors chatted '
                                                                         'filled with life in the mornings.'},
                                                          {   'spanish': 'A ház, amely mögött a műhely állt, a 19. '
                                                                         'század végén épült.',
                                                              'english': 'The house behind which the workshop stood '
                                                                         'was built in the late 19th century.'},
                                                          {   'spanish': 'A szoba, amely felett zongoráztak, az első '
                                                                         'emeleten volt.',
                                                              'english': 'The room above which they played the piano '
                                                                         'was on the first floor.'}],
                                          'tip': 'Never place an article between amely and the postposition: write '
                                                 "'amely mellett', never '*amely a mellett'."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'pairs': [   ['körfolyosó', 'open courtyard balcony / gang'],
                                                         ['bérház', 'tenement apartment building'],
                                                         ['házmester', 'building caretaker / concierge'],
                                                         ['nagypolgári lakás', 'grand bourgeois apartment'],
                                                         ['kapupénz', 'nighttime gate fee'],
                                                         ['társbérlet', 'co-tenancy / partitioned flat']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'question': 'Milyen szerepet töltött be a házmester a klasszikus pesti '
                                                        'bérházakban?',
                                            'options': [   'Ügyelt a rendre, este zárta a bejárati kaput, beszedte a '
                                                           'kapupénzt, és felügyelte a lakóközösséget.',
                                                           'Kizárólag az épület mérnöki terveit rajzolta újra minden '
                                                           'évben.',
                                                           'A belvárosi színházakban árusított belépőjegyeket a '
                                                           'bérlőknek.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'sentence': 'A belső udvar felett futó nyitott _____ a lakók mindennapi '
                                                        'találkozásainak és pletykáinak fő színtere volt.',
                                            'answer': 'körfolyosó',
                                            'english': 'The open courtyard balcony running above the inner yard was '
                                                       "the main scene of residents' daily encounters and gossip."},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-relative-postpositions'],
                                            'question': "Melyik vonatkozó szerkezet illeszkedik a mondatba? 'A bérház "
                                                        'kapualja, _____ a házmester lakása volt, este tíz után '
                                                        "bezárult.'",
                                            'options': ['amely mellett', 'amelyre', 'amelyből', 'amelyért'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'sentence': 'A belső udvar, _____ nyitott körfolyosók futottak körbe, '
                                                        'akusztikailag felerősítette a hangokat.',
                                            'answer': 'amely körül',
                                            'english': 'The inner courtyard, around which open galleries ran, '
                                                       'acoustically amplified the sounds.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'tiles': [   'A',
                                                         'fal,',
                                                         'amely',
                                                         'mögött',
                                                         'a',
                                                         'konyha',
                                                         'volt,',
                                                         'megrepedt.'],
                                            'solution': [   'A',
                                                            'fal,',
                                                            'amely',
                                                            'mögött',
                                                            'a',
                                                            'konyha',
                                                            'volt,',
                                                            'megrepedt.'],
                                            'english': 'The wall behind which the kitchen was located cracked.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-relative-postpositions'],
                                            'prompt': [   {   'speaker': 'Várostörténész',
                                                              'text': 'Hogyan jellemezné a gangos bérházak közösségi '
                                                                      'életét a századfordulón?'},
                                                          {'speaker': 'Építész', 'text': '_____'}],
                                            'options': [   'A belső udvar, amely körül a körfolyosók húzódtak, '
                                                           'egyfajta színházzá tette a mindennapokat, ahol alig '
                                                           'létezett titok a szomszédok előtt.',
                                                           'Az épületekben senki sem beszélt egymással, mert tilos '
                                                           'volt kilépni a folyosóra.',
                                                           'A lakások mind a puszta közepén álltak és nem voltak '
                                                           'folyosóik.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan alakult át sok nagypolgári lakás funkciója a második '
                                                        'világháború utáni Budapesten?',
                                            'options': [   'A lakáshiány miatt társbérletekké darabolták őket, ahol '
                                                           'idegen családok osztoztak a helyiségeken.',
                                                           'Valamennyit lebontották és mezőgazdasági területté '
                                                           'alakították.',
                                                           'Kizárólag diplomáciai követségekké alakították át a '
                                                           'belvárosi épületeket.'],
                                            'correct': 0}]},
                   {   'num': 2,
                       'title': 'Wekerletelep: A Garden City Vision in Budapest',
                       'grammar_label': 'Possessive relative chains with postpositions (amelynek udvarán, amelynek '
                                        'területén)',
                       'goals': [   'I can explain the origins, architectural philosophy, and community life of '
                                    "Kispest's Wekerletelep.",
                                    'I can construct complex relative clauses using amelynek + possessive noun + '
                                    'postposition.',
                                    'I can discuss garden-city planning, Transylvanian folk-revival architecture (Kós '
                                    'Károly), and municipal housing.'],
                       'story_segment': {   'seg_slug': 'wekerletelep',
                                            'title': 'Wekerletelep: A zöldellő kertvárosi álom',
                                            'summary': 'Initiated in 1908 by Prime Minister Sándor Wekerle, this model '
                                                       "garden suburb in Kispest combined Ebenezer Howard's urbanist "
                                                       'vision with Transylvanian folk-revival architecture designed '
                                                       "by Kós Károly and the 'Fiatalok' group.",
                                            'location': 'Budapest, Kispest Wekerletelep (1908–1930)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A huszadik század elejének rohamos '
                                                                          'iparosodása nyomán a fővárosi gyárak és '
                                                                          'hivatalok környékén súlyos lakásínség és '
                                                                          'egészségtelen zsúfoltság alakult ki. '
                                                                          'Wekerle Sándor miniszterelnök '
                                                                          'kezdeményezésére az állam 1908-ban '
                                                                          'nagyszabású kísérletbe kezdett: Kispest '
                                                                          'határában egy önálló, mintaszerű állami '
                                                                          'munkás- és tisztviselőtelep felépítését '
                                                                          'határozta el.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A tervezők az angol Ebenezer Howard által '
                                                                          'megfogalmazott kertváros-mozgalom elveit '
                                                                          'követték, amely a vidéki zöld környezet és '
                                                                          'a városi infrastruktúra előnyeit ötvözte. A '
                                                                          'település, amelynek területén több mint '
                                                                          'ötvenezer fát ültettek el, széles '
                                                                          'sugárutakkal, különálló kertes házakkal és '
                                                                          'önálló közintézményekkel — iskolákkal, '
                                                                          'orvosi rendelőkkel, rendőrséggel és piaccal '
                                                                          '— büszkélkedhetett.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A telep szimbolikus és építészeti szíve a '
                                                                          'központi Fő tér lett, a tér, amelynek '
                                                                          'mentén Kós Károly és az erdélyi népi '
                                                                          'motívumokból építkező „Fiatalok” '
                                                                          'építészcsoportja megalkotta a magyar népi '
                                                                          'szecesszió remekműveit. A faragott fa '
                                                                          'kapubélletek, a zömök tornyok és a meredek '
                                                                          'tetősíkok a kalotaszegi és székelyföldi '
                                                                          'erődtemplomok világát idézték fel a pesti '
                                                                          'síkságon.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Wekerletelep nemcsak építészeti, hanem '
                                                                          'szociális csodának is számított: minden '
                                                                          'lakóházhoz saját kertrész tartozott, '
                                                                          'amelynek udvarán a bérlők gyümölcsfákat '
                                                                          'gondoztak és zöldséget termesztettek. Ez a '
                                                                          'közvetlen földkapcsolat és a tiszta levegő '
                                                                          'hozzájárult ahhoz, hogy a telepen lakók '
                                                                          'egészségi állapota és gyermekhalandósága '
                                                                          'lényegesen jobb volt a belső kerületek '
                                                                          'átlagánál.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A telep máig megőrizte varázslatos, '
                                                                          'falusias jellegét és erős közösségi '
                                                                          'kohézióját. Wekerletelep védettséget élvező '
                                                                          'épületei azt bizonyítják, hogy a méltó és '
                                                                          'emberléptékű lakhatás megteremtése a modern '
                                                                          'várostervezés legsikeresebb és legtartósabb '
                                                                          'befektetése lehet.'}]},
                       'words': [   {'lemma': 'kertváros', 'translation': 'garden city / garden suburb', 'pos': 'noun'},
                                    {'lemma': 'főépítész', 'translation': 'chief architect', 'pos': 'noun'},
                                    {   'lemma': 'népi szecesszió',
                                        'translation': 'folk Secession / vernacular Art Nouveau',
                                        'pos': 'noun'},
                                    {   'lemma': 'mintatelep',
                                        'translation': 'model estate / model settlement',
                                        'pos': 'noun'},
                                    {'lemma': 'zöldövezet', 'translation': 'green belt / green zone', 'pos': 'noun'},
                                    {   'lemma': 'közösségkovácsoló',
                                        'translation': 'community-building / fostering solidarity',
                                        'pos': 'adjective'}],
                       'grammar_doc': {   'slug': 'amelynek-possessive-postpositions',
                                          'title': 'Possessive Relative Chains with Postpositions (amelynek udvarán, '
                                                   'amelynek területén)',
                                          'text1_title': 'Constructing Genitive Relative Postpositional Chains',
                                          'text1': 'When the anchor of a postposition is possessed by the antecedent, '
                                                   'Hungarian creates a genitive relative chain using amelynek + '
                                                   '[possessed noun + possessive suffix] + [postposition/case ending]: '
                                                   "'A kertváros, amelynek területén sok fa nő' (The garden city on "
                                                   "the territory of which many trees grow), 'A Fő tér, amelynek "
                                                   "mentén épületek állnak' (The Main Square along which buildings "
                                                   'stand).',
                                          'text2_title': 'Register and Style',
                                          'text2': "In spoken Hungarian, speakers often colloquially say 'aminek a "
                                                   "területén'. In elevated B2 essays and architectural evaluations, "
                                                   "always write 'amelynek területén' or 'amelynek mentén', omitting "
                                                   'the definite article after amelynek for elegant conciseness.',
                                          'table_title': 'Possessive Relative Chains with Postpositions',
                                          'table_rows': [   [   'A mintatelep, amelynek területén iskolák épültek, '
                                                                'mintaként szolgált.',
                                                                'The model estate on the territory of which schools '
                                                                'were built served as a pattern.'],
                                                            [   'A ház, amelynek udvarán virágoskert nyílt, Kós Károly '
                                                                'stílusát őrzi.',
                                                                'The house in the courtyard of which a flower garden '
                                                                "bloomed preserves Kós's style."],
                                                            [   'A sugárút, amelynek mentén platánok állnak, a Fő '
                                                                'térre vezet.',
                                                                'The boulevard along which plane trees stand leads to '
                                                                'the Main Square.']],
                                          'examples': [   {   'spanish': 'A városrész, amelynek központjában Kós kapui '
                                                                         'magasodnak, védett műemlék.',
                                                              'english': 'The city district in the center of which '
                                                                         "Kós's gates tower is a protected monument."},
                                                          {   'spanish': 'A lakóövezet, amelynek lakói összetartó '
                                                                         'közösséget alkotnak, példaértékű.',
                                                              'english': 'The residential zone whose residents form a '
                                                                         'tight-knit community is exemplary.'},
                                                          {   'spanish': 'A tér, amelynek peremén üzletek működtek, '
                                                                         'mindig forgalmas volt.',
                                                              'english': 'The square on the edge of which shops '
                                                                         'operated was always busy.'}],
                                          'tip': 'Ensure the noun has the 3rd person singular possessive suffix '
                                                 '(-a/-e/-ja/-je) before the postposition or case ending: amelynek '
                                                 'udvar-á-n, amelynek terület-é-n.'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'pairs': [   ['kertváros', 'garden suburb / garden city'],
                                                         ['főépítész', 'chief architect'],
                                                         ['népi szecesszió', 'vernacular Art Nouveau / folk Secession'],
                                                         ['mintatelep', 'model settlement estate'],
                                                         ['zöldövezet', 'green belt'],
                                                         ['közösségkovácsoló', 'community-building force']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'question': 'Milyen építészeti stílust képviselnek a Wekerletelep Fő '
                                                        'terének ikonikus épületei és kapui?',
                                            'options': [   'Kós Károly és a Fiatalok által megteremtett erdélyi '
                                                           'gyökerű magyar népi szecessziót.',
                                                           'A szovjet típusú szocialista realista panelesített '
                                                           'brutalizmust.',
                                                           'A francia mintájú neobarokk versailles-i palotastílust.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'sentence': 'Wekerletelep Kispest határában olyan állami _____ épült fel, '
                                                        'amely a munkások és tisztviselők számára biztosított emberhez '
                                                        'méltó lakhatást.',
                                            'answer': 'mintatelep',
                                            'english': 'Wekerletelep was built on the border of Kispest as a state '
                                                       'model settlement that ensured humane housing for workers and '
                                                       'clerks.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-relative-postpositions'],
                                            'question': 'Melyik birtokos vonatkozó kifejezés fejezi be helyesen a '
                                                        "mondatot? 'A Fő tér, _____ Kós Károly faragott kapui állnak, "
                                                        "a település központja.'",
                                            'options': ['amelynek mentén', 'amelyen', 'amellyel', 'amelyből'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'sentence': 'A kertes lakóház, _____ gyümölcsfák virágoztak, nyugalmat '
                                                        'nyújtott a lakóknak.',
                                            'answer': 'amelynek udvarán',
                                            'english': 'The residential house in the yard of which fruit trees bloomed '
                                                       'offered tranquility to the residents.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'tiles': [   'A',
                                                         'telep,',
                                                         'amelynek',
                                                         'területén',
                                                         'iskola',
                                                         'működött,',
                                                         'önellátó',
                                                         'volt.'],
                                            'solution': [   'A',
                                                            'telep,',
                                                            'amelynek',
                                                            'területén',
                                                            'iskola',
                                                            'működött,',
                                                            'önellátó',
                                                            'volt.'],
                                            'english': 'The settlement on the territory of which a school operated was '
                                                       'self-sufficient.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-relative-postpositions'],
                                            'prompt': [   {   'speaker': 'Várostervező',
                                                              'text': 'Miért számított különlegesnek Wekerletelep a '
                                                                      'korabeli Európában?'},
                                                          {'speaker': 'Építészettörténész', 'text': '_____'}],
                                            'options': [   'Mert egy olyan átgondolt kertváros valósult meg, amelynek '
                                                           'zöldövezetében a szociális jólét és a magas szintű népi '
                                                           'szecessziós építészet harmonikusan egyesült.',
                                                           'Mert kizárólag huszonöt emeletes felhőkarcolókat emeltek a '
                                                           'mezőn.',
                                                           'Mert a lakóknak megtiltották a kertek és növények '
                                                           'gondozását.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan befolyásolta a telepi lakók egészségét a kertes '
                                                        'környezet a szöveg szerint?',
                                            'options': [   'A saját kerti zöldségtermesztés és a tiszta levegő miatt a '
                                                           'halandóság lényegesen alacsonyabb volt a belvárosi '
                                                           'átlagnál.',
                                                           'A lakók azonnal megbetegedtek a fák túlzott közelségétől.',
                                                           'Semmilyen hatással nem volt az egészségi állapotukra.'],
                                            'correct': 0}]},
                   {   'num': 3,
                       'title': 'The Panel Era: Millions Move into Concrete Towers',
                       'grammar_label': 'Comparative and relational relative postpositions (amelyhez képest, amellyel '
                                        'szemben, amelynek révén)',
                       'goals': [   'I can recount the social and urban planning history of Hungarian prefabricated '
                                    'housing estates (lakótelepek).',
                                    'I can use amelyhez képest, amellyel szemben, and amelynek révén to draw nuanced '
                                    'architectural and sociological comparisons.',
                                    'I can discuss district heating, prefabrication, and modernization using B2 '
                                    'Hungarian vocabulary.'],
                       'story_segment': {   'seg_slug': 'lakotelepek',
                                            'title': 'Házgyári korszak: Modernizáció panelből',
                                            'summary': 'Between the 1960s and 1980s, state-directed industrial '
                                                       'prefabrication plants built massive housing estates across '
                                                       'Hungary, offering modern plumbing and district heating to '
                                                       'millions of working-class citizens.',
                                            'location': 'Óbuda, Újpalota és Pécs (1965–1985)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A második világháborút követően a gyors '
                                                                          'ütemű iparosítás és az urbanizáció '
                                                                          'Magyarországon is akut lakhatási krízist '
                                                                          'idézett elő. A Kádár-korszak vezetése '
                                                                          'felismerte, hogy a hagyományos téglás '
                                                                          'építkezés képtelen lépést tartani a '
                                                                          'lakásigényekkel, ezért 1960-ban '
                                                                          'meghirdették a tizenöt éves lakásépítési '
                                                                          'tervet, amely egymillió új otthon '
                                                                          'felépítését tűzte ki célul.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A megoldást a szovjet és dán licenc alapján '
                                                                          'létrehozott állami házgyárak jelentették. A '
                                                                          'vasbeton panelekből futószalagon '
                                                                          'előállított tíz- és négyemeletes '
                                                                          'épülettömbökből hatalmas új városrészek '
                                                                          'születtek: Budapesten Óbuda, Újpalota, '
                                                                          'Békásmegyer és Kelenföld, vidéken pedig '
                                                                          'Miskolc, Debrecen és Pécs alakult át '
                                                                          'gyökeresen.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A panelbe költözés a korabeli családok '
                                                                          'százezrei számára valóságos civilizációs '
                                                                          'ugrást jelentett, a régi komfort nélküli '
                                                                          'szoba-konyhás albérletekhez képest, '
                                                                          'amelyekhez képest az új lakások központi '
                                                                          'távfűtést, állandó meleg vizet, beépített '
                                                                          'konyhabútort és tiszta, saját fürdőszobát '
                                                                          'kínáltak.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Ugyanakkor a lakótelepi életnek megvoltak a '
                                                                          'maga árnyoldalai is. A rossz hangszigetelés '
                                                                          'nyomán a szomszédok léptei és veszekedései '
                                                                          'áthallatszottak a vékony falakon, az '
                                                                          'egyenméretű terek szűkössé váltak a növekvő '
                                                                          'kamaszok számára, a sivár beton terek pedig '
                                                                          'lassan alakultak át valódi zöldellő '
                                                                          'közösségi környezetté.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A rendszerváltás után a privatizáció révén '
                                                                          'a lakók többsége megvásárolta otthonát. Az '
                                                                          'ezredfordulón indított felújítási '
                                                                          'programok, amelyek révén a házak '
                                                                          'hőszigetelést és színes homlokzatot kaptak, '
                                                                          'megújították a telepek arculatát, ahol máig '
                                                                          'a magyar lakosság közel egyötöde éli '
                                                                          'mindennapjait.'}]},
                       'words': [   {   'lemma': 'házgyár',
                                        'translation': 'prefabrication plant / concrete panel factory',
                                        'pos': 'noun'},
                                    {   'lemma': 'lakótelep',
                                        'translation': 'prefab housing estate / panel development',
                                        'pos': 'noun'},
                                    {'lemma': 'távfűtés', 'translation': 'district heating', 'pos': 'noun'},
                                    {   'lemma': 'összkomfortos',
                                        'translation': 'fully modernized / with all conveniences',
                                        'pos': 'adjective'},
                                    {'lemma': 'lakáshiány', 'translation': 'housing shortage', 'pos': 'noun'},
                                    {   'lemma': 'panelprogram',
                                        'translation': 'panel refurbishment / thermal retrofitting program',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'amelyhez-kepest-relational',
                                          'title': 'Comparative and Relational Relative Postpositions (amelyhez '
                                                   'képest, amellyel szemben)',
                                          'text1_title': 'Relational Postpositions with Inflected Relative Pronouns',
                                          'text1': 'Postpositions that govern oblique grammatical cases require the '
                                                   'relative pronoun amely to take the matching case suffix: képest '
                                                   'governs the allative (-hoz/-hez/-höz -> amelyhez képest = '
                                                   "'compared to which'); szemben governs the instrumental (-val/-vel "
                                                   "-> amellyel szemben = 'in contrast to which'); révén governs the "
                                                   "genitive/nominative -> amelynek révén = 'by means of which'.",
                                          'text2_title': 'Sociological Nuance in Comparative Discourse',
                                          'text2': 'These structures are fundamental in B2 academic and evaluative '
                                                   'Hungarian, allowing concise contrasts without interrupting '
                                                   "sentence cohesion: 'A panel lakás összkomfortot nyújtott, amelyhez "
                                                   "képest a régi cselédlakások szinte lakhatatlanok voltak.'",
                                          'table_title': 'Comparative Relational Postpositions',
                                          'table_rows': [   [   'A régi bérházak sötétek voltak, amelyekhez képest a '
                                                                'panel világos volt.',
                                                                'The old tenements were dark, compared to which the '
                                                                'panel flat was bright.'],
                                                            [   'Megjelent a modern technológia, amellyel szemben a '
                                                                'kézi munka lassúnak tűnt.',
                                                                'Modern technology appeared, in contrast to which '
                                                                'manual labor seemed slow.'],
                                                            [   'Elindult a felújítás, amelynek révén csökkent a '
                                                                'fűtési költség.',
                                                                'Renovation started, by means of which heating costs '
                                                                'decreased.']],
                                          'examples': [   {   'spanish': 'A távfűtés olyan kényelmet biztosított, '
                                                                         'amelyhez képest a szenes kályha elavult '
                                                                         'volt.',
                                                              'english': 'District heating provided such comfort '
                                                                         'compared to which the coal stove was '
                                                                         'obsolete.'},
                                                          {   'spanish': 'A szürke beton tömbökkel szemben a mai '
                                                                         'lakótelepek színesek és parkosítottak.',
                                                              'english': "In contrast to gray concrete blocks, today's "
                                                                         'housing estates are colorful and '
                                                                         'landscaped.'},
                                                          {   'spanish': 'A szigetelési program, amelynek révén '
                                                                         'energiát takarítanak meg, sikeres volt.',
                                                              'english': 'The insulation program, by means of which '
                                                                         'they save energy, was successful.'}],
                                          'tip': "Carefully align pronoun suffixes: 'amely-hez képest', 'amellyel "
                                                 "(amely-vel) szemben', 'amely-nek révén'."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'pairs': [   ['házgyár', 'prefabricated panel factory'],
                                                         ['lakótelep', 'prefab housing estate'],
                                                         ['távfűtés', 'district central heating'],
                                                         ['összkomfortos', 'with all modern conveniences'],
                                                         ['lakáshiány', 'housing shortage'],
                                                         ['panelprogram', 'thermal retrofitting program']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'question': 'Miért jelentett óriási civilizációs előrelépést a lakótelepi '
                                                        'lakás a hatvanas évek bérlői számára?',
                                            'options': [   'Mert összkomfortos lakást kaptak központi távfűtéssel, '
                                                           'folyó meleg vízzel és saját fürdőszobával.',
                                                           'Mert minden lakáshoz ingyenes gépkocsi és vidéki nyaraló '
                                                           'járt az államtól.',
                                                           'Mert a lakásokban nem kellett villanyszámlát fizetni '
                                                           'semmilyen elektromos eszköz után.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'sentence': 'A panelépületek energetikai korszerűsítését és hőszigetelését '
                                                        'az államilag támogatott _____ segítette elő.',
                                            'answer': 'panelprogram',
                                            'english': 'The energetic modernization and thermal insulation of panel '
                                                       'buildings was fostered by the state-subsidized panel program.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-relative-postpositions'],
                                            'question': "Melyik szerkezet fejezi ki helyesen az összehasonlítást? 'A "
                                                        'panel modern kényelmet adott, _____ a régi udvari '
                                                        "szoba-konyha elmaradottnak tűnt.'",
                                            'options': [   'amelyhez képest',
                                                           'amelynek révén',
                                                           'amellyel szemben',
                                                           'amely felé'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'sentence': 'Megvalósult az épület felújítása, _____ az ott élők '
                                                        'jelentősen csökkentették fűtési kiadásaikat.',
                                            'answer': 'amelynek révén',
                                            'english': 'The building refurbishment was realized, by means of which '
                                                       'residents significantly lowered their heating expenses.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'tiles': [   'A',
                                                         'távfűtés',
                                                         'olyan',
                                                         'kényelem',
                                                         'volt,',
                                                         'amelyhez',
                                                         'képest',
                                                         'a',
                                                         'kályha',
                                                         'elavult.'],
                                            'solution': [   'A',
                                                            'távfűtés',
                                                            'olyan',
                                                            'kényelem',
                                                            'volt,',
                                                            'amelyhez',
                                                            'képest',
                                                            'a',
                                                            'kályha',
                                                            'elavult.'],
                                            'english': 'District heating was such a comfort, compared to which the '
                                                       'stove was obsolete.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-relative-postpositions'],
                                            'prompt': [   {   'speaker': 'Szociológus',
                                                              'text': 'Hogyan ítélik meg ma a szakemberek a '
                                                                      'szocialista lakótelepek örökségét?'},
                                                          {'speaker': 'Urbanista', 'text': '_____'}],
                                            'options': [   'Bár az egyhangú betontömbökkel szemben sok kritika '
                                                           'fogalmazódott meg, a házgyári lakások százezrek lakhatási '
                                                           'gondját oldották meg modern módon.',
                                                           'Valamennyi panelépületet lebontották már az 1990-es évek '
                                                           'elején.',
                                                           'A lakótelepeken ma már senki sem lakik Magyarországon.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan privatizálták a panel lakásokat a rendszerváltást '
                                                        'követően?',
                                            'options': [   'A bérlők rendkívül kedvezményes áron megvásárolhatták az '
                                                           'állami bérlakásaikat.',
                                                           'Az állam kötelezte a lakókat a lakások elhagyására.',
                                                           'Az épületeket külföldi luxushotelekké alakították át.'],
                                            'correct': 0}]},
                   {   'num': 4,
                       'title': 'Ruin Bars and the Reinvention of the Inner Districts',
                       'grammar_label': 'Spatial-directional postpositions in relative clauses (amely felé, amely '
                                        'köré, amelyeken keresztül)',
                       'goals': [   'I can analyze the rise of ruin bars (romkocsmák) and cultural revival in '
                                    "Budapest's historic 7th District.",
                                    'I can construct relative clauses with directional postpositions (felé, köré, '
                                    'át/keresztül).',
                                    'I can evaluate heritage conservation, alternative art spaces, and overtourism in '
                                    'Hungarian.'],
                       'story_segment': {   'seg_slug': 'romkocsmak',
                                            'title': 'Romkocsmák: Az elhagyott terek új élete',
                                            'summary': 'At the turn of the millennium, abandoned courtyards and '
                                                       'slated-for-demolition tenements in the old Jewish Quarter '
                                                       "became the birthplace of Budapest's world-famous ruin bar "
                                                       'culture, turning urban decay into alternative artistic '
                                                       'vitality.',
                                            'location': 'Budapest, Erzsébetváros (Kazinczy utca és Klauzál tér) '
                                                        '(2001–2024)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A rendszerváltást követő évtizedben '
                                                                          'Budapest történelmi zsidónegyede, '
                                                                          'Belső-Erzsébetváros a pusztulás szélére '
                                                                          'sodródott. Az elhanyagolt tizenkilencedik '
                                                                          'századi bérházak omladozó vakolattal, '
                                                                          'bedeszkázott ablakokkal várták a '
                                                                          'bizonytalan sorsú ingatlanfejlesztéseket '
                                                                          'vagy a teljes bontást.'},
                                                              {   'type': 'narration',
                                                                  'text': '2001 körül azonban fiatal művészek és '
                                                                          'vállalkozók felismerték az elhagyott '
                                                                          'terekben rejlő szabadságot. Megnyitották az '
                                                                          'első romkocsmákat — köztük a legendás '
                                                                          'Szimpla Kertet —, amely a Kazinczy utcai '
                                                                          'romos udvarra költözve a budapesti '
                                                                          'kulturális reneszánsz jelképévé vált.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A romkocsma-esztétika lényege a kreatív '
                                                                          'újrahasznosítás volt. A lomtalanítások '
                                                                          'során összegyűjtött régi fotelok, '
                                                                          'zománcozott kádak, leselejtezett Trabant '
                                                                          'autók és eklektikus lámpák olyan bohém '
                                                                          'atmoszférát teremtettek, a kezdeményezés, '
                                                                          'amely köré gyorsan nemzetközi '
                                                                          'művészközösség és élénk civil élet '
                                                                          'szerveződött.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A romkocsmák napközben termelői piacoknak, '
                                                                          'civil kerekasztaloknak, független színházi '
                                                                          'előadásoknak és bolhapiacoknak adtak '
                                                                          'otthont. A szűk utcák, amelyeken keresztül '
                                                                          'a látogatók az udvarokba áramlottak, a '
                                                                          'világ minden tájáról vonzották az '
                                                                          'alternatív városi kultúrára fogékony '
                                                                          'utazókat.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A spontán siker azonban hamarosan '
                                                                          'konfliktusokhoz vezetett. A rohamosan '
                                                                          'terjedő buliturizmus, az éjszakai '
                                                                          'zajártalom és a rövid távú lakáskiadás '
                                                                          'kiszorította a régi helyi lakosokat, éles '
                                                                          'vitát robbantva ki a műemlékvédelem, az '
                                                                          'élhető lakókörnyezet és a szórakoztatóipar '
                                                                          'érdekei között.'}]},
                       'words': [   {'lemma': 'romkocsma', 'translation': 'ruin bar', 'pos': 'noun'},
                                    {   'lemma': 'műemlékvédelem',
                                        'translation': 'historic heritage preservation',
                                        'pos': 'noun'},
                                    {'lemma': 'buliturizmus', 'translation': 'party tourism', 'pos': 'noun'},
                                    {'lemma': 'patina', 'translation': 'patina / aged character', 'pos': 'noun'},
                                    {   'lemma': 'közösségi tér',
                                        'translation': 'community space / civic venue',
                                        'pos': 'noun'},
                                    {   'lemma': 'lomtalanítás',
                                        'translation': 'annual municipal bulk-waste clearing / salvage',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'amely-directional-postpositions',
                                          'title': 'Directional and Dynamic Relative Postpositions (amely köré, amely '
                                                   'felé, amelyeken keresztül)',
                                          'text1_title': 'Expressing Dynamic Movement and Orientation',
                                          'text1': 'Directional postpositions govern movement or metaphorical '
                                                   'orientation: köré expresses movement around or focal gathering '
                                                   "('az ötlet, amely köré művészek gyűltek' = the idea around which "
                                                   "artists gathered); felé marks orientation toward a destination ('a "
                                                   "cél, amely felé törekednek'); keresztül indicates passage through "
                                                   "space ('az udvarok, amelyeken keresztül átvághatunk').",
                                          'text2_title': 'Plural Concord with amelyek',
                                          'text2': 'When the antecedent noun is plural, ensure the relative pronoun '
                                                   "matches in number before the postposition: 'a kapualjak, amelyeken "
                                                   "keresztül' (the gateways through which), 'az épületek, amelyek "
                                                   "köré vendéglők települtek' (the buildings around which restaurants "
                                                   'settled).',
                                          'table_title': 'Directional Relative Postpositions',
                                          'table_rows': [   [   'A romkocsma lett a mag, amely köré az alternatív '
                                                                'kultúra szerveződött.',
                                                                'The ruin bar became the core around which alternative '
                                                                'culture organized.'],
                                                            [   'A szűk utcák, amelyeken keresztül a vendégek '
                                                                'érkeztek, megteltek élettel.',
                                                                'The narrow streets through which guests arrived '
                                                                'filled with life.'],
                                                            [   'A városvezetés kijelölte az irányt, amely felé '
                                                                'fejleszteni kívánja a negyedet.',
                                                                'The city leadership designated the direction toward '
                                                                'which it wishes to develop the district.']],
                                          'examples': [   {   'spanish': 'A civil összefogás, amely köré a lakók '
                                                                         'tömörültek, megvédte a fákat.',
                                                              'english': 'The civic coalition around which residents '
                                                                         'banded together protected the trees.'},
                                                          {   'spanish': 'A sikátorok, amelyeken keresztül '
                                                                         'megközelíthető az udvar, macskakövesek.',
                                                              'english': 'The alleys through which the courtyard can '
                                                                         'be approached are cobblestone.'},
                                                          {   'spanish': 'A kulturális megújulás, amely felé a negyed '
                                                                         'elindult, világhírűvé vált.',
                                                              'english': 'The cultural renewal toward which the '
                                                                         'district set off became world-famous.'}],
                                          'tip': 'Distinguish köré (motion toward/around: amely köré) from körül '
                                                 '(static location: amely körül).'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'pairs': [   ['romkocsma', 'ruin bar'],
                                                         ['műemlékvédelem', 'heritage monument protection'],
                                                         ['buliturizmus', 'party tourism'],
                                                         ['patina', 'historic architectural patina'],
                                                         ['közösségi tér', 'community civic space'],
                                                         ['lomtalanítás', 'annual bulk waste cleanup']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'question': 'Hogyan alakult ki a budapesti romkocsmák jellegzetes vizuális '
                                                        'berendezése?',
                                            'options': [   'Lomtalanítások során megmentett vintage bútorok, retró '
                                                           'tárgyak és művészi alkotások kreatív újrahasznosításával.',
                                                           'Kizárólag svéd bútoráruházakból rendelt egységes, modern '
                                                           'műanyag elemekből.',
                                                           'Történelmi királyi palotákból kiselejtezett aranyozott '
                                                           'trónszékekből.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'sentence': 'A történelmi épületek eredeti homlokzatának és hangulatának '
                                                        'megőrzését a szigorú állami _____ hivatott biztosítani.',
                                            'answer': 'műemlékvédelem',
                                            'english': 'The preservation of the original façade and atmosphere of '
                                                       'historic buildings is meant to be ensured by strict state '
                                                       'monument protection.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-relative-postpositions'],
                                            'question': 'Melyik irányhármassági névutós alak fejezi ki a '
                                                        "csoportosulást egy központi mag felé? 'A romkocsma olyan "
                                                        'kulturális központtá vált, _____ sok fiatal alkotó gyűlt '
                                                        "össze.'",
                                            'options': ['amely köré', 'amely alól', 'amely nélkül', 'amely szerint'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'sentence': 'A történelmi átjáróházak, _____ a gyalogosok átvághattak a '
                                                        'szomszédos utcákba, igazi pesti különlegességek.',
                                            'answer': 'amelyeken keresztül',
                                            'english': 'The historic passage-houses through which pedestrians could '
                                                       'cut across to neighboring streets are true Pest specialties.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'tiles': [   'A',
                                                         'kezdeményezés,',
                                                         'amely',
                                                         'köré',
                                                         'művészek',
                                                         'gyűltek,',
                                                         'világhírű',
                                                         'lett.'],
                                            'solution': [   'A',
                                                            'kezdeményezés,',
                                                            'amely',
                                                            'köré',
                                                            'művészek',
                                                            'gyűltek,',
                                                            'világhírű',
                                                            'lett.'],
                                            'english': 'The initiative around which artists gathered became '
                                                       'world-famous.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-relative-postpositions'],
                                            'prompt': [   {   'speaker': 'Kulturális újságíró',
                                                              'text': 'Hogyan egyeztethető össze a romkocsmák sikere '
                                                                      'az Erzsébetváros lakóinak érdekeivel?'},
                                                          {'speaker': 'Városkutató', 'text': '_____'}],
                                            'options': [   'Nehezen, mert a buliturizmus, amely felé a negyed '
                                                           'eltolódott, komoly zajterhelést okoz az ott élőknek, '
                                                           'miközben a kulturális funkció háttérbe szorult.',
                                                           'Nagyon könnyen, mert a turisták kizárólag csendben '
                                                           'olvasnak a kocsmákban.',
                                                           'Az Erzsébetvárosban nincsenek lakók, így nincs senki, akit '
                                                           'zavarna a zaj.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen nappali közösségi funkciókat töltöttek be a népszerűbb '
                                                        'romkocsmák a szöveg szerint?',
                                            'options': [   'Termelői piacoknak, civil kerekasztaloknak és független '
                                                           'színházi előadásoknak adtak teret.',
                                                           'Gépjármű-összeszerelő üzemekként működtek reggeltől estig.',
                                                           'Kizárólag politikai pártok központi irodáiként '
                                                           'szolgáltak.'],
                                            'correct': 0}]},
                   {   'num': 5,
                       'title': 'Affordability, Heritage, and the Future of the City',
                       'grammar_label': 'Complex nested relative clauses with postpositional phrases in urban '
                                        'sociology',
                       'goals': [   'I can summarize contemporary debates on Budapest housing affordability, '
                                    'suburbanization, and smart urban renewal.',
                                    'I can construct complex multi-tiered relative clauses with postpositional phrases '
                                    'in B2 prose.',
                                    'I can debate gentrification, energy efficiency, and urban design in Hungarian.'],
                       'story_segment': {   'seg_slug': 'varoseletjovoje',
                                            'title': 'Megfizethetőség, zöld város és jövőkép',
                                            'summary': 'Contemporary Budapest faces the dual challenges of '
                                                       'skyrocketing property prices and climate adaptation, prompting '
                                                       'urbanists to champion brownfield regenerations, municipal '
                                                       'rental systems, and balanced suburban transit.',
                                            'location': 'Budapest és az agglomeráció (napjainkban)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A huszonegyedik század harmadik évtizedére '
                                                                          'a magyar főváros lakáspiacán komoly '
                                                                          'lakhatási válság bontakozott ki. A '
                                                                          'négyzetméterárak és a bérleti díjak '
                                                                          'ugrásszerű növekedése miatt a fiatal '
                                                                          'pályakezdők és az alacsonyabb jövedelmű '
                                                                          'családok számára a belvárosi lakásbérlés '
                                                                          'szinte megfizethetetlenné vált.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Ennek közvetlen következményeként '
                                                                          'felgyorsult a szuburbanizáció: családok '
                                                                          'tízezrei költöztek ki a Budapest körüli '
                                                                          'agglomerációs településekre a zöldebb '
                                                                          'környezet és a megfizethetőbb kertes házak '
                                                                          'reményében. A tömeges kiköltözés azonban a '
                                                                          'bevezető utakon mindennapos közlekedési '
                                                                          'dugókat, a kistelepüléseken pedig súlyos '
                                                                          'óvodai és iskolai férőhelyhiányt idézett '
                                                                          'elő.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Az urbanisták arra hívják fel a figyelmet, '
                                                                          'hogy a valódi megoldást a meglévő városi '
                                                                          'szövet megújítása jelenti. A volt ipari és '
                                                                          'vasúti rozsdaövezetek, amelyek mentén új '
                                                                          'lakónegyedek épülnek, és amelyek területén '
                                                                          'modern parkokat alakítanak ki, hatékonyan '
                                                                          'tehermentesíthetik a zsúfolt belvárost a '
                                                                          'zöldterületek feláldozása nélkül.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Kiemelt feladat a meglévő épületállomány '
                                                                          'energetikai korszerűsítése. A történelmi '
                                                                          'bérházak, amelyek homlokzata mögött rosszul '
                                                                          'szigetelt falak húzódnak, hatalmas fűtési '
                                                                          'energiát pazarolnak el, így az '
                                                                          'energiahatékonyság javítása nemcsak '
                                                                          'rezsicsökkentési, hanem klímavédelmi '
                                                                          'kötelesség is.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A jövő fenntartható Budapestje olyan átfogó '
                                                                          'bérlakásrendszerre és városrehabilitációra '
                                                                          'épülhet, amely a gazdasági innovációt, a '
                                                                          'műemléki örökség tiszteletét és a szociális '
                                                                          'biztonságot egyszerre garantálja minden '
                                                                          'városlakó számára.'}]},
                       'words': [   {   'lemma': 'lakhatási válság',
                                        'translation': 'housing crisis / affordability crisis',
                                        'pos': 'noun'},
                                    {   'lemma': 'rozsdaövezet',
                                        'translation': 'brownfield zone / former industrial site',
                                        'pos': 'noun'},
                                    {   'lemma': 'szuburbanizáció',
                                        'translation': 'suburbanization / suburban sprawl',
                                        'pos': 'noun'},
                                    {'lemma': 'energiahatékonyság', 'translation': 'energy efficiency', 'pos': 'noun'},
                                    {   'lemma': 'bérlakásrendszer',
                                        'translation': 'municipal rental housing system',
                                        'pos': 'noun'},
                                    {   'lemma': 'városrehabilitáció',
                                        'translation': 'urban renewal / neighborhood regeneration',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'nested-relative-postpositions',
                                          'title': 'Synthesizing Complex Relative Postpositional Structures in Urban '
                                                   'Debates',
                                          'text1_title': 'Multi-Tiered Relative Clauses with Postpositions',
                                          'text1': 'Advanced B2 essays often coordinate multiple relative clauses '
                                                   "anchored by postpositions: 'Az a rozsdaövezeti beruházás, amelynek "
                                                   'területén lakások épülnek, és amelyhez képest a régebbi telepek '
                                                   "elavultnak tűnnek...' (That brownfield investment on the territory "
                                                   'of which flats are being built, and compared to which older '
                                                   'estates seem obsolete...).',
                                          'text2_title': 'Clarity in Complex Syntax',
                                          'text2': 'Maintain clear antecedents and proper punctuation. Repeat the '
                                                   "relative pronoun when shifting postpositional cases: 'A városrész, "
                                                   'amelynek mentén villamosvonal fut, és amelyben modern parkokat '
                                                   "terveztek...'",
                                          'table_title': 'Complex Postpositional Relative Constructions',
                                          'table_rows': [   [   'A rozsdaövezet, amelynek területén új lakások '
                                                                'épülnek, zöld parkot kapott.',
                                                                'The brownfield on the territory of which new flats '
                                                                'are built received a green park.'],
                                                            [   'A program, amelynek révén megújul a negyed, mintaként '
                                                                'szolgál.',
                                                                'The program by means of which the district is renewed '
                                                                'serves as a model.'],
                                                            [   'A régi bérház, amelynek falai mögött korszerű lakások '
                                                                'vannak, megújult.',
                                                                'The old tenement behind whose walls are modern flats '
                                                                'was renewed.']],
                                          'examples': [   {   'spanish': 'A városrehabilitáció, amelynek keretében '
                                                                         'felújítják a házakat, javítja az '
                                                                         'életminőséget.',
                                                              'english': 'The urban rehabilitation in the framework of '
                                                                         'which houses are renovated improves quality '
                                                                         'of life.'},
                                                          {   'spanish': 'Az agglomerációs zóna, amely felé a családok '
                                                                         'költöznek, közlekedési fejlesztést igényel.',
                                                              'english': 'The agglomeration zone toward which families '
                                                                         'are moving requires transport development.'},
                                                          {   'spanish': 'Az új bérlakásrendszer, amelyhez képest a '
                                                                         'piaci albérlet drága, biztonságot nyújt.',
                                                              'english': 'The new municipal rental system, compared to '
                                                                         'which market rent is expensive, provides '
                                                                         'security.'}],
                                          'tip': 'Keep antecedent reference unambiguous: if coordinating two relative '
                                                 "clauses, link them with 'és' while repeating 'amely' with its proper "
                                                 'postposition or case.'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'pairs': [   ['lakhatási válság', 'housing affordability crisis'],
                                                         ['rozsdaövezet', 'industrial brownfield site'],
                                                         ['szuburbanizáció', 'suburban sprawl migration'],
                                                         ['energiahatékonyság', 'energy efficiency'],
                                                         ['bérlakásrendszer', 'municipal rental housing system'],
                                                         ['városrehabilitáció', 'urban neighborhood regeneration']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'question': 'Milyen kihívásokkal szembesülnek azok a családok, akik a '
                                                        'szuburbanizáció révén az agglomerációba költöznek?',
                                            'options': [   'Mindennapos közlekedési dugókkal a bevezető utakon és '
                                                           'férőhelyhiánnyal az intézményekben.',
                                                           'Az elektromos áram és a vezetékes víz teljes hiányával.',
                                                           'A belvárosba való belépés hatósági megtiltásával.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-lakhatas-vocab'],
                                            'sentence': 'A használaton kívüli vasúti és ipari telephelyek, vagyis a '
                                                        'volt _____, kiváló terepet nyújtanak új, zöld lakónegyedek '
                                                        'építésére.',
                                            'answer': 'rozsdaövezetek',
                                            'english': 'Disused railway and industrial premises, that is, former '
                                                       'brownfields, provide excellent grounds for building new green '
                                                       'residential districts.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-relative-postpositions'],
                                            'question': "Melyik szerkezet illeszkedik a mondatba? 'A felújítási "
                                                        'program, _____ korszerűsítik az épületeket, támogatást '
                                                        "kapott.'",
                                            'options': [   'amelynek keretében',
                                                           'amellyel szemben',
                                                           'amely felé',
                                                           'amely alól'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'sentence': 'A történelmi bérház, _____ modern hőszigetelést építettek be, '
                                                        'lényegesen kevesebb energiát fogyaszt.',
                                            'answer': 'amelynek falai közé',
                                            'english': 'The historic tenement between whose walls modern insulation '
                                                       'was installed consumes significantly less energy.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-relative-postpositions'],
                                            'tiles': [   'A',
                                                         'rozsdaövezet,',
                                                         'amelynek',
                                                         'területén',
                                                         'park',
                                                         'épül,',
                                                         'megújul.'],
                                            'solution': [   'A',
                                                            'rozsdaövezet,',
                                                            'amelynek',
                                                            'területén',
                                                            'park',
                                                            'épül,',
                                                            'megújul.'],
                                            'english': 'The brownfield on the territory of which a park is being built '
                                                       'is renewed.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-relative-postpositions'],
                                            'prompt': [   {   'speaker': 'Urbanista',
                                                              'text': 'Hogyan oldható meg a budapesti lakhatási válság '
                                                                      'hosszú távon?'},
                                                          {'speaker': 'Polgármester', 'text': '_____'}],
                                            'options': [   'Olyan bérlakásprogrammal, amelynek révén megfizethető '
                                                           'otthonok létesülnek a volt rozsdaövezetekben, és amelyhez '
                                                           'képest a piaci albérletárak mérséklődhetnek.',
                                                           'Úgy, hogy betiltjuk a vidékről érkező diákok letelepedését '
                                                           'a fővárosban.',
                                                           'Úgy, hogy minden parkot betonozott parkolóvá alakítunk '
                                                           'át.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Miért kiemelten fontos a belvárosi épületállomány energetikai '
                                                        'korszerűsítése a szöveg szerint?',
                                            'options': [   'Mert a régi, rosszul szigetelt bérházak rengeteg energiát '
                                                           'pazarolnak el, így a felújítás klímavédelmi és anyagi '
                                                           'érdek is.',
                                                           'Mert a fűtés teljesen feleslegessé vált a fővárosban.',
                                                           'Mert az új szigetelés megsemmisíti a történelmi '
                                                           'műemlékeket.'],
                                            'correct': 0}]}],
    'consolidation': {   'goals': [   'I can trace the social history of Hungarian housing from 19th-century gangos '
                                      'tenements and Wekerletelep to socialist panel estates and modern ruin bars.',
                                      'I can master relative clauses with simple, possessive, relational, and '
                                      'directional postpositions (amely mellett, amelynek udvarán, amelyhez képest, '
                                      'amely köré, amelyeken keresztül).',
                                      'I can debate gentrification, urban regeneration, and housing affordability in '
                                      'sophisticated B2 Hungarian.',
                                      'I can actively deploy 30 B2 architecture, urban planning, and housing sociology '
                                      'terms.'],
                         'exercises': [   {   'type': 'matching',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-lakhatas-vocab'],
                                              'pairs': [   ['körfolyosó', 'open courtyard balcony / gang'],
                                                           ['kertváros', 'garden suburb / garden city'],
                                                           ['lakótelep', 'prefabricated housing estate'],
                                                           ['romkocsma', 'ruin bar'],
                                                           ['rozsdaövezet', 'industrial brownfield site'],
                                                           ['lakhatási válság', 'housing affordability crisis']]},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'teaches': ['b2-relative-postpositions'],
                                              'question': 'Which relative postpositional construction correctly '
                                                          "expresses 'compared to which' in Hungarian?",
                                              'options': [   'amelyhez képest',
                                                             'amellyel szemben',
                                                             'amelynek révén',
                                                             'amely felé'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-lakhatas-vocab'],
                                              'question': 'Kinek a tervei alapján épült fel a kispesti Wekerletelep '
                                                          'ikonikus Fő tere és székely kapus épületegyüttese?',
                                              'options': [   'Kós Károly és a Fiatalok építészcsoportja tervei '
                                                             'alapján.',
                                                             'Pollack Mihály és Ybl Miklós tervei alapján.',
                                                             'Le Corbusier tervei alapján.',
                                                             'Steindl Imre tervei alapján.'],
                                              'correct': 0},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'teaches': ['b2-lakhatas-vocab'],
                                              'sentence': 'A klasszikus pesti bérházban este tíz óra után a bérlőknek '
                                                          '_____ kellett fizetniük a kaput nyitó gondnoknak.',
                                              'answer': 'kapupénzt',
                                              'english': "In the classic Pest tenement, after ten o'clock at night "
                                                         'tenants had to pay a gate fee to the caretaker opening the '
                                                         'door.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-relative-postpositions'],
                                              'sentence': 'A belső udvar, _____ nyitott körfolyosók húzódtak, a ház '
                                                          'társasági központja volt.',
                                              'answer': 'amely körül',
                                              'english': 'The inner courtyard around which open galleries ran was the '
                                                         'social center of the house.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-relative-postpositions'],
                                              'sentence': 'A panel kényelmes otthont adott, _____ a régi szoba-konyhás '
                                                          'lakások sötétnek bizonyultak.',
                                              'answer': 'amelyhez képest',
                                              'english': 'The panel provided a comfortable home, compared to which the '
                                                         'old room-and-kitchen flats proved dark.'},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-relative-postpositions'],
                                              'prompt': [   {   'speaker': 'Turista',
                                                                'text': 'Hogyan jöttek létre a híres pesti romkocsmák '
                                                                        'az ezredforduló után?'},
                                                            {'speaker': 'Idegenvezető', 'text': '_____'}],
                                              'options': [   'A zsidónegyed elhagyott bérházaiban nyíltak meg, amelyek '
                                                             'udvarán művészek és fiatalok alakítottak ki egyedi '
                                                             'közösségi tereket újrahasznosított tárgyakból.',
                                                             'Minden romkocsmát a kormány építtetett hatalmas '
                                                             'költségvetésből.',
                                                             'A romkocsmák kizárólag a Duna vizén úszó hajókon '
                                                             'működnek.'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'teaches': ['b2-relative-postpositions'],
                                              'question': 'Which sentence demonstrates proper grammatical concord with '
                                                          'a plural antecedent and a directional postposition?',
                                              'options': [   'A szűk sikátorok, amelyeken keresztül a vendégek az '
                                                             'udvarba jutottak, macskakövesek voltak.',
                                                             'A szűk sikátorok, amely keresztül a vendégek mentek, '
                                                             'kövesek voltak.',
                                                             'A sikátor, amelyeken keresztül a vendégek futottak, '
                                                             'széles volt.',
                                                             'A vendégek, sikátorok amely keresztül érkeztek, '
                                                             'megálltak.'],
                                              'correct': 0},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-relative-postpositions'],
                                              'prompt': [   {   'speaker': 'Kutató',
                                                                'text': 'Milyen előnyöket kínálnak a barnamezős '
                                                                        'beruházások a zöldmezős építkezésekkel '
                                                                        'szemben?'},
                                                            {'speaker': 'Urbanista', 'text': '_____'}],
                                              'options': [   'A volt ipari rozsdaövezetek, amelyek területén új '
                                                             'negyedek épülnek, már rendelkeznek közlekedési '
                                                             'kapcsolatokkal, és megóvják a külvárosi természeti '
                                                             'zónákat.',
                                                             'A rozsdaövezetekben tilos lakóépületeket emelni az '
                                                             'elkövetkező száz évben.',
                                                             'A zöldmezős beruházások mindig olcsóbbak és nem '
                                                             'igényelnek utakat.'],
                                              'correct': 0},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-relative-postpositions'],
                                              'tiles': [   'A',
                                                           'mintatelep,',
                                                           'amelynek',
                                                           'területén',
                                                           'fák',
                                                           'állnak,',
                                                           'védett',
                                                           'örökség.'],
                                              'solution': [   'A',
                                                              'mintatelep,',
                                                              'amelynek',
                                                              'területén',
                                                              'fák',
                                                              'állnak,',
                                                              'védett',
                                                              'örökség.'],
                                              'english': 'The model settlement on the territory of which trees stand '
                                                         'is protected heritage.'},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-relative-postpositions'],
                                              'tiles': [   'A',
                                                           'program,',
                                                           'amelynek',
                                                           'révén',
                                                           'szigeteltek,',
                                                           'nagyon',
                                                           'sikeres',
                                                           'volt.'],
                                              'solution': [   'A',
                                                              'program,',
                                                              'amelynek',
                                                              'révén',
                                                              'szigeteltek,',
                                                              'nagyon',
                                                              'sikeres',
                                                              'volt.'],
                                              'english': 'The program by means of which they insulated was very '
                                                         'successful.'},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'teaches': ['b2-relative-postpositions'],
                                              'template': [   {   'prompt': 'Write a sentence describing the '
                                                                            'architecture of Wekerletelep using a '
                                                                            "possessive relative clause (use 'amelynek "
                                                                            "mentén' or 'amelynek területén').",
                                                                  'answer': 'Wekerletelep olyan egyedülálló '
                                                                            'mintatelep, amelynek területén Kós Károly '
                                                                            'erdélyi népi szecessziós épületei és '
                                                                            'zöldellő kertes házak állnak.'},
                                                              {   'prompt': 'Write a sentence comparing panel '
                                                                            'apartments with pre-war tenements using a '
                                                                            'comparative relative construction (use '
                                                                            "'amelyhez képest').",
                                                                  'answer': 'A panellakás összkomfortot és távfűtést '
                                                                            'nyújtott, amelyhez képest a régi komfort '
                                                                            'nélküli bérházi lakások sötétnek és '
                                                                            'hidegnek bizonyultak.'}]}]}}



UNIT_24_KORNYEZETPOLITIKA = {   'unit_num': 24,
    'slug': 'kornyezetpolitika',
    'title': 'The Blue Danube: Ecology, Dams & Civic Awakening',
    'grammar_skill': 'b2-causal-purposive-chains',
    'vocab_skill': 'b2-kornyezetpolitika-vocab',
    'theme': 'Danube ecology, Duna Kör protests and environmental politics',
    'location': 'Nagymaros, Dunaszaurusz, Balaton, Tisza és Szigetköz',
    'intro_body': [   'In the late twentieth century, Hungarian environmental movements played an extraordinary role '
                      'not only in safeguarding rivers and ecosystems, but in dismantling the communist one-party '
                      'dictatorship itself. What began in the 1980s as a scientific and cultural critique against the '
                      'monumental socialist dam project at Bős–Nagymaros transformed into the Duna Kör (Danube '
                      'Circle), uniting tens of thousands of citizens in the largest grassroots protests since 1956.',
                      'Across these five lessons, you will examine the great 19th-century river engineering of the '
                      'Danube and Tisza, dive into the high-stakes political and ecological struggle over the '
                      'Nagymaros dam, experience the civic mass demonstrations of 1988 that heralded the democratic '
                      'transition, study the ecological recovery of Lake Balaton and the response to the tragic 2000 '
                      'Tisza cyanide spill, and explore contemporary strategies for drought resilience on the Great '
                      'Plain. Grammatically, you will master formal causal and purposive postpositional chains '
                      '(következtében, folytán, hatására, megóvása érdekében, elkerülése végett).'],
    'combined_story_title': 'A Duna Kör és a folyó szabadsága',
    'combined_story_summary': "How environmental activism became the catalyst for Hungary's democratic transition: "
                              'Duna Kör demonstrations against the Bős–Nagymaros dam, Balaton preservation, the 2000 '
                              'Tisza cyanide spill, and Great Plain drought adaptation.',
    'lessons': [   {   'num': 1,
                       'title': 'Regulating the Rivers: 19th-Century Flood Control',
                       'grammar_label': "Formal causal postpositions: következtében, folytán, and nyomán ('as a result "
                                        "/ consequence of')",
                       'goals': [   'I can recount the history and monumental scale of 19th-century Hungarian river '
                                    'regulation (Széchenyi, Vásárhelyi).',
                                    'I can use következtében, folytán, and nyomán to articulate clear causal '
                                    'relationships in formal prose.',
                                    'I can discuss river regulation, floodplains, and wetland ecology using B2 '
                                    'Hungarian terms.'],
                       'story_segment': {   'seg_slug': 'folyoszabalyozas',
                                            'title': 'A folyók megzabolázása: A 19. századi árvízvédelem',
                                            'summary': 'In the 19th century, Count István Széchenyi and engineer Pál '
                                                       'Vásárhelyi directed the regulation of the Danube and Tisza, '
                                                       "creating Europe's largest flood-defense dike system and "
                                                       'opening millions of acres to farming while fundamentally '
                                                       'transforming floodplain ecologies.',
                                            'location': 'A Tisza és a Duna mentén (1846–1880-as évek)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A reformkor előtti Magyarországon a Duna és '
                                                                          'a Tisza kiterjedt mocsárvilággal és '
                                                                          'kiszámíthatatlan áradásokkal uralta a '
                                                                          'tájat. Az évről évre ismétlődő árvizek '
                                                                          'következtében hatalmas területek váltak '
                                                                          'megközelíthetetlenné, és a mezőgazdasági '
                                                                          'termelés bizonytalansága gátolta az ország '
                                                                          'gazdasági felemelkedését.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Gróf Széchenyi István kezdeményezésére és '
                                                                          'Vásárhelyi Pál mérnöki zsenialitása révén '
                                                                          '1846-ban kezdetét vette a világ akkori '
                                                                          'legnagyobb folyószabályozási vállalkozása. '
                                                                          'A Tisza kanyarulatainak átvágása és a '
                                                                          'gigantikus védgátak megépítése nyomán a '
                                                                          'folyó hossza több mint négyszáz '
                                                                          'kilométerrel rövidült le.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A folyószabályozás következtében több '
                                                                          'millió hektárnyi termékeny szántóföld '
                                                                          'szabadult fel a víz alól, megteremtve a '
                                                                          'modern magyar gabonatermesztés és '
                                                                          'vasúthálózat alapjait. A folyók gyorsabb '
                                                                          'lefolyása folytán a városok és mezővárosok '
                                                                          'biztonságosabbá váltak, bár az 1879-es '
                                                                          'szegedi nagy árvíz katasztrófája még '
                                                                          'figyelmeztetett a természet erejére.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A gazdasági sikerek mögött azonban mély '
                                                                          'ökológiai árnyoldalak húzódtak meg. Az '
                                                                          'ártéri vadvilág, a hagyományos '
                                                                          'fokgazdálkodás és a halászat a mocsarak '
                                                                          'lecsapolása nyomán szinte teljesen '
                                                                          'felszámolódott, és a talajvízszint '
                                                                          'süllyedése évtizedek múltával az Alföld '
                                                                          'kiszáradásához vezetett.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A folyók 19. századi mérnöki megzabolázása '
                                                                          'történelmi bravúr volt, amely megmentette a '
                                                                          'nemzetet az éhínségektől, ám a '
                                                                          'huszonegyedik század vízügyi szakemberei ma '
                                                                          'már az egykori árterek részleges '
                                                                          'revitalizációján dolgoznak.'}]},
                       'words': [   {   'lemma': 'folyószabályozás',
                                        'translation': 'river regulation / hydraulic engineering',
                                        'pos': 'noun'},
                                    {   'lemma': 'árvízvédelem',
                                        'translation': 'flood protection / defense',
                                        'pos': 'noun'},
                                    {'lemma': 'ártér', 'translation': 'floodplain', 'pos': 'noun'},
                                    {'lemma': 'kanyarulat', 'translation': 'river bend / meander', 'pos': 'noun'},
                                    {'lemma': 'töltés', 'translation': 'levee / earthen dike', 'pos': 'noun'},
                                    {   'lemma': 'talajvízszint',
                                        'translation': 'groundwater level / water table',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'kovetkezteben-folytan-causal',
                                          'title': 'Formal Causal Postpositions: következtében, folytán, and nyomán '
                                                   "('as a result of')",
                                          'text1_title': 'Nuances of High-Register Causal Connectors',
                                          'text1': 'In academic and environmental discourse, everyday miatt is '
                                                   'replaced by precise causal postpositions: következtében indicates '
                                                   'an objective, often physical consequence of an event or '
                                                   "intervention ('a gátak építése következtében' = as a consequence "
                                                   'of dam construction); folytán denotes an intrinsic outcome '
                                                   "stemming from continuous characteristics ('gyors lefolyása "
                                                   "folytán' = by virtue of its rapid flow); nyomán marks an outcome "
                                                   "directly triggered by an initiative or preceding development ('a "
                                                   "reformok nyomán' = in the wake of reforms).",
                                          'text2_title': 'Case and Syntactic Agreement',
                                          'text2': 'Both következtében and nyomán govern nouns with possessive '
                                                   "suffixes: 'A szabályozás következtében a vízszint megváltozott.' "
                                                   'folytán typically follows unmarked nouns or nouns ending in -a/-e: '
                                                   "'gondatlanság folytán' (through negligence), 'intézkedések "
                                                   "folytán' (as a result of measures).",
                                          'table_title': 'Causal Postpositions in Environmental History',
                                          'table_rows': [   [   'A folyószabályozás következtében lecsapolták a '
                                                                'mocsarakat.',
                                                                'As a result of river regulation, they drained the '
                                                                'marshes.'],
                                                            [   'A gyors lefolyás folytán a folyó medre kimélyült.',
                                                                'By virtue of rapid run-off, the riverbed deepened.'],
                                                            [   'A kutatások nyomán feltárták az ökológiai károkat.',
                                                                'In the wake of research, they uncovered the '
                                                                'ecological damages.']],
                                          'examples': [   {   'spanish': 'A kanyarulatok átvágása következtében a '
                                                                         'folyó sodrása felgyorsult.',
                                                              'english': 'As a result of cutting through meanders, the '
                                                                         "river's current accelerated."},
                                                          {   'spanish': 'Az áradások elmaradása folytán az ártéri '
                                                                         'erdők kiszáradtak.',
                                                              'english': 'Owing to the absence of inundations, the '
                                                                         'floodplain forests dried out.'},
                                                          {   'spanish': 'Széchenyi fellépése nyomán országszerte '
                                                                         'megindultak a gátépítések.',
                                                              'english': "In the wake of Széchenyi's initiative, dike "
                                                                         'constructions started nationwide.'}],
                                          'tip': "Reserve 'következtében' for tangible consequences and 'nyomán' when "
                                                 'tracing historical lineages or follow-up outcomes.'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'pairs': [   ['folyószabályozás', 'river regulation hydraulic engineering'],
                                                         ['árvízvédelem', 'flood protection defense'],
                                                         ['ártér', 'river floodplain'],
                                                         ['kanyarulat', 'river bend / meander'],
                                                         ['töltés', 'earthen levee dike'],
                                                         ['talajvízszint', 'groundwater water table level']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'question': 'Ki volt az a kiemelkedő magyar mérnök, aki a Tisza '
                                                        'szabályozásának grandiózus terveit kidolgozta a 19. '
                                                        'században?',
                                            'options': [   'Vásárhelyi Pál.',
                                                           'Kempelen Farkas.',
                                                           'Semmelweis Ignác.',
                                                           'Jedlik Ányos.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'sentence': 'A folyómedrek kiegyenesítése miatt a környező területeken '
                                                        'drasztikusan lecsökkent a talaj nedvességét biztosító _____.',
                                            'answer': 'talajvízszint',
                                            'english': 'Due to the straightening of riverbeds, the groundwater level '
                                                       'ensuring soil moisture drastically fell in surrounding areas.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'question': 'Melyik névutó fejezi ki a legválasztékosabban a közvetlen '
                                                        "fizikai következményt? 'A gátak megépítése _____ a folyó "
                                                        "menti városok megmenekültek az áradásoktól.'",
                                            'options': ['következtében', 'végett', 'helyett', 'ellenére'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'sentence': 'A Tisza szabályozása _____ több millió hektárnyi szántóföld '
                                                        'vált művelhetővé.',
                                            'answer': 'nyomán',
                                            'english': 'In the wake of the regulation of the Tisza, millions of '
                                                       'hectares of arable land became cultivable.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'tiles': [   'A',
                                                         'mocsarak',
                                                         'lecsapolása',
                                                         'következtében',
                                                         'megváltozott',
                                                         'a',
                                                         'táj',
                                                         'ökológiája.'],
                                            'solution': [   'A',
                                                            'mocsarak',
                                                            'lecsapolása',
                                                            'következtében',
                                                            'megváltozott',
                                                            'a',
                                                            'táj',
                                                            'ökológiája.'],
                                            'english': 'As a consequence of the drainage of marshes, the ecology of '
                                                       'the landscape changed.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'prompt': [   {   'speaker': 'Történész',
                                                              'text': 'Milyen kettős mérleget vontak a kutatók a 19. '
                                                                      'századi folyószabályozásról?'},
                                                          {'speaker': 'Hidrológus', 'text': '_____'}],
                                            'options': [   'A védművek kiépítése következtében megszűntek a pusztító '
                                                           'árvizek, ám a mocsarak eltűnése folytán az Alföld '
                                                           'fokozatosan szárazabbá vált.',
                                                           'A folyószabályozás semmilyen hatással nem volt sem a '
                                                           'mezőgazdaságra, sem az árvizekre.',
                                                           'A szabályozás miatt Magyarország összes városa víz alá '
                                                           'került.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan rövidült le a Tisza folyó teljes hossza Vásárhelyi Pál '
                                                        'mérnöki tervei szerint?',
                                            'options': [   'A kanyarulatok átvágása révén több mint négyszáz '
                                                           'kilométerrel rövidült meg a folyó folyása.',
                                                           'Egy hatalmas hegy felrobbantásával elzárták a forrását.',
                                                           'A Tiszát teljes egészében a Duna medrébe vezették.'],
                                            'correct': 0}]},
                   {   'num': 2,
                       'title': 'The Bős–Nagymaros Dam Controversy',
                       'grammar_label': "Catalytic causal constructions with hatására ('under the impact of') and "
                                        'révén',
                       'goals': [   'I can explain the political and ecological background of the '
                                    'Czechoslovak–Hungarian Bős–Nagymaros hydroelectric project.',
                                    'I can use hatására and révén to describe catalytic changes, environmental '
                                    'impacts, and institutional mechanisms.',
                                    'I can discuss ecological risk, drinking water reservoirs, and socialist '
                                    'gigantomania.'],
                       'story_segment': {   'seg_slug': 'bosnagymarosvita',
                                            'title': 'A vízlépcső terve és a Duna kanyarulata',
                                            'summary': 'Signed in 1977, the Czechoslovak–Hungarian treaty to dam the '
                                                       'Danube at Gabčíkovo (Bős) and Nagymaros ignited fierce '
                                                       'scientific opposition over drinking water contamination and '
                                                       'the desiccation of the Szigetköz delta.',
                                            'location': 'Nagymaros, Visegrád és Szigetköz (1977–1985)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': '1977-ben a Magyar Népköztársaság és '
                                                                          'Csehszlovákia kormánya nemzetközi '
                                                                          'szerződést írt alá a Bős–nagymarosi '
                                                                          'vízlépcsőrendszer közös megépítéséről. A '
                                                                          'szocialista államvezetés a tervet a '
                                                                          'béketábor technológiai diadalaként és a '
                                                                          'megújuló energia forrásaként ünnepelte, '
                                                                          'figyelmen kívül hagyva a szakértők '
                                                                          'aggodalmait.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A terv egy gigantikus duzzasztóművet '
                                                                          'irányzott elő Nagymarosnál, a festői '
                                                                          'Dunakanyar szívében, amely felduzzasztotta '
                                                                          'volna a folyamot Visegrádnál. A '
                                                                          'hidrológusok és biológusok rámutattak, hogy '
                                                                          'a beruházás veszélybe sodorja Budapest '
                                                                          'legfőbb ivóvízbázisát, a parti szűrésű '
                                                                          'kavicságyat, amely évmilliók óta '
                                                                          'természetes módon tisztítja a vizet.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Még drámaibb helyzet fenyegetett a '
                                                                          'Szigetközben: a Duna fő medrének elterelése '
                                                                          'egy betonozott üzemvízcsatornába azzal '
                                                                          'fenyegetett, hogy az egyedülálló belső '
                                                                          'delta mellékágrendszere és az ártéri '
                                                                          'ligeterdők ökológiai katasztrófa áldozatává '
                                                                          'válnak.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A hivatalos cenzúra éveken keresztül '
                                                                          'elhallgatta a tudományos '
                                                                          'figyelmeztetéseket, ám a független '
                                                                          'értelmiségiek memorandumai és külföldi '
                                                                          'szakvélemények révén a valóság lassan '
                                                                          'beszivárgott a köztudatba. A nyilvánosságra '
                                                                          'hozott adatok hatására egyre több kutató, '
                                                                          'mérnök és író szólalt fel a megalomán '
                                                                          'tervek ellen.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A nagymarosi gátépítés elleni tiltakozás '
                                                                          'hamarosan túlnőtt a szigorúan vett '
                                                                          'környezetvédelmen: a Dunakanyar védelme az '
                                                                          'állampárti önkényuralom elleni általános '
                                                                          'társadalmi ellenállás szimbólumává '
                                                                          'emelkedett.'}]},
                       'words': [   {   'lemma': 'vízlépcső',
                                        'translation': 'hydroelectric barrage / dam system',
                                        'pos': 'noun'},
                                    {   'lemma': 'megalománia',
                                        'translation': 'megalomania / gigantic engineering overreach',
                                        'pos': 'noun'},
                                    {   'lemma': 'parti szűrésű ivóvíz',
                                        'translation': 'bank-filtered drinking water',
                                        'pos': 'noun'},
                                    {'lemma': 'ökoszisztéma', 'translation': 'ecosystem', 'pos': 'noun'},
                                    {'lemma': 'mederelterelés', 'translation': 'riverbed diversion', 'pos': 'noun'},
                                    {   'lemma': 'ökológiai katasztrófa',
                                        'translation': 'ecological catastrophe',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'hatasara-reven-causal',
                                          'title': "Expressing Catalysts and Means with hatására and révén ('under the "
                                                   "impact of / through')",
                                          'text1_title': 'Catalytic Transformation with hatására',
                                          'text1': "hatására (literally 'on its effect') expresses the catalytic "
                                                   'impact of an event, argument, or external pressure that prompts a '
                                                   "shift in attitude or physical state: 'A tudományos cikkek hatására "
                                                   "a közvélemény felébredt' (Under the impact of scientific articles, "
                                                   'public opinion awakened). It requires a noun with a possessive '
                                                   'suffix.',
                                          'text2_title': 'Instrumental Agency with révén',
                                          'text2': 'révén signifies the channel, instrument, or intermediary through '
                                                   "which a result is accomplished: 'A szamizdat sajtó révén jutottak "
                                                   "el a hírek a társadalomhoz' (By means of the samizdat press, news "
                                                   'reached society). It gives an authoritative, elegant tone.',
                                          'table_title': 'Causal Dynamics: hatására and révén',
                                          'table_rows': [   [   'A tiltakozások hatására a kormány kénytelen volt '
                                                                'tárgyalni.',
                                                                'Under the impact of protests, the government was '
                                                                'forced to negotiate.'],
                                                            [   'A szamizdat kiadványok révén terjedtek a független '
                                                                'tanulmányok.',
                                                                'By means of samizdat publications, independent '
                                                                'studies spread.'],
                                                            [   'A nyilvánosság hatására megváltozott a társadalom '
                                                                'gondolkodása.',
                                                                "Under the influence of public exposure, society's "
                                                                'thinking changed.']],
                                          'examples': [   {   'spanish': 'A szakmai érvek hatására sok képviselő '
                                                                         'megkérdőjelezte a vízlépcső hasznát.',
                                                              'english': 'Under the influence of professional '
                                                                         'arguments, many delegates questioned the '
                                                                         "dam's utility."},
                                                          {   'spanish': 'A nemzetközi összefogás révén a mozgalom '
                                                                         'pénzügyi támogatást kapott.',
                                                              'english': 'By means of international solidarity, the '
                                                                         'movement received financial support.'},
                                                          {   'spanish': 'Az ökológiai kutatások hatására kiderült az '
                                                                         'ivóvízbázis sebezhetősége.',
                                                              'english': 'Under the impact of ecological research, the '
                                                                         'vulnerability of the drinking water base was '
                                                                         'revealed.'}],
                                          'tip': "Distinguish agency from impact: use 'révén' for the "
                                                 "instrument/channel and 'hatására' for the persuasive or physical "
                                                 'catalyst.'},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'pairs': [   ['vízlépcső', 'hydroelectric barrage dam system'],
                                                         ['megalománia', 'gigantic engineering megalomania'],
                                                         ['parti szűrésű ivóvíz', 'bank-filtered drinking water'],
                                                         ['ökoszisztéma', 'natural ecosystem'],
                                                         ['mederelterelés', 'riverbed diversion'],
                                                         ['ökológiai katasztrófa', 'ecological catastrophe']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'question': 'Miért jelentett rendkívüli ökológiai veszélyt a nagymarosi '
                                                        'gát felépítése Budapest számára?',
                                            'options': [   'Mert veszélyeztette a főváros ivóvízellátását biztosító '
                                                           'parti szűrésű kavicságy tisztaságát.',
                                                           'Mert teljesen kiszárította volna a Balatont és a '
                                                           'Velencei-tavat.',
                                                           'Mert megszüntette volna a vasúti közlekedést Bécs és '
                                                           'Budapest között.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'sentence': 'A Duna vizének betoncsatornába kényszerítése, vagyis a '
                                                        'drasztikus _____, a Szigetköz pusztulásával fenyegetett.',
                                            'answer': 'mederelterelés',
                                            'english': "Forcing the Danube's water into a concrete canal, that is, "
                                                       'drastic riverbed diversion, threatened the destruction of the '
                                                       'Szigetköz.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'question': 'Melyik kifejezés fejezi ki a külső hatás következtében '
                                                        "végbemenő változást? 'A nyilvánosságra hozott adatok _____ az "
                                                        "emberek ráébredtek a beruházás veszélyeire.'",
                                            'options': ['hatására', 'végett', 'helyett', 'gyanánt'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'sentence': 'A szamizdat folyóiratok és röplapok _____ a cenzúrázott '
                                                        'információk eljutottak a nagyközönséghez.',
                                            'answer': 'révén',
                                            'english': 'By means of samizdat journals and leaflets, censored '
                                                       'information reached the general public.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'tiles': [   'A',
                                                         'tudományos',
                                                         'érvek',
                                                         'hatására',
                                                         'a',
                                                         'közvélemény',
                                                         'megváltozott.'],
                                            'solution': [   'A',
                                                            'tudományos',
                                                            'érvek',
                                                            'hatására',
                                                            'a',
                                                            'közvélemény',
                                                            'megváltozott.'],
                                            'english': 'Under the impact of scientific arguments, public opinion '
                                                       'changed.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'prompt': [   {   'speaker': 'Egyetemi hallgató',
                                                              'text': 'Hogyan tudtak fellépni a kutatók a hivatalos '
                                                                      'állásponttal szemben a nyolcvanas évek elején?'},
                                                          {'speaker': 'Ökológus', 'text': '_____'}],
                                            'options': [   'Független szakvélemények révén bizonyították a környezeti '
                                                           'kockázatokat, és ezen tények hatására egyre szélesebb '
                                                           'társadalmi támogatást szereztek.',
                                                           'A kutatók mind támogatták a nagymarosi gát felépítését az '
                                                           'első pillanattól kezdve.',
                                                           'Kizárólag külföldi tv-műsorokban szerepeltek álnéven.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Hogyan tekintett a korabeli kommunista propaganda a '
                                                        'Bős–nagymarosi beruházásra?',
                                            'options': [   'A szocialista mérnöki tudás és a megújuló energia '
                                                           'diadalaként ünnepelte.',
                                                           'Súlyos kudarcként és pénzkidobásként jellemezte.',
                                                           'Kifejezetten kapitalista spekulációnak minősítette.'],
                                            'correct': 0}]},
                   {   'num': 3,
                       'title': 'How the Duna Kör Mobilized Tens of Thousands in 1988',
                       'grammar_label': "Purposive postpositions: érdekében ('in the interest of / for the purpose "
                                        "of')",
                       'goals': [   'I can narrate the formation of the Duna Kör (1984) and the historic 1988 mass '
                                    'demonstrations in Budapest.',
                                    'I can form formal purposive clauses using érdekében with possessive verbal nouns '
                                    'and nominal phrases.',
                                    'I can debate how environmental activism functioned as a catalyst for political '
                                    'democratization.'],
                       'story_segment': {   'seg_slug': 'dunakor1988',
                                            'title': '1988: Amikor a Duna védelme megrengette a rezsimet',
                                            'summary': 'Founded in 1984 by biologist János Vargha, the underground '
                                                       'Duna Kör mobilized 40,000 demonstrators in September 1988, '
                                                       'forcing the Hungarian government to halt the Nagymaros dam and '
                                                       'accelerating the collapse of the one-party regime.',
                                            'location': 'Budapest, Vörösmarty tér és a Parlament (1984–1989)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': '1984-ben Vargha János biológus-újságíró '
                                                                          'vezetésével megalakult a Duna Kör, egy nem '
                                                                          'hivatalos, független környezetvédő civil '
                                                                          'szervezet. Mivel az egypártrendszerben a '
                                                                          'közvetlen politikai pártalapítást a '
                                                                          'hatóságok szigorúan büntették, a '
                                                                          'természetvédelem és a Duna megmentése olyan '
                                                                          'legális esernyővé vált, amely alatt a '
                                                                          'demokratikus ellenzék és a társadalom '
                                                                          'egésze felsorakozhatott.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A Duna Kör bátor kiállását 1985-ben a svéd '
                                                                          'parlamentben az Alternatív Nobel-díjjal '
                                                                          '(Right Livelihood Award) ismerték el. A '
                                                                          'mozgalom tagjai a lakosság tájékoztatása '
                                                                          'érdekében illegális röplapokat '
                                                                          'terjesztettek, szamizdat kiadványokat '
                                                                          'szerkesztettek, és országos aláírásgyűjtést '
                                                                          'indítottak a nagymarosi építkezés '
                                                                          'leállítása érdekében.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A társadalmi öntudat ébredése 1988. '
                                                                          'szeptember 12-én érte el tetőpontját. Ezen '
                                                                          'a történelmi napon mintegy negyvenezer '
                                                                          'ember vonult a Vörösmarty térről a '
                                                                          'Parlament elé békésen, „Nem kell '
                                                                          'vízlépcső!” és „Tiszta Dunát!” jelszavakat '
                                                                          'skandálva. Ez volt a legnagyobb '
                                                                          'tömegtüntetés Magyarországon az 1956-os '
                                                                          'forradalom óta.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A hatalom megrendült a demonstráció '
                                                                          'látványától: a rendőrség nem mert '
                                                                          'közbeavatkozni, és a tüntetés nyilvánvalóvá '
                                                                          'tette, hogy a rezsim elveszítette a '
                                                                          'társadalom feletti morális uralmát. A '
                                                                          'Duna-mozgalom a magyar polgári '
                                                                          'engedetlenség és a formálódó többpárti '
                                                                          'demokrácia bölcsőjévé vált.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A folyamatos nyomás hatására 1989 májusában '
                                                                          'Németh Miklós miniszterelnök kormánya '
                                                                          'elrendelte a nagymarosi építkezés '
                                                                          'felfüggesztését, majd végleges leállítását. '
                                                                          'A folyó szabadsága így vált a nemzet '
                                                                          'szabadságának legfőbb előhírnökévé a '
                                                                          'rendszerváltás hajnalán.'}]},
                       'words': [   {   'lemma': 'polgári engedetlenség',
                                        'translation': 'civil disobedience',
                                        'pos': 'noun'},
                                    {   'lemma': 'tömegtüntetés',
                                        'translation': 'mass demonstration / protest rally',
                                        'pos': 'noun'},
                                    {   'lemma': 'aláírásgyűjtés',
                                        'translation': 'signature campaign / petition collection',
                                        'pos': 'noun'},
                                    {   'lemma': 'társadalmi öntudat',
                                        'translation': 'civic awareness / public consciousness',
                                        'pos': 'noun'},
                                    {   'lemma': 'rendszerváltó',
                                        'translation': 'regime-changing / transitional',
                                        'pos': 'adjective'},
                                    {   'lemma': 'természetvédelem',
                                        'translation': 'nature conservation / environmental protection',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'erdekeben-purposive',
                                          'title': "Purposive Framing with érdekében ('in the interest of / for the "
                                                   "purpose of')",
                                          'text1_title': 'Elevated Purposive Phrasing with érdekében',
                                          'text1': 'In formal, political, and academic Hungarian, érdekében attaches '
                                                   'to a possessed noun or verbal noun (ending in -ása/-ése) to '
                                                   "formulate clear programmatic objectives: 'a Duna megóvása "
                                                   "érdekében' (for the purpose of protecting the Danube), 'a lakosság "
                                                   "tájékoztatása érdekében' (in the interest of informing the "
                                                   'public).',
                                          'text2_title': 'Contrast with azért, hogy Clauses',
                                          'text2': 'While colloquial Hungarian relies on finite subordinate clauses '
                                                   "with azért, hogy ('Azért tüntettek, hogy megállítsák...'), "
                                                   "professional prose heavily favors noun + érdekében ('A beruházás "
                                                   "megállítása érdekében tüntettek'). This condenses sentences and "
                                                   'creates an authoritative civic tone.',
                                          'table_title': 'Purposive Structures with érdekében',
                                          'table_rows': [   [   'A Duna megóvása érdekében békés tüntetést szerveztek.',
                                                                'In the interest of preserving the Danube, they '
                                                                'organized a peaceful protest.'],
                                                            [   'A környezeti károk elkerülése érdekében leállították '
                                                                'a munkát.',
                                                                'In order to avoid environmental damage, they stopped '
                                                                'the work.'],
                                                            [   'A jogállamiság kivívása érdekében civil szervezetek '
                                                                'alakultak.',
                                                                'For the sake of winning the rule of law, civic '
                                                                'organizations formed.']],
                                          'examples': [   {   'spanish': 'A folyó élővilágának védelme érdekében '
                                                                         'százezrek írták alá a petíciót.',
                                                              'english': "In the interest of protecting the river's "
                                                                         'wildlife, hundreds of thousands signed the '
                                                                         'petition.'},
                                                          {   'spanish': 'A tiszta tájékoztatás érdekében szamizdat '
                                                                         'lapokat adtak ki.',
                                                              'english': 'For the sake of uncorrupted information, '
                                                                         'they published samizdat papers.'},
                                                          {   'spanish': 'A közös jövő megóvása érdekében a társadalom '
                                                                         'egységesen lépett fel.',
                                                              'english': 'In order to protect our shared future, '
                                                                         'society acted in unity.'}],
                                          'tip': 'Ensure the preceding noun carries the 3rd person possessive suffix: '
                                                 "'megóvás-a érdekében', 'tájékoztatás-a érdekében'."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'pairs': [   ['polgári engedetlenség', 'civil disobedience'],
                                                         ['tömegtüntetés', 'mass protest rally'],
                                                         ['aláírásgyűjtés', 'petition signature campaign'],
                                                         ['társadalmi öntudat', 'civic public consciousness'],
                                                         ['rendszerváltó', 'regime-changing transitional'],
                                                         ['természetvédelem', 'nature conservation']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'question': 'Hány ember vonult az utcára Budapesten 1988. szeptember 12-én '
                                                        'a nagymarosi gát ellen tüntetve?',
                                            'options': [   'Körülbelül negyvenezer ember a Vörösmarty tértől a '
                                                           'Parlamentig.',
                                                           'Mindössze néhány tucat egyetemi hallgató egy kollégiumban.',
                                                           'Több mint kétmillió fegyveres katona.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'sentence': 'A békés Duna-mozgalom a modern magyar _____ és a demokratikus '
                                                        'átmenet egyik legfontosabb előfutára volt.',
                                            'answer': 'polgári engedetlenség',
                                            'english': 'The peaceful Danube movement was one of the most important '
                                                       'precursors of modern Hungarian civil disobedience and the '
                                                       'democratic transition.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'question': "Melyik szerkezet fejezi ki helyesen a célt? 'A Dunakanyar "
                                                        'természeti szépségének _____ a tüntetők leállították a '
                                                        "teherautókat.'",
                                            'options': ['megóvása érdekében', 'következtében', 'nélkül', 'gyanánt'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'sentence': 'A lakosság pontos tájékoztatása _____ a Duna Kör független '
                                                        'füzeteket nyomtatott.',
                                            'answer': 'érdekében',
                                            'english': 'In the interest of accurate public information, the Danube '
                                                       'Circle printed independent pamphlets.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'tiles': [   'A',
                                                         'folyó',
                                                         'megmentése',
                                                         'érdekében',
                                                         'negyvenezer',
                                                         'ember',
                                                         'tüntetett.'],
                                            'solution': [   'A',
                                                            'folyó',
                                                            'megmentése',
                                                            'érdekében',
                                                            'negyvenezer',
                                                            'ember',
                                                            'tüntetett.'],
                                            'english': 'In the interest of saving the river, forty thousand people '
                                                       'protested.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'prompt': [   {   'speaker': 'Történész',
                                                              'text': 'Miért vált a vízlépcső elleni küzdelem a '
                                                                      'rendszerváltás katalizátorává?'},
                                                          {'speaker': 'Politológus', 'text': '_____'}],
                                            'options': [   'Mert a Duna védelme érdekében százezrek mertek nyíltan '
                                                           'fellépni, és a tüntetések révén a társadalom '
                                                           'megtapasztalta a békés szolidaritás erejét.',
                                                           'Mert a gát építése azonnal megoldotta a gazdasági '
                                                           'válságot.',
                                                           'Mert a kormány minden környezetvédőt miniszterré nevezett '
                                                           'ki.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen nemzetközi elismerésben részesült a Duna Kör 1985-ben '
                                                        'a bátor természetvédelmi tevékenységéért?',
                                            'options': [   'Megkapta az Alternatív Nobel-díjat (Right Livelihood '
                                                           'Award) Svédországban.',
                                                           'Olimpiai aranyérmet nyert evezésben.',
                                                           'Megkapta az Oscar-díjat a legjobb dokumentumfilmért.'],
                                            'correct': 0}]},
                   {   'num': 4,
                       'title': 'Saving Lake Balaton and the Tisza River',
                       'grammar_label': 'Preventive and formal purposive constructions: végett, elkerülése végett, and '
                                        'megelőzésére',
                       'goals': [   'I can explain the ecological rescue of Lake Balaton (Kis-Balaton) and the '
                                    'recovery from the 2000 Tisza cyanide spill.',
                                    'I can properly use végett and elkerülése végett to express formal purpose and '
                                    'preventive measures in B2 prose.',
                                    'I can discuss ecological rehabilitation, industrial pollution, and international '
                                    'environmental law.'],
                       'story_segment': {   'seg_slug': 'balatontiszavedelme',
                                            'title': 'Két sérülékeny kincs: A Balaton és a Tisza megpróbáltatásai',
                                            'summary': 'From the successful biological filtration revival of Lake '
                                                       'Balaton via the Kis-Balaton wetlands to the devastating 2000 '
                                                       "Tisza cyanide spill and its miraculous recovery, Hungary's "
                                                       'waters have tested national resilience.',
                                            'location': 'Balaton, Kis-Balaton és a Tiszazug (1980–2005)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A magyar vízvédelem történetének két '
                                                                          'legfontosabb fejezete a Balaton vizének '
                                                                          'megmentése és a Tiszát ért 2000-es '
                                                                          'bányakatasztrófa elhárítása volt. Az '
                                                                          '1970-es és 1980-as években a Balaton az '
                                                                          'intenzív mezőgazdasági műtrágyázás és a '
                                                                          'szennyvizek miatt súlyos eutrofizációval '
                                                                          'küzdött: a víz elalgásodott, és a tó '
                                                                          'biológiai egyensúlya összeomlással '
                                                                          'fenyegetett.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A katasztrófa elkerülése végett a '
                                                                          'szakemberek megvalósították a Kis-Balaton '
                                                                          'védőrendszer rekonstrukcióját. A Zala folyó '
                                                                          'torkolatánál elterülő mocsárvilág és a '
                                                                          'hatalmas kiterjedésű nádas természetes '
                                                                          'biológiai szűrőként felfogta a foszfort és '
                                                                          'a hordalékot, minek köszönhetően a tó vize '
                                                                          'csodálatos módon kitisztult.'},
                                                              {   'type': 'narration',
                                                                  'text': 'Alig lélegzett fel az ország, amikor 2000. '
                                                                          'január 30-án a romániai Nagybányán '
                                                                          'átszakadt egy aranybánya gátja. Több mint '
                                                                          'százezer köbméternyi ciánnal és '
                                                                          'nehézfémekkel mérgezett zagy ömlött a '
                                                                          'Szamosba, majd onnan a Tiszába, a '
                                                                          'közép-európai folyók legsúlyosabb '
                                                                          'környezeti tragédiáját okozva.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A ciánfolt fekete szalagként vonult végig a '
                                                                          'folyón: több mint ezer tonna hal pusztult '
                                                                          'el, és a mérgezés megelőzése végett a '
                                                                          'hatóságok azonnal elzárták az ivóvízkutakat '
                                                                          'és a holtágak zsilipjeit. A katasztrófa '
                                                                          'orvoslása végett nemzetközi '
                                                                          'vizsgálóbizottság alakult, amely '
                                                                          'megállapította az aranybánya felelősségét.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A tragédia után azonban csoda történt: a '
                                                                          'Tisza és ártereinek természetes '
                                                                          'regenerálódása a vízügyi szakemberek '
                                                                          'összehangolt munkájának köszönhetően '
                                                                          'meglepően gyorsan megindult. Néhány év '
                                                                          'múltával a tiszavirágzás és a halállomány '
                                                                          'visszatért, megerősítve a közép-európai '
                                                                          'környezetvédelmi összefogás '
                                                                          'szükségességét.'}]},
                       'words': [   {   'lemma': 'eutrofizáció',
                                        'translation': 'eutrophication / excessive algal nutrient enrichment',
                                        'pos': 'noun'},
                                    {   'lemma': 'víztisztítás',
                                        'translation': 'water purification / wastewater treatment',
                                        'pos': 'noun'},
                                    {   'lemma': 'ciánszennyezés',
                                        'translation': 'cyanide contamination / toxic spill',
                                        'pos': 'noun'},
                                    {   'lemma': 'nádas',
                                        'translation': 'reed bed / biological marsh filter',
                                        'pos': 'noun'},
                                    {   'lemma': 'regenerálódás',
                                        'translation': 'ecological regeneration / natural recovery',
                                        'pos': 'noun'},
                                    {   'lemma': 'felelősségre vonás',
                                        'translation': 'holding legally accountable / liability litigation',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'vegett-preventive',
                                          'title': "Formal Purposive and Preventive Phrasing with végett ('for the "
                                                   "purpose of / in order to')",
                                          'text1_title': 'Intentional and Preventive Scope of végett',
                                          'text1': 'végett is a traditional high-register postposition expressing '
                                                   "intended aim or deliberate precaution: 'a katasztrófa elkerülése "
                                                   "végett' (in order to avoid catastrophe), 'a vízminőség ellenőrzése "
                                                   "végett' (for the purpose of inspecting water quality). It combines "
                                                   'with verbal nouns or nominal phrases.',
                                          'text2_title': 'Crucial Distinction: végett vs. miatt',
                                          'text2': 'Never confuse végett with miatt! miatt denotes an existing or past '
                                                   "cause ('A szennyezés miatt pusztultak el a halak' = The fish died "
                                                   'because of the pollution). végett strictly denotes future purpose '
                                                   "or intended prevention ('A szennyezés elkerülése végett elzárták a "
                                                   "gátakat' = They closed the dams in order to avoid pollution).",
                                          'table_title': 'Preventive and Purposive Formulations',
                                          'table_rows': [   [   'A mérgezés elkerülése végett elzárták a kutakat.',
                                                                'In order to avoid poisoning, they shut off the '
                                                                'wells.'],
                                                            [   'A tó megmentése végett kiépítették a nádast.',
                                                                'For the purpose of saving the lake, they developed '
                                                                'the reed bed.'],
                                                            [   'A felelősség tisztázása végett vizsgálatot '
                                                                'indítottak.',
                                                                'In order to clarify responsibility, they launched an '
                                                                'investigation.']],
                                          'examples': [   {   'spanish': 'A szennyezés megelőzése végett a szakemberek '
                                                                         'folyamatosan mérték a vízminőséget.',
                                                              'english': 'In order to prevent pollution, experts '
                                                                         'continuously measured water quality.'},
                                                          {   'spanish': 'Az ártér megóvása végett szigorították a '
                                                                         'környezetvédelmi előírásokat.',
                                                              'english': 'For the purpose of protecting the '
                                                                         'floodplain, they tightened environmental '
                                                                         'regulations.'},
                                                          {   'spanish': 'A halállomány védelme végett ideiglenesen '
                                                                         'betiltották a halászatot.',
                                                              'english': 'In order to protect the fish population, '
                                                                         'they temporarily banned fishing.'}],
                                          'tip': "Remember: 'miatt' looks backward to a cause (because of X), while "
                                                 "'végett' looks forward to an aim (in order to achieve/prevent Y)."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'pairs': [   ['eutrofizáció', 'algal bloom nutrient enrichment'],
                                                         ['víztisztítás', 'water purification treatment'],
                                                         ['ciánszennyezés', 'cyanide contamination spill'],
                                                         ['nádas', 'marsh reed bed buffer'],
                                                         ['regenerálódás', 'ecological natural recovery'],
                                                         ['felelősségre vonás', 'legal liability accountability']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'question': 'Hogyan mentette meg a Kis-Balaton rekonstrukciója a Balaton '
                                                        'vízminőségét a 80-as években?',
                                            'options': [   'Természetes biológiai szűrőként a hatalmas nádas felfogta '
                                                           'a foszfort és a hordalékot a Zala torkolatánál.',
                                                           'Kizárólag vegyi tisztítószereket öntöttek a tóba heteken '
                                                           'keresztül.',
                                                           'Lecapolták a Balaton vizét és új vizet hoztak a Dunából.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'sentence': '2000 telén a Nagybányáról kiinduló tragikus _____ hatalmas '
                                                        'pusztítást végzett a Tisza élővilágában.',
                                            'answer': 'ciánszennyezés',
                                            'english': 'In the winter of 2000, the tragic cyanide contamination '
                                                       'originating from Baia Mare wrought immense destruction on the '
                                                       'wildlife of the Tisza.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'question': "Melyik mondat alkalmazza helyesen a 'végett' célhatározói "
                                                        "névutót a 'miatt' helyett?",
                                            'options': [   'A további mérgezések elkerülése végett a vízügy lezárta a '
                                                           'holtágak zsilipjeit.',
                                                           'A ciánszennyezés végett halt meg több ezer tonna hal.',
                                                           'Az esőzés végett megáradt a folyó a múlt héten.',
                                                           'A hideg tél végett befagyott a tó vize.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'sentence': 'A lakosság biztonságának garantálása _____ a hatóságok '
                                                        'azonnal mintát vettek az ivóvízből.',
                                            'answer': 'végett',
                                            'english': 'In order to guarantee the safety of the public, the '
                                                       'authorities immediately took samples of the drinking water.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'tiles': [   'A',
                                                         'katasztrófa',
                                                         'elkerülése',
                                                         'végett',
                                                         'azonnal',
                                                         'lezárták',
                                                         'a',
                                                         'zsilipeket.'],
                                            'solution': [   'A',
                                                            'katasztrófa',
                                                            'elkerülése',
                                                            'végett',
                                                            'azonnal',
                                                            'lezárták',
                                                            'a',
                                                            'zsilipeket.'],
                                            'english': 'In order to avoid catastrophe, they immediately shut the '
                                                       'sluices.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'prompt': [   {   'speaker': 'Újságíró',
                                                              'text': 'Hogyan élte túl a Tisza folyó a 2000-es '
                                                                      'ciánszennyezést?'},
                                                          {'speaker': 'Biológus', 'text': '_____'}],
                                            'options': [   'A hideg víz lassította a méreg felszívódását, a védelmi '
                                                           'intézkedések végett a holtágak megmenekültek, és a '
                                                           'természet regenerálódása révén visszatért az élet.',
                                                           'A Tiszát teljes egészében lebetonozták a mérgezés után.',
                                                           'A folyóból soha többé nem fogtak ki egyetlen élő halat '
                                                           'sem.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Milyen rovar tömeges rajzása jelezte néhány évvel a '
                                                        'katasztrófa után a Tisza vizének megtisztulását?',
                                            'options': [   'A tiszavirág (kérész) látványos rajzása.',
                                                           'A vándorsáskák megjelenése.',
                                                           'A kolorádóbogarak elszaporodása.'],
                                            'correct': 0}]},
                   {   'num': 5,
                       'title': 'Drought on the Alföld and 21st-Century Water Strategy',
                       'grammar_label': 'Synthesizing causal (következtében, hatására) and purposive chains '
                                        '(érdekében, végett) in environmental policy',
                       'goals': [   'I can evaluate the acute challenges of climate change, desertification, and water '
                                    "retention on Hungary's Great Plain (Alföld).",
                                    'I can integrate complex causal and purposive postpositional structures into '
                                    'professional environmental policy essays.',
                                    'I can debate modern landscape water retention (vízvisszatartás) versus historic '
                                    'drainage strategies in Hungarian.'],
                       'story_segment': {   'seg_slug': 'alfoldivizgazdalkodas',
                                            'title': 'Aszály az Alföldön: Vízmegtartás a 21. században',
                                            'summary': 'Recurrent severe droughts and falling water tables in the '
                                                       'Homokhát have forced a paradigm shift in 21st-century '
                                                       'Hungarian water strategy: shifting from draining water off the '
                                                       'land to landscape-scale water retention and wetland '
                                                       'restoration.',
                                            'location': 'A Duna–Tisza köze és a Homokhát (napjainkban)',
                                            'paragraphs': [   {   'type': 'narration',
                                                                  'text': 'A huszonegyedik században az '
                                                                          'éghajlatváltozás közvetlen '
                                                                          'következményeként Magyarországot egyre '
                                                                          'súlyosabb és elhúzódóbb aszályok sújtják. '
                                                                          'Különösen a Duna–Tisza közi Homokhát '
                                                                          'térségében vált kritikussá a helyzet, ahol '
                                                                          'a talajvízszint süllyedése következtében az '
                                                                          'elsivatagosodás valóságos fenyegetéssé vált '
                                                                          'a mezőgazdaság számára.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A klímaváltozás hatására a vízügyi '
                                                                          'szakembereknek alapvetően újra kell '
                                                                          'értékelniük a korábbi két évszázad '
                                                                          'szemléletét. Míg a 19. századi '
                                                                          'szabályozások idején a víz mielőbbi '
                                                                          'levezetése volt az elsődleges cél, a mai '
                                                                          'aszályos évtizedekben a tájléptékű '
                                                                          'vízvisszatartás vált a túlélés zálogává.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A termőföldek megóvása érdekében a '
                                                                          'gazdáknak és a mérnököknek együtt kell '
                                                                          'működniük: a tavaszi árhullámok idején a '
                                                                          'többletvizet nem szabad azonnal a tenger '
                                                                          'felé vezetni, hanem a mélyárterekbe, '
                                                                          'egykori medrekbe és vizes élőhelyekbe kell '
                                                                          'kormányozni a talajvíz pótlása végett.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A modern öntözőrendszerek kiépítése mellett '
                                                                          'a természetközeli tájgazdálkodás és a '
                                                                          'szárazságtűrő növényfajták telepítése '
                                                                          'elengedhetetlen a jövő agrártermeléséhez. '
                                                                          'Az erdősávok telepítése és a talajkímélő '
                                                                          'művelés révén a szél által okozott erózió '
                                                                          'is jelentősen mérsékelhető.'},
                                                              {   'type': 'narration',
                                                                  'text': 'A Duna és a Tisza országa a 21. században a '
                                                                          'víz megtartásának művészetét tanulja: a '
                                                                          'folyók és a táj harmonikus együttélése '
                                                                          'bizonyítja, hogy az ökológiai '
                                                                          'felelősségvállalás és a nemzeti gazdasági '
                                                                          'jólét elválaszthatatlan egymástól.'}]},
                       'words': [   {'lemma': 'aszály', 'translation': 'drought', 'pos': 'noun'},
                                    {   'lemma': 'vízvisszatartás',
                                        'translation': 'water retention / landscape hydration',
                                        'pos': 'noun'},
                                    {'lemma': 'elsivatagosodás', 'translation': 'desertification', 'pos': 'noun'},
                                    {'lemma': 'éghajlatváltozás', 'translation': 'climate change', 'pos': 'noun'},
                                    {'lemma': 'öntözőrendszer', 'translation': 'irrigation system', 'pos': 'noun'},
                                    {   'lemma': 'tájgazdálkodás',
                                        'translation': 'landscape stewardship / agroecological management',
                                        'pos': 'noun'}],
                       'grammar_doc': {   'slug': 'causal-purposive-synthesis',
                                          'title': 'Mastering Causal and Purposive Postpositional Chains in Policy '
                                                   'Analysis',
                                          'text1_title': 'Linking Cause to Policy Remedy',
                                          'text1': 'Advanced B2 essays on ecological and public policy chain causal '
                                                   'diagnostic markers (az aszály következtében, a felmelegedés '
                                                   'hatására) with deliberate purposive interventions (a talajvíz '
                                                   'pótlása érdekében, az erózió megelőzése végett).',
                                          'text2_title': 'Syntactic Symmetry and Rhythm',
                                          'text2': 'Alternating between következtében (structural cause), hatására '
                                                   '(catalytic trigger), érdekében (aspirational aim), and végett '
                                                   '(preventive precaution) creates authoritative, nuanced academic '
                                                   'prose that conforms to European environmental policy registers.',
                                          'table_title': 'Causal-Purposive Argumentative Chains',
                                          'table_rows': [   [   'Az aszály következtében kiszáradt a talaj a '
                                                                'Homokháton.',
                                                                'As a consequence of drought, the soil dried out on '
                                                                'the Homokhát.'],
                                                            [   'A termés megóvása érdekében új tározókat építenek.',
                                                                'In the interest of protecting crops, they build new '
                                                                'reservoirs.'],
                                                            [   'Az elsivatagosodás elkerülése végett erdősávokat '
                                                                'ültetnek.',
                                                                'In order to avoid desertification, they plant '
                                                                'shelterbelts.']],
                                          'examples': [   {   'spanish': 'A klímaváltozás hatására a vízvisszatartás '
                                                                         'lett a vízügy legfőbb feladata.',
                                                              'english': 'Under the impact of climate change, water '
                                                                         "retention became water management's primary "
                                                                         'task.'},
                                                          {   'spanish': 'A talajvízszint megőrzése érdekében a vizet '
                                                                         'a tájban kell tartani.',
                                                              'english': 'In order to preserve the groundwater table, '
                                                                         'water must be kept in the landscape.'},
                                                          {   'spanish': 'A károk megelőzése végett a gazdák '
                                                                         'szárazságtűrő növényeket választanak.',
                                                              'english': 'In order to prevent damages, farmers select '
                                                                         'drought-tolerant crops.'}],
                                          'tip': 'In B2 writing, construct balanced paragraphs: diagnose the problem '
                                                 "with 'következtében' or 'hatására', then propose the programmatic "
                                                 "solution with 'érdekében' or 'végett'."},
                       'exercises': [   {   'type': 'matching',
                                            'category': 'vocabulary',
                                            'stage': 'introduce',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'pairs': [   ['aszály', 'severe agricultural drought'],
                                                         ['vízvisszatartás', 'landscape water retention'],
                                                         ['elsivatagosodás', 'land desertification'],
                                                         ['éghajlatváltozás', 'global climate change'],
                                                         ['öntözőrendszer', 'agricultural irrigation system'],
                                                         ['tájgazdálkodás', 'landscape ecological stewardship']]},
                                        {   'type': 'multiple-choice',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'question': 'Milyen szemléletváltásra van szükség a 21. századi magyar '
                                                        'vízgazdálkodásban az aszályok miatt?',
                                            'options': [   'A vizek gyors levezetése helyett a tájléptékű '
                                                           'vízvisszatartásra és a talajvíz pótlására kell áttérni.',
                                                           'Minden folyót le kell betonozni és el kell tüntetni a '
                                                           'szántóföldekről.',
                                                           'Abba kell hagyni a mezőgazdasági termelést az egész '
                                                           'Alföldön.'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'vocabulary',
                                            'stage': 'controlled',
                                            'teaches': ['b2-kornyezetpolitika-vocab'],
                                            'sentence': 'A Homokhát homokos talaján a tartós szárazság miatt a '
                                                        'fenyegető _____ megállítása a legfőbb nemzeti feladat.',
                                            'answer': 'elsivatagosodás',
                                            'english': 'On the sandy soils of the Homokhát, halting threatening '
                                                       'desertification due to prolonged drought is the foremost '
                                                       'national task.'},
                                        {   'type': 'multiple-choice',
                                            'category': 'grammar',
                                            'stage': 'controlled',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'question': "Válassza ki a helyes ok- és célhatározói láncot: 'Az aszályok "
                                                        "_____ a gazdák új tározókat építenek a víz megtartása _____.'",
                                            'options': [   'következtében ... érdekében',
                                                           'végett ... nyomán',
                                                           'helyett ... révén',
                                                           'gyanánt ... nélkül'],
                                            'correct': 0},
                                        {   'type': 'fill-blank',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'sentence': 'A termőföldek kiszáradásának megelőzése _____ mélyártereket '
                                                        'alakítanak ki a Duna mentén.',
                                            'answer': 'végett',
                                            'english': 'In order to prevent the desiccation of arable lands, they '
                                                       'develop deep floodplains along the Danube.'},
                                        {   'type': 'sentence-builder',
                                            'category': 'grammar',
                                            'stage': 'practice',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'tiles': [   'A',
                                                         'klímaváltozás',
                                                         'hatására',
                                                         'a',
                                                         'vízvisszatartás',
                                                         'lett',
                                                         'a',
                                                         'fő',
                                                         'cél.'],
                                            'solution': [   'A',
                                                            'klímaváltozás',
                                                            'hatására',
                                                            'a',
                                                            'vízvisszatartás',
                                                            'lett',
                                                            'a',
                                                            'fő',
                                                            'cél.'],
                                            'english': 'Under the impact of climate change, water retention became the '
                                                       'main goal.'},
                                        {   'type': 'dialogue-complete',
                                            'category': 'dialogue',
                                            'stage': 'dialogue',
                                            'teaches': ['b2-causal-purposive-chains'],
                                            'prompt': [   {   'speaker': 'Agrármérnök',
                                                              'text': 'Hogyan alkalmazkodhat az alföldi mezőgazdaság a '
                                                                      'tartós vízhiányhoz?'},
                                                          {'speaker': 'Környezetkutató', 'text': '_____'}],
                                            'options': [   'Az aszályok következtében a víz megtartása érdekében '
                                                           'mélyárteri tározást kell alkalmazni, és a talaj védelme '
                                                           'végett erdősávokat kell telepíteni.',
                                                           'Úgy, hogy kivágjuk az összes fát a folyók mentén.',
                                                           'Úgy, hogy a Dunát teljes egészében külföldre '
                                                           'szivattyúzzuk.'],
                                            'correct': 0},
                                        {   'type': 'multiple-choice',
                                            'category': 'reading',
                                            'stage': 'reading',
                                            'question': 'Melyik tájegységben vált különösen kritikussá a talajvíz '
                                                        'süllyedése a szöveg szerint?',
                                            'options': [   'A Duna–Tisza közi Homokhát térségében.',
                                                           'A Magas-Tátra csúcsain.',
                                                           'A Balaton déli partjának sekély vizeiben.'],
                                            'correct': 0}]}],
    'consolidation': {   'goals': [   'I can recount the history of Hungarian river engineering, the 1980s Duna Kör '
                                      "movement, Lake Balaton's preservation, and the 2000 Tisza cyanide spill.",
                                      'I can master formal causal (következtében, folytán, hatására, révén) and '
                                      'purposive postpositions (érdekében, végett, elkerülése végett).',
                                      'I can critically evaluate water retention versus historical drainage paradigms '
                                      'in the context of 21st-century climate adaptation.',
                                      'I can actively deploy 30 B2 environmental policy, ecology, and hydraulic '
                                      'management terms.'],
                         'exercises': [   {   'type': 'matching',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-kornyezetpolitika-vocab'],
                                              'pairs': [   [   'folyószabályozás',
                                                               'river regulation hydraulic engineering'],
                                                           ['vízlépcső', 'hydroelectric barrage dam system'],
                                                           ['polgári engedetlenség', 'civil disobedience'],
                                                           ['ciánszennyezés', 'cyanide contamination spill'],
                                                           ['vízvisszatartás', 'landscape water retention'],
                                                           ['elsivatagosodás', 'land desertification']]},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'question': 'Which postposition expresses deliberate future precaution '
                                                          "('in order to prevent/avoid') rather than a retrospective "
                                                          "cause ('because of')?",
                                              'options': ['végett', 'miatt', 'következtében', 'folytán'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'teaches': ['b2-kornyezetpolitika-vocab'],
                                              'question': 'Milyen nemzetközi elismerést nyert el a Duna Kör 1985-ben a '
                                                          'nagymarosi gát elleni bátor és békés kiállásáért?',
                                              'options': [   'Az Alternatív Nobel-díjat (Right Livelihood Award).',
                                                             'A Pulitzer-díjat.',
                                                             'A Nemzetközi Vöröskereszt érdemrendjét.',
                                                             'Az ENSZ Környezetvédelmi Fődíját.'],
                                              'correct': 0},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'teaches': ['b2-kornyezetpolitika-vocab'],
                                              'sentence': '1988 szeptemberében negyvenezer fős békés _____ zajlott le '
                                                          'a budapesti Parlament előtt a Duna védelmében.',
                                              'answer': 'tömegtüntetés',
                                              'english': 'In September 1988, a peaceful mass protest rally of forty '
                                                         'thousand people took place in front of the Budapest '
                                                         'Parliament in defense of the Danube.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'sentence': 'A folyó medrének kiegyenesítése _____ felgyorsult a tavaszi '
                                                          'árhullámok lefolyása.',
                                              'answer': 'következtében',
                                              'english': 'As a consequence of the straightening of the riverbed, the '
                                                         'run-off of spring flood waves accelerated.'},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'sentence': 'A folyó és az élővilág megmentése _____ országszerte több '
                                                          'százezer ember írta alá a petíciót.',
                                              'answer': 'érdekében',
                                              'english': 'In the interest of saving the river and wildlife, several '
                                                         'hundred thousand people signed the petition nationwide.'},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'prompt': [   {   'speaker': 'Környezetvédő',
                                                                'text': 'Hogyan járult hozzá a Duna Kör a '
                                                                        'rendszerváltáshoz?'},
                                                            {'speaker': 'Történész', 'text': '_____'}],
                                              'options': [   'A környezet megóvása érdekében szervezett békés '
                                                             'tüntetések hatására a társadalom ráébredt saját erejére, '
                                                             'és a rezsim morálisan megbukott.',
                                                             'A Duna Kör minden tüntetőnek autót vásárolt.',
                                                             'A mozgalom elrendelte a Parlament azonnali lebontását.'],
                                              'correct': 0},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'question': "Which sentence demonstrates the idiomatic use of 'hatására' "
                                                          'to indicate a catalyst causing a shift in policy?',
                                              'options': [   'A szakmai érvek és a tömegtüntetések hatására a kormány '
                                                             'elrendelte az építkezés leállítását.',
                                                             'A kormány építkezett a hatására a tüntetéseknek.',
                                                             'A tüntetések hatására kormány nem volt Nagymaroson.',
                                                             'A szakmai hatására a folyó megállt a gátban.'],
                                              'correct': 0},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'prompt': [   {   'speaker': 'Hidrológus',
                                                                'text': 'Miért kiemelten fontos a Kis-Balaton '
                                                                        'védőrendszerének fenntartása?'},
                                                            {'speaker': 'Kutató', 'text': '_____'}],
                                              'options': [   'A Balaton elalgásodásának elkerülése végett a '
                                                             'mocsárvilág kiszűri a felesleges tápanyagokat a Zala '
                                                             'vizéből, ami megőrzi a tó tisztaságát.',
                                                             'Mert a Kis-Balatonon aranybánya működik.',
                                                             'Mert a Balaton vize kizárólag a Kis-Balatonból '
                                                             'származik.'],
                                              'correct': 0},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'tiles': [   'A',
                                                           'Duna',
                                                           'megóvása',
                                                           'érdekében',
                                                           'országos',
                                                           'összefogás',
                                                           'született.'],
                                              'solution': [   'A',
                                                              'Duna',
                                                              'megóvása',
                                                              'érdekében',
                                                              'országos',
                                                              'összefogás',
                                                              'született.'],
                                              'english': 'In the interest of protecting the Danube, nationwide '
                                                         'solidarity was born.'},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'tiles': [   'A',
                                                           'szennyezés',
                                                           'elkerülése',
                                                           'végett',
                                                           'a',
                                                           'hatóságok',
                                                           'lezárták',
                                                           'a',
                                                           'zsilipeket.'],
                                              'solution': [   'A',
                                                              'szennyezés',
                                                              'elkerülése',
                                                              'végett',
                                                              'a',
                                                              'hatóságok',
                                                              'lezárták',
                                                              'a',
                                                              'zsilipeket.'],
                                              'english': 'In order to avoid pollution, the authorities shut the '
                                                         'sluices.'},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'teaches': ['b2-causal-purposive-chains'],
                                              'template': [   {   'prompt': 'Write a sentence diagnosing an '
                                                                            'environmental consequence of drought on '
                                                                            "the Great Plain (use 'következtében' or "
                                                                            "'hatására').",
                                                                  'answer': 'A tartós aszályok következtében a '
                                                                            'Homokháton drasztikusan lecsökkent a '
                                                                            'talajvízszint, ami elsivatagosodással '
                                                                            'fenyegeti a mezőgazdaságot.'},
                                                              {   'prompt': 'Write a sentence proposing a water policy '
                                                                            "solution (use 'érdekében' or 'elkerülése "
                                                                            "végett').",
                                                                  'answer': 'A termőföldek megóvása érdekében a '
                                                                            'tavaszi árhullámok vizét a tájban kell '
                                                                            'tartani az elsivatagosodás megelőzése '
                                                                            'végett.'}]}]}}


if __name__ == "__main__":
    print("Building Hungarian B2 Culture Units 22, 23, and 24...")
    build_culture_unit(UNIT_22_DEMOGRAFIA)
    build_culture_unit(UNIT_23_LAKHATAS)
    build_culture_unit(UNIT_24_KORNYEZETPOLITIKA)
    print("All 3 Culture Track units (22, 23, 24) built successfully!")
