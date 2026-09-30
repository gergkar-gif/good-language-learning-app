#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 13, 14, and 15:
  - Unit 13: b2-pestihumor (The Pesti Humor: Cabaret, Satire & Survival)
  - Unit 14: b2-magyarfilm (Allegory on Screen: A Century of Hungarian Cinema)
  - Unit 15: b2-szamizdat (The Three Ts: Censorship, Aczél's Cultural Policy & Samizdat)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402


UNIT_13_PESTIHUMOR = {
    "unit_num": 13,
    "slug": "pestihumor",
    "title": "The Pesti Humor: Cabaret, Satire & Survival",
    "grammar_skill": "b2-discourse-particles",
    "vocab_skill": "b2-pestihumor-vocab",
    "theme": "Budapest cabaret, political satire and Pesti humor",
    "location": "Budapest (Nagymező utca, Mikroszkóp Színpad és a pesti kabarék)",
    "intro_body": [
        "Few cultural phenomena are as deeply woven into Budapest's identity as the 'pesti vicc' (Budapest political joke) and the urban cabaret tradition. Born in the bohemian coffeehouses of the late Austro-Hungarian Empire, polished by literary giants of the Nyugat journal, and refined in the smoky theatres of Nagymező utca (Budapest's Broadway), political satire was never merely entertainment: it was an essential psychological survival mechanism through wars, sieges, totalitarian dictatorships, and ideological censorship.",
        "In this unit, you will discover the legacy of Endre Nagy, Frigyes Karinthy, Béla Salamon, and Géza Hofi, while mastering B2 pragmatic discourse particles (hiszen, ugyebár, korántsem, aligha, éppenséggel) that express subtle speaker stance, shared assumptions, irony, and conversational nuance."
    ],
    "combined_story_title": "Ha már sírni nem lehet: A pesti kabaré száz éve",
    "combined_story_summary": "How Budapest's cabaret tradition—from Endre Nagy and Frigyes Karinthy to Béla Salamon and Géza Hofi—used self-irony, wordplay, and licensed political satire as a survival mechanism across turbulent twentieth-century history.",
    "lessons": [
        {
            "num": 1,
            "title": "Endre Nagy and the Birth of the Pesti Cabaret",
            "grammar_label": "Evident and explanatory assertion with hiszen ('after all / as you know')",
            "goals": [
                "I can explain how Endre Nagy transformed the French cabaret into a unique Budapest literary phenomenon.",
                "I can use the modal particle hiszen to introduce shared background knowledge and explanatory justifications.",
                "I can discuss early 20th-century cabaret, conferenciers, and urban satire using B2 Hungarian vocabulary."
            ],
            "story_segment": {
                "seg_slug": "nagyendre",
                "title": "Nagy Endre és a modern pesti kabaré születése",
                "summary": "At the turn of the century, writer and conferencier Endre Nagy created the Budapest cabaret in Nagymező utca, turning the stage into an intellectual forum for literary satire.",
                "location": "Budapest, Nagymező utca (1907)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század első évtizedében a budapesti éjszakai élet alapvető változáson ment keresztül. Amikor Nagy Endre 1907-ben fellépett a Nagymező utcai Bonbonnière színpadára, nem csupán a párizsi kabarék könnyed, sanzonos hangulatát akarta lemásolni. Felismerte, hogy a pesti polgárságnak olyan szellemi térre van szüksége, ahol a kávéházi pletykák és a napi politikai események azonnal szatírává formálódhatnak."
                    },
                    {
                        "type": "narration",
                        "text": "Nagy Endre megteremtette a pesti konferanszié klasszikus alakját. Szmokingban, cigarettával a kezében lépett ki a függöny elé, és nem kész vicceket mesélt, hanem közvetlen, szellemes párbeszédet kezdeményezett a nézőkkel. Úgy beszélt a miniszterek botrányairól és a polgármesteri hivatal korrupciójáról, mintha egy szűk baráti társaságban osztaná meg a legfrissebb városi híreket."
                    },
                    {
                        "type": "narration",
                        "text": "Hamarosan a Nyugat folyóirat legjelesebb írói is csatlakoztak a kezdeményezéshez. Ady Endre, Babits Mihály, Szép Ernő és a fiatal Karinthy Frigyes egyfelvonásos jeleneteket, szatirikus verseket és kuplékat írtak a színháznak. A kabaré az igényes irodalom és a pesti utca nyelvének egyedülálló fúziójává vált, ahol a művészet és a társadalomkritika elválaszthatatlanul összefonódott."
                    },
                    {
                        "type": "narration",
                        "text": "A budapesti közönség rajongott az új műfajért, hiszen a mindennapi feszültségeket és kiszolgáltatottságot végre felszabadító nevetéssé alakíthatta. A kortárs kritikusok megjegyezték, hogy a pesti ember a kávéházban él, a parlamentben vitatkozik, de a kabarében gondolkodik: a konferanszié a főváros kollektív lelkiismeretévé lépett elő."
                    },
                    {
                        "type": "narration",
                        "text": "Nagy Endre ezzel lefektette a magyar kabaré örök törvényét: a hatalmat nem szabad kímélni, de a bírálatnak mindig elegánsnak, nyelvi szempontból bravúrosnak kell maradnia. Ez az örökség tette a Nagymező utcát a pesti Broadwayvé, amely évtizedeken át meghatározta a magyar főváros kulturális hangulatát."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "kabaré",
                    "translation": "cabaret",
                    "pos": "noun"
                },
                {
                    "lemma": "konferanszié",
                    "translation": "cabaret master of ceremonies / conferencier",
                    "pos": "noun"
                },
                {
                    "lemma": "hiszen",
                    "translation": "after all / since / surely",
                    "pos": "conjunction"
                },
                {
                    "lemma": "önirónia",
                    "translation": "self-irony",
                    "pos": "noun"
                },
                {
                    "lemma": "társadalomkritika",
                    "translation": "social criticism",
                    "pos": "noun"
                },
                {
                    "lemma": "szellemes",
                    "translation": "witty",
                    "pos": "adjective"
                }
            ],
            "grammar_doc": {
                "slug": "discourse-particle-hiszen",
                "title": "Pragmatic Discourse Particle: hiszen",
                "text1_title": "Evident Knowledge and Explanatory Justification",
                "text1": "The discourse particle hiszen ('after all / since / as you know') marks an assertion as self-evident, mutually understood, or providing a natural justification for an earlier statement. Rather than introducing completely unexpected facts, hiszen appeals to common ground between the speaker and the interlocutor.",
                "text2_title": "Position and Conversational Tone",
                "text2": "Hiszen can open a sentence ('Hiszen ezt mindenki tudja!') or stand immediately before the focal element. In polite debate, it softens potential disagreement by presenting the speaker's reasoning as an obvious reality that both parties can easily acknowledge.",
                "table_title": "Pragmatic Usage of hiszen",
                "table_rows": [
                    [
                        "A közönség azonnal nevetett a célzáson, hiszen a botrányról minden lap írt.",
                        "The audience laughed at the allusion immediately, since after all every paper wrote about the scandal."
                    ],
                    [
                        "Nem kell bemutatnom Nagy Endrét, hiszen a műfaj megalapítója.",
                        "I don't need to introduce Endre Nagy, since as you know he is the founder of the genre."
                    ],
                    [
                        "Hiszen nem tehettünk mást ebben a képtelen helyzetben!",
                        "After all, we could not have done anything else in this absurd situation!"
                    ],
                    [
                        "Miért csodálkozol a sikerén, hiszen rendkívül szellemes szövegeket írt?",
                        "Why are you surprised at his success, since after all he wrote extraordinarily witty texts?"
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A kabarészínpad gyorsan megtelt, hiszen a pesti polgárok szomjaztak a bátor társadalomkritikára.",
                        "english": "The cabaret stage quickly filled up, since after all Budapest citizens thirsted for courageous social criticism."
                    },
                    {
                        "spanish": "Nagy Endre nem félt a kényes témáktól, hiszen a közönség szimpátiája mellette állt.",
                        "english": "Endre Nagy did not fear delicate topics, since after all the sympathy of the audience stood by him."
                    },
                    {
                        "spanish": "Hiszen a nevetés az egyetlen méltó fegyver a bürokrácia ostobasága ellen.",
                        "english": "After all, laughter is the only worthy weapon against the stupidity of bureaucracy."
                    }
                ],
                "tip": "Use hiszen when you want to gently remind your listener of an uncontroversial fact: 'Hiszen te is láttad az előadást!' (After all, you saw the performance too!). Do not confuse it with purely factual mert."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi a 'konferanszié' feladata a klasszikus pesti kabaréban?",
                    "options": [
                        "A műsorszámokat összekötő, a közönséggel közvetlen kapcsolatot teremtő, szellemes műsorvezető.",
                        "A színház gazdasági ügyeit irányító főkönyvelő.",
                        "A színpadi jelmezeket és parókákat készítő iparos."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Nagy Endre előadásai nem pusztán szórakoztattak, hanem mélyreható _____ nyújtottak a polgári életről. (social criticism)",
                    "answer": "társadalomkritikát",
                    "english": "Endre Nagy's performances did not merely entertain, but offered profound social criticism of bourgeois life.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A nézők azonnal felismerték a politikus paródiáját, _____ a hanghordozása összetéveszthetetlen volt. (since after all)",
                    "answer": "hiszen",
                    "english": "The spectators immediately recognized the parody of the politician, since after all his intonation was unmistakable.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban fejezi ki a 'hiszen' partikula a közös előzetes tudásra való hivatkozást?",
                    "options": [
                        "Nem szükséges részleteznem az ügyet, hiszen mindannyian olvastuk a reggeli sajtót.",
                        "Nem szükséges részleteznem az ügyet, holott mindannyian olvastuk a reggeli sajtót.",
                        "Nem szükséges részleteznem az ügyet, aligha mindannyian olvastuk a reggeli sajtót."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Hiszen",
                        "a",
                        "budapesti",
                        "közönség",
                        "mindig",
                        "értette",
                        "a",
                        "szellemes",
                        "célzásokat."
                    ],
                    "solution": [
                        "Hiszen",
                        "a",
                        "budapesti",
                        "közönség",
                        "mindig",
                        "értette",
                        "a",
                        "szellemes",
                        "célzásokat."
                    ],
                    "english": "After all, the Budapest audience has always understood witty allusions.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan újította meg Nagy Endre a kabaréműfajt Budapesten?",
                    "options": [
                        "A francia sanzonos szórakoztatást igényes irodalmi és közéleti szatírává alakította át.",
                        "Kizárólag külföldi színészeket és zenészeket hívott meg a színházába.",
                        "Megtiltotta a nézőkkel való közvetlen párbeszédet és a politikai témákat."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "magyar",
                        "értelmiség",
                        "az",
                        "önirónia",
                        "segítségével",
                        "dolgozta",
                        "fel",
                        "a",
                        "kudarcokat."
                    ],
                    "solution": [
                        "A",
                        "magyar",
                        "értelmiség",
                        "az",
                        "önirónia",
                        "segítségével",
                        "dolgozta",
                        "fel",
                        "a",
                        "kudarcokat."
                    ],
                    "english": "The Hungarian intelligentsia processed failures with the help of self-irony.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence explaining why Endre Nagy's cabaret was beloved using 'hiszen'.",
                            "answer": "A kabaré rendkívül népszerűvé vált, hiszen a legnevesebb magyar írók írtak jeleneteket a színpadára."
                        },
                        {
                            "prompt": "Remind someone that laughing at authority was a Budapest tradition using 'Hiszen...'.",
                            "answer": "Hiszen a pesti polgárok mindig is gúnnyal válaszoltak a hatalom packázásaira."
                        }
                    ],
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                }
            ]
        },
        {
            "num": 2,
            "title": "Laughing Through Historical Catastrophes",
            "grammar_label": "Seeking consensus and common ground with ugyebár ('isn't it / as you know')",
            "goals": [
                "I can analyze how Budapest humor and political jokes served as psychological defense mechanisms during wars and crises.",
                "I can employ ugyebár to appeal to common ground, conversational consensus, and subtle shared complicity.",
                "I can discuss historical anecdotes, black humor, and survival satire in fluent B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "tulniatortenelmet",
                "title": "Nevetés a romok felett: Történelmi túlélés",
                "summary": "From World War I through the siege of 1944-45 and the 1950s, Budapest responded to devastation with instantaneous, biting political jokes that spread faster than official news.",
                "location": "Budapest kávéházai és óvóhelyei (1914–1956)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század viharai különösen keményen sújtották Budapestet. Világháborúk, forradalmak, a trianoni trauma és a negyvenes évek pusztítása követték egymást, a város lakossága azonban a legsötétebb órákban sem veszítette el sajátos fegyverét: a pesti viccet. Amikor az eseményeket már nem lehetett ésszel felfogni, a humor vált az egyetlen működő védekező mechanizmussá."
                    },
                    {
                        "type": "narration",
                        "text": "Az 1944–45-ös ostrom idején, miközben a főváros felett bombák robbantak és a hidak a Dunába dőltek, az óvóhelyek félhomályában szájról szájra jártak a legújabb történetek. A túlélési ösztön része volt, hogy a rettegést fanyar nevetéssel oldják fel: a pesti polgár a pincében is észrevette a helyzet tragikomikus abszurditását."
                    },
                    {
                        "type": "narration",
                        "text": "Ebben a korszakban emelkedett legendás rangra Salamon Béla, a kabarészínpadok felejthetetlen alakja. Jellegzetes, orrhangú beszédével és a kisember csetlő-botló figurájával a mindenkori kiszolgáltatottságot jelenítette meg. Híres szállóigéje — „Lepsénynél még megvolt!” — a mai napig az értelmetlen veszteségek szimbóluma a magyar nyelvben."
                    },
                    {
                        "type": "narration",
                        "text": "Az ötvenes évek sztálinista terrorja idején a politikai vicc mesélése börtönbüntetéssel járhatott. Ennek ellenére a viccek órákon belül körbejárták a várost: ugyebár az elnyomó hatalom képtelen volt minden kávéházi asztal és villamosperon mellé besúgót állítani. A rendszer abszurd jelszavait kiforgató szóviccek leleplezték a hivatalos ideológia ürességét."
                    },
                    {
                        "type": "narration",
                        "text": "A pesti vicc soha nem volt puszta szórakozás: valóságos túlélési stratégia és kollektív terápia volt. A közös nevetés visszaadta az emberek emberi méltóságát egy olyan világban, amely minden erejével a megalázásukra és megfélemlítésükre törekedett."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "túlélési ösztön",
                    "translation": "survival instinct",
                    "pos": "noun"
                },
                {
                    "lemma": "fanyar",
                    "translation": "tart / dry / wry",
                    "pos": "adjective"
                },
                {
                    "lemma": "ugyebár",
                    "translation": "isn't it so / as we know",
                    "pos": "adverb"
                },
                {
                    "lemma": "szóvicc",
                    "translation": "pun / play on words",
                    "pos": "noun"
                },
                {
                    "lemma": "abszurditás",
                    "translation": "absurdity",
                    "pos": "noun"
                },
                {
                    "lemma": "óvóhely",
                    "translation": "air raid shelter",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "discourse-particle-ugyebar",
                "title": "Pragmatic Discourse Particle: ugyebár",
                "text1_title": "Appealing to Presumed Common Ground",
                "text1": "The discourse particle ugyebár ('isn't it / as you know / surely / right?') signals that the speaker expects the listener to agree with a stated premise. It functions similarly to an English tag question or conversational parenthetical, drawing the listener into shared complicity or mutual understanding.",
                "text2_title": "Irony and Conversational Rhythm",
                "text2": "In satirical and essayistic Hungarian, ugyebár often carries an ironic edge, pointing out an obvious contradiction between official pretension and undeniable reality. It can stand at the beginning, middle, or end of a clause.",
                "table_title": "Communicative Uses of ugyebár",
                "table_rows": [
                    [
                        "A pesti humor, ugyebár, mindig a legnehezebb időkben volt a legélesebb.",
                        "Pesti humor, as we well know, was always sharpest in the hardest times."
                    ],
                    [
                        "Nem gondoltad komolyan, ugyebár, hogy a hivatalos sajtó igazat írt?",
                        "You didn't think seriously, did you, that the official press told the truth?"
                    ],
                    [
                        "Ugyebár emlékszel még Salamon Béla híres mondására?",
                        "You remember Béla Salamon's famous saying, don't you?"
                    ],
                    [
                        "A legnehezebb körülmények között, ugyebár, a nevetés jelentette a menedéket.",
                        "Under the hardest circumstances, as is well known, laughter meant the refuge."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Az óvóhelyek sötétjében, ugyebár, a fanyar viccek segítettek elviselni a bombázásokat.",
                        "english": "In the dark of the air raid shelters, as we know, wry jokes helped endure the bombings."
                    },
                    {
                        "spanish": "A totalitárius hatalom, ugyebár, leginkább a gúnytól és a nevetségessé válástól rettegett.",
                        "english": "Totalitarian power, isn't it true, dreaded mockery and becoming ridiculous above all else."
                    },
                    {
                        "spanish": "Ti sem vettétek komolyan a propaganda ígéreteit, ugyebár?",
                        "english": "You didn't take the promises of the propaganda seriously either, did you?"
                    }
                ],
                "tip": "Use ugyebár to create rapport or subtle ironic distance. In spoken speech, it can be shortened to 'ugye', but in formal writing and B2 essays, 'ugyebár' is the preferred literary form."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'óvóhely' kifejezés a történelmi elbeszélésekben?",
                    "options": [
                        "Bombatámadások és katonai csapások idején védelmet nyújtó, megerősített föld alatti helyiség.",
                        "Kizárólag színházi díszletek tárolására használt raktárépület.",
                        "Nyári szabadtéri kávéház a Duna partján."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A nehéz időkben a pesti polgárok szomorúságát a _____ humor és az önirónia enyhítette. (dry / wry)",
                    "answer": "fanyar",
                    "english": "In difficult times, the sorrow of Budapest citizens was eased by dry humor and self-irony.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A diktatúrában a politikai vicc mesélése, _____ komoly börtönbüntetést vonhatott maga után. (as is well known)",
                    "answer": "ugyebár",
                    "english": "Under the dictatorship, telling political jokes, as is well known, could entail serious imprisonment.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Hogyan fejezhetjük ki finoman a közös egyetértés elvárását az 'ugyebár' segítségével?",
                    "options": [
                        "Nem felejtettétek el Salamon Béla híres jelenetét, ugyebár?",
                        "Nem felejtettétek el Salamon Béla híres jelenetét, minél inkább?",
                        "Nem felejtettétek el Salamon Béla híres jelenetét, amennyiben?"
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "túléléshez,",
                        "ugyebár,",
                        "a",
                        "remény",
                        "és",
                        "a",
                        "humor",
                        "is",
                        "szükséges",
                        "volt."
                    ],
                    "solution": [
                        "A",
                        "túléléshez,",
                        "ugyebár,",
                        "a",
                        "remény",
                        "és",
                        "a",
                        "humor",
                        "is",
                        "szükséges",
                        "volt."
                    ],
                    "english": "For survival, as is well known, hope and humor were also necessary.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért terjedtek a politikai viccek még a legsúlyosabb terror idején is Budapesten?",
                    "options": [
                        "Mert a humor kollektív terápiaként és a lelki túlélés elengedhetetlen eszközeként működött.",
                        "Mert a hatóságok jutalmazták a legviccesebb történetek kitalálóit.",
                        "Mert a lakosságnak nem volt más híre a külvilágból."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "túlélési",
                        "ösztön",
                        "arra",
                        "késztette",
                        "az",
                        "embereket,",
                        "hogy",
                        "nevessenek",
                        "a",
                        "félelmen."
                    ],
                    "solution": [
                        "A",
                        "túlélési",
                        "ösztön",
                        "arra",
                        "késztette",
                        "az",
                        "embereket,",
                        "hogy",
                        "nevessenek",
                        "a",
                        "félelmen."
                    ],
                    "english": "The survival instinct prompted people to laugh at their fear.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence confirming that humor was a defense against fear using 'ugyebár'.",
                            "answer": "A legnehezebb ostromnapokban, ugyebár, a nevetés jelentette a lelki menedéket a pincékben."
                        },
                        {
                            "prompt": "Ask someone rhetorically if they remember the absurdity of the era using '..., ugyebár?'.",
                            "answer": "Ti is emlékeztek még az ötvenes évek abszurditására, ugyebár?"
                        }
                    ],
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                }
            ]
        },
        {
            "num": 3,
            "title": "Géza Hofi and the Art of Licensed Criticism",
            "grammar_label": "Categorical refutation with the particle korántsem ('by no means / far from it')",
            "goals": [
                "I can explain Géza Hofi's unique status at the Mikroszkóp Színpad during the Kádár consolidation.",
                "I can use the emphatic negative particle korántsem to decisively counter assumptions and exaggerate contrasts.",
                "I can debate the boundary between genuine political dissent and state-tolerated safety-valve humor."
            ],
            "story_segment": {
                "seg_slug": "hofigeza",
                "title": "Hofi Géza és a szelephumor művészete",
                "summary": "At the Mikroszkóp Színpad in Nagymező utca, Géza Hofi became Hungary's most influential satirist, using brilliant mimicry to voice citizens' frustrations within regime-tolerated limits.",
                "location": "Budapest, Mikroszkóp Színpad (1970-es és 80-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A kádári konszolidáció évtizedeiben a magyar politikai élet különleges intézménnyel gazdagodott: a Mikroszkóp Színpaddal. Komlós János igazgató vezetése alatt a Nagymező utcai színház a rendszer ellenőrzött „bizalmi szelepévé” vált, ahol a nézők olyan bátor és csípős bírálatokat hallhattak az állami bürokráciáról, amilyeneket a hivatalos sajtóban sehol sem engedélyeztek."
                    },
                    {
                        "type": "narration",
                        "text": "Ennek a színpadnak lett a vitathatatlan királya Hofi Géza. Karrierje kezdetén még egyszerű parodistaként lépett fel, de hamarosan egyéni műfajt teremtett. Előadásai nem egyszerűen kabarészámok voltak, hanem lendületes, improvizatív monológok, amelyekben a gyári melós, a kisember és a józan paraszti ész szemszögéből figurázta ki a szocialista gazdaság képtelenségeit."
                    },
                    {
                        "type": "narration",
                        "text": "Hofi zsenialitása abban állt, hogy pontosan érezte a kimondhatóság határait. A pártvezetés korántsem engedett meg mindent: a szovjet csapatok jelenléte vagy az 1956-os forradalom tabutéma maradt. Ugyanakkor a hiánygazdaság, a korrupt vállalatvezetők és a pártfunkcionáriusok gőgje állandó céltáblája volt a poénjainak."
                    },
                    {
                        "type": "narration",
                        "text": "Hanglemezei százezres példányszámban fogytak el, előadásaira pedig hónapokkal korábban elkapkodták a jegyeket. A nézők tapsviharral jutalmazták, amikor kimondta azt, amit ők csak otthon, a konyhaasztal mellett mertek suttogni. A hatalom számára Hofi azért volt nélkülözhetetlen, mert a nevetés levezette a társadalmi elégedetlenséget anélkül, hogy a rendszer stabilitását veszélyeztette volna."
                    },
                    {
                        "type": "narration",
                        "text": "Bár sokan bírálták a „szelep” szerepe miatt, Hofi művészete túlélte a rendszerváltást is. Haláláig a magyar közönség legkedvesebb és leghitelesebb nevettetője maradt, aki bebizonyította, hogy a humor nemcsak szórakoztat, hanem szembesít saját gyengeségeinkkel is."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "bizalmi szelep",
                    "translation": "safety valve",
                    "pos": "noun"
                },
                {
                    "lemma": "korántsem",
                    "translation": "by no means / far from",
                    "pos": "adverb"
                },
                {
                    "lemma": "paródia",
                    "translation": "parody",
                    "pos": "noun"
                },
                {
                    "lemma": "kettős beszéd",
                    "translation": "double speak / coded speech",
                    "pos": "noun"
                },
                {
                    "lemma": "tapsvihar",
                    "translation": "storm of applause",
                    "pos": "noun"
                },
                {
                    "lemma": "rendszerkritika",
                    "translation": "regime critique",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "discourse-particle-korantsem",
                "title": "Emphatic Negative Particle: korántsem",
                "text1_title": "Decisive and Categorical Denial",
                "text1": "The emphatic negative adverbial particle korántsem ('by no means / far from it / anything but') decisively refutes an assertion or assumed state of affairs. It modifies adjectives, adverbs, or verbs, stressing that reality is vastly different from an optimistic or simplistic assumption.",
                "text2_title": "Register and Syntactic Behavior",
                "text2": "Korántsem belongs to the formal, analytical, and critical register of Hungarian. When modifying an adjective or adverb, it does not require an additional 'nem' (e.g., 'korántsem egyszerű' = far from simple). When modifying a verb, it precedes the finite verb or focal element.",
                "table_title": "Emphatic Refutation with korántsem",
                "table_rows": [
                    [
                        "A szelephumor korántsem jelentett valódi szólásszabadságot.",
                        "Safety-valve humor by no means meant genuine freedom of speech."
                    ],
                    [
                        "Hofi szerepe korántsem volt egyértelmű a korszak politikai életében.",
                        "Hofi's role was far from unambiguous in the political life of the era."
                    ],
                    [
                        "A pártvezetés korántsem nézte mindig jó szemmel a maró poénokat.",
                        "The party leadership by no means always looked favorably on the scathing punchlines."
                    ],
                    [
                        "A gazdasági helyzet korántsem volt olyan fényes, mint ahogyan a hírek állították.",
                        "The economic situation was far from as bright as the news claimed."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A Mikroszkóp Színpad előadásai korántsem voltak mentesek a cenzori beavatkozástól.",
                        "english": "The performances of the Mikroszkóp Színpad were by no means free from censorial intervention."
                    },
                    {
                        "spanish": "Hofi sikere korántsem a véletlennek, hanem rendkívüli őszinteségének és tehetségének volt köszönhető.",
                        "english": "Hofi's success was by no means due to chance, but to his extraordinary sincerity and talent."
                    },
                    {
                        "spanish": "A szocialista tervgazdaság hibái korántsem maradtak észrevétlenek a nézők előtt.",
                        "english": "The flaws of the socialist planned economy by no means remained unnoticed before the spectators."
                    }
                ],
                "tip": "Never write '*korántsem nem szép'. Use 'korántsem szép' (far from beautiful). Korántsem already carries the negative value!"
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'bizalmi szelep' kifejezés a kádári kultúrpolitika kontextusában?",
                    "options": [
                        "Olyan engedélyezett intézményt vagy előadót, amelyen keresztül a társadalmi elégedetlenség kontrolláltan levezetődhetett.",
                        "Gázvezetékek javítására szolgáló műszaki berendezést a gyárakban.",
                        "A színházi tűzoltókészülékek kötelező ellenőrzési jegyzőkönyvét."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Hofi Géza előadásait a közönség szűnni nem akaró _____ kísérte a Mikroszkóp Színpadon. (storm of applause)",
                    "answer": "tapsviharral",
                    "english": "Géza Hofi's performances were accompanied by unceasing storm of applause from the audience at the Mikroszkóp Színpad.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A kabaréműsorok bátor hangvétele _____ jelentette azt, hogy a tabutémákról is szabadon lehetett beszélni. (by no means)",
                    "answer": "korántsem",
                    "english": "The courageous tone of the cabaret shows by no means meant that taboo subjects could also be discussed freely.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat alkalmazza nyelvtanilag helyesen a 'korántsem' partikulát?",
                    "options": [
                        "A szocialista hiánygazdaság problémái korántsem voltak elszigeteltek.",
                        "A szocialista hiánygazdaság problémái korántsem nem voltak elszigeteltek.",
                        "A szocialista hiánygazdaság problémái korántsem nem elszigeteltek voltak."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "hatalom",
                        "korántsem",
                        "tűrt",
                        "el",
                        "minden",
                        "nyílt",
                        "rendszerkritikát."
                    ],
                    "solution": [
                        "A",
                        "hatalom",
                        "korántsem",
                        "tűrt",
                        "el",
                        "minden",
                        "nyílt",
                        "rendszerkritikát."
                    ],
                    "english": "The authorities by no means tolerated all open regime criticism.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért engedélyezte a Kádár-rendszer Hofi Géza éles bírálatait?",
                    "options": [
                        "Mert fellépései biztonsági szelepként működtek, levezetve a lakosság feszültségét a rendszer megdöntése nélkül.",
                        "Mert Hofi titokban a belügyminisztérium vezető tisztviselője volt.",
                        "Mert a műsorait kizárólag külföldi turisták láthatták."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "Hofi",
                        "zseniális",
                        "módon",
                        "alkalmazta",
                        "a",
                        "kettős",
                        "beszéd",
                        "és",
                        "a",
                        "paródia",
                        "eszközeit."
                    ],
                    "solution": [
                        "Hofi",
                        "zseniális",
                        "módon",
                        "alkalmazta",
                        "a",
                        "kettős",
                        "beszéd",
                        "és",
                        "a",
                        "paródia",
                        "eszközeit."
                    ],
                    "english": "Hofi brilliantly applied the tools of doublespeak and parody.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence refuting that Hofi's humor was harmless using 'korántsem'.",
                            "answer": "Hofi Géza humora korántsem volt ártalmatlan szórakozás, hiszen a társadalom legégetőbb gondjaira tapintott rá."
                        },
                        {
                            "prompt": "State that licensed criticism was by no means equal to genuine freedom using 'korántsem'.",
                            "answer": "Az engedélyezett kabaré korántsem jelentett valódi sajtószabadságot a szocialista korszakban."
                        }
                    ],
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                }
            ]
        },
        {
            "num": 4,
            "title": "Satirical Press from Borsszem Jankó to Today",
            "grammar_label": "Epistemic doubt and improbability with aligha ('hardly / scarcely')",
            "goals": [
                "I can trace Hungarian satirical publishing from 19th-century Borsszem Jankó and Ludas Matyi to modern absurdism.",
                "I can express high improbability and epistemic reservation with aligha.",
                "I can analyze political caricatures, satirical tropes, and print parodies in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szatirikussajto",
                "title": "A Borsszem Jankótól a Kétfarkú Kutyáig",
                "summary": "From Adolf Ágai's 1868 Borsszem Jankó through the post-war Ludas Matyi to contemporary political satire, Hungarian cartoonists and writers exposed hypocrisy in print.",
                "location": "Budapest szerkesztőségei (1868–2020-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar szatirikus sajtó gyökerei a tizenkilencedik század második felébe nyúlnak vissza. Az 1867-es kiegyezés után Ágai Adolf megalapította a Borsszem Jankó című élclapot, amely hamarosan a dualizmus korának legbefolyásosabb humoros sajtótermékévé vált. Lapjának állandó figurái — a vidéki nemes Mokány Berci vagy a pesti polgár Seffenreisz — tűpontos görbe tükröt tartottak a korabeli társadalom elé."
                    },
                    {
                        "type": "narration",
                        "text": "A két világháború között és a szocializmus évtizedeiben a karikatúra maradt a vizuális véleménynyilvánítás legfőbb formája. Az 1945-ben alapított Ludas Matyi című hetilap óriási népszerűségnek örvendett. Bár a lapot a pártállami cenzúra felügyelte, kiváló grafikusai — köztük Kaján Tibor és Balázs-Piri Balázs — mesterien rejtették el a bürokrácia és a képmutatás elleni gúnyt a rajzok apró részleteiben."
                    },
                    {
                        "type": "narration",
                        "text": "A szatirikus sajtó nélkül aligha érthetnénk meg a magyar közélet valódi reflexeit. A rajzolt alakok és a csattanós képaláírások olyan igazságokat fogalmaztak meg, amelyeket a komoly vezércikkekben aligha lehetett volna leírni: a gúny és a szarkazmus leplezte le a hivatalos frázisok mögött rejtőző hazugságokat."
                    },
                    {
                        "type": "narration",
                        "text": "A rendszerváltás után a Hócipő című szatirikus kéthetilap vitte tovább ezt a hagyományt Farkasházy Tivadar vezetésével. A digitális korban pedig új formák születtek: a Magyar Kétfarkú Kutya Párt az abszurd humor és a politikai paródia eszközeivel — ingyen sör és örök élet ígéretével — hívta fel a figyelmet a politikai ígéretek ürességére."
                    },
                    {
                        "type": "narration",
                        "text": "A Borsszem Jankó lapjaitól a mai internetes mémekig a szatíra mindig ugyanazt a funkciót töltötte be: megvédte a polgárokat a cinizmustól, és bebizonyította, hogy a hatalom képmutatását egyetlen találó karikatúrával is össze lehet zúzni."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "karikatúra",
                    "translation": "caricature / political cartoon",
                    "pos": "noun"
                },
                {
                    "lemma": "élclap",
                    "translation": "satirical weekly / comic paper",
                    "pos": "noun"
                },
                {
                    "lemma": "aligha",
                    "translation": "hardly / scarcely / unlikely",
                    "pos": "adverb"
                },
                {
                    "lemma": "képmutatás",
                    "translation": "hypocrisy",
                    "pos": "noun"
                },
                {
                    "lemma": "gúny",
                    "translation": "mockery / scorn",
                    "pos": "noun"
                },
                {
                    "lemma": "rovat",
                    "translation": "column / newspaper section",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "discourse-particle-aligha",
                "title": "Epistemic Modality: aligha",
                "text1_title": "Expressing Strong Doubt and Improbability",
                "text1": "The epistemic particle aligha ('hardly / scarcely / almost certainly not') expresses a speaker's strong doubt regarding the likelihood or truth of a proposition. It intrinsically embeds negation, eliminating the need for 'nem'.",
                "text2_title": "Focus Position and Verb-Prefix Inversion",
                "text2": "Because aligha occupies the pre-verbal focus position, any separable verbal prefix (igekötő) attached to the finite verb MUST invert and follow the verb: 'Aligha hiszem el' (I hardly believe it), 'Aligha érik el a céljukat' (They will hardly achieve their goal).",
                "table_title": "Expressing Doubt with aligha",
                "table_rows": [
                    [
                        "A cenzorok aligha vették észre a rajz minden apró részletét.",
                        "The censors hardly noticed every tiny detail of the drawing."
                    ],
                    [
                        "Aligha kétséges, hogy a karikatúra mélyen megsértette a minisztert.",
                        "It is hardly doubtful that the caricature deeply offended the minister."
                    ],
                    [
                        "Ilyen feltételek mellett aligha maradhatott volna független a szerkesztőség.",
                        "Under such conditions, the editorial office could hardly have remained independent."
                    ],
                    [
                        "A politikusok aligha örültek a róluk készült szatirikus rajzoknak.",
                        "Politicians hardly rejoiced over the satirical drawings made of them."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A szatíra ereje nélkül aligha maradt volna meg a magyar társadalom szellemi ellenállása.",
                        "english": "Without the power of satire, Hungarian society's intellectual resistance would hardly have survived."
                    },
                    {
                        "spanish": "Aligha képzelhető el hiteles sajtó csipkelődő karikatúrák nélkül.",
                        "english": "Authentic press can hardly be imagined without teasing caricatures."
                    },
                    {
                        "spanish": "A képmutatást aligha lehetett volna ennél találóbban kigúnyolni.",
                        "english": "Hypocrisy could hardly have been mocked more aptly than this."
                    }
                ],
                "tip": "Never combine 'aligha' with 'nem'. Say 'Aligha hiszem' (I hardly believe it), never '*Aligha nem hiszem'."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi az 'élclap' kifejezés jelentése a magyar sajtótörténetben?",
                    "options": [
                        "Kifejezetten humoros, szatirikus írásokat és politikai karikatúrákat közlő periodika.",
                        "Mezőgazdasági vetőmagok árait hirdető hivatalos közlöny.",
                        "Orvosi sebészeti műszereket bemutató tudományos folyóirat."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Ludas Matyi grafikusai a maró _____ eszközével leplezték le a bürokrácia képmutatását. (mockery / scorn)",
                    "answer": "gúny",
                    "english": "The graphic artists of Ludas Matyi unmasked the hypocrisy of bureaucracy using the tool of scathing mockery.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A rajzban rejlő politikai üzenetet a korabeli olvasók _____ értették félre. (hardly / scarcely)",
                    "answer": "aligha",
                    "english": "The contemporary readers hardly misunderstood the political message hidden in the drawing.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban követi helyes szórend és igekötő-inverzió az 'aligha' partikulát?",
                    "options": [
                        "A cenzorok aligha ismerték fel a szatirikus rajz valódi célpontját.",
                        "A cenzorok aligha felismerték a szatirikus rajz valódi célpontját.",
                        "A cenzorok aligha nem ismerték fel a szatirikus rajz valódi célpontját."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Aligha",
                        "találunk",
                        "jobb",
                        "példát",
                        "a",
                        "politikai",
                        "képmutatás",
                        "leleplezésére."
                    ],
                    "solution": [
                        "Aligha",
                        "találunk",
                        "jobb",
                        "példát",
                        "a",
                        "politikai",
                        "képmutatás",
                        "leleplezésére."
                    ],
                    "english": "We can hardly find a better example for unmasking political hypocrisy.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen szerepet játszott az 1868-ban indult Borsszem Jankó című lap a dualizmusban?",
                    "options": [
                        "Tipikus figuráin keresztül görbe tükröt tartott a magyar politikai és polgári társadalom elé.",
                        "A bécsi udvar hivatalos rendeleteit tette közzé német nyelven.",
                        "Kizárólag gyermekmeséket és verseket publikált az iskolák számára."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "lap",
                        "népszerű",
                        "karikatúra",
                        "rovata",
                        "minden",
                        "héten",
                        "megnevettette",
                        "az",
                        "olvasókat."
                    ],
                    "solution": [
                        "A",
                        "lap",
                        "népszerű",
                        "karikatúra",
                        "rovata",
                        "minden",
                        "héten",
                        "megnevettette",
                        "az",
                        "olvasókat."
                    ],
                    "english": "The paper's popular caricature column made readers laugh every week.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence stating that censors could hardly ban the paper without scandal using 'aligha'.",
                            "answer": "A hatóságok aligha tilthatták be a lapot anélkül, hogy hatalmas felháborodást keltettek volna."
                        },
                        {
                            "prompt": "State that one could hardly find a more influential cartoonist than Tibor Kaján using 'Aligha...'.",
                            "answer": "Aligha találhatunk Kaján Tibornál nagyobb hatású karikaturistát a huszadik századi sajtóban."
                        }
                    ],
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                }
            ]
        },
        {
            "num": 5,
            "title": "Why Hungarian Humor Thrives on Self-Irony",
            "grammar_label": "Modal reservation and unexpected concession with éppenséggel ('actually / if anything')",
            "goals": [
                "I can articulate why self-deprecating humor and linguistic absurdism (Karinthy, Örkény) characterize Hungarian identity.",
                "I can qualify claims, introduce concessions, and hedge assertions using éppenséggel.",
                "I can synthesize the themes of cabaret, satire, and resilience across twentieth-century Hungarian culture."
            ],
            "story_segment": {
                "seg_slug": "onironia",
                "title": "Miért nevet a magyar saját magán?",
                "summary": "Frigyes Karinthy famously wrote that he took humor too seriously to joke about it: self-irony in Hungarian culture is not defeatism, but the ultimate declaration of intellectual sovereignty.",
                "location": "Budapest kávéházai és színházai",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "„A humorban nem ismerek tréfát” — írta híres aforizmájában Karinthy Frigyes, a huszadik századi magyar irodalom egyik legnagyobb szelleme. Ez az első pillantásra paradox kijelentés pontosan megragadja a magyar humor lényegét: az irónia és a szatíra nálunk soha nem felszínes bohóckodás, hanem a legmélyebb filozófiai önismeret és valóságérzékelés formája."
                    },
                    {
                        "type": "narration",
                        "text": "A magyar kultúrában az önirónia korántsem azonos az önfeladással vagy az önostorozással. Éppenséggel a belső szellemi függetlenség végső menedékét jelenti. Amikor egy nép a történelme során számtalan vereséget, megszállást és csalódást kénytelen elviselni, a saját hibáin és gyarlóságain való nevetés megóvja a lelkét a végzetes megkeseredéstől."
                    },
                    {
                        "type": "narration",
                        "text": "Örkény István az 1960-as években az Egyperces novellák műfajával emelte világirodalmi szintre a groteszk magyar humort. Az abszurd, mindössze néhány soros történetek megmutatták, hogy a háborúk és diktatúrák poklában a túlélés egyetlen méltó eszköze a fanyar, keserédes látásmód. Az emberi butaságot nem leordítani kell, hanem finom iróniával bemutatni."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a fajta humor éppenséggel abban segít, hogy reálisan lássuk a világot: ne higgyünk a dagályos pátosznak és az üres ideológiai jelszavaknak. A pesti vicc mesélője és hallgatója cinkos pillantást vált, jelezve, hogy átlátnak a hivatalos kulisszákon, és tisztában vannak a dolgok valódi természetével."
                    },
                    {
                        "type": "narration",
                        "text": "A pesti kabaré, Karinthy paródiái, Hofi Géza monológjai és Örkény egypercesei mind ugyanabból a tiszta forrásból táplálkoznak. A magyar humor nem menekülés a valóság elől, hanem szuverén válasz a történelem kihívásaira: amíg nevetni tudunk önmagunkon, addig legyőzhetetlenek vagyunk."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "önostorozás",
                    "translation": "self-flagellation / harsh self-criticism",
                    "pos": "noun"
                },
                {
                    "lemma": "éppenséggel",
                    "translation": "actually / for that matter / if anything",
                    "pos": "adverb"
                },
                {
                    "lemma": "egyperces novella",
                    "translation": "one-minute short story",
                    "pos": "noun"
                },
                {
                    "lemma": "szuverenitás",
                    "translation": "sovereignty",
                    "pos": "noun"
                },
                {
                    "lemma": "keserédes",
                    "translation": "bittersweet",
                    "pos": "adjective"
                },
                {
                    "lemma": "groteszk",
                    "translation": "grotesque",
                    "pos": "adjective"
                }
            ],
            "grammar_doc": {
                "slug": "discourse-particle-eppenseggel",
                "title": "Modal Nuance: éppenséggel",
                "text1_title": "Concessive Nuance and Pragmatic Softening",
                "text1": "The modal particle éppenséggel ('actually / for that matter / if anything / as a matter of fact') qualifies an assertion by introducing an unexpected concession, potential possibility, or mild hedge. It signals that although a perspective might seem contrary to intuition, it is perfectly valid.",
                "text2_title": "Syntactic Functions and Hedging",
                "text2": "Éppenséggel frequently co-occurs with conditional verb forms or potential suffixes (-hat/-het) to offer polite alternative interpretations: 'Ezt éppenséggel másképp is értelmezhetjük' (We could actually interpret this differently). In negative sentences, it softens critique.",
                "table_title": "Modal Qualification with éppenséggel",
                "table_rows": [
                    [
                        "A magyar önirónia éppenséggel a szellemi szuverenitás jele.",
                        "Hungarian self-irony is actually a mark of intellectual sovereignty."
                    ],
                    [
                        "Örkény egypercesei éppenséggel mély tragédiaként is olvashatók.",
                        "Örkény's one-minute stories could actually be read as profound tragedies as well."
                    ],
                    [
                        "Nem éppenséggel a legszerencsésebb megoldás volt, de működött.",
                        "It was not exactly the most fortunate solution, but it worked."
                    ],
                    [
                        "Ezt a fanyar humort éppenséggel a külföldi olvasók is megérthetik.",
                        "This dry humor can actually be understood by foreign readers as well."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A nevetés éppenséggel megóvta az embereket attól, hogy elkeseredetté váljanak.",
                        "english": "Laughter actually protected people from becoming embittered."
                    },
                    {
                        "spanish": "Karinthy paródiái éppenséggel a legmélyebb tiszteletből születtek a parodizált szerzők iránt.",
                        "english": "Karinthy's parodies were actually born of the deepest respect toward the parodied authors."
                    },
                    {
                        "spanish": "A groteszk szemlélet éppenséggel a legőszintébb realizmusként fogható fel.",
                        "english": "The grotesque perspective can actually be conceived of as the most sincere realism."
                    }
                ],
                "tip": "Use éppenséggel when presenting a counter-intuitive observation in your B2 argumentation: 'A kudarc éppenséggel új lehetőségeket nyitott meg' (Failure actually opened up new possibilities)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen műfajt teremtett meg Örkény István az 1960-as években?",
                    "options": [
                        "Az abszurd és fanyar humorra épülő, tömör 'egyperces novella' műfaját.",
                        "A többszáz oldalas történelmi verses lovagregényt.",
                        "A rádiós politikai hírműsorok hivatalos tudósítását."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A magyar kultúrában a humor nem romboló _____, hanem a túlélést segítő belső erő. (self-flagellation)",
                    "answer": "önostorozás",
                    "english": "In Hungarian culture, humor is not destructive self-flagellation, but an inner strength helping survival.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A fanyar önirónia _____ a nemzeti önbecsülés és függetlenség sajátos jeleként is felfogható. (actually / for that matter)",
                    "answer": "éppenséggel",
                    "english": "Dry self-irony can actually be conceived of as a distinctive sign of national self-esteem and independence.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban fejez ki az 'éppenséggel' finom, óvatos megerősítést vagy engedményt?",
                    "options": [
                        "Karinthy szellemes aforizmái éppenséggel korunkban is érvényes igazságokat hordoznak.",
                        "Karinthy szellemes aforizmái holott korunkban is érvényes igazságokat hordoznak.",
                        "Karinthy szellemes aforizmái jóllehet korunkban is érvényes igazságokat hordoznak."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "groteszk",
                        "látásmód",
                        "éppenséggel",
                        "a",
                        "legmélyebb",
                        "valóságérzékelésből",
                        "fakad."
                    ],
                    "solution": [
                        "A",
                        "groteszk",
                        "látásmód",
                        "éppenséggel",
                        "a",
                        "legmélyebb",
                        "valóságérzékelésből",
                        "fakad."
                    ],
                    "english": "The grotesque perspective actually stems from the deepest perception of reality.",
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan értelmezte Karinthy Frigyes a humort híres mondásában?",
                    "options": [
                        "A humort olyan komoly dolognak tartotta, amelyben nem ismert felszínes tréfálkozást.",
                        "Úgy gondolta, hogy a humornak semmi köze sincs a valódi irodalomhoz.",
                        "Kizárólag pénzkereseti forrásként tekintett a színházi jelenetekre."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "Örkény",
                        "abszurd",
                        "és",
                        "keserédes",
                        "történetei",
                        "nemzetközi",
                        "hírnevet",
                        "szereztek",
                        "a",
                        "magyar",
                        "irodalomnak."
                    ],
                    "solution": [
                        "Örkény",
                        "abszurd",
                        "és",
                        "keserédes",
                        "történetei",
                        "nemzetközi",
                        "hírnevet",
                        "szereztek",
                        "a",
                        "magyar",
                        "irodalomnak."
                    ],
                    "english": "Örkény's absurd and bittersweet stories brought international fame to Hungarian literature.",
                    "teaches": [
                        "b2-pestihumor-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence claiming that Hungarian humor can actually be seen as an art of survival using 'éppenséggel'.",
                            "answer": "A pesti humor éppenséggel a történelmi túlélés legkifinomultabb művészeteként is értelmezhető."
                        },
                        {
                            "prompt": "State that laughing at ourselves actually protects us from despair using 'éppenséggel'.",
                            "answer": "Az önmagunkon való nevetés éppenséggel megvédi a közösséget a végső kétségbeeséstől."
                        }
                    ],
                    "teaches": [
                        "b2-discourse-particles"
                    ]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can synthesize the development of Budapest cabaret from Endre Nagy to Géza Hofi and Örkény István.",
            "I can accurately deploy modal and discourse particles (hiszen, ugyebár, korántsem, aligha, éppenséggel) to convey subtle pragmatic stance.",
            "I can discuss historical satire, political censorship, and self-irony in sophisticated B2 Hungarian."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik partikula fejez ki határozott, kategorikus cáfolatot egy feltételezéssel szemben?",
                "options": [
                    "korántsem",
                    "hiszen",
                    "ugyebár"
                ],
                "correct": 0,
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "question": "Ki volt a klasszikus pesti kabaré megteremtője a Nagymező utcában?",
                "options": [
                    "Nagy Endre",
                    "Kaján Tibor",
                    "Ágai Adolf"
                ],
                "correct": 0,
                "teaches": [
                    "b2-pestihumor-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik partikula hivatkozik a beszélő és a hallgató közös, magától értetődő háttértudására?",
                "options": [
                    "hiszen",
                    "aligha",
                    "korántsem"
                ],
                "correct": 0,
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A szocialista korszak cenzorai _____ engedték volna meg az 1956-os forradalom nyílt megvitatását. (hardly / scarcely)",
                "answer": "aligha",
                "english": "The censors of the socialist era would hardly have allowed the open discussion of the 1956 revolution.",
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "sentence": "A Mikroszkóp Színpad a politikai feszültségek levezetésére szolgáló bizalmi _____ funkcióját töltötte be. (safety valve)",
                "answer": "szelep",
                "english": "The Mikroszkóp Színpad fulfilled the function of a safety valve designed to relieve political tensions.",
                "teaches": [
                    "b2-pestihumor-vocab"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A politikai viccek sikere _____ jelentette azt, hogy a társadalom feladta volna a szabadságvágyát. (by no means)",
                "answer": "korántsem",
                "english": "The success of political jokes by no means meant that society had given up its desire for freedom.",
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "in-context",
                "tiles": [
                    "A",
                    "pesti",
                    "ember,",
                    "ugyebár,",
                    "még",
                    "az",
                    "óvóhelyen",
                    "is",
                    "viccet",
                    "mesélt."
                ],
                "solution": [
                    "A",
                    "pesti",
                    "ember,",
                    "ugyebár,",
                    "még",
                    "az",
                    "óvóhelyen",
                    "is",
                    "viccet",
                    "mesélt."
                ],
                "english": "The Budapest resident, as is well known, told jokes even in the air raid shelter.",
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "stage": "in-context",
                "tiles": [
                    "Karinthy",
                    "paródiái",
                    "és",
                    "Örkény",
                    "groteszk",
                    "egypercesei",
                    "a",
                    "magyar",
                    "irodalom",
                    "remekművei."
                ],
                "solution": [
                    "Karinthy",
                    "paródiái",
                    "és",
                    "Örkény",
                    "groteszk",
                    "egypercesei",
                    "a",
                    "magyar",
                    "irodalom",
                    "remekművei."
                ],
                "english": "Karinthy's parodies and Örkény's grotesque one-minute stories are masterpieces of Hungarian literature.",
                "teaches": [
                    "b2-pestihumor-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "question": "Melyik mondatban fejez ki az 'éppenséggel' meglepő, de érvényes megállapítást?",
                "options": [
                    "A nevetés éppenséggel a legmélyebb belső szabadság kifejeződése volt a diktatúrában.",
                    "A nevetés aligha a legmélyebb belső szabadság kifejeződése volt a diktatúrában.",
                    "A nevetés korántsem a legmélyebb belső szabadság kifejeződése volt a diktatúrában."
                ],
                "correct": 0,
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "tiles": [
                    "Nem",
                    "kell",
                    "csodálkoznunk",
                    "a",
                    "sikeren,",
                    "hiszen",
                    "a",
                    "közönség",
                    "imádta",
                    "Hofit."
                ],
                "solution": [
                    "Nem",
                    "kell",
                    "csodálkoznunk",
                    "a",
                    "sikeren,",
                    "hiszen",
                    "a",
                    "közönség",
                    "imádta",
                    "Hofit."
                ],
                "english": "We need not wonder at the success, since after all the audience adored Hofi.",
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Synthesize the role of Budapest satire in dark times using 'hiszen' and 'aligha'.",
                        "answer": "A pesti vicc nélkül aligha élték volna túl a nehéz éveket, hiszen a nevetés jelentette az egyetlen szabad menedéket."
                    }
                ],
                "teaches": [
                    "b2-discourse-particles"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Explain the philosophical nature of Hungarian self-irony using 'korántsem' and 'éppenséggel'.",
                        "answer": "A magyar önirónia korántsem gyengeség, hanem éppenséggel a legmagasabb szintű szellemi szuverenitás bizonyítéka."
                    }
                ],
                "teaches": [
                    "b2-discourse-particles"
                ]
            }
        ]
    }
}


