# scripts/archive/

One-shot scripts that have already done their job, kept for history. Nothing in
the build, CI, the pre-push hook or the engine uses them, so nothing here needs
to keep working.

What's in here (archived 2026-09-30, from `scripts/` and one stray root file):

- **Unit generators.** `generate_hu_*`, `data_hu_*`, `helpers_hu_*`,
  `reauthor_hu_*` (Hungarian B1/B2/C1 units); `generate_es_latam_*`, `gen_unit*`,
  `unit3x_*`, `make_unit3x_*`, `reauthor_latam_*` (Latin America units);
  `generate_es_b1_ccse_*`, `gen_es_*` (Spain CCSE and A1/A2 gaps). Each wrote
  lesson, grammar, exercise and vocabulary files once; the output is now the
  content itself and edits happen there.
- **A1/A2 block scaffolding.** `block*_all_reqs.json`, `build_block*`,
  `extract_block*`, `inspect_*`, `overhaul_block*`.
- **One-off repairs and backfills.** `fix_*`, `backfill_*`, `calibrate_*`,
  `check_*`, `dump_*`, `list_*`, `show_*`.
- `download_verbs.py` (the original verb downloader, from the repo root).

These scripts were written against the layout at the time and may use paths
relative to `scripts/`; running one would need that adjusted. To see when and why
one was used, search `ACHIEVED.md` and `git log -- scripts/archive/<name>`.
