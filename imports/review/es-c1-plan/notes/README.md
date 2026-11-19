# Unit notes: how to write them (ES C1)

Each unit has `notes/<unit id>.md`, which `scripts/fill_c1_prompts.py` puts into the writer's
brief. Claude wrote the notes for every unit that teaches a new C1 skill (they carry the norm
rules checked against the RAE). A unit that teaches no new skill (its row in `../level-plan.md`
says "–") may get its notes from the writer, before writing the unit, in this exact shape:

```
Genre: <the genre in level-plan.md>
This unit teaches no new skill: every lesson recaps known B1/B2 skills at C1 density in <domain>
(screens open with "You know *X* from <Level> Unit N", the unit number taken from the knowledge
sheet, and add what is new at C1: how <domain> uses the form). Items are tagged with those skills
or `c1-<unit id>-vocab`.
Lesson plan:
- 01 <what the lesson lets the learner do>: recap `<slug>` (<level>): <2-3 Spanish examples in the domain>.
- 02 …
- 03 …
- 04 …
- 05 …: recap `<slug>` (<level>); plus the text and the Reading group.
Domain words: <the domain> (*word, word, …*); check each against the sheet first: a word an
earlier unit lists is used, never re-listed (`vocab-relisted` fails it).
Text: <genre> in an invented setting on <topic>: what it argues or reports; only general,
uncontroversial facts, hedged where they are judgements. No real person, institution, study,
statistic, or country (a country only when the topic needs it and every fact about it is certain).
```

Rules for choosing:
- Recap skills from `python scripts/c1_recap_candidates.py` (least used in C1 first, each with the
  unit that teaches it): pick five that suit the domain, at most one already used in 3+ C1 units.
  One skill per lesson; a lesson may instead be vocabulary-led (collocations, fixed expressions),
  tagged with the unit vocabulary skill: at most two such lessons a unit.
- Every recap lesson adds something the earlier screen did not teach (a C1 variant, a formal or written use, a contrast with a near form); first print that screen (`python scripts/show_screen.py es-latam <screen id>`) and name in the notes what is new. A lesson that would repeat the earlier screen whole is not allowed (Unit 10, 2026-11-19).
- Never a skill the sheet lists as later, hidden-only or C2, and never a new C1 skill of a later
  unit (the brief's "C1 forms not met yet").
- No norm claim in the notes that you cannot back with a source; if a lesson depends on one, pick
  another skill.
- Commit the notes file with the unit.
