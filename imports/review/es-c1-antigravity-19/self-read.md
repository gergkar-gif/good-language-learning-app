# Self-read: ES C1 core Unit 19 (`warnings-conditions`)

Applied **9 fixes** across 5 files via `apply_replacements.py` (`self-read-fixes.json`), then locked all 55 exercises (`lock_tags.py --update --reason "self-read"`).

## Findings fixed

1. **Unnatural Spanish phrasing (`c1-19-01-a-gr.json`):**
   - Replaced `*Como hayas borrado mi computadora, tendremos un problema*` ("deleted my computer") with `*Como hayas tocado mi computadora, tendremos un problema*`.
   - Fixed example 4, which had combined conditional `como vuelvas a retrasarte` and `de lo contrario` redundantly in the same sentence, to `"Tienes que llegar a tiempo; de lo contrario, no podremos contar contigo."`.
2. **Missing personal *a* (`c1-19-01.ex07`):** Fixed `perderemos el cliente.` → `perderemos al cliente.` in both `tiles` and `solution` of the `sentence-builder` exercise.
3. **Distractor quality (`c1-19-01.ex05`, `c1-19-01.ex08`, `c1-19-05.ex01`):**
   - Fixed impossible English time frame `"was delayed tomorrow"` in `c1-19-01.ex05` distractor → `"will be delayed tomorrow"` (cleanly isolating conditional `If` vs causal `Since`).
   - Replaced asymmetric option 4 in `c1-19-01.ex08` with a parallel sentence on `la entrega` and `el cliente`.
   - Replaced unnatural double-auxiliary distractor `Debí habría guardado` in `c1-19-05.ex01` with a realistic single-fault learner error (`Debería haber guardando`).
4. **House style & challenge alignment (`c1-19-03-a-gr.json`, `challenges.json`):**
   - Replaced ALL CAPS `ALWAYS` with bold `**always**` in Lesson 03's tip.
   - Replaced calque `"repeat the file"` (`repetir el archivo`) in `c1-19-02` challenge with `"redo the report"` (`repetir el informe`).
   - Aligned `c1-19-04` challenge scenario wording (`"detected"` → `"seen"`) with its target and English (`De haber visto` / `Had we seen`).

## Re-verification after fixes
- `check-content.py es-latam c1 warnings-conditions`: **0 errors, 0 suspects**
- `unmet-words.js` (`--with-hidden`): **0 unmet words**
- `check_es_c1_forms.py`: **0 hits before their screen**
- `check_unit_refs.py --bare --named`: **0 issues**
- `audit-reader-coverage.js --story c1-19`: **353 tokens, 0 missing from dictionary, 0 lookup throws**
- `render_lesson.js`: **0 `!!` lines**
- `validate-content.py --changed`: **25 passed, 0 failed** (1 es-es registry sync + 24 es-latam)
