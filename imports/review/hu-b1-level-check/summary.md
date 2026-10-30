# HU B1 level checklist (Claude, 2026-10-30)

Run after the citizenship read-through froze the last units (ROADMAP 153; pipeline doc § "Before
calling a level done"). Outputs in this folder.

| Check | Result |
|---|---|
| `freeze_unit.py --status hu` | B1 75/75 frozen (A1 33/33, A2 47/47 still frozen) |
| `check-content.py hu b1` | 0 errors, 0 suspects (accepted findings are stored with each unit) — `check-content.txt` |
| `validate-content.py --warnings` | hu 7,987 passed, 0 failed; no warning for B1 (the 704 retired-slug warnings are all B2) — `validate-warnings.txt` |
| Challenges | 450/450 B1 lessons have a hand-written entry |
| `walk_lessons.js hu b1 --jobs 4` (dev server on 8131) | 450/450 lessons play to the summary, every challenge on screen and its typed target accepted by the grader; 0 console errors or failed requests; 517 s — `walk.txt` |
| `fix_glued_blanks.py hu b1` | no glued blanks |

## Not covered by these checks

- **Speaking steps:** skipped in 448 lessons (microphone; two per lesson).
- **Spoken challenge answers:** only the typed target is graded.
- **Wrong-answer paths:** the walk answers correctly; feedback for wrong answers is not exercised.
- **Audio:** TTS is stubbed in the walk; real voices, the live site and `--live-tts` can't be
  reached from the cloud container.
- **A native speaker's eye:** readers and reviewer are not native speakers; Hungarian naturalness is
  the user's spot-check.
- **Facts the web could not settle** (listed per batch in `imports/review/hu-b1-batch-cit-*/review.md`):
  the citizenship oath's exact wording (Unit 73 paraphrases it), Apponyi's quoted line (Unit 42),
  and present-day details that may change again after 2026 (office names, procedures, figures).
- **Outside B1:** B2 and C1 files still using *vármegye*/*főispán* (list in
  `imports/review/hu-b1-batch-cit-64-69/review.md`); B2's 704 retired skill slugs.

## Decided by the user (2026-10-30)

- The citizenship oath stays paraphrased in Unit 73.
- Apponyi's line stays as a voice line in Unit 42.
- The five vocabulary words used nowhere in their unit stay.
- The *megye*/*kormánymegbízott* change is approved; B2 and C1 still to do.
