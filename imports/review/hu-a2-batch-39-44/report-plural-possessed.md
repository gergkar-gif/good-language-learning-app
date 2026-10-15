# Review report: hu A2 units 39, 40, 41 (plural-possessed, inflected-postpositions, inflected-infinitives-necessity)

Files written (only these): fixes-plural-possessed.json (72 fixes), fixes-inflected-postpositions.json (70), fixes-inflected-infinitives-necessity.json (58); challenges-plural-possessed.json, challenges-inflected-postpositions.json, challenges-inflected-infinitives-necessity.json (6 each); this report. All in /home/user/parlour-read-a/. Each fix list passes `python scripts/check_fixes.py hu a2 <unit> <fixes>`: 0 rejected, every check-content ERROR (4 + 1 + 2) is fixed, no new finding except the vocab-unused notes named per unit. Nothing was applied to the content (the checker restores files; I deleted its .auto/.review output). Fix `why` fields explain each fix; `kind: hungarian` marks changed Hungarian, `sure: false` the unsure ones.

Unit knowledge-sheet checks: unit 39 anaphoric -é only in a2-195 (OK); unit 40 inflected postpositions only from a2-196 on, except *számunkra* in a2-193 (reported); unit 41 sheet lists nothing new, so everything is recap except the plural inflected infinitives (reported).

# UNIT 39: plural-possessed (a2-191 .. a2-195-consolidation, story a2-unit-39)

Fixes: `/home/user/parlour-read-a/fixes-plural-possessed.json` (72 fixes, validated with scripts/check_fixes.py: 0 rejected, no new check-content findings except vocab-unused a2-195 *elindul*, which the controlled-1 rewrite leaves unused). Challenges: `/home/user/parlour-read-a/challenges-plural-possessed.json` (6).

