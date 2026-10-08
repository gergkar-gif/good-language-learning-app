# Task: remove the length give-away from Hungarian choice exercises (ROADMAP 130)

In these choice exercises the correct option is at least twice as long as
the longest wrong option (and 15+ characters longer). It is a full,
specific sentence next to short fragments, so a learner can pick it by
length without understanding anything:

    Eladó: Mit kér?
    Meg: _____
    * Kérek kenyeret, tejet és sajtot.
    - Hol van a piac?

Fix every listed exercise so that **no option stands out by its length or
its level of detail**.

This is the Hungarian counterpart of
`imports/review/ANTIGRAVITY-length-giveaway-es.md`, which you did for
Spanish. Its method (shorten / match / log), its rules and its review notes
carry over. **Read it first, including the review notes at the bottom**,
then this brief. Where the two differ, this brief wins.

Repository: this one (Parlour). Commit straight to `master` and push after
every commit.

## Scope: Hungarian exercise files, and only these

- Edit only the files listed in your worksheet block under
  `content/hu/exercises/`, plus your worksheet and
  `imports/review/hu-review-questions.txt`.
- **Don't touch `content/es-es/`, `content/es-latam/`, `skills/`, any
  `tags.lock.json`, or any `teaches`, `distractor_skills`, `category` or
  `stage` value.** Another agent is retagging Hungarian exercises in these
  same files (ROADMAP 144) and edits exactly those fields.
- Stage only the files you changed: `git add <path> …`, never
  `git add -A` or `git add .`. Run `git pull --rebase origin master` before
  you start a block and before each push. If it complains about local
  changes that aren't yours, or reports a conflict in an exercise file,
  stop and report. Don't stash, reset or commit anything that isn't yours.
- Not part of this task, even though the checker flags them:
  - the 14 `dialogue-complete` exercises in `a1-121` … `a1-150`, a native
    speaker reviewed them on 2026-10-01. Ids: a1-121-dialogue-1,
    a1-124-practice-5, a1-125-consolidation-13, a1-127-practice-5,
    a1-128-dialogue-1, a1-135-dialogue-2, a1-141-practice-5,
    a1-142-practice-5, a1-144-dialogue-1, a1-145-consolidation-13,
    a1-145-consolidation-14, a1-147-dialogue-1, a1-149-dialogue-1,
    a1-150-dialogue-1. After block 1 these 14 are the only A1 hits left;
  - `c1-21-*` and `c1-22-*` (being rewritten, ROADMAP 127). The checker
    skips them already.

## The worksheet comes first

`imports/review/hu-length-giveaway-worksheet.txt` has one entry per
exercise (586 entries; lesson and consolidation copies of the same
exercise are one entry), in five blocks:

| Block | Exercises |
|---|---|
| 1: A1 + A2 | 70 |
| 2: B1, first half | 149 |
| 3: B1, second half | 148 |
| 4: B2 | 55 |
| 5: C1 | 164 |

Each entry shows the question, the options (`*` = correct), **every file
the exercise appears in**, and its lesson. For each block:

1. Read every entry in the block and fill in `decision:` and `why:` (the
   format is at the top of the worksheet) **before** editing any exercise
   in that block. For each unit, read its lesson file first (the `lesson:`
   line) and, for reading questions, its story: you need to know what the
   learner has met and what the text actually says.
2. Apply exactly what the worksheet says, in every file listed.
3. Run the checks, commit, push, **stop and report**.

The reviewer compares the diff with the worksheet entry by entry. An
option changed without a matching decision, or a decision not applied,
counts as an error. Your report counts are checked too, so count, don't
estimate.

**Start each block in a fresh chat.** Re-read this brief, the Spanish brief
and the review notes at the bottom of this file first. **Do block 1 only,
then stop.** The reviewer tells you when to start block 2.

## How to fix one

Choose **one** of these, as in the Spanish brief:

1. **shorten**: cut the correct option down to the key point, in the same
   style as the wrong options. The usual fix for reading questions and
   fact questions.
2. **match**: rewrite the wrong options into equally long, equally specific
   options that are clearly wrong. Use it when the length *is* the point
   (a grammar item that needs a full sentence, a dialogue reply that would
   no longer fit its line if cut short).

Aim for options whose lengths are close. Going just under 2× is not
enough: the correct option should no longer be the obviously fullest one.

