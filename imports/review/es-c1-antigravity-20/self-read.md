# Self-read report: ES C1 core Unit 20 (`concession-evaluation`)

## 1. Found by reading
- `c1-20-01.ex02`: hint `"ser (3rd person singular, present concession)"` named the tested grammar label; changed to `"ser (3rd person singular, 'may well be')"`.
- `c1-20-01.ex03`: hint `"tener (3rd person singular, past concession)"` named the tested grammar label; changed to `"tener (3rd person singular, 'may well have had')"`.
- `c1-20-01.ex06`: option 2 `"Era costoso, pero te lo regalan gratis este semestre."` had a tautology (*regalan gratis*) and an asymmetric time word (*este semestre*), and option 3 `"Sería costoso, pero el horario te compensa de sobra."` was a potentially valid hedged conditional; replaced both with clear mood faults (*Sea costoso...*, *Fuera costoso...*).
- `c1-20-01.ex08`: option 1 `"Tendría algún defecto, porque hoy funciona perfectamente."` changed tense and phrasing; tightened to `"Habrá tenido algún defecto, porque hoy vale la pena."` (one fault: *porque* instead of *pero*).
- `c1-20-02.ex01`: option 1 `"Aún cuando el desembolso es elevado mañana, el barrio necesita ese servicio."` had two faults plus an asymmetric time word (*mañana*); replaced with `"Aun cuando el desembolso será elevado, el barrio necesita ese servicio."` (one fault: future indicative after *aun cuando*).
- `c1-20-03.ex02`: hint `"alto (agreeing with «la tarifa»)"` gave away the agreement being tested; reduced to `"alto"`.
- `c1-20-03.ex03`: hint `"preposition setting a benchmark ('for')"` named the tested function; reduced to `"preposition ('for')"`.
- `c1-20-03.ex06`: option 3 `"Para lo largas que fue las obras, el resultado es muy decepcionante."` had two faults (wrong preposition and singular verb); replaced with `"Con lo largo que fueron las obras, el resultado es muy decepcionante."` (one adjective-agreement fault).
- `c1-20-04.ex06`: prompt refers to yesterday's completed report (`ayer no incluyeron`), so shifted options from present subjunctive (*pasen*) to present perfect subjunctive (*hayan pasado por alto*) and added `distractor_skills` for indicative *han pasado*.
- `c1-20-05.ex09`: options had asymmetric time phrases (*hoy* vs *hace tres años*); aligned all four options to one frame testing discourse-marker choice (*no obstante* vs *por el contrario* / *al contrario* / *por lo tanto*).
- `c1-20-consolidation.ex02`: option 3 had an asymmetric time word (*hoy*); removed *hoy*.
- `c1-20-consolidation.ex04`: hint `"tener (3rd person singular)"` allowed present indicative *tiene* alongside *tendrá*; added `'may well have'` to pin the concessive future.
- `c1-20-consolidation.ex05`: hint `"costoso (agreeing with «las obras»)"` gave away the agreement being tested; reduced to `"costoso"`.
- `c1-20-consolidation.ex06`: hint `"dar (3rd person plural, completed past)"` named a grammar label; changed to `"dar (3rd person plural, 'have given')"`.
- `c1-20-consolidation.ex11`: prompt did not pin word order (`Será alta la tarifa` vs `La tarifa será alta`); pinned default order starting with `La tarifa`.
- `c1-20-03` (challenge): target used `Para lo alta que es` while `canDo` (`checklist[0]`) specifies *con lo* + adjective/adverb + *que*; aligned scenario, prompt, cues, target and English to `Con lo alta que es la tarifa, el servicio deja mucho que desear.`
- `c1-20-consolidation` (challenge): scenario said `"was costly"` (past) while prompt and target used present concessive future (`Será costosa`); aligned scenario to `"is costly"`.
- `c1-original-20` (story): `"El proyecto costará todavía varios años de amortización"` was an unnatural collocation; changed `costará` to `exigirá`.

## 2. Metadata
- `c1-20-04.ex06`: added `"distractor_skills": {"1": "preterito-perfecto"}` for the indicative distractor *han pasado*.
- All 55 exercise tags, categories, and unit vocabulary tags verified; `c1-20-01-a-gr`–`c1-20-05-a-gr` recap references verified against the actual A2/B1/B2 screens.

## 3. Goals / checklists
- All 6 lessons' goals and checklists match 1-to-1 and every line is practised in its lesson.
- All 6 challenge `canDo` fields match `checklist[0]` verbatim and match the target's form after the `c1-20-03` fix.

## 4. Doubtful
- `c1-20-04-a-gr` tip: `"*Es lamentable que subieron la tarifa* is non-standard in careful Spanish"` — (unsure) RAE NGLE notes indicative occasionally appears after factive evaluative predicates in some regional spoken varieties, though subjunctive is the standard norm; worded as "non-standard in careful Spanish" for the reviewer's RAE check.
- Factual claims in `c1-20.json`: completely fictional unnamed city, unnamed tram line, and invented column figures (18% overrun, 14 vs 40 minutes, 2 southern neighbourhoods). No real city, study, or person named.

## 5. Dictionary
- `node scripts/audit-reader-coverage.js es-latam --story c1-20 --top 0`: 0 words not in dictionary, 0 literal compound guesses, 0 lookup throws.

Total fixes for Unit 20 (`concession-evaluation`): 18 fixes.
