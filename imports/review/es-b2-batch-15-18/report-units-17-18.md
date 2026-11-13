# ES B2 Units 17 and 18, agent B report

Worktree `/home/user/parlour-read-b`, nothing committed. The report file was refused by the harness, so this reply is the full report.

Challenges files, 6 entries each, with `canDo` equal to the first checklist line:
- `/home/user/parlour-read-b/challenges-reported-speech-past-frames.json`
- `/home/user/parlour-read-b/challenges-rhetorical-reporting-verbs.json`

I checked the targets with unmet-words by temporarily merging them into `challenges.json`. There were 0 hits, and `challenges.json` is restored.

## Counts, before then after
| | check-content errors | suspects | unmet-words hits |
|---|---|---|---|
| Unit 17 | 8 -> 0 | 9 -> 0 | 93 -> 0 |
| Unit 18 | 11 -> 0 | 7 -> 1 | 121 -> 0 |

- **Unit 18 leftover:** `answers-alternatives` on b2-18-01.ex02 (*añadió* / *agregó*). They are true synonyms, and *agregar* is in that lesson's vocabulary.
- **Other checks:** `check_unit_refs --labels --bare` shows 0 for both units, `validate-content --changed` is clean, and render shows no `!!`.
- **Checks rerun:** after the last edit I reran `build-manifest`, `build_word_lesson_index`, check-content, unmet-words, check_unit_refs and validate-content.

## Unit 17 (reported-speech-past-frames)
Screens, titles, goals and checklists are in English, and all vocabulary lists are replaced. Exercises are rewritten with English stems, 3 options and no hint or english on multiple choice. Dialogue items carry the quote in `hint`. Lessons 01-05 gained `srs` and `checklist`. Every item has `category` and `teaches`, and `distractor_skills` are set where a wrong option is a real form of another skill.
- **b2-17-01 "Reported Statements: Shift or Stay"**
  - Screen: recap of B1 Units 13, 33 and 38, the shift table, and the new B2 point that the verb may stay when the fact is still true, still to come, or after a present reporting verb.
  - Items: ex01 matching (aún, vigente, cumplirse, quedar en), ex02 *había* (*el día anterior* blocks *ha*), ex03 Lima/never moved, ex04 builder, ex05 dialogue, ex06 dictation. Tag `estilo-indirecto`.
- **b2-17-02 "Reported Questions in the Past"**
  - Screen: recap of A2 Unit 14 and B1 Unit 33; new are the shift inside reported questions and *se preguntaba si* / *no sabía dónde* / *nadie entendía por qué*.
  - Items: ex02-ex06, tag `discurso-indirecto-interrogativas`. ex03 tests the accent on the question word, ex05 tests *si* against *que*.
  - Vocabulary: preguntarse, desconocer, el interrogante, aclarar.
- **b2-17-03 "Reported Orders and Requests"**
  - Screen: recap of B1 Units 38 and 4; new are a request asked as a question (*¿Puedes…?* becomes *pidió que*) and the present subjunctive after *ha pedido*.
  - Items: tag `estilo-indirecto-ordenes`; ex02 takes `answers` trabajáramos/trabajásemos.
  - Vocabulary: suplicar, encargar, reclamar, el encargo.
- **b2-17-04 "Time and Place Words in Retelling"**
  - Screen: recap of B1 Units 33/38 and A1 Unit 11; new are the full list (ahora, esta semana, hace tres días, acá/allá, este to aquel), *venir* to *ir*, and when nothing changes.
  - Items: tag `discurso-indirecto-deicticos`; ex02 takes `answers` allí/allá.
- **b2-17-05 "Thoughts Without a Reporting Verb"**
  - Screen: free indirect speech taught for recognition only, with four clues and invented examples.
  - Items: tag `discurso-indirecto-libre`; ex02 (*Mañana* stays next to a past verb), ex03 recognition, ex05 dialogue.
- **b2-17-consolidation:** ex01-ex08 rewritten, and `b2-17.json` replaced by an original text. The checklist line names Icaza and *Huasipungo*.

