# ES C1 core Unit 28 (`migration-identity`) — Antigravity report

- **Model & setting:** Gemini 4 Neon (Medium)
- **Wall-clock time:** ~12 minutes (09:19–09:31)
- **Allowance:** not visible in environment

## Files created / updated

- Notes: `imports/review/es-c1-plan/notes/migration-identity.md`
- Brief: `imports/review/es-c1-plan/antigravity/unit-28-migration-identity.md`
- Lessons: `content/es-latam/lessons/c1/c1-28-01.json` … `c1-28-05.json`, `c1-28-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-28-01-a-gr.json` … `c1-28-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-28-01-voc.json` … `c1-28-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-28-01-ex.json` … `c1-28-05-ex.json`, `c1-28-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-28.json`
- Challenges: 6 `tier1` entries added to `content/es-latam/curriculum/challenges.json`
- Tag lock: 55 exercises locked in `content/es-latam/indexes/tags.lock.json`
- Index: `content/es-latam/indexes/word-lesson-index.json`

## Per-lesson summary

- **c1-28-01** (`conectores-temporales-narrativos`, recap B2 Unit 2 + B1 Unit 1): screen `c1-28-01-a-gr`; words: *la travesía, el migrante, el consulado, el permiso de residencia, la acogida, acoger*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-28-02** (`gerund-periphrases`, recap B2 Unit 24 + B1 Unit 18): screen `c1-28-02-a-gr`; words: *arraigarse, el acento, el bilingüismo, la asimilación, la red de apoyo, la segunda generación*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-28-03** (`perifrasis-llegar-a-infinitivo`, recap B2 Unit 25): screen `c1-28-03-a-gr`; words: *el forastero, la lengua materna, echar raíces, el apego, la hospitalidad, el recelo*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-28-04** (`concesivas-por-mas-que`, recap B2 Unit 8): screen `c1-28-04-a-gr`; words: *la nacionalidad, la patria, el refugio, el compatriota, retornar, la permanencia*; 8 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-28-05** (`counterfactual-wishes`, recap B2 Unit 16 + B2 Unit 15): screen `c1-28-05-a-gr`; words: *la añoranza, el reencuentro, la tierra natal, la sobremesa, la panadería, el muelle*; 11 items (`multiple-choice` ×2, `matching`, `fill-blank` ×2, `listening-choice`, Reading `multiple-choice` ×3, `dialogue-complete`, `structured-writing`).
- **c1-28-consolidation**: 12 items covering all 5 grammar skills + `c1-migration-identity-vocab` (`multiple-choice` ×3, `matching`, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing` ×2).

## Unit text

- **Genre:** first-person testimony (*crónica*)
- **Title:** *Entre dos orillas: crónica de una panadería en el puerto*
- **Word count:** 567 words
- **Factual claims:** none (entirely invented coastal port city, unnamed neighbourhood bakery, and general reflections on migration, bilingualism, and belonging; no real person, country, institution, date, or statistic).

## Norm claims

- `c1-28-01-a-gr`: *Whenever the main clause looks ahead to the future, Spanish requires the subjunctive (*apenas reciban*, *conforme lleguen*).*
- `c1-28-02-a-gr`: *the auxiliary (*ir* or *venir*) agrees with the grammatical subject. Use the singular for a singular subject (*se va perdiendo el acento*) and the plural for a plural subject (*se van mezclando los acentos*, *se vienen conservando estas recetas*).*
- `c1-28-02-a-gr`: *with verbs like *arraigarse* or *adaptarse*, the pronoun may stand before the auxiliary (*se fue arraigando*) or attach to the gerund (*fue arraigándose*, with a written accent). Both are standard; fronting *se* is more common in speech.*
- `c1-28-03-a-gr`: *Do not drop the preposition *a* between *llegar* and the infinitive: write *no llegó a entender* and *había llegado a echar raíces*, never *no llegó entender*.*
- `c1-28-04-a-gr`: *Never use *muy* before a noun.* / *nouns require *por mucho, mucha, muchos, muchas*, *por poco, poca, pocos, pocas*, or *por más* (*por mucha distancia que haya*, never *por muy distancia que haya*).*
- `c1-28-04-a-gr`: *When referring to a real, completed fact in the past, the indicative is also possible in chronicles, though the subjunctive remains the standard choice whenever the amount is framed as irrelevant.*
- `c1-28-05-a-gr`: *all three require the subjunctive, never *habría* or *podría*.*
- `c1-28-05-a-gr`: **¡quién!* in a wish always governs the third-person singular verb (*¡Quién pudiera!*, *¡Quién hubiera sabido!*), even when the speaker means 'I'. Never conjugate it in the first person (*¡Quién hubiéramos!* is ungrammatical), and never use the conditional (*¡Quién podría!*).*

## Checks

- `python scripts/check-content.py es-latam c1 migration-identity`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-28-01,c1-28-02,c1-28-03,c1-28-04,c1-28-05,c1-28-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `python scripts/check_unit_refs.py es-latam c1 migration-identity --bare --named`: 0 recap reference(s) to check
- `python scripts/c1_known_forms.py migration-identity`: 4 basic forms not separately recapped (*cuando*, *mucho*, *poco*, *por más* — *por más que* is recapped from B2 Unit 8)
- `node scripts/render_lesson.js es-latam c1-28-01 ... c1-28-consolidation`: 0 `!!` errors; targeted review caught and fixed 7 defects (acceptable-Spanish distractors in `c1-28-02.ex06`, `c1-28-04.ex06`, `c1-28-consolidation.ex02`, `c1-28-consolidation.ex03`; two-fault distractor in `c1-28-05.ex01`; unanchored tense in `c1-28-02.ex03` and `c1-28-consolidation.ex05`; prompt wording mismatch in `c1-28-consolidation` challenge).
- `python scripts/lock_tags.py es-latam c1/migration-identity --update`: locked 55 exercise(s)
- `python scripts/validate-content.py --changed`: es-latam 24 passed, 0 failed

## Unsure Spanish lines

- None.

## For the user

- None.
