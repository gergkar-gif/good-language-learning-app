# Hungarian fill-blank translations: brief for Antigravity (ROADMAP 151)

> **Done 2026-10-09** (ACHIEVED.md 151). All levels have `english` and the HU
> schema now requires it. Kept as a record of the rules used.

You are adding the missing `english` line to Hungarian fill-blank exercises.
Read this whole file, then [AGENTS.md](../AGENTS.md) § "Exercise metadata" and
[course-generation-brief.md](course-generation-brief.md) § 6.4, before you change anything.

**A1 and A2 are done and reviewed (2026-10-09).** B1 (1,115) remains
as its own run. Pull before you commit.

## What is wrong

Every Spanish fill-blank has an `english` field: the whole sentence translated
with the blank filled in. The engine shows it after the learner settles the
answer, and as the second step of "Need a hint?" (after the first letter).
In Hungarian the field is optional, and **2,417 of 5,083 fill-blanks have
none**, so the learner gets no meaning after answering and the hint button stops
at the first letter.

When all of them have one, Claude makes `english` required in
`content/hu/schemas/exercises.schema.json`, as it is in Spanish.

## The list

```
python scripts/check-content.py hu a2      # or b1
```

lists every one under `missing-english`, by file and exercise id;
`--summary` gives the count. The count goes down as you work; the level is done
when it is 0. (`validate-content.py --warnings` lists the same ones for all
levels together, under `fill-blank without english`.)

## What to write

Add one field, `"english"`, to each listed exercise. Change nothing else.

- **Translate the whole Hungarian sentence with the blank filled in** by
  `answer` (or the first entry of `answers`). A suffix blank (`Magyarország_____`
  + `ban`) is translated as the full word (*in Hungary*).
- **Natural, plain English**, one sentence (or the same number of lines as a
  dialogue sentence, `A: … / B: …`), starting with a capital letter and ending
  with the sentence's punctuation. US spelling, as in the existing HU lines.
- **Match the `hint`.** If the hint is English (`at the weekend`, `my wife`),
  the translation uses those words for the blank. If it is a lemma plus grammar
  (`válik, past`), translate the form the answer actually is.
- **Pin the answer.** The English must fit every entry in `answers` and must
  not fit a different form: keep the person, number, tense and possessor of the
  answer (*my wife*, not *wife*; *had happened*, not *happens*).
- **Say what an English speaker would say, not word for word.** *Kérek egy
  kávét* is *I'd like a coffee*, never *I request a coffee*; *Holnap is
  találkozunk* is *We're meeting tomorrow too*, not *Tomorrow we also meet*.
  Pinning the answer means keeping its meaning and form, not its word order.
- **Hungarian has no gender.** A dropped or *ő* subject is *He/She* (as in the
  existing lines) unless the sentence or story fixes it (*Ő a feleségem* → *She is my wife*).
- **Translate only the Hungarian.** If the sentence starts with an English
  instruction ("Complete: …"), translate the Hungarian part only. Proper names
  stay as they are.
- **Never put the translation in `sentence`**, in brackets or otherwise. The
  validator fails a trailing `[English]` in a fill-blank sentence.

Examples:

| sentence | answer | hint | english |
|---|---|---|---|
| `Ő a ____.` | feleségem | my wife | She is my wife. |
| `A lámpa a tükör ____ van.` | előtt | in front of | The lamp is in front of the mirror. |
| `Úgy viselkedett, mintha semmi sem történ_____ volna.` | t | had happened | He/She behaved as if nothing had happened. |
| `Az ünneplők azért tűznek kokárdát a kabátjukra, ____ a szabadság eszméje eleven maradjon.` | hogy | so that | The celebrants pin cockades on their coats so that the idea of freedom stays alive. |

## How to edit

- Put `"english"` on its own line right after `"hint"`, or after `"sentence"` when
  there is no hint, with the same indentation. Edit the text of the file: do not
  load and re-dump the JSON, which reformats every array in the file.
- Do not change `sentence`, `answer`, `answers`, `hint`, tags, ids or order.
  Tags are locked; the validator fails a changed tag.
- **If an exercise looks wrong** (the answer doesn't fit, two answers fit, the
  hint gives the answer away, the Hungarian is unnatural), still write the
  translation of what is there, and add the exercise id and the problem to a
  list in your hand-back message. Don't fix it yourself.

## Checks before you hand back

1. `python scripts/validate-content.py --changed` passes.
2. `python scripts/check-content.py hu <level> --summary` shows `missing-english` 0.
3. Read 20 of your translations against their sentences at random.

## Records

- Commit per level (`content(hu): english lines for A2 fill-blanks (ROADMAP 151)`).
- Update ROADMAP item 151 with what is done; the run that finishes the last of
  A2 and B1 moves the item to ACHIEVED.md in the same commit (AGENTS.md §
  "Project records").
- Hand back with: counts per level, the "looks wrong" list, anything unclear.
