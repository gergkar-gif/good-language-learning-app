# es-es b1 money-economy (B1 Unit 37): reader B report

Files: fixes-money-economy.json (74 fixes, 1 of them es-latam only), challenges-money-economy.json (6). es-latam files are identical to es-es except for the shared *billetes* (see 1); the other 73 fixes mirror (0 unmatched).
check-content: 13 errors + 2 suspects before; 0 errors, 0 suspects after (es-es); es-latam also had a `course-variant` suspect (*billetes*), now fixed. Unmet words: es-es 33 hits before, 1 after (consolidation.ex12 *afecta*, inflected form of *afectar*, now listed in b1-19-05); es-latam 42 before, 1 after (same form).

## 1. Found by reading
- b1-19-01 grammar: *más … que*, *menos … que*, *tan … como* (A2 Unit 6) presented as new; stray italics ("Use mucho, poco, bastante, *demasiado*, …"). Fix: recap "from A2 Unit 6", tip on *demasiados gastos* vs *gasto demasiado*.
- b1-19-01.ex02 length 46 vs 22, Spanish gloss "[¿Cuál expresa una comparación?]": new options of equal length. ex06 stem in unmet Spanish (*palabra*, *significa*): English only. ex13 wrong options *suficientemente dinero* (unmet adverb) and *demasiados dinero* (two faults): now *suficiente de dinero* and *suficientes dinero*. ex14 wrong options *de el mes pasado* and *tan gastos que* carried two faults: now *como* and a missing article. ex15, ex16 prompts did not pin the stored answers.
- b1-19-02 grammar: present perfect (A2 Unit 1), *estar* + gerund (A1 Unit 19), comparatives presented as new: recap. ex06 stem Spanish gloss (*significa*). ex15 wrong options glossed identically to the right one ("more expensive" for *más caro*): gloss now "(singular)". ex16, ex17 prompts pinned.
- b1-19-03 grammar: *porque* / *por eso* (A2 Unit 5) and *debido a* (B1 Unit 11) presented as new; **por lo tanto is B2** (named in the screen and accepted in ex07 `answers`, with *por tanto*): removed from both. ex03 `answers` *ya que* (suspect answers-alternatives): narrowed to *porque*. Tip claimed punctuation marks each connector's role: rewritten as what follows each connector.
- b1-19-03.ex12 length 43 vs 32 and an unEnglish option "As a cause, families spend more." ex14 reply "Por eso, el precio aumenta." to "¿Qué ocurre cuando hay poca oferta?" was unnatural, wrong options *Porque, el precio aumenta* / *Debido a, el precio aumenta* were non-phrases: A now says "Hay poca oferta." ex15 wrong options *Algunas familias debido a menos* / *…porque menos* were non-phrases; the right answer had no connector although the item is tagged `porque-y-por-eso`: now *Por eso, algunas familias gastan menos.*
- b1-19-03.ex02 (es-latam): *billetes de tren* in a shared file: es-latam fix to *boletos* (variant es-latam).
- b1-19-04 grammar: conditional (A2 Unit 26) and *si* + imperfect subjunctive (B1 Unit 7) presented as new; tip said "Spanish never confuses" would-as-habit with would-as-hypothesis (false: *iba a* / the imperfect). Rewritten. ex02 and ex06 stems in unmet Spanish (*hipotética*, *completa*, *frase*), ex02 option *gastos fijos* unmet. ex09 length 47 vs 35. ex03 `answers` also accepted *tuviese*, an *-se* form the brief lists as later (the sheet lists it as taught in b1-04-02): reduced to *tuviera* (unsure). ex16, ex17 prompts pinned.
- b1-19-05 grammar: *se observa que* (B1 Unit 11), *creo que* / *me parece que* (B1 Unit 13), *considero que* (B1 Unit 35), *estar* + gerund presented as new: recap. ex02 options used *cubierto* / *ministerio* (unmet). ex06 length 14 vs 10 and unmet *observación*. ex09 length 46 vs 30. ex14 copied ex04's sentence and used *opinas* (unmet). Prompts of ex16-19 pinned (ex18, ex19 are in no lesson section, see below).
- b1-19-05 reading ex20-23 asked about "a family that learns to manage its expenses", a text that does not exist (not the story shown): replaced by four questions on the story. Old ex20 and ex23 also had `tell-absolute` (*nunca*) and give-away lengths 71 vs 39 / 77 vs 51.
- b1-19-05: ex11, ex12, ex18, ex19 are in the exercise file but in no lesson section (never shown). Reviewer decides.
- b1-19-05 vocabulary: story and unit words in no list added (*alacrán, joya, prestamista, fraile, negocio, papel, observar, afectar*); each used in an exercise.
- b1-19-consolidation: ex02 length 46 vs 22 and copy of 01.ex02; ex03 *ya que* answers, *materiales* unmet, copy of 03.ex03; ex04 copy of 04.ex03 (varied); ex06 stem unmet (*hipotética*, *condición*); ex08 *economía* unmet in es-latam; ex09 second wrong option had two faults (*si tendría … invirtiera*); ex16 five unmet words (*rápidamente, competitivo, consumidores, tarifas, combina*). Left as copies of lesson items: ex10-12 (listening/dictation), ex05.
- Story b1-19-tradicionesperuanas: rewritten at B1 in six short paragraphs (about 230 words). Removed *antes de que terminara*, *en cuanto pudiera*, *como si nada hubiera ocurrido*, *lo que ella imaginaba*, *lo que debían*, *cuyo*-style relatives; dropped the invented closing moral ("el valor … está en la fe …") and the invented Lima proverb, which no source the reviewer could read supports. The pawn is now explicit ("se quedó con la joya") so the story agrees with the core (wrapped scorpion, jewel, pawned, returned, scorpion again). Comprehension questions were jargon ("prodigio insólito", "probidad", "zozobra") and one asked for the moral; replaced.
- Goals/checklists: see 3.

