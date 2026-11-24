# Review of content/es-latam/tests/c1-test.json (Spanish C1 test)

Each item was checked against the screen its `teaches` slug points to. I printed the screens for 20 of the 20 slugs. No item has two right answers, and no `correct` value is wrong. Three defects are worth fixing: one real, two minor.

## Defects

### 1. c1-se-aspectual: two wrong options are grammatical Spanish (real defect)
- **What is wrong.** The stem asks "¿Qué frase suena natural en español?". The options are bare, subjectless sentences. *Se comió pan.* and *Se bebió agua.* are well-formed passive/impersonal *se* sentences ("se bebió agua en abundancia"). A strong C1 learner can defend either as natural, so the item can have more than one right answer.
- **Why.** Screen c1-17-01-a-gr (Aspectual Se) says aspectual *se* is the point and that it does not go with a bare, unquantified object. The wrong options are wrong only on the aspectual reading, but the stem does not ask for that reading. A named subject removes the passive reading, so the same wrong options become clearly wrong. This is also the screen's own contrast: *Comió pan* against *Se comió el pastel entero*.
- **Fix, stem.** Old: `"prompt": "¿Qué frase suena natural en español?",`
  New: `"prompt": "¿Qué frase usa bien el se que indica que la acción se completó?",`
- **Fix, options.** Old:
```
        "Se comió el pastel entero.",
        "Se comió pan.",
        "Se bebió agua.",
        "Se leyó novelas."
```
  New:
```
        "Ana se comió el pastel entero.",
        "Ana se comió pan.",
        "Ana se bebió agua.",
        "Ana se leyó novelas."
```
- **Why the new options are safe.** With Ana as subject, *se comió pan* and *se bebió agua* can only be aspectual *se* on a bare noun, which the screen rejects. *Ana se leyó novelas* is the same case.

### 2. rs-c1 passage: Spain-marked vocabulary (minor, optional)
- **What is wrong.** The passage says *ayuntamiento* (twice) and *solicitar ayudas*. In most of Latin America a town's government is *alcaldía* or *municipalidad*, and subsidies are *subsidios* or *apoyos*. The passage already uses *computadoras*, so the Latin American register is set.
- **Why.** Brief point 6. *Ayuntamiento* is used officially in Mexico and the Dominican Republic, so it is not wrong, only marked. *Una planta entera* (line 486 and in the passage) is usable in Mexico and Colombia, so I leave it.
- **Fix 1.** Old: `Cuando el ayuntamiento anunció` New: `Cuando la alcaldía anunció`
- **Fix 2.** Old: `sorprendió al propio ayuntamiento` New: `sorprendió a la propia alcaldía`
- **Fix 3.** Old: `solicitar ayudas en línea` New: `solicitar subsidios en línea`
- **Check after editing.** These strings are inside one long `passage` line, so confirm each old string occurs once. Nothing else in the questions refers to *ayuntamiento* or *ayudas*.

### 3. ls-c1-04: evidence is not verbatim (cosmetic)
- **What is wrong.** The transcript says "Y muchas veces el problema no es tanto el volumen como sentir que el otro no te respeta." The evidence drops "muchas veces" and capitalises "El".
- **Fix.** Old: `"evidence": "El problema no es tanto el volumen como sentir que el otro no te respeta."`
  New: `"evidence": "Muchas veces el problema no es tanto el volumen como sentir que el otro no te respeta."`

## Borderline, no change required
- **c1-como-advertencia.** Screen c1-19-01-a-gr says *como* + subjunctive as a warning is colloquial and especially Spanish, and that Latin America prefers *si* + indicative. This is a recognition item and the screen teaches it, so it is acceptable. Do not turn it into a production item in this Latin American test.
- **c1-condicional-rumor.** The right option is the longest and the only one with "según". I do not call it a give-away, because options 2 to 4 are plausible readings.
- **c1-titular.** *Dimitirá pronto* as a reading of a present-tense headline is excluded only by the screen's convention (present for a past event). It is fine at the strength the screen states.
- **c1-partitivo.** The verb is fixed as *aprobó*. The screen allows singular or plural for partitives, but the options vary only the preposition, so this is safe.

## Checked, no defect
c1-infinitivo-compuesto, c1-dequeismo, c1-queismo, c1-gerundio, c1-derivacion, c1-condicional-rumor, c1-titular, c1-futuro-subjuntivo, c1-el-cual, c1-lo-cual, c1-colectivo (*la gente opinan* and *opinamos* are rejected per the screen), c1-partitivo, c1-de-lo-que, c1-de-las-que, c1-dislocacion-od (*le* for a thing is not accepted), c1-dislocacion-oi, c1-sentir, c1-suponer, c1-marcadores, c1-como-advertencia, c1-futuro-concesivo, c1-con-lo, c1-para-lo, c1-ni-que, c1-sufijos, c1-leismo.

Reading questions rs-c1-01 to rs-c1-06 are answerable from the passage, and their true/false/not-stated values (0, 1, 2) are right. The correct MC options are not guessable without the text.

Listening questions ls-c1-01, 02, 03, 05 and 06 are answerable from the transcript, and their evidence matches it. ls-c1-04 is also correct (value 1); only its evidence wording is in defect 3.

Writing task `es-c1-writing` and speaking task `es-c1-speaking` ask for things a C1 learner can do, and their keywords are natural. Two notes, no change needed: *vamos* can match the everyday phrase "vamos a…" in the speaking answer, and the writing keywords do not include *será*, which the prompt itself suggests.
