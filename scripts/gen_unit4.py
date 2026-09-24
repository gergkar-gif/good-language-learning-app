# -*- coding: utf-8 -*-
"""
Unit 4 Overhaul: Saint Stephen & the Founding of the State (1000) (b1-istvankiraly)
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
# Lesson 1: Géza fejedelem és Koppány leverése
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly-01-gezafejedelem.json", make_story(
    "story.b1.istvankiraly.01",
    "Géza fejedelem öröksége és a hatalom megszilárdítása",
    "Grand Prince Géza's western diplomacy, baptism of his son Vajk (Stephen), marriage with Bavarian Princess Gizella, and Stephen's victory over pagan rebel Koppány at Veszprém.",
    "Esztergom és Veszprém",
    ["folyamatos és befejezett melléknévi igenevek címszavakban"],
    ["Géza fejedelem", "Koppány felkelése", "Primogenitúra"],
    [
        "A 10. század végén Géza fejedelem békét kötött a Német-Római Birodalommal, és nyugati keresztény hittérítőket hívott Esztergomba. Fiát, Vajkot megkereszteltette, aki a keresztségben az István nevet kapta.",
        "Géza dinasztikus házasságot szervezett: István feleségül vette Gizella bajor hercegnőt. Gizellával német lovagok (Vecellin, Hont, Pázmány) és mesteremberek érkeztek Magyarországra.",
        "Géza 997-ben bekövetkezett halála után trónviszály tört ki. A somogyi pogány fejedelem, Koppány az ősi sztyeppei öröklési rend, a szeniorátus (a nemzetség legidősebb férfi tagjának joga) alapján követelte a hatalmat és Géza özvegyének kezét.",
        "István a keresztény és európai elvet, az elsőszülött fiú öröklési jogát (primogenitúra) képviselte.",
        "A Veszprém melletti sorsdöntő csatában István a német nehézlovagok és hűséges magyar harcosai segítségével legyőzte Koppányt, megszilárdítva az egyszemélyi uralmat az egész országban."
    ],
    [
        {"lemma": "megkeresztel", "pos": "verb", "cefr": "B1", "gloss": "to baptize"},
        {"lemma": "szeniorátus", "pos": "noun", "cefr": "B1", "gloss": "senioratus (oldest male succession)"},
        {"lemma": "primogenitúra", "pos": "noun", "cefr": "B1", "gloss": "primogeniture (firstborn male succession)"},
        {"lemma": "megszilárdít", "pos": "verb", "cefr": "B1", "gloss": "to consolidate / solidify"}
    ],
    [
        {
            "question": "Milyen elv alapján követelte Koppány a hatalmat Géza fejedelem halála után?",
            "options": ["A szeniorátus (a nemzetség legidősebb férfi tagjának joga) alapján", "A primogenitúra (elsőszülöttségi jog) alapján", "Demokratikus népszavazás alapján", "A pápa kijelölése alapján"],
            "correctIndex": 0,
            "explanation": "Koppány az ősi pogány szeniorátus elve alapján tartott igényt a trónra."
        },
        {
            "question": "Ki volt István király bajor származású felesége?",
            "options": ["Gizella bajor hercegnő", "Árpád-házi Szent Erzsébet", "Anjou Mária", "Mária Terézia"],
            "correctIndex": 0,
            "explanation": "István Gizella bajor hercegnőt vette feleségül, aki keresztény kultúrát és lovagokat hozott az országba."
        },
        {
            "question": "Hol győzte le István Koppány lázadó seregeit 997-ben?",
            "options": ["Veszprém mellett", "A tatár pusztákon", "Pozsony várában", "A Balaton jegén"],
            "correctIndex": 0,
            "explanation": "István seregei Veszprém közelében arattak sorsdöntő győzelmet Koppány felett."
        }
    ]
))

write_json(VOCAB_DIR / "b1-istvankiraly-01-voc.json", {
    "title": "Géza fejedelem öröksége és Koppány leverése",
    "words": [
        {"lemma": "megkeresztel", "pos": "verb", "cefr": "B1", "translation": "to baptize", "examples": [{"hungarian": "Vajkot Szent István névre keresztelték meg.", "english": "Vajk was baptized under the name of Saint Stephen."}]},
        {"lemma": "trónviszály", "pos": "noun", "cefr": "B1", "translation": "throne dispute / succession conflict", "examples": [{"hungarian": "A trónviszály véres harcokhoz vezetett.", "english": "The succession conflict led to bloody battles."}]},
        {"lemma": "szeniorátus", "pos": "noun", "cefr": "B1", "translation": "seniorate (succession by oldest male)", "examples": [{"hungarian": "Koppány a szeniorátus jogára hivatkozott.", "english": "Koppány appealed to the right of the seniorate."}]},
        {"lemma": "primogenitúra", "pos": "noun", "cefr": "B1", "translation": "primogeniture (inheritance by firstborn)", "examples": [{"hungarian": "A primogenitúra biztosította az apa-fiú öröklést.", "english": "Primogeniture ensured father-to-son inheritance."}]},
        {"lemma": "lovag", "pos": "noun", "cefr": "B1", "translation": "knight", "examples": [{"hungarian": "Német lovagok harcoltak István oldalán.", "english": "German knights fought on Stephen's side."}]},
        {"lemma": "megszilárdít", "pos": "verb", "cefr": "B1", "translation": "to solidify / consolidate", "examples": [{"hungarian": "István megszilárdította a központi királyi hatalmat.", "english": "Stephen consolidated central royal power."}]},
        {"lemma": "hittérítő", "pos": "noun", "cefr": "B1", "translation": "missionary", "examples": [{"hungarian": "Nyugati hittérítők érkeztek az országba.", "english": "Western missionaries arrived in the country."}]},
        {"lemma": "pogány", "pos": "adj", "cefr": "B1", "translation": "pagan / heathen", "examples": [{"hungarian": "A pogány lázadók nem fogadták el az új törvényeket.", "english": "The pagan rebels did not accept the new laws."}]},
        {"lemma": "hadsereg", "pos": "noun", "cefr": "B1", "translation": "army", "examples": [{"hungarian": "A királyi hadsereg legyőzte a lázadókat.", "english": "The royal army defeated the rebels."}]},
        {"lemma": "öröklési rend", "pos": "noun", "cefr": "B1", "translation": "order of succession", "examples": [{"hungarian": "Az európai öröklési rend szerint a legidősebb fiú örököl.", "english": "According to European order of succession, the eldest son inherits."}]},
        {"lemma": "dinasztikus", "pos": "adj", "cefr": "B1", "translation": "dynastic", "examples": [{"hungarian": "A dinasztikus házasság megerősítette a békét.", "english": "The dynastic marriage strengthened peace."}]},
        {"lemma": "sorsdöntő", "pos": "adj", "cefr": "B1", "translation": "decisive / fateful", "examples": [{"hungarian": "A veszprémi csata sorsdöntő győzelmet hozott.", "english": "The battle of Veszprém brought a decisive victory."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-istvankiraly-01-igenev-cim-gr.json", {
    "title": "Melléknévi igenevek használata történelmi címekben és leírásokban",
    "level": "B1",
    "rules": [
        {
            "id": "participles-titles",
            "title": "Participles in Historical Descriptions",
            "text": "Past participles (*-t / -tt*) and present participles (*-ó / -ő*) form dense, informative descriptions: *a megkeresztelt fejedelem* (the baptized prince), *a lázadó vezér* (the rebelling chieftain), *a bekövetkezett halál* (the occurred death).",
            "tip": "They function as descriptive adjectives and precede the noun."
        },
        {
            "id": "causal-alapjan",
            "title": "Expressing Legal Basis with 'alapján'",
            "text": "The postposition *alapján* (on the basis of / according to) follows nouns: *a törvény alapján* (on the basis of the law), *a szeniorátus elve alapján* (according to the principle of senioratus).",
            "tip": "Use this structure in citizenship legal topics."
        }
    ],
    "examples": [
        {"spanish": "A primogenitúra elve alapján István örökölte a fejedelmi hatalmat.", "english": "On the basis of primogeniture, Stephen inherited the princely power."},
        {"spanish": "A Veszprém mellett vívott csatában győzött a király.", "english": "In the battle fought near Veszprém, the king won."},
        {"spanish": "A Gizellával érkező lovagok segítették a győzelmet.", "english": "The knights arriving with Gisela aided the victory."}
    ]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-01-ex.json", {
    "exercises": [
        {
            "id": "b1-istvankiraly-01.ex01",
            "type": "multiple-choice",
            "title": "István eredeti neve",
            "instruction": "Hogyan hívták István királyt a megkeresztelése előtt?",
            "question": "Mi volt Szent István pogány neve?",
            "options": ["Vajk", "Koppány", "Taksony", "Álmos"],
            "correctIndex": 0,
            "explanation": "István eredeti, születési neve Vajk volt, mielőtt megkeresztelkedett volna.",
            "teaches": ["megkeresztel", "dinasztikus"]
        },
        {
            "id": "b1-istvankiraly-01.ex02",
            "type": "fill-blank",
            "title": "Trónöröklési elvek",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "István az európai keresztény elvet, az elsőszülöttségi ___ (primogenitúrát) képviselte.",
            "correctAnswer": "öröklést",
            "options": ["öröklést", "vásárlást", "kereskedelmet", "játékot"],
            "teaches": ["primogenitura", "oroklesi-rend"]
        },
        {
            "id": "b1-istvankiraly-01.ex03",
            "type": "sentence-builder",
            "title": "A veszprémi diadal",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["István", "Veszprém", "mellett", "legyőzte", "Koppány", "lázadó", "seregét."],
            "correctSentence": "István Veszprém mellett legyőzte Koppány lázadó seregét.",
            "english": "Stephen defeated Koppány's rebelling army near Veszprém.",
            "teaches": ["pogany", "sorsdonto"]
        },
        {
            "id": "b1-istvankiraly-01.ex04",
            "type": "multiple-choice",
            "title": "Koppány elve",
            "instruction": "Mire hivatkozott Koppány a hatalom megszerzéséért?",
            "question": "Mit jelent a szeniorátus fogalma?",
            "options": ["A nemzetség legidősebb élő férfi tagjának öröklési jogát", "A legfiatalabb gyermek öröklését", "A választott parlament döntését", "A római császár ajándékát"],
            "correctIndex": 0,
            "explanation": "A szeniorátus a család legidősebb férfi tagjának biztosította a vezetést a nomád hagyományban.",
            "teaches": ["szenioratus", "tronviszaly"]
        },
        {
            "id": "b1-istvankiraly-01.ex05",
            "type": "fill-blank",
            "title": "Bajor hercegnő",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "István felesége, ___ bajor hercegnő segítette a keresztény kultúra elterjedését.",
            "correctAnswer": "Gizella",
            "options": ["Gizella", "Erzsébet", "Katalin", "Mária"],
            "teaches": ["dinasztikus", "lovag"]
        },
        {
            "id": "b1-istvankiraly-01.ex06",
            "type": "sentence-builder",
            "title": "A jog alapján (alapján)",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "törvény", "alapján", "István", "volt", "a", "jogos", "örökös."],
            "correctSentence": "A törvény alapján István volt a jogos örökös.",
            "english": "On the basis of the law, Stephen was the legitimate heir.",
            "teaches": ["oroklesi-rend", "megszilardit"]
        },
        {
            "id": "b1-istvankiraly-01.ex07",
            "type": "multiple-choice",
            "title": "Géza fejedelem diplomáciája",
            "instruction": "Hogyan készítette elő Géza fejedelem a keresztény királyságot?",
            "question": "Mit tett Géza fejedelem a békéért?",
            "options": ["Nyugati hittérítőket hívott és dinasztikus házasságot kötött a fiának", "Minden várost felgyújtott", "Megtiltotta a magyar nyelv használatát", "Elhagyta az országot"],
            "correctIndex": 0,
            "explanation": "Géza nyugati kapcsolatokat épített, hittérítőket hívott és bajor hercegnőt kért fia feleségéül.",
            "teaches": ["hitterito", "dinasztikus"]
        },
        {
            "id": "b1-istvankiraly-01.ex08",
            "type": "fill-blank",
            "title": "Hatalom megszilárdítása",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A veszprémi győzelem után István ___ a központi királyi hatalmat.",
            "correctAnswer": "megszilárdította",
            "options": ["megszilárdította", "elvesztette", "eladta", "elfelejtette"],
            "teaches": ["megszilardit"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-istvankiraly-01.json", make_lesson(
    "lesson.b1.istvankiraly-01",
    "Géza fejedelem és Koppány leverése (Géza & Victory over Koppány)",
    "Melléknévi igenevek használata történelmi címekben és leírásokban",
    [
        "Welcome to Unit 4 of the Hungarian Citizenship Track, focusing on Saint Stephen (*Szent István*), the founder of the Christian Hungarian state in 1000.",
        "In this first lesson, we explore the transition from Grand Prince Géza to Stephen (Vajk), his marriage to Bavarian Princess Gisela, and the decisive battle against pagan chieftain Koppány at Veszprém over succession rights (*szeniorátus* vs. *primogenitúra*).",
        "We also practice participles in titles and the postposition *alapján* (on the basis of)."
    ],
    [
        "I can describe the succession conflict between Stephen and Koppány (*primogenitúra* vs. *szeniorátus*).",
        "I can explain Grand Prince Géza's western diplomatic opening and the role of Princess Gisela.",
        "I can locate the decisive battle of Veszprém (997).",
        "I can use participles and *alapján* correctly in formal B1 historical sentences."
    ],
    "stories/world/b1/b1-istvankiraly-01-gezafejedelem.json",
    "vocabulary/b1/b1-istvankiraly-01-voc.json",
    "grammar/b1/b1-istvankiraly-01-igenev-cim-gr.json",
    "exercises/b1/b1-istvankiraly-01-ex.json",
    [f"b1-istvankiraly-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: A királyi koronázás (1000/1001)
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly-02-koronazas.json", make_story(
    "story.b1.istvankiraly.02",
    "A királyi koronázás és a Magyar Királyság születése (1000)",
    "The coronation of Saint Stephen on Christmas 1000 / New Year's Day 1001 with the crown sent by Pope Sylvester II and supported by Holy Roman Emperor Otto III, establishing a sovereign apostolic kingdom.",
    "Esztergom és Székesfehérvár",
    ["múlt idejű passzív kifejezések és állapothatározók"],
    ["Koronázás 1000", "II. Szilveszter pápa", "Aposztoli királyság"],
    [
        "1000 karácsonyán (vagy 1001. január 1-jén) történelmi esemény zajlott Esztergomban: István fejedelmet Magyarország első királyává koronázták.",
        "A koronát II. Szilveszter pápa küldte Rómából Asztrik apát közvetítésével, III. Ottó német-római császár egyetértésével és támogatásával.",
        "A pápai korona elfogadása óriási diplomáciai siker volt: Magyarország önálló, szuverén keresztény királysággá vált, anélkül hogy a német császár hűbéresévé süllyedt volna.",
        "István elnyerte az 'apostoli király' címet, ami felhatalmazta őt önálló egyházmegyék alapítására és püspökök kinevezésére.",
        "A koronázással Magyarország végleg belépett a keresztény európai népek közösségébe, megalapozva a több mint ezeréves magyar államiságot."
    ],
    [
        {"lemma": "koronázás", "pos": "noun", "cefr": "B1", "gloss": "coronation"},
        {"lemma": "szuverén", "pos": "adj", "cefr": "B1", "gloss": "sovereign / independent"},
        {"lemma": "apostoli király", "pos": "noun", "cefr": "B1", "gloss": "apostolic king"},
        {"lemma": "államiság", "pos": "noun", "cefr": "B1", "gloss": "statehood"}
    ],
    [
        {
            "question": "Mikor és melyik pápától kapta a koronát I. István király?",
            "options": ["1000 karácsonyán / 1001-ben II. Szilveszter pápától", "1526-ban a török szultántól", "1848-ban a Habsburg császártól", "895-ben a frank királytól"],
            "correctIndex": 0,
            "explanation": "Istvánt 1000/1001 fordulóján koronázták meg a II. Szilveszter pápa által küldött koronával."
        },
        {
            "question": "Miért volt döntő fontosságú, hogy a korona Rómából, a pápától érkezett?",
            "options": ["Mert biztosította az ország szuverenitását és függetlenségét a német császártól", "Mert a pápa ingyen adta a koronát", "Mert kötelező volt minden évben visszaküldeni", "Mert csak a pápa tudott aranyat készíteni"],
            "correctIndex": 0,
            "explanation": "A közvetlen pápai korona független európai királysággá tette Magyarországot, elkerülve a császári hűbéri függőséget."
        },
        {
            "question": "Milyen különleges jogot jelentett az 'apostoli király' cím?",
            "options": ["Jogot önálló egyházmegyék alapítására és püspökök kinevezésére", "Jogot más országok kötelező megkeresztelésére", "Korlátlan aranybányászatot Rómában", "Minden adó eltörlését"],
            "correctIndex": 0,
            "explanation": "Az apostoli királyi jogkör biztosította az önálló magyar egyházszervezet felépítését."
        }
    ]
))

write_json(VOCAB_DIR / "b1-istvankiraly-02-voc.json", {
    "title": "A királyi koronázás és a Magyar Királyság születése",
    "words": [
        {"lemma": "koronázás", "pos": "noun", "cefr": "B1", "translation": "coronation", "examples": [{"hungarian": "A koronázás 1000 karácsonyán történt.", "english": "The coronation took place on Christmas 1000."}]},
        {"lemma": "szuverén", "pos": "adj", "cefr": "B1", "translation": "sovereign / independent", "examples": [{"hungarian": "Magyarország szuverén európai királysággá vált.", "english": "Hungary became a sovereign European kingdom."}]},
        {"lemma": "apostoli király", "pos": "noun", "cefr": "B1", "translation": "apostolic king", "examples": [{"hungarian": "István elnyerte az apostoli király címet.", "english": "Stephen earned the title of apostolic king."}]},
        {"lemma": "államiság", "pos": "noun", "cefr": "B1", "translation": "statehood", "examples": [{"hungarian": "A koronázással megszületett a magyar államiság.", "english": "With the coronation, Hungarian statehood was born."}]},
        {"lemma": "felhatalmaz", "pos": "verb", "cefr": "B1", "translation": "to authorize / empower", "examples": [{"hungarian": "A pápa felhatalmazta a királyt az egyházszervezésre.", "english": "The Pope authorized the king to organize the church."}]},
        {"lemma": "közvetítés", "pos": "noun", "cefr": "B1", "translation": "mediation", "examples": [{"hungarian": "Asztrik apát közvetítésével érkezett a korona.", "english": "The crown arrived through the mediation of Abbot Astrik."}]},
        {"lemma": "hűbéri függés", "pos": "noun", "cefr": "B1", "translation": "feudal vassalage / dependency", "examples": [{"hungarian": "Elkerülték a német császárnak való hűbéri függést.", "english": "They avoided feudal dependency on the German emperor."}]},
        {"lemma": "egyházmegye", "pos": "noun", "cefr": "B1", "translation": "diocese", "examples": [{"hungarian": "Tíz egyházmegyét alapított a király.", "english": "The king founded ten dioceses."}]},
        {"lemma": "püspök", "pos": "noun", "cefr": "B1", "translation": "bishop", "examples": [{"hungarian": "A püspökök vezették a helyi egyházi intézményeket.", "english": "The bishops led the local church institutions."}]},
        {"lemma": "méltóság", "pos": "noun", "cefr": "B1", "translation": "dignity / office", "examples": [{"hungarian": "A királyi méltóság szakrális tiszteletet élvezett.", "english": "The royal dignity enjoyed sacred respect."}]},
        {"lemma": "egyetértés", "pos": "noun", "cefr": "B1", "translation": "agreement / consent", "examples": [{"hungarian": "A császár egyetértésével küldték a koronát.", "english": "The crown was sent with the Emperor's consent."}]},
        {"lemma": "belépés", "pos": "noun", "cefr": "B1", "translation": "entry / accession", "examples": [{"hungarian": "Ez jelentette a belépést az európai nemzetek közé.", "english": "This signified entry into the community of European nations."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-istvankiraly-02-koronazott-kiraly-gr.json", {
    "title": "Múlt idejű passzív és állapothatározói szerkezetek",
    "level": "B1",
    "rules": [
        {
            "id": "passive-state-expressions",
            "title": "Describing Historical States (koronázták, lett alapítva)",
            "text": "Hungarian prefers active 3rd person plural for passive events: *Istvánt királlyá koronázták* (They crowned Stephen king = Stephen was crowned king). Alternatively, past participles express established status: *a megkoronázott király* (the crowned king).",
            "tip": "Use *-vá / -vé* for transformation: *királlyá választották / koronázták*."
        },
        {
            "id": "translative-case",
            "title": "Translative Case (-vá / -vé) for Roles and Ranks",
            "text": "When someone becomes something or is made into a title, use *-vá / -vé*: *király-lyá*, *érsek-ké*, *szent-té*. Assimilates to final consonants: *szent + vé = szentté*.",
            "tip": "Example: *Szentté avatták 1083-ban.* (He was canonized in 1083.)"
        }
    ],
    "examples": [
        {"spanish": "Istvánt 1000 karácsonyán királlyá koronázták.", "english": "Stephen was crowned king on Christmas 1000."},
        {"spanish": "Magyarország független keresztény állammá vált.", "english": "Hungary became an independent Christian state."},
        {"spanish": "Asztrik apátot érsekké nevezték ki.", "english": "Abbot Astrik was appointed archbishop."}
    ]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-02-ex.json", {
    "exercises": [
        {
            "id": "b1-istvankiraly-02.ex01",
            "type": "multiple-choice",
            "title": "A koronázás éve",
            "instruction": "Melyik évben koronázták meg I. István királyt?",
            "question": "Mikor jött létre a keresztény Magyar Királyság?",
            "options": ["1000 karácsonyán / 1001. január 1-jén", "895-ben", "1222-ben", "1526-ban"],
            "correctIndex": 0,
            "explanation": "Szent István megkoronázása 1000/1001 fordulóján történt.",
            "teaches": ["koronazas", "allamisag"]
        },
        {
            "id": "b1-istvankiraly-02.ex02",
            "type": "fill-blank",
            "title": "A korona küldője",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A koronát II. ___ pápa küldte Rómából Asztrik apát közvetítésével.",
            "correctAnswer": "Szilveszter",
            "options": ["Szilveszter", "Gergely", "János", "Orbán"],
            "teaches": ["koronazas", "kozvetites"]
        },
        {
            "id": "b1-istvankiraly-02.ex03",
            "type": "sentence-builder",
            "title": "Királyi koronázás",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Istvánt", "Magyarország", "első", "keresztény", "királyává", "koronázták."],
            "correctSentence": "Istvánt Magyarország első keresztény királyává koronázták.",
            "english": "Stephen was crowned the first Christian king of Hungary.",
            "teaches": ["koronazas", "szuveren"]
        },
        {
            "id": "b1-istvankiraly-02.ex04",
            "type": "multiple-choice",
            "title": "Függetlenség és szuverenitás",
            "instruction": "Mit jelentett a pápai korona Magyarország számára?",
            "question": "Milyen jogi státuszt biztosított a közvetlen pápai elismerés?",
            "options": ["Szuverén, független európai királyságot a német hűbériség helyett", "A német császár teljes uralmát", "A Kárpát-medence átadását Rómának", "Minden fegyver azonnali beszolgáltatását"],
            "correctIndex": 0,
            "explanation": "A pápától kapott korona független, szuverén európai királysággá emelte Magyarországot.",
            "teaches": ["szuveren", "huberi-fugges"]
        },
        {
            "id": "b1-istvankiraly-02.ex05",
            "type": "fill-blank",
            "title": "Aposztoli jogkör",
            "instruction": "Válaszd ki a helyes kifejezést!",
            "sentence": "István elnyerte az '___ király' címet, amely felhatalmazta egyházmegyék alapítására.",
            "correctAnswer": "apostoli",
            "options": ["apostoli", "tengeri", "császári", "hadvezér"],
            "teaches": ["apostoli-kiraly", "felhatalmaz"]
        },
        {
            "id": "b1-istvankiraly-02.ex06",
            "type": "sentence-builder",
            "title": "Európai integráció",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Magyarország", "belépett", "a", "keresztény", "európai", "államok", "közösségébe."],
            "correctSentence": "Magyarország belépett a keresztény európai államok közösségébe.",
            "english": "Hungary entered the community of Christian European states.",
            "teaches": ["belepes", "allamisag"]
        },
        {
            "id": "b1-istvankiraly-02.ex07",
            "type": "multiple-choice",
            "title": "Asztrik apát szerepe",
            "instruction": "Ki volt Asztrik apát?",
            "question": "Milyen feladatot teljesített Asztrik követsége?",
            "options": ["Elhozta a pápai koronát és áldást Rómából", "Hadat üzent a német császárnak", "Megépítette a budai várat", "Megírta a magyar alkotmányt 1989-ben"],
            "correctIndex": 0,
            "explanation": "Asztrik apát vezette a római követséget és hozta el a pápai koronát.",
            "teaches": ["kozvetites"]
        },
        {
            "id": "b1-istvankiraly-02.ex08",
            "type": "fill-blank",
            "title": "Államiság alapjai",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A koronázás megalapozta a több mint ezeréves magyar ___.",
            "correctAnswer": "államiságot",
            "options": ["államiságot", "vasutat", "időjárást", "repülést"],
            "teaches": ["allamisag"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-istvankiraly-02.json", make_lesson(
    "lesson.b1.istvankiraly-02",
    "A királyi koronázás (The Royal Coronation - 1000)",
    "Múlt idejű passzív és állapothatározói szerkezetek",
    [
        "In this second lesson, we study the milestone event of Christmas 1000 / New Year 1001: the royal coronation of Saint Stephen.",
        "You will learn about Pope Sylvester II, Abbot Astrik, the title of 'Apostolic King' (*apostoli király*), and the diplomatic significance of achieving sovereign European statehood independent of the Holy Roman Empire.",
        "We also practice the translative case (*-vá / -vé: királlyá koronázták*) and passive descriptive structures."
    ],
    [
        "I can state the date and historical meaning of Saint Stephen's coronation (1000/1001).",
        "I can explain why the papal crown from Sylvester II protected Hungary's sovereign independence.",
        "I can define the privileges associated with the title *apostoli király*.",
        "I can apply the translative suffix *-vá / -vé* to express ranks and transitions."
    ],
    "stories/world/b1/b1-istvankiraly-02-koronazas.json",
    "vocabulary/b1/b1-istvankiraly-02-voc.json",
    "grammar/b1/b1-istvankiraly-02-koronazott-kiraly-gr.json",
    "exercises/b1/b1-istvankiraly-02-ex.json",
    [f"b1-istvankiraly-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: Államszervezet és egyházszervezet
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly-03-keresztenykiralysag.json", make_story(
    "story.b1.istvankiraly.03",
    "Vármegyék, püspökségek és a tized törvénye",
    "Building the kingdom: 10 dioceses (Esztergom & Kalocsa archdioceses), Pannonhalma Abbey, the royal county system (*vármegyék*) led by ispáns, and mandatory church construction ('every 10 villages shall build a church').",
    "Esztergom, Pannonhalma és Székesfehérvár",
    ["számnévi kifejezések és kötelezettséget kifejező igék"],
    ["Vármegyerendszer", "Ispánok", "Egyházmegyék", "Tized és templomépítés"],
    [
        "A koronázás után I. István zseniális szervezőmunkával létrehozta a Magyar Királyság közigazgatási és egyházi struktúráját, amely évszázadokon át fennmaradt.",
        "Egyházi téren tíz püspökséget alapított: Esztergomot és Kalocsát érseki rangra emelte, biztosítva a magyar katolikus egyház teljes függetlenségét a német érsekektől. Pannonhalmán megalapította az első bencés apátságot.",
        "Világi téren az ország területét királyi vármegyékre osztotta. Minden vármegye élére egy királyi tisztviselőt, az ispánt állította, aki beszedte az adókat, bíráskodott, és vezette a vármegyei hadsereget.",
        "István törvényei szigorúan védték a keresztény vallást és a magántulajdont: elrendelte, hogy minden tíz falu köteles egy templomot építeni és felszerelni.",
        "Bevezette a tizedet (decima), vagyis a termés egytizedének egyházi adóját, amely biztosította a papok és a templomok anyagi fenntartását."
    ],
    [
        {"lemma": "vármegye", "pos": "noun", "cefr": "B1", "gloss": "county (historic & modern Hungarian administrative unit)"},
        {"lemma": "ispán", "pos": "noun", "cefr": "B1", "gloss": "count / head of county (historic royal bailiff)"},
        {"lemma": "érsekség", "pos": "noun", "cefr": "B1", "gloss": "archdiocese"},
        {"lemma": "tized", "pos": "noun", "cefr": "B1", "gloss": "tithe (10% ecclesiastical tax)"}
    ],
    [
        {
            "question": "Hány egyházmegyét alapított Szent István király Magyarországon?",
            "options": ["Tíz egyházmegyét (köztük Esztergom és Kalocsa érsekségét)", "Száz egyházmegyét", "Csak egyetlen kis kápolnát", "Ötven püspökséget"],
            "correctIndex": 0,
            "explanation": "István 10 egyházmegyét hozott létre, Esztergomot és Kalocsát érseki székhellyé téve."
        },
        {
            "question": "Ki vezette a királyi vármegyéket Szent István korában?",
            "options": ["Az ispán", "A polgármester", "A kende", "A törzsfőnök"],
            "correctIndex": 0,
            "explanation": "A királyi vármegye élén a király által kinevezett ispán állt."
        },
        {
            "question": "Milyen híres törvényt hozott István a templomok építéséről?",
            "options": ["Minden tíz falu köteles egy templomot építeni", "Tilos templomot építeni kőből", "Minden városban tíz templomnak kell állnia", "Csak a hegycsúcsokon lehet misézni"],
            "correctIndex": 0,
            "explanation": "István törvénye előírta, hogy minden 10 falunak közösen egy templomot kell építenie és fenntartania."
        }
    ]
))

write_json(VOCAB_DIR / "b1-istvankiraly-03-voc.json", {
    "title": "Vármegyék, püspökségek és a tized törvénye",
    "words": [
        {"lemma": "vármegye", "pos": "noun", "cefr": "B1", "translation": "county", "examples": [{"hungarian": "A királyi vármegye a közigazgatás alapköve volt.", "english": "The royal county was the cornerstone of public administration."}]},
        {"lemma": "ispán", "pos": "noun", "cefr": "B1", "translation": "head of county / bailiff", "examples": [{"hungarian": "Az ispán vezette a vármegye hadait és szedte be az adót.", "english": "The ispán led the county's troops and collected taxes."}]},
        {"lemma": "érsekség", "pos": "noun", "cefr": "B1", "translation": "archdiocese", "examples": [{"hungarian": "Esztergom lett a magyar egyház első érseksége.", "english": "Esztergom became the first archdiocese of the Hungarian church."}]},
        {"lemma": "apátság", "pos": "noun", "cefr": "B1", "translation": "abbey", "examples": [{"hungarian": "A Pannonhalmi Főapátság ma is működik.", "english": "The Pannonhalma Archabbey is still functioning today."}]},
        {"lemma": "tized", "pos": "noun", "cefr": "B1", "translation": "tithe", "examples": [{"hungarian": "A tized a termés egytized részének befizetését jelentette.", "english": "The tithe meant the payment of one-tenth of the harvest."}]},
        {"lemma": "magántulajdon", "pos": "noun", "cefr": "B1", "translation": "private property", "examples": [{"hungarian": "István törvényei szigorúan védték a magántulajdont.", "english": "Stephen's laws strictly protected private property."}]},
        {"lemma": "tisztviselő", "pos": "noun", "cefr": "B1", "translation": "official / officer", "examples": [{"hungarian": "A királyi tisztviselők feleltek a rendért.", "english": "Royal officials were responsible for order."}]},
        {"lemma": "bíráskodik", "pos": "verb", "cefr": "B1", "translation": "to administer justice / judge", "examples": [{"hungarian": "A várban az ispán bíráskodott a vitás ügyekben.", "english": "In the castle, the ispán judged in disputed matters."}]},
        {"lemma": "elrendel", "pos": "verb", "cefr": "B1", "translation": "to decree / order", "examples": [{"hungarian": "A király elrendelte a templomépítést.", "english": "The king ordered the construction of churches."}]},
        {"lemma": "fenntartás", "pos": "noun", "cefr": "B1", "translation": "maintenance / upkeep", "examples": [{"hungarian": "A tized az egyház fenntartását szolgálta.", "english": "The tithe served the upkeep of the church."}]},
        {"lemma": "szervezőmunka", "pos": "noun", "cefr": "B1", "translation": "organizational work", "examples": [{"hungarian": "Hatalmas szervezőmunka hozta létre az államot.", "english": "Immense organizational work created the state."}]},
        {"lemma": "bencés", "pos": "adj", "cefr": "B1", "translation": "Benedictine", "examples": [{"hungarian": "A bencés szerzetesek tanítottak és gyógyítottak.", "english": "Benedictine monks taught and healed."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-istvankiraly-03-alapitott-intezmenyek-gr.json", {
    "title": "Számnévi szerkezetek és kötelezettséget kifejező igék (kell, köteles)",
    "level": "B1",
    "rules": [
        {
            "id": "obligation-modal-verbs",
            "title": "Expressing Obligation with 'köteles' and 'kell'",
            "text": "Laws and duties use *köteles + infinitív* (obliged to do): *Minden tíz falu köteles templomot építeni.* (Every ten villages are obliged to build a church.) Or *kell + datív + inf.*: *Mindenkinek tizedet kell fizetnie.* (Everyone must pay a tithe.)",
            "tip": "Useful in both historical laws and modern constitutional obligations."
        },
        {
            "id": "numeral-singular-noun",
            "title": "Singular Nouns After Hungarian Numbers",
            "text": "Remember: in Hungarian, all nouns following numbers or quantity words take the **singular** form: *tíz falu* (not *falvak*), *tíz egyházmegye*, *minden vármegye*.",
            "tip": "Golden rule of Hungarian grammar tested in all CEFR levels."
        }
    ],
    "examples": [
        {"spanish": "Minden tíz falu köteles egy templomot építeni.", "english": "Every ten villages are obliged to build a church."},
        {"spanish": "A földműveseknek tizedet kellett fizetniük a termésből.", "english": "The farmers had to pay a tithe from the harvest."},
        {"spanish": "Tíz egyházmegye jött létre az országban.", "english": "Ten dioceses came into being in the country."}
    ]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-03-ex.json", {
    "exercises": [
        {
            "id": "b1-istvankiraly-03.ex01",
            "type": "multiple-choice",
            "title": "Egyházmegyék száma",
            "instruction": "Hány egyházmegyét hozott létre Szent István?",
            "question": "Hány püspökséget és érsekséget alapított István király?",
            "options": ["10 egyházmegyét (Esztergom és Kalocsa érsekségével)", "50 egyházmegyét", "2 egyházmegyét", "100 püspökséget"],
            "correctIndex": 0,
            "explanation": "Szent István 10 egyházmegyét alapított, köztük két érsekséget.",
            "teaches": ["ersekseg", "egyhazmegye"]
        },
        {
            "id": "b1-istvankiraly-03.ex02",
            "type": "fill-blank",
            "title": "A vármegye vezetője",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A királyi vármegye élén a király tisztviselője, az ___ állt.",
            "correctAnswer": "ispán",
            "options": ["ispán", "polgármester", "rendelet", "miniszter"],
            "teaches": ["ispan", "varmegye"]
        },
        {
            "id": "b1-istvankiraly-03.ex03",
            "type": "sentence-builder",
            "title": "Templomépítési törvény",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Minden", "tíz", "falu", "köteles", "egy", "templomot", "építeni."],
            "correctSentence": "Minden tíz falu köteles egy templomot építeni.",
            "english": "Every ten villages are obliged to build a church.",
            "teaches": ["elrendel"]
        },
        {
            "id": "b1-istvankiraly-03.ex04",
            "type": "multiple-choice",
            "title": "A tized fogalma",
            "instruction": "Mit jelentett a tized (decima) törvénye?",
            "question": "Mit kellett beszolgáltatni tizedként?",
            "options": ["A mezőgazdasági termés és szaporulat egytized részét az egyháznak", "Minden tizedik gyermeket katonának", "A pénz felét Rómának", "Tíz lovat havonta a királynak"],
            "correctIndex": 0,
            "explanation": "A tized a termés 10%-ának egyházi adója volt a papok és templomok fenntartására.",
            "teaches": ["tized", "fenntartas"]
        },
        {
            "id": "b1-istvankiraly-03.ex05",
            "type": "fill-blank",
            "title": "Pannonhalmi apátság",
            "instruction": "Válaszd ki a megfelelő szerzetesrendet!",
            "sentence": "Pannonhalmán az első ___ apátságot alapította meg a király.",
            "correctAnswer": "bencés",
            "options": ["bencés", "katonai", "tengeri", "jezsuita"],
            "teaches": ["apatsag", "bences"]
        },
        {
            "id": "b1-istvankiraly-03.ex06",
            "type": "sentence-builder",
            "title": "Magántulajdon védelme",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["István", "törvényei", "szigorúan", "védték", "a", "magántulajdont."],
            "correctSentence": "István törvényei szigorúan védték a magántulajdont.",
            "english": "Stephen's laws strictly protected private property.",
            "teaches": ["magantulajdon"]
        },
        {
            "id": "b1-istvankiraly-03.ex07",
            "type": "multiple-choice",
            "title": "Számnév utáni egyes szám",
            "instruction": "Melyik alak helyes a magyar nyelvtan szabályai szerint?",
            "question": "Hogyan mondjuk helyesen magyarul a 'ten counties' kifejezést?",
            "options": ["Tíz vármegye", "Tíz vármegyék", "Tízből vármegyék", "Vármegyék tízek"],
            "correctIndex": 0,
            "explanation": "Magyarban tőszámnév után mindig egyes számú főnevet használunk: tíz vármegye.",
            "teaches": ["varmegye"]
        },
        {
            "id": "b1-istvankiraly-03.ex08",
            "type": "fill-blank",
            "title": "Bíráskodás a várban",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A vitás ügyekben a vármegyei ispán ___ a helyi lakosok felett.",
            "correctAnswer": "bíráskodott",
            "options": ["bíráskodott", "énekelt", "futott", "aludt"],
            "teaches": ["biraskodik", "ispan"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-istvankiraly-03.json", make_lesson(
    "lesson.b1.istvankiraly-03",
    "Államszervezet és egyházszervezet (State & Church Organization)",
    "Számnévi szerkezetek és kötelezettséget kifejező igék",
    [
        "In this third lesson, we explore the administrative and ecclesiastical foundation of medieval Hungary under Saint Stephen.",
        "You will learn about the 10 dioceses (Esztergom and Kalocsa archdioceses), Pannonhalma Benedictine Abbey, the royal county system (*vármegyerendszer*) headed by *ispánok*, and early laws (tithe and 'every 10 villages shall build a church').",
        "We also practice expressions of obligation (*köteles, kell*) and the rule of singular nouns after numerals."
    ],
    [
        "I can describe the 10 bishoprics and the administrative county system (*vármegyék, ispánok*).",
        "I can explain the law of building churches (*minden tíz falu köteles templomot építeni*) and the tithe (*tized*).",
        "I can identify Pannonhalma as Hungary's oldest Benedictine abbey.",
        "I can use singular nouns with numbers and modal verbs of obligation correctly."
    ],
    "stories/world/b1/b1-istvankiraly-03-keresztenykiralysag.json",
    "vocabulary/b1/b1-istvankiraly-03-voc.json",
    "grammar/b1/b1-istvankiraly-03-alapitott-intezmenyek-gr.json",
    "exercises/b1/b1-istvankiraly-03-ex.json",
    [f"b1-istvankiraly-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: Intelmek és Szent István öröksége
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly-04-szentistvanoroksege.json", make_story(
    "story.b1.istvankiraly.04",
    "Az Intelmek Imre herceghez és Szent István emléke",
    "King Stephen's moral testament 'Intelmek' (Admonitiones) to Prince Emeric, his vision of a multilingual welcoming realm, his 1083 canonization, and Saint Stephen's Day on August 20.",
    "Székesfehérvár",
    ["szentté avatás kifejezései és idéző szerkezetek"],
    ["Intelmek Imre herceghez", "Szentté avatás 1083", "Augusztus 20."],
    [
        "Uralkodása végén István király latin nyelvű intelmeket fogalmazott meg fiához, a trónörökös Imre herceghez (Admonitiones / Intelmek Imre herceghez).",
        "Az Intelmek a keresztény uralkodói etika legszebb középkori magyar emléke. Híres mondata szerint: 'Mert az egynyelvű és egyszokású ország gyenge és esendő' – tanácsolva a más nemzetekből érkező vendégek és telepesek tiszteletét és befogadását.",
        "Bár Imre herceg egy vadkanvadászaton fiatalon életét vesztette, és a király halála után trónharcok törtek ki, István műve szilárd maradt.",
        "1083-ban VII. Gergely pápa engedélyével I. László király szentté avatta István királyt, Imre herceget és Gellért püspököt.",
        "Szent István napja, augusztus 20-a a magyar államalapítás és az állam ezeréves folytonosságának legnagyobb nemzeti ünnepe."
    ],
    [
        {"lemma": "intelmek", "pos": "noun", "cefr": "B1", "gloss": "admonitions / moral advice (Admonitiones)"},
        {"lemma": "esendő", "pos": "adj", "cefr": "B1", "gloss": "fragile / frail"},
        {"lemma": "szentté avatás", "pos": "noun", "cefr": "B1", "gloss": "canonization"},
        {"lemma": "államalapítás", "pos": "noun", "cefr": "B1", "gloss": "state foundation"}
    ],
    [
        {
            "question": "Mit tanácsolt Szent István a fiának a külföldről érkező vendégekről az Intelmekben?",
            "options": ["Hogy fogadja be és tisztelje őket, mert az egynyelvű ország gyenge és esendő", "Hogy minden idegent űzzön el az országból", "Hogy tiltsa meg az idegen nyelveket", "Hogy ne engedjen be senkit a határokon"],
            "correctIndex": 0,
            "explanation": "István a befogadás és a vendégek tiszteletének fontosságát hangsúlyozta fiának."
        },
        {
            "question": "Melyik évben avatták szentté István királyt, Imre herceget és Gellért püspököt?",
            "options": ["1083-ban Szent László király idején", "1526-ban", "1848-ban", "1956-ban"],
            "correctIndex": 0,
            "explanation": "1083-ban avatták szentté Istvánt, Imrét és Gellértet I. László király uralkodása alatt."
        },
        {
            "question": "Melyik nemzeti ünnep kapcsolódik Szent Istvánhoz és az államalapításhoz?",
            "options": ["Augusztus 20.", "Március 15.", "Október 23.", "Május 1."],
            "correctIndex": 0,
            "explanation": "Augusztus 20-a Szent István napja és a magyar államalapítás hivatalos ünnepe."
        }
    ]
))

write_json(VOCAB_DIR / "b1-istvankiraly-04-voc.json", {
    "title": "Az Intelmek és Szent István öröksége",
    "words": [
        {"lemma": "intelmek", "pos": "noun", "cefr": "B1", "translation": "admonitions / counsels", "examples": [{"hungarian": "Az Intelmek Imre herceghez bölcs tanácsokat tartalmaz.", "english": "The Admonitions to Prince Emeric contains wise advice."}]},
        {"lemma": "esendő", "pos": "adj", "cefr": "B1", "translation": "frail / vulnerable", "examples": [{"hungarian": "Az egynyelvű ország gyenge és esendő.", "english": "A unilingual country is weak and frail."}]},
        {"lemma": "szentté avatás", "pos": "noun", "cefr": "B1", "translation": "canonization", "examples": [{"hungarian": "A szentté avatás 1083-ban zajlott le.", "english": "The canonization took place in 1083."}]},
        {"lemma": "államalapítás", "pos": "noun", "cefr": "B1", "translation": "state foundation", "examples": [{"hungarian": "Augusztus 20. az államalapítás ünnepe.", "english": "August 20 is the holiday of state foundation."}]},
        {"lemma": "trónörökös", "pos": "noun", "cefr": "B1", "translation": "heir to the throne", "examples": [{"hungarian": "Imre herceg volt a trónörökös.", "english": "Prince Emeric was the heir to the throne."}]},
        {"lemma": "erkölcs", "pos": "noun", "cefr": "B1", "translation": "morality / ethics", "examples": [{"hungarian": "A keresztény erkölcs vezette az uralkodót.", "english": "Christian morality guided the monarch."}]},
        {"lemma": "befogadás", "pos": "noun", "cefr": "B1", "translation": "admission / welcoming", "examples": [{"hungarian": "A vendégek befogadása erősítette az országot.", "english": "Welcoming guests strengthened the country."}]},
        {"lemma": "telepes", "pos": "noun", "cefr": "B1", "translation": "settler", "examples": [{"hungarian": "Külföldi telepesek érkeztek új ismeretekkel.", "english": "Foreign settlers arrived with new knowledge."}]},
        {"lemma": "folytonosság", "pos": "noun", "cefr": "B1", "translation": "continuity", "examples": [{"hungarian": "A magyar állam ezeréves folytonosságot képvisel.", "english": "The Hungarian state represents a thousand-year continuity."}]},
        {"lemma": "tisztelet", "pos": "noun", "cefr": "B1", "translation": "respect / reverence", "examples": [{"hungarian": "Mély tisztelet övezi Szent István emlékét.", "english": "Deep respect surrounds the memory of Saint Stephen."}]},
        {"lemma": "örökség", "pos": "noun", "cefr": "B1", "translation": "legacy / heritage", "examples": [{"hungarian": "István öröksége a nemzet fennmaradásának alapja.", "english": "Stephen's legacy is the foundation of the nation's survival."}]},
        {"lemma": "ünnepel", "pos": "verb", "cefr": "B1", "translation": "to celebrate", "examples": [{"hungarian": "Augusztus 20-án az egész ország ünnepel.", "english": "On August 20, the entire country celebrates."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-istvankiraly-04-szentte-avatott-gr.json", {
    "title": "Idéző mondatok és a szentté avatás nyelvtani szerkezetei",
    "level": "B1",
    "rules": [
        {
            "id": "direct-indirect-quotes",
            "title": "Reporting Quotes in Hungarian (szerint, mondván)",
            "text": "Attributing famous quotes uses *szerint* (+ noun/name) or quotation clauses: *István király szerint az egynyelvű ország gyenge.* (According to King Stephen, a unilingual country is weak.) *Azt tanácsolta a fiának, hogy tisztelje a vendégeket.*",
            "tip": "Always use a comma before *hogy* in reported speech."
        },
        {
            "id": "canonization-verbs",
            "title": "Factitive / Resultative Form (-vá / -vé tesz, avat)",
            "text": "*Szentté avat* (to canonize), *hőssé válik* (to become a hero). The translative *-vá / -vé* shows change of condition or status.",
            "tip": "Example: *László király szentté avatta Istvánt.*"
        }
    ],
    "examples": [
        {"spanish": "István király szerint az egynyelvű ország gyenge és esendő.", "english": "According to King Stephen, a unilingual country is weak and frail."},
        {"spanish": "1083-ban Istvánt és Imrét szentté avatták.", "english": "In 1083, Stephen and Emeric were canonized."},
        {"spanish": "Augusztus 20-án az államalapítást ünnepeljük.", "english": "On August 20, we celebrate the foundation of the state."}
    ]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-04-ex.json", {
    "exercises": [
        {
            "id": "b1-istvankiraly-04.ex01",
            "type": "multiple-choice",
            "title": "Az Intelmek híres gondolata",
            "instruction": "Mit fogalmazott meg Szent István az Intelmekben?",
            "question": "Hogyan jellemezte István az egynyelvű országot?",
            "options": ["'Az egynyelvű és egyszokású ország gyenge és esendő'", "'Az egynyelvű ország a világ legerősebb állama'", "'Minden országnak teljesen egyformának kell lennie'", "'Senkit nem szabad beengedni más országból'"],
            "correctIndex": 0,
            "explanation": "István híres intelme szerint a sokszínűség és a vendégek befogadása erősíti az országot.",
            "teaches": ["intelmek", "esendo"]
        },
        {
            "id": "b1-istvankiraly-04.ex02",
            "type": "fill-blank",
            "title": "Szentté avatás éve",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Szent Istvánt, Imre herceget és Gellért püspököt ___ avatták szentté I. László uralkodása alatt.",
            "correctAnswer": "1083-ban",
            "options": ["1083-ban", "1526-ban", "1848-ban", "1956-ban"],
            "teaches": ["szentte-avatas"]
        },
        {
            "id": "b1-istvankiraly-04.ex03",
            "type": "sentence-builder",
            "title": "Augusztus 20. ünnepe",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Augusztus", "20-a", "a", "magyar", "államalapítás", "hivatalos", "nemzeti", "ünnepe."],
            "correctSentence": "Augusztus 20-a a magyar államalapítás hivatalos nemzeti ünnepe.",
            "english": "August 20 is the official national holiday of Hungarian state foundation.",
            "teaches": ["allamalapitas", "unnepel"]
        },
        {
            "id": "b1-istvankiraly-04.ex04",
            "type": "multiple-choice",
            "title": "A trónörökös",
            "instruction": "Ki volt Szent István fia, akihez az Intelmeket írta?",
            "question": "Hogy hívták István király trónörökös fiát?",
            "options": ["Imre herceg", "László herceg", "Kálmán herceg", "Béla herceg"],
            "correctIndex": 0,
            "explanation": "Szent Imre herceg volt István trónörökös fia.",
            "teaches": ["tronorokos", "intelmek"]
        },
        {
            "id": "b1-istvankiraly-04.ex05",
            "type": "fill-blank",
            "title": "Vendégek tisztelete",
            "instruction": "Válaszd ki a megfelelő kifejezést!",
            "sentence": "Az Intelmek a más népekből érkező vendégek és telepesek ___ tanácsolja.",
            "correctAnswer": "befogadását",
            "options": ["befogadását", "elűzését", "megbüntetését", "bezárását"],
            "teaches": ["befogadas", "telepes"]
        },
        {
            "id": "b1-istvankiraly-04.ex06",
            "type": "sentence-builder",
            "title": "Szentté avatás (szentté)",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["László", "király", "1083-ban", "szentté", "avatta", "István", "királyt."],
            "correctSentence": "László király 1083-ban szentté avatta István királyt.",
            "english": "King Ladislaus canonized King Stephen in 1083.",
            "teaches": ["szentte-avatas"]
        },
        {
            "id": "b1-istvankiraly-04.ex07",
            "type": "multiple-choice",
            "title": "Állami folytonosság",
            "instruction": "Mit szimbolizál Szent István napja?",
            "question": "Mit ünneplünk augusztus 20-án Magyarországon?",
            "options": ["Az államalapítást és az állam ezeréves folytonosságát", "A forradalom kitörését 1848-ban", "A tél végét és a tavasz kezdetét", "A parlament építésének befejezését"],
            "correctIndex": 0,
            "explanation": "Augusztus 20-a az államalapító Szent István király és az államiság ünnepe.",
            "teaches": ["allamalapitas", "folytonossag"]
        },
        {
            "id": "b1-istvankiraly-04.ex08",
            "type": "fill-blank",
            "title": "Bölcs intelmek",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Az Intelmek a keresztény uralkodói ___ szép középkori emléke.",
            "correctAnswer": "erkölcs",
            "options": ["erkölcs", "háború", "kereskedelem", "zeneművészet"],
            "teaches": ["erkolcs"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-istvankiraly-04.json", make_lesson(
    "lesson.b1.istvankiraly-04",
    "Az Intelmek és Szent István öröksége (The Admonitions & Legacy)",
    "Idéző mondatok és a szentté avatás nyelvtani szerkezetei",
    [
        "In this fourth lesson, we examine Saint Stephen's moral and political testament: the *Intelmek* (Admonitiones) to Prince Emeric.",
        "You will learn about his famous counsel on diversity and hospitality (*'egynyelvű és egyszokású ország gyenge és esendő'*), the 1083 canonization under Saint Ladislaus, and Saint Stephen's Day on August 20.",
        "We also practice reported speech with *szerint* and factitive transformations with *-vá / -vé* (*szentté avat*)."
    ],
    [
        "I can quote and explain the core message of the *Intelmek* to Prince Emeric.",
        "I can state the year of Saint Stephen's canonization (1083).",
        "I can explain why August 20 is Hungary's major state foundation holiday.",
        "I can construct accurate reported speech and translative case sentences."
    ],
    "stories/world/b1/b1-istvankiraly-04-szentistvanoroksege.json",
    "vocabulary/b1/b1-istvankiraly-04-voc.json",
    "grammar/b1/b1-istvankiraly-04-szentte-avatott-gr.json",
    "exercises/b1/b1-istvankiraly-04-ex.json",
    [f"b1-istvankiraly-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: A Szent Korona és a Szent Korona-tan
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly-05-szentkorona.json", make_story(
    "story.b1.istvankiraly.05",
    "A Szent Korona és a Szent Korona-tan",
    "The Holy Crown of Hungary (Corona Graeca + Corona Latina, tilted cross), the Doctrine of the Holy Crown (*Szent Korona-tan*), and its legal symbolism in the Országház dome hall.",
    "Budapest, Országház kupolaterme",
    ["szintetizáló mondatok és alkotmányjogi fogalmak"],
    ["Szent Korona", "Szent Korona-tan", "Nemzeti ereklye"],
    [
        "A Szent Korona Magyarország legfontosabb nemzeti ereklyéje és az állami szuverenitás legfőbb szimbóluma. Jelenleg a Parlament (Országház) kupolacsarnokában őrzik a Koronaőrség felügyelete alatt.",
        "A korona két fő részből áll: az alsó, görög feliratú Corona Graecából és a felső, latin feliratú pántokból álló Corona Latinából. Tetején a jellegzetes ferde kereszt látható.",
        "A magyar alkotmánytörténetben a Szent Korona nem csupán egy ékszer, hanem önálló jogi személy: a Szent Korona-tan szerint a legfőbb hatalom és a szuverenitás magát a Koronát illeti meg.",
        "A király és a nemzet tagjai (a korona tagjai) a Szent Korona nevében közösen gyakorolták a törvényhozó és kormányzó hatalmat.",
        "Az Alaptörvény ma is rögzíti, hogy a Szent Korona megtestesíti Magyarország alkotmányos állami folytonosságát és a nemzet egységét."
    ],
    [
        {"lemma": "nemzeti ereklye", "pos": "noun", "cefr": "B1", "gloss": "national relic"},
        {"lemma": "Szent Korona-tan", "pos": "noun", "cefr": "B1", "gloss": "Doctrine of the Holy Crown"},
        {"lemma": "ferde kereszt", "pos": "noun", "cefr": "B1", "gloss": "tilted cross (on Holy Crown)"},
        {"lemma": "állami folytonosság", "pos": "noun", "cefr": "B1", "gloss": "state continuity"}
    ],
    [
        {
            "question": "Hol őrzik ma a Magyar Szent Koronát?",
            "options": ["A Parlament (Országház) kupolacsarnokában", "A Magyar Nemzeti Múzeum pincéjében", "Egy bécsi bankban", "A párizsi Louvre-ban"],
            "correctIndex": 0,
            "explanation": "A Szent Koronát az Országház (Parlament) kupolatermében őrzik szigorú biztonsági védelem mellett."
        },
        {
            "question": "Mi a Szent Korona-tan lényege a magyar közjogban?",
            "options": ["Hogy a főhatalom és az állami szuverenitás hordozója maga a Szent Korona", "Hogy a korona kizárólag a király magántulajdona", "Hogy bárki szabadon eladhatja a koronát külföldre", "Hogy a koronát csak ünnepeken lehet felpróbálni"],
            "correctIndex": 0,
            "explanation": "A Szent Korona-tan szerint az államhatalom forrása a Szent Korona, amely megtestesíti a király és a nemzet egységét."
        },
        {
            "question": "Melyik két fő részből tevődik össze a Szent Korona?",
            "options": ["A görög feliratú Corona Graecából és a latin Corona Latinából", "Egy arany és egy fa koszorúból", "Csak ezüst érmékből", "Modern acélrudakból"],
            "correctIndex": 0,
            "explanation": "A Szent Korona a görög zománcképes Corona Graecából és a latin feliratú pántokból áll."
        }
    ]
))

write_json(VOCAB_DIR / "b1-istvankiraly-05-voc.json", {
    "title": "A Szent Korona és a Szent Korona-tan",
    "words": [
        {"lemma": "nemzeti ereklye", "pos": "noun", "cefr": "B1", "translation": "national relic", "examples": [{"hungarian": "A Szent Korona a legnagyobb nemzeti ereklye.", "english": "The Holy Crown is the greatest national relic."}]},
        {"lemma": "Szent Korona-tan", "pos": "noun", "cefr": "B1", "translation": "Doctrine of the Holy Crown", "examples": [{"hungarian": "A Szent Korona-tan a magyar alkotmányfejlődés alapja.", "english": "The Doctrine of the Holy Crown is the basis of Hungarian constitutional development."}]},
        {"lemma": "ferde kereszt", "pos": "noun", "cefr": "B1", "translation": "tilted cross", "examples": [{"hungarian": "A ferde kereszt a korona tetején látható.", "english": "The tilted cross can be seen on top of the crown."}]},
        {"lemma": "állami folytonosság", "pos": "noun", "cefr": "B1", "translation": "state continuity", "examples": [{"hungarian": "A korona megtestesíti az állami folytonosságot.", "english": "The crown embodies state continuity."}]},
        {"lemma": "kupolacsarnok", "pos": "noun", "cefr": "B1", "translation": "dome hall", "examples": [{"hungarian": "A Parlament kupolacsarnokában őrzik a koronát.", "english": "The crown is kept in the dome hall of the Parliament."}]},
        {"lemma": "koronaőrség", "pos": "noun", "cefr": "B1", "translation": "crown guard", "examples": [{"hungarian": "A Koronaőrség vigyázza a nemzeti jelképeket.", "english": "The Crown Guard watches over the national symbols."}]},
        {"lemma": "zománckép", "pos": "noun", "cefr": "B1", "translation": "enamel picture", "examples": [{"hungarian": "Finom zománcképek díszítik a pántokat.", "english": "Delicate enamel pictures decorate the bands."}]},
        {"lemma": "szimbólum", "pos": "noun", "cefr": "B1", "translation": "symbol", "examples": [{"hungarian": "A Szent Korona a függetlenség szimbóluma.", "english": "The Holy Crown is the symbol of independence."}]},
        {"lemma": "jogkör", "pos": "noun", "cefr": "B1", "translation": "sphere of authority / jurisdiction", "examples": [{"hungarian": "A törvényhozó jogkör a nemzetet és a királyt illette.", "english": "Legislative authority belonged to the nation and the king."}]},
        {"lemma": "megtestesít", "pos": "verb", "cefr": "B1", "translation": "to embody / personify", "examples": [{"hungarian": "A korona megtestesíti a nemzet egységét.", "english": "The crown embodies the unity of the nation."}]},
        {"lemma": "alaptörvény", "pos": "noun", "cefr": "B1", "translation": "Fundamental Law / Constitution", "examples": [{"hungarian": "Az Alaptörvény tiszteletben tartja a Szent Korona örökségét.", "english": "The Fundamental Law respects the heritage of the Holy Crown."}]},
        {"lemma": "főhatalom", "pos": "noun", "cefr": "B1", "translation": "supreme power / sovereignty", "examples": [{"hungarian": "A főhatalom a Koronából ered a hagyomány szerint.", "english": "Supreme power originates from the Crown according to tradition."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-istvankiraly-05-synthesis-gr.json", {
    "title": "Alkotmányjogi szintaxis és absztrakt összefüggések",
    "level": "B1",
    "rules": [
        {
            "id": "impersonal-verbs-law",
            "title": "Impersonal Legal Verbs (illet meg, rögzít)",
            "text": "Formal constitutional statements use impersonal active verbs: *A törvény rögzíti, hogy...* (The law records that...), *A hatalom a nemzetet illeti meg.* (Power belongs to / pertains to the nation.)",
            "tip": "*Megillet* takes an accusative object (*a nemzetet illeti meg*)."
        },
        {
            "id": "participial-compounds",
            "title": "Complex Participial Compounds in Formal Hungarian",
            "text": "High-register texts use participial compounds: *alkotmányos állami folytonosság* (constitutional state continuity), *nemzetet megillető jogok* (rights pertaining to the nation).",
            "tip": "Essential for the constitutional knowledge exam (*alkotmányos alapismeretek*)."
        }
    ],
    "examples": [
        {"spanish": "A Szent Korona megtestesíti a nemzet egységét.", "english": "The Holy Crown embodies the unity of the nation."},
        {"spanish": "Az Alaptörvény rögzíti az állami folytonosságot.", "english": "The Fundamental Law records state continuity."},
        {"spanish": "A legfőbb hatalom a Szent Korona nevében működik.", "english": "Supreme power operates in the name of the Holy Crown."}
    ]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-05-ex.json", {
    "exercises": [
        {
            "id": "b1-istvankiraly-05.ex01",
            "type": "multiple-choice",
            "title": "A Szent Korona őrzési helye",
            "instruction": "Hol őrzik jelenleg a Szent Koronát?",
            "question": "Melyik épületben tekinthető meg a Szent Korona?",
            "options": ["Az Országház (Parlament) kupolacsarnokában", "A Budavári Palota bástyáján", "A Széchenyi Könyvtárban", "A Bazilika harangtornyában"],
            "correctIndex": 0,
            "explanation": "A Szent Korona és a koronázási jelvények az Országház kupolacsarnokában találhatók.",
            "teaches": ["kupolacsarnok", "nemzeti-ereklye"]
        },
        {
            "id": "b1-istvankiraly-05.ex02",
            "type": "fill-blank",
            "title": "A korona keresztje",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A Szent Korona tetején a jellegzetes ___ kereszt látható.",
            "correctAnswer": "ferde",
            "options": ["ferde", "egyenes", "világító", "fa"],
            "teaches": ["ferde-kereszt"]
        },
        {
            "id": "b1-istvankiraly-05.ex03",
            "type": "sentence-builder",
            "title": "Nemzet egysége",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "Szent", "Korona", "megtestesíti", "a", "nemzet", "egységét."],
            "correctSentence": "A Szent Korona megtestesíti a nemzet egységét.",
            "english": "The Holy Crown embodies the unity of the nation.",
            "teaches": ["megtestesit", "allami-folytonossag"]
        },
        {
            "id": "b1-istvankiraly-05.ex04",
            "type": "multiple-choice",
            "title": "A Szent Korona-tan",
            "instruction": "Mit tanít a Szent Korona-tan a hatalomról?",
            "question": "Ki vagy mi a legfőbb hatalom birtokosa a Szent Korona-tan szerint?",
            "options": ["Maga a Szent Korona, mint az állam jogi személye", "Csak az idegen császár", "Kizárólag a pénzügyminiszter", "Bármelyik külföldi utazó"],
            "correctIndex": 0,
            "explanation": "A Szent Korona-tan szerint a szuverenitás és a hatalom hordozója a Szent Korona.",
            "teaches": ["Szent-Korona-tan", "fohatalom"]
        },
        {
            "id": "b1-istvankiraly-05.ex05",
            "type": "fill-blank",
            "title": "A korona két része",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A korona a görög Corona Graecából és a latin Corona ___ áll.",
            "correctAnswer": "Latinából",
            "options": ["Latinából", "Francából", "Anglicából", "Germanicából"],
            "teaches": ["zomanckep"]
        },
        {
            "id": "b1-istvankiraly-05.ex06",
            "type": "sentence-builder",
            "title": "Alkotmányos folytonosság",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Az", "Alaptörvény", "elismeri", "a", "Szent", "Korona", "történelmi", "szerepét."],
            "correctSentence": "Az Alaptörvény elismeri a Szent Korona történelmi szerepét.",
            "english": "The Fundamental Law recognizes the historical role of the Holy Crown.",
            "teaches": ["alaptorveny", "allami-folytonossag"]
        },
        {
            "id": "b1-istvankiraly-05.ex07",
            "type": "multiple-choice",
            "title": "A Koronaőrség",
            "instruction": "Ki felügyeli a Szent Korona biztonságát?",
            "question": "Mely testület őrzi a koronát a Parlamentben?",
            "options": ["A Honvéd Koronaőrség", "Egy külföldi biztonsági cég", "Csak a parlament takarítói", "A tűzoltóság"],
            "correctIndex": 0,
            "explanation": "A Magyar Honvédség Koronaőrsége látja el a Szent Korona protokolláris és biztonsági őrzését.",
            "teaches": ["koronaorseg"]
        },
        {
            "id": "b1-istvankiraly-05.ex08",
            "type": "fill-blank",
            "title": "Legfőbb ereklye",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A Szent Korona a magyar államiság legféltettebb nemzeti ___.",
            "correctAnswer": "ereklyéje",
            "options": ["ereklyéje", "könyvtára", "autója", "hajója"],
            "teaches": ["nemzeti-ereklye"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-istvankiraly-05.json", make_lesson(
    "lesson.b1.istvankiraly-05",
    "A Szent Korona és a Szent Korona-tan (The Holy Crown & Doctrine)",
    "Alkotmányjogi szintaxis és absztrakt összefüggések",
    [
        "In this fifth lesson, we examine the Holy Crown of Hungary (*Szent Korona*) and the Doctrine of the Holy Crown (*Szent Korona-tan*).",
        "You will learn about the physical components of the crown (Corona Graeca, Corona Latina, the tilted cross), its location in the Parliament dome hall, and its constitutional role as the embodiment of state continuity in the Hungarian *Alaptörvény*.",
        "We also practice legal verbs (*megillet, rögzít*) and participial noun compounds."
    ],
    [
        "I can describe the Holy Crown, its structure, tilted cross, and location in the Parliament.",
        "I can explain the Doctrine of the Holy Crown (*Szent Korona-tan*) as a constitutional pillar.",
        "I can state the role of the Holy Crown in the Fundamental Law (*Alaptörvény*).",
        "I can use formal legal syntax and abstract terminology in Hungarian B1."
    ],
    "stories/world/b1/b1-istvankiraly-05-szentkorona.json",
    "vocabulary/b1/b1-istvankiraly-05-voc.json",
    "grammar/b1/b1-istvankiraly-05-synthesis-gr.json",
    "exercises/b1/b1-istvankiraly-05-ex.json",
    [f"b1-istvankiraly-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 4 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-istvankiraly.json", make_story(
    "story.b1.istvankiraly",
    "Szent István király és a keresztény államalapítás (1000)",
    "The comprehensive story of Saint Stephen and the founding of the Hungarian kingdom: from defeating Koppány and the 1000 coronation, through church and county building, to the Intelmek and the enduring legacy of the Holy Crown.",
    "Esztergom, Székesfehérvár és Pannonhalma",
    ["összetett mondatok", "államelméleti kifejezések"],
    ["Szent István király", "Keresztény királyság", "Szent Korona", "Államalapítás"],
    [
        "Géza fejedelem halála után fia, István a keresztény hit és a nyugati jogrend mellett kötelezte el magát. Miután 997-ben Veszprémnél legyőzte a pogány Koppányt, megnyílt az út az európai államalapítás előtt.",
        "1000 karácsonyán Istvánt királlyá koronázták a II. Szilveszter pápa által küldött koronával, amellyel Magyarország szuverén, független keresztény királysággá vált.",
        "István zseniális államszervezőként tíz egyházmegyét, köztük az esztergomi és kalocsai érsekséget alapította meg, kiépítette a királyi vármegyék rendszerét az ispánok vezetésével, és törvénybe iktatta a tizedet és a tízfalunkénti templomépítést.",
        "Fia számára megfogalmazta az Intelmeket, amely a keresztény uralkodói erkölcs és a nemzeti befogadás örökérvényű dokumentuma. 1083-as szentté avatása után augusztus 20-a lett a magyar államalapítás legfőbb nemzeti ünnepe.",
        "A Szent Korona és a Szent Korona-tan ma is a magyar állami szuverenitás, a jogfolytonosság és a nemzeti összetartozás legszentebb jelképe."
    ],
    [
        {"lemma": "államalapító", "pos": "noun", "cefr": "B1", "gloss": "state founder"},
        {"lemma": "szuverenitás", "pos": "noun", "cefr": "B1", "gloss": "sovereignty"},
        {"lemma": "törvényhozás", "pos": "noun", "cefr": "B1", "gloss": "legislation"},
        {"lemma": "jogfolytonosság", "pos": "noun", "cefr": "B1", "gloss": "legal continuity"}
    ],
    [
        {
            "question": "Melyik évszámhoz kötődik a keresztény Magyar Királyság megalapítása és I. István koronázása?",
            "options": ["1000 karácsonya / 1001. január 1.", "895", "1222", "1848"],
            "correctIndex": 0,
            "explanation": "Szent István koronázása 1000/1001-ben történt a pápától küldött koronával."
        },
        {
            "question": "Milyen intézményeket hozott létre Szent István a közigazgatásban és az egyházban?",
            "options": ["Vármegyéket ispánokkal és tíz egyházmegyét érsekségekkel", "Csak lovagi tornákat", "Modern minisztériumokat", "Kizárólag katonai táborokat"],
            "correctIndex": 0,
            "explanation": "István királyi vármegyéket és 10 egyházmegyét alapított."
        },
        {
            "question": "Mit szimbolizál ma a Szent Korona a Parlamentben?",
            "options": ["Magyarország alkotmányos állami folytonosságát és a nemzet egységét", "Egy múzeumi ékszert politikai jelentőség nélkül", "A császári megszállást", "A köztársaság eltörlését"],
            "correctIndex": 0,
            "explanation": "Az Alaptörvény szerint a Szent Korona az állami folytonosságot és a nemzet egységét testesíti meg."
        }
    ]
))

u4_cons_ex = []
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex01",
    "type": "multiple-choice",
    "title": "Koronázás éve",
    "instruction": "Mikor koronázták meg Szent Istvánt?",
    "question": "Melyik évszám a magyar államalapítás éve?",
    "options": ["1000", "895", "1241", "1526"],
    "correctIndex": 0,
    "explanation": "Szent István koronázása 1000-ben történt.",
    "teaches": ["koronazas", "allamisag"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex02",
    "type": "fill-blank",
    "title": "Pápai korona",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A koronát II. ___ pápa küldte Rómából.",
    "correctAnswer": "Szilveszter",
    "options": ["Szilveszter", "Gergely", "Pál", "Leó"],
    "teaches": ["koronazas", "szuveren"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex03",
    "type": "sentence-builder",
    "title": "Veszprémi csata",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["István", "Veszprém", "mellett", "legyőzte", "Koppányt,", "megszilárdítva", "a", "hatalmat."],
    "correctSentence": "István Veszprém mellett legyőzte Koppányt, megszilárdítva a hatalmat.",
    "english": "Stephen defeated Koppány near Veszprém, solidifying power.",
    "teaches": ["szenioratus", "primogenitura"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex04",
    "type": "multiple-choice",
    "title": "Vármegyerendszer",
    "instruction": "Ki vezette a királyi vármegyét?",
    "question": "Ki volt a vármegye élén álló királyi tisztviselő?",
    "options": ["Az ispán", "A polgármester", "A gyula", "A hadnagy"],
    "correctIndex": 0,
    "explanation": "A királyi vármegyét az ispán irányította.",
    "teaches": ["ispan", "varmegye"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex05",
    "type": "fill-blank",
    "title": "Templomépítés",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "István elrendelte, hogy minden tíz falu köteles egy ___ építeni.",
    "correctAnswer": "templomot",
    "options": ["templomot", "várat", "hajót", "hidat"],
    "teaches": ["elrendel"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex06",
    "type": "sentence-builder",
    "title": "Tized adó",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["A", "tized", "a", "termés", "egytizedének", "egyházi", "adója", "volt."],
    "correctSentence": "A tized a termés egytizedének egyházi adója volt.",
    "english": "The tithe was an ecclesiastical tax of one-tenth of the harvest.",
    "teaches": ["tized", "fenntartas"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex07",
    "type": "multiple-choice",
    "title": "Az Intelmek üzenete",
    "instruction": "Melyik híres mondat származik Szent István Intelmeiből?",
    "question": "Mit írt István az egynyelvű országról?",
    "options": ["'Az egynyelvű és egyszokású ország gyenge és esendő'", "'Minden ember tanuljon meg latinul'", "'Csak a király dönthet mindenről'", "'Az országnak nincs szüksége vendégekre'"],
    "correctIndex": 0,
    "explanation": "István a befogadás és a sokszínűség erejét tanította fiának, Imre hercegnek.",
    "teaches": ["intelmek", "esendo"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex08",
    "type": "fill-blank",
    "title": "Szentté avatás",
    "instruction": "Válaszd ki a megfelelő évet!",
    "sentence": "I. Istvánt és fiát, Imre herceget ___ avatták szentté.",
    "correctAnswer": "1083-ban",
    "options": ["1083-ban", "1526-ban", "1848-ban", "1989-ben"],
    "teaches": ["szentte-avatas"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex09",
    "type": "sentence-builder",
    "title": "Augusztus 20.",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Augusztus", "20-án", "ünnepeljük", "Szent", "István", "királyt", "és", "az", "államalapítást."],
    "correctSentence": "Augusztus 20-án ünnepeljük Szent István királyt és az államalapítást.",
    "english": "On August 20, we celebrate King Saint Stephen and the foundation of the state.",
    "teaches": ["allamalapitas", "unnepel"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex10",
    "type": "multiple-choice",
    "title": "A Szent Korona helye",
    "instruction": "Hol tekinthető meg ma a Szent Korona?",
    "question": "Melyik teremben őrzik a magyar állam legfőbb ereklyéjét?",
    "options": ["Az Országház kupolacsarnokában", "A Nemzeti Színházban", "A Budapesti Műszaki Egyetemen", "A Deák téri metróban"],
    "correctIndex": 0,
    "explanation": "A Szent Korona az Országház (Parlament) fenséges kupolatermében látható.",
    "teaches": ["kupolacsarnok", "nemzeti-ereklye"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex11",
    "type": "fill-blank",
    "title": "Aposztoli jogkör",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "István elnyerte az ___ királyi jogkört az egyházmegyék önálló megszervezésére.",
    "correctAnswer": "apostoli",
    "options": ["apostoli", "tengeri", "császári", "hadvezér"],
    "teaches": ["apostoli-kiraly", "felhatalmaz"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex12",
    "type": "sentence-builder",
    "title": "Szent Korona-tan",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["A", "Szent", "Korona-tan", "szerint", "a", "főhatalom", "a", "Koronát", "illeti", "meg."],
    "correctSentence": "A Szent Korona-tan szerint a főhatalom a Koronát illeti meg.",
    "english": "According to the Doctrine of the Holy Crown, supreme power belongs to the Crown.",
    "teaches": ["Szent-Korona-tan", "fohatalom"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex13",
    "type": "multiple-choice",
    "title": "Pannonhalma",
    "instruction": "Melyik szerzetesrend kapott apátságot Pannonhalmán István idején?",
    "question": "Melyik rend alapította Pannonhalmát?",
    "options": ["A bencés rend", "A ferences rend", "A jezsuita rend", "A pálos rend"],
    "correctIndex": 0,
    "explanation": "A bencés szerzetesek telepedtek le Pannonhalmán, ahol az első apátság felépült.",
    "teaches": ["apatsag", "bences"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex14",
    "type": "fill-blank",
    "title": "Ferde kereszt",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A Szent Korona tetején lévő ___ kereszt a nemzeti jelkép egyedi sajátossága.",
    "correctAnswer": "ferde",
    "options": ["ferde", "aranyos", "fa", "műanyag"],
    "teaches": ["ferde-kereszt"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex15",
    "type": "sentence-builder",
    "title": "Alkotmányos folytonosság",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["A", "Szent", "Korona", "Magyarország", "alkotmányos", "állami", "folytonosságát", "képviseli."],
    "correctSentence": "A Szent Korona Magyarország alkotmányos állami folytonosságát képviseli.",
    "english": "The Holy Crown represents Hungary's constitutional state continuity.",
    "teaches": ["allami-folytonossag", "megtestesit"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex16",
    "type": "multiple-choice",
    "title": "Bajor Gizella hercegnő",
    "instruction": "Ki volt Szent István király felesége?",
    "question": "Melyik országból származott Gizella királyné?",
    "options": ["Bajorországból", "Angliából", "Spanyolországból", "Oroszországból"],
    "correctIndex": 0,
    "explanation": "Gizella bajor hercegnő volt, II. Henrik német-római császár testvére.",
    "teaches": ["dinasztikus", "lovag"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex17",
    "type": "fill-blank",
    "title": "Érsekségek",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "István két érseki székhelyet alapított: Esztergomot és ___.",
    "correctAnswer": "Kalocsát",
    "options": ["Kalocsát", "Debrecent", "Miskolcot", "Szegedet"],
    "teaches": ["ersekseg", "egyhazmegye"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex18",
    "type": "sentence-builder",
    "title": "Magántulajdon törvénye",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["István", "király", "törvényei", "biztosították", "a", "békét", "és", "a", "rendet."],
    "correctSentence": "István király törvényei biztosították a békét és a rendet.",
    "english": "King Stephen's laws ensured peace and order.",
    "teaches": ["magantulajdon", "megszilardit"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex19",
    "type": "multiple-choice",
    "title": "Primogenitúra elve",
    "instruction": "Mit jelent a primogenitúra?",
    "question": "Kinek adja az öröklési jogot a primogenitúra elve?",
    "options": ["Az elsőszülött fiúgyermeknek", "A legidősebb nagybácsinak", "A falu legbátrabb harcosának", "A legidősebb női rokonnak"],
    "correctIndex": 0,
    "explanation": "A primogenitúra az elsőszülött fiú törvényes öröklési joga a nyugat-európai keresztény jogban.",
    "teaches": ["primogenitura", "oroklesi-rend"]
})
u4_cons_ex.append({
    "id": "b1-istvankiraly-consolidation.ex20",
    "type": "fill-blank",
    "title": "Államalapítás dicsősége",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Szent István műve megalapozta a magyar nemzet több mint ezeréves európai ___.",
    "correctAnswer": "megmaradását",
    "options": ["megmaradását", "eltűnését", "feledését", "vereségét"],
    "teaches": ["allamisag", "allamalapitas"]
})

write_json(EXERCISES_DIR / "b1-istvankiraly-consolidation-ex.json", {"exercises": u4_cons_ex})

write_json(LESSONS_DIR / "b1-istvankiraly-consolidation.json", make_consolidation_lesson(
    "lesson.b1.istvankiraly-consolidation",
    "Saint Stephen & State Foundation (1000) - Consolidation",
    [
        "Congratulations on completing Unit 4 of the Hungarian Citizenship Track!",
        "In this unit, you have mastered the foundational pillars of the Hungarian Christian Kingdom: Grand Prince Géza's reforms, the victory over Koppány, the coronation of 1000/1001 with the papal crown, the county (*vármegye*) and diocesan institutions, the moral testament of the *Intelmek*, and the Doctrine of the Holy Crown (*Szent Korona-tan*).",
        "Practice all 20 consolidation exercises to master the core constitutional and historical questions frequently asked in the citizenship naturalization examination."
    ],
    [
        "I can explain the historical milestones of Saint Stephen's reign (1000 coronation, 1083 canonization, August 20).",
        "I can describe the administrative (*vármegyék, ispánok*) and religious (*10 egyházmegye, tized*) structures of the medieval kingdom.",
        "I can analyze the legal significance of the Holy Crown and the *Intelmek*.",
        "I can confidently discuss Saint Stephen's state foundation in B1 Hungarian."
    ],
    "stories/world/b1/b1-istvankiraly.json",
    "exercises/b1/b1-istvankiraly-consolidation-ex.json",
    [f"b1-istvankiraly-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 4 (b1-istvankiraly) overhaul complete!")
