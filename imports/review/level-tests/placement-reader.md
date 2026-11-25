# Placement tiers B2/C1 review (es-latam, hu; es-es skimmed)

## Defects

1. content/es-latam/tests/diagnostic-test.json, es-diag-b2-03 (also in es-es if the same item is copied there)
   - "Busco a alguien que sabe hablar húngaro." is correct Spanish when the speaker has a specific person in mind. The screen b2-13-01-a-gr teaches exactly this contrast (Busco a alguien que me ayude vs. Encontré a alguien que me ayuda). So the wrong option "sabe" fits with a different sensible meaning.
   - Fix: use a negative antecedent, which forces the subjunctive, as the screen says.
   - old: `"sentence": "Busco a alguien que _____ hablar húngaro."`
   - new: `"sentence": "No conozco a nadie que _____ hablar húngaro."`
   - Options (sepa, sabe, sabrá, supo) stay. Apply in es-es too if the sentence is identical there.

2. content/es-latam/tests/diagnostic-test.json, latam-diag-b2-r02 and the passage of diag-rs-b2-es-latam
   - "ayuntamiento" is the Spain word. The latam file uses "alcaldía" elsewhere (a bike-share passage). es-es keeps "ayuntamiento" (3 uses there), so only the latam file needs changing.
   - old (passage): `el ayuntamiento ha decidido mantenerlo al menos un año.`
   - new: `la alcaldía ha decidido mantenerlo al menos un año.`
   - old (statement): `"statement": "El ayuntamiento ha decidido mantener el horario nuevo al menos un año."`
   - new: `"statement": "La alcaldía ha decidido mantener el horario nuevo al menos un año."`

## Possible defects (not sure)

3. content/hu/tests/diagnostic-test.json, hu-diag-c1-02 (feltéve, hogy)
   - The wrong option "ha" gives "feltéve, ha". This is attested in real usage, and some usage guides tolerate it. A strict grader could call it a second right answer. The screen c1-07-03 teaches only "feltéve, hogy" and "kivéve, ha".
   - Safer fix: replace the distractor "ha" with one that is plainly wrong.
   - old: `"hogy",
    "ha",
    "mert",
    "mint"` (the options list of hu-diag-c1-02)
   - new: `"hogy",
    "hanem",
    "mert",
    "mint"`

4. content/hu/tests/diagnostic-test.json, hu-diag-b2-07 (mintha)
   - "mintha mindent tud" (indicative) is wrong only by the screen's rule. The screen b2-31-02-a-gr requires the conditional. Colloquial Hungarian does use the indicative after mintha. I am not certain the standard rejects it, so I did not write a replacement. If you want zero risk, replace "tud" with "tudtak" (wrong person and number, so plainly wrong).
   - old: `"tudna",
    "tud",
    "tudjon",
    "tudott"`
   - new: `"tudna",
    "tudtak",
    "tudjon",
    "tudott"`

5. content/es-latam/tests/diagnostic-test.json, es-diag-c1-07 (low risk)
   - "seas" in "¡Ni que seas el único...!" is rejected by the screen (c1-21-01-a-gr), so it is fine for the course. Outside the course, "ni que" + present subjunctive has a concessive reading ("even if you are"), so it is not plainly wrong in every context. Optional: replace "seas" with "serías".
   - old: `"fueras",
    "eres",
    "seas",
    "serás"`
   - new: `"fueras",
    "eres",
    "serías",
    "serás"`

## Checked, no defect

es-latam: es-diag-b2-01, -02, -04, -05, -06, -07, -08, -09, -10; es-diag-c1-01 to -06, -08, -09, -10; latam-diag-b2-r01; latam-diag-c1-r01 and -r02. The C1 passage is fine.
Note on b2-10: it tests tanto...que, which is easy for B2, but it matches its screen b2-31-02-a-gr.

hu: hu-diag-b2-01 to -06, -08, -09, -10; hu-diag-c1-01, -03 to -10; hu-diag-b2-r01 and -r02; hu-diag-c1-r01 and -r02 (the false value 1 is right: the passage says efficiency barely changed).
Note on c1-01: the three wrong options are grammatical but contradict "egyértelműek, ezért", so they are wrong by meaning.

es-es: the B2 and C1 sentences, options and passages are word-for-word the same as latam. The only oddity is "ayuntamiento", which is correct in Spain.
