# Report: hu B1 Unit 2 `hungary-today-land-symbols` (prompt-b)

The harness refused to write the report file, so this reply is the only copy of the report.

Files written in `/home/user/parlour-read-b/`:
- `fixes-hungary-today-land-symbols.json` (106 fixes)
- `challenges-hungary-today-land-symbols.json` (6 challenges, flat object keyed by lesson stem)
- `facts-hungary-today-land-symbols.md`

I changed nothing else in the worktree.

**Testing.** I tested the fix list on a scratch copy of the tree, not the worktree.
- `check_fixes.py` gave 0 rejected.
- `check-content` went from 1 error and 4 suspects to 0 and 0.
- `unmet-words.js` went from 248 hits to 5. The 5 are false positives: *helyezkedik* without *el*, the name *Pest*, and *tevődik össze* read as a phrase.

**To do after applying the fixes:**
- Rebuild `word-lesson-index.json` (new vocabulary words).
- Rebuild the combined `b1-orszagma.json` from the segments (I fixed the segment files only).
- Run `lock_tags.py hu b1/hungary-today-land-symbols --update --reason "..."`. `validate-content` fails on the four items whose `distractor_skills` I added (L3 ex09, consolidation ex03/ex05/ex06), and on L5 ex07 if the unsure retag is taken.

**check-content before my fixes:** one ERROR (tell-absolute, L1 ex03 *kizárólag*) and four suspects (vocab-unused *tanúhegy*, *északkelet*, *délnyugat*, *kifejez*). All are fixed. L5 *kötelék* was also unused, found by reading, and is fixed.

## 1. Found by reading

