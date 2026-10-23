# hu b1 problems-solutions (B1 Unit 39) review

check-content: 0 errors, 0 suspects. unmet-words: ~110 hits. Fixes: 54 in fixes-problems-solutions.json (50 sure, 4 unsure), 6 challenges in challenges-problems-solutions.json.

## 1. Found by reading
- b1-20-01.ex04 drills *kellett volna lennünk* ("Sokkal körültekintőbbnek kellett ____ lennünk ...", tagged `kellett-volna`) in lesson 1, but `kellett-volna` is taught in b1-20-02-a; also "körültekintőbbnek", "meghozatalakor" unmet. Fix: "Ha tudtam ____, időben szóltam volna." (hint "if I had", tag `past-conditional-volna`).
- b1-20-01.ex02, 02.ex02, 03.ex02, 04.ex02, 05.ex02: "(Lesson N)" English in the Hungarian stem; both wrong options are garbled non-sentences with several faults ("Ha szólni időben ezért nem hiba van volt.") or two faults ("megbeszélnénk volna ... elkerüljük volna"); several use unmet words (elhárítottuk, újabb, hamarabb). Fix: "Melyik mondat helyes?" with one real fault each (*szólnál volna*, conditional for past, `distractor_skills` {"1": "nek-conditional"}; *volt* for *volna*).
- b1-20-consolidation.ex02: wrong options "Jobb volt ha megbeszélni volt kezdettől a kétségeket volna." and "Kellett volna hogy megbeszélni lett kétség nélkül." are junk; fix: *Jobb lenne volna* (ds `irregular-nek-conditional`) and *Jobb lett volt*.
- b1-20-01.ex03 "megtaláltuk a helyes ____" unmet (megtaláltuk, helyes) and answers with L3 vocabulary; fix: "Néha mindenki követ el ____." (hint "mistake", hibát).
- b1-20-01.ex05 unmet (tévedést, megpróbáljuk, hárítjuk, felmondunk); wrong option "Azonnal felmondunk ... szó nélkül." absurd; rewritten ("Mit jelent a következmény?").
- b1-20-01.ex06 "magyarázatára" unmet; fix "... a tanácsra!".
- b1-20-01.ex07 builder "A hibákból levont tanulság segít a jövőbeli helyes döntésekben." unmet (levont, jövőbeli, helyes) and english "Build the sentence in the correct order." is no translation; fix "Minden hibának van következménye."
- b1-20-01.ex08 "Miért fontos a konstruktív hozzáállás ..." unmet (hibáztatás, megakadályozza, automatikusan ...), absurd wrong options, no text; all six ex08 are generic or story questions with unmet words; rewritten as story questions: where the student goes, what is in his pocket, what the father says, who waits at home, what he promises, how he explains the grade (answerable from the story).
- b1-20-02.ex04 "Hamarabb meg kellett ____ előznünk" (előznünk unmet); fix "Időben el kellett ____ indulnotok." (the screen's own phrase).
- b1-20-02.ex05 unmet (következzen, utólag, elrejtsük, büntessünk); rewritten.
- b1-20-02.ex07 "beismerése" unmet; fix "... őszinte megbeszélése."
- b1-20-02.ex08, 03.ex08, 04.ex08, 05.ex08 "Mit jelent az, hogy ..." wrong options plainly absurd ("Soha senki nem használja."); replaced by story questions (see above).
- b1-20-03-a screen: example "A nehézségek ellenére sikerült időben befejezni a munkát." uses the postposition *ellenére* (`concessive-postpositions`, Unit 57) and is the speaking prompt; fix: "Bár nagyok voltak a nehézségek, sikerült időben befejezni a munkát."
- b1-20-03.ex03 "leküzdötte" unmet; fix "A csapat végül megoldotta a legnagyobb ____."
- b1-20-03.ex05 unmet (kikerülhetünk, megállít); rewritten.
- b1-20-03.ex06, ex07 "elhárítottuk", "megtalálnunk" unmet; fixes "Ha időben láttam ____ az akadályt, ..." and "Végül sikerült megoldanunk a nehézséget."
- b1-20-04.ex05 unmet (megvizsgáljuk, okolunk, eltitkoljuk); rewritten. ex07 "elkerülésében" unmet; fix "... sokat segít."
- b1-20-05.ex03 "igazgató" unmet; ex04 "fontolnunk" unmet; ex05 unmet (kitűzött, valósul ...); ex06 "hamarabb végeztünk" unmet; all rewritten with met words.
- b1-20-consolidation.ex03 hint "proposal -át" names the ending and "szakmai", "bizottság" unmet; fix "A főnök elfogadta a csapat ____." (hint "proposal").
- b1-20-consolidation.ex05 "pozitív" unmet; fix "jó"; english was generic, now a translation.
- b1-20-consolidation.ex06 unmet and "megfellebbezhetetlen" is a -hetetlen form (Unit 59); rewritten ("Egy másik megoldás.").
- b1-20-consolidation.ex07 "tapasztalt", "vállal" unmet (answer itself unmet); fix: "Egy hiba után fontos a ____." (felelősségvállalás).
- b1-20-consolidation.ex08 unmet (logikával, bevallja, eltépi ...) and calls the adaptation "a klasszikus novellában"; rewritten.
- b1-20-01-b screen: example 2 "Kár, hogy nem hallgattunk a szakértő tanácsára." is a plain past with *kár, hogy*, not *bárcsak ... volna* as the rule says; fix: "Bárcsak hallgattunk volna a szakértő tanácsára!" and recap "You know bárcsak from Unit 5".
- b1-20-05-a screen presents *hogy* + subjunctive (Unit 5) as new; fix: recap sentence. (No item practises *azt javaslom, hogy ...*.)

## 2. Metadata
- b1-20-01.ex04 retagged `kellett-volna` -> `past-conditional-volna` (see above); new distractor_skills on the five lesson ex02 and consolidation ex02 (`nek-conditional` on *szólnál/megbeszélnénk/megoldanánk/tanulnánk/javasolnánk volna*, `irregular-nek-conditional` on *lenne volna*). Run lock_tags --update after applying.
- Reading items carry no `teaches` (correct); after the rewrite all ex08 stay `reading`.

## 3. Goals / checklists
- Lines 2-4 of every lesson are shared ("I can form past conditional sentences using volna in Hungarian.", "I can talk about mistakes, regrets, lessons learned, and solutions.", "I can master four new target vocabulary items in authentic context."); line 1 is "I can understand and use vocabulary for if it had happened differently / what should have been done ..." (ungrammatical pattern); line 4 is not a can-do. Lessons 3-5 practise no past conditional teaching of their own (L3 sikerült, L4 reflection, L5 proposals). Rewritten per lesson (3 lines each, only what the lesson practises) in both `goal` and the goal screen.

## 4. Doubtful
- Past conditional *ha ... volna* and *ha ... akkor ... volna* are already taught in Unit 26 (b1-rakoczi-01, b1-rakoczi-02), while `past-conditional-volna` has `taught_in` b1-20-01-a: lesson 1 presents it as new. Recap fix added (unsure); the real fix may be the skill's taught_in/level. (unsure)
- Skill `kellett-volna` is titled "kellett volna and lehetett volna"; no screen shows *lehetett volna*. (unsure)
- b1-20-02-b "Jobb lett volna, ha azonnal szólunk." (ha + present after *lett volna*) is acceptable colloquial Hungarian but is not the past conditional the unit teaches; the consolidation key option uses the same pattern. (unsure)
- Story b1-20-karinthy: *gesztikulálva* (-va/-ve, Unit 57), *kérlelhetetlen* and *elkerülhetetlen* (-hetetlen, Unit 59), *tapinthatóvá*, *mentegetőző*; three unsure fixes written. (unsure)
- Reading items ex08 of lessons 1-5 ask about a story the learner reads only in the consolidation lesson.
- The lesson ex02 is the same item five times (one verb phrase swapped); the five lessons mostly list phrases, not rules (L2-b, L3-b, L4-a, L4-b, L5-b).

## 5. Dictionary
diáksapkáját | diáksapka | noun | school cap, student's cap |
feküdt | fekszik | verb | to lie, to be lying down (nem feküdt neki: did not suit him) |
gesztikulálva | gesztikulál | verb | to gesticulate |
gimnazistának | gimnazista | noun | secondary-school student |
kapucsengőt | kapucsengő | noun | doorbell at the gate, entry buzzer |
keresztüldöfi | keresztüldöf | verb | to pierce through, to stab through |
mentegetőző | mentegetőző | adj | apologetic, making excuses |
orrcsiptetőjét | orrcsiptető | noun | pince-nez |
plüssfüggönyökkel | plüssfüggöny | noun | plush curtain |
kalaposbolt | kalaposbolt | noun | hat shop, milliner's |
leghátsó | leghátsó | adj | rearmost, furthest back |
sötétlett | sötétlik | verb | to show dark, to loom dark |
vészhelyzet | vészhelyzet | noun | emergency |

Fix count: 54 (50 sure, 4 unsure); challenges 6.
