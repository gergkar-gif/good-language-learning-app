# ES B1 core close-out (2026-11-12)

Decisions by the user, 2026-11-12, and what was done:

| Decision | Done |
|---|---|
| es-es must teach every B1 grammar skill | Six skills that only the hidden `latam` track taught are now taught on core screens in both courses, each with a screen section and 6 items: `estar-a-punto-de` b1-01-02, `gerundio-acciones-paralelas` b1-02-02, `relativo-posesivo-cuyo` b1-05-04, `dejar-de-infinitivo` b1-12-05, `futuro-perfecto` b1-22-04, `correlativos-no-solo-sino` b1-40-02 (registry: 69c3dcf4; content by agent A, reviewed: 42dfd9a1). |
| Hide the unread tracks (es-es B1 `cultura`, es-latam B1 and B2 `latam`) | `HIDDEN_TRACKS` in build-manifest.py; the curriculum, Reader and Decks loaders drop them; content untouched (d461e373). |
| Keep the 29 B1 Reader stories no lesson uses, and check them | Agent B rewrote all 29 (es-es) / 28 (es-latam); the reviewer checked the five classics against the chapters in `sources/` and spot-checked the originals; es-latam labels aligned with es-es. |
| *por lo tanto* is known from A2 Unit 28 | Rulebook relabelled (d461e373). |
| Keep the `-se` alternative answers | Kept; none is a first or model answer (checked by script). |
| Thin skills get their items | `resultar-adjective`, `cuanto-mas-tanto-mas`, `superlatives`: 6 core items per course each. |

## Agent A (six skills, thin skills): 237k tokens, 11 min

Checks after applying: check-content 0 errors / 0 unaccepted suspects in the 8 touched units, both courses; validate 25/25; unmet words 0 (es-latam: *acercó*, an older line); walk 48/48 lessons per course; refrozen. Reviewer changes: a builder with punctuation as separate tiles (merged, also in the older b1-40-02.ex03); a screen line promising a later lesson that does not exist.

Earlier uses the agent found (left as they are): *dejar de* in b1-05-05 (screen example, ex05, ex11), before its new screen in Unit 23; it is a vocabulary use there. *tanto … como* / *no solo* appear before b1-40-02 only as wrong options, glosses or story text.

**For the user:** the b1-02-04 screen teaches *a medida que* only, and its skill is titled `cuanto-mas-tanto-mas` ("covers *a medida que*", your decision of 2026-11-11). Either the screen gets a *cuanto más …, más …* line, or the title should change.

## Agent B (29 stories): 291k tokens, 14 min

- 24 "original" texts were labelled as inspired by Dickens, Rousseau, Adam Smith, Mill, Austen, Huxley and others, with nothing of those works in them: relabelled as original. Template filler, repeated sentences and C1 questions were removed or rewritten. Ulises and Gulliver were put into invented episodes; they are now invented characters. Carlos (a course character) was renamed Pablo in b1-27.
- The classics were corrected against the source chapters: Alice ch. 7, Dorian Gray (it now has the real ending), Perrault's Cinderella (the father is alive, there are two nights, and Perrault's own moral) and Pazos de Ulloa ch. 1 (the real second half of the scene; the one quoted line is verbatim). Sherlock Holmes is now a labelled pastiche.
- Not verified: the 1865 and 1890 dates in `work` (common knowledge, not in the Gutenberg texts).