UNIT_14_MAGYARFILM = {
    "unit_num": 14,
    "slug": "magyarfilm",
    "title": "Allegory on Screen: A Century of Hungarian Cinema",
    "grammar_skill": "b2-simultaneity-conjunctions",
    "vocab_skill": "b2-magyarfilm-vocab",
    "theme": "Hungarian cinema from Hollywood pioneers to Jancsó, Szabó and Tarr",
    "location": "Kolozsvár, Hollywood, Budapest és a Hortobágy",
    "intro_body": [
        "From the earliest silent experiments in Kolozsvár and Budapest to the soundstages of Hollywood, Hungarian filmmakers have exerted an outsized influence on world cinema. Yet Hungarian cinema's greatest domestic triumph was developing a visual poetry of allegorical resistance: finding cinematic metaphors for freedom, power, and historical trauma when open dissent was impossible.",
        "In this unit, you will journey from Hollywood's Hungarian studio pioneers (Adolph Zukor, William Fox, Michael Curtiz) to the choreographies of Miklós Jancsó, István Szabó's Oscar-winning Mephisto, the auteur vision of Márta Mészáros and Béla Tarr, and contemporary masterworks like Saul fia. Grammatically, you will master subordinating conjunctions of simultaneity, immediate sequence, and proportional recurrence (miközben, mialatt, amint, mihelyt, valahányszor)."
    ],
    "combined_story_title": "A pusztai plánoktól az Oscar-díjig: A magyar film története",
    "combined_story_summary": "A century of Hungarian filmmaking: from the Hungarian emigrants who founded Hollywood to Miklós Jancsó's long-take historical parables, István Szabó's Mephisto, Márta Mészáros, Béla Tarr's Sátántangó, and contemporary international acclaim.",
    "lessons": [
        {
            "num": 1,
            "title": "Hungarians Who Built Classic Hollywood",
            "grammar_label": "Simultaneity and contrastive background action with miközben ('while / at the same time')",
            "goals": [
                "I can narrate the origins of Hollywood studios and the pivotal contributions of Adolph Zukor, William Fox, and Michael Curtiz (Kertész Mihály).",
                "I can connect concurrent events and contrast concurrent states using the conjunction miközben.",
                "I can discuss silent cinema, studio production, and film directing in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "hollywoodialapitok",
                "title": "A pesti kávéházaktól a Paramount stúdiójáig",
                "summary": "How Adolph Zukor from Ricse founded Paramount Pictures, William Fox from Tolcsva created 20th Century Fox, and Mihály Kertész directed Casablanca, laying the foundation of classic Hollywood cinema.",
                "location": "Ricse, Kolozsvár, Hollywood",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszadik század elején a mozgókép még csak vásári látványosságnak számított, ám néhány bátor és látnoki erejű magyar emigráns felismerte, hogy a film a modern világ legfontosabb művészeti és üzleti ágává válik. Zukor Adolf, aki a zempléni Ricséről vándorolt ki Amerikába szegény árvagyerekként, 1912-ben megalapította a Famous Players céget, amelyből később a legendás Paramount Pictures stúdió nőtt ki."
                    },
                    {
                        "type": "narration",
                        "text": "Zukorral szinte egy időben egy másik magyar származású fiatalember, a tolcsvai születésű Fuchs Vilmos — amerikai nevén William Fox — lerakta a Fox Film Corporation alapjait. Miközben az amerikai filmgyártás a keleti partról a napfényes Kaliforniába költözött, ezek a magyar producerek alakították ki a stúdiórendszer szabályait, felfedezve a sztárok vonzerejét és a nagyszabású történetmesélés erejét."
                    },
                    {
                        "type": "narration",
                        "text": "Nemcsak az üzletemberek, hanem a rendezők között is kiemelkedő szerepet játszottak a magyarok. Kertész Mihály, aki Budapesten és Kolozsváron sajátította el a némafilmes mesterséget Janovics Jenő műhelyében, Michael Curtiz néven Hollywood egyik legmegbízhatóbb rendezőjévé vált. 1942-ben ő rendezte meg a filmtörténet egyik legnagyobb klasszikusát, a Casablancát, elnyerve a legjobb rendezőnek járó Oscar-díjat."
                    },
                    {
                        "type": "narration",
                        "text": "A Paramount stúdió kapuján a legenda szerint egy tábla figyelmeztette a látogatókat: „Nem elég magyarnak lenni, tehetség is kell hozzá.” Miközben a magyar alkotók az amerikai álom megfilmesítésén dolgoztak, filmjeikben mindig megmaradt valami a közép-európai melankóliából, a feszes tempóból és a precíz képi kompozícióból."
                    },
                    {
                        "type": "narration",
                        "text": "Korda Sándor Nagy-Britanniában épített ki stúdióbirodalmat, Lugosi Béla Drakulaként vált a filmtörténet ikonjává, Rózsa Miklós pedig Oscar-díjas filmzenéivel teremtette meg a hollywoodi hangzást. A magyar jelenlét nélkül az egyetemes filmtörténet aranykora aligha lett volna ugyanaz."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "filmgyártás",
                    "translation": "film production",
                    "pos": "noun"
                },
                {
                    "lemma": "rendező",
                    "translation": "director",
                    "pos": "noun"
                },
                {
                    "lemma": "miközben",
                    "translation": "while / at the same time as",
                    "pos": "conjunction"
                },
                {
                    "lemma": "némafilm",
                    "translation": "silent film",
                    "pos": "noun"
                },
                {
                    "lemma": "forgatókönyv",
                    "translation": "screenplay / script",
                    "pos": "noun"
                },
                {
                    "lemma": "stúdiórendszer",
                    "translation": "studio system",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "simultaneity-mikozben",
                "title": "Simultaneity Conjunction: miközben",
                "text1_title": "Simultaneous Events and Background Framing",
                "text1": "The subordinating conjunction miközben ('while / at the same time as / during which') connects two clauses describing events occurring simultaneously. Often, one clause describes an ongoing background state or activity while the main clause introduces an event.",
                "text2_title": "Adversative Nuances ('whereas / while')",
                "text2": "In B2 literary and argumentative Hungarian, miközben frequently carries a contrastive or adversative shade, highlighting a surprising coexistence of two conflicting realities: 'Vagyonokat kerestek Amerikában, miközben sosem felejtették el szülőfalujukat'.",
                "table_title": "Simultaneity and Contrast with miközben",
                "table_rows": [
                    [
                        "Zukor megalapította a Paramount stúdiót, miközben új üzleti modelleket fejlesztett ki.",
                        "Zukor founded Paramount studios while developing new business models."
                    ],
                    [
                        "Kertész Mihály a Casablancát forgatta, miközben Európában dúlt a háború.",
                        "Michael Curtiz was filming Casablanca while war raged in Europe."
                    ],
                    [
                        "A stúdiók versengtek egymással, miközben mindketten magyar emigránsok kezében voltak.",
                        "The studios competed with each other, while both were in the hands of Hungarian emigrants."
                    ],
                    [
                        "A közönség a moziban nevetett, miközben a rendező a vágószobában izgult.",
                        "The audience laughed in the cinema while the director was anxious in the editing room."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Zukor Adolf meghódította a tengerentúli filmpiacot, miközben megőrizte kapcsolatát az európai kultúrával.",
                        "english": "Adolph Zukor conquered the overseas film market while preserving his connection with European culture."
                    },
                    {
                        "spanish": "Hollywoodban dolgoztak a világ legkiválóbb színészei, miközben a rendezői székben gyakran magyar alkotók ültek.",
                        "english": "The world's most outstanding actors worked in Hollywood, while Hungarian creators often sat in the director's chair."
                    },
                    {
                        "spanish": "A hangosfilm forradalmasította az ipart, miközben sok némafilmes sztár karrierje derékba tört.",
                        "english": "Sound film revolutionized the industry, while the careers of many silent film stars were cut short."
                    }
                ],
                "tip": "Use miközben to link concurrent actions in both past and present. Always place a comma before miközben when it introduces a subordinate clause."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit takar a 'stúdiórendszer' fogalma a klasszikus hollywoodi korszakban?",
                    "options": [
                        "A filmgyártást, a forgalmazást és a mozikat egyetlen nagyvállalat kezében egyesítő ipari modellt.",
                        "A forgatási helyszínek közötti buszjáratok menetrendjét.",
                        "A filmvetítő gépek alkatrészeit gyártó manufaktúrákat."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Kertész Mihály nemzetközi hírű _____ lett, aki több mint száz filmet készített pályája során. (director)",
                    "answer": "rendező",
                    "english": "Michael Curtiz became an internationally renowned director who made more than one hundred films during his career.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Kertész a Casablancát rendezte, _____ Európában milliók menekültek a háborús pusztítás elől. (while / at the same time)",
                    "answer": "miközben",
                    "english": "Curtiz was directing Casablanca while in Europe millions were fleeing war devastation.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen két cselekvés egyidejűségét és ellentétét a 'miközben' kötőszóval?",
                    "options": [
                        "A producerek hatalmas profitot könyveltek el, miközben az írók gyakran háttérbe szorultak.",
                        "A producerek hatalmas profitot könyveltek el, holott az írók csakugyan háttérbe szorultak.",
                        "A producerek hatalmas profitot könyveltek el, amennyiben az írók háttérbe szorulnak."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "magyar",
                        "alkotók",
                        "Hollywoodot",
                        "építették,",
                        "miközben",
                        "megőrizték",
                        "közép-európai",
                        "identitásukat."
                    ],
                    "solution": [
                        "A",
                        "magyar",
                        "alkotók",
                        "Hollywoodot",
                        "építették,",
                        "miközben",
                        "megőrizték",
                        "közép-európai",
                        "identitásukat."
                    ],
                    "english": "Hungarian creators built Hollywood while preserving their Central European identity.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen jelentős stúdiót alapított a magyar származású Zukor Adolf?",
                    "options": [
                        "A Paramount Pictures stúdiót.",
                        "A Walt Disney animációs stúdiót.",
                        "A Cinecittà római filmvárost."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "hangosfilm",
                        "megjelenése",
                        "alapjaiban",
                        "változtatta",
                        "meg",
                        "a",
                        "modern",
                        "filmgyártás",
                        "menetét."
                    ],
                    "solution": [
                        "A",
                        "hangosfilm",
                        "megjelenése",
                        "alapjaiban",
                        "változtatta",
                        "meg",
                        "a",
                        "modern",
                        "filmgyártás",
                        "menetét."
                    ],
                    "english": "The emergence of sound film fundamentally changed the course of modern film production.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing Adolph Zukor's dual achievements using 'miközben'.",
                            "answer": "Zukor Adolf meghódította a globális filmpiacot, miközben folyamatosan támogatta szülőföldjének rászorulóit."
                        },
                        {
                            "prompt": "Contrast the success of Hollywood directors with European turbulence using 'miközben'.",
                            "answer": "Kertész Mihály az amerikai film aranykorát építette, miközben Európa lángokban állt."
                        }
                    ],
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                }
            ]
        },
        {
            "num": 2,
            "title": "Miklós Jancsó: Choreography of Power and History",
            "grammar_label": "Parallel duration and ongoing timeframe with mialatt ('during which / while')",
            "goals": [
                "I can describe Miklós Jancsó's cinematic style: long sequence shots, bare landscapes (Hortobágy), and geometric choreography of power.",
                "I can express actions transpiring simultaneously over an extended temporal window using mialatt.",
                "I can analyze cinematic allegories, historical parables, and power dynamics in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "jancsomiklos",
                "title": "Jancsó Miklós: A hatalom koreográfiája",
                "summary": "In masterpieces like Szegénylegények and Csillagosok, katonák, Miklós Jancsó invented a revolutionary visual language using unbroken ten-minute takes across the Hungarian plain to dissect authoritarian control.",
                "location": "Hortobágy és a kunsági puszta (1960-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1960-as években a magyar filmművészet olyan vizuális forradalmat élt át, amely azonnal a világ élvonalába repítette a hazai rendezőket. Ennek a korszaknak a legnagyobb hatású újítója Jancsó Miklós volt. Jancsó szakított a hagyományos lélektani realizmussal, és egy teljesen egyéni, költői filmnyelvet dolgozott ki, amelyben az elnyomás és a hatalom mechanizmusai váltak főszereplővé."
                    },
                    {
                        "type": "narration",
                        "text": "Legismertebb remekműve, az 1965-ben bemutatott Szegénylegények az 1848–49-es szabadságharc utáni megtorlást jelenítette meg egy pusztai sáncerődben. A filmben alig volt párbeszéd: a dráma a rideg tekintetekből, a katonai parancsokból és a megalázó kihallgatásokból épült fel. Mialatt a rabok körbe-körbe masíroztak a deszkafalak között, a néző a modern diktatúrák lélektanát ismerhette fel a vásznon."
                    },
                    {
                        "type": "narration",
                        "text": "Jancsó védjegyévé a rendkívül hosszú beállítások váltak. Egy-egy jelenet akár nyolc-tíz percig is tartott vágás nélkül: a kamera folytonos mozgásban volt, darukon emelkedett a magasba vagy lovasok között siklott a fűben. A sík kunsági puszta tágas horizontja éles ellentétben állt a szereplők bezártságával és kiszolgáltatottságával."
                    },
                    {
                        "type": "narration",
                        "text": "A szereplők nem egyénített személyekként, hanem hatalmi csoportok képviselőiként mozogtak a térben: egyenruhások és meztelenre vetkőztetett foglyok, elnyomók és áldozatok cseréltek helyet egy kegyetlen rituális koreográfiában. Mialatt a kamera körbefogta a csoportokat, a hatalom változékonysága és abszurditása vált nyilvánvalóvá."
                    },
                    {
                        "type": "narration",
                        "text": "A Szegénylegények a cannes-i filmfesztiválon óriási nemzetközi sikert aratott. Bár a hivatalos cenzúra történelmi kosztümös drámaként engedélyezte a filmet, a kortárs közönség pontosan érezte, hogy Jancsó parabolája az 1956 utáni kádári megtorlások és az elnyomó mechanizmusok leleplezése volt."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "hosszú beállítás",
                    "translation": "long take / sequence shot",
                    "pos": "noun"
                },
                {
                    "lemma": "mialatt",
                    "translation": "while / during the time that",
                    "pos": "conjunction"
                },
                {
                    "lemma": "allegória",
                    "translation": "allegory",
                    "pos": "noun"
                },
                {
                    "lemma": "puszta",
                    "translation": "plain / steppe",
                    "pos": "noun"
                },
                {
                    "lemma": "koreográfia",
                    "translation": "choreography",
                    "pos": "noun"
                },
                {
                    "lemma": "elnyomás",
                    "translation": "oppression / repression",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "simultaneity-mialatt",
                "title": "Parallel Duration: mialatt",
                "text1_title": "Stretching Across Time: mialatt",
                "text1": "The conjunction mialatt ('during the time that / while') emphasizes temporal duration and ongoing span. Unlike miközben, which can also mark an adversative contrast, mialatt focuses purely on the temporal envelope during which another process takes place.",
                "text2_title": "Aspect and Verb Tenses with mialatt",
                "text2": "Clauses connected by mialatt usually employ imperfective verbs (often with ongoing past or present actions) because the main action is framed as occurring inside the temporal boundaries of the subordinate event.",
                "table_title": "Temporal Duration Patterns with mialatt",
                "table_rows": [
                    [
                        "A kamera percekig pásztázta a pusztát, mialatt a foglyok némán meneteltek.",
                        "The camera panned across the plain for minutes while the prisoners marched in silence."
                    ],
                    [
                        "Mialatt a katonák felállították az alakzatot, a tisztek a háttérben tanácskoztak.",
                        "While the soldiers set up the formation, the officers conferred in the background."
                    ],
                    [
                        "A néző feszülten figyelte a képeket, mialatt a feszültség fokozatosan növekedett.",
                        "The viewer watched the images tensely, while the tension gradually increased."
                    ],
                    [
                        "Sokan elhagyták az országot, mialatt a diktatúra megszilárdította hatalmát.",
                        "Many left the country while the dictatorship consolidated its power."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Jancsó filmjeiben a kamera folyamatosan mozgásban volt, mialatt a szereplők rideg geometriai alakzatokba rendeződtek.",
                        "english": "In Jancsó's films the camera was continuously in motion while the actors arranged themselves into cold geometric formations."
                    },
                    {
                        "spanish": "Mialatt a cenzúra a direkt politikai utalásokat kereste, a rendező az egyetemes hatalmi mechanizmusokat ábrázolta.",
                        "english": "While the censorship looked for direct political references, the director depicted universal mechanisms of power."
                    },
                    {
                        "spanish": "A cannes-i fesztivál közönsége lélegzetvisszafojtva nézte a Szegénylegényeket, mialatt a nemzetközi kritikusok az új filmnyelvet méltatták.",
                        "english": "The audience at the Cannes festival watched The Round-Up holding their breath while international critics praised the new cinematic language."
                    }
                ],
                "tip": "Choose mialatt when you want to highlight the continuous temporal duration of an activity ('during the time that...'). Choose miközben when you want to contrast two simultaneous states."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'hosszú beállítás' a filmrendezésben?",
                    "options": [
                        "Olyan filmjelenetet, amelyet percekig rögzítenek vágás és megszakítás nélkül.",
                        "A színészek arcának sminkelésére szánt időtartamot.",
                        "A mozijegyek elővételi árusításának határidejét."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A Szegénylegények a hatalom és az _____ egyetemes mechanizmusait mutatta be a pusztai díszletben. (oppression)",
                    "answer": "elnyomás",
                    "english": "The Round-Up presented the universal mechanisms of power and oppression in the steppe setting.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A kamera tíz percen át követte a lovasokat, _____ a szereplők egyetlen szót sem szóltak. (during which / while)",
                    "answer": "mialatt",
                    "english": "The camera followed the riders for ten minutes, during which the actors did not speak a single word.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki a párhuzamos időtartamot a 'mialatt' kötőszóval?",
                    "options": [
                        "Mialatt a tisztek a sánc tetején álltak, a rabokat a belső udvarra terelték.",
                        "Feltéve, hogy a tisztek a sánc tetején álltak, a rabokat terelték.",
                        "Minél tovább a tisztek a sánc tetején álltak, annál rabokat terelték."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Mialatt",
                        "a",
                        "fogvatartók",
                        "tanácskoztak,",
                        "a",
                        "rabok",
                        "némán",
                        "várták",
                        "a",
                        "döntést."
                    ],
                    "solution": [
                        "Mialatt",
                        "a",
                        "fogvatartók",
                        "tanácskoztak,",
                        "a",
                        "rabok",
                        "némán",
                        "várták",
                        "a",
                        "döntést."
                    ],
                    "english": "While the captors conferred, the prisoners silently awaited the decision.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan ábrázolta Jancsó Miklós a történelmi konfliktusokat a Szegénylegényekben?",
                    "options": [
                        "Hosszú beállításokkal, ritmikus csoportmozgásokkal és a pusztai tér geometriai koreográfiájával.",
                        "Gyors vágásokkal és pörgős akciójelenetekkel teli hollywoodi stílusban.",
                        "Kizárólag stúdióban felvett, zárt szobai viták formájában."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "magyar",
                        "puszta",
                        "kopár",
                        "tájképe",
                        "a",
                        "történelmi",
                        "kiszolgáltatottság",
                        "erőteljes",
                        "allegóriája",
                        "volt."
                    ],
                    "solution": [
                        "A",
                        "magyar",
                        "puszta",
                        "kopár",
                        "tájképe",
                        "a",
                        "történelmi",
                        "kiszolgáltatottság",
                        "erőteljes",
                        "allegóriája",
                        "volt."
                    ],
                    "english": "The barren landscape of the Hungarian plain was a powerful allegory of historical vulnerability.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing the simultaneous movement of actors and camera in Jancsó's film using 'mialatt'.",
                            "answer": "A kamera folyamatosan siklott a horizont előtt, mialatt a katonák rideg alakzatokba rendeződtek."
                        },
                        {
                            "prompt": "State how the historical parable spoke to the audience using 'mialatt'.",
                            "answer": "Mialatt a film látszólag a múltat ábrázolta, a közönség a jelenkor elnyomását látta a vásznon."
                        }
                    ],
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                }
            ]
        },
        {
            "num": 3,
            "title": "István Szabó and Moral Compromise in Central Europe",
            "grammar_label": "Punctual simultaneity and immediate trigger with amint ('as soon as / the moment that')",
            "goals": [
                "I can discuss István Szabó's Oscar-winning Mephisto, Redl ezredes, and Hanussen regarding intellectual compromise with power.",
                "I can connect an immediate sequential trigger to a resulting action using amint.",
                "I can debate Central European identity, artistic responsibility, and moral compromise in B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szaboistvan",
                "title": "Szabó István és a Mephisto dilemmája",
                "summary": "In 1982, István Szabó won Hungary's first Oscar for Best Foreign Language Film with Mephisto, exploring how actor Hendrik Höfgen sold his soul to fascist power for artistic vanity.",
                "location": "Budapest és Berlin (1981)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1982 márciusában Los Angelesben, a Dorothy Chandler Pavilionban felhangzott a bejelentés: a legjobb idegen nyelvű filmnek járó Oscar-díjat a magyar Mephisto kapta. Szabó István rendezése hozta el Magyarország első Oscar-díját ebben a kategóriában, és nemzetközi szinten is a huszadik századi erkölcsi dilemmák legfontosabb filmes reflexiójává vált."
                    },
                    {
                        "type": "narration",
                        "text": "A Klaus Mann regénye alapján készült film Hendrik Höfgen színész sorsát követi nyomon a náci Németországban. Höfgen, akit a zseniális osztrák színművész, Klaus Maria Brandauer alakított, tehetséges és ambiciózus művész, aki kezdetben baloldali színházakban lép fel. Amint azonban megérzi a hatalom és a hírnév vonzását, fokozatosan feladja minden erkölcsi elvét, és a náci kultúrpolitika ünnepelt bábjává válik."
                    },
                    {
                        "type": "narration",
                        "text": "Szabó István filmje korántsem csak a fasizmusról szólt. A közép-európai értelmiségi örök drámáját fogalmazta meg: meddig mehet el a művész az államhatalommal kötött kompromisszumokban? Höfgen kétségbeesett mondata a hatalmas, üres stadion fénycsóváiban — „Mit akarnak tőlem? Hiszen én csak egy színész vagyok!” — a megalkuvás leplezetlen önvallomásává vált."
                    },
                    {
                        "type": "narration",
                        "text": "A Mephisto sikere után Szabó megalkotta a történelmi trilógia további darabjait, a Redl ezredest és a Hanussent. Ezek a művek amint bemutatásra kerültek a világ mozijában, azonnal viták sorát indították el arról, miként torzítja el a totalitárius hatalom a személyiséget, a lojalitást és az emberi méltóságot."
                    },
                    {
                        "type": "narration",
                        "text": "Szabó István életműve arra tanít, hogy a művészet sohasem független a politikától: a tehetség nem mentesít a személyes felelősség alól, és a hatalommal kötött paktum előbb-utóbbi a lélek elvesztéséhez vezet."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "erkölcsi kompromisszum",
                    "translation": "moral compromise",
                    "pos": "noun"
                },
                {
                    "lemma": "amint",
                    "translation": "as soon as / the moment that",
                    "pos": "conjunction"
                },
                {
                    "lemma": "főszereplő",
                    "translation": "protagonist / lead actor",
                    "pos": "noun"
                },
                {
                    "lemma": "megalkuvás",
                    "translation": "opportunism / capitulation / compromise",
                    "pos": "noun"
                },
                {
                    "lemma": "színművész",
                    "translation": "actor / dramatic artist",
                    "pos": "noun"
                },
                {
                    "lemma": "díjátadó",
                    "translation": "award ceremony",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "simultaneity-amint",
                "title": "Immediate Simultaneity: amint",
                "text1_title": "Punctual Simultaneity and Instant Triggers",
                "text1": "The conjunction amint ('as soon as / the moment that / just as') marks immediate temporal sequence and punctual coincidence: event B occurs immediately upon the realization or inception of event A.",
                "text2_title": "Word Order and Verbal Aspect with amint",
                "text2": "Subordinate clauses introduced by amint often feature perfective verbs (with verbal prefixes like meg-, el-, fel-), indicating the completion of the triggering condition: 'Amint átvette a díjat, a rendező megköszönte stábja munkáját'.",
                "table_title": "Immediate Triggering with amint",
                "table_rows": [
                    [
                        "Amint bemutatták a Mephistót, a nemzetközi sajtó azonnal remekműként ünnepelte.",
                        "As soon as Mephisto was screened, the international press immediately celebrated it as a masterpiece."
                    ],
                    [
                        "A színész engedett a kísértésnek, amint megérezte a hatalom vonzerejét.",
                        "The actor yielded to temptation the moment he felt the allure of power."
                    ],
                    [
                        "Amint elhangzott a győztes neve, az egész magyar küldöttség felugrott a helyéről.",
                        "As soon as the winner's name was uttered, the whole Hungarian delegation jumped from their seats."
                    ],
                    [
                        "A nézők megértették a párhuzamot, amint meghallották a főhős védekezését.",
                        "The viewers understood the parallel as soon as they heard the protagonist's defense."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Amint Szabó István átvette az Oscar-díjat 1982-ben, a magyar filmművészet felkerült a világ térképére.",
                        "english": "As soon as István Szabó received the Oscar in 1982, Hungarian cinema was put on the world map."
                    },
                    {
                        "spanish": "A diktatúra valódi természete lelepleződik, amint a művész szembesül saját lelkiismeretével.",
                        "english": "The true nature of dictatorship is unveiled as soon as the artist confronts his own conscience."
                    },
                    {
                        "spanish": "Amint Höfgen felölti a Mephisto-maszkot, elveszíti emberi szuverenitását.",
                        "english": "As soon as Höfgen puts on the Mephisto mask, he loses his human sovereignty."
                    }
                ],
                "tip": "Use amint when you want to capture the precise instant when one event triggers another: 'Amint belépett a szobába, mindenki elhallgatott'."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'megalkuvás' fogalma Szabó István Mephisto című filmjében?",
                    "options": [
                        "A saját erkölcsi elvek feladását és a hatalomhoz való elvtelen dörgölőzést a karrier érdekében.",
                        "A színházi szerződés pontos és tisztességes betartását.",
                        "A forgatókönyv nyomdai hibáinak javítását a próbák előtt."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Klaus Maria Brandauer felejthetetlen alakítást nyújtott a Mephisto című film _____ szerepében. (protagonist)",
                    "answer": "főszereplő",
                    "english": "Klaus Maria Brandauer gave an unforgettable performance in the role of the protagonist of Mephisto.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A színész azonnal eladta a lelkét, _____ felkínálták neki a nemzeti színház igazgatói székét. (as soon as)",
                    "answer": "amint",
                    "english": "The actor sold his soul immediately, as soon as he was offered the director's chair of the national theatre.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen az azonnali időbeli következményt az 'amint' kötőszóval?",
                    "options": [
                        "Amint a díjátadó ceremónián kinyitották a borítékot, kiderült a magyar film győzelme.",
                        "Amint kinyitották a borítékot, holott a magyar film győzött.",
                        "Amint kinyitották a borítékot, minél inkább kiderült a győzelem."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Amint",
                        "a",
                        "film",
                        "véget",
                        "ért,",
                        "a",
                        "nézők",
                        "döbbenten",
                        "gondolkodtak",
                        "a",
                        "kompromisszumokról."
                    ],
                    "solution": [
                        "Amint",
                        "a",
                        "film",
                        "véget",
                        "ért,",
                        "a",
                        "nézők",
                        "döbbenten",
                        "gondolkodtak",
                        "a",
                        "kompromisszumokról."
                    ],
                    "english": "As soon as the film ended, the viewers reflected in shock on the compromises.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen díjat nyert el Szabó István Mephisto című alkotása 1982-ben?",
                    "options": [
                        "A legjobb idegen nyelvű filmnek járó Oscar-díjat.",
                        "A Berlini Nemzetközi Filmfesztivál Arany Medve díját.",
                        "A Velencei Nemzetközi Filmfesztivál Arany Oroszlán díját."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "művész",
                        "súlyos",
                        "erkölcsi",
                        "kompromisszumot",
                        "kötött",
                        "a",
                        "politikai",
                        "hatalommal."
                    ],
                    "solution": [
                        "A",
                        "művész",
                        "súlyos",
                        "erkölcsi",
                        "kompromisszumot",
                        "kötött",
                        "a",
                        "politikai",
                        "hatalommal."
                    ],
                    "english": "The artist struck a grave moral compromise with political power.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing the moment Mephisto won the Oscar using 'amint'.",
                            "answer": "Amint bejelentették a Mephisto győzelmét, Szabó István történelmet írt a magyar filmművészetben."
                        },
                        {
                            "prompt": "State how an intellectual succumbs to authoritarian power using 'amint'.",
                            "answer": "A művész elveszíti integritását, amint a karrierjét a lelkiismerete elé helyezi."
                        }
                    ],
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                }
            ]
        },
        {
            "num": 4,
            "title": "Márta Mészáros and Béla Tarr: Realism and Cosmic Time",
            "grammar_label": "Instantaneous succession and non-negotiable immediacy with mihelyt ('as soon as / no sooner than')",
            "goals": [
                "I can contrast Márta Mészáros's intimate historical memoirs (Napló gyermekeimnek) with Béla Tarr's hypnotic slow cinema (Sátántangó, Werckmeister harmóniák).",
                "I can use mihelyt to express strict immediate sequence and instant temporal consequence.",
                "I can critique cinematic pacing, black-and-white cinematography, and philosophical existentialism in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "meszarostarr",
                "title": "Mészáros Márta és Tarr Béla: A valóság két tükre",
                "summary": "From Márta Mészáros's courageous autobiographical diary films confronting Stalinism to Béla Tarr's meditative, seven-hour Sátántangó capturing the weight of cosmic time.",
                "location": "Budapest, vidéki elhagyatott kollektívák",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A magyar szerzői film a nyolcvanas és kilencvenes években két olyan radikálisan eltérő, mégis korszakos alkotóval gazdagodott, akik a filmnyelv határait feszegették: Mészáros Mártával és Tarr Bélával. Mindketten a fekete-fehér képi világ szigorú puritánságát választották, ám teljesen más szemszögből vizsgálták az emberi létezést."
                    },
                    {
                        "type": "narration",
                        "text": "Mészáros Márta a női nézőpont és az önéletrajzi emlékezet úttörőjévé vált a kelet-európai filmművészetben. Híres Napló-sorozatában (Napló gyermekeimnek, Napló szerelmeimnek) a sztálinista ötvenes évek személyes traumáit és az 1956-os forradalom tabuit tárta fel. Mihelyt a filmek a nemzetközi közönség elé kerültek, Cannes-ban a Zsűri Különdíjával jutalmazták a rendezőnő kérlelhetetlen történelmi őszinteségét."
                    },
                    {
                        "type": "narration",
                        "text": "Ezzel szemben Tarr Béla a lassú film (slow cinema) nemzetközileg elismert prófétájává lépett elő. Krasznahorkai László íróval és Vig Mihály zeneszerzővel közösen megalkotott monumentális munkái — mint a hétórás Sátántangó és a Werckmeister harmóniák — nem politikai történeteket mesélnek, hanem a létezés kozmikus súlyát és a reményvesztettséget ragadják meg."
                    },
                    {
                        "type": "narration",
                        "text": "Tarr filmjeiben az idő maga válik matériává: mihelyt a kamera elindul az esőáztatta, sáros utcán vagy egy kocsmai tánc hipnotikus forgatagában, a néző kilép a hétköznapi időérzékelésből. A végtelenül lassú plánok arra kényszerítenek bennünket, hogy szembenézzünk az emberi méltóság törékenységével és az elmúlással."
                    },
                    {
                        "type": "narration",
                        "text": "Mészáros Márta a történelem elhallgatott sebeit gyógyította meg a filmjeivel, míg Tarr Béla a modern civilizáció kiábrándultságának állított emléket. Mindketten bebizonyították, hogy a magyar filmművészet a kompromisszummentes alkotói szabadság legmagasabb csúcsaira képes eljutni."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "fekete-fehér film",
                    "translation": "black-and-white film",
                    "pos": "noun"
                },
                {
                    "lemma": "mihelyt",
                    "translation": "as soon as / no sooner than",
                    "pos": "conjunction"
                },
                {
                    "lemma": "önéletrajzi",
                    "translation": "autobiographical",
                    "pos": "adjective"
                },
                {
                    "lemma": "monumentális",
                    "translation": "monumental",
                    "pos": "adjective"
                },
                {
                    "lemma": "időérzékelés",
                    "translation": "perception of time",
                    "pos": "noun"
                },
                {
                    "lemma": "kiábrándultság",
                    "translation": "disillusionment",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "simultaneity-mihelyt",
                "title": "Instant Succession: mihelyt",
                "text1_title": "Strict Immediate Succession with mihelyt",
                "text1": "The subordinating conjunction mihelyt ('as soon as / the very instant / no sooner than') marks an uncompromisingly immediate sequence of events. It conveys a sharper sense of urgency or direct dependency than amint.",
                "text2_title": "Stylistic and Syntactic Distribution",
                "text2": "Mihelyt often links causal prerequisites to subsequent actions in narrative prose. Like amint, it governs subordinate clauses that set off immediate consequences in the main clause.",
                "table_title": "Instant Succession with mihelyt",
                "table_rows": [
                    [
                        "Mihelyt eleredt az eső a filmben, a falu lakói némán elindultak a sárban.",
                        "As soon as rain began to fall in the film, the village residents started out silently in the mud."
                    ],
                    [
                        "A néző elveszíti a szokásos időérzékét, mihelyt Tarr Béla lassú világa magába szippantja.",
                        "The viewer loses the usual sense of time as soon as Béla Tarr's slow world absorbs them."
                    ],
                    [
                        "Mihelyt Mészáros Márta bemutatta a Napló-filmeket, a cenzorok megrettentek az őszinteségétől.",
                        "No sooner had Márta Mészáros presented the Diary films than the censors were terrified by her honesty."
                    ],
                    [
                        "A valóság súlya azonnal érezhetővé válik, mihelyt a fekete-fehér képek megjelennek a vásznon.",
                        "The weight of reality becomes immediately palpable as soon as the black-and-white images appear on screen."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Mihelyt felcsendül a hipnotikus tangózene a kocsmában, a szereplők sorsa megpecsételődik.",
                        "english": "As soon as the hypnotic tango music rings out in the tavern, the fate of the characters is sealed."
                    },
                    {
                        "spanish": "A közönség megdöbbent, mihelyt szembesült az ötvenes évek elhallgatott valóságával.",
                        "english": "The audience was stunned as soon as they confronted the hushed-up reality of the nineteen-fifties."
                    },
                    {
                        "spanish": "Mihelyt véget ért a vetítés, a nézők percekig némán ültek a moziteremben.",
                        "english": "The instant the screening ended, the audience sat silently in the cinema hall for minutes."
                    }
                ],
                "tip": "Choose mihelyt when you want to emphasize that not a second was lost between the two actions: 'Mihelyt megkapta az engedélyt, elindult forgatni'."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen műfaji sajátosság jellemzi Mészáros Márta Napló-filmjeit?",
                    "options": [
                        "A saját gyermekkori és fiatalkori élményein alapuló, őszinte önéletrajzi történelmi dráma.",
                        "Könnyed zenés vígjáték a balatoni nyaralásokról.",
                        "Fantáziafilm a jövőbeli űrutazásokról."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Tarr Béla hétórás remekműve, a Sátántangó, a modern filmművészet egyik leginkább _____ alkotása. (monumental)",
                    "answer": "monumentális",
                    "english": "Béla Tarr's seven-hour masterpiece, Sátántangó, is one of modern cinema's most monumental works.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A néző teljesen elmerül a történetben, _____ felcsendül a film hipnotikus kísérőzenéje. (as soon as / no sooner than)",
                    "answer": "mihelyt",
                    "english": "The viewer becomes completely immersed in the story as soon as the film's hypnotic soundtrack rings out.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat alkalmazza helyesen a szigorú azonnali egymásutániságot a 'mihelyt' kötőszóval?",
                    "options": [
                        "Mihelyt befejeződött a forgatás, a rendező azonnal megkezdte az utómunkát.",
                        "Mihelyt befejeződött a forgatás, annál inkább megkezdte az utómunkát.",
                        "Mihelyt befejeződött a forgatás, amennyiben megkezdte az utómunkát."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Mihelyt",
                        "a",
                        "képek",
                        "megjelentek",
                        "a",
                        "vásznon,",
                        "a",
                        "teremben",
                        "teljes",
                        "csönd",
                        "lett."
                    ],
                    "solution": [
                        "Mihelyt",
                        "a",
                        "képek",
                        "megjelentek",
                        "a",
                        "vásznon,",
                        "a",
                        "teremben",
                        "teljes",
                        "csönd",
                        "lett."
                    ],
                    "english": "As soon as the images appeared on the screen, total silence fell in the hall.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan kezeli Tarr Béla az időt filmjeiben (például a Sátántangóban)?",
                    "options": [
                        "Rendkívül lassú, meditatív kameramozgásokkal az idő múlását szinte tapinthatóvá teszi a néző számára.",
                        "Videóklipszerű gyors vágásokkal sűríti az eseményeket.",
                        "Számítógépes animációkkal gyorsítja fel a szereplők mozgását."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "szigorú",
                        "fekete-fehér",
                        "film",
                        "hangulata",
                        "tökéletesen",
                        "tükrözte",
                        "a",
                        "korszak",
                        "kiábrándultságát."
                    ],
                    "solution": [
                        "A",
                        "szigorú",
                        "fekete-fehér",
                        "film",
                        "hangulata",
                        "tökéletesen",
                        "tükrözte",
                        "a",
                        "korszak",
                        "kiábrándultságát."
                    ],
                    "english": "The atmosphere of the austere black-and-white film perfectly reflected the disillusionment of the era.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing the audience's reaction to Márta Mészáros's honesty using 'mihelyt'.",
                            "answer": "A nemzetközi közönség mélyen megrendült, mihelyt szembesült Mészáros Márta filmjének kíméletlen őszinteségével."
                        },
                        {
                            "prompt": "State how the viewer is drawn into Béla Tarr's visual world using 'Mihelyt...'.",
                            "answer": "Mihelyt elindul a hipnotikus lassú kameramozgás, a néző elfelejti a hétköznapi valóságot."
                        }
                    ],
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                }
            ]
        },
        {
            "num": 5,
            "title": "Contemporary Revival: Saul fia and Testről és lélekről",
            "grammar_label": "Iterative recurrence and proportional simultaneity with valahányszor ('whenever / each time that')",
            "goals": [
                "I can evaluate contemporary Hungarian cinematic triumphs: László Nemes Jeles's Saul fia (2015 Oscar) and Ildikó Enyedi's Testről és lélekről (2017 Golden Bear).",
                "I can construct complex iterative temporal clauses using valahányszor.",
                "I can express nuanced film criticism and subjective emotional responses to modern cinematic masterpieces."
            ],
            "story_segment": {
                "seg_slug": "kortarsmagyarfilm",
                "title": "Új aranykor: Saul fia és Testről és lélekről",
                "summary": "In the 2010s, Hungarian cinema experienced a stunning resurgence: Saul fia reinvented Holocaust representation with claustrophobic shallow focus, while Testről és lélekről explored fragile intimacy through shared dreams of deer.",
                "location": "Cannes, Los Angeles, Berlin és Budapest",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A 2010-es években a magyar filmművészet valóságos új aranykort élt át. Hosszú évek bizonytalansága és forráshiánya után egy új rendezőgeneráció lépett színre, amely egyszerre tudott radikálisan újszerű formanyelvet teremteni és a világ legrangosabb fesztiváljainak fődíjait elhódítani."
                    },
                    {
                        "type": "narration",
                        "text": "Ennek a megújulásnak a legnagyobb nemzetközi diadalát Nemes Jeles László debütáló rendezése, a Saul fia hozta el 2015-ben. A film szakított a holokauszt-filmek hagyományos melodramatikus ábrázolásmódjával: a kamera szűk látószöggel, szinte végig a főszereplő, a sonderkommandós Saul Ausländer tarkójára és arcára tapadva követte a krematóriumok poklát. A háttér eseményei homályban maradtak, a hangkulissza fojtogató moraja azonban valósággal sokkolta a nézőket."
                    },
                    {
                        "type": "narration",
                        "text": "A Saul fia a cannes-i Nagydíj után 2016-ban elnyerte a legjobb idegen nyelvű filmnek járó Oscar-díjat is, megismételve Szabó István harmincnégy évvel korábbi sikerét. A kritikusok kiemelték, hogy valahányszor a kamera Saul tekintetére fókuszál, a film nem a pusztulást, hanem az emberi méltóság és a túlélő emberség utolsó szikráját ragadja meg."
                    },
                    {
                        "type": "narration",
                        "text": "Nem sokkal később, 2017-ben Enyedi Ildikó Testről és lélekről című lírai mesterműve elnyerte a Berlini Nemzetközi Filmfesztivál fődíját, az Arany Medvét. A film egy vágóhídi környezet rideg valóságát állította szembe a két magányos főszereplő közös álomvilágával, ahol szarvasokként találkoznak a havas erdőben. Valahányszor a szereplők közeledni próbálnak egymáshoz, a törékeny intimitás és az elidegenedés drámája bontakozik ki."
                    },
                    {
                        "type": "narration",
                        "text": "Ezek a sikerek bebizonyították, hogy a magyar film képes megőrizni egyedi szerzői hangját a globális filmpiacon is. Legyen szó a történelem legsötétebb traumáinak feldolgozásáról vagy a legfinomabb lélektani drámákról, a magyar rendezők munkái ma is a világ filmművészetének legértékesebb kincsei közé tartoznak."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "aranykor",
                    "translation": "golden age",
                    "pos": "noun"
                },
                {
                    "lemma": "valahányszor",
                    "translation": "whenever / each time that",
                    "pos": "conjunction"
                },
                {
                    "lemma": "szűk látószög",
                    "translation": "shallow focus / narrow field of view",
                    "pos": "noun"
                },
                {
                    "lemma": "lélektani dráma",
                    "translation": "psychological drama",
                    "pos": "noun"
                },
                {
                    "lemma": "nemzetközi elismerés",
                    "translation": "international acclaim",
                    "pos": "noun"
                },
                {
                    "lemma": "álomvilág",
                    "translation": "dream world",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "simultaneity-valahanyszor",
                "title": "Iterative Simultaneity: valahányszor",
                "text1_title": "Iterative and Recurrent Simultaneity",
                "text1": "The relative conjunction valahányszor ('whenever / each time that / every time that') establishes that every single repetition of an action in the subordinate clause triggers a simultaneous or directly resulting action in the main clause.",
                "text2_title": "Emphasizing Regularity and Inevitability",
                "text2": "In analytical and film criticism prose, valahányszor creates an impression of unbreakable aesthetic or psychological rules: 'Valahányszor a kamera Saul arcára fókuszál, a külvilág elmosódik'.",
                "table_title": "Iterative Recurrence with valahányszor",
                "table_rows": [
                    [
                        "Valahányszor a főszereplő elaludt, ugyanazzal a szarvassal álmodott a havas erdőben.",
                        "Whenever the protagonist fell asleep, she dreamed of the same deer in the snowy forest."
                    ],
                    [
                        "A néző összeszoruló szívvel figyeli a vásznat, valahányszor a háttérben felzúgnak a krematórium zajai.",
                        "The viewer watches the screen with a clutched heart whenever the noises of the crematorium roar up in the background."
                    ],
                    [
                        "Valahányszor új magyar film érkezett a fesztiválra, a zsűri elismeréssel fogadta.",
                        "Whenever a new Hungarian film arrived at the festival, the jury received it with acclaim."
                    ],
                    [
                        "A rendező újra megrendíti a közönséget, valahányszor az emberi méltóság kérdését vizsgálja.",
                        "The director moves the audience anew whenever he examines the question of human dignity."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "Valahányszor a kamera Saul tarkóját követi, a néző átéli a láger klausztrofób poklát.",
                        "english": "Whenever the camera follows the nape of Saul's neck, the viewer experiences the claustrophobic hell of the camp."
                    },
                    {
                        "spanish": "Enyedi Ildikó filmjében a rideg valóság megenyhül, valahányszor a két magányos lélek az álmokban találkozik.",
                        "english": "In Ildikó Enyedi's film, cold reality softens whenever the two lonely souls meet in dreams."
                    },
                    {
                        "spanish": "Valahányszor új nemzedék lép a színre, a magyar film megújítja kifejezőeszközeit.",
                        "english": "Whenever a new generation steps onto the stage, Hungarian cinema renews its expressive tools."
                    }
                ],
                "tip": "Use valahányszor when you want to formulate general rules, habits, or psychological patterns that repeat on every occasion."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Milyen operatőri megoldást alkalmazott a Saul fia a feszültség megteremtésére?",
                    "options": [
                        "Szűk látószöget, amely folyamatosan a főszereplő arcára és tarkójára tapad, homályban hagyva a hátteret.",
                        "Szélesvásznú helikopteres felvételeket a táborról.",
                        "Fekete-fehér rajzfilmes animációs betéteket."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Enyedi Ildikó Testről és lélekről című filmje rendkívüli _____ aratott, elnyerve a Berlini Arany Medvét. (international acclaim)",
                    "answer": "nemzetközi elismerést",
                    "english": "Ildikó Enyedi's film On Body and Soul achieved extraordinary international acclaim, winning the Berlin Golden Bear.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A néző mély megrendülést érez, _____ a film a halál árnyékában felvillanó emberséget ábrázolja. (whenever / each time)",
                    "answer": "valahányszor",
                    "english": "The viewer feels profound emotion whenever the film depicts humanity flashing up in the shadow of death.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat fejezi ki helyesen az ismétlődő egyidejűséget a 'valahányszor' kötőszóval?",
                    "options": [
                        "Valahányszor újra megnézem a filmet, mindig felfedezek benne egy új képi részletet.",
                        "Valahányszor újra megnézem a filmet, holott felfedezek egy új képi részletet.",
                        "Valahányszor újra megnézem a filmet, minél inkább felfedezek egy új részletet."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "Valahányszor",
                        "a",
                        "két",
                        "magányos",
                        "ember",
                        "találkozott,",
                        "ugyanarról",
                        "az",
                        "erdőről",
                        "álmodtak."
                    ],
                    "solution": [
                        "Valahányszor",
                        "a",
                        "két",
                        "magányos",
                        "ember",
                        "találkozott,",
                        "ugyanarról",
                        "az",
                        "erdőről",
                        "álmodtak."
                    ],
                    "english": "Whenever the two lonely people met, they dreamed about the same forest.",
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen rangos díjat nyert el a Saul fia 2016-ban?",
                    "options": [
                        "A legjobb idegen nyelvű filmnek járó Oscar-díjat.",
                        "A Velencei Nemzetközi Filmfesztivál Arany Oroszlán díját.",
                        "A Torontói Filmfesztivál Közönségdíját."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "két",
                        "főszereplő",
                        "közös",
                        "álomvilága",
                        "segített",
                        "feloldani",
                        "a",
                        "mindennapi",
                        "magányt."
                    ],
                    "solution": [
                        "A",
                        "két",
                        "főszereplő",
                        "közös",
                        "álomvilága",
                        "segített",
                        "feloldani",
                        "a",
                        "mindennapi",
                        "magányt."
                    ],
                    "english": "The two protagonists' shared dream world helped dissolve everyday loneliness.",
                    "teaches": [
                        "b2-magyarfilm-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing the recurring impact of Saul fia using 'valahányszor'.",
                            "answer": "Valahányszor a kamera a főszereplő arcát mutatja, a néző átéli a tábor klausztrofób borzalmát."
                        },
                        {
                            "prompt": "State that whenever a new Hungarian masterwork appears, world cinema celebrates using 'Valahányszor...'.",
                            "answer": "Valahányszor új magyar remekmű születik, a nemzetközi kritika elragadtatással méltatja az alkotókat."
                        }
                    ],
                    "teaches": [
                        "b2-simultaneity-conjunctions"
                    ]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can trace the history of Hungarian cinema from Hollywood founders to Jancsó, Szabó, Tarr, and Nemes Jeles.",
            "I can correctly use subordinating conjunctions of simultaneity and succession (miközben, mialatt, amint, mihelyt, valahányszor).",
            "I can analyze visual aesthetics, cinematic parables, and historical compromise in B2 Hungarian."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik kötőszó fejez ki szigorú, késlekedés nélküli azonnali egymásutániságot?",
                "options": [
                    "mihelyt",
                    "mialatt",
                    "miközben"
                ],
                "correct": 0,
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "question": "Melyik film hozta el Magyarország első Oscar-díját a legjobb idegen nyelvű film kategóriájában?",
                "options": [
                    "Szabó István: Mephisto",
                    "Jancsó Miklós: Szegénylegények",
                    "Tarr Béla: Sátántangó"
                ],
                "correct": 0,
                "teaches": [
                    "b2-magyarfilm-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik kötőszó fejez ki szabályosan ismétlődő időbeli egyidejűséget ('minden alkalommal, amikor')?",
                "options": [
                    "valahányszor",
                    "mialatt",
                    "amint"
                ],
                "correct": 0,
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A stúdióvezetők új szerződéseket kötöttek, _____ a rendezők az európai tapasztalataikat hasznosították. (while / at the same time)",
                "answer": "miközben",
                "english": "The studio heads signed new contracts while the directors utilized their European experience.",
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "sentence": "Jancsó Miklós filmjeiben a pusztai táj az elnyomó hatalom rideg _____ vált. (allegory)",
                "answer": "allegóriájává",
                "english": "In Miklós Jancsó's films, the steppe landscape became the cold allegory of oppressive power.",
                "teaches": [
                    "b2-magyarfilm-vocab"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A nézők felállva tapsoltak, _____ a gálán átadták az Oscar-díjat a magyar rendezőnek. (as soon as)",
                "answer": "amint",
                "english": "The spectators applauded standing as soon as the Oscar was handed to the Hungarian director at the gala.",
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "in-context",
                "tiles": [
                    "Mialatt",
                    "a",
                    "színészek",
                    "a",
                    "sárban",
                    "gyalogoltak,",
                    "a",
                    "kamera",
                    "percekig",
                    "nem",
                    "vágott."
                ],
                "solution": [
                    "Mialatt",
                    "a",
                    "színészek",
                    "a",
                    "sárban",
                    "gyalogoltak,",
                    "a",
                    "kamera",
                    "percekig",
                    "nem",
                    "vágott."
                ],
                "english": "While the actors walked in the mud, the camera did not cut for minutes.",
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "stage": "in-context",
                "tiles": [
                    "A",
                    "színész",
                    "nehéz",
                    "erkölcsi",
                    "kompromisszumot",
                    "kötött",
                    "a",
                    "karrierje",
                    "érdekében."
                ],
                "solution": [
                    "A",
                    "színész",
                    "nehéz",
                    "erkölcsi",
                    "kompromisszumot",
                    "kötött",
                    "a",
                    "karrierje",
                    "érdekében."
                ],
                "english": "The actor struck a difficult moral compromise for the sake of his career.",
                "teaches": [
                    "b2-magyarfilm-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "question": "Melyik mondatban fejezi ki a 'mihelyt' a késlekedés nélküli eseménybekövetkezést?",
                "options": [
                    "Mihelyt elcsendesedett a terem, felhangzott a főszereplő drámai monológja.",
                    "Amikor elcsendesedett a terem, jóllehet felhangzott a monológ.",
                    "Elcsendesedett a terem, holott felhangzott a monológ."
                ],
                "correct": 0,
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "tiles": [
                    "Valahányszor",
                    "új",
                    "filmet",
                    "mutattak",
                    "be,",
                    "a",
                    "kritikusok",
                    "elragadtatással",
                    "írtak",
                    "róla."
                ],
                "solution": [
                    "Valahányszor",
                    "új",
                    "filmet",
                    "mutattak",
                    "be,",
                    "a",
                    "kritikusok",
                    "elragadtatással",
                    "írtak",
                    "róla."
                ],
                "english": "Whenever a new film was screened, the critics wrote about it with delight.",
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Synthesize Jancsó's and Szabó's achievements using 'miközben' and 'amint'.",
                        "answer": "Jancsó a hatalom koreográfiáját kutatta, miközben Szabó István remekműve világhírű lett, amint elnyerte az Oscar-díjat."
                    }
                ],
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Describe the emotional impact of contemporary Hungarian cinema using 'valahányszor' and 'mihelyt'.",
                        "answer": "Mihelyt elkezdődik a vetítés, a néző elnémul, valahányszor a magyar alkotók az emberi lélek mélyére pillantanak."
                    }
                ],
                "teaches": [
                    "b2-simultaneity-conjunctions"
                ]
            }
        ]
    }
}


