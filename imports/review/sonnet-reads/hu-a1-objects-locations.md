# Second read: hu a1 objects-locations (Sonnet, 2026-10-09)

Report-only read of the unit as Antigravity committed it unfrozen
(`32c36e88c`), checked and filtered by Claude. Fix every item below, re-lock
where tags change, then freeze. "Met" follows `docs/unit-finish-brief.md`
step 4.

Several of the length fixes in `32c36e88c` brought in unmet words to pad
options (*barista*, *mérnök*, *tanár*, *diák*, *Honnan jössz*). A length fix
still has to use met words; if no met option of the right length exists,
shorten the right answer or accept the suspect with a reason.

## Words and forms used before they are taught

- *tea* is in no vocabulary list before a1-111; before a1-21 it is only an example in the reading-unit screens, which is not "met". It is used in `a1-21-controlled-1`, `-practice-5`, `-practice-7`, `-dialogue-1`, `-writing-2`, `a1-25-consolidation-13`, `-16` and the a1-21 challenge target. Use met nouns (*kávé*, *könyv*, *telefon*, *víz*). `a1-21-practice-7` (*Ez nem kávé, ez egy ____*, hint "a hot drink") needs a new hint that pins one met noun.
- Unmet professions in wrong replies: *Ő egy tanár.* (`a1-21-dialogue-1`), *Ő egy barista.* (`a1-21-dialogue-2`, `a1-22-dialogue-1`), *Ő egy mérnök.* (`a1-22-dialogue-2`, `a1-25-dialogue-1`, `a1-25-consolidation-14`), *Ő egy diák.* (`a1-25-consolidation-13`). Use met replies that fail on meaning.
- *jössz* (taught a1-136): *Honnan jössz, Károly?* / *Honnan jössz te?* in `a1-23-practice-5`, `a1-24-practice-5`, `a1-25-practice-5`. Use met questions (*Mi ez?*, *Ki ő?*, *Hány éves vagy?*).
- *ez a* + noun as "this + noun" (*Mi ez a tárgy?*, *Mi ez a könyv?*) is never taught; a1-21 and a1-23 gloss *Ez a szoba.* / *Ez a lámpa.* as "This is the …". Same ruling as *az a* + noun in unit 3. Fix `a1-25-practice-4`, `-writing-2`, `-dialogue-1` and the story line: *Mi ez?* / *Mi az?*.
- `a1-22` screens: *sör* / *sörök* and *két könyv* use unmet words. Swap for met ones (*ház* → *házak*) and drop *két*.

## Misleading content

- `a1-22-a-gr`: *drop it when the object already has van* is wrong, and its own example is *Itt van egy könyv.* Fix the rule text (*egy* stays with *van*; leave the *nincs* case out unless the screen teaches it).
- `a1-22` plural / harmony screens: *könyv → könyvek* sits next to the rule that ö takes *-ök*, which predicts *könyvök*. `a1-22-practice-6` (*könyvek / könyvok / könyvak*) then tests the exception. Use a regular noun (*asztal*, *telefon*, *ablak*) in the table and in practice-6.
- `a1-23-practice-1` (*Which definite article goes with "ablak"?*: *az ablak / a ablak / az ablakok*): two options carry *az*, the third breaks the noun. Ask "How do you say 'the window'?" with *az ablak / a ablak / egy ablak*, `distractor_skills` `{"2": "indefinite-article-egy"}`.
- `a1-23-practice-6`: wrong option *A konyha a könyvben van.* is absurd. Use a sensible one-fault near miss.
- `a1-24-practice-6`: *Nem itt szék.* and *Itt szék nincs van.* are word salad (the second breaks several things). Use *Itt van szék.* (polarity) and *Ott nincs szék.* (place), each breaking one thing; record `distractor_skills` where an option is a real form of another skill.
- `a1-24-practice-8`: *Itt nincs ajtó.* differs in place **and** polarity. Use *Ott nincs ajtó.* and record `{"2": "van-and-nincs-there-is-there-isn-t"}` if it is that skill's form against a different `teaches`.
- `a1-24-practice-9`: `hint` repeats the whole `english` line (*There is no window here.*). Use `hint` "here".
- `a1-24-controlled-2`, `a1-25-consolidation-10`: `hint` "there" also reads as existential "there is"; *Itt* would fit. Use "over there".
- `a1-25-practice-6`: *Szoba ez van.* is word salad. Use *Ez van a szoba.* (copula, the skill it teaches) and *Az a szoba.* with `{"2": "demonstratives-ez-az"}` (or another one-fault option).
- `a1-24-b` tip: says "not *Van itt a könyv*", but `a1-24-dialogue-1` and `a1-25-dialogue-2` ask *Van itt egy asztal?* / *Van itt egy szék?*. Add one line: a yes/no question starts with *Van*.

## Metadata

- Harmony-variant choices are `vowel-harmony` (`docs/skill-tagging-spec.md` § Read-through conventions): `a1-22-practice-1` (*asztalok/asztalak/asztalek*), `a1-22-practice-6` (after its rewrite), `a1-25-practice-1` (*lakásban/lakásben/lakások*, keep `{"2": "plural-nouns-k"}`). Retag.
- `a1-25-practice-1`: the question's *(it has back vowels)* hands over the rule. Drop the parenthetical.
- `a1-21-controlled-1`: option *Mi* is a `ki-and-mi` form; record it, as `a1-21-practice-6` does for *Ki az?*.
- `a1-24-check-2`: "negative existential ('isn't there')" is jargon. Use "Which means 'there isn't'?".
- Re-lock after the changes.

## Goals, checklists, challenges

- `a1-25`: checklist line 1 / `canDo` "…combining this unit's location and plural patterns": nothing in the lesson or challenge uses plurals. Reword to what the lesson does (what objects are, where they are, whether they are there); copy into `canDo`.
- `a1-25-consolidation`: generic goal and checklist (*I can recognise the main language from this unit.*). Write its own two lines (a1-20-consolidation is the model) and copy the first into `canDo`.
- `a1-22` checklist line 2 (plural *-k*): only two choice items practise it. Add one plural fill-blank or soften the line.
- `a1-21` challenge: the scenario has Meg ask Károly, but the learner says both question and answer. Make the learner the one asking and answering ("You ask Károly what is on the table, then say what you think it is"), and replace *tea* in the target.

## Not taken (no action)

- Story *asztalon* and the story's *Micsoda ez?* order: stories may run ahead; the ending reads oddly but is a judgement call.
- `a1-24-check-1` (*van / vagyok / vagy*) tag: defensible as it stands.
- Builder alternative orders (*A konyhában van a telefon.*): ROADMAP 148(b), parked.
- `a1-23-practice-2` blank `___`, curly quotes in `a1-24-practice-8`, a1-23 examples using *a konyhában* before the article screen: cosmetic or ordering only.
- `a1-21-practice-1` options too easy: met and correct, fine.