## 1. Found by reading
**Recap / new-vs-known**
- a2-191-a (grammar): the unit opens with "When you possess multiple items, Hungarian uses a special plural possession suffix..." with no "You know szülei, testvérei from Unit 13". Fixed: recap sentence added, other persons presented as new.
- a2-191-a: "-jaim / -jeim after certain vowels and consonants" is wrong (j-forms come after consonants: céljaim; after a vowel it is just -im: cipőim, ruháim); cipő -> cipőim is listed under -aim/-eim. Fixed. "dolog -> dolgaim (my things / chores)": "chores" is wrong; fixed (also 192-a "dolgod (your chore)").
- a2-191-b: "short vowel undergo regular vowel lengthening or dropping" is vague and contradicts cipő/szülő (long vowels); "fleeting-vowel" mis-describes szülő -> szüleim. Fixed.
- a2-192-b: the 3rd person -ai/-ei (szülei, testvérei) is known from a2-13 but presented as new, no recap. Fixed (recap sentence).
- a2-195-a: "accusative case (-at/-et/-ot/t)": there is no -ot here, -t only after -ai/-ei; the accusative on possessed nouns is known (acc-poss a2-14-a, and 191-practice-4, 191-dialogue-2, 192-practice-4 already drill it before this screen). Fixed: recap + correct rule.
- a2-195-b is a grammar screen titled "Communicative Checklist: 'Minden megvan?'" (lesson 195 therefore has 4 grammar screens, rule is two): rename/move to a tip (not fixed, structural).
- a2-195-consolidation: the unit teaches anaphoric -é (195-c) but the consolidation has no -é item and its goal/checklist omit it (not fixed: needs a new item; suggest swapping consolidation-13 or -14 for a Péteré/szomszédoké item).
**Used before taught**
- a2-193-practice-1 (builder): *számunkra* is an inflected postposition (a2-196) used before its screen. Fix: *nekünk*.
**Unmet words / forms (fixed with met words)**
- a2-192-writing-2 *élnek* (b1) -> *laknak*; a2-192-practice-4 *partin*; a2-193-controlled-1 *örülünk, megvalósulnak*; -controlled-2 *nyissátok, negyvenedik, oldalon*; -practice-2 *virágok*; -practice-4 *felejtjük, tanácsokat*; -dialogue-1 *hétvégi*; -dialogue-2 *füzeteket/füzeteink*; -writing-1 *hagyomány, külföldi, vendég, legszebb*; -writing-2 *támogatják, álmainkat*; -check-1 *kint*; -check-2 *megkérdeztük, benyomásaikról, turistákat*; a2-194-controlled-2 *házassági, évfordulójukra*; -dialogue-1 *tengerpartra, egyetemi*; -writing-1 *számíthatok, hűséges*; -writing-2 *karácsonyt*; -check-1 *beszélgetek*; -check-2 *látogatok*; a2-195-controlled-1 *mielőtt, ellenőrzöm*; -controlled-2 *hagyd, vonatfülke*; -practice-2 *ahol*; -practice-4 *felejtettem*; -dialogue-2 *nyaralás, béreltünk*; -writing-1 *mielőtt, elhagyom, szállodai, átnézem, felejtsem*; -writing-2 *személyes*; -check-1 *bemásolom/beteszem/berakom*; -check-2 *recepcióján, bemutattuk*; consolidation-7 *vidéken* (the speaking step repeats it, auto-follows); -8 *megkérdezted*; -9 *professzor, hallgatók*; -11 *pakoltam*; -12 *örültek*; -15 *ellenőrzöm*; -16 *köszöntelek* (köszönt is not met) and *szeretettel*; -18 *gondosan*; -20 *felejtem*.
**Exercise defects**
- a2-191-check-1 ERROR length (36 vs 23): shortened right option. a2-192-check-1 ERROR (55 vs 39): shortened. a2-193-controlled-4 ERROR (36 vs 24): shortened. a2-195-consolidation-2 ERROR (46 vs 25): shortened.
- a2-191-check-2: "Az új sport____" blank glued to a stem. Fixed (whole word *cipőim*).
- a2-195-dialogue-1: "repülő____" blank glued to a stem. Fixed.
- a2-191-dialogue-1: wrong option *barátunk* fails person AND number (Kik jönnek...?). -> *barátom* (number only).
- a2-192-controlled-2: "János nagyon elfoglalt, sokak a kérdései az új projekttel kapcsolatban" is not Hungarian. Rewritten.
- a2-192-dialogue-1: wrong options *dolgaid/dolgai* each fail person + missing -t. -> *dolgaim* / *dolgaidat*.
- a2-194-intro-1: *barátaivel* fails person + harmony. -> *barátaimmel*. a2-194-controlled-4: *barátaidval* (person + assimilation), *barátaivalvel* (double suffix) -> *barátaiddal*, *barátaimmal*.
- a2-195-intro-2: *holmi* is a collective singular noun (*a holmimat* is the natural "my belongings"), so "holmijaimat" as the single right answer is dubious and *a holmim* fails two things. Rewritten with *ruháimat*.
- a2-195-check-1: *Bemásolom a ruháimat* is wrong by meaning alone, plus unmet verbs. Rewritten, one fault each.
- a2-195-consolidation-11: "Hová tetted..." answered by "A hálószobában pakoltam ki"; every wrong option also lacked -t (two faults) and `distractor_skills` {"2"} must go with the changed option. Rewritten, ds removed.
- a2-195-consolidation-12: reply answers differently (örültek unmet). Rewritten.
- a2-195-dialogue-2: reply did not answer "Kivel fogsz lakni" sensibly (béreltünk...). Rewritten.
- hint word "sublative" (a2-194-practice-4, a2-194-writing-1, consolidation-9, -10) is not a term the course teaches: replaced by "-ra/-re".
**Story**
- a2-unit-39: narration "végigtapogatta az összes zsebét ... nem találta a kulcsokat" contradicts the keys being in "a kabátom másik zsebében" (unsure; fix: "a nadrágzsebeit").

