# Report: ES C1 core Unit 19 (`warnings-conditions`)

Self-read: 9 fixes

## Summary
Authored ES C1 core Unit 19 (`warnings-conditions`, *"Warnings, conditions and threats"*) in `content/es-latam/` following `imports/review/es-c1-plan/notes/warnings-conditions.md` and `imports/review/es-c1-plan/antigravity/unit-19-warnings-conditions.md`.

### Skill & lesson structure
- **New skill:** `como-condicional-subjuntivo` (`taught_in` set to `c1-19-01-a-gr` via `set_planned_taught_in.py`; synced `skills/es.json` and `content/*/indexes/skill-registry.json`).
- **Lesson 01 (`c1-19-01`):** Warnings & threats with *como* + present/perfect subjunctive contrasted with causal *como* + indicative (B1 Unit 32), with explicit regional note (colloquial, more frequent in Spain; *si* more usual in Latin America). 10 items tagged `como-condicional-subjuntivo` across Lesson 01 and Consolidation.
- **Lesson 02 (`c1-19-02`):** Precision with *si*-clauses & mixed conditions (*si* + present/imperfect/pluperfect subjunctive; *por si acaso*) — recap `si-clauses` (B1 Unit 8) and `hypothetical-structures` (B1 Unit 4).
- **Lesson 03 (`c1-19-03`):** *A menos que* / *salvo que* (exception) vs *con tal de que* / *siempre que* (minimum condition) + subjunctive — recap `conditional-conjunctions` (B1 Unit 21).
- **Lesson 04 (`c1-19-04`):** Compact conditions without *si* (*de no ser así*, *de* + infinitive, *de haber* + participle, conditional gerund) — recap `implicit-conditionals` (B2 Unit 10).
- **Lesson 05 (`c1-19-05`):** Past regrets, reproaches & near misses (*debería haber*, *tendría que haber*, *me arrepiento de haber*, *si* + pluperfect subjunctive + conditional perfect) — recap `regrets-reproaches` (B2 Unit 10) and `pluscuamperfecto-subjuntivo-si` (B1 Unit 35) + original story `c1-19.json` (*Diez minutos antes de las cinco*, 353 tokens, featuring Carlos and an unnamed office colleague).
- **Consolidation (`c1-19-consolidation`):** 12 exercises across 7 types and all 8 unit tags.
- **Challenges:** 6 challenges added to `content/es-latam/curriculum/challenges.json` (5 `tier1`, 1 `tier2`).

## Checks
- `python scripts/check-content.py es-latam c1 warnings-conditions`: **0 errors, 0 suspects**
- `node scripts/unmet-words.js es-latam c1 --stems c1-19-01,...,c1-19-consolidation --with-hidden`: **0**
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: **0**
- `python scripts/check_unit_refs.py es-latam c1 warnings-conditions --bare --named`: **0**
- `node scripts/audit-reader-coverage.js es-latam --story c1-19 --top 0`: **353 tokens, 0 missing, 0 throws**
- `node scripts/render_lesson.js`: **0 `!!`**
- `python scripts/validate-content.py --changed`: **25 passed, 0 failed**
- `tags.lock.json`: **55 exercises locked** (`self-read`)

## For the user
None for Unit 19 — all notes, skills, and checks aligned cleanly.

---

## 4-Unit Block Summary (Units 16–19)

| Unit | Slug | Type / New skill | Self-read fixes | Checks (`check-content` / `unmet` / `c1_forms` / `unit_refs` / `render !!` / `reader-cov` / `validate`) | Locked exercises |
|---|---|---|---|---|---|
| 16 | `cities-housing` | Topic unit (notes drafted) | 33 | 0 err / 0 susp · 0 · 0 · 0 · 0 · 0 · 24/24 pass | 55 |
| 17 | `everyday-aspect` | New: `se-aspectual` | 20 | 0 err / 0 susp · 0 · 0 · 0 · 0 · 0 · 25/25 pass | 55 |
| 18 | `conversation-markers` | New: `marcadores-conversacionales` | 23 | 0 err / 0 susp · 0 · 0 · 0 · 0 · 0 · 25/25 pass | 55 |
| 19 | `warnings-conditions` | New: `como-condicional-subjuntivo` | 9 | 0 err / 0 susp · 0 · 0 · 0 · 0 · 0 · 25/25 pass | 55 |

### Items for the user across Units 16–19
- **Unit 16 (`cities-housing`):** Topic unit had no pre-existing notes file; drafted `imports/review/es-c1-plan/notes/cities-housing.md` before writing.
- **Unit 17 (`everyday-aspect`):** Lesson 02 taught accidental *se* (`se me olvidó`, `se le cayó`) as **NEW** rather than recap after confirming via repo search that no earlier screen in the course had taught it.
- **Next unit ready:** Unit 20 (`speculation-concession`) is next in a fresh chat.
