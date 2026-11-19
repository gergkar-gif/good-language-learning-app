# ES C1 Core Unit 22 (`tone-attitude`) — Writer Report

Self-read: 9 fixes (`imports/review/es-c1-antigravity-22/self-read.md`, `imports/review/es-c1-antigravity-22/self-read-fixes.json`).

## What was written
- **New skill taught:** `sufijos-apreciativos` (`taught_in`: `c1-22-01-a-gr`).
- **Recap skills:** `imperfecto-de-cortesia` (`c1-22-02-a-gr`), `superlatives` + `resultar-adjective` (`c1-22-03-a-gr`), `relative-clauses` (`cuyo`, `por/desde donde`) + `stance-adverbs` (`c1-22-04-a-gr`).
- **Content files:** 6 lessons (`c1-22-01` .. `c1-22-05`, `c1-22-consolidation`), 5 grammar screens (`c1-22-01-a-gr` .. `c1-22-05-a-gr`), 5 vocab files (`c1-22-01-voc` .. `c1-22-05-voc`), 6 exercise files (`c1-22-01-ex` .. `c1-22-consolidation-ex`, 55 exercises locked), 1 story (`content/es-latam/stories/original/c1/c1-22.json`, *La plaza de los cafés pequeños*, 435 words, descriptive sketch with Carlos and Meg), and 6 challenges in `content/es-latam/curriculum/challenges.json`.

## Norm claims
- `es-latam` only: no `vosotros` / `os` anywhere, no Spain-only vocabulary (`course_variants.py` clean).
- No unintroduced later-unit grammar (`leismo-laismo-reconocimiento` not used; `check_es_c1_forms.py` 0 hits).
- Only recurring course characters (Carlos, Meg) named in exercises, story, and challenges.
- All 6 challenges match their lesson's `checklist[0]` verbatim in `canDo` and use the `canDo` form in `target`.

## Checks after self-read
- `python scripts/check-content.py es-latam c1 tone-attitude`: **0 error(s), 0 suspect(s)**
- `python scripts/check-content.py --changed`: **no new errors**
- `node scripts/unmet-words.js es-latam --stems c1-22-01,c1-22-02,c1-22-03,c1-22-04,c1-22-05,c1-22-consolidation --with-hidden`: **`[]` (0 unmet words)**
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: **0 hit(s) before their screen**
- `python scripts/check_unit_refs.py es-latam c1`: **0 hits in Unit 22** (only pre-existing `c1-12-01-a-gr.json`)
- `node scripts/audit-reader-coverage.js es-latam --story c1-22 --top 0`: **0 not in dictionary, 0 literal compound guesses, 0 lookup throws** (435 tokens, 281 unique words)
- `python scripts/validate-content.py --changed`: **24/24 es-latam passed, 1/1 es-es passed, 0 failed**
- `python scripts/lock_tags.py es-latam c1/tone-attitude --update --reason "self-read"`: **55 exercise(s) locked**
