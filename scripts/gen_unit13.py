# -*- coding: utf-8 -*-
"""
Full Unit 13 Overhaul: Rákóczi's War of Independence (b1-rakoczi)
Lessons:
1. A szabadságharc kitörése és a brezáni kiáltvány (1703)
2. A szécsényi országgyűlés és a rendi konföderáció (1705)
3. Az ónodi országgyűlés és a Habsburg-ház trónfosztása (1707)
4. A kuruc hadsereg, a libertás és a belső nehézségek
5. A szatmári béke (1711) és Rákóczi emigrációja
Consolidation: Unit 13 Capstone (20 exercises)
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

def make_exercise_group(group_id, title, desc, exercises):
    return {
        "id": group_id,
        "title": title,
        "description": desc,
        "exercises": exercises
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
        "track": "citizenship",
        "estimatedMinutes": 15,
        "prerequisites": [],
        "grammar": [grammar_label],
        "vocabulary": [voc_ref],
        "culturalContext": "Magyar történelem és állampolgársági ismeretek (Honosítási tananyag)",
        "sections": sections
    }

# ==========================================
# LESSON 1: b1-rakoczi-01 (A szabadságharc kitörése 1703)
# ==========================================
story_1 = make_story(
    "story.b1.rakoczi.01",
    "A szabadságharc kitörése és a brezáni kiáltvány (1703)",
    "1703-ban II. Rákóczi Ferenc a lengyelországi Brezánban kibocsátotta kiáltványát, és a nemeseket meg jobbágyokat egyesítve harcba szólította a nemzetet a Habsburg önkény ellen.",
    "Brezán és a Tiszahát",
    ["Introductory narrative clauses (amikor, mihelyt, kibocsát)", "Patriotic proclamations in Hungarian"],
    ["II. Rákóczi Ferenc", "brezáni kiáltvány", "Esze Tamás", "zászlóbontás", "kurucok"],
    [
        "A 18. század hajnalán a Habsburg udvar elnyomása és az elviselhetetlen adók fegyverbe szólították a tiszaháti szegénylegényeket. 1703 tavaszán Esze Tamás tarpai jobbágy és társai felkeresték a Lengyelországban bujdosó fiatal és gazdag főurat, II. Rákóczi Ferencet, kérve, hogy álljon a felkelés élére.",
        "Rákóczi vállalta a történelmi küldetést. 1703 májusában Brezán várában kibocsátotta híres kiáltványát, amelyben harcba hívott 'minden nemest és nemtelent'. Vörös selyemzászlót küldött haza a latin jelmondattal: 'Cum Deo pro Patria et Libertate' (Istennel a hazáért és a szabadságért).",
        "Amikor Rákóczi 1703 júniusában Vereckénél átlépte a magyar határt, a nép ujjongva fogadta. Alig néhány hónap leforgása alatt a kuruc seregek felszabadították a Tiszántúlt és a Felvidéket, és a szabadságharc országos méretű nemzeti küzdelemmé vált."
    ],
    [
        {"lemma": "kiáltvány", "pos": "noun", "cefr": "B1", "gloss": "manifesto, proclamation"},
        {"lemma": "zászlóbontás", "pos": "noun", "cefr": "B1", "gloss": "unfurling of the banner, raising the flag of revolt"},
        {"lemma": "kuruc", "pos": "noun", "cefr": "B1", "gloss": "Kuruc (anti-Habsburg Hungarian insurgent)"},
        {"lemma": "bujdosik", "pos": "verb", "cefr": "B1", "gloss": "to live in exile/hiding"},
        {"lemma": "szabadságharc", "pos": "noun", "cefr": "B1", "gloss": "war of independence / freedom fight"}
    ],
    [
        {
            "question": "Mi volt II. Rákóczi Ferenc szabadságharcának híres latin jelmondata?",
            "options": ["Cum Deo pro Patria et Libertate (Istennel a hazáért és a szabadságért)", "Ne bántsd a magyart!", "Fényesebb a láncnál a kard", "Egy a haza"],
            "correctIndex": 0,
            "explanation": "Rákóczi zászlóira a 'Cum Deo pro Patria et Libertate' jelmondatot hímezték."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakoczi.01.json", story_1)

voc_1 = {
    "id": "voc.b1.rakoczi.01",
    "title": "A Rákóczi-szabadságharc kitörésének szókincse",
    "description": "Kiáltvány, zászlóbontás, kuruc felkelés, bujdosás és függetlenségi harc.",
    "entries": [
        {"lemma": "kiáltvány", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "proclamation, political manifesto", "examples": [{"hu": "Rákóczi brezáni kiáltványa fegyverbe szólította a népet.", "en": "Rákóczi's Brezán proclamation called the people to arms."}]}]},
        {"lemma": "zászlóbontás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unfurling of the flag, launching a revolt", "examples": [{"hu": "1703-ban megtörtént a kuruc zászlóbontás.", "en": "In 1703, the Kuruc banner was unfurled."}]}]},
        {"lemma": "kuruc", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Kuruc, Hungarian anti-Habsburg rebel soldier", "examples": [{"hu": "A kuruc katonák hűségesen követték a fejedelmet.", "en": "The Kuruc soldiers loyally followed the prince."}]}]},
        {"lemma": "bujdosik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to live in exile, hide from persecution", "examples": [{"hu": "A nemesek Lengyelországban bujdostak a császár elől.", "en": "The nobles lived in exile in Poland away from the Emperor."}]}]},
        {"lemma": "szabadságharc", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "war of independence, freedom fight", "examples": [{"hu": "A Rákóczi-szabadságharc nyolc évig tartott.", "en": "Rákóczi's War of Independence lasted eight years."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakoczi.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.rakoczi.01",
    "title": "Időhatározói és felhívó összetett mondatok (amikor, mihelyt, felszólít)",
    "description": "Narrating the ignition of popular movements and historical appeals.",
    "rules": [
        "Az 'amikor' és 'mihelyt' időhatározói kötőszavak a szabadságharc kulcspillanatainak egymásutániságát jelenítik meg.",
        "A felhívásokban és kiáltványokban a felszólító mód fejezi ki a közös cselekvésre ösztönzést: 'hívja a népet, hogy harcoljon'."
    ],
    "tables": [
        {"headers": ["Kötőszó / Szerkezet", "Jelentés", "Példa"], "rows": [
            ["amikor", "when", "Amikor Rákóczi megérkezett, a nép csatlakozott."],
            ["mihelyt", "as soon as", "Mihelyt kibocsátotta a kiáltványt, kitört a harc."],
            ["felszólít arra, hogy", "urges to", "Felszólította a nemzetet, hogy fogjon fegyvert."]
        ]}
    ],
    "examples": [
        {"spanish": "Amikor Rákóczi átlépte a határt Vereckénél, megkezdődött a szabadságharc.", "english": "When Rákóczi crossed the border at Verecke, the war of independence began."},
        {"spanish": "A kiáltványban felszólította a magyarokat, hogy álljanak ki a szabadságért.", "english": "In the proclamation, he called on Hungarians to stand up for freedom."},
        {"spanish": "Mihelyt kibontották a vörös zászlókat, ezrek csatlakoztak a sereghez.", "english": "As soon as the red banners were unfurled, thousands joined the army."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakoczi.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.rakoczi.01.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.01", "teaches": ["Rakoczi-1703"], "prompt": "Melyik évben tört ki a Rákóczi-szabadságharc?", "options": ["1703-ban", "1686-ban", "1711-ben", "1848-ban"], "correctIndex": 0, "explanation": "A Rákóczi-szabadságharc 1703 tavaszán tört ki a brezáni kiáltvánnyal."},
    {"id": "ex.b1.rakoczi.01.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.01", "teaches": ["kialtvany"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Rákóczi Brezán várában bocsátotta ki a híres *kiáltványát*.", "target": "kiáltványát"},
    {"id": "ex.b1.rakoczi.01.03", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.01", "teaches": ["amikor", "szabadsagharc"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["Amikor", "Rákóczi", "hazaérkezett,", "kitört", "a", "szabadságharc."], "target": "Amikor Rákóczi hazaérkezett, kitört a szabadságharc.", "english": "When Rákóczi arrived home, the war of independence broke out."},
    {"id": "ex.b1.rakoczi.01.04", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.01", "teaches": ["Esze-Tamas"], "prompt": "Ki volt a tiszaháti felkelés jobbágy származású vezetője, aki felkereste Rákóczit?", "options": ["Esze Tamás", "Bercsényi Miklós", "Károlyi Sándor", "Vak Bottyán"], "correctIndex": 0, "explanation": "Esze Tamás tarpai jobbágy vezette a delegációt Rákóczihoz Brezánba."},
    {"id": "ex.b1.rakoczi.01.05", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.01", "teaches": ["zaszlobontas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kuruc *zászlóbontás* összefogta a nemességet és a jobbágyságot.", "target": "zászlóbontás"},
    {"id": "ex.b1.rakoczi.01.06", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.01", "teaches": ["kuruc", "fejedelem"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["A", "kurucok", "lelkesen", "támogatták", "a", "fiatal", "fejedelmet."], "target": "A kurucok lelkesen támogatták a fiatal fejedelmet.", "english": "The Kuruc rebels enthusiastically supported the young prince."},
    {"id": "ex.b1.rakoczi.01.07", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.01", "teaches": ["jelmondat"], "prompt": "Mit jelent magyarul a 'Cum Deo pro Patria et Libertate'?", "options": ["Istennel a hazáért és a szabadságért", "Mindent a királyért", "Egy mindenkiért, mindenki egyért", "A törvény előtt mindannyian egyenlők vagyunk"], "correctIndex": 0, "explanation": "A latin jelmondat jelentése: 'Istennel a hazáért és a szabadságért'."},
    {"id": "ex.b1.rakoczi.01.08", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.01", "teaches": ["szabadsagharc"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Rákóczi-*szabadságharc* a magyar függetlenség jelképévé vált.", "target": "szabadságharc"}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.01.json", make_exercise_group("ex.b1.rakoczi.01", "A szabadságharc kitörése gyakorlatok", "Gyakorlatok az 1703-as eseményekről és az időhatározói mondatszerkezetekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.rakoczi.01",
    "A szabadságharc kitörése és a brezáni kiáltvány (1703)",
    "Időhatározói és felhívó szerkezetek (amikor, mihelyt, felszólít)",
    "Megismerjük a Rákóczi-szabadságharc kitörését, a brezáni kiáltványt, Esze Tamás szerepét és a híres jelmondatot.",
    ["Megérteni az 1703-as szabadságharc okait és kitörését", "Használni az időhatározói és felszólító kötőszavakat", "Ismerni a 'Cum Deo pro Patria et Libertate' jelmondat értelmét"],
    "story.b1.rakoczi.01",
    "voc.b1.rakoczi.01",
    "gr.b1.rakoczi.01",
    "ex.b1.rakoczi.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.rakoczi.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-rakoczi-02 (Szécsényi országgyűlés 1705)
# ==========================================
story_2 = make_story(
    "story.b1.rakoczi.02",
    "A szécsényi országgyűlés és a rendi konföderáció (1705)",
    "1705-ben a szécsényi mezőn a rendek szövetségre léptek (konföderáció), és II. Rákóczi Ferencet választották Magyarország vezérlő fejedelmévé.",
    "Szécsény",
    ["Constitutional and state-building vocabulary (konföderáció, vezérlő fejedelem, kancellária)", "Parliamentary resolutions"],
    ["szécsényi országgyűlés", "rendi konföderáció", "vezérlő fejedelem", "szenátus", "államszervezet"],
    [
        "A katonai sikerek után szükségessé vált az új, kuruc államszervezet törvényes megalapozása. 1705 szeptemberében a Nógrád vármegyei Szécsény melletti mezőn, sátortáborban gyűltek össze a magyar nemesek, főurak és városi küldöttek az országgyűlésre.",
        "A gyűlés történelmi határozatot hozott: a lengyel mintájú rendi konföderációt (államszövetséget) hozott létre. A rendek II. Rákóczi Ferencet egyhangúlag megválasztották Magyarország 'vezérlő fejedelmévé', teljhatalmat biztosítva számára a hadügy és a külügy irányításában.",
        "A fejedelem mellé egy huszonnégy tagú főúri tanácsot (szenátust) állítottak Bercsényi Miklós gróf vezetésével, valamint felállították a Gazdasági Tanácsot és a Kancelláriát. Ezzel Szécsényben létrejött az önálló, független kuruc államigazgatás."
    ],
    [
        {"lemma": "konföderáció", "pos": "noun", "cefr": "B1", "gloss": "confederation, alliance of estates"},
        {"lemma": "vezérlő fejedelem", "pos": "noun", "cefr": "B1", "gloss": "Ruling / Governing Prince"},
        {"lemma": "szenátus", "pos": "noun", "cefr": "B1", "gloss": "senate, noble governing council"},
        {"lemma": "államszervezet", "pos": "noun", "cefr": "B1", "gloss": "state organization / apparatus"},
        {"lemma": "teljhatalom", "pos": "noun", "cefr": "B1", "gloss": "plenipotentiary power, full authority"}
    ],
    [
        {
            "question": "Milyen tisztségre választotta meg az 1705-ös szécsényi országgyűlés II. Rákóczi Ferencet?",
            "options": ["Vezérlő fejedelemmé (a rendi konföderáció élére)", "Királynak", "Nádornak", "Kancellárnak"],
            "correctIndex": 0,
            "explanation": "Rákóczit a szécsényi gyűlésen Magyarország vezérlő fejedelmévé választották."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakoczi.02.json", story_2)

voc_2 = {
    "id": "voc.b1.rakoczi.02",
    "title": "A kuruc államszervezet és országgyűlés szókincse",
    "description": "Konföderáció, vezérlő fejedelem, szenátus, teljhatalom és közigazgatás.",
    "entries": [
        {"lemma": "konföderáció", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "confederation, league of estates", "examples": [{"hu": "A rendek konföderációt kötöttek a haza szabadságáért.", "en": "The estates formed a confederation for the freedom of the homeland."}]}]},
        {"lemma": "vezérlő fejedelem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Ruling Prince, Head of State in Kuruc Hungary", "examples": [{"hu": "Rákóczi vezérlő fejedelemként irányította a háborút.", "en": "Rákóczi directed the war as Ruling Prince."}]}]},
        {"lemma": "szenátus", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "governing senate council", "examples": [{"hu": "A 24 tagú szenátus segítette a fejedelem munkáját.", "en": "The 24-member senate assisted the Prince's work."}]}]},
        {"lemma": "államszervezet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "state organization and administration", "examples": [{"hu": "Szécsényben felépült az új államszervezet.", "en": "The new state apparatus was built in Szécsény."}]}]},
        {"lemma": "teljhatalom", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "full authority, plenipotentiary executive power", "examples": [{"hu": "A fejedelem teljhatalmat kapott a diplomáciában.", "en": "The Prince was granted full authority in diplomacy."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakoczi.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.rakoczi.02",
    "title": "Államszervezeti és intézményi szerkezetek (megválasztatik, felállít, biztosít)",
    "description": "Expressing state creation, elections, and constitutional delegations.",
    "rules": [
        "A hivatalos és intézményi nyelvhasználatban a választást, megbízást kifejező igék vonzatait alkalmazzuk: 'valamivé választ', 'valamivel megbíz'.",
        "A passzív vagy formális állítások a döntések intézményes súlyát hangsúlyozzák."
    ],
    "tables": [
        {"headers": ["Ige", "Vonzat / Szerkezet", "Példa"], "rows": [
            ["választ", "-vá / -vé választ", "Rákóczit fejedelemmé választották."],
            ["felállít", "-t felállít", "Felállították a Kancelláriát."],
            ["biztosít", "-nak / -nek biztosít", "Teljhatalmat biztosítottak a fejedelemnek."]
        ]}
    ],
    "examples": [
        {"spanish": "A szécsényi országgyűlésen Rákóczi Ferencet vezérlő fejedelemmé választották.", "english": "At the Diet of Szécsény, Ferenc Rákóczi was elected Ruling Prince."},
        {"spanish": "A rendek konföderációra léptek a nemzeti önállóság védelmében.", "english": "The estates entered into a confederation in defense of national independence."},
        {"spanish": "A szenátus Bercsényi vezetésével irányította a kormányzást.", "english": "The senate, under Bercsényi's leadership, guided the government."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakoczi.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.rakoczi.02.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.02", "teaches": ["szecsenyi-orszaggyules-1705"], "prompt": "Melyik évben tartották a rendi konföderációt megalapító szécsényi országgyűlést?", "options": ["1705-ben", "1703-ban", "1707-ben", "1711-ben"], "correctIndex": 0, "explanation": "A szécsényi országgyűlést 1705 őszén tartották."},
    {"id": "ex.b1.rakoczi.02.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.02", "teaches": ["konfoderacio"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A rendek szövetséget, azaz *konföderációt* hoztak létre a szabadságharc vezetésére.", "target": "konföderációt"},
    {"id": "ex.b1.rakoczi.02.03", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.02", "teaches": ["vezerlo-fejedelem", "valaszt"], "prompt": "Rakd össze az államszervezeti mondatot!", "chips": ["Rákóczit", "egyhangúlag", "vezérlő", "fejedelemmé", "választották", "meg."], "target": "Rákóczit egyhangúlag vezérlő fejedelemmé választották meg.", "english": "Rákóczi was unanimously elected Ruling Prince."},
    {"id": "ex.b1.rakoczi.02.04", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.02", "teaches": ["szenatus"], "prompt": "Ki vezette a Rákóczi mellé rendelt 24 tagú szenátust?", "options": ["Gróf Bercsényi Miklós", "Károlyi Sándor", "Esze Tamás", "Vak Bottyán"], "correctIndex": 0, "explanation": "Bercsényi Miklós gróf, Rákóczi legfőbb támasza állt a szenátus élén."},
    {"id": "ex.b1.rakoczi.02.05", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.02", "teaches": ["teljhatalom"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A fejedelem *teljhatalmat* kapott a hadügyek intézésében.", "target": "teljhatalmat"},
    {"id": "ex.b1.rakoczi.02.06", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.02", "teaches": ["allamszervezet", "szecseny"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Szécsényben", "létrejött", "az", "önálló", "kuruc", "államszervezet."], "target": "Szécsényben létrejött az önálló kuruc államszervezet.", "english": "The independent Kuruc state apparatus was established in Szécsény."},
    {"id": "ex.b1.rakoczi.02.07", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.02", "teaches": ["konfoderacio-modell"], "prompt": "Milyen mintát követett a szécsényi rendi konföderáció?", "options": ["A lengyel nemesi konföderáció mintáját", "A török vilajetrendszert", "Az abszolutista francia modellt", "A svájci kantonrendszert"], "correctIndex": 0, "explanation": "A magyar rendek a lengyel mintájú nemesi szövetséget (konföderációt) vették alapul."},
    {"id": "ex.b1.rakoczi.02.08", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.02", "teaches": ["szenatus"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A huszonnégy tagú *szenátus* hozta a legfontosabb kormányzati döntéseket.", "target": "szenátus"}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.02.json", make_exercise_group("ex.b1.rakoczi.02", "A szécsényi országgyűlés gyakorlatai", "Gyakorlatok a konföderációról és a kuruc államszervezeti szerkezetekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.rakoczi.02",
    "A szécsényi országgyűlés és a rendi konföderáció (1705)",
    "Államszervezeti és megbízási szerkezetek (-vá/-vé választ, felállít)",
    "Megismerjük a szécsényi országgyűlést, Rákóczi vezérlő fejedelemmé választását és a kuruc állam felépítését.",
    ["Megérteni az 1705-ös szécsényi országgyűlés határozatait", "Használni a tisztségviselési és választási nyelvtani formákat", "Ismerni a rendi konföderáció és a szenátus fogalmát"],
    "story.b1.rakoczi.02",
    "voc.b1.rakoczi.02",
    "gr.b1.rakoczi.02",
    "ex.b1.rakoczi.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.rakoczi.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-rakoczi-03 (Ónodi országgyűlés és trónfosztás 1707)
# ==========================================
story_3 = make_story(
    "story.b1.rakoczi.03",
    "Az ónodi országgyűlés és a Habsburg-ház trónfosztása (1707)",
    "1707-ben az ónodi országgyűlésen kimondták a Habsburg-dinasztia trónfosztását és a magyar történelemben először a nemesség adófizetését.",
    "Ónod mezeje",
    ["Emphatic and declarative proclamations (kinyilvánít, kimondatik, többé nem)", "Political dethronement acts"],
    ["ónodi országgyűlés", "trónfosztás", "Eb ura fakó", "közteherviselés", "I. József"],
    [
        "1707 nyarán a Sajó partján, Ónod mezővárosában gyűlt össze az országgyűlés rendkívül feszült nemzetközi és belső légkörben. A hadviselés költségei miatt a rendek között éles viták robbantak ki a pénzügyi terhekről és az adózásról.",
        "A feszült helyzetben Rákóczi és Bercsényi radikális lépésre szánta el magát a nemzetközi szövetségek megkötése érdekében. Bercsényi Miklós híres felkiáltása – 'Eb ura fakó! Mai naptól fogva József nem királyunk!' – után az országgyűlés ünnepélyesen kimondta a Habsburg-ház trónfosztását (detronizációját), kinyilvánítva Magyarország teljes állami függetlenségét.",
        "Ónodon egy másik korszakalkotó döntés is született: a háborús kiadások fedezésére – a magyar történelemben elsőként – a nemességre is adófizetési kötelezettséget róttak ki (közteherviselés). Ezzel az ónodi gyűlés a szabadságharc politikai csúcspontjává vált."
    ],
    [
        {"lemma": "trónfosztás", "pos": "noun", "cefr": "B1", "gloss": "dethronement, deposition of a dynasty"},
        {"lemma": "közteherviselés", "pos": "noun", "cefr": "B1", "gloss": "universal / shared taxation of all estates"},
        {"lemma": "kinyilvánít", "pos": "verb", "cefr": "B1", "gloss": "to proclaim, declare publicly"},
        {"lemma": "függetlenség", "pos": "noun", "cefr": "B1", "gloss": "independence, sovereignty"},
        {"lemma": "korszakalkotó", "pos": "adjective", "cefr": "B1", "gloss": "epoch-making, groundbreaking"}
    ],
    [
        {
            "question": "Mit mondott ki az 1707-es ónodi országgyűlés a Habsburg-házzal kapcsolatban?",
            "options": ["A Habsburg-ház trónfosztását (Magyarország függetlenségét)", "A császár azonnali megkoronázását", "A békekötést Béccsel", "A törökök elleni új szövetséget"],
            "correctIndex": 0,
            "explanation": "Ónodon 1707-ben kimondták a Habsburg-ház trónfosztását ('Eb ura fakó!')."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakoczi.03.json", story_3)

voc_3 = {
    "id": "voc.b1.rakoczi.03",
    "title": "A trónfosztás és függetlenség szókincse",
    "description": "Trónfosztás, közteherviselés, kinyilvánítás, függetlenség és korszakalkotó döntések.",
    "entries": [
        {"lemma": "trónfosztás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dethronement, deposition of monarchs", "examples": [{"hu": "Az ónodi országgyűlésen kimondták a trónfosztást.", "en": "At the Diet of Ónod, dethronement was proclaimed."}]}]},
        {"lemma": "közteherviselés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "shared taxation across all social classes", "examples": [{"hu": "Ónodon megkísérelték a közteherviselés bevezetését.", "en": "In Ónod, they attempted to introduce universal taxation."}]}]},
        {"lemma": "kinyilvánít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to declare, proclaim formally", "examples": [{"hu": "A rendek kinyilvánították a haza függetlenségét.", "en": "The estates proclaimed the homeland's independence."}]}]},
        {"lemma": "függetlenség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "national independence, freedom", "examples": [{"hu": "A nemzet a teljes függetlenségért harcolt.", "en": "The nation fought for complete independence."}]}]},
        {"lemma": "korszakalkotó", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "epoch-making, historic milestone", "examples": [{"hu": "Korszakalkotó törvényeket hoztak Ónodon.", "en": "Epoch-making laws were passed in Ónod."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakoczi.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.rakoczi.03",
    "title": "Nyomatékos kinyilatkoztató és tiltó szerkezetek (kinyilvánít, kimondatik, többé nem)",
    "description": "Formulating decisive political declarations and irrevocable legal breaks.",
    "rules": [
        "A kinyilvánító igék ('kinyilvánít', 'deklarál', 'kimond') a függetlenségi nyilatkozatok alapvető nyelvi eszközei.",
        "A 'többé nem' tagadó határozószó a végleges, vissza nem fordítható állapotváltozást fejezi ki: 'többé nem a királyunk'."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["kinyilvánít", "hivatalos kinyilatkoztatás", "Kinyilvánították a függetlenséget."],
            ["kimondatik", "ünnepélyes törvényi forma", "Kimondatott a dinasztia trónfosztása."],
            ["többé nem", "végleges tagadás", "József többé nem királyunk."]
        ]}
    ],
    "examples": [
        {"spanish": "Az országgyűlés kinyilvánította, hogy a Habsburgok nem uralkodnak Magyarországon.", "english": "The Diet declared that the Habsburgs would no longer rule in Hungary."},
        {"spanish": "Ónodon kimondatott a nemesség adófizetési kötelezettsége.", "english": "In Ónod, the tax liability of the nobility was decreed."},
        {"spanish": "A nemzet kinyilvánította a függetlenséget, elutasítva a császári uralmat.", "english": "The nation declared independence, rejecting imperial rule."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakoczi.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.rakoczi.03.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.03", "teaches": ["onodi-orszaggyules-1707"], "prompt": "Melyik évben mondta ki az ónodi országgyűlés a trónfosztást?", "options": ["1707-ben", "1703-ban", "1705-ben", "1711-ben"], "correctIndex": 0, "explanation": "Az ónodi országgyűlést 1707-ben tartották."},
    {"id": "ex.b1.rakoczi.03.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.03", "teaches": ["tronfosztas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az ónodi országgyűlésen kimondták a Habsburg-ház *trónfosztását*.", "target": "trónfosztását"},
    {"id": "ex.b1.rakoczi.03.03", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.03", "teaches": ["Eb-ura-fako", "tronfosztas"], "prompt": "Rakd össze Bercsényi híres felkiáltását helyes sorrendben!", "chips": ["Eb", "ura", "fakó,", "József", "nem", "királyunk!"], "target": "Eb ura fakó, József nem királyunk!", "english": "The dog is master of the wolf, Joseph is not our king!"},
    {"id": "ex.b1.rakoczi.03.04", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.03", "teaches": ["kozteherviszeles"], "prompt": "Milyen modern adózási elv jelent meg először Ónodon?", "options": ["A közteherviselés (a nemesség adófizetése a háború idejére)", "A fegyverváltság", "A tized eltörlése", "Az aranyvaluta bevezetése"], "correctIndex": 0, "explanation": "Ónodon a történelemben először a nemeseket is adófizetésre kötelezték a háborús célokra."},
    {"id": "ex.b1.rakoczi.03.05", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.03", "teaches": ["kinyilvanit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A rendek ünnepélyesen *kinyilvánították* az ország függetlenségét.", "target": "kinyilvánították"},
    {"id": "ex.b1.rakoczi.03.06", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.03", "teaches": ["fuggetlenseg", "allam"], "prompt": "Alkoss szabályos kinyilatkoztató mondatot!", "chips": ["Magyarország", "független", "és", "szabad", "állammá", "vált."], "target": "Magyarország független és szabad állammá vált.", "english": "Hungary became an independent and free state."},
    {"id": "ex.b1.rakoczi.03.07", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.03", "teaches": ["Bercsenyi-Milos"], "prompt": "Ki volt az ónodi trónfosztás legfőbb szónoka Rákóczi oldalán?", "options": ["Gróf Bercsényi Miklós", "Károlyi Sándor", "Bottyán János", "Radvánszky János"], "correctIndex": 0, "explanation": "Bercsényi Miklós mondta ki a trónfosztást sürgető híres mondatot."},
    {"id": "ex.b1.rakoczi.03.08", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.03", "teaches": ["korszakalkoto"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az ónodi döntések *korszakalkotó* jelentőségűek voltak a szabadságharcban.", "target": "korszakalkotó"}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.03.json", make_exercise_group("ex.b1.rakoczi.03", "Az ónodi trónfosztás gyakorlatai", "Gyakorlatok az 1707-es eseményekről és a kinyilatkoztató kifejezésekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.rakoczi.03",
    "Az ónodi országgyűlés és a Habsburg-ház trónfosztása (1707)",
    "Kinyilatkoztató és ünnepélyes szerkezetek (kinyilvánít, kimondatik)",
    "Részletesen elemezzük az 1707-es ónodi országgyűlést, a trónfosztást, a közteherviselés első megjelenését és a híres felkiáltást.",
    ["Megérteni az 1707-es ónodi trónfosztás hátterét és következményeit", "Használni a kinyilvánító és ünnepélyes nyelvtani szerkezeteket", "Ismerni az 'Eb ura fakó!' szállóigét és a közteherviselés korai kísérletét"],
    "story.b1.rakoczi.03",
    "voc.b1.rakoczi.03",
    "gr.b1.rakoczi.03",
    "ex.b1.rakoczi.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.rakoczi.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-rakoczi-04 (A kuruc hadsereg és libertás)
# ==========================================
story_4 = make_story(
    "story.b1.rakoczi.04",
    "A kuruc hadsereg, a libertás és a belső nehézségek",
    "A kuruc hadsereg bátor huszárai Vak Bottyán és Bercsényi vezetésével uralták a vidéket, de a pénzhiány, az 1708-as trencséni vereség és a pestis megpecsételte a harc sorsát.",
    "Trencsén és a Dunántúl",
    ["Economic and monetary terminology (libertás, kibocsát, infláció, fedezet)", "Military difficulties in long wars"],
    ["libertás", "rézpénz", "Vak Bottyán", "trencséni csata", "pestisjárvány"],
    [
        "A kuruc hadsereg gerincét a könnyűlovasság (a híres kuruc huszárok és hajdúk) alkotta, akik meglepetésszerű rajtaütéseikkel rettegésben tartották a császári labancokat. A Dunántúlt a legendás hírű idős tábornok, Vak Bottyán János foglalta el és védte sikeresen éveken át.",
        "A szabadságharc legnagyobb gondja a kincstár folyamatos pénzhiánya volt. Mivel a francia pénzügyi segély elmaradt, Rákóczi rézpénzt bocsátott ki a 'Pro Libertate' felirattal, amelyet a népnyelv libertásnak nevezett. Mivel azonban a rézpénznek nem volt valódi aranyfedezete, gyorsan elértéktelenedett, és gazdasági válságot okozott.",
        "1708-ban a trencséni csatában a kuruc sereg súlyos vereséget szenvedett, amelynek során a fejedelem lova felbukott, és maga Rákóczi is eszméletét vesztette. A katonai kudarcot pusztító pestisjárvány követte, amely tízezrek életét követelte és megtörte a lakosság ellenállási erejét."
    ],
    [
        {"lemma": "libertás", "pos": "noun", "cefr": "B1", "gloss": "Libertás (Kuruc copper coin inscribed Pro Libertate)"},
        {"lemma": "labanc", "pos": "noun", "cefr": "B1", "gloss": "Labanc (pro-Habsburg imperial soldier)"},
        {"lemma": "kibocsát", "pos": "verb", "cefr": "B1", "gloss": "to issue (currency, decree)"},
        {"lemma": "fedezet", "pos": "noun", "cefr": "B1", "gloss": "financial backing, collateral"},
        {"lemma": "pestisjárvány", "pos": "noun", "cefr": "B1", "gloss": "plague epidemic"}
    ],
    [
        {
            "question": "Hogy hívták Rákóczi híres rézpénzét, amelyen a 'Pro Libertate' felirat állt?",
            "options": ["Libertás", "Tallér", "Aranyforint", "Krajcár"],
            "correctIndex": 0,
            "explanation": "A 'Pro Libertate' feliratú kuruc rézpénzt libertásnak hívták."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakoczi.04.json", story_4)

voc_4 = {
    "id": "voc.b1.rakoczi.04",
    "title": "A kuruc hadviselés és gazdaság szókincse",
    "description": "Libertás, rézpénz, labanc ellenfél, fedezet, infláció és járványok.",
    "entries": [
        {"lemma": "libertás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Kuruc copper coin with 'Pro Libertate' inscription", "examples": [{"hu": "A fejedelem libertást veretett a hadsereg fizetésére.", "en": "The Prince minted libertás coins to pay the army."}]}]},
        {"lemma": "labanc", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Labanc, Austrian imperial soldier or supporter", "examples": [{"hu": "A kurucok és labancok évekig harcoltak egymással.", "en": "The Kuruc and Labanc forces fought each other for years."}]}]},
        {"lemma": "kibocsát", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to issue currency or decrees", "examples": [{"hu": "A kincstár papír- és rézpénzt bocsátott ki.", "en": "The treasury issued paper and copper currency."}]}]},
        {"lemma": "fedezet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "monetary backing, gold reserves", "examples": [{"hu": "Aranyfedezet nélkül a rézpénz elértéktelenedett.", "en": "Without gold backing, the copper money lost its value."}]}]},
        {"lemma": "pestisjárvány", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "bubonic plague epidemic", "examples": [{"hu": "A pestisjárvány megtizedelte a lakosságot.", "en": "The plague epidemic decimated the population."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakoczi.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.rakoczi.04",
    "title": "Pénzügyi és gazdasági szerkezetek (kibocsát, fedezetet nyújt, elértéktelenedik)",
    "description": "Describing monetary policies, economic crises, and inflation in historical essays.",
    "rules": [
        "A gazdaságtörténeti leírásokban a pénzkibocsátás, értékesés és fedezethiány speciális igéi szerepelnek.",
        "Az ok-okozati viszonyt a gazdasági folyamatokban az 'ennek következtében', 'hiányában' szerkezetekkel fejezzük ki."
    ],
    "tables": [
        {"headers": ["Ige / Szerkezet", "Jelentés", "Példa"], "rows": [
            ["kibocsát", "to issue", "Új pénzt bocsátottak ki."],
            ["elértéktelenedik", "to devalue / lose value", "A rézpénz gyorsan elértéktelenedett."],
            ["fedezetet nyújt", "to back / provide collateral", "Az állam nem tudott fedezetet nyújtani."]
        ]}
    ],
    "examples": [
        {"spanish": "Rákóczi rézpénzt bocsátott ki, hogy fizesse a katonák zsoldját.", "english": "Rákóczi issued copper coins in order to pay the soldiers' wages."},
        {"spanish": "Fedezet hiányában a libertás értéke folyamatosan csökkent.", "english": "Lacking backing, the value of the libertás continuously decreased."},
        {"spanish": "A trencséni vereség és a pestis megtörte a kuruc sereget.", "english": "The defeat at Trencsén and the plague broke the Kuruc army."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakoczi.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.rakoczi.04.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.04", "teaches": ["libertas"], "prompt": "Mi volt a 'libertás' a Rákóczi-szabadságharcban?", "options": ["A 'Pro Libertate' feliratú kuruc rézpénz", "A kurucok nemesi rangja", "Egy fontos békekötés", "Rákóczi lova"], "correctIndex": 0, "explanation": "A libertás a szabadságharc idején vert rézpénz volt."},
    {"id": "ex.b1.rakoczi.04.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.04", "teaches": ["kibocsat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A fejedelem szükségpénzként rézpénzt *bocsátott ki*.", "target": "bocsátott ki"},
    {"id": "ex.b1.rakoczi.04.03", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.04", "teaches": ["fedezet", "elertektelenedik"], "prompt": "Rakd össze a gazdasági mondatot!", "chips": ["Fedezet", "nélkül", "a", "pénz", "gyorsan", "elértéktelenedett."], "target": "Fedezet nélkül a pénz gyorsan elértéktelenedett.", "english": "Without backing, the money quickly devalued."},
    {"id": "ex.b1.rakoczi.04.04", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.04", "teaches": ["Vak-Bottyan"], "prompt": "Ki volt a Dunántúlt felszabadító híres, félszemű kuruc generális?", "options": ["Vak Bottyán János", "Esze Tamás", "Bercsényi Miklós", "Károlyi Sándor"], "correctIndex": 0, "explanation": "Vak Bottyán János volt a Dunántúl legendás kuruc hadvezére."},
    {"id": "ex.b1.rakoczi.04.05", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.04", "teaches": ["labanc"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kurucok ellenfelei a császárhű *labancok* voltak.", "target": "labancok"},
    {"id": "ex.b1.rakoczi.04.06", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.04", "teaches": ["trencseni-csata-1708"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["Az", "1708-as", "trencséni", "csata", "súlyos", "vereséget", "hozott."], "target": "Az 1708-as trencséni csata súlyos vereséget hozott.", "english": "The 1708 battle of Trencsén brought a heavy defeat."},
    {"id": "ex.b1.rakoczi.04.07", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.04", "teaches": ["pestis"], "prompt": "Milyen csapás tizedelte meg a hadsereget és a lakosságot a szabadságharc végén?", "options": ["Súlyos pestisjárvány", "Földrengés", "Tűzvész Budán", "Árvíz a Dunán"], "correctIndex": 0, "explanation": "A pusztító pestisjárvány tízezrek halálát okozta a hadjáratok végén."},
    {"id": "ex.b1.rakoczi.04.08", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.04", "teaches": ["pestisjarvany"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kitört *pestisjárvány* megtörte a harcolók erejét.", "target": "pestisjárvány"}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.04.json", make_exercise_group("ex.b1.rakoczi.04", "A kuruc hadsereg és gazdaság gyakorlatai", "Gyakorlatok a libertásról, a kuruc hadvezetésről és a gazdasági válságról.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.rakoczi.04",
    "A kuruc hadsereg, a libertás és a belső nehézségek",
    "Pénzügyi és gazdasági szerkezetek (kibocsát, fedezet, elértéktelenedik)",
    "Megismerjük a kuruc hadviselést, Vak Bottyán dunántúli hadjáratát, a libertás gazdaságtanát és a trencséni vereséget.",
    ["Megérteni a kuruc gazdaság kihívásait és a libertás szerepét", "Használni a pénzügyi és gazdasági kifejezéseket", "Ismerni Vak Bottyán és az 1708-as trencséni csata jelentőségét"],
    "story.b1.rakoczi.04",
    "voc.b1.rakoczi.04",
    "gr.b1.rakoczi.04",
    "ex.b1.rakoczi.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.rakoczi.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-rakoczi-05 (Szatmári béke 1711 és emigráció)
# ==========================================
story_5 = make_story(
    "story.b1.rakoczi.05",
    "A szatmári béke (1711) és Rákóczi emigrációja",
    "1711-ben a szatmári békével zárult a küzdelem: a kurucok letették a zászlókat a majtényi síkon, megőrizve a magyar rendi alkotmányt, míg Rákóczi a hűséges emigrációt választotta Rodostóban.",
    "Majtényi sík és Rodostó",
    ["Concluding evaluative synthesis (annak dacára, végső soron, megmarad)", "Exile and national legacy"],
    ["szatmári béke", "majtényi sík", "Károlyi Sándor", "amnesztia", "Rodostó"],
    [
        "1711 tavaszára a szabadságharc katonailag és gazdaságilag kimerült. Mialatt Rákóczi Oroszországban tárgyalt I. Péter cárral segítségért, megbízottja, gróf Károlyi Sándor tábornok megkötötte a kompromisszumos szatmári békét a bécsi udvarral.",
        "1711. május 1-jén a majtényi síkon tizenkétezer kuruc harcos méltósággal letette zászlóit a császári csapatok előtt, és hűségesküt tett. A béke amnesztiát (közkegyelmet) biztosított a felkelőknek, visszaállította a magyar rendi alkotmányt, garantálta a vallásszabadságot, és eltörölte a gyűlölt Újszerzeményi Bizottságot.",
        "Annak dacára, hogy a császár felajánlotta birtokai megtartását, II. Rákóczi Ferenc nem fogadta el az amnesztiát, mert nem akart hűségesküt tenni a Habsburgoknak. Hű kísérőivel, köztük Mikes Kelemennel a törökországi Rodostóban (Tekirdağ) telepedett le, ahol haláláig a magyar szabadság tiszta erkölcsi jelképe maradt."
    ],
    [
        {"lemma": "amnesztia", "pos": "noun", "cefr": "B1", "gloss": "amnesty, general pardon"},
        {"lemma": "kompromisszum", "pos": "noun", "cefr": "B1", "gloss": "compromise, mutual concession"},
        {"lemma": "emigráció", "pos": "noun", "cefr": "B1", "gloss": "political exile / emigration"},
        {"lemma": "méltóság", "pos": "noun", "cefr": "B1", "gloss": "dignity"},
        {"lemma": "erkölcsi", "pos": "adjective", "cefr": "B1", "gloss": "moral, ethical"}
    ],
    [
        {
            "question": "Hol élt száműzetésben II. Rákóczi Ferenc haláláig?",
            "options": ["A törökországi Rodostóban (Tekirdağ)", "Párizsban", "Bécsben", "Szentpéterváron"],
            "correctIndex": 0,
            "explanation": "Rákóczi hű társaival a Márvány-tenger partján, Rodostóban élt emigrációban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakoczi.05.json", story_5)

voc_5 = {
    "id": "voc.b1.rakoczi.05",
    "title": "A szatmári béke és rodostói emigráció szókincse",
    "description": "Amnesztia, kompromisszum, emigráció, hűség, méltóság és történelmi örökség.",
    "entries": [
        {"lemma": "amnesztia", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "amnesty, royal pardon for insurgents", "examples": [{"hu": "A szatmári béke teljes amnesztiát adott a kurucoknak.", "en": "The Peace of Szatmár granted full amnesty to the Kuruc rebels."}]}]},
        {"lemma": "kompromisszum", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "political compromise", "examples": [{"hu": "A szatmári béke ésszerű kompromisszumot teremtett.", "en": "The Peace of Szatmár created a reasonable compromise."}]}]},
        {"lemma": "emigráció", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "political exile abroad", "examples": [{"hu": "Rákóczi az emigrációt választotta a hódolás helyett.", "en": "Rákóczi chose exile instead of submission."}]}]},
        {"lemma": "méltóság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dignity, honor", "examples": [{"hu": "A katonák méltósággal tették le a fegyvert Majténynál.", "en": "The soldiers laid down their weapons with dignity at Majtény."}]}]},
        {"lemma": "erkölcsi", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "moral, ethical integrity", "examples": [{"hu": "Rákóczi a nemzet erkölcsi példaképe maradt.", "en": "Rákóczi remained the moral role model of the nation."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakoczi.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.rakoczi.05",
    "title": "Összegző és értékelő lezárások (annak dacára, végső soron, megmarad)",
    "description": "Synthesizing long-term historical outcomes and moral legacies.",
    "rules": [
        "Az 'annak dacára, hogy' (in spite of / despite the fact that) az emelkedett stílusú megengedést és erkölcsi kitartást hangsúlyozza.",
        "A 'végső soron' és 'mindent egybevetve' a történelmi események végső mérlegének megvonására szolgál."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["annak dacára, hogy", "nyomatékos ellentét", "Annak dacára, hogy vesztettek, megmaradt az alkotmány."],
            ["végső soron", "összegző mérlegelés", "Végső soron megmentették a nemzeti jogokat."],
            ["megmarad", "tartós eredmény", "A magyar nyelv és jogrend megmaradt."]
        ]}
    ],
    "examples": [
        {"spanish": "Annak dacára, hogy a szabadságharc elbukott, a nemesi alkotmány érvényben maradt.", "english": "Despite the fact that the freedom fight failed, the noble constitution remained in force."},
        {"spanish": "Végső soron a szatmári béke megakadályozta Magyarország beolvasztását a birodalomba.", "english": "Ultimately, the Peace of Szatmár prevented Hungary's absorption into the Empire."},
        {"spanish": "Rákóczi emléke mindmáig a tiszta hazaszeretet szimbóluma maradt.", "english": "Rákóczi's memory has remained the symbol of pure patriotism to this day."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakoczi.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.rakoczi.05.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.05", "teaches": ["szatmari-beke-1711"], "prompt": "Melyik évben és milyen békével ért véget a Rákóczi-szabadságharc?", "options": ["1711-ben a szatmári békével", "1707-ben az ónodi békével", "1699-ben a karlócai békével", "1705-ben a szécsényi békével"], "correctIndex": 0, "explanation": "A szabadságharc 1711-ben ért véget a szatmári békeszerződéssel."},
    {"id": "ex.b1.rakoczi.05.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.05", "teaches": ["amnesztia"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szatmári béke teljes *amnesztiát* biztosított a felkelőknek.", "target": "amnesztiát"},
    {"id": "ex.b1.rakoczi.05.03", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.05", "teaches": ["annak-dacara", "alkotmany"], "prompt": "Rakd össze az értékelő mondatot!", "chips": ["Annak", "dacára,", "hogy", "letették", "a", "fegyvert,", "megmaradt", "az", "alkotmány."], "target": "Annak dacára, hogy letették a fegyvert, megmaradt az alkotmány.", "english": "Despite the fact that they laid down arms, the constitution remained."},
    {"id": "ex.b1.rakoczi.05.04", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.05", "teaches": ["majtenyi-sik"], "prompt": "Hol tették le a zászlókat a kuruc csapatok 1711. május 1-jén?", "options": ["A majtényi síkon", "A mohácsi mezőn", "Ónod váránál", "Szécsény mellett"], "correctIndex": 0, "explanation": "A kuruc hadsereg a majtényi síkon tette le a zászlókat Károlyi Sándor vezetésével."},
    {"id": "ex.b1.rakoczi.05.05", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.05", "teaches": ["emigracio"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "II. Rákóczi Ferenc a törökországi *emigrációt* választotta.", "target": "emigrációt"},
    {"id": "ex.b1.rakoczi.05.06", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.05", "teaches": ["vegso-soron", "kompromisszum"], "prompt": "Alkoss összefoglaló mondatot!", "chips": ["Végső", "soron", "a", "béke", "megmentette", "az", "ország", "jogait."], "target": "Végső soron a béke megmentette az ország jogait.", "english": "Ultimately, the peace saved the country's rights."},
    {"id": "ex.b1.rakoczi.05.07", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.05", "teaches": ["Mikes-Kelemen"], "prompt": "Ki volt Rákóczi hű íródeákja, aki Törökországi leveleivel megörökítette a rodostói emigrációt?", "options": ["Mikes Kelemen", "Bercsényi Miklós", "Károlyi Sándor", "Apáczai Csere János"], "correctIndex": 0, "explanation": "Mikes Kelemen írta a híres Törökországi leveleket Rodostóból."},
    {"id": "ex.b1.rakoczi.05.08", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.05", "teaches": ["erkolcsi"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Rákóczi a nemzeti függetlenség tiszta *erkölcsi* példaképe maradt.", "target": "erkölcsi"}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.05.json", make_exercise_group("ex.b1.rakoczi.05", "A szatmári béke és emigráció gyakorlatai", "Gyakorlatok az 1711-es békéről, a rodostói évekről és az összegző szerkezetekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.rakoczi.05",
    "A szatmári béke (1711) és Rákóczi emigrációja",
    "Összegző és értékelő szerkezetek (annak dacára, végső soron)",
    "Összegezzük a szabadságharc lezárását, a szatmári kompromisszumot, Rákóczi rodostói emigrációját és történelmi örökségét.",
    ["Megérteni az 1711-es szatmári béke feltételeit és jelentőségét", "Használni az értékelő és összegző kifejezéseket", "Ismerni Rákóczi és Mikes Kelemen rodostói száműzetésének emlékét"],
    "story.b1.rakoczi.05",
    "voc.b1.rakoczi.05",
    "gr.b1.rakoczi.05",
    "ex.b1.rakoczi.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.rakoczi.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-rakoczi-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.rakoczi.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Rakoczi-evek"], "prompt": "Melyik évszámok közé esett a Rákóczi-szabadságharc?", "options": ["1703–1711", "1848–1849", "1686–1699", "1526–1541"], "correctIndex": 0, "explanation": "A Rákóczi-szabadságharc 1703-tól 1711-ig tartott."},
    {"id": "ex.b1.rakoczi.cons.02", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["kialtvany"], "prompt": "1703-ban Rákóczi a brezáni *kiáltványban* szólította harcba a nemzetet.", "sentence": "1703-ban Rákóczi a brezáni *kiáltványban* szólította harcba a nemzetet.", "target": "kiáltványban"},
    {"id": "ex.b1.rakoczi.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Cum-Deo"], "prompt": "Mit jelent a 'Cum Deo pro Patria et Libertate' jelmondat?", "options": ["Istennel a hazáért és a szabadságért", "Mindent a nemzetért", "A király és a haza védelmében", "Békével a jövőért"], "correctIndex": 0, "explanation": "A jelmondat: Istennel a hazáért és a szabadságért."},
    {"id": "ex.b1.rakoczi.cons.04", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Esze-Tamas"], "prompt": "A felkelés jobbágy származású tiszaháti vezére *Esze Tamás* volt.", "sentence": "A felkelés jobbágy származású tiszaháti vezére *Esze Tamás* volt.", "target": "Esze Tamás"},
    {"id": "ex.b1.rakoczi.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["amikor", "szabadsagharc"], "prompt": "Rakd össze a mondatot!", "chips": ["Amikor", "megérkezett,", "a", "nép", "fegyvert", "ragadott."], "target": "Amikor megérkezett, a nép fegyvert ragadott.", "english": "When he arrived, the people took up arms."},
    {"id": "ex.b1.rakoczi.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["szecsenyi-1705"], "prompt": "Hol választották Rákóczit vezérlő fejedelemmé 1705-ben?", "options": ["A szécsényi országgyűlésen", "Az ónodi gyűlésen", "Pozsonyban", "Debrecenben"], "correctIndex": 0, "explanation": "Szécsényben választották meg vezérlő fejedelemmé a rendi konföderáció élére."},
    {"id": "ex.b1.rakoczi.cons.07", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["vezerlo-fejedelem"], "prompt": "Rákóczi Ferencet Magyarország *vezérlő fejedelmévé* választotta a szécsényi országgyűlés.", "sentence": "Rákóczi Ferencet Magyarország *vezérlő fejedelmévé* választotta a szécsényi országgyűlés.", "target": "vezérlő fejedelmévé"},
    {"id": "ex.b1.rakoczi.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["szenatus", "Bercsenyi"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "szenátust", "Bercsényi", "Miklós", "gróf", "irányította."], "target": "A szenátust Bercsényi Miklós gróf irányította.", "english": "The senate was directed by Count Miklós Bercsényi."},
    {"id": "ex.b1.rakoczi.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["onodi-1707"], "prompt": "Melyik országgyűlésen mondták ki a Habsburg-ház trónfosztását 1707-ben?", "options": ["Az ónodi országgyűlésen", "A szécsényi gyűlésen", "A szatmári békénél", "A tordai diétán"], "correctIndex": 0, "explanation": "1707-ben az ónodi országgyűlésen mondták ki a trónfosztást."},
    {"id": "ex.b1.rakoczi.cons.10", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["tronfosztas"], "prompt": "Ónodon 'Eb ura fakó!' felkiáltással mondták ki a Habsburgok *trónfosztását*.", "sentence": "Ónodon 'Eb ura fakó!' felkiáltással mondták ki a Habsburgok *trónfosztását*.", "target": "trónfosztását"},
    {"id": "ex.b1.rakoczi.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["kinyilvanit", "fuggetlenseg"], "prompt": "Rakd össze a kinyilatkoztató mondatot!", "chips": ["A", "rendek", "kinyilvánították", "az", "ország", "teljes", "függetlenségét."], "target": "A rendek kinyilvánították az ország teljes függetlenségét.", "english": "The estates proclaimed the country's full independence."},
    {"id": "ex.b1.rakoczi.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["libertas"], "prompt": "Milyen felirat szerepelt Rákóczi rézpénzén, a libertáson?", "options": ["Pro Libertate", "Cum Deo", "Regnum Hungariae", "Iustitia et Pax"], "correctIndex": 0, "explanation": "A 'Pro Libertate' (A szabadságért) felirat szerepelt a rézpénzeken."},
    {"id": "ex.b1.rakoczi.cons.13", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Vak-Bottyan"], "prompt": "A Dunántúlt felszabadító kuruc generális *Vak Bottyán* János volt.", "sentence": "A Dunántúlt felszabadító kuruc generális *Vak Bottyán* János volt.", "target": "Vak Bottyán"},
    {"id": "ex.b1.rakoczi.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["fedezet", "elertektelenedik"], "prompt": "Alkoss gazdaságtörténeti mondatot!", "chips": ["Aranyfedezet", "nélkül", "a", "rézpénz", "gyorsan", "elértéktelenedett."], "target": "Aranyfedezet nélkül a rézpénz gyorsan elértéktelenedett.", "english": "Without gold backing, the copper money quickly devalued."},
    {"id": "ex.b1.rakoczi.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["szatmari-beke-1711"], "prompt": "Melyik békekötéssel zárult le a szabadságharc 1711-ben?", "options": ["A szatmári békével", "A karlócai békével", "A bécsi békével", "A linzi békével"], "correctIndex": 0, "explanation": "A szatmári békeszerződés zárta le a Rákóczi-szabadságharcot 1711-ben."},
    {"id": "ex.b1.rakoczi.cons.16", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["amnesztia"], "prompt": "A szatmári béke *amnesztiát* és a nemesi alkotmány megőrzését biztosította.", "sentence": "A szatmári béke *amnesztiát* és a nemesi alkotmány megőrzését biztosította.", "target": "amnesztiát"},
    {"id": "ex.b1.rakoczi.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["annak-dacara", "megmarad"], "prompt": "Rakd össze az összegző mondatot!", "chips": ["Annak", "dacára,", "hogy", "elbukott,", "a", "rendi", "alkotmány", "megmaradt."], "target": "Annak dacára, hogy elbukott, a rendi alkotmány megmaradt.", "english": "Despite the fact that it failed, the estate constitution remained."},
    {"id": "ex.b1.rakoczi.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Rodosto"], "prompt": "Melyik városban élt száműzetésben II. Rákóczi Ferenc Törökországban?", "options": ["Rodostóban (Tekirdağ)", "Konstantinápolyban", "Athénban", "Velencében"], "correctIndex": 0, "explanation": "Rákóczi Rodostóban töltötte emigrációs éveit."},
    {"id": "ex.b1.rakoczi.cons.19", "type": "fill-blank", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Mikes-Kelemen"], "prompt": "A rodostói bujdosók életét *Mikes Kelemen* örökítette meg leveleiben.", "sentence": "A rodostói bujdosók életét *Mikes Kelemen* örökítette meg leveleiben.", "target": "Mikes Kelemen"},
    {"id": "ex.b1.rakoczi.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.rakoczi.consolidation", "teaches": ["Rakoczi-ertekeles"], "prompt": "Miért számít a Rákóczi-szabadságharc nemzeti büszkeségnek?", "options": ["Mert megakadályozta a birodalmi beolvasztást és megőrizte a magyar önállóságot", "Mert elfoglalták Bécset", "Mert új királyt koronáztak", "Mert gazdaggá tette a jobbágyokat"], "correctIndex": 0, "explanation": "A szabadságharc megvédte a magyar rendi alkotmányt az abszolutizmussal szemben."}
]
write_json(EXERCISES_DIR / "ex.b1.rakoczi.consolidation.json", make_exercise_group("ex.b1.rakoczi.consolidation", "A Rákóczi-szabadságharc összefoglaló gyakorlatok", "Átfogó teszt az 1703–1711-es szabadságharc történetéről és nyelvtani szerkezeteiről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.rakoczi.consolidation",
    "title": "Rákóczi's War of Independence: Unit 13 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.rakoczi.01",
        "lesson.b1.rakoczi.02",
        "lesson.b1.rakoczi.03",
        "lesson.b1.rakoczi.04",
        "lesson.b1.rakoczi.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 13 Consolidation: Rákóczi's War of Independence (1703–1711)",
            "body": "Ebben az összefoglaló leckében áttekintjük a brezáni kiáltványt (1703), a szécsényi országgyűlést és a rendi konföderációt (1705), az ónodi trónfosztást (1707), a kuruc hadsereg mindennapjait és a libertást, valamint az 1711-es szatmári békét és a rodostói emigrációt."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A Rákóczi-szabadságharc legfőbb éveinek (1703, 1705, 1707, 1711) és helyszíneinek pontos ismerete",
                "Időhatározói, megbízási és összegző nyelvtani szerkezetek magabiztos alkalmazása",
                "A kuruc függetlenségi mozgalom kulcsfogalmainak (konföderáció, trónfosztás, libertás, amnesztia) birtoklása"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 13 Practice",
            "ref": "ex.b1.rakoczi.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor kezdődött és ért véget a szabadságharc (1703–1711)",
                "Ismerem a 'Cum Deo pro Patria et Libertate' és 'Eb ura fakó!' szállóigék hátterét",
                "Megértem a szécsényi és ónodi országgyűlés döntéseit",
                "Tudom, mit garantált a szatmári béke és hol élt Rákóczi emigrációban"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.rakoczi.consolidation.json", cons_lesson)

print("Unit 13 (b1-rakoczi) complete!")
