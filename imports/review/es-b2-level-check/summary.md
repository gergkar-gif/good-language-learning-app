# ES B2 core level checklist (es-latam, 2026-11-14)

Scope: the 36 core units (216 lessons). The 36 hidden `latam` units are not read yet and are
out of scope; they carry all of the level's open findings (490 errors / 638 suspects).

| Check | Result |
|---|---|
| `freeze_unit.py --status` | core 36/36 frozen (level 36/72) |
| `check-content.py es-latam b2` | core: 0 errors, 0 unaccepted suspects |
| `validate-content.py --warnings` | es-latam: none |
| `walk_lessons.js` (core stems, challenges typed and graded) | 216/216, 0 failures |
| unmet words, all core stems | 6 kept cases (a title word ×2, *haberlo*, *hubiésemos* ×2, *consiste*) |
| Reader library: B2 stories with no unit, not hidden | 0 |
| Asterisks in the 36 core texts | 0 |
| Story `summary` language | 36/36 Spanish (Units 24 and 26 translated today) |

Fixed during the checklist: reader and critic claims in 11 items and 2 challenges (new check
`item-reader`), `nominalization` merged (user), two summaries.

Not covered: speaking steps, spoken challenge answers, wrong-answer paths, audio (TTS is
stubbed in the container), and a native speaker's eye. Facts for Units 31–36 rest on web-search
results only (Wikipedia, Firecrawl and Perplexity unreachable that night). Not verified against
a source: regional word lists in 34-02 and *ustedeo* regions in 34-01 (user: "thats ok").
