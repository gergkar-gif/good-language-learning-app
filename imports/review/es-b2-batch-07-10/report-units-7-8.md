REPORT, Units 7 and 8 (es-latam B2), everything in /home/user/parlour-read-a, nothing committed.
Files changed: grammar, lessons, exercises, vocabulary and story files for b2-07-* and b2-08-*, plus /home/user/parlour-read-a/challenges-temporal-clauses-future.json and /home/user/parlour-read-a/challenges-concession-counter-argument.json (six challenges each). `build-manifest.py` also regenerated the decks and stories manifests, as expected. I did not write a report file; this reply is the report.

CHECK COUNTS (before -> after)
- Unit 7 (temporal-clauses-future): check-content 9 errors, 17 suspects -> 0 errors, 0 suspects. unmet-words: about 65 hits (counted by eye) -> 0.
- Unit 8 (concession-counter-argument): check-content 19 errors, 22 suspects -> 0 errors, 1 suspect. unmet-words: 68 hits -> 0.
- The one Unit 8 suspect is `answer-in-prompt` on b2-08-05.ex03 ("Pase lo que __"). It is unavoidable, because the reduplicated formula repeats the verb.
- `render_lesson.js` shows 0 `!!` lines for both units.
- `validate-content.py --changed` is clean: "All content files match their schemas", with only the fr/it warnings that were already there.
- `check_unit_refs.py` is clean except as follows.
  - False positives, Unit 7: b2-07-01 `*en cuanto*` and b2-07-02 `*hasta que*` are claimed from A2 Unit 27. The checker finds them first in a hidden B1 Latin America unit, because the A2 Unit 27 table writes them without italics. The sheet lists both under `cuando-subjuntivo`.
  - Unit 8: it asks for a hand check of two recaps that carry no italic word (b2-08-02 "You know it from B1 Unit 32", b2-08-05 "present subjunctive from A2 Unit 27").

UNIT 7
- General: the screens are rewritten in English with recaps. Lessons 02–05 lost their boilerplate intro; lesson 01 keeps a rewritten unit intro. Lessons 01–05 got an `srs` section and a `checklist`. Vocabulary lists are replaced with words the items use (no vocab-unused left). Dialogue items are now `dialogue-complete` turn lists, and the old identical ex05 is gone.
- 01 (*en cuanto*, *tan pronto como*, *apenas* + subjunctive): the screen recaps A2 Unit 27, B1 Unit 37 and B2 Units 1 and 2, and drops *una vez que*. Items ex01–ex06 are all new.
- 02 (*hasta que*): the screen adds the extra *no* in *hasta que no* as a recognition point. *hasta no* + infinitive and *hasta tanto* are dropped. ex07 is new. Items ex01–ex07 are all new.
- 03 (*mientras*): the screen covers indicative "while", subjunctive "as long as" (duration and condition) and *mientras que*. Items ex01–ex06 are all new.
- 04 (*siempre que*, *cada vez que*): the screen covers "whenever" with the indicative, "provided that" with the subjunctive, and *cada vez que*. *cada que* is dropped. Items ex01–ex06 are all new.
- 05 (*antes/después de que*): the screen teaches the same-subject infinitive, *antes de que* as always subjunctive (present, or imperfect after a past verb), and *después de que* with the indicative for the past and the subjunctive for the future. ex07 is new. Items ex01–ex07 are all new.
- Consolidation: ex01–ex08 are rewritten (2 reading items, answerable from the text). The checklist is rewritten, and its text line names the novel because the generic García Márquez line was shared with b2-03.
- Text: 323 words, 6 `narration` paragraphs, original, with English comprehension questions and explanations. Every claim, with how sure I am:
  - García Márquez was a Colombian writer: sure (brief).
  - Born 1927, died 2014: sure (brief).
  - Nobel Prize 1982: sure (brief).
  - "de Literatura": sure, it is true, but the brief says only "Nobel Prize". "uno de los premios más conocidos del mundo" is general knowledge, not on the list.
  - In the 1950s he was in Paris working as a press correspondent, and wrote the novel there: sure (brief). "Corresponsal de prensa" is glossed as "periodista que envía noticias desde otro país": fairly sure.
  - First appeared in a magazine in 1958 and as a book in 1961: sure (brief). "Antes de que saliera como libro, ya había aparecido en una revista" follows from those dates: sure.
  - An old, retired, poor colonel lives with his wife in a small town: sure (brief). The gloss "un coronel es un oficial del ejército" is a general fact, not on the list.
  - He has waited for many years for the pension promised for his service: sure (brief).
  - Every Friday he waits for the letter, which does not come: sure (brief).
  - The couple keep a fighting cock: sure (brief).
  - "Mientras no llegue la carta, el coronel sigue esperando" and "cuando llegue el viernes siguiente, volverá a esperarla": an extrapolation of "every Friday" (reviewer to check). It gives no ending.
  - "Es un libro corto", plus the reading advice at the end: derived from "short novel".
  - The date list (1927, 1958, 1961, 1982, 2014) is a repeat of the above.

