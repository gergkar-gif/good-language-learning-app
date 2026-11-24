# ES C1 core: level checklist (2026-11-24)

Run on master after the last batch (docs/unit-pipeline-log.md § "Before calling a level done").

| Check | es-latam | es-es |
|---|---|---|
| Units frozen (`freeze_unit.py --status`) | 36/36 | 36/36 |
| `check-content.py <course> c1` | 0 errors, 0 suspects | 0 errors, 0 suspects |
| `validate-content.py --warnings`, C1 | none | none |
| `check_es_c1_forms.py <course> c1 --track core` | 0 | 0 |
| Story attribution (`story-attribution`) | 0 | 0 |
| Walk with challenges (`walk_lessons.js <course> c1`) | 216/216 | 216/216 |
| Library: C1 stories with no unit, not hidden | 0 | 0 |

Accepted at this check: two `listening-many-changes` suspects in Unit 6 (c1-06-01.ex05, c1-06-02.ex05:
each wrong option one plausible misreading, at the check's 10-word threshold; the check was added
after the unit was read).

How C1 core was made: 36 units, 216 lessons, 1,980 exercises a course; Units 1-7 by Claude writers,
8-36 by Antigravity; every unit norm-checked by the reviewer (screens' normative claims against RAE
material) and read by a Sonnet reader (Units 8-36: 18-64 fixes a unit, all applied); es-es planted
from es-latam with Spain's words (Unit 25 unconverted on purpose). Reviews: imports/review/es-c1-*.

Not covered by any of this: speaking steps (microphone), spoken challenge answers, wrong-answer
paths, real audio (TTS is stubbed in the walk), and a native speaker's eye. RAE entries were read
through search excerpts and secondary sources, not the full DPD/NGLE text (rae.es refuses automated
fetches).

Still to do before learners see C1 (for the user): a C1 level test (es-latam and es-es have none;
HU has `content/hu/tests/c1-test.json`); unhiding (remove `c1` from `HIDDEN_TRACKS` in
build-manifest.py); `engine/guide.js` says "Spanish A1–B2" twice.
