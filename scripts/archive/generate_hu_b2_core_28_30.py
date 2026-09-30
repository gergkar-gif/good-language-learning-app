#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 28, 29, and 30:
  - Unit 28: Exile, Emigration & Global Networks (b2-figurative-preverbs)
  - Unit 29: Diplomacy, Alliances & Sovereignty (b2-diplomatic-conditionals)
  - Unit 30: Civic Participation, Advocacy & Public Institutions (b2-abstract-case-government)

Uses build_core_unit from b2_unit_builder_helper.py.
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from b2_unit_builder_helper import build_core_unit  # noqa: E402
from data_hu_b2_core_28 import UNIT_28  # noqa: E402
from data_hu_b2_core_29 import UNIT_29  # noqa: E402
from data_hu_b2_core_30 import UNIT_30  # noqa: E402


def main():
    print("Building Hungarian B2 Core Units 28, 29, and 30...")
    for spec in (UNIT_28, UNIT_29, UNIT_30):
        print(f"Building Unit {spec['unit_num']}: {spec['title']}...")
        build_core_unit(spec)
    print("Successfully built all 3 units (b2-28, b2-29, b2-30)!")


if __name__ == "__main__":
    main()
