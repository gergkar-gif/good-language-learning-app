# AI gloss review log

Each week a scheduled review looks over the glosses the Reader's AI fallback produced for words
learners tapped (`python scripts/fill-dictionary-gaps.py pull-ai hu|es`), imports the ones that are
right, and records here what it did. Anything it turned down is listed with the reason, and the word
is added to `ai-rejected.json` so it is not offered again. To overrule a rejection, remove the word
from `ai-rejected.json` and run the pull again, or add the entry by hand to `additions-<lang>.json`.

Newest entries first.
