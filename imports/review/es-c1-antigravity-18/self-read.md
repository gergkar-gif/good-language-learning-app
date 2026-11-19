# Self-read: ES C1 core Unit 18 (`conversation-markers`)

Applied **23 fixes** across 11 files via `apply_replacements.py` (`self-read-fixes.json`), then locked all 55 exercises (`lock_tags.py --update --reason "self-read"`).

## Findings fixed

1. **First-person stance opener paired with 3rd-person report (`c1-18-05.ex01`, `c1-18-consolidation.ex06`):** `Para ser sincera, la panadera admitió...` and `Para ser _____, Carlos admitió...` misused a 1st-person speaker-oriented opener with a 3rd-person verb. Rewrote `c1-18-05.ex01` as direct 1st-person speech by *la panadera* (`Para ser sincera, el primer año en la panadería fue muy duro.`) and `c1-18-consolidation.ex06` as direct speech (`Carlos dijo: «Para ser _____, la entrevista me sorprendió mucho».`).
2. **Self-contradictory stacking of stance openers (`c1-18-05-a-gr.json`, `c1-18-05.ex03`, `c1-18-05` challenge):** Lesson 05's tip warns against stacking two stance openers back-to-back, yet example 4, `ex03`, and the challenge stacked `Dicho esto, en todo caso...`. Simplified all three to `Dicho esto, ...`.
3. **Single-fault distractors (`c1-18-01.ex01`, `c1-18-01.ex08`, `c1-18-04.ex01`, `c1-18-04.ex06`, `c1-18-04.ex08`, `c1-18-05.ex01`, `c1-18-05.ex11`, `c1-18-consolidation.ex01`):**
   - Replaced sentence-final `, pues.` in `c1-18-01.ex01` (acceptable in several Latin American varieties) with `, o sea.`.
   - Eliminated repeated-fault distractor pairs (`¿Verdad?` + `¿No?` in `c1-18-01.ex08`; `oiga` + `mira` in `c1-18-consolidation.ex01`) so every wrong option has a distinct fault.
   - Reduced double-fault distractors in `c1-18-04.ex01`, `ex06`, `ex08` and `c1-18-05.ex01`, `ex11` to one clean fault per option.
4. **Prompt accuracy (`c1-18-03.ex01`, `c1-18-03.ex08`):** Fixed `c1-18-03.ex01` (`or` → `and`) and removed unreferenced `*puede que*` from `c1-18-03.ex08` question text (options only test `*dudo que*` and `*a lo mejor*`).
5. **Story transcript formatting (`c1-18.json`):** Split paragraph 7 (which combined both `Entrevistador:` and `Invitada:` turns) into paragraphs 7 and 8 to match paragraphs 1–6.
6. **Rendered prose & house style (`c1-18-01-a-gr.json`, `c1-18-03-a-gr.json`, `c1-18-04-a-gr.json`, `c1-18-05-a-gr.json`):** Removed parenthetical glosses `(formal)` / `(female speaker)` from English translations (which rendered with stray spaces before commas), replaced ASCII `->` arrows with Unicode `→` in Lesson 04's table/tip, and replaced ALL CAPS `ALWAYS` with bold `**always**` in Lesson 03's table.

## Re-verification after fixes
- `check-content.py es-latam c1 conversation-markers`: **0 errors, 0 suspects**
- `unmet-words.js` (`--with-hidden`): **0 unmet words**
- `check_es_c1_forms.py`: **0 hits before their screen**
- `check_unit_refs.py --bare --named`: **0 issues**
- `audit-reader-coverage.js --story c1-18`: **351 tokens, 0 missing from dictionary, 0 lookup throws**
- `render_lesson.js`: **0 `!!` lines**
- `validate-content.py --changed`: **25 passed, 0 failed** (1 es-es registry sync + 24 es-latam)
