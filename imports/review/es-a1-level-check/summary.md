# Spanish A1 level checklist (2026-10-21), both courses

Run per docs/unit-pipeline-log.md § "Before calling a level done".

- `freeze_unit.py --status`: es-es a1 26/26, es-latam a1 26/26 frozen.
- `check-content.py es-es a1` and `es-latam a1`: 0 errors, 0 suspects (every remaining suspect accepted with a reason at freeze; lists in each batch folder's accept-list.txt).
- `validate-content.py --warnings`: no A1 skill in either course's warnings (the 64 thin skills listed are A2-C1); `--changed` passes.
- Walk (`walk_lessons.js`, TTS stubbed): es-es 156/156, es-latam 156/156 lessons to their summary, no console errors, no failed requests (walk-es-es.json, walk-es-latam.json).
- Story narration timings refreshed for the edited stories (`narrate-story.py`, which now keeps reviewed speakers and questions); story audio is live TTS from the text, so no recording step.
- Pre-push gate: check-content --changed and the test suite pass.

Not covered: speaking and challenge steps (skipped by the walk), wrong-answer paths, live TTS audio, the live site (not reachable from the cloud container), and a native speaker's read.