## 2. Metadata
- a2-193-writing-2 `teaches` acc-poss -> plural-possessive (after the rewrite the tested form is *szüleink*, no accusative).
- a2-195-consolidation-11: remove `distractor_skills` {"2": "plural-possessive"} (option replaced).
- a2-195-intro-2: added `distractor_skills` {"1": "acc-poss"} for *ruhámat* (well-formed singular accusative).
- a2-192-practice-3 ("What is the English meaning of 'szülei'?") is tagged plural-possessive while a2-191-practice-3 (word meaning of dolgaim) is vocabulary: inconsistent (unsure, left).
- a2-194: -nak and -ra items (194-controlled-2, -dialogue-2, -practice-4, -writing-1, consolidation-9/-10/-19/-20) are tagged plural-possessive while 194-check-2 (-hoz) is tagged hoz-suffix and the -val items val-vel; no A2 skill fits -ra on büszke/vigyáz (`verb-government-ra-re` is B1, see 4). Left as is (unsure).
- Lesson challenge screens: all six lessons render "Put your Hungarian skills into practice for this goal." / "Form " cues and truncated titles ("Communicative Challenge: Form and use 1st person plural"): no entries exist in content/hu/curriculum/challenges.json. The six new challenges (my file) replace them.
- Vocabulary files list inflected forms as lemmas (barátaimmal, könyveimben, szüleimnek ...): affects dictionary/SRS (left).

## 3. Goals / checklists
- a2-191 line 1 "1st person plural possessed nouns" reads as plural owner (that is a2-193). Reworded in goal array, goal screen, checklist (3 places).
- a2-192 line 1 "2nd person ... and 3rd person ... plural possessed nouns" ambiguous with ti/ők; reworded.
- a2-193 line 2 "community activities" never practised -> removed.
- a2-195: goal screen lacked the -é line the checklist has; line 1 "synthesize ... locative endings" vague (locative barely practised). Reworded; goal now has 3 lines.
- a2-195-consolidation: "master ... effortlessly" overpromise; reworded. No -é line (see 1).
- Challenges canDo copied from the fixed checklist line 1.

## 4. Doubtful
- B1 same-family list (kent-vs-mint, terminative -ig): not presented or drilled (only plain *orvosként*, known). 
- a2-194, a2-195, consolidation: *büszke ... -ra*, *vigyáz ... -ra* are government of -ra/-re, whose skill `verb-government-ra-re` is B1 (b1-02-04-b-gr). Used in a2-194-practice-4, -writing-1, a2-195-practice-3/-writing-2, consolidation-9/-10. After my rewrites büszke/vigyáz remain in 194-practice-4, 194-writing-1 (new), 195-practice-3, 195-writing-2, consolidation-10 (sikereinkre). Either the lesson goes beyond A2 or the skill's level is wrong (unsure).
- a2-192 examples "Péter barátai", "A professzor válaszai", a2-192-controlled-4 "a tanár könyvei": bare noun possessor without -nak (not the dative-possessor pattern of a2-12-c). 3rd-person-possessive a1-41 covers it, so acceptable (unsure).
- a2-195 example "Nem felejtem el a jegyeimet és az irataimat az asztalon" ("I don't forget my tickets and documents on the table") is odd English-Hungarian (also a speaking step); suggest "Nem hagyom az asztalon a jegyeimet...". Unsure, not fixed.
- a2-195-practice-3: wrong options "carry one's umbrella", "lose one's tickets" mention things absent from the prompt (rule § 2.3, mild).
- a2-195-dialogue-3 has only two options (fine).
- a2-195-vocab and a2-194-vocab: *segítség, könyveimben, készülődés, elfelejt, elindul* never used in an exercise (check-content vocab-unused).
- Story: other lines fine; question 1 and 3 overlap (both "why rush").

## 5. Dictionary
lakáskulcsaid | lakáskulcs | noun | apartment key, house key |
nyugodj | nyugszik | verb | to rest, to calm down (megnyugszik: to calm down) |
végigtapogatta | végigtapogat | verb | to feel along, to pat down from one end to the other |
bálint | Bálint | noun | Bálint, a Hungarian male first name |

# UNIT 40: inflected-postpositions (a2-196 .. a2-200-consolidation, story a2-unit-40)

Fixes: `/home/user/parlour-read-a/fixes-inflected-postpositions.json` (70 fixes, check_fixes: 0 rejected, no new findings). Challenges: `/home/user/parlour-read-a/challenges-inflected-postpositions.json` (6).

