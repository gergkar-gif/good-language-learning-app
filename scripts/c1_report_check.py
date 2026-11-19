#!/usr/bin/env python3
"""Check that an Antigravity ES C1 unit report has every section the reviewer needs (2026-11-19).

The reports of Units 18-19 left out the norm-claims list, which the reviewer checks against the
RAE before the read; later reports in a long chat get shorter. Run before committing a unit:

    python scripts/c1_report_check.py <unit number>

Fails (exit 1) when a section is missing or empty: the model/time line, "Self-read: N fixes",
"Norm claims" (at least one quoted claim, or the words "no normative claim"), "Checks", and the
Spanish lines the writer is unsure of ("unsure" or "none").
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEEDED = [
    ("model and time", r"(?im)^\W*\**\s*(model|wall-clock)"),
    ("Self-read: N fixes", r"(?i)self-read:\s*\**\s*\d+\s+fix"),
    ("Norm claims section", r"(?im)^#+\s*norm claims"),
    ("Checks section", r"(?im)^#+\s*check"),
    ("unsure Spanish lines (or 'none')", r"(?i)unsure|none"),
]


def main(argv):
    if not argv:
        sys.exit(__doc__)
    p = ROOT / f"imports/review/es-c1-antigravity-{int(argv[0]):02d}/report.md"
    if not p.exists():
        sys.exit(f"missing {p.relative_to(ROOT)}")
    t = p.read_text(encoding="utf-8")
    bad = [name for name, rx in NEEDED if not re.search(rx, t)]
    m = re.search(r"(?ims)^#+\s*norm claims[^\n]*\n(.*?)(?=^#+\s|\Z)", t)
    if m and not (re.search(r"\*[^*]+\*", m.group(1)) or re.search(r"(?i)no normative claim", m.group(1))):
        bad.append("Norm claims section is empty (quote each claim, with its screen id)")
    for b in bad:
        print(f"missing: {b}")
    print("report OK" if not bad else f"{len(bad)} missing: complete the report before committing")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
