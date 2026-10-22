# es A2 level checklist (2026-10-22)

Run per docs/unit-pipeline-log.md § "Before calling a level done", after batch 31–33.

| Check | es-es | es-latam |
|---|---|---|
| `freeze_unit.py --status` | 33 / 33 frozen | 32 / 32 frozen |
| `check-content.py <course> a2` | 0 errors, 0 unaccepted suspects | 0 errors, 0 unaccepted suspects |
| `validate-content.py --warnings` | no A2 warning; output identical to origin/master before the batch | same |
| `walk_lessons.js <course> a2 --jobs 4` (challenges typed and graded) | 198 / 198 OK, 0 FAIL (402 s) | 192 / 192 OK, 0 FAIL (407 s) |
| Stories read in order | 33 A2 stories, no contradiction left | es-latam endings checked for Units 31–32 |
| Test suite | run by the pre-push gate on push | same |

Not covered: speaking steps (microphone), spoken challenge answers,
wrong-answer paths, audio (TTS stubbed), and a native speaker's eye.

Left for the user:
- No story shows Carlos and Meg leaving Hanoi. Unit 31 opens in Madrid,
  "de camino a su nueva vida en Budapest", after Unit 30 in Hanoi.
- The stories never tell the grandmothers apart. The grandmother in Madrid
  is his father's mother; the childhood stories show a grandmother in Hungary.
- es-latam has a Spain reading outside the units
  (`stories/current/a2/a2-01-sagradafamilia.json`).
- `ponerse a` (Unit 32 lesson 04) is tagged `perifrasis-verbales`, while
  `skills/es.json` lists it under `inceptive-periphrases` (B2). The skill
  list is frozen, so moving it needs your sign-off.
