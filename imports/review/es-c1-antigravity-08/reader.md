# Reader report: Unit 8 data-demography (es-latam C1 core), stems c1-08-01..05, c1-08-consolidation

Checks run: check-content 0 errors / 0 suspects (before and after the fixes, via check_fixes.py: 33 fixes, 13 auto, 20 review, 0 rejected, no unmet words left); check_es_c1_forms 0 hits; check_unit_refs 0 recaps to check (I checked every "You know" by hand: ir + gerund B2 U24, a medida que B1 U2, llegar a B2 U25, más/menos que A2 U6, superlatives B1 U7, numbers A1, hedging B2 U21, modals B2 U26: all right); unmet-words --with-hidden: none; story audit: 458 words, 0 not in dictionary, 0 literal compound guesses; no vosotros, no Spain-only words. Nothing was edited in content; only .scratch files written.

## 1. Found by reading
- c1-08-02.ex03: time words only in the wrong options (*el próximo año*, *este mes*). Right option -> *Los mayores llegaron a duplicarse en veinte años.* (fixed)
- c1-08-02.ex05: *no llegó a superar el descenso anterior* (an uptick cannot exceed a decline) -> *el nivel anterior*; english updated.
- c1-08-02.ex08: *llegó a alcanzar un nuevo descenso* is not natural; english "went so far as to hit a new drop" -> *alcanzar un nivel más bajo*, "even reached a lower level" (*mínimo* would be an unmet word).
- c1-08-02-a-gr tip: *crecer* -> *creciendo* listed as a stem-changing -ir / irregular gerund; crecer is regular -> *pedir* -> *pidiendo*. Example 4 english "is changing ... since" -> "has been changing".
- c1-08-03.ex07 item 1: *Más localidades rurales rebasaron el límite de las que preveía el estudio* puts *de las que* after *el límite* (reads as "the limit of those that"); "exceeded" and "towns" unpinned. -> prompt gives «rebasar» and «más localidades rurales ... de las que», answer *Más localidades rurales de las que preveía el estudio rebasaron el límite.* Item 2: pin «localidad».
- c1-08-03.ex05, c1-08-01.ex05, c1-08-05.ex05, c1-08-consolidation.ex03 (listening): wrong options are unrelated sentences with several faults and absolute words (*whole population ... in person*, *proves ... entire decline ... whole region*, *no further census*). Rewritten as one-fault variants (más/menos, swap of subject, mayoría/minoría, phone/writing, caution/confidence, sudden/gradual).
- c1-08-04.ex02: *La proporción ... se situó en torno a los treinta puntos* (a share is not in "points") -> *en torno al treinta por ciento*.
- c1-08-04.ex05 (dictation): digits and % (TTS says "cuarenta por ciento", the learner types it) and *cuenta con aproximadamente dos personas* is unnatural; also *la mitad* was never practised. -> *Aproximadamente la mitad de los hogares tiene dos personas.*
- c1-08-04.ex06: wrong option *en torno de un veinte por ciento* is accepted Spanish (DLE lists en torno a / de) = second right answer (unsure) -> *en torno un veinte por ciento*. Screen claim "*en torno* ... require *a*" softened to "keep their own prepositions" (unsure).
- c1-08-04-a-gr: tip first sentence garbled ("'around' has no preposition after 'roughly' or 'about'") -> "'around' and 'about' take no preposition"; table row "en torno a / alrededor de + number" showed *ronda / se sitúa en torno a* -> *El promedio se sitúa en torno a los dos hijos.*
- c1-08-04.ex07 item 2: "children" fits *hijos* and *niños* -> pin «hijos».
- c1-08-05-a-gr tip: first sentence names no learner error ("use 'indicate' or 'suggest' followed by a blunt claim") -> "English speakers often keep the indicative after a negated verb of concluding."
- c1-08-05.ex10 item 2: *haya* / *exista*, *una sola* / *una única* both fit -> prompt gives «no permiten concluir que haya» and «una sola causa».
- c1-08-consolidation.ex08: the reply *La caída tiene que deberse a una única causa clara* is a natural answer to "Why did it drop?" (second right answer). Carlos's line now opens *Todavía no se conoce la causa.*
- c1-08-consolidation.ex06: *en la localidad de las que* reads as one phrase -> *Hubo más vacantes de ____ que aparecían en el censo.*
- c1-08-consolidation.ex11: "People think" = *opina / piensa / cree*, "stands at" = *se sitúa / está en*: pin «opinar», «situarse».
- Challenges: c1-08-02 scenario says "rural area" but target and cue say "last year"; title "A Ten-Year Trend" -> title "What the Chart Shows", scenario "...even fell last year". c1-08-03 scenario never mentions the young people the target talks about -> added. c1-08-consolidation scenario "in two sentences", target is one -> "in one sentence". c1-08-01, 04, 05: fine (roles, people, canDo = first checklist line all right).
- Article claim (unsure): the unit says dropping the article after *de* is wrong for *la mayoría de encuestados* (c1-08-01 tip, c1-08-01.ex06 option 3 *La mayoría de vecinos*, consolidation.ex02 option 2). *la mayoría de + bare plural* is common and I believe accepted (*la mayoría de países*). Switched those three to *la mitad de encuestados / vecinos* (needs its article). Marked unsure; if the reviewer's RAE check covered *mayoría* specifically, drop these three fixes.
- Story c1-08: grammar, facts (all invented, no real study or person named) and register fine; questions answerable. Small: "un índice inferior al del estudio previo" calls an average (*promedio*) an *índice* (see 4).

