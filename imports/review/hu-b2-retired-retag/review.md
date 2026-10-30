# HU B2 clean-up before the read-through (2026-10-30)

## Retired skill slugs: 176 items retagged

The brief said 704 HU B2 exercises carried a retired slug. `validate-content.py
--warnings` lists 704 for **HU as a whole**: 176 are B2, 528 are C1 (32 `c1-*`
topic slugs in 23 C1 lesson groups). Only the B2 ones were retagged; C1 stays
for the C1 pass.

The 176 B2 items are in four units: Unit 59 `civic-participation-advocacy-public`
(b2-30, 59 items, `b2-abstract-case-government`), Unit 60 `ombudsman-civic-rights`
(b2-jogvedelem, 29), Unit 71 `mastery-voice` (b2-36, 59, `b2-mastery-synthesis`),
Unit 72 `speaking-hungarian-today` (b2-magyaridentitas, 29). Neither retired slug
has an alias, so nothing could be followed mechanically except one rule.

`scripts/retag_retired.py hu b2 decisions.json [--apply]` (new): open writing gets
the unit's vocabulary skill without a decision (24 items); every other item needs
a line in `decisions.txt`/`decisions.json`, or the script refuses. It also refuses a
retired or unknown slug, a skill above the level, a skill taught after the item's
lesson, and a `distractor_skills` entry naming the item's own skill or its right
option. `category` follows the new tag on choice, fill-blank and builder items.

How the 152 decisions were made (by what a wrong answer shows):

| Class | Tag | Items |
|---|---|---|
| governed case with a registry skill (*ragaszkodik -hoz*, *hivatkozik -ra*, *beszámol -ról*, *részesül -ban*, *helyt ad -nak*, *elszámol -val*, *bízik -ban*) | `verb-government-*` (B1/A2), with `distractor_skills` on wrong options that are other governed cases | 40 |
| a governed case with no skill (*eltekint -tól*, *ellen*, *iránt*), a supplied word, a connector no screen teaches as a skill (*jóllehet*, *következésképp*, *egyszersmind*, *mindamellett*, *szíveskedjék*), builders, mixed-fault dialogues, meta questions | the unit vocabulary skill | 91 |
| *mindazonáltal* (taught on b2-16-02-a, the skill's screen) | `contrastive-discourse-markers` | 5 |
| focus and preverb inversion | `b2-focus-inversion` | 4 |
| left-branching participial phrases | `participial-clauses` | 3 |
| conditional hedges (*indokolt volna*) | `diplomatic-softening` | 4 |
| *egyfelől … másfelől* | `egyreszt-masreszt` | 2 |
| *-va/-ve*; *papírra vetett sorok* | `participle-actions`, `past-participle-adjective` | 2 |

After: `validate-content.py --changed` passes; `--warnings` lists no B2 line
(HU: 704 → 528, all C1). These four units are read later in the pass; their
readers check every tag again, and many of these items will be rewritten (meta
questions such as "Report the archaic words to the police", garbled wrong options).

## *vármegye* / *főispán* (since 1 October 2026: *megye*, *kormánymegbízott*)

Every B2 hit was read in context (grep over `content/hu/**/b2`): *főispán* occurs
in no B2 file; every *vármegye* is historical and stays: the 19th-century classic
of Unit 49 (*A falu jegyzője*: Tengelyi, Viola, the county's nobility), Unit 59's
*Különös házasság*, Kossuth's county reports (b2-mediatortenet), the Diet's
language struggle (b2-nyelvujitas), cardinal laws of the historical constitution
(b2-alkotmanytortenet), Bartók in Csík county 1907 (b2-bartokkodaly), the 1830s
National Theatre (b2-szinhazmuveszet), the 1900s emigration (b2-diaszpora), Eötvös
Collegium graduates (b2-gimnaziumok), a count in a Mikszáth-style scene (b2-13-04),
*Úri muri* (b2-18) and *Anyám könnyű álmot ígér* (b2-27). Present-day B2 lines
already say *megye* (b2-21-04, b2-28-02, b2-19-03, b2-falutortenet-04,
b2-hatarontul-01, b2-nemzetisegek). No B2 edit was needed. The C1 files in the
same list (c1-08-05, c1-07-04, c1-egeszsegugy, c1-kozlekedespolitika,
c1-emlekezetpolitika) are left for the C1 pass. Readers of the B2 culture units are
told the rule, as present-day facts are checked per batch.
