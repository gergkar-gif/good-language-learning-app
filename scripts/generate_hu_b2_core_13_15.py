#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Hungarian B2 Core Units 13, 14, and 15 (b2-13, b2-14, b2-15)
using build_core_unit from b2_unit_builder_helper.py.
"""
import sys

sys.path.insert(
    0,
    r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch",
)
from b2_unit_builder_helper import build_core_unit


# ============================================================================== #
# UNIT 13: Irony, Satire & Reading Between the Lines (b2-13)
# ============================================================================== #
UNIT_13 = {   'unit_num': 13,
    'title': 'Irony, Satire & Reading Between the Lines',
    'grammar_summary': 'Pragmatic stance particles for mitigation, emphatic denial, and irony: aligha, korántsem, '
                       'éppenséggel, cseppet sem; signaling shared background with hiszen, ugyebár, and mégiscsak; '
                       'litotes and understatement with nem éppen, alighanem, and mondhatni; and satirical modal '
                       'framing.',
    'grammar_skill': 'b2-discourse-particles',
    'vocab_skill': 'b2-13-vocab',
    'theme': 'Irony, satire and discourse stance',
    'intro_body': [   'Hungarian discourse relies heavily on nuanced pragmatic particles to signal speaker attitude, '
                      'skepticism, irony, and conversational stance without altering core syntactic structure. '
                      'Particles such as aligha (hardly), korántsem (by no means), éppenséggel (as a matter of fact / '
                      "actually), hiszen (after all), and ugyebár (isn't that so) guide the listener toward the "
                      "speaker's true evaluative meaning.",
                      "Through Kálmán Mikszáth's satirical masterpiece Beszterce ostroma (1894)—in which Count István "
                      'Pongrácz maintains a medieval fiefdom in 19th-century Upper Hungary, waging war against towns '
                      'while the narrator looks on with affectionate irony—you will master how Hungarians express '
                      'polite skepticism, litotes (understatement), and satirical critique.'],
    'classic_story': {   'slug': 'beszterceostroma',
                         'author': 'Mikszáth Kálmán',
                         'work': 'Beszterce ostroma (1894)',
                         'title': 'Pongrácz István gróf különös világa',
                         'summary': 'Pongrácz István gróf Nedec várában a középkori lovagkor szabályai szerint él, '
                                    'magánhadsereget tart fenn, és még Beszterce városát is ostrom alá veszi egy vélt '
                                    'sérelem miatt; ám amikor az árva Apolka a várba kerül, a komikus lovagi játék '
                                    'váratlanul mély emberi érzelmekkel telik meg.',
                         'characters': ['Pongrácz István gróf', 'Apolka'],
                         'paragraphs': [   {   'type': 'narration',
                                               'text': 'Nedec várának ódon bástyáin a tizenkilencedik század végén is '
                                                       'úgy lobogtak a zászlók, mintha a történelem megállt volna a '
                                                       'Mátyás király korabeli időkben. Pongrácz István gróf korántsem '
                                                       'tartotta magát modern embernek; éppenséggel úgy vélte, hogy a '
                                                       'modern világ a becsület és a lovagi erények hanyatlását hozta '
                                                       'magával.'},
                                           {   'type': 'narration',
                                               'text': 'A gróf udvartartása aligha hasonlított bármelyik korabeli '
                                                       'felvidéki úri lakhoz. Páncélos vitézeknek öltöztetett '
                                                       'zsoldosok őrizték a kapukat, a vendégeket ágyúlövéssel '
                                                       'fogadták, és a gróf minden reggel haditornát rendezett a '
                                                       'várudvaron, ugyebár a testi erő és a bátorság ébrentartása '
                                                       'végett.'},
                                           {   'type': 'narration',
                                               'text': 'A szomszédos városok lakói eleinte gyanakodva és félelemmel '
                                                       'figyelték a különc nemesúr viselt dolgait. Később azonban '
                                                       'ráébredtek, hogy a gróf szeszélyei mögött cseppet sem lakozik '
                                                       'gonoszság; hiszen István úr gavallér volt a végsőkig, és a '
                                                       'rászorulóknak mindig bőkezűen osztotta a pénzt.'},
                                           {   'type': 'narration',
                                               'text': 'Egy napon aztán váratlan hír rázta meg a vidéket: Beszterce '
                                                       'városa állítólag megsértette a várurak ősi előjogait. Pongrácz '
                                                       'gróf éktelen haragra gerjedt, és hadüzenetet küldött: '
                                                       'hadseregével ostrom alá veszi Besztercét, alighanem addig lőve '
                                                       'a bástyákat, amíg a magisztrátus bocsánatot nem kér a '
                                                       'sérelemért.'},
                                           {   'type': 'narration',
                                               'text': 'A hatóságok és a megyei tisztviselők persze kétségbeestek a '
                                                       'készülő botrány láttán. Hogyan lehetne megfékezni a grófot '
                                                       'anélkül, hogy vér folyna? Hiszen mindenki tudta, hogy a gróf '
                                                       'komolyan veszi a fenyegetést, és a fegyveres csendőrség '
                                                       'kivezénylése aligha vezetne békés megoldáshoz.'},
                                           {   'type': 'narration',
                                               'text': 'Ekkor lépett közbe a szerencse és a furfang: a tanácsosok '
                                                       'kitalálták, hogy a grófnak egy túszt kell adni a béke '
                                                       'zálogául. Így került Nedec várába a tizenhat éves, szelíd '
                                                       'Apolka, akit a rokonai magára hagytak, és akit a gróf a '
                                                       'leglovagiasabb tisztelettel fogadott a palotájában.'},
                                           {   'type': 'narration',
                                               'text': 'Apolka érkezésével a zord várfalak között új élet kezdődött. '
                                                       'Az öreg gróf szívét elöntötte a gyengédség; a lány nem éppen '
                                                       'rettegve, hanem inkább mosolyogva figyelte a lovagi '
                                                       'ceremóniákat, és szép lassan megszelídítette az idős nemesúr '
                                                       'vad fantáziáját.'},
                                           {   'type': 'narration',
                                               'text': 'Mikszáth zseniális elbeszélésében a komikum és a tragikum '
                                                       'elválaszthatatlanul összefonódik. Pongrácz gróf alakja '
                                                       'mégiscsak több egyszerű nevetséges hóbortnál: a letűnt '
                                                       'illúziók utolsó, megható védelmezője ő, akinek a világa aligha '
                                                       'térhet vissza többé, de emléke örökre fennmarad a magyar '
                                                       'irodalomban.'}],
                         'reading_questions': [   {   'question': 'Mi jellemezte Pongrácz István gróf életmódját Nedec '
                                                                  'várában?',
                                                      'options': [   'Középkori lovagként élt, magánhadsereget tartott '
                                                                     'és elutasította a modern világ szabályait.',
                                                                     'Modern gyárat építtetett a vár tövében, és banki '
                                                                     'ügyekkel foglalkozott.',
                                                                     'Elhagyta a várat, és Párizsban töltötte a '
                                                                     'mindennapjait.'],
                                                      'correct': 0},
                                                  {   'question': 'Hogyan fogadták a szomszédos városok lakói a gróf '
                                                                  'különc viselkedését?',
                                                      'options': [   'Ráébredtek, hogy a szeszélyei mögött cseppet sem '
                                                                     'lakozik gonoszság, hiszen gavallér és bőkezű '
                                                                     'volt.',
                                                                     'Azonnal felgyújtották a várat, és elűzték a '
                                                                     'grófot a Felvidékről.',
                                                                     'Bírósághoz fordultak, és elmegyógyintézetbe '
                                                                     'zárták a nemesurat.'],
                                                      'correct': 0},
                                                  {   'question': 'Mi történt Nedec várában, miután Apolka túszként a '
                                                                  'várba került?',
                                                      'options': [   'Apolka szelíd mosolyával és kedvességével '
                                                                     'megszelídítette a gróf vad lovagi fantáziáját.',
                                                                     'Apolka megszökött a várból az ostromlók '
                                                                     'segítségével.',
                                                                     'A gróf azonnal bezárta a lányt a legmélyebb '
                                                                     'várbörtönbe.'],
                                                      'correct': 0}]},
    'lessons': [   {   'num': 1,
                       'title': 'Hardly and By No Means (aligha, korántsem, éppenséggel)',
                       'grammar_label': 'Mitigating and emphatic denial particles: aligha, korántsem, cseppet sem, '
                                        'éppenséggel',
                       'goals': [   'I can express polite skepticism and mitigating doubt using aligha.',
                                    'I can firmly refute assumptions with korántsem and cseppet sem.',
                                    'I can introduce counter-intuitive nuances using éppenséggel.'],
                       'grammar_doc': {   'slug': 'mitigating-denial-particles',
                                          'title': 'Mitigating and Emphatic Denial: aligha, korántsem, éppenséggel',
                                          'text1_title': "Nuances of Epistemic Doubt with 'aligha'",
                                          'text1': "While everyday Hungarian uses 'nem valószínű' (not likely), B2 "
                                                   "discourse prefers 'aligha' (hardly / scarcely) to express nuanced "
                                                   "skepticism. 'Aligha' precedes the verb or focused element and "
                                                   "softens categorical negation into an educated doubt: 'Ez aligha "
                                                   "valósul meg' (This will hardly be realized). Never combine "
                                                   "'aligha' with 'nem' (*aligha nem is ungrammatical double negative "
                                                   'in modern Hungarian).',
                                          'text2_title': "Emphatic Refutation: 'korántsem', 'cseppet sem', and "
                                                         "Concession with 'éppenséggel'",
                                          'text2': "'Korántsem' (by no means / far from it) directly challenges an "
                                                   "unfounded presupposition: 'A feladat korántsem egyszerű' (The task "
                                                   "is far from simple). 'Cseppet sem' (not in the least / not a bit) "
                                                   "emphasizes zero degree of impact: 'Cseppet sem zavar' (It doesn't "
                                                   "bother me in the least). In contrast, 'éppenséggel' indicates an "
                                                   "unexpected possibility or polite concession: 'Éppenséggel "
                                                   "megpróbálhatjuk' (We could actually try it / it's not out of the "
                                                   'question).',
                                          'table_title': 'Denial and Mitigation Particles at B2',
                                          'table_rows': [   [   'aligha + verb',
                                                                'hardly / scarcely (epistemic mitigation)'],
                                                            [   'korántsem + adjective/adverb',
                                                                'by no means / far from (refuting assumption)'],
                                                            [   'cseppet sem + verb/adjective',
                                                                'not in the least (emphatic zero degree)'],
                                                            [   'éppenséggel + verb/modal',
                                                                'as a matter of fact / actually (concessive '
                                                                'possibility)']],
                                          'examples': [   {   'spanish': 'Az új javaslat aligha oldja meg a fennálló '
                                                                         'gazdasági nehézségeket.',
                                                              'english': 'The new proposal will hardly solve the '
                                                                         'existing economic difficulties.'},
                                                          {   'spanish': 'A helyzet korántsem olyan kétségbeejtő, mint '
                                                                         'amilyennek a hírek láttatják.',
                                                              'english': 'The situation is by no means as desperate as '
                                                                         'the news makes it seem.'},
                                                          {   'spanish': 'A vendég viselkedése cseppet sem zavarta az '
                                                                         'idős házigazdát.',
                                                              'english': "The guest's behavior did not disturb the "
                                                                         'elderly host in the least.'},
                                                          {   'spanish': 'Éppenséggel maradhatnánk még egy órát, ha '
                                                                         'nem sietsz a vonathoz.',
                                                              'english': 'As a matter of fact, we could stay another '
                                                                         "hour if you're not rushing to the train."}],
                                          'tip': "Use 'aligha' before verbs without 'nem' to sound natural and "
                                                 "elegant: say 'Aligha hiszem' instead of 'Nem hiszem nagyon'."},
                       'words': [   {'lemma': 'aligha', 'translation': 'hardly, scarcely', 'pos': 'adverb'},
                                    {'lemma': 'korántsem', 'translation': 'by no means, far from it', 'pos': 'adverb'},
                                    {   'lemma': 'éppenséggel',
                                        'translation': 'as a matter of fact, actually',
                                        'pos': 'adverb'},
                                    {'lemma': 'cseppet sem', 'translation': 'not in the least', 'pos': 'adverb'},
                                    {'lemma': 'tagadás', 'translation': 'denial, negation', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the Hungarian adverb 'korántsem' mean?",
                                                         'options': [   'by no means / far from it',
                                                                        'always without exception',
                                                                        'at the exact moment'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': "Which particle softens negation to mean 'hardly "
                                                                     "/ scarcely' without using 'nem'?",
                                                         'options': ['aligha', 'ugyebár', 'minduntalan'],
                                                         'correct': 0,
                                                         'teaches': ['b2-discourse-particles']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['aligha', 'hardly / scarcely'],
                                                                           ['korántsem', 'by no means'],
                                                                           ['éppenséggel', 'as a matter of fact'],
                                                                           ['cseppet sem', 'not in the least'],
                                                                           ['tagadás', 'denial / negation']],
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'A feladat ____ olyan egyszerű, mint '
                                                                          'amilyennek elsőre látszott. (by no means)',
                                                              'answer': 'korántsem',
                                                              'english': 'The task is by no means as simple as it '
                                                                         'seemed at first.',
                                                              'teaches': ['b2-discourse-particles']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A miniszter határozott ____ ellenére '
                                                                          'mindenki sejtette az igazságot. (denial)',
                                                              'answer': 'tagadása',
                                                              'english': "Despite the minister's firm denial, everyone "
                                                                         'suspected the truth.',
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence expresses polite skepticism '
                                                                          'about a proposal passing?',
                                                              'options': [   'Ez a javaslat aligha kap támogatást a '
                                                                             'bizottságban.',
                                                                             'Ez a javaslat minden bizonnyal azonnal '
                                                                             'érvénybe lép.',
                                                                             'Ez a javaslat tegnap este már megjelent '
                                                                             'az újságban.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-discourse-particles']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'terv',
                                                                         'aligha',
                                                                         'valósul',
                                                                         'meg',
                                                                         'az',
                                                                         'idén',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'terv',
                                                                            'aligha',
                                                                            'valósul',
                                                                            'meg',
                                                                            'az',
                                                                            'idén',
                                                                            '.'],
                                                            'english': 'The plan will hardly be realized this year.',
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A helyzet korántsem reménytelen a '
                                                                             'tárgyalások után.',
                                                            'base_word': 'korántsem',
                                                            'options': [   {   'word': 'aligha',
                                                                               'inflected': 'aligha',
                                                                               'sentence': 'A helyzet aligha '
                                                                                           'reménytelen a tárgyalások '
                                                                                           'után.',
                                                                               'gloss': 'hardly'},
                                                                           {   'word': 'cseppet sem',
                                                                               'inflected': 'cseppet sem',
                                                                               'sentence': 'A helyzet cseppet sem '
                                                                                           'reménytelen a tárgyalások '
                                                                                           'után.',
                                                                               'gloss': 'not in the least'}],
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'Nem haragszom rád, ____ bántott a tréfás '
                                                                        'megjegyzésed. (not in the least)',
                                                            'answer': 'cseppet sem',
                                                            'english': 'I am not angry with you, your playful remark '
                                                                       'did not hurt me in the least.',
                                                            'teaches': ['b2-13-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "Which sentence uses 'éppenséggel' to express "
                                                                        'a polite alternative possibility?',
                                                            'options': [   'Éppenséggel maradhatnánk még egy órát, ha '
                                                                           'van kedved beszélgetni.',
                                                                           'Éppenséggel soha többé nem látom ezt a '
                                                                           'várost.',
                                                                           'Éppenséggel tegnap délben ebédeltünk a '
                                                                           'vendéglőben.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Képviselő',
                                                                              'text': 'Szerinted elfogadják a '
                                                                                      'költségvetési módosítást a '
                                                                                      'képviselők?'},
                                                                          {'speaker': 'Tanácsos', 'text': '_____'}],
                                                            'options': [   'Aligha, hiszen a frakciók többsége már '
                                                                           'korábban ellenezte a kiadásokat.',
                                                                           'Igen, mert tegnap délután minden képviselő '
                                                                           'elutazott vidékre.',
                                                                           'Nem, minthogy a bástyák tegnap hajnalban '
                                                                           'leomlottak.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kolléga',
                                                                              'text': 'Nem zavar, ha megkérdezem a '
                                                                                      'véleményedet erről a cikkről?'},
                                                                          {'speaker': 'Szerkesztő', 'text': '_____'}],
                                                            'options': [   'Cseppet sem zavar, éppenséggel örülök, '
                                                                           'hogy kikéred a tanácsomat.',
                                                                           'Igen, mert a vonat már elindult az '
                                                                           'állomásról.',
                                                                           'Nem zavar, bár semmit sem értek a '
                                                                           'színházhoz.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write that the new proposal '
                                                                                         'will hardly solve the '
                                                                                         'existing crisis.',
                                                                               'answer': 'Az új javaslat aligha oldja '
                                                                                         'meg a fennálló válságot.'}],
                                                           'teaches': ['b2-discourse-particles']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write that the situation is '
                                                                                         'by no means hopeless, as a '
                                                                                         'matter of fact we can still '
                                                                                         'succeed.',
                                                                               'answer': 'A helyzet korántsem '
                                                                                         'reménytelen, éppenséggel még '
                                                                                         'sikerülhet is.'}],
                                                           'teaches': ['b2-discourse-particles']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What nuance does 'aligha' carry?",
                                                         'options': [   'hardly / scarcely (epistemic doubt)',
                                                                        'certainly / without doubt',
                                                                        'precisely at noon'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A vizsgálat eredménye ____ volt kielégítő a '
                                                                     'bizottság számára. (by no means)',
                                                         'answer': 'korántsem',
                                                         'english': 'The result of the examination was by no means '
                                                                    'satisfactory for the committee.',
                                                         'teaches': ['b2-discourse-particles']}]}},
                   {   'num': 2,
                       'title': 'Signaling Shared Knowledge and Irony (hiszen, ugyebár)',
                       'grammar_label': 'Pragmatic stance particles: hiszen, ugyebár, hát, mégiscsak',
                       'goals': [   'I can invoke shared knowledge and background assumptions using hiszen.',
                                    'I can seek consensus or convey ironic complicity using ugyebár.',
                                    'I can reaffirm neglected truths in a discussion using mégiscsak.'],
                       'grammar_doc': {   'slug': 'shared-knowledge-irony',
                                          'title': 'Shared Knowledge and Pragmatic Complicity: hiszen, ugyebár, '
                                                   'mégiscsak',
                                          'text1_title': "Appealing to Shared Premises with 'hiszen'",
                                          'text1': "'Hiszen' (after all / surely) invokes a fact that both speaker and "
                                                   'listener already know, using it as justification or gentle '
                                                   "protest: 'Nem kell bemutatnom őt, hiszen mindannyian ismeritek' (I "
                                                   "don't need to introduce him, after all, you all know him). In "
                                                   "dialogue, clause-initial 'Hiszen...' expresses surprise when "
                                                   "reality contradicts expectations: 'Hiszen tegnap még egészen mást "
                                                   "mondtál!'",
                                          'text2_title': "Seeking Consensus and Ironic Complicity with 'ugyebár'",
                                          'text2': "'Ugyebár' (isn't that so / as is well known) invites agreement or "
                                                   "reminds the interlocutor of an inescapable premise: 'A szabályok "
                                                   "mindenkire érvényesek, ugyebár?' In ironic contexts, it creates "
                                                   'humorous distance by appealing to a pretense both speakers '
                                                   "recognize as absurd. 'Mégiscsak' (after all / nonetheless) "
                                                   'reasserts a core value or truth despite counter-arguments: '
                                                   "'Mégiscsak érdemes volt eljönni.'",
                                          'table_title': 'Pragmatic Stance Particles',
                                          'table_rows': [   [   'hiszen + clause',
                                                                'after all (appealing to shared '
                                                                'knowledge/justification)'],
                                                            [   'ugyebár (parenthetical)',
                                                                "isn't it so? / as you know (seeking agreement or "
                                                                'ironic complicity)'],
                                                            [   'mégiscsak + verb',
                                                                'after all / nonetheless (reasserting neglected '
                                                                'truth)'],
                                                            [   'hát (clause-initial)',
                                                                'well / as you see (discourse marker of '
                                                                'obviousness/resignation)']],
                                          'examples': [   {   'spanish': 'Miért kételkednénk benne, hiszen mindenki '
                                                                         'ismeri az igazságot?',
                                                              'english': 'Why would we doubt it, after all, everyone '
                                                                         'knows the truth?'},
                                                          {   'spanish': 'A becsület, ugyebár, mindennél fontosabb egy '
                                                                         'nemesember számára.',
                                                              'english': 'Honor, as is well known, is more important '
                                                                         'than anything for a nobleman.'},
                                                          {   'spanish': 'Bár sokba került, mégiscsak megérte '
                                                                         'felújítani a régi várat.',
                                                              'english': 'Although it cost a lot, it was nonetheless '
                                                                         'worth renovating the old castle.'},
                                                          {   'spanish': 'Hát persze hogy nem haragszom, csak '
                                                                         'meglepődtem a híren.',
                                                              'english': "Well of course I'm not angry, I was just "
                                                                         'surprised by the news.'}],
                                          'tip': "When 'ugyebár' appears mid-sentence as a parenthetical remark, set "
                                                 "it off with commas: 'Ez a kérdés, ugyebár, nem tartozik ide.'"},
                       'words': [   {'lemma': 'hiszen', 'translation': 'after all, surely', 'pos': 'conjunction'},
                                    {'lemma': 'ugyebár', 'translation': "isn't that so, as we know", 'pos': 'adverb'},
                                    {'lemma': 'mégiscsak', 'translation': 'after all, nonetheless', 'pos': 'adverb'},
                                    {'lemma': 'célzás', 'translation': 'allusion, hint', 'pos': 'noun'},
                                    {'lemma': 'közhely', 'translation': 'platitude, cliché', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the noun 'közhely' mean?",
                                                         'options': [   'platitude / cliché',
                                                                        'noble castle',
                                                                        'ironic question'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which particle appeals to shared knowledge or '
                                                                     "obvious justification ('after all')?",
                                                         'options': ['hiszen', 'aligha', 'korántsem'],
                                                         'correct': 0,
                                                         'teaches': ['b2-discourse-particles']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['hiszen', 'after all / surely'],
                                                                           [   'ugyebár',
                                                                               "isn't that so / as is well known"],
                                                                           ['mégiscsak', 'after all / nonetheless'],
                                                                           ['célzás', 'allusion / hint'],
                                                                           ['közhely', 'platitude / cliché']],
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Nem kell bemutatnom őt, ____ mindannyian '
                                                                          'jól ismeritek a könyveit. (after all)',
                                                              'answer': 'hiszen',
                                                              'english': 'I do not need to introduce him, after all, '
                                                                         'you all know his books well.',
                                                              'teaches': ['b2-discourse-particles']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A szónok beszéde tele volt unalmas ____ és '
                                                                          'közhelyekkel. (platitudes)',
                                                              'answer': 'közhelyekkel',
                                                              'english': "The orator's speech was full of boring "
                                                                         'platitudes and clichés.',
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': "Select the sentence where 'ugyebár' invites "
                                                                          'consensus from the listener:',
                                                              'options': [   'Ez a döntés, ugyebár, mindannyiunk '
                                                                             'jövőjét érinti.',
                                                                             'A döntés aligha érinti a város lakóit.',
                                                                             'A döntés tegnap délután született meg a '
                                                                             'városházán.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-discourse-particles']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'szabályok',
                                                                         'mindenkire',
                                                                         'vonatkoznak,',
                                                                         'ugyebár',
                                                                         'nem',
                                                                         'tévedek',
                                                                         '?'],
                                                            'solution': [   'A',
                                                                            'szabályok',
                                                                            'mindenkire',
                                                                            'vonatkoznak,',
                                                                            'ugyebár',
                                                                            'nem',
                                                                            'tévedek',
                                                                            '?'],
                                                            'english': 'The rules apply to everyone, I am not '
                                                                       'mistaken, am I?',
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Mégiscsak sikerült megállapodnunk a '
                                                                             'legfontosabb feltételekben.',
                                                            'base_word': 'Mégiscsak',
                                                            'options': [   {   'word': 'hiszen',
                                                                               'inflected': 'Hiszen',
                                                                               'sentence': 'Hiszen sikerült '
                                                                                           'megállapodnunk a '
                                                                                           'legfontosabb '
                                                                                           'feltételekben.',
                                                                               'gloss': 'after all'},
                                                                           {   'word': 'ugyebár',
                                                                               'inflected': 'Ugyebár',
                                                                               'sentence': 'Ugyebár sikerült '
                                                                                           'megállapodnunk a '
                                                                                           'legfontosabb '
                                                                                           'feltételekben.',
                                                                               'gloss': 'as you know'}],
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A cikk finom ____ élt a polgármester '
                                                                        'legutóbbi baklövésére. (allusion)',
                                                            'answer': 'célzással',
                                                            'english': 'The article made a subtle allusion to the '
                                                                       "mayor's recent blunder.",
                                                            'teaches': ['b2-13-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "Which sentence uses 'mégiscsak' to reassert a "
                                                                        'neglected truth despite obstacles?',
                                                            'options': [   'Minden nehézség ellenére mégiscsak érdemes '
                                                                           'volt elindítani a kutatást.',
                                                                           'Minden nehézség ellenére aligha indul el a '
                                                                           'kutatás az idén.',
                                                                           'A kutatás tegnap este hét órakor '
                                                                           'fejeződött be az egyetemen.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Újságíró',
                                                                              'text': 'Miért vitatkozunk még mindig '
                                                                                      'ezen a nyilvánvaló kérdésen?'},
                                                                          {'speaker': 'Főszerkesztő', 'text': '_____'}],
                                                            'options': [   'Hiszen a tények magukért beszélnek, '
                                                                           'felesleges tovább húzni az időt.',
                                                                           'Mert a posta tegnap délután négy órakor '
                                                                           'bezárt.',
                                                                           'Ugyebár a villamos éppen most kanyarodott '
                                                                           'a sarkon.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kritikus',
                                                                              'text': 'Nem gondolod, hogy túlzottan '
                                                                                      'szigorú volt a könyvről írt '
                                                                                      'bírálat?'},
                                                                          {'speaker': 'Olvasó', 'text': '_____'}],
                                                            'options': [   'Mégiscsak be kell látnunk, hogy a regény '
                                                                           'nem érte el a szerző korábbi színvonalát.',
                                                                           'Igen, mert a színészek tegnap '
                                                                           'elfelejtették a szövegüket a színpadon.',
                                                                           'Hiszen a könyvesboltban nem volt egyetlen '
                                                                           'vásárló sem tegnap.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Why would we doubt '
                                                                                         'it, after all, everyone '
                                                                                         'knows the truth?',
                                                                               'answer': 'Miért kételkednénk benne, '
                                                                                         'hiszen mindenki ismeri az '
                                                                                         'igazságot?'}],
                                                           'teaches': ['b2-discourse-particles']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: In the end, it was '
                                                                                         'nonetheless worth listening '
                                                                                         'to his advice.',
                                                                               'answer': 'Végül mégiscsak érdemes volt '
                                                                                         'meghallgatni a tanácsát.'}],
                                                           'teaches': ['b2-discourse-particles']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'célzás' mean in Hungarian literary "
                                                                     'and everyday discourse?',
                                                         'options': [   'allusion / indirect hint',
                                                                        'direct military attack',
                                                                        'official invitation'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A becsület, ____, mindennél fontosabb egy '
                                                                     'úriember számára. (as is well known)',
                                                         'answer': 'ugyebár',
                                                         'english': 'Honor, as is well known, is more important than '
                                                                    'anything for a gentleman.',
                                                         'teaches': ['b2-discourse-particles']}]}},
                   {   'num': 3,
                       'title': 'Exaggeration and Understatement',
                       'grammar_label': 'Litotes and ironic understatement: nem éppen, alighanem, mondhatni',
                       'goals': [   'I can use litotes (nem éppen) to soften criticism or convey dry irony.',
                                    'I can hedge assertions prudently with alighanem and mondhatni.',
                                    'I can distinguish between literal statements and sardonic understatements.'],
                       'grammar_doc': {   'slug': 'litotes-ironic-understatement',
                                          'title': 'Litotes and Hedged Assertion: nem éppen, alighanem, mondhatni',
                                          'text1_title': 'The Power of Litotes (nem éppen)',
                                          'text1': 'Litotes (understatement through negation) is a hallmark of '
                                                   'sophisticated Hungarian commentary. Instead of blunt criticism '
                                                   "('Ez nagyon rossz volt'), an educated speaker says 'Nem éppen volt "
                                                   "zseniális' (It was not exactly brilliant). Saying 'nem éppen "
                                                   "olcsó' signals that something is prohibitively expensive. The "
                                                   "pitch falls on 'nem' and rises ironically on the adjective.",
                                          'text2_title': "Hedged Probability: 'alighanem' and 'mondhatni'",
                                          'text2': "'Alighanem' expresses strong probability tempered with modesty "
                                                   "('in all likelihood / most probably'): 'Alighanem igaza van' (In "
                                                   "all likelihood he is right). 'Mondhatni' functions as a "
                                                   "parenthetical hedge ('so to speak / one might say'): 'Ez a döntés, "
                                                   "mondhatni, elhamarkodott volt.' Together, they allow a writer to "
                                                   'critique without appearing overly aggressive.',
                                          'table_title': 'Litotes and Understatement Patterns',
                                          'table_rows': [   [   'nem éppen + adjective',
                                                                'not exactly / far from (polite or ironic negation)'],
                                                            [   'alighanem + verb/predicate',
                                                                'in all likelihood / most probably (hedged assertion)'],
                                                            [   'mondhatni (parenthetical)',
                                                                'so to speak / one might say (stylistic moderation)'],
                                                            [   'enyhítés vs. túlzás',
                                                                'understatement vs. exaggeration / hyperbole']],
                                          'examples': [   {   'spanish': 'A szálloda szolgáltatásai nem éppen a luxust '
                                                                         'idézték.',
                                                              'english': "The hotel's services did not exactly evoke "
                                                                         'luxury.'},
                                                          {   'spanish': 'Alighanem elfelejtette, hogy a határidő '
                                                                         'tegnap lejárt.',
                                                              'english': 'In all likelihood, he forgot that the '
                                                                         'deadline expired yesterday.'},
                                                          {   'spanish': 'A helyzet, mondhatni, meglehetősen '
                                                                         'bonyolulttá vált.',
                                                              'english': 'The situation has become, so to speak, '
                                                                         'rather complicated.'},
                                                          {   'spanish': 'Az író fanyar humorral mutatta be a nemesség '
                                                                         'gyengeségeit.',
                                                              'english': "The writer depicted the nobility's "
                                                                         'weaknesses with wry humor.'}],
                                          'tip': "Pay attention to context: 'nem éppen zseniális' is rarely neutral; "
                                                 'in Hungarian culture, it is an unmistakable signal of ironic '
                                                 'disapproval.'},
                       'words': [   {   'lemma': 'alighanem',
                                        'translation': 'in all likelihood, most probably',
                                        'pos': 'adverb'},
                                    {   'lemma': 'mondhatni',
                                        'translation': 'so to speak, one might say',
                                        'pos': 'adverb'},
                                    {'lemma': 'enyhítés', 'translation': 'mitigation, understatement', 'pos': 'noun'},
                                    {'lemma': 'túlzás', 'translation': 'exaggeration, hyperbole', 'pos': 'noun'},
                                    {'lemma': 'fanyar', 'translation': 'tart, wry, sardonic', 'pos': 'adjective'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the adjective 'fanyar' mean when "
                                                                     'describing humor?',
                                                         'options': [   'wry / tart / sardonically dry',
                                                                        'cheerful and loud',
                                                                        'completely absent'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'What rhetorical device is used when someone says '
                                                                     "'nem éppen zseniális' instead of 'rossz'?",
                                                         'options': [   'litotes (ironic understatement)',
                                                                        'tautology',
                                                                        'metaphorical inversion'],
                                                         'correct': 0,
                                                         'teaches': ['b2-discourse-particles']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['alighanem', 'in all likelihood'],
                                                                           ['mondhatni', 'so to speak'],
                                                                           ['enyhítés', 'understatement / mitigation'],
                                                                           ['túlzás', 'exaggeration / hyperbole'],
                                                                           ['fanyar', 'wry / sardonic']],
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'A professzor tegnapi előadása ____ volt '
                                                                          'magával ragadó. (not exactly)',
                                                              'answer': 'nem éppen',
                                                              'english': "The professor's lecture yesterday was not "
                                                                         'exactly captivating.',
                                                              'teaches': ['b2-discourse-particles']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'Nem kellene megijedni, ez a híresztelés '
                                                                          'nyilvánvaló ____. (exaggeration)',
                                                              'answer': 'túlzás',
                                                              'english': 'There is no need to be frightened, this '
                                                                         'rumor is an obvious exaggeration.',
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence contains a hedged assertion '
                                                                          "with 'alighanem'?",
                                                              'options': [   'A gróf alighanem elfelejtette, hogy '
                                                                             'melyik évszázadban élünk.',
                                                                             'A gróf tegnap megérkezett a várba.',
                                                                             'A gróf minden bizonnyal azonnal '
                                                                             'elrendelte az ostromot.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-discourse-particles']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Ez',
                                                                         'a',
                                                                         'megoldás,',
                                                                         'mondhatni,',
                                                                         'nem',
                                                                         'éppen',
                                                                         'tökéletes',
                                                                         '.'],
                                                            'solution': [   'Ez',
                                                                            'a',
                                                                            'megoldás,',
                                                                            'mondhatni,',
                                                                            'nem',
                                                                            'éppen',
                                                                            'tökéletes',
                                                                            '.'],
                                                            'english': 'This solution is, one might say, not exactly '
                                                                       'perfect.',
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Alighanem tévedett a szerző az '
                                                                             'elemzésében.',
                                                            'base_word': 'Alighanem',
                                                            'options': [   {   'word': 'mondhatni',
                                                                               'inflected': 'Mondhatni,',
                                                                               'sentence': 'Mondhatni, tévedett a '
                                                                                           'szerző az elemzésében.',
                                                                               'gloss': 'one might say'},
                                                                           {   'word': 'nem éppen',
                                                                               'inflected': 'Nem éppen',
                                                                               'sentence': 'Nem éppen tévedett a '
                                                                                           'szerző az elemzésében.',
                                                                               'gloss': 'not quite'}],
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'Az író ____ humorral mutatta be a vidéki '
                                                                        'nemesség hóbortjait. (wry)',
                                                            'answer': 'fanyar',
                                                            'english': 'The writer depicted the whims of the '
                                                                       'provincial nobility with wry humor.',
                                                            'teaches': ['b2-13-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "What does the speaker mean when saying 'A "
                                                                        "szálloda nem éppen a kényelem csúcsa volt'?",
                                                            'options': [   'A szálloda meglehetősen kényelmetlen és '
                                                                           'szerény volt.',
                                                                           'A szálloda a világ legdrágább palotája '
                                                                           'volt.',
                                                                           'A szállodát tegnap bontották le.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Néző',
                                                                              'text': 'Hogy tetszett a tegnapi '
                                                                                      'színházi bemutató a '
                                                                                      'Nemzetiben?'},
                                                                          {'speaker': 'Kritikus', 'text': '_____'}],
                                                            'options': [   'Hát, mondhatni, nem éppen életem '
                                                                           'legnagyobb élménye volt.',
                                                                           'A színház ma délután zárva tart átépítés '
                                                                           'miatt.',
                                                                           'Mert a jegyeket már két hete megvettem a '
                                                                           'pénztárban.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Várnagy',
                                                                              'text': 'Szerinted megérkezik a gróf a '
                                                                                      'haditanácsra a megbeszélt '
                                                                                      'időben?'},
                                                                          {'speaker': 'Hadsegéd', 'text': '_____'}],
                                                            'options': [   'Alighanem késni fog, hiszen még a '
                                                                           'lószállító hintó sem indult el a '
                                                                           'várkapuból.',
                                                                           'Igen, mert a postakocsi már tavaly '
                                                                           'megérkezett a faluba.',
                                                                           'Nem, mivel soha nem látott még lovat az '
                                                                           'életében.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: In all likelihood, '
                                                                                         'the author intended this '
                                                                                         'character as an ironic '
                                                                                         'critique.',
                                                                               'answer': 'Alighanem ironikus '
                                                                                         'bírálatnak szánta a szerző '
                                                                                         'ezt a szereplőt.'}],
                                                           'teaches': ['b2-discourse-particles']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: His reaction was, so '
                                                                                         'to speak, not exactly '
                                                                                         'welcoming.',
                                                                               'answer': 'A reakciója, mondhatni, nem '
                                                                                         'éppen volt szívélyes.'}],
                                                           'teaches': ['b2-discourse-particles']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'mondhatni' mean when used "
                                                                     'parenthetically?',
                                                         'options': [   'so to speak / one might say',
                                                                        'definitely never',
                                                                        'without a doubt'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A fogadtatás ____ volt szívélyes, de legalább '
                                                                     'udvariasan meghallgattak minket. (not exactly)',
                                                         'answer': 'nem éppen',
                                                         'english': 'The reception was not exactly cordial, but at '
                                                                    'least they listened to us politely.',
                                                         'teaches': ['b2-discourse-particles']}]}},
                   {   'num': 4,
                       'title': 'Social Satire in Action',
                       'grammar_label': 'Satirical stance: combining modal particles with conditional forms',
                       'goals': [   'I can combine conditional verb forms with modal particles (szinte, mintha) to '
                                    'satirize absurd behavior.',
                                    'I can formulate humorous critique without aggressive confrontation.',
                                    'I can recognize the satirical techniques used by Hungarian feuilleton writers.'],
                       'grammar_doc': {   'slug': 'social-satire-in-action',
                                          'title': 'Satirical Rhetoric: Conditionals, Counterfactuals, and Modality',
                                          'text1_title': "Counterfactual Framing with 'mintha... lenne'",
                                          'text1': 'Social satire exposes human folly by treating absurd illusions as '
                                                   "if they were unquestioned reality. In Hungarian, pairing 'mintha' "
                                                   '(as if) with conditional forms creates this theatrical distance: '
                                                   "'Úgy viselkedik, mintha ő irányítaná az egész várost' (He behaves "
                                                   "as if he were directing the whole town). The particle 'szinte "
                                                   "már-már' (virtually / bordering on) heightens this disproportion: "
                                                   "'Szinte már-már azt hihetnénk, hogy a gróf maga Napóleon császár.'",
                                          'text2_title': 'Polite Irony vs. Open Mockery (gúny vs. irónia)',
                                          'text2': "While 'gúny' (mockery / sarcasm) is aggressive and divisive, "
                                                   "authentic literary satire ('szatíra') uses polite formal phrasing "
                                                   "and rhetorical restraint to let hypocrisy ('álszentség') defeat "
                                                   "itself. Framing questions with 'Aligha hinné bárki, hogy...' "
                                                   'exposes pretensions without resorting to insult.',
                                          'table_title': 'Satirical Discourse Structures',
                                          'table_rows': [   [   'mintha + conditional',
                                                                'as if it were (counterfactual framing)'],
                                                            [   'szinte már-már + conditional',
                                                                'virtually bordering on (exposing exaggeration)'],
                                                            [   'aligha hinné bárki, hogy...',
                                                                'hardly would anyone believe that... (rhetorical '
                                                                'skepticism)'],
                                                            [   'képmutató magatartás',
                                                                'hypocritical conduct (target of satire)']],
                                          'examples': [   {   'spanish': 'Úgy tesz a hivatalnok, mintha az ő engedélye '
                                                                         'nélkül megállna az élet.',
                                                              'english': 'The official acts as if life would stop '
                                                                         'without his permission.'},
                                                          {   'spanish': 'Szinte már-már azt hihetnénk, hogy a '
                                                                         'kisvárosi vita világméretű konfliktus.',
                                                              'english': 'One would virtually think that the '
                                                                         'small-town dispute is a worldwide conflict.'},
                                                          {   'spanish': 'A szatíra kíméletlenül leleplezi a '
                                                                         'társadalmi álszentséget és gőgöt.',
                                                              'english': 'Satire ruthlessly unmasks social hypocrisy '
                                                                         'and arrogance.'},
                                                          {   'spanish': 'Aligha hinné bárki, hogy a gróf komolyan '
                                                                         'gondolta az ágyúlövéseket.',
                                                              'english': 'Hardly would anyone believe that the count '
                                                                         'was serious about the cannon shots.'}],
                                          'tip': 'In Hungarian satire, the most damaging critiques are wrapped in '
                                                 'impeccable formal politeness.'},
                       'words': [   {'lemma': 'gúny', 'translation': 'mockery, sarcasm', 'pos': 'noun'},
                                    {'lemma': 'szatíra', 'translation': 'satire', 'pos': 'noun'},
                                    {'lemma': 'álszentség', 'translation': 'hypocrisy, sanctimony', 'pos': 'noun'},
                                    {   'lemma': 'képmutató',
                                        'translation': 'hypocritical, hypocrite',
                                        'pos': 'adjective'},
                                    {'lemma': 'bírálat', 'translation': 'critique, review, censure', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the noun 'álszentség' mean in social "
                                                                     'and literary criticism?',
                                                         'options': [   'hypocrisy / sanctimony',
                                                                        'generous charity',
                                                                        'military courage'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which construction frames behavior as absurdly '
                                                                     'theatrical?',
                                                         'options': [   'mintha... lenne (conditional)',
                                                                        'amint... lett (indicative)',
                                                                        'mialatt... volt'],
                                                         'correct': 0,
                                                         'teaches': ['b2-discourse-particles']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['gúny', 'mockery / sarcasm'],
                                                                           ['szatíra', 'satire'],
                                                                           ['álszentség', 'hypocrisy'],
                                                                           ['képmutató', 'hypocritical'],
                                                                           ['bírálat', 'critique / censure']],
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Úgy tesz a hivatalnok, ____ ő irányítaná az '
                                                                          'egész várost. (as if)',
                                                              'answer': 'mintha',
                                                              'english': 'The official acts as if he were directing '
                                                                         'the entire city.',
                                                              'teaches': ['b2-discourse-particles']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A komédia kíméletlenül leleplezi a '
                                                                          'kisvárosi társadalom ____. (hypocrisy)',
                                                              'answer': 'álszentségét',
                                                              'english': 'The comedy ruthlessly exposes the hypocrisy '
                                                                         'of small-town society.',
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence combines modal particles '
                                                                          'with conditional forms for satirical '
                                                                          'effect?',
                                                              'options': [   'Szinte már-már azt hihetnénk, hogy a '
                                                                             'gróf maga Napóleon császár.',
                                                                             'A gróf megvette a könyvet a boltban '
                                                                             'tegnap.',
                                                                             'A csendőrök reggel hétkor masíroztak a '
                                                                             'főtéren.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-discourse-particles']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Aligha',
                                                                         'hinné',
                                                                         'bárki,',
                                                                         'hogy',
                                                                         'ez',
                                                                         'a',
                                                                         'bohózat',
                                                                         'valóság',
                                                                         '.'],
                                                            'solution': [   'Aligha',
                                                                            'hinné',
                                                                            'bárki,',
                                                                            'hogy',
                                                                            'ez',
                                                                            'a',
                                                                            'bohózat',
                                                                            'valóság',
                                                                            '.'],
                                                            'english': 'Hardly would anyone believe that this farce is '
                                                                       'reality.',
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Szinte már-már nevetségesnek tűnik ez a '
                                                                             'túlzott buzgalom.',
                                                            'base_word': 'Szinte már-már',
                                                            'options': [   {   'word': 'alighanem',
                                                                               'inflected': 'Alighanem',
                                                                               'sentence': 'Alighanem nevetségesnek '
                                                                                           'tűnik ez a túlzott '
                                                                                           'buzgalom.',
                                                                               'gloss': 'in all likelihood'},
                                                                           {   'word': 'korántsem',
                                                                               'inflected': 'Korántsem',
                                                                               'sentence': 'Korántsem nevetségesnek '
                                                                                           'tűnik ez a túlzott '
                                                                                           'buzgalom.',
                                                                               'gloss': 'by no means'}],
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A bátor újságíró nem rejtette véka alá a '
                                                                        'rendszerről szóló éles ____. (critique)',
                                                            'answer': 'bírálatát',
                                                            'english': 'The courageous journalist did not hide his '
                                                                       'sharp critique of the system.',
                                                            'teaches': ['b2-13-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "What makes Mikszáth's portrayal of Pongrácz "
                                                                        'István satirical rather than cruel?',
                                                            'options': [   'Együttérző iróniával mutatja be a lovagi '
                                                                           'pózok és a rideg valóság ellentétét.',
                                                                           'A szerző durva szitkokkal illeti a '
                                                                           'felvidéki nemességet.',
                                                                           'A történetben senki sem beszél magyarul a '
                                                                           'várban.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Polgármester',
                                                                              'text': 'Hogyan merészelt hadat üzenni a '
                                                                                      'gróf egy egész békés városnak?'},
                                                                          {'speaker': 'Jegyző', 'text': '_____'}],
                                                            'options': [   'Úgy érezte, mintha a középkori törvények '
                                                                           'még mindig érvényben lennének a '
                                                                           'vármegyében.',
                                                                           'Mert a postás elfelejtette kézbesíteni a '
                                                                           'tegnapi újságot a városházára.',
                                                                           'Hiszen a polgármester már régen lemondott '
                                                                           'tisztségéről az ünnepségen.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Szerkesztő',
                                                                              'text': 'Nem tartasz attól, hogy '
                                                                                      'megbántod őt ezzel a nyílt '
                                                                                      'bírálattal?'},
                                                                          {'speaker': 'Cikkíró', 'text': '_____'}],
                                                            'options': [   'Nem nyílt gúnnyal válaszolok, hanem finom '
                                                                           'iróniával figyelmeztetem a képmutatásra.',
                                                                           'Igen, ezért azonnal elküldöm a zsoldosokat '
                                                                           'a kapu elé.',
                                                                           'Mert a hadüzenet már tegnap érvényét '
                                                                           'vesztette a megyei bíróságon.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: One would virtually '
                                                                                         'think that the count lives '
                                                                                         'in another century.',
                                                                               'answer': 'Szinte már-már azt '
                                                                                         'hihetnénk, hogy a gróf egy '
                                                                                         'másik évszázadban él.'}],
                                                           'teaches': ['b2-discourse-particles']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Satire unmasks '
                                                                                         'hypocritical behavior '
                                                                                         'through polite irony.',
                                                                               'answer': 'A szatíra udvarias iróniával '
                                                                                         'leplezi le a képmutató '
                                                                                         'viselkedést.'}],
                                                           'teaches': ['b2-discourse-particles']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the adjective 'képmutató' describe?",
                                                         'options': [   'a person who pretends to have virtues they '
                                                                        'lack',
                                                                        'a talented painter of portraits',
                                                                        'a strict military officer'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'Olyan büszkén lépeget az udvaron, ____ ő lenne a '
                                                                     'vár egyetlen ura. (as if)',
                                                         'answer': 'mintha',
                                                         'english': 'He steps so proudly in the courtyard as if he '
                                                                    'were the sole lord of the castle.',
                                                         'teaches': ['b2-discourse-particles']}]}},
                   {   'num': 5,
                       'title': 'Writing an Ironic Commentary',
                       'grammar_label': 'Stylistic integration: discourse particles and irony in essays and reviews',
                       'goals': [   'I can write a sophisticated ironic commentary or cultural column (tárca).',
                                    'I can weave discourse particles (hiszen, korántsem, alighanem) into flowing '
                                    'prose.',
                                    "I can analyze Mikszáth's portrayal of Pongrácz István in Beszterce ostroma."],
                       'grammar_doc': {   'slug': 'ironic-commentary-tarca',
                                          'title': 'The Art of the Tárca: Crafting an Ironic Literary Essay',
                                          'text1_title': 'The Hungarian Tárca Tradition',
                                          'text1': "The Hungarian 'tárca' (feuilleton or cultural column) developed by "
                                                   'Mikszáth, Kosztolányi, and Márai blends casual storytelling with '
                                                   'sharp philosophical observation. The author maintains a '
                                                   "conversational tone ('társalgási hangnem') that engages the reader "
                                                   'as an intellectual equal while dissecting social vanity.',
                                          'text2_title': 'Weaving Stance Particles into Seamless Prose',
                                          'text2': 'An effective commentary never announces its humor bluntly. '
                                                   "Instead, it weaves together rhetorical appeals ('Hiszen ki ne "
                                                   "ismerné...?'), litotes ('nem éppen csekély siker'), hedged "
                                                   "probability ('alighanem úgy vélték'), and self-irony ('önirónia'). "
                                                   "The writer banters ('élcelődik') without cruelty, inviting the "
                                                   'reader into amused complicity.',
                                          'table_title': 'Feuilleton and Essay Phrasing',
                                          'table_rows': [   [   'tárca / tárcanovella',
                                                                'feuilleton / short satirical narrative'],
                                                            ['választékos hangnem', 'refined tone / register'],
                                                            [   'öniróniával szemlélni',
                                                                'to view with self-irony / humility'],
                                                            [   'élcelődik valamin',
                                                                'to banter / joke sardonically about something']],
                                          'examples': [   {   'spanish': 'A szerző szellemes tárcát ír a modern élet '
                                                                         'mulandó divatjairól.',
                                                              'english': 'The author writes a witty feuilleton about '
                                                                         'the fleeting fads of modern life.'},
                                                          {   'spanish': 'Az önirónia segít abban, hogy ne vegyük '
                                                                         'magunkat túlságosan komolyan.',
                                                              'english': 'Self-irony helps us not to take ourselves '
                                                                         'too seriously.'},
                                                          {   'spanish': 'A publicista csípős hangnemben élcelődött a '
                                                                         'bürokrácia tehetetlenségén.',
                                                              'english': 'The publicist bantered in a biting tone '
                                                                         'about the helplessness of bureaucracy.'},
                                                          {   'spanish': 'Pongrácz gróf alakja az illúziók költői '
                                                                         'emlékműve marad.',
                                                              'english': "Count Pongrácz's figure remains a poetic "
                                                                         'monument of illusions.'}],
                                          'tip': 'Restraint is key: do not use exclamation marks or overt signposts of '
                                                 "humor; let particles like 'hiszen', 'ugyebár', and 'alighanem' "
                                                 'establish the ironic mood.'},
                       'words': [   {'lemma': 'tárca', 'translation': 'feuilleton, newspaper column', 'pos': 'noun'},
                                    {'lemma': 'hangnem', 'translation': 'tone, register', 'pos': 'noun'},
                                    {'lemma': 'irónia', 'translation': 'irony', 'pos': 'noun'},
                                    {'lemma': 'önirónia', 'translation': 'self-irony, self-deprecation', 'pos': 'noun'},
                                    {   'lemma': 'élcelődik',
                                        'translation': 'to banter, joke sardonically',
                                        'pos': 'verb'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What is the meaning of 'önirónia'?",
                                                         'options': [   'self-irony / self-deprecation',
                                                                        'hatred of strangers',
                                                                        'blind admiration'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which literary genre blends conversational wit '
                                                                     'with philosophical social observation?',
                                                         'options': [   'tárca (feuilleton)',
                                                                        'hivatali körlevél',
                                                                        'szótári címszó'],
                                                         'correct': 0,
                                                         'teaches': ['b2-discourse-particles']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['tárca', 'feuilleton / column'],
                                                                           ['hangnem', 'tone / register'],
                                                                           ['irónia', 'irony'],
                                                                           ['önirónia', 'self-irony'],
                                                                           [   'élcelődik',
                                                                               'to banter / joke sardonically']],
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'A szerző barátságosan ____ a barátai apró '
                                                                          'gyengeségein. (banters)',
                                                              'answer': 'élcelődik',
                                                              'english': 'The author friendly banters about his '
                                                                         "friends' small weaknesses.",
                                                              'teaches': ['b2-discourse-particles']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A publicista szellemes ____ írt a szombati '
                                                                          'lap kulturális rovatába. (feuilleton)',
                                                              'answer': 'tárcát',
                                                              'english': 'The publicist wrote a witty feuilleton for '
                                                                         "the Saturday paper's cultural column.",
                                                              'teaches': ['b2-13-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence demonstrates a masterly '
                                                                          'ironic stance in a commentary?',
                                                              'options': [   'Hiszen ki vonhatná kétségbe, hogy a mi '
                                                                             'kisvárosunk a világ közepe?',
                                                                             'A kisváros lakossága ötezer fő a '
                                                                             'legfrissebb felmérés szerint.',
                                                                             'Tegnap esett az eső a kisváros főterén '
                                                                             'délután négykor.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-discourse-particles']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Az',
                                                                         'igazi',
                                                                         'irónia',
                                                                         'mindig',
                                                                         'társul',
                                                                         'egy',
                                                                         'adag',
                                                                         'öniróniával',
                                                                         '.'],
                                                            'solution': [   'Az',
                                                                            'igazi',
                                                                            'irónia',
                                                                            'mindig',
                                                                            'társul',
                                                                            'egy',
                                                                            'adag',
                                                                            'öniróniával',
                                                                            '.'],
                                                            'english': 'True irony is always coupled with a dose of '
                                                                       'self-irony.',
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A publicista fanyar hangnemben bírálta a '
                                                                             'döntést.',
                                                            'base_word': 'fanyar hangnemben',
                                                            'options': [   {   'word': 'finom iróniával',
                                                                               'inflected': 'finom iróniával',
                                                                               'sentence': 'A publicista finom '
                                                                                           'iróniával bírálta a '
                                                                                           'döntést.',
                                                                               'gloss': 'with subtle irony'},
                                                                           {   'word': 'cseppet sem kíméletesen',
                                                                               'inflected': 'cseppet sem kíméletesen',
                                                                               'sentence': 'A publicista cseppet sem '
                                                                                           'kíméletesen bírálta a '
                                                                                           'döntést.',
                                                                               'gloss': 'not in the least gently'}],
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A cikk csípős ____ azonnal felkeltette a '
                                                                        'szerkesztőség figyelmét. (tone)',
                                                            'answer': 'hangneme',
                                                            'english': "The article's biting tone immediately caught "
                                                                       "the editorial board's attention.",
                                                            'teaches': ['b2-13-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': 'How does Mikszáth achieve emotional depth at '
                                                                        'the conclusion of Beszterce ostroma?',
                                                            'options': [   'A komikus lovagi játék Apolka iránti '
                                                                           'tiszta szeretetté nemesül.',
                                                                           'Pongrácz gróf megöli az összes besztercei '
                                                                           'polgárt a csatában.',
                                                                           'A gróf bankot nyit és eladja a várat a '
                                                                           'városnak.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Egyetemista',
                                                                              'text': 'Miért olyan népszerű Mikszáth '
                                                                                      'Kálmán prózája a mai napig?'},
                                                                          {   'speaker': 'Irodalomtanár',
                                                                              'text': '_____'}],
                                                            'options': [   'Mert a páratlan mesélőkedv és a melegszívű '
                                                                           'irónia minden sorát áthatja.',
                                                                           'Mert kizárólag száraz statisztikai '
                                                                           'adatokat közölt a felvidéki falvakról.',
                                                                           'Mivel nem használt egyetlen metaforát sem '
                                                                           'a műveiben.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kezdő újságíró',
                                                                              'text': 'Hogyan érdemes megfogalmazni '
                                                                                      'egy ironikus bírálatot egy '
                                                                                      'kulturális lapban?'},
                                                                          {'speaker': 'Rovatvezető', 'text': '_____'}],
                                                            'options': [   'Kerülni kell a durva támadást; sokkal '
                                                                           'hatásosabb a finom célzás és a mértéktartó '
                                                                           'humor.',
                                                                           'Azonnal perrel kell fenyegetni az összes '
                                                                           'érintett személyt.',
                                                                           'Csak akkor szabad írni, ha a rendőrség '
                                                                           'előzetes engedélyt ad rá.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-discourse-particles']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write that the author writes '
                                                                                         'a witty feuilleton about the '
                                                                                         'vanity of modern life.',
                                                                               'answer': 'A szerző szellemes tárcát ír '
                                                                                         'a modern élet hiúságáról.'}],
                                                           'teaches': ['b2-discourse-particles']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write that self-irony helps '
                                                                                         'us see our own mistakes with '
                                                                                         'a smile.',
                                                                               'answer': 'Az önirónia segít abban, '
                                                                                         'hogy mosolyogva lássuk be a '
                                                                                         'saját hibáinkat.'}],
                                                           'teaches': ['b2-discourse-particles']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'élcelődik' mean?",
                                                         'options': [   'to banter / tease sardonically',
                                                                        'to weep bitterly',
                                                                        'to purchase goods'],
                                                         'correct': 0,
                                                         'teaches': ['b2-13-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A cikk írója alighanem túlzásba vitte az ____, '
                                                                     'így az olvasók félreértették a szándékát. '
                                                                     '(irony)',
                                                         'answer': 'iróniát',
                                                         'english': "The article's writer in all likelihood overdid "
                                                                    'the irony, so the readers misunderstood his '
                                                                    'intention.',
                                                         'teaches': ['b2-discourse-particles']}]}}],
    'consolidation': {   'goals': [   'I can use aligha, korántsem, and éppenséggel to navigate polite doubt and '
                                      'emphatic denial.',
                                      'I can signal shared premises and ironic complicity using hiszen and ugyebár.',
                                      'I can formulate litotes, hedged statements, and social satire in writing.'],
                         'exercises': [   {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': 'Which particle expresses that an assumption is far from '
                                                          'being true?',
                                              'options': ['korántsem', 'alighanem', 'mondhatni'],
                                              'correct': 0,
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'question': "What is the meaning of 'önirónia' in literary discourse?",
                                              'options': [   'self-deprecation / self-irony',
                                                             'open sarcasm against others',
                                                             'tragic despair'],
                                              'correct': 0,
                                              'teaches': ['b2-13-vocab']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': "What does 'aligha' express in B2 Hungarian prose?",
                                              'options': [   'high epistemic doubt / polite skepticism',
                                                             'absolute unconditional certainty',
                                                             'strict temporal sequence'],
                                              'correct': 0,
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'sentence': 'A bátor kritikus nyílt ____ illette a színház elavult '
                                                          'műsorpolitikáját. (critique)',
                                              'answer': 'bírálattal',
                                              'english': "The brave critic leveled an open critique at the theater's "
                                                         'outdated programming.',
                                              'teaches': ['b2-13-vocab']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': 'Nem kell aggódnod, a helyzet ____ olyan kétségbeejtő, mint '
                                                          'hiszed. (by no means)',
                                              'answer': 'korántsem',
                                              'english': "You don't need to worry, the situation is by no means as "
                                                         'desperate as you think.',
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': 'Miért kételkedsz, ____ a saját szemeddel láttad a '
                                                          'bizonyítékot? (after all)',
                                              'answer': 'hiszen',
                                              'english': 'Why do you doubt it, after all, you saw the evidence with '
                                                         'your own eyes?',
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'prompt': [   {   'speaker': 'Polgár',
                                                                'text': 'Szerinted megvalósul valaha a gróf merész '
                                                                        'terve?'},
                                                            {'speaker': 'Bíró', 'text': '_____'}],
                                              'options': [   'Aligha, hiszen a modern törvények nem engedik a '
                                                             'magánhadseregek működését.',
                                                             'Igen, mert tegnap már felépült a harmadik bástya a '
                                                             'réten.',
                                                             'Nem, mert senki sem tudott magyarul a városban.'],
                                              'correct': 0,
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'question': 'Which sentence illustrates litotes (ironic understatement)?',
                                              'options': [   'A tegnapi fogadás nem éppen a szerénység mintaképe volt.',
                                                             'A tegnapi fogadás rendkívül zajos volt.',
                                                             'A fogadásra senki sem ment el a faluból.'],
                                              'correct': 0,
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'in-context',
                                              'question': 'Which adjective describes a person who pretends to possess '
                                                          'moral virtues they lack?',
                                              'options': ['képmutató', 'fanyar', 'tárgyilagos'],
                                              'correct': 0,
                                              'teaches': ['b2-13-vocab']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'A',
                                                           'gróf',
                                                           'szeszélyei',
                                                           'mögött',
                                                           'cseppet',
                                                           'sem',
                                                           'lakozott',
                                                           'gonoszság',
                                                           '.'],
                                              'solution': [   'A',
                                                              'gróf',
                                                              'szeszélyei',
                                                              'mögött',
                                                              'cseppet',
                                                              'sem',
                                                              'lakozott',
                                                              'gonoszság',
                                                              '.'],
                                              'english': "Behind the count's whims there resided not the least "
                                                         'wickedness.',
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'A',
                                                           'lovagi',
                                                           'játék',
                                                           'végül',
                                                           'mégiscsak',
                                                           'őszinte',
                                                           'szeretetté',
                                                           'vált',
                                                           '.'],
                                              'solution': [   'A',
                                                              'lovagi',
                                                              'játék',
                                                              'végül',
                                                              'mégiscsak',
                                                              'őszinte',
                                                              'szeretetté',
                                                              'vált',
                                                              '.'],
                                              'english': 'The chivalric game ultimately became, after all, sincere '
                                                         'love.',
                                              'teaches': ['b2-discourse-particles']},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'template': [   {   'prompt': 'Write: True satire unmasks hypocrisy not '
                                                                            'with hatred, but with wise irony.',
                                                                  'answer': 'Az igazi szatíra nem gyűlölettel, hanem '
                                                                            'bölcs iróniával leplezi le az '
                                                                            'álszentséget.'}],
                                              'teaches': ['b2-discourse-particles']}]}}


# ============================================================================== #
# UNIT 14: Visual Storytelling, Perspective & Time (b2-14)
# ============================================================================== #
UNIT_14 = {   'unit_num': 14,
    'title': 'Visual Storytelling, Perspective & Time',
    'grammar_summary': 'Conjunctions of simultaneity, immediate sequence, duration, and iterative temporal framing: '
                       'amint, mihelyt, alighogy... máris, miközben, mialatt, eközben, valahányszor, ahányszor csak, '
                       'and amióta csak; narrative pacing and visual montage in Hungarian prose and critical reviews.',
    'grammar_skill': 'b2-simultaneity-conjunctions',
    'vocab_skill': 'b2-14-vocab',
    'theme': 'Visual storytelling, pacing and cinema',
    'intro_body': [   'Narrative pacing in Hungarian prose and film criticism depends on sophisticated temporal '
                      'conjunctions that establish parallel actions (miközben, mialatt), immediate succession (amint, '
                      'mihelyt, alighogy... máris), and recurrent cinematic rhythms (valahányszor, ahányszor csak).',
                      "Through Miklós Mészöly's stark existential masterpiece Magasiskola (1967)—adapted for cinema by "
                      'István Gaál—you will explore how visual focus, spatial geometry, and the cold discipline of '
                      'falconry on the Hungarian plain serve as a powerful allegory of power, obedience, and '
                      'observation.'],
    'classic_story': {   'slug': 'magasiskola',
                         'author': 'Mészöly Miklós',
                         'work': 'Magasiskola (1967)',
                         'title': 'A sólyomröptetés és a távlat fegyelme',
                         'summary': 'A végtelen puszta közepén fekvő elszigetelt sólyomtelepen a fiatal narrátor a '
                                    'madarak idomításának szigorú, hallgatag rendjét figyeli; Lilik, a solymászmester '
                                    'mozdulatai mögött felsejlik a hatalom, a fegyelem és a szabadság rideg, mégis '
                                    'lenyűgöző parabolája.',
                         'characters': ['A narrátor', 'Lilik'],
                         'paragraphs': [   {   'type': 'narration',
                                               'text': 'A puszta peremén álló sólyomtelep felett az égbolt oly '
                                                       'tágasnak és mozdulatlannak tetszett, mintha a távlat maga '
                                                       'volna az idő egyetlen mérője. Amint megérkeztem a '
                                                       'deszkakerítéssel körülvett barakkokhoz, azonnal megcsapott a '
                                                       'ragadozó madarak éles szaga és a telepet uraló különös, '
                                                       'feszült csend.'},
                                           {   'type': 'narration',
                                               'text': 'Lilik, a telep vezetője, szótlanul fogadott. Mihelyt kezet '
                                                       'ráztunk, tekintetét máris a dúcok felé fordította, ahol a '
                                                       'vándorsólymok és kerecsenek ültek a bőrrel bevont ülőfákon. '
                                                       'Alighogy beléptem az udvarra, máris éreztem, hogy itt minden '
                                                       'emberi mozdulat a madarak ösztöneihez igazodik.'},
                                           {   'type': 'narration',
                                               'text': 'A délelőtti órákban kezdetét vette a fegyelmezett munka. '
                                                       'Miközben Lilik vastag bőrhuzatú kesztyűjét felhúzta, a madarak '
                                                       'türelmetlenül verdesni kezdtek a szárnyukkal, mialatt a segéd '
                                                       'a csalétket készítette elő a tágas rét szélén. Eközben én a '
                                                       'kerítés mellől figyeltem a készülődés kimért ritmusát.'},
                                           {   'type': 'narration',
                                               'text': 'Amint a sólyom elhagyta a mester öklét, hirtelen elnémult '
                                                       'minden zaj a mezőn. A madár meredeken tört a magasba, miközben '
                                                       'a tekintetünk alig tudta követni a fenséges ívben emelkedő '
                                                       'árnyékot. Lilik mozdulatlanul állt a szélben, mintha '
                                                       'láthatatlan szállal irányítaná a ragadozó repülését.'},
                                           {   'type': 'narration',
                                               'text': 'Valahányszor a sólyom elérte a kívánt magasságot, a telepen '
                                                       'tartózkodók lélegzete is elakadt. Ahányszor csak lecsapott a '
                                                       'zsákmányra, a zuhanás pontossága egyszerre keltett csodálatot '
                                                       'és dermesztő félelmet a szemlélőben; a természet kegyetlen '
                                                       'tisztasága mutatkozott meg a nyers sebességben.'},
                                           {   'type': 'narration',
                                               'text': 'Mihelyt a madár visszaért a kesztyűre, Lilik azonnal ráhúzta a '
                                                       'szemellenzőt. A vad lény egyetlen pillanat alatt visszavedlett '
                                                       'szelíd, vak rabmadárrá. Miközben a mester a húscafattal '
                                                       'jutalmazta az állatot, én a látvány mélyebb allegóriáján '
                                                       'tűnődtem: vajon a rend és az engedelmesség mindig a látás '
                                                       'korlátozásával érhető el?'},
                                           {   'type': 'narration',
                                               'text': 'Amióta csak a telepen tartózkodtam, nem tudtam szabadulni '
                                                       'ettől a kettős érzéstől. A madarak röpte a határtalan '
                                                       'szabadságot jelképezte, miközben a telep fegyelme a tökéletes '
                                                       'alávetettség mintája volt. A narrátor szeme előtt a pusztai '
                                                       'solymászat az emberi társadalom hatalmi szerkezetének '
                                                       'félelmetes tükrévé vált.'},
                                           {   'type': 'narration',
                                               'text': 'Mészöly kisregénye a modern magyar próza egyik csúcspontja, '
                                                       'amelyben a vizuális ábrázolás pontossága filozófiai mélységgel '
                                                       'párosul. A távlat tiszta vonalai, a mozgás és a mozdulatlanság '
                                                       'ellentéte minduntalan arra figyelmeztet, hogy a fegyelem rideg '
                                                       'mechanizmusa mögött az emberi szabadság törékeny sorsa forog '
                                                       'kockán.'}],
                         'reading_questions': [   {   'question': 'Milyen hangulat és környezet fogadta a narrátort a '
                                                                  'sólyomtelepre érkezésekor?',
                                                      'options': [   'Tágas égbolt, éles madárszag és feszült csend '
                                                                     'uralta a deszkabarakkokat.',
                                                                     'Hangos zene és vidám vásári forgatag várta a '
                                                                     'látogatókat.',
                                                                     'Sűrű erdő és elhagyatott, romos kastély vette '
                                                                     'körül az udvart.'],
                                                      'correct': 0},
                                                  {   'question': 'Mit tett Lilik, mihelyt a sólyom visszatért a '
                                                                  'vadászatból a kesztyűjére?',
                                                      'options': [   'Azonnal ráhúzta a szemellenzőt a madár fejére, '
                                                                     'miközben hússal jutalmazta.',
                                                                     'Szabadon engedte a madarat, hogy örökre a '
                                                                     'pusztán éljen.',
                                                                     'Elkergette a segédet, mert elrontotta a csalétek '
                                                                     'előkészítését.'],
                                                      'correct': 0},
                                                  {   'question': 'Milyen filozófiai felismerésre jutott a narrátor a '
                                                                  'sólyomröptetés megfigyelése közben?',
                                                      'options': [   'A sólyomkiképzés a hatalom, az alávetettség és a '
                                                                     'fegyelem rideg allegóriája.',
                                                                     'A ragadozó madarak kizárólag szórakozási célt '
                                                                     'szolgálnak a pusztán.',
                                                                     'A solymászat haszontalan mesterség a modern '
                                                                     'mezőgazdaság szempontjából.'],
                                                      'correct': 0}]},
    'lessons': [   {   'num': 1,
                       'title': 'The Moment That: Immediate Sequence (amint, mihelyt)',
                       'grammar_label': 'Immediate succession conjunctions: amint, mihelyt, alighogy ... máris',
                       'goals': [   'I can link sudden sequential actions using amint and mihelyt.',
                                    'I can express immediate, instantaneous succession with alighogy ... máris.',
                                    'I can maintain correct focus word order in temporal subordinate clauses.'],
                       'grammar_doc': {   'slug': 'immediate-sequence-conjunctions',
                                          'title': 'Immediate Succession: amint, mihelyt, and alighogy ... máris',
                                          'text1_title': "Punctual Triggers: 'amint' and 'mihelyt'",
                                          'text1': "Both 'amint' and 'mihelyt' translate 'as soon as' or 'the moment "
                                                   "that', introducing a temporal subordinate clause that immediately "
                                                   "triggers the action in the main clause. While 'amint' is neutral "
                                                   'and stylistically versatile across formal and literary registers, '
                                                   "'mihelyt' places sharper focus on the instantaneousness of the "
                                                   "temporal trigger: 'Mihelyt földet ért, azonnal ráugrott a "
                                                   "zsákmányra.'",
                                          'text2_title': "Overlapping Boundaries with 'alighogy ... máris'",
                                          'text2': "'Alighogy' (scarcely / no sooner) followed by 'máris' (already) in "
                                                   'the main clause captures two events that follow each other in a '
                                                   "flash, almost overlapping: 'Alighogy elhangzott a parancs, a segéd "
                                                   "máris elindult.' The clause introduced by 'alighogy' typically "
                                                   'puts the conjugated verb in the focus position immediately after '
                                                   'the conjunction.',
                                          'table_title': 'Immediate Succession Conjunctions',
                                          'table_rows': [   [   'amint + clause',
                                                                'as soon as / the moment that (neutral immediate '
                                                                'sequence)'],
                                                            [   'mihelyt + clause',
                                                                'the moment that / as soon as (punctual immediate '
                                                                'trigger)'],
                                                            [   'alighogy + verb ..., máris ...',
                                                                'scarcely had ... when already ... (instantaneous '
                                                                'succession)'],
                                                            [   'amint lehet',
                                                                'as soon as possible (idiomatic fixed expression)']],
                                          'examples': [   {   'spanish': 'Amint megérkeztem a telepre, azonnal '
                                                                         'megcsapott a feszült csend.',
                                                              'english': 'As soon as I arrived at the station, the '
                                                                         'tense silence immediately struck me.'},
                                                          {   'spanish': 'Mihelyt kinyílt a kapu, a vadászok kiléptek '
                                                                         'a ködös pusztára.',
                                                              'english': 'The moment the gate opened, the hunters '
                                                                         'stepped out onto the foggy plain.'},
                                                          {   'spanish': 'Alighogy felszállt a sólyom, máris fenséges '
                                                                         'ívben emelkedett a magasba.',
                                                              'english': 'Scarcely had the falcon taken flight when '
                                                                         'already it rose in a majestic arc.'},
                                                          {   'spanish': 'A solymász egyetlen pillantással felmérte a '
                                                                         'madár állapotát.',
                                                              'english': "The falconer assessed the bird's condition "
                                                                         'with a single glance.'}],
                                          'tip': "Always place a comma before 'amint' and 'mihelyt' when they "
                                                 'introduce a subordinate clause, even if the clause comes first: '
                                                 "'Amint vége a jelenetnek, felkapcsolják a fényt.'"},
                       'words': [   {   'lemma': 'amint',
                                        'translation': 'as soon as, the moment that',
                                        'pos': 'conjunction'},
                                    {   'lemma': 'mihelyt',
                                        'translation': 'the moment that, as soon as',
                                        'pos': 'conjunction'},
                                    {'lemma': 'alighogy', 'translation': 'scarcely, no sooner', 'pos': 'conjunction'},
                                    {'lemma': 'pillantás', 'translation': 'glance, look', 'pos': 'noun'},
                                    {'lemma': 'reagál', 'translation': 'to react, respond', 'pos': 'verb'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the Hungarian noun 'pillantás' mean?",
                                                         'options': ['glance / look', 'deep sleep', 'feathered wing'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which conjunction introduces an immediate '
                                                                     "temporal sequence ('as soon as / the moment "
                                                                     "that')?",
                                                         'options': ['amint', 'habár', 'mialatt'],
                                                         'correct': 0,
                                                         'teaches': ['b2-simultaneity-conjunctions']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['amint', 'as soon as'],
                                                                           ['mihelyt', 'the moment that'],
                                                                           ['alighogy', 'scarcely / no sooner'],
                                                                           ['pillantás', 'glance / look'],
                                                                           ['reagál', 'to react / respond']],
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': '____ belépett a barakkba, azonnal érezte a '
                                                                          'feszültséget. (as soon as)',
                                                              'answer': 'Amint',
                                                              'english': 'As soon as he entered the barrack, he '
                                                                         'immediately felt the tension.',
                                                              'teaches': ['b2-simultaneity-conjunctions']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A solymász egyetlen éles ____ mérte fel a '
                                                                          'madár állapotát. (glance)',
                                                              'answer': 'pillantással',
                                                              'english': "The falconer assessed the bird's condition "
                                                                         'with a single sharp glance.',
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which pair expresses that one action '
                                                                          'happens immediately and overlappingly after '
                                                                          'another?',
                                                              'options': [   'alighogy ... máris',
                                                                             'noha ... mégis',
                                                                             'jóllehet ... mindeddig'],
                                                              'correct': 0,
                                                              'teaches': ['b2-simultaneity-conjunctions']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Alighogy',
                                                                         'felszállt',
                                                                         'a',
                                                                         'sólyom,',
                                                                         'máris',
                                                                         'lecsapott',
                                                                         'a',
                                                                         'zsákmányra',
                                                                         '.'],
                                                            'solution': [   'Alighogy',
                                                                            'felszállt',
                                                                            'a',
                                                                            'sólyom,',
                                                                            'máris',
                                                                            'lecsapott',
                                                                            'a',
                                                                            'zsákmányra',
                                                                            '.'],
                                                            'english': 'Scarcely had the falcon taken flight when '
                                                                       'already it struck the prey.',
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Amint véget ért a bemutató, a közönség '
                                                                             'tapsolni kezdett.',
                                                            'base_word': 'Amint',
                                                            'options': [   {   'word': 'mihelyt',
                                                                               'inflected': 'Mihelyt',
                                                                               'sentence': 'Mihelyt véget ért a '
                                                                                           'bemutató, a közönség '
                                                                                           'tapsolni kezdett.',
                                                                               'gloss': 'the moment that'},
                                                                           {   'word': 'alighogy',
                                                                               'inflected': 'Alighogy',
                                                                               'sentence': 'Alighogy véget ért a '
                                                                                           'bemutató, a közönség '
                                                                                           'tapsolni kezdett.',
                                                                               'gloss': 'no sooner'}],
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A ragadozó madár azonnal ____ a legkisebb '
                                                                        'zörejre is a fűben. (reacts)',
                                                            'answer': 'reagál',
                                                            'english': 'The bird of prey reacts immediately to even '
                                                                       'the slightest noise in the grass.',
                                                            'teaches': ['b2-14-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "Which sentence correctly uses 'mihelyt' in "
                                                                        'standard B2 register?',
                                                            'options': [   'Mihelyt megjelent a mester az udvaron, a '
                                                                           'segédek fegyelmezetten munkához láttak.',
                                                                           'Mihelyt megjelent a mester az udvaron, bár '
                                                                           'senki sem volt ott.',
                                                                           'A segédek munkához láttak, mihelyt a nap '
                                                                           'tegnap lement a hegyek mögé.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kutató',
                                                                              'text': 'Mikor engedhetjük szabadon a '
                                                                                      'fiatal sólymot a pusztán?'},
                                                                          {   'speaker': 'Solymászmester',
                                                                              'text': '_____'}],
                                                            'options': [   'Mihelyt megszokja a kesztyű érintését és a '
                                                                           'sípszó jelzéseit.',
                                                                           'Tegnap reggel, mert a kapuk már nyitva '
                                                                           'álltak a faluban.',
                                                                           'Amikor a színházban felkapcsolják a '
                                                                           'lámpákat a szünetben.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Néző',
                                                                              'text': 'Hogyan reagált a közönség a '
                                                                                      'feszült jelenet kezdetén?'},
                                                                          {'speaker': 'Rendező', 'text': '_____'}],
                                                            'options': [   'Alighogy megcsendült a fegyver hangja, '
                                                                           'máris feszült csend támadt a teremben.',
                                                                           'Mert a vonat késett harminc percet a vihar '
                                                                           'miatt.',
                                                                           'Igen, hiszen a vetítőgépész hazament '
                                                                           'aludni a szünetben.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: As soon as the falcon '
                                                                                         'returns to the glove, the '
                                                                                         'master puts on the hood.',
                                                                               'answer': 'Amint a sólyom visszatér a '
                                                                                         'kesztyűre, a mester ráhúzza '
                                                                                         'a szemellenzőt.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Scarcely had the '
                                                                                         'director called action, the '
                                                                                         'actor immediately reacted.',
                                                                               'answer': 'Alighogy a rendező intett, a '
                                                                                         'színész máris reagált.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the verb 'reagál' mean?",
                                                         'options': [   'to react / respond',
                                                                        'to sleep deeply',
                                                                        'to paint a canvas'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': '____ elcsitult a szél a pusztán, a vadászok '
                                                                     'azonnal útnak indultak. (the moment that)',
                                                         'answer': 'Mihelyt',
                                                         'english': 'The moment the wind died down on the plain, the '
                                                                    'hunters immediately set off.',
                                                         'teaches': ['b2-simultaneity-conjunctions']}]}},
                   {   'num': 2,
                       'title': 'Long Takes: Simultaneity and Duration (miközben, mialatt)',
                       'grammar_label': 'Simultaneity and parallel duration: miközben, mialatt, eközben',
                       'goals': [   'I can depict simultaneous actions unfolding in parallel using miközben and '
                                    'mialatt.',
                                    'I can contrast subordinate clauses (miközben) with coordinating discourse adverbs '
                                    '(eközben).',
                                    'I can describe cinematic scenes with multiple layers of foreground and background '
                                    'action.'],
                       'grammar_doc': {   'slug': 'simultaneity-parallel-duration',
                                          'title': 'Simultaneous Duration: miközben, mialatt, and eközben',
                                          'text1_title': "Parallel Action with Subordinate 'miközben' and 'mialatt'",
                                          'text1': "Hungarian uses 'miközben' (while / in the course of) and 'mialatt' "
                                                   '(during the time that / while) to link two events occurring '
                                                   "simultaneously. 'Miközben' emphasizes concurrent activity, often "
                                                   "setting a background action against a foreground event: 'A madár "
                                                   "körözött, miközben a solymász lentről figyelte.' 'Mialatt' "
                                                   'highlights the span of elapsed time throughout which the action '
                                                   'continues.',
                                          'text2_title': "Independent Discourse Sequencing with 'eközben'",
                                          'text2': "'Eközben' is an adverb meaning 'meanwhile / in the meantime'. "
                                                   "Unlike 'miközben', it does not introduce a subordinate clause; "
                                                   "instead, it starts a new independent clause or sentence: 'A "
                                                   'solymász a madarat etette. Eközben a narrátor a füzetébe '
                                                   "jegyzetelt.' In film analysis, 'eközben' establishes cross-cutting "
                                                   'between two parallel scenes.',
                                          'table_title': 'Simultaneity Markers at B2',
                                          'table_rows': [   [   'miközben + clause',
                                                                'while / in the course of (concurrent parallel '
                                                                'action)'],
                                                            [   'mialatt + clause',
                                                                'during the time that / while (emphasis on elapsed '
                                                                'duration)'],
                                                            [   'eközben (sentence-initial)',
                                                                'meanwhile / in the meantime (independent discourse '
                                                                'adverb)'],
                                                            [   'párhuzamos cselekmény',
                                                                'parallel storyline / concurrent action']],
                                          'examples': [   {   'spanish': 'Miközben a kamera lassan mozgott, a zene '
                                                                         'fokozta a feszültséget.',
                                                              'english': 'While the camera moved slowly, the music '
                                                                         'heightened the tension.'},
                                                          {   'spanish': 'Mialatt a segéd a húst vágta, a narrátor a '
                                                                         'dúcokat vizsgálta.',
                                                              'english': 'While the assistant was cutting the meat, '
                                                                         'the narrator examined the roosts.'},
                                                          {   'spanish': 'Lilik a mezőn gyakorolt; eközben a telepen '
                                                                         'csend honolt.',
                                                              'english': 'Lilik was practicing in the field; '
                                                                         'meanwhile, silence reigned at the station.'},
                                                          {   'spanish': 'A festmény sötét háttere még élesebben '
                                                                         'kiemeli a főalakot.',
                                                              'english': "The painting's dark background highlights "
                                                                         'the main figure even more sharply.'}],
                                          'tip': "Distinguish grammar clearly: 'miközben' requires a comma before it "
                                                 "as a conjunction, while 'eközben' begins an independent sentence or "
                                                 'follows a semicolon.'},
                       'words': [   {   'lemma': 'miközben',
                                        'translation': 'while, in the course of',
                                        'pos': 'conjunction'},
                                    {   'lemma': 'mialatt',
                                        'translation': 'during the time that, while',
                                        'pos': 'conjunction'},
                                    {'lemma': 'eközben', 'translation': 'meanwhile, in the meantime', 'pos': 'adverb'},
                                    {'lemma': 'háttér', 'translation': 'background, setting', 'pos': 'noun'},
                                    {'lemma': 'párhuzamos', 'translation': 'parallel, concurrent', 'pos': 'adjective'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the adjective 'párhuzamos' mean?",
                                                         'options': [   'parallel / concurrent',
                                                                        'circular and endless',
                                                                        'suddenly interrupted'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which word is a subordinating conjunction '
                                                                     'connecting two simultaneous actions?',
                                                         'options': ['miközben', 'eközben', 'aligha'],
                                                         'correct': 0,
                                                         'teaches': ['b2-simultaneity-conjunctions']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['miközben', 'while / in the course of'],
                                                                           ['mialatt', 'during the time that'],
                                                                           ['eközben', 'meanwhile / in the meantime'],
                                                                           ['háttér', 'background / setting'],
                                                                           ['párhuzamos', 'parallel / concurrent']],
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'A madár a felhők alatt körözött, ____ a '
                                                                          'solymász lentről figyelte mozgását. (while)',
                                                              'answer': 'miközben',
                                                              'english': 'The bird circled beneath the clouds, while '
                                                                         'the falconer watched its movement from '
                                                                         'below.',
                                                              'teaches': ['b2-simultaneity-conjunctions']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A dráma komor történelmi ____ még élesebben '
                                                                          'kiemeli a személyes tragédiát. (background)',
                                                              'answer': 'háttere',
                                                              'english': "The drama's somber historical background "
                                                                         'highlights the personal tragedy even more '
                                                                         'sharply.',
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': "Select the sentence using 'eközben' as an "
                                                                          'independent coordinating adverb:',
                                                              'options': [   'A rendező a színészekkel próbált. '
                                                                             'Eközben az operatőr a fényeket állította '
                                                                             'be.',
                                                                             'A rendező próbált, eközben az eső '
                                                                             'szakadni kezdett a tetőre.',
                                                                             'Eközben megérkezett a vonat, mindenki '
                                                                             'hazament.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-simultaneity-conjunctions']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Miközben',
                                                                         'a',
                                                                         'kamera',
                                                                         'lassan',
                                                                         'mozgott,',
                                                                         'a',
                                                                         'zene',
                                                                         'fokozta',
                                                                         'a',
                                                                         'feszültséget',
                                                                         '.'],
                                                            'solution': [   'Miközben',
                                                                            'a',
                                                                            'kamera',
                                                                            'lassan',
                                                                            'mozgott,',
                                                                            'a',
                                                                            'zene',
                                                                            'fokozta',
                                                                            'a',
                                                                            'feszültséget',
                                                                            '.'],
                                                            'english': 'While the camera moved slowly, the music '
                                                                       'heightened the tension.',
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Mialatt a segéd a húst vágta, a narrátor '
                                                                             'a dúcokat vizsgálta.',
                                                            'base_word': 'Mialatt',
                                                            'options': [   {   'word': 'miközben',
                                                                               'inflected': 'Miközben',
                                                                               'sentence': 'Miközben a segéd a húst '
                                                                                           'vágta, a narrátor a '
                                                                                           'dúcokat vizsgálta.',
                                                                               'gloss': 'while'},
                                                                           {   'word': 'amint',
                                                                               'inflected': 'Amint',
                                                                               'sentence': 'Amint a segéd a húst '
                                                                                           'vágta, a narrátor a '
                                                                                           'dúcokat vizsgálta.',
                                                                               'gloss': 'as soon as'}],
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A film két ____ történetszálat követ '
                                                                        'párhuzamosan a háború éveiben. (parallel)',
                                                            'answer': 'párhuzamos',
                                                            'english': 'The film follows two parallel storylines '
                                                                       'concurrently during the war years.',
                                                            'teaches': ['b2-14-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': 'What is the syntactic difference between '
                                                                        "'miközben' and 'eközben'?",
                                                            'options': [   "A 'miközben' kötőszó mellékmondatot vezet "
                                                                           "be, míg az 'eközben' önálló mondatkezdő "
                                                                           'határozószó.',
                                                                           'Nincs semmilyen különbség, mindkettő '
                                                                           'igekötő.',
                                                                           "A 'miközben' csak jövő időben, az "
                                                                           "'eközben' csak múlt időben állhat."],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Filmesztéta',
                                                                              'text': 'Hogyan épül fel a Magasiskola '
                                                                                      'híres nyitójelenete?'},
                                                                          {'speaker': 'Kritikus', 'text': '_____'}],
                                                            'options': [   'A kamera a pusztát pásztázza, miközben '
                                                                           'halk, feszült zúgás hallatszik a távolból.',
                                                                           'Mert a vetítővászon elszakadt a film '
                                                                           'harmadik percében a moziban.',
                                                                           'Alighogy felkapcsolták a lámpát a teremben '
                                                                           'tegnap este.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Látogató',
                                                                              'text': 'Mit csinált a solymászsegéd a '
                                                                                      'madarak röptetése alatt?'},
                                                                          {'speaker': 'Narrátor', 'text': '_____'}],
                                                            'options': [   'A csalétekkel futott a réten, mialatt a '
                                                                           'mester szigorú pillantással követte a '
                                                                           'sólyom ívét.',
                                                                           'Hazament a szomszéd faluba, mert nem '
                                                                           'szerette a madarakat.',
                                                                           'Mihelyt lecsukta a szemét, azonnal elaludt '
                                                                           'a fűben délután.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: While the narrator '
                                                                                         'observes the birds, he '
                                                                                         'reflects on the nature of '
                                                                                         'authority.',
                                                                               'answer': 'Miközben a narrátor a '
                                                                                         'madarakat figyeli, a hatalom '
                                                                                         'természetén töpreng.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The master trained '
                                                                                         'the falcon; meanwhile, the '
                                                                                         'assistant prepared the '
                                                                                         'field.',
                                                                               'answer': 'A mester a sólymot '
                                                                                         'idomította; eközben a segéd '
                                                                                         'előkészítette a mezőt.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'háttér' mean in cinematography and "
                                                                     'literary description?',
                                                         'options': [   'background / setting',
                                                                        'front row seating',
                                                                        'sharp hunting weapon'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'Mindenki csendben figyelt a teremben, ____ a '
                                                                     'megrázó képsorok peregtek a vásznon. (while)',
                                                         'answer': 'mialatt',
                                                         'english': 'Everyone watched in silence in the room while the '
                                                                    'moving footage rolled on screen.',
                                                         'teaches': ['b2-simultaneity-conjunctions']}]}},
                   {   'num': 3,
                       'title': 'Framing, Pacing, and Atmosphere',
                       'grammar_label': 'Iterative temporal framing: valahányszor, ahányszor csak, amióta csak',
                       'goals': [   'I can describe recurring visual motifs using valahányszor and ahányszor csak.',
                                    'I can express unbroken duration from an initial starting point with amióta csak.',
                                    'I can analyze cinematic pacing and atmospheric tension in Hungarian prose.'],
                       'grammar_doc': {   'slug': 'iterative-temporal-framing',
                                          'title': 'Iterative and Continuous Framing: valahányszor, ahányszor csak, '
                                                   'amióta',
                                          'text1_title': "Recurring Cycles with 'valahányszor' and 'ahányszor csak'",
                                          'text1': "'Valahányszor' (whenever / every single time that) and 'ahányszor "
                                                   "csak' (as often as / whenever) establish iterative rhythms and "
                                                   "leitmotifs in narrative. Adding the emphatic particle 'csak' "
                                                   "intensifies the universality of the condition: 'Ahányszor csak "
                                                   "felszállt a madár, a telepen elnémult mindenki.'",
                                          'text2_title': "Continuous Pacing with 'amióta csak'",
                                          'text2': "'Amióta' (ever since) with optional 'csak' sets an unbroken "
                                                   "continuum of experience starting from a pivotal event: 'Amióta "
                                                   'csak a telepre érkezett, nem tudott szabadulni a fegyelem '
                                                   "nyomasztó érzésétől.' In visual analysis, it anchors the "
                                                   'psychological transformation of a character.',
                                          'table_title': 'Iterative and Continuous Conjunctions',
                                          'table_rows': [   [   'valahányszor + clause',
                                                                'whenever / each time that (cyclical recurring '
                                                                'events)'],
                                                            [   'ahányszor csak + clause',
                                                                'as often as / every single time (emphatic iterative)'],
                                                            [   'amióta csak + clause',
                                                                'ever since (continuous state from an initial turning '
                                                                'point)'],
                                                            [   'belső feszültség',
                                                                'internal tension / psychological suspense']],
                                          'examples': [   {   'spanish': 'Valahányszor a sólyom elhagyta az öklöt, '
                                                                         'megállt a levegő a puszta felett.',
                                                              'english': 'Whenever the falcon left the fist, the air '
                                                                         'stood still above the plain.'},
                                                          {   'spanish': 'Ahányszor csak lecsapott a ragadozó, a '
                                                                         'zuhanás pontossága lenyűgözte a szemlélőt.',
                                                              'english': 'As often as the predator struck, the '
                                                                         'precision of the dive captivated the '
                                                                         'observer.'},
                                                          {   'spanish': 'Amióta csak a telepen él, a solymászat rideg '
                                                                         'törvényeit követi.',
                                                              'english': 'Ever since he has lived at the station, he '
                                                                         'follows the cold laws of falconry.'},
                                                          {   'spanish': 'A képek kimért ritmusa mély belső '
                                                                         'feszültséget keltett a nézőben.',
                                                              'english': 'The measured rhythm of the images created '
                                                                         'deep internal tension in the viewer.'}],
                                          'tip': "Pair 'valahányszor' with iterative verb forms (pl. 'figyelget', "
                                                 "'körözget') to evoke repeated rhythmic actions."},
                       'words': [   {   'lemma': 'valahányszor',
                                        'translation': 'whenever, every time that',
                                        'pos': 'conjunction'},
                                    {   'lemma': 'ahányszor',
                                        'translation': 'as often as, whenever',
                                        'pos': 'conjunction'},
                                    {'lemma': 'amióta', 'translation': 'ever since', 'pos': 'conjunction'},
                                    {'lemma': 'feszültség', 'translation': 'tension, suspense', 'pos': 'noun'},
                                    {'lemma': 'ritmus', 'translation': 'rhythm, pace', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the noun 'feszültség' mean in literary "
                                                                     'and cinematic analysis?',
                                                         'options': [   'tension / suspense',
                                                                        'comic relief',
                                                                        'unimportant background'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which conjunction introduces an iterative '
                                                                     "condition meaning 'every single time that'?",
                                                         'options': ['valahányszor', 'mialatt', 'noha'],
                                                         'correct': 0,
                                                         'teaches': ['b2-simultaneity-conjunctions']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['valahányszor', 'whenever / every time'],
                                                                           ['ahányszor', 'as often as'],
                                                                           ['amióta', 'ever since'],
                                                                           ['feszültség', 'tension / suspense'],
                                                                           ['ritmus', 'rhythm / pace']],
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': '____ a sólyom elhagyta az öklöt, a levegő '
                                                                          'megdermedt a puszta felett. (whenever)',
                                                              'answer': 'Valahányszor',
                                                              'english': 'Whenever the falcon left the fist, the air '
                                                                         'froze over the plain.',
                                                              'teaches': ['b2-simultaneity-conjunctions']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A film lassú, kimért ____ a nézőt is '
                                                                          'feszült figyelemre készteti. (rhythm)',
                                                              'answer': 'ritmusa',
                                                              'english': "The film's slow, measured rhythm compels the "
                                                                         'viewer to tense attention as well.',
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence emphasizes an unbroken '
                                                                          'continuous state from a past starting '
                                                                          'point?',
                                                              'options': [   'Amióta csak a telepen él, nem látott más '
                                                                             'embert a solymászon kívül.',
                                                                             'Amint megérkezett a telepre, azonnal '
                                                                             'aludni tért a szobájában.',
                                                                             'Miközben a telepen élt, sokat sétált a '
                                                                             'közeli faluban.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-simultaneity-conjunctions']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Ahányszor',
                                                                         'csak',
                                                                         'lecsapott',
                                                                         'a',
                                                                         'ragadozó,',
                                                                         'mindig',
                                                                         'célba',
                                                                         'ért',
                                                                         '.'],
                                                            'solution': [   'Ahányszor',
                                                                            'csak',
                                                                            'lecsapott',
                                                                            'a',
                                                                            'ragadozó,',
                                                                            'mindig',
                                                                            'célba',
                                                                            'ért',
                                                                            '.'],
                                                            'english': 'As often as the predator struck, it always '
                                                                       'reached its mark.',
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Valahányszor megszólalt a síp, a madarak '
                                                                             'megriadtak a telepen.',
                                                            'base_word': 'Valahányszor',
                                                            'options': [   {   'word': 'ahányszor csak',
                                                                               'inflected': 'Ahányszor csak',
                                                                               'sentence': 'Ahányszor csak megszólalt '
                                                                                           'a síp, a madarak '
                                                                                           'megriadtak a telepen.',
                                                                               'gloss': 'as often as'},
                                                                           {   'word': 'amint',
                                                                               'inflected': 'Amint',
                                                                               'sentence': 'Amint megszólalt a síp, a '
                                                                                           'madarak megriadtak a '
                                                                                           'telepen.',
                                                                               'gloss': 'as soon as'}],
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A drámai jelenetben a kimondatlan szavak '
                                                                        'növelték a belső ____. (tension)',
                                                            'answer': 'feszültséget',
                                                            'english': 'In the dramatic scene, unspoken words '
                                                                       'heightened the internal tension.',
                                                            'teaches': ['b2-14-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "What aesthetic nuance does 'amióta csak' "
                                                                        'produce in narrative?',
                                                            'options': [   'Megszakítatlan érzelmi folyamatot jelöl ki '
                                                                           'egy meghatározó kezdeti élménytől.',
                                                                           'Hirtelen bekövetkező, pillanatnyi eseményt '
                                                                           'fejez ki.',
                                                                           'Két ellentétes dolgot hasonlít össze.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kritikus',
                                                                              'text': 'Hogyan tartja fenn a rendező a '
                                                                                      'feszültséget párbeszéd nélküli '
                                                                                      'percekben?'},
                                                                          {'speaker': 'Dramaturg', 'text': '_____'}],
                                                            'options': [   'A képek kimért ritmusával és a tekintetek '
                                                                           'feszült találkozásával.',
                                                                           'Mert a színházi büfé már kinyitott a '
                                                                           'szünetben a folyosón.',
                                                                           'Alighogy lekapcsolták a vetítőgépet tegnap '
                                                                           'délután.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Érdeklődő',
                                                                              'text': 'Mióta él Lilik ezen a magányos '
                                                                                      'pusztai telepen?'},
                                                                          {'speaker': 'Segéd', 'text': '_____'}],
                                                            'options': [   'Amióta csak az eszét tudja, erre a kietlen '
                                                                           'vidékre kötötte az életét.',
                                                                           'Tegnap délután óta, amikor megvette a '
                                                                           'madarat a piacon.',
                                                                           'Valahányszor megérkezik a postakocsi a '
                                                                           'szomszédos városból.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Whenever the falcon '
                                                                                         'takes flight, perfect '
                                                                                         'silence falls over the '
                                                                                         'plain.',
                                                                               'answer': 'Valahányszor a sólyom '
                                                                                         'felszáll, tökéletes csend '
                                                                                         'telepszik a pusztára.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Ever since he arrived '
                                                                                         'at the station, he has felt '
                                                                                         'the weight of discipline.',
                                                                               'answer': 'Amióta csak megérkezett a '
                                                                                         'telepre, érzi a fegyelem '
                                                                                         'súlyát.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'ritmus' mean in narrative pacing?",
                                                         'options': [   'pacing / rhythm',
                                                                        'color palette',
                                                                        'loud explosion'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': '____ csak ránézett a mesterre, azonnal '
                                                                     'megértette a szavak nélküli parancsot. (as often '
                                                                     'as)',
                                                         'answer': 'Ahányszor',
                                                         'english': 'As often as he merely looked at the master, he '
                                                                    'immediately understood the wordless command.',
                                                         'teaches': ['b2-simultaneity-conjunctions']}]}},
                   {   'num': 4,
                       'title': 'Interpreting Allegory and Symbolism',
                       'grammar_label': 'Narrative layering: combining temporal framing with visual description',
                       'goals': [   'I can combine complex temporal subordinate clauses with symbolic interpretation.',
                                    'I can articulate philosophical allegories behind concrete visual descriptions.',
                                    'I can discuss perspective, spatial geometry, and camera angles at a B2 level.'],
                       'grammar_doc': {   'slug': 'allegory-and-symbolism',
                                          'title': 'Visual Allegory: Framing Meaning Through Space and Time',
                                          'text1_title': 'From Concrete Observation to Universal Allegory',
                                          'text1': 'Hungarian visual storytelling (exemplified by writers like Miklós '
                                                   'Mészöly and filmmakers like Miklós Jancsó, István Gaál, and Béla '
                                                   "Tarr) uses wide spatial horizons ('távlat') and prolonged silence "
                                                   'to elevate physical actions into philosophical allegories '
                                                   "('allegória'). The falconry station in Magasiskola is not merely "
                                                   'an animal shelter; it is an allegory of authoritarian power and '
                                                   'conditioning.',
                                          'text2_title': 'Complex Multi-Clause Syntactic Layering',
                                          'text2': 'When articulating symbolic interpretations, B2 Hungarian relies on '
                                                   "layered multi-clause sentences: 'Miközben a sólyom a magasban "
                                                   'köröz, és mihelyt lecsap a prédára, a néző rádöbben a fegyelem '
                                                   "rideg természetére.' The combination of temporal clauses grounds "
                                                   'the abstract insight in vivid visual moments.',
                                          'table_title': 'Visual Description and Symbolic Terms',
                                          'table_rows': [   [   'jelkép (pl. a szemellenző a rabság jelképe)',
                                                                'symbol (concrete object standing for an idea)'],
                                                            [   'allegória (pl. a hatalom allegóriája)',
                                                                'allegory (extended symbolic narrative)'],
                                                            [   'távlat (térbeli és gondolati távlat)',
                                                                'perspective / vista / horizon'],
                                                            ['kifejező ábrázolás', 'evocative / expressive depiction']],
                                          'examples': [   {   'spanish': 'A sólyom röpte a határtalan szabadság '
                                                                         'kifejező jelképe.',
                                                              'english': 'The flight of the falcon is an expressive '
                                                                         'symbol of boundless freedom.'},
                                                          {   'spanish': 'A regény a hatalom és az alávetettség mély '
                                                                         'filozófiai allegóriája.',
                                                              'english': 'The novel is a deep philosophical allegory '
                                                                         'of power and submission.'},
                                                          {   'spanish': 'A pusztai horizont tágas távlatot nyit a '
                                                                         'gondolatok előtt.',
                                                              'english': 'The horizon of the plain opens a spacious '
                                                                         'perspective before thoughts.'},
                                                          {   'spanish': 'A vizuális ábrázolás pontossága lenyűgözte a '
                                                                         'filmkritikusokat.',
                                                              'english': 'The precision of the visual depiction '
                                                                         'captivated the film critics.'}],
                                          'tip': "Connect concrete sensory nouns ('kesztyű', 'szemellenző', 'puszta') "
                                                 "to abstract thematic nouns ('szabadság', 'engedelmesség', 'magány') "
                                                 'to create compelling analytical sentences.'},
                       'words': [   {'lemma': 'jelkép', 'translation': 'symbol', 'pos': 'noun'},
                                    {'lemma': 'allegória', 'translation': 'allegory', 'pos': 'noun'},
                                    {'lemma': 'távlat', 'translation': 'perspective, vista', 'pos': 'noun'},
                                    {'lemma': 'ábrázolás', 'translation': 'depiction, representation', 'pos': 'noun'},
                                    {'lemma': 'kifejező', 'translation': 'expressive, evocative', 'pos': 'adjective'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the noun 'allegória' mean in literary "
                                                                     'analysis?',
                                                         'options': [   'allegory / symbolic narrative',
                                                                        'short rhyming poem',
                                                                        'factual timetable'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'How do temporal clauses enrich symbolic '
                                                                     'description in B2 prose?',
                                                         'options': [   'They link concrete actions to abstract '
                                                                        'philosophical meanings.',
                                                                        'They remove all verbs from the sentence.',
                                                                        'They make the text read like a legal '
                                                                        'contract.'],
                                                         'correct': 0,
                                                         'teaches': ['b2-simultaneity-conjunctions']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['jelkép', 'symbol'],
                                                                           ['allegória', 'allegory'],
                                                                           ['távlat', 'perspective / vista'],
                                                                           ['ábrázolás', 'depiction / representation'],
                                                                           ['kifejező', 'expressive / evocative']],
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Miközben a madár szabadon repül, a '
                                                                          'szemellenző a rabság rideg ____ marad. '
                                                                          '(symbol)',
                                                              'answer': 'jelképe',
                                                              'english': 'While the bird flies freely, the hood '
                                                                         'remains the cold symbol of captivity.',
                                                              'teaches': ['b2-simultaneity-conjunctions']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A végtelen pusztai horizont tágas ____ nyit '
                                                                          'a szereplők gondolatai előtt. (perspective)',
                                                              'answer': 'távlatot',
                                                              'english': 'The endless horizon of the plain opens a '
                                                                         "spacious perspective before the characters' "
                                                                         'thoughts.',
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence connects spatial perspective '
                                                                          'with symbolic meaning?',
                                                              'options': [   'A tágas távlat és a szűk kalitka '
                                                                             'ellentéte a kiszolgáltatottság '
                                                                             'allegóriája.',
                                                                             'A kalitka fából készült és a sarokban '
                                                                             'állt.',
                                                                             'A távlat szép volt tegnap délben a '
                                                                             'hegytetőről.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-simultaneity-conjunctions']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'sólyom',
                                                                         'idomítása',
                                                                         'az',
                                                                         'emberi',
                                                                         'társadalom',
                                                                         'fegyelmének',
                                                                         'kifejező',
                                                                         'jelképe',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'sólyom',
                                                                            'idomítása',
                                                                            'az',
                                                                            'emberi',
                                                                            'társadalom',
                                                                            'fegyelmének',
                                                                            'kifejező',
                                                                            'jelképe',
                                                                            '.'],
                                                            'english': 'The training of the falcon is an expressive '
                                                                       "symbol of human society's discipline.",
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A regény a hatalom és az alávetettség '
                                                                             'mély allegóriája.',
                                                            'base_word': 'mély allegóriája',
                                                            'options': [   {   'word': 'kifejező ábrázolása',
                                                                               'inflected': 'kifejező ábrázolása',
                                                                               'sentence': 'A regény a hatalom és az '
                                                                                           'alávetettség kifejező '
                                                                                           'ábrázolása.',
                                                                               'gloss': 'expressive depiction'},
                                                                           {   'word': 'szuggesztív jelképe',
                                                                               'inflected': 'szuggesztív jelképe',
                                                                               'sentence': 'A regény a hatalom és az '
                                                                                           'alávetettség szuggesztív '
                                                                                           'jelképe.',
                                                                               'gloss': 'suggestive symbol'}],
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A színészi játék rendkívül ____ és megrendítő '
                                                                        'volt a dráma csúcspontján. (expressive)',
                                                            'answer': 'kifejező',
                                                            'english': 'The acting was exceptionally expressive and '
                                                                       "moving at the drama's climax.",
                                                            'teaches': ['b2-14-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "In Mészöly's Magasiskola, what does the "
                                                                        'falconry station symbolize?',
                                                            'options': [   'A mechanikus fegyelemre épülő '
                                                                           'tekintélyelvű társadalmi rendszert.',
                                                                           'A modern nagyvárosi turizmus fejlődését a '
                                                                           'Felvidéken.',
                                                                           'A mezőgazdasági termelés gépesítését.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Irodalmár',
                                                                              'text': 'Miért nem egyszerű '
                                                                                      'vadásztörténet Mészöly Miklós '
                                                                                      'Magasiskolája?'},
                                                                          {'speaker': 'Filozófus', 'text': '_____'}],
                                                            'options': [   'Mert a solymászat rideg fegyelme a hatalom '
                                                                           'működésének egyetemes allegóriáját '
                                                                           'hordozza.',
                                                                           'Mert a szerző maga soha nem látott még '
                                                                           'sólymot életében a pusztán.',
                                                                           'Mivel a történet a tengerparton játszódik '
                                                                           'a huszadik században.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Diák',
                                                                              'text': 'Hogyan segíti a vizuális '
                                                                                      'ábrázolás a mű mélyebb '
                                                                                      'értelmezését?'},
                                                                          {'speaker': 'Tanár', 'text': '_____'}],
                                                            'options': [   'A tágas puszta és a szűk dúcok ellentéte a '
                                                                           'szabadság és korlátozottság drámáját '
                                                                           'tükrözi.',
                                                                           'A színes díszletek elvonják a figyelmet a '
                                                                           'madarakról a filmben.',
                                                                           'A könyvben nincsenek leírások a tájról '
                                                                           'vagy az állatokról.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The flight of the '
                                                                                         'falcon is a symbol of '
                                                                                         'freedom, while the hood '
                                                                                         'signifies obedience.',
                                                                               'answer': 'A sólyom röpte a szabadság '
                                                                                         'jelképe, miközben a '
                                                                                         'szemellenző az '
                                                                                         'engedelmességet fejezi ki.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The visual depiction '
                                                                                         'gives deep perspective to '
                                                                                         'the conflict between man and '
                                                                                         'nature.',
                                                                               'answer': 'A vizuális ábrázolás mély '
                                                                                         'távlatot ad az ember és a '
                                                                                         'természet konfliktusának.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'távlat' mean?",
                                                         'options': [   'perspective / vista / horizon',
                                                                        'sharp animal claw',
                                                                        'sudden rainfall'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A történet a hatalom rideg mechanizmusának '
                                                                     'tiszta ____ válik. (allegory)',
                                                         'answer': 'allegóriájává',
                                                         'english': 'The story becomes a pure allegory of the cold '
                                                                    'mechanism of power.',
                                                         'teaches': ['b2-simultaneity-conjunctions']}]}},
                   {   'num': 5,
                       'title': 'An Analytical Film or Theatre Review',
                       'grammar_label': 'Writing a critical review: temporal architecture, pacing, and visual '
                                        'vocabulary',
                       'goals': [   'I can write a sophisticated critical review of a film, play, or visual artwork.',
                                    'I can evaluate editing (vágás), directing (rendezés), and pacing (ritmus) using '
                                    'precise terminology.',
                                    "I can synthesize Mészöly's Magasiskola in terms of visual storytelling and "
                                    'narrative restraint.'],
                       'grammar_doc': {   'slug': 'film-theatre-review',
                                          'title': 'Crafting an Analytical Review: Pacing, Montage, and Visual Rhythm',
                                          'text1_title': 'Balancing Description and Critical Evaluation',
                                          'text1': 'An analytical arts review avoids simplistic plot summaries. '
                                                   'Instead, it weaves temporal subordinate clauses into evaluation of '
                                                   "staging and cinematic form: 'Amint felgördül a függöny...', "
                                                   "'Miközben a kamera körbefordul...'. Key technical terms like "
                                                   "'vágás' (film cut / editing), 'jelenet' (scene), 'rendezés' "
                                                   "(direction / staging), and 'filmkocka' (frame) give authority to "
                                                   'the critique.',
                                          'text2_title': 'Dynamic Temporal Transitions in Review Prose',
                                          'text2': 'Fluency in a review comes from shifting smoothly between temporal '
                                                   "perspectives: using 'alighogy' to describe rapid pacing, 'mialatt' "
                                                   "to evaluate counterpoint sound design, and 'amint' to flag "
                                                   "dramatic turning points. Adjectives like 'hatásos' (striking / "
                                                   "effective), 'szuggesztív', and 'feszes' reinforce the analytical "
                                                   'tone.',
                                          'table_title': 'Critical Review Terminology',
                                          'table_rows': [   ['vágás / montázs', 'editing / cut / montage'],
                                                            ['rendezői koncepció', 'directorial concept / staging'],
                                                            [   'hatásos vizuális nyelv',
                                                                'striking / effective visual language'],
                                                            ['feszes tempójú jelenet', 'taut, tightly paced scene']],
                                          'examples': [   {   'spanish': 'Gaál István feszes rendezése hűségesen '
                                                                         'közvetíti a kisregény fegyelmét.',
                                                              'english': "István Gaál's taut direction faithfully "
                                                                         "conveys the novella's discipline."},
                                                          {   'spanish': 'A gyors vágások fokozták a jelenet drámai '
                                                                         'hatását.',
                                                              'english': 'The fast cuts heightened the dramatic effect '
                                                                         'of the scene.'},
                                                          {   'spanish': 'Minden egyes filmkocka a puszta fenséges '
                                                                         'magányát tükrözi.',
                                                              'english': 'Every single film frame reflects the '
                                                                         'majestic solitude of the plain.'},
                                                          {   'spanish': 'Amint véget ér a film, a néző még percekig a '
                                                                         'látottak hatása alatt marad.',
                                                              'english': 'As soon as the film ends, the viewer remains '
                                                                         'under the impact of what was seen for '
                                                                         'minutes.'}],
                                          'tip': "Avoid generic praise like 'nagyon tetszett'; use precise analytical "
                                                 "language: 'A rendezés hatásosan ellenpontozza a madarak mozgását a "
                                                 "szereplők dermedtségével.'"},
                       'words': [   {'lemma': 'filmkocka', 'translation': 'film frame', 'pos': 'noun'},
                                    {'lemma': 'vágás', 'translation': 'cut, editing', 'pos': 'noun'},
                                    {'lemma': 'jelenet', 'translation': 'scene', 'pos': 'noun'},
                                    {'lemma': 'rendezés', 'translation': 'direction, staging', 'pos': 'noun'},
                                    {'lemma': 'hatásos', 'translation': 'effective, striking', 'pos': 'adjective'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the film term 'vágás' mean in "
                                                                     'Hungarian?',
                                                         'options': [   'cut / film editing',
                                                                        'camera battery',
                                                                        'cinema ticket'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'How does an analytical reviewer structure '
                                                                     'transitions between scene analysis and '
                                                                     'evaluation?',
                                                         'options': [   'Using temporal conjunctions (amint, miközben) '
                                                                        'to link dramatic moments to aesthetic '
                                                                        'judgments.',
                                                                        'Listing actor birthdays in chronological '
                                                                        'order.',
                                                                        'Writing only in the future tense without '
                                                                        'punctuation.'],
                                                         'correct': 0,
                                                         'teaches': ['b2-simultaneity-conjunctions']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['filmkocka', 'film frame'],
                                                                           ['vágás', 'cut / editing'],
                                                                           ['jelenet', 'scene'],
                                                                           ['rendezés', 'direction / staging'],
                                                                           ['hatásos', 'effective / striking']],
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': '____ felcsendülnek az utolsó akkordok, a '
                                                                          'nézőtér felállva tapsol. (the moment that)',
                                                              'answer': 'Amint',
                                                              'english': 'The moment the final chords sound, the '
                                                                         'auditorium applauds standing.',
                                                              'teaches': ['b2-simultaneity-conjunctions']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'Gaál István feszes ____ mesterien adja '
                                                                          'vissza a kisregény fojtogató légkörét. '
                                                                          '(direction)',
                                                              'answer': 'rendezése',
                                                              'english': "István Gaál's taut direction masterfully "
                                                                         "recreates the novella's stifling atmosphere.",
                                                              'teaches': ['b2-14-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence belongs to an analytical '
                                                                          'arts review?',
                                                              'options': [   'A film minden egyes filmkockája a '
                                                                             'vizuális fegyelem és a lélektani '
                                                                             'feszültség remeke.',
                                                                             'A mozijegy ötven forintba került a '
                                                                             'pénztárban.',
                                                                             'Tegnap este hat órakor kezdődött az '
                                                                             'előadás a moziban.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-simultaneity-conjunctions']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'gyors',
                                                                         'vágások',
                                                                         'fokozták',
                                                                         'a',
                                                                         'jelenet',
                                                                         'drámai',
                                                                         'hatását',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'gyors',
                                                                            'vágások',
                                                                            'fokozták',
                                                                            'a',
                                                                            'jelenet',
                                                                            'drámai',
                                                                            'hatását',
                                                                            '.'],
                                                            'english': 'The fast cuts heightened the dramatic effect '
                                                                       'of the scene.',
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A rendezés rendkívül hatásos és '
                                                                             'fegyelmezett volt.',
                                                            'base_word': 'hatásos',
                                                            'options': [   {   'word': 'kifejező',
                                                                               'inflected': 'kifejező',
                                                                               'sentence': 'A rendezés rendkívül '
                                                                                           'kifejező és fegyelmezett '
                                                                                           'volt.',
                                                                               'gloss': 'expressive'},
                                                                           {   'word': 'szuggesztív',
                                                                               'inflected': 'szuggesztív',
                                                                               'sentence': 'A rendezés rendkívül '
                                                                                           'szuggesztív és '
                                                                                           'fegyelmezett volt.',
                                                                               'gloss': 'suggestive'}],
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A záró ____ a főhős szótlan tekintetével '
                                                                        'fejeződik be a lemenő napban. (scene)',
                                                            'answer': 'jelenet',
                                                            'english': 'The closing scene finishes with the '
                                                                       "protagonist's wordless gaze in the setting "
                                                                       'sun.',
                                                            'teaches': ['b2-14-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "Why is Gaál István's adaptation of "
                                                                        'Magasiskola considered a cinematic '
                                                                        'masterpiece?',
                                                            'options': [   'Mert a szűkszavú képi világ és a montázs '
                                                                           'erejével teremti meg a belső drámát.',
                                                                           'Mert a főszereplők végig énekelnek a '
                                                                           'pusztában.',
                                                                           'Mivel a filmet egyetlen nap alatt '
                                                                           'forgatták le.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Egyetemista',
                                                                              'text': 'Hogyan értékeli a szakma a '
                                                                                      'Magasiskola képi világát?'},
                                                                          {'speaker': 'Docens', 'text': '_____'}],
                                                            'options': [   'A kamera mozgása és a montázs ritmusa '
                                                                           'rendkívül hatásos vizuális nyelvet teremt.',
                                                                           'A film túlságosan színes és vidám volt egy '
                                                                           'drámához képest.',
                                                                           'Mert a színészek nem tanulták meg a '
                                                                           'szövegüket a forgatás előtt.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kezdő kritikus',
                                                                              'text': 'Milyen szempontokat érdemes '
                                                                                      'figyelembe venni egy színházi '
                                                                                      'előadás elemzésekor?'},
                                                                          {'speaker': 'Szerkesztő', 'text': '_____'}],
                                                            'options': [   'A rendezés koncepcióját, a színészi játék '
                                                                           'hitelességét és a ritmus dinamikáját.',
                                                                           'Kizárólag azt, hogy milyen kényelmesek '
                                                                           'voltak a székek a nézőtéren.',
                                                                           'Hogy mennyi ideig tartott a jegyvásárlás a '
                                                                           'pénztár előtt.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-simultaneity-conjunctions']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The director uses '
                                                                                         'fast cuts while the '
                                                                                         'protagonist flees across the '
                                                                                         'plain.',
                                                                               'answer': 'A rendező gyors vágásokat '
                                                                                         'alkalmaz, miközben a főhős a '
                                                                                         'pusztán át menekül.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Every single film '
                                                                                         'frame reflects the cold '
                                                                                         'discipline of the falconry '
                                                                                         'station.',
                                                                               'answer': 'Minden egyes filmkocka a '
                                                                                         'sólyomtelep rideg fegyelmét '
                                                                                         'tükrözi.'}],
                                                           'teaches': ['b2-simultaneity-conjunctions']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the adjective 'hatásos' mean in art "
                                                                     'and film criticism?',
                                                         'options': [   'striking / effective',
                                                                        'completely invisible',
                                                                        'tiresomely long'],
                                                         'correct': 0,
                                                         'teaches': ['b2-14-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': '____ lefutott a záró felirat, a közönség még '
                                                                     'percekig a helyén maradt. (the moment that)',
                                                         'answer': 'Mihelyt',
                                                         'english': 'The moment the closing credits ran, the audience '
                                                                    'remained in their seats for minutes.',
                                                         'teaches': ['b2-simultaneity-conjunctions']}]}}],
    'consolidation': {   'goals': [   'I can link immediate sequences using amint, mihelyt, and alighogy... máris.',
                                      'I can represent parallel actions and duration with miközben, mialatt, and '
                                      'eközben.',
                                      'I can use iterative temporal conjunctions (valahányszor, ahányszor csak) and '
                                      'visual terminology in reviews.'],
                         'exercises': [   {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': 'Which conjunction expresses that two ongoing processes '
                                                          'occur at the same time in parallel?',
                                              'options': ['miközben', 'alighogy', 'mihelyt'],
                                              'correct': 0,
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'question': "What is the meaning of the technical film term 'filmkocka'?",
                                              'options': ['film frame', 'soundtrack recording', 'stage curtain'],
                                              'correct': 0,
                                              'teaches': ['b2-14-vocab']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': 'Which construction captures two actions happening almost '
                                                          'overlappingly in a flash?',
                                              'options': [   'alighogy ... máris',
                                                             'noha ... mégis',
                                                             'jóllehet ... mindeddig'],
                                              'correct': 0,
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'sentence': 'A solymászmester szigorú ____ igazgatta a telepen folyó '
                                                          'feszült munkát. (discipline)',
                                              'answer': 'fegyelemmel',
                                              'english': 'The master falconer directed the tense work on the station '
                                                         'with strict discipline.',
                                              'teaches': ['b2-14-vocab']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': '____ elhagyta a sólyom az öklöt, azonnal a magasba tört. '
                                                          '(as soon as)',
                                              'answer': 'Amint',
                                              'english': 'As soon as the falcon left the fist, it immediately broke '
                                                         'toward the heights.',
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': 'A narrátor a földön állt, ____ a ragadozó madár a fellegek '
                                                          'között körözött. (while)',
                                              'answer': 'miközben',
                                              'english': 'The narrator stood on the ground while the bird of prey '
                                                         'circled among the clouds.',
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'prompt': [   {   'speaker': 'Kérdező',
                                                                'text': 'Hogyan érezte magát a narrátor a telepen '
                                                                        'töltött hetek alatt?'},
                                                            {'speaker': 'Szakértő', 'text': '_____'}],
                                              'options': [   'Amióta csak megérkezett, nem tudott szabadulni a '
                                                             'fegyelem és a szabadság kettősségétől.',
                                                             'Azonnal elutazott a fővárosba egy új autót vásárolni.',
                                                             'Mivel nem volt villany a barakkban, egész nap mélyen '
                                                             'aludt.'],
                                              'correct': 0,
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'question': "Which sentence correctly uses 'valahányszor' in an "
                                                          'iterative context?',
                                              'options': [   'Valahányszor a sólyom lecsapott, a rét felett elnémult '
                                                             'minden madárdal.',
                                                             'Valahányszor lecsapott a madár, holnap újra vadászni '
                                                             'fogunk.',
                                                             'A sólyom valahányszor a tegnapi napon repült először.'],
                                              'correct': 0,
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'in-context',
                                              'question': 'Which term describes a narrative where characters and '
                                                          'events embody abstract philosophical concepts?',
                                              'options': ['allegória', 'szótár', 'monológ'],
                                              'correct': 0,
                                              'teaches': ['b2-14-vocab']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'Alighogy',
                                                           'belépett',
                                                           'a',
                                                           'kapun,',
                                                           'máris',
                                                           'megcsapta',
                                                           'a',
                                                           'puszta',
                                                           'illata',
                                                           '.'],
                                              'solution': [   'Alighogy',
                                                              'belépett',
                                                              'a',
                                                              'kapun,',
                                                              'máris',
                                                              'megcsapta',
                                                              'a',
                                                              'puszta',
                                                              'illata',
                                                              '.'],
                                              'english': 'Scarcely had he stepped through the gate when already the '
                                                         'scent of the plain struck him.',
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'Miközben',
                                                           'Lilik',
                                                           'a',
                                                           'madarat',
                                                           'idomította,',
                                                           'a',
                                                           'segéd',
                                                           'a',
                                                           'mezőt',
                                                           'járta',
                                                           '.'],
                                              'solution': [   'Miközben',
                                                              'Lilik',
                                                              'a',
                                                              'madarat',
                                                              'idomította,',
                                                              'a',
                                                              'segéd',
                                                              'a',
                                                              'mezőt',
                                                              'járta',
                                                              '.'],
                                              'english': 'While Lilik trained the bird, the assistant walked the '
                                                         'field.',
                                              'teaches': ['b2-simultaneity-conjunctions']},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'template': [   {   'prompt': 'Write: As soon as the scene ends, the '
                                                                            'tension dissolves into quiet '
                                                                            'contemplation.',
                                                                  'answer': 'Amint véget ér a jelenet, a feszültség '
                                                                            'csendes elmélkedésbe oldódik.'}],
                                              'teaches': ['b2-simultaneity-conjunctions']}]}}


# ============================================================================== #
# UNIT 15: Censorship, Ambiguity & Indirect Expression (b2-15)
# ============================================================================== #
UNIT_15 = {   'unit_num': 15,
    'title': 'Censorship, Ambiguity & Indirect Expression',
    'grammar_summary': 'Impersonal and agent-backgrounding structures in Hungarian: agentless 3rd-person plural verbs '
                       '(elhallgatják, betiltották), middle voice reflexives in -ódik/-ődik (megoldódik, tisztázódik), '
                       'bureaucratic nominal-verbal periphrases (kerül + -ásra/-ésre: elfogadásra kerül, megvitatásra '
                       'kerül), and diplomatic hedging formulas (úgy tűnik, némiképp, bizonyos értelemben).',
    'grammar_skill': 'b2-agent-backgrounding',
    'vocab_skill': 'b2-15-vocab',
    'theme': 'Censorship, euphemism and passive-avoidance',
    'intro_body': [   'Hungarian expresses impersonal actions and conceals or backgrounds the agent not through an '
                      'English-style passive voice (which sounds clumsy and unidiomatic in Hungarian when overused), '
                      'but through authentic synthetic devices: 3rd-person plural agentless verbs (elhallgatják, '
                      'betiltották), spontaneous middle verbs in -ódik/-ődik (megoldódik, tisztázódik), bureaucratic '
                      'nominal constructions (-ásra/-ésre kerül), and diplomatic hedging formulas (úgy tűnik, '
                      'némiképp).',
                      "Through Tibor Déry's poignant short novel Niki: Egy kutya története (1956)—set during the dark "
                      'paranoia of the Rákosi era, when engineer János Ancsa disappears into prison without '
                      'explanation and his wife and terrier Niki endure years of whispered evasions and institutional '
                      'silence—you will master how to read between the lines, decode euphemisms, and reframe sensitive '
                      'statements with diplomatic restraint.'],
    'classic_story': {   'slug': 'niki',
                         'author': 'Déry Tibor',
                         'work': 'Niki: Egy kutya története (1956)',
                         'title': 'Niki és a kimondhatatlan évek',
                         'summary': 'Az ötvenes évek nyomasztó légkörében Ancsa János mérnököt váratlanul, indoklás '
                                    'nélkül letartóztatják; felesége és a hűséges foxterrier, Niki öt éven át viselik '
                                    'a bürokratikus hallgatás, a társadalmi kiközösítés és a kimondhatatlan szorongás '
                                    'súlyát.',
                         'characters': ['Ancsa Jánosné', 'Niki'],
                         'paragraphs': [   {   'type': 'narration',
                                               'text': 'Az ezerkilencszázötvenes évek elején egy budai kertes ház '
                                                       'csendjében élt Ancsa János bányamérnök a feleségével és egy '
                                                       'fiatal foxterrier szukával, akit Nikinek neveztek el. A kutya '
                                                       'ragaszkodása és életvidámsága kezdetben menedéket nyújtott a '
                                                       'házaspárnak a külvilágból egyre fenyegetőbben beszivárgó '
                                                       'politikai feszültségek elől.'},
                                           {   'type': 'narration',
                                               'text': 'Egy őszi délutánon azonban bekövetkezett a tragédia: Ancsa '
                                                       'mérnök nem tért haza a munkahelyéről. Nem mondták meg, hová '
                                                       'vitték, és a hivatalos szervek részéről semmiféle '
                                                       'felvilágosítás nem adatott; az államhatalom gépezetében az '
                                                       'ember egyszerűen nyom nélkül eltűnt, mintha soha nem is '
                                                       'létezett volna.'},
                                           {   'type': 'narration',
                                               'text': 'A következő hetekben Ancsa Jánosné hiába járta a '
                                                       'minisztériumok és a rendőrség rideg folyosóit. Mindenütt '
                                                       'elutasításra lelt: a beadványok megválaszolatlanul maradtak, a '
                                                       'tisztviselők óvatosan elfordították a fejüket, és az ügy '
                                                       'kivizsgálása minduntalan elhalasztódott a láthatatlan felsőbb '
                                                       'utasításokra hivatkozva.'},
                                           {   'type': 'narration',
                                               'text': 'Az asszony hamarosan elveszítette a tanári állását is, és '
                                                       'kisebb albérletbe kényszerült a kutyával. A szomszédok és a '
                                                       'korábbi barátok zöme elhallgatott, amikor találkoztak vele a '
                                                       'lépcsőházban; a félelem légkörében a letartóztatott mérnök '
                                                       'feleségével való érintkezés is gyanúsnak számított, így az '
                                                       'asszony körül lassanként megfagyott a levegő.'},
                                           {   'type': 'narration',
                                               'text': 'Egyedül Niki maradt hűséges hozzá a növekvő nyomorúságban. A '
                                                       'kutya ugyan nem értette az emberi szavakat, de finom '
                                                       'ösztöneivel pontosan megérezte a gazdasszonya bánatát; '
                                                       'csendesen simult a lábához a fűtetlen szobában, miközben '
                                                       'odakinn az utcán a hangszórókból a semmitmondó politikai '
                                                       'jelszavak harsogtak.'},
                                           {   'type': 'narration',
                                               'text': 'Évek teltek el anélkül, hogy a mérnök sorsáról bármi biztos '
                                                       'kiderült volna. A hivatalos nyelvezetben a letartóztatás '
                                                       'tényét eufemizmusokkal fedték el: az illetékesek úgy '
                                                       "fogalmaztak, hogy a mérnök elvtárs 'más megbízatást kapott', "
                                                       "vagy az ügye 'folyamatban lévő eljárás tárgyát képezi'."},
                                           {   'type': 'narration',
                                               'text': 'Niki időközben megöregedett, szőre megfakult, és ereje fogytán '
                                                       'volt a hosszú nélkülözés miatt. Amikor öt év után, a politikai '
                                                       'enyhülés idején végre tisztázódott a mérnök ártatlansága, és a '
                                                       'börtönkapu megnyílt előtte, a meggyötört kutya már nem érhette '
                                                       'meg a gazdája hazatérését; éppen aznap hajnalban hunyt el a '
                                                       'szőnyegen.'},
                                           {   'type': 'narration',
                                               'text': 'Déry Tibor mesterműve megrázó látlelet az önkényuralom '
                                                       'éveiről. Niki története a sorok között olvasó korabeli '
                                                       'közönség számára a kiszolgáltatottság, az elnyomás és a hűség '
                                                       'egyetemes jelképévé vált; olyan alkotássá, amely a kutyasors '
                                                       'tükrében mutatta fel az emberi méltóság tragikumát.'}],
                         'reading_questions': [   {   'question': 'Mi történt Ancsa János mérnökkel az ötvenes évek '
                                                                  'elején?',
                                                      'options': [   'Váratlanul letartóztatták, és a hatóságok '
                                                                     'semmiféle felvilágosítást nem adtak a '
                                                                     'feleségének a hollétéről.',
                                                                     'Külföldre utazott egy nemzetközi bányászati '
                                                                     'konferenciára, és ott telepedett le.',
                                                                     'Önszántából elköltözött a budai házból, hogy új '
                                                                     'kutatóintézetet alapítson vidéken.'],
                                                      'correct': 0},
                                                  {   'question': 'Hogyan viselkedtek a szomszédok és a barátok Ancsa '
                                                                  'Jánosnéval a férje eltűnése után?',
                                                      'options': [   'A félelem miatt elfordították a fejüket, '
                                                                     'elhallgattak, és elkerülték a vele való '
                                                                     'érintkezést.',
                                                                     'Minden nap ételt vittek neki, és tüntetést '
                                                                     'szerveztek a minisztérium előtt.',
                                                                     'Kiköltöztették őt egy tágasabb villába a Duna '
                                                                     'partján.'],
                                                      'correct': 0},
                                                  {   'question': 'Mi tette Déry Tibor regényét a korabeli olvasók '
                                                                  'számára felejthetetlenné?',
                                                      'options': [   'A sorok között a hűséges kutya sorsán keresztül '
                                                                     'az önkényuralom és az emberi kiszolgáltatottság '
                                                                     'tragédiáját ábrázolta.',
                                                                     'Mert részletes útmutatót adott a vadászkutyák '
                                                                     'helyes etetéséről és gondozásáról.',
                                                                     'Mert kizárólag a budai kertek növényvilágáról és '
                                                                     'virágairól szólt.'],
                                                      'correct': 0}]},
    'lessons': [   {   'num': 1,
                       'title': 'When the Agent Disappears (megvitatásra kerül)',
                       'grammar_label': 'Agentless 3rd-person plural and middle verbs: elhallgatják, betiltották, '
                                        'megoldódik',
                       'goals': [   'I can use agentless 3rd-person plural verbs to state that an action occurred '
                                    'without naming who did it.',
                                    'I can use middle verbs in -ódik/-ődik to describe events as unfolding '
                                    'spontaneously.',
                                    'I can avoid awkward passive calques (anglicisms) by applying natural Hungarian '
                                    'agent-backgrounding.'],
                       'grammar_doc': {   'slug': 'agentless-and-middle-verbs',
                                          'title': 'Natural Agent-Backgrounding: 3rd-Person Plural and Middle Verbs',
                                          'text1_title': 'The Authentic Alternative to the Passive Voice',
                                          'text1': "While English regularly uses the passive voice ('The book was "
                                                   "banned', 'The engineer was arrested'), natural Hungarian strongly "
                                                   "prefers agentless 3rd-person plural verbs: 'Betiltották a "
                                                   "könyvet', 'Letartóztatták a mérnököt'. The plural ending implies "
                                                   'institutional or unspecified agents without creating heavy '
                                                   'participial constructions (*A könyv be lett tiltva is unidiomatic '
                                                   'in Hungarian).',
                                          'text2_title': 'Spontaneous Processes with Middle Verbs (-ódik/-ődik)',
                                          'text2': "Hungarian middle verbs ending in '-ódik/-ődik' present events as "
                                                   "unfolding on their own, removing human agency entirely: 'A helyzet "
                                                   "tisztázódott' (The situation cleared up), 'A probléma magától "
                                                   "megoldódik' (The problem resolves itself), 'A feszültség "
                                                   "fokozódik' (The tension is escalating). In narrative prose, this "
                                                   'shifts attention from the perpetrator to the state itself.',
                                          'table_title': 'Agent-Backgrounding Structures',
                                          'table_rows': [   [   '3rd plural verb (pl. betiltották)',
                                                                'they banned / was banned (agentless active)'],
                                                            [   'middle verb in -ódik/-ődik (pl. megoldódik)',
                                                                'resolves itself / is resolved (spontaneous process)'],
                                                            [   'kiderül (pl. kiderült az igazság)',
                                                                'turns out / becomes known (spontaneous revelation)'],
                                                            [   'elhallgat (pl. elhallgatták a tényeket)',
                                                                'concealed / kept silent about (deliberate omission)']],
                                          'examples': [   {   'spanish': 'Az önkényuralom idején sok bátor író művét '
                                                                         'betiltották.',
                                                              'english': 'During the tyranny, the works of many '
                                                                         'courageous writers were banned.'},
                                                          {   'spanish': 'A vitás kérdés szerencsére békés úton '
                                                                         'megoldódott.',
                                                              'english': 'The disputed question was fortunately '
                                                                         'resolved peacefully.'},
                                                          {   'spanish': 'A hivatalos sajtóban teljesen elhallgatták a '
                                                                         'bírálatokat.',
                                                              'english': 'In the official press, criticisms were '
                                                                         'completely concealed.'},
                                                          {   'spanish': 'Hamarosan kiderült, hogy a vádak alaptalanok '
                                                                         'voltak.',
                                                              'english': 'Soon it turned out that the accusations were '
                                                                         'unfounded.'}],
                                          'tip': "Never say 'A könyv el lett olvasva' or 'A törvény meg lett hozva'; "
                                                 "say 'Elolvasták a könyvet' or 'Megszületett a törvény' to speak "
                                                 'authentic B2 Hungarian.'},
                       'words': [   {   'lemma': 'elhallgat',
                                        'translation': 'to keep silent about, conceal',
                                        'pos': 'verb'},
                                    {'lemma': 'betilt', 'translation': 'to ban, prohibit', 'pos': 'verb'},
                                    {   'lemma': 'megoldódik',
                                        'translation': 'to be resolved, resolve itself',
                                        'pos': 'verb'},
                                    {'lemma': 'kiderül', 'translation': 'to turn out, become clear', 'pos': 'verb'},
                                    {'lemma': 'cenzúra', 'translation': 'censorship', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the Hungarian noun 'cenzúra' mean?",
                                                         'options': [   'censorship / official suppression',
                                                                        'scientific publishing',
                                                                        'free debate'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'How does authentic Hungarian avoid the passive '
                                                                     'voice when the agent is unknown or unspecified?',
                                                         'options': [   'Using agentless 3rd-person plural verbs: '
                                                                        'elhallgatják, betiltották.',
                                                                        "Using the conditional past with 'lett volna'.",
                                                                        'Repeating the subject noun five times in each '
                                                                        'sentence.'],
                                                         'correct': 0,
                                                         'teaches': ['b2-agent-backgrounding']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   [   'elhallgat',
                                                                               'to keep silent about / conceal'],
                                                                           ['betilt', 'to ban / prohibit'],
                                                                           ['megoldódik', 'to resolve itself'],
                                                                           ['kiderül', 'to turn out / become clear'],
                                                                           ['cenzúra', 'censorship']],
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Az önkényuralom idején sok bátor író művét '
                                                                          '____. (they banned)',
                                                              'answer': 'betiltották',
                                                              'english': 'During the tyranny, the works of many '
                                                                         'courageous writers were banned.',
                                                              'teaches': ['b2-agent-backgrounding']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A diktatúrában a szigorú sajtó-____ miatt '
                                                                          'nem jelenhettek meg a valós hírek. '
                                                                          '(censorship)',
                                                              'answer': 'cenzúra',
                                                              'english': 'Under the dictatorship, real news could not '
                                                                         'appear due to strict press censorship.',
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence uses a middle verb in -ódik '
                                                                          'to show spontaneous resolution?',
                                                              'options': [   'A vitás kérdés szerencsére békés úton '
                                                                             'megoldódott.',
                                                                             'A vitás kérdést tegnap este vitatták meg '
                                                                             'a minisztériumban.',
                                                                             'A bizottság elnöke azonnal felolvasta a '
                                                                             'határozatot.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-agent-backgrounding']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'mérnököt',
                                                                         'egy',
                                                                         'őszi',
                                                                         'délutánon',
                                                                         'váratlanul',
                                                                         'letartóztatták',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'mérnököt',
                                                                            'egy',
                                                                            'őszi',
                                                                            'délutánon',
                                                                            'váratlanul',
                                                                            'letartóztatták',
                                                                            '.'],
                                                            'english': 'The engineer was unexpectedly arrested on an '
                                                                       'autumn afternoon.',
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'Hamarosan kiderült az igazság a '
                                                                             'tárgyaláson.',
                                                            'base_word': 'kiderült',
                                                            'options': [   {   'word': 'tisztázódott',
                                                                               'inflected': 'tisztázódott',
                                                                               'sentence': 'Hamarosan tisztázódott az '
                                                                                           'igazság a tárgyaláson.',
                                                                               'gloss': 'became cleared up'},
                                                                           {   'word': 'megoldódott',
                                                                               'inflected': 'megoldódott',
                                                                               'sentence': 'Hamarosan megoldódott az '
                                                                                           'igazság a tárgyaláson.',
                                                                               'gloss': 'got resolved'}],
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A hivatalos közleményben szándékosan ____ a '
                                                                        'legfontosabb tényeket. (they concealed)',
                                                            'answer': 'elhallgatták',
                                                            'english': 'In the official communiqué, they deliberately '
                                                                       'concealed the most important facts.',
                                                            'teaches': ['b2-15-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "Why is 'A könyv be lett tiltva' avoided in "
                                                                        'good Hungarian writing?',
                                                            'options': [   'Mert idegenszerű passzív szerkezet; '
                                                                           "helyette a természetes 'Betiltották a "
                                                                           "könyvet' használandó.",
                                                                           "Mert a 'tiltva' szót nem ismeri a magyar "
                                                                           'nyelv.',
                                                                           'Mert csak latin szavakat szabad használni '
                                                                           'a mondatban.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Feleség',
                                                                              'text': 'Miért nem kapott értesítést a '
                                                                                      'család a mérnök hollétéről a '
                                                                                      'hatóságoktól?'},
                                                                          {'speaker': 'Ügyvéd', 'text': '_____'}],
                                                            'options': [   'Mert az ilyen politikai ügyeket a hatalom '
                                                                           'képviselői teljesen elhallgatták a '
                                                                           'nyilvánosság elől.',
                                                                           'Mivel a postás elhagyta a leveleket a '
                                                                           'villamoson tegnap délután.',
                                                                           'Igen, hiszen a mérnök mindennap telefonált '
                                                                           'a börtönből a családjának.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kolléga',
                                                                              'text': 'Vajon mikor tisztázódik végre a '
                                                                                      'letartóztatott szakemberek '
                                                                                      'helyzete?'},
                                                                          {'speaker': 'Barát', 'text': '_____'}],
                                                            'options': [   'Csak akkor, ha az ügyek független bíróság '
                                                                           'elé kerülnek, és minden körülmény kiderül.',
                                                                           'Tegnap reggel, mert a könyvtár már '
                                                                           'kinyitott a téren.',
                                                                           'Alighogy megérkezett a villamos az '
                                                                           'állomásra tegnap este.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The novel was banned, '
                                                                                         'but people read it in '
                                                                                         'secret.',
                                                                               'answer': 'A regényt betiltották, de az '
                                                                                         'emberek titokban olvasták.'}],
                                                           'teaches': ['b2-agent-backgrounding']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: After years of '
                                                                                         'silence, the truth finally '
                                                                                         'turned out.',
                                                                               'answer': 'Évekig tartó hallgatás után '
                                                                                         'végül kiderült az igazság.'}],
                                                           'teaches': ['b2-agent-backgrounding']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the verb 'megoldódik' express?",
                                                         'options': [   'to be resolved / to resolve itself '
                                                                        'spontaneously',
                                                                        'to tie a tight knot',
                                                                        'to make a mistake'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A tárgyalások során minden félreértés békésen '
                                                                     '____ a felek között. (cleared up)',
                                                         'answer': 'tisztázódott',
                                                         'english': 'In the course of the negotiations, every '
                                                                    'misunderstanding cleared up peacefully between '
                                                                    'the parties.',
                                                         'teaches': ['b2-agent-backgrounding']}]}},
                   {   'num': 2,
                       'title': 'Bureaucratic Nominal-Verbal Constructions (bevezetésre kerül)',
                       'grammar_label': 'Bureaucratic function-verb periphrases: -ásra/-ésre kerül',
                       'goals': [   'I can recognize and formulate formal administrative statements using -ásra/-ésre '
                                    'kerül.',
                                    'I can understand official decrees, institutional communiqués, and legal notices.',
                                    'I can critically assess when bureaucratic nominalization creates distance or '
                                    'obscures accountability.'],
                       'grammar_doc': {   'slug': 'bureaucratic-nominal-constructions',
                                          'title': 'Administrative Passive-Avoidance: -ásra/-ésre kerül',
                                          'text1_title': 'The Institutional Formula: -ásra/-ésre kerül',
                                          'text1': 'In Hungarian administrative, judicial, and corporate '
                                                   'communication, the periphrasis formed by a verbal noun (ending in '
                                                   "-ás/-és) + sublative case suffix (-ra/-re) + the verb 'kerül' "
                                                   'serves as the primary formal surrogate for passive constructions: '
                                                   "'A javaslat elfogadásra került' (The proposal was adopted), 'Az új "
                                                   "szabályzat bevezetésre kerül' (The new policy will be introduced).",
                                          'text2_title': 'Syntactic Agreement and Communicative Function',
                                          'text2': "The verb 'kerül' inflects normally for tense and number according "
                                                   "to the grammatical subject: 'A határozatok elfogadásra kerültek' "
                                                   '(plural past). While stylistic purists caution against its overuse '
                                                   'in creative prose, mastering this structure is indispensable for '
                                                   "understanding government decrees ('határozat'), legal statutes, "
                                                   'and diplomatic communiqués where the agency of the decision-maker '
                                                   'is deliberately backgrounded.',
                                          'table_title': 'Bureaucratic Passive Periphrases',
                                          'table_rows': [   ['bevezetésre kerül', 'is introduced / implemented'],
                                                            ['elfogadásra került', 'was accepted / adopted'],
                                                            ['megvalósításra kerül', 'is realized / executed'],
                                                            ['elutasításra került', 'was rejected / declined']],
                                          'examples': [   {   'spanish': 'Az új törvényjavaslat a parlamentben '
                                                                         'egyhangúlag elfogadásra került.',
                                                              'english': 'The new bill was unanimously adopted in '
                                                                         'parliament.'},
                                                          {   'spanish': 'A tervezett intézkedések a jövő hónapban '
                                                                         'bevezetésre kerülnek.',
                                                              'english': 'The planned measures will be implemented '
                                                                         'next month.'},
                                                          {   'spanish': 'A minisztérium határozatban rögzítette a '
                                                                         'döntést.',
                                                              'english': 'The ministry recorded the decision in a '
                                                                         'decree.'},
                                                          {   'spanish': 'A polgárok beadványa sajnos elutasításra '
                                                                         'került a hivatalban.',
                                                              'english': "The citizens' petition was unfortunately "
                                                                         'rejected at the office.'}],
                                          'tip': "Pay close attention to vowel harmony: back-vowel stems take '-ásra "
                                                 "kerül' (pl. 'elfogadásra'), while front-vowel stems take '-ésre "
                                                 "kerül' (pl. 'bevezetésre')."},
                       'words': [   {   'lemma': 'bevezetés',
                                        'translation': 'introduction, implementation',
                                        'pos': 'noun'},
                                    {'lemma': 'elfogadás', 'translation': 'acceptance, adoption', 'pos': 'noun'},
                                    {'lemma': 'megvalósítás', 'translation': 'realization, execution', 'pos': 'noun'},
                                    {'lemma': 'elutasítás', 'translation': 'rejection, refusal', 'pos': 'noun'},
                                    {   'lemma': 'határozat',
                                        'translation': 'resolution, decree, decision',
                                        'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the administrative noun 'határozat' "
                                                                     'mean?',
                                                         'options': [   'resolution / decree / formal decision',
                                                                        'literary novel',
                                                                        'medical prescription'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which bureaucratic periphrase serves as a '
                                                                     'passive equivalent in administrative Hungarian?',
                                                         'options': [   'kerül + -ásra/-ésre: elfogadásra kerül',
                                                                        'fog + infinitive: el fog fogadni',
                                                                        'kell + subjunctive: el kelljen fogadni'],
                                                         'correct': 0,
                                                         'teaches': ['b2-agent-backgrounding']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   [   'bevezetés',
                                                                               'introduction / implementation'],
                                                                           ['elfogadás', 'acceptance / adoption'],
                                                                           ['megvalósítás', 'realization / execution'],
                                                                           ['elutasítás', 'rejection / refusal'],
                                                                           ['határozat', 'decree / resolution']],
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Az új szabályozás a következő hónapban ____ '
                                                                          'kerül. (introduced)',
                                                              'answer': 'bevezetésre',
                                                              'english': 'The new regulation will be introduced next '
                                                                         'month.',
                                                              'teaches': ['b2-agent-backgrounding']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A minisztérium hivatalos ____ közzétette a '
                                                                          'legújabb intézkedéseket. (decree)',
                                                              'answer': 'határozatban',
                                                              'english': 'In an official decree, the ministry '
                                                                         'published the latest measures.',
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': "Which phrase translates 'was adopted / "
                                                                          "accepted' in formal government prose?",
                                                              'options': [   'elfogadásra került',
                                                                             'elutasításra jutott',
                                                                             'megvalósítást keresett'],
                                                              'correct': 0,
                                                              'teaches': ['b2-agent-backgrounding']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'törvényjavaslat',
                                                                         'a',
                                                                         'parlamentben',
                                                                         'egyhangúlag',
                                                                         'elfogadásra',
                                                                         'került',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'törvényjavaslat',
                                                                            'a',
                                                                            'parlamentben',
                                                                            'egyhangúlag',
                                                                            'elfogadásra',
                                                                            'került',
                                                                            '.'],
                                                            'english': 'The bill was unanimously adopted in '
                                                                       'parliament.',
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A bizottsági javaslat elfogadásra került '
                                                                             'az ülésen.',
                                                            'base_word': 'elfogadásra került',
                                                            'options': [   {   'word': 'elutasításra került',
                                                                               'inflected': 'elutasításra került',
                                                                               'sentence': 'A bizottsági javaslat '
                                                                                           'elutasításra került az '
                                                                                           'ülésen.',
                                                                               'gloss': 'was rejected'},
                                                                           {   'word': 'megvitatásra került',
                                                                               'inflected': 'megvitatásra került',
                                                                               'sentence': 'A bizottsági javaslat '
                                                                                           'megvitatásra került az '
                                                                                           'ülésen.',
                                                                               'gloss': 'was discussed'}],
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A terv gyakorlati ____ sajnos számos '
                                                                        'nehézségbe ütközött. (realization)',
                                                            'answer': 'megvalósítása',
                                                            'english': 'The practical realization of the plan '
                                                                       'unfortunately ran into numerous difficulties.',
                                                            'teaches': ['b2-15-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': 'In which register is the structure '
                                                                        "'-ásra/-ésre kerül' most naturally used?",
                                                            'options': [   'Hivatalos, jogi, gazdasági és bürokratikus '
                                                                           'szövegekben.',
                                                                           'Kizárólag óvodás mesékben és '
                                                                           'gyermekversekben.',
                                                                           'Kocsmában folytatott közvetlen baráti '
                                                                           'beszélgetésekben.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Ügyfél',
                                                                              'text': 'Mikor várható döntés a '
                                                                                      'benyújtott kártérítési '
                                                                                      'kérelemről?'},
                                                                          {'speaker': 'Tisztviselő', 'text': '_____'}],
                                                            'options': [   'A beadvány a jövő heti tanácsülésen '
                                                                           'érdemben megvitatásra kerül.',
                                                                           'Mert a miniszter tegnap elutazott három '
                                                                           'hetes szabadságra a tengerhez.',
                                                                           'Mihelyt kinyit a színházi pénztár a túlsó '
                                                                           'sarkon.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Újságíró',
                                                                              'text': 'Miért fogalmaznak ilyen '
                                                                                      'személytelenül a minisztériumi '
                                                                                      'határozatokban?'},
                                                                          {'speaker': 'Jogász', 'text': '_____'}],
                                                            'options': [   'A személytelen szerkezetekkel a '
                                                                           'döntéshozók intézményi jelleget adnak a '
                                                                           'szövegnek.',
                                                                           'Mert a hivatalnokok elfelejtették a magyar '
                                                                           'nyelv alapvető szavait.',
                                                                           'Igen, hiszen minden állampolgár azonnal '
                                                                           'megérti a határozatot.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The project was '
                                                                                         'approved and will be '
                                                                                         'implemented soon.',
                                                                               'answer': 'A tervezet elfogadásra '
                                                                                         'került, és hamarosan '
                                                                                         'megvalósításra kerül.'}],
                                                           'teaches': ['b2-agent-backgrounding']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': "Write: The citizen's "
                                                                                         'complaint was rejected by '
                                                                                         'the authorities.',
                                                                               'answer': 'Az állampolgár panasza '
                                                                                         'elutasításra került a '
                                                                                         'hatóságok részéről.'}],
                                                           'teaches': ['b2-agent-backgrounding']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does 'elutasítás' mean?",
                                                         'options': [   'rejection / refusal',
                                                                        'warm invitation',
                                                                        'financial profit'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A vitás pontok részletesen ____ kerültek a '
                                                                     'tegnapi jelentésben. (discussed)',
                                                         'answer': 'megvitatásra',
                                                         'english': 'The disputed points were discussed in detail in '
                                                                    "yesterday's report.",
                                                         'teaches': ['b2-agent-backgrounding']}]}},
                   {   'num': 3,
                       'title': 'Euphemism and Diplomatic Hedging',
                       'grammar_label': 'Euphemistic softening and modal hedging: úgy tűnik, némiképp, bizonyos '
                                        'értelemben',
                       'goals': [   'I can soften harsh criticisms and delicate assessments using némiképp and '
                                    'bizonyos értelemben.',
                                    'I can frame subjective evaluations objectively using impersonal úgy tűnik.',
                                    'I can identify euphemisms used in political discourse and corporate '
                                    'communication.'],
                       'grammar_doc': {   'slug': 'euphemism-diplomatic-hedging',
                                          'title': 'Diplomatic Hedging and Euphemism: Softening the Unpleasant',
                                          'text1_title': 'Mitigating Critical Pronouncements',
                                          'text1': 'In sensitive public and diplomatic discussions, direct statements '
                                                   "('Ez a javaslat rossz', 'Ön tévedett') provoke unnecessary "
                                                   'friction. B2 communicators soften assertions by inserting '
                                                   "mitigating adverbs: 'némiképp' (somewhat / slightly), 'bizonyos "
                                                   "értelemben' (in a certain sense / in some respects), and "
                                                   "'mondhatni' (one might say): 'A döntés némiképp elhamarkodott "
                                                   "volt.'",
                                          'text2_title': "Impersonal Matrices with 'úgy tűnik'",
                                          'text2': "'Úgy tűnik, hogy...' (It appears that...) and 'Úgy látszik...' (It "
                                                   'seems...) frame evaluations as provisional observations rather '
                                                   'than dogma. In authoritarian or corporate prose, euphemisms '
                                                   "('eufemizmus') are routinely deployed to replace unpleasant "
                                                   "truths: calling political arrests 'más megbízatás' or firing "
                                                   "workers 'átszervezés'.",
                                          'table_title': 'Hedging and Softening Patterns',
                                          'table_rows': [   [   'úgy tűnik, hogy...',
                                                                'it appears that... (impersonal observation)'],
                                                            [   'némiképp + adjective',
                                                                'somewhat / slightly (polite mitigation)'],
                                                            [   'bizonyos értelemben / tekintetben',
                                                                'in a certain sense / in some respects'],
                                                            [   'finomítani a megfogalmazást',
                                                                'to tone down / refine the phrasing']],
                                          'examples': [   {   'spanish': 'Úgy tűnik, hogy a bírálat némiképp túlzó '
                                                                         'volt a körülményekhez képest.',
                                                              'english': 'It appears that the criticism was somewhat '
                                                                         'exaggerated given the circumstances.'},
                                                          {   'spanish': 'Bizonyos értelemben a félreértés segített '
                                                                         'tisztázni az álláspontokat.',
                                                              'english': 'In a certain sense, the misunderstanding '
                                                                         'helped clarify the standpoints.'},
                                                          {   'spanish': 'A diplomata óvatos szavakkal finomította a '
                                                                         'kormány hivatalos válaszát.',
                                                              'english': "The diplomat toned down the government's "
                                                                         'official response with cautious words.'},
                                                          {   'spanish': 'A sajtófőnök eufemizmusokkal fedte el a '
                                                                         'lemondás valódi okait.',
                                                              'english': 'The press chief masked the real reasons for '
                                                                         'the resignation with euphemisms.'}],
                                          'tip': "Combine 'úgy tűnik' with a conditional verb ('hasznosabb lenne') to "
                                                 'formulate the ultimate diplomatic suggestion without causing '
                                                 'offense.'},
                       'words': [   {'lemma': 'némiképp', 'translation': 'somewhat, slightly', 'pos': 'adverb'},
                                    {'lemma': 'eufemizmus', 'translation': 'euphemism', 'pos': 'noun'},
                                    {'lemma': 'finomít', 'translation': 'to refine, soften, tone down', 'pos': 'verb'},
                                    {'lemma': 'óvatos', 'translation': 'cautious, discreet', 'pos': 'adjective'},
                                    {'lemma': 'félreértés', 'translation': 'misunderstanding', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What is an 'eufemizmus'?",
                                                         'options': [   'a mild or indirect word used instead of a '
                                                                        'harsh or blunt one',
                                                                        'a loud marching song',
                                                                        'a strictly military weapon'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'Which phrase softens a potentially harsh factual '
                                                                     'judgment in diplomatic speech?',
                                                         'options': [   'némiképp / bizonyos értelemben',
                                                                        'mindenképpen és azonnal',
                                                                        'egyáltalán soha'],
                                                         'correct': 0,
                                                         'teaches': ['b2-agent-backgrounding']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['némiképp', 'somewhat / slightly'],
                                                                           ['eufemizmus', 'euphemism'],
                                                                           ['finomít', 'to soften / tone down'],
                                                                           ['óvatos', 'cautious / discreet'],
                                                                           ['félreértés', 'misunderstanding']],
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Úgy tűnik, hogy a döntés ____ elhamarkodott '
                                                                          'volt a tárgyalások előtt. (somewhat)',
                                                              'answer': 'némiképp',
                                                              'english': 'It seems that the decision was somewhat '
                                                                         'hasty before the negotiations.',
                                                              'teaches': ['b2-agent-backgrounding']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A diplomata igyekezett eloszlatni a két fél '
                                                                          'közötti kínos ____. (misunderstanding)',
                                                              'answer': 'félreértést',
                                                              'english': 'The diplomat endeavored to dispel the '
                                                                         'awkward misunderstanding between the two '
                                                                         'parties.',
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence demonstrates diplomatic '
                                                                          'hedging?',
                                                              'options': [   'Bizonyos értelemben indokolt lehet az '
                                                                             'aggodalom, bár a helyzet kezelhető.',
                                                                             'A helyzet katasztrofális, azonnal '
                                                                             'mindenki mondjon le!',
                                                                             'Tegnap esett az eső a nagykövetség '
                                                                             'udvarán.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-agent-backgrounding']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'Úgy',
                                                                         'tűnik,',
                                                                         'hogy',
                                                                         'finomítani',
                                                                         'kell',
                                                                         'a',
                                                                         'nyilatkozat',
                                                                         'szövegét',
                                                                         '.'],
                                                            'solution': [   'Úgy',
                                                                            'tűnik,',
                                                                            'hogy',
                                                                            'finomítani',
                                                                            'kell',
                                                                            'a',
                                                                            'nyilatkozat',
                                                                            'szövegét',
                                                                            '.'],
                                                            'english': 'It seems that the text of the declaration '
                                                                       'needs to be toned down.',
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A javaslat némiképp eltér az eredeti '
                                                                             'elképzeléstől.',
                                                            'base_word': 'némiképp',
                                                            'options': [   {   'word': 'bizonyos tekintetben',
                                                                               'inflected': 'bizonyos tekintetben',
                                                                               'sentence': 'A javaslat bizonyos '
                                                                                           'tekintetben eltér az '
                                                                                           'eredeti elképzeléstől.',
                                                                               'gloss': 'in a certain respect'},
                                                                           {   'word': 'alighanem',
                                                                               'inflected': 'alighanem',
                                                                               'sentence': 'A javaslat alighanem eltér '
                                                                                           'az eredeti elképzeléstől.',
                                                                               'gloss': 'in all likelihood'}],
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A politikus az elbocsátások helyett az '
                                                                        'átszervezés ____ használta. (euphemism)',
                                                            'answer': 'eufemizmusát',
                                                            'english': 'Instead of layoffs, the politician used the '
                                                                       'euphemism of reorganization.',
                                                            'teaches': ['b2-15-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "What purpose does 'óvatos fogalmazás' serve "
                                                                        'in diplomatic discourse?',
                                                            'options': [   'Megelőzi a nyílt konfliktust és '
                                                                           'tiszteletben tartja a tárgyalópartner '
                                                                           'méltóságát.',
                                                                           'Célja a másik fél durva megsértése és '
                                                                           'megbüntetése.',
                                                                           'Megakadályozza, hogy bárki megértse az '
                                                                           'anyanyelvét.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Riporter',
                                                                              'text': 'Valóban kudarcot vallott a '
                                                                                      'nemzetközi tárgyalássorozat?'},
                                                                          {   'speaker': 'Külügyi szóvivő',
                                                                              'text': '_____'}],
                                                            'options': [   'Úgy tűnik, bizonyos kérdésekben némiképp '
                                                                           'eltértek az álláspontok, de a párbeszéd '
                                                                           'folytatódik.',
                                                                           'Igen, mindenki azonnal összeveszett és '
                                                                           'azonnal hazautazott.',
                                                                           'Mert a tolmács nem jött el a megbeszélésre '
                                                                           'tegnap délután.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kolléga',
                                                                              'text': 'Hogyan értékelték a hivatalos '
                                                                                      'szervek a mérnök váratlan '
                                                                                      'hiányzását?'},
                                                                          {'speaker': 'Asszony', 'text': '_____'}],
                                                            'options': [   'Óvatos eufemizmusokkal közölték, hogy a '
                                                                           'mérnök más megbízatást kapott a '
                                                                           'minisztériumtól.',
                                                                           'Azonnal feljelentették őt a rendőrségen '
                                                                           'sikkasztás vádjával.',
                                                                           'Alighogy lecsukta a szemét a szobában, '
                                                                           'elfelejtette a címét.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: It seems that the '
                                                                                         'criticism was somewhat '
                                                                                         'exaggerated, but we must be '
                                                                                         'cautious.',
                                                                               'answer': 'Úgy tűnik, a bírálat '
                                                                                         'némiképp túlzó volt, de '
                                                                                         'óvatosnak kell lennünk.'}],
                                                           'teaches': ['b2-agent-backgrounding']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: In a certain sense, '
                                                                                         'the misunderstanding helped '
                                                                                         'clarify our positions.',
                                                                               'answer': 'Bizonyos értelemben a '
                                                                                         'félreértés segített '
                                                                                         'tisztázni az '
                                                                                         'álláspontunkat.'}],
                                                           'teaches': ['b2-agent-backgrounding']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the verb 'finomít' mean in the context "
                                                                     'of drafting texts?',
                                                         'options': [   'to refine / soften / tone down phrasing',
                                                                        'to make something completely sharp',
                                                                        'to erase entirely'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A jelentés megállapításai ____ eltérnek a '
                                                                     'korábbi várakozásoktól. (slightly)',
                                                         'answer': 'némiképp',
                                                         'english': "The report's findings differ slightly from "
                                                                    'earlier expectations.',
                                                         'teaches': ['b2-agent-backgrounding']}]}},
                   {   'num': 4,
                       'title': 'Decoding Double Meaning',
                       'grammar_label': 'Interpreting subtext: Aesopian language, allusions, and ambiguity',
                       'goals': [   'I can recognize Aesopian language and indirect political subtext in historical '
                                    'texts.',
                                    'I can read between the lines (a sorok között olvas) in state-controlled or '
                                    'constrained media.',
                                    'I can identify ambiguous phrasing (kétértelmű fogalmazás) designed to evade '
                                    'censorship.'],
                       'grammar_doc': {   'slug': 'decoding-double-meaning',
                                          'title': 'Aesopian Language and Subtext: Reading Between the Lines',
                                          'text1_title': 'Ezópusi nyelv (Aesopian Language)',
                                          'text1': 'Under authoritarian censorship in Central Europe, writers and '
                                                   "journalists developed 'ezópusi nyelv' (Aesopian language)—using "
                                                   'historical allegories, animal fables, and coded references '
                                                   "('utalás') to convey forbidden political truths. Words carried "
                                                   "dual meanings ('kétértelmű'), allowing the public to understand "
                                                   'what the censor could not formally prove.',
                                          'text2_title': 'Reading Between the Lines (a sorok között)',
                                          'text2': "'A sorok között olvasni' (to read between the lines) is a vital "
                                                   'cultural skill. Texts conceal multiple layers of meaning '
                                                   "('jelentésréteg'). The author criticizes covertly ('rejtetten "
                                                   "bírál'), relying on shared cultural memory rather than overt "
                                                   "accusations. Déry's Niki uses the physical suffering of a dog to "
                                                   'portray the unmentionable anguish of an entire terrorized society.',
                                          'table_title': 'Aesopian Rhetorical Devices',
                                          'table_rows': [   [   'a sorok között olvas',
                                                                'to read between the lines (perceive concealed '
                                                                'subtext)'],
                                                            [   'kétértelmű fogalmazás',
                                                                'ambiguous / double-edged wording'],
                                                            ['burkolt utalás', 'veiled allusion / coded reference'],
                                                            ['rejtetten bírálni', 'to criticize covertly / subtly']],
                                          'examples': [   {   'spanish': 'A művelt olvasóközönség azonnal tudott a '
                                                                         'sorok között olvasni.',
                                                              'english': 'The educated reading public knew immediately '
                                                                         'how to read between the lines.'},
                                                          {   'spanish': 'A történelmi dráma valójában a jelenkor '
                                                                         'zsarnokságára tett burkolt utalás volt.',
                                                              'english': 'The historical drama was in fact a veiled '
                                                                         'allusion to present-day tyranny.'},
                                                          {   'spanish': 'A megfogalmazás szándékosan kétértelmű '
                                                                         'maradt a cenzorok miatt.',
                                                              'english': 'The phrasing remained deliberately ambiguous '
                                                                         'due to the censors.'},
                                                          {   'spanish': 'A novella több mélyebb jelentésréteget '
                                                                         'hordoz magában.',
                                                              'english': 'The short story carries multiple deeper '
                                                                         'layers of meaning within itself.'}],
                                          'tip': 'When analyzing historical texts, look for what is omitted: what is '
                                                 "unsaid ('elhallgatott') is often the most important theme."},
                       'words': [   {   'lemma': 'kétértelmű',
                                        'translation': 'ambiguous, double-edged',
                                        'pos': 'adjective'},
                                    {'lemma': 'sorok között', 'translation': 'between the lines', 'pos': 'expression'},
                                    {'lemma': 'utalás', 'translation': 'allusion, reference', 'pos': 'noun'},
                                    {'lemma': 'rejtetten', 'translation': 'covertly, secretly', 'pos': 'adverb'},
                                    {'lemma': 'jelentésréteg', 'translation': 'layer of meaning', 'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the expression 'a sorok között "
                                                                     "olvasni' mean?",
                                                         'options': [   'to read between the lines (understand hidden '
                                                                        'subtext)',
                                                                        'to underline every word with a pencil',
                                                                        'to read aloud slowly'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'What is Aesopian language (ezópusi nyelv) in '
                                                                     'Hungarian literary history?',
                                                         'options': [   'Indirect, allegorical phrasing used to convey '
                                                                        'truth without alerting censors.',
                                                                        'The ancient Greek dialect used by '
                                                                        'philosophers in Athens.',
                                                                        'A computer programming language used for '
                                                                        'statistics.'],
                                                         'correct': 0,
                                                         'teaches': ['b2-agent-backgrounding']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   ['kétértelmű', 'ambiguous / double-edged'],
                                                                           ['sorok között', 'between the lines'],
                                                                           ['utalás', 'allusion / reference'],
                                                                           ['rejtetten', 'covertly / secretly'],
                                                                           ['jelentésréteg', 'layer of meaning']],
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'A művelt közönség azonnal tudott a ____ '
                                                                          'olvasni a diktatúra idején. (between the '
                                                                          'lines)',
                                                              'answer': 'sorok között',
                                                              'english': 'The educated public knew immediately how to '
                                                                         'read between the lines during the '
                                                                         'dictatorship.',
                                                              'teaches': ['b2-agent-backgrounding']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A történelmi dráma valójában a jelenkor '
                                                                          'zsarnokságára tett burkolt ____. (allusion)',
                                                              'answer': 'utalás',
                                                              'english': 'The historical drama was in fact a veiled '
                                                                         'allusion to present-day tyranny.',
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which sentence describes a literary work '
                                                                          'with coded depth?',
                                                              'options': [   'A novella mélyebb jelentésrétegei csak a '
                                                                             'gondos újraolvasás során tárulnak fel.',
                                                                             'A könyv pontosan százötven oldalból áll '
                                                                             'és kék a borítója.',
                                                                             'Tegnap este a polcra tettem a könyvtári '
                                                                             'regényt.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-agent-backgrounding']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'szerző',
                                                                         'rejtetten',
                                                                         'bírálta',
                                                                         'a',
                                                                         'rendszer',
                                                                         'igazságtalan',
                                                                         'döntéseit',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'szerző',
                                                                            'rejtetten',
                                                                            'bírálta',
                                                                            'a',
                                                                            'rendszer',
                                                                            'igazságtalan',
                                                                            'döntéseit',
                                                                            '.'],
                                                            'english': "The author covertly criticized the system's "
                                                                       'unjust decisions.',
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A megfogalmazás szándékosan kétértelmű '
                                                                             'volt a cikkben.',
                                                            'base_word': 'kétértelmű',
                                                            'options': [   {   'word': 'óvatos',
                                                                               'inflected': 'óvatos',
                                                                               'sentence': 'A megfogalmazás '
                                                                                           'szándékosan óvatos volt a '
                                                                                           'cikkben.',
                                                                               'gloss': 'cautious'},
                                                                           {   'word': 'finomított',
                                                                               'inflected': 'finomított',
                                                                               'sentence': 'A megfogalmazás '
                                                                                           'szándékosan finomított '
                                                                                           'volt a cikkben.',
                                                                               'gloss': 'softened'}],
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A szöveg több egymásra épülő ____ tartalmaz '
                                                                        'az avatott szemlélő számára. (layers of '
                                                                        'meaning)',
                                                            'answer': 'jelentésréteget',
                                                            'english': 'The text contains multiple overlapping layers '
                                                                       'of meaning for the initiated viewer.',
                                                            'teaches': ['b2-15-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': "In Déry Tibor's Niki, how is political "
                                                                        'persecution conveyed?',
                                                            'options': [   'Nem politikai jelszavakkal, hanem a '
                                                                           'mindennapi hiány és a kutya szenvedésének '
                                                                           'ábrázolásával.',
                                                                           'Nyílt parlamenti viták szó szerinti '
                                                                           'jegyzőkönyveivel.',
                                                                           'Kizárólag angol nyelvű idézetekkel.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Egyetemista',
                                                                              'text': 'Hogyan tudtak a magyar írók '
                                                                                      'társadalmi kritikát '
                                                                                      'megfogalmazni az ötvenes '
                                                                                      'években?'},
                                                                          {'speaker': 'Professzor', 'text': '_____'}],
                                                            'options': [   'Történelmi parabolákkal, szimbolikus '
                                                                           'állattörténetekkel és a sorok közé rejtett '
                                                                           'utalásokkal.',
                                                                           'Úgy, hogy mindent nyíltan bekiabáltak a '
                                                                           'minisztérium folyosóján.',
                                                                           'Mert a cenzúra kifejezetten támogatta a '
                                                                           'rendszer elleni lázadást.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Kutató',
                                                                              'text': 'Miért volt kétértelmű a '
                                                                                      'hatóságok válasza a mérnök '
                                                                                      'feleségének levelére?'},
                                                                          {'speaker': 'Történész', 'text': '_____'}],
                                                            'options': [   'Mert nem merték leírni a letartóztatás '
                                                                           'tényét, de elismerni sem akarták az '
                                                                           'ártatlanságát.',
                                                                           'Mivel a gépírónő véletlenül kétszer '
                                                                           'nyomtatta ki az oldalt a gépen.',
                                                                           'Igen, hiszen a miniszter személyesen '
                                                                           'ismerte a kutyát a parkból.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: Under censorship, '
                                                                                         'readers learn to read '
                                                                                         'between the lines.',
                                                                               'answer': 'A cenzúra idején az olvasók '
                                                                                         'megtanulnak a sorok között '
                                                                                         'olvasni.'}],
                                                           'teaches': ['b2-agent-backgrounding']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The novel criticizes '
                                                                                         'dictatorship through subtle '
                                                                                         'allusions.',
                                                                               'answer': 'A regény finom utalásokon '
                                                                                         'keresztül bírálja a '
                                                                                         'diktatúrát.'}],
                                                           'teaches': ['b2-agent-backgrounding']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the adjective 'kétértelmű' mean?",
                                                         'options': [   'ambiguous / having multiple interpretations',
                                                                        'completely obvious',
                                                                        'grammatically incorrect'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A színpadi előadás után mindenki megértette a '
                                                                     'jelenet rejtett ____. (meaning)',
                                                         'answer': 'értelmét',
                                                         'english': 'After the stage performance, everyone understood '
                                                                    'the hidden meaning of the scene.',
                                                         'teaches': ['b2-agent-backgrounding']}]}},
                   {   'num': 5,
                       'title': 'Rewriting Blunt Statements Diplomatically',
                       'grammar_label': 'Synthesizing impersonal style: converting direct blame into diplomatic prose',
                       'goals': [   'I can rewrite aggressive, accusatory sentences into polished, impersonal '
                                    'administrative Hungarian.',
                                    'I can draft formal letters and public statements that clarify positions without '
                                    'provoking conflict.',
                                    "I can analyze the human cost of bureaucratic obfuscation in Déry Tibor's Niki."],
                       'grammar_doc': {   'slug': 'diplomatic-rewriting-synthesis',
                                          'title': 'From Confrontation to Restraint: The Art of Diplomatic Phrasing',
                                          'text1_title': 'Three Rules of Diplomatic Transformation',
                                          'text1': "Converting a confrontational sentence ('Te hibáztál, és rossz "
                                                   "döntést hoztál') into diplomatic Hungarian involves three "
                                                   'systematic shifts: 1) replacing 2nd-person accusations with '
                                                   "impersonal noun phrases ('félreértés történt'), 2) using nominal "
                                                   "periphrases with 'kerül' or 'szorul' ('a döntés felülvizsgálatra "
                                                   "szorul'), and 3) inserting mitigating adverbs ('némiképp', 'úgy "
                                                   "tűnik').",
                                          'text2_title': 'Focusing on Problem Resolution Rather than Guilt',
                                          'text2': "An objective, matter-of-fact tone ('tárgyilagos hangnem') "
                                                   'separates the disputed facts from personal egos. Verbs like '
                                                   "'tisztáz' (to clarify) and nouns like 'álláspont' (standpoint / "
                                                   'position) allow parties to save face while resolving contentious '
                                                   "matters ('kérdések tisztázása').",
                                          'table_title': 'Confrontational vs. Diplomatic Phrasing',
                                          'table_rows': [   [   'Nem mondasz igazat!',
                                                                'Az adatok bizonyos pontosításra szorulnak.'],
                                                            [   'Elrontottátok a szerződést!',
                                                                'Úgy tűnik, a szerződéstervezet némiképp módosításra '
                                                                'kerül.'],
                                                            [   'Azonnal fizessetek kártérítést!',
                                                                'A kárrendezés kérdése megvitatásra kerül.'],
                                                            [   'álláspontot tisztázni',
                                                                'to clarify positions constructively']],
                                          'examples': [   {   'spanish': 'A tárgyilagos hangnem segít tisztázni a '
                                                                         'vitatott kérdéseket.',
                                                              'english': 'An objective tone helps clarify the disputed '
                                                                         'questions.'},
                                                          {   'spanish': 'Kérjük a feleket, hogy képviseljék a '
                                                                         'kérdésben a saját álláspontjukat.',
                                                              'english': 'We ask the parties to represent their own '
                                                                         'standpoint on the matter.'},
                                                          {   'spanish': 'A hivatalos levél gondos fogalmazása '
                                                                         'megelőzte a konfliktust.',
                                                              'english': 'The careful drafting of the official letter '
                                                                         'prevented conflict.'},
                                                          {   'spanish': 'Az ügy felülvizsgálatra került, és '
                                                                         'diplomáciai átirat készült.',
                                                              'english': 'The matter was reviewed and a diplomatic '
                                                                         'rewrite was prepared.'}],
                                          'tip': "Focus entirely on the issue ('a probléma megoldása'), never on "
                                                 "attacking the person ('a te hibád')."},
                       'words': [   {   'lemma': 'fogalmazás',
                                        'translation': 'wording, phrasing, drafting',
                                        'pos': 'noun'},
                                    {   'lemma': 'tárgyilagos',
                                        'translation': 'objective, matter-of-fact',
                                        'pos': 'adjective'},
                                    {   'lemma': 'átirat',
                                        'translation': 'transcription, rewrite, adaptation',
                                        'pos': 'noun'},
                                    {'lemma': 'tisztáz', 'translation': 'to clarify, clear up', 'pos': 'verb'},
                                    {   'lemma': 'álláspont',
                                        'translation': 'standpoint, position, point of view',
                                        'pos': 'noun'}],
                       'exercises': {   'intro': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'introduce',
                                                         'question': "What does the adjective 'tárgyilagos' mean in "
                                                                     'administrative and critical contexts?',
                                                         'options': [   'objective / matter-of-fact / impartial',
                                                                        'highly emotional and aggressive',
                                                                        'written in verse'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'multiple-choice',
                                                         'category': 'grammar',
                                                         'stage': 'introduce',
                                                         'question': 'How do we convert an accusatory statement into '
                                                                     'diplomatic Hungarian?',
                                                         'options': [   "Focus on the process impersonally: 'Úgy "
                                                                        "tűnik, a kérdés további tisztázásra szorul'.",
                                                                        'Use capital letters and multiple exclamation '
                                                                        'marks.',
                                                                        'Threaten the other party with immediate '
                                                                        'punishment.'],
                                                         'correct': 0,
                                                         'teaches': ['b2-agent-backgrounding']}],
                                        'controlled': [   {   'type': 'matching',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'pairs': [   [   'fogalmazás',
                                                                               'wording / phrasing / drafting'],
                                                                           [   'tárgyilagos',
                                                                               'objective / matter-of-fact'],
                                                                           ['átirat', 'rewrite / adaptation'],
                                                                           ['tisztáz', 'to clarify / clear up'],
                                                                           ['álláspont', 'standpoint / position']],
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'sentence': 'Kérjük a feleket, hogy határozottan '
                                                                          'képviseljék a kérdésben saját ____. '
                                                                          '(standpoint)',
                                                              'answer': 'álláspontjukat',
                                                              'english': 'We ask the parties to firmly represent their '
                                                                         'own standpoint on the matter.',
                                                              'teaches': ['b2-agent-backgrounding']},
                                                          {   'type': 'fill-blank',
                                                              'category': 'vocabulary',
                                                              'stage': 'controlled',
                                                              'sentence': 'A hivatalos válaszlevél gondos ____ '
                                                                          'megelőzte a felesleges vitát. (drafting)',
                                                              'answer': 'fogalmazása',
                                                              'english': 'The careful drafting of the official '
                                                                         'response letter prevented unnecessary '
                                                                         'dispute.',
                                                              'teaches': ['b2-15-vocab']},
                                                          {   'type': 'multiple-choice',
                                                              'category': 'grammar',
                                                              'stage': 'controlled',
                                                              'question': 'Which version is the most diplomatic '
                                                                          "rewrite of 'A cég hazudott a számokról'?",
                                                              'options': [   'A közzétett adatok bizonyos tekintetben '
                                                                             'pontosításra szorulnak.',
                                                                             'A cég vezetői mind csalók és bűnözők!',
                                                                             'Tegnap délben zárva volt a cég központi '
                                                                             'irodája.'],
                                                              'correct': 0,
                                                              'teaches': ['b2-agent-backgrounding']}],
                                        'practice': [   {   'type': 'sentence-builder',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'tiles': [   'A',
                                                                         'tárgyilagos',
                                                                         'hangnem',
                                                                         'segít',
                                                                         'tisztázni',
                                                                         'a',
                                                                         'vitatott',
                                                                         'kérdéseket',
                                                                         '.'],
                                                            'solution': [   'A',
                                                                            'tárgyilagos',
                                                                            'hangnem',
                                                                            'segít',
                                                                            'tisztázni',
                                                                            'a',
                                                                            'vitatott',
                                                                            'kérdéseket',
                                                                            '.'],
                                                            'english': 'An objective tone helps clarify the disputed '
                                                                       'questions.',
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'substitution',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'base_sentence': 'A kérdés tisztázása mindkét fél érdeke.',
                                                            'base_word': 'tisztázása',
                                                            'options': [   {   'word': 'megvitatása',
                                                                               'inflected': 'megvitatása',
                                                                               'sentence': 'A kérdés megvitatása '
                                                                                           'mindkét fél érdeke.',
                                                                               'gloss': 'discussion'},
                                                                           {   'word': 'megoldása',
                                                                               'inflected': 'megoldása',
                                                                               'sentence': 'A kérdés megoldása mindkét '
                                                                                           'fél érdeke.',
                                                                               'gloss': 'resolution'}],
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'fill-blank',
                                                            'category': 'vocabulary',
                                                            'stage': 'practice',
                                                            'sentence': 'A diplomáciai tárgyalásokon alapvető elvárás '
                                                                        'a higgadt és ____ megközelítés. (objective)',
                                                            'answer': 'tárgyilagos',
                                                            'english': 'In diplomatic negotiations, a calm and '
                                                                       'objective approach is a fundamental '
                                                                       'expectation.',
                                                            'teaches': ['b2-15-vocab']},
                                                        {   'type': 'multiple-choice',
                                                            'category': 'grammar',
                                                            'stage': 'practice',
                                                            'question': 'How does passive-avoidance through '
                                                                        'nominalization support a diplomatic tone?',
                                                            'options': [   'Elveszi a közvetlen vád élét azáltal, hogy '
                                                                           'nem nevezi meg a konkrét bűnöst.',
                                                                           'Kötelezővé teszi a latin szavak '
                                                                           'használatát a levélben.',
                                                                           'Lehetővé teszi, hogy senki ne válaszoljon '
                                                                           'a kérdésekre.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'dialogue': [   {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Titkár',
                                                                              'text': 'Hogyan válaszoljunk erre a '
                                                                                      'kifejezetten agresszív '
                                                                                      'hangvételű panaszra?'},
                                                                          {'speaker': 'Igazgató', 'text': '_____'}],
                                                            'options': [   'Válaszoljunk higgadtan és tárgyilagosan, '
                                                                           'tisztázva a tényeket személyeskedés '
                                                                           'nélkül.',
                                                                           'Azonnal hívjuk fel a rendőrséget és '
                                                                           'pereljük be az ügyfelet.',
                                                                           'Tépjük szét a panaszt, és tegyünk úgy, '
                                                                           'mintha meg sem érkezett volna.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']},
                                                        {   'type': 'dialogue-complete',
                                                            'category': 'dialogue',
                                                            'stage': 'dialogue',
                                                            'prompt': [   {   'speaker': 'Olvasó',
                                                                              'text': 'Mi a tanulsága Ancsa Jánosné '
                                                                                      'tragikus küzdelmének Déry '
                                                                                      'regényében?'},
                                                                          {'speaker': 'Kritikus', 'text': '_____'}],
                                                            'options': [   'A hűség és az erkölcsi tisztesség '
                                                                           'felülmúlja a személytelen önkényuralmi '
                                                                           'gépezetet.',
                                                                           'Hogy a mérnököknek tilos vadászkutyát '
                                                                           'tartaniuk a budai lakásban.',
                                                                           'Hogy a minisztérium minden beadványt '
                                                                           'huszonnégy órán belül teljesített.'],
                                                            'correct': 0,
                                                            'teaches': ['b2-agent-backgrounding']}],
                                        'writing': [   {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: An objective tone '
                                                                                         'helps clarify positions '
                                                                                         'without hurting others.',
                                                                               'answer': 'A tárgyilagos hangnem segít '
                                                                                         'tisztázni az álláspontokat '
                                                                                         'mások megbántása nélkül.'}],
                                                           'teaches': ['b2-agent-backgrounding']},
                                                       {   'type': 'structured-writing',
                                                           'category': 'writing',
                                                           'stage': 'production',
                                                           'template': [   {   'prompt': 'Write: The matter was '
                                                                                         'reviewed and a diplomatic '
                                                                                         'rewrite was prepared.',
                                                                               'answer': 'Az ügy felülvizsgálatra '
                                                                                         'került, és diplomáciai '
                                                                                         'átirat készült.'}],
                                                           'teaches': ['b2-agent-backgrounding']}],
                                        'check': [   {   'type': 'multiple-choice',
                                                         'category': 'vocabulary',
                                                         'stage': 'check',
                                                         'question': "What does the verb 'tisztáz' mean?",
                                                         'options': [   'to clarify / clear up',
                                                                        'to muddy the waters',
                                                                        'to arrest without warrant'],
                                                         'correct': 0,
                                                         'teaches': ['b2-15-vocab']},
                                                     {   'type': 'fill-blank',
                                                         'category': 'grammar',
                                                         'stage': 'check',
                                                         'sentence': 'A helyzet békés rendezése érdekében '
                                                                     'felülvizsgálatra szorul az eddigi ____. '
                                                                     '(standpoint)',
                                                         'answer': 'álláspont',
                                                         'english': 'In the interest of a peaceful resolution of the '
                                                                    'situation, the standpoint held so far needs '
                                                                    'review.',
                                                         'teaches': ['b2-agent-backgrounding']}]}}],
    'consolidation': {   'goals': [   'I can background the agent naturally using 3rd-person plural verbs and middle '
                                      'verbs in -ódik/-ődik.',
                                      'I can formulate administrative sentences with -ásra/-ésre kerül and decode '
                                      'euphemisms.',
                                      'I can rewrite confrontational accusations into diplomatic, objective prose.'],
                         'exercises': [   {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': 'Which construction represents natural Hungarian '
                                                          'agent-backgrounding instead of passive voice?',
                                              'options': [   '3rd-person plural verbs: letartóztatták, betiltották',
                                                             'Past conditional: lett volna tiltva',
                                                             'Nominal suffix: -hatnék'],
                                              'correct': 0,
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'recognize',
                                              'question': "What does the adjective 'tárgyilagos' mean?",
                                              'options': [   'objective / matter-of-fact',
                                                             'overly passionate',
                                                             'ironically bitter'],
                                              'correct': 0,
                                              'teaches': ['b2-15-vocab']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'recognize',
                                              'question': "What does '-ásra/-ésre kerül' express in official Hungarian "
                                                          'prose?',
                                              'options': [   'administrative passive-avoidance (an action being '
                                                             'performed or implemented)',
                                                             'a spatial movement into a room',
                                                             'a polite greeting between colleagues'],
                                              'correct': 0,
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'fill-blank',
                                              'category': 'vocabulary',
                                              'stage': 'recall',
                                              'sentence': 'A diktatúrában a sajtó-____ minden rendszerkritikus cikket '
                                                          'megsemmisített. (censorship)',
                                              'answer': 'cenzúra',
                                              'english': 'Under the dictatorship, press censorship destroyed every '
                                                         'article critical of the regime.',
                                              'teaches': ['b2-15-vocab']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': 'A kényes kérdés a jövő heti konferencián érdemben '
                                                          'megvitatásra ____. (will be / comes)',
                                              'answer': 'kerül',
                                              'english': 'The delicate question will be discussed in earnest at next '
                                                         "week's conference.",
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'fill-blank',
                                              'category': 'grammar',
                                              'stage': 'recall',
                                              'sentence': 'Úgy tűnik, hogy a döntés ____ túlzott óvatosságból fakadt. '
                                                          '(somewhat)',
                                              'answer': 'némiképp',
                                              'english': 'It seems that the decision stemmed somewhat from excessive '
                                                         'caution.',
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'dialogue-complete',
                                              'category': 'dialogue',
                                              'stage': 'in-context',
                                              'prompt': [   {   'speaker': 'Történész',
                                                                'text': 'Hogyan élték túl az emberek a legsötétebb '
                                                                        'önkényuralmi éveket?'},
                                                            {'speaker': 'Író', 'text': '_____'}],
                                              'options': [   'Megtanultak a sorok között olvasni, és a csendben '
                                                             'őrizték meg emberi méltóságukat.',
                                                             'Mindennap hangos felvonulást tartottak az utcán katonai '
                                                             'zenével.',
                                                             'Mivel semmiféle probléma nem létezett a korabeli '
                                                             'társadalomban.'],
                                              'correct': 0,
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'multiple-choice',
                                              'category': 'grammar',
                                              'stage': 'in-context',
                                              'question': "Which rewrite of 'Ti elrontottátok a szerződést' is best "
                                                          'suited for formal business communication?',
                                              'options': [   'Úgy tűnik, a szerződés tervezete némiképp módosításra '
                                                             'szorul.',
                                                             'Ti tehettek mindenről, azonnal fizessetek kártérítést!',
                                                             'A szerződés tegnap az asztalon maradt a tárgyalóban.'],
                                              'correct': 0,
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'multiple-choice',
                                              'category': 'vocabulary',
                                              'stage': 'in-context',
                                              'question': "Which Hungarian expression means 'to read between the "
                                                          "lines'?",
                                              'options': [   'a sorok között olvas',
                                                             'a sor végére áll',
                                                             'sorban áll a pénztárnál'],
                                              'correct': 0,
                                              'teaches': ['b2-15-vocab']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'A',
                                                           'törvény',
                                                           'a',
                                                           'hétfői',
                                                           'ülésen',
                                                           'elfogadásra',
                                                           'került',
                                                           '.'],
                                              'solution': [   'A',
                                                              'törvény',
                                                              'a',
                                                              'hétfői',
                                                              'ülésen',
                                                              'elfogadásra',
                                                              'került',
                                                              '.'],
                                              'english': 'The law was adopted at the Monday session.',
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'sentence-builder',
                                              'category': 'grammar',
                                              'stage': 'produce',
                                              'tiles': [   'A',
                                                           'nehéz',
                                                           'helyzet',
                                                           'idővel',
                                                           'magától',
                                                           'megoldódott',
                                                           '.'],
                                              'solution': [   'A',
                                                              'nehéz',
                                                              'helyzet',
                                                              'idővel',
                                                              'magától',
                                                              'megoldódott',
                                                              '.'],
                                              'english': 'The difficult situation resolved itself in time on its own.',
                                              'teaches': ['b2-agent-backgrounding']},
                                          {   'type': 'structured-writing',
                                              'category': 'writing',
                                              'stage': 'produce',
                                              'template': [   {   'prompt': 'Write: Under censorship, authors use '
                                                                            'Aesopian language and subtle allusions.',
                                                                  'answer': 'A cenzúra idején a szerzők ezópusi '
                                                                            'nyelvet és finom utalásokat használnak.'}],
                                              'teaches': ['b2-agent-backgrounding']}]}}


def main():
    for unit_spec in (UNIT_13, UNIT_14, UNIT_15):
        build_core_unit(unit_spec)
    print("Successfully generated Hungarian B2 Core Units 13, 14, and 15.")


if __name__ == "__main__":
    main()