UNIT_15_SZAMIZDAT = {
    "unit_num": 15,
    "slug": "szamizdat",
    "title": "The Three Ts: Censorship, Aczél's Cultural Policy & Samizdat",
    "grammar_skill": "b2-agent-backgrounding",
    "vocab_skill": "b2-szamizdat-vocab",
    "theme": "Aczél's Three Ts cultural policy, censorship and Samizdat underground",
    "location": "Budapest (Kulturális Minisztérium, illegális nyomdák és szamizdat lakások)",
    "intro_body": [
        "Under the Kádár regime following the crushed 1956 revolution, Hungary developed a uniquely insidious form of cultural control. Steered by cultural commissar György Aczél, the state replaced crude Stalinist terror with the subtle policy of the 'Three Ts': Támogatott (Supported), Tűrt (Tolerated), and Tiltott (Prohibited). Instead of rigid rules, ambiguity reigned, prompting artists to internalize self-censorship or invent elaborate allegorical codes.",
        "In this unit, you will explore the secret bargains between censors and creators, decode the 'flower language' (virágnyelv) of Hungarian theatre and literature, visit clandestine stencil printshops in private apartments, and examine how the underground samizdat journal Beszélő prepared the ground for democratic transition. Grammatically, you will master Hungarian agent-backgrounding and impersonal structures (institutional 3rd plural, -ra/-re kerül, evaluative predicates, and middle-voice verbs)."
    ],
    "combined_story_title": "Támogatott, tűrt, tiltott: Kultúra a sorok között",
    "combined_story_summary": "How cultural life operated under György Aczél's 'Three Ts' (Supported, Tolerated, Prohibited) during the Kádár era, how artists mastered coded allegory, and how the underground Samizdat press paved the way for 1989.",
    "lessons": [
        {
            "num": 1,
            "title": "How the 'Three Ts' System Worked",
            "grammar_label": "Institutional classification with impersonal active 3rd plural (kategóriába sorolják / tekintik)",
            "goals": [
                "I can explain the architecture of György Aczél's 'Three Ts' (támogatott, tűrt, tiltott) cultural policy in Kádár-era Hungary.",
                "I can use agentless 3rd person plural active verbs to describe institutional classification and societal norms.",
                "I can discuss state censorship, cultural subsidies, and ideological boundaries in fluent B2 Hungarian."
            ],
            "story_segment": {
                "seg_slug": "haromt",
                "title": "A három T: Támogatott, tűrt, tiltott",
                "summary": "Rather than overt, brutal Stalinist bans, cultural czar György Aczél divided art into three fluid categories: Supported, Tolerated, and Prohibited, keeping artists in constant self-censoring uncertainty.",
                "location": "Budapest, Szalay utca (Kulturális Minisztérium)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1956-os forradalom leverése után a Kádár-rendszer hamar felismerte, hogy a sztálini típusú nyers erőszak és a direkt terror hosszú távon képtelen biztosítani a társadalmi békét. A hatalomnak szüksége volt az értelmiség lojalitására vagy legalábbis a csendes semlegességére. Ezt a célt szolgálta a korszak teljhatalmú kultúrpápája, Aczél György által kidolgozott kultúrpolitika, amely a híres „három T” — támogatott, tűrt, tiltott — rendszerére épült."
                    },
                    {
                        "type": "narration",
                        "text": "A rendszer lényege a határok szándékos elmosása volt. A támogatott kategóriába sorolták a szocialista realizmust dicsérő, politikailag megbízható műveket, amelyek hatalmas állami támogatást, papírkvótát és díjakat kaptak. A tiltott kategóriába kerültek a nyíltan antikommunista, 1956-ot forradalomnak nevező vagy a szovjet megszállást bíráló írások — ezek szerzőit elhallgatták, megfigyelték vagy emigrációba kényszerítették."
                    },
                    {
                        "type": "narration",
                        "text": "A legszélesebb és leginkább kényes zónát azonban a tűrt kategória jelentette. Ide sorolták a polgári írók műveit, a modernista kísérleteket és a szórakoztató műfajok többségét. Ezek a művek megjelenhettek ugyan, de korlátozott példányszámban, szigorú szerkesztőségi szűrőkön keresztül, és a szerzők soha nem lehettek biztosak abban, hogy a következő munkájukat nem nyilvánítják-e hirtelen tiltottnak."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a lebegtetett bizonytalanság a leghatékonyabb eszközzé tette az öncenzúrát. Az alkotók maguk kezdték kihúzni a kényes mondatokat a kézirataikból, mielőtt a szerkesztők vagy a minisztérium egyáltalán elolvasta volna azokat. Mindenki pontosan tudta, hogy hol húzódnak a kimondhatóság határai, még akkor is, ha ezeket a szabályokat soha nem foglalták törvénybe."
                    },
                    {
                        "type": "narration",
                        "text": "Aczél rendszere a látszólagos szabadság illúzióját keltette, miközben a kultúra minden szegmensét kézben tartotta. A magyar értelmiség a legvidámabb barakkban élt, de a barakk rácsai ettől még valóságosak maradtak."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "kultúrpolitika",
                    "translation": "cultural policy",
                    "pos": "noun"
                },
                {
                    "lemma": "öncenzúra",
                    "translation": "self-censorship",
                    "pos": "noun"
                },
                {
                    "lemma": "kategóriába sorol",
                    "translation": "classify into a category",
                    "pos": "verb"
                },
                {
                    "lemma": "támogatott",
                    "translation": "supported / subsidized",
                    "pos": "adjective"
                },
                {
                    "lemma": "tűrt",
                    "translation": "tolerated",
                    "pos": "adjective"
                },
                {
                    "lemma": "tiltott",
                    "translation": "prohibited / banned",
                    "pos": "adjective"
                }
            ],
            "grammar_doc": {
                "slug": "agent-backgrounding-institutional-3pl",
                "title": "Agent Backgrounding: Impersonal 3rd Plural",
                "text1_title": "Institutional and Systemic 3rd Person Plural",
                "text1": "In Hungarian, when an action is carried out by an administrative institution, state apparatus, or unnamed collective body, standard usage employs the 3rd person plural active verb WITHOUT an overt subject pronoun (ők): 'A művet a tűrt kategóriába sorolják' (They classify the work into the tolerated category = The work is classified as tolerated).",
                "text2_title": "Avoiding Artificial Passives",
                "text2": "Unlike English, which uses passive voice ('The book is considered dangerous'), natural Hungarian avoids the rare morphological passive (-atik/-etik) and instead uses this impersonal 3rd plural: 'Veszélyesnek tartják a kiadványt'. This focuses attention on the object while conveying bureaucratic power.",
                "table_title": "Institutional 3rd Plural Constructions",
                "table_rows": [
                    [
                        "A rendszerellenes írásokat azonnal a tiltott kategóriába sorolják.",
                        "Anti-regime writings are immediately classified into the prohibited category."
                    ],
                    [
                        "A hivatalos lapokban szigorúan ellenőrzik a megjelenő szövegeket.",
                        "In official papers, published texts are strictly inspected."
                    ],
                    [
                        "Megbízhatatlannak tartják azokat, akik nem hajlandók öncenzúrát gyakorolni.",
                        "Those who are unwilling to practice self-censorship are deemed untrustworthy."
                    ],
                    [
                        "A támogatott szerzőknek jelentős anyagi juttatásokat és állami díjakat biztosítanak.",
                        "Significant financial stipends and state awards are provided for supported authors."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A minisztériumban eldöntik, melyik regény kaphat állami papírkvótát a kiadáshoz.",
                        "english": "In the ministry they decide which novel can receive state paper quota for publication."
                    },
                    {
                        "spanish": "A kéziratot évekig asztalfiókban tartják, mielőtt engedélyezik a megjelenését.",
                        "english": "The manuscript is kept in a desk drawer for years before its publication is authorized."
                    },
                    {
                        "spanish": "Nem tiltják be nyíltan a darabot, de a próbákat folyamatosan akadályozzák.",
                        "english": "They do not ban the play openly, but rehearsals are continuously hindered."
                    }
                ],
                "tip": "Do not try to translate English passive 'is considered' as '*van tekintve'. Use 'tekintik' or 'tartják' in the active 3rd plural."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'öncenzúra' fogalma a kádári korszak művészeti életében?",
                    "options": [
                        "Azt a folyamatot, amikor az alkotó a retorzióktól félve maga törli a rendszerkritikus gondolatokat a művéből.",
                        "A könyvek nyomtatás előtti helyesírási ellenőrzését.",
                        "A külföldi utazási engedélyek hivatalos jóváhagyását."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "Aczél György _____ a szocialista realizmust részesítette előnyben a modern kísérletekkel szemben. (cultural policy)",
                    "answer": "kultúrpolitikája",
                    "english": "György Aczél's cultural policy favored socialist realism over modern experiments.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A vitatott kéziratokat a pártbizottságban a veszélyesnek ítélt kategóriába _____ a bírálók. (classify / 3rd plural)",
                    "answer": "sorolják",
                    "english": "The disputed manuscripts are classified into the category deemed dangerous in the party committee by the reviewers.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Hogyan fejezzük ki természetes magyar mondatszerkezettel az intézményi cselekvést a passzív helyett?",
                    "options": [
                        "A forradalmat dicsőítő verseket szigorúan tiltják a hivatalos sajtóban.",
                        "A versek szigorúan tiltva vannak a hivatalos sajtóban.",
                        "A versek a cenzúra által betiltásra jutnak a hivatalos sajtóban."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "megbízhatatlan",
                        "szerzőket",
                        "gyakran",
                        "a",
                        "tűrt",
                        "kategóriába",
                        "sorolják",
                        "a",
                        "hivatalban."
                    ],
                    "solution": [
                        "A",
                        "megbízhatatlan",
                        "szerzőket",
                        "gyakran",
                        "a",
                        "tűrt",
                        "kategóriába",
                        "sorolják",
                        "a",
                        "hivatalban."
                    ],
                    "english": "Untrustworthy authors are often classified into the tolerated category in the office.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Melyik három fogalomra épült Aczél György kultúrpolitikája?",
                    "options": [
                        "Támogatott, tűrt, tiltott.",
                        "Tudományos, társadalmi, történelmi.",
                        "Törvényes, titkos, tiltakozó."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "támogatott",
                        "és",
                        "a",
                        "tiltott",
                        "művek",
                        "között",
                        "a",
                        "tűrt",
                        "kategória",
                        "húzódott."
                    ],
                    "solution": [
                        "A",
                        "támogatott",
                        "és",
                        "a",
                        "tiltott",
                        "művek",
                        "között",
                        "a",
                        "tűrt",
                        "kategória",
                        "húzódott."
                    ],
                    "english": "Between supported and prohibited works stretched the tolerated category.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence explaining how authorities categorized literature using 3rd plural impersonal verbs.",
                            "answer": "A hivatalos szervek a politikai lojalitás alapján sorolják a szerzőket a támogatott vagy a tűrt kategóriába."
                        },
                        {
                            "prompt": "State that uncensored thought was considered dangerous using 'tekintik'.",
                            "answer": "A cenzúrázatlan és önálló gondolatokat a pártállamban rendszert veszélyeztető elemnek tekintik."
                        }
                    ],
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                }
            ]
        },
        {
            "num": 2,
            "title": "Bargaining Between Artists and Censors",
            "grammar_label": "Formal periphrastic state transition: verbal noun in -ra/-re + kerül (betiltásra kerül)",
            "goals": [
                "I can analyze the personal negotiations between cultural czar György Aczél and prominent intellectuals (Déry, Illyés, Jancsó).",
                "I can use the high-register construction verbal noun + -ra/-re + kerül to express events without naming the agent.",
                "I can discuss compromise, publishing permits, and behind-the-scenes political deals in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "alkudozas",
                "title": "Alku a cenzorral: A kompromisszum művészete",
                "summary": "Aczél personally phoned directors, editors, and poets, offering travel passports and publication in exchange for removing delicate paragraphs or toning down historical critiques.",
                "location": "Budapest, miniszteri dolgozószoba",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Aczél György hatalomgyakorlásának legkülönlegesebb vonása a személyes kapcsolatok ápolása volt. Nem arctalan bürokrataként irányított a minisztériumból, hanem maga hívta fel telefonon a korszak legjelesebb íróit, költőit és filmrendezőit. Illyés Gyula, Déry Tibor vagy Jancsó Miklós rendszeresen megfordult a dolgozószobájában, ahol egy kávé mellett órákon át vitatkoztak a megjelenésre váró művekről."
                    },
                    {
                        "type": "narration",
                        "text": "Ezek a találkozók a látszat ellenére kőkemény alkuk voltak. Aczél nem parancsolt nyersen: javaslatokat tett, aggodalmait fejezte ki a „baráti országok” esetleges felháborodása miatt, és kompromisszumot ajánlott. Ha a szerző hajlandó volt kihúzni két vitatott bekezdést vagy megváltoztatni a befejezést, a könyv azonnal kiadásra került, és a szerző megkapta a régóta várt nyugati útlevelet is."
                    },
                    {
                        "type": "narration",
                        "text": "Amennyiben egy alkotó megtagadta az együttműködést, nem börtön várt rá, hanem a lassú elszigetelés. A kész kézirat fiókban maradt, az előadás betiltásra került, és a szerző útlevélkérelme hosszú évekre elutasításra lelt. Ez a finomra hangolt zsarolási technika sokkal hatékonyabbnak bizonyult a nyílt megtorlásnál, hiszen magukra a művészekre hárította a döntés felelősségét."
                    },
                    {
                        "type": "narration",
                        "text": "Sokan úgy érezték, hogy az alkuk révén legalább a lényeget megmenthetik és eljuttathatják az olvasókhoz. Mások viszont az erkölcsi integritás elvesztését látták ebben: a hatalom baráti mosolya mögött a cenzúra pókhálója húzódott meg, amely lassan mindenkit foglyul ejtett."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a kettős játék határozta meg a kádári évtizedek szellemi életét: az állandó egyensúlyozás az alkotói kompromisszum és az önfeladás, a megjelenési engedély és az elvek megtartása között."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "kompromisszum",
                    "translation": "compromise",
                    "pos": "noun"
                },
                {
                    "lemma": "megjelenési engedély",
                    "translation": "publication permit",
                    "pos": "noun"
                },
                {
                    "lemma": "betiltásra kerül",
                    "translation": "comes to be banned / is banned",
                    "pos": "expression"
                },
                {
                    "lemma": "útlevélkérelem",
                    "translation": "passport application",
                    "pos": "noun"
                },
                {
                    "lemma": "szerkesztőségi alku",
                    "translation": "editorial bargain",
                    "pos": "noun"
                },
                {
                    "lemma": "diplomáciai érzék",
                    "translation": "diplomatic tact",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "agent-backgrounding-verbnoun-kerul",
                "title": "Agent Backgrounding: Verbal Noun + -ra/-re kerül",
                "text1_title": "Periphrastic Event State with -ra/-re kerül",
                "text1": "In formal, administrative, and journalistic Hungarian, events and institutional decisions are frequently expressed using a verbal noun (ending in -ás/-és) in the sublative case (-ra/-re) combined with the verb kerül: 'A könyv betiltásra került' (The book came to be banned / was banned).",
                "text2_title": "Displacing the Human Agent",
                "text2": "This structure backgrounds or completely omits the agent of the decision, presenting the outcome as a bureaucratic event or established fact: 'A cikk közlésre kerül' (The article will be published), 'Az útlevélkérelem elutasításra került' (The passport application was rejected).",
                "table_title": "Formal Event Predications with -ra/-re kerül",
                "table_rows": [
                    [
                        "A vitatott fejezet törlésre került a kéziratból a nyomdába adás előtt.",
                        "The disputed chapter came to be deleted from the manuscript before being sent to press."
                    ],
                    [
                        "A színházi előadás bemutatásra kerülhet, amennyiben a rendező elfogadja a módosításokat.",
                        "The theatrical production can come to be presented provided that the director accepts the modifications."
                    ],
                    [
                        "Több száz példány elkobzásra került a határon a vámosok által.",
                        "Several hundred copies came to be confiscated at the border by customs officials."
                    ],
                    [
                        "A szerző kérése felülvizsgálatra kerül a kulturális bizottság ülésén.",
                        "The author's request will come under review at the meeting of the cultural committee."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A kézirat alapos átdolgozásra került, miután a cenzor kifogásolta a politikai áthallásokat.",
                        "english": "The manuscript came to be thoroughly revised after the censor objected to the political allusions."
                    },
                    {
                        "spanish": "Az író útlevélkérelme jóváhagyásra került a minisztériumban kötött kompromisszum után.",
                        "english": "The writer's passport application came to be approved after the compromise struck in the ministry."
                    },
                    {
                        "spanish": "Egyetlen kritikus hangvételű kötet sem kerülhetett kiadásra hivatalos jóváhagyás nélkül.",
                        "english": "Not a single volume of critical tone could come to be published without official authorization."
                    }
                ],
                "tip": "Use [verbal noun]-ra/-re kerül when reporting administrative outcomes in formal essays. While purists sometimes caution against overusing it, in historical and political register it is omnipresent."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a 'megjelenési engedély' a cenzúra működésében?",
                    "options": [
                        "A minisztérium vagy a kiadói főigazgatóság hivatalos jóváhagyását egy könyv kinyomtatására és terjesztésére.",
                        "A színházi belépőjegyek kedvezményes vásárlási utalványát.",
                        "A szerzői jogdíjak bankszámlára történő átutalásának igazolását."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A művész kénytelen volt nehéz _____ kötni a hatalommal, ha publikálni akarta műveit. (compromise)",
                    "answer": "kompromisszumot",
                    "english": "The artist was forced to strike a difficult compromise with power if he wanted to publish his works.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A dráma a cenzori kifogások miatt végül betiltásra _____, és nem mutathatták be a színházban. (came to be / was)",
                    "answer": "került",
                    "english": "Due to censorial objections the drama finally came to be banned, and could not be presented in the theatre.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat alkalmazza a hivatalos cselekvőháttérbe szorító '-ra/-re kerül' szerkezetet?",
                    "options": [
                        "A kézirat alapos felülvizsgálatra került a kiadás engedélyezése előtt.",
                        "A kéziratot felülvizsgálták, amennyiben kiadásra jutott.",
                        "A kézirat felülvizsgálódott minél hamarabb."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "vitatott",
                        "fejezet",
                        "törlésre",
                        "került",
                        "a",
                        "kéziratból",
                        "a",
                        "nyomtatás",
                        "előtt."
                    ],
                    "solution": [
                        "A",
                        "vitatott",
                        "fejezet",
                        "törlésre",
                        "került",
                        "a",
                        "kéziratból",
                        "a",
                        "nyomtatás",
                        "előtt."
                    ],
                    "english": "The disputed chapter came to be deleted from the manuscript before printing.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen módszerrel érte el Aczél György az írók kompromisszumkészségét?",
                    "options": [
                        "Személyes beszélgetésekkel, zsarolással, valamint útlevelek és megjelenések ígéretével.",
                        "Rendőrségi börtönbüntetésekkel és kényszermunkával.",
                        "Kizárólag névtelen hivatalos levelek küldésével."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "szerző",
                        "útlevélkérelem",
                        "benyújtásával",
                        "próbált",
                        "eljutni",
                        "a",
                        "nyugati",
                        "konferenciára."
                    ],
                    "solution": [
                        "A",
                        "szerző",
                        "útlevélkérelem",
                        "benyújtásával",
                        "próbált",
                        "eljutni",
                        "a",
                        "nyugati",
                        "konferenciára."
                    ],
                    "english": "The author tried to reach the Western conference by submitting a passport application.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence reporting that a book was published after concessions using 'kiadásra került'.",
                            "answer": "A módosítások elfogadása után a vitatott regény végül kiadásra került a kiadónál."
                        },
                        {
                            "prompt": "Report that an application was rejected by the ministry using 'elutasításra került'.",
                            "answer": "A rendszerkritikus író külföldi útlevélkérelme indoklás nélkül elutasításra került a hivatalban."
                        }
                    ],
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                }
            ]
        },
        {
            "num": 3,
            "title": "Allegory as a Language of Truth",
            "grammar_label": "Impersonal modal and evaluative predicates (elkerülhetetlennek tartják, vitathatatlannak tűnik)",
            "goals": [
                "I can explain how authors and audiences learned 'flower language' (virágnyelv) and Aesopian allegory to discuss taboo topics like 1956 or Soviet occupation.",
                "I can deploy impersonal evaluative framing predicates with -nak/-nek.",
                "I can decode historical metaphors and subtextual messages in Hungarian literature and theatre."
            ],
            "story_segment": {
                "seg_slug": "viragnyelv",
                "title": "A virágnyelv: Igazság a sorok között",
                "summary": "When speaking directly of the 1956 revolution or Soviet presence was strictly forbidden, writers disguised modern Hungarian history as Ottoman-era struggles or medieval allegories.",
                "location": "Budapesti színházak és folyóiratok",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Amikor a valóságról nyíltan nem lehetett beszélni, a magyar művészet kifejlesztette a sorok közötti olvasás és írás virtuóz mesterségét: a virágnyelvet. Az ezópuszi beszédmód lényege az volt, hogy a művek felszínen ártalmatlan történelmi vagy mitológiai témákat dolgoztak fel, a beavatott közönség számára azonban minden egyes mondat a jelenkorról szólt."
                    },
                    {
                        "type": "narration",
                        "text": "A legnagyobb tabutémát a szovjet katonai megszállás és az 1956-os forradalom emléke jelentette. A szovjet szót ki sem lehetett ejteni, ám a drámaírók és regényírók felfedezték a török hódoltság korát. Amikor a színpadon a tizenhatodik századi Habsburg- vagy oszmán önkényről, az idegen helyőrségekről és a megalkuvó főurakról beszéltek, a nézőtér feszülten elnémult: mindenki pontosan tudta, hogy a jelenkori elnyomásról van szó."
                    },
                    {
                        "type": "narration",
                        "text": "A színházi előadásokon a politikai áthallások valóságos villámcsapásként érték a közönséget. Egy-egy hangsúly, egy ironikus gesztus vagy egy váratlan csend elegendő volt ahhoz, hogy a nézőtéren tapsvihar törjön ki. A színészek és a nézők között cinkos szövetség jött létre: a cenzor hiába ült a páholyban, a szavak rejtett értelmét képtelen volt letartóztatni."
                    },
                    {
                        "type": "narration",
                        "text": "A virágnyelv használatát a korabeli értelmiség elengedhetetlennek tartotta a szellemi túléléshez. Bár a direkt politikai ellenállás kockázata túl nagy volt, a metaforák és parabolák révén a nemzet kollektív emlékezete nem szakadt meg: az igazság a sorok között élt tovább."
                    },
                    {
                        "type": "narration",
                        "text": "Ez a kettős olvasat különleges érzékenységet tanított a magyar közönségnek. A mai napig jellemző a hazai kultúrafogyasztókra, hogy a legártatlanabb történetek mögött is a rejtett politikai üzeneteket és áthallásokat keresik."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "virágnyelv",
                    "translation": "coded / Aesopian language ('flower language')",
                    "pos": "noun"
                },
                {
                    "lemma": "áthallás",
                    "translation": "allusion / double entendre / resonance",
                    "pos": "noun"
                },
                {
                    "lemma": "tabutéma",
                    "translation": "taboo subject",
                    "pos": "noun"
                },
                {
                    "lemma": "sorok között olvas",
                    "translation": "read between the lines",
                    "pos": "expression"
                },
                {
                    "lemma": "történelmi parabola",
                    "translation": "historical parable",
                    "pos": "noun"
                },
                {
                    "lemma": "cenzúrázatlan",
                    "translation": "uncensored",
                    "pos": "adjective"
                }
            ],
            "grammar_doc": {
                "slug": "agent-backgrounding-evaluative-predicates",
                "title": "Agent Backgrounding: Impersonal Evaluative Predicates",
                "text1_title": "Evaluative Predicates with -nak/-nek",
                "text1": "Formal Hungarian expresses widespread consensus and objective assessments by attaching the dative/essive suffix -nak/-nek to evaluative adjectives combined with tart ('consider'), tekint ('regard'), tűnik ('seem'), or mutatkozik ('prove to be'): 'Elkerülhetetlennek tartják a kompromisszumot' (Compromise is considered unavoidable).",
                "text2_title": "Stance without Subject",
                "text2": "These predicates allow authors to express analytical judgements with authoritative neutrality, without attributing the view to a specific person: 'Nyilvánvalónak tűnik, hogy a darab 1956-ra utalt' (It seems obvious that the play referred to 1956).",
                "table_title": "Evaluative Impersonal Framing",
                "table_rows": [
                    [
                        "A virágnyelv használatát elengedhetetlennek tartották a színházi világban.",
                        "The use of Aesopian language was considered indispensable in the theatre world."
                    ],
                    [
                        "Vitathatatlannak tűnik, hogy a történelmi drámák a jelenről szóltak.",
                        "It seems indisputable that the historical dramas were about the present."
                    ],
                    [
                        "A közvetlen politikai bírálatot túlságosan kockázatosnak tekintették.",
                        "Direct political criticism was regarded as overly risky."
                    ],
                    [
                        "A sorok közötti olvasás képessége alapvető fontosságúnak bizonyult.",
                        "The ability to read between the lines proved to be of fundamental importance."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A szovjet megszállást tabutémának tekintették, ezért a darabokban török hódítókról beszéltek.",
                        "english": "Soviet occupation was regarded as a taboo topic, which is why in plays they spoke of Turkish conquerors."
                    },
                    {
                        "spanish": "A nézők reakciója alapján egyértelműnek tűnt, hogy mindenki értette a politikai áthallásokat.",
                        "english": "Based on the viewers' reaction it seemed unmistakable that everyone understood the political allusions."
                    },
                    {
                        "spanish": "A cenzúra kijátszását a művészi szuverenitás próbájának tartották.",
                        "english": "Outwitting censorship was considered a test of artistic sovereignty."
                    }
                ],
                "tip": "Construct evaluative impersonal frames by pairing an adjective with -nak/-nek plus tartják / tekintik: 'Szükségesnek tartják az önállóságot' (Independence is considered necessary)."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az 'áthallás' kifejezés a színházi előadások kapcsán?",
                    "options": [
                        "Olyan kétértelmű mondatot vagy gesztust, amely a történelmi téma mögött a jelenkori politikai valóságra utal.",
                        "A színpadi hangosító mikrofonok technikai hibájából adódó sípolást.",
                        "A szomszédos színháztermekből átszűrődő zenei zajt."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A szovjet megszállás és az 1956-os forradalom szigorúan őrzött _____ volt a szocializmusban. (taboo subject)",
                    "answer": "tabutéma",
                    "english": "Soviet occupation and the 1956 revolution were strictly guarded taboo subjects in socialism.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A történelmi allegóriák alkalmazását elengedhetetlennek _____ a cenzúra kikerülésére. (consider / 3rd plural)",
                    "answer": "tartották",
                    "english": "The application of historical allegories was considered indispensable for bypassing censorship.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondat alkalmaz személytelen értékelő szerkezetet dative '-nak/-nek' raggal?",
                    "options": [
                        "A nézők tapsa alapján nyilvánvalónak tűnt a darab politikai üzenete.",
                        "A nézők tapsa alapján nyilvánvalóan tűnt a darab üzenete.",
                        "A nézők tapsa alapján nyilvánvaló volt hogy tűnt a darab."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "közvetlen",
                        "ellenállást",
                        "túlságosan",
                        "kockázatosnak",
                        "tartották",
                        "a",
                        "terror",
                        "éveiben."
                    ],
                    "solution": [
                        "A",
                        "közvetlen",
                        "ellenállást",
                        "túlságosan",
                        "kockázatosnak",
                        "tartották",
                        "a",
                        "terror",
                        "éveiben."
                    ],
                    "english": "Direct resistance was considered overly risky during the years of terror.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan beszélt a virágnyelv a tiltott témákról a szocialista korszakban?",
                    "options": [
                        "Történelmi parabolák, például a török hódoltság ábrázolása révén utalt a jelenkori elnyomásra.",
                        "Kizárólag latin és görög nyelven írt tudományos értekezésekben.",
                        "Néma pantomimjátékokkal fejezte ki a tiltakozást."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "tapasztalt",
                        "közönség",
                        "megtanult",
                        "a",
                        "sorok",
                        "között",
                        "olvasni",
                        "a",
                        "színházban."
                    ],
                    "solution": [
                        "A",
                        "tapasztalt",
                        "közönség",
                        "megtanult",
                        "a",
                        "sorok",
                        "között",
                        "olvasni",
                        "a",
                        "színházban."
                    ],
                    "english": "The experienced audience learned to read between the lines in the theatre.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence stating that using Aesopian language was considered necessary using 'szükségesnek tartották'.",
                            "answer": "A virágnyelv használatát szükségesnek tartották ahhoz, hogy a cenzorok ne tilthassák be a darabot."
                        },
                        {
                            "prompt": "State that it seems indisputable that everyone understood the historical parables using 'vitathatatlannak tűnik'.",
                            "answer": "Vitathatatlannak tűnik, hogy a budapesti közönség minden politikai áthallást pontosan megértett."
                        }
                    ],
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                }
            ]
        },
        {
            "num": 4,
            "title": "Stencils in the Kitchen: The Samizdat Underground",
            "grammar_label": "Passive-avoidance with reflexive and middle-voice verbs (-ódik/-ődik, terjed, alakul)",
            "goals": [
                "I can describe how the underground samizdat movement produced clandestine books and periodicals using ramshackle stencil duplicators (ramka) in private apartments.",
                "I can use reflexive and intransitive middle verbs (-ódik/-ődik) to express actions happening organically without human subjects.",
                "I can discuss illegal printing, police house searches, and underground distribution networks in Hungarian."
            ],
            "story_segment": {
                "seg_slug": "szamizdatnyomda",
                "title": "Stencilek a konyhában: Az illegális nyomdák világa",
                "summary": "In small Budapest apartments, dissidents like Gábor Demszky and Jenő Nagy operated manual 'ramka' stencil duplicators by night, producing thousands of uncensored books smelling of crude ink.",
                "location": "Budapesti bérlakások (1980-as évek)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Az 1970-es évek végére a magyar demokratikus ellenzék megelégelte az aczéli kompromisszumokat és a virágnyelv korlátait. Rájöttek, hogy az igazi szabadság csak akkor valósulhat meg, ha megtörik az állami információmonopóliumot. Így született meg a magyar szamizdat: a cenzúrázatlan, kézzel és házi gépekkel sokszorosított illegális irodalom."
                    },
                    {
                        "type": "narration",
                        "text": "A mozgalom központjai egyszerű pesti bérlakások és vidéki présházak voltak. Mivel a hivatalos fénymásolókhoz szigorú állami engedély kellett, az ellenzékiek lengyel mintára fából készült kézi szitanyomó kereteket — úgynevezett ramkákat — és egyszerű stencileket használtak. A fürdőszobákban és konyhákban éjszakákon át folyt a munka: a festékszag elárasztotta a lakást, miközben lapról lapra sokszorosítódtak a tiltott írások."
                    },
                    {
                        "type": "narration",
                        "text": "Demszky Gábor és Nagy Jenő megalapították az AB Független Kiadót, amely nemcsak folyóiratokat, hanem teljes könyveket adott ki: George Orwell 1984-ét, Arthur Koestler Sötétség délben című regényét és az 1956-os megtorlások titkos dokumentumait. A kötetek puha kötésben, gyakran halvány és maszatos betűkkel jelentek meg, az olvasók számára mégis felbecsülhetetlen kincset jelentettek."
                    },
                    {
                        "type": "narration",
                        "text": "A titkosrendőrség folyamatosan vadászott a nyomdákra. Rendszeresek voltak a házkutatások, az illegális kiadványok és nyomdagépek elkobzása, a kihallgatások és a pénzbírságok. Ennek ellenére a szamizdathálózat nem szűnt meg, sőt egyre szervezettebbé vált: a könyvek kézről kézre adva terjedtek az egyetemisták, tanárok és orvosok között."
                    },
                    {
                        "type": "narration",
                        "text": "A szamizdat nemcsak könyveket terjesztett, hanem a félelemmentes cselekvés kultúráját honosította meg. Bebizonyította, hogy a totalitárius hatalom hazugságai ellen a legegyszerűbb nyomdafesték is ellenállhatatlan fegyverré válhat."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "szamizdat",
                    "translation": "samizdat / underground publication",
                    "pos": "noun"
                },
                {
                    "lemma": "stencilgép",
                    "translation": "stencil duplicating machine / mimeograph",
                    "pos": "noun"
                },
                {
                    "lemma": "sokszorosítódik",
                    "translation": "is duplicated / multiplies",
                    "pos": "verb"
                },
                {
                    "lemma": "házkutatás",
                    "translation": "house search / police raid",
                    "pos": "noun"
                },
                {
                    "lemma": "elkobzás",
                    "translation": "confiscation / seizure",
                    "pos": "noun"
                },
                {
                    "lemma": "titkosrendőrség",
                    "translation": "secret police",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "agent-backgrounding-middle-verbs",
                "title": "Passive-Avoidance: Reflexive and Middle Verbs",
                "text1_title": "Spontaneous and Agentless Action with -ódik/-ődik",
                "text1": "Hungarian regularly derives middle-voice and reflexive intransitive verbs from transitive stems using the suffixes -ódik / -ődik. These verbs portray an event as unfolding spontaneously or naturally, without specifying an external human actor: 'A szöveg sokszorosítódik' (The text is duplicated / gets multiplied).",
                "text2_title": "Organic Process vs. External Force",
                "text2": "Verbs like terjed ('spreads'), alakul ('develops/forms'), megoldódik ('resolves itself'), and másolódik ('gets copied') allow speakers to discuss social and cultural phenomena without attributing blame or tracking individual agents, making them vital for historical description.",
                "table_title": "Middle-Voice Agentless Verbs",
                "table_rows": [
                    [
                        "A tiltott könyvek lapjai éjszaka sokszorosítódtak a pesti konyhákban.",
                        "The pages of prohibited books multiplied at night in Budapest kitchens."
                    ],
                    [
                        "A szabad gondolatok gyorsan terjedtek az egyetemi ifjúság körében.",
                        "Free thoughts spread quickly among university youth."
                    ],
                    [
                        "A másolatok kézről kézre adva cserélődtek a lakásokban.",
                        "The copies were exchanged hand to hand in private apartments."
                    ],
                    [
                        "Az illegális kiadók hálózata fokozatosan épült ki a rendőrségi zaklatások ellenére.",
                        "The network of underground publishers built up gradually despite police harassment."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A szamizdat füzetek több ezer példányban terjedtek a fővárosban.",
                        "english": "The samizdat booklets spread in thousands of copies in the capital."
                    },
                    {
                        "spanish": "A titkos nyomdákban a stencilfesték szaga keveredett a dohányfüsttel.",
                        "english": "In the clandestine printshops, the smell of stencil ink mixed with tobacco smoke."
                    },
                    {
                        "spanish": "A házkutatások során az elrejtett iratok egy része elkobzódott, de a mozgalom nem tört meg.",
                        "english": "During the house searches a portion of hidden papers was confiscated, but the movement did not break."
                    }
                ],
                "tip": "Use -ódik/-ődik verbs when you want to describe how materials, ideas, or networks emerge and spread naturally: 'A hálózat gyorsan kibontakozott'."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi a 'szamizdat' kifejezés jelentése a kelet-európai történelemben?",
                    "options": [
                        "Az állami cenzúrát megkerülő, illegálisan sokszorosított és terjesztett irodalmi és politikai kiadvány.",
                        "A hivatalos pártlapok karácsonyi ünnepi melléklete.",
                        "A szovjet mezőgazdasági statisztikákat összesítő kézikönyv."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A rendőrség hajnalban váratlan _____ tartott az illegális nyomdának helyet adó lakásban. (house search)",
                    "answer": "házkutatást",
                    "english": "At dawn the police conducted an unexpected house search in the apartment hosting the illegal printshop.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A tiltott könyvek ezer meg ezer példányban _____ az éjszakai műszakok alatt. (multiplied / were duplicated)",
                    "answer": "sokszorosítódtak",
                    "english": "The prohibited books multiplied in thousands and thousands of copies during the night shifts.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban fejez ki a cselekvő nélküli folyamatot egy '-ódik/-ődik' képzős ige?",
                    "options": [
                        "A cenzúrázatlan írások gyorsan terjedtek, és kézről kézre adva másolódtak.",
                        "A cenzúrázatlan írásokat gyorsan másolták amennyiben terjesztették.",
                        "A cenzúrázatlan írások másolásra jutottak a rendőrség által."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "tiltott",
                        "szamizdat",
                        "irodalom",
                        "rohamosan",
                        "terjedt",
                        "az",
                        "értelmiségiek",
                        "között."
                    ],
                    "solution": [
                        "A",
                        "tiltott",
                        "szamizdat",
                        "irodalom",
                        "rohamosan",
                        "terjedt",
                        "az",
                        "értelmiségiek",
                        "között."
                    ],
                    "english": "Prohibited samizdat literature spread rapidly among intellectuals.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan állították elő a szamizdat könyveket a budapesti lakásokban?",
                    "options": [
                        "Fából készült kézi szitanyomó keretekkel (ramkákkal) és egyszerű stencilekkel sokszorosították őket.",
                        "A Magyar Tudományos Akadémia hivatalos nyomdagépein nyomtatták őket.",
                        "Kizárólag külföldi nagykövetségeken készítettek róluk másolatokat."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "titkosrendőrség",
                        "rendszeres",
                        "zaklatással",
                        "és",
                        "elkobzással",
                        "próbálta",
                        "megfélemlíteni",
                        "az",
                        "ellenzéket."
                    ],
                    "solution": [
                        "A",
                        "titkosrendőrség",
                        "rendszeres",
                        "zaklatással",
                        "és",
                        "elkobzással",
                        "próbálta",
                        "megfélemlíteni",
                        "az",
                        "ellenzéket."
                    ],
                    "english": "The secret police tried to intimidate the opposition with regular harassment and confiscation.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing how samizdat copies multiplied organically using 'sokszorosítódtak'.",
                            "answer": "A tiltott könyvek lapjai egyszerű konyhai ramkákon sokszorosítódtak a pesti éjszakában."
                        },
                        {
                            "prompt": "State how the underground distribution network developed despite raids using 'épült ki'.",
                            "answer": "A független terjesztői hálózat a folyamatos házkutatások ellenére sikeresen kiépült az egész országban."
                        }
                    ],
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                }
            ]
        },
        {
            "num": 5,
            "title": "How Democratic Opposition Emerged from Print",
            "grammar_label": "Agentless nominalization and systemic attribution (közzétételre kerül, nyilvánosságra hozatal)",
            "goals": [
                "I can evaluate the historic role of the samizdat journal Beszélő (founded in 1981 by János Kis, Miklós Haraszti, Ferenc Kőszeg) in paving the way for the 1989 regime change.",
                "I can use agentless nominalized event structures (közzétételre kerül, elemzés tárgyát képezi) in formal analysis.",
                "I can synthesize the trajectory from state censorship to free public discourse in 20th-century Hungary."
            ],
            "story_segment": {
                "seg_slug": "beszelofolyoirat",
                "title": "A Beszélő és a demokratikus ellenzék felemelkedése",
                "summary": "Founded in 1981, the underground journal Beszélő broke the state monopoly on information, formulating programmatic demands for civil liberties that directly shaped Hungary's 1989 transition.",
                "location": "Budapest és Monor (1981–1989)",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "1981 decemberében, szinte egy időben a lengyelországi szükségállapot bevezetésével, Budapesten megjelent egy vékony, gépelt lapokból álló illegális folyóirat: a Beszélő. A szerkesztők — Kis János filozófus, Haraszti Miklós író, Kőszeg Ferenc szerkesztő és Solt Ottilia szociológus — nem kevesebbre vállalkoztak, mint a demokratikus nyilvánosság megteremtésére az egypártrendszer díszletei mögött."
                    },
                    {
                        "type": "narration",
                        "text": "A Beszélő minőségi fordulatot hozott az ellenállás történetében. Nem csupán tiltakozott, hanem pontos tényfeltáró cikkeket közölt: beszámolt az elhallgatott szegénységről, a határon túli magyarság jogfosztottságáról, a börtönök állapotáról és a független békemozgalmakról. A lap hasábjain a valóság dokumentálása közzétételre került, megtörve a hivatalos média hazugságait."
                    },
                    {
                        "type": "narration",
                        "text": "A folyóirat köré szerveződő demokratikus ellenzék 1985-ben Monoron, egy kemping faházaiban történelmi találkozót szervezett, ahol a népi és az urbánus gondolkodók először ültek közös asztalhoz, hogy megvitassák az ország jövőjét. A Beszélőben megfogalmazott követelések — az emberi jogok, a sajtószabadság és a többpártrendszer — a rendszerváltás politikai alapköveivé váltak."
                    },
                    {
                        "type": "narration",
                        "text": "1987-ben a lap különszámaként megjelent a híres program: a Társadalmi Szerződés, amely nyíltan kimondta az addig elképzelhetetlent: „Kádárnak mennie kell!” A cenzúrázatlan nyilvánosság ereje olyan hatalmasnak bizonyult, hogy a rezsim már nem tudta elhallgattatni a követeléseket."
                    },
                    {
                        "type": "narration",
                        "text": "Amikor 1989-ben leomlottak a vasfüggöny rácsai és Magyarország kikiáltotta a köztársaságot, a Beszélő szerkesztői a parlament és a független sajtó vezetőiként folytathatták munkájukat. A konyhai stencilek szabadságharca békés, demokratikus győzelemmel zárult."
                    }
                ]
            },
            "words": [
                {
                    "lemma": "demokratikus ellenzék",
                    "translation": "democratic opposition",
                    "pos": "noun"
                },
                {
                    "lemma": "közzétételre kerül",
                    "translation": "comes to be published / is made public",
                    "pos": "expression"
                },
                {
                    "lemma": "polgárjogok",
                    "translation": "civil rights",
                    "pos": "noun"
                },
                {
                    "lemma": "információs monopólium",
                    "translation": "information monopoly",
                    "pos": "noun"
                },
                {
                    "lemma": "rendszerváltás",
                    "translation": "regime change / transition to democracy",
                    "pos": "noun"
                },
                {
                    "lemma": "független sajtó",
                    "translation": "independent press",
                    "pos": "noun"
                }
            ],
            "grammar_doc": {
                "slug": "agent-backgrounding-nominalized-action",
                "title": "Agentless Nominalization: Formal Written Register",
                "text1_title": "Nominalization of Events in High Register",
                "text1": "In sophisticated academic, legal, and historical Hungarian, entire clauses are compressed into verbal nouns (közzététel, nyilvánosságra hozatal, megfogalmazás, felszámolás). These noun phrases are then governed by verbs like kerül ('comes to'), történik ('occurs'), or valósul meg ('materializes').",
                "text2_title": "Syntactic Precision and Objectivity",
                "text2": "Nominalization lends texts an objective, analytical tone suitable for analyzing historical processes: 'A Beszélőben megfogalmazott követelések nyilvánosságra hozatala megrendítette a pártállam tekintélyét' (The making public of demands formulated in Beszélő shook the authority of the party-state).",
                "table_title": "Nominalized Event Structures",
                "table_rows": [
                    [
                        "A szamizdat folyóiratban a tabutémák nyílt megvitatásra kerültek.",
                        "In the samizdat periodical, taboo topics came under open discussion."
                    ],
                    [
                        "Az emberi jogok megsértésének dokumentálása elengedhetetlen lépés volt.",
                        "The documentation of human rights violations was an indispensable step."
                    ],
                    [
                        "A demokratikus átmenet programja a sajtószabadság megteremtésével valósult meg.",
                        "The program of democratic transition was realized with the creation of press freedom."
                    ],
                    [
                        "A cenzúra intézményes felszámolása a rendszerváltás alapvető eredménye volt.",
                        "The institutional dismantling of censorship was a fundamental achievement of the regime change."
                    ]
                ],
                "examples": [
                    {
                        "spanish": "A demokratikus ellenzék programja a Beszélő hasábjain került közzétételre.",
                        "english": "The program of the democratic opposition came to be published in the columns of Beszélő."
                    },
                    {
                        "spanish": "A politikai foglyok ügyeinek nyilvánosságra hozatala megtörte a rezsim információs monopóliumát.",
                        "english": "The public disclosure of political prisoners' cases broke the regime's information monopoly."
                    },
                    {
                        "spanish": "A szabad választások követelése az illegális sajtó legfontosabb célkitűzéseként fogalmazódott meg.",
                        "english": "The demand for free elections was formulated as the most important objective of the illegal press."
                    }
                ],
                "tip": "When writing B2 essays on historical transitions, use nominalized structures ('az információs monopólium megtörése', 'közzétételre kerül') to elevate your style to native academic standard."
            },
            "exercises": [
                {
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mi volt a 'Beszélő' című szamizdat folyóirat fő jelentősége az 1980-as években?",
                    "options": [
                        "Megtörte a pártállam információs monopóliumát, és megfogalmazta a demokratikus átmenet programját.",
                        "A sportesemények hivatalos eredményeit közölte a külföldi diplomaták számára.",
                        "A minisztérium által támogatott szépirodalmi antológia volt."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A cenzúrázatlan lapok következetesen kiálltak a _____ és a sajtószabadság megteremtése mellett. (civil rights)",
                    "answer": "polgárjogok",
                    "english": "The uncensored papers consistently stood up for the creation of civil rights and freedom of the press.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A demokratikus ellenzék politikai programja a szamizdat sajtóban _____ közzétételre 1987-ben. (came to / was)",
                    "answer": "került",
                    "english": "The political program of the democratic opposition came to be published in the samizdat press in 1987.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": "Melyik mondatban találunk akadémiai szintű, cselekvőtlen eseménynominalizációt?",
                    "options": [
                        "A cenzúra felszámolása és a sajtószabadság kikiáltása a rendszerváltás kulcsfontosságú eredménye volt.",
                        "Felszámolták a cenzúrát és kikiáltották a sajtószabadságot amikor rendszert váltottak.",
                        "A cenzúra felszámolódása közben kikiáltódott a sajtószabadság."
                    ],
                    "correct": 0,
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": [
                        "A",
                        "tények",
                        "nyilvánosságra",
                        "hozatala",
                        "alapjaiban",
                        "ingatta",
                        "meg",
                        "a",
                        "diktatúra",
                        "tekintélyét."
                    ],
                    "solution": [
                        "A",
                        "tények",
                        "nyilvánosságra",
                        "hozatala",
                        "alapjaiban",
                        "ingatta",
                        "meg",
                        "a",
                        "diktatúra",
                        "tekintélyét."
                    ],
                    "english": "The making public of the facts fundamentally shook the authority of the dictatorship.",
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                },
                {
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mit követelt a Beszélő 1987-es 'Társadalmi Szerződés' című különszáma?",
                    "options": [
                        "A Kádár-vezetés távozását, többpártrendszert és demokratikus szabadságjogokat.",
                        "A szocialista gazdaságtervezés szigorítását.",
                        "A külföldi utazások teljes betiltását a lakosság védelmében."
                    ],
                    "correct": 0
                },
                {
                    "type": "sentence-builder",
                    "category": "vocabulary",
                    "tiles": [
                        "A",
                        "független",
                        "sajtó",
                        "megteremtése",
                        "nélkül",
                        "a",
                        "békés",
                        "rendszerváltás",
                        "elképzelhetetlen",
                        "lett",
                        "volna."
                    ],
                    "solution": [
                        "A",
                        "független",
                        "sajtó",
                        "megteremtése",
                        "nélkül",
                        "a",
                        "békés",
                        "rendszerváltás",
                        "elképzelhetetlen",
                        "lett",
                        "volna."
                    ],
                    "english": "Without the creation of independent press, peaceful regime change would have been unimaginable.",
                    "teaches": [
                        "b2-szamizdat-vocab"
                    ]
                },
                {
                    "type": "structured-writing",
                    "category": "writing",
                    "template": [
                        {
                            "prompt": "Write a sentence describing the publication of the Beszélő manifesto using 'közzétételre került'.",
                            "answer": "A Társadalmi Szerződés című történelmi dokumentum 1987-ben került közzétételre a szamizdatban."
                        },
                        {
                            "prompt": "State that breaking the information monopoly was crucial for civil rights using 'nyilvánosságra hozatala'.",
                            "answer": "Az elhallgatott valóság nyilvánosságra hozatala elengedhetetlen volt a polgárjogok kivívásához."
                        }
                    ],
                    "teaches": [
                        "b2-agent-backgrounding"
                    ]
                }
            ]
        }
    ],
    "consolidation": {
        "goals": [
            "I can analyze Aczél's 'Three Ts' cultural policy and the historic emergence of the Samizdat underground.",
            "I can deploy agent-backgrounding structures (institutional 3rd plural, -ra/-re kerül, evaluative predicates, middle verbs, and nominalization).",
            "I can discuss censorship, double speak, and civil resistance in fluent B2 Hungarian."
        ],
        "exercises": [
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik szerkezet fejezi ki legtermészetesebben a hivatalos intézményi cselekvést a magyarban?",
                "options": [
                    "A 3. személyű többes számú igealak rejtett alannyal (pl. 'a tiltott kategóriába sorolják').",
                    "A -tat/-tet műveltető képző használata.",
                    "A segédigés passzív szerkezet (pl. 'be van tiltva')."
                ],
                "correct": 0,
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "vocabulary",
                "stage": "recognize",
                "question": "Melyik kategóriába sorolta Aczél György kultúrpolitikája azokat a műveket, amelyek korlátozottan megjelenhettek?",
                "options": [
                    "tűrt",
                    "támogatott",
                    "tiltott"
                ],
                "correct": 0,
                "teaches": [
                    "b2-szamizdat-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "recognize",
                "question": "Melyik ige fejez ki spontán, cselekvő nélküli folyamatot '-ódik/-ődik' képzővel?",
                "options": [
                    "sokszorosítódik",
                    "sokszorosíttat",
                    "sokszorosítana"
                ],
                "correct": 0,
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A vitatott kézirat a minisztériumi egyeztetések után végül kiadásra _____. (came to be / was)",
                "answer": "került",
                "english": "After the ministerial consultations, the disputed manuscript finally came to be published.",
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "fill-blank",
                "category": "vocabulary",
                "stage": "recall",
                "sentence": "A szerzők a cenzúrát elkerülendő gyakran éltek a rejtett politikai _____ eszközével a színházban. (allusion / double entendre)",
                "answer": "áthallások",
                "english": "To avoid censorship, authors often resorted to the tool of hidden political allusions in the theatre.",
                "teaches": [
                    "b2-szamizdat-vocab"
                ]
            },
            {
                "type": "fill-blank",
                "category": "grammar",
                "stage": "recall",
                "sentence": "A szamizdat folyóiratot a pártvezetésben súlyos államellenes veszélynek _____ a tisztviselők. (consider / 3rd plural)",
                "answer": "tekintették",
                "english": "In the party leadership, officials regarded the samizdat periodical as a grave anti-state danger.",
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "in-context",
                "tiles": [
                    "A",
                    "szamizdat",
                    "irodalom",
                    "lapjai",
                    "titokban",
                    "sokszorosítódtak",
                    "a",
                    "konyhákban."
                ],
                "solution": [
                    "A",
                    "szamizdat",
                    "irodalom",
                    "lapjai",
                    "titokban",
                    "sokszorosítódtak",
                    "a",
                    "konyhákban."
                ],
                "english": "The pages of samizdat literature multiplied in secret in the kitchens.",
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "vocabulary",
                "stage": "in-context",
                "tiles": [
                    "A",
                    "demokratikus",
                    "ellenzék",
                    "fellépése",
                    "megtörte",
                    "az",
                    "állami",
                    "információs",
                    "monopóliumot."
                ],
                "solution": [
                    "A",
                    "demokratikus",
                    "ellenzék",
                    "fellépése",
                    "megtörte",
                    "az",
                    "állami",
                    "információs",
                    "monopóliumot."
                ],
                "english": "The emergence of the democratic opposition broke the state information monopoly.",
                "teaches": [
                    "b2-szamizdat-vocab"
                ]
            },
            {
                "type": "multiple-choice",
                "category": "grammar",
                "stage": "in-context",
                "question": "Melyik mondat alkalmazza helyesen az értékelő személytelen szerkezetet?",
                "options": [
                    "A virágnyelv használatát alapvető fontosságúnak tartották a színházi előadásokon.",
                    "A virágnyelv használatát alapvető fontosságúan tartották a színházi előadásokon.",
                    "A virágnyelv használatát alapvető fontosságú tartották a színházi előadásokon."
                ],
                "correct": 0,
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "sentence-builder",
                "category": "grammar",
                "stage": "produce",
                "tiles": [
                    "A",
                    "követelések",
                    "nyilvánosságra",
                    "hozatala",
                    "alapozta",
                    "meg",
                    "a",
                    "békés",
                    "átmenetet."
                ],
                "solution": [
                    "A",
                    "követelések",
                    "nyilvánosságra",
                    "hozatala",
                    "alapozta",
                    "meg",
                    "a",
                    "békés",
                    "átmenetet."
                ],
                "english": "The public disclosure of the demands laid the groundwork for the peaceful transition.",
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Synthesize the mechanism of censorship and samizdat resistance using 'sorolják' and 'sokszorosítódtak'.",
                        "answer": "Bár a bátor műveket a tiltott kategóriába sorolják a hatóságok, a lapok mégis titokban sokszorosítódtak a lakásokban."
                    }
                ],
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            },
            {
                "type": "structured-writing",
                "category": "writing",
                "stage": "produce",
                "template": [
                    {
                        "prompt": "Formulate how the underground press prepared the 1989 transition using 'közzétételre került'.",
                        "answer": "A demokratikus ellenzék történelmi programja a Beszélő hasábjain került közzétételre a rendszerváltás előtt."
                    }
                ],
                "teaches": [
                    "b2-agent-backgrounding"
                ]
            }
        ]
    }
}


def main():
    print("Building Hungarian B2 Culture Units 13, 14, and 15...")
    build_culture_unit(UNIT_13_PESTIHUMOR)
    build_culture_unit(UNIT_14_MAGYARFILM)
    build_culture_unit(UNIT_15_SZAMIZDAT)
    print("All 3 Culture Track units (13, 14, 15) built successfully!")


if __name__ == "__main__":
    main()
