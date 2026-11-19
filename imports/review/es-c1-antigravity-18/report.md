# Report: ES C1 core Unit 18 (`conversation-markers`)

Self-read: 23 fixes

## Summary
Authored ES C1 core Unit 18 (`conversation-markers`, *"Conversation and spoken markers"*) in `content/es-latam/` following `imports/review/es-c1-plan/notes/conversation-markers.md` and `imports/review/es-c1-plan/antigravity/unit-18-conversation-markers.md`.

### Skill & lesson structure
- **New skill:** `marcadores-conversacionales` (`taught_in` set to `c1-18-01-a-gr` via `set_planned_taught_in.py`; synced `skills/es.json` and `content/*/indexes/skill-registry.json`).
- **Lesson 01 (`c1-18-01`):** Pan-Hispanic spoken discourse markers (*pues, bueno, mira/mire, oye/oiga, o sea, vamos, ¿no?, ¿verdad?*) with *tú* vs *usted* register and recognition note for regional markers (*vale, órale, che, dale*).
- **Lesson 02 (`c1-18-02`):** Buying time, softening excuses & steering (*a ver, es que, ir al grano, sin rodeos, salirse del tema, volver al tema, el inciso*) + recap of `refutacion-no-es-que-sino` (B2 Unit 5) in casual *No es que* + subj., *es que* + ind.
- **Lesson 03 (`c1-18-03`):** Agreeing, hedging & pushing back (*puede que* + subj. vs *a lo mejor* + ind.; *ni hablar, desde luego, por supuesto, qué va, asentir, el diálogo*) — recap `subjunctive-doubt` (B1 Unit 13).
- **Lesson 04 (`c1-18-04`):** Live retelling of speech — same-day/same-place non-shift vs later-day shift (*la anécdota, el oyente, la locutora, la emisora, el micrófono, soltar*) — recap `discurso-indirecto-deicticos` (B2 Unit 17).
- **Lesson 05 (`c1-18-05`):** Spoken stance openers (*a decir verdad, para ser sincero/a, con franqueza, en todo caso, dicho esto*) — recap `stance-adverbs` (B2 Unit 1) + original radio interview transcript `c1-18.json` (*El pan de cada mañana*, 351 tokens).
- **Consolidation (`c1-18-consolidation`):** 12 exercises across 7 types and all 6 unit tags (`marcadores-conversacionales`, `refutacion-no-es-que-sino`, `subjunctive-doubt`, `discurso-indirecto-deicticos`, `stance-adverbs`, `c1-conversation-markers-vocab`).
- **Challenges:** 6 challenges added to `content/es-latam/curriculum/challenges.json` (5 `tier1`, 1 `tier2`).

## Checks
- `python scripts/check-content.py es-latam c1 conversation-markers`: **0 errors, 0 suspects**
- `node scripts/unmet-words.js es-latam c1 --stems c1-18-01,...,c1-18-consolidation --with-hidden`: **0**
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: **0**
- `python scripts/check_unit_refs.py es-latam c1 conversation-markers --bare --named`: **0**
- `node scripts/audit-reader-coverage.js es-latam --story c1-18 --top 0`: **351 tokens, 0 missing, 0 throws**
- `node scripts/render_lesson.js`: **0 `!!`**
- `python scripts/validate-content.py --changed`: **25 passed, 0 failed**
- `tags.lock.json`: **55 exercises locked** (`self-read`)

## For the user
None — all notes, skills, and checks aligned cleanly.
