# Report: hu b1 kormanyablak (B1 Unit 74, citizenship track)

Commands run: check-content (6 errors, 8 suspects), render_lesson, audit-reader-coverage (story b1-kormanyablak), unmet-words (about 110 hits). 71 fixes in fixes-kormanyablak.json, 6 challenges, facts-kormanyablak.md.

## 1. Found by reading
- Story p1: "a központi Kormányablakba" -> kormányablak is a common noun, lower case (same in the lessons' grammar example).
- Story p2: "belépett az ügyfélszolgálatra" is not Hungarian (belép + -ba/-be; ügyfélszolgálat is a service) -> "az ügyfélszolgálati térbe"; "az online kapott foglalási kódot" -> "az e-mailben kapott".
- Story p4: "ujjnyomatot" (not in the dictionary; ujjlenyomat is the word; the clerk takes, not "makes", fingerprints) -> "levette az ujjlenyomatát" (unsure). "az új szállásadója által aláírt lakcímbejelentő lap": the form is signed by the owner or person entitled to use the home (check; the lesson and consolidation use szállásadó and tulajdonos side by side).
- Story p5: "Ügyfélkapu+" is the old higher security level; check whether it still exists in 2026 (fix: "Ügyfélkapu-regisztrációja", unsure). Lesson 03 title has the same "+".
- Story has no `questions`; the lessons' reading items asked facts the story never states (walk-in rule, residence proof, Ügyfélkapu uses, deadlines, lost ID). 01.ex01 rewritten to ask what the story says; 02.ex01, 03.ex01, 03.ex04, 04.ex01, 05.ex01, cons.ex01, ex04, ex10 retagged `vocabulary` + unit vocab skill (definition items). None copies a story question.
- Grammar 01: the screen presented -ra/-re (A2 Unit 6) as new; "wait until" does not translate "amikor".
- Grammar 02: false rule "bejelent with the allative or inessive: ... a lakcímkártyáján" (bejelent takes the accusative); screen shows "igazolom magam" while ex02 needs "magamat"; -val/-vel presented as new.
- Grammar 03: "specific motion verbs and cases" presented four known endings (-ra/-re, -t, -n, -val/-vel) as new -> recap with unit numbers.
- Grammar 04: dative -nak/-nek presented as new; "előterjeszt" is "kérelmet terjeszt elő"; "két tanúval ... szükséges" overstated (a lawyer or notary can replace the witnesses), hedged "általában".
- Grammar 05: the screen text says "tizenöt napon belül" while its first example says "nyolc napon belül"; example 3 and ex03 say appeals within 30 days, the Ákr. appeal deadline is 15 days (30 is the court deadline) -> fixed (unsure, check); instrumental presented as new.
- 02.ex08 "A tartózkodási hely öt évig marad érvényes": unsafe figure -> neutral sentence. 03.ex08 "teljes bizonyító erejű magánokirat" legal claim -> neutral sentence. 04.ex08 "harminc napig használható": no general rule -> "a megadott ideig". 05.ex07 "húsz nap" -> "néhány hét".
- Cons.ex02: blank glued to a non-word stem (megten + ni) -> blank "megtenni"; three working days (munkanap).
- Cons.ex09 "illeték mentességet" -> illetékmentességet. Cons.ex12 "gyors és szakszerű" praises an office -> neutral. Cons.ex06 "decree" for határozat -> decision. Cons.ex05 ID cards are not collected by proxy as a rule (check) -> "iratokat".
- Absurd wrong options (scissors, cinema ticket, carrier pigeons, football club) replaced by plausible ones in 01.ex04, ex07, 02.ex01, ex04, ex07, 03.ex01, ex04, ex07, 04.ex01, ex04, ex07, 05.ex01, ex07, cons ex01, ex04, ex08, ex10.
- check-content errors (6 length give-aways) fixed in 01.ex04, 02.ex01, 03.ex07, cons ex01, ex04, ex08; tells (final punctuation) in 02.ex01, ex07, 03.ex07, 05.ex04; vocab-unused: sorszámhúzó automata (01.ex01), érvényességi idő (02.ex05), nyomtatvány (04.ex05), bankkártyás fizetés (05.ex05).
- Unmet words: about 70 lemmas added to the vocab lists (01: 8, 02: 9, 03: 11, 04: 5, 05: 18 incl. the consolidation's words, as it has no vocab file). `sel` (answer token) ignored.

## 2. Metadata
- 02.ex02 hint "myself, accusative ending" named the tested ending -> "myself".
- Reading items retagged (see above). All other tags kept; fill-blanks tagged by suffix skills (ra-re, acc-poss, val-vel, past-tense-indefinite, verb-government-nak-nek, on-en-on, ban-ben-in) are fine.
- No distractor_skills on any item; none needed.

## 3. Goals / checklists
All first goal lines were the template ("Master essential Hungarian administrative terms for ..."); lines 2 and 3 were identical in lessons 1-5. All rewritten as plain can-do lines (fixes on the lesson files; canDo in the challenges file copies line 1). Consolidation goal 4 ("full independent capability") over-promised.

## 4. Doubtful
- "Kormányablak" capitalised in lesson titles, voc titles, unit title and `location` of the story: the reviewer may lower-case globally (I fixed the text I touched).
- Whether walk-in visits without a booking are possible (not asked now).
- "digitális állampolgárság" gloss in the vocab: refers to the DÁP programme/app; check 2026 wording.
- Lesson "unit": 37 / story "order" values in the lesson and story files do not match the unit number 74 (reviewer's call).

## 5. Dictionary
személyazonosító | személyazonosító | adj | identity-proving, used in "személyazonosító igazolvány" (identity card) |
átvételi | átvételi | adj | relating to receiving (e.g. a receipt for taking over a document) |
érintőképernyős | érintőképernyős | adj | with a touchscreen |
intézhesse | intéz | verb | to arrange, to deal with (matters) |
lakcímbejelentő | lakcímbejelentő | adj | for registering an address |
lejárat | lejárat | noun | expiry |
szállásadója | szállásadó | noun | accommodation provider, host |
ujjnyomatot | ujjnyomat | noun | fingerprint |

Fix count: 71 (kormanyablak).