## 1. Found by reading
**Level / used before taught / presented as new**
- a2-198-a example *Nélküled nagyon unalmas lett volna a tegnapi este* (also the a2-198 speaking step) and a2-198-writing-1 *nem tudtam volna megoldani*: past conditional with *volna* is `past-conditional-volna` (B1, b1-20-01). Fixed to plain past / present (*volt*; *nem tudom megoldani*).
- Story a2-unit-40: Máté's *nélküled ma is otthon ültem volna a szobámban* (same B1 form) and comprehension question 3 (correct option + explanation quote it). Fixed to *ülnék* / *maradna* (unsure).
- Story a2-unit-40: *onnan felette is ellátsz a kupoláig* is spatial -ig (terminative, B1, rulebook § 6); also question 2 option and explanation. Fixed to *jól látod a kupolát* (unsure).
- a2-196-a: no recap: plain *előtt, mellett, alatt, között* (a1-87-b) and personal endings on case suffixes (*bennem, nálam*, a2-161) are known; the screen starts "In Hungarian, when postpositions...". Recap added.
- a2-199-b: *-ért* ("for", forintért, a2-38-b) presented as a new "suffix/postposition ért" with no recap. Recap added (unsure how much of -ért the user counts as known; a2-161 teaches only benn- paradigm).
- a2-200-a: the 3-way contrast hol/hová/honnan (a2-28-b) is presented as new ("Just like Hungarian case endings, postpositions exhibit a 3-way distinction"). Recap added. *utánam* is listed as a member of the "motion towards" triad, but *után* has no mellé/mellől-type partner: moved out.
- a2-200-consolidation-8: answer *elé* (noun + elé, "a vendég elé") and -16 *elétek* (2nd person plural), a2-200-practice-2 *melléd* (2nd person): the 200 screen shows only the 1st person of the motion forms (mellém, elém, mögém), so *elé/elétek/melléd* are untaught forms. Rewritten with *elém* / *mellém*.
**Wrong Hungarian**
- a2-196-b: *Pont énelőttem áll!* "If emphasized, add the pronoun": not Hungarian; also contradicts a2-197-check-1 ("mi köztünk" incorrect). Replaced.
- a2-198-b example 2: *a recepOption* (corrupted text); fixed to *a boltban* (and English).
- a2-200-consolidation-20: *a legjobb barátaim ____* with answer *nélkülük* doubles the marking ("barátaim nélkülük"): rewritten.
- a2-198-dialogue-2: *megtartom mellette / előtte* nonsense options; rewritten with person-only options.
- a2-198-dialogue-1: *ne menjetek el mellettem* is a natural sentence ("don't walk past me"): a possible true answer. Option replaced.
- a2-199-dialogue-2: Eszter apologises that Bence missed the film start, Bence answers "we weren't late because of you": contradictory. Rewritten.
**Unmet words (fixed with met words)**
- a2-196: controlled-1 *gyere*; practice-2 *színpadot*; practice-4 *kijárat*; dialogue-2 *hölgy*; writing-1 *tolakodj*; check-2 *észre, éppen*. a2-197: controlled-1 *közvetlenül, élnek*; -2 *hangulat, megvolt*; practice-4 *repülőgép, húzott*; dialogue-1 *ugye*; dialogue-2 *feszültség, kiváló, munkahelyi*; writing-1 *örülök, megbízható*; writing-2 *vita*; check-2 *tisztázzátok, magatok*. a2-198: controlled-2 *érem, értekezletre*; practice-2 *bevásárlást*; practice-4 *igazi*; dialogue-1 *mindjárt, rohanok, semmiképpen*; dialogue-2 *megtartani, prezentációt*; check-2 *érsz, értekezletre*. a2-199: controlled-2 *négykor, kocsival*; practice-2 *baleset* (a2-219!), *következett*; practice-4 *áldozatot*; dialogue-1 *késő, kocsival*; dialogue-2 *sajnálom, lemaradtál*; writing-1 *bármikor, szívből, kiállok*; check-2 *magyarázkodnod*. a2-200: practice-4 *lépj, mindjárt*; check-2 *lépj*. Consolidation: -6 *rohanok*; -10 *parkoló* (a2-203, a later unit), *közvetlenül*; -11 *belvárosban, szökőkút*; -15 *észre, közvetlenül*; -16 *örülök, látogatásotoknak, elétek*; -18 *dugó*; -20 *elképzelni, nyaralást*. Left: consolidation-12 *elmentek* and -13 *megtettünk* (past of known verbs; unsure), check-1 in a2-199 *vs/distinction* are English words in the prompt (checker false positive).
**Exercise defects**
- a2-200-controlled-4 ERROR length (61 vs 35): shortened the right option.
- a2-198-controlled-2: "Nem érem el a vonatot, be tudsz menni az értekezletre helyettem?" does not follow; rewritten.
- a2-200-consolidation-10 uses *parkoló*, a word first taught in a2-203 (the next unit).
- Several "vary items" repeats: a2-197 has six items whose answer is *köztünk/közöttünk* and three *felettünk* (controlled-1, practice-4, dialogue-1); the pattern is thin but not a defect.

