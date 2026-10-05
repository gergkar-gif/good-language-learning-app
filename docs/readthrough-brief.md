# Skill-tag read-through: subagent rule sheet (ROADMAP 125 step 3)

This is the only rules document you read. You get two units. For every exercise in them
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
- **Wrong-person options** generally → `present-tense-routine-language`, not the skill the
  sentence happens to contain. `ik-verbs-dolgozom-not-dolgozok` is only the 1st-person
  singular *-m* form (*dolgozom*).
- Thin skills are fine: don't stretch a tag to reach 6. A wrong tag isn't.
- **Slugs only from the lists at the end of the dump.** The list is frozen: never invent or
  rename a skill. A grammar point with no skill → the unit vocabulary skill, said in the
  report. The old tags came from bulk retags and are often wrong; don't trust them.
- **B1 has two tracks** (`core`, `citizenship`). A unit's vocabulary skill is its own;
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