## 2. Metadata
- b1-19-05.ex13 `opinion-verbs-mood` -> `progressive` (the options differ in *están aumentando* vs *estén aumentando* / *aumentarían*; there is no *creo que* in the item). (unsure)
- b1-19-05.ex06 retagged to `vocabulary` / `b1-money-economy-vocab` (it asks what a phrase means) and its `distractor_skills` removed. (unsure)
- b1-19-03.ex14 ds {2: formal-cause-connectors}; ex15 no ds.
- After retags: `lock_tags.py es-es b1/money-economy --update`.
- The unit teaches no new grammar (sheet: "Grammar this unit teaches" is empty), so all lessons review known skills; nothing to move.

## 3. Goals / checklists
- b1-19-01 "Use four new money terms." (list has five) -> "Use the new money words."
- b1-19-03 "Connect causes with consequences." (checklist-shared with b1-20-02) -> "Link a cause to its result with porque, por eso and como consecuencia."
- b1-19-02 "Use three new price terms.", b1-19-03 "Use three new economic terms.", b1-19-04 "Use three new financial terms." -> "Use the new price / economic / financial words." (goal lines never count words)
- b1-19-05 "Use three new economy terms." (list has five, now more) -> "Use the new economy words."
- b1-19-consolidation "Explain causes and consequences." (shared with b1-16-consolidation, b1-32-consolidation) -> "Say why prices change and what follows from it."
- Challenges: generic text replaced by six role-based ones; lesson 05's retells the story.

## 4. Doubtful
- Story plot details, all unchecked because the tradición could not be found in the Gutenberg volumes the reviewer searched: Lima in colonial times; the friar Gómez known for kindness; a weeping woman who comes to his cell; her husband's small business and a debt due that same week; the friar owns almost no money; the scorpion on the cell wall, wrapped in paper; the woman takes it to a moneylender (*prestamista*); the moneylender gives more money than the debt and keeps the jewel; the woman promises to return it; a few weeks later the couple pay and take the jewel back; they return it to the friar at the convent; he puts it on the wall and it walks away as a living scorpion. The story keeps the label "inspirada en una tradición de … Ricardo Palma". Whether Palma's tradición names the sum, the husband's illness or an owner other than the friar is not known to me. (unsure)
- Paragraph 6 of the old text (moral, proverb) dropped, and paragraph 5 split in two to keep six paragraphs; fixes on story text are marked unsure.
- b1-19-04.ex03 `answers` reduced to *tuviera*: if the reviewer holds that *-se* is taught (b1-04-02), restore *tuviese*. (unsure)
- Present-day facts: none.

## 5. Dictionary
None: `audit-reader-coverage` on the retold story: 0 not in the dictionary, 0 literal compound guesses.

Fix count: 74 (73 shared + 1 es-latam only).
