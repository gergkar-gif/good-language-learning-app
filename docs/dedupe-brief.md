# Dedupe rewrite: subagent rule sheet (ROADMAP 143 / small-fixes pass)

Goal: in one unit, every lesson should practise its own material. Exact copies of an
exercise in several lessons of the same unit (the same question, options and answer in
lessons 01–05) are replaced by new exercises that test the same skill with that
lesson's own words, grammar screen and story. The learner's north star: each lesson
must teach and check something that lesson introduced.

Work only in `C:/dev/parlour-claude` (absolute paths); no git writes; set
`PYTHONIOENCODING=utf-8` on every python command. Never run `apply_tags.py` or
`lock_tags.py`.

## Steps

1. `python scripts/dup_report.py <course> <level> <unit id>` lists every copy: its
   lesson, id, `copy_of` (the first occurrence, which stays), type, `teaches` and content.
2. `python scripts/readthrough_dump.py <course> <level> <unit id>` shows each lesson's
   grammar screen, vocabulary and story. Read the lesson of each copy before writing.
3. Rewrite each copy **in place** in `content/<course>/exercises/<level>/<stem>-ex.json`
   (keep the file's line endings and 2-space indent; change only the listed exercises):
   - **Keep:** `id`, `type`, `category`, `teaches`, `distractor_skills` (and the option
     index it points at, if you keep the same number of options). Tags must not change.
   - **Replace:** the content (question/sentence, options, answer, hint, english line,
     pairs, tiles, prompts) with a new item that tests the same skill in the context of
     *that lesson* (its screen's examples, its vocabulary list, its story characters).
   - Where the copy is a matching, listening, dictation or sentence-builder, change the
     words, not the format.
4. Rules the new items must follow (same as the read-through):
   - exactly one grammatical/correct option; a wrong option must not be a valid answer
     (free word order, optional subject, a present for the future, colloquial forms);
   - fill-blank answers needing a person carry a person in the hint or the English line;
     the parenthesised hint must not be the answer; sentence-builders need an `english`
     prompt; no grammar the course teaches later; a wrong dialogue reply must not be a
     valid answer to its question;
   - the new item must differ from every other item of the unit (check with step 6);
   - one option must not be much longer than the others.
5. Spanish: `es-es` and `es-latam` share the exercise ids and text; make the identical
   edit in both courses (the unit `vosotros` and the `vosotros`/`ustedes` choices are
   the only es-es-only things; use *ustedes* in shared items). Hungarian: `hu` only.
6. Re-run `python scripts/dup_report.py ...` (it must list nothing for the unit) and
   `python scripts/readthrough_check.py <course> <level> <unit id> <decisions.json>`
   is NOT needed (tags are unchanged), but run
   `python scripts/validate-content.py --changed` once at the end and report any error.
7. Report: unit, number of copies replaced, any copy you left (and why), anything
   in the first occurrences that looked wrong, validator result.
