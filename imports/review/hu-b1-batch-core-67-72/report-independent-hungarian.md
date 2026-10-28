# hu B1 Unit 72 `independent-hungarian` (b1-36-01 .. b1-36-05, b1-36-consolidation; story b1-36-gardonyi)

Commands run: check-content (11 errors, 5 suspects before fixes), render_lesson, unmet-words (about 130 hits in 6 lessons), audit-reader-coverage. Fixes: `fixes-independent-hungarian.json` (78). Challenges: `challenges-independent-hungarian.json` (6). Nothing else was edited.

## 1. Found by reading

Whole-unit pattern: nearly every exercise was written with words of B2/C1 (unmet-words lists `first` stems in b2/c1 for dozens of them) and every vocabulary/definition item has three options of very different length. All of that is rewritten in the fixes file with A1-B1 words and the unit's own words; the right answers keep their point.

b1-36-01
- ex01: wrong options *Mindamellett*, *Kivételesen* unmet (b2) -> *Apropó*, *Egyébként* (met screen words).
- ex02: blank glued to the stem (`érde_____` + *ke*) -> blank the whole word *érdeke*; english said "after all" for *ugyebár* (glossed "as you know").
- ex03/ex07: english was the placeholder "Build the sentence in the correct order." -> real translations (same placeholder in every builder of the unit: 01.ex03/07, 02.ex03/07, 03.ex03/07, 04.ex03/07, 05.ex03/07, consolidation.ex03/07).
- ex04: length give-away 68 vs 44; unmet *képesség, fordítóprogram, kommunikáljunk, szótárkönyv, eladási* -> three "Azt, hogy az ember ..." options of 37-44 characters, each wrong one the meaning of another unit word.
- ex05: blank glued (`folyékonyság_____` + *ot*); unmet *rendszeres* -> whole-word blank *folyékonyságot*.
- ex06: wrong option *Ezzel szemben tilos* is not a real phrase; *tetejébe* unmet; question words *kapcsolódhatunk, felmerülő* -> "Melyik jelenti angolul: 'that reminds me'?" with *Ezzel szemben*, *Következésképpen* (real connectors, not "that reminds me").

b1-36-02
- ex01: tell-absolute *Teljesen*; *Azonnal megállva* is a -va form (and no phrase); question word *természetesen* unmet -> *Hogy is mondjam csak*, *Egyébként*.
- ex02: unmet *felkészülést*; hint "only" glosses the answer of a blank that the screen supplies -> hint removed, *odafigyelést* from the screen.
- ex04: length give-away 56 vs 38; eight unmet words; *közbeszólás* was unused (check-content suspect) -> "Melyik szó jelenti angolul: 'interjection, chiming in'?".
- ex05: blank glued (`számá_____` + *ra*); unmet *élvezetes, mindkét* -> whole-word blank *Szerintem* (inflected postposition, hint "in my opinion").
- ex07: unmet *elengedhetetlen, sikeres* -> "A spontaneitás fontos a társalgásban." (*spontaneitás* was otherwise only in a lost item).
- 02-b screen, first example: "Én nem mondtam semmit. vs Nem én mondtam, hogy gyere ide." pairs two sentences that do not contrast -> one clear example; and the focus position before the verb is A1 Unit 4 material -> "You know ..." added.

b1-36-03
- ex01: unmet *fejezd, témát*; rude/absurd wrong options; tell-punctuation (only the right option ended in "...") -> three full sentences, only the first one clarifies.
- ex02: blank glued (`egy_____` + *mást*) -> whole word *egymást*.
- ex04: length give-away 64 vs 40; unmet *kreatív, mondanivaló, kifejezésére, azonnali, megtalálása* -> "Melyik szó jelenti angolul: 'resourcefulness'?".
- ex05: blank glued (`tisztázás_____` + *a*); unmet *megkönnyebbültünk* -> whole word *tisztázása*.
- ex06: unmet *követelem, elmondom*; "Nem érdekel, de elmondom" is absurd; question word *udvariasan* -> *Hadd kérdezzem meg, hogy...*, *Attól tartok, hogy...*.
- ex07: unmet *nyugalom, megőrzése* -> "Váratlan helyzetben fontos a találékonyság."
- 03-b screen presents *attól tartok, hogy* as new; it is A2 Unit 27 (and *tart attól, hogy* B1 Unit 61) -> "You know ..." recap.

