#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 25, 26, and 27 (b2-25, b2-26, b2-27)
using build_core_unit from b2_unit_builder_helper.py.
"""
import json
import sys
from pathlib import Path

# Add helper module path as required
sys.path.insert(
    0,
    r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch",
)
from b2_unit_builder_helper import ROOT, build_core_unit

# Add scripts directory to path for unit data imports
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from data_hu_b2_core_25 import UNIT_25
from data_hu_b2_core_26 import UNIT_26
from data_hu_b2_core_27 import UNIT_27


def update_curriculum_units():
    """Wire fully authored B2 Core units 25, 26, 27 into content/hu/curriculum/units/b2.json."""
    b2_units_path = ROOT / "content" / "hu" / "curriculum" / "units" / "b2.json"
    if not b2_units_path.exists():
        print(f"Warning: {b2_units_path} does not exist, skipping curriculum wiring.")
        return

    units_data = json.loads(b2_units_path.read_text(encoding="utf-8"))
    existing_stems = set()
    for u in units_data:
        for s in u.get("stems", []):
            existing_stems.add(s)

    units_to_add = [
        {
            "unit": 25,
            "title": UNIT_25["title"],
            "stems": [
                "b2-25-01",
                "b2-25-02",
                "b2-25-03",
                "b2-25-04",
                "b2-25-05",
                "b2-25-consolidation",
            ],
            "track": "core",
        },
        {
            "unit": 26,
            "title": UNIT_26["title"],
            "stems": [
                "b2-26-01",
                "b2-26-02",
                "b2-26-03",
                "b2-26-04",
                "b2-26-05",
                "b2-26-consolidation",
            ],
            "track": "core",
        },
        {
            "unit": 27,
            "title": UNIT_27["title"],
            "stems": [
                "b2-27-01",
                "b2-27-02",
                "b2-27-03",
                "b2-27-04",
                "b2-27-05",
                "b2-27-consolidation",
            ],
            "track": "core",
        },
    ]

    added = 0
    for u_spec in units_to_add:
        if not any(stem in existing_stems for stem in u_spec["stems"]):
            units_data.append({
                "title": u_spec["title"],
                "stems": u_spec["stems"],
                "track": u_spec["track"],
            })
            added += 1

    if added > 0:
        b2_units_path.write_text(json.dumps(units_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Added {added} units to {b2_units_path.relative_to(ROOT)}")
    else:
        print("Curriculum b2.json already contains units 25, 26, 27")


def main():
    print("Building Hungarian B2 Core Units 25, 26, and 27...")
    for spec in (UNIT_25, UNIT_26, UNIT_27):
        build_core_unit(spec)
    update_curriculum_units()
    print("All B2 Core Units 25-27 generated successfully!")


if __name__ == "__main__":
    main()
