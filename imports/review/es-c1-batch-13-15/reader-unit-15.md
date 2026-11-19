# Reader report: Unit 15 ai-digital-ethics (es-latam C1)

Fixes: .scratch/fixes-ai-digital-ethics.json (30 fixes). Checks run: check-content 0/0; check_es_c1_forms 0 hits; unmet-words (with-hidden) [] before and after fixes (only an inflected *garantizado* in a challenge); validate-content on a scratch copy after fixes: only the 4 locked-tag failures (tag fixes need lock_tags.py --update).

## 1. Found by reading
- c1-15-02-a-gr (screen): "You know *mediante* from B1 Unit 24" then presents *a raíz de*, *en virtud de*, *en torno a* as new. *a raíz de* is B1 Unit 6 (re-taught B2 Unit 27 L1), *en virtud de* is B2 Unit 27, *en torno a* is C1 Unit 8. Only *frente a* and *con respecto a* are new. Fix: recap names all four units, text says what is new.
- c1-15-02.ex06: Carlos asks why the debate "volvió"; Meg: "Nació en torno a la protección de datos…". *en torno a* gives a topic, not a reason, and "nació" does not answer a return. Fix: "¿De qué trata el debate…?" / "Es un debate en torno a…" with the same three prep slips.
- c1-15-03-a-gr (screen): prepositional cleft, plural agreement and donde-over-que are all B2 Unit 1 (b2-01-01-a: "Fue con Ana con quien hablé", "Fueron los vecinos quienes", tip on donde) but are presented as a new "C1 variation". Fix: recap says so; new = contrastive cleft + inverted pseudo-cleft.
- c1-15-03.ex01 option 2 "No es el contenido sintético que más preocupa, sino…": reads as a plain relative clause, arguably acceptable (unsure). Fix: "…lo que más preocupa, pero la falta de verificación" (pero for sino); ds removed.
- c1-15-05.ex01, c1-15-consolidation.ex12, c1-15-05.ex09 (unsure): wrong options that are the INDICATIVE after negated *dar por sentado/hecho que* (elimina, respeta, desapareció) are natural Spanish, so possibly second right answers; screen says "shifts to the subjunctive because the assumption is rejected". Fix: wrong options become dequeísmo (*de que*) and personal *a* before an inanimate noun; screen softened to "normally takes". ds removed.
- c1-15-04.ex05: *la ciberseguridad básica* (adjective only in one wrong option, a tell). Fix: *la ciberseguridad*.
- c1-15-consolidation.ex09 (unsure): *la protección de datos* can be read as a second answer to "legal ability to have data removed". Fix: *la vigilancia masiva*.
- c1-15-05.ex04: "programmes" for software; British is "programs". Fix in all four options.
- c1-15-05 text, paragraph 1: "todo modelo predictivo aprende de datos humanos…" is an absolute and not true of all models. Fix: "un modelo predictivo suele aprender de…".
- Reading (c1-15-05.ex06-08 and the same questions in stories/original/c1/c1-15.json): Q1 right option says the data contains "bias and opacity" (text: historical inequalities; opacity is the system's, not the data's). Q2 asks for the "main threat behind synthetic content and echo chambers": the text names none; it says verification and moderation are essential because facts and manipulation are hard to tell apart. Q3 asks about the "closing argument" and "independent" audits: human oversight and audits are in paragraph 4, not the close; "independent" is not in the text; wrong options had absolutes (fully, all, without). All three rewritten, explanations updated.
- Text facts: no real person, study or statistic. The claims are general opinion, hedged ("suele", "rara vez", "puede"). 454 words, op-ed, no asterisks.

## 2. Metadata
- c1-15-01.ex08: wrong options *redujera* and *ha reducido* are real forms of other skills but had no distractor_skills (option 3 had one). Fix: {1: imperfect-subjunctive-forms, 2: preterito-perfecto, 3: present-tense}.
- Tags are locked: after applying, run `python scripts/lock_tags.py es-latam c1/ai-digital-ethics --update --reason "reader fixes"` (changed: 01.ex08, 03.ex01, 05.ex01, 05.ex09, consolidation.ex12).
- Types per lesson (>=5), Practice listening item, consolidation 12 items and 6 tags: all fine.

## 3. Goals / checklists
- c1-15-01-a-gr recap names only B1 Unit 7; the perfect subjunctive (B1 Unit 37) and imperfect after a past verb (B1 Unit 38) were presented as new. Fix: both named.
- c1-15-04-a-gr: passive *se* used without recap (B1 Unit 6). Fix: named.
- c1-15-consolidation challenge: canDo = first checklist line (opinion verbs) but the target had no opinion verb. Fix: scenario, prompt, cues, target, english now "No considero que el sistema haya garantizado la neutralidad. La regulación tecnológica exige que se audite cada algoritmo."
- Goals/checklists otherwise match, are practised, and are the lesson's own. Challenges 01-05 otherwise fine (roles, people, canDo).

## 4. Doubtful
- c1-15-03.ex06 wrong option "Es las cámaras de eco las que…": the B2 Unit 1 screen says singular *es* after a plural is heard in everyday speech, so in a spoken dialogue it is arguably not an error (unsure; not re-raising the agreement norm itself). No fix written.
- c1-15-05-a-gr tip and goal 2 (participle agreement, invariable with *que*) repeat B2 Unit 25 (b2-25-05-a); the lesson's new point is only the negated + subjunctive. No fix.
- c1-15-consolidation.ex02 reuses the wrong options of c1-15-02.ex01 (*en virtud a*, *mediante de*, *a raíz con*). No fix.
- c1-15-03 challenge target has contrastive + prepositional cleft; canDo also names the inverted pseudo-cleft. No fix.
- check_unit_refs says "*en torno a* claimed from C1 Unit 8, first appears nowhere": a false positive (C1 core is hidden in the index; the sheet lists it in C1 Unit 8 words and c1-08-04-a teaches it).
- c1-15-02.ex03 hint "root" is the gloss of the answer *raíz* (fixed expression, left).

## 5. Dictionary
None: the audit reports 0 words not in the dictionary and 0 literal compound guesses.

## Fix count
Unit 15 ai-digital-ethics: 30 fixes (24 sure, 6 flagged "sure": false: 03.ex01, 05 screen mood sentence, 05.ex01, 05.ex09, consolidation.ex09, consolidation.ex12).
