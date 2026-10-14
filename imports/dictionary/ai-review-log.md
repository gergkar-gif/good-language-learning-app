# AI gloss review log

Each week a scheduled review looks over the glosses the Reader's AI fallback produced for words
learners tapped (`python scripts/fill-dictionary-gaps.py pull-ai hu|es`), imports the ones that are
right, and records here what it did. Anything it turned down is listed with the reason, and the word
is added to `ai-rejected.json` so it is not offered again. To overrule a rejection, remove the word
from `ai-rejected.json` and run the pull again, or add the entry by hand to `additions-<lang>.json`.

Newest entries first.

## 2026-10-14

- **hu:** 0 approved, 3 rejected (5 cached answers, 3 not yet in the dictionary).
- **es:** 0 approved, 0 rejected (1 cached answer, already in the dictionary).
- Nothing imported, so no coverage audit and no `sw.js` bump.

Rejected (hu):
- `granja`: Spanish word ("farm"), not Hungarian; cached under the hu course.
- `mayoría`: Spanish word ("majority"), not Hungarian; cached under the hu course.
- `quería`: Spanish word (form of *querer*), not Hungarian; cached under the hu course.

All three look like taps on Spanish text while the Hungarian course was active, so the Worker
glossed them as Spanish but cached them under `hu`.