UNIT 8
- General: the screens are rewritten in English with recaps, and lesson 01 keeps a rewritten unit intro. Lessons 01–05 got an `srs` section and a `checklist`. Wrong claims are removed (the pluperfect-subjunctive and imperfect-conditional rows in lesson 01, which are later material). Vocabulary lists are rewritten to words the items use.
- 01 (*aunque*): the screen recaps A2 Unit 28 and B1 Unit 1, with indicative = fact, subjunctive = possibility or a point granted. ex07 is new. Items ex01–ex07 are all new.
- 02 (*si bien*): the screen recaps B1 Units 32 and 1 and A2 Unit 28, and teaches *si bien* + indicative as formal. Items ex01–ex06 are all new, so there are 6 new `concesivas-si-bien` items as asked (ex02–ex06 are tagged with it).
- 03 (*por más que*): the screen covers *por mucho que*, *por muy... que*, and the indicative only for a completed past effort. Items ex01–ex06 are all new.
- 04 (*aun cuando*): the screen covers the same mood rule as *aunque*, formal register, and the spelling of *aun* without an accent. *aun a riesgo de que* and *así* + subjunctive are dropped. Items ex01–ex06 are all new.
- 05 (reduplicated subjunctive): the screen covers *pase lo que pase*, *diga lo que diga*, *sea como sea*, *quieras o no*, and the pattern of verb, relative word, same verb. Items ex01–ex06 are all new.
- Consolidation: ex01–ex09 are rewritten (3 reading items). The checklist is rewritten.
- Text: 331 words, 7 paragraphs, original, with English comprehension questions. The author field has no birthplace. Every claim, with how sure I am:
  - Carpentier was a Cuban writer, 1904–1980: sure (brief).
  - *El reino de este mundo* was published in 1949 in Mexico: sure (brief).
  - It is set in Haiti in the time of the Haitian Revolution: sure (brief).
  - The events are seen through the eyes of Ti Noel, an enslaved man: sure (brief).
  - The prologue was first published in Caracas in 1948: sure (brief).
  - The prologue came before the book (1948 vs 1949): sure, derived from those dates.
  - Presented as Carpentier's idea (*lo real maravilloso*): the history and nature of Latin America are full of the marvellous: sure (brief), paraphrased with no quotation.
  - "Su marco es un periodo real de la historia de Haití", "ficción" and "el lector conoce esa época desde la mirada de una sola persona": derived from the brief, and fairly sure.
  - "La historia de Ti Noel ocurre en un lugar real y en una época real": derived, fairly sure.
  - The date recap repeats the above. The remaining sentences are meta-commentary with no new facts.

SPANISH I AM UNSURE OF (unsure)
- b2-08-01 screen: *Dijo que saldría aunque lloviera*, which uses the conditional (B1 Unit 22 covers the future and conditional of probability).
- b2-08-02: "do not add *que* after *si bien*" (*si bien que* is, I believe, non-standard).
- b2-08-04 and b2-08-05 grammar claims: *aun* is unaccented in *aun cuando*; *dondequiera* and *cualquiera* are avoided.
- b2-08-03 screen: the indicative "Por más que insistió" is given as a past-effort recognition point.
- Distractors that a native might partly accept, though I judged them wrong in context:
  - b2-08-01.ex05, option "Aunque hay huelga..." after "No sé si mañana habrá huelga".
  - b2-08-04.ex02, options "tenga"/"tuviera miedo": they are wrong only because the stem asks for a real fact.

FOR THE USER
- Skills used before their screen (the checker flagged none; these are my reading):
  - `tan pronto como` is met in B1 Unit 37 (a vocabulary word and the screen b1-37-04, with *haya* + participle), so b2-07-01 recaps it instead of teaching it new.
  - `siempre que` + subjunctive "provided that" is already taught in B1 Unit 21 (`conditional-conjunctions`, b1-21-05). b2-07-04 therefore recaps that sense and adds only the indicative "whenever" and *cada vez que*.
  - `mientras` + subjunctive is recapped against `siempre que` in B1 Unit 21.
  - Lesson 8-01 and 8-02 items use the imperfect subjunctive and the future only as recaps or wrong options.
- Skills I tagged on items outside the lesson skill: `conditional-conjunctions` for the *siempre que* "provided that" items (b2-07-04.ex02, ex04, ex06; b2-07-consolidation.ex07), and `cuando-mientras` on b2-07-03.ex02.
- b2-07-05: the user said the screen must teach `antes-despues-de-que` fully. It does (antes de que always subjunctive, después de que with the indicative for past facts and the subjunctive for the future, same-subject infinitive), and 7 items test it.
- No lesson's whole point is a skill the sheet lists as later or hidden. I used nothing from the hidden-track list.
- The checker flagged two recaps in each unit (see CHECK COUNTS above). Please look at the Unit 7 false positives, the Unit 8 uncertain recaps and the one remaining suspect.
- Not fixed: nothing else. I did not touch `skills/*.json` or `tags.lock.json`. The new items are not yet locked, so `lock_tags.py` is for the reviewer.