b1-36-04
- ex01: unmet *informált, fényképen, képzőművészeti, galériában* -> literal-reading distractors (*a falon van egy kép*).
- ex02: blank glued (`tart_____` + *sak*); unmet *technológiával* -> whole word *tartsak*, hint "keep, I".
- ex04: length give-away 71 vs 49; unmet *megegyeztek, tegeződésben, minisztériumi* -> choose the formal sentence for a stranger (*Kérem, foglaljon helyet!*), wrong options te form and a mixed form.
- ex05: blank glued (`stílusárnyalat_____` + *ok*); *jelzik* unmet -> "Ennek a szónak más a stílusárnyalata." (retagged `3rd-person-possessive`, run `lock_tags.py ... --update` after the fix).
- ex06: length give-away 46 vs 28; unmet *vitás, ügyben, vidéki, földúton*.
- ex07: unmet *helyes, kulcsfontosságú*; *köznyelv* was unused and *nyelvi regiszter* only in this item -> "A köznyelv és a hivatalos nyelv két nyelvi regiszter."
- Speaking steps 1 and 2 read the examples "Kérem, foglaljon helyet! vs Ülj le bátran!" and "Hogy tetszik lenni? vs Hogy vagy?": the learner has to say "vs" -> one sentence per example (informal halves kept as their own examples).
- 04-a screen presents *Ön/te* and *tetszik* as new; known from A1 Unit 25 and A2 Unit 37 (formal-address-on) -> "You know ..." recap.
- 04-b screen presents *dűlőre jut* as new; it is B1 Unit 53 (b1-27-02-b) -> recap. Example 3 *dűlőre jutottunk a szerződésről*: *dűlőre jut* takes *-ban/-ben* (*a kérdésben*) -> *a szerződés kérdésében* (unsure).
- 04-b *túl van a nehezén* has no example sentence (left).

b1-36-05
- ex01: tell-absolute *Kizárólag*; absurd option "aranyfalak"; unmet *védők, lelkében, megvédeni*; asks what Dobó said "in Gárdonyi's novel", but the sentence *A falak ereje nem a kőben van, hanem a védők lelkében* is the adapter's, not a known line of the novel -> asks about the story.
- ex02: blank glued (`boldogul_____` + *jak*), *boldogul* unmet -> whole word *éljek*.
- ex03: unmet *fejezni, gondolataimat* -> sentence from the screen's own words (*el tudom magyarázni a magyar történelmet*).
- ex04: eleven unmet words (*gyakorlati, kommunikációs, képességet, ... tudását*) -> "Mit jelent a 'nyelvtudás'?".
- ex05: blank glued (`távlat_____` + *okat*); unmet *sikeres, tanulásban* -> whole word *távlatokat*.
- ex06: all three options are slogans, two plainly absurd ("Semmit sem tanultam meg"); tell-punctuation; *kurzus* unmet; *anyanyelvi szint* was unused -> "Mit jelent az 'anyanyelvi szint'?".
- 05-a "B1 Subordination Synthesis" presents earlier units' clauses without saying they are known -> recap with unit numbers from the sheet (miután/mielőtt B1 Unit 1, mivel/mert A1 Unit 24, bár ... mégis B1 Unit 9, ha ... volna B1 Unit 39, reported speech B1 Unit 25).
- 05-b example 1 *bármilyen* is the B2 concessive indefinite (`concessive-indefinites`) -> *minden*.
- Story and lesson: the lesson is about "where I go from here" and the story is the siege of Eger; the link is only the word *önálló* in the summary (see 4).

b1-36-consolidation
- ex01: length give-away 109 vs 69, tell-absolute *Kizárólag*, eight unmet words -> "Melyik mondat igaz az önálló magyar nyelvhasználóra?".
- ex02: blank glued to *még* + `is` (the answer is the one word *mégis*) -> whole word.
- ex03: *természetesen* unmet (b2) -> *magabiztosan*.
- ex04: length give-away 75 vs 44, unmet *elszántság, fizikai, kőfalakat, magasabbra, téglából, fegyverek*; "a famous sentence of Gárdonyi's novel" is not a quote of the novel -> "Mi történt Eger várában a történet végén?" (answerable from the story).
- ex05: blank glued (`gyümölcs_____` + *ét*); unmet *kitartó, meghozta, maga* -> "Minden nap gyakorlom a szókincsemet." (acc-poss).
- ex06: *dűlőre* and *füstbe* unmet (the consolidation has no screens; *dűlőre jut* is only a multi-word italic of Unit 53 and lesson 04) -> the three single-word particles of lesson 01.
- ex07: unmet *szóló, kincs*.
- Speaking steps of the consolidation read the right answers of ex02 and ex05; they follow the new answers.

Vocabulary glosses: *közbeszólás* "polite interruption" (an interjection is not polite) -> "interjection, chiming in"; *stílusárnyalat* "tone of voice" (that is *hangnem*) -> "shade of style"; *anyanyelvi szint* "native-like level, near-native mastery" contradicts itself -> "native-speaker level". Screen 01-a: *márpedig* "nevertheless" and *ugyancsak* "thoroughly" are wrong glosses (and *ugyancsak* has no example); example 2 english "shared mutual interest" is redundant.

