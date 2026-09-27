#!/usr/bin/env python3
"""
Generates Hungarian B2 Core Units 34, 35, and 36:
  - Unit 34: Slang, Register Shifting & Living Language (b2-twin-words-register)
  - Unit 35: Technology, Futurism & Human Agency (b2-speculative-conditionals)
  - Unit 36: Mastery & Voice: Upper-Intermediate Synthesis (b2-mastery-synthesis)

Uses build_core_unit from b2_unit_builder_helper.py.
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from b2_unit_builder_helper import build_core_unit  # noqa: E402
from data_hu_b2_core_34 import UNIT_34  # noqa: E402
from data_hu_b2_core_35 import UNIT_35  # noqa: E402
from data_hu_b2_core_36 import UNIT_36  # noqa: E402


def main():
    print("Building Hungarian B2 Core Units 34, 35, and 36...")
    for spec in (UNIT_34, UNIT_35, UNIT_36):
        print(f"Building Unit {spec['unit_num']}: {spec['title']}...")
        build_core_unit(spec)
    print("Successfully built all 3 units (b2-34, b2-35, b2-36)!")


if __name__ == "__main__":
    main()
