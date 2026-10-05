# Skill-tag read-through: subagent rule sheet (ROADMAP 125 step 3)

> **Status:** the HU A2 brief as used, with its review notes appended. Before the next
> level, condense it into a one-page rule sheet per [readthrough-process.md](readthrough-process.md)
> (fold the review notes into the rules, drop step 1's spec/log reading, make it
> course- and level-neutral, and switch to two units per subagent).

You read every exercise of the units you're given and decide each one's single skill tag.
Work only in the repo `C:/dev/parlour-claude` (absolute paths). Never touch the
Google Drive checkout. Never run git write commands (no add/commit/stash/checkout/reset).
Set `PYTHONIOENCODING=utf-8` for every python command.

## Steps

1. Read this sheet; it holds every rule you need.
2. Dump the unit: `python scripts/readthrough_dump.py <course> <level> <unit id> > <scratch>/<unit id>.txt`
   and read ALL of it: grammar screens, vocabulary, every exercise, and the skill lists at the end.
3. For every exercise decide `teaches` (one slug), category if it must change, and
   `distractor_skills` (`ds`, option index → slug) for wrong options that are a
   well-formed form of another GRAMMAR skill.
4. Write `<scratch>/<unit id>.decisions.json`:
   `{"<exercise id>": {"teaches": "<slug>", "category": "<only if it changes>", "ds": {"1": "<slug>"}}}`
   — every exercise in the unit, none skipped.
5. Run `python scripts/readthrough_check.py <course> <level> <unit id> <scratch>/<unit id>.decisions.json`.
   Fix every error. Warnings: fix, or explain in your report why they stand
   ("taught later" is acceptable when the lesson's own grammar screen already teaches the
   form but the registry's `taught_in` points later — name the screen).
6. Content fixes: while reading, fix real defects directly in the unit's own files under
   `content/<course>/exercises/<level>/`, `content/hu/grammar/...` or vocabulary files of this unit
   (keep JSON formatting, 2-space indent, UTF-8, no other changes). Defects worth fixing:
   - a choice/dialogue item with two acceptable answers (make the wrong option clearly wrong);
   - a fill-blank that accepts one answer where several fit (add an English hint in a trailing
     parenthetical in `sentence`, e.g. `(on Tuesday)`, or add the alternatives via an
     `answers` array replacing `answer`);
   - the answer printed in the prompt; a wrong gloss; a wrong "correct" answer;
   - an item whose answer needs grammar or words not yet taught by that point (rewrite with taught material);
   - a consolidation item that copies a lesson item you fixed: apply the same fix to the copy.
   Don't rewrite items that merely could be better. Don't touch tags in the files — the
   decisions file carries them (`apply_tags.py` is run later by the reviewer).
   After editing, check the JSON still parses and re-run step 5.
7. Do NOT run apply_tags.py or lock_tags.py.

## Rules (summary; the spec wins)

- Tag by **what a wrong answer shows**. Word meaning → the unit vocabulary skill
  (`<level>-<unit id>-vocab`). A choice between paradigm members (all options are forms of one
  paradigm: persons of a verb, case endings of one noun, *-ban/-ba/-ból*) → that grammar skill.
  A gloss against mixed words stays vocabulary.
- Review items keep the skill they review (an earlier unit's vocab skill, or the grammar skill),
  not the lesson's new skill. In a review unit, matching takes the vocab skill of the unit its
  words come from.
- Category follows the tag on multiple-choice, fill-blank, sentence-builder and matching:
  vocabulary tag → `vocabulary`, grammar tag → `grammar`. `dialogue`, `writing`, `listening`,
  `reading` keep their category.
- An any-answer item or open writing with no single target → unit vocabulary skill.
- `ds` only for a well-formed form of another grammar skill; an ungrammatical option gets none;
  never point `ds` at a vocabulary skill or at the item's own `teaches`.
- Only use slugs from the lists at the end of the dump (A1/A2 grammar, this and earlier
  units' vocabulary). The skill list is frozen: never invent or rename a skill. If no skill
  fits a grammar point, use the unit vocabulary skill and say so in the report.
- The old tags came from bulk retags and are often wrong; don't trust them.

## Report (your final message, under 400 words)

- Tag counts (slug: n), category changes count, `ds` count.
- Judgment calls a reviewer should check (with exercise ids).
- Content fixes made (id: what and why, one line each).
- Defects left alone and why.
- Remaining check warnings and why they stand.

## Notes from reviewing earlier A2 units

- `-ig` items use `tol-tol` (`terminative-case-ig` is B1).
- No `ds` on meta-questions whose options are suffix names rather than word forms.
- `ds` must name the skill that actually owns that form; if unsure, leave it out.
- A dialogue or choice whose wrong option is also a sensible answer is a defect to fix.
- A fill-blank hint must pin the person too when the blank is a possessed or conjugated
  form (`(his family)`, `(I have a cousin)`), not just the bare word.
- A "Which means X?" whose wrong options include the `-s`/possessive/plural form of the same
  word is the grammar skill of that form, consistently across the unit.
- The *-ik* skill (`ik-verbs-dolgozom-not-dolgozok`) is only for the 1st-person singular
  *-m* form (*dolgozom*, *barátkozom*); other persons of an *-ik* verb are
  `present-tense-routine-language`. Wrong-person options generally →
  `present-tense-routine-language`, not the skill the sentence happens to contain.
- Don't stretch a tag to reach 6 exercises; a thin skill is fine, a wrong tag isn't.
- *ide/oda/innen/onnan* (the here/there series) → `itt-ott-here-there`; question words
  *hol/hová/honnan* → `spatial-questions-hol-hova`.
- Choosing the harmony variant of a suffix (*-hoz/-hez/-höz* as options, or *rendőrséghoz*
  as a wrong option on a choice) → `vowel-harmony`; a plain fill-blank producing the whole
  suffixed word → the suffix's own skill.
- "Which means *to eat*?" against other verbs is a gloss → vocabulary. A dialogue whose
  wrong option swaps in a different verb (*iszom* for *eszem*) fails on meaning →
  vocabulary; only a wrong form of the same verb points to its grammar skill.
- A dialogue whose wrong reply is a non-sequitur (answers a different question) fails on
  meaning → unit vocabulary skill, even when the right reply contains a grammar point.
  Only a wrong reply that differs in a FORM points to a grammar skill.
- An Igen/Nem contradiction in a dialogue (wrong reply "Nem, …" that affirms) → `yes-no-questions`.
- Matching pairs are always vocabulary, even when the pairs are two forms of a sentence.
- A multiple-choice/fill-blank/builder item whose category is `dialogue` or `writing` still
  follows the tag (set `category` to the tag's kind) — the check warns otherwise. Only
  dialogue-complete, structured-writing and listening TYPES keep their category.
