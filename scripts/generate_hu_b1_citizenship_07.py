#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 7: The Angevin & Later Medieval Kings (b1-anjouk)."""

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

def build_unit_7_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.anjouk.01",
        "lesson": "b1-anjouk-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "aranyforint", "translation": "gold florin", "pos": "noun"},
            {"lemma": "bányászat", "translation": "mining", "pos": "noun"},
            {"lemma": "nemesfém", "translation": "precious metal", "pos": "noun"},
            {"lemma": "kiskirály", "translation": "petty king, oligarch", "pos": "noun"},
            {"lemma": "pénzverés", "translation": "minting, coinage", "pos": "noun"},
            {"lemma": "jövedelem", "translation": "revenue, income", "pos": "noun"},
            {"lemma": "megszilárdít", "translation": "to consolidate, stabilize", "pos": "verb"},
            {"lemma": "kincstár", "translation": "treasury", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-anjouk-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.anjouk.02",
        "lesson": "b1-anjouk-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "királytalálkozó", "translation": "royal summit, meeting of kings", "pos": "noun"},
            {"lemma": "szövetség", "translation": "alliance, league", "pos": "noun"},
            {"lemma": "kereskedelmi út", "translation": "trade route", "pos": "noun"},
            {"lemma": "vámmegállapodás", "translation": "customs agreement", "pos": "noun"},
            {"lemma": "szomszédos", "translation": "neighbouring, adjacent", "pos": "adjective"},
            {"lemma": "közvetítő", "translation": "mediator, intermediary", "pos": "noun"},
            {"lemma": "elkerül", "translation": "to bypass, avoid", "pos": "verb"},
            {"lemma": "egyezség", "translation": "agreement, treaty", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-anjouk-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.anjouk.03",
        "lesson": "b1-anjouk-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "lovagkirály", "translation": "knight-king", "pos": "noun"},
            {"lemma": "ősiség", "translation": "entailment of noble estates (aviticitas)", "pos": "noun"},
            {"lemma": "kilenced", "translation": "ninth (feudal tax paid by serfs)", "pos": "noun"},
            {"lemma": "nemesség", "translation": "nobility", "pos": "noun"},
            {"lemma": "megerősít", "translation": "to confirm, reinforce", "pos": "verb"},
            {"lemma": "öröklés", "translation": "inheritance, succession", "pos": "noun"},
            {"lemma": "uralkodás", "translation": "reign, rule", "pos": "noun"},
            {"lemma": "törvénykönyv", "translation": "code of laws, statute book", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-anjouk-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.anjouk.04",
        "lesson": "b1-anjouk-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "császár", "translation": "emperor", "pos": "noun"},
            {"lemma": "végvár", "translation": "border fortress", "pos": "noun"},
            {"lemma": "végvárrendszer", "translation": "border fortress defence system", "pos": "noun"},
            {"lemma": "oszmán", "translation": "Ottoman", "pos": "adjective"},
            {"lemma": "hadjárat", "translation": "military campaign", "pos": "noun"},
            {"lemma": "fenyeget", "translation": "to threaten, menace", "pos": "verb"},
            {"lemma": "védelem", "translation": "defence, protection", "pos": "noun"},
            {"lemma": "lovagrend", "translation": "order of chivalry / knighthood", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-anjouk-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.anjouk.05",
        "lesson": "b1-anjouk-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kormányzó", "translation": "regent, governor", "pos": "noun"},
            {"lemma": "ostrom", "translation": "siege", "pos": "noun"},
            {"lemma": "törökverő", "translation": "Turk-beater (epithet of János Hunyadi)", "pos": "noun"},
            {"lemma": "déli harangszó", "translation": "noon bell, midday chimes", "pos": "noun"},
            {"lemma": "hősiesség", "translation": "heroism, bravery", "pos": "noun"},
            {"lemma": "győzelem", "translation": "victory, triumph", "pos": "noun"},
            {"lemma": "pestis", "translation": "plague, Black Death", "pos": "noun"},
            {"lemma": "emlékezet", "translation": "memory, commemoration", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-anjouk-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.anjouk.01.reported-chronicles",
        "title": "Chronicler Reporting: A krónikák szerint, úgy mondják",
        "sections": [
            {
                "type": "text",
                "title": "Attributing historical claims in Hungarian",
                "content": "When narrating medieval history, Hungarian frequently uses framing expressions like *a krónikák szerint* (according to the chronicles) or *azt mondják, hogy...* (it is said that...). This allows the speaker to report historical traditions without claiming direct eyewitness certainty."
            },
            {
                "type": "examples",
                "title": "Chronicler expressions in practice",
                "items": [
                    {
                        "spanish": "A krónikák szerint Károly Róbert értékálló aranyforintot veretett Körmöcbányán.",
                        "english": "According to the chronicles, Charles Robert minted stable gold florins in Körmöcbánya."
                    },
                    {
                        "spanish": "Úgy mondják, hogy a király kemény harcokban győzte le a lázadó kiskirályokat.",
                        "english": "It is said that the king defeated the rebellious petty oligarchs in fierce battles."
                    },
                    {
                        "spanish": "A korabeli források alapján a magyar kincstár bevételei jelentősen nőttek.",
                        "english": "Based on contemporary sources, revenues of the Hungarian royal treasury grew significantly."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Notice that *szerint* takes the nominative case (*a krónikák szerint*, *a történészek szerint*). It is an essential marker for natural historical and civic discussions."
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-anjouk-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.anjouk.02.reporting-agreements",
        "title": "Diplomatic Reporting: megállapodtak abban, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Reporting treaties and multilateral summits",
                "content": "In diplomatic narration, agreements between rulers are introduced with prepositional verbs: *megállapodik vmiben* (to agree on something) followed by *abban, hogy...* (in that...). This pattern is central to describing historical treaties like the 1335 Congress of Visegrád."
            },
            {
                "type": "examples",
                "title": "Treaty reporting structures",
                "items": [
                    {
                        "spanish": "A három király megállapodott abban, hogy új kereskedelmi utat nyitnak.",
                        "english": "The three kings agreed that they would open a new trade route."
                    },
                    {
                        "spanish": "Károly Róbert közvetítő szerepet vállalt a lengyel és cseh uralkodó között.",
                        "english": "Charles Robert undertook a mediator role between the Polish and Bohemian rulers."
                    },
                    {
                        "spanish": "A felek egyezséget kötöttek a bécsi árumegállító jog elkerüléséről.",
                        "english": "The parties concluded an agreement on bypassing Vienna's staple right."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-anjouk-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.anjouk.03.laws-and-epithets",
        "title": "Historical Titles & Law Enactments: úgy nevezték, megerősítette",
        "sections": [
            {
                "type": "text",
                "title": "Describing royal epithets and legal statutes",
                "content": "Kings often carry traditional epithets introduced by *úgy nevezték, mint...* (he was referred to as...) or *a nép ...-ként emlegette* (people referred to him as...). Legal acts use transitive past verbs like *megerősített* (confirmed) and *bevezetett* (introduced)."
            },
            {
                "type": "examples",
                "title": "1351 legal and royal descriptions",
                "items": [
                    {
                        "spanish": "Nagy Lajost Európa-szerte igazi lovagkirályként tisztelték.",
                        "english": "Louis the Great was respected across Europe as a true knight-king."
                    },
                    {
                        "spanish": "Az 1351-es törvényekben a király megerősítette az Aranybullát.",
                        "english": "In the laws of 1351, the king reaffirmed the Golden Bull."
                    },
                    {
                        "spanish": "Az ősiség törvénye kimondta, hogy a nemesi birtok a családon belül marad.",
                        "english": "The law of entailment stated that noble estates must remain within the family."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-anjouk-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.anjouk.04.threats-and-fortifications",
        "title": "Expressing Threat & Defence: fenyeget, kiépít, védelmet nyújt",
        "sections": [
            {
                "type": "text",
                "title": "Narrating geopolitical threats and defense lines",
                "content": "To explain border defense systems (*végvárrendszer*), Hungarian uses verbs of building and protection: *kiépít* (to build up fully), *védelmet nyújt* (to provide protection), and *fenyegetést jelent* (to pose a threat)."
            },
            {
                "type": "examples",
                "title": "Border defense narration",
                "items": [
                    {
                        "spanish": "A déli határon közeledő oszmán sereg súlyos veszélyt jelentett az országra.",
                        "english": "The Ottoman army approaching at the southern border posed a grave threat to the country."
                    },
                    {
                        "spanish": "Luxemburgi Zsigmond király erős végvárrendszert épített ki a védelemre.",
                        "english": "King Sigismund of Luxembourg built up a strong border fortress system for defence."
                    },
                    {
                        "spanish": "A déli erődítmények éveken át védelmet nyújtottak a betörések ellen.",
                        "english": "The southern fortifications provided protection against incursions for years."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-anjouk-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.anjouk.05.commemorative-synthesis",
        "title": "Historical Commemoration: azóta, emlékére, tiszteletére",
        "sections": [
            {
                "type": "text",
                "title": "Linking past triumphs to present traditions",
                "content": "Hungarian historical memory uses temporal and commemorative markers like *azóta* (ever since then), *emlékére* (in memory of him/it), and *tiszteletére* (in honor of him/it) to connect medieval events with national symbols such as the midday bell."
            },
            {
                "type": "examples",
                "title": "Commemorative sentences",
                "items": [
                    {
                        "spanish": "A hagyomány szerint a déli harangszó azóta hirdeti a nándorfehérvári győzelmet.",
                        "english": "According to tradition, the noon bell has proclaimed the Belgrade victory ever since."
                    },
                    {
                        "spanish": "Hunyadi János hősiessége megmentette a keresztény Európát az oszmán hódítástól.",
                        "english": "János Hunyadi's heroism saved Christian Europe from Ottoman conquest."
                    },
                    {
                        "spanish": "A pápa a keresztény világban imát és harangzúgást rendelt el a védők tiszteletére.",
                        "english": "The Pope ordered prayer and ringing of church bells across Christendom in honour of the defenders."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-anjouk-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.anjouk.01",
        "title": "Károly Róbert és a gazdasági rend",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Following the extinction of the Árpád dynasty, Charles Robert of Anjou restored central authority in Hungary, broke the power of the oligarchs, and created economic prosperity with Europe's most famous gold florin.",
        "characters": [],
        "location": "Magyar Királyság, Visegrád, Körmöcbánya",
        "grammar": ["reported-chronicles"],
        "vocabularyTopics": ["A gazdasági megújulás", "Az aranyforint"],
        "paragraphs": [
            {"type": "narration", "text": "Az Árpád-ház kihalása után súlyos zűrzavar és bizonytalanság uralkodott a Magyar Királyságban."},
            {"type": "narration", "text": "A tartományurak, akiket kiskirályoknak neveztek, saját hadsereggel uralkodtak hatalmas országrészek felett."},
            {"type": "narration", "text": "A fiatal Anjou Károly Róbert király azonban kitartó és kemény harcokban fokozatosan legyőzte a lázadó főurakat."},
            {"type": "narration", "text": "A király megerősítette a bányászatot Körmöcbányán és Selmecbányán, és bevezette az értékálló magyar aranyforintot."},
            {"type": "narration", "text": "A stabil pénzverés és az új vámrendszer révén a királyi kincstár gyorsan megtelt arannyal és ezüsttel."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk-01-karolyrobert.json", story_01)

    story_02 = {
        "id": "story.b1.anjouk.02",
        "title": "A visegrádi királytalálkozó",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In 1335, Charles Robert hosted a historic diplomatic congress in the royal palace of Visegrád with the kings of Bohemia and Poland, forging alliances and opening new trade routes.",
        "characters": [],
        "location": "Visegrád, Királyi Palota",
        "grammar": ["reporting-agreements"],
        "vocabularyTopics": ["Visegrád 1335", "Diplomácia"],
        "paragraphs": [
            {"type": "narration", "text": "1335 őszén a fenséges visegrádi királyi palotában rendkívüli nemzetközi találkozóra gyűltek össze a közép-európai uralkodók."},
            {"type": "narration", "text": "Károly Róbert magyar király meghívására János cseh király és Kázmér lengyel király érkezett Visegrádra."},
            {"type": "narration", "text": "A vendéglátó magyar király közvetítőként sikeresen kibékítette egymással a cseh és a lengyel uralkodót."},
            {"type": "narration", "text": "A három király megállapodott abban, hogy új kereskedelmi utat nyitnak, amely elkerüli a gazdag Bécs városának vámjait."},
            {"type": "narration", "text": "Ez a visegrádi királytalálkozó szilárd szövetséget teremtett, amely évszázadokon át formálta a térség történelmét."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk-02-visegrad.json", story_02)

    story_03 = {
        "id": "story.b1.anjouk.03",
        "title": "Nagy Lajos és az 1351-es törvények",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "King Louis the Great, celebrated as a chivalric monarch, expanded Hungary's power across Poland and Italy and enshrined fundamental noble liberties in the 1351 laws.",
        "characters": [],
        "location": "Buda, Székesfehérvár",
        "grammar": ["laws-and-epithets"],
        "vocabularyTopics": ["Lovagkor", "1351-es törvények"],
        "paragraphs": [
            {"type": "narration", "text": "Károly Róbert fia, Lajos király negyven éven át uralkodott a Magyar Királyság trónján."},
            {"type": "narration", "text": "Bátorsága, mély keresztény hite és lovagi erényei miatt a nép és az utókor Nagy Lajosnak nevezte őt."},
            {"type": "narration", "text": "1370-ben Lajos megörökölte a lengyel trónt is, így a két szomszédos ország perszonálunióba lépett egymással."},
            {"type": "narration", "text": "1351-ben a király megújította az Aranybullát, és bevezette az ősiség törvényét a nemesi birtokok védelmére."},
            {"type": "narration", "text": "Egyúttal kötelezővé tette a jobbágyok számára a kilenced megfizetését, ami egységes gazdasági rendet biztosított."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk-03-nagylajos.json", story_03)

    story_04 = {
        "id": "story.b1.anjouk.04",
        "title": "Zsigmond és a déli végvárrendszer",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Sigismund of Luxembourg, king of Hungary and Holy Roman Emperor, recognized the rising Ottoman peril and pioneered a formidable double chain of border fortresses.",
        "characters": [],
        "location": "Déli határvidék, Nándorfehérvár, Duna",
        "grammar": ["threats-and-fortifications"],
        "vocabularyTopics": ["Végvárrendszer", "Oszmán fenyegetés"],
        "paragraphs": [
            {"type": "narration", "text": "A tizennegyedik század végén egy új, hatalmas katonai erő jelent meg Európa déli határain: az Oszmán Birodalom."},
            {"type": "narration", "text": "Luxemburgi Zsigmond magyar király felismerte a halálos veszélyt, és 1396-ban nemzetközi keresztes hadjáratot vezetett Nikápolyhoz."},
            {"type": "narration", "text": "Bár a nikápolyi csata vereséggel végződött, Zsigmond új védelmi stratégiát dolgozott ki a birodalom megóvására."},
            {"type": "narration", "text": "A király megerősítette a déli határvidéket, és korszerű végvárrendszert épített ki a Duna és a Száva mentén."},
            {"type": "narration", "text": "Később Zsigmondot német-római császárrá koronázták, de Magyarország védelme mindig központi feladata maradt."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk-04-zsigmond.json", story_04)

    story_05 = {
        "id": "story.b1.anjouk.05",
        "title": "Hunyadi János és a nándorfehérvári diadal",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In July 1456, governor János Hunyadi and crusader friar John of Capistrano repelled Mehmed II's siege of Belgrade, securing Hungary and inspiring the worldwide midday church bell decree.",
        "characters": [],
        "location": "Nándorfehérvár (Belgrád)",
        "grammar": ["commemorative-synthesis"],
        "vocabularyTopics": ["Nándorfehérvár 1456", "Déli harangszó"],
        "paragraphs": [
            {"type": "narration", "text": "1456 nyarán II. Mehmed szultán százezres hadsereggel vette ostrom alá Magyarország kapuját, Nándorfehérvárat."},
            {"type": "narration", "text": "Hunyadi János kormányzó és a lánglelkű Kapisztrán János keresztesei siettek a vár védőinek megsegítésére."},
            {"type": "narration", "text": "A hős védők július 22-én áttörték az oszmán hajózárat a Dunán, és merész rohammal szétverték a szultán seregét."},
            {"type": "narration", "text": "A győzelem megállította az oszmán hódítást hetven évre, és a pápa elrendelte a déli harangszót a keresztény templomokban."},
            {"type": "narration", "text": "Bár a dicső Hunyadi János a csata után pestisben meghalt, neve a nemzeti önfeláldozás örök jelképévé vált."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk-05-nandorfehervar.json", story_05)

    story_combined = {
        "id": "story.b1.anjouk",
        "title": "Az Anjouk és a középkori királyok",
        "level": "B1",
        "order": 7,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The complete chronological saga of 14th and 15th century Hungary: from Charles Robert's financial revival and the 1335 Visegrád summit to Louis the Great's knightly empire, Sigismund's border fortifications, and Hunyadi's immortal victory at Nándorfehérvár in 1456.",
        "characters": [],
        "location": "Magyar Királyság, Visegrád, Nándorfehérvár",
        "grammar": ["reported-chronicles", "reporting-agreements", "laws-and-epithets", "threats-and-fortifications", "commemorative-synthesis"],
        "vocabularyTopics": ["Anjou-kor", "Visegrádi találkozó", "1351-es törvények", "Nándorfehérvár", "Déli harangszó"],
        "paragraphs": [
            {"type": "narration", "text": "Az Árpád-ház 1301-es kihalása után Károly Róbert személyében egy tehetséges nápolyi Anjou herceg lépett a magyar trónra. Kemény harcokban legyőzte a tartományurakat, megreformálta a bányászatot Körmöcbányán, és stabil aranyforintjával megalapozta a virágzó gazdaságot."},
            {"type": "narration", "text": "1335-ben Károly Róbert a visegrádi királyi palotában vendégül látta a cseh és lengyel uralkodót. A híres visegrádi királytalálkozón a királyok szövetséget kötöttek és új kereskedelmi utat nyitottak, megkerülve a bécsi vámokat."},
            {"type": "narration", "text": "Fia, Nagy Lajos lovagkirály uralkodása idején a Magyar Királyság európai nagyhatalommá vált, és perszonálunióban egyesült Lengyelországgal. Az 1351-es törvények megerősítették a nemesi szabadságjogokat és bevezették az ősiség törvényét."},
            {"type": "narration", "text": "A tizennegyedik század végén Luxemburgi Zsigmond király — a későbbi német-római császár — felismerte az oszmán veszedelmet, és erős végvárrendszer kiépítésével védte a déli határokat."},
            {"type": "narration", "text": "Végül 1456 júliusában Nándorfehérvárnál Hunyadi János kormányzó fényes győzelmet aratott II. Mehmed szultán ostromló serege felett. Ez a diadal hetven évre megállította az oszmán előrenyomulást, és azóta is minden délben a harangszó hirdeti a hősök emlékét."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-anjouk.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-anjouk-01",
        "exercises": [
            {
                "id": "b1-anjouk-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["aranyforint", "gold florin"],
                    ["bányászat", "mining"],
                    ["nemesfém", "precious metal"],
                    ["kincstár", "treasury"]
                ]
            },
            {
                "id": "b1-anjouk-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["kiskirály", "petty king / oligarch"],
                    ["pénzverés", "minting"],
                    ["jövedelem", "revenue / income"],
                    ["megszilárdít", "to consolidate"]
                ]
            },
            {
                "id": "b1-anjouk-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt Károly Róbert, és melyik dinasztiából származott?",
                "options": [
                    "Az Anjou-házból származó magyar király, aki helyreállította az ország rendjét.",
                    "A Habsburg-ház első császára.",
                    "Az utolsó Árpád-házi uralkodó."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol verték a híres középkori magyar aranyforintot?",
                "options": ["Körmöcbányán.", "Bécsben.", "Rómában."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Complete with the chronicler phrase: '... Károly Róbert erős kézzel kormányzott.'",
                "options": ["A krónikák szerint", "A krónikákban", "A krónikákhoz"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "A király megbízható és értékálló [aranyforintot] vezetett be az országban.",
                "options": ["aranyforintot", "kiskirályt", "ostromot"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért fontos a honosítási vizsgán Károly Róbert gazdasági reformja?",
                "options": [
                    "Mert a virágzó bányászat és az aranyforint révén Magyarország gazdasági hatalommá vált.",
                    "Mert ő hozta létre az Európai Uniót.",
                    "Mert megszüntette a hadsereget."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kiket hívtak 'kiskirályoknak' a 14. század elején?",
                "options": [
                    "A hatalmaskodó tartományurakat, akik nem engedelmeskedtek a központi királyi hatalomnak.",
                    "A király gyermekeit.",
                    "A szomszédos országok uralkodóit."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen hatással volt a nemesfémbányászat a királyi kincstárra?",
                "options": [
                    "Jelentősen megnövelte a kincstár bevételeit és stabil valutát biztosított.",
                    "Tönkretette az állami pénzügyeket.",
                    "Bezárta a városi piacokat."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-anjouk-02",
        "exercises": [
            {
                "id": "b1-anjouk-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["királytalálkozó", "royal summit"],
                    ["szövetség", "alliance"],
                    ["kereskedelmi út", "trade route"],
                    ["vámmegállapodás", "customs agreement"]
                ]
            },
            {
                "id": "b1-anjouk-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szomszédos", "neighbouring"],
                    ["közvetítő", "mediator"],
                    ["elkerül", "to bypass"],
                    ["egyezség", "pact / treaty"]
                ]
            },
            {
                "id": "b1-anjouk-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikor zajlott a híres visegrádi királytalálkozó?",
                "options": ["1335-ben.", "1222-ben.", "1526-ban."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik három ország királyai találkoztak Visegrádon 1335-ben?",
                "options": [
                    "Magyarország, Csehország és Lengyelország királyai.",
                    "Magyarország, Ausztria és Anglia királyai.",
                    "Franciaország, Spanyolország és Magyarország királyai."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "A három uralkodó megállapodott abban, hogy ...",
                "options": [
                    "új kereskedelmi utat nyitnak.",
                    "új kereskedelmi utat nyitottak régen.",
                    "nem beszélnek egymással soha."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "Károly Róbert [közvetítő] szerepet játszott a cseh és a lengyel király békéjében.",
                "options": ["közvetítő", "aranyforint", "ostrom"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért hívják a mai közép-európai együttműködést 'Visegrádi Négyeknek' (V4)?",
                "options": [
                    "Mert az 1335-ös történelmi visegrádi királytalálkozó örökségére épül.",
                    "Mert ott épült fel az első parlament.",
                    "Mert ott született az Alaptörvény."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen gazdasági célt szolgált az új visegrádi kereskedelmi út?",
                "options": [
                    "Hogy elkerüljék Bécs árumegállító jogát és a magas vámokat.",
                    "Hogy a Dunát eltereljék a várostól.",
                    "Hogy leállítsák a kereskedelmet."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol fogadta Károly Róbert a vendég uralkodókat?",
                "options": ["A visegrádi királyi palotában.", "A budai várban.", "Esztergomban."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-anjouk-03",
        "exercises": [
            {
                "id": "b1-anjouk-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["lovagkirály", "knight-king"],
                    ["ősiség", "entailment (aviticitas)"],
                    ["kilenced", "ninth (peasant tax)"],
                    ["nemesség", "nobility"]
                ]
            },
            {
                "id": "b1-anjouk-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["megerősít", "to confirm / reinforce"],
                    ["öröklés", "inheritance"],
                    ["uralkodás", "reign"],
                    ["törvénykönyv", "law book"]
                ]
            },
            {
                "id": "b1-anjouk-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért nevezték Nagy Lajost 'lovagkirálynak'?",
                "options": [
                    "Mert személyes bátorsága, lovagiassága és mély hite példaképül szolgált Európában.",
                    "Mert csak lovon szeretett utazni.",
                    "Mert ő készítette a páncélokat a vitézeknek."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik törvényt vezette be Nagy Lajos 1351-ben a nemesi birtok öröklésére?",
                "options": ["Az ősiség törvényét (aviticitas).", "A jobbágyfelszabadítást.", "A szabad költözés jogát."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Nagy Lajost Európa-szerte igazi lovagkirály... tisztelték.",
                "options": ["-ként", "-ban", "-hoz"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "Az 1351-es törvényekben a király [megerősítette] a magyar nemesség jogait.",
                "options": ["megerősítette", "megszüntette", "elfelejtette"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit mondott ki az ősiség (aviticitas) törvénye?",
                "options": [
                    "Hogy a nemesi földbirtok nem adható el, hanem a családon belül öröklődik.",
                    "Hogy a birtok a királyé lesz azonnal.",
                    "Hogy a jobbágyok feloszthatják a földet egymás között."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mi volt a 'kilenced' az 1351-es törvények szerint?",
                "options": [
                    "A földesúrnak fizetendő egységes terményadó a jobbágyoktól.",
                    "A kilencedik hónapban fizetendő vám.",
                    "A királyi udvar személyzete."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik másik országnak lett a királya Nagy Lajos 1370-ben?",
                "options": ["Lengyelországnak.", "Angliának.", "Spanyolországnak."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-anjouk-04",
        "exercises": [
            {
                "id": "b1-anjouk-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["császár", "emperor"],
                    ["végvár", "border fortress"],
                    ["végvárrendszer", "border defense system"],
                    ["oszmán", "Ottoman"]
                ]
            },
            {
                "id": "b1-anjouk-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hadjárat", "military campaign"],
                    ["fenyeget", "to threaten"],
                    ["védelem", "defence"],
                    ["lovagrend", "order of knighthood"]
                ]
            },
            {
                "id": "b1-anjouk-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen birodalmi címet nyert el Luxemburgi Zsigmond a magyar királyi korona mellett?",
                "options": [
                    "Német-római császárrá választották.",
                    "Orosz cár lett.",
                    "Angol király lett."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik felkelő birodalom fenyegette közvetlenül Magyarország déli határait?",
                "options": ["Az Oszmán (Török) Birodalom.", "A Római Birodalom.", "A Mongol Birodalom."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Híre ment Európában, hogy az oszmán hadsereg Magyarországot ...",
                "options": ["fenyegeti.", "fenyegette volt.", "fenyegetne."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "A király megerősített [végvárrendszert] épített ki a déli folyók mentén.",
                "options": ["végvárrendszert", "kiskirályt", "bizonyítványt"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mi volt a célja a déli végvárrendszer felépítésének?",
                "options": [
                    "Megállítani az oszmán betöréseket a Magyar Királyság és Európa határán.",
                    "Megakadályozni a magyarok utazását délre.",
                    "Vámot szedni a belföldi halászoktól."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik fontos nemzetközi egyházi zsinatot hívta össze Zsigmond császár?",
                "options": [
                    "A konstanzi zsinatot (1414–1418).",
                    "A tridenti zsinatot.",
                    "A pannonhalmi gyűlést."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik híres lovagrendet alapította Zsigmond király 1408-ban?",
                "options": ["A Sárkány Lovagrendet.", "A Máltai Lovagrendet.", "A Templomos Rendt."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-anjouk-05",
        "exercises": [
            {
                "id": "b1-anjouk-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["kormányzó", "governor / regent"],
                    ["ostrom", "siege"],
                    ["törökverő", "Turk-beater (Hunyadi)"],
                    ["déli harangszó", "noon bell"]
                ]
            },
            {
                "id": "b1-anjouk-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hősiesség", "heroism"],
                    ["győzelem", "victory"],
                    ["pestis", "plague"],
                    ["emlékezet", "historical memory"]
                ]
            },
            {
                "id": "b1-anjouk-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikor zajlott a nándorfehérvári diadal?",
                "options": ["1456 júliusában.", "1526 augusztusában.", "1241 tavaszán."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki vezette a magyar felmentő sereget Nándorfehérvár védelmében?",
                "options": [
                    "Hunyadi János kormányzó és Kapisztrán János keresztesei.",
                    "Szent István király.",
                    "Károly Róbert király."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "A hagyomány szerint a déli harangszó ... hirdeti a keresztény győzelmet.",
                "options": ["azóta", "azalatt", "azelőtt"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex05",
                "type": "fill-in-the-blank",
                "category": "grammar",
                "sentence": "Hunyadi János [hősiessége] és katonai tehetsége megvédte Európa kapuját.",
                "options": ["hősiessége", "kincstára", "bányászata"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mire emlékeztet a templomok déli harangszója mind a mai napig?",
                "options": [
                    "A nándorfehérvári diadalra és a hős védők imádságos helytállására.",
                    "A tatárjárás végére.",
                    "A trianoni békére."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen szultán vezette a török ostromot Nándorfehérvárnál?",
                "options": [
                    "II. Mehmed szultán, Konstantinápoly hódítója.",
                    "Szulejmán szultán.",
                    "Batu kán."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan halt meg Hunyadi János a fényes diadal után?",
                "options": [
                    "A táborban kitört pestisjárványban hunyt el.",
                    "Csatában esett el nyílvesszőtől.",
                    "Időskori békés betegségben."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-anjouk-consolidation",
        "exercises": [
            {
                "id": "b1-anjouk-consolidation.ex01",
                "type": "matching",
                "category": "review",
                "pairs": [
                    ["Károly Róbert", "aranyforint és körmöcbányai pénzverés"],
                    ["1335", "visegrádi királytalálkozó"],
                    ["Nagy Lajos", "lovagkirály és 1351-es törvények"],
                    ["Hunyadi János", "nándorfehérvári diadal 1456-ban"]
                ]
            },
            {
                "id": "b1-anjouk-consolidation.ex02",
                "type": "matching",
                "category": "review",
                "pairs": [
                    ["ősiség", "nemesi birtok elidegeníthetetlensége"],
                    ["kilenced", "jobbágyi terményadó a földesúrnak"],
                    ["végvárrendszer", "déli határvédelmi erődítmények"],
                    ["déli harangszó", "emlékezés a nándorfehérvári győzelemre"]
                ]
            },
            {
                "id": "b1-anjouk-consolidation.ex03",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik évben halt ki az Árpád-ház férfiága?",
                "options": ["1301-ben.", "1222-ben.", "1456-ban."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex04",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik király hívta össze az 1335-ös visegrádi találkozót?",
                "options": ["Károly Róbert.", "Nagy Lajos.", "Zsigmond."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex05",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen országgal lépett perszonálunióba Magyarország Nagy Lajos alatt 1370-ben?",
                "options": ["Lengyelországgal.", "Ausztriával.", "Oroszországgal."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex06",
                "type": "multiple-choice",
                "category": "review",
                "question": "Mit jelent az 'ősiség' kifejezés?",
                "options": [
                    "A nemesi birtok a nemzetségen belül öröklődik, eladni nem szabad.",
                    "A legrégebbi falu joga.",
                    "A királyi aranybányák adója."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex07",
                "type": "multiple-choice",
                "category": "review",
                "question": "Kivel szemben győzött Hunyadi János 1456-ban Nándorfehérvárnál?",
                "options": [
                    "II. Mehmed oszmán szultán seregével szemben.",
                    "Batu kán mongol hadával szemben.",
                    "A német-római császárral szemben."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex08",
                "type": "multiple-choice",
                "category": "review",
                "question": "Miért szól délben a harang az összes keresztény templomban?",
                "options": [
                    "A nándorfehérvári győzelem tiszteletére elrendelt pápai ima miatt.",
                    "Hogy jelezze az ebédszünetet.",
                    "Szent István megkoronázására emlékezve."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex09",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen szövetség viseli ma a visegrádi királytalálkozó nevét?",
                "options": ["A Visegrádi Négyek (V4).", "A NATO.", "Az OECD."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex10",
                "type": "multiple-choice",
                "category": "review",
                "question": "Kik voltak a 'kiskirályok' Károly Róbert uralkodásának elején?",
                "options": [
                    "A lázadó tartományurak (oligarchák), mint Csák Máté.",
                    "A kisgyermekként megkoronázott hercegek.",
                    "A falu vezetői."
                ],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex11",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik bányavárosban verték a híres aranyforintokat?",
                "options": ["Körmöcbányán.", "Pécsen.", "Győrben."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex12",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hogyan nevezték a déli határ védelmére felépített erődök láncolatát?",
                "options": ["Végvárrendszernek.", "Kőfalnak.", "Városfalnak."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex13",
                "type": "multiple-choice",
                "category": "review",
                "question": "Ki harcolt Hunyadi János mellett Nándorfehérvárnál lánglelkű ferences keresztesek élén?",
                "options": ["Kapisztrán János.", "Gellért püspök.", "Julianus barát."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex14",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik törvény megerősítését jelentették az 1351-es dekrétumok?",
                "options": ["Az 1222-es Aranybulla megerősítését.", "A vérszerződését.", "A trianoni békéét."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex15",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hány évre állította meg az oszmán terjeszkedést a nándorfehérvári diadal?",
                "options": ["Körülbelül hetven évre (1521–1526-ig).", "Egyetlen hétre.", "Ötszáz évre."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex16",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hogyan mondjuk magyarul: 'According to the chronicles'?",
                "options": ["A krónikák szerint", "A krónikákkal", "A krónikákban"],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex17",
                "type": "multiple-choice",
                "category": "review",
                "question": "Hogyan mondjuk magyarul: 'The parties agreed that...'?",
                "options": ["A felek megállapodtak abban, hogy...", "A felek álltak abban, hogy...", "A felek beszéltek arról, hogy..."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex18",
                "type": "multiple-choice",
                "category": "review",
                "question": "Melyik város mai neve Belgrád?",
                "options": ["Nándorfehérvár.", "Pozsony.", "Kolozsvár."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex19",
                "type": "multiple-choice",
                "category": "review",
                "question": "Milyen nemesi tisztséget viselt Hunyadi János, mielőtt fia király lett?",
                "options": ["Magyarország kormányzója volt.", "Német császár volt.", "Pápa volt."],
                "correct": 0
            },
            {
                "id": "b1-anjouk-consolidation.ex20",
                "type": "multiple-choice",
                "category": "review",
                "question": "Miért kiemelkedő ez a korszak az állampolgársági interjún?",
                "options": [
                    "Mert bemutatja Magyarország középkori európai nagyhatalmi szerepét és hősies nemzetvédelmét.",
                    "Mert ekkor vezették be a forintot euró helyett.",
                    "Mert ekkor nyíltak meg az autópályák."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-anjouk-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.anjouk-01",
        "title": "Charles Robert & Financial Stability - Károly Róbert és a gazdasági rend",
        "level": "B1",
        "grammar": "Chronicler reported speech: A krónikák szerint, úgy tartják, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the rise of Charles Robert and the defeat of the oligarchs (kiskirályok).",
                    "I can explain the economic significance of Körmöcbánya mining and the gold florin (aranyforint).",
                    "I can use chronicler reporting expressions (a krónikák szerint, úgy tartják).",
                    "I can use eight new vocabulary items related to medieval finance and royal authority."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-anjouk-01-karolyrobert.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-anjouk-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-anjouk-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-anjouk-01-ex.json", "exerciseRefs": [
                "b1-anjouk-01.ex01", "b1-anjouk-01.ex01b", "b1-anjouk-01.ex02", "b1-anjouk-01.ex03",
                "b1-anjouk-01.ex04", "b1-anjouk-01.ex05", "b1-anjouk-01.ex06", "b1-anjouk-01.ex07", "b1-anjouk-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the rise of Charles Robert and the defeat of the oligarchs (kiskirályok).",
                    "I can explain the economic significance of Körmöcbánya mining and the gold florin (aranyforint).",
                    "I can use chronicler reporting expressions (a krónikák szerint, úgy tartják).",
                    "I can use eight new vocabulary items related to medieval finance and royal authority."
                ]
            }
        ],
        "goal": [
            "I can describe the rise of Charles Robert and the defeat of the oligarchs (kiskirályok).",
            "I can explain the economic significance of Körmöcbánya mining and the gold florin (aranyforint).",
            "I can use chronicler reporting expressions (a krónikák szerint, úgy tartják).",
            "I can use eight new vocabulary items related to medieval finance and royal authority."
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.anjouk-02",
        "title": "The Congress of Visegrád 1335 - A visegrádi királytalálkozó",
        "level": "B1",
        "grammar": "Diplomatic agreement reporting: megállapodtak abban, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the 1335 Congress of Visegrád and its participants.",
                    "I can explain the commercial purpose of bypassing Vienna's staple right.",
                    "I can use diplomatic reporting phrases like megállapodtak abban, hogy.",
                    "I can connect the 1335 summit with today's Visegrád Group (V4)."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-anjouk-02-visegrad.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-anjouk-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-anjouk-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-anjouk-02-ex.json", "exerciseRefs": [
                "b1-anjouk-02.ex01", "b1-anjouk-02.ex01b", "b1-anjouk-02.ex02", "b1-anjouk-02.ex03",
                "b1-anjouk-02.ex04", "b1-anjouk-02.ex05", "b1-anjouk-02.ex06", "b1-anjouk-02.ex07", "b1-anjouk-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the 1335 Congress of Visegrád and its participants.",
                    "I can explain the commercial purpose of bypassing Vienna's staple right.",
                    "I can use diplomatic reporting phrases like megállapodtak abban, hogy.",
                    "I can connect the 1335 summit with today's Visegrád Group (V4)."
                ]
            }
        ],
        "goal": [
            "I can describe the 1335 Congress of Visegrád and its participants.",
            "I can explain the commercial purpose of bypassing Vienna's staple right.",
            "I can use diplomatic reporting phrases like megállapodtak abban, hogy.",
            "I can connect the 1335 summit with today's Visegrád Group (V4)."
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.anjouk-03",
        "title": "Louis the Great & the Laws of 1351 - Nagy Lajos és az 1351-es törvények",
        "level": "B1",
        "grammar": "Epithets & law enactments: úgy nevezték, mint; megerősítette a törvényt",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain why Louis I is remembered as Louis the Great and the knight-king (lovagkirály).",
                    "I can describe the 1351 renewal of the Golden Bull and the law of entailment (ősiség).",
                    "I can explain the feudal ninth tax (kilenced) paid by serfs.",
                    "I can discuss the Polish-Hungarian personal union established in 1370."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-anjouk-03-nagylajos.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-anjouk-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-anjouk-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-anjouk-03-ex.json", "exerciseRefs": [
                "b1-anjouk-03.ex01", "b1-anjouk-03.ex01b", "b1-anjouk-03.ex02", "b1-anjouk-03.ex03",
                "b1-anjouk-03.ex04", "b1-anjouk-03.ex05", "b1-anjouk-03.ex06", "b1-anjouk-03.ex07", "b1-anjouk-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain why Louis I is remembered as Louis the Great and the knight-king (lovagkirály).",
                    "I can describe the 1351 renewal of the Golden Bull and the law of entailment (ősiség).",
                    "I can explain the feudal ninth tax (kilenced) paid by serfs.",
                    "I can discuss the Polish-Hungarian personal union established in 1370."
                ]
            }
        ],
        "goal": [
            "I can explain why Louis I is remembered as Louis the Great and the knight-king (lovagkirály).",
            "I can describe the 1351 renewal of the Golden Bull and the law of entailment (ősiség).",
            "I can explain the feudal ninth tax (kilenced) paid by serfs.",
            "I can discuss the Polish-Hungarian personal union established in 1370."
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.anjouk-04",
        "title": "Sigismund & the Ottoman Threat - Zsigmond és az oszmán veszély",
        "level": "B1",
        "grammar": "Threats & border fortifications: fenyeget, kiépít, végvárrendszer",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can outline Sigismund of Luxembourg's reign as king and Holy Roman Emperor.",
                    "I can explain the rising Ottoman threat following the 1396 Battle of Nicopolis.",
                    "I can describe the creation of the southern border defense system (végvárrendszer).",
                    "I can use defense and warfare vocabulary (császár, hadjárat, végvár)."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-anjouk-04-zsigmond.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-anjouk-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-anjouk-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-anjouk-04-ex.json", "exerciseRefs": [
                "b1-anjouk-04.ex01", "b1-anjouk-04.ex01b", "b1-anjouk-04.ex02", "b1-anjouk-04.ex03",
                "b1-anjouk-04.ex04", "b1-anjouk-04.ex05", "b1-anjouk-04.ex06", "b1-anjouk-04.ex07", "b1-anjouk-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can outline Sigismund of Luxembourg's reign as king and Holy Roman Emperor.",
                    "I can explain the rising Ottoman threat following the 1396 Battle of Nicopolis.",
                    "I can describe the creation of the southern border defense system (végvárrendszer).",
                    "I can use defense and warfare vocabulary (császár, hadjárat, végvár)."
                ]
            }
        ],
        "goal": [
            "I can outline Sigismund of Luxembourg's reign as king and Holy Roman Emperor.",
            "I can explain the rising Ottoman threat following the 1396 Battle of Nicopolis.",
            "I can describe the creation of the southern border defense system (végvárrendszer).",
            "I can use defense and warfare vocabulary (császár, hadjárat, végvár)."
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.anjouk-05",
        "title": "János Hunyadi & the Victory at Nándorfehérvár - Hunyadi János és a nándorfehérvári diadal",
        "level": "B1",
        "grammar": "Commemorative synthesis: azóta hirdeti, emlékére, tiszteletére",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can narrate the siege and triumph of Belgrade / Nándorfehérvár in July 1456.",
                    "I can describe János Hunyadi's leadership as regent and 'Turk-beater' (törökverő).",
                    "I can explain the historical origin of the worldwide midday church bells (déli harangszó).",
                    "I can confidently answer citizenship interview questions about Nándorfehérvár and Hunyadi."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-anjouk-05-nandorfehervar.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-anjouk-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-anjouk-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-anjouk-05-ex.json", "exerciseRefs": [
                "b1-anjouk-05.ex01", "b1-anjouk-05.ex01b", "b1-anjouk-05.ex02", "b1-anjouk-05.ex03",
                "b1-anjouk-05.ex04", "b1-anjouk-05.ex05", "b1-anjouk-05.ex06", "b1-anjouk-05.ex07", "b1-anjouk-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the siege and triumph of Belgrade / Nándorfehérvár in July 1456.",
                    "I can describe János Hunyadi's leadership as regent and 'Turk-beater' (törökverő).",
                    "I can explain the historical origin of the worldwide midday church bells (déli harangszó).",
                    "I can confidently answer citizenship interview questions about Nándorfehérvár and Hunyadi."
                ]
            }
        ],
        "goal": [
            "I can narrate the siege and triumph of Belgrade / Nándorfehérvár in July 1456.",
            "I can describe János Hunyadi's leadership as regent and 'Turk-beater' (törökverő).",
            "I can explain the historical origin of the worldwide midday church bells (déli harangszó).",
            "I can confidently answer citizenship interview questions about Nándorfehérvár and Hunyadi."
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.anjouk-consolidation",
        "title": "Unit 7 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can narrate the complete history of 14th–15th century Hungary from Károly Róbert to Hunyadi János.",
                    "I can explain the significance of the 1335 Visegrád meeting, the 1351 laws, and the 1456 Belgrade triumph.",
                    "I can use all key historical grammar: chronicler speech, treaty reporting, law enactments, and commemoration.",
                    "I can answer all citizenship interview questions on the Angevin period and Nándorfehérvár with confidence."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-anjouk-consolidation-ex.json", "exerciseRefs": [
                "b1-anjouk-consolidation.ex01", "b1-anjouk-consolidation.ex02", "b1-anjouk-consolidation.ex03", "b1-anjouk-consolidation.ex04",
                "b1-anjouk-consolidation.ex05", "b1-anjouk-consolidation.ex06", "b1-anjouk-consolidation.ex07", "b1-anjouk-consolidation.ex08",
                "b1-anjouk-consolidation.ex09", "b1-anjouk-consolidation.ex10", "b1-anjouk-consolidation.ex11", "b1-anjouk-consolidation.ex12",
                "b1-anjouk-consolidation.ex13", "b1-anjouk-consolidation.ex14", "b1-anjouk-consolidation.ex15", "b1-anjouk-consolidation.ex16",
                "b1-anjouk-consolidation.ex17", "b1-anjouk-consolidation.ex18", "b1-anjouk-consolidation.ex19", "b1-anjouk-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the complete history of 14th–15th century Hungary from Károly Róbert to Hunyadi János.",
                    "I can explain the significance of the 1335 Visegrád meeting, the 1351 laws, and the 1456 Belgrade triumph.",
                    "I can use all key historical grammar: chronicler speech, treaty reporting, law enactments, and commemoration.",
                    "I can answer all citizenship interview questions on the Angevin period and Nándorfehérvár with confidence."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-anjouk-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_7_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 7!")
