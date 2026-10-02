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
