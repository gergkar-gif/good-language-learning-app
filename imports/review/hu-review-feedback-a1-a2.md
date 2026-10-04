# Review of the Hungarian A1-A2 pass (ROADMAP 117)

Reviewer's findings on commits `50e415b8` … `e446e5c8`. Read this before
continuing B1, and apply section 1 to B1 now. Sections 2-3 are a follow-up
for A1-A2 once B1 is finished.

## What went well

The changes themselves are mostly good: real near misses on the taught
point (*Petrán / Petrával keresztül*, *egy hónapra / egy hónapban
érvényes*, *akit szorgalmas*, *a szekrényben / a szekrényre*), the a1-58
case errors fixed, and *Az övé / Az enyém* (two right answers) resolved.
No structure was broken and the check script is clean.

## 1. Change how you work (applies to B1 now)

- **Slow down.** A1 (185 files) took 14 minutes and A2 (263 files)
  18 minutes, about 2-4 seconds per exercise. That is not enough to read
  the lesson and grammar first, as the brief asks. Only 1.6% of A1 and
  4.5% of A2 exercises changed, and a sample of the untouched ones still
  has problems (section 3).
- **All exercise types.** In A2 every change was a dialogue or multiple
  choice: no fill-blank, writing, matching or sentence-builder exercise
  was touched. Review them too.
- **Use the questions file.** It is still empty after ~8,000 exercises.
  When you are not sure (is this Hungarian natural? are both options
  acceptable?), log it in `hu-review-questions.txt` instead of deciding.
- **New pattern to fix: fill-blank hints that contain the answer.** The
  hint in brackets must not *be* the answer:
  `Az ötlet valósággá ____ (became: vált).` → answer `vált`.
  Give the base form or a description instead: `(válik, past)`,
  `(to become, past)`. Counts: A2 119, **B1 642 of 1,179**, B2 95.
  (A hint that is the dictionary form is fine when the answer happens to
  equal it, e.g. `(olvas + she)` → `olvas`.)

## 2. Fix these A1-A2 changes (rule 1: exactly one right answer)

- `a2-96-dialogue-1`, `a2-60-dialogue-1`: the new wrong option *"Nagyon jó
  ötlet / Szuper ötlet, de sajnos nem érek rá."* is a perfectly good reply
  to an invitation. Replace with a near miss that is actually wrong
  (e.g. a wrong person or case).
- `a1-09-dialogue-1`: the prompt became *"Szia, Meg, hogy vagy?"* but the
  marked answer is still *"Nem értem. Még egyszer, légyszi."*, which
  doesn't answer "how are you". The lesson teaches asking for
  repetition, so the prompt must be something Meg plausibly didn't
  catch (a fast or long sentence), or the answer must change.
- `a2-89-practice-1`: new option *"Nem tudok, mert nagyon szeretek
  sportolni."* is nonsense and still describes a personal ability, which is
  what the question asks for. Use a general rule (*Itt nem szabad
  dohányozni.*) or another clear non-ability sentence.
- `a2-91-dialogue-2`: *"Mióta tanulsz itt?"* — *"2021-ben."* is a common,
  acceptable reply. Pick a clearly wrong form.

## 3. Missed in A1-A2 (from a sample of untouched exercises)

- `a2-191-dialogue-2`: *megkeresem a ____ a kabátzsebemben* —
  *kulcsaimat* and *kulcsomat* are both correct.
- `a2-181-practice-3` (`tetszenek` given in the hint),
  `a2-185-consolidation-17` (`adunk` given in the hint): see section 1.
- *Mennyi az ár?* (20 times in A1) and *Milyen a méret?* (5) are
  unnatural; the native speaker changed them to *Mennyibe kerül?* and
  *Milyen méretek vannak?* in a1-121…130. Use those forms everywhere.
- `a2-68-dialogue-1`: *Mikor érkezik a villamos?* — the marked answer
  *Tíz percenként jön.* (every ten minutes) doesn't answer "when";
  *Tíz perc múlva jön.* does.
- Prompts that depend on another step are still there, e.g.
  `a1-29-dialogue-2` *"És ők?"* (rule H6).

After B1, do one more pass over A1-A2 for sections 2-3 and the hint
pattern, then report.

