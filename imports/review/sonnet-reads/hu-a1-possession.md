# Second read: hu a1 possession (Sonnet, 2026-10-10) — pilot arm B

Blind report-only read of the unit as it stands (`33be289d7`), checked and
filtered by Claude. This unit is a template stub: all ten grammar screens are
the same two placeholder screens copied into every lesson, the story
contradicts itself, and many items use forms taught much later. So this list
is mostly a rewrite plan. Also fix everything `check-content.py` reports
(`kié`, `-on`, *nekem* and the rest), which this list doesn't repeat.

"Met" follows `docs/unit-finish-brief.md` step 4. Never use: *-on/-en/-ön*
(`on-en-on`, taught a1-78; *az asztalon*), *nekem / neki / nekünk / nekik*
(taught a1-148), *megvan*, *ez a / az a* + noun (untaught in A1), *-ért*,
*-ból*. Location is *itt / ott van*.

## 1. Grammar screens: one point per lesson

Delete the five `a1-4x-b-gr` placeholder screens (files and their `grammar`
sections), except where noted, and rewrite the `a` screens. Each follows the
brief § 3 (text, a `table` for the paradigm, 3–5 examples using met words,
one tip).

- **a1-41-a, "My, your, his/her: -m, -d, -a/-ja, -e/-je".** Table for one
  owner: *kulcsom, kulcsod, kulcsa*; *táskám, táskád, táskája*; *könyvem,
  könyved, könyve*; *telefonom, telefonod, telefonja*. Say plainly: after a
  vowel the 3rd person is *-ja/-je* (*táskája*); after a consonant it is
  *-a/-e* or *-ja/-je*, and which one is learned with the word (*kulcsa*,
  but *telefonja*). *-m* and *-d* were met in a1-26; the new point is the
  3rd person.
- **a1-42-a, "Our, your (plural), their: -nk, -tok/-tek/-ötök, -uk/-ük".**
  Table for several owners: *szobánk, szobátok, szobájuk*; *barátunk,
  barátotok, barátjuk*; *családunk, családotok, családjuk*. After a vowel
  *-juk/-jük* (the *j* is part of the suffix, as in *-ja*). Don't claim that
  every vowel-final stem lengthens.
- **a1-43-a, "Mine, yours, his/hers: enyém, tiéd, övé"** (the `taught_in` of
  `possessive-pronouns-enyem`). *A kulcs az enyém.*, *A táska a tiéd?*, *Az
  autó az övé.*; *kulcsom* ("my key") against *enyém* ("mine"). Add *kié?*
  ("whose?") here and to `a1-43-voc.json`. Move *tiéd*, *övé* from
  `a1-44-voc.json` to `a1-43-voc.json`.
- **a1-44-a, "Ours, yours, theirs: miénk, tiétek, övék".** Same shape. Move
  *övék* from `a1-45-voc.json` to `a1-44-voc.json`. Keep **a1-44-b** but
  rewrite it as "Having: *Van egy …-m*" across persons without the dative:
  *Van egy autónk.*, *Van egy szobájuk.*, *Nincs kulcsom.* (`van-possessive-to-have`,
  met in a1-27; the new part is the other persons).
- **a1-45-a, "Saját: my own".** *Van saját szobám.*, *A saját kulcsom.*; one
  short screen. No *megvan*, no *minden … dolog*.

Retitle the lessons to match: a1-41 "His and Her Things", a1-42 "Our and
Their Things", a1-43 "Mine and Yours", a1-44 "Ours, Theirs and Having",
a1-45 "My Own Things" (keep the Hungarian half in the same style).
Vocabulary: replace *tulajdon* ("property") with a useful met-level word
the lessons use (or drop it); every listed word must be used in its
lesson's exercises.

## 2. Exercises

Rewrite every exercise that no longer fits its lesson's screen. Each lesson
drills its own point; *Van egy …* items go in a1-44 (and a1-45), not 41–43.
Specific faults to remove wherever they occur (including the consolidation
and the `review-*` items):

