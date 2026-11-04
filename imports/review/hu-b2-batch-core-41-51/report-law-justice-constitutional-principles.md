# Report: hu b2 law-justice-constitutional-principles (B2 Unit 49)

Fixes: `fixes-law-justice-constitutional-principles.json` (100). Challenges: `challenges-law-justice-constitutional-principles.json` (6).

## 1. Found by reading
- grammar b2-25-02-a-gr: presents *köteles* (B1 Unit 19, `formal-obligation`) and the participle in -andó/-endő (B1 Unit 27, `future-participle-ando`; recapped B2 Unit 23) as new; also the Hungarian grammar term "beálló melléknévi igenév". Fix: "You know ..." opening (new word: *jogosult*).
- grammar b2-25-01-a-gr: does not link *sérelmére*, *terhére* to *rovására*, *javára* (B2 Unit 39, `b2-relational-compounds`). Fix: recap opening. Its tip says *alapján* "requires the preceding noun to take an explicit possessive agreement suffix (e.g. 'a törvény alapján')": the example has no suffix, so the rule contradicts itself. Rewritten (bare noun before *alapján*; *-nak/-nek* optional before *sérelmére/terhére*).
- grammar b2-25-02-a-gr tip: says *kell* "creates an impersonal sentence" (not true of *nekem kell ...*). Rewritten.
- grammar b2-25-03-a-gr tip: C1 style (*a szó szerinti értelmezés helyett a teleologikus jogértelmezést részesítve előnyben*), unmet words. Rewritten with one plain frame.
- grammar b2-25-05-a-gr tip: *A felperes tisztelettel indítványozza ...* is the official register (C1 `official-register`, like *szíveskedjék*); b2-25-05-writing-1 repeated it. Replaced by the plain third-person frame (*A felperes indítványozza ...*).
- b2-25-05-controlled-4: sentence subject is "A bíróság" but the English and `hint` say a party motioned ("The party motioned ... at the defendant's request"): the court does not move for the end of its own proceedings. Rewritten with "Az alperes ügyvédje".
- b2-25-05-reading-1/2/3, story: reading-1 says "Eötvös József regényében" and its wrong options (robbing the county treasury, foreign army) are not in the text; the story is an original scene under the book's name, so the question now asks about "the story" only. Right options (92-132 characters) were 1.4-1.6x the wrong ones: rewritten from the text (*A bíróság nem hallgatta meg a tanúimat*; *a jogrend gyökeres reformja*; *törvény ... igazság*).
- Length give-aways (all 14 check-content errors): b2-25-02-check-2, 03-controlled-3, 04-controlled-3, 05-controlled-3, 05-intro-1, 05-reading-1/2/3, consolidation-2, -3, -7, -9; tell-absolute *senki* (consolidation-3), *mindenki* (consolidation-7) removed.
- Meta questions with absurd wrong options: b2-25-03-controlled-3 ("completely arbitrarily based on personal mood"), 04-controlled-3 ("official award from the bar association"), consolidation-3 (garbled non-phrases), consolidation-7 ("A törvény sérelmére mindenki vidáman ünnepelt"), consolidation-9 ("jogosult is an archaic noun only found in 19th-century novels"). Rewritten with plausible one-fault options; consolidation-9 became a direct choice (jogosult / köteles / megismerné).
- b2-25-03-dialogue-2: the right option *megismerhetők* and wrong option *megismerhetőek* are two accepted spellings of the same word. Item rewritten.
- b2-25-03-dialogue-1 wrong option 2 changed two things (accusative and *követnének*); b2-25-04-dialogue-1/-2, 05-dialogue-1/-2: wrong options rewritten to one fault.
- Unmet words (unmet-words.js, about 110 hits): rewritten in b2-25-01 intro-2, controlled-4, practice-1, -3, -4, dialogue-1, -2, writing-1, -2, check-1, -2; 25-02 controlled-2, -3, -4, practice-1, -2, -3, dialogue-1, -2, writing-1, check-1; 25-03 controlled-2, practice-1, -2, -3, dialogue-1, -2, writing-1, -2, check-1, -2; 25-04 controlled-4, practice-1, -4, dialogue-1, -2, writing-2, check-1, -2; 25-05 intro-2, practice-1, -4, dialogue-1, -2, writing-1, -2, check-1, reading-1..3; consolidation-4, -6, -7, -8, -11, -12. No word was added to a vocabulary list.
- b2-25-02-controlled-3: wrong options *teljesített*, *teljesítő* are real participles of other skills (`past-participle-adjective`, `present-participle`); kept in form, on *betartandó/betartott/betartó* (met words), with `distractor_skills`.
- Present-day / legal facts, flag "check": 25-04-dialogue-2 "tizenöt napon belül fellebbezést" (15-day civil appeal period) and consolidation-4 "harminc napon belül ... keresetlevelet" (30-day period for a claim against an administrative decision); *Polgári Törvénykönyv*, *Alaptörvény*, *Alkotmánybíróság* are the current names. The story uses *vármegye* correctly for the 19th century (historical; the counties are *megye* again since 1 October 2026, no present-day claim).

