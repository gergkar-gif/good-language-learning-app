# Skill-tag read-through: subagent rule sheet (ROADMAP 125 step 3)

This is the only rules document you read. You get two units, in Hungarian (`hu`) or
Spanish (`es-es` + `es-latam`, see § Spanish; the examples in the rules are Hungarian,
the Spanish section says how each applies). For every exercise in them
you decide one skill tag, fix real content defects, and report. Work only in
`C:/dev/parlour-claude` (absolute paths); never touch the Google Drive checkout; no git
writes; set `PYTHONIOENCODING=utf-8` on every python command. Never run `apply_tags.py`
or `lock_tags.py`.

## Steps (per unit)

1. `python scripts/readthrough_dump.py <course> <level> <unit id> > <scratch>/<unit id>.txt`
   and read ALL of it: grammar screens, vocabulary, every exercise, and the skill lists at
   the end (the only slugs you may use).
2. Decide `teaches` (one slug), `category` (only if it must change) and `ds`
   (`distractor_skills`: option index → slug) for every exercise; none skipped. Write
   `<scratch>/<unit id>.decisions.json`:
   `{"<exercise id>": {"teaches": "<slug>", "category": "<only if it changes>", "ds": {"1": "<slug>"}}}`
3. `python scripts/readthrough_check.py <course> <level> <unit id> <that file>`. Fix every
   error. Fix each warning or say in the report why it stands.
4. Fix content defects (below) in the unit's own files under
   `content/<course>/exercises/<level>/`, its grammar screens or vocabulary files (2-space
   indent, UTF-8, nothing else changed). Don't touch `teaches` in the files; the decisions
   file carries tags. Re-run step 3 after editing.

## Tagging rules

- **Tag by what a wrong answer shows.** A word's meaning → the unit vocabulary skill
  (`<level>-<unit id>-vocab`). A choice between members of one paradigm (persons of a verb,
  case endings of one noun, *-ban/-ba/-ból*, harmony variants of a suffix) → that grammar
  skill. A gloss against mixed words stays vocabulary. A fill-blank that produces the whole
  suffixed word → the suffix's own skill; a choice between its harmony variants →
  `vowel-harmony`.
- **Review units and review items** keep the skill they review (the earlier unit's
  vocabulary skill, or the grammar skill), not the lesson's new skill.
- **Category follows the tag** on multiple-choice, fill-blank, sentence-builder,
  sentence-order and substitution: vocabulary tag → `vocabulary`, grammar tag → `grammar`,
  even when the old category was `dialogue` or `writing`. `dialogue-complete`,
  `structured-writing`, `dictation` and `listening-choice` keep their category.
- **Matching is always vocabulary** (the checker errors otherwise), even when the pairs are
  two forms of a sentence. In a review unit it takes the vocabulary skill of the unit the
  words come from.
- **Reading** (`category: reading`, comprehension questions about a story) stays untagged:
  `{"teaches": null}`. If a reading item actually tests a form or a word, change its
  `category` and tag it as usual.
- **History/civics fact questions** (citizenship track: who, when, why) are `category: reading` and untagged, like any
  comprehension question; only an item that defines or glosses a unit word is vocabulary.
- An item any answer passes, and open writing with no single target → the unit vocabulary
  skill.
- **Dialogues:** a wrong reply that answers a different question, or contradicts the
  prompt in meaning, fails on meaning → unit vocabulary skill; a wrong reply differing in a
  FORM (person, tense, case) → that form's skill. A wrong *Nem, …* that affirms (or *Igen, …*
  that denies) → `yes-no-questions`.