## Hungarian-specific rules (these are the risk here)

You are writing Hungarian that nobody checks before it ships. A new option
that is wrong Hungarian *by accident*, or a new "wrong" option that is
actually fine, is worse than the give-away it replaces.

1. **Every word you write must be certainly correct Hungarian.** Case
   endings (*a postán*, not *postába*; *az állomásra*), vowel harmony
   (*-hoz/-hez/-höz*), definite vs indefinite conjugation, the focus
   position before the verb, agreement, accents and long/short vowels.
   If you are not certain of a form, don't use it.
2. **Build wrong options by breaking exactly one thing.** Take the correct
   sentence, or a sentence of the same shape, and break the point the
   exercise teaches (`teaches` says which): wrong person, wrong case
   ending, wrong tense where the context allows only one, wrong connector.
   Don't compose long free-standing sentences, that is where invented
   Hungarian goes wrong. For reading and fact questions make the wrong
   option **false according to the text** (a changed fact), not just
   different.
3. **Exactly one right answer, and say why.** The `why:` line must state
   why the marked option is the only acceptable one. Watch for synonyms
   (*heti / hetente*, *kedvezmény / akció*), for replies that are fine in
   another register, and for options that are true but "less complete".
4. **Don't swap one give-away for another.** No time word that clashes
   with the tense (*tegnap* with a future verb), no absurd, rude or
   off-topic lines, no *Nem tudom.* (it answers anything), no absolutes
   (*soha*, *mindig*, *semmi*) when the correct option is the only
   moderate one. At A1 a harmless off-topic reply is acceptable when a
   near miss would be too subtle for a beginner, **as long as it isn't a
   sensible reply**.
5. **Level-appropriate vocabulary.** At A1/A2 keep new options to words
   the learner has met in that unit or earlier. At B1 and above, keep the
   register of the original.
6. **Two-option exercises** (44 entries, mostly dialogue replies): there is
   one wrong option, so `match:` gives one text. It must be a reply that
   does not fit the prompt, but not an absurd one.
7. **The correct option must still fit.** After shortening it must answer
   the exact question, fit the dialogue line, and keep the fact the
   question asks about. A shortened answer that no longer answers the
   question is worse than the give-away.
8. **Keep conventions.** If options carry an English gloss in square
   brackets, every new or shortened option gets one too, translated
   literally, errors included. (None of the current hits have glosses, but
   check.)
9. **Don't change structure.** `id`, `type`, `teaches`,
   `distractor_skills`, `category`, `stage`, `correct` and the order of
   options stay as they are. Don't touch the `question` or `prompt`, except
   to fix a number mismatch your change creates.
10. **Keep formatting.** Edit the JSON in place, non-ASCII as-is, each
    file's own indentation, so the diff shows only changed option lines.
11. **When unsure, log it and leave the exercise unchanged.** Write
    `decision: log` and add the exercise to
    `imports/review/hu-review-questions.txt` in that file's format (`###`
    id and file, `why:`, `current:`, `proposed:`). Fewer, certain fixes
    beat many risky ones.
