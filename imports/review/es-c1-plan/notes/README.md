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

Topics with real people, works and ideas (Units 27-35: history, migration, human rights, politics,
art, literature, philosophy, geopolitics, public speaking; added 2026-11-19):
- Texts and items name no living person, no politician, party, government or company, and invent
  no event about a real country. An invented setting is the default.
- Never quote a law, a speech, a poem, a philosopher or any real text: not from memory, not
  paraphrased as a quotation. Describe ideas in your own words ("some philosophers argue that…")
  only when the idea is widely known and stated without a name, a date or a figure.
- A real work or artist may be named only for a fact you are certain of (title, author, century);
  never retell its plot or describe scenes. Literature (Unit 32) is an essay on a genre or a way of
  reading, built on invented examples.
- Human rights and history: only general, uncontroversial statements; no figures, no dates you
  are not sure of; hedge judgements.