## 2. Metadata
- c1-08-04.ex03, c1-08-04.ex04, c1-08-05.ex04: category `grammar` with the vocabulary tag `c1-data-demography-vocab` -> category `vocabulary` (fixes).
- c1-08-01.ex05 and consolidation.ex07 (listening / dictation) (unsure): tagged `concordancia-ad-sensum` / `numbers`, but a wrong answer shows misheard *minoría* vs *mayoría* / *tercio*; unit vocabulary fits better. Not fixed (no fix written).
- c1-08-05.ex02 (unsure): tagged `hedging` (parece que, según parece, podría decirse que), but the tested form is the subjunctive after a negated *concluir*; no better C1 slug is taught here, left.
- c1-08-04.ex07: item 2 is *rondar*, not agreement; tag stays `concordancia-ad-sensum`, acceptable.
- distractor_skills: 02.ex03 (0 `ir-infinitive`, 2 `perifrasis-verbales`) correct; no others needed.
- After applying: `python scripts/lock_tags.py es-latam c1/data-demography --update --reason "..."` (c1-08-04 category changes).

## 3. Goals / checklists
- c1-08-02 goal and checklist item 3 (*ir* + gerund apart from *ir a*) is practised by one wrong option only -> "I can tell a gradual trend (*ir* + gerund) from a peak reached (*llegar a* + infinitive)." (goal and checklist, two fixes). Item 1 (first line = canDo) unchanged.
- c1-08-03 goal 3 "*de* before an affirmative number" was practised nowhere: third item added to ex07 (*Más de cien localidades participaron en el estudio.*).
- c1-08-04 goal 3 "*la mitad* and *un tercio*": *la mitad* was never practised: now in ex05.
- Goals and checklists otherwise identical, counts and order match, each lesson's own; canDo of all six challenges = first checklist line.

## 4. Doubtful
- c1-08-04-a-gr: "*en torno* ... require *a*" (unsure, see 1; DLE has *en torno a/de*).
- c1-08-02-b-gr: *tasa de envejecimiento* (example 1) (unsure): demographers say *índice de envejecimiento*; left.
- Story: *dos coma dos* (Mexico and Central America say *dos punto dos*) (unsure); "un índice inferior" for an average -> *una cifra inferior a la del estudio previo* (no fix written, story).
- c1-08-01.ex08: "individual people" for *hogares* (households); acceptable, no fix.
- c1-08-01.ex03 / 05.ex03: two wrong options share one fault; acceptable.
- c1-08-03.ex08 and ex02 hints name the article's gender/neuter nature; the "neuter *de lo que* after a noun" question is left open as the reviewer said (ex08 marks *lo* wrong only through its hint).
- Table labels use *gerundio* (c1-08-02-a-gr): Spanish metalanguage, known from B2; left.
- 02-a text: "(B1 Unit 2)" sits after *a medida que*, ok.

## 5. Dictionary
None: the audit lists no "literal compound guess" and no "not in the dictionary" word for c1-08.

## Norm claims added by this reading (for the reviewer)
*la mayoría de* + bare plural noun (1); *en torno de* (4).

## Fix count (file .scratch/fixes-data-demography.json; check_fixes: 13 auto, 20 review, 0 rejected)
Unit 8: 33 fixes (7 screen text, 2 lesson goal/checklist, 21 exercise sets/texts, 3 challenge sets).