---

# Round 2: review of B1 and the A1-A2 follow-up (2026-10-02)

Fixed well: all section 2-3 items above, and the hint leaks (B1 642 → 7,
A2 119 → 3). The hint rewrites are good.

## 4. Push your work

Your 19 commits (`1fb6118e` … `ef082b2c`) are only in the local
checkout; nothing reached origin. Origin has 3 newer commits (sync fix,
lesson goals). Run `git pull --rebase` and then `git push`. Also give
commit messages a body: `ef082b2c` has none.

## 5. Must fix: B1 replies with two right answers (64 exercises to recheck)

In B1 "choose the reply" exercises you replaced absurd wrong options
with **sensible alternative replies**. That breaks rule 1: the learner can
pick them and be right. Examples:

- *Ott hagytam a táskámat a vonaton!* — new wrong option *Nyugodj meg,
  mindjárt felhívjuk a talált tárgyak osztályát.* (a good reply)
- *Van közvetlen járat Pécsre?* — *Sajnos csak két átszállással tudsz
  eljutni oda.* (a good reply)
- *Hogy sikerült a szóbeli vizsgád?* — *Sajnos megbuktam, mert nem
  készültem eleget.* (a good reply)
- *Sikerül átadni a jelentést péntek délutánig?* — *Nem, sajnos
  túllépjük a megadott határidőt.* (a good reply)

In a reply exercise, a different *content* is almost always also a valid
reply. So the wrong options must be wrong in **form**: the right reply
with a grammar error on the lesson's point (wrong person, case, tense,
conjugation, word order), as you did well at A2 (*Petrán / Petrával
keresztül*). Or a reply that contradicts itself (*Igen, még nem jártam
Japánban.*). Never a different but sensible answer.

The 64 changed B1 reply exercises to recheck are listed in
`imports/review/b1-situational-recheck.txt`. Check each one against rule
1 and fix those that fail.

## 6. Broken fill-blanks (8, in B1)

The answer is already written next to the blank, so the solved sentence
doubles it: `Teljes mértékben meg_____bízom … (prefix)` → answer `meg`
gives *megmegbízom*. Remove the duplicated letters from the sentence:
`b1-27-03.ex05`, `b1-28-01.ex05`, `b1-29-01.ex05`, `b1-32-03.ex02`,
`b1-allamszervezet-02.ex07` (also has an empty `(over - )` hint), and
the rest found by searching for an answer that touches `___`.

## 7. Still

- The questions file is still empty after ~12,000 exercises. Use it.
- B1 went at ~15 minutes for 400 files again. Section 5 is what that
  speed costs.

---

# Round 3: review of B2 (2026-10-02)

B2 is the best level so far: absurd wrong options became real near misses
on the B2 grammar (*érdekében*, *arra hivatkozott*, *a milliárdszorosára*),
and most reply exercises follow the form-error rule. Pushed, checks clean.

## 8. Never rewrite a correct answer that is right

44 B2 correct answers were rewritten, apparently to show off the lesson's
grammar. **17 of them no longer answered the question** (*Miért nem
zongorával kezdik a Kodály-módszerben?* answered with Bartók collecting
folk songs; *Hol láthatom a Majálist?* answered with plein-air technique;
all three nemzetisegek and three demografia items). The reviewer restored
them (commit `86adda2b`). Rule: change a correct answer **only** when it
is wrong Hungarian or doesn't answer the question, and then make sure the
new one answers that exact question.

## 9. Correction to the hint rule (section 1): whole-word blanks

Dropping the Hungarian from the hint was right when the hint *was* the
answer, but for whole-word blanks it left English only, so synonyms are
now correct and get marked wrong: *(consent)* → *beleegyezését* or
*hozzájárulását*; *(solitude)* → *egyedüllét* or *magány*; *(became)* →
*vált* or *lett*. Fix, per exercise:

- If the answer is an **inflected** form, put the **dictionary form** in
  the hint, plus the grammar: `(beleegyezés, possessive + accusative)`,
  `(válik, past)`, `(egyedüllét)`.
- If the answer **is** the dictionary form, keep the English hint and add
  every other correct word to `answers` (a list), so synonyms are accepted.