## 2. Metadata
- All dialogue-complete items (a2-196-dialogue-1/2, 197-d1/2, 198-d1/2, 199-d1/2, 200-d1/2, consolidation-11/-12) are tagged `a2-inflected-postpositions-vocab` although their options differ in the postposition chosen (word choice among postpositions) or the person; I left them (unsure): if the intent is "differ in a form -> that form's skill" they should be `inflected-postpositions`.
- a2-198-check-1 (options differ only in nélkül/helyett/velük), a2-199-intro-2, -controlled-4, -check-1, a2-200-intro-2, consolidation-13/-19: tagged vocabulary although they test the form choice (unsure, same reason).
- a2-200-consolidation-4: option *között* is a well-formed plain postposition (postpositions-basic): added `distractor_skills` {"1": "postpositions-basic"}.
- Lesson challenge screens: all six render the generic "Put your Hungarian skills into practice for this goal." / "Express the idea clearly and naturally" (no entries in challenges.json); the six new challenges replace them.
- a2-198-dialogue-1 / -2 options changed: no ds needed.

## 3. Goals / checklists
- a2-197 line 2 "interpersonal dynamics"; a2-198 line 2 "express reliance on friends, coordinate social events"; a2-199 line 1 "purposive ... postpositions" (-ért is a case ending, miatt "causal") and line 2 "sincere apologies, mutual support"; a2-200 lines 1-2 ("synthesize", "navigate public transport, give clear directions": no directions are practised); consolidation "command the full paradigm ... effortlessly" (2nd person plural never drilled). All reworded (goal array, goal screen and checklist).
- a2-196 goals are fine; challenges' canDo copy checklist line 1.

## 4. Doubtful
- B1 same-family list (felé/felől): not used.
- a2-197-check-1 "Which form is incorrect in standard Hungarian? *mi köztünk*": emphatic *mi köztünk* is heard; mark of the screen ("Both forms are completely correct") only covers közöttünk/köztünk. Unsure.
- a2-197-a: "között ... naturally used only in the plural or with pairs": fine; 3rd person singular *közte* not given.
- a2-199-controlled-4 "next to you" option mentions nothing absent from the prompt; fine.
- a2-200-consolidation-12 *elmentek* (unmet form) kept.
- a2-200-a lists *előlem, mellőlem, mögülem* (motion away) but no exercise drills them (a2-200-intro-1 offers *mellőlem* as a distractor only).
- Vocabulary: a2-199-voc *miattunk*, a2-200-voc *kereszteződés* were unused; *megbeszélés, unalmas* now used by the rewrites; *kereszteződés*, *miattunk* remain unused.
- Story: other lines natural; "Máté Anna mögé lépett" fine.

## 5. Dictionary
halászbástya | Halászbástya | noun | Fisherman's Bastion, a landmark terrace in Buda Castle district |

# UNIT 41: inflected-infinitives-necessity (a2-201 .. a2-205-consolidation, story a2-unit-41)

Fixes: `/home/user/parlour-read-a/fixes-inflected-infinitives-necessity.json` (58 fixes, check_fixes: 0 rejected; only new finding vocab-unused a2-203 *belépnem*, left by the dialogue-2 rewrite). Challenges: `/home/user/parlour-read-a/challenges-inflected-infinitives-necessity.json` (6).