## 2. Metadata
- Every grammar item of the unit (about 55) is tagged `formal-obligation` (B1 Unit 19), but only the *köteles* items test it. Retagged: 25-01 grammar items (alapján, összhangban, sérelmére) to `b2-relational-compounds` (known, Unit 39; unsure, the skill title says "social and economic analysis"); 25-02 -andó/-endő items (controlled-3, practice-1, writing-2) to `future-participle-ando`; 25-02 dialogue-1 to `verb-government-ra-re`; accusative-form dialogues and fills (25-02 dialogue-2, 25-03 dialogue-1/-2, 25-04 controlled-4, dialogue-1/-2, 25-05 dialogue-1, consolidation-8) to `how-the-accusative-t-works`; 25-05 dialogue-2 to `3rd-person-possessive`; 25-05 controlled-4 to `definite-past` (grammar); 25-03 practice-1 to `inflected-infinitives`; consolidation-3 to `future-participle-ando`.
- Word-meaning items in lessons 3-5 and 25-01 controlled-2 were tagged `formal-obligation` / grammar: retagged to the unit vocabulary `b2-law-justice-constitutional-principles-vocab` with `category` vocabulary (25-01 controlled-2; 25-03 controlled-2, -3, -4, practice-2, check-1; 25-04 controlled-2, -3, practice-1, -2, -4, check-1; 25-05 controlled-2, -3, practice-1, -2, -4, check-1; consolidation-11); writing items 25-03 to 25-05 and consolidation-12 to the unit vocabulary (open writing).
- `distractor_skills`: 25-01 dialogue-2 `val-vel`; 25-02 controlled-3 (`past-participle-adjective`, `present-participle`); consolidation-9 `nek-conditional`.

## 3. Goals / checklists
- Promised but not practised: 25-01 "cite statutory bases ... using alapján and értelmében" (*értelmében* only on the screen), "state procedural prejudice and legal detriment"; 25-02 "employ prescriptive future/obligatory participles"; 25-03 "articulate statutory interpretation using teleological and grammatical principles", "evaluate judicial discretion"; 25-04 "analyze constitutional tensions between public authority and civil liberties", "evaluate proportional restrictions ... using legal criteria"; 25-05 "formulate binding petitions and formal motions (indítványoz, kérelmez)" (*kérelmez* never appears), "structure formal legal pleadings"; consolidation "draft structured legal arguments integrating ...". All reworded to what the items drill.
- Lesson challenge screens ("Put your Hungarian skills into practice for this goal.") are replaced by the six challenges in the challenges file.

## 4. Doubtful
- Lesson built on a known skill, taught in B1 Unit 19 (`formal-obligation`) and B2 Unit 39 (`b2-relational-compounds`): the unit teaches no registry skill, so lessons 1-2 are largely review (köteles, -andó/-endő, rovására-type postpositions); new words are *jogosult*, *alapján*, *összhangban*, *sérelmére*, *terhére*, and the legal nouns.
- C1 family: `epistemic-modality` and `official-register` are listed at C1. No epistemic *kell, hogy* / *lehet, hogy legyen* form occurs; the only official-register item was the *tisztelettel* petition formula (fixed). 25-04 screen example *nem hozhatott volna* is the known past potential (Unit 15), not epistemic.
- 25-04 screen tip uses *illetékesség* (unmet, tip only).
- 25-05 story: *vármegyei*, *statáriális*, *szolgabíró*, *pandúr* are historical; fine for the 1840s scene. Not the novel's plot as such ("original scene").
- 25-03 screen says courts use *méltányosság* to mitigate; in Hungarian practice this is mainly a power of authorities (e.g. remitting a fine, as its own example shows). Left (unsure).

## 5. Dictionary
jogrend | jogrend | noun | legal order, system of law |
bosszúállás | bosszúállás | noun | taking revenge |
kezűleg | kezűleg | adverb | with one's own hand (saját kezűleg) |
szolgabíró | szolgabíró | noun | county magistrate (historical) |
tiszaréti | tiszaréti | adjective | of Tiszarét (place name) |
alkonyodott | alkonyodik | verb | to grow dusky, dusk falls |
átszövi | átsző | verb | to weave through, to permeate |
botbüntetésre | botbüntetés | noun | flogging, caning as punishment |
búcsúzóul | búcsúzóul | adverb | as a farewell |
bujdosásba | bujdosás | noun | life as a fugitive, wandering in hiding |
büntethető | büntethető | adjective | punishable |
füzesekben | füzes | noun | willow grove |
jogegyenlőségért | jogegyenlőség | noun | equality before the law |
mocsárvilágban | mocsárvilág | noun | marsh world, marshland |
ólálkodsz | ólálkodik | verb | to lurk, to prowl |
önkénnyel | önkény | noun | arbitrariness, tyranny |
önkényes | önkényes | adjective | arbitrary |
paragrafusok | paragrafus | noun | section, article of a law |
sötétedéskor | sötétedés | noun | nightfall, dusk |
statáriális | statáriális | adjective | summary (martial-law) |
susogó | susogó | adjective | whispering, rustling |
szavával | szó | noun | word |
vándorbotjával | vándorbot | noun | walking staff |

Fix count: 100 (law-justice-constitutional-principles), challenges 6.
