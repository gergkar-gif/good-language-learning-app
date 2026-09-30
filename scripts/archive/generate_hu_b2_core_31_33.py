#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 31, 32, and 33:
  - Unit 31: Gastronomy, Conviviality & Cultural Rituals (b2-resultative-similes)
  - Unit 32: Competition, Mastery & Peak Performance (b2-consecutive-degree)
  - Unit 33: Political Philosophy, Freedom & Historical Hysteria (b2-cleft-identification)

Uses build_core_unit from b2_unit_builder_helper.py.
"""
import json
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from b2_unit_builder_helper import ROOT, build_core_unit  # noqa: E402
from data_hu_b2_core_31 import UNIT_31  # noqa: E402
from data_hu_b2_core_32 import UNIT_32  # noqa: E402
from data_hu_b2_core_33 import UNIT_33  # noqa: E402


def update_curriculum_units():
    """Wire fully authored B2 Core units 31, 32, 33 into content/hu/curriculum/units/b2.json."""
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
            "title": UNIT_31["title"],
            "stems": [
                "b2-31-01",
                "b2-31-02",
                "b2-31-03",
                "b2-31-04",
                "b2-31-05",
                "b2-31-consolidation",
            ],
            "track": "core",
        },
        {
            "title": UNIT_32["title"],
            "stems": [
                "b2-32-01",
                "b2-32-02",
                "b2-32-03",
                "b2-32-04",
                "b2-32-05",
                "b2-32-consolidation",
            ],
            "track": "core",
        },
        {
            "title": UNIT_33["title"],
            "stems": [
                "b2-33-01",
                "b2-33-02",
                "b2-33-03",
                "b2-33-04",
                "b2-33-05",
                "b2-33-consolidation",
            ],
            "track": "core",
        },
    ]

    added = 0
    for u_spec in units_to_add:
        if not any(stem in existing_stems for stem in u_spec["stems"]):
            units_data.append(u_spec)
            added += 1

    if added > 0:
        b2_units_path.write_text(json.dumps(units_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Added {added} units to {b2_units_path.relative_to(ROOT)}")
    else:
        print("Curriculum b2.json already contains units 31, 32, 33")


def main():
    print("Building Hungarian B2 Core Units 31, 32, and 33...")
    for spec in (UNIT_31, UNIT_32, UNIT_33):
        print(f"Building Unit {spec['unit_num']}: {spec['title']}...")
        build_core_unit(spec)
    update_curriculum_units()
    print("Successfully built all 3 units (b2-31, b2-32, b2-33)!")


if __name__ == "__main__":
    main()
