# ES C1 core Unit 31 (`art-criticism`): Antigravity report

- **Model & setting:** Antigravity (remote agent, standard)
- **Wall-clock time:** ~8 minutes
- **Allowance used:** not visible in this environment

## Files created / updated

- `imports/review/es-c1-plan/notes/art-criticism.md` (drafted unit notes)
- `imports/review/es-c1-plan/antigravity/unit-31-art-criticism.md` (unit brief)
- `content/es-latam/lessons/c1/c1-31-01.json` … `c1-31-05.json`, `c1-31-consolidation.json`
- `content/es-latam/grammar/c1/c1-31-01-a-gr.json` … `c1-31-05-a-gr.json`
- `content/es-latam/vocabulary/c1/c1-31-01-voc.json` … `c1-31-05-voc.json`
- `content/es-latam/exercises/c1/c1-31-01-ex.json` … `c1-31-05-ex.json`, `c1-31-consolidation-ex.json`
- `content/es-latam/stories/original/c1/c1-31.json`
- `content/es-latam/curriculum/challenges.json` (6 `tier1` challenges added via `add_challenges.py`)
- `content/es-latam/indexes/tags.lock.json` (55 exercises locked via `lock_tags.py`)
- `content/es-latam/indexes/word-lesson-index.json`
- `imports/review/es-c1-plan/lessons-learned.md`

## Per-lesson summary

- **c1-31-01** (`resultar-adjective`, recap B1 Unit 15): screen `c1-31-01-a-gr` (`grammar.c1.31.01.resultar`); 7 words (*el espectador, desconcertante, evocador, sobrio, audaz, el claroscuro, descifrar*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-31-02** (`pasiva-estado-estar-participio`, recap B2 Unit 20): screen `c1-31-02-a-gr` (`grammar.c1.31.02.estar-participio`); 7 words (*la curaduría, el boceto, el lienzo, la instalación, la iluminación, articular, restaurar*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-31-03** (`superlatives`, recap B1 Unit 7): screen `c1-31-03-a-gr` (`grammar.c1.31.03.superlatives`); 7 words (*sumamente, la paleta, cromático, la textura, el trazo, la maestría, desigual*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `dialogue-complete`, `sentence-builder`).
- **c1-31-04** (`manner-clauses`, recap B2 Unit 32): screen `c1-31-04-a-gr` (`grammar.c1.31.04.manner-clauses`); 7 words (*el catálogo, la pincelada, el encuadre, la escultura, el grabado, el relieve, la vanguardia*); 8 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `dictation`, `dialogue-complete`, `structured-writing`).
- **c1-31-05** (`se-impersonal`, recap B1 Unit 6): screen `c1-31-05-a-gr` (`grammar.c1.31.05.se-impersonal`); 7 words (*la galería, la exposición, la cerámica, el carboncillo, el retrato, contemplar, apreciar*); 11 items (`matching`, `multiple-choice` ×2, `fill-blank` ×2, `listening-choice`, `reading` ×3, `dialogue-complete`, `sentence-builder`) + exhibition review `c1-31.json`.
- **c1-31-consolidation**: 12 items (`multiple-choice` ×3, `fill-blank` ×3, `listening-choice`, `dialogue-complete`, `dictation`, `sentence-builder`, `structured-writing` ×2) covering all 5 grammar skills + `c1-art-criticism-vocab` (6 tags).

## Unit text

- **Genre:** exhibition review (`c1-original-31`, *Materia y silencio: reseña de una retrospectiva municipal*)
- **Word count:** 464 Spanish words (5 paragraphs, 3 English comprehension questions)
- **Factual claims:** none about real people, artists, museums, works, dates, or statistics; entirely invented municipal museum retrospective with general, hedged aesthetic observations (high certainty).

## Norm claims

- `c1-31-01-a-gr`: "Use *de* only when a concrete subject precedes the verb (*La obra resulta difícil de descifrar*); when the infinitive itself is the subject, omit *de* (*Resulta difícil descifrar la obra*)."
- `c1-31-02-a-gr`: "Use *estar* whenever you describe how the exhibition or composition stands before the viewer, and reserve *ser* for the event of making, buying, or restoring it."
- `c1-31-03-a-gr`: "when a superlative evaluates the highest degree within a reviewer's experience, the relative clause usually takes the present perfect or present subjunctive (*Es la retrospectiva más ambiciosa que haya acogido este museo*, *Es el trazo más preciso que conozca el público local*)."
- `c1-31-03-a-gr`: "adjectives in *-co/-ca* change to *-quísimo* (*rico* → *riquísimo*), and adjectives in *-io* simplify *-i-* (*amplio* → *amplísimo*)."
- `c1-31-03-a-gr`: "watch the spelling change in *riquísimo* (never `*ricísimo*`)."
- `c1-31-04-a-gr`: "When *según* introduces a changing condition that has not been fixed in advance (*según varíe la luz*, *según se mire*), Spanish uses the subjunctive, not the indicative. By contrast, *tal como* citing a stated fact in a catalogue or wall text takes the indicative (*tal como señala el catálogo*)."
- `c1-31-05-a-gr`: "when *se* combines with a plural human direct object marked by *a*, the construction is impersonal and the verb **must stay singular** (*Se invita a los visitantes a detenerse*, *Se homenajea a las artesanas locales*, never `*se invitan a los visitantes*`)."

## Check results

- `check-content.py es-latam c1 art-criticism`: 0 error(s), 0 suspect(s)
- `unmet-words.js` (`--with-hidden`): 0 hit(s) (`[]`)
- `check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `check_unit_refs.py es-latam c1 art-criticism --bare --named`: 0 hit(s)
- `c1_known_forms.py art-criticism`: 0 form(s) not recapped
- `render_lesson.js`: 0 `!!` errors
- `validate-content.py --changed`: 24 passed, 0 failed
- `lock_tags.py`: locked `C1/art-criticism` (55 exercises)

## Unsure lines

- `c1-31-01-a-gr` table: *Resulta evidente admirar el claroscuro.* (unsure — slightly compressed collocation; reviewer may prefer *Resulta natural admirar el claroscuro* or *Resulta imposible ignorar el claroscuro*).

## For the user

- Nothing blocking; all checks pass cleanly.