- **Word-salad wrong options** that break 2–4 things: *A kulcs ő van itt.*,
  *Kulcsa ő itt.*, *A telefon ő van asztalon.*, *Igen, kulcsa van itt a.*,
  *A szoba kicsi mi van.*, *Igen, barát itt van om.*, *A lakás itt van om.*,
  *Az autó enyém van.*, *Enyém az autó van.*, *miénk van*, *övé van*, *övék
  van*, *Van saját szoba van.*, *Saját szobám van egy.*, *barátnk*,
  *Táskája nagy ő.*, *Szobánk itt van ő.*, *Tiéd kulcs van.* A wrong option
  is a real form that fails one way: the wrong person (*kulcsod* for
  *kulcsa*), a missing suffix (*a kulcs*), the wrong pronoun (*az övé* for
  *az enyém*).
- **Who "he/she" is.** `a1-41-dialogue-1`, `-dialogue-2`,
  `a1-45-consolidation-13`: Károly talks about his own phone as *a telefonja*.
  His own things are *-m*; a 3rd-person item needs a third person in the
  prompt (*Hol van Anna kulcsa?* is untaught; use a line that names her:
  *Anna itt van. Hol van a kulcsa?*).
- **Meta questions** to replace with form items: `a1-41-controlled-3`
  (answer printed in the option), `a1-42-practice-1` ("vowel-final stems
  shift shape", false), `a1-43-practice-1` ("both are equally natural"),
  `a1-44-practice-1` (*ti(e) + -d*), `a1-45-practice-1` ("which sound gets
  inserted", false).
- **Second right answers:** `a1-44-controlled-2`, `a1-44-practice-2` (hint
  "yours": *tiétek* also fits; hint "yours (one person)");
  `a1-43-check-2` (*Az autó enyém.* is colloquially fine: use a clearly
  wrong option); `a1-45-dialogue-1` (*Kié …?* with no "they" in the prompt:
  name the owners).
- `a1-45-practice-2`, `-practice-3`, its speaking step: *Minden saját dolog
  megvan.* is unnatural and its `english` doesn't match. Replace.
- `a1-45-practice-7` substitution: `gloss` "room" → "their room".
- `a1-43-intro-2`: options *tiéd*, *övé* before their screen are fine once
  the screen is a1-43 (above).

## 3. Story `a1-unit-09`

Rewrite it with the same scene (Meg and Károly check their things before
leaving the flat), 80–150 Hungarian words, met words only: Károly's own
things are *-m* (*A telefonom itt van.*); keep Meg's bag hers throughout (it
is *az enyém*, later *a miénk* contradicts it); *tiétek* only to more than
one person; *az övék* only with a "they" in the scene; no *megvan*,
*tulajdon*, *asztalon*. Three comprehension questions on facts in the text.

## 4. Metadata

- "Which line does this reply answer" items: `a1-44-practice-5` is
  `grammar` / `possessive-pronouns-enyem`, the others `a1-possession-vocab`.
  Use the unit vocabulary where the options differ by content.
- After rewriting a dialogue's wrong option to a wrong-person form, tag it
  `possessive-suffixes` (no `distractor_skills`: same skill).
- `van-possessive-to-have` has 5 items, all in a1-45; with *Van egy …* in
  a1-44, it gets enough.
- Re-lock: `python scripts/lock_tags.py hu a1/possession --update --reason "..."`.

## 5. Goals, checklists, challenges

Every lesson has the same two generic lines. Write each lesson's own (from
its new screen), and a challenge for all six stems (none exist): A1 shape
from `docs/unit-finish-brief.md` step 3, `canDo` = the first checklist
line. The consolidation's lines name what the unit can do.

## Not taken (no action)

- *Dél-Afrikában* (a place name): fine.
- *címem* in `a1-43-practice-2`: met through a1-18 and the a1-26 rule.
- `distractor_skills` *telefonok*, *szobák* (`plural-nouns-k`): still fit.
- Single-option substitution items (a1-36 … a1-45): an engine-wide pattern,
  not this unit's.
