# ES B1 core Units 65–76 (2026-11-12): the last core batch

Units (es-es numbers): 65 `reported-speech`, 67 `complex-opinions`, 69 `hypotheticals-possibilities`, 71 `independent-spanish` (reader A); 73 `present-perfect-subjunctive`, 74 `sequence-of-tenses`, 75 `verbs-of-becoming`, 76 `connectors-prepositional-regimes` (reader B). Two Sonnet readers, four units each (Units 73–76 are short: 63 items a unit, no story). Neither hit the usage limit.

| Reader | Tokens, minutes | Fixes proposed (per unit) | Rejected by check_fixes | Changed or added by the reviewer |
|---|---|---|---|---|
| A | 481,357, 28 | 337 (86 / 78 / 94 / 79) | 0 | 1 invented story sentence cut, 2 wrong recap units (*es posible que* is B1 Unit 25) |
| B | 459,982, 32 | 350 (90 / 85 / 85 / 90) | 0 | 1 ambiguous matching item, 1 invented character fact (Kaylee "became a teacher"), 37 words listed and 4 text fixes for unmet words its own check missed, 2 challenge words |

State: all eight frozen in es-es and es-latam. **The core track is complete: 40/40 units per course.** check-content 0 errors; accepted: three list words used only in a consolidation or by a scenario (accept.txt). Unmet words: *convertí* (es-latam, inflected). Walk 48/48 lessons per course. 48 challenges per course.

## Stories

- **El rumor de la calle del Correo**: labelled a Palma *tradición*, but found in neither Gutenberg collection nor any Wikisource series (`reviewer-facts.md`); relabelled as a pastiche; the narrator draws the lesson.
- **Dudas razonables**: an invented Clarín *palique* with readers' letters and quotations; now the narrator's own article in the present (no imperfect subjunctive after a past verb, no *sino que*).
- **Los ojos verdes** (Bécquer): retold to the Gutenberg text. No fiancée, Íñigo restored, the end as Bécquer wrote it; four *si hubiera …, habría …* sentences carry the unit's new grammar.
- **Cinco voces, una historia**: course text; only its questions rewritten.

## What the read found

- **Recap units presented as new everywhere** (65, 67, 71, 75; b1-40-01 re-taught `verbos-regimen-preposicional`): every screen now opens with what is known and from which unit.
- **b1-35-03 now teaches `pluscuamperfecto-subjuntivo-si`** (*si* + *hubiera* + participle, *habría* + participle, a paradigm table; the *-se* forms removed); 33 items retagged to it.
- **Later forms as wrong options** (present perfect subjunctive before b1-37, the future perfect) replaced in Units 69 and 71.
- Units 73–76 (another generator) had Spanish grammar jargon on screens and in vocabulary lists (*correlación, subordinada, espectro, maestría*), Spanish writing prompts, and *después de que* (B2) in b1-37-04: all rewritten.
- **Reader B's unmet-word counts were wrong** (reported 0–3 a unit; 21 hits in es-es and 24 in es-latam remained). The cause is unknown (a checkout without `imports/dictionary/` was tested and is not it); the reviewer's run caught it, and `unmet-words.js` now refuses to run when the lexicon or index fails to load.

## For the user

- **The ES B1 core track is done.** The `cultura` (es-es) and `latam` (es-latam) tracks are still parked: your decision.
- Orphan story files in the manifest, linked by no lesson: `b1-33.json`, `b1-34.json`, `b1-35.json`, `b1-36-pazosdeulloa.json`, `b1-37.json` … `b1-40.json` (plus the earlier ones). Delete or unlist?
- Thin B1 skills for the level checklist: `resultar-adjective` 4 items (both courses); latam-track skills `estar-a-punto-de`, `futuro-perfecto` (2 each, es-latam) and `relativo-posesivo-cuyo` (3, es-es).
- `-se` imperfect subjunctive forms are still accepted as alternative `answers` in some b1-38 fill-blanks (never shown); keep or remove?
- *por lo tanto* (A2 Unit 28 vs treated as B2), unchanged from the last batch.
