# Curriculum Map — superseded

This file (and `lessons/a1/module-1-meeting-people-lessons-1-4.md`) was written before I found the project's real content tree at `content/es/`. It mapped the 16 planning docs in "App-curriculum docs" onto an invented module structure ("Module 1: Meeting People", etc.) that doesn't match how the app is actually built.

The real A1 curriculum lives in `content/es/`:

- `content/es/curriculum/curriculum.json` — the 20-lesson A1 list (titles, grammar, goals), corrected 2026-08-07 to match the story content actually written.
- `content/es/guides/a1.md` — full lesson-by-lesson overview (goal, grammar, vocab theme, story event).
- `content/es/guides/a1-grammar.md`, `a1-vocabulary-themes.md`, `a1-story.md`, `a1-reading-plan.md`, `a1-learning-objectives.md` — per-aspect progressions, all reconciled against the actual stories.
- `content/es/lessons/a1/a1-01.json` through `a1-04.json` — fully built lessons (goals, grammar, vocabulary, story, exercises, checklist). Lessons 5–20 exist as scaffolds with story chapters written but grammar/vocabulary/exercise files not yet built.
- `content/es/stories/original/a1/` — all 20 story chapters, the ground truth the rest of the spec was corrected to match.
- `content/es/characters/characters.md` — character bible, corrected for first-appearance timing.

The A1 word-target/lesson-count figures in this old file (142 total core lessons, B1/B2/C1 module structure from the 16 planning docs) are a separate, higher-level planning layer that was never reconciled against `content/es/`. Worth deciding whether the 16 docs in "App-curriculum docs" should be updated to describe the real content structure, the way the `content/es/guides/` docs now are — they currently describe an aspirational module framework that A1's actual implementation doesn't follow.