## 1. Found by reading
**Known material presented as new**
- a2-201-a: opens "In Hungarian, when an infinitive refers to a specific person ... the infinitive takes personal endings", i.e. presents the inflected infinitive as new, although a2-105-b taught *dolgoznom, dolgoznod, dolgoznia*. No "You know ... from Unit 105". Fix: recap added; the plural forms (mennünk, mennetek, menniük) are the new part.
- a2-202-a: *kell*/*muszáj* + infinitive (a1-118-b) and the person on the infinitive (a2-105-b) shown as new; gloss "I should go / I must go" (kell is "have to", rulebook § 6). Recap added, gloss fixed; vocab a2-202 *kell = must / have to*, *muszáj = must / unavoidable* -> "have to / need to", "have to (no choice)".
- a2-203-a: *szabad/tilos* (a2-114-b) and *lehet* (a1-149-b) with an infinitive presented as new; recap added.
- a2-204-a: *érdemes* is known (a2-87-a); recap added (unsure). *kellett* (a2-204-b) is introduced as new: no A2 skill covers past *kellett*/*szabadna*/*lehetne* (skills frozen; the unit's "Grammar this unit teaches" list is empty), so these items are tagged inflected-infinitives. Report only.
**Wrong Hungarian / typos**
- a2-202-a example 1 and its speaking step: *lekésük a gépet* -> *lekéssük*.
- a2-205-consolidation-10: blank is the bare ending "ned" glued to "fejez" (answer *ned*): the learner types a suffix, teaches a split word. Fixed to the whole word *befejeznem*.
- Blanks glued to a prefix: a2-203-check-2 *el____*, a2-204-controlled-1 *el____*, a2-204-writing-1 *fel____*, a2-204-check-2 and -dialogue-2 *meg____*, a2-205-consolidation-7 *el____*. All blanked as whole words (*elfelejtened, elindulnod, felkelned, megértenie, megvenned*, consolidation-7 now *főznünk*).
- a2-204-dialogue-2: *használt autó* is a past participle used as a modifier (`past-participle-adjective`, b1-02-03, in the sheet's B1 list). Replaced by *régi autó*.
- a2-201-controlled-4: wrong option "Instrumental (Péterrel kell mennie)" is a correct sentence ("he has to go with Péter"); replaced by a nominative option.
**Exercise defects**
- a2-203-practice-3 ERROR length (43 vs 33): shortened the right option ("entry is forbidden without a permit").
- a2-205-check-1 ERROR length (50 vs 34), tell-opener *sajnos*, and the wrong options "Nem jövök, mert nem akarlak látni." / "Nem megyek mert alszom." are wrong by tone/punctuation only: rewritten with one form fault each (category/teaches set to grammar / inflected-infinitives).
- a2-202-intro-1: the question contains the answer ("Where does the preverb go in 'Fel kell kelnem'?" with option "Before 'kell' (Fel kell kelnem)") and options 2-3 fail the same way; option-language suspect. Rewritten. a2-205-consolidation-2 is the same item (also option-language suspect): rewritten with a different verb.
- a2-205-intro-1: option "Leadni kell nekem a jelentés." failed three things; now one fault each.
- a2-205-consolidation-13: wrong options each broke word order and the article/-t; one fault each now.
- a2-203-check-1, a2-205-consolidation-19: wrong options ("Kell adnod egy igazolást!", "Muszáj kapnom ...!") are wrong by tone/meaning, not form; and *igazolás* is first taught in a2-220. Rewritten with one form fault each (unsure; the ds entries are removed with the options).
- a2-203-dialogue-2, a2-201-dialogue-1: wrong option *menni* ("nekem menni kell") is heard colloquially (unsure, left).
**Unmet words (fixed with met words)**
- a2-201: controlled-1 *késő*; dialogue-2 *kisfiam, fejeznem, leckét*; writing-1 *kipihenhetem*; check-2 *reptérre*. a2-202: controlled-1 *mindjárt*; practice-2 *felejtheted*; dialogue-1 *pénzügyi, fejeznem*; writing-1 *házi* (b2); writing-2 *érnem*; check-2 *betegség*. a2-203: controlled-1 *kocsival*; practice-2 *egyedül, kiabálnod*; dialogue-1 *igazgató, természetesen, éppen*; dialogue-2 *belépés*; writing-1 *végeztünk*; writing-2 *zajt, csapnia*; check-1 *igazolást, adnod*. a2-204: controlled-1 *odakint, zuhog*; dialogue-1 *állásinterjúd, szakmai, készülnöm*; dialogue-2 *fenntartása*; writing-1 *érni*; check-2 *professzor, előadását*. a2-205: controlled-1 *délig, feltétlenül, dolgozatomat*; practice-2 *mielőtt, alaposan*; practice-4 *értekezletre, érned*; dialogue-1 *készülnöm, prezentációra*; dialogue-2 *személyesen*; writing-1 *szívből, teljesítenem*; check-1 *másnap*; check-2 *hétvégi*. Consolidation: -7 *készítenünk*; -8 *járművel*; -9 *betegség*; -11 *eljössz*; -12 *valamilyen*; -13 *teszt*; -15 *interjúra, készülnöm*; -17 *beszámolót*; -18 *annyit*.
- Not changed: a2-205-consolidation-6 and speaking step fine; a2-201-dialogue-2 *kész kell lennem* kept (natural).
**Story**
- a2-unit-41 summary mentions "orvosi időpontok" (no doctor appears in the story). Fixed (unsure). Story has no B1 forms; inflected infinitives used naturally (*be kell érnem, le kell adnom*). Minor: Dániel says he is home at six, Nóra says "hétkor találkozunk itthon" (fine). *szabad együtt főznünk valamit* is a stiff use of *szabad* (left).


## 2. Metadata
- a2-205-check-1: `category` vocabulary / `teaches` a2-inflected-infinitives-necessity-vocab -> grammar / inflected-infinitives (the options now differ in a form). Set in the fix.
- a2-203-check-1 and a2-205-consolidation-19: `distractor_skills` {"1": "kell-infinitive", "2": "kell-infinitive"} removed with the replaced options.
- No skill covers past *kellett* (a2-204-b), *szabadna/lehetne* (a2-203-b) or the evaluative predicates; items are tagged inflected-infinitives (skills frozen; report only). "Grammar this unit teaches" in the sheet is empty, so the unit has no new skill: if the user wants one it needs a frozen-list entry.
- a2-204-intro-2, a2-204-controlled-4 and a2-205-consolidation-5 (vocabulary) test which modal/evaluative word fits: consistent with the rulebook.
- Lesson challenge screens render the generic placeholder (no entries in challenges.json); the six new challenges replace them. The a2-205-consolidation challenge screen reads "In Hungarian, i have mastered inflected infinitives ..." (goal wording turned into a prompt); fixed by the goal rewrite.
- `distractor_skills` a2-201-intro-1 {"2": imperative-indefinite} (*menjek*) and a2-205-consolidation-1 {"2": irregular-nek-conditional} (*Mennék*) are right.

## 3. Goals / checklists
- a2-205-consolidation: "I have mastered inflected infinitives across all tenses, moods, and predicates ... with complete confidence" (no moods are drilled; the challenge prompt turns it into "In Hungarian, i have mastered ..."). Reworded in goal array, goal screen, checklist.
- a2-201 goal "across all six persons" is true only after the recap (singular known, plural new).
- Other lessons' goals are fine; challenges' canDo copy checklist line 1.

## 4. Doubtful
- B1 same-family list: *köteles/kénytelen* not used; *kellett volna* not used (only plain *kellett*); participles: only *használt autó* (fixed). -va/-ve, -andó, -ó/-ő: none.
- a2-203-b third bullet "Nem szabad elfelejtenünk a biztonsági szabályokat." sits under "Polite Inquiries: Szabadna / Lehetne" but is not a polite request (left).
- a2-205-b "Holnap délelőtt szabad találkoznunk?" glossed "Is it free for us to meet tomorrow morning?" is stiff (left, unsure). Story a2-unit-41 *szabad együtt főznünk valamit* likewise.
- Vocabulary files list inflected forms (mennem, menned, tanulnom ...) that restate a2-105-b material (parked: re-listing earlier words). Still unused after the rewrites: a2-201 *kötelező*, a2-202 *számla, befizet, különben*, a2-203 *belépnem*, a2-205 *elfoglaltság*.

## 5. Dictionary
adnom | ad | verb | to give (le+ad: to hand in) |
érnem | ér | verb | to reach, to arrive (be+ér: to get in on time) |
napsütéses | napsütéses | adjective | sunny |
projekttervezetet | projekttervezet | noun | project draft, plan for a project |
túlóráznom | túlórázik | verb | to work overtime |

# 6. miatt (units 40 and 41, a2-199 and after)
Skill `causal-postpositions` (plain *miatt*, *X miatt*) is B1 (b1-16-02-a-gr). No item in these units carries that tag: all are `inflected-postpositions`, `a2-inflected-postpositions-vocab` (unit 40) or `inflected-infinitives` (unit 41). Nothing was rewritten away; only unmet words next to *miatt* were replaced.

**Inflected miatt (miattam, miattad, miatta, miattunk, miattuk, miattatok), unit 40 only (none in unit 41)**
PRESENTED (new, taught)
- a2-199 title/`grammar` "Causal and purposive inflected postpositions: miatt and ért"; goal/checklist line 1 "inflected causal (miattam, miattad) ... postpositions" (I reworded it to "miattam, miattad (because of me, you)").
- a2-199-a (grammar screen "Because of Me: The Inflection of 'miatt'"): full paradigm miattam ... miattuk; text "Ne aggódj miattam!", "Ne haragudj, miattam késtünk el!"; examples "Ne aggódj miattam, már sokkal jobban érzem magam!" (also speaking step 1), "Nem miattad történt a félreértés, ne hibáztasd magad!" (also speaking step 2).
- a2-199-voc: miattam, miattad, miatta, miattunk (+ SRS cards, "miattunk" never used in an exercise).
DRILLED (tested; `teaches` in brackets)
- a2-199-intro-1 (right option *miattam*; wrong *miattamval*; inflected-postpositions); a2-199-intro-2 (*Ne aggódj miattam!*; vocab); a2-199-controlled-1 (*miattam*, fill-blank; inflected-postpositions); a2-199-controlled-3 (matching miattam/miattad; vocab); a2-199-practice-1 (builder "Kérlek, ne aggódj miattam!"; inflected-postpositions); a2-199-practice-2 (*miattad*; inflected-postpositions); a2-199-dialogue-2 (*miattad*; vocab); a2-199-check-1 ("miattam vs értem"; vocab); a2-199-check-2 (*miattad*; inflected-postpositions).
- a2-200-consolidation-7 (*miattam*; inflected-postpositions); -18 (*miattad*; inflected-postpositions); consolidation speaking step 2 (derived from -7); consolidation goal/checklist line 1 names *miattam*.
- Wrong options (tested only as distractors): a2-200-consolidation-12 *miattam* (vocab-tagged dialogue); -13 "Mindent megtettünk miattuk." (vocab); -19 "Kijössz miattam az állomásra?" (vocab); a2-199-dialogue-1 / a2-199-intro-2 contain no miatt.
- My challenge for a2-199 ("Ne aggódj miattam! ...") also uses it.

**Plain miatt (noun + miatt)**
PRESENTED / in passing in a screen
- a2-199-a example 3: "A dugó miatt késtünk, nem miattuk." (example only; not in a speaking step).
- a2-202-a example 3: "Holnap korán muszáj felkelnem a megbeszélés miatt." (example only).
USED IN PASSING IN EXERCISES (the tested form is something else)
- a2-200-consolidation-18: "Ne félj, a késés nem ____ történt, hanem a dugó miatt." (I changed *dugó* -> *vonat*, plain *miatt* kept; the blank is *miattad*; inflected-postpositions).
- a2-202-check-2: "A betegség miatt Tamásnak ágyban kell ____." (blank *maradnia*; inflected-infinitives; I changed *betegség* -> *fejfájás*).
- a2-204-writing-2 (builder, tile *miatt*): "Felesleges volt ennyit aggódnod a vizsga miatt." (inflected-infinitives).
- a2-205-consolidation-9: "A betegség miatt a szobában kellett ____." (blank *maradnia*; inflected-infinitives; changed to *fejfájás*).
- Story a2-unit-40, comprehension question 3, wrong option: "... a rossz fényviszonyok miatt." Story a2-unit-41: no miatt.
- Unit 39: no miatt.