313 such exercises (A2 106, B1 134, B2 73) are listed in
`imports/review/fill-blank-hint-recheck.txt` (id, sentence, answer).

## 10. Leftovers in B2

- 18 fill-blank hints still contain the answer; 36 time-word give-aways
  and 4 case suspects from `check-hu-exercises.py b2`. Fix or explain each.
- Word-order distractors at B2 must be clearly wrong: several are just a
  different but grammatical word order (*Rádöbbentem a vonat indulása
  után.* for *Mikor döbbentél rá?*). If the lesson is about focus, the
  wrong option must break the focus rule unambiguously.

---

# Round 4: review of C1 block 1 (ROADMAP 120, 2026-10-04)

Commits `976ca84b` and `2767a529`. **The best round so far.** 333
exercises changed in 72 files. Checks are clean, every commit was
pushed, structure is intact, and you logged 4 good questions. The absurd
wrong options (*aranyból készítik a kilincseket*) are now real near
misses on the content or form. Good models to repeat: `c1-03-02-dialogue-6`
(the blank carries the hedge, and the rest of the line rules out the
other options), `c1-03-01-dialogue-6` (*tanúsága szerint / tanúságával /
tanúságát tekintve*), `c1-04-01-dialogue-6`, and the fix in
`c1-03-05-practice-6` (*válasznál*). The lemma + ending hints
(`tanúság + -a`, `ragaszkodik, inf 3pl`) are clear.

## 11. Fix in block 1

- **`c1-01-01-practice-9`: wrong options pasted in.** The question is still
  *Why is 'holott' chosen instead of 'jóllehet' …?* but all three options
  were replaced with the options of `c1-01-05-practice-9` (*By
  methodically anticipating objections …*). The marked answer no longer
  answers the question. Write three options about *holott* vs *jóllehet*:
  the correct one (it stresses the contradiction between knowing and
  staying silent, with a note of blame) and two near misses about
  register or meaning. Whenever you replace every option of an exercise,
  read its question again before saving.
- **Two replies with more than one right answer (R1):**
  `c1-03-04-dialogue-6` (*Megbízhatunk a mérési adatokban?*: *Minden
  kétséget kizáróan megbízhatunk bennük …* and *Egyáltalán nem bízhatunk
  bennük …* are both sensible replies) and `c1-06-01-dialogue-6`
  (*Hogyan értékeli a választási eredményt?*: *kizárólag átmeneti
  kompromisszum* is as good an assessment as *egyértelmű vízválasztó*).
  Rebuild them like `c1-03-02-dialogue-6`: put the taught expression in
  the blank and give the line a second half that only it fits.
- **Synonyms missing from `answers`.** When the hint is English only, list
  every word a C1 learner could correctly write. Missed in the sample:
  `c1-02-consolidation-8` *tükrében*: add *fényében* (taught in
  `c1-01-04`). `c1-emlekezetpolitika-05-controlled-2` *elengedhetetlen*:
  add *nélkülözhetetlen*. `c1-06-02-practice-4` *tartás*: add *gerinc*.
  `c1-03-04-practice-4` *némiképp, valamelyest*: add *némileg*, *kissé*.
  `c1-03-consolidation-4` *minden bizonnyal*: add *valószínűleg*, as you
  did in `c1-03-02-practice-4`. Check every English-only hint in block 1
  again. That is about 70 exercises, and these five came from a sample
  of about 13.
- **A small one:** `c1-egeszsegugy-02-practice-4` *nem _____ meg* with
  the hint `megfoszt + -hatja` suggests *megfoszthatja*, but *meg* is
  already in the sentence. Give `foszt + -hatja (megfoszt)` instead.

## 12. Going on

Fix section 11, then do **blocks 2 and 3** and stop after block 3 to
report, with the same report as before. Keep the pace and the questions
file exactly as in block 1. Don't apply your own proposed changes from
the questions file before the native speaker answers
(`c1-05-04-controlled-2` already says *depressing*).

---

# Round 5: review of C1 blocks 2-3 (ROADMAP 120, 2026-10-04)