- **`ds`** only for a wrong option that is a well-formed form of another GRAMMAR skill (a
  present form where the past is needed, another case's suffix); an ungrammatical option
  gets none. Never `ds` at a vocabulary skill or the item's own tag; none when the options
  are suffix names or patterns ("Which suffix?"); if unsure of the owning skill, leave it out.
- **Wrong-person options** (Hungarian) generally → `present-tense-routine-language`, not the skill the
  sentence happens to contain. `ik-verbs-dolgozom-not-dolgozok` is only the 1st-person
  singular *-m* form (*dolgozom*).
- Thin skills are fine: don't stretch a tag to reach 6. A wrong tag isn't.
- **Slugs only from the lists at the end of the dump.** The list is frozen: never invent or
  rename a skill. A grammar point with no skill → the unit vocabulary skill, said in the
  report. The old tags came from bulk retags and are often wrong; don't trust them.
- **HU B1 has two tracks** (`core`, `citizenship`). A unit's vocabulary skill is its own;
  citizenship history/civics comprehension is `reading` (untagged) or vocabulary, never a
  grammar skill it doesn't test. "Taught later" means the skill's `taught_in` screen comes
  after this lesson: if one of this unit's own screens teaches it, say which in the report
  (the reviewer fixes the registry).
- A skill above the unit's level is an error (a B2 slug on a B1 item): retag by what the
  item really tests.

## Content defects worth fixing

- a choice/dialogue item with two acceptable answers (make the wrong option clearly wrong);
- a fill-blank accepting one answer where several fit: add alternatives via an `answers`
  array replacing `answer`, or pin it with an English hint in a trailing parenthetical that
  names the person for a conjugated or possessed form (`(his family)`, `(I closed)`);
- the answer printed in the prompt (the checker warns), a wrong gloss, a wrong "correct"
  answer, a "which means X?" whose options include another form of the same word;
- an item whose answer needs grammar or words not yet taught, or that asks about the
  lesson's story before the learner reaches it (rewrite it to test material already shown);
- a consolidation item that copies a lesson item you fixed: apply the same fix to the copy.

Don't rewrite items that merely could be better.

## Report (final message, under 400 words, per unit)

Tag counts (slug: n), category changes, `ds` count; judgment calls to check (exercise ids);
content fixes (id: what and why); defects left alone and why; warnings that stand and why.

## Worked examples

- *Which means "back then"?* `akkoriban / később / most` → unit vocab skill, category
  `vocabulary`.
- A choice whose options are *megy / menjen / ment* for "(that) he go(es)" → the
  `-jon/-jen` grammar skill, with `ds` on the present and past options.
- Dialogue reply "Igen, utálok főzni." against "Nem, utálok főzni." → `yes-no-questions`.
- Pairs of Hungarian sentence and English → matching → unit vocab skill.
- *Which suffix …?* with options `-ban / -ból` → grammar skill, no `ds`.

## Spanish (es-es + es-latam)

One registry (`skills/es.json`) and one set of exercise ids serve both courses, so **one
decisions file covers both**. Run the dump and the check with `es-es`; the dump ends with
the exercises whose text differs in `es-latam` (usually *vosotros* vs *ustedes/ellos*), and
the check errors on an id missing from either course. The tag must fit both versions; if
the two would need different tags, say so in the report. List each content fix once and say
whether it applies to both courses or one. Unit tables are identical at A1 (no es-es-only or
es-latam-only units); stems are irregular (`a1-03c-01`, `a1-directions-01`,
`a1-reflexive-01`), the table order is the teaching order, and the dump marks each grammar
skill `[taught in this unit]` or `[taught LATER]` by that order.

- **A2 (added 2026-10-06).** Unit 33 `vosotros` exists only in `es-es`: the check's "missing from es-latam" error is expected there, so say so and continue. A2 vocabulary skills are `a2-<unit id>-vocab`. All verbal periphrases (*empezar a, dejar de, seguir + gerundio, llevar + tiempo + gerundio, acabar de, ponerse a, al + infinitivo*) are one skill, `perifrasis-verbales`; *cuando* + subjunctive is `cuando-subjuntivo`. Units 1–20 repeat a small set of tenses across many units (*pretérito perfecto, indefinido, ya / todavía*): tag by the form the wrong answer gets wrong (`preterito-perfecto`, `past-participles`, `ya-todavia-no`, `preterito-indefinido`), not by the unit's story. If an item tests something no A2 skill covers, tag the nearest skill, list it under judgment calls and do not invent a slug.

- **Paradigms.** A choice between persons or forms of one verb gets that verb's skill (`ser`,
  `estar`, `tener`, `ir`, `doler`, `gustar`, `querer-poder`, …); regular verbs get `ar-verbs`
  / `er-ir-verbs`; stem-changing verbs once taught get `stem-changes`. `present-tense`
  is the general present (first screen of the daily-routine unit); use it only when no more
  specific verb skill owns the form. Choosing the pronoun itself (*Which pronoun goes with
  hablas?*) is `subject-pronouns`.
- **`ds` for Spanish:** a wrong option that is a well-formed form of another taught skill
  (*es* where *está* is needed, *tiene* where *tienen*, *gusta* for *gustan*, a present form where
  `progressive` or `ir-infinitive` is needed). *Ella es en casa* is ungrammatical: no `ds`.
- **Articles, gender, agreement.** *el/la, un/una* chosen to match a noun's gender → `gender`;
  definite vs indefinite, or article vs none → `articles`; an adjective's ending →
  `adjective-agreement`; singular vs plural of a noun or adjective → `plural`.
- **Set chunks are vocabulary until their skill is taught.** *Me llamo*, *me gusta*, *mucho
  gusto*, *¿Y tú?*, *Aquí está*, *Hay* in a greeting-style item: if the item tests the chunk as a
  unit, tag the unit vocabulary skill. If it asks the learner to choose between forms of a
  skill that is `[taught LATER]` (*me gusta / me gustan*), the item is ahead of the course:
  tag the skill, list it under judgment calls.
- **Exception to the Sí/No rule: a unit's own contrast.** When the wrong replies in a dialogue differ in the contrast the unit teaches (*Sí, todavía no…* beside *Sí, ya…* in a *ya / todavía no* unit; *desde hace* vs *desde enero* in a *desde* unit), the item tests that grammar skill: tag the skill. Use the vocabulary skill only when the wrong replies differ just by Sí/No or an infinitive.
- **No Sí/No skill.** A wrong *No, …* that affirms (or *Sí, …* that denies) fails on meaning →
  unit vocabulary skill.
- **Pronunciation has no skill yet** (ROADMAP 133). A spelling or sound item → unit vocabulary
  skill, said in the report.
- **Vocabulary skills are per unit.** `a1-greetings-introductions-vocab` sits on about 270
  exercises outside unit 1 from an old bulk tag. Use this unit's own `a1-<unit id>-vocab`; the
  check warns when a vocabulary tag belongs to another unit (fine only for a true review item).
  The 2–6 old tags on an exercise are noise: decide one.
- **Fill-blank pinning.** Spanish drops the subject, so a blank like *___ en casa* may accept
  several persons: add the missing forms to `answers`, or pin it with an English hint naming the
  person (`(I am)`). *Tú/usted* and *vosotros/ustedes* variants both count when the course allows
  them.
- Worked examples: *Mi hermana ___ (tener) dos hijos* → `tener`; *El libro es ___ (rojo/roja)* →
  `adjective-agreement`; *¿Cómo se dice "brother"?* → unit vocabulary; *Ellos __ dos hijos*
  (`tienen / tiene / tengo`) → `tener`, no `ds` (every option is a form of `tener`); *Ella __ en
  casa* (`está / es`) → `estar`, `ds` `{"1": "ser"}` only if `es` is a well-formed answer to
  another question, which here it is not, so none.
