# -*- coding: utf-8 -*-
"""
Unit 6 Overhaul: The Mongol Invasion (1241–42) (b1-tatarjaras)
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(".")
LESSONS_DIR = ROOT / "content/hu/lessons/b1"
GRAMMAR_DIR = ROOT / "content/hu/grammar/b1"
VOCAB_DIR = ROOT / "content/hu/vocabulary/b1"
EXERCISES_DIR = ROOT / "content/hu/exercises/b1"
STORIES_DIR = ROOT / "content/hu/stories/world/b1"

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def make_story(id_str, title, summary, location, grammar_topics, vocab_topics, paragraphs_text, key_voc, comp_questions):
    paras = [{"type": "narration", "text": p} for p in paragraphs_text]
    total_time = 0.0
    segments = []
    for i, p in enumerate(paragraphs_text):
        dur = max(4.0, round(len(p.split()) * 0.45, 1))
        start = total_time
        end = round(start + dur, 1)
        total_time = end
        segments.append({
            "paraIndex": i,
            "startTime": start,
            "endTime": end,
            "speaker": "Narrator",
            "lang": "hu",
            "cues": [{"type": "pause", "durationMs": 250, "reason": "clause-boundary"}] if i < len(paragraphs_text)-1 else [],
            "pronunciations": []
        })

    return {
        "id": id_str,
        "title": title,
        "level": "B1",
        "estimatedMinutes": 5,
        "summary": summary,
        "characters": [],
        "location": location,
        "grammar": grammar_topics,
        "vocabularyTopics": vocab_topics,
        "paragraphs": paras,
        "narration": {
            "durationSeconds": total_time,
            "pacing": {
                "speedMultiplier": 1.0,
                "rate_str": "+0%",
                "rate_wpm": 150,
                "style": "natural, expressive"
            },
            "speakers": {
                "Narrator": {
                    "role": "narrator",
                    "gender": "neutral",
                    "tone": "clear, warm, steady storytelling guide"
                }
            },
            "segments": segments,
            "pedagogical": {
                "keyVocabulary": key_voc,
                "targetGrammar": grammar_topics,
                "comprehensionQuestions": comp_questions
            }
        }
    }

def make_lesson(lesson_id, title, grammar_label, intro_body, goals, story_ref, voc_ref, gr_ref, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title.split(" - ")[0] if " - " in title else title, "body": intro_body},
        {"type": "goal", "title": "Lesson Goals", "items": goals},
        {"type": "recycle", "count": 3},
        {"type": "story", "ref": story_ref},
        {"type": "vocabulary", "ref": voc_ref},
        {"type": "grammar", "ref": gr_ref},
        {"type": "exercise-group", "title": "Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "srs"},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "grammar": grammar_label,
        "sections": sections,
        "goal": goals
    }

def make_consolidation_lesson(lesson_id, title, intro_body, goals, story_ref, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title.split(" - ")[0] if " - " in title else title, "body": intro_body},
        {"type": "goal", "title": "Unit Goals", "items": goals},
        {"type": "recycle", "count": 4},
        {"type": "story", "ref": story_ref},
        {"type": "exercise-group", "title": "Consolidation Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "srs"},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "grammar": "összefoglalás és ismétlés",
        "sections": sections,
        "goal": goals
    }

# -----------------
# Lesson 1: Julianus barát és a tatár fenyegetés
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras-01-tatarokerkezese.json", make_story(
    "story.b1.tatarjaras.01",
    "Julianus barát utazása és a közeledő vihar (1235–1241)",
    "Friar Julian's journey to the East (1235) discovering Magna Hungaria, his return with Batu Khan's warning letter, and the arrival of Cuman refugees under Kötöny.",
    "Volga vidéke és Pest",
    ["időhatározói viszonyok és előrejelző szerkezetek"],
    ["Julianus barát", "Magna Hungaria", "Mongol fenyegetés", "Kunok befogadása"],
    [
        "1235-ben Julianus domonkos rendi szerzetes három társával keletre indult, hogy felkutassa a keleten maradt ősmagyarokat. Hosszú és veszélyes út után a Volga folyó mellett rátalált Magna Hungariára, ahol a helyiekkel még magyarul tudott beszélni.",
        "Második keleti utazásakor Julianus már a megállíthatatlanul előrenyomuló mongol (tatár) világbirodalommal találkozott, és Batu kán fenyegető levelével tért vissza IV. Béla királyhoz.",
        "A mongolok elől menekülő Kötöny kun fejedelem negyvenezer harcosával menedéket kért és kapott a magyar királytól az Alföldön.",
        "A magyar főurak és a nomád kunok között azonban súlyos feszültség alakult ki. Amikor a tatár seregek 1241 tavaszán áttörték a Vereckei-hágó torlaszait, a pesti felkelők meggyilkolták Kötönyt.",
        "A feldühödött kunok rabolva és pusztítva kivonultak az országból dél felé, éppen akkor fosztva meg IV. Bélát legfontosabb könnyűlovas szövetségesétől, amikor a tatár fősereg már a Duna felé közeledett."
    ],
    [
        {"lemma": "szerzetes", "pos": "noun", "cefr": "B1", "gloss": "monk / friar"},
        {"lemma": "fenyegető levél", "pos": "noun", "cefr": "B1", "gloss": "threatening letter / ultimatum"},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "gloss": "refuge / shelter"},
        {"lemma": "könnyűlovasság", "pos": "noun", "cefr": "B1", "gloss": "light cavalry"}
    ],
    [
        {
            "question": "Mit fedezett fel Julianus barát 1235-ös keleti utazása során?",
            "options": ["A Volga mentén élő keleti magyarokat (Magna Hungaria)", "Egy lakatlan új kontinenst", "A római császár aranybányáit", "Egy elfelejtett piramist"],
            "correctIndex": 0,
            "explanation": "Julianus barát rátalált a Volga vidékén maradt magyarokra, akikkel saját nyelvén beszélt."
        },
        {
            "question": "Milyen veszélyes hírt hozott Julianus második útja után IV. Béla királynak?",
            "options": ["Batu kán és a mongol hadsereg közeledését és fenyegető levelét", "Egy gazdag kereskedelmi békét", "Hogy a mongolok békésen visszafordultak", "A római pápa látogatását"],
            "correctIndex": 0,
            "explanation": "Julianus hozta el Batu kán levelét, amely a tatár invázió közvetlen veszélyére figyelmeztetett."
        },
        {
            "question": "Mi történt a kunokkal közvetlenül a tatár betörés előtt?",
            "options": ["Kötöny vezért meggyilkolták Pesten, a kunok pedig pusztítva elhagyták az országot", "A kunok legyőzték a tatárokat egyedül", "A kunok királyává koronázták Kötönyt", "Minden kun elhajózott Amerikába"],
            "correctIndex": 0,
            "explanation": "Kötöny meggyilkolása miatt a kunok kivonultak, megfosztva a királyt a könnyűlovas erősítéstől."
        }
    ]
))

write_json(VOCAB_DIR / "b1-tatarjaras-01-voc.json", {
    "title": "Julianus barát és a tatár fenyegetés",
    "words": [
        {"lemma": "szerzetes", "pos": "noun", "cefr": "B1", "translation": "monk / friar", "examples": [{"hungarian": "Julianus domonkos szerzetes volt.", "english": "Julian was a Dominican friar."}]},
        {"lemma": "fenyegető levél", "pos": "noun", "cefr": "B1", "translation": "threatening letter / ultimatum", "examples": [{"hungarian": "Batu kán fenyegető levelet küldött a királynak.", "english": "Batu Khan sent a threatening letter to the king."}]},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "translation": "refuge / shelter", "examples": [{"hungarian": "A kunok menedéket kerestek Magyarországon.", "english": "The Cumans sought refuge in Hungary."}]},
        {"lemma": "könnyűlovasság", "pos": "noun", "cefr": "B1", "translation": "light cavalry", "examples": [{"hungarian": "A kun könnyűlovasság hiányzott a döntő csatában.", "english": "The Cuman light cavalry was missing in the decisive battle."}]},
        {"lemma": "felkutat", "pos": "verb", "cefr": "B1", "translation": "to track down / search out", "examples": [{"hungarian": "Felkutatta a keleten maradt ősmagyarokat.", "english": "He searched out the ancient Magyars remaining in the east."}]},
        {"lemma": "előrenyomul", "pos": "verb", "cefr": "B1", "translation": "to advance / press forward", "examples": [{"hungarian": "A tatár seregek gyorsan nyomultak előre.", "english": "The Tatar armies advanced rapidly."}]},
        {"lemma": "feszültség", "pos": "noun", "cefr": "B1", "translation": "tension", "examples": [{"hungarian": "Súlyos feszültség keletkezett a főurak és a kunok között.", "english": "Severe tension arose between the lords and the Cumans."}]},
        {"lemma": "torlasz", "pos": "noun", "cefr": "B1", "translation": "barricade / roadblock", "examples": [{"hungarian": "Fa torlaszokkal zárták le a hágókat.", "english": "They closed the passes with wooden barricades."}]},
        {"lemma": "meggyilkol", "pos": "verb", "cefr": "B1", "translation": "to murder / assassinate", "examples": [{"hungarian": "A pesti tömeg meggyilkolta Kötöny vezért.", "english": "The Pest crowd murdered Chieftain Kötöny."}]},
        {"lemma": "kivonul", "pos": "verb", "cefr": "B1", "translation": "to withdraw / march out", "examples": [{"hungarian": "A kunok kivonultak az országból dél felé.", "english": "The Cumans marched out of the country to the south."}]},
        {"lemma": "megfoszt", "pos": "verb", "cefr": "B1", "translation": "to deprive of", "examples": [{"hungarian": "A viszály megfosztotta a királyt a seregtől.", "english": "The strife deprived the king of the army."}]},
        {"lemma": "közeledik", "pos": "verb", "cefr": "B1", "translation": "to approach / near", "examples": [{"hungarian": "A veszedelem napról napra közeledett.", "english": "The peril neared day by day."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-tatarjaras-01-gr.json", {
    "title": "Időhatározói viszonyok és előrejelző szerkezetek",
    "level": "B1",
    "rules": [
        {
            "id": "temporal-participle-mikor",
            "title": "Adverbial Clauses with 'amikor' and 'éppen akkor'",
            "text": "*Éppen akkor..., amikor...* (at the very moment when...): *Éppen akkor gyilkolták meg Kötönyt, amikor a tatárok betörtek az országba.* (They assassinated Kötöny at the exact moment when the Tatars invaded.)",
            "tip": "Emphasizes dramatic timing in historical writing."
        },
        {
            "id": "deprivation-suffix-tol",
            "title": "Verbs of Deprivation with '-tól / -től'",
            "text": "*Megfoszt valakit valamitől* (to deprive someone of something): *A lázadás megfosztotta a királyt a könnyűlovasságtól.*",
            "tip": "Always takes the ablative case *-tól / -től*."
        }
    ],
    "examples": [
        {"spanish": "Éppen akkor vesztették el a kun szövetségest, amikor megérkezett a tatár sereg.", "english": "They lost their Cuman allies at the very moment when the Tatar army arrived."},
        {"spanish": "Julianus barát hírt hozott a közeledő veszélyről.", "english": "Friar Julian brought news about the approaching danger."},
        {"spanish": "A viszály megfosztotta az országot az egységes védelemtől.", "english": "The discord deprived the country of unified defense."}
    ]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-01-ex.json", {
    "exercises": [
        {
            "id": "b1-tatarjaras-01.ex01",
            "type": "multiple-choice",
            "title": "Julianus barát útja",
            "instruction": "Kiket talált meg Julianus barát 1235-ben a Volga mellett?",
            "question": "Mely népcsoporttal találkozott Julianus Magna Hungariában?",
            "options": ["A keleten maradt magyarokkal, akikkel még magyarul beszélt", "A római császár katonáival", "Angol tengerészekkel", "Spanyol lovagokkal"],
            "correctIndex": 0,
            "explanation": "Julianus barát rátalált a keleti magyarokra Magna Hungariában.",
            "teaches": ["szerzetes", "felkutat"]
        },
        {
            "id": "b1-tatarjaras-01.ex02",
            "type": "fill-blank",
            "title": "Batu kán levele",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Julianus Batu kán ___ tért vissza IV. Béla királyhoz.",
            "correctAnswer": "levelével",
            "options": ["levelével", "aranyával", "kutyájával", "hajójával"],
            "teaches": ["fenyegeto-level"]
        },
        {
            "id": "b1-tatarjaras-01.ex03",
            "type": "sentence-builder",
            "title": "Kunok befogadása",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["IV.", "Béla", "menedéket", "adott", "a", "menekülő", "kunoknak."],
            "correctSentence": "IV. Béla menedéket adott a menekülő kunoknak.",
            "english": "Béla IV gave shelter to the fleeing Cumans.",
            "teaches": ["menedek", "konnyulovassag"]
        },
        {
            "id": "b1-tatarjaras-01.ex04",
            "type": "multiple-choice",
            "title": "Kötöny sorsa",
            "instruction": "Mi történt Kötöny kun fejedelemmel Pesten?",
            "question": "Hogyan halt meg Kötöny fejedelem?",
            "options": ["A lázadó pesti tömeg és a főurak meggyilkolták", "Békésen, idős korban hunyt el", "A tatár fogságban halt meg Ázsiában", "Visszatért a tengerre"],
            "correctIndex": 0,
            "explanation": "A gyanakvó tömeg meggyilkolta Kötönyt, ami a kunok dühös kivonulásához vezetett.",
            "teaches": ["meggyilkol", "feszultseg"]
        },
        {
            "id": "b1-tatarjaras-01.ex05",
            "type": "fill-blank",
            "title": "Hágók elzárása",
            "instruction": "Válaszd ki a megfelelő szót!",
            "sentence": "A határvédők fa ___ zárták le a Kárpátok hágóit.",
            "correctAnswer": "torlaszokkal",
            "options": ["torlaszokkal", "virágokkal", "könyvekkel", "képekkel"],
            "teaches": ["torlasz"]
        },
        {
            "id": "b1-tatarjaras-01.ex06",
            "type": "sentence-builder",
            "title": "Megfosztva a seregtől",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "kunok", "kivonulása", "megfosztotta", "a", "királyt", "a", "könnyűlovasságtól."],
            "correctSentence": "A kunok kivonulása megfosztotta a királyt a könnyűlovasságtól.",
            "english": "The withdrawal of the Cumans deprived the king of the light cavalry.",
            "teaches": ["megfoszt", "konnyulovassag", "kivonul"]
        },
        {
            "id": "b1-tatarjaras-01.ex07",
            "type": "multiple-choice",
            "title": "A tatár sereg vezére",
            "instruction": "Ki vezette a Magyarországot megtámadó mongol fősereget?",
            "question": "Hogy hívták a mongol hadvezért 1241-ben?",
            "options": ["Batu kán", "Dzsingisz kán", "Attila", "Szulejmán szultán"],
            "correctIndex": 0,
            "explanation": "Batu kán vezette a tatár inváziós sereget a Kárpát-medence ellen.",
            "teaches": ["fenyegeto-level", "elorenyomul"]
        },
        {
            "id": "b1-tatarjaras-01.ex08",
            "type": "fill-blank",
            "title": "Közeledő veszély",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "1241 tavaszán a mongol sereg feltartóztathatatlanul ___ Pest felé.",
            "correctAnswer": "közeledett",
            "options": ["közeledett", "aludt", "úszott", "táncolt"],
            "teaches": ["kozeledik", "elorenyomul"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-tatarjaras-01.json", make_lesson(
    "lesson.b1.tatarjaras-01",
    "Julianus barát és a tatár fenyegetés (Friar Julian & the Threat - 1235)",
    "Időhatározói viszonyok és előrejelző szerkezetek",
    [
        "Welcome to Unit 6 of the Hungarian Citizenship Track, examining one of the most tragic yet formative trials of medieval Hungary: the Mongol (Tatar) Invasion of 1241–42 (*Tatárjárás*).",
        "In this first lesson, we explore Friar Julian's 1235 discovery of Magna Hungaria along the Volga, his return with Batu Khan's ultimatum, and the fatal internal tensions leading to the murder of Cuman Chieftain Kötöny.",
        "We also practice dramatic temporal constructions (*éppen akkor..., amikor...*) and verbs of deprivation (*megfoszt valamitől*)."
    ],
    [
        "I can describe Friar Julian's journey (1235) and the discovery of Magna Hungaria.",
        "I can explain Batu Khan's ultimatum and the approach of the Mongol armies.",
        "I can summarize the conflict regarding Cuman refugees (*kunok*) and Chieftain Kötöny.",
        "I can use ablative deprivation structures (*megfoszt valamitől*) correctly."
    ],
    "stories/world/b1/b1-tatarjaras-01-tatarokerkezese.json",
    "vocabulary/b1/b1-tatarjaras-01-voc.json",
    "grammar/b1/b1-tatarjaras-01-gr.json",
    "exercises/b1/b1-tatarjaras-01-ex.json",
    [f"b1-tatarjaras-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: A muhi csata (1241)
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras-02-muhicsata.json", make_story(
    "story.b1.tatarjaras.02",
    "A muhi csata (1241. április 11–12.)",
    "The catastrophic Battle of Muhi on the Sajó river (April 11–12, 1241): the confined wagon camp, Batu Khan and Subutai's night bridge-crossing, the annihilation of the royal army, and King Béla IV's narrow escape.",
    "Muhi (Sajó folyó)",
    ["ok-okozati viszonyok és csataleírások"],
    ["Muhi csata 1241", "Sajó folyó", "Szekértábor", "IV. Béla menekülése"],
    [
        "1241. április 11-én a Sajó folyó partján, Muhi falu mellett találkozott IV. Béla királyi serege és Batu kán főserege. A magyar hadsereg nehézlovagokból, főpapi és vármegyei csapatokból állt.",
        "A magyar vezetés szűk területen, láncokkal és szekerekkel megerősített szekértábort hozott létre, amely azonban végzetes csapdának bizonyult, mert megakadályozta a lovasság szabad manőverezését.",
        "Éjszaka Szubotáj és Batu kán csapatai a híd védőit kijátszva átgázoltak a Sajó sekély vizén, és hajnalban teljesen bekerítették a magyar tábort.",
        "A tatárok gyújtónyilakkal és kőhajító gépekkel bombázták a bezsúfolódott sereget. A véres és kaotikus harcban a magyar hadsereg színe-java – köztük Ugrin kalocsai érsek és a templomos lovagok – életét vesztette.",
        "Hűséges hívei önfeláldozásának köszönhetően IV. Béla király csodával határos módon kiszabadult a gyűrűből, és nyugat felé menekült, hogy megmentse a királyságot."
    ],
    [
        {"lemma": "muhi csata", "pos": "noun", "cefr": "B1", "gloss": "Battle of Muhi (1241)"},
        {"lemma": "szekértábor", "pos": "noun", "cefr": "B1", "gloss": "wagon fort / corral"},
        {"lemma": "gyújtónyíl", "pos": "noun", "cefr": "B1", "gloss": "fire arrow"},
        {"lemma": "kiszabadul", "pos": "verb", "cefr": "B1", "gloss": "to break free / escape"}
    ],
    [
        {
            "question": "Mikor és melyik folyónál zajlott le a sorsdöntő muhi csata?",
            "options": ["1241. április 11–12-én a Sajó folyó partján", "1000-ben a Duna mellett", "1526-ban a Tisza partján", "1848-ban a Dráva mellett"],
            "correctIndex": 0,
            "explanation": "A muhi csata 1241. április 11–12-én zajlott a Sajó folyónál."
        },
        {
            "question": "Miért vált veszedelmessé a magyar sereg számára a szekértábor?",
            "options": ["Mert túl szűk volt, és megakadályozta a lovasság szabad mozgását és kibontakozását", "Mert aranyból készült és ellopták", "Mert a katonák elaludtak benne", "Mert a szekerek elúsztak a folyón"],
            "correctIndex": 0,
            "explanation": "A szűk szekértáborban összezsúfolódott sereg nem tudott manőverezni és csapdába esett."
        },
        {
            "question": "Mi történt IV. Béla királlyal a muhi csata után?",
            "options": ["Hívei segítségével sikeresen kiszabadult és nyugat felé menekült", "Fogságba esett és Mongóliába hurcolták", "Azonnal békét kötött Batu kánnal", "A csatatéren életét vesztette"],
            "correctIndex": 0,
            "explanation": "Béla király önfeláldozó lovagjai segítségével megmenekült és nyugat felé menekült."
        }
    ]
))

write_json(VOCAB_DIR / "b1-tatarjaras-02-voc.json", {
    "title": "A muhi csata (1241)",
    "words": [
        {"lemma": "muhi csata", "pos": "noun", "cefr": "B1", "translation": "Battle of Muhi", "examples": [{"hungarian": "A muhi csata nemzeti tragédia volt.", "english": "The Battle of Muhi was a national tragedy."}]},
        {"lemma": "szekértábor", "pos": "noun", "cefr": "B1", "translation": "wagon fort", "examples": [{"hungarian": "A szekértábort láncokkal kötötték össze.", "english": "They tied the wagon fort together with chains."}]},
        {"lemma": "gyújtónyíl", "pos": "noun", "cefr": "B1", "translation": "fire arrow", "examples": [{"hungarian": "Gyújtónyilakkal lőtték a tábor sátrait.", "english": "They shot the tents of the camp with fire arrows."}]},
        {"lemma": "kiszabadul", "pos": "verb", "cefr": "B1", "translation": "to break free / escape", "examples": [{"hungarian": "A király alig tudott kiszabadulni a bekerítésből.", "english": "The king could barely break free from the encirclement."}]},
        {"lemma": "bekerít", "pos": "verb", "cefr": "B1", "translation": "to surround / encircle", "examples": [{"hungarian": "A tatár lovasok teljesen bekerítették a sereget.", "english": "The Tatar horsemen completely encircled the army."}]},
        {"lemma": "katasztrófa", "pos": "noun", "cefr": "B1", "translation": "catastrophe", "examples": [{"hungarian": "A csata katasztrófával végződött.", "english": "The battle ended in catastrophe."}]},
        {"lemma": "manőverezik", "pos": "verb", "cefr": "B1", "translation": "to manoeuvre", "examples": [{"hungarian": "A nehézlovasság nem tudott manőverezni a szűk helyen.", "english": "The heavy cavalry could not manoeuvre in the confined space."}]},
        {"lemma": "összezsúfolódik", "pos": "verb", "cefr": "B1", "translation": "to crowd together", "examples": [{"hungarian": "A katonák összezsúfolódtak a tábor közepén.", "english": "The soldiers crowded together in the middle of the camp."}]},
        {"lemma": "híd", "pos": "noun", "cefr": "B1", "translation": "bridge", "examples": [{"hungarian": "A Sajó hídját hősiesen védték a magyarok.", "english": "The Hungarians heroically defended the bridge of the Sajó."}]},
        {"lemma": "érsek", "pos": "noun", "cefr": "B1", "translation": "archbishop", "examples": [{"hungarian": "A kalocsai érsek a csatamezőn esett el.", "english": "The archbishop of Kalocsa fell on the battlefield."}]},
        {"lemma": "hajnal", "pos": "noun", "cefr": "B1", "translation": "dawn", "examples": [{"hungarian": "Hajnalban indult meg a döntő roham.", "english": "At dawn the decisive charge began."}]},
        {"lemma": "önfeláldozás", "pos": "noun", "cefr": "B1", "translation": "self-sacrifice", "examples": [{"hungarian": "A lovagok önfeláldozása megmentette az uralkodót.", "english": "The knights' self-sacrifice saved the monarch."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-tatarjaras-02-gr.json", {
    "title": "Ok-okozati viszonyok és csataleírások (miatt, következtében)",
    "level": "B1",
    "rules": [
        {
            "id": "causal-chain-battle",
            "title": "Expressing Cause and Consequence in Military Narratives",
            "text": "Link tactical causes to outcomes: *A szűk tábor miatt a sereg nem tudott manőverezni.* (Because of the narrow camp, the army could not manoeuvre.) *A bekerítés következtében a katonák csapdába estek.* (As a consequence of the encirclement, the soldiers fell into a trap.)",
            "tip": "*Miatt* follows nouns (*tábor miatt*); *következtében* follows nouns in the possessive (*bekerítés következtében*)."
        },
        {
            "id": "result-ugyhogy",
            "title": "Consecutive Clauses with 'úgyhogy' (so that / such that)",
            "text": "*Úgyhogy* introduces factual results: *A tatárok átkeltek a folyón, úgyhogy meglepték a tábort.* (The Tatars crossed the river, so that they surprised the camp.)",
            "tip": "Always preceded by a comma."
        }
    ],
    "examples": [
        {"spanish": "A szekértábor szűk volt, úgyhogy a magyar lovasság nem tudott kibontakozni.", "english": "The wagon camp was narrow, so that the Hungarian cavalry could not deploy."},
        {"spanish": "A váratlan éjszakai támadás miatt kitört a pánik.", "english": "Because of the unexpected night attack, panic broke out."},
        {"spanish": "A lovagok önfeláldozásának köszönhetően a király megmenekült.", "english": "Thanks to the self-sacrifice of the knights, the king escaped."}
    ]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-02-ex.json", {
    "exercises": [
        {
            "id": "b1-tatarjaras-02.ex01",
            "type": "multiple-choice",
            "title": "A muhi csata dátuma",
            "instruction": "Melyik évben zajlott le a muhi csata?",
            "question": "Mikor szenvedett vereséget a magyar sereg Muhinál?",
            "options": ["1241-ben", "1000-ben", "1526-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "A muhi csata 1241. április 11–12-én zajlott le.",
            "teaches": ["muhi-csata", "katasztrofa"]
        },
        {
            "id": "b1-tatarjaras-02.ex02",
            "type": "fill-blank",
            "title": "A csata folyója",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A muhi csata a ___ folyó partján zajlott le.",
            "correctAnswer": "Sajó",
            "options": ["Sajó", "Duna", "Tisza", "Rába"],
            "teaches": ["muhi-csata", "hid"]
        },
        {
            "id": "b1-tatarjaras-02.ex03",
            "type": "sentence-builder",
            "title": "Szekértábor csapdája",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "szűk", "szekértábor", "megakadályozta", "a", "lovasság", "szabad", "mozgását."],
            "correctSentence": "A szűk szekértábor megakadályozta a lovasság szabad mozgását.",
            "english": "The narrow wagon camp prevented the free movement of the cavalry.",
            "teaches": ["szekertabor", "manoverezik"]
        },
        {
            "id": "b1-tatarjaras-02.ex04",
            "type": "multiple-choice",
            "title": "Éjszakai átkelés",
            "instruction": "Hogyan lepték meg a tatárok a magyar tábort?",
            "question": "Mit tettek Szubotáj csapatai az éjszaka leple alatt?",
            "options": ["Átkeltek a Sajó sekély vizén és hajnalban bekerítették a tábort", "Békésen hazamentek", "Hajókat építettek egy hét alatt", "Megvárták a magyarok támadását"],
            "correctIndex": 0,
            "explanation": "A tatárok átgázoltak a folyón és hajnalban teljesen bekerítették a magyar tábort.",
            "teaches": ["bekerit", "hajnal"]
        },
        {
            "id": "b1-tatarjaras-02.ex05",
            "type": "fill-blank",
            "title": "Következmény (miatt)",
            "instruction": "Válaszd ki a helyes szót!",
            "sentence": "A meglepetésszerű éjszakai támadás ___ pánik tört ki a táborban.",
            "correctAnswer": "miatt",
            "options": ["miatt", "után", "előtt", "nélkül"],
            "teaches": ["katasztrofa"]
        },
        {
            "id": "b1-tatarjaras-02.ex06",
            "type": "sentence-builder",
            "title": "A király megmenekülése",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["IV.", "Béla", "hűséges", "lovagjai", "segítségével", "kiszabadult", "a", "bekerítésből."],
            "correctSentence": "IV. Béla hűséges lovagjai segítségével kiszabadult a bekerítésből.",
            "english": "Béla IV broke free from the encirclement with the help of his loyal knights.",
            "teaches": ["kiszabadul", "onfelaldozas"]
        },
        {
            "id": "b1-tatarjaras-02.ex07",
            "type": "multiple-choice",
            "title": "Tűzfegyverek és nyilak",
            "instruction": "Mivel lőtték a tatárok a szekértábort?",
            "question": "Milyen fegyvereket használtak a tatárok a tábor felgyújtására?",
            "options": ["Gyújtónyilakat és kőhajító gépeket", "Modern rakétákat", "Csak kardokat közelharcban", "Puskákat és ágyúkat"],
            "correctIndex": 0,
            "explanation": "A tatárok gyújtónyilakkal és katapultokkal gyújtották fel a szekereket és sátrakat.",
            "teaches": ["gyujtonyil"]
        },
        {
            "id": "b1-tatarjaras-02.ex08",
            "type": "fill-blank",
            "title": "Hősies védelem",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A kalocsai érsek és vitézei ___ életüket adták a hazáért.",
            "correctAnswer": "önfeláldozóan",
            "options": ["önfeláldozóan", "lustán", "gyáván", "titokban"],
            "teaches": ["onfelaldozas", "ersek"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-tatarjaras-02.json", make_lesson(
    "lesson.b1.tatarjaras-02",
    "A muhi csata (The Battle of Muhi - 1241)",
    "Ok-okozati viszonyok és csataleírások (miatt, következtében)",
    [
        "In this second lesson, we study the catastrophe of the Battle of Muhi (April 11–12, 1241) on the banks of the Sajó river.",
        "You will learn about the tactical vulnerabilities of the crowded wagon fort (*szekértábor*), Batu Khan and Subutai's night river crossing, the destruction of the royal army, and King Béla IV's miraculous escape.",
        "We also practice causal expressions (*miatt, következtében*) and consecutive clauses with *úgyhogy*."
    ],
    [
        "I can state the date (April 11–12, 1241) and location (Sajó river, Muhi) of the battle.",
        "I can explain the strategic reasons for the Hungarian defeat (confinement in wagon fort, night encirclement).",
        "I can describe King Béla IV's escape to preserve royal authority.",
        "I can use causal prepositions and result conjunctions (*úgyhogy*) accurately."
    ],
    "stories/world/b1/b1-tatarjaras-02-muhicsata.json",
    "vocabulary/b1/b1-tatarjaras-02-voc.json",
    "grammar/b1/b1-tatarjaras-02-gr.json",
    "exercises/b1/b1-tatarjaras-02-ex.json",
    [f"b1-tatarjaras-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: A pusztulás és a király menekülése
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras-03-pusztulas.json", make_story(
    "story.b1.tatarjaras.03",
    "A pusztulás éve és a király menekülése az Adriához (1241–1242)",
    "The winter of 1241–42: the frozen Danube, the devastation of Transdanubia, King Béla IV's flight to Trau (Trogir) fortress on the Adriatic, and Master Rogerius's Carmen Miserabile (*Siralmas ének*).",
    "Dunántúl és Trau (Trogir)",
    ["szenvedő szerkezeteket helyettesítő cselekvő formák"],
    ["1241–1242 pusztítása", "Befagyott Duna", "Trau vára", "Rogerius mester"],
    [
        "A muhi vereség után a tatárok elfoglalták és felégették Pestet és az egész Alföldet. 1241–1242 rendkívül kemény telén a Duna vize vastagon befagyott, így a tatár lovasság átkelt a jégen és feldúlta a Dunántúlt is.",
        "Csak néhány megerősített kővár és fallal védett város – mint Esztergom fellegvára, Székesfehérvár, Pannonhalma és Klissza – tudott ellenállni a támadóknak.",
        "IV. Béla király Ausztrián és Horvátországon keresztül az Adriai-tenger partjára, Trau (a mai Trogir) jól védhető tengerparti sziklavárába menekült a családjával.",
        "A mongol csapatok üldözték a királyt a tengerpartig, de Trau megerősített szigetét nem tudták bevenni hajók hiányában.",
        "A pusztítás mértékét Rogerius váradi kanonok Siralmas ének (Carmen Miserabile) című krónikája örökítette meg: a falvak kiürültek, a lakosság mintegy fele elpusztult vagy fogságba esett."
    ],
    [
        {"lemma": "pusztítás", "pos": "noun", "cefr": "B1", "gloss": "devastation / destruction"},
        {"lemma": "befagy", "pos": "verb", "cefr": "B1", "gloss": "to freeze over"},
        {"lemma": "fellegvár", "pos": "noun", "cefr": "B1", "gloss": "citadel / acropolis"},
        {"lemma": "fogság", "pos": "noun", "cefr": "B1", "gloss": "captivity"}
    ],
    [
        {
            "question": "Hogyan tudtak átkelni a tatárok a Dunántúlra 1241/1242 telén?",
            "options": ["A rendkívüli hideg miatt a Duna befagyott, és átlovagoltak a jégen", "Hatalmas hidat építettek fából", "Gőzhajókkal keltek át", "Alagutat ástak a Duna alatt"],
            "correctIndex": 0,
            "explanation": "A kemény télen befagyott Duna jegén kelt át a mongol lovasság a Dunántúlra."
        },
        {
            "question": "Hová menekült IV. Béla király a tatárok elől?",
            "options": ["Trau (Trogir) adriai tengerparti sziklavárába", "Londonba a királyi palotába", "Rómába a Vatikánba", "Egy hegyi kunyhóba Svájcban"],
            "correctIndex": 0,
            "explanation": "Béla az adriai tengerparti Trau szigetvárába menekült, amelyet a tatárok nem tudtak elérni."
        },
        {
            "question": "Melyik mű örökítette meg a tatárjárás borzalmait?",
            "options": ["Rogerius mester Siralmas éneke (Carmen Miserabile)", "Petőfi Nemzeti dala", "Kölcsey Himnusza", "Anonymus Gesta Hungaroruma"],
            "correctIndex": 0,
            "explanation": "Rogerius mester 'Siralmas ének' (Carmen Miserabile) című munkája a pusztítás legfontosabb szemtanúi forrása."
        }
    ]
))

write_json(VOCAB_DIR / "b1-tatarjaras-03-voc.json", {
    "title": "A pusztulás éve és a király menekülése",
    "words": [
        {"lemma": "pusztítás", "pos": "noun", "cefr": "B1", "translation": "devastation", "examples": [{"hungarian": "A tatár pusztítás a lakosság felét érintette.", "english": "The Tatar devastation affected half of the population."}]},
        {"lemma": "befagy", "pos": "verb", "cefr": "B1", "translation": "to freeze over", "examples": [{"hungarian": "A Duna vastagon befagyott a kemény télen.", "english": "The Danube froze over thickly in the harsh winter."}]},
        {"lemma": "fellegvár", "pos": "noun", "cefr": "B1", "translation": "citadel", "examples": [{"hungarian": "Az esztergomi fellegvár ellenállt az ostromnak.", "english": "The Esztergom citadel resisted the siege."}]},
        {"lemma": "fogság", "pos": "noun", "cefr": "B1", "translation": "captivity", "examples": [{"hungarian": "Sokan fogságba estek és elhurcolták őket.", "english": "Many fell into captivity and were carried away."}]},
        {"lemma": "felég", "pos": "verb", "cefr": "B1", "translation": "to burn down", "examples": [{"hungarian": "A védtelen falvak felégtek a harcokban.", "english": "The defenseless villages burned down in the fighting."}]},
        {"lemma": "sziklavár", "pos": "noun", "cefr": "B1", "translation": "rock fortress", "examples": [{"hungarian": "Trau sziklavára biztonságos menedék volt.", "english": "The rock fortress of Trau was a safe refuge."}]},
        {"lemma": "kanonok", "pos": "noun", "cefr": "B1", "translation": "canon", "examples": [{"hungarian": "Rogerius mester váradi kanonok volt.", "english": "Master Rogerius was a canon of Várad."}]},
        {"lemma": "szemtanú", "pos": "noun", "cefr": "B1", "translation": "eyewitness", "examples": [{"hungarian": "A szemtanúk részletesen leírták a vészt.", "english": "The eyewitnesses described the calamity in detail."}]},
        {"lemma": "üldöz", "pos": "verb", "cefr": "B1", "translation": "to pursue / chase", "examples": [{"hungarian": "A tatárok a tengerig üldözték a királyt.", "english": "The Tatars pursued the king all the way to the sea."}]},
        {"lemma": "kiürül", "pos": "verb", "cefr": "B1", "translation": "to become empty / deserted", "examples": [{"hungarian": "Egész országrészek ürültek ki a háború alatt.", "english": "Entire regions became deserted during the war."}]},
        {"lemma": "ostrom", "pos": "noun", "cefr": "B1", "translation": "siege", "examples": [{"hungarian": "A kővárak sikeresen védték ki az ostromot.", "english": "The stone castles successfully repelled the siege."}]},
        {"lemma": "vészkorszak", "pos": "noun", "cefr": "B1", "translation": "time of calamity", "examples": [{"hungarian": "A magyar történelem egyik legsúlyosabb vészkorszaka volt.", "english": "It was one of the most severe times of calamity in Hungarian history."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-tatarjaras-03-gr.json", {
    "title": "Passzív jelentésű aktív igék és igekötős igék a történeti narratívában",
    "level": "B1",
    "rules": [
        {
            "id": "verbal-prefixes-destruction",
            "title": "Verbal Prefixes of Completion and Destruction (fel-, le-, el-, el-)",
            "text": "Prefixes modify aspect dramatically: *ég* (burns) -> *felég* (burns completely down); *pusztul* (perishes) -> *elpusztul*; *fagy* (freezes) -> *befagy* (freezes over).",
            "tip": "Prefixes precede the verb in unmarked order: *A falu felégett.*"
        },
        {
            "id": "mediopassive-intransitive",
            "title": "Mediopassive Reflexive Verbs (-ul / -ül, -ódik / -ődik)",
            "text": "Hungarian expresses passive states through intransitive reflexive endings: *kiürül* (becomes empty), *elpusztul* (gets destroyed), *befagy* (freezes over).",
            "tip": "No agent is required with mediopassive verbs."
        }
    ],
    "examples": [
        {"spanish": "A kemény télen a Duna befagyott, és a falvak felégtek.", "english": "In the harsh winter the Danube froze over, and the villages burned down."},
        {"spanish": "Egész országrészek ürültek ki a tatárjárás idején.", "english": "Entire regions emptied out during the Mongol invasion."},
        {"spanish": "Trau vára ellenállt a mongol ostromnak.", "english": "The castle of Trau resisted the Mongol siege."}
    ]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-03-ex.json", {
    "exercises": [
        {
            "id": "b1-tatarjaras-03.ex01",
            "type": "multiple-choice",
            "title": "Átkelés a befagyott Dunán",
            "instruction": "Hogyan jutottak át a tatárok a Dunántúlra 1241/42 telén?",
            "question": "Mi tette lehetővé a tatár átkelést a Dunán?",
            "options": ["A Duna vastag jégpáncélja a rendkívüli hidegben", "Római kőhíd építése", "Alagút fúrása", "Gőzhajók vásárlása"],
            "correctIndex": 0,
            "explanation": "A kemény télben befagyott Duna jegén keltek át a mongolok.",
            "teaches": ["befagy", "pusztitas"]
        },
        {
            "id": "b1-tatarjaras-03.ex02",
            "type": "fill-blank",
            "title": "Trau vára az Adrián",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "IV. Béla az adriai tengerparti ___ sziklavárába menekült.",
            "correctAnswer": "Trau",
            "options": ["Trau", "London", "Párizs", "Bécs"],
            "teaches": ["sziklavar", "uldoz"]
        },
        {
            "id": "b1-tatarjaras-03.ex03",
            "type": "sentence-builder",
            "title": "Rogerius mester krónikája",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Rogerius", "mester", "megírta", "a", "Siralmas", "ének", "című", "krónikát."],
            "correctSentence": "Rogerius mester megírta a Siralmas ének című krónikát.",
            "english": "Master Rogerius wrote the chronicle titled Carmen Miserabile.",
            "teaches": ["kanonok", "szemtanu"]
        },
        {
            "id": "b1-tatarjaras-03.ex04",
            "type": "multiple-choice",
            "title": "Ellenálló kővárak",
            "instruction": "Mely helyszínek tudtak ellenállni a tatár ostromnak?",
            "question": "Milyen típusú erődítményeket nem tudtak bevenni a tatárok?",
            "options": ["A megerősített kővárakat (pl. Esztergom fellegvára, Pannonhalma)", "A fából épült egyszerű falvakat", "A nyitott mezei sátrakat", "Semmilyen helyszín nem tudott ellenállni"],
            "correctIndex": 0,
            "explanation": "A szilárd kővárak, mint Esztergom és Pannonhalma, sikeresen visszaverték a tatárokat.",
            "teaches": ["fellegvar", "ostrom"]
        },
        {
            "id": "b1-tatarjaras-03.ex05",
            "type": "fill-blank",
            "title": "Igekötős ige (kiürül)",
            "instruction": "Válaszd ki a helyes igét!",
            "sentence": "A pusztítás következtében a falvak ___ és elnéptelenedtek.",
            "correctAnswer": "kiürültek",
            "options": ["kiürültek", "kitágultak", "felépültek", "megnőttek"],
            "teaches": ["kiurul", "veszkorszak"]
        },
        {
            "id": "b1-tatarjaras-03.ex06",
            "type": "sentence-builder",
            "title": "Sziklavár védelme",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "tatárok", "nem", "tudták", "bevenni", "Trau", "sziklavárát."],
            "correctSentence": "A tatárok nem tudták bevenni Trau sziklavárát.",
            "english": "The Tatars could not capture the rock fortress of Trau.",
            "teaches": ["sziklavar", "ostrom"]
        },
        {
            "id": "b1-tatarjaras-03.ex07",
            "type": "multiple-choice",
            "title": "A pusztítás mértéke",
            "instruction": "Mennyi áldozatot követelt a tatárjárás?",
            "question": "A becslések szerint a lakosság mekkora része pusztult el 1241–42-ben?",
            "options": ["A lakosság 20–50%-a elpusztult vagy fogságba került", "Egyetlen ember sem halt meg", "Csak a királyi család", "Mindenki túlélte sértetlenül"],
            "correctIndex": 0,
            "explanation": "A tatárjárás során a lakosság 20–50%-a pusztult el, óriási demográfiai katasztrófát okozva.",
            "teaches": ["pusztitas", "fogsag"]
        },
        {
            "id": "b1-tatarjaras-03.ex08",
            "type": "fill-blank",
            "title": "Felégő falvak",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A védelem nélküli falvak mind ___ a tatár hordák nyomában.",
            "correctAnswer": "felégtek",
            "options": ["felégtek", "virágoztak", "elúsztak", "kinyíltak"],
            "teaches": ["feleg"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-tatarjaras-03.json", make_lesson(
    "lesson.b1.tatarjaras-03",
    "A pusztulás éve és a király menekülése (Devastation & Flight - 1241–42)",
    "Passzív jelentésű aktív igék és igekötős igék a történeti narratívában",
    [
        "In this third lesson, we explore the darkest year of medieval Hungary: the winter of 1241–42.",
        "You will learn about the frozen Danube, the destruction of Transdanubia, the few stone castles that held out (Esztergom citadel, Pannonhalma), King Béla IV's refuge in Trau (Trogir) on the Adriatic, and Master Rogerius's *Carmen Miserabile* (*Siralmas ének*).",
        "We also practice mediopassive verbs (*kiürül, elpusztul*) and verbal prefixes of total destruction (*felég, befagy*)."
    ],
    [
        "I can describe the winter of 1241–42 and the crossing of the frozen Danube.",
        "I can explain Béla IV's flight to Trau (Trogir) and the strategic advantage of island stone fortresses.",
        "I can cite Master Rogerius's *Carmen Miserabile* as a primary historical source.",
        "I can use completive prefixes (*felég, kiürül, befagy*) to describe historical events."
    ],
    "stories/world/b1/b1-tatarjaras-03-pusztulas.json",
    "vocabulary/b1/b1-tatarjaras-03-voc.json",
    "grammar/b1/b1-tatarjaras-03-gr.json",
    "exercises/b1/b1-tatarjaras-03-ex.json",
    [f"b1-tatarjaras-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: IV. Béla, a második honalapító
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras-04-belaujjapitese.json", make_story(
    "story.b1.tatarjaras.04",
    "IV. Béla, a második honalapító és az ország újjáépítése",
    "The sudden Mongol withdrawal in spring 1242 (death of Great Khan Ögedei), King Béla IV's return, and his visionary reconstruction: recalling and integrating Cumans and Jazygians, inviting German settlers (*hospesek*), and granting urban privileges.",
    "Alföld és Buda",
    ["cél- és eredményhatározói szerkezetek"],
    ["Második honalapító", "Tatár kivonulás 1242", "Újjáépítés", "Kunok és jászok"],
    [
        "1242 tavaszán a mongol seregek ugyanolyan hirtelen, ahogyan érkeztek, elhagyták a Kárpát-medencét. A kivonulás legfőbb oka Ögödej nagykán halála volt, ami miatt Batu kán visszasietett a vezérválasztó kurgánba.",
        "A hazatérő IV. Béla egy romokban heverő, elnéptelenedett országot talált. A király felismerte: ha nem változtat radikálisan a védelempolitikán, a következő tatár támadás elpusztítja a magyarságot.",
        "Béla ezért történelmi méretű újjáépítési programba kezdett, amiért az utókor méltán nevezte őt 'a második honalapítónak'.",
        "A népesség pótlására visszahívta a kunokat, letelepítette a jászokat, és nyugati (főként német) telepeseket, úgynevezett hospeseket hívott az országba, adókedvezményeket és önkormányzati jogokat adva nekik.",
        "Fia, István herceg feleségül vette Erzsébet kun hercegnőt, szoros vérségi és szövetségi köteléket teremtve a magyarság és a betelepülő nomád népek között."
    ],
    [
        {"lemma": "második honalapító", "pos": "noun", "cefr": "B1", "gloss": "second founder of the state (Béla IV)"},
        {"lemma": "kivonulás", "pos": "noun", "cefr": "B1", "gloss": "withdrawal / evacuation"},
        {"lemma": "hospes", "pos": "noun", "cefr": "B1", "gloss": "guest settler (medieval German colonist)"},
        {"lemma": "újjáépítés", "pos": "noun", "cefr": "B1", "gloss": "reconstruction"}
    ],
    [
        {
            "question": "Miért vonultak ki a tatárok váratlanul 1242 tavaszán Magyarországról?",
            "options": ["Ögödej nagykán halála miatt Batu kán sietett a kánválasztó gyűlésre", "Mert a magyar király legyőzte őket a tengeren", "Mert megijedtek a hidegtől", "Mert elfogyott a vizük"],
            "correctIndex": 0,
            "explanation": "Ögödej nagykán halála belső hatalmi harcot indított el, ezért a tatár sereg elhagyta Európát."
        },
        {
            "question": "Hogyan nevezi az utókor és a történettudomány IV. Béla királyt?",
            "options": ["'A második honalapítónak'", "'A Napkirálynak'", "'A lovagkirálynak'", "'A kalandozó vezérnek'"],
            "correctIndex": 0,
            "explanation": "Hatalmas újjáépítő és várépítő munkája miatt IV. Bélát a 'második honalapítónak' nevezik."
        },
        {
            "question": "Milyen népcsoportokat telepített le IV. Béla az elnéptelenedett területekre?",
            "options": ["Kunokat, jászokat és nyugati (német) hospes telepeseket", "Csak viking tengerészeket", "Római légiósokat", "Kizárólag perzsa kereskedőket"],
            "correctIndex": 0,
            "explanation": "Béla kunokat, jászokat és német hospeseket telepített le a népesség pótlására."
        }
    ]
))

write_json(VOCAB_DIR / "b1-tatarjaras-04-voc.json", {
    "title": "IV. Béla, a második honalapító",
    "words": [
        {"lemma": "második honalapító", "pos": "noun", "cefr": "B1", "translation": "second founder of the state", "examples": [{"hungarian": "IV. Béla a második honalapítóként vonult be a történelembe.", "english": "Béla IV entered history as the second founder of the state."}]},
        {"lemma": "kivonulás", "pos": "noun", "cefr": "B1", "translation": "withdrawal", "examples": [{"hungarian": "A tatárok kivonulása után azonnal megindult a munka.", "english": "After the Tatars' withdrawal, work started immediately."}]},
        {"lemma": "hospes", "pos": "noun", "cefr": "B1", "translation": "guest settler / colonist", "examples": [{"hungarian": "A német hospesek bányákat és városokat építettek.", "english": "The German guest settlers built mines and towns."}]},
        {"lemma": "újjáépítés", "pos": "noun", "cefr": "B1", "translation": "reconstruction", "examples": [{"hungarian": "Az ország újjáépítése óriási feladat volt.", "english": "The reconstruction of the country was an immense task."}]},
        {"lemma": "elnéptelenedett", "pos": "adj", "cefr": "B1", "translation": "depopulated / deserted", "examples": [{"hungarian": "Az elnéptelenedett falvakba új telepesek érkeztek.", "english": "New settlers arrived in the depopulated villages."}]},
        {"lemma": "betelepít", "pos": "verb", "cefr": "B1", "translation": "to settle / colonize", "examples": [{"hungarian": "Béla kunokat és jászokat telepített be az Alföldre.", "english": "Béla settled Cumans and Jazygians in the Great Plain."}]},
        {"lemma": "adókedvezmény", "pos": "noun", "cefr": "B1", "translation": "tax relief / exemption", "examples": [{"hungarian": "A király adókedvezményt adott a városoknak.", "english": "The king granted tax relief to the towns."}]},
        {"lemma": "önkormányzati jog", "pos": "noun", "cefr": "B1", "translation": "self-government right", "examples": [{"hungarian": "Önkormányzati jogokat kaptak a polgárok.", "english": "The citizens received rights of self-government."}]},
        {"lemma": "radikális", "pos": "adj", "cefr": "B1", "translation": "radical", "examples": [{"hungarian": "Radikális fordulatot hajtott végre a védelempolitikában.", "english": "He carried out a radical turn in defense policy."}]},
        {"lemma": "pótol", "pos": "verb", "cefr": "B1", "translation": "to replace / make up for", "examples": [{"hungarian": "Pótolni kellett az elveszett lakosságot.", "english": "The lost population had to be replaced."}]},
        {"lemma": "kötelék", "pos": "noun", "cefr": "B1", "translation": "bond / alliance", "examples": [{"hungarian": "Házassággal pecsételték meg a szövetségi köteléket.", "english": "They sealed the alliance bond with a marriage."}]},
        {"lemma": "rom", "pos": "noun", "cefr": "B1", "translation": "ruin", "examples": [{"hungarian": "A romokból új, erős királyság született.", "english": "Out of the ruins, a new, strong kingdom was born."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-tatarjaras-04-gr.json", {
    "title": "Cél- és eredményhatározói mondatszerkezetek (azért, hogy; úgy, hogy)",
    "level": "B1",
    "rules": [
        {
            "id": "purpose-policy",
            "title": "Expressing Royal Purpose (azért, hogy + felszólító mód)",
            "text": "When royal reforms have clear goals: *Béla kedvezményeket adott azért, hogy a hospesek letelepedjenek.* (Béla gave privileges so that the settlers would settle.)",
            "tip": "Subjunctive suffix *-jon / -jen* is mandatory after *hogy* in purpose clauses."
        },
        {
            "id": "manner-result",
            "title": "Result and Manner Clauses (úgy, hogy / oly módon)",
            "text": "*Úgy építette újjá az országot, hogy az ellenállhasson a támadásnak.* (He rebuilt the country in such a way that it could resist an attack.)",
            "tip": "Combines *úgy* with indicative or potential conditional."
        }
    ],
    "examples": [
        {"spanish": "IV. Béla azért telepített be kunokat, hogy megerősítse a hadsereget.", "english": "Béla IV settled Cumans in order to strengthen the army."},
        {"spanish": "Olyan jogokat adott a városoknak, amelyek segítették a fejlődést.", "english": "He gave such rights to the towns that helped development."},
        {"spanish": "Azért nevezték második honalapítónak, mert újjáépítette a hazát.", "english": "He was called the second founder because he rebuilt the homeland."}
    ]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-04-ex.json", {
    "exercises": [
        {
            "id": "b1-tatarjaras-04.ex01",
            "type": "multiple-choice",
            "title": "A második honalapító",
            "instruction": "Kire utal a 'második honalapító' elnevezés?",
            "question": "Melyik Árpád-házi király kapta a második honalapító nevet?",
            "options": ["IV. Béla", "Szent István", "Szent László", "Könyves Kálmán"],
            "correctIndex": 0,
            "explanation": "IV. Bélát hatalmas országépítő és védelmi munkájáért hívják második honalapítónak.",
            "teaches": ["masodik-honalapito", "ujjaepites"]
        },
        {
            "id": "b1-tatarjaras-04.ex02",
            "type": "fill-blank",
            "title": "A tatár kivonulás oka",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A tatárok 1242 tavaszán ___ nagykán halála miatt vonultak ki váratlanul.",
            "correctAnswer": "Ögödej",
            "options": ["Ögödej", "Julianus", "István", "Mátyás"],
            "teaches": ["kivonulas"]
        },
        {
            "id": "b1-tatarjaras-04.ex03",
            "type": "sentence-builder",
            "title": "Telepesek behívása",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Béla", "király", "hospeseket", "telepített", "be", "a", "népesség", "pótlására."],
            "correctSentence": "Béla király hospeseket telepített be a népesség pótlására.",
            "english": "King Béla settled guest settlers to replace the population.",
            "teaches": ["hospes", "potol", "betelepit"]
        },
        {
            "id": "b1-tatarjaras-04.ex04",
            "type": "multiple-choice",
            "title": "Betelepülő népek",
            "instruction": "Mely népek kaptak szállásterületet az Alföldön a tatárjárás után?",
            "question": "Kiket telepített le IV. Béla a Duna-Tisza közén és a Tiszántúlon?",
            "options": ["A kunokat és a jászokat", "Csak spanyol katonákat", "Egyiptomi hajósokat", "Senkit nem engedett be"],
            "correctIndex": 0,
            "explanation": "A kunok és a jászok az Alföldön kaptak önálló szállásterületeket (Kunság, Jászság).",
            "teaches": ["betelepit", "elneptelenedett"]
        },
        {
            "id": "b1-tatarjaras-04.ex05",
            "type": "fill-blank",
            "title": "Célhatározó (azért, hogy)",
            "instruction": "Válaszd ki a helyes kötőszót!",
            "sentence": "IV. Béla várakat épített ___, hogy megvédje az országot egy újabb támadástól.",
            "correctAnswer": "azért",
            "options": ["azért", "miatt", "után", "pedig"],
            "teaches": ["ujjaepites"]
        },
        {
            "id": "b1-tatarjaras-04.ex06",
            "type": "sentence-builder",
            "title": "Városi kiváltságok",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "király", "adókedvezményeket", "és", "önkormányzati", "jogokat", "adott."],
            "correctSentence": "A király adókedvezményeket és önkormányzati jogokat adott.",
            "english": "The king granted tax exemptions and self-government rights.",
            "teaches": ["adokedvezmeny", "onkormanyzati-jog"]
        },
        {
            "id": "b1-tatarjaras-04.ex07",
            "type": "multiple-choice",
            "title": "Dinasztikus kapcsolat",
            "instruction": "Hogyan erősítette meg a királyi család a szövetséget a kunokkal?",
            "question": "Kit vett feleségül IV. Béla fia, István herceg?",
            "options": ["Erzsébet kun hercegnőt", "Egy francia királylányt", "Egy római hercegnőt", "Nem nősült meg"],
            "correctIndex": 0,
            "explanation": "István herceg feleségül vette Erzsébet kun hercegnőt, szoros dinasztikus kapcsolatot hozva létre.",
            "teaches": ["kotelek"]
        },
        {
            "id": "b1-tatarjaras-04.ex08",
            "type": "fill-blank",
            "title": "Újjáépítés sikere",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A király hatalmas munkával újjáépítette a romokban heverő ___.",
            "correctAnswer": "országot",
            "options": ["országot", "autót", "tengert", "csillagot"],
            "teaches": ["ujjaepites", "rom"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-tatarjaras-04.json", make_lesson(
    "lesson.b1.tatarjaras-04",
    "IV. Béla, a második honalapító (Béla IV, the Second Founder)",
    "Cél- és eredményhatározói mondatszerkezetek",
    [
        "In this fourth lesson, we explore the extraordinary resilience and reconstruction of Hungary under King Béla IV, revered as the 'Second Founder of the State' (*második honalapító*).",
        "You will learn about the sudden Mongol withdrawal in 1242 after the death of Great Khan Ögedei, the resettlement of Cumans (*kunok*) and Jazygians (*jászok*), the arrival of German guest settlers (*hospesek*), and urban privileges.",
        "We also practice purpose clauses with *azért, hogy* and result structures."
    ],
    [
        "I can explain why Béla IV is called the 'Second Founder of the State'.",
        "I can state the geopolitical cause of the Mongol withdrawal in 1242 (death of Ögedei).",
        "I can describe the resettlement policies involving Cumans, Jazygians, and German hospes settlers.",
        "I can construct purpose and result clauses (*azért, hogy*) fluently."
    ],
    "stories/world/b1/b1-tatarjaras-04-belaujjapitese.json",
    "vocabulary/b1/b1-tatarjaras-04-voc.json",
    "grammar/b1/b1-tatarjaras-04-gr.json",
    "exercises/b1/b1-tatarjaras-04-ex.json",
    [f"b1-tatarjaras-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: Kővárak építése és a megerősített városok
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras-05-kovarak.json", make_story(
    "story.b1.tatarjaras.05",
    "A kővárak kora, Buda megalapítása és a második tatárjárás (1285)",
    "The stone castle revolution: the founding of Buda Castle (1247), Visegrád citadel, noble fortified castles, walled royal free cities, and the total defeat of the second Mongol invasion in 1285.",
    "Buda vára és Visegrád",
    ["eredményhatározók és védelmi terminológia"],
    ["Kővárak építése", "Buda megalapítása 1247", "Visegrádi fellegvár", "1285-ös győzelem"],
    [
        "A tatárjárás legfőbb tanulsága az volt, hogy csak a masszív kővárak tudnak ellenállni a nomád hadaknak. IV. Béla ezért felhagyott a korábbi királyi monopóliummal, és földadományokkal ösztönözte a nemeseket és főurakat kővárak építésére.",
        "Maga a király mintegy száz új kővárat építtetett országszerte. Közülük kiemelkedett a visegrádi fellegvár és az új királyi székhely: a Budai Várhegyen 1247 körül felépített vár.",
        "A király fallal körülvett szabad királyi városokat hozott létre (Buda, Pest, Székesfehérvár, Sopron, Nagyszombat), amelyek polgárai önvédelmi feladatokat láttak el.",
        "A védelmi reformok hatékonysága 1285-ben bizonyosodott be, amikor a tatárok második alkalommal törtek be Magyarországra. A megerősített kővárak és a felkészült hadsereg tönkreverte a támadókat, megfutamítva a kán seregeit.",
        "A kővárak és városfalak rendszere megmentette a keresztény Magyar Királyságot, és évszázadokra meghatározta a magyar táj és településhálózat arculatát."
    ],
    [
        {"lemma": "kővár", "pos": "noun", "cefr": "B1", "gloss": "stone castle / stone fortress"},
        {"lemma": "szabad királyi város", "pos": "noun", "cefr": "B1", "gloss": "royal free city"},
        {"lemma": "városfal", "pos": "noun", "cefr": "B1", "gloss": "town wall / city rampart"},
        {"lemma": "visszaver", "pos": "verb", "cefr": "B1", "gloss": "to repel / beat back"}
    ],
    [
        {
            "question": "Melyik híres várat alapította meg IV. Béla király 1247 körül az új királyi székhelyként?",
            "options": ["A Budai Várat a Várhegyen", "A versailles-i kastélyt", "A Tower of Londont", "A Schönbrunni kastélyt"],
            "correctIndex": 0,
            "explanation": "IV. Béla építtette fel a Budai Várat a Várhegyen a tatárjárás után."
        },
        {
            "question": "Hogyan ösztönözte IV. Béla a nemeseket kővárak építésére?",
            "options": ["Földbirtokokat adományozott azoknak, akik kővárat emeltek", "Katonai büntetéssel fenyegette őket", "Betiltotta a magánvárakat", "Minden pénzt elvett tőlük"],
            "correctIndex": 0,
            "explanation": "Béla birtokadományokkal kötelezte és motiválta a főurakat szilárd kővárak építésére."
        },
        {
            "question": "Mi történt, amikor a tatárok 1285-ben másodszor is megtámadták Magyarországot?",
            "options": ["A megerősített kővárak és a hadsereg sikeresen visszaverte és tönkreverte a tatárokat", "Az ország teljesen elpusztult", "A király újra Trau várába menekült", "A tatárok elfoglalták Budát"],
            "correctIndex": 0,
            "explanation": "1285-ben az új kővárak rendszere miatt a magyar seregek megsemmisítő vereséget mértek a betörő tatárokra."
        }
    ]
))

write_json(VOCAB_DIR / "b1-tatarjaras-05-voc.json", {
    "title": "Kővárak építése és a megerősített városok",
    "words": [
        {"lemma": "kővár", "pos": "noun", "cefr": "B1", "translation": "stone castle", "examples": [{"hungarian": "Száz új kővár épült a tatárjárás után.", "english": "A hundred new stone castles were built after the Mongol invasion."}]},
        {"lemma": "szabad királyi város", "pos": "noun", "cefr": "B1", "translation": "royal free city", "examples": [{"hungarian": "A szabad királyi városok fallal vették körül magukat.", "english": "The royal free cities surrounded themselves with walls."}]},
        {"lemma": "városfal", "pos": "noun", "cefr": "B1", "translation": "town wall", "examples": [{"hungarian": "Erős kő városfal védte a polgárokat.", "english": "A strong stone town wall protected the citizens."}]},
        {"lemma": "visszaver", "pos": "verb", "cefr": "B1", "translation": "to beat back / repel", "examples": [{"hungarian": "1285-ben sikeresen visszaverték a második tatár támadást.", "english": "In 1285 they successfully repelled the second Tatar attack."}]},
        {"lemma": "fellegvár", "pos": "noun", "cefr": "B1", "translation": "citadel", "examples": [{"hungarian": "A visegrádi fellegvár stratégiai ponton áll.", "english": "The Visegrád citadel stands on a strategic point."}]},
        {"lemma": "tanulság", "pos": "noun", "cefr": "B1", "translation": "lesson / moral", "examples": [{"hungarian": "Levonták a háború legfontosabb tanulságát.", "english": "They drew the most important lesson of the war."}]},
        {"lemma": "monopólium", "pos": "noun", "cefr": "B1", "translation": "monopoly", "examples": [{"hungarian": "Feladta a királyi várépítési monopóliumot.", "english": "He gave up the royal castle-building monopoly."}]},
        {"lemma": "ösztönöz", "pos": "verb", "cefr": "B1", "translation": "to encourage / incentivize", "examples": [{"hungarian": "Birtokokkal ösztönözte a nemeseket a várépítésre.", "english": "He incentivized the nobles to build castles with estates."}]},
        {"lemma": "székhely", "pos": "noun", "cefr": "B1", "translation": "seat / capital", "examples": [{"hungarian": "Buda lett az ország új királyi székhelye.", "english": "Buda became the new royal seat of the country."}]},
        {"lemma": "hatékonyság", "pos": "noun", "cefr": "B1", "translation": "effectiveness / efficiency", "examples": [{"hungarian": "A kővárak hatékonysága bebizonyosodott.", "english": "The effectiveness of the stone castles was proven."}]},
        {"lemma": "polgár", "pos": "noun", "cefr": "B1", "translation": "burgher / citizen", "examples": [{"hungarian": "A városi polgárok védték a bástyákat.", "english": "The town burghers defended the bastions."}]},
        {"lemma": "megfutamít", "pos": "verb", "cefr": "B1", "translation": "to put to flight / rout", "examples": [{"hungarian": "A magyar csapatok megfutamították az ellenséget.", "english": "The Hungarian troops routed the enemy."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-tatarjaras-05-gr.json", {
    "title": "Eredményhatározói kifejezések és védelmi szintaxis",
    "level": "B1",
    "rules": [
        {
            "id": "resultative-participles",
            "title": "Resultative Participles (megerősített, körülvett)",
            "text": "Describe fortified states using past participles: *fallal körülvett városok* (walled cities), *megerősített kővárak* (fortified stone castles), *felkészült sereg* (prepared army).",
            "tip": "Precedes the modified noun directly."
        },
        {
            "id": "proof-construction-bebizonyosodik",
            "title": "Proof and Confirmation Verbs (bebizonyosodik, kiderül)",
            "text": "*A reformok hatékonysága 1285-ben bizonyosodott be.* (The effectiveness of the reforms was proven in 1285.) *Kiderült, hogy a kővárak megvédik az országot.*",
            "tip": "Combines prefixed verb with subordinate clause."
        }
    ],
    "examples": [
        {"spanish": "A kőfalakkal körülvett városok megvédték a lakosságot.", "english": "The cities surrounded with stone walls protected the population."},
        {"spanish": "1285-ben bebizonyosodott a várak hatékonysága.", "english": "In 1285, the effectiveness of the castles was proven."},
        {"spanish": "IV. Béla felépítette a Budai Várat az új székhelyként.", "english": "Béla IV built Buda Castle as the new seat."}
    ]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-05-ex.json", {
    "exercises": [
        {
            "id": "b1-tatarjaras-05.ex01",
            "type": "multiple-choice",
            "title": "Buda várának alapítása",
            "instruction": "Melyik uralkodó alapította meg a Budai Várat?",
            "question": "Ki építtette fel a Várhegyen az új királyi székhelyet 1247 körül?",
            "options": ["IV. Béla", "Szent István", "Mátyás király", "Károly Róbert"],
            "correctIndex": 0,
            "explanation": "IV. Béla alapította meg a Budai Várat a tatárjárás utáni védelmi program részeként.",
            "teaches": ["szekhely", "kovar"]
        },
        {
            "id": "b1-tatarjaras-05.ex02",
            "type": "fill-blank",
            "title": "Városfalak építése",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A szabad királyi városokat erős kő ___ vették körül a védelem érdekében.",
            "correctAnswer": "városfallal",
            "options": ["városfallal", "virággal", "szalaggal", "erdővel"],
            "teaches": ["varosfal", "szabad-kiralyi-varos"]
        },
        {
            "id": "b1-tatarjaras-05.ex03",
            "type": "sentence-builder",
            "title": "Második tatár betörés (1285)",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["1285-ben", "a", "magyar", "hadsereg", "sikeresen", "visszaverte", "a", "második", "tatár", "támadást."],
            "correctSentence": "1285-ben a magyar hadsereg sikeresen visszaverte a második tatár támadást.",
            "english": "In 1285 the Hungarian army successfully repelled the second Tatar attack.",
            "teaches": ["visszaver", "megfutamit"]
        },
        {
            "id": "b1-tatarjaras-05.ex04",
            "type": "multiple-choice",
            "title": "Kővárépítési program",
            "instruction": "Hogyan változtatta meg a védelempolitikát IV. Béla?",
            "question": "Mit ösztönzött a király földadományokkal a tatárjárás után?",
            "options": ["Masszív kővárak építését országszerte", "Minden fegyver megsemmisítését", "Fából készült falvak építését", "A városok elhagyását"],
            "correctIndex": 0,
            "explanation": "IV. Béla birtokadományokkal segítette és ösztönözte a nemeseket szilárd kővárak építésére.",
            "teaches": ["kovar", "osztonoz", "monopolium"]
        },
        {
            "id": "b1-tatarjaras-05.ex05",
            "type": "fill-blank",
            "title": "Visegrádi fellegvár",
            "instruction": "Válaszd ki a helyes szót!",
            "sentence": "A Duna-kanyarban felépült visegrádi ___ a királyság kulcsfontosságú erődje lett.",
            "correctAnswer": "fellegvár",
            "options": ["fellegvár", "hajó", "malom", "híd"],
            "teaches": ["fellegvar", "kovar"]
        },
        {
            "id": "b1-tatarjaras-05.ex06",
            "type": "sentence-builder",
            "title": "A reformok hatékonysága",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "kővárak", "hatékonysága", "1285-ben", "fényesen", "bebizonyosodott."],
            "correctSentence": "A kővárak hatékonysága 1285-ben fényesen bebizonyosodott.",
            "english": "The effectiveness of the stone castles was brilliantly proven in 1285.",
            "teaches": ["hatekonysag", "tanulsag"]
        },
        {
            "id": "b1-tatarjaras-05.ex07",
            "type": "multiple-choice",
            "title": "Szabad királyi városok szerepe",
            "instruction": "Mi volt a szabad királyi városok polgárainak feladata?",
            "question": "Milyen kötelességük volt a fallal védett városok polgárainak?",
            "options": ["Önvédelmi feladatokat láttak el és védték a bástyákat", "Csak a tengerparton nyaraltak", "Nem viselhettek fegyvert soha", "Kizárólag adót fizettek védelem nélkül"],
            "correctIndex": 0,
            "explanation": "A szabad királyi városok polgárai maguk gondoskodtak a városfalak és bástyák fegyveres védelméről.",
            "teaches": ["szabad-kiralyi-varos", "polgar"]
        },
        {
            "id": "b1-tatarjaras-05.ex08",
            "type": "fill-blank",
            "title": "A tatárjárás tanulsága",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A király levonta a háború legfontosabb ___ a védelem megerősítésére.",
            "correctAnswer": "tanulságát",
            "options": ["tanulságát", "pénzét", "hajóját", "térképét"],
            "teaches": ["tanulsag"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-tatarjaras-05.json", make_lesson(
    "lesson.b1.tatarjaras-05",
    "Kővárak építése és megerősített városok (Stone Castles & Fortified Cities)",
    "Eredményhatározói kifejezések és védelmi szintaxis",
    [
        "In this fifth lesson, we examine the stone castle revolution triggered by the Mongol invasion.",
        "You will learn about IV. Béla's decision to incentivize private stone castle building, the founding of Buda Castle (c. 1247) and Visegrád citadel, the creation of walled royal free cities (*szabad királyi városok*), and the decisive victory over the second Mongol invasion in 1285.",
        "We also practice resultative participles (*megerősített, körülvett*) and proof structures (*bebizonyosodik*)."
    ],
    [
        "I can describe the stone castle building program and the founding of Buda Castle (1247).",
        "I can define the concept and defensive role of royal free cities (*szabad királyi városok*).",
        "I can state the historical outcome of the second Mongol invasion of 1285.",
        "I can use resultative participles in descriptive historical prose."
    ],
    "stories/world/b1/b1-tatarjaras-05-kovarak.json",
    "vocabulary/b1/b1-tatarjaras-05-voc.json",
    "grammar/b1/b1-tatarjaras-05-gr.json",
    "exercises/b1/b1-tatarjaras-05-ex.json",
    [f"b1-tatarjaras-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 6 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-tatarjaras.json", make_story(
    "story.b1.tatarjaras",
    "A tatárjárás és a második honalapítás (1241–1242)",
    "The complete saga of the Mongol Invasion and the Second State Foundation: Friar Julian's warning, the disaster at Muhi (1241), the frozen Danube and Trau fortress, Béla IV's reconstruction program, the stone castles of Buda and Visegrád, and the triumph of 1285.",
    "Kárpát-medence",
    ["összetett mondatszerkezetek", "történeti szintézis"],
    ["Tatárjárás 1241–1242", "Muhi csata", "Második honalapítás", "Kővárak és Buda"],
    [
        "1235-ben Julianus barát felfedezte a Volga melletti Magna Hungariát, de második útja után már Batu kán fenyegető levelével tért vissza a közeledő mongol világbirodalomról.",
        "1241. április 11–12-én a Sajó menti muhi csatában a szűk szekértáborban összezsúfolódott magyar királyi sereg katasztrofális vereséget szenvedett a tatár főseregtől, de IV. Béla hívei segítségével megmenekült.",
        "A fagyos télen a tatárok átkeltek a Duna jegén, felégették a védtelen falvakat, míg a király az adriai Trau sziklavárában talált menedéket. A pusztítást Rogerius mester Siralmas éneke örökítette meg.",
        "1242 tavaszán a mongolok Ögödej kán halála miatt kivonultak. A visszatérő IV. Béla – 'a második honalapító' – kunokat, jászokat és hospeseket telepített le, újjáépítette az országot, és mintegy száz kővárat (köztük a Budai Várat és Visegrádot) emeltetett.",
        "A védelmi reformok sikerét az 1285-ös második tatárjárás visszaverése igazolta, megmentve az ezeréves keresztény Magyar Királyságot."
    ],
    [
        {"lemma": "tatárjárás", "pos": "noun", "cefr": "B1", "gloss": "Mongol Invasion (1241–42)"},
        {"lemma": "muhi csata", "pos": "noun", "cefr": "B1", "gloss": "Battle of Muhi"},
        {"lemma": "második honalapító", "pos": "noun", "cefr": "B1", "gloss": "second founder of the state"},
        {"lemma": "kővár", "pos": "noun", "cefr": "B1", "gloss": "stone castle"}
    ],
    [
        {
            "question": "Mely években zajlott a magyarországi tatárjárás?",
            "options": ["1241–1242-ben", "1000-ben", "1526-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "A tatárjárás 1241 tavaszától 1242 tavaszáig tartott."
        },
        {
            "question": "Ki volt az a király, akit az ország újjáépítéséért 'második honalapítónak' neveznek?",
            "options": ["IV. Béla", "Szent István", "Szent László", "Könyves Kálmán"],
            "correctIndex": 0,
            "explanation": "IV. Bélát hívják második honalapítónak a tatárjárás utáni újjáépítés és várépítés miatt."
        },
        {
            "question": "Milyen védelmi reform bizonyult sikeresnek a mongol hadak ellen?",
            "options": ["A kővárak építése és a megerősített városfalak rendszere (pl. Buda, Visegrád)", "A falvak fegyvertelenül hagyása", "A hegyekből való elköltözés", "Kizárólag a folyókban való bízás"],
            "correctIndex": 0,
            "explanation": "A kővárak és fallal védett városok építése tette lehetővé a második támadás (1285) visszaverését."
        }
    ]
))

u6_cons_ex = []
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex01",
    "type": "multiple-choice",
    "title": "A tatárjárás éve",
    "instruction": "Mely években pusztított a tatárjárás Magyarországon?",
    "question": "Mikor történt a tatárjárás?",
    "options": ["1241–1242-ben", "895-ben", "1000-ben", "1526-ban"],
    "correctIndex": 0,
    "explanation": "A tatárjárás 1241 és 1242 között zajlott.",
    "teaches": ["tatarjaras"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex02",
    "type": "fill-blank",
    "title": "Muhi csata",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "1241 áprilisában a ___ folyó partján zajlott le a muhi csata.",
    "correctAnswer": "Sajó",
    "options": ["Sajó", "Duna", "Tisza", "Dráva"],
    "teaches": ["muhi-csata"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex03",
    "type": "sentence-builder",
    "title": "Második honalapító",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["IV.", "Bélát", "az", "ország", "újjáépítéséért", "második", "honalapítónak", "nevezik."],
    "correctSentence": "IV. Bélát az ország újjáépítéséért második honalapítónak nevezik.",
    "english": "Béla IV is called the second founder of the state for rebuilding the country.",
    "teaches": ["masodik-honalapito", "ujjaepites"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex04",
    "type": "multiple-choice",
    "title": "Julianus barát utazása",
    "instruction": "Mit talált meg Julianus barát 1235-ben?",
    "question": "Hol talált rá a keleti magyarokra Julianus?",
    "options": ["A Volga menti Magna Hungariában", "A Csendes-óceánon", "Egyiptomban", "Spanyolországban"],
    "correctIndex": 0,
    "explanation": "Julianus 1235-ben rátalált Magna Hungariára a Volga mellett.",
    "teaches": ["szerzetes", "felkutat"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex05",
    "type": "fill-blank",
    "title": "Trau vára",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "IV. Béla az adriai tengerparti ___ sziklavárába menekült a tatárok elől.",
    "correctAnswer": "Trau",
    "options": ["Trau", "Róma", "Bécs", "Prága"],
    "teaches": ["sziklavar", "uldoz"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex06",
    "type": "sentence-builder",
    "title": "Buda vára",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["IV.", "Béla", "építtette", "fel", "a", "Budai", "Várat", "a", "Várhegyen."],
    "correctSentence": "IV. Béla építtette fel a Budai Várat a Várhegyen.",
    "english": "Béla IV built Buda Castle on Castle Hill.",
    "teaches": ["kovar", "szekhely"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex07",
    "type": "multiple-choice",
    "title": "Rogerius mester műve",
    "instruction": "Melyik krónika írja le a tatárjárás pusztítását?",
    "question": "Mi a címe Rogerius mester művének?",
    "options": ["Siralmas ének (Carmen Miserabile)", "Gesta Hungarorum", "Képes Krónika", "Ómagyar Mária-siralom"],
    "correctIndex": 0,
    "explanation": "Rogerius mester a Siralmas énekben írta meg a tatárjárás megrázó eseményeit.",
    "teaches": ["szemtanu", "kanonok"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex08",
    "type": "fill-blank",
    "title": "Tatár kivonulás éve",
    "instruction": "Válaszd ki az évet!",
    "sentence": "A tatár sereg ___ tavaszán vonult ki Magyarországról.",
    "correctAnswer": "1242",
    "options": ["1242", "1526", "1848", "1000"],
    "teaches": ["kivonulas"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex09",
    "type": "sentence-builder",
    "title": "Második tatárjárás (1285)",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["1285-ben", "a", "magyar", "kővárak", "sikeresen", "megállították", "a", "tatárokat."],
    "correctSentence": "1285-ben a magyar kővárak sikeresen megállították a tatárokat.",
    "english": "In 1285, the Hungarian stone castles successfully stopped the Tatars.",
    "teaches": ["visszaver", "hatekonysag"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex10",
    "type": "multiple-choice",
    "title": "Betelepülő népek",
    "instruction": "Kiket telepített le IV. Béla az Alföldre?",
    "question": "Mely nomád népeket integrálta a király a tatárjárás után?",
    "options": ["A kunokat és a jászokat", "Csak görög filozófusokat", "Skót lovagokat", "Senkit nem engedett be"],
    "correctIndex": 0,
    "explanation": "A kunok és jászok letelepítése pótolta a hatalmas lakossági veszteségeket.",
    "teaches": ["betelepit", "potol"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex11",
    "type": "fill-blank",
    "title": "Befagyott Duna",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "1241/42 kemény telén a Duna ___ , és a tatárok átkeltek a Dunántúlra.",
    "correctAnswer": "befagyott",
    "options": ["befagyott", "kiszáradt", "eltűnt", "felforrt"],
    "teaches": ["befagy", "pusztitas"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex12",
    "type": "sentence-builder",
    "title": "Hospes telepesek",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["A", "német", "hospesek", "új", "városokat", "és", "bányákat", "nyitottak."],
    "correctSentence": "A német hospesek új városokat és bányákat nyitottak.",
    "english": "The German guest settlers opened new towns and mines.",
    "teaches": ["hospes", "szabad-kiralyi-varos"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex13",
    "type": "multiple-choice",
    "title": "A tatár vezér",
    "instruction": "Ki vezette a mongol hordákat Magyarország ellen?",
    "question": "Hogy hívták a tatár invázió főseregének vezérét?",
    "options": ["Batu kán", "Julius Caesar", "Nagy Sándor", "Szulejmán szultán"],
    "correctIndex": 0,
    "explanation": "Batu kán vezette az 1241–42-es mongol hadjáratot.",
    "teaches": ["fenyegeto-level"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex14",
    "type": "fill-blank",
    "title": "Kővárépítés ösztönzése",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Béla király földadományokkal ___ a nemeseket kővárak építésére.",
    "correctAnswer": "ösztönözte",
    "options": ["ösztönözte", "büntette", "tiltotta", "kerülte"],
    "teaches": ["osztonoz", "kovar"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex15",
    "type": "sentence-builder",
    "title": "Visegrádi vár",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["A", "visegrádi", "fellegvár", "a", "királyság", "egyik", "legerősebb", "erődítménye", "volt."],
    "correctSentence": "A visegrádi fellegvár a királyság egyik legerősebb erődítménye volt.",
    "english": "The Visegrád citadel was one of the strongest fortifications of the kingdom.",
    "teaches": ["fellegvar", "kovar"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex16",
    "type": "multiple-choice",
    "title": "Szekértábor csapdája",
    "instruction": "Mi okozta a magyar sereg vesztét Muhinál?",
    "question": "Miért volt hátrányos a szekértábor?",
    "options": ["A szűk hely miatt a sereg összezsúfolódott és nem tudott manőverezni", "Mert túl messze volt a folyótól", "Mert a szekerek felrobbantak", "Mert a katonák hazamentek"],
    "correctIndex": 0,
    "explanation": "A szűk szekértábor megakadályozta a lovasság manőverezését és csapdává vált.",
    "teaches": ["szekertabor", "manoverezik"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex17",
    "type": "fill-blank",
    "title": "Szabad királyi városok",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A szabad királyi városok polgárai kőfallal védték a ___.",
    "correctAnswer": "várost",
    "options": ["várost", "tengert", "erdőt", "mezőt"],
    "teaches": ["szabad-kiralyi-varos", "varosfal"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex18",
    "type": "sentence-builder",
    "title": "Célhatározó mondat",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["IV.", "Béla", "azért", "épített", "várakat,", "hogy", "megvédje", "a", "hazát."],
    "correctSentence": "IV. Béla azért épített várakat, hogy megvédje a hazát.",
    "english": "Béla IV built castles in order to protect the homeland.",
    "teaches": ["ujjaepites"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex19",
    "type": "multiple-choice",
    "title": "A kivonulás oka",
    "instruction": "Miért hagyta el Batu kán Magyarországot 1242-ben?",
    "question": "Melyik mongol nagykán halt meg 1241 végén?",
    "options": ["Ögödej nagykán", "Batu kán", "Dzsingisz kán", "Kubiláj kán"],
    "correctIndex": 0,
    "explanation": "Ögödej nagykán halála miatt Batu kán sietett a kánválasztó gyűlésre Belső-Ázsiába.",
    "teaches": ["kivonulas"]
})
u6_cons_ex.append({
    "id": "b1-tatarjaras-consolidation.ex20",
    "type": "fill-blank",
    "title": "Újjászületett állam",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A kővárak és az újjáépítés megmentette a magyar állam ezeréves ___.",
    "correctAnswer": "megmaradását",
    "options": ["megmaradását", "eltűnését", "vesztét", "feledését"],
    "teaches": ["masodik-honalapito", "tatarjaras"]
})

write_json(EXERCISES_DIR / "b1-tatarjaras-consolidation-ex.json", {"exercises": u6_cons_ex})

write_json(LESSONS_DIR / "b1-tatarjaras-consolidation.json", make_consolidation_lesson(
    "lesson.b1.tatarjaras-consolidation",
    "The Mongol Invasion (1241–42) - Consolidation",
    [
        "Congratulations on completing Unit 6 and concluding Block 1 of the Hungarian Citizenship Track!",
        "In this unit, you have mastered the pivotal history of the Mongol Invasion (*Tatárjárás*, 1241–42): Friar Julian's discovery of Magna Hungaria, the disaster of the Battle of Muhi (1241), the frozen winter of destruction, King Béla IV's refuge in Trau, and the visionary reconstruction under 'the Second Founder of the State' (stone castles, Buda Castle, Visegrád, hospes settlers, repelling the 1285 invasion).",
        "Review your knowledge across all 20 consolidation exercises and celebrate mastering early Hungarian statehood."
    ],
    [
        "I can summarize the timeline and key events of the Mongol Invasion (1241–42, Muhi, Trau).",
        "I can explain why Béla IV is honored as the 'Second Founder of the State'.",
        "I can describe the stone castle building program and the founding of Buda Castle (1247).",
        "I can analyze the outcome of the 1285 second Mongol invasion in fluent B1 Hungarian."
    ],
    "stories/world/b1/b1-tatarjaras.json",
    "exercises/b1/b1-tatarjaras-consolidation-ex.json",
    [f"b1-tatarjaras-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 6 (b1-tatarjaras) overhaul complete!")