Commits `810dd6c6` … `abc24a66`. Section 11 is fixed well: the new
*holott* options, the two rebuilt replies and the block 1 synonyms are
all good. Blocks 2-3 are mechanically clean (0 errors, 0 suspects in
reviewed files), and most new wrong options are good near misses
(*hatályon kívül / érvényen felül*, *kivéve ha / tekintettel arra hogy*).

But the quality dropped in two places, the same way as at A1-B1: the
half-blocks came 6-17 minutes apart (about 1-2 seconds per exercise),
**no questions were logged** in 216 files, and three of the four commits
have no body.

## 13. English-only hints: the main problem (199 to recheck)

In blocks 2-3 you removed the Hungarian from 172 hints but added a
second accepted answer to only 21. In a sample of 30, about 12 were
wrong. Two kinds:

**a) A correct synonym is marked wrong.** *nyomán*: *következtében*.
*bármi*: *akármi*. *éppúgy*: *ugyanúgy*. *valószínűsíthetően*:
*valószínűleg*. *annak függvényében, hogy*: *attól függően, hogy*.
*zöldrefestés*: *zöldre festés*, *zöldmosás*. *Aggasztó (módon)*:
*Nyugtalanító*, *Riasztó*. *Miként … akként*: *Amint*. For every
English-only hint, ask: what else would a good C1 learner write here?
Put every correct word in `answers`.

**b) The English hint can't lead to the answer.** Function words and
correlatives can't be hinted in English:
- `c1-16-01-practice-4` *_____ dacára, hogy* (In spite of) → *Annak*.
  "In spite of" is already *dacára*.
- `c1-17-02-practice-4` *_____ … arra kell* (Where) → *Amerre*. "Where"
  suggests *Ahol*.
- `c1-kozlekedespolitika-consolidation-7` *Minél több …, _____ kevesebb*
  (the more) → *annál*. The English is wrong: it is "the less".

For these, give a Hungarian hint: `(az + -nak)`, `(correlative of
arra)`, `(minél … ___)`.

Do the whole list: `imports/review/c1-english-hint-recheck.txt`, a
worksheet. Write a `decision:` for every item (format at the top of the
file) before you change that exercise, and commit the filled-in
worksheet with the fixes. It holds 199 fill-blanks from blocks 1-3 with an English-only
hint and one accepted answer. Some really have only one answer (*Párizsi*,
*jogosult*): leave those. The rest get synonyms in `answers`, or a
Hungarian hint.

## 14. Correct answers (R2 again), and two replies (R1)

Three of the eight changed correct answers are wrong. Restore or rewrite:
- `c1-16-01-introduce-1`: *Mit jelent a 'deliberatív demokrácia'?* is now
  answered with *Az ellenfél érveinek elismerése mellett a saját álláspont
  finom hangsúlyozására*, another exercise's options pasted in (the same
  mistake as `c1-01-01-practice-9`). Restore the original answer and
  write two wrong options about democracy models.
- `c1-16-01-dialogue-6`: *érvelési fegyelem* was right and natural;
  *érvelési kompromisszum* is not a phrase. Restore *fegyelem*.
- `c1-geopolitika-01-introduce-1`: *hintapolitika* means swinging
  tactically between two great powers. That was the old answer. The new
  one (*az euroatlanti elköteleződés feladása a keleti autoriter
  rezsimek felé történő közeledésért*) is a political judgement, not a
  definition. Restore the original.

Two replies with a second right answer:
- `c1-mediakritika-02-dialogue-6`: *mindenkinek megvan a maga (saját)
  igazsága* is a stock phrase and fits. Replace *igazsága*.
- `c1-14-03-dialogue-6`: *az uniós irányelvnek való megfelelés* is fine
  Hungarian and makes sense. Use a form error (*taxonómiához*,
  *taxonómiával*) instead.

## 15. Going on

Fix sections 13 and 14 first, in one commit with a body. Then do
**block 4 only** and stop. From block 4 on, every hint you make English-only gets
an entry in the same worksheet (append it, with its `decision:`), so the
reviewer can see you considered the other correct words. Back to one block at a time until a block
comes back without these problems. Every commit needs a body: counts by
type, hints rewritten, synonyms added, correct answers changed (ids),
questions logged. If you log no questions for a whole block, explain
why in the report.
