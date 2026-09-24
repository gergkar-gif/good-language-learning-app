# -*- coding: utf-8 -*-
"""
Full Unit 7 Overhaul: The Angevin Kings (b1-anjouk)
Lessons:
1. Károly Róbert és a gazdasági megújulás
2. A visegrádi királytalálkozó (1335)
3. Nagy Lajos lovagkirály és az 1351-es törvények (ősiség / aviticitas, kilenced)
4. Luxemburgi Zsigmond és a konstanzi zsinat (1387–1437)
5. Hunyadi János és a nándorfehérvári diadal (1456, déli harangszó)
Consolidation: Unit 7 Capstone
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
# Lesson 1: Károly Róbert
# -----------------
write_json(STORIES_DIR / "b1-anjouk-01-karolyrobert.json", make_story(
    "story.b1.anjouk.01",
    "Károly Róbert és a gazdasági megújulás",
    "Charles Robert of Anjou (1308–1342): victory at Rozgony (1312), mining reforms, golden florin, and the gate tax.",
    "Temesvár, Visegrád és Rozgony",
    ["számszerű adatok és gazdasági szakkifejezések"],
    ["Károly Róbert", "Aranyforint", "Rozgonyi csata 1312", "Gazdasági reformok"],
    [
        "Az Árpád-ház kihalása után hosszas küzdelmek árán a nápolyi Anjou-házból származó Károly Róbert (1308–1342) szerezte meg a magyar trónt. 1312-ben a rozgonyi csatában legyőzte az Aba nemzetséget, majd felszámolta a kiskirályok tartományi uralmát.",
        "A rend helyreállítása után Károly Róbert átfogó gazdasági reformokat vezetett be. Megreformálta a bányászatot: a bányabér (urbura) egyharmadát átengedte a birtokosoknak, ami hatalmas arany- és ezüstbányászati fellendülést eredményezett Körmöcbányán.",
        "Károly értékálló, firenzei mintájú aranyforintot veretett, amely Európa egyik legmegbízhatóbb fizetőeszközévé vált.",
        "A kieső királyi jövedelmek pótlására bevezette az első közvetlen állami adót, a kapuadót, amelyet minden olyan jobbágytelek után meg kellett fizetni, amelynek kapuján egy szénásszekér átfért.",
        "Károly Róbert reformjai révén a Magyar Királyság Európa legnagyobb aranytermelőjévé és a kontinens egyik legvirágzóbb gazdaságává vált."
    ],
    [
        {"lemma": "aranyforint", "pos": "noun", "cefr": "B1", "gloss": "golden florin"},
        {"lemma": "kapuadó", "pos": "noun", "cefr": "B1", "gloss": "gate tax"},
        {"lemma": "urbura", "pos": "noun", "cefr": "B1", "gloss": "mining royalty"},
        {"lemma": "értékálló", "pos": "adj", "cefr": "B1", "gloss": "stable in value"}
    ],
    [
        {"question": "Melyik csatában győzte le Károly Róbert a kiskirályokat 1312-ben?", "options": ["A rozgonyi csatában", "A muhi csatában", "A mohácsi csatában", "Az augsburgi csatában"], "correctIndex": 0, "explanation": "Az 1312-es rozgonyi csata törte meg a tartományurak ellenállását."},
        {"question": "Milyen stabil pénzt vezetett be Károly Róbert?", "options": ["Értékálló aranyforintot", "Papírbankjegyet", "Rézgarast", "Ezüstkoronát"], "correctIndex": 0, "explanation": "Károly Róbert a firenzei mintájú aranyforintot verette."},
        {"question": "Mi volt a kapuadó?", "options": ["Közvetlen állami adó minden jobbágy kapu után", "Vám a budai várkapunál", "Hídpénz a Dunán", "Külföldi utazási adó"], "correctIndex": 0, "explanation": "A kapuadó az első közvetlen állami adó volt minden jobbágytelek után."}
    ]
))

write_json(VOCAB_DIR / "b1-anjouk-01-voc.json", {
    "title": "Károly Róbert és a gazdasági megújulás",
    "words": [
        {"lemma": "aranyforint", "pos": "noun", "cefr": "B1", "translation": "golden florin", "examples": [{"hungarian": "A magyar aranyforint megbízható valuta volt.", "english": "The Hungarian golden florin was a reliable currency."}]},
        {"lemma": "kapuadó", "pos": "noun", "cefr": "B1", "translation": "gate tax", "examples": [{"hungarian": "A kapuadó rendszeres királyi jövedelmet adott.", "english": "The gate tax provided regular royal income."}]},
        {"lemma": "urbura", "pos": "noun", "cefr": "B1", "translation": "mining royalty", "examples": [{"hungarian": "Az urbura egyharmada a földbirtokost illette.", "english": "One third of the mining royalty belonged to the landowner."}]},
        {"lemma": "értékálló", "pos": "adj", "cefr": "B1", "translation": "stable in value", "examples": [{"hungarian": "Értékálló pénzt vertek a pénzverdében.", "english": "They minted currency of stable value in the mint."}]},
        {"lemma": "felszámol", "pos": "verb", "cefr": "B1", "translation": "to eliminate / dismantle", "examples": [{"hungarian": "Felszámolta a kiskirályok hatalmát.", "english": "He dismantled the power of the petty kings."}]},
        {"lemma": "nemesfém", "pos": "noun", "cefr": "B1", "translation": "precious metal", "examples": [{"hungarian": "Az arany és ezüst fontos nemesfém volt.", "english": "Gold and silver were important precious metals."}]},
        {"lemma": "fellendülés", "pos": "noun", "cefr": "B1", "translation": "boom / upswing", "examples": [{"hungarian": "Gazdasági fellendülés követte a reformokat.", "english": "An economic boom followed the reforms."}]},
        {"lemma": "pénzverés", "pos": "noun", "cefr": "B1", "translation": "coin minting", "examples": [{"hungarian": "Körmöcbánya volt a pénzverés központja.", "english": "Körmöcbánya was the center of coin minting."}]},
        {"lemma": "kincstár", "pos": "noun", "cefr": "B1", "translation": "treasury", "examples": [{"hungarian": "A kincstár bevételei megsokszorozódtak.", "english": "Revenues of the treasury multiplied."}]},
        {"lemma": "jobbágytelek", "pos": "noun", "cefr": "B1", "translation": "serf holding", "examples": [{"hungarian": "A jobbágytelkek után fizették a kapuadót.", "english": "The gate tax was paid on serf holdings."}]},
        {"lemma": "átfogó", "pos": "adj", "cefr": "B1", "translation": "comprehensive", "examples": [{"hungarian": "Átfogó reformprogramot vezetett be.", "english": "He introduced a comprehensive reform program."}]},
        {"lemma": "helyreállít", "pos": "verb", "cefr": "B1", "translation": "to restore", "examples": [{"hungarian": "Helyreállította a központi hatalmat.", "english": "He restored central power."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-anjouk-01-gr.json", {
    "title": "Számszerű adatok és gazdasági kifejezések (egyharmada, révén)",
    "level": "B1",
    "rules": [
        {
            "id": "fractions-usage",
            "title": "Fractions with Possessive Suffixes",
            "text": "Express proportions with *egyharmada* (one-third), *fele* (half), *kétharmada* (two-thirds). *A bányabér egyharmadát átengedte a király.*",
            "tip": "Case endings attach after possessive suffixes (*egyharmad-á-t*)."
        },
        {
            "id": "reve-postposition",
            "title": "Postposition 'révén' (By means of / Through)",
            "text": "*A reformok révén az ország gazdag lett.* (Through the reforms, the country became rich.)",
            "tip": "Requires possessive nouns."
        }
    ],
    "examples": [
        {"spanish": "A reformok révén Magyarország gazdaggá vált.", "english": "Through the reforms, Hungary became wealthy."},
        {"spanish": "A bányabér egyharmadát a birtokosok kapták meg.", "english": "The landowners received one-third of the mining royalty."},
        {"spanish": "Értékálló aranyforintot veretett Körmöcbányán.", "english": "He minted stable golden florins in Körmöcbánya."}
    ]
})

write_json(EXERCISES_DIR / "b1-anjouk-01-ex.json", {
    "exercises": [
        {"id": "b1-anjouk-01.ex01", "type": "multiple-choice", "title": "A rozgonyi csata", "instruction": "Válaszd ki a helyes évet!", "question": "Mikor győzte le Károly Róbert a kiskirályokat Rozgonynál?", "options": ["1312-ben", "1222-ben", "1456-ban", "1526-ban"], "correctIndex": 0, "explanation": "A rozgonyi csata 1312-ben zajlott le.", "teaches": ["rozgonyi-csata", "felszamol"]},
        {"id": "b1-anjouk-01.ex02", "type": "fill-blank", "title": "Aranyforint", "instruction": "Egészítsd ki a mondatot!", "sentence": "Károly Róbert értékálló ___ veretett Körmöcbányán.", "correctAnswer": "aranyforintot", "options": ["aranyforintot", "papírdollárt", "ezüstkrajcárt", "fakártyát"], "teaches": ["aranyforint", "ertekallo"]},
        {"id": "b1-anjouk-01.ex03", "type": "sentence-builder", "title": "A kapuadó", "instruction": "Állítsd össze a mondatot!", "words": ["Károly", "Róbert", "bevezette", "a", "kapuadót", "a", "királyságban."], "correctSentence": "Károly Róbert bevezette a kapuadót a királyságban.", "english": "Charles Robert introduced the gate tax in the kingdom.", "teaches": ["kapuado", "jobbagytelek"]},
        {"id": "b1-anjouk-01.ex04", "type": "multiple-choice", "title": "Bányabér", "instruction": "Mi volt az urbura?", "question": "Mit jelentett a bányabér reformja?", "options": ["Egyharmadát a földbirtokos kapta a bányanyitás ösztönzésére", "Minden bányát azonnal bezártak", "Megtiltották az arany exportját", "Csak külföldiek bányászhattak"], "correctIndex": 0, "explanation": "Az urbura harmadának átengedése hatalmas aranylázat indított el.", "teaches": ["urbura", "nemesfem"]},
        {"id": "b1-anjouk-01.ex05", "type": "fill-blank", "title": "Eredmény (révén)", "instruction": "Válaszd ki a helyes szót!", "sentence": "A pénzügyi reformok ___ megerősödött a kincstár.", "correctAnswer": "révén", "options": ["révén", "nélkül", "ellen", "alatt"], "teaches": ["fellendules", "kincstar"]},
        {"id": "b1-anjouk-01.ex06", "type": "sentence-builder", "title": "Nemesfémbányászat", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Magyarország", "Európa", "vezető", "aranytermelő", "állama", "lett."], "correctSentence": "Magyarország Európa vezető aranytermelő állama lett.", "english": "Hungary became Europe's leading gold-producing state.", "teaches": ["nemesfem", "penzveres"]},
        {"id": "b1-anjouk-01.ex07", "type": "multiple-choice", "title": "Az Anjou-ház", "instruction": "Honnan származott az új király?", "question": "Melyik dinasztia tagja volt Károly Róbert?", "options": ["A nápolyi Anjou-ház", "A Habsburg-ház", "A Bourbon-ház", "A Tudor-ház"], "correctIndex": 0, "explanation": "Károly Róbert az Anjou-ház nápolyi ágából érkezett.", "teaches": ["dinasztia"]},
        {"id": "b1-anjouk-01.ex08", "type": "fill-blank", "title": "Körmöcbányai pénzverde", "instruction": "Egészítsd ki a mondatot!", "sentence": "A híres aranypénzeket a felvidéki ___ verték.", "correctAnswer": "Körmöcbányán", "options": ["Körmöcbányán", "Londonban", "Párizsban", "Rómában"], "teaches": ["penzveres", "aranyforint"]}
    ]
})

write_json(LESSONS_DIR / "b1-anjouk-01.json", make_lesson(
    "lesson.b1.anjouk-01",
    "Károly Róbert és a gazdasági megújulás (Charles Robert & Economy)",
    "Számszerű adatok és gazdasági kifejezések (egyharmada, révén)",
    [
        "Welcome to Unit 7 of the Hungarian Citizenship Track, exploring the Angevin era and late medieval power.",
        "In this first lesson, we explore Charles Robert of Anjou (1308–1342): crushing the oligarchs at Rozgony (1312), introducing the stable golden florin (*aranyforint*), mining royalties (*urbura*), and the gate tax (*kapuadó*).",
        "We also practice expressing fractions (*egyharmada*) and achievements with *révén*."
    ],
    [
        "I can describe Charles Robert's victory at Rozgony (1312) and the end of the oligarchs.",
        "I can explain the economic significance of the golden florin (*aranyforint*), urbura, and gate tax (*kapuadó*).",
        "I can state Hungary's role as Europe's leading gold producer in the 14th century.",
        "I can use economic and financial vocabulary fluently in Hungarian B1."
    ],
    "stories/world/b1/b1-anjouk-01-karolyrobert.json",
    "vocabulary/b1/b1-anjouk-01-voc.json",
    "grammar/b1/b1-anjouk-01-gr.json",
    "exercises/b1/b1-anjouk-01-ex.json",
    [f"b1-anjouk-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: Visegrádi királytalálkozó (1335)
# -----------------
# (Already generated above, let's ensure it's written)
write_json(STORIES_DIR / "b1-anjouk-02-visegrad.json", make_story(
    "story.b1.anjouk.02",
    "A visegrádi királytalálkozó (1335) és a közép-európai szövetség",
    "The 1335 Congress of Visegrád: Charles Robert hosts King John of Bohemia and King Casimir III of Poland, creating new trade routes bypassing Vienna's staple right.",
    "Visegrádi királyi palota",
    ["diplomáciai kifejezések és egyeztetett többes számok"],
    ["Visegrád 1335", "Királytalálkozó", "Bécsi árumegállító jog", "Közép-európai együttműködés"],
    [
        "1335 őszén Károly Róbert magyar király történelmi csúcstalálkozóra hívta meg a visegrádi királyi palotába Luxemburgi János cseh királyt és III. Kázmér lengyel királyt.",
        "A visegrádi királytalálkozón a három uralkodó elsimította a cseh és lengyel királyság közötti évtizedes területi vitákat, és szoros szövetséget kötött.",
        "A találkozó legnagyobb gazdasági eredménye egy új kereskedelmi úthálózat megnyitása volt, amely kikerülte a bécsi árumegállító jogot, lehetővé téve a vámmentes kereskedelmet Németország felé.",
        "Károly Róbert heteken át fejedelmi pompával és bőséges lakomákkal vendégelte meg a királyi kíséreteket, bemutatva a megújult Magyar Királyság gazdagságát.",
        "Ez az 1335-ös történelmi találkozó lett a modern kori Visegrádi Négyek (V4) közép-európai együttműködésének történelmi alapköve és szimbóluma."
    ],
    [
        {"lemma": "királytalálkozó", "pos": "noun", "cefr": "B1", "gloss": "royal summit"},
        {"lemma": "árumegállító jog", "pos": "noun", "cefr": "B1", "gloss": "staple right"},
        {"lemma": "csúcstalálkozó", "pos": "noun", "cefr": "B1", "gloss": "summit meeting"},
        {"lemma": "együttműködés", "pos": "noun", "cefr": "B1", "gloss": "cooperation"}
    ],
    [
        {"question": "Melyik évben tartották a visegrádi királytalálkozót?", "options": ["1335-ben", "1222-ben", "1456-ban", "1526-ban"], "correctIndex": 0, "explanation": "A visegrádi királytalálkozó 1335-ben zajlott le."},
        {"question": "Melyik három király találkozott Visegrádon?", "options": ["A magyar, a cseh és a lengyel király", "A spanyol, a francia és az angol király", "A pápa és a német császár", "Csak magyar hercegek"], "correctIndex": 0, "explanation": "Károly Róbert, Luxemburgi János és III. Kázmér tanácskozott."},
        {"question": "Melyik modern szövetség őrzi az 1335-ös találkozó emlékét?", "options": ["A Visegrádi Négyek (V4)", "Az Európai Tanács", "A NATO", "Az ENSZ"], "correctIndex": 0, "explanation": "A V4 regionális szövetsége a visegrádi csúcs nevét és hagyományát viszi tovább."}
    ]
))

write_json(VOCAB_DIR / "b1-anjouk-02-voc.json", {
    "title": "A visegrádi királytalálkozó (1335)",
    "words": [
        {"lemma": "királytalálkozó", "pos": "noun", "cefr": "B1", "translation": "royal summit", "examples": [{"hungarian": "A visegrádi királytalálkozó megváltoztatta a kereskedelmet.", "english": "The royal summit of Visegrád changed trade."}]},
        {"lemma": "árumegállító jog", "pos": "noun", "cefr": "B1", "translation": "staple right", "examples": [{"hungarian": "Kikerülték Bécs árumegállító jogát.", "english": "They bypassed Vienna's staple right."}]},
        {"lemma": "csúcstalálkozó", "pos": "noun", "cefr": "B1", "translation": "summit meeting", "examples": [{"hungarian": "A csúcstalálkozón békét kötöttek.", "english": "At the summit meeting they made peace."}]},
        {"lemma": "együttműködés", "pos": "noun", "cefr": "B1", "translation": "cooperation", "examples": [{"hungarian": "A közép-európai együttműködés ma is él.", "english": "Central European cooperation is alive today."}]},
        {"lemma": "kereskedelmi útvonal", "pos": "noun", "cefr": "B1", "translation": "trade route", "examples": [{"hungarian": "Új kereskedelmi útvonalat nyitottak meg.", "english": "They opened a new trade route."}]},
        {"lemma": "vámmentes", "pos": "adj", "cefr": "B1", "translation": "duty-free", "examples": [{"hungarian": "Vámmentes kereskedelmi kedvezményeket adtak.", "english": "They granted duty-free trade privileges."}]},
        {"lemma": "vendégel", "pos": "verb", "cefr": "B1", "translation": "to host / entertain", "examples": [{"hungarian": "A király pompásan vendégelte meg a királyokat.", "english": "The king entertained the kings splendidly."}]},
        {"lemma": "kíséret", "pos": "noun", "cefr": "B1", "translation": "retinue / entourage", "examples": [{"hungarian": "Nagy királyi kíséret érkezett Prágából.", "english": "A large royal retinue arrived from Prague."}]},
        {"lemma": "elsimít", "pos": "verb", "cefr": "B1", "translation": "to smooth over / settle", "examples": [{"hungarian": "Elsimították a régi vitákat.", "english": "They smoothed over the old disputes."}]},
        {"lemma": "pompa", "pos": "noun", "cefr": "B1", "translation": "pomp / splendour", "examples": [{"hungarian": "Királyi pompa díszítette a visegrádi várat.", "english": "Royal pomp adorned the castle of Visegrád."}]},
        {"lemma": "szövetség", "pos": "noun", "cefr": "B1", "translation": "alliance", "examples": [{"hungarian": "Hosszú távú szövetséget kötöttek.", "english": "They formed a long-term alliance."}]},
        {"lemma": "előkép", "pos": "noun", "cefr": "B1", "translation": "precursor / prototype", "examples": [{"hungarian": "Ez a találkozó a V4 előképe.", "english": "This meeting is the precursor of the V4."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-anjouk-02-gr.json", {
    "title": "Diplomáciai kifejezések és melléknévi igenévi szerkezetek",
    "level": "B1",
    "rules": [
        {
            "id": "diplomatic-participles",
            "title": "Participles in Treaty Narratives",
            "text": "*A Visegrádon kötött szerződés* (the treaty concluded at Visegrád), *a megnyitott kereskedelmi útvonal* (the opened trade route).",
            "tip": "Participles sit directly in front of the head noun."
        },
        {
            "id": "adverbial-participle-means",
            "title": "Adverbial Participles (-va / -ve) Expressing Circumstances",
            "text": "*Kikerülve a bécsi vámokat, közvetlen utakat nyitottak.*",
            "tip": "Acts as an adverb modifying the main clause."
        }
    ],
    "examples": [
        {"spanish": "A Visegrádon kötött szövetség békét hozott a térségbe.", "english": "The alliance concluded at Visegrád brought peace to the region."},
        {"spanish": "Kikerülve a vámokat, új utakat nyitottak meg.", "english": "Bypassing customs, they opened new routes."},
        {"spanish": "A királyi csúcstalálkozó történelmi jelentőségű volt.", "english": "The royal summit was of historic significance."}
    ]
})

write_json(EXERCISES_DIR / "b1-anjouk-02-ex.json", {
    "exercises": [
        {"id": "b1-anjouk-02.ex01", "type": "multiple-choice", "title": "A visegrádi találkozó éve", "instruction": "Válaszd ki az évet!", "question": "Mikor tartották a visegrádi királytalálkozót?", "options": ["1335-ben", "1222-ben", "1456-ban", "1526-ban"], "correctIndex": 0, "explanation": "A visegrádi királytalálkozó 1335-ben zajlott le.", "teaches": ["kiralykozep", "csucstalalkozo"]},
        {"id": "b1-anjouk-02.ex02", "type": "fill-blank", "title": "Árumegállító jog", "instruction": "Egészítsd ki a mondatot!", "sentence": "Az új útvonalak kikerülték Bécs ___ jogát.", "correctAnswer": "árumegállító", "options": ["árumegállító", "repülési", "tengeri", "halászati"], "teaches": ["arumegallito-jog", "kereskedelmi-utvonal"]},
        {"id": "b1-anjouk-02.ex03", "type": "sentence-builder", "title": "Három király szövetsége", "instruction": "Állítsd össze a mondatot!", "words": ["A", "három", "király", "szoros", "szövetséget", "kötött", "Visegrádon."], "correctSentence": "A három király szoros szövetséget kötött Visegrádon.", "english": "The three kings formed a close alliance in Visegrád.", "teaches": ["szovetseg", "egyuttmukodes"]},
        {"id": "b1-anjouk-02.ex04", "type": "multiple-choice", "title": "A V4 szimbóluma", "instruction": "Melyik mai szövetség gyökerezik az 1335-ös találkozóban?", "question": "Mit szimbolizál Visegrád ma?", "options": ["A Visegrádi Négyek (V4) együttműködését", "Az Európai Bankot", "A NATO flottáját", "A G7 csoportot"], "correctIndex": 0, "explanation": "A V4 együttműködés az 1335-ös találkozóra épül.", "teaches": ["elokep", "egyuttmukodes"]},
        {"id": "b1-anjouk-02.ex05", "type": "fill-blank", "title": "Fejedelmi vendéglátás", "instruction": "Válaszd ki a megfelelő szót!", "sentence": "Károly Róbert fejedelmi ___ fogadta a vendégeket.", "correctAnswer": "pompával", "options": ["pompával", "haraggal", "fegyverrel", "csenddel"], "teaches": ["pompa", "vendegel"]},
        {"id": "b1-anjouk-02.ex06", "type": "sentence-builder", "title": "Vámmentes kereskedelem", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Kikerülve", "Bécs", "vámjait,", "új", "kereskedelmi", "utakat", "nyitottak."], "correctSentence": "Kikerülve Bécs vámjait, új kereskedelmi utakat nyitottak.", "english": "Bypassing Vienna's customs, they opened new trade routes.", "teaches": ["arumegallito-jog", "vammentes"]},
        {"id": "b1-anjouk-02.ex07", "type": "multiple-choice", "title": "Résztvevők", "instruction": "Kik voltak Károly Róbert vendégei?", "question": "Mely uralkodók érkeztek Visegrádra?", "options": ["A cseh és a lengyel király", "A francia és az angol király", "A török szultán és a perzsa sah", "A svéd király és a dán király"], "correctIndex": 0, "explanation": "A cseh és lengyel király kötött szövetséget Visegrádon.", "teaches": ["csucstalalkozo", "kiselet"]},
        {"id": "b1-anjouk-02.ex08", "type": "fill-blank", "title": "Békekötés", "instruction": "Egészítsd ki a mondatot!", "sentence": "A királyok elsimították a cseh-lengyel ___.", "correctAnswer": "ellentéteket", "options": ["ellentéteket", "zenét", "hajókat", "hegyeket"], "teaches": ["elsimit"]}
    ]
})

write_json(LESSONS_DIR / "b1-anjouk-02.json", make_lesson(
    "lesson.b1.anjouk-02",
    "A visegrádi királytalálkozó (The Congress of Visegrád - 1335)",
    "Diplomáciai kifejezések és melléknévi igenévi szerkezetek",
    [
        "In this second lesson, we study the famous 1335 Congress of Visegrád (*visegrádi királytalálkozó*).",
        "You will learn how Charles Robert hosted King John of Bohemia and King Casimir III of Poland, resolved Central European border disputes, opened new trade routes bypassing Vienna's staple right (*árumegállító jog*), and laid the foundation for the modern Visegrád Group (V4).",
        "We also practice diplomatic participles and adverbial participles (*kikerülve*)."
    ],
    [
        "I can state the date (1335) and participants (Hungary, Bohemia, Poland) of the Visegrád summit.",
        "I can explain the economic aim of bypassing Vienna's staple right (*bécsi árumegállító jog*).",
        "I can connect the 1335 meeting to modern Central European cooperation (V4).",
        "I can use diplomatic vocabulary and adverbial participles (*-va / -ve*) accurately."
    ],
    "stories/world/b1/b1-anjouk-02-visegrad.json",
    "vocabulary/b1/b1-anjouk-02-voc.json",
    "grammar/b1/b1-anjouk-02-gr.json",
    "exercises/b1/b1-anjouk-02-ex.json",
    [f"b1-anjouk-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: Nagy Lajos és az 1351-es törvények
# -----------------
write_json(STORIES_DIR / "b1-anjouk-03-nagylajos.json", make_story(
    "story.b1.anjouk.03",
    "Nagy Lajos király és az 1351-es törvények",
    "King Louis the Great (1342–1382): chivalric campaigns to Naples and the Balkans, personal union with Poland (1370), founding Pécs University (1367), and the 1351 laws: aviticitas (*ősiség*), ninth tax (*kilenced*), and 'one and the same liberty' for nobles.",
    "Buda, Visegrád és Pécs",
    ["jogi és öröklési kifejezések, jogegyenlőség"],
    ["Nagy Lajos", "1351-es törvények", "Ősiség törvénye", "Kilenced", "Lengyel-magyar unió"],
    [
        "Károly Róbert fia, I. (Nagy) Lajos király (1342–1382) alatt a középkori Magyar Királyság elérte hatalmának és nemzetközi tekintélyének egyik csúcspontját. A lovagi erényeket megtestesítő királyt a krónikák 'lovagkirályként' és 'a magyarok dicsőségeként' emlegették.",
        "Lajos hadjáratokat vezetett a Nápolyi Királyságba és a Balkánra, 1370-ben pedig nagybátyja halála után megörökölte a lengyel trónt is, létrehozva a Balti-tengertől az Adriáig terjedő magyar-lengyel perszonáluniót.",
        "1367-ben Pécsett megalapította Magyarország legelső egyetemét.",
        "1351-ben Lajos megújította az Aranybullát, és három sorsdöntő törvényt hozott: bevezette az ősiség törvényét (aviticitas), amely megtiltotta a nemesi birtokok eladását és a családon belüli öröklést írta elő; elrendelte a kilenced (a termés 9. tizedének) kötelező beszedését a jobbágyoktól; és kimondta az 'egy és ugyanazon szabadság' elvét, rögzítve minden nemes jogi egyenlőségét.",
        "Az 1351-es törvények egészen 1848-ig, a polgári forradalomig a magyar nemesi jogrendszer és társadalom legfőbb alapját képezték."
    ],
    [
        {"lemma": "ősiség", "pos": "noun", "cefr": "B1", "gloss": "aviticitas / inalienability of noble estates"},
        {"lemma": "kilenced", "pos": "noun", "cefr": "B1", "gloss": "ninth (feudal tax paid by serfs to landlords)"},
        {"lemma": "jogegyenlőség", "pos": "noun", "cefr": "B1", "gloss": "equality before the law"},
        {"lemma": "egyetem", "pos": "noun", "cefr": "B1", "gloss": "university (Pécs 1367)"}
    ],
    [
        {
            "question": "Melyik évben hozta Nagy Lajos király a híres törvényeket, amelyek az ősiséget és a kilencedet bevezették?",
            "options": ["1351-ben", "1222-ben", "1456-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "Nagy Lajos 1351-ben adta ki a híres törvényeket."
        },
        {
            "question": "Mit mondott ki az ősiség (aviticitas) törvénye?",
            "options": ["A nemesi birtok elidegeníthetetlen, a nemzetségen belül öröklődik, és csak a család kihalásakor száll a koronára", "Bárki szabadon eladhatta a nemesi földet külföldre", "Minden földet felosztottak a parasztok között", "A király bármikor elvehette a birtokot"],
            "correctIndex": 0,
            "explanation": "Az ősiség törvénye védte a nemesi birtokot az eladástól és a nemzetségben tartotta a vagyont."
        },
        {
            "question": "Melyik városban alapította meg Nagy Lajos az első magyar egyetemet 1367-ben?",
            "options": ["Pécsett", "Budán", "Esztergomban", "Debrecenben"],
            "correctIndex": 0,
            "explanation": "A pécsi egyetem volt Magyarország első egyeteme, amelyet 1367-ben alapítottak."
        }
    ]
))

write_json(VOCAB_DIR / "b1-anjouk-03-voc.json", {
    "title": "Nagy Lajos király és az 1351-es törvények",
    "words": [
        {"lemma": "ősiség", "pos": "noun", "cefr": "B1", "translation": "aviticitas / inalienability of estates", "examples": [{"hungarian": "Az ősiség törvénye 1848-ig érvényben maradt.", "english": "The law of aviticitas remained in force until 1848."}]},
        {"lemma": "kilenced", "pos": "noun", "cefr": "B1", "translation": "ninth (feudal landlord tax)", "examples": [{"hungarian": "A jobbágyok kilencedet fizettek a földesúrnak.", "english": "The serfs paid the ninth to the landlord."}]},
        {"lemma": "jogegyenlőség", "pos": "noun", "cefr": "B1", "translation": "legal equality", "examples": [{"hungarian": "Kimondták a nemesi jogegyenlőség elvét.", "english": "They declared the principle of noble legal equality."}]},
        {"lemma": "egyetem", "pos": "noun", "cefr": "B1", "translation": "university", "examples": [{"hungarian": "1367-ben megalapították a pécsi egyetemet.", "english": "In 1367 they founded the University of Pécs."}]},
        {"lemma": "tekintély", "pos": "noun", "cefr": "B1", "translation": "authority / prestige", "examples": [{"hungarian": "Nagy Lajos nemzetközi tekintélye kiemelkedő volt.", "english": "Louis the Great's international prestige was outstanding."}]},
        {"lemma": "lovagi erény", "pos": "noun", "cefr": "B1", "translation": "chivalric virtue", "examples": [{"hungarian": "A lovagi erények vezérelték az uralkodót.", "english": "Chivalric virtues guided the monarch."}]},
        {"lemma": "perszonálunió", "pos": "noun", "cefr": "B1", "translation": "personal union", "examples": [{"hungarian": "Létrejött a magyar-lengyel perszonálunió 1370-ben.", "english": "The Hungarian-Polish personal union was established in 1370."}]},
        {"lemma": "öröklés", "pos": "noun", "cefr": "B1", "translation": "inheritance / succession", "examples": [{"hungarian": "Az ősiség biztosította a családon belüli öröklést.", "english": "Aviticitas ensured inheritance within the family."}]},
        {"lemma": "elidegeníthetetlen", "pos": "adj", "cefr": "B1", "translation": "inalienable", "examples": [{"hungarian": "A nemesi földbirtok elidegeníthetetlen volt.", "english": "The noble land estate was inalienable."}]},
        {"lemma": "megújít", "pos": "verb", "cefr": "B1", "translation": "to renew / confirm", "examples": [{"hungarian": "Lajos megújította az Aranybulla rendelkezéseit.", "english": "Louis renewed the provisions of the Golden Bull."}]},
        {"lemma": "sorsdöntő", "pos": "adj", "cefr": "B1", "translation": "fateful / decisive", "examples": [{"hungarian": "Sorsdöntő törvényeket hoztak 1351-ben.", "english": "They made decisive laws in 1351."}]},
        {"lemma": "beszed", "pos": "verb", "cefr": "B1", "translation": "to collect (taxes)", "examples": [{"hungarian": "A földesurak beszedték a kilencedet.", "english": "The landlords collected the ninth."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-anjouk-03-gr.json", {
    "title": "Jogi kifejezések és határozói szerkezetek (egészen ... -ig)",
    "level": "B1",
    "rules": [
        {
            "id": "egeszen-ig-temporal",
            "title": "Temporal Span with 'egészen ... -ig' (All the way until)",
            "text": "*Az 1351-es törvények egészen 1848-ig érvényben maradtak.* (The 1351 laws remained in force all the way until 1848.)",
            "tip": "Combines *egészen* with the terminative suffix *-ig*."
        },
        {
            "id": "legal-principles-szabadsag",
            "title": "Noun Coordination with 'egy és ugyanazon'",
            "text": "Formal Hungarian legal phrases: *egy és ugyanazon szabadság* (one and the same liberty). Demonstrates invariable demonstrative *ugyanazon* modifying nouns.",
            "tip": "High-register phrase tested in constitutional history."
        }
    ],
    "examples": [
        {"spanish": "Az 1351-es törvények egészen 1848-ig meghatározták a társadalmat.", "english": "The 1351 laws determined society all the way until 1848."},
        {"spanish": "Minden nemest egy és ugyanazon szabadság illetett meg.", "english": "Every noble was entitled to one and the same liberty."},
        {"spanish": "Nagy Lajos 1367-ben Pécsett megalapította az első egyetemet.", "english": "Louis the Great founded the first university in Pécs in 1367."}
    ]
})

write_json(EXERCISES_DIR / "b1-anjouk-03-ex.json", {
    "exercises": [
        {"id": "b1-anjouk-03.ex01", "type": "multiple-choice", "title": "1351-es törvények", "instruction": "Melyik évben hozta Nagy Lajos a híres törvényeket?", "question": "Mikor vezették be az ősiség törvényét?", "options": ["1351-ben", "1222-ben", "1456-ban", "1526-ban"], "correctIndex": 0, "explanation": "Nagy Lajos 1351-ben hozta a törvényeket.", "teaches": ["osiseg", "kilenced"]},
        {"id": "b1-anjouk-03.ex02", "type": "fill-blank", "title": "Ősiség elve", "instruction": "Egészítsd ki a mondatot!", "sentence": "Az ___ törvénye (aviticitas) megtiltotta a nemesi birtokok eladását.", "correctAnswer": "ősiség", "options": ["ősiség", "adósság", "vásárlás", "szabadság"], "teaches": ["osiseg", "elidegenithetetlen"]},
        {"id": "b1-anjouk-03.ex03", "type": "sentence-builder", "title": "Pécsi egyetem alapítása", "instruction": "Állítsd össze a mondatot!", "words": ["Nagy", "Lajos", "1367-ben", "megalapította", "a", "pécsi", "egyetemet."], "correctSentence": "Nagy Lajos 1367-ben megalapította a pécsi egyetemet.", "english": "Louis the Great founded the University of Pécs in 1367.", "teaches": ["egyetem"]},
        {"id": "b1-anjouk-03.ex04", "type": "multiple-choice", "title": "A kilenced", "instruction": "Mi volt a kilenced?", "question": "Kinek fizették a jobbágyok a kilencedet?", "options": ["A földbirtokosnak (a termés 9. tizedét)", "A királynak közvetlenül", "A római pápának", "A külföldi kereskedőknek"], "correctIndex": 0, "explanation": "A kilenced a földesúrnak járó kötelező jobbágyadó volt.", "teaches": ["kilenced", "beszed"]},
        {"id": "b1-anjouk-03.ex05", "type": "fill-blank", "title": "Időbeli hatály (egészen ... -ig)", "instruction": "Válaszd ki a megfelelő toldalékos alakot!", "sentence": "Az 1351-es törvények egészen 1848-___ maradtak érvényben.", "correctAnswer": "ig", "options": ["ig", "ban", "kor", "val"], "teaches": ["osiseg"]},
        {"id": "b1-anjouk-03.ex06", "type": "sentence-builder", "title": "Nemesi jogegyenlőség", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["A", "törvény", "kimondta", "az", "egy", "és", "ugyanazon", "szabadság", "elvét."], "correctSentence": "A törvény kimondta az egy és ugyanazon szabadság elvét.", "english": "The law declared the principle of one and the same liberty.", "teaches": ["jogegyenloseg"]},
        {"id": "b1-anjouk-03.ex07", "type": "multiple-choice", "title": "Lengyel-magyar unió", "instruction": "Melyik ország királya lett Nagy Lajos 1370-ben?", "question": "Mely állammal jött létre perszonálunió 1370-ben?", "options": ["Lengyelországgal", "Franciaországgal", "Angliával", "Oroszországgal"], "correctIndex": 0, "explanation": "Nagy Lajos 1370-ben megörökölte a lengyel trónt.", "teaches": ["perszonalunio", "tekintely"]},
        {"id": "b1-anjouk-03.ex08", "type": "fill-blank", "title": "Lovagi eszmény", "instruction": "Egészítsd ki a mondatot!", "sentence": "Nagy Lajos a keresztény ___ mintaképe volt Európában.", "correctAnswer": "lovagkirályok", "options": ["lovagkirályok", "kalózok", "parasztok", "kereskedők"], "teaches": ["lovagi-ereny"]}
    ]
})

write_json(LESSONS_DIR / "b1-anjouk-03.json", make_lesson(
    "lesson.b1.anjouk-03",
    "Nagy Lajos és az 1351-es törvények (Louis the Great & 1351 Laws)",
    "Jogi kifejezések és határozói szerkezetek (egészen ... -ig)",
    [
        "In this third lesson, we explore King Louis the Great (*Nagy Lajos*, 1342–1382), the chivalric powerhouse of 14th-century Europe.",
        "You will learn about the Hungarian-Polish personal union (1370), the founding of Hungary's first university in Pécs (1367), and the foundational 1351 laws: the inalienability of noble land (*ősiség / aviticitas*), the landlord tax (*kilenced*), and 'one and the same liberty' (*egy és ugyanazon szabadság*).",
        "We also practice temporal limits with *egészen ... -ig* and legal register expressions."
    ],
    [
        "I can state the main provisions of the 1351 laws (ősiség / aviticitas, kilenced, noble equality).",
        "I can describe King Louis the Great's European prestige and the 1370 Polish union.",
        "I can identify Pécs as the location of Hungary's first university (1367).",
        "I can construct sentences expressing long historical spans (*egészen ... -ig*)."
    ],
    "stories/world/b1/b1-anjouk-03-nagylajos.json",
    "vocabulary/b1/b1-anjouk-03-voc.json",
    "grammar/b1/b1-anjouk-03-gr.json",
    "exercises/b1/b1-anjouk-03-ex.json",
    [f"b1-anjouk-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: Luxemburgi Zsigmond
# -----------------
write_json(STORIES_DIR / "b1-anjouk-04-zsigmond.json", make_story(
    "story.b1.anjouk.04",
    "Luxemburgi Zsigmond és az európai politika (1387–1437)",
    "King Sigismund of Luxemburg (1387–1437): Holy Roman Emperor, convening the Council of Constance (1414–1418) to heal the Western Schism, expanding Buda Castle, and building the southern border fortress system (*végvárrendszer*) against the Ottoman threat.",
    "Buda, Visegrád és Konstanz",
    ["nemzetközi politikai kifejezések és időviszonyok"],
    ["Luxemburgi Zsigmond", "Konstanzi zsinat", "Végvári vonal", "Oszmán fenyegetés"],
    [
        "Nagy Lajos lányának, Mária királynőnek férjeként Luxemburgi Zsigmond (1387–1437) ült fél évszázadon át a magyar trónon. Zsigmond kivételes diplomáciai tehetségével nemcsak magyar király, hanem cseh király és német-római császár is lett.",
        "Európai uralkodóként Zsigmond hívta össze az 1414 és 1418 közötti konstanzi zsinatot, amely sikeresen felszámolta a nyugati egyházszakadást és helyreállította a katolikus egyház egységét.",
        "Buda Zsigmond alatt igazi európai császári székhellyé vált: hatalmas gótikus palotaszárnnyal (Friss-palota) bővíttette a királyi várat.",
        "Uralkodása idején jelent meg a határokon a növekvő Oszmán (Török) Birodalom veszélye. Az 1396-os nikápolyi csata után Zsigmond felismerte a védelem szükségességét, és kiépítette a déli végvárrendszer első vonalát Szörénytől Galambócig.",
        "Zsigmond ötvenéves országlása szilárd alapot teremtett a magyarországi gótikus művészetnek és a déli határok évszázados védelmének."
    ],
    [
        {"lemma": "zsinat", "pos": "noun", "cefr": "B1", "gloss": "church council / synod (Constance)"},
        {"lemma": "egyházszakadás", "pos": "noun", "cefr": "B1", "gloss": "schism"},
        {"lemma": "végvárrendszer", "pos": "noun", "cefr": "B1", "gloss": "border fortress system"},
        {"lemma": "császári székhely", "pos": "noun", "cefr": "B1", "gloss": "imperial capital / seat"}
    ],
    [
        {
            "question": "Melyik híres nemzetközi egyházi zsinatot hívta össze Luxemburgi Zsigmond 1414-ben?",
            "options": ["A konstanzi zsinatot", "A trienti zsinatot", "A vatikáni zsinatot", "A nizzai zsinatot"],
            "correctIndex": 0,
            "explanation": "Zsigmond hívta össze a konstanzi zsinatot az egyházszakadás felszámolására."
        },
        {
            "question": "Milyen uralkodói címeket viselt Luxemburgi Zsigmond?",
            "options": ["Magyar király, cseh király és német-római császár volt", "Csak budai polgármester", "Angol király és francia herceg", "Oszmán szultán"],
            "correctIndex": 0,
            "explanation": "Zsigmond magyar és cseh királyként a Német-Római Birodalom császára is volt."
        },
        {
            "question": "Mit épített ki Zsigmond a déli határokon a török veszély ellen?",
            "options": ["A déli végvárrendszer védelmi vonalát", "Egy mély tengeri árkot", "Vasútvonalat", "Nem épített semmilyen védelmet"],
            "correctIndex": 0,
            "explanation": "Zsigmond hozta létre a déli végvárrendszert az Oszmán Birodalom feltartóztatására."
        }
    ]
))

write_json(VOCAB_DIR / "b1-anjouk-04-voc.json", {
    "title": "Luxemburgi Zsigmond és az európai politika",
    "words": [
        {"lemma": "zsinat", "pos": "noun", "cefr": "B1", "translation": "ecclesiastical council / synod", "examples": [{"hungarian": "A konstanzi zsinat helyreállította az egyház egységét.", "english": "The Council of Constance restored the unity of the church."}]},
        {"lemma": "egyházszakadás", "pos": "noun", "cefr": "B1", "translation": "schism", "examples": [{"hungarian": "Felszámolták a nyugati egyházszakadást.", "english": "They eliminated the Western Schism."}]},
        {"lemma": "végvárrendszer", "pos": "noun", "cefr": "B1", "translation": "border fortress system", "examples": [{"hungarian": "A végvárrendszer védte az ország déli határait.", "english": "The border fortress system defended the country's southern borders."}]},
        {"lemma": "császári székhely", "pos": "noun", "cefr": "B1", "translation": "imperial seat", "examples": [{"hungarian": "Buda császári székhellyé fejlődött.", "english": "Buda developed into an imperial seat."}]},
        {"lemma": "diplomáciai", "pos": "adj", "cefr": "B1", "translation": "diplomatic", "examples": [{"hungarian": "Zsigmond nagy diplomáciai tehetség volt.", "english": "Sigismund was a great diplomatic talent."}]},
        {"lemma": "országlás", "pos": "noun", "cefr": "B1", "translation": "reign", "examples": [{"hungarian": "Ötvenéves országlása hosszú békét hozott.", "english": "His fifty-year reign brought long peace."}]},
        {"lemma": "gótikus", "pos": "adj", "cefr": "B1", "translation": "Gothic", "examples": [{"hungarian": "Gótikus palotát épített a Budai Várban.", "english": "He built a Gothic palace in Buda Castle."}]},
        {"lemma": "fenyegetés", "pos": "noun", "cefr": "B1", "translation": "threat", "examples": [{"hungarian": "Az oszmán fenyegetés egyre nőtt délen.", "english": "The Ottoman threat grew continuously in the south."}]},
        {"lemma": "összehív", "pos": "verb", "cefr": "B1", "translation": "to convene / call together", "examples": [{"hungarian": "A császár zsinatot hívott össze Konstanzban.", "english": "The emperor convened a synod in Constance."}]},
        {"lemma": "felismer", "pos": "verb", "cefr": "B1", "translation": "to realize / recognize", "examples": [{"hungarian": "Felismerte a végvárak fontosságát.", "english": "He recognized the importance of border forts."}]},
        {"lemma": "bővít", "pos": "verb", "cefr": "B1", "translation": "to expand / enlarge", "examples": [{"hungarian": "Új szárnyakkal bővítette a királyi várat.", "english": "He expanded the royal castle with new wings."}]},
        {"lemma": "határvonal", "pos": "noun", "cefr": "B1", "translation": "frontier / borderline", "examples": [{"hungarian": "A déli határvonalat várakkal erősítették meg.", "english": "The southern frontier was reinforced with castles."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-anjouk-04-gr.json", {
    "title": "Nemzetközi politikai szintaxis és összetett alanyok (nemcsak ... hanem ... is)",
    "level": "B1",
    "rules": [
        {
            "id": "correlative-nemcsak-hanem",
            "title": "Correlative Conjunctions: 'nemcsak ..., hanem ... is' (not only ... but also)",
            "text": "*Zsigmond nemcsak magyar király, hanem német-római császár is volt.* (Sigismund was not only king of Hungary, but also Holy Roman Emperor.)",
            "tip": "Always place a comma before *hanem*."
        },
        {
            "id": "temporal-kozotti",
            "title": "Adjectival Range Expressions with 'közötti'",
            "text": "*Az 1414 és 1418 közötti zsinat* (the synod between 1414 and 1418).",
            "tip": "*Közötti* turns a prepositional time range into an adjective."
        }
    ],
    "examples": [
        {"spanish": "Zsigmond nemcsak Magyarországot, hanem a császárságot is irányította.", "english": "Sigismund ruled not only Hungary, but also the Empire."},
        {"spanish": "Az 1414 és 1418 közötti konstanzi zsinat sikeres volt.", "english": "The Council of Constance between 1414 and 1418 was successful."},
        {"spanish": "Kiépítette a déli végvárak védelmi vonalát.", "english": "He built up the defensive line of the southern border forts."}
    ]
})

write_json(EXERCISES_DIR / "b1-anjouk-04-ex.json", {
    "exercises": [
        {"id": "b1-anjouk-04.ex01", "type": "multiple-choice", "title": "A konstanzi zsinat", "instruction": "Melyik európai esemény fűződik Luxemburgi Zsigmond nevéhez?", "question": "Mit hívott össze Zsigmond 1414-ben Konstanzban?", "options": ["A konstanzi egyházi zsinatot", "A párizsi békekonferenciát", "A bécsi kongresszust", "A római olimpiát"], "correctIndex": 0, "explanation": "Zsigmond hívta össze a konstanzi zsinatot (1414–1418).", "teaches": ["zsinat", "egyhazszakadas"]},
        {"id": "b1-anjouk-04.ex02", "type": "fill-blank", "title": "Déli védelem", "instruction": "Egészítsd ki a mondatot!", "sentence": "Zsigmond kiépítette a déli ___ első vonalát az oszmánok ellen.", "correctAnswer": "végvárrendszer", "options": ["végvárrendszer", "vasúthálózat", "tengerpart", "autópálya"], "teaches": ["vegvarrendszer", "hatarvonal"]},
        {"id": "b1-anjouk-04.ex03", "type": "sentence-builder", "title": "Nemcsak ... hanem ... is", "instruction": "Állítsd össze a mondatot!", "words": ["Zsigmond", "nemcsak", "magyar", "király,", "hanem", "német-római", "császár", "is", "volt."], "correctSentence": "Zsigmond nemcsak magyar király, hanem német-római császár is volt.", "english": "Sigismund was not only king of Hungary, but also Holy Roman Emperor.", "teaches": ["csaszari-szekhely", "diplomaciai"]},
        {"id": "b1-anjouk-04.ex04", "type": "multiple-choice", "title": "Buda vára Zsigmond alatt", "instruction": "Hogyan fejlesztette Zsigmond a budai királyi székhelyet?", "question": "Milyen palotát épített Zsigmond Budán?", "options": ["Gótikus császári palotaszárnyat (Friss-palota)", "Barokk felhőkarcolót", "Egy fából készült sátrat", "Nem épített semmit"], "correctIndex": 0, "explanation": "Zsigmond hatalmas gótikus Friss-palotát épített a Budai Várban.", "teaches": ["gotikus", "csaszari-szekhely", "bovit"]},
        {"id": "b1-anjouk-04.ex05", "type": "fill-blank", "title": "Időtartam (közötti)", "instruction": "Válaszd ki a megfelelő szót!", "sentence": "Az 1414 és 1418 ___ konstanzi zsinat megszüntette az egyházszakadást.", "correctAnswer": "közötti", "options": ["közötti", "utáni", "előtti", "alatti"], "teaches": ["zsinat"]},
        {"id": "b1-anjouk-04.ex06", "type": "sentence-builder", "title": "Török fenyegetés", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["A", "déli", "határokon", "megjelent", "az", "Oszmán", "Birodalom", "fenyegetése."], "correctSentence": "A déli határokon megjelent az Oszmán Birodalom fenyegetése.", "english": "The threat of the Ottoman Empire appeared on the southern borders.", "teaches": ["fenyegetes", "hatarvonal"]},
        {"id": "b1-anjouk-04.ex07", "type": "multiple-choice", "title": "Országlás hossza", "instruction": "Meddig uralkodott Zsigmond Magyarországon?", "question": "Hány évig volt magyar király Luxemburgi Zsigmond?",
        "options": ["50 évig (1387–1437)", "Csak 2 évig", "100 évig", "5 hónapig"], "correctIndex": 0, "explanation": "Zsigmond fél évszázadon át (1387–1437) uralkodott.", "teaches": ["orszoglas"]},
        {"id": "b1-anjouk-04.ex08", "type": "fill-blank", "title": "Egyház egysége", "instruction": "Egészítsd ki a mondatot!", "sentence": "A császár sikeresen helyreállította az egyház ___ Konstanzban.", "correctAnswer": "egységét", "options": ["egységét", "pénzét", "falait", "könyvtárát"], "teaches": ["egyhazszakadas", "zsinat"]}
    ]
})

write_json(LESSONS_DIR / "b1-anjouk-04.json", make_lesson(
    "lesson.b1.anjouk-04",
    "Luxemburgi Zsigmond és az európai politika (Sigismund of Luxemburg)",
    "Nemzetközi politikai szintaxis és összetett alanyok (nemcsak ... hanem ... is)",
    [
        "In this fourth lesson, we study King Sigismund of Luxemburg (1387–1437), King of Hungary, King of Bohemia, and Holy Roman Emperor.",
        "You will learn about his convening of the Council of Constance (1414–1418) to heal the Western Schism, the Gothic expansion of Buda Castle, and the construction of the southern border fortress line (*végvárrendszer*) against the expanding Ottoman Empire.",
        "We also practice correlative conjunctions (*nemcsak ..., hanem ... is*) and adjectival range structures (*közötti*)."
    ],
    [
        "I can describe Sigismund's roles as King of Hungary and Holy Roman Emperor.",
        "I can explain the significance of the Council of Constance (1414–1418).",
        "I can summarize the creation of the southern border fortress system (*végvárrendszer*).",
        "I can use correlative structures (*nemcsak ..., hanem ... is*) in formal Hungarian."
    ],
    "stories/world/b1/b1-anjouk-04-zsigmond.json",
    "vocabulary/b1/b1-anjouk-04-voc.json",
    "grammar/b1/b1-anjouk-04-gr.json",
    "exercises/b1/b1-anjouk-04-ex.json",
    [f"b1-anjouk-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: Hunyadi János és Nándorfehérvár (1456)
# -----------------
write_json(STORIES_DIR / "b1-anjouk-05-nandorfehervar.json", make_story(
    "story.b1.anjouk.05",
    "Hunyadi János és a nándorfehérvári diadal (1456)",
    "John Hunyadi ('the Turk-beater'): his military genius, the legendary Siege of Nándorfehérvár (Belgrade, July 1456), Capistrano's crusader army, Dugovics Titusz's heroism, the noon bell decree by Pope Callixtus III, and halting the Ottoman advance for 70 years.",
    "Nándorfehérvár (Belgrád)",
    ["hősies narratíva és a déli harangszó története"],
    ["Hunyadi János", "Nándorfehérvári diadal 1456", "Déli harangszó", "Kapisztrán János"],
    [
        "A 15. század közepén az Oszmán Birodalom elfoglalta Bizáncot (1453), és II. Mehmed szultán Magyarország kapuja, Nándorfehérvár (a mai Belgrád) ellen indult hatalmas hadsereggel.",
        "Az ország védelmét Magyarország kormányzója és hadvezére, a 'törökverő' Hunyadi János vette kezébe. Hunyadi saját seregével és Kapisztrán János ferences szerzetes lelkes keresztes népfelkelőivel sietett a vár felmentésére.",
        "1456. július 14-én Hunyadi flottája a Dunán áttörte a török hajózárat, bejutva a szorongatott várba. Július 21-én a törökök mindent eldöntő rohamot indítottak, de a védők – köztük a mélybe ugró Dugovics Titusz legendás önfeláldozásával – visszaverték a janicsárokat.",
        "Másnap, július 22-én Hunyadi és Kapisztrán ellentámadásba lendült, elfoglalta a szultán ágyúit, és megsemmisítő vereséget mért a török főseregre.",
        "A nándorfehérvári diadal tiszteletére rendelte el III. Kallixtusz pápa a déli harangszót, amely mindmáig a keresztény világban minden délben a magyar győzelemre és hősiességre emlékeztet. A diadal hét évtizedre megállította a török hódítást."
    ],
    [
        {"lemma": "törökverő", "pos": "adj", "cefr": "B1", "gloss": "Turk-beater (Hunyadi's epithet)"},
        {"lemma": "déli harangszó", "pos": "noun", "cefr": "B1", "gloss": "noon bell (papal decree after 1456)"},
        {"lemma": "keresztes", "pos": "noun", "cefr": "B1", "gloss": "crusader"},
        {"lemma": "várkapu", "pos": "noun", "cefr": "B1", "gloss": "gate of the realm / stronghold"}
    ],
    [
        {
            "question": "Melyik évben aratott világraszóló diadalt Hunyadi János Nándorfehérvárnál?",
            "options": ["1456-ban", "1241-ben", "1526-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "A nándorfehérvári diadal 1456 júliusában zajlott le."
        },
        {
            "question": "Mire emlékeztet a katolikus templomokban mindmáig megszólaló déli harangszó?",
            "options": ["A nándorfehérvári győzelemre (1456) és a kereszténység megvédésére", "A király születésnapjára", "Az aratás kezdetére", "A déli ebédidőre kizárólag"],
            "correctIndex": 0,
            "explanation": "A pápa által elrendelt déli harangszó az 1456-os nándorfehérvári győzelem emlékét őrzi."
        },
        {
            "question": "Ki volt Hunyadi János fontos lelki és katonai szövetségese Nándorfehérvárnál?",
            "options": ["Kapisztrán János ferences szerzetes", "Julianus barát", "Gellért püspök", "Anonymus"],
            "correctIndex": 0,
            "explanation": "Kapisztrán János vezette a keresztes népfelkelőket Nándorfehérvár felmentésére."
        }
    ]
))

write_json(VOCAB_DIR / "b1-anjouk-05-voc.json", {
    "title": "Hunyadi János és a nándorfehérvári diadal (1456)",
    "words": [
        {"lemma": "törökverő", "pos": "adj", "cefr": "B1", "translation": "Turk-beater", "examples": [{"hungarian": "Hunyadi Jánost törökverő hősként tisztelték.", "english": "John Hunyadi was revered as a Turk-beater hero."}]},
        {"lemma": "déli harangszó", "pos": "noun", "cefr": "B1", "translation": "noon bell", "examples": [{"hungarian": "A déli harangszó a nándorfehérvári győzelemre emlékeztet.", "english": "The noon bell commemorates the victory of Nándorfehérvár."}]},
        {"lemma": "keresztes", "pos": "noun", "cefr": "B1", "translation": "crusader", "examples": [{"hungarian": "Kapisztrán keresztes serege hősiesen küzdött.", "english": "Capistrano's crusader army fought heroically."}]},
        {"lemma": "felmentés", "pos": "noun", "cefr": "B1", "translation": "relief (of a siege)", "examples": [{"hungarian": "Hunyadi a vár felmentésére sietett.", "english": "Hunyadi hurried to the relief of the fortress."}]},
        {"lemma": "áttör", "pos": "verb", "cefr": "B1", "translation": "to break through", "examples": [{"hungarian": "A hajóhad áttörte a dunai hajózárat.", "english": "The fleet broke through the Danube river blockade."}]},
        {"lemma": "önfeláldozás", "pos": "noun", "cefr": "B1", "translation": "self-sacrifice", "examples": [{"hungarian": "Dugovics Titusz önfeláldozása legendává vált.", "english": "Titusz Dugovics's self-sacrifice became a legend."}]},
        {"lemma": "ellentámadás", "pos": "noun", "cefr": "B1", "translation": "counter-attack", "examples": [{"hungarian": "A magyar ellentámadás megfutamította a szultánt.", "english": "The Hungarian counter-attack routed the sultan."}]},
        {"lemma": "diadal", "pos": "noun", "cefr": "B1", "translation": "glorious victory / triumph", "examples": [{"hungarian": "Világraszóló diadalt arattak 1456-ban.", "english": "They won a world-renowned triumph in 1456."}]},
        {"lemma": "megállít", "pos": "verb", "cefr": "B1", "translation": "to halt / stop", "examples": [{"hungarian": "Hetven évre megállították a török terjeszkedést.", "english": "They stopped Ottoman expansion for seventy years."}]},
        {"lemma": "hadvezér", "pos": "noun", "cefr": "B1", "translation": "commander / general", "examples": [{"hungarian": "Hunyadi zseniális hadvezér volt.", "english": "Hunyadi was a genius military commander."}]},
        {"lemma": "hősiesség", "pos": "noun", "cefr": "B1", "translation": "heroism", "examples": [{"hungarian": "A védők hősiessége megmentette Európát.", "english": "The heroism of the defenders saved Europe."}]},
        {"lemma": "szorongatott", "pos": "adj", "cefr": "B1", "translation": "hard-pressed / beleaguered", "examples": [{"hungarian": "A szorongatott vár kitartott az utolsó pillanatig.", "english": "The beleaguered castle held out until the last moment."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-anjouk-05-gr.json", {
    "title": "Hősi elbeszélés és emlékezetkifejezések (emlékeztet valamire)",
    "level": "B1",
    "rules": [
        {
            "id": "verb-emlekeztet-re",
            "title": "Verbs of Remembrance (emlékeztet vmire, tiszteletére)",
            "text": "*A harangszó a győzelemre emlékeztet.* (The bell reminds of / commemorates the victory.) *A győzelem tiszteletére rendelték el.* (Ordered in honor of the victory.)",
            "tip": "*Emlékeztet* takes the sublative case *-ra / -re*."
        },
        {
            "id": "heroic-clauses",
            "title": "Participial Phrases in Dramatic Battle Descriptions",
            "text": "*Áttörve a hajózárat, bejutottak a várba.* (Breaking through the blockade, they entered the fort.)",
            "tip": "Adverbial participle *-va / -ve* provides compact narrative drive."
        }
    ],
    "examples": [
        {"spanish": "A déli harangszó a nándorfehérvári diadalra emlékeztet.", "english": "The noon bell commemorates the triumph of Nándorfehérvár."},
        {"spanish": "Hunyadi János serege megállította a török terjeszkedést.", "english": "John Hunyadi's army halted Ottoman expansion."},
        {"spanish": "A vár védői visszaverték a janicsárok rohamát.", "english": "The defenders of the castle repelled the charge of the Janissaries."}
    ]
})

write_json(EXERCISES_DIR / "b1-anjouk-05-ex.json", {
    "exercises": [
        {"id": "b1-anjouk-05.ex01", "type": "multiple-choice", "title": "A nándorfehérvári diadal éve", "instruction": "Melyik évben győzte le Hunyadi a szultánt Nándorfehérvárnál?", "question": "Mikor zajlott a nándorfehérvári diadal?", "options": ["1456-ban", "1241-ben", "1526-ban", "1848-ban"], "correctIndex": 0, "explanation": "A nándorfehérvári diadal 1456 júliusában történt.", "teaches": ["nandorfehervari-diadal", "diadal"]},
        {"id": "b1-anjouk-05.ex02", "type": "fill-blank", "title": "Déli harangszó", "instruction": "Egészítsd ki a mondatot!", "sentence": "A pápa rendeletére a ___ harangszó mindmáig az 1456-os győzelemre emlékeztet.", "correctAnswer": "déli", "options": ["déli", "reggeli", "esti", "éjféli"], "teaches": ["deli-harangszo", "emlekeztet"]},
        {"id": "b1-anjouk-05.ex03", "type": "sentence-builder", "title": "A törökverő hadvezér", "instruction": "Állítsd össze a mondatot!", "words": ["Hunyadi", "János", "megállította", "az", "oszmán", "hadsereget", "Nándorfehérvárnál."], "correctSentence": "Hunyadi János megállította az oszmán hadsereget Nándorfehérvárnál.", "english": "John Hunyadi halted the Ottoman army at Nándorfehérvár.", "teaches": ["torokvero", "megallit"]},
        {"id": "b1-anjouk-05.ex04", "type": "multiple-choice", "title": "Kapisztrán János szerepe", "instruction": "Ki vezette a keresztes népfelkelőket?", "question": "Melyik ferences hitszónok segítette Hunyadit?", "options": ["Kapisztrán János", "Julianus barát", "Gellért püspök", "Pázmány Péter"], "correctIndex": 0, "explanation": "Kapisztrán János ferences szerzetes buzdította a keresztes sereget.", "teaches": ["keresztes"]},
        {"id": "b1-anjouk-05.ex05", "type": "fill-blank", "title": "Emlékeztet (valamire)", "instruction": "Válaszd ki a helyes toldalékot!", "sentence": "A harangszó a magyar katonák hősiességé___ emlékeztet.", "correctAnswer": "re", "options": ["re", "ben", "vel", "től"], "teaches": ["hosiesseg"]},
        {"id": "b1-anjouk-05.ex06", "type": "sentence-builder", "title": "Dunai hajózár áttörése", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Hunyadi", "hajóhada", "áttörte", "a", "török", "dunai", "zárat."], "correctSentence": "Hunyadi hajóhada áttörte a török dunai zárat.", "english": "Hunyadi's fleet broke through the Turkish Danube blockade.", "teaches": ["attor", "felmentes"]},
        {"id": "b1-anjouk-05.ex07", "type": "multiple-choice", "title": "A győzelem hatása", "instruction": "Mennyi időre állította meg a diadal a török terjeszkedést?", "question": "Hány évre biztosította Nándorfehérvár az ország békéjét?", "options": ["Mintegy 70 évre (1521-ig / 1526-ig)", "Csak 2 napra", "Örök időkre", "1000 évre"], "correctIndex": 0, "explanation": "A nándorfehérvári diadal hét évtizedre megállította az oszmán előrenyomulást.", "teaches": ["megallit", "diadal"]},
        {"id": "b1-anjouk-05.ex08", "type": "fill-blank", "title": "Hősi önfeláldozás", "instruction": "Egészítsd ki a mondatot!", "sentence": "Dugovics Titusz legendás ___ a vár bástyáján mentette meg a zászlót.", "correctAnswer": "önfeláldozása", "options": ["önfeláldozása", "futása", "álma", "zenéje"], "teaches": ["onfelaldozas"]}
    ]
})

write_json(LESSONS_DIR / "b1-anjouk-05.json", make_lesson(
    "lesson.b1.anjouk-05",
    "Hunyadi János és a nándorfehérvári diadal (Hunyadi & Nándorfehérvár - 1456)",
    "Hősi elbeszélés és emlékezetkifejezések (emlékeztet valamire)",
    [
        "In this fifth lesson, we examine one of the greatest military triumphs of European and Hungarian history: the 1456 Siege of Nándorfehérvár (Belgrade).",
        "You will learn about John Hunyadi ('the Turk-beater'), Friar John of Capistrano, the naval breakthrough on the Danube, the sacrifice of Titusz Dugovics, and the papal decree establishing the worldwide noon bell (*déli harangszó*).",
        "We also practice verbs of commemoration (*emlékeztet vmire*) and dramatic battle syntax."
    ],
    [
        "I can state the year (1456) and significance of the Siege of Nándorfehérvár (Belgrade).",
        "I can explain the historical origin of the worldwide noon bell (*déli harangszó*).",
        "I can describe the leadership of John Hunyadi and John of Capistrano.",
        "I can use verbs of remembrance (*emlékeztet vmire*) accurately in B1 Hungarian."
    ],
    "stories/world/b1/b1-anjouk-05-nandorfehervar.json",
    "vocabulary/b1/b1-anjouk-05-voc.json",
    "grammar/b1/b1-anjouk-05-gr.json",
    "exercises/b1/b1-anjouk-05-ex.json",
    [f"b1-anjouk-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 7 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-anjouk.json", make_story(
    "story.b1.anjouk",
    "Az Anjou-kor és a késő középkor dicsősége (1308–1456)",
    "A synthesis of the late medieval golden era: Charles Robert's economic renewal, the 1335 Visegrád summit, Louis the Great's 1351 laws and Pécs university, Sigismund of Luxemburg's European diplomacy, and John Hunyadi's triumph at Nándorfehérvár (1456).",
    "Kárpát-medence",
    ["összetett mondatok", "történeti szintézis"],
    ["Anjou-kor", "Károly Róbert", "Nagy Lajos", "Hunyadi János", "Nándorfehérvár 1456"],
    [
        "A 14. és 15. század a középkori Magyar Királyság nemzetközi nagyhatalmi virágkora volt. Károly Róbert legyőzte a kiskirályokat, megteremtette az értékálló aranyforintot, és 1335-ben Visegrádon cseh és lengyel szövetségeseivel új kereskedelmi utakat nyitott.",
        "Fia, Nagy Lajos lovagkirály uralkodása alatt a Balti-tengerig terjedt a birodalom tekintélye. 1351-es törvényei (az ősiség és a kilenced) évszázadokra meghatározták a magyar jogrendszert, miközben 1367-ben Pécsett megalapította az első egyetemet.",
        "Luxemburgi Zsigmond német-római császárként a konstanzi zsinaton (1414–1418) felszámolta az egyházszakadást, Budát császári székhellyé emelte, és kiépítette a déli végvárrendszert.",
        "A korszak legdicsőbb pillanata az 1456-os nándorfehérvári diadal volt: Hunyadi János megállította az Oszmán Birodalom hódítását, amelynek emlékét a mai napig minden délben megkonduló harangszó hirdeti a világban.",
        "Ez a másfél évszázad tette Magyarországot a keresztény Európa megkerülhetetlen védőbástyájává és gazdasági motorjává."
    ],
    [
        {"lemma": "aranyforint", "pos": "noun", "cefr": "B1", "gloss": "golden florin"},
        {"lemma": "ősiség", "pos": "noun", "cefr": "B1", "gloss": "aviticitas (1351)"},
        {"lemma": "végvárrendszer", "pos": "noun", "cefr": "B1", "gloss": "border fortress system"},
        {"lemma": "déli harangszó", "pos": "noun", "cefr": "B1", "gloss": "noon bell (1456)"}
    ],
    [
        {"question": "Melyik évben zajlott a visegrádi királytalálkozó?", "options": ["1335-ben", "1222-ben", "1456-ban", "1526-ban"], "correctIndex": 0, "explanation": "A visegrádi királytalálkozót 1335-ben tartották."},
        {"question": "Mely törvények származnak Nagy Lajos 1351-es rendelkezéseiből?", "options": ["Az ősiség (aviticitas) és a kilenced törvénye", "A jobbágyfelszabadítás", "A tized törvénye", "A vérszerződés"], "correctIndex": 0, "explanation": "Nagy Lajos 1351-ben vezette be az ősiséget és a kötelező kilencedet."},
        {"question": "Melyik győzelem tiszteletére szól mindmáig a déli harangszó?", "options": ["Hunyadi János 1456-os nándorfehérvári diadala tiszteletére", "A mohácsi csata emlékére", "A honfoglalás tiszteletére", "Az Aranybulla kiadására"], "correctIndex": 0, "explanation": "A déli harangszó az 1456-os nándorfehérvári diadalra emlékeztet."}
    ]
))

u7_cons_ex = []
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex01", "type": "multiple-choice", "title": "Aranyforint", "instruction": "Ki vezette be a magyar aranyforintot?", "question": "Melyik Anjou király vezette be az értékálló aranyforintot?", "options": ["Károly Róbert", "Nagy Lajos", "Szent István", "IV. Béla"], "correctIndex": 0, "explanation": "Károly Róbert vezette be az aranyforintot és a kapuadót.", "teaches": ["aranyforint"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex02", "type": "fill-blank", "title": "Visegrádi csúcs éve", "instruction": "Egészítsd ki a mondatot!", "sentence": "A híres visegrádi királytalálkozót ___ őszén rendezték meg.", "correctAnswer": "1335", "options": ["1335", "1222", "1456", "1848"], "teaches": ["csucstalalkozo"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex03", "type": "sentence-builder", "title": "Ősiség törvénye", "instruction": "Állítsd össze a mondatot!", "words": ["Az", "ősiség", "törvénye", "megtiltotta", "a", "nemesi", "birtokok", "eladását."], "correctSentence": "Az ősiség törvénye megtiltotta a nemesi birtokok eladását.", "english": "The law of aviticitas prohibited the sale of noble estates.", "teaches": ["osiseg"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex04", "type": "multiple-choice", "title": "Pécsi egyetem", "instruction": "Melyik évben alapították Magyarország első egyetemét?", "question": "Mikor alapította Nagy Lajos a pécsi egyetemet?", "options": ["1367-ben", "1000-ben", "1456-ban", "1900-ban"], "correctIndex": 0, "explanation": "1367-ben jött létre a pécsi egyetem.", "teaches": ["egyetem"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex05", "type": "fill-blank", "title": "Nándorfehérvári győzelem", "instruction": "Egészítsd ki a mondatot!", "sentence": "Hunyadi János ___ aratott történelmi győzelmet Nándorfehérvárnál.", "correctAnswer": "1456-ban", "options": ["1456-ban", "1241-ben", "1526-ban", "1848-ban"], "teaches": ["nandorfehervari-diadal"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex06", "type": "sentence-builder", "title": "Déli harangszó", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["A", "déli", "harangszó", "minden", "nap", "a", "hősökre", "emlékeztet."], "correctSentence": "A déli harangszó minden nap a hősökre emlékeztet.", "english": "The noon bell commemorates the heroes every day.", "teaches": ["deli-harangszo", "emlekeztet"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex07", "type": "multiple-choice", "title": "Konstanzi zsinat", "instruction": "Ki hívta össze a konstanzi zsinatot?", "question": "Melyik magyar uralkodó volt egyben német-római császár?", "options": ["Luxemburgi Zsigmond", "Károly Róbert", "Nagy Lajos", "Hunyadi János"], "correctIndex": 0, "explanation": "Luxemburgi Zsigmond hívta össze a zsinatot.", "teaches": ["zsinat", "egyhazszakadas"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex08", "type": "fill-blank", "title": "Bécsi árumegállító jog", "instruction": "Válaszd ki a megfelelő kifejezést!", "sentence": "Az 1335-ös megállapodás kikerülte Bécs ___ jogát.", "correctAnswer": "árumegállító", "options": ["árumegállító", "repülési", "vásárlási", "építési"], "teaches": ["arumegallito-jog"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex09", "type": "sentence-builder", "title": "Végvárrendszer", "instruction": "Állítsd össze a mondatot!", "words": ["Zsigmond", "kiépítette", "a", "déli", "határok", "végvárrendszerét."], "correctSentence": "Zsigmond kiépítette a déli határok végvárrendszerét.", "english": "Sigismund built up the border fortress system of the southern borders.", "teaches": ["vegvarrendszer"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex10", "type": "multiple-choice", "title": "Kilenced adó", "instruction": "Mi volt a kilenced 1351-től?", "question": "Kinek járt a kilenced?", "options": ["A földbirtokosnak járó kötelező jobbágyadó", "A pápának küldött adomány", "A királyi udvar konyhapénze", "A külföldi utazási díj"], "correctIndex": 0, "explanation": "A kilenced a jobbágyok által a földesúrnak fizetett terményadó volt.", "teaches": ["kilenced"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex11", "type": "fill-blank", "title": "Bányabér (urbura)", "instruction": "Egészítsd ki a mondatot!", "sentence": "A bányabér egyharmadát a király átengedte a ___.", "correctAnswer": "földbirtokosoknak", "options": ["földbirtokosoknak", "katonáknak", "törököknek", "pápának"], "teaches": ["urbura"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex12", "type": "sentence-builder", "title": "Lengyel-magyar unió", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Nagy", "Lajos", "1370-ben", "megörökölte", "a", "lengyel", "trónt."], "correctSentence": "Nagy Lajos 1370-ben megörökölte a lengyel trónt.", "english": "Louis the Great inherited the Polish throne in 1370.", "teaches": ["perszonalunio"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex13", "type": "multiple-choice", "title": "Kapuadó lényege", "instruction": "Mikor kellett kapuadót fizetni?", "question": "Milyen jobbágytelek után fizettek kapuadót?", "options": ["Amelynek a kapuján átfért egy szénásszekér", "Amelynek tíz ablaka volt", "Amelynek volt saját kútja", "Csak a hegyekben fekvő telkek után"], "correctIndex": 0, "explanation": "A kapuadót minden olyan kapu után fizették, amin átfért egy megrakott szénásszekér.", "teaches": ["kapuado"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex14", "type": "fill-blank", "title": "Törökverő hadvezér", "instruction": "Egészítsd ki a mondatot!", "sentence": "Hunyadi Jánost a nép '___' hősként dicsőítette.", "correctAnswer": "törökverő", "options": ["törökverő", "tengeri", "békés", "gyáva"], "teaches": ["torokvero"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex15", "type": "sentence-builder", "title": "Gótikus palota Budán", "instruction": "Állítsd össze a mondatot!", "words": ["Zsigmond", "hatalmas", "gótikus", "palotával", "bővítette", "Buda", "várát."], "correctSentence": "Zsigmond hatalmas gótikus palotával bővítette Buda várát.", "english": "Sigismund expanded Buda Castle with a huge Gothic palace.", "teaches": ["gotikus", "bovit"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex16", "type": "multiple-choice", "title": "Rozgonyi diadal", "instruction": "Melyik évben győzte le Károly Róbert az Abákat Rozgonynál?", "question": "Mikor volt a rozgonyi csata?", "options": ["1312", "1222", "1335", "1456"], "correctIndex": 0, "explanation": "1312-ben zajlott a rozgonyi csata.", "teaches": ["rozgonyi-csata"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex17", "type": "fill-blank", "title": "V4 gyökerei", "instruction": "Egészítsd ki a mondatot!", "sentence": "A modern V4 együttműködés az 1335-ös ___ királytalálkozóra épül.", "correctAnswer": "visegrádi", "options": ["visegrádi", "budai", "bécsi", "prágai"], "teaches": ["elokep"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex18", "type": "sentence-builder", "title": "Nemesi jogegyenlőség 1351", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["1351-ben", "minden", "nemes", "ugyanazokat", "a", "jogokat", "kapta", "meg."], "correctSentence": "1351-ben minden nemes ugyanazokat a jogokat kapta meg.", "english": "In 1351 all nobles received the same rights.", "teaches": ["jogegyenloseg"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex19", "type": "multiple-choice", "title": "Keresztes felkelők", "instruction": "Ki vezette a nándorfehérvári keresztes népfelkelőket?", "question": "Hogy hívták a ferences hitszónokot?", "options": ["Kapisztrán János", "Julianus barát", "Gellért püspök", "Pázmány Péter"], "correctIndex": 0, "explanation": "Kapisztrán János vezette a keresztes felkelőket 1456-ban.", "teaches": ["keresztes"]})
u7_cons_ex.append({"id": "b1-anjouk-consolidation.ex20", "type": "fill-blank", "title": "Hetven évnyi béke", "instruction": "Egészítsd ki a mondatot!", "sentence": "A nándorfehérvári győzelem hetven évre ___ a török terjeszkedést.", "correctAnswer": "megállította", "options": ["megállította", "segítette", "gyorsította", "felejtette"], "teaches": ["megallit", "diadal"]})

write_json(EXERCISES_DIR / "b1-anjouk-consolidation-ex.json", {"exercises": u7_cons_ex})

write_json(LESSONS_DIR / "b1-anjouk-consolidation.json", make_consolidation_lesson(
    "lesson.b1.anjouk-consolidation",
    "The Angevin Kings & Late Medieval Power - Consolidation",
    [
        "Congratulations on completing Unit 7 of the Hungarian Citizenship Track!",
        "In this unit, you have explored Hungary's late medieval golden age: Charles Robert's economic renewal (aranyforint, kapuadó, urbura), the 1335 Congress of Visegrád, Louis the Great's 1351 laws (ősiség, kilenced, noble equality) and the first university in Pécs (1367), Sigismund of Luxemburg's European diplomacy at Constance, and John Hunyadi's epochal victory at Nándorfehérvár (1456) commemorated by the worldwide noon bell.",
        "Review your vocabulary and test your mastery across all 20 consolidation exercises."
    ],
    [
        "I can explain the economic and diplomatic achievements of Charles Robert (aranyforint, 1335 Visegrád).",
        "I can describe Louis the Great's 1351 laws (*ősiség / aviticitas, kilenced*) and the 1367 university of Pécs.",
        "I can summarize Sigismund's council of Constance and border fortress network (*végvárrendszer*).",
        "I can explain the significance of the 1456 Siege of Nándorfehérvár and the noon bell (*déli harangszó*)."
    ],
    "stories/world/b1/b1-anjouk.json",
    "exercises/b1/b1-anjouk-consolidation-ex.json",
    [f"b1-anjouk-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 7 (b1-anjouk) complete!")
