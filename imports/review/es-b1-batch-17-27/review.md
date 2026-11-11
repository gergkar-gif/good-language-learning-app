# ES B1 core Units 17–27 (2026-11-11)

Units (es-es numbers): 17 `health-wellbeing`, 19 `home-housing`, 21 `cities-communities` (reader A); 23 `food-lifestyle`, 25 `media-information`, 27 `technology-communication` (reader B). Two Sonnet readers, three units each; es-es read once and mirrored.

| Reader | Tokens, minutes | Fixes proposed (per unit) | Rejected | Changed by the reviewer |
|---|---|---|---|---|
| A | 393,512 by the resumed notice (stopped by the 5-hour limit after two units, resumed after the reset) | 257 (82 / 96 / 79) | 0 | 2 |
| B | 374,756, 21 min; unmet-word follow-up on resume +34k, 4 min | 311 (112 / 106 / 93), then 27 + 31 words | 0 (2 duplicate fixes merged) | 3 |

State: all six units frozen in es-es and es-latam (B1 14/76 per course). check-content 0 errors and 0 suspects. Unmet words, run with comma-separated stems in both courses: 0 in Units 17–21; in Units 23–27 only *facilita* (inflected form of the listed *facilitar*). Walk 36/36 lessons per course. 36 challenges per course.

## Reviewer changes and additions

- Unit 17 story: "el jefe de la oficina" → "un jefe de su oficina" (Kafka's chief clerk, not the head of the firm).
- Unit 21 story: *una vida en la que* (b1-20-01, later) → *una vida donde*.
- Story `b1-10` relabelled: the invented author and work removed, `type` original.
- Reader A's units: 12 words listed (13 in es-latam), one consolidation item rewritten.
- Reader B's units: its first unmet check was void (107 hits in es-es, 130 in es-latam on the applied content); sent back and fixed by the same reader. Then by the reviewer: two challenge targets, one option (*a mi modo de ver*), es-latam *vídeo* → *video*.
- Challenges: Carlos's grandmother lives in Madrid and he grew up in Hungary, so "every Sunday" became "every summer, when you visited her".

## Facts

`reviewer-facts.md`: Kafka and Dickens checked against Project Gutenberg; the Statue of Liberty date (28 October 1886) and copper skin by web search. Not checked against a text: Martí's chronicle and Bécquer's letters (both stories say they are simplified adaptations, nothing is presented as the author's words).

## For the user

1. **Four of the six units teach no grammar of their own** (17, 19, 21 and most of 23, 27): every screen is a recap of A2 or earlier B1. They are vocabulary and practice units. Fine if intended; the skill map will show few new cells for them.
2. **Orphan story files** `b1-12.json`, `b1-13.json`, `b1-14.json` belong to no lesson (Units 23–27 use `b1-12-picanteria`, `b1-13-cronicanuevayork`, `b1-14-cartasveruela`). Delete, or keep as Library extras.
3. **Vocabulary lists are growing:** 76 words added in this batch (basic and topic words that were in no list: *tecnología, utilizar, vídeo, clínica, casi, viejo, espacio*). Lesson lists that had 3–5 words now have up to 14 (b1-13-05). Say if a lesson list should have a ceiling.
4. `b1-12-picanteria` keeps `author` "Ricardo Palma (estilo)": honest, but it could read as attribution.
5. es-latam now says *video*; `course_variants.py` does not know the pair *vídeo/video* yet (to add if it recurs).