**Forms used before their screen (the sheet's "later" list)**
- L1 g01 tip and ex06 (old tiles): *Közép-Európában fekvő* is a present participle (`present-participle`, B1 Unit 11). Fixed: the tip now uses a finite verb, and ex06 is *Magyarország egy szárazföldi ország Közép-Európában.*
- L2 g02 text, examples 2 and 3, speaking 2, ex08 (old): the screen teaches "participial modifiers (-ó/-ő)" as new (*húzódó*, *fekvő*, *elterülő*). Fixed with finite verbs.
- L3 ex05, ex08, consolidation ex11 and ex16 (old): *lévő*, *kiemelkedő*. Fixed. Story 03 comprehension Q1–Q3 also used *lévő*; the stories are exempt, the questions are not. Fixed.
- L5 g05 example 2 *a jövőbe vetett hitet* is a past participle (`past-participle-adjective`, B1 Unit 3). Fixed to *a reményt is kifejezik*.
- Verbal nouns in -ás/-és (`nominalization`, B1 Unit 31) were used in several places:
  - *elhelyezkedését*: L1 ex07 (old) and L5 g05 example 1 plus its speaking step.
  - *egyesülésével*: L2 ex06 (old).
  - *kapcsolattartás* and *megszerzése*.

  Fixed. L5 now reuses the screen's own phrase *a földrajzi fekvést tekintjük*.
- Adverbial participles in -va/-ve (`participle-actions`, B1 Unit 57): *haladva* (consolidation ex04 old), *állva* (consolidation ex05 old), *összekötve* and *mellőzve* (L5 ex02 old). Fixed.
- *ahol* (`ahol-amikor`, B1 Unit 10) in L4 ex07 old, and *míg* (`mig-egyidejuseg`, B1 Unit 4) in L1 ex03 and L2 ex05 old. Fixed. The stories use *míg*, which is exempt.
- L5 g05 teaches discourse connectors (*mint köztudott*, *összefoglalásképpen*, *nemcsak… hanem… is*). The skill `additive-connectors` has `taught_in` b1-32-01-b-gr (B1 Unit 63). Either the lesson goes beyond B1 order or the skill's level is wrong. I left it alone; see group 4.

**Known material presented as new (screens)**
- L2 g02: *mellett* and *között* (A1 Unit 18) had no recap. Added "You know … from A1 (Unit 18)".
- L3 g03: *-ból/-ből* (A1 Unit 31) was presented as new. Recap added. The text also said *tagolódik* takes *-ból*; it takes *-ra/-re*, as the table row says. Fixed.
- L4 g04: *-val/-vel* (A1 Unit 28, verbs governing it A2 Unit 5) and *-ra/-re* (A2 Unit 6) were presented as new. Recap added.
- L5 g05: *ha* clauses (A2 Unit 13) and *nemcsak… hanem… is* (A2 Unit 5) were presented as new. Recap added.

**Wrong or misleading Hungarian and grammar claims**
- L2 g02 text said postpositions follow an unmarked nominative noun, yet the table row *X-en túl / innen* needs *-n*. Fixed: *túl* and *innen* are named as the exception, and the table row reads *X-n/-on/-en/-ön túl / innen*.
- L2 g02 example 3 *A Dunántúl a Duna jobb partján túl elterülő dombos táj.*: Transdanubia is on the right bank, not beyond it. Fixed to *A Dunántúl a Dunán túl fekszik.*
- L4 g04 text called *északkeleten* "inessive (-ban/-ben)". It is *-n* (on). Fixed.
- L4 g04 tip had a plural subject with a singular verb, *Szerbia és Horvátország terül el*. Fixed to *terülnek el*.
- L4 ex06 (old) had the same agreement error, and *nyugatra* was unmet. Fixed: *Magyarországtól északra Szlovákia fekszik, délre pedig Szerbia.*
- L3 g03 example 4 *a Tátra, a Mátra és a Fátra hegycsúcsait*: they are mountain ranges, not peaks. Fixed (*hegyeit*). Consolidation ex12 *hegycsúcsot* is fixed too.
- L3 g03 example 3 stated the four-rivers reading flatly. It is a tradition; now *A hagyomány szerint…* (unsure).
- L1 ex04 and consolidation ex10: *terül (el)* is a second right answer (it is on the L1 screen). Fixed with `answers`.
- L3 ex10 had a blank glued to a stem (`pajzs____` + `ból`). Fixed: *A címer a ___ és a Szent Koronából áll.* / *pajzsból*.
- L3 ex06 used *hasított*, which is not on the screen (it says *kettéosztott*). Fixed.
- L3 ex09 and consolidation ex05:
  - *zászló* was unmet (the listed word is *lobogó*).
  - Consolidation ex05 copied L3 ex09.
  - Fixed; the wrong options are now real forms of other skills, with `distractor_skills`.
- Story 01 p3 *medenceföldrajz* is not a word. Fixed to *zárt földrajzi egység*.
- Story 03 p5 *beavató korona* is not a term and *legépebben* is odd. Fixed.
- Story 03 p5 and comprehension Q3 present the bent cross's 17th-century lid story as certain. Hedged with *a hagyomány szerint* (unsure).
- Story 02 p5 *északnyugaton a barokk Győr, a Dunántúl történelmi koronázóvárosa, Székesfehérvár* reads as if Győr were the coronation city and puts Székesfehérvár in the north-west. Fixed.
- Story 02 p2 and L2 ex04 (old): the Tisza joins the Danube "délen". The confluence is in Serbia. Fixed: *már Szerbiában*, and the ex04 sentence now names Serbia.
- L4 ex05 (old): the right answer listed only Austria, Slovakia, Slovenia and Croatia as border-check-free. Romania has been inside Schengen since 1 January 2025. Fixed in ex05 and the story (unsure, verify).
- Story 04 p5 says the simplified naturalization procedure requires this knowledge. I doubt it. Reworded (unsure).
- L1 intro said "36-unit track" (the citizenship track has 39). Fixed.
- L1 intro said "exam that most applicants have to pass". Probably only the ordinary procedure. Fixed (unsure).
- L5 ex03 (old) had English inside a Hungarian question ("a citizenship track első egysége"). Fixed.

**Answer-set defects**
- L5 ex07 (old): all three replies were natural answers to "why do you want to be a citizen", so there was no single right answer. Fixed: a formal-greeting reply, with a register fault and a wrong-time-of-day fault.
- Pre-pass wrong options that were absurd, false or full of unmet words were rewritten with one fault each:
  - L1: ex02, ex03, ex07, ex08.
  - L2: ex02, ex03, ex05, ex07, ex08.
  - L3: ex03, ex07, ex08.
  - L4: ex02, ex03, ex07, ex08.
  - L5: ex02, ex03, ex05, ex08.
  - Consolidation: ex02, ex03, ex11, ex13, ex17 (*az egész ország egyetlen hegycsúcs*), ex19, ex20.
- Consolidation ex03 (old): both wrong options lacked the case ending (same fault). They are now real *-be* and *-n* forms.
- Consolidation ex07 (old): *mentén* would also fit the blank. It is now *Buda és Pest ___ folyik a Duna* (*között*).
- L1 ex05: the wrong options now differ from the right one by a single number each.
- The length give-away (L1 ex03 *kizárólag*) is gone after the rewrite. Two new check-content findings from my drafts (L5 ex02 *Mindig*, L4 ex03 first-letter case) were fixed before the list was finalised.
- L5 ex01 and ex01b now use 5 pairs each, so *kötelék* and *kifejez* are used.

**Unmet words**
- 248 unmet-word hits in the exercises, mostly from the pre-pass options, were rewritten with met words.
- Added to vocabulary lists (used in items, in no list):
  - L1: *körülbelül*, *millió*, *négyzetkilométer*.
  - L2: *dombos*, *síkság*.
  - L3: *címer*, *pajzs*, *sáv*.
- The L3 vocabulary gloss *patriarchal / apostolic double cross* is now *apostolic double cross*.

## 2. Metadata

- L3 ex09: add `distractor_skills` {"0": "plural-nouns-k", "2": "ra-re"} (in the fixes).
- Consolidation ex03: `distractor_skills` {"1": "movement-with-ba-be", "2": "on-en-on"}.
- Consolidation ex05: `distractor_skills` {"1": "ban-ben-in", "2": "delative-rol-rel"}.
- Consolidation ex06: `distractor_skills` {"1": "movement-with-ba-be", "2": "tol-tol"}.
- The tags are locked, so run `lock_tags.py --update --reason "..."` after applying.
- L5 ex07: `teaches` from b1-hungary-today-land-symbols-vocab to `formal-address-on` (unsure).
- L4 ex06 builder is tagged vocabulary but tests *északra/délre* (`ra-re`). Left alone (unsure).
- The grammar screens of L1, L2, L4 and L5 teach known material (L5 a later skill) and have no tagged exercise. Only L3 tests its own skill `verb-government-bol-bol`.
- Reading items carry no `teaches`, which is correct. Other categories follow their tags.

## 3. Goals / checklists

- L1 goal 4 promised *terül el*, which no item practises, "in B1 sentences". Reworded.
- L2: all five goals promised things no item practises (*magyar tenger*, *mellett*, *túl*, "autonomous capital", city locations). Reworded; the new first line is the challenge `canDo`.
- L3 goals 3 and 4 covered the bent cross, a legend no item practises. Reworded. Goal 2 now says "traditionally four rivers".
- L4 goal 1: "describe where each one lies" is now "where some of them lie".
- L5 goal 1 ("structured B1 Hungarian") and goal 5 ("confidently participate in a simulated interview") reworded.
- Consolidation goal 1 ("I can consolidate…") is not a can-do. Goal 3 (cross-border regions) is no longer reviewed. Both reworded.
- The challenge screens the lessons generate from the goals are broken:
  - The scenario is "Put your Hungarian skills into practice for this goal."
  - Titles are cut mid-phrase (*Communicative Challenge: Describe the Hungarian flag's*, *Name Hungary's seven*, *Consolidate Hungary's*).
  - Cues are garbled (*A Kárpát-medencében*, *Rivers in structured B1 Hungarian*, *Cities*).

  My six challenges replace them; they still need merging into `challenges.json` and wiring to the lessons.
- Goals and checklists are identical lines, stored three times in lessons 1–5 and twice in the consolidation. The fixes replace each copy.

## 4. Doubtful

- L5 g05 and `additive-connectors`: it is taught in B1 Unit 63 but its content is on this screen (unsure which is wrong).
- L2 *mentén*, *túl* and *innen* are listed here as new, but the sheet's B2 family has `b2-spatial-postpositions`. The level of those words may be wrong (unsure).
- L3 ex03 and g03: "bal/jobb oldal" is read from the viewer's side, while Hungarian heraldic description often means the heraldic side (the opposite). I dropped the side-swap option so a heraldry-trained learner is not penalised, but the item still asserts "left = Árpád stripes" (unsure).
- Consolidation ex08 and L3 ex04 accept *tevődik össze*. It is fine in L3, but `unmet-words` flags it in the consolidation (a phrase, not a single word). Kept.
- Each lesson has three same-shape MC items (ex02, ex03, ex05) plus a dialogue MC. This is the template and is course-wide; not changed.
- The consolidation title "Unit 1 Consolidation" is the track's Unit 1, but this is B1 Unit 2, and the core B1 Unit 1 consolidation has the same title. The next citizenship unit's "Unit 2 Consolidation" collides with core Unit 2. Naming scheme, course-wide.
- Story 02 p1 says Hungary splits into two great regions; many sources use three (with the northern uplands). Marked "check" in the facts file.
- *szigetjelleg* (story 01) is stiff but legal. The Finno-Ugric node is debated by some linguists; named in the facts file only.
- The stories' comprehension questions in this unit carry no `questionEnglish` or `optionsEnglish`. Not changed.
- Wrong options naming real places (Bécs, Rajna, Bajkál, Pireneusok) are fine as wrong options. Check that L2 ex03 and consolidation ex20 stay unambiguous (Vienna has a parliament, not the crown).

## 5. Dictionary

szigetjelleg | szigetjelleg | noun | island character, insular nature |
mélyülő | mélyül | verb | to deepen, to get deeper |
napfényes | napfényes | adjective | sunny |
népköltészet | népköltészet | noun | folk poetry |
borvidékeiről | borvidék | noun | wine region |
édesvizű | édesvizű | adjective | freshwater, of fresh water |
koronázóvárosa | koronázóváros | noun | coronation city |
közigazgatásilag | közigazgatásilag | adverb | administratively |
tagolódik | tagolódik | verb | to be divided into, to be structured |
tanúhegyekről | tanúhegy | noun | butte, isolated remnant hill |
címerpajzs | címerpajzs | noun | coat-of-arms shield |
koronaláda | koronaláda | noun | crown chest, chest for the crown |
koronaőrség | koronaőrség | noun | crown guard |
államalapításának | államalapítás | noun | founding of a state |
lecsapódásakor | lecsapódás | noun | slamming down, impact |
mementója | memento | noun | memento, reminder |
vasfedelének | vasfedél | noun | iron lid |
ellenőrzésmentes | ellenőrzésmentes | adjective | free of checks |
határellenőrzés | határellenőrzés | noun | border control |
határszakaszt | határszakasz | noun | border section |
körbetekintünk | körbetekint | verb | to look around |
nemzetrész | nemzetrész | noun | part of the nation (living across a border) |

*medenceföldrajz* is flagged by the audit but is not a word; the fix replaces it in the story.

## Facts

The full per-claim list (claim | where | sure / check) is in `facts-hungary-today-land-symbols.md`. The "check" lines the reviewer should verify are:
- the Alps and Dinaric boundary wording of the Basin
- the Finno-Ugric node
- the Tisza as the most-sung river
- Balaton as the largest lake in Central Europe
- "vármegye" as the traditional or official name
- the "autonomous" capital
- the flag colours' meaning and "kiontott vér"
- the four rivers and the Tátra/Mátra/Fátra readings of the arms
- the double cross as a memento of St Stephen
- "one of the oldest and best-preserved crowns"
- the 17th-century cause of the bent cross
- the Romania/Schengen change
- the simplified procedure's requirements
- the ordinary-procedure-only exam (L1 intro)
- what the oath expresses

No modern political judgement was found. All story reading questions are answerable from the story.

## Fix count per unit

hungary-today-land-symbols: 106 fixes (72 change Hungarian text; 8 marked unsure).