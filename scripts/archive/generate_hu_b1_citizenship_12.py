#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 12: Driving Out the Ottomans (b1-torokkiuzese)."""

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

def build_unit_12_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.torokkiuzese.01",
        "lesson": "b1-torokkiuzese-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Szent Liga", "translation": "Holy League (anti-Ottoman Christian alliance)", "pos": "noun"},
            {"lemma": "Buda visszafoglalása", "translation": "reconquest / liberation of Buda (1686)", "pos": "noun"},
            {"lemma": "ostrom", "translation": "siege", "pos": "noun"},
            {"lemma": "Lotaringiai Károly", "translation": "Charles V, Duke of Lorraine", "pos": "noun"},
            {"lemma": "Petneházy Dávid", "translation": "Dávid Petneházy (heroic Hungarian officer)", "pos": "noun"},
            {"lemma": "Abdurrahman pasa", "translation": "Abdi Pasha (last Ottoman pasha of Buda)", "pos": "noun"},
            {"lemma": "felszabadulás", "translation": "liberation", "pos": "noun"},
            {"lemma": "ágyútűz", "translation": "artillery fire, cannonade", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-torokkiuzese-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.torokkiuzese.02",
        "lesson": "b1-torokkiuzese-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "felszabadító hadjárat", "translation": "liberation campaign", "pos": "noun"},
            {"lemma": "Nagyharsányi csata", "translation": "Battle of Nagyharsány / Second Mohács (1687)", "pos": "noun"},
            {"lemma": "Zentai csata", "translation": "Battle of Zenta (1697)", "pos": "noun"},
            {"lemma": "Savoyai Jenő", "translation": "Prince Eugene of Savoy", "pos": "noun"},
            {"lemma": "karlócai béke", "translation": "Peace of Karlowitz (1699)", "pos": "noun"},
            {"lemma": "hódoltság vége", "translation": "end of Ottoman rule in Hungary", "pos": "noun"},
            {"lemma": "határvonal", "translation": "border demarcation line", "pos": "noun"},
            {"lemma": "fennhatóság", "translation": "sovereignty, dominion", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-torokkiuzese-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.torokkiuzese.03",
        "lesson": "b1-torokkiuzese-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "pusztulás", "translation": "devastation, destruction", "pos": "noun"},
            {"lemma": "elnéptelenedés", "translation": "depopulation", "pos": "noun"},
            {"lemma": "romváros", "translation": "ruined city / town", "pos": "noun"},
            {"lemma": "járvány", "translation": "epidemic, pestilence", "pos": "noun"},
            {"lemma": "hadseregtartás", "translation": "quartering / maintenance of army", "pos": "noun"},
            {"lemma": "porció", "translation": "portion (compulsory military food tax)", "pos": "noun"},
            {"lemma": "forspont", "translation": "forced military haulage / transport duty", "pos": "noun"},
            {"lemma": "anyagi teher", "translation": "financial burden", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-torokkiuzese-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.torokkiuzese.04",
        "lesson": "b1-torokkiuzese-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Habsburg-uralom", "translation": "Habsburg imperial rule", "pos": "noun"},
            {"lemma": "újszerzeményi bizottság", "translation": "Neoacquistica Commissio (land confiscation committee)", "pos": "noun"},
            {"lemma": "fegyverváltság", "translation": "weapon ransom / 10% redemption fee on reclaimed land", "pos": "noun"},
            {"lemma": "nemesi jogok sérelme", "translation": "infringement of noble constitutional rights", "pos": "noun"},
            {"lemma": "katonai megszállás", "translation": "military occupation", "pos": "noun"},
            {"lemma": "elégedetlenség", "translation": "widespread dissatisfaction / discontent", "pos": "noun"},
            {"lemma": "örökös királyság", "translation": "hereditary Habsburg monarchy (enacted 1687)", "pos": "noun"},
            {"lemma": "ellenállási jog", "translation": "right of armed resistance (jus resistendi, repealed 1687)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-torokkiuzese-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.torokkiuzese.05",
        "lesson": "b1-torokkiuzese-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kuruc", "translation": "Kuruc (anti-Habsburg insurgent / soldier)", "pos": "noun"},
            {"lemma": "bujdosó", "translation": "exiled fugitive / outlaw rebel", "pos": "noun"},
            {"lemma": "Thököly Imre", "translation": "Imre Thököly (Kuruc leader)", "pos": "noun"},
            {"lemma": "II. Rákóczi Ferenc", "translation": "Ferenc Rákóczi II (ruling prince, national leader)", "pos": "noun"},
            {"lemma": "szabadságharc", "translation": "war of independence (1703–1711)", "pos": "noun"},
            {"lemma": "nemzeti összefogás", "translation": "national solidarity / unity in struggle", "pos": "noun"},
            {"lemma": "történelmi fordulat", "translation": "historic turning point", "pos": "noun"},
            {"lemma": "függetlenség", "translation": "national independence", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-torokkiuzese-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.torokkiuzese.01.purpose-clauses-liberation",
        "title": "Purpose Clauses in Military Campaigns: azért, hogy + Subjunctive",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Strategic Objectives with 'azért, hogy'",
                "content": "To explain military operations and international alliances, Hungarian uses purpose clauses with *azért, hogy...* ('in order that / so that...') followed by the subjunctive mood (*-jon / -jen*)."
            },
            {
                "type": "examples",
                "title": "Purpose clause examples",
                "items": [
                    {
                        "spanish": "Az európai keresztény államok létrehozták a Szent Ligát azért, hogy kiűzzék a törököt Magyarországról.",
                        "english": "The European Christian states created the Holy League so that they would drive the Turks out of Hungary."
                    },
                    {
                        "spanish": "A szövetséges sereg hetekig ostromolta Budát azért, hogy megtörje a várvédők ellenállását.",
                        "english": "The allied army besieged Buda for weeks in order to break the defenders' resistance."
                    },
                    {
                        "spanish": "A magyar katonák hősiesen harcoltak azért, hogy másfél évszázad után felszabadítsák az ősi fővárost.",
                        "english": "Hungarian soldiers fought heroically so that they could liberate the ancient capital after 150 years."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-torokkiuzese-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.torokkiuzese.02.temporal-sequencing-war",
        "title": "Temporal Sequencing in Warfare: mihelyt, amint, azt követően, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Narrating Chains of Strategic Victories and Treaties",
                "content": "Narrating long-duration multi-year military campaigns utilizes temporal conjunctions indicating immediate succession: *amint / mihelyt* ('as soon as'), *azt követően, hogy...* ('following the fact that...'), and *végül* ('in the end / finally')."
            },
            {
                "type": "examples",
                "title": "Campaign sequence examples",
                "items": [
                    {
                        "spanish": "Amint Buda felszabadult, a császári hadak dél felé nyomultak előre.",
                        "english": "As soon as Buda was liberated, the imperial armies advanced southward."
                    },
                    {
                        "spanish": "Azt követően, hogy Savoyai Jenő Zentánál döntő vereséget mért a szultánra, a törökök békét kértek.",
                        "english": "Following Eugene of Savoy dealing a decisive defeat to the sultan at Zenta, the Turks sued for peace."
                    },
                    {
                        "spanish": "Az 1699-es karlócai békével végleg lezárult a 150 éves oszmán hódoltság korszaka.",
                        "english": "With the 1699 Peace of Karlowitz, the 150-year era of Ottoman rule came to a permanent close."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-torokkiuzese-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.torokkiuzese.03.hardship-obligation",
        "title": "Expressing Inevitable Hardship: kénytelen volt, kénytelenek voltak",
        "sections": [
            {
                "type": "text",
                "title": "Depicting Compelled Suffering and Wartime Exactions",
                "content": "When narrating civilian hardship and unavoidable duties, Hungarian uses *kénytelen volt / voltak* (+ infinitive: 'was / were compelled to / had no choice but to'): *kénytelen volt elviselni* (was forced to endure), *kénytelenek voltak fizetni* (were forced to pay)."
            },
            {
                "type": "examples",
                "title": "Hardship examples",
                "items": [
                    {
                        "spanish": "A szétrombolt falvak lakossága kénytelen volt a császári katonák ellátásáról gondoskodni.",
                        "english": "The population of ruined villages had no choice but to provide for the imperial troops."
                    },
                    {
                        "spanish": "A jobbágyok kénytelenek voltak elviselni a hadseregtartás súlyos adóterheit, a porciót és a forspontot.",
                        "english": "The serfs were compelled to endure the heavy taxes of quartering troops: food levies and transport duties."
                    },
                    {
                        "spanish": "A pestisjárványok miatt sokan kénytelenek voltak elhagyni ősi otthonaikat.",
                        "english": "Because of plague epidemics, many people were forced to abandon their ancestral homes."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-torokkiuzese-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.torokkiuzese.04.concession-frustration",
        "title": "Concession & Discontent: noha, jóllehet, annak dacára, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Contrasting Liberation with Imperial Oppression",
                "content": "To express historical disappointment and contradictory outcomes, use concessive expressions: *annak dacára, hogy...* ('in spite of the fact that...'), *noha* ('although'), and *ennek ellenére* ('nevertheless')."
            },
            {
                "type": "examples",
                "title": "Discontent examples",
                "items": [
                    {
                        "spanish": "Noha a törököket kiűzték az országból, a magyar nemesek súlyos sérelmeket szenvedtek el Bécstől.",
                        "english": "Although the Turks were expelled from the country, Hungarian nobles suffered heavy grievances from Vienna."
                    },
                    {
                        "spanish": "Annak dacára, hogy a birtokaikat visszakapták volna, az Újszerzeményi Bizottság fegyverváltságot követelt.",
                        "english": "In spite of expecting their estates back, the Neoacquistica Commission demanded a weapon ransom fee."
                    },
                    {
                        "spanish": "Az 1687-es pozsonyi országgyűlésen a rendek lemondtak az Aranybulla ellenállási jogáról.",
                        "english": "At the 1687 Diet of Pozsony, the estates renounced the Golden Bull's right of resistance."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-torokkiuzese-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.torokkiuzese.05.anticipating-struggle",
        "title": "Anticipating National Revolts: elkerülhetetlenné vált, utat nyitott",
        "sections": [
            {
                "type": "text",
                "title": "Historical Foreshadowing and Causality",
                "content": "To link the end of Ottoman occupation to the Kuruc independence struggle, use transitional phrases: *elkerülhetetlenné vált* ('became inevitable'), *előkészítette az utat* ('paved the way for'), and *szabadságharcba torkollott* ('culminated in a war of independence')."
            },
            {
                "type": "examples",
                "title": "Foreshadowing examples",
                "items": [
                    {
                        "spanish": "A bécsi udvar önkényuralma miatt egy új nemzeti felkelés elkerülhetetlenné vált.",
                        "english": "Due to the absolutism of the Viennese court, a new national uprising became inevitable."
                    },
                    {
                        "spanish": "A bujdosó kurucok elkeseredett harca utat nyitott a Rákóczi-szabadságharc kitöréséhez.",
                        "english": "The desperate struggle of the fugitive Kuruc rebels paved the way for the outbreak of Rákóczi's War of Independence."
                    },
                    {
                        "spanish": "1703-ban II. Rákóczi Ferenc vezetésével megindult a magyar történelem legnagyobb függetlenségi küzdelme.",
                        "english": "In 1703, under the leadership of Ferenc Rákóczi II, the greatest independence struggle in Hungarian history began."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-torokkiuzese-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (5 serialized segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.torokkiuzese.01",
        "title": "Buda visszavétele 1686-ban",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "In the summer of 1686, the multinational Christian army of the Holy League besieged Buda. On September 2, 1686, led by Hungarian hero Dávid Petneházy, allied troops stormed the ramparts, ending 145 years of Ottoman rule in the ancient capital.",
        "characters": [],
        "location": "Buda vára, Gellért-hegy, Víziváros",
        "grammar": ["purpose-clauses-liberation"],
        "vocabularyTopics": ["Buda 1686", "Szent Liga", "Lotaringiai Károly", "Petneházy Dávid"],
        "paragraphs": [
            {"type": "narration", "text": "1686 forró nyarán az európai Szent Liga mintegy 80 ezer fős nemzetközi keresztény sereggel vette ostrom alá Budát."},
            {"type": "narration", "text": "Lotaringiai Károly herceg parancsnoksága alatt német, spanyol, olasz és tizenötezer magyar katona küzdött a falaknál."},
            {"type": "narration", "text": "A várat az idős, de rendíthetetlen Abdurrahman pasa védte elszánt janicsárjaival az utolsó leheletéig."},
            {"type": "narration", "text": "Szeptember 2-án délután megindult a döntő roham: a magyar hajdúk élén Petneházy Dávid elsőként jutott fel a várfalra."},
            {"type": "narration", "text": "A véres harcban a vár elesett: 145 év oszmán uralom után Buda ismét keresztény kézre került, ami egész Európában harangzúgást váltott ki."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese-01-ostrom.json", story_01)

    story_02 = {
        "id": "story.b1.torokkiuzese.02",
        "title": "A győzelmes hadjáratok és a karlócai béke",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Following Buda's fall, allied forces crushed the Ottomans at Nagyharsány (1687) and Zenta (1697) under Eugene of Savoy. The 1699 Peace of Karlowitz formally ended Ottoman occupation across virtually all of historic Hungary.",
        "characters": [],
        "location": "Nagyharsány, Zenta, Karlóca",
        "grammar": ["temporal-sequencing-war"],
        "vocabularyTopics": ["Felszabadító hadjárat", "Zentai csata", "Karlócai béke 1699"],
        "paragraphs": [
            {"type": "narration", "text": "Buda visszafoglalása után a keresztény szövetséges hadak lendületes offenzívát indítottak dél felé."},
            {"type": "narration", "text": "1687-ben Nagyharsánynál, a 'második mohácsi csatában' megsemmisítő vereséget mértek a szultán főseregére."},
            {"type": "narration", "text": "Tíz évvel később, 1697-ben a zentai csatában a zseniális ifjú hadvezér, Savoyai Jenő herceg szétzúzta a török erőket a Tiszánál."},
            {"type": "narration", "text": "A katonai vereségek után az Oszmán Birodalom kénytelen volt elfogadni az 1699-es karlócai békeszerződés feltételeit."},
            {"type": "narration", "text": "A Temesköz kivételével egész Magyarország és Erdély felszabadult a másfél évszázados török iga alól."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese-02-karloca.json", story_02)

    story_03 = {
        "id": "story.b1.torokkiuzese.03",
        "title": "A felszabadulás súlyos ára",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Liberation came at immense human and material cost: scorched earth, plague epidemics, devastated towns, and crushing military taxes (porció and forspont) imposed by imperial troops quartered across Hungarian villages.",
        "characters": [],
        "location": "Alföld, Dunántúl, magyar falvak",
        "grammar": ["hardship-obligation"],
        "vocabularyTopics": ["Pusztulás és elnéptelenedés", "Porció és forspont", "Hadseregtartás"],
        "paragraphs": [
            {"type": "narration", "text": "A hosszan tartó felszabadító háborúk óriási áldozatokat és pusztulást hoztak a magyar földre."},
            {"type": "narration", "text": "Az Alföld virágzó települései elnéptelenedtek, a visszavonuló török és az előrenyomuló császári hadak felégették a falvakat."},
            {"type": "narration", "text": "A lakosságot pestisjárványok tizedelték meg, miközben a bécsi hadvezetés elviselhetetlen terheket rótt a népre."},
            {"type": "narration", "text": "A jobbágyok kénytelenek voltak elviselni a katonák élelmezését szolgáló porciót és a fuvarozási kényszert, a forspontot."},
            {"type": "narration", "text": "Sok magyar ember keserűen úgy érezte: a török félhold helyébe a császári sas nehéz vasmarka lépett."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese-03-ara.json", story_03)

    story_04 = {
        "id": "story.b1.torokkiuzese.04",
        "title": "Csalódás és elégedetlenség a felszabadulás után",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "Vienna treated Hungary as a conquered province rather than a liberated partner. The Neoacquistica Commission demanded exorbitant redemption fees from Hungarian nobles, while the Diet of 1687 revoked the hereditary right to elect kings and the right of armed resistance.",
        "characters": [],
        "location": "Pozsony, Bécs, Buda",
        "grammar": ["concession-frustration"],
        "vocabularyTopics": ["Újszerzeményi Bizottság", "Fegyverváltság", "1687 pozsonyi országgyűlés"],
        "paragraphs": [
            {"type": "narration", "text": "A felszabadulás után I. Lipót császár kormánya meghódított tartományként kezelte Magyarországot."},
            {"type": "narration", "text": "Felállították az Újszerzeményi Bizottságot (Neoacquistica Commissio), amely megkérdőjelezte a magyar nemesek ősi birtokjogait."},
            {"type": "narration", "text": "A nemeseknek írásos bizonyítékokat kellett felmutatniuk és a birtok értékének tíz százalékát 'fegyverváltságként' befizetniük a kincstárba."},
            {"type": "narration", "text": "Az 1687-es pozsonyi országgyűlésen a rendek kénytelenek voltak lemondani a szabad királyválasztásról és az Aranybulla ellenállási jogáról."},
            {"type": "narration", "text": "A sérelmek miatt a magyar társadalom minden rétegében mély elkeseredés és dac alakult ki a bécsi önkénnyel szemben."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese-04-serelmek.json", story_04)

    story_05 = {
        "id": "story.b1.torokkiuzese.05",
        "title": "A kuruc mozgalom és a Rákóczi-szabadságharc hajnala",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The smoldering resentment gave birth to the Kuruc insurgent movement. When young Prince Ferenc Rákóczi II answered the call of the peasants in 1703, Hungary launched its greatest struggle for independence under the banner 'Cum Deo pro Patria et Libertate'.",
        "characters": [],
        "location": "Tiszahát, Munkács, Sárospatak",
        "grammar": ["anticipating-struggle"],
        "vocabularyTopics": ["Kuruc mozgalom", "II. Rákóczi Ferenc", "Szabadságharc 1703"],
        "paragraphs": [
            {"type": "narration", "text": "A császári zsoldosok kegyetlensége miatt az erdőkben és hegyekben bujdosó kurucok fegyveres ellenállást kezdtek szervezni."},
            {"type": "narration", "text": "A felkelőknek olyan tekintélyes, gazdag és feddhetetlen vezetőre volt szükségük, aki mögé az egész nemzet felsorakozhat."},
            {"type": "narration", "text": "Tekintetük az ország leghatalmasabb főnemesére, a fiatal és művelt II. Rákóczi Ferencre irányult."},
            {"type": "narration", "text": "1703 tavaszán a tiszaháti szegény legények küldöttsége felkereste Rákóczit a lengyelországi Brezánban, és a fejedelem igent mondott."},
            {"type": "narration", "text": "A 'Cum Deo pro Patria et Libertate' (Istennel a hazáért és a szabadságért) feliratú zászlók alatt megkezdődött a dicsőséges Rákóczi-szabadságharc."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese-05-szabadsagharc.json", story_05)

    story_combined = {
        "id": "story.b1.torokkiuzese",
        "title": "A török kiűzése és Magyarország új korszaka (1686–1699)",
        "level": "B1",
        "order": 12,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The dramatic liberation of Hungary from Ottoman rule (1686–1699): the heroic storming of Buda Castle on September 2, 1686 by the Holy League, crushing victories at Nagyharsány and Zenta, the milestone 1699 Peace of Karlowitz, the devastating economic toll of war on common folk, imperial absolutism and noble grievances, and the rise of the Kuruc rebellion under Prince Ferenc Rákóczi II.",
        "characters": [],
        "location": "Buda, Bécs, Zenta, Karlóca, Tiszahát",
        "grammar": ["purpose-clauses-liberation", "temporal-sequencing-war", "hardship-obligation", "concession-frustration", "anticipating-struggle"],
        "vocabularyTopics": ["Buda visszafoglalása", "Karlócai béke", "Savoyai Jenő", "Újszerzeményi Bizottság", "Rákóczi-szabadságharc"],
        "paragraphs": [
            {"type": "narration", "text": "1686 nyarán az európai Szent Liga hadserege ostrom alá vette Budát. Szeptember 2-án a magyar és nemzetközi ezredek elszánt rohamban bevették a várat, és 145 év után véget vetettek a török uralomnak Magyarország szívében."},
            {"type": "narration", "text": "Buda eleste után a szövetséges csapatok sorozatos győzelmeket arattak: Nagyharsánynál (1687), majd Savoyai Jenő vezetésével Zentánál (1697) döntő vereséget mértek az oszmán seregre. Az 1699-es karlócai béke lezárta a másfél évszázados hódoltságot."},
            {"type": "narration", "text": "A felszabadulás azonban elképesztő áldozatokat követelt. A hadjáratok felégették az Alföld falvait, a lakosságot járványok tizedelték, és a bécsi hadvezetés elviselhetetlen katonai adókkal (porció, forspont) terhelte a szegény jobbágyságot."},
            {"type": "narration", "text": "A császári udvar önkényuralmat vezetett be: az Újszerzeményi Bizottság fegyverváltságot követelt a magyar nemesektől a földjeikért, miközben az 1687-es országgyűlésen a rendek lemondtak a szabad királyválasztás és az ellenállás ősi jogáról."},
            {"type": "narration", "text": "A növekvő sérelmek a bujdosó kuruc mozgalom kibontakozásához vezettek. 1703-ban a tiszaháti parasztok felhívására a fiatal II. Rákóczi Ferenc a nemzet élére állt, megnyitva a dicsőséges kuruc szabadságharc új történelmi fejezetét."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-torokkiuzese.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-torokkiuzese-01",
        "exercises": [
            {
                "id": "b1-torokkiuzese-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Szent Liga", "Holy League (Christian alliance)"],
                    ["Buda visszafoglalása", "liberation / reconquest of Buda"],
                    ["ostrom", "siege"],
                    ["Lotaringiai Károly", "Charles of Lorraine"]
                ]
            },
            {
                "id": "b1-torokkiuzese-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Petneházy Dávid", "Dávid Petneházy (officer)"],
                    ["Abdurrahman pasa", "last Ottoman pasha of Buda"],
                    ["felszabadulás", "liberation"],
                    ["ágyútűz", "artillery fire"]
                ]
            },
            {
                "id": "b1-torokkiuzese-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben és napon foglalták vissza Buda várát a keresztény szövetséges hadak?",
                "options": ["1686. szeptember 2-án.", "1541. augusztus 29-én.", "1699. január 26-án."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-01.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt a Szent Liga főseregeinek főparancsnoka Buda 1686-os ostromakor?",
                "options": ["Lotaringiai Károly herceg.", "Savoyai Jenő.", "II. Rákóczi Ferenc."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki a célt a mondatban: „A szövetségesek egyesítették erejüket ______ , hogy felszabadítsák Budát.”?",
                "options": ["azért", "ellenére", "helyett"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar hajdúk élén Petneházy Dávid első____ jutott fel a budai várfalra a döntő roham során. (first: elsőként)",
                "answer": "ként"
            },
            {
                "id": "b1-torokkiuzese-01.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hány évig tartott a török uralom Budán (1541-től 1686-ig)?",
                "options": ["145 évig (közel másfél évszázadig).", "Mindössze 20 évig.", "300 évig."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-01.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan fogadta Európa Buda 1686-os felszabadulásának hírét?",
                "options": [
                    "Hatalmas örömmel és hálaadással: Rómában és a kontinens nagyvárosaiban zúgtak a templomok harangjai.",
                    "Közönnyel, senki sem figyelt rá.",
                    "Gyásszal, mert szerették volna a török jelenlétet."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt az utolsó budai pasa, aki a várfalakon esett el az ostrom végén?",
                "options": ["Abdurrahman pasa.", "Gül Baba.", "Ibrahim pasa."],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-torokkiuzese-02",
        "exercises": [
            {
                "id": "b1-torokkiuzese-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["felszabadító hadjárat", "liberation campaign"],
                    ["Nagyharsányi csata", "Battle of Nagyharsány"],
                    ["Zentai csata", "Battle of Zenta"],
                    ["Savoyai Jenő", "Eugene of Savoy"]
                ]
            },
            {
                "id": "b1-torokkiuzese-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["karlócai béke", "Peace of Karlowitz (1699)"],
                    ["hódoltság vége", "end of Ottoman rule"],
                    ["határvonal", "border line"],
                    ["fennhatóság", "sovereignty / authority"]
                ]
            },
            {
                "id": "b1-torokkiuzese-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik híres csatában aratott döntő győzelmet Savoyai Jenő 1697-ben a török sereg felett?",
                "options": ["A zentai csatában a Tisza partján.", "A rigómezei csatában.", "A mohácsi csatában."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-02.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben írták alá a karlócai békét, amely hivatalosan lezárta az oszmán hódoltságot?",
                "options": ["1699-ben.", "1686-ban.", "1703-ban."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki az időbeli azonnaliságot: „______ Buda felszabadult, a csapatok dél felé vonultak.”?",
                "options": ["Amint", "Habár", "Jóllehet"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-02.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A karlócai békeszerződés a Temesköz kivételével egész Magyarország területét a Habsburgok ____ alá helyezte. (authority / sovereignty: fennhatósága)",
                "answer": "fennhatósága"
            },
            {
                "id": "b1-torokkiuzese-02.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Miért hívták a korabeliek az 1687-es nagyharsányi győzelmet 'második mohácsi csatának'?",
                "options": [
                    "Mert közel Mohácshoz zajlott, és megsemmisítő elégtételt jelentett az 1526-os tragédiáért.",
                    "Mert ott is elhunyt egy király a folyóban.",
                    "Mert a törökök arattak győzelmet."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-02.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen országrész maradt még török kézen az 1699-es karlócai béke után rövid ideig?",
                "options": ["A Temesköz (Bánság).", "Buda vára.", "Egész Dunántúl."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt Savoyai Jenő herceg a törökellenes harcokban?",
                "options": [
                    "A kor egyik legzseniálisabb hadvezére, aki Zentánál és később Belgrádnál is legyőzte az oszmánokat.",
                    "A francia király nagykövete Konstantinápolyban.",
                    "A pozsonyi érsek."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-torokkiuzese-03",
        "exercises": [
            {
                "id": "b1-torokkiuzese-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["pusztulás", "devastation / ruin"],
                    ["elnéptelenedés", "depopulation"],
                    ["romváros", "ruined town"],
                    ["járvány", "epidemic / pestilence"]
                ]
            },
            {
                "id": "b1-torokkiuzese-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hadseregtartás", "quartering of troops"],
                    ["porció", "food tax for soldiers"],
                    ["forspont", "forced transport duty"],
                    ["anyagi teher", "financial burden"]
                ]
            },
            {
                "id": "b1-torokkiuzese-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen állapotban volt Magyarország jelentős része a 150 éves hódoltság és a felszabadító háborúk után?",
                "options": [
                    "Súlyosan elpusztult, falvak százai váltak lakatlanná, az Alföld pedig terméketlen pusztává.",
                    "Gazdag és modern ipari országgá vált.",
                    "Teljesen érintetlen maradt a háborútól."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-03.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt a 'porció' és a 'forspont' a császári katonai igazgatásban?",
                "options": [
                    "A porció a katonák kötelező élelmezési adója, a forspont pedig a katonai fuvarozási kényszermunka volt.",
                    "Két különböző katonai kitüntetés.",
                    "Külföldi zsoldosok fegyverzete."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti a kényszerűséget a mondatban: „A lakosság ______ elviselni a nehéz adókat.”?",
                "options": ["kénytelen volt", "szívesen akart", "mindig tudott"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-03.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felégett falvak jobbágyai kénytelenek ____ a császári sereg ellátását biztosítani. (were forced: voltak)",
                "answer": "voltak"
            },
            {
                "id": "b1-torokkiuzese-03.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen járvány pusztított a felszabadító hadjáratok kísérőjeként Magyarországon?",
                "options": [
                    "A pestis és a tífusz (a 'magyar láz').",
                    "A malária kizárólag a hegyekben.",
                    "Semmilyen betegség nem fordult elő."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-03.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan próbálta pótolni a bécsi udvar az elnéptelenedett déli és alföldi vidékek lakosságát?",
                "options": [
                    "Tervezett betelepítésekkel: német (sváb), szerb és szlovák telepeseket hívtak az országba.",
                    "Kizárólag külföldi katonák letelepítésével.",
                    "A városok teljes bezárásával."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért okozott csalódást a felszabadulás a magyar lakosságnak?",
                "options": [
                    "Mert a császári hadsereg fosztogatása és az elviselhetetlen hadiadók nem hoztak azonnali békés jólétet.",
                    "Mert vissza akarták hívni a törököket.",
                    "Mert nem engedték a templomok megnyitását."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-torokkiuzese-04",
        "exercises": [
            {
                "id": "b1-torokkiuzese-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Habsburg-uralom", "Habsburg rule"],
                    ["újszerzeményi bizottság", "Neoacquistica Commissio"],
                    ["fegyverváltság", "weapons ransom / fee"],
                    ["katonai megszállás", "military occupation"]
                ]
            },
            {
                "id": "b1-torokkiuzese-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemesi jogok sérelme", "infringement of noble rights"],
                    ["elégedetlenség", "discontent"],
                    ["örökös királyság", "hereditary monarchy (1687)"],
                    ["ellenállási jog", "right of resistance (repealed)"]
                ]
            },
            {
                "id": "b1-torokkiuzese-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt az 'Újszerzeményi Bizottság' (Neoacquistica Commissio) feladata?",
                "options": [
                    "A felszabadított magyar földek felülvizsgálata és a nemesektől fegyverváltság (10%) követelése birtokaik visszaadásáért.",
                    "Új templomok építése.",
                    "A határok felmérése."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-04.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miről mondtak le a magyar rendek az 1687-es pozsonyi országgyűlésen császári nyomásra?",
                "options": [
                    "A szabad királyválasztás jogáról (a Habsburg-ház fiágának örökösödését elismerve) és az Aranybulla ellenállási záradékáról.",
                    "A magyar nyelv használatáról.",
                    "Minden nemesi címről."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik megengedő kifejezés illik az ellentétre: „______ a török uralom véget ért, a nemzet nem kapott szabadságot.”?",
                "options": ["Noha", "Mert", "Minthogy"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar nemeseknek a birtok értékének tíz százalékát kellett kifizetniük ____ gyanánt. (weapon fee: fegyverváltság)",
                "answer": "fegyverváltság"
            },
            {
                "id": "b1-torokkiuzese-04.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hogyan tekintett I. Lipót császár és a bécsi udvar Magyarországra 1686 után?",
                "options": [
                    "Fegyverrel meghódított tartományként (fegyver jogán szerzett területként), korlátozva az alkotmányos önállóságot.",
                    "Egyenlő és független partnerországként.",
                    "Különálló semleges államként."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-04.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelentett az Aranybulla híres 'ellenállási záradéka' (31. cikkely), amelyet 1687-ben eltöröltek?",
                "options": [
                    "A nemesek jogát arra, hogy fegyveresen is ellenálljanak a törvényt szegő királlyal szemben a hűtlenség vétke nélkül.",
                    "Azt, hogy a király bárkit kivégezhet bírói ítélet nélkül.",
                    "A jobbágyok jogát a szabad költözésre."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen hangulat uralkodott Magyarországon a 17. század legvégén?",
                "options": [
                    "Általános elkeseredés és felháborodás a bécsi adók és az idegen katonaság elnyomása miatt.",
                    "Végtelen megelégedettség és hála a császárnak.",
                    "Teljes érdektelenség."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-torokkiuzese-05",
        "exercises": [
            {
                "id": "b1-torokkiuzese-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["kuruc", "Kuruc (rebel soldier)"],
                    ["bujdosó", "fugitive / outlaw rebel"],
                    ["II. Rákóczi Ferenc", "Ferenc Rákóczi II"],
                    ["szabadságharc", "war of independence"]
                ]
            },
            {
                "id": "b1-torokkiuzese-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemzeti összefogás", "national solidarity / unity"],
                    ["történelmi fordulat", "historic turning point"],
                    ["függetlenség", "independence"],
                    ["Thököly Imre", "Imre Thököly"]
                ]
            },
            {
                "id": "b1-torokkiuzese-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben tört ki a dicsőséges Rákóczi-szabadságharc a Habsburg uralom ellen?",
                "options": ["1703-ban.", "1686-ban.", "1848-ban."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-05.ex03",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki állt a kuruc mozgalom és a szabadságharc élére 1703-ban?",
                "options": ["II. Rákóczi Ferenc fejedelem.", "Kossuth Lajos.", "Petőfi Sándor."],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés utal az elkerülhetetlen történelmi eseményre: „A felkelés ______ vált a bécsi önkény miatt.”?",
                "options": ["elkerülhetetlenné", "lehetetlenné", "feleslegessé"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Rákóczi zászlajára a híres latin jelmondatot hímezték: „Cum Deo pro Patria et ____” (and Liberty: Libertate).",
                "answer": "Libertate"
            },
            {
                "id": "b1-torokkiuzese-05.ex06",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Kik voltak a 'kurucok' a magyar történelemben?",
                "options": [
                    "A Habsburg-ellenes nemzeti felkelések és szabadságharcok magyar harcosai.",
                    "A császár hűséges osztrák zsoldosai.",
                    "A török janicsárok."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-05.ex07",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mi tette II. Rákóczi Ferencet a nemzet vitathatatlan vezetőjévé?",
                "options": [
                    "Óriási vagyona, fejedelmi származása, tiszta erkölcsi jelleme és önzetlen hazaszeretete.",
                    "Mert ő volt a bécsi császár kedvence.",
                    "Mert külföldi király volt."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen történelmi korszak kezdődött a török kiűzését követő elégedetlenségből?",
                "options": [
                    "A 18. századi kuruc függetlenségi küzdelmek és a Rákóczi-szabadságharc nyolc éve (1703–1711).",
                    "A reformkor közvetlen kezdete.",
                    "Az első világháború."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-torokkiuzese-consolidation",
        "exercises": [
            {
                "id": "b1-torokkiuzese-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Szent Liga", "Holy League"],
                    ["Buda visszafoglalása", "liberation of Buda 1686"],
                    ["Lotaringiai Károly", "Charles of Lorraine"],
                    ["Petneházy Dávid", "Dávid Petneházy"]
                ]
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex02",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Nagyharsányi csata", "Battle of Nagyharsány"],
                    ["Zentai csata", "Battle of Zenta"],
                    ["Savoyai Jenő", "Prince Eugene of Savoy"],
                    ["karlócai béke", "Peace of Karlowitz 1699"]
                ]
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex03",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hadseregtartás", "quartering of army"],
                    ["porció", "food levy tax"],
                    ["forspont", "forced transport labor"],
                    ["elnéptelenedés", "depopulation"]
                ]
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex04",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["újszerzeményi bizottság", "Neoacquistica Commissio"],
                    ["fegyverváltság", "weapons fee (10%)"],
                    ["kuruc", "Kuruc rebel soldier"],
                    ["II. Rákóczi Ferenc", "Ferenc Rákóczi II"]
                ]
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex05",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben foglalták vissza Budát a szövetséges keresztény hadak?",
                "options": ["1686-ban (szeptember 2-án)", "1541-ben", "1526-ban", "1703-ban"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik békével zárult le végleg a 150 éves oszmán hódoltság korszaka 1699-ben?",
                "options": ["A karlócai békével", "A pozsonyi békével", "A tordai ediktummal", "A bécsi békével"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt a döntő 1697-es zentai csata szövetséges hadvezére?",
                "options": ["Savoyai Jenő", "Petneházy Dávid", "Zrínyi Miklós", "Dózsa György"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik évben állt II. Rákóczi Ferenc a magyar szabadságharc élére?",
                "options": ["1703-ban", "1686-ban", "1699-ben", "1711-ben"],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex09",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a célt és a következményt?",
                "options": [
                    "A Szent Liga serege azért ostromolta Budát, hogy kiűzze a törököket.",
                    "A Szent Liga serege azért ostromolta Budát, mert kiűzte a törököket volt.",
                    "A Szent Liga serege ezért ostromolta Budát ahová ment."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex10",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "1686. szeptember 2-án, 145 év oszmán uralom után végre felszabadult ____ vára. (Buda)",
                "answer": "Buda"
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex11",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A visszafoglalt birtokokért a nemeseknek tíz százalék fegyver____ kellett fizetniük. (ransom / fee: váltságot)",
                "answer": "váltságot"
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex12",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nép terhei miatt az újabb szabadságharc kirobbanása elkerülhetetlenné ____. (became: vált)",
                "answer": "vált"
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex13",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kuruc felkelők élére a brezáni kiáltvány után II. Rákóczi ____ lépett. (Ferenc)",
                "answer": "Ferenc"
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex14",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Hány évig tartott a török hódoltság Magyarországon (1541-től 1686/1699-ig)?",
                "options": [
                    "Körülbelül másfél évszázadig (150 évig).",
                    "Ötven évig.",
                    "Négyszáz évig.",
                    "Tíz évig."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex15",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mit jelentett a 'fegyverváltság' (jus armorum) intézménye a magyar birtokosok számára?",
                "options": [
                    "A nemeseknek a birtok becsértékének 10%-át be kellett fizetniük Bécsnek a fegyveres felszabadítás költségei címén.",
                    "Katonai fegyvereket kellett vásárolniuk a falusiaknak.",
                    "Minden fegyvert le kellett adniuk a rendőrségen.",
                    "Nem kellett semmit sem fizetniük."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex16",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Melyik két ősi alkotmányos jogról mondott le a magyar rendi országgyűlés 1687-ben?",
                "options": [
                    "A szabad királyválasztás jogáról és az Aranybulla fegyveres ellenállási záradékáról.",
                    "A borkészítés és a sóbányászat jogáról.",
                    "A magyar nyelv és az anyanyelvi oktatás jogáról.",
                    "A bírósági tárgyalások tartásáról."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex17",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Kik voltak a 'labancok' a kuruc korban?",
                "options": [
                    "A Habsburg császárhoz hű katonák és támogatók.",
                    "A török hódoltságban maradt kereskedők.",
                    "A lengyel szövetségesek.",
                    "A református diákok."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex18",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Mi volt Rákóczi fejedelem latin jelmondata a zászlókon?",
                "options": [
                    "„Cum Deo pro Patria et Libertate” (Istennel a hazáért és a szabadságért).",
                    "„Veni, vidi, vici”.",
                    "„Ora et labora”.",
                    "„Meghalt Mátyás, oda az igazság”."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex19",
                "type": "multiple-choice",
                "category": "civics",
                "question": "Milyen demográfiai változások történtek a török kor utáni betelepítések következtében?",
                "options": [
                    "Magyarország soknemzetiségű országgá vált a svábok, szlovákok, szerbek és románok betelepülése miatt.",
                    "Kizárólag magyarok éltek az egész Kárpát-medencében.",
                    "A lakosság teljesen kihalt.",
                    "Minden város lakossága azonnal francia lett."
                ],
                "correct": 0
            },
            {
                "id": "b1-torokkiuzese-consolidation.ex20",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen történelmi tanulságot hordoz Buda 1686-os visszafoglalása a magyar állampolgársági vizsgán?",
                "options": [
                    "Az európai keresztény összefogás és a nemzeti hősök önfeláldozása révén a nemzet képes volt feltámadni a legsúlyosabb hódoltság után is.",
                    "A diplomácia teljesen felesleges háborúban.",
                    "A várakat soha nem szabad megvédeni.",
                    "Csak a külföldi hadseregek számítanak."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-torokkiuzese-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.torokkiuzese-01",
        "title": "Buda visszavétele 1686-ban (The Siege of Buda)",
        "level": "B1",
        "grammar": "Purpose Clauses: azért, hogy + Subjunctive in Military Contexts",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can narrate the siege and liberation of Buda Castle on September 2, 1686.",
                    "I can identify Charles of Lorraine, Dávid Petneházy, and Abdurrahman Pasha.",
                    "I can formulate strategic intentions using purpose clauses (azért, hogy).",
                    "I can master eight new vocabulary items related to the siege and liberation."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-torokkiuzese-01-ostrom.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-torokkiuzese-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-torokkiuzese-01-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-torokkiuzese-01-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-01.ex01", "b1-torokkiuzese-01.ex01b", "b1-torokkiuzese-01.ex02", "b1-torokkiuzese-01.ex03",
                "b1-torokkiuzese-01.ex04", "b1-torokkiuzese-01.ex05", "b1-torokkiuzese-01.ex06", "b1-torokkiuzese-01.ex07", "b1-torokkiuzese-01.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the siege and liberation of Buda Castle on September 2, 1686.",
                    "I can identify Charles of Lorraine, Dávid Petneházy, and Abdurrahman Pasha.",
                    "I can formulate strategic intentions using purpose clauses (azért, hogy).",
                    "I can master eight new vocabulary items related to the siege and liberation."
                ]
            }
        ],
        "goal": [
            "I can narrate the siege and liberation of Buda Castle on September 2, 1686.",
            "I can identify Charles of Lorraine, Dávid Petneházy, and Abdurrahman Pasha.",
            "I can formulate strategic intentions using purpose clauses (azért, hogy).",
            "I can master eight new vocabulary items related to the siege and liberation."
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.torokkiuzese-02",
        "title": "A felszabadító hadjáratok (The Reconquest Campaigns)",
        "level": "B1",
        "grammar": "Temporal Sequences in Warfare: amint, mihelyt, azt követően, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the battles of Nagyharsány (1687) and Zenta (1697).",
                    "I can explain the terms of the 1699 Peace of Karlowitz ending Ottoman occupation.",
                    "I can connect military victories in sequence using amint and azt követően, hogy...",
                    "I can deploy eight new vocabulary items concerning campaigns and peace treaties."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-torokkiuzese-02-karloca.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-torokkiuzese-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-torokkiuzese-02-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-torokkiuzese-02-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-02.ex01", "b1-torokkiuzese-02.ex01b", "b1-torokkiuzese-02.ex02", "b1-torokkiuzese-02.ex03",
                "b1-torokkiuzese-02.ex04", "b1-torokkiuzese-02.ex05", "b1-torokkiuzese-02.ex06", "b1-torokkiuzese-02.ex07", "b1-torokkiuzese-02.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the battles of Nagyharsány (1687) and Zenta (1697).",
                    "I can explain the terms of the 1699 Peace of Karlowitz ending Ottoman occupation.",
                    "I can connect military victories in sequence using amint and azt követően, hogy...",
                    "I can deploy eight new vocabulary items concerning campaigns and peace treaties."
                ]
            }
        ],
        "goal": [
            "I can describe the battles of Nagyharsány (1687) and Zenta (1697).",
            "I can explain the terms of the 1699 Peace of Karlowitz ending Ottoman occupation.",
            "I can connect military victories in sequence using amint and azt követően, hogy...",
            "I can deploy eight new vocabulary items concerning campaigns and peace treaties."
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.torokkiuzese-03",
        "title": "A felszabadulás ára (The Cost of Liberation)",
        "level": "B1",
        "grammar": "Inevitable Hardship: kénytelen volt / kénytelenek voltak",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the devastation, scorched earth, and depopulation following the wars.",
                    "I can explain military exactions such as porció (food levy) and forspont (forced transport).",
                    "I can use kénytelen volt to express unavoidable civilian hardship.",
                    "I can use eight new vocabulary items related to wartime destruction and taxation."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-torokkiuzese-03-ara.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-torokkiuzese-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-torokkiuzese-03-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-torokkiuzese-03-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-03.ex01", "b1-torokkiuzese-03.ex01b", "b1-torokkiuzese-03.ex02", "b1-torokkiuzese-03.ex03",
                "b1-torokkiuzese-03.ex04", "b1-torokkiuzese-03.ex05", "b1-torokkiuzese-03.ex06", "b1-torokkiuzese-03.ex07", "b1-torokkiuzese-03.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can describe the devastation, scorched earth, and depopulation following the wars.",
                    "I can explain military exactions such as porció (food levy) and forspont (forced transport).",
                    "I can use kénytelen volt to express unavoidable civilian hardship.",
                    "I can use eight new vocabulary items related to wartime destruction and taxation."
                ]
            }
        ],
        "goal": [
            "I can describe the devastation, scorched earth, and depopulation following the wars.",
            "I can explain military exactions such as porció (food levy) and forspont (forced transport).",
            "I can use kénytelen volt to express unavoidable civilian hardship.",
            "I can use eight new vocabulary items related to wartime destruction and taxation."
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.torokkiuzese-04",
        "title": "Új uralkodó, régi sérelmek (New Rulers, Old Grievances)",
        "level": "B1",
        "grammar": "Concession & Discontent: noha, annak dacára, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can outline imperial absolutism under Leopold I and the Neoacquistica Commission.",
                    "I can explain weapons ransom (fegyverváltság) and the Diet of 1687.",
                    "I can construct sentences expressing political disillusionment using noha and annak dacára, hogy...",
                    "I can use eight new vocabulary items concerning constitutional grievances."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-torokkiuzese-04-serelmek.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-torokkiuzese-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-torokkiuzese-04-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-torokkiuzese-04-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-04.ex01", "b1-torokkiuzese-04.ex01b", "b1-torokkiuzese-04.ex02", "b1-torokkiuzese-04.ex03",
                "b1-torokkiuzese-04.ex04", "b1-torokkiuzese-04.ex05", "b1-torokkiuzese-04.ex06", "b1-torokkiuzese-04.ex07", "b1-torokkiuzese-04.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can outline imperial absolutism under Leopold I and the Neoacquistica Commission.",
                    "I can explain weapons ransom (fegyverváltság) and the Diet of 1687.",
                    "I can construct sentences expressing political disillusionment using noha and annak dacára, hogy...",
                    "I can use eight new vocabulary items concerning constitutional grievances."
                ]
            }
        ],
        "goal": [
            "I can outline imperial absolutism under Leopold I and the Neoacquistica Commission.",
            "I can explain weapons ransom (fegyverváltság) and the Diet of 1687.",
            "I can construct sentences expressing political disillusionment using noha and annak dacára, hogy...",
            "I can use eight new vocabulary items concerning constitutional grievances."
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.torokkiuzese-05",
        "title": "A szabadságharc felé (Toward the War of Independence)",
        "level": "B1",
        "grammar": "Anticipating Conflict: elkerülhetetlenné vált, utat nyitott",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain how Kuruc resistance coalesced into a nationwide movement.",
                    "I can identify Prince Ferenc Rákóczi II and the 1703 Brezán proclamation.",
                    "I can foreshadow historic turning points using elkerülhetetlenné vált.",
                    "I can pass citizenship exam questions regarding the end of the Ottoman era and Rákóczi's rise."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b1/b1-torokkiuzese-05-szabadsagharc.json"},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-torokkiuzese-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-torokkiuzese-05-gr.json"},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-torokkiuzese-05-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-05.ex01", "b1-torokkiuzese-05.ex01b", "b1-torokkiuzese-05.ex02", "b1-torokkiuzese-05.ex03",
                "b1-torokkiuzese-05.ex04", "b1-torokkiuzese-05.ex05", "b1-torokkiuzese-05.ex06", "b1-torokkiuzese-05.ex07", "b1-torokkiuzese-05.ex08"
            ]},
            {"type": "srs"},
            {
                "type": "checklist",
                "items": [
                    "I can explain how Kuruc resistance coalesced into a nationwide movement.",
                    "I can identify Prince Ferenc Rákóczi II and the 1703 Brezán proclamation.",
                    "I can foreshadow historic turning points using elkerülhetetlenné vált.",
                    "I can pass citizenship exam questions regarding the end of the Ottoman era and Rákóczi's rise."
                ]
            }
        ],
        "goal": [
            "I can explain how Kuruc resistance coalesced into a nationwide movement.",
            "I can identify Prince Ferenc Rákóczi II and the 1703 Brezán proclamation.",
            "I can foreshadow historic turning points using elkerülhetetlenné vált.",
            "I can pass citizenship exam questions regarding the end of the Ottoman era and Rákóczi's rise."
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.torokkiuzese-consolidation",
        "title": "Unit 12 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can narrate the 1686 reconquest of Buda, battles of Nagyharsány and Zenta, and the 1699 Peace of Karlowitz.",
                    "I can discuss the post-war devastation, porció/forspont burdens, and noble grievances under Leopold I.",
                    "I can explain the rise of the Kuruc movement and the outbreak of the Rákóczi War of Independence (1703).",
                    "I can answer all citizenship interview questions on the liberation of Hungary with complete precision."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b1/b1-torokkiuzese-consolidation-ex.json", "exerciseRefs": [
                "b1-torokkiuzese-consolidation.ex01", "b1-torokkiuzese-consolidation.ex02", "b1-torokkiuzese-consolidation.ex03", "b1-torokkiuzese-consolidation.ex04",
                "b1-torokkiuzese-consolidation.ex05", "b1-torokkiuzese-consolidation.ex06", "b1-torokkiuzese-consolidation.ex07", "b1-torokkiuzese-consolidation.ex08",
                "b1-torokkiuzese-consolidation.ex09", "b1-torokkiuzese-consolidation.ex10", "b1-torokkiuzese-consolidation.ex11", "b1-torokkiuzese-consolidation.ex12",
                "b1-torokkiuzese-consolidation.ex13", "b1-torokkiuzese-consolidation.ex14", "b1-torokkiuzese-consolidation.ex15", "b1-torokkiuzese-consolidation.ex16",
                "b1-torokkiuzese-consolidation.ex17", "b1-torokkiuzese-consolidation.ex18", "b1-torokkiuzese-consolidation.ex19", "b1-torokkiuzese-consolidation.ex20"
            ]},
            {
                "type": "checklist",
                "items": [
                    "I can narrate the 1686 reconquest of Buda, battles of Nagyharsány and Zenta, and the 1699 Peace of Karlowitz.",
                    "I can discuss the post-war devastation, porció/forspont burdens, and noble grievances under Leopold I.",
                    "I can explain the rise of the Kuruc movement and the outbreak of the Rákóczi War of Independence (1703).",
                    "I can answer all citizenship interview questions on the liberation of Hungary with complete precision."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-torokkiuzese-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_12_citizenship()
    print("Successfully built Hungarian B1 Citizenship Unit 12 (b1-torokkiuzese)!")
