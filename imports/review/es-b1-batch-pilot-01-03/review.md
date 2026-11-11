# ES B1 pilot: core Units 1 `telling-stories` and 3 `experiences-memories` (2026-11-11)

Two Sonnet readers, one unit each, es-es read once and mirrored to es-latam.

| Unit | Reader | Tokens, minutes | Fixes proposed | Rejected by check_fixes | Changed by the reviewer | Baseline errors / suspects (es-es, es-latam) | After |
|---|---|---|---|---|---|---|---|
| 1 telling-stories | A | 230k, 8 min; story rewrite on resume +18k, 2 min (248k total) | 80 + 28 (story) | 0 | 4 | 17 / 4, 21 / 4 | 0 / 1 accepted in both |
| 3 experiences-memories | B | 237k, 12 min | 135 | 0 | 3, plus 2 per-course extras | 13 / 2, 16 / 2 | es-es 0 / 0; es-latam 3 / 0 (below) |

State: Unit 1 frozen in es-es and es-latam; Unit 3 frozen in es-es only. Walk 12/12 lessons in each course, challenges on screen and passing. Unmet words 0 in both units and courses (lesson stems; stories are not scanned).

## Reviewer changes to the readers' fixes

- Unit 1: story punctuation (a closing dash before the narration), a wordy recap line, *a pesar de* (taught b1-32-03) in a comprehension answer, *tenía mucho dolor* → *le dolía todo el cuerpo*.
- Unit 3: a wrong option built on *antes de que* + indicative (later form) replaced by an imperfect fault; *me di cuenta que* as a "fault" (common usage) replaced by a tense fault; a calque (*la enseñanza quedó conmigo*) rewritten.
- Per course: es-latam lost the *vosotros* rows of three Unit 1 tables (`latam-vosotros`); es-es b1-02-04.ex06 *los acercó* → *os acercó*; *estufa* → *cocina* in both courses (the word is in no list).
- Challenges: each scenario given its role line ("You are Meg." / "You are Carlos."), as in A2; an invented cousin replaced by Ana; "lost the train" → "missed the train".

## Facts

See `reviewer-facts.md`. The Unit 1 story no longer quotes or half-quotes Cervantes; the source text could not be fetched from the container, only search results.

## For the user

1. **`cuanto-mas-tanto-mas` (the skill that covers *a medida que*) has its `taught_in` on the latam-track screen `b1-eeuu-03-cuanto-mas-gr`, but the core lesson b1-02-04 teaches *a medida que* first, in both courses.** Three items (b1-02-04.ex02, ex11, b1-02-consolidation.ex08) are therefore `taught-later` errors in es-latam, and es-es has no screen for the skill at all (ROADMAP 148(n)). Proposal: move `taught_in` to `b1-02-04-conectores-temporales-gr`. es-latam Unit 3 stays unfrozen until this is decided.
2. *soler* is in the b1-01-02 vocabulary list and two items use it as a word; its grammar screen is b1-05-02. Left as is.
3. The Unit 3 story keeps the frame story's premise (the king has each wife killed the next day), said plainly in B1 words.
4. Story words are not checked against the vocabulary lists by any script; the Unit 3 story uses a few unlisted words (*palacio*, *reino*, *visir*, *genio*, *traición*, *jurar*, *amanecer*). Decide whether retold classics must use listed words only (then a check gets written) or may rely on tap-to-translate.
5. Lesson b1-02-03 repeats the pluscuamperfecto of b1-01-03; it now opens as a recap with a "discoveries" angle.
