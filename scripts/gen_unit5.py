# -*- coding: utf-8 -*-
"""
Unit 5 Overhaul: The Árpád Dynasty (b1-arpadhaz)
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
# Lesson 1: Szent László király, a lovagkirály
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz-01-arpadhazikiralyok.json", make_story(
    "story.b1.arpadhaz.01",
    "Szent László, a lovagkirály és a törvények szigora",
    "King Saint Ladislaus (1077–1095): the ideal Christian knight-king, defender against Cuman incursions, creator of strict property laws, and unifier of Hungary and Croatia (1091).",
    "Nagyvárad és Zágráb",
    ["vonatkozó névmások: aki, akik"],
    ["Szent László király", "Lovagkirály", "Horvát-magyar perszonálunió"],
    [
        "I. László király (1077–1095) az Árpád-kor egyik legkiemelkedőbb uralkodója volt, akit a néphagyomány és a krónikák igazi keresztény lovagkirályként őriztek meg.",
        "A trónharcok után László helyreállította az ország belső békéjét. Rendkívül szigorú törvényeket hozott a lopás és a rablás ellen, hogy megvédje a magántulajdont és megszilárdítsa a közbiztonságot.",
        "László vitéz harcosként személyesen vezette hadait a keletről betörő nomád kunok és besenyők ellen, megerősítve a keleti határokat és megalapítva a nagyváradi püspökséget.",
        "1091-ben László hadjárata során elfoglalta Horvátországot, és megalapította a zágrábi püspökséget. Ezzel kezdetét vette a több mint nyolc évszázadon át tartó magyar-horvát államközösség (perszonálunió).",
        "László királyt 1192-ben szentté avatták; alakja a keresztény vitézség és az igazságos király örök példaképévé vált."
    ],
    [
        {"lemma": "lovagkirály", "pos": "noun", "cefr": "B1", "gloss": "knight-king / chivalric king"},
        {"lemma": "közbiztonság", "pos": "noun", "cefr": "B1", "gloss": "public safety / security"},
        {"lemma": "perszonálunió", "pos": "noun", "cefr": "B1", "gloss": "personal union"},
        {"lemma": "vitézség", "pos": "noun", "cefr": "B1", "gloss": "valour / bravery"}
    ],
    [
        {
            "question": "Milyen uralkodói eszményt képviselt I. László király?",
            "options": ["A keresztény lovagkirály és az igazságos hadvezér eszményét", "A visszavonult szerzetes életmódját", "A tengeri kalózkodást", "A despota keleti kán szerepét"],
            "correctIndex": 0,
            "explanation": "Szent László a keresztény lovagi eszmény, a bátorság és a törvényes szigor megtestesítője volt."
        },
        {
            "question": "Melyik országot kapcsolta a Magyar Királysághoz Szent László 1091-ben?",
            "options": ["Horvátországot (perszonálunió)", "Angliát", "Spanyolországot", "Svédországot"],
            "correctIndex": 0,
            "explanation": "1091-ben László megszerezte Horvátországot, megteremtve a nyolc évszázados államközösséget."
        },
        {
            "question": "Mi jellemezte Szent László törvényhozását?",
            "options": ["Rendkívül szigorúan büntette a lopást és védte a magántulajdont", "Eltörölte a magántulajdont", "Megengedte a rablóhadjáratokat", "Betiltotta a templomok építését"],
            "correctIndex": 0,
            "explanation": "László törvényei szigorúan büntették a tolvajlást a közbiztonság és a tulajdon védelmében."
        }
    ]
))

write_json(VOCAB_DIR / "b1-arpadhaz-01-voc.json", {
    "title": "Szent László, a lovagkirály",
    "words": [
        {"lemma": "lovagkirály", "pos": "noun", "cefr": "B1", "translation": "knight-king", "examples": [{"hungarian": "Szent László a magyar történelem legismertebb lovagkirálya.", "english": "Saint Ladislaus is the most famous knight-king of Hungarian history."}]},
        {"lemma": "közbiztonság", "pos": "noun", "cefr": "B1", "translation": "public security", "examples": [{"hungarian": "Szigorú törvényekkel állította helyre a közbiztonságot.", "english": "He restored public security with strict laws."}]},
        {"lemma": "perszonálunió", "pos": "noun", "cefr": "B1", "translation": "personal union", "examples": [{"hungarian": "A perszonálunió közös uralkodó alatti szövetséget jelentett.", "english": "The personal union meant an alliance under a common monarch."}]},
        {"lemma": "vitézség", "pos": "noun", "cefr": "B1", "translation": "valour / bravery", "examples": [{"hungarian": "A király vitézsége legendássá vált a csatákban.", "english": "The king's valour became legendary in battles."}]},
        {"lemma": "lopás", "pos": "noun", "cefr": "B1", "translation": "theft", "examples": [{"hungarian": "A lopást szigorúan büntették abban a korban.", "english": "Theft was strictly punished in that era."}]},
        {"lemma": "szigor", "pos": "noun", "cefr": "B1", "translation": "strictness / rigor", "examples": [{"hungarian": "A törvények szigora meghozta a rendet.", "english": "The strictness of the laws brought about order."}]},
        {"lemma": "helyreállít", "pos": "verb", "cefr": "B1", "translation": "to restore", "examples": [{"hungarian": "László helyreállította a belső békét.", "english": "Ladislaus restored internal peace."}]},
        {"lemma": "hadjárat", "pos": "noun", "cefr": "B1", "translation": "campaign / expedition", "examples": [{"hungarian": "Déli hadjárata kiterjesztette az ország határait.", "english": "His southern campaign expanded the country's borders."}]},
        {"lemma": "példakép", "pos": "noun", "cefr": "B1", "translation": "role model / exemplar", "examples": [{"hungarian": "Szent László a későbbi királyok példaképe lett.", "english": "Saint Ladislaus became a role model for later kings."}]},
        {"lemma": "megszáll", "pos": "verb", "cefr": "B1", "translation": "to occupy", "examples": [{"hungarian": "A seregek biztosították a déli tartományokat.", "english": "The armies secured the southern provinces."}]},
        {"lemma": "legendás", "pos": "adj", "cefr": "B1", "translation": "legendary", "examples": [{"hungarian": "Számos legendás monda fűződik a nevéhez.", "english": "Numerous legendary tales are attached to his name."}]},
        {"lemma": "püspökség", "pos": "noun", "cefr": "B1", "translation": "bishopric", "examples": [{"hungarian": "Megalapította a zágrábi püspökséget 1091-ben.", "english": "He founded the Zagreb bishopric in 1091."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-arpadhaz-01-aki-vonatkozoi-mellekmondat-gr.json", {
    "title": "Vonatkozó mellékmondatok személyekre (aki, akik)",
    "level": "B1",
    "rules": [
        {
            "id": "relative-pronoun-aki",
            "title": "Relative Pronouns for Persons: aki / akik",
            "text": "When the antecedent is a person, use *aki* (singular) and *akik* (plural): *László király volt az, aki megvédte a hazát.* (It was King Ladislaus who defended the homeland.) *A lovagok, akik a királlyal harcoltak, hűségesek voltak.*",
            "tip": "Always place a comma before *aki / akik*."
        },
        {
            "id": "case-agreement-relative",
            "title": "Case Marking on Relative Pronouns (akit, akinek)",
            "text": "The relative pronoun takes the grammatical case required by the subordinate clause: *a király, akit szentté avattak* (accusative), *az ispán, akinek a király parancsolt* (dative).",
            "tip": "Identify the verb in the subclause to choose the right suffix."
        }
    ],
    "examples": [
        {"spanish": "I. László volt az a király, aki szigorú törvényeket hozott.", "english": "Ladislaus I was the king who made strict laws."},
        {"spanish": "A harcosok, akik a kunok ellen küzdöttek, bátrak voltak.", "english": "The warriors who fought against the Cumans were brave."},
        {"spanish": "Szent László az az uralkodó, akit a lovagok példaképüknek tekintettek.", "english": "Saint Ladislaus is the monarch whom the knights considered their role model."}
    ]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-01-ex.json", {
    "exercises": [
        {
            "id": "b1-arpadhaz-01.ex01",
            "type": "multiple-choice",
            "title": "Szent László eszménye",
            "instruction": "Hogyan nevezi a magyar történetírás I. László királyt?",
            "question": "Milyen uralkodóként él László király a nemzeti emlékezetben?",
            "options": ["A lovagkirályként", "A vaskancellárként", "A Napkirályként", "A tengeri hajósként"],
            "correctIndex": 0,
            "explanation": "Szent László a magyar történelem legismertebb lovagkirálya.",
            "teaches": ["lovagkiraly", "vitezseg"]
        },
        {
            "id": "b1-arpadhaz-01.ex02",
            "type": "fill-blank",
            "title": "Törvényes szigor",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Szent László szigorú törvényeket hozott a ___ ellen a rend helyreállítására.",
            "correctAnswer": "lopás",
            "options": ["lopás", "tanulás", "utazás", "borkészítés"],
            "teaches": ["lopas", "szigor"]
        },
        {
            "id": "b1-arpadhaz-01.ex03",
            "type": "sentence-builder",
            "title": "Horvát perszonálunió",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["László", "király", "1091-ben", "Magyarországhoz", "kapcsolta", "Horvátországot."],
            "correctSentence": "László király 1091-ben Magyarországhoz kapcsolta Horvátországot.",
            "english": "King Ladislaus attached Croatia to Hungary in 1091.",
            "teaches": ["perszonalunio", "hadjarat"]
        },
        {
            "id": "b1-arpadhaz-01.ex04",
            "type": "multiple-choice",
            "title": "Vonatkozó névmás (aki)",
            "instruction": "Válaszd ki a helyes névmást a mondatba!",
            "question": "Szent László volt az az uralkodó, ___ legyőzte a kun támadókat.",
            "options": ["aki", "amely", "ahol", "amikor"],
            "correctIndex": 0,
            "explanation": "Személyekre a magyar nyelvben az 'aki' vonatkozó névmást használjuk.",
            "teaches": ["lovagkiraly"]
        },
        {
            "id": "b1-arpadhaz-01.ex05",
            "type": "fill-blank",
            "title": "Zágrábi püspökség",
            "instruction": "Válaszd ki a várost!",
            "sentence": "Szent László alapította meg a ___ püspökséget a déli tartományokban.",
            "correctAnswer": "zágrábi",
            "options": ["zágrábi", "párizsi", "londoni", "madridi"],
            "teaches": ["puspokseg", "perszonalunio"]
        },
        {
            "id": "b1-arpadhaz-01.ex06",
            "type": "sentence-builder",
            "title": "Közbiztonság helyreállítása",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "szigorú", "törvények", "helyreállították", "a", "közbiztonságot."],
            "correctSentence": "A szigorú törvények helyreállították a közbiztonságot.",
            "english": "The strict laws restored public security.",
            "teaches": ["kozbiztonsag", "helyreallit"]
        },
        {
            "id": "b1-arpadhaz-01.ex07",
            "type": "multiple-choice",
            "title": "Szentté avatás",
            "instruction": "Mikor avatták szentté László királyt?",
            "question": "Melyik évben avatták szentté I. Lászlót Nagyváradon?",
            "options": ["1192-ben III. Béla idején", "1526-ban", "1848-ban", "1000-ben"],
            "correctIndex": 0,
            "explanation": "Szent Lászlót 1192-ben avatták szentté Nagyváradon.",
            "teaches": ["peldakep"]
        },
        {
            "id": "b1-arpadhaz-01.ex08",
            "type": "fill-blank",
            "title": "Lovagi példakép",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Szent László a keresztény uralkodók örök ___ lett.",
            "correctAnswer": "példaképe",
            "options": ["példaképe", "ellensége", "rabja", "idegenje"],
            "teaches": ["peldakep", "vitezseg"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-arpadhaz-01.json", make_lesson(
    "lesson.b1.arpadhaz-01",
    "Szent László, a lovagkirály (Saint Ladislaus, the Knight-King)",
    "Vonatkozó mellékmondatok személyekre (aki, akik)",
    [
        "Welcome to Unit 5 of the Hungarian Citizenship Track, dedicated to the Árpád Dynasty (*Árpád-ház*), the founding royal lineage of Hungary (1000–1301).",
        "In this first lesson, we explore King Saint Ladislaus (*Szent László*, 1077–1095), the ideal Christian knight-king, his strict defense of public order and property, his defense against nomadic incursions, and the incorporation of Croatia (1091).",
        "We also practice relative clauses referring to persons with *aki / akik* and their case forms."
    ],
    [
        "I can describe the reign of Saint Ladislaus and his ideal of the Christian knight-king (*lovagkirály*).",
        "I can explain the personal union with Croatia founded in 1091.",
        "I can summarize Ladislaus's strict legal code protecting property and public safety.",
        "I can use personal relative pronouns (*aki, akik, akit*) accurately in complex sentences."
    ],
    "stories/world/b1/b1-arpadhaz-01-arpadhazikiralyok.json",
    "vocabulary/b1/b1-arpadhaz-01-voc.json",
    "grammar/b1/b1-arpadhaz-01-aki-vonatkozoi-mellekmondat-gr.json",
    "exercises/b1/b1-arpadhaz-01-ex.json",
    [f"b1-arpadhaz-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: II. András és az Aranybulla (1222)
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz-02-aranybulla.json", make_story(
    "story.b1.arpadhaz.02",
    "Az Aranybulla (1222) és a nemesi jogok születése",
    "King Andrew II and the Golden Bull of 1222 (*Aranybulla*): the foundational charter of Hungarian constitutional rights, tax exemption for royal servientes (nobles), and the famous Right of Resistance (*ellenállási záradék*).",
    "Székesfehérvár",
    ["vonatkozó névmások tárgyakra és fogalmakra: amely, amelyek, ami"],
    ["Aranybulla 1222", "II. András király", "Királyi szerviensek", "Ellenállási záradék"],
    [
        "A 13. század elején II. András király mértéktelen birtokadományozásai felborították a királyi birtokrendszert, és megerősítették a főurak (bárók) hatalmát a kisebb birtokosok rovására.",
        "A királyi szolgálattevők, a szerviensek és a várjobbágyok mozgalmat indítottak jogaik és birtokaik védelmében. Az elégedetlenség hatására II. András 1222-ben Székesfehérváron kiadta a híres Aranybullát.",
        "Az Aranybulla – amelyet függő aranypecsétjéről neveztek el – a magyar alkotmányfejlődés egyik legfontosabb alapdokumentuma, amelyet gyakran az angol Magna Cartához (1215) hasonlítanak.",
        "A dokumentum rögzítette a nemesek adómentességét, biztosította, hogy bírói ítélet nélkül senkit sem lehet fogságba vetni, és korlátozta a nemesek kötelező külföldi hadviselését.",
        "A legnevezetesebb a 31. pont, a híres ellenállási záradék (ius resistendi) volt, amely feljogosította a nemeseket és a főpapokat arra, hogy fegyverrel álljanak ellen a királynak, ha az megsérti az Aranybulla törvényeit."
    ],
    [
        {"lemma": "Aranybulla", "pos": "noun", "cefr": "B1", "gloss": "Golden Bull (1222 charter of rights)"},
        {"lemma": "aranypecsét", "pos": "noun", "cefr": "B1", "gloss": "golden seal / bulla"},
        {"lemma": "adómentesség", "pos": "noun", "cefr": "B1", "gloss": "tax exemption"},
        {"lemma": "ellenállási záradék", "pos": "noun", "cefr": "B1", "gloss": "clause of resistance (ius resistendi)"}
    ],
    [
        {
            "question": "Melyik évben adta ki II. András király az Aranybullát Székesfehérváron?",
            "options": ["1222-ben", "1000-ben", "1526-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "Az Aranybulla kiadásának éve 1222."
        },
        {
            "question": "Miről kapta az Aranybulla a nevét?",
            "options": ["A dokumentumra függesztett hitelesítő arany pecsétről (bulla)", "Mert aranylemezre vésték a szöveget", "Mert a király aranypénzt osztott mindenkinek", "Mert aranybányát nyitottak Székesfehérváron"],
            "correctIndex": 0,
            "explanation": "A bulla elnevezés a latin fém függőpecsétre utal, az Aranybullán aranypecsét lógott."
        },
        {
            "question": "Mit jelentett a 31. cikkely, az ellenállási záradék?",
            "options": ["Hogy a nemesek fegyverrel is ellenállhattak a királynak, ha az megszegte a törvényeket", "Hogy senki sem tagadhatta meg a katonai szolgálatot", "Hogy a parasztok nem mehettek el a földről", "Hogy a király bármikor feloszlathatta az országgyűlést"],
            "correctIndex": 0,
            "explanation": "Az ellenállási záradék felhatalmazta a rendeket a törvényszegő uralkodóval szembeni fegyveres fellépésre."
        }
    ]
))

write_json(VOCAB_DIR / "b1-arpadhaz-02-voc.json", {
    "title": "Az Aranybulla (1222) és a nemesi szabadságjogok",
    "words": [
        {"lemma": "Aranybulla", "pos": "noun", "cefr": "B1", "translation": "Golden Bull", "examples": [{"hungarian": "Az Aranybulla 1222-ben született meg.", "english": "The Golden Bull was born in 1222."}]},
        {"lemma": "aranypecsét", "pos": "noun", "cefr": "B1", "translation": "golden seal", "examples": [{"hungarian": "A király aranypecséttel hitelesítette az oklevelet.", "english": "The king authenticated the charter with a golden seal."}]},
        {"lemma": "adómentesség", "pos": "noun", "cefr": "B1", "translation": "tax exemption", "examples": [{"hungarian": "A nemesek teljes adómentességet kaptak.", "english": "The nobles received full tax exemption."}]},
        {"lemma": "ellenállási záradék", "pos": "noun", "cefr": "B1", "translation": "resistance clause", "examples": [{"hungarian": "Az ellenállási záradék a törvények betartását garantálta.", "english": "The resistance clause guaranteed adherence to the laws."}]},
        {"lemma": "szerviens", "pos": "noun", "cefr": "B1", "translation": "royal servant / early noble", "examples": [{"hungarian": "A királyi szerviensek a nemesség elődei voltak.", "english": "The royal servientes were the predecessors of the nobility."}]},
        {"lemma": "birtokadományozás", "pos": "noun", "cefr": "B1", "translation": "donation of estates", "examples": [{"hungarian": "A mértéktelen birtokadományozás gyengítette a kincstárat.", "english": "Excessive donation of estates weakened the treasury."}]},
        {"lemma": "elégedetlenség", "pos": "noun", "cefr": "B1", "translation": "discontent / dissatisfaction", "examples": [{"hungarian": "A nemesi elégedetlenség kényszerítette ki a reformot.", "english": "Noble discontent forced the reform."}]},
        {"lemma": "ítélet", "pos": "noun", "cefr": "B1", "translation": "verdict / judgment", "examples": [{"hungarian": "Bírói ítélet nélkül senkit nem lehetett elfogni.", "english": "Without a judicial verdict no one could be captured."}]},
        {"lemma": "fogság", "pos": "noun", "cefr": "B1", "translation": "captivity / imprisonment", "examples": [{"hungarian": "Védelmet élveztek a jogtalan fogság ellen.", "english": "They enjoyed protection against unlawful imprisonment."}]},
        {"lemma": "alapdokumentum", "pos": "noun", "cefr": "B1", "translation": "foundational document", "examples": [{"hungarian": "Az alkotmányos jogok alapdokumentuma lett.", "english": "It became the foundational document of constitutional rights."}]},
        {"lemma": "korlátoz", "pos": "verb", "cefr": "B1", "translation": "to limit / restrict", "examples": [{"hungarian": "A törvény korlátozta az uralkodó önkényét.", "english": "The law restricted the monarch's arbitrariness."}]},
        {"lemma": "feljogosít", "pos": "verb", "cefr": "B1", "translation": "to entitle / authorize", "examples": [{"hungarian": "A záradék feljogosította a nemeseket a tiltakozásra.", "english": "The clause entitled the nobles to protest."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-arpadhaz-02-aki-amely-gr.json", {
    "title": "Vonatkozó névmások tárgyakra és elvont fogalmakra (amely, amelyek, ami)",
    "level": "B1",
    "rules": [
        {
            "id": "relative-amely",
            "title": "Distinction Between 'aki' and 'amely'",
            "text": "While *aki* refers strictly to people, *amely / amelyek* refers to things, objects, laws, and abstract concepts: *az oklevél, amely rögzítette a jogokat* (the charter that recorded rights); *a törvények, amelyeket betartottak* (the laws that they observed).",
            "tip": "*Ami* refers to whole preceding ideas or indefinite pronouns (*minden, ami fontos*)."
        },
        {
            "id": "case-suffixes-amely",
            "title": "Case Endings on 'amely' (amelyet, amelyben, amellyel)",
            "text": "*Amely* inflects like a standard noun: accusative *amelyet*, inessive *amelyben*, instrumental *amellyel* (with consonant gemination *ly + v = lly*).",
            "tip": "Example: *a záradék, amellyel biztosították a jogokat*."
        }
    ],
    "examples": [
        {"spanish": "Az Aranybulla az az oklevél, amely biztosította a nemesi jogokat.", "english": "The Golden Bull is the charter that ensured noble rights."},
        {"spanish": "A dokumentumok, amelyeket 1222-ben írtak, ma is híresek.", "english": "The documents that were written in 1222 are famous even today."},
        {"spanish": "A pecsét, amellyel lezárták a levelet, aranyból készült.", "english": "The seal with which they closed the letter was made of gold."}
    ]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-02-ex.json", {
    "exercises": [
        {
            "id": "b1-arpadhaz-02.ex01",
            "type": "multiple-choice",
            "title": "Az Aranybulla éve",
            "instruction": "Melyik évben adta ki II. András király az Aranybullát?",
            "question": "Melyik történelmi évszámhoz kötődik az Aranybulla?",
            "options": ["1222", "1000", "1241", "1526"],
            "correctIndex": 0,
            "explanation": "Az Aranybulla kiadásának éve 1222.",
            "teaches": ["Aranybulla", "alapdokumentum"]
        },
        {
            "id": "b1-arpadhaz-02.ex02",
            "type": "fill-blank",
            "title": "Aranypecsét",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Az oklevél a rá függesztett ___ kapta az Aranybulla nevet.",
            "correctAnswer": "aranypecsétről",
            "options": ["aranypecsétről", "ezüstkardról", "papírról", "szalagról"],
            "teaches": ["aranypecset", "Aranybulla"]
        },
        {
            "id": "b1-arpadhaz-02.ex03",
            "type": "sentence-builder",
            "title": "Nemesi adómentesség",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Az", "Aranybulla", "biztosította", "a", "királyi", "szerviensek", "adómentességét."],
            "correctSentence": "Az Aranybulla biztosította a királyi szerviensek adómentességét.",
            "english": "The Golden Bull ensured the tax exemption of royal servientes.",
            "teaches": ["adomentesseg", "szerviens"]
        },
        {
            "id": "b1-arpadhaz-02.ex04",
            "type": "multiple-choice",
            "title": "Az ellenállási záradék",
            "instruction": "Melyik pont volt az Aranybulla leghíresebb rendelkezése?",
            "question": "Mit tartalmazott a 31. cikkely (ellenállási záradék)?",
            "options": ["Fegyveres ellenállási jogot a törvényszegő uralkodóval szemben", "A királyi korona külföldre küldését", "Minden mezőgazdasági adó megduplázását", "Az országgyűlés örökös betiltását"],
            "correctIndex": 0,
            "explanation": "Az ellenállási záradék a nemesség jogát rögzítette az alkotmánysértő királlyal szembeni fellépésre.",
            "teaches": ["ellenallasi-zaradek", "feljogosit"]
        },
        {
            "id": "b1-arpadhaz-02.ex05",
            "type": "fill-blank",
            "title": "Vonatkozó névmás (amely)",
            "instruction": "Válaszd ki a megfelelő névmást!",
            "sentence": "Ez volt az az oklevél, ___ rögzítette a magyar nemesség alapvető jogait.",
            "correctAnswer": "amely",
            "options": ["amely", "aki", "ahol", "amikor"],
            "teaches": ["alapdokumentum"]
        },
        {
            "id": "b1-arpadhaz-02.ex06",
            "type": "sentence-builder",
            "title": "Bírói ítélet nélkül",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Bírói", "ítélet", "nélkül", "senkit", "sem", "lehetett", "fogságba", "vetni."],
            "correctSentence": "Bírói ítélet nélkül senkit sem lehetett fogságba vetni.",
            "english": "Without a judicial verdict no one could be thrown into captivity.",
            "teaches": ["itelet", "fogsag"]
        },
        {
            "id": "b1-arpadhaz-02.ex07",
            "type": "multiple-choice",
            "title": "Párhuzam a Magna Cartával",
            "instruction": "Melyik híres angol oklevélhez szokták hasonlítani az Aranybullát?",
            "question": "Melyik európai dokumentum kortársa az 1222-es Aranybulla?",
            "options": ["Az 1215-ös angol Magna Carta", "A francia Emberi Jogi Nyilatkozat (1789)", "A washingtoni Függetlenségi Nyilatkozat (1776)", "A római tizenkét táblás törvények"],
            "correctIndex": 0,
            "explanation": "Az Aranybulla a kontinens egyik legkorábbi alkotmányos szabadságlevele a Magna Carta (1215) mellett.",
            "teaches": ["alapdokumentum"]
        },
        {
            "id": "b1-arpadhaz-02.ex08",
            "type": "fill-blank",
            "title": "Királyi hatalom korlátozása",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A törvények sikerrel ___ az uralkodó önkényes birtokadományozásait.",
            "correctAnswer": "korlátozták",
            "options": ["korlátozták", "dicsérték", "főzték", "énekelték"],
            "teaches": ["korlatoz", "birtokadomanyozas"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-arpadhaz-02.json", make_lesson(
    "lesson.b1.arpadhaz-02",
    "Az Aranybulla és a nemesi jogok (The Golden Bull - 1222)",
    "Vonatkozó névmások tárgyakra és fogalmakra (amely, amelyek, ami)",
    [
        "In this second lesson, we explore King Andrew II and the Golden Bull of 1222 (*Aranybulla*), one of Europe's earliest constitutional charters of liberty.",
        "You will learn about the movement of the royal *servientes*, the tax exemptions and personal liberties guaranteed to nobles, and the famous Right of Resistance (*ellenállási záradék*).",
        "We also practice relative pronouns referring to inanimate objects, laws, and abstract concepts (*amely, amelyek, amellyel*)."
    ],
    [
        "I can state the year (1222) and historical significance of the Golden Bull (*Aranybulla*).",
        "I can explain the main rights guaranteed in the charter (tax exemption, judicial protection, no arbitrary arrest).",
        "I can define the Right of Resistance (*ellenállási záradék / ius resistendi*).",
        "I can distinguish between *aki* (persons) and *amely* (concepts/things) in complex sentences."
    ],
    "stories/world/b1/b1-arpadhaz-02-aranybulla.json",
    "vocabulary/b1/b1-arpadhaz-02-voc.json",
    "grammar/b1/b1-arpadhaz-02-aki-amely-gr.json",
    "exercises/b1/b1-arpadhaz-02-ex.json",
    [f"b1-arpadhaz-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: Könyves Kálmán és III. Béla
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz-03-orszagszervezes.json", make_story(
    "story.b1.arpadhaz.03",
    "Könyves Kálmán felvilágosult törvényei és III. Béla kancelláriája",
    "King Coloman the Learned (1095–1116) and his enlightened decree ('Concerning witches who do not exist...'), followed by King Béla III (1172–1196), who established the Royal Chancellery and organized written state administration.",
    "Esztergom és Székesfehérvár",
    ["vonatkozó névmások esetei: amelyben, amellyel, amelynek"],
    ["Könyves Kálmán", "Boszorkánytörvény", "III. Béla király", "Királyi kancellária"],
    [
        "Szent László után unokaöccse, Könyves Kálmán király (1095–1116) lépett a trónra, aki mély teológiai és jogi műveltségével érdemelte ki a 'Könyves' jelzőt Európa-szerte.",
        "Kálmán enyhítette László szigorú büntetéseit, és híres felvilágosult törvényt hozott a boszorkányokról: 'A boszorkányokról pedig, mivelhogy nincsenek, semmiféle vizsgálatot ne tartsanak' (De strigis vero quae non sunt...).",
        "A 12. század második felében III. Béla király (1172–1196) uralkodása alatt Magyarország Európa egyik leggazdagabb és leghatalmasabb nagyhatalmává vált.",
        "Béla Bizáncban nevelkedett, és bevezette az írásbeliséget a közigazgatásba: elrendelte a Királyi Kancellária felállítását, megkövetelve, hogy minden elintézett ügyről írásos oklevél szülessen.",
        "III. Béla korában virágzott a gazdaság, az ezüst- és sóbányászat, és a király jövedelmei vetekedtek a francia és angol uralkodók vagyonával."
    ],
    [
        {"lemma": "műveltség", "pos": "noun", "cefr": "B1", "gloss": "erudition / education"},
        {"lemma": "kancellária", "pos": "noun", "cefr": "B1", "gloss": "royal chancellery"},
        {"lemma": "írásbeliség", "pos": "noun", "cefr": "B1", "gloss": "written administration / literacy"},
        {"lemma": "oklevél", "pos": "noun", "cefr": "B1", "gloss": "charter / diploma"}
    ],
    [
        {
            "question": "Miről híres Könyves Kálmán király törvénye a boszorkányokról?",
            "options": ["Kijelentette, hogy boszorkányok nem léteznek, ezért tilos vizsgálatot indítani ellenük", "Máglyahalált rendelt el minden faluban", "Boszorkányiskolát alapított Esztergomban", "Megtiltotta a könyvolvasást"],
            "correctIndex": 0,
            "explanation": "Könyves Kálmán híres törvénye szerint a boszorkányok nem léteznek ('De strigis vero quae non sunt...')."
        },
        {
            "question": "Mit vezetett be III. Béla király a közigazgatás megreformálására?",
            "options": ["A Királyi Kancelláriát és a kötelező írásbeli ügyintézést", "Az internetes adatbázist", "Minden hivatalos levél eltörlését", "A vármegyék feloszlatását"],
            "correctIndex": 0,
            "explanation": "III. Béla létrehozta a Királyi Kancelláriát és elrendelte az írásbeliséget minden hivatalos ügyben."
        },
        {
            "question": "Milyen volt Magyarország nemzetközi helyzete III. Béla idején?",
            "options": ["Európai nagyhatalom volt hatalmas királyi jövedelmekkel és virágzó kultúrával", "Egy elszegényedett, kiszolgáltatott tartomány", "Német hűbéri uralom alatt állt", "Teljesen elszigetelődött a világtól"],
            "correctIndex": 0,
            "explanation": "III. Béla kora a középkori Magyar Királyság virágkora és európai nagyhatalmi korszaka volt."
        }
    ]
))

write_json(VOCAB_DIR / "b1-arpadhaz-03-voc.json", {
    "title": "Könyves Kálmán és III. Béla reformjai",
    "words": [
        {"lemma": "műveltség", "pos": "noun", "cefr": "B1", "translation": "education / erudition", "examples": [{"hungarian": "Könyves Kálmán kiemelkedő műveltséggel rendelkezett.", "english": "Coloman the Learned possessed outstanding erudition."}]},
        {"lemma": "kancellária", "pos": "noun", "cefr": "B1", "translation": "chancellery", "examples": [{"hungarian": "A Királyi Kancellária készítette a hivatalos okleveleket.", "english": "The Royal Chancellery prepared the official charters."}]},
        {"lemma": "írásbeliség", "pos": "noun", "cefr": "B1", "translation": "written culture / administration", "examples": [{"hungarian": "Az írásbeliség bevezetése modernizálta az államot.", "english": "The introduction of written administration modernized the state."}]},
        {"lemma": "oklevél", "pos": "noun", "cefr": "B1", "translation": "charter / official deed", "examples": [{"hungarian": "Minden birtokról hiteles oklevél készült.", "english": "An authentic charter was made for every estate."}]},
        {"lemma": "felvilágosult", "pos": "adj", "cefr": "B1", "translation": "enlightened", "examples": [{"hungarian": "Felvilágosult törvényei megelőzték korukat.", "english": "His enlightened laws were ahead of their time."}]},
        {"lemma": "enyhít", "pos": "verb", "cefr": "B1", "translation": "to ease / mitigate", "examples": [{"hungarian": "Kálmán enyhítette a korábbi szigorú büntetéseket.", "english": "Coloman mitigated earlier harsh punishments."}]},
        {"lemma": "jövedelem", "pos": "noun", "cefr": "B1", "translation": "revenue / income", "examples": [{"hungarian": "A királyi jövedelmek a bányászatból származtak.", "english": "The royal revenues stemmed from mining."}]},
        {"lemma": "sóbányászat", "pos": "noun", "cefr": "B1", "translation": "salt mining", "examples": [{"hungarian": "Az erdélyi sóbányászat hatalmas vagyont hozott.", "english": "Transylvanian salt mining brought immense wealth."}]},
        {"lemma": "vetekszik", "pos": "verb", "cefr": "B1", "translation": "to rival / compete with", "examples": [{"hungarian": "Béla vagyona vetekedett a francia királyéval.", "english": "Béla's wealth rivalled that of the French king."}]},
        {"lemma": "ügyintézés", "pos": "noun", "cefr": "B1", "translation": "administration / management", "examples": [{"hungarian": "Az írásbeli ügyintézés pontos nyilvántartást teremtett.", "english": "Written administration created accurate record-keeping."}]},
        {"lemma": "nagyhatalom", "pos": "noun", "cefr": "B1", "translation": "great power", "examples": [{"hungarian": "A királyság közép-európai nagyhatalommá vált.", "english": "The kingdom became a Central European great power."}]},
        {"lemma": "vizsgálat", "pos": "noun", "cefr": "B1", "translation": "investigation", "examples": [{"hungarian": "Megtiltotta a boszorkányok elleni vizsgálatot.", "english": "He prohibited investigation against witches."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-arpadhaz-03-vonatkozoi-nevmas-esetei-gr.json", {
    "title": "A vonatkozó névmás esetragjai (amelyben, amellyel, amelynek)",
    "level": "B1",
    "rules": [
        {
            "id": "relatives-location-instrument",
            "title": "Inessive (amelyben) and Instrumental (amellyel)",
            "text": "*Amelyben* (in which / wherein): *a kancellária, amelyben az okleveleket írták* (the chancellery in which charters were written). *Amellyel* (with which): *a törvény, amellyel enyhítette a büntetéseket* (the law with which he mitigated punishments).",
            "tip": "Notice that the case corresponds to the role in the subclause."
        },
        {
            "id": "relatives-possessive",
            "title": "Genitive and Dative Forms (amelynek, amelyeknek)",
            "text": "*Amelynek* (whose / of which): *a királyság, amelynek a bevételei nőttek* (the kingdom whose revenues increased).",
            "tip": "Combines *amely* + *-nek* dative/genitive."
        }
    ],
    "examples": [
        {"spanish": "A Kancellária volt az az intézmény, amelyben az okleveleket fogalmazták.", "english": "The Chancellery was the institution in which charters were drafted."},
        {"spanish": "A törvény, amellyel Kálmán tiltotta a boszorkánypereket, felvilágosult volt.", "english": "The law with which Coloman banned witch trials was enlightened."},
        {"spanish": "III. Béla olyan országot vezetett, amelynek a vagyona vetekedett a császáréval.", "english": "Béla III led a country whose wealth rivalled that of the Emperor."}
    ]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-03-ex.json", {
    "exercises": [
        {
            "id": "b1-arpadhaz-03.ex01",
            "type": "multiple-choice",
            "title": "Könyves Kálmán ragadványneve",
            "instruction": "Miért kapta Kálmán király a 'Könyves' nevet?",
            "question": "Miért nevezték az uralkodót Könyves Kálmánnak?",
            "options": ["Kiemelkedő műveltsége és nagy olvasottsága miatt", "Mert könyvesboltot nyitott Esztergomban", "Mert nem tudott írni és olvasni", "Mert elégette a könyveket"],
            "correctIndex": 0,
            "explanation": "Kálmán korának egyik legműveltebb egyházi és világi tudósa volt.",
            "teaches": ["muveltseg", "felvilagosult"]
        },
        {
            "id": "b1-arpadhaz-03.ex02",
            "type": "fill-blank",
            "title": "Boszorkányok létezése",
            "instruction": "Egészítsd ki a híres törvény mondatát!",
            "sentence": "A boszorkányokról pedig, mivelhogy ___, semmiféle vizsgálatot ne tartsanak.",
            "correctAnswer": "nincsenek",
            "options": ["nincsenek", "vannak", "repülnek", "félnek"],
            "teaches": ["vizsgalat", "felvilagosult"]
        },
        {
            "id": "b1-arpadhaz-03.ex03",
            "type": "sentence-builder",
            "title": "Királyi Kancellária",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["III.", "Béla", "létrehozta", "a", "Királyi", "Kancelláriát", "az", "írásbeli", "ügyintézésre."],
            "correctSentence": "III. Béla létrehozta a Királyi Kancelláriát az írásbeli ügyintézésre.",
            "english": "Béla III established the Royal Chancellery for written administration.",
            "teaches": ["kancellaria", "irasbeliseg", "ugyintezes"]
        },
        {
            "id": "b1-arpadhaz-03.ex04",
            "type": "multiple-choice",
            "title": "Királyi jövedelmek",
            "instruction": "Mely gazdasági ágak biztosították III. Béla gazdagságát?",
            "question": "Honnan származtak a hatalmas királyi bevételek?",
            "options": ["Az ezüst- és sóbányászatból, vámokból és királyi birtokokból", "Csak külföldi kölcsönökből", "A gépgyártásból", "Tengeri kereskedelmi flottákból"],
            "correctIndex": 0,
            "explanation": "A nemesfém- és sóbányászat (különösen Erdélyben és a Felvidéken) tette gazdaggá a kincstárat.",
            "teaches": ["jovedelem", "sobanyaszat", "vetekszik"]
        },
        {
            "id": "b1-arpadhaz-03.ex05",
            "type": "fill-blank",
            "title": "Vonatkozó rag (amelyben)",
            "instruction": "Válaszd ki a mondatba illő alakot!",
            "sentence": "A kancellária volt az a hivatal, ___ minden hivatalos oklevelet kiállítottak.",
            "correctAnswer": "amelyben",
            "options": ["amelyben", "amellyel", "amelynek", "amelyre"],
            "teaches": ["kancellaria", "oklevel"]
        },
        {
            "id": "b1-arpadhaz-03.ex06",
            "type": "sentence-builder",
            "title": "Büntetések enyhítése",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Kálmán", "király", "enyhítette", "a", "korábbi", "szigorú", "törvényeket."],
            "correctSentence": "Kálmán király enyhítette a korábbi szigorú törvényeket.",
            "english": "King Coloman eased earlier strict laws.",
            "teaches": ["enyhit"]
        },
        {
            "id": "b1-arpadhaz-03.ex07",
            "type": "multiple-choice",
            "title": "Közép-európai nagyhatalom",
            "instruction": "Hogyan értékelik a történészek III. Béla uralkodását?",
            "question": "Milyen szerepet töltött be Magyarország a 12. század végén?",
            "options": ["Virágzó európai nagyhatalom volt fejlett kancelláriával", "Egy hanyatló kis falu volt", "Teljes belső zűrzavar jellemezte", "Nem létezett még állam"],
            "correctIndex": 0,
            "explanation": "III. Béla alatt a Magyar Királyság elérte középkori hatalmának egyik csúcspontját.",
            "teaches": ["nagyhatalom"]
        },
        {
            "id": "b1-arpadhaz-03.ex08",
            "type": "fill-blank",
            "title": "Írásos oklevelek",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Béla elrendelte, hogy minden elintézett ügyről írásos ___ szülessen.",
            "correctAnswer": "oklevél",
            "options": ["oklevél", "fénykép", "film", "hangfelvétel"],
            "teaches": ["oklevel", "irasbeliseg"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-arpadhaz-03.json", make_lesson(
    "lesson.b1.arpadhaz-03",
    "Könyves Kálmán és III. Béla (Coloman the Learned & Béla III)",
    "A vonatkozó névmás esetragjai (amelyben, amellyel, amelynek)",
    [
        "In this third lesson, we examine two great reform monarchs of the 12th century: Coloman the Learned (*Könyves Kálmán*) and Béla III (*III. Béla*).",
        "You will learn about Coloman's enlightened laws against witch persecutions, and Béla III's institution of the Royal Chancellery (*Királyi Kancellária*), establishing written public administration across a wealthy European powerhouse.",
        "We also practice case endings on relative pronouns (*amelyben, amellyel, amelynek*)."
    ],
    [
        "I can explain Coloman the Learned's enlightened law on witches (*'De strigis vero...'*).",
        "I can describe Béla III's establishment of the Royal Chancellery and the introduction of written administration.",
        "I can summarize the economic strength (salt and silver mining) of 12th-century Hungary.",
        "I can use oblique cases of *amely* (*amelyben, amellyel, amelynek*) correctly."
    ],
    "stories/world/b1/b1-arpadhaz-03-orszagszervezes.json",
    "vocabulary/b1/b1-arpadhaz-03-voc.json",
    "grammar/b1/b1-arpadhaz-03-vonatkozoi-nevmas-esetei-gr.json",
    "exercises/b1/b1-arpadhaz-03-ex.json",
    [f"b1-arpadhaz-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: Egyház, kultúra és Árpád-házi szentek
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz-04-egyhazesallam.json", make_story(
    "story.b1.arpadhaz.04",
    "Árpád-házi szentek és a román kori művészet",
    "The dynasty of saints: Saint Elizabeth of Hungary (patron of charity in Thuringia) and Saint Margaret of Hungary (her life of sacrifice on Rabbits' Island / Margaret Island), and Romanesque architecture (Ják, Zsámbék).",
    "Türingia (Wartburg), Margit-sziget és Ják",
    ["hely- és időhatározói vonatkozó névmások: ahol, amikor"],
    ["Árpád-házi szentek", "Szent Erzsébet", "Szent Margit", "Román stílus"],
    [
        "Az Árpád-házat Európában a 'szent királyok nemzetségeként' emlegették, mivel a dinasztia számos szentet és boldogot adott a keresztény világnak.",
        "A leghíresebb Árpád-házi női szent II. András lánya, Árpád-házi Szent Erzsébet volt. Türingia hercegnéjeként életét a szegények és betegek önfeláldozó gyógyításának és a karitatív munkának szentelte. Halála után alig négy évvel szentté avatták, és a caritas védőszentjévé vált.",
        "IV. Béla király leánya, Árpád-házi Szent Margit a Nyulak szigetén (a mai Margit-szigeten) lévő domonkos kolostorban élt, ahol életét az ország megmentéséért és a lelki békéért ajánlotta fel.",
        "A korszak építészetét a vastag falú, félköríves ablakokkal ellátott román stílusú templomok jellemezték. Legszebb máig fennmaradt példájuk a jáki bencés apátsági templom és a zsámbéki premontrei prépostság romja.",
        "Ezek a szentek és műemlékek a középkori magyar keresztény kultúra és európai kisugárzás maradandó értékeit képviselik."
    ],
    [
        {"lemma": "önfeláldozó", "pos": "adj", "cefr": "B1", "gloss": "self-sacrificing"},
        {"lemma": "karitatív", "pos": "adj", "cefr": "B1", "gloss": "charitable"},
        {"lemma": "román stílus", "pos": "noun", "cefr": "B1", "gloss": "Romanesque style"},
        {"lemma": "védőszent", "pos": "noun", "cefr": "B1", "gloss": "patron saint"}
    ],
    [
        {
            "question": "Miről vált világhírűvé Árpád-házi Szent Erzsébet?",
            "options": ["A szegények és betegek önfeláldozó gondozásáról és a jótékonyságról", "Katonai hódításairól és hadjáratairól", "Hatalmas aranykincsek gyűjtéséről", "Hajóépítésről"],
            "correctIndex": 0,
            "explanation": "Szent Erzsébet a jótékonyság, a karitatív munka és az elesettek segítésének világszerte tisztelt védőszentje."
        },
        {
            "question": "Hol élt és ajánlotta fel életét Árpád-házi Szent Margit?",
            "options": ["A mai Margit-szigeten lévő domonkos kolostorban", "Párizsban egy palotában", "Róma erődítményeiben", "Egy távoli szigeten Ázsiában"],
            "correctIndex": 0,
            "explanation": "Szent Margit a Nyulak szigetén (amelyet róla neveztek el Margit-szigetnek) élt szent életet."
        },
        {
            "question": "Melyik híres magyarországi templom képviseli a román stílusú építészet csúcsát?",
            "options": ["A jáki apátsági templom", "A Parlament épülete", "A Lánchíd pilonjai", "A Nyugati pályaudvar"],
            "correctIndex": 0,
            "explanation": "A jáki templom a magyarországi román stílusú építészet legismertebb remekműve."
        }
    ]
))

write_json(VOCAB_DIR / "b1-arpadhaz-04-voc.json", {
    "title": "Árpád-házi szentek és a román stílus",
    "words": [
        {"lemma": "önfeláldozó", "pos": "adj", "cefr": "B1", "translation": "self-sacrificing", "examples": [{"hungarian": "Önfeláldozó szeretettel segítette a rászorulókat.", "english": "She helped the needy with self-sacrificing love."}]},
        {"lemma": "karitatív", "pos": "adj", "cefr": "B1", "translation": "charitable", "examples": [{"hungarian": "A karitatív tevékenység mintaképe lett.", "english": "She became the archetype of charitable activity."}]},
        {"lemma": "védőszent", "pos": "noun", "cefr": "B1", "translation": "patron saint", "examples": [{"hungarian": "Szent Erzsébet a segélyszervezetek védőszentje.", "english": "Saint Elizabeth is the patron saint of charity organizations."}]},
        {"lemma": "román stílus", "pos": "noun", "cefr": "B1", "translation": "Romanesque style", "examples": [{"hungarian": "A jáki templom a román stílus gyöngyszeme.", "english": "The church of Ják is a gem of Romanesque style."}]},
        {"lemma": "kolostor", "pos": "noun", "cefr": "B1", "translation": "monastery / convent", "examples": [{"hungarian": "Margit a szigeti kolostorban élt.", "english": "Margaret lived in the island convent."}]},
        {"lemma": "domonkos", "pos": "adj", "cefr": "B1", "translation": "Dominican", "examples": [{"hungarian": "A domonkos apácák imádkoztak a békéért.", "english": "The Dominican nuns prayed for peace."}]},
        {"lemma": "szegénygondozás", "pos": "noun", "cefr": "B1", "translation": "care for the poor", "examples": [{"hungarian": "A szegénygondozás vezérelte Erzsébet életét.", "english": "Care for the poor guided Elizabeth's life."}]},
        {"lemma": "félköríves", "pos": "adj", "cefr": "B1", "translation": "semicircular / rounded arch", "examples": [{"hungarian": "Félköríves ablakok és kapuk díszítik a falakat.", "english": "Semicircular windows and portals decorate the walls."}]},
        {"lemma": "apátság", "pos": "noun", "cefr": "B1", "translation": "abbey", "examples": [{"hungarian": "A jáki apátság ma is látogatható.", "english": "The Ják abbey can still be visited today."}]},
        {"lemma": "kisugárzás", "pos": "noun", "cefr": "B1", "translation": "cultural impact / radiance", "examples": [{"hungarian": "A magyar szentek európai kisugárzása hatalmas volt.", "english": "The European cultural impact of Hungarian saints was immense."}]},
        {"lemma": "emlékezet", "pos": "noun", "cefr": "B1", "translation": "remembrance / memory", "examples": [{"hungarian": "Nevüket hálával őrzi az egyházi emlékezet.", "english": "Ecclesiastical memory preserves their names with gratitude."}]},
        {"lemma": "nemzetség", "pos": "noun", "cefr": "B1", "translation": "dynasty / lineage", "examples": [{"hungarian": "A szent királyok nemzetségeként tisztelték az Árpád-házat.", "english": "The Árpád Dynasty was revered as the lineage of holy kings."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-arpadhaz-04-ahol-amikor-gr.json", {
    "title": "Hely- és időhatározói vonatkozó névmások (ahol, amikor)",
    "level": "B1",
    "rules": [
        {
            "id": "relatives-ahol-amikor",
            "title": "Relative Adverbs: ahol (where) and amikor (when)",
            "text": "Use *ahol* for places (*a sziget, ahol Margit élt* = the island where Margaret lived) and *amikor* for points in time (*az év, amikor szentté avatták* = the year when she was canonized).",
            "tip": "Always put a comma before *ahol* and *amikor*."
        },
        {
            "id": "directional-relatives",
            "title": "Directional Relatives (ahonnan, ahová)",
            "text": "*Ahová* (to where / whither): *a kolostor, ahová beköltözött*; *Ahonnan* (from where / whence): *a város, ahonnan elindult*.",
            "tip": "Match the relative adverb to the direction of motion."
        }
    ],
    "examples": [
        {"spanish": "A Margit-sziget az a hely, ahol Szent Margit imádkozott az országért.", "english": "Margaret Island is the place where Saint Margaret prayed for the country."},
        {"spanish": "1235 volt az az év, amikor Szent Erzsébetet szentté avatták.", "english": "1235 was the year when Saint Elizabeth was canonized."},
        {"spanish": "Ják az a falu, ahol a híres román stílusú templom áll.", "english": "Ják is the village where the famous Romanesque church stands."}
    ]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-04-ex.json", {
    "exercises": [
        {
            "id": "b1-arpadhaz-04.ex01",
            "type": "multiple-choice",
            "title": "Szent Erzsébet tevékenysége",
            "instruction": "Miről ismert világszerte Árpád-házi Szent Erzsébet?",
            "question": "Melyik terület védőszentje Szent Erzsébet?",
            "options": ["A jótékonyság, az elesettek és a szeretetszolgálat védőszentje", "A haditengerészet parancsnoka", "A banki kereskedelem vezetője", "A lovagi tornák győztese"],
            "correctIndex": 0,
            "explanation": "Szent Erzsébet a világ egyik legismertebb katolikus karitatív szentje.",
            "teaches": ["vedoszent", "karitativ", "onfelaldozo"]
        },
        {
            "id": "b1-arpadhaz-04.ex02",
            "type": "fill-blank",
            "title": "Szent Margit szigete",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "IV. Béla leánya, Szent Margit a mai ___ lévő domonkos kolostorban élt.",
            "correctAnswer": "Margit-szigeten",
            "options": ["Margit-szigeten", "Hajógyári-szigeten", "Csepel-szigeten", "Szentendrei-szigeten"],
            "teaches": ["kolostor", "domonkos"]
        },
        {
            "id": "b1-arpadhaz-04.ex03",
            "type": "sentence-builder",
            "title": "Jáki templom",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "jáki", "apátsági", "templom", "a", "román", "stílus", "híres", "remekműve."],
            "correctSentence": "A jáki apátsági templom a román stílus híres remekműve.",
            "english": "The Ják abbey church is a famous masterpiece of Romanesque style.",
            "teaches": ["roman-stilus", "apatsag"]
        },
        {
            "id": "b1-arpadhaz-04.ex04",
            "type": "multiple-choice",
            "title": "Helyhatározói vonatkozó (ahol)",
            "instruction": "Válaszd ki a helyes kötőszót!",
            "question": "Ez az a kolostor, ___ Szent Margit élt.",
            "options": ["ahol", "amikor", "aki", "amelyet"],
            "correctIndex": 0,
            "explanation": "Helyszínekre az 'ahol' vonatkozó névmást használjuk.",
            "teaches": ["kolostor"]
        },
        {
            "id": "b1-arpadhaz-04.ex05",
            "type": "fill-blank",
            "title": "A szent királyok nemzetsége",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Az Árpád-házat Európa-szerte a szent királyok ___ nevezték.",
            "correctAnswer": "nemzetségének",
            "options": ["nemzetségének", "ellenségének", "rabjának", "hadseregének"],
            "teaches": ["nemzetseg", "kisugarzas"]
        },
        {
            "id": "b1-arpadhaz-04.ex06",
            "type": "sentence-builder",
            "title": "Időhatározói vonatkozó (amikor)",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["1235", "volt", "az", "év,", "amikor", "Erzsébetet", "szentté", "avatták."],
            "correctSentence": "1235 volt az év, amikor Erzsébetet szentté avatták.",
            "english": "1235 was the year when Elizabeth was canonized.",
            "teaches": ["vedoszent"]
        },
        {
            "id": "b1-arpadhaz-04.ex07",
            "type": "multiple-choice",
            "title": "Román stílusú építészet",
            "instruction": "Milyen építészeti stílus jellemezte az Árpád-kori templomokat?",
            "question": "Mely stílusjegyek láthatók a jáki és zsámbéki templomokon?",
            "options": ["Román stílus vastag falakkal és félköríves kapukkal", "Gótikus felhőkarcolók üveggel", "Barokk aranyozott kupolák", "Modern betonépületek"],
            "correctIndex": 0,
            "explanation": "A kor építészetét a román stílus félköríves ablakai és masszív kőfalai határozták meg.",
            "teaches": ["roman-stilus", "felkorives"]
        },
        {
            "id": "b1-arpadhaz-04.ex08",
            "type": "fill-blank",
            "title": "Szegénygondozás",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Szent Erzsébet az elesettek és a betegek ___ szentelte életét.",
            "correctAnswer": "segítésének",
            "options": ["segítésének", "eladásának", "bezárásának", "kerülésének"],
            "teaches": ["szegenygondozas", "onfelaldozo"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-arpadhaz-04.json", make_lesson(
    "lesson.b1.arpadhaz-04",
    "Árpád-házi szentek és a román stílus (Dynasty of Saints & Romanesque Art)",
    "Hely- és időhatározói vonatkozó névmások (ahol, amikor)",
    [
        "In this fourth lesson, we explore the spiritual and cultural radiance of the Árpád Dynasty, known across medieval Christendom as the 'Lineage of Holy Kings'.",
        "You will learn about Saint Elizabeth of Hungary (patron saint of charity and hospitals), Saint Margaret of Hungary on Margaret Island (*Margit-sziget*), and the Romanesque masterpieces of Ják and Zsámbék.",
        "We also practice relative adverbs of location (*ahol, ahová, ahonnan*) and time (*amikor*)."
    ],
    [
        "I can describe the life and global legacy of Saint Elizabeth of Hungary (*Árpád-házi Szent Erzsébet*).",
        "I can explain Saint Margaret's historical connection to Margaret Island (*Margit-sziget*).",
        "I can recognize Romanesque architectural features (*román stílus, jáki templom*).",
        "I can use relative adverbs *ahol* and *amikor* fluently in Hungarian."
    ],
    "stories/world/b1/b1-arpadhaz-04-egyhazesallam.json",
    "vocabulary/b1/b1-arpadhaz-04-voc.json",
    "grammar/b1/b1-arpadhaz-04-ahol-amikor-gr.json",
    "exercises/b1/b1-arpadhaz-04-ex.json",
    [f"b1-arpadhaz-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: Az Árpád-ház kihalása (1301)
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz-05-arpadhazvege.json", make_story(
    "story.b1.arpadhaz.05",
    "Az Árpád-ház kihalása (1301) és a kiskirályok kora",
    "The death of King Andrew III in 1301 ('the last golden twig'), the end of the 300-year Árpád Dynasty, and the era of oligarchs (*kiskirályok / tartományurak*) like Máté Csák.",
    "Buda, Visegrád és Trencsén",
    ["szintetizáló szerkezetek és trónöröklési fordulatok"],
    ["1301", "III. András halála", "Kiskirályok kora", "Interregnum"],
    [
        "1301. január 14-én Budán elhunyt III. András király, akit a kortárs krónikás 'Szent István első király nemzetségének utolsó aranyágacskájaként' siratott el.",
        "Halálával fiágon kihalt a több mint három évszázadon át uralkodó Árpád-dinasztia, amely megteremtette és megszilárdította a független magyar keresztény államot.",
        "Az uralkodó halálát követően súlyos hatalmi válság (interregnum) és trónviszály tört ki. A hatalmat a megerősödött főurak, a tartományurak – gúnynevükön a 'kiskirályok' – ragadták magukhoz.",
        "Olyan nagyurak, mint Csák Máté a Felvidéken, Kőszegi Henrik a Dunántúlon vagy Aba Amadé északkeleten saját magánhadsereget tartottak, pénzt vertek és független fejedelemként uralkodtak birtokaikon.",
        "Az ország egységének helyreállítása és a kiskirályok letörése az új dinasztia, az Anjou-ház feladata lett a 14. század elején."
    ],
    [
        {"lemma": "utolsó aranyágacska", "pos": "noun", "cefr": "B1", "gloss": "the last golden twig (last Árpád king)"},
        {"lemma": "tartományúr", "pos": "noun", "cefr": "B1", "gloss": "provincial lord / oligarch (kiskirály)"},
        {"lemma": "kihal", "pos": "verb", "cefr": "B1", "gloss": "to die out / become extinct (dynasty)"},
        {"lemma": "hatalmi válság", "pos": "noun", "cefr": "B1", "gloss": "power crisis / interregnum"}
    ],
    [
        {
            "question": "Melyik évben halt meg III. András, amellyel kihalt az Árpád-ház férfiága?",
            "options": ["1301-ben", "1000-ben", "1222-ben", "1526-ban"],
            "correctIndex": 0,
            "explanation": "1301-ben III. András halálával halt ki fiágon az Árpád-ház."
        },
        {
            "question": "Hogyan nevezte a középkori krónika III. András királyt?",
            "options": ["'Az utolsó aranyágacskának'", "'A lovagkirálynak'", "'A honalapítónak'", "'A gazdag császárnak'"],
            "correctIndex": 0,
            "explanation": "A krónikás Szent István nemzetségének 'utolsó aranyágacskájaként' jellemezte III. Andrást."
        },
        {
            "question": "Kik uralták az ország részeit az Árpád-ház kihalása után az interregnum idején?",
            "options": ["A függetlenedő tartományurak (kiskirályok, pl. Csák Máté)", "A római császár légiói", "A török szultán seregei", "A spanyol zsoldosok"],
            "correctIndex": 0,
            "explanation": "A tartományurak (kiskirályok, pl. Csák Máté, Aba Amadé) ragadták magukhoz a tényleges hatalmat."
        }
    ]
))

write_json(VOCAB_DIR / "b1-arpadhaz-05-voc.json", {
    "title": "Az Árpád-ház kihalása (1301) és a tartományurak",
    "words": [
        {"lemma": "utolsó aranyágacska", "pos": "noun", "cefr": "B1", "translation": "the last golden twig", "examples": [{"hungarian": "III. András volt az Árpád-ház utolsó aranyágacskája.", "english": "Andrew III was the last golden twig of the Árpád Dynasty."}]},
        {"lemma": "tartományúr", "pos": "noun", "cefr": "B1", "translation": "oligarch / provincial lord", "examples": [{"hungarian": "A tartományurak saját törvényeik szerint éltek.", "english": "The provincial lords lived according to their own laws."}]},
        {"lemma": "kihal", "pos": "verb", "cefr": "B1", "translation": "to die out / go extinct", "examples": [{"hungarian": "1301-ben kihalt az uralkodóház férfiága.", "english": "In 1301 the male line of the ruling house died out."}]},
        {"lemma": "hatalmi válság", "pos": "noun", "cefr": "B1", "translation": "power crisis / interregnum", "examples": [{"hungarian": "Súlyos hatalmi válság rázta meg az országot.", "english": "A severe power crisis shook the country."}]},
        {"lemma": "kiskirály", "pos": "noun", "cefr": "B1", "translation": "petty king / oligarch", "examples": [{"hungarian": "A kiskirályok megosztották a királyságot.", "english": "The petty kings divided the kingdom."}]},
        {"lemma": "magánhadsereg", "pos": "noun", "cefr": "B1", "translation": "private army", "examples": [{"hungarian": "Csák Máté hatalmas magánhadsereget tartott fenn.", "english": "Máté Csák maintained a huge private army."}]},
        {"lemma": "interregnum", "pos": "noun", "cefr": "B1", "translation": "interregnum / rulerless period", "examples": [{"hungarian": "Az interregnum évei bizonytalanságot hoztak.", "english": "The years of interregnum brought uncertainty."}]},
        {"lemma": "helyreállít", "pos": "verb", "cefr": "B1", "translation": "to restore", "examples": [{"hungarian": "Az új király helyreállította az egységet.", "english": "The new king restored unity."}]},
        {"lemma": "letör", "pos": "verb", "cefr": "B1", "translation": "to crush / break down", "examples": [{"hungarian": "Hosszú harcokban törték le a bárók uralmát.", "english": "In long battles they crushed the rule of the barons."}]},
        {"lemma": "trónviszály", "pos": "noun", "cefr": "B1", "translation": "throne conflict", "examples": [{"hungarian": "Több külföldi herceg vetélkedett a trónért.", "english": "Several foreign princes competed for the throne."}]},
        {"lemma": "dinasztia", "pos": "noun", "cefr": "B1", "translation": "dynasty", "examples": [{"hungarian": "Az Árpád-dinasztia 300 éven át vezette a hazát.", "english": "The Árpád dynasty led the homeland for 300 years."}]},
        {"lemma": "elsirat", "pos": "verb", "cefr": "B1", "translation": "to mourn / weep for", "examples": [{"hungarian": "Az egész ország elsiratta a szeretett királyt.", "english": "The whole country mourned the beloved king."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-arpadhaz-05-synthesis-gr.json", {
    "title": "Történeti korszakváltások kifejezése és összetett szintézis",
    "level": "B1",
    "rules": [
        {
            "id": "epoch-transition-phrases",
            "title": "Expressing Eras and Transitions in Hungarian",
            "text": "Mark epoch shifts using: *halálával lezárult a korszak* (with his death an era closed); *kezdetét vette az új korszak* (the new era began); *utódot hagyott hátra* (he left behind a successor).",
            "tip": "Combines instrumental (*-val / -vel*) and inchoative verbs (*kezdetét veszi*)."
        },
        {
            "id": "consequence-modifiers",
            "title": "Participial Adverbials (-va / -ve) in Historical Summaries",
            "text": "Express accompanying circumstances with the adverbial participle (*-va / -ve*): *megosztva az országot* (dividing the country), *birtokba véve a várakat* (taking possession of the castles).",
            "tip": "Adverbial participles describe how or under what circumstances the main action happened."
        }
    ],
    "examples": [
        {"spanish": "III. András halálával lezárult az Árpád-kor háromszáz éves korszaka.", "english": "With the death of Andrew III, the three-hundred-year era of the Árpád Age came to a close."},
        {"spanish": "A tartományurak magánhadsereget tartva uralkodtak birtokaikon.", "english": "The provincial lords ruled their estates while maintaining private armies."},
        {"spanish": "1301 után új dinasztia került a magyar trónra.", "english": "After 1301, a new dynasty ascended to the Hungarian throne."}
    ]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-05-ex.json", {
    "exercises": [
        {
            "id": "b1-arpadhaz-05.ex01",
            "type": "multiple-choice",
            "title": "Az Árpád-ház kihalása",
            "instruction": "Melyik évben halt meg III. András?",
            "question": "Mikor ért véget az Árpád-dinasztia férfiága?",
            "options": ["1301-ben", "1222-ben", "1456-ban", "1526-ban"],
            "correctIndex": 0,
            "explanation": "1301. január 14-én hunyt el III. András király.",
            "teaches": ["kihal", "dinasztia"]
        },
        {
            "id": "b1-arpadhaz-05.ex02",
            "type": "fill-blank",
            "title": "Az utolsó aranyágacska",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A krónikás Szent István nemzetségének utolsó ___ nevezte III. Andrást.",
            "correctAnswer": "aranyágacskájaként",
            "options": ["aranyágacskájaként", "lovagjaként", "püspökeként", "katonájaként"],
            "teaches": ["utolso-aranyagacska"]
        },
        {
            "id": "b1-arpadhaz-05.ex03",
            "type": "sentence-builder",
            "title": "Kiskirályok kora",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Az", "Árpád-ház", "kihalása", "után", "a", "tartományurak", "ragadták", "magukhoz", "a", "hatalmat."],
            "correctSentence": "Az Árpád-ház kihalása után a tartományurak ragadták magukhoz a hatalmat.",
            "english": "After the extinction of the Árpád Dynasty, the provincial lords seized power.",
            "teaches": ["tartomanyur", "kiskiraly", "hatalmi-valsag"]
        },
        {
            "id": "b1-arpadhaz-05.ex04",
            "type": "multiple-choice",
            "title": "A leghíresebb tartományúr",
            "instruction": "Ki volt a Felvidék leghatalmasabb oligarchája az interregnum idején?",
            "question": "Melyik kiskirály uralta a Felvidéket Trencsén központtal?",
            "options": ["Csák Máté", "Kossuth Lajos", "Petőfi Sándor", "Széchenyi István"],
            "correctIndex": 0,
            "explanation": "Csák Máté trencséni várából független uralkodóként irányította a Felvidék nagy részét.",
            "teaches": ["tartomanyur", "kiskiraly"]
        },
        {
            "id": "b1-arpadhaz-05.ex05",
            "type": "fill-blank",
            "title": "Korszakzárás",
            "instruction": "Válaszd ki a helyes kifejezést!",
            "sentence": "III. András halálával ___ vette a trónharcok és az interregnum korszaka.",
            "correctAnswer": "kezdetét",
            "options": ["kezdetét", "végét", "békéjét", "ünnepét"],
            "teaches": ["interregnum", "hatalmi-valsag"]
        },
        {
            "id": "b1-arpadhaz-05.ex06",
            "type": "sentence-builder",
            "title": "Magánhadseregek",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "tartományurak", "saját", "magánhadsereget", "tartottak", "fenn."],
            "correctSentence": "A tartományurak saját magánhadsereget tartottak fenn.",
            "english": "The provincial lords maintained their own private armies.",
            "teaches": ["maganhadsereg"]
        },
        {
            "id": "b1-arpadhaz-05.ex07",
            "type": "multiple-choice",
            "title": "Az új dinasztia",
            "instruction": "Melyik dinasztia szerezte meg a magyar trónt az Árpád-ház után?",
            "question": "Melyik uralkodóház egyesítette újra az országot a 14. század elején?",
            "options": ["Az Anjou-ház (Károly Róbert)", "A Habsburg-ház", "A Bourbon-ház", "A Tudor-ház"],
            "correctIndex": 0,
            "explanation": "Az Árpád-ház után az Anjou-dinasztia (Károly Róbert) szerezte meg a koronát és törte le a kiskirályokat.",
            "teaches": ["dinasztia", "helyreallit"]
        },
        {
            "id": "b1-arpadhaz-05.ex08",
            "type": "fill-blank",
            "title": "Hatalmi válság",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A király halála után súlyos ___ válság rázta meg Magyarországot.",
            "correctAnswer": "hatalmi",
            "options": ["hatalmi", "tengeri", "erdészeti", "sport"],
            "teaches": ["hatalmi-valsag"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-arpadhaz-05.json", make_lesson(
    "lesson.b1.arpadhaz-05",
    "Az Árpád-ház kihalása (Extinction of the Árpád Dynasty - 1301)",
    "Történeti korszakváltások kifejezése és összetett szintézis",
    [
        "In this fifth lesson, we examine the conclusion of the Árpád Age in 1301 with the death of King Andrew III ('the last golden twig').",
        "You will learn about the interregnum, the rise of provincial oligarchs (*kiskirályok / tartományurak*) such as Máté Csák, and the stage set for the Angevin restoration.",
        "We also practice epoch-transition discourse markers and adverbial participles (*-va / -ve*)."
    ],
    [
        "I can state the year of the extinction of the Árpád Dynasty (1301) and identify King Andrew III.",
        "I can describe the era of oligarchs (*kiskirályok, tartományurak, Csák Máté*).",
        "I can explain the significance of the 300-year Árpád Dynasty in Hungarian statehood.",
        "I can construct sentences describing historic turning points and transitions."
    ],
    "stories/world/b1/b1-arpadhaz-05-arpadhazvege.json",
    "vocabulary/b1/b1-arpadhaz-05-voc.json",
    "grammar/b1/b1-arpadhaz-05-synthesis-gr.json",
    "exercises/b1/b1-arpadhaz-05-ex.json",
    [f"b1-arpadhaz-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 5 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-arpadhaz.json", make_story(
    "story.b1.arpadhaz",
    "Az Árpád-kor három évszázada (1000–1301)",
    "A grand synthesis of the three-century Árpád Dynasty: Saint Ladislaus the knight-king, the Golden Bull of 1222, Coloman's enlightened laws, Béla III's chancellery, the dynasty of saints, and the close of the golden era in 1301.",
    "Kárpát-medence",
    ["összetett mondatszerkezetek", "történeti szintézis"],
    ["Árpád-ház", "Aranybulla", "Középkori Magyarország", "Szentek és reformok"],
    [
        "Az Árpád-kor három évszázada (1000–1301) megalapozta a független, virágzó keresztény Magyar Királyságot Közép-Európa szívében.",
        "Szent László lovagkirály megvédte az országot a keleti nomád betörésektől, szigorú törvényekkel garantálta a belső rendet és a magántulajdont, és 1091-ben Horvátország megszerzésével létrehozta a több mint nyolcszáz éves perszonáluniót.",
        "Könyves Kálmán felvilágosult törvényei és III. Béla kancelláriája modernizálták az államigazgatást és az írásbeliséget, európai rangú nagyhatalommá emelve a királyságot.",
        "1222-ben II. András Aranybullája lefektette a magyar alkotmányosság alapköveit, rögzítve a nemesi adómentességet és a híres ellenállási záradékot.",
        "A dinasztia olyan világhírű szenteket adott a kereszténységnek, mint Szent Erzsébet és Szent Margit, mielőtt 1301-ben III. András, 'az utolsó aranyágacska' halálával lezárult volna a dicső Árpád-kor."
    ],
    [
        {"lemma": "Árpád-kor", "pos": "noun", "cefr": "B1", "gloss": "Árpád Age (1000–1301)"},
        {"lemma": "Aranybulla", "pos": "noun", "cefr": "B1", "gloss": "Golden Bull (1222)"},
        {"lemma": "alkotmányosság", "pos": "noun", "cefr": "B1", "gloss": "constitutionalism"},
        {"lemma": "dinasztia", "pos": "noun", "cefr": "B1", "gloss": "dynasty"}
    ],
    [
        {
            "question": "Melyik időszakot öleli fel az Árpád-kor a magyar történelemben?",
            "options": ["1000-től 1301-ig (Szent Istvántól III. András haláláig)", "895-től 907-ig", "1526-tól 1686-ig", "1848-tól 1918-ig"],
            "correctIndex": 0,
            "explanation": "Az Árpád-dinasztia korszaka 1000-től 1301-ig tartott."
        },
        {
            "question": "Melyik 1222-es oklevél vált a magyar alkotmányfejlődés alapjává?",
            "options": ["Az Aranybulla", "A Pragmatica Sanctio", "A Hármaskönyv", "A Függetlenségi Nyilatkozat"],
            "correctIndex": 0,
            "explanation": "Az 1222-es Aranybulla rögzítette a nemesi jogokat és az ellenállási záradékot."
        },
        {
            "question": "Mely európai szentek származtak az Árpád-házból?",
            "options": ["Árpád-házi Szent Erzsébet és Szent Margit", "Szűz Mária és Mária Magdolna", "Jeanne d'Arc", "Avilai Teréz"],
            "correctIndex": 0,
            "explanation": "Szent Erzsébet és Szent Margit az Árpád-ház világszerte tisztelt szentjei."
        }
    ]
))

u5_cons_ex = []
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex01",
    "type": "multiple-choice",
    "title": "Árpád-kor időtartama",
    "instruction": "Melyik évszámok határolják az Árpád-kort?",
    "question": "Mettől meddig uralkodott az Árpád-ház?",
    "options": ["1000–1301", "895–1000", "1301–1526", "1526–1686"],
    "correctIndex": 0,
    "explanation": "Az Árpád-kor 1000-től 1301-ig tartott.",
    "teaches": ["Arpad-kor", "dinasztia"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex02",
    "type": "fill-blank",
    "title": "Aranybulla éve",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "II. András király ___ adta ki az Aranybullát Székesfehérváron.",
    "correctAnswer": "1222-ben",
    "options": ["1222-ben", "1000-ben", "1526-ban", "1848-ban"],
    "teaches": ["Aranybulla"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex03",
    "type": "sentence-builder",
    "title": "Horvát-magyar unió",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Szent", "László", "1091-ben", "megteremtette", "a", "horvát-magyar", "perszonáluniót."],
    "correctSentence": "Szent László 1091-ben megteremtette a horvát-magyar perszonáluniót.",
    "english": "Saint Ladislaus created the Croatian-Hungarian personal union in 1091.",
    "teaches": ["perszonalunio", "lovagkiraly"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex04",
    "type": "multiple-choice",
    "title": "Ellenállási jog",
    "instruction": "Mit rögzített az Aranybulla 31. pontja?",
    "question": "Mi az ellenállási záradék lényege?",
    "options": ["A nemesek joga a törvényszegő királlyal szembeni fegyveres ellenállásra", "A teljes paraszti adómentesség", "Minden vár lebontása", "A királyi korona külföldi eladása"],
    "correctIndex": 0,
    "explanation": "Az ellenállási záradék garantálta az alkotmányos jogok fegyveres védelmét.",
    "teaches": ["ellenallasi-zaradek", "alkotmanyossag"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex05",
    "type": "fill-blank",
    "title": "Könyves Kálmán boszorkánytörvénye",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Könyves Kálmán kimondta, hogy boszorkányok nem ___.",
    "correctAnswer": "léteznek",
    "options": ["léteznek", "alszanak", "repülnek", "főznek"],
    "teaches": ["felvilagosult", "muveltseg"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex06",
    "type": "sentence-builder",
    "title": "Királyi kancellária",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["III.", "Béla", "bevezette", "a", "kötelező", "írásbeli", "ügyintézést."],
    "correctSentence": "III. Béla bevezette a kötelező írásbeli ügyintézést.",
    "english": "Béla III introduced mandatory written administration.",
    "teaches": ["kancellaria", "irasbeliseg"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex07",
    "type": "multiple-choice",
    "title": "Szent Erzsébet",
    "instruction": "Melyik erényéről ismert Árpád-házi Szent Erzsébet?",
    "question": "Mely nemes cselekedetéről híres Szent Erzsébet?",
    "options": ["A szegények és betegek önfeláldozó karitatív segítéséről", "Hatalmas adók kivetéséről", "Várak ostromlásáról", "Lovas hadjáratok vezetéséről"],
    "correctIndex": 0,
    "explanation": "Szent Erzsébet a keresztény szeretet és caritas világhírű védőszentje.",
    "teaches": ["onfelaldozo", "karitativ", "vedoszent"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex08",
    "type": "fill-blank",
    "title": "Jáki apátság stílusa",
    "instruction": "Válaszd ki az építészeti stílust!",
    "sentence": "A jáki templom a magyarországi ___ stílusú építészet legszebb emléke.",
    "correctAnswer": "román",
    "options": ["román", "barokk", "gótikus", "modern"],
    "teaches": ["roman-stilus"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex09",
    "type": "sentence-builder",
    "title": "Az utolsó aranyágacska",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["III.", "András", "halálával", "1301-ben", "kihalt", "az", "Árpád-ház."],
    "correctSentence": "III. András halálával 1301-ben kihalt az Árpád-ház.",
    "english": "With the death of Andrew III in 1301, the Árpád Dynasty died out.",
    "teaches": ["utolso-aranyagacska", "kihal"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex10",
    "type": "multiple-choice",
    "title": "Tartományurak korszaka",
    "instruction": "Hogyan nevezték a 14. század elején önkényeskedő oligarchákat?",
    "question": "Mi volt a tartományurak gúnyneve?",
    "options": ["Kiskirályok (pl. Csák Máté)", "Polgármesterek", "Ispánok", "Szerzetesek"],
    "correctIndex": 0,
    "explanation": "A kiskirályok (tartományurak) magánhadseregekkel uralták az ország egyes részeit.",
    "teaches": ["kiskiraly", "tartomanyur"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex11",
    "type": "fill-blank",
    "title": "Adómentesség rögzítése",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Az Aranybulla törvénybe iktatta a nemesek teljes ___.",
    "correctAnswer": "adómentességét",
    "options": ["adómentességét", "fizetését", "büntetését", "fogságát"],
    "teaches": ["adomentesseg", "szerviens"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex12",
    "type": "sentence-builder",
    "title": "Szent Margit imája",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["Szent", "Margit", "a", "kolostorban", "imádkozott", "az", "országért."],
    "correctSentence": "Szent Margit a kolostorban imádkozott az országért.",
    "english": "Saint Margaret prayed for the country in the convent.",
    "teaches": ["kolostor", "domonkos"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex13",
    "type": "multiple-choice",
    "title": "Vonatkozó névmás (amely)",
    "instruction": "Válaszd ki a helyes névmást!",
    "question": "Az Aranybulla az az oklevél, ___ megalapozta a nemesi jogokat.",
    "options": ["amely", "aki", "ahol", "amikor"],
    "correctIndex": 0,
    "explanation": "Tárgyakra és jogi fogalmakra az 'amely' névmást használjuk.",
    "teaches": ["alkotmanyossag"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex14",
    "type": "fill-blank",
    "title": "Szent László szigora",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "I. László szigorú törvényekkel védte a belső békét és a ___.",
    "correctAnswer": "közbiztonságot",
    "options": ["közbiztonságot", "tengerpartot", "autópályát", "időjárást"],
    "teaches": ["kozbiztonsag", "szigor"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex15",
    "type": "sentence-builder",
    "title": "Helyhatározói vonatkozó (ahol)",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Székesfehérvár", "volt", "a", "város,", "ahol", "kiadták", "az", "Aranybullát."],
    "correctSentence": "Székesfehérvár volt a város, ahol kiadták az Aranybullát.",
    "english": "Székesfehérvár was the city where they issued the Golden Bull.",
    "teaches": ["Aranybulla"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex16",
    "type": "multiple-choice",
    "title": "A szent királyok háza",
    "instruction": "Miért hívták az Árpád-házat a 'szent királyok nemzetségének'?",
    "question": "Hány szentet adott az Árpád-ház a kereszténységnek?",
    "options": ["Számos szentet és boldogot (István, Imre, László, Erzsébet, Margit)", "Csak egyetlen embert", "Egyet sem", "Több ezer névtelen katonát"],
    "correctIndex": 0,
    "explanation": "Az Árpád-dinasztia kivételesen sok szentet adott a katolikus egyháznak.",
    "teaches": ["nemzetseg", "kisugarzas"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex17",
    "type": "fill-blank",
    "title": "III. Béla vagyona",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A király jövedelmei az ezüst- és ___ származtak.",
    "correctAnswer": "sóbányászatból",
    "options": ["sóbányászatból", "űrhajózásból", "számítógépekből", "kávézásból"],
    "teaches": ["sobanyaszat", "jovedelem"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex18",
    "type": "sentence-builder",
    "title": "Törvényes ítélet",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["Senkit", "nem", "lehetett", "bírói", "ítélet", "nélkül", "elfogni."],
    "correctSentence": "Senkit nem lehetett bírói ítélet nélkül elfogni.",
    "english": "No one could be captured without a judicial verdict.",
    "teaches": ["itelet", "fogsag"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex19",
    "type": "multiple-choice",
    "title": "A dinasztia vége",
    "instruction": "Ki volt az Árpád-ház utolsó királya?",
    "question": "Ki hunyt el 1301-ben az Árpád-házi uralkodók közül?",
    "options": ["III. András", "IV. Béla", "Szent István", "Könyves Kálmán"],
    "correctIndex": 0,
    "explanation": "III. András volt az Árpád-ház utolsó férfiági királya.",
    "teaches": ["utolso-aranyagacska", "kihal"]
})
u5_cons_ex.append({
    "id": "b1-arpadhaz-consolidation.ex20",
    "type": "fill-blank",
    "title": "Háromszáz éves örökség",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Az Árpád-kor három évszázada szilárd európai alapot teremtett a magyar ___.",
    "correctAnswer": "államnak",
    "options": ["államnak", "autónak", "időjárásnak", "repülőgépnek"],
    "teaches": ["Arpad-kor", "alkotmanyossag"]
})

write_json(EXERCISES_DIR / "b1-arpadhaz-consolidation-ex.json", {"exercises": u5_cons_ex})

write_json(LESSONS_DIR / "b1-arpadhaz-consolidation.json", make_consolidation_lesson(
    "lesson.b1.arpadhaz-consolidation",
    "The Árpád Dynasty (1000–1301) - Consolidation",
    [
        "Congratulations on completing Unit 5 of the Hungarian Citizenship Track!",
        "In this unit, you have explored three hundred years of medieval statehood: the chivalric rule of Saint Ladislaus (*lovagkirály*) and union with Croatia (1091), the Golden Bull of 1222 (*Aranybulla*) establishing constitutional rights and the right of resistance, Coloman's enlightened laws, Béla III's chancellery and European power, the lineage of saints (Elizabeth, Margaret), and the close of the dynasty in 1301.",
        "Review your vocabulary and test your mastery across all 20 consolidation exercises."
    ],
    [
        "I can summarize the three centuries of the Árpád Dynasty (1000–1301) and its key monarchs.",
        "I can explain the constitutional principles of the 1222 Golden Bull (*Aranybulla*).",
        "I can describe the spiritual impact of Árpád-era saints (Saint Elizabeth, Saint Margaret).",
        "I can fluently construct complex relative clauses using *aki, amely, ahol, amikor*."
    ],
    "stories/world/b1/b1-arpadhaz.json",
    "exercises/b1/b1-arpadhaz-consolidation-ex.json",
    [f"b1-arpadhaz-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 5 (b1-arpadhaz) overhaul complete!")
