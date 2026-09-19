#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 21: Opinions & Arguments (b1-21)."""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_json(rel_path, data):
    full_path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

def build_unit_21_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.21.01",
        "lesson": "b1-21-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "állítólag", "translation": "allegedly, supposedly", "pos": "adverb"},
            {"lemma": "híresztelés", "translation": "rumor, hearsay, unverified report", "pos": "noun"},
            {"lemma": "megbízhatóság", "translation": "reliability, trustworthiness", "pos": "noun"},
            {"lemma": "forrás", "translation": "source (of information)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-21-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.21.02",
        "lesson": "b1-21-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "bizonyosság", "translation": "certainty, firm conviction", "pos": "noun"},
            {"lemma": "kétségtelenül", "translation": "undoubtedly, beyond doubt", "pos": "adverb"},
            {"lemma": "valószínűleg", "translation": "probably, likely", "pos": "adverb"},
            {"lemma": "feltételezés", "translation": "assumption, supposition", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-21-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.21.03",
        "lesson": "b1-21-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "érv", "translation": "argument, supporting point", "pos": "noun"},
            {"lemma": "alátámaszt", "translation": "to back up, substantiate, support", "pos": "verb"},
            {"lemma": "tény", "translation": "fact, verified reality", "pos": "noun"},
            {"lemma": "bizonyíték", "translation": "evidence, proof", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-21-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.21.04",
        "lesson": "b1-21-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "részben", "translation": "partly, in part", "pos": "adverb"},
            {"lemma": "egyetértés", "translation": "agreement, consensus", "pos": "noun"},
            {"lemma": "ellentmondás", "translation": "contradiction, discrepancy", "pos": "noun"},
            {"lemma": "szempont", "translation": "viewpoint, aspect, perspective", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-21-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.21.05",
        "lesson": "b1-21-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "érvelés", "translation": "line of argument, reasoning", "pos": "noun"},
            {"lemma": "meggyőző", "translation": "convincing, persuasive", "pos": "adjective"},
            {"lemma": "következtetés", "translation": "conclusion, deduction", "pos": "noun"},
            {"lemma": "összegzés", "translation": "summary, synthesizing wrap-up", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-21-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.21.01.evidential-allitolag",
        "title": "Evidential Particle: állítólag ('supposedly, allegedly')",
        "sections": [
            {
                "type": "text",
                "title": "Reporting Unverified Information",
                "content": "*Állítólag* indicates that the speaker is reporting hearsay without personal verification: *Állítólag holnap esni fog az eső.* ('Supposedly it will rain tomorrow.'). It functions like German *angeblich* or Spanish *al parecer / supuestamente*."
            },
            {
                "type": "examples",
                "title": "Sentences with állítólag",
                "items": [
                    {
                        "spanish": "Állítólag új szabályokat vezetnek be a cégnél a jövő hónaptól.",
                        "english": "Supposedly they are introducing new rules at the company from next month."
                    },
                    {
                        "spanish": "A hírek szerint a forrás nem volt teljesen megbízható.",
                        "english": "According to the news, the source was not entirely reliable."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.21.01.quoting-sources",
        "title": "Attributing Information: valaki szerint, a források szerint",
        "sections": [
            {
                "type": "text",
                "title": "Phrases for Source Attribution",
                "content": "To attribute statements in intellectual and media discourse: *X szerint...* ('according to X...'), *a szakértők véleménye alapján...* ('on the basis of experts' opinions...'): *A legfrissebb felmérések szerint nő a lakosság elégedettsége.*"
            },
            {
                "type": "examples",
                "title": "Source attribution phrases",
                "items": [
                    {
                        "spanish": "A professzor szerint a kérdés sokkal összetettebb annál, mint gondoltuk.",
                        "english": "According to the professor, the question is much more complex than we thought."
                    },
                    {
                        "spanish": "A hivatalos források szerint nem történt semmilyen szabálytalanság.",
                        "english": "According to official sources, no irregularity of any kind occurred."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.21.02.epistemic-probability",
        "title": "Degrees of Certainty: biztosan, kétségtelenül, valószínűleg",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Certainty vs Probability",
                "content": "Hungarian modal adverbs convey exact degrees of certainty: *kétségtelenül* (100% certainty, without doubt), *biztosan* (high certainty), *valószínűleg* (probability, ~70%), *esetleg / talán* (possibility, ~30%)."
            },
            {
                "type": "examples",
                "title": "Certainty scale",
                "items": [
                    {
                        "spanish": "Kétségtelenül ez volt a legjobb döntés a jelenlegi körülmények között.",
                        "english": "Undoubtedly this was the best decision under the current circumstances."
                    },
                    {
                        "spanish": "Valószínűleg még ma megérkezik a várva várt hivatalos válasz.",
                        "english": "The long-awaited official answer will probably arrive today."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.21.02.belief-verbs",
        "title": "Belief and Assumption Verbs: feltételez, meg van győződve",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Conviction",
                "content": "*Meg vagyok győződve arról, hogy...* ('I am convinced that...'), *Feltételezem, hogy...* ('I assume that...'), *Nem kétlem, hogy...* ('I do not doubt that...')."
            },
            {
                "type": "examples",
                "title": "Verbs of conviction in context",
                "items": [
                    {
                        "spanish": "Meg vagyok győződve arról, hogy a kitartó munka mindig meghozza az eredményt.",
                        "english": "I am convinced that persevering work always brings results."
                    },
                    {
                        "spanish": "Feltételezzük, hogy minden fél betartja az előzetes megállapodást.",
                        "english": "We assume that all parties will adhere to the preliminary agreement."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.21.03.backing-up-arguments",
        "title": "Backing Up Arguments: alátámaszt valamivel, tényekkel igazol",
        "sections": [
            {
                "type": "text",
                "title": "Substantiating Arguments",
                "content": "*Alátámaszt valamivel* ('supports with something') takes *-val/-vel*: *érvekkel támasztja alá az álláspontját* ('substantiates his position with arguments'). *Bizonyítja a tényt* ('proves the fact')."
            },
            {
                "type": "examples",
                "title": "Substantiating statements",
                "items": [
                    {
                        "spanish": "A kutató pontos adatokkal és tényekkel támasztotta alá az elméletét.",
                        "english": "The researcher supported his theory with accurate data and facts."
                    },
                    {
                        "spanish": "A vádak alaptalannak bizonyultak, mert nem volt semmilyen kézzelfogható bizonyíték.",
                        "english": "The accusations proved groundless because there was no tangible evidence."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.21.03.linking-evidence",
        "title": "Connecting Evidence: erre utal az is, hogy... / ezt bizonyítja",
        "sections": [
            {
                "type": "text",
                "title": "Evidence Linkers",
                "content": "To introduce evidence persuasively: *Erre utal az is, hogy...* ('This is also indicated by the fact that...'), *Ezt bizonyítja az a tény, hogy...* ('This is proven by the fact that...')."
            },
            {
                "type": "examples",
                "title": "Evidence linkers in context",
                "items": [
                    {
                        "spanish": "Erre utal az is, hogy évről évre növekszik az érdeklődés a kiállítás iránt.",
                        "english": "This is also indicated by the fact that interest in the exhibition grows year by year."
                    },
                    {
                        "spanish": "Ezt támasztja alá a legutóbbi nemzetközi statisztikai jelentés.",
                        "english": "This is supported by the most recent international statistical report."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.21.04.nuanced-agreement",
        "title": "Partial Agreement: Részben egyetértek, de...",
        "sections": [
            {
                "type": "text",
                "title": "Agreeing with Qualifications",
                "content": "In mature discussion: *Részben egyetértek azzal, hogy..., ugyanakkor figyelembe kell venni...* ('I partly agree that..., at the same time one must take into account...'). *Ebben a tekintetben igazad van, de...* ('In this respect you are right, but...')."
            },
            {
                "type": "examples",
                "title": "Qualified agreement phrases",
                "items": [
                    {
                        "spanish": "Részben egyetértek a javaslattal, de a költségeket túl magasnak találom.",
                        "english": "I partly agree with the proposal, but I find the costs too high."
                    },
                    {
                        "spanish": "Megértem az álláspontodat, mindazonáltal van egy másik fontos szempont is.",
                        "english": "I understand your point of view; nevertheless, there is another important aspect as well."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.21.04.perspective-aspects",
        "title": "Considering Perspectives: szempontjából, tekintettel arra, hogy",
        "sections": [
            {
                "type": "text",
                "title": "Perspectives and Angles",
                "content": "Postposition *szempontjából* ('from the standpoint of'): *gazdasági szempontból* ('from an economic standpoint'), *a biztonság szempontjából* ('from the safety point of view'). *Tekintettel arra, hogy...* ('considering that...')."
            },
            {
                "type": "examples",
                "title": "Perspective phrases",
                "items": [
                    {
                        "spanish": "Környezetvédelmi szempontból ez a beruházás rendkívül előnyös.",
                        "english": "From an environmental point of view, this investment is extremely advantageous."
                    },
                    {
                        "spanish": "Tekintettel arra, hogy kevés az időnk, gyors döntést kell hoznunk.",
                        "english": "Considering that we have little time, we must make a quick decision."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.21.05.structuring-arguments",
        "title": "Structuring an Argument: Először is, Továbbá, Végeredményben",
        "sections": [
            {
                "type": "text",
                "title": "Sequence Markers in Discourse",
                "content": "Organizing points logically: *Először is...* ('First of all...'), *Továbbá nem szabad elfelejteni...* ('Furthermore, we must not forget...'), *Végeredményben arra a következtetésre jutunk...* ('In the final analysis we reach the conclusion...')."
            },
            {
                "type": "examples",
                "title": "Argument structuring phrases",
                "items": [
                    {
                        "spanish": "Először is tisztáznunk kell a legfontosabb fogalmakat.",
                        "english": "First of all, we must clarify the most important concepts."
                    },
                    {
                        "spanish": "Továbbá fontos megvizsgálni a döntés hosszú távú hatásait is.",
                        "english": "Furthermore, it is important to examine the long-term effects of the decision as well."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.21.05.drawing-conclusions",
        "title": "Synthesizing: összegzésképpen megállapítható, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Drawing Formal Conclusions",
                "content": "*Összegzésképpen megállapítható, hogy...* ('In summary it can be established that...'), *Mindezek alapján levonhatjuk a következtetést, hogy...* ('On the basis of all this we can draw the conclusion that...')."
            },
            {
                "type": "examples",
                "title": "Synthesizing phrases in use",
                "items": [
                    {
                        "spanish": "Összegzésképpen megállapítható, hogy a vita mindkét fél számára hasznos volt.",
                        "english": "In summary, it can be established that the debate was useful for both parties."
                    },
                    {
                        "spanish": "A bemutatott érvek meggyőzően bizonyítják az elképzelés helyességét.",
                        "english": "The presented arguments convincingly prove the correctness of the idea."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-21-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-21-{padded}",
            "exercises": [
                {
                    "id": f"b1-21-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
                },
                {
                    "id": f"b1-21-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen az álláspontot vagy érvelést? (Lesson {i})",
                    "options": [
                        "Állítólag a bizottság már holnap meghozza a végső döntést.",
                        "Állítólag a bizottság holnap döntést hozni volt mert nem tudja.",
                        "Biztosan hogy a bizottság nem dönt semmit tegnap volna."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-21-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A vitában a professzor világos és logikus ____ támasztotta alá az álláspontját. (arguments - érvekkel)",
                    "answer": "érvekkel"
                },
                {
                    "id": f"b1-21-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Kétségtelenül ez a legmeggyőzőbb javaslat, ____ eddig hallottunk. (that - amit)",
                    "answer": "amit"
                },
                {
                    "id": f"b1-21-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'állítólag' kifejezés a hírekben?",
                    "options": [
                        "Azt, hogy az információ mások elmondásán alapul, és még nem teljesen igazolt.",
                        "Azt, hogy az esemény már ezer évvel ezelőtt lezárult.",
                        "Azt, hogy a hír teljesen titkos és tilos továbbadni."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-21-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Részben egyetértek a felvetéssel, ____ van egy másik fontos szempont is. (however - de)",
                    "answer": "de"
                },
                {
                    "id": f"b1-21-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "tényekkel", "alátámasztott", "érvelés", "minden", "vitában", "a", "legmeggyőzőbb."],
                    "solution": ["A", "tényekkel", "alátámasztott", "érvelés", "minden", "vitában", "a", "legmeggyőzőbb."]
                },
                {
                    "id": f"b1-21-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért fontos a megbízható források ellenőrzése az érvelés során?",
                    "options": [
                        "Mert a valódi tények és bizonyítékok erősítik meg a hiteles álláspontot.",
                        "Mert így minden vitát szavazás nélkül azonnal meg lehet nyerni.",
                        "Mert a források nélkül tilos bármilyen könyvet kinyitni."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-21-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-21-consolidation",
        "exercises": [
            {
                "id": "b1-21-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["állítólag", "allegedly"],
                    {"lemma": "alátámaszt", "translation": "substantiate"}.values() if False else ["alátámaszt", "substantiate"],
                    ["szempont", "viewpoint"],
                    ["következtetés", "conclusion"]
                ]
            },
            {
                "id": "b1-21-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat mutat be érett és árnyalt vitastílust?",
                "options": [
                    "Részben egyetértek az álláspontoddal, ugyanakkor a gazdasági szempontokat sem szabad figyelmen kívül hagyni.",
                    "Állítólag te tévedsz mert én mindig mindent jobban tudok volna.",
                    "Biztosan nincs semmi vita mert senki sem beszélhet semmit."
                ],
                "correct": 0
            },
            {
                "id": "b1-21-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A bemutatott bizonyítékok alapján a szakértők meggyőző ____ jutottak. (to a conclusion - következtetésre)",
                "answer": "következtetésre"
            },
            {
                "id": "b1-21-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Összegzésképpen megállapítható, ____ a felkészülés alapos volt. (that - hogy)",
                "answer": "hogy"
            },
            {
                "id": "b1-21-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "logikus", "következtetés", "és", "a", "kölcsönös", "tisztelet", "a", "kulturált", "vita", "alapja."],
                "solution": ["A", "logikus", "következtetés", "és", "a", "kölcsönös", "tisztelet", "a", "kulturált", "vita", "alapja."]
            },
            {
                "id": "b1-21-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kétségtelenül' szó egy érvelő szövegben?",
                "options": [
                    "Azt, hogy valami teljesen bizonyos és vitathatatlan.",
                    "Azt, hogy valami rendkívül bizonytalan és valószínűtlen.",
                    "Azt, hogy a kérdésről tilos véleményt nyilvánítani."
                ],
                "correct": 0
            },
            {
                "id": "b1-21-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vitapartnerem érvei rendkívül meg____ bizonyultak a záróbeszédben. (convincing - győzőnek)",
                "answer": "győzőnek"
            },
            {
                "id": "b1-21-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan érvel a diák a felelés során Karinthy halhatatlan szatírájában?",
                "options": [
                    "Látszólag mélyen elgondolkodva, sejtelmes szavakkal próbálja elhitetni, hogy mindent tud.",
                    "Hangosan felolvassa a tankönyv pontos definícióját hibátlanul.",
                    "Sírva fakad és kiszalad a tanteremből az udvarra."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-21-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.21.classic",
        "title": "A rossz tanuló felel",
        "level": "B1",
        "order": 21,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation of Frigyes Karinthy's classic 'A rossz tanuló felel' from 'Tanár úr kérem'. Called to the blackboard unprepared, student Ábrahám deploys every rhetorical weapon: dramatic pauses, evidential hints ('állítólag', 'biztosan'), clearing his throat, and attempting to construct an argument out of thin air while the teacher watches with ironic patience.",
        "characters": [
            "Ábrahám, a felelő diák",
            "A tanár úr",
            "Az osztály"
        ],
        "location": "Gimnáziumi tanterem, Budapest",
        "author": "Karinthy Frigyes",
        "work": "Tanár úr kérem",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A tanteremben hirtelen jeges csend támadt, amikor a tanár úr ujja végigfutott az osztálynapló névsorán. 'Ábrahám!' – hangzott a megfellebbezhetetlen ítélet. Ábrahám lassan, megfontoltan állt fel, mint egy filozófus, akinek a gondolatai messze a földi tények felett lebegnek."
            },
            {
                "type": "dialogue",
                "speaker": "A tanár úr",
                "text": "No, Ábrahám fiam, halljuk a mohácsi csata következményeit! Milyen érveket tud felhozni a korszak hanyatlása mellett?"
            },
            {
                "type": "narration",
                "text": "Ábrahám a táblához lépett, kezébe vette a krétát, mélyen a szemöldökét ráncolta, és köhintett egyet. Pontosan tudta: ha nincsenek tényei, a formával és a meggyőző hanghordozással kell pótolnia a tudást."
            },
            {
                "type": "dialogue",
                "speaker": "Ábrahám",
                "text": "Kérem tisztelettel... a kérdés kétségtelenül rendkívül összetett szempontból vizsgálható. Először is... állítólag már a csata előtt komoly nézeteltérések voltak a hadvezetésben. Valószínűleg Tomori Pál is érezte, hogy a források nem voltak egészen megbízhatóak..."
            },
            {
                "type": "narration",
                "text": "A tanár úr karba tette a kezét, szemüvege mögött huncut mosoly bujkált. Pontosan ismerte ezt a taktikát, ahol minden mondat egy újabb ígéret, de a bizonyíték soha nem érkezik meg."
            },
            {
                "type": "dialogue",
                "speaker": "A tanár úr",
                "text": "Igen, Ábrahám, ez mind szép általánosság. De mondjon egyetlen konkrét tényt is! Ki vezette az ellenséges sereget?"
            },
            {
                "type": "dialogue",
                "speaker": "Ábrahám",
                "text": "Tény, kérem szépen... a tény az, hogy történelmi szempontból tekintettel kell lennünk a szultánra... akit természetesen Szulejmánnak hívtak, s aki bizonyosan nem egyedül jött, hanem sereggel! Ezt a következtetést mindannyian levonhatjuk!"
            },
            {
                "type": "narration",
                "text": "Az osztály padsoraiban elfojtott kuncogás hullámzott végig. A tanár úr lassan bólintott, beírta a jegyet a naplóba, és szelíden csak annyit mondott: 'Ábrahám, a költői hozzáállás dicséretes, de a logikus érveléshez legközelebb tanulni is érdemes lesz!'"
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-21-karinthy.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Supposedly...", "Állítólag: Híresztelések és források"),
            "02": ("Degrees of Certainty", "Bizonyosság és feltételezés: Kétségtelenül, valószínűleg"),
            "03": ("Backing Up an Opinion", "Érvek és tények: Az álláspont alátámasztása"),
            "04": ("Agreeing, Up to a Point", "Árnyalt egyetértés: Részben igaz, de más szempontból..."),
            "05": ("A Structured Argument", "A felépített érvelés: Következtetés és összegzés")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.21-{padded}",
            "unit": 21,
            "title": en_title,
            "level": "B1",
            "grammar": "Evidentials & Probability Particles (állítólag, biztosan, valószínűleg) in Argumentation",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can express degrees of certainty and quote sources in Hungarian.",
                "I can back up opinions with facts and build structured arguments.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can express degrees of certainty and quote sources in Hungarian.",
                        "I can back up opinions with facts and build structured arguments.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-21-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-21-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-21-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-21-{padded}-ex.json",
                    "exerciseRefs": [f"b1-21-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-21-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.21-consolidation",
        "unit": 21,
        "title": "Unit 21 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Argumentation & Evidential Discourse Markers",
        "sections": [
            {
                "type": "story",
                "title": "A rossz tanuló felel (Karinthy Frigyes)",
                "ref": "stories/classics/b1/b1-21-karinthy.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-21-consolidation-ex.json",
                "exerciseRefs": [f"b1-21-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-21-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 21 (b1-21)!")

if __name__ == "__main__":
    build_unit_21_core()