## 2. Metadata
- 04.ex05 retagged `teaches: ["3rd-person-possessive"]` (new sentence tests -a/-e on a noun possessor); the unit needs `python scripts/lock_tags.py hu b1/independent-hungarian --update --reason "..."` if it is locked.
- 01.ex06 gets `distractor_skills {"1": "adversative-contrast"}` (*Ezzel szemben* is the B1 Unit 21 connector); unsure, *Következésképpen* shares the tested skill `additive-connectors` and gets none.
- Skills tagged through aliases: `hogy-jon-jen` carries the register-modulation, subordination-synthesis and autonomous-expression screens; `egyreszt-masreszt` the self-repair and focal-inversion screens; `additive-connectors` the turn-taking and assertiveness screens. The tags on the items are sensible for what a wrong answer shows (04.ex02, 05.ex02 `hogy-jon-jen`; 04.ex04 `formal-address-on`; 02.ex05 `inflected-postpositions`; consolidation.ex02 `concessive-annak-ellenere`; consolidation.ex05 `acc-poss`); no change.
- 05.ex01 `category: reading` with `stage: literature` and consolidation.ex04 `category: reading` have no `teaches` (correct).

## 3. Goals / checklists
Goal lines rewritten (each lesson's first line stays except in 05 and the consolidation; challenge `canDo` copies the lines after the fix):
- 01: "I can master 4 vocabulary words ..." (master overpromises), "I can connect ideas smoothly across extended Hungarian speech." (not practised).
- 02: "I can exploit expressive Hungarian word order for subtle focal emphasis.", "I can learn 4 words ...", "I can participate with confidence in rapid, authentic group discussions."
- 03: "I can express disagreement with diplomatic softeners ...", "I can acquire 4 vocabulary terms ...", "I can navigate complex social misunderstandings smoothly and effectively."
- 04: "I can master 4 words ...", "I can interpret subtext, subtle humor, and implicit meaning in conversations." (nothing practises it).
- 05: "I can construct multi-tiered compound and complex Hungarian sentences with ease." (nothing practises it; it was also the `canDo`), "I can express complex thoughts and future ambitions in my own words.", "I can learn 4 words ..."
- Consolidation: "Consolidate all 20 capstone vocabulary items" (no vocabulary review), "Demonstrate effortless control over ..." and "Confirm full independent ability to communicate, debate, and thrive in Hungarian." (overclaims), "Graduate with pride from the Hungarian B1 Core Curriculum!" (not a can-do; claims the level is finished). The consolidation has no vocabulary section.

## 4. Doubtful
- Level: lesson 01 teaches `discourse-particles` material (*ugyebár* is first taught in b2-13-02-a, *elvégre* in b2-34-02-a, both B2); 02-b is the B2 family `b2-focus-inversion`; 03-b *hadd* appears first in a B2 screen; the vocabulary words *szófordulat* (b2-36-04-a) and *köznyelv* (b2-34-04-a) are first taught at B2 (unsure: either these screens go beyond B1 or the B2 skills' level is wrong). Left as is, items rewritten to stay inside the lesson's own words. Skill registry is frozen, so nothing is retagged.
- Story: the "oath" line *A falak ereje nem a kőben van, hanem a védők lelkében* is presented as Dobó's famous words in Gárdonyi's *Egri csillagok* (summary: "legendary oath"); I could not tie it to the novel (unsure). The story says "százezres" army (the novel's figure; historians give about 40,000; unsure whether to hedge). Exercises now ask only what the story says. The comprehension questions of the story are untouched (they use story words: *túlerő, zsoldos, ostromgép*).
- Lesson 05 topic (next steps in Hungarian) and the story (siege of Eger) are only linked through the word "independent"; the lesson is a graduation capstone with a literary text attached.
- 05-a: the summing-up screen's examples contain no *mégis*; only the speaking steps use them.
- The unit teaches almost no new grammar (the "Grammar this unit teaches" list of the sheet is empty): all six screens are discourse phrases or recaps. Not changed.
- Every fill-blank and builder in the unit reads as a slogan sentence ("A továbbfejlődés útja mostantól nyitva áll előttem"); only the unmet and tagging defects are fixed.

## 5. Dictionary
honolt | honol | verb | to reign, to prevail (of a silence or mood); to dwell |
puskaporos | puskaporos | adj | smelling of or full of gunpowder |
vártemplom | vártemplom | noun | castle church, church inside a fortress |
acélkardját | acélkard | noun | steel sword |
ágyútűztől | ágyútűz | noun | cannon fire, artillery bombardment |
bevehetetlen | bevehetetlen | adj | impregnable, that cannot be taken |
mellvédeken | mellvéd | noun | parapet, breastwork on a rampart |
szégyenszemre | szégyenszemre | adv | in disgrace, shamefully |
várudvart | várudvar | noun | castle courtyard |
szolnokot | Szolnok | noun | Szolnok (town on the Tisza, Hungary) |

Fix count: independent-hungarian 78 fixes (41 exercise `set` fixes, 37 text fixes in grammar, vocabulary and lesson files); 6 challenges.
