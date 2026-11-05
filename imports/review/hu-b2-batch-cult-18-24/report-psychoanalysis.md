# Reader B report: hu b2 psychoanalysis (Unit 22, culture track)

Files: fixes-psychoanalysis.json (76 fixes), challenges-psychoanalysis.json (6), facts-psychoanalysis.md. Commands run: check-content (15 errors, all addressed below), render_lesson, unmet-words, audit-reader-coverage for five stories.

## 1. Found by reading
- story 01 par.1 "nem elégedett meg azzal, hogy lefordítsa Freud műveit": unsupported; rewritten as a plain founding statement (check).
- story 01 par.2 "az értelmiség azonnal nyitottan fordult": overstated (medical establishment resisted); hedged "egy része már korán".
- story 01 par.3 "világossá vált, hogy ... nem idegi gyengeségből": contested clinical view as settled; now "egyre többen úgy látták". 01.ex08 credited Ferenczi and said "jellemgyengeség" (not in story): fixed.
- story 01 par.4 "a világon elsőként ... tanszék": priority claim hedged "a források szerint".
- story 01 par.5 "csak akkor javul ... Ez a felismerés alapozta meg": overstated cause; softened.
- story 02 par.1 "a pszichoanalízis nem zárt orvosi rendelőben született meg, hanem a ... kávéház márványasztalainál": false (born in Vienna); rewritten. "alapító tagja" (Ignotus) reduced to "tagja" (check). "minden héten együtt vacsorázott" is an anecdote: hedged "a hagyomány szerint gyakran".
- story 02 par.2 "mesteri ábrázolására" (unhedged judgement) -> "a kritikusok szerint". Par.4 "felismerték, hogy" mind-reading -> "tanulhattak"; par.5 single-cause claim softened.
- story 03 par.1 "kimutatták" -> "úgy látták"; "legfontosabb újítása" -> "egyik legfontosabb". Par.2 implied Bálint went to the Tavistock at once (he joined c.1948, check): fixed. Par.4: 03.ex03 asks "londoni háziorvosok" but the story never said the groups were for GPs: added. Par.5 "egyenes út ... bebizonyította ... mindig": overstated (attachment theory is Bowlby's); softened.
- story 04: "1949 elején" (month unverified), "a folyóiratokat betiltották" (unverified), "budai lakásán esténként" (unverified), "a legkorszerűbb ... folyamatosan gazdagodott", "megdöbbenve ... semmit sem veszített" (mind-reading, absolute), "konferenciák nyíltak meg" (unnatural): all fixed. "titkos szemináriumok" kept (check).
- story 05: "magyar pszichológus" -> "magyar származású"; "A kutatások igazolták" -> "Csíkszentmihályi szerint"; the 1990 book is the English Flow, not "Flow — Az áramlat" (Hungarian title, later); "alapkövévé" -> "egyik alapkövévé"; closing link to the Budapest school hedged.
- lesson 02 title and vocabulary title "Café Ignotus": no such café (Ignotus was the editor; the cafés were the New York and the Centrál). Fixed in lesson, voc and story metadata. The combined reading, manifest.json and curriculum.json carry the old title (rebuilt).
- lesson 01 intro: "Freud declared that Budapest was poised to become the capital of psychoanalysis" (unconfirmed quotation paraphrase, removed); "his literary patients (Kosztolányi, Karinthy, Csáth, Attila József)": wrong (József's analyst was Gyömrői).
- grammar 02: "kritikus -> kritizál / akadékoskodik, titok -> titkolózik" are not -kodik/-kedik/-ködik formations: replaced by hős -> hősködik, gyerek -> gyerekeskedik.
- grammar 04: "Unlike English or German" breaks the English-only comparison rule.
- grammar 05: "órákra elmélyül" -> "órákig" (unsure).
- 04.ex08: wrong options imported the Nemzeti Színház and the Rubik cube (later units, absurd); the story never says the community "celebrated" an anniversary: question and options rewritten.
- consolidation.ex03: wrong options Rátz László, Kempelen Farkas, Jedlik Ányos name people of later units: replaced by Bálint, Hermann, Csíkszentmihályi.
- Wrong options with two faults or garbled: 01.ex07 (3rd), consolidation.ex02 (3rd, 4th), ex09 (3rd): one fault each now. 04.ex04 "újjászervezett" is a grammatical transitive past (unsure): replaced by "újjászervezték".
- Glued blanks in multiple-choice stems: 02.ex04 (ábrázolásá_____), 05.ex04 (zené_____ / dallamok_____): whole-word options. No glued fill-blank found.
- check-content errors: length-giveaway 01.ex02/ex08, 02.ex02/ex08, 03.ex02/ex08, 04.ex02, 05.ex08; tell-absolute 01.ex08 (semmi), 02.ex02 (Kizárólag), 03.ex02 (soha), 04.ex02 (Teljesen), 05.ex08 (Kizárólag); hint-is-answer 03.ex05, 05.ex05: all rewritten.
- Recaps: grammar 01 and 04 present the A2 Unit 31 mediopassive as new: recap added. Grammar 02 and 03 present known government (-val A2 Unit 5, -ra B1 Unit 3, -hoz B1 Unit 9, -ba A1 Unit 12): recap added (unit numbers from the knowledge sheet).
- Unmet words: 39 culture words appended to the vocabulary lists of the first lessons using them (01: 10, 02: 5, 03: 9, 04: 6, 05: 21 incl. the consolidation's *munkásság, fejleszt, ítélkezés, analitikus, tevékenység, értelmes*, since the consolidation has no list). *tárulnak* (ex05) is the split prefix of listed *feltárul*: not added.

## 2. Metadata
- 02.ex04 teaches mediopassive but tests -ra/-re government of vállalkozik: -> verb-government-ra-re (unsure). 02.ex05 (past of szembenéz) -> past-tense-indefinite; 02.ex06 -> verb-government-val-vel; 02.ex07 -> verb-government-ra-re (all unsure).
- 03.ex05, 05.ex05: the blank supplies the verb; retagged vocabulary (category vocabulary).
- 03.ex04 and 05.ex04 test case government with bele-/-ba and -ban but carry mediopassive-verbs-odik; no existing skill fits -ba/-be government (movement-with-ba-be is motion): left, reported.
- 03.ex06 (Az orvosnak képesnek kell lennie ...) tests an inflected infinitive/dative; left.
- Items ex02 and ex08 of every lesson are story-fact questions; ex02 is tagged vocabulary (category vocabulary), ex08 reading. Left (unsure).
- Lesson file `unit: 11` and story `grammar: ["b2-reflexive-middle"]` do not match the registry (Unit 22; skill b2-reflexive-middle does not exist in skills/hu.json). Not edited.

## 3. Goals / checklists
- 02 goal 2: onmarcangol, megnyílik were never taught: replaced by szembenéz, foglalkozik, vállalkozik, megnyilatkozik. 02 goal 3 ("analyze literary self-reflection") -> plain can-do.
- 03 goal 1: "trauma theory ... revolutionized clinical medicine" -> plain can-do (also first checklist line, and the challenge canDo copies it). 03 goal 2: együttérez never practised -> viszonyul valakihez.
- 04 goal 3: Lucy Liebermann / Lilly Hajdu / György Vikár ("Lilly Hajdu" is nowhere in the story) -> plain can-do.
- Each goal line is fixed in the goal key, the goal screen and the checklist (3 fixes per line).

## 4. Doubtful
- Unit 22 teaches no new grammar of its own ("Grammar this unit teaches" is empty). Lesson 01 and 04 re-present A2 Unit 31 mediopassive (recap added). Lesson 04's "passive-like middle verbs to narrate without naming the doer" overlaps B2 Unit 29 `agentless-constructions` (later): unsure.
- *megörökítődik* / *örökítődött meg* (story 01, grammar 01 table and examples) is rare and clumsy; *fenn maradt* is natural. Not changed (screens teach it).
- Facts to verify: see facts-psychoanalysis.md (Academy venue 1918, Ignotus membership, "first chair in the world" 1919, 1949 date, Hermann circle names, Liebermann Lucy, 1993 events, Tavistock 1948).
- Present-day: Csíkszentmihályi died in 2021; the story uses the past tense (ok). Magyar Pszichoanalitikai Egyesület name today: check.
- Consolidation has no vocabulary file (see group 1).

## 5. Dictionary
ezerkétszáz | ezerkétszáz | number | one thousand two hundred |
feldolgozatlan | feldolgozatlan | adjective | unprocessed / not worked through |
örökítődött | örökítődik | verb | to be handed down / recorded for posterity |
álomfejtés | álomfejtés | noun | dream interpretation |
naplószerű | naplószerű | adjective | diary-like |
novellista | novellista | noun | short-story writer |
paródiáiban | paródia | noun | parody |
belehelyezkedni | belehelyezkedik | verb | to put oneself into (someone's position) |
csoporttagok | csoporttag | noun | group member |
hangolódva | hangolódik | verb | to attune oneself |
kötődéselméletig | kötődéselmélet | noun | attachment theory |
térnyerése | térnyerés | noun | gaining ground / spread |
gyermekpszichológiai | gyermekpszichológiai | adjective | child-psychological |
hazalátogató | hazalátogat | verb | to visit home |
mélylélektan | mélylélektan | noun | depth psychology |
százhuszadik | százhuszadik | number | one hundred and twentieth |
kiképző | kiképző | adjective | training (adj.) |
lakásszemináriumokban | lakásszeminárium | noun | apartment seminar |
magánlakások | magánlakás | noun | private flat |
megőrződött | megőrződik | verb | to be preserved |
újjászerveződött | újjászerveződik | verb | to be reorganised |
időérzék | időérzék | noun | sense of time |
áramlatélménynek | áramlatélmény | noun | flow experience |
belefeledkezik | belefeledkezik | verb | to lose oneself in |
teljesedik | teljesedik | verb | to be fulfilled |
tudatállapotot | tudatállapot | noun | state of consciousness |
vízfolyás | vízfolyás | noun | watercourse / stream |
zenetanárok | zenetanár | noun | music teacher |

Fix count: 76 fixes (fixes-psychoanalysis.json), 6 challenges.