**Text `b2-17.json`:** 327 words, 7 paragraphs, 4 comprehension questions with English stems and Spanish options. Every claim, with how sure I am:
- Icaza was an Ecuadorian writer, born 1906, died 1978: sure (brief).
- He wrote *Huasipungo*, published in 1934: sure.
- It is a novel of Ecuadorian indigenismo: sure.
- "Indigenista" glossed as a novel about indigenous people and their problems: fairly sure (generic definition).
- The theme is the poverty of indigenous people and their exploitation by the landowners: sure (brief).
- "Muchos críticos dijeron que la novela era un buen ejemplo de ese movimiento": unsure (generic attribution, taken from the brief's own sample).
- "Los críticos dijeron que *Huasipungo* trataba de la explotación…": unsure (same).
- A huasipungo was the small plot a hacienda let an indigenous worker use, and the title names it: sure (brief).
- A hacienda is a large rural property with an owner: sure (generic).
- Hypothetical readers' questions and an imagined young reader who looks up the word: conditional wording, no claim.
- Novel 1934, author died 1978, 44 years later; born 1906, about 28 years before the novel: sure (arithmetic).

## Unit 18 (rhetorical-reporting-verbs)
- **b2-18-01 "Reporting Verbs: How It Was Said"**
  - Teaches the skill fully on the first screen: a table of the ten verbs (afirmar, asegurar, explicar, añadir, admitir, negar, advertir, recordar, reprochar, sugerir) and the mood rule.
  - The mood rule: a fact takes the indicative, a rejected claim the subjunctive, *advertir* and *recordar* either, *sugerir* and *reprochar* the subjunctive. It also covers señalar, precisar, agregar, recalcar.
  - Recap: B1 Units 13/33/38 and B2 Units 5/16/17.
  - Items ex01-ex06, all `reporting-verbs` except matching (vocab).
- **b2-18-02 "Denying, Admitting, Answering Back"**
  - Screen: *negar/desmentir que* + subjunctive; *haber* + participle for the same person (the B2 Unit 4 rule); admitir/reconocer/replicar/objetar + indicative.
  - ex02 takes `answers` hubiera/hubiese.
  - Vocabulary: contradecir, replicar, objetar, oponerse a.
- **b2-18-03 "Warning and Reminding"**
  - Screen: advertir and recordar by fact or task, *alertar de que*, and *me recordó* against *recordé*.
  - ex02 takes `answers` cruzáramos/cruzásemos.
- **b2-18-04 "Reproaching and Blaming"**
  - Screen: reprochar/echar en cara + que + subjunctive, *reprochar* + *haber* + participle, culpar/acusar a alguien de.
- **b2-18-05 "Keeping Your Distance"**
  - Screen: según, al parecer, supuestamente, presunto, dar a entender que, impersonal *se*.
  - The news conditional (*habría dicho*) is shown for recognition only and not drilled, so there is no `future-probability` item.
  - ex02 *Según* is tagged `estilo-indirecto-informacion`. `hedging` is not taught.
- **b2-18-consolidation:** 8 items, a new text, and a checklist line that names Alegría.

**Text `b2-18.json`:** 318 words, 7 paragraphs, 4 comprehension questions. Every claim, with how sure I am:
- Alegría was a Peruvian writer, 1909-1967. He grew up on his grandfather's estate and knew the indigenous world closely. The novel appeared in 1941. Sure (brief).
- "That world later appeared in his novel": fairly sure.
- Rumi is an indigenous community of the northern Andes of Peru, led by the alcalde Rosendo Maqui, and a powerful landowner takes the community's land: sure (brief).
- The title says that for the poor the world is wide but belongs to others: sure (brief). *Ajeno* is glossed as "belongs to another person": sure.
- "Quien lea el título no podrá negar que se refiere a la pobreza": fairly sure (it follows from "the poor").
- "Los críticos afirman que la novela trata de la pérdida de las tierras de una comunidad indígena": fairly sure (generic).
- "Otros críticos explican que el autor conocía bien ese mundo, porque creció en la hacienda de su abuelo": unsure (attributes the brief's fact to critics).
- "Algunos lectores admiten que no conocían la palabra *ajeno* y que tuvieron que buscarla": unsure (invented generic reader behaviour; cut if the reviewer prefers).
- "Se suele advertir que un resumen no sustituye a la lectura": unsure (generic).
- Novel 1941, author died 1967, 26 years later: sure.

## Spanish lines I am unsure of
- The 18-01 screen gives *reprochar que* as subjunctive only. The indicative also occurs in real use (unsure). No item tests the indicative against it.
- The 18-05 screen says some style guides advise against the news conditional. I am fairly sure of this, but it is worth a check.
- Vocabulary entries *darle vueltas a*, *oponerse a* and *cuidarse de* are listed as phrases; this is style only.
- The text lines flagged "unsure" above.

## For the user
- **Sheets undercount what B1 taught.** B1 Units 27, 33 and 38 already teach *preguntó si*, *aquí -> allí*, *mañana -> al día siguiente*, *hoy -> aquel día*, and *advertir que* + indicative or subjunctive. The knowledge sheets list B1 Unit 33's grammar neither as Known nor in their skill lists. So `discurso-indirecto-interrogativas` and `-deicticos` (Unit 17) and part of `reporting-verbs` (Unit 18) are really recaps plus extension. I recapped them with the unit numbers from the screens.
- **Skills met in time.** No skill is used before its screen. Nothing from the hidden track or the "later" lists is used. *se dice que* is on no earlier screen (only impersonal *se*, B1 Unit 6). It appears once in an 18-05 table row and example.
- **Generated files changed outside my units.** `build-manifest.py` also rewrote the decks and story manifests of es-es, fr, hu and it (one-line changes each), plus es-latam `curriculum.json`, `decks.json` and `word-lesson-index.json`.
- **Challenge screens not final.** In the render they still show the curriculum placeholder text until the challenges files are merged into `content/es-latam/curriculum/challenges.json`.
- **Tags not locked.** The `lock_tags.py` step is left to the reviewer.
- **Could not fix:** nothing outstanding.