12. **Other defects.** If an exercise on your list has a different defect
    (the marked answer doesn't answer the question, two right answers,
    prompt that depends on another step; see
    `imports/review/ANTIGRAVITY-exercise-quality.md`, H1-H7), fix the
    length give-away only if the exercise is then fully correct. Otherwise
    `decision: log`, and name the defect in the logged `why:`. Known one:
    `a1-09-dialogue-1` (prompt asks how Meg is, marked answer is "Nem
    értem. Még egyszer, légyszi."), see
    `imports/review/hu-review-feedback-a1-a2.md` § 2: log it. Don't go
    looking for defects in exercises that aren't on your list.

## Checks before each commit

Run the checker for the level(s) of your block, and the other two:

    python imports/review/check-slash-giveaway.py --length hu a1 a2 --list
    python imports/review/check-hu-exercises.py a1
    python scripts/validate-content.py --changed

(`check-hu-exercises.py` takes one level at a time: run it for each level
in your block.) None of the ids in your block may still appear in the first
list, except `decision: log` entries, and for A1 the 14 excluded
`a1-121…150` ids. `check-hu-exercises.py` must report `errors: 0`. The
validator must pass; its tag warnings are known and not yours.

Commit per block, e.g.

    fix(hu/a1-a2): remove the length give-away from 70 choice exercises (ROADMAP 130)

The body gives: shorten count, match count, log count, and the ids where a
correct option was changed (all `shorten` ids).

## The report at each stop

- the block's counts (shorten / match / log), counted from the worksheet;
- every id where the **correct option** changed;
- every id where you also fixed a second give-away or defect (rule 12);
- every logged question, with its `why`.

Do not edit ROADMAP.md or ACHIEVED.md. The reviewer does.

---

## Review notes

(The reviewer adds notes here after each stop. Read them before starting
the next block.)

### Block 1 (A1 + A2), reviewed 2026-10-07

Commit `a1471d26`. The mechanics are right: all 70 decisions are applied
exactly as written in every listed copy (74 exercise copies changed, all
identical where they are the same exercise); nothing outside the worksheet
changed; no `teaches`, `category`, `stage` or `correct` value moved; no
block 1 id is still flagged except `a1-09-dialogue-1` (logged) and the 14
excluded `a1-121…150` ids; the validator passes; the counts in the report
(4 shorten / 65 match / 1 log) are correct. The four shortenings are good,
and so are the grammar near misses (*Két szobák van.*, *A sport vagyok
jó.*, *A konyhába megyek.* for *Hol vagy?*). Keep doing that.

**Fix these in a separate commit before you start block 2** (edit the
worksheet entry as well, so it still matches the files, and log nothing
twice).

1. **"Sajnos" is now a tell.** 14 new wrong options contain *Sajnos* (an
   unhappy off-topic reply) and none of the correct options does:
   a2-100-dialogue-1, a2-101-dialogue-1, a2-127-dialogue-1,
   a2-130-dialogue-1, a2-146-dialogue-1, a2-157-dialogue-1, a2-46-dialogue-1,
   a2-51-dialogue-2, a2-73-dialogue-2, a2-80-consolidation-7,
   a2-89-dialogue-2, a2-92-dialogue-1, a2-96-dialogue-2, a2-97-dialogue-2.
   Rewrite them without *Sajnos*, and not as another stock "bad news"
   line. Prefer what rule 2 says: the correct reply with one point broken,
   or a reply that answers a neighbouring question (*Mi a foglalkozásod?*
   → *Hétfőtől péntekig dolgozom.* style, same tone as the correct
   option). Across the whole of block 2 onward, don't let one opener or one
   mood mark the wrong option.
2. **Absolutes and absurd lines (rule 4).** These new wrong options give
   themselves away by *csak / kizárólag / bármilyen / egyáltalán nem /
   semmilyen / nyugodtan / completely / never*, or by being cartoonish.
   Replace each with a plausible near miss that is wrong because it is
   **false**, not because it is extreme (a different real document, a
   different real step, a neighbouring fact): a1-42-practice-1,
   a2-50-controlled-4, a2-180-consolidation-14, a2-180-intro-1,
   a2-210-intro-1, a2-211-intro-1, a2-214-check-1, a2-214-controlled-4,
   a2-215-check-1, a2-215-intro-1, a2-217-intro-1, a2-217-intro-2,
   a2-218-check-1, a2-218-controlled-4, a2-220-check-1, a2-220-controlled-4
   (*jeges fürdőzés*, *hideg fagylalt*), a2-210-intro-2, a2-211-check-1,
   a2-214-intro-1, a2-212-check-1, a2-125-dialogue-1 (*sosem*),
   a2-70-dialogue-2, a2-75-consolidation-8, a2-90-consolidation-7.
   Dialogue ones need only lose the absolute or the stock phrase.
3. **a2-127-dialogue-2** (*Milyen volt a vicc?*): *Egyáltalán nem tetszett,
   mert nagyon drága volt.* is an opinion about the joke, so it arguably
   answers the question. Use a reply that gives no opinion about the joke.
4. **a1-27-practice-1**: *habok* is not a Hungarian word. Use a real form
   (a real verb or suffix that is wrong for "I have"), or `log`.
5. **a1-09-dialogue-1** is logged correctly, but its entry in
   `hu-review-questions.txt` says `proposed: KEEP`. Write a real proposal
   there (a prompt Meg plausibly did not catch, or a marked answer that
   answers *hogy vagy*), per `hu-review-feedback-a1-a2.md` § 2.

The wrong options in the 14 + 24 entries above are the only ones to
change. Don't touch the rest of block 1.

### Block 1 fixes, reviewed 2026-10-07

Commit `18762204`. All 40 changed exercise copies match the worksheet, no
correct option or non-option field changed, and the checker is back to the
logged `a1-09-dialogue-1` plus the 14 excluded ids. The rewrites are good:
no more *Sajnos* tell, and the post, bank and pharmacy distractors are now
plausible but false. **Carry this standard into block 2:** each wrong
option should be a different real fact, document, step or form, in the
same tone as the correct one, never an absolute, never a stock "bad news"
line.

### Block 2 (B1, first half), reviewed 2026-10-07

Commit `0e2aef36`. The mechanics are right: all 149 decisions (76 shorten /
73 match / 0 log) are applied exactly as written; the 149 changed exercise
copies are all in the worksheet; no `teaches`, `category`, `stage` or
`correct` value moved, and in every `shorten` the wrong options are
untouched; the validator passes; no block 2 id is still flagged. The
shortenings keep the fact asked for (checked against the stories, e.g.
*budai* in b1-09-05-reading-1 is in the Esti Kornél text). The "false, not
extreme" standard from block 1 held: no *Sajnos*-style tell, few absolutes.

**Fix these seven first, in a separate commit before you start block 3**
(edit the worksheet entries as well). Each is a new wrong option that is
arguably a second right answer (rule 3):

1. `b1-05-consolidation-9` (*Miért nem beszélsz Zsófival?*): the new wrong
   option *Mert teljesen más lett az érdeklődési körünk …* is a perfectly
   good answer to the question. Use a reply that does not give a reason for
   not talking to her.
2. `b1-12-05-practice-3` (*Mit kérdez a pincér a vacsora végén?*): *Ízlett
   az étel, vagy ajánlhatok még egy kis desszertet a kávé mellé?* is
   something a waiter really says near the end of a dinner. Use a question
   that belongs to the start or middle of a meal.
3. `b1-12-01-practice-4` (traditional Hungarian spices): *A fahéj, a
   vanília, a szegfűszeg, a kardamom és a szerecsendió* are all used in
   Hungarian baking. Use a list that is clearly not traditional Hungarian
   (as the other wrong option already is).
4. `b1-10-02-practice-4` (advantages of a condo): *a társasházakban sokkal
   nagyobb a csend és a nyugalom …* can be argued as an advantage. Make the
   claim clearly false or clearly a disadvantage.
5. `b1-10-05-controlled-1`: *… biztonságos lenne* can pass as a polite
   conditional after *az a legfontosabb szempont, hogy*. Keep *volt* (clearly
   wrong tense) and replace *lenne* with a form that is plainly wrong there.
6. `b1-04-05-dialogue-1`: *A helyedben te is mérlegelnéd …* ("you too")
   reads as nearly correct advice. Use a version whose error is clear, or a
   reply that is not advice.
7. `b1-04-03-practice-4`: *… inkább vársz egy kicsit, mint azonnal döntesz*
   is a blunt present-tense preference and could pass as correct. Keep the
   past-tense wrong option and make the other one clearly wrong (for example
   the wrong mood or wrong person).

Also, no action needed but keep in mind for block 3: in `shorten` entries
the correct option is sometimes still the shortest-but-noticeably-fuller
one (`b1-12-03-practice-4`: 21 characters against 12 and 11). That is under
the threshold, so leave it, but when you can pick a version closer in
length, do.

The wrong options in the 7 entries above are the only ones to change.

### Block 3 (B1, second half), reviewed 2026-10-08

Commit `70db33b3`. The mechanics match the worksheet: all 148 decisions
(48 shorten / 100 match / 0 log) are applied as written, nothing outside
the worksheet changed, no `teaches` / `category` / `stage` / `correct`
value moved, the validator passes and no block 3 id is still flagged. The
history and civics distractors are good: real, different, false facts, no
absolutes, no stock lines. Most shortenings keep the fact asked for.

**But one pair is broken, and the worksheet itself was wrong, so a
worksheet-versus-files check cannot catch it.** Two decisions were swapped
between neighbouring entries:

- `b1-honfoglalas-04.ex07` (*Miért volt jó hely az Alföld a magyaroknak?*)
  now has the correct option *Árpád fejedelemmel.*, which does not answer
  the question.
- `b1-honfoglalas-03.ex07` (*Kicsoda Árpád?*) now has wrong options
  *Mert a sűrű erdőségek elzárták …* and *Mert közvetlen tengerparti
  kijáratot …*, which are answers to *Miért*, not *Kicsoda*.

**Fix these four first, in a separate commit before you start block 4**
(edit the worksheet entries as well):

1. `b1-honfoglalas-04.ex07`: restore the correct option to an answer to
   *Miért* in the style of the wrong ones (*Mert füves, legelőkben gazdag
   terület volt.* or the original sentence). Keep the two wrong options
   (*Mert sűrű erdő borította.*, *Mert ott voltak a legnagyobb városok.*).
2. `b1-honfoglalas-03.ex07`: two wrong options that answer *Kicsoda
   Árpád?* with a person, same length as the correct one and clearly
   wrong (for example a different real figure of the period, described
   in the same style).
3. `b1-matyas-05.ex06` (*Miért fontos Mátyás kora …?*): the shortened
   correct option lost its *Mert*, while both wrong options start with it,
   so it now stands out. Start it with *Mert*.
4. `b1-honfoglalas-consolidation.ex06` (*Melyik mondat kapcsol össze
   helyesen több szereplőt egy miután-tagmondattal?*): the new wrong
   option *Miután átkeltek a Kárpátokon, Árpád vezetésével vérszerződést
   kötöttek a pusztán.* is a grammatically correct *miután* sentence, so it
   is a second right answer to a grammar question. Make it wrong in the
   grammar (wrong conjunction use or wrong tense sequence), not in the
   history.

Also fix `b1-haromresz-05.ex08` (*Hogyan maradhatott fenn …?*): its
unchanged wrong option *Mert a török szultán kötelezővé tette a magyar
nyelvet.* starts with *Mert* under a *Hogyan* question, which is a tell
against the two other options. Rewrite it as a *how* answer that is false.

**New rule for blocks 4 and 5 (rule 13).** After you fill in a block's
decisions and again before you commit, read each new option next to **its
own question**: does a *Miért* question have only *Mert…* answers, a
*Kicsoda* question only people, a *Hány/Melyik évben* question only
numbers or years, a dialogue reply a reply to **that** line? Decisions
moved to the neighbouring entry are exactly the mistake the diff against
the worksheet cannot see.

### Block 4 (B2), reviewed 2026-10-08

Commit `9761fb22`. The mechanics are right and this block had no swapped
decisions (every new option was read next to its own question): all 55
decisions (9 shorten / 46 match / 0 log) are applied as written, nothing
outside the worksheet changed, no `teaches` / `category` / `stage` /
`correct` value moved, the validator passes, no B2 id is still flagged. The
distractors are the best so far: plausible, specific and false.

**Fix these three in a separate commit before you start block 5**
(edit the worksheet entries as well):

1. `b2-urbanusnepi-consolidation.ex08` (*native B2 placement of 'ellenben'
   and 'ezzel szemben'*): two of the three wrong options are acceptable
   Hungarian. *… ellenben Monoron …, az urbánusok ezzel szemben …* just
   swaps the two connectors, and *szemben ezzel* is a normal variant of
   *ezzel szemben*. Rewrite them so they are plainly wrong placements (for
   example *ellenben* at the end of the sentence or between the article and
   its noun, *ezzel szemben* inside a verb phrase). Keep the one that
   puts *ellenben* right after the first subject if you find it clearly
   wrong; if you are not sure it is, replace that too.
2. `b2-07-02-dialogue-2`: *Amennyire pontosabban figyelte …, annyira
   kevésbé …* can pass as a (clumsy) correlative. Replace it with a form
   that is plainly wrong (wrong correlative pair, or a comparative missing
   where the pair needs one). Keep *Minél pontosan …*.
3. `b2-35-04-controlled-3` (*Select the postposition that commonly pairs
   with 'érdekében'*): the question is itself malformed, since *érdekében*
   is in the stem and in the marked answer. Don't change the options: set
   `decision: log` (restore the original shortened option if you changed
   it, which you did, from *a fenntarthatóság érdekében (in the interest of
   sustainability)* back to that text) and add it to
   `hu-review-questions.txt` with a proposed rewritten question.

### Block 5 (C1), reviewed 2026-10-08

Commit `4bffe8f8`. The mechanics are right: all 164 decisions (all `match`)
are applied exactly as written, nothing outside the worksheet changed, no
`teaches` / `category` / `stage` / `correct` value moved, the validator
passes, and no C1 id is still flagged. Rule 13 held: no swapped decisions,
every new option fits its own question. The content is on topic, specific
and false, and the grammar items (*Minél … annál*, *ellenben*, participles)
are plainly wrong rather than stylistic variants.

**One systematic problem, which is the last item of ROADMAP 130.** The
"false, not extreme" standard slipped: in about 60 of the 164 exercises the
new wrong options are the extreme version of the correct one, with
*kizárólag*, *teljesen*, *semmilyen*, *egyáltalán*, *soha*, *végleg*,
*korlátlan*, *feltétel nélkül*, *kategorikusan* or *maradéktalanul*, while
the correct option is moderate. A learner can pick the moderate one without
understanding the topic, which is the same kind of shape cue this whole item
removes (it was the "Sajnos" tell in block 1).

**Fix these in a separate commit** (edit the worksheet entries as well).
For each id, reread the wrong options; where one of them carries such a word
and the correct option does not, rewrite that option as a *moderate-sounding
but false* claim, in the same tone and length (a different real mechanism,
body, date or concept, not "all / never / only"). The list is a candidate
list from a pattern search, so skip an id where the word is natural and the
correct option has one too:

c1-03-03-introduce-1, c1-14-03-check-8, c1-14-05-reading-4, c1-14-consolidation-9, c1-15-03-introduce-1, c1-15-05-introduce-1, c1-15-05-reading-4, c1-17-01-introduce-1, c1-17-03-introduce-1, c1-17-05-introduce-1, c1-17-05-reading-4, c1-17-consolidation-1, c1-18-01-introduce-1, c1-18-05-reading-4, c1-19-01-introduce-1, c1-19-04-introduce-1, c1-19-05-reading-4, c1-23-02-introduce-1, c1-24-01-introduce-1, c1-24-04-introduce-1, c1-24-05-reading-4, c1-27-02-introduce-1, c1-27-03-introduce-1, c1-28-01-introduce-1, c1-28-02-introduce-1, c1-30-02-introduce-1, c1-32-05-introduce-1, c1-33-02-introduce-1, c1-33-04-introduce-1, c1-34-02-introduce-1, c1-34-03-introduce-1, c1-35-02-introduce-1, c1-35-04-introduce-1, c1-35-05-introduce-1, c1-felsooktatas-05-introduce-1, c1-irodalmielet-03-introduce-1, c1-kiberbiztonsag-01-introduce-1, c1-kozlekedespolitika-02-introduce-1, c1-kozlekedespolitika-03-introduce-1, c1-kozlekedespolitika-04-introduce-1, c1-kulturalisorokseg-02-introduce-1, c1-kulturalisorokseg-03-introduce-1, c1-kulturalisorokseg-04-introduce-1, c1-kulturalisorokseg-consolidation-9, c1-magyarjovo-consolidation-9, c1-mediaszabadsag-02-introduce-1, c1-mestersegesintelligencia-01-introduce-1, c1-mestersegesintelligencia-03-introduce-1, c1-mestersegesintelligencia-consolidation-9, c1-mestersegesnyelv-02-introduce-1, c1-mestersegesnyelv-03-introduce-1, c1-mestersegesnyelv-05-introduce-1, c1-mestersegesnyelv-consolidation-9, c1-metaforak-02-introduce-1, c1-monetaris-03-check-8, c1-monetaris-04-introduce-1, c1-monetaris-04-check-8, c1-monetaris-consolidation-1, c1-tarsadalmireteg-05-introduce-1, c1-tudomanyosszabadsag-03-introduce-1, c1-tudomanyosszabadsag-05-introduce-1, c1-vitakultura-01-introduce-1, c1-vitakultura-consolidation-2

Also check `c1-15-03-introduce-1` (*feketedoboz-jelenség*): the wrong option
*… a fejlesztők szándékosan titokban tartják a forráskódot …* is a real
second meaning of "black box" (proprietary secrecy), so it can pass as a
correct answer. Make it plainly wrong.

Once this commit is in and checked, ROADMAP 130 is complete except for the
14 native-speaker-reviewed A1 ids, `c1-21-*` / `c1-22-*` (item 127) and the
logged items.
