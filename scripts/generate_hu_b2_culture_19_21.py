#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 19, 20, and 21:
  - Unit 19: b2-tajegysegek (Alföld, Dunántúl & Felföld: Regional Identities)
  - Unit 20: b2-falutortenet (The Changing Hungarian Village: From Tanya to Today)
  - Unit 21: b2-gazdasagiatmenet (From Goulash Socialism to the European Single Market)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402
from data_hu_b2_culture_19 import UNIT_19_TAJEGYSEGEK  # noqa: E402
from data_hu_b2_culture_20 import UNIT_20_FALUTORTENET  # noqa: E402
from data_hu_b2_culture_21 import UNIT_21_GAZDASAGIATMENET  # noqa: E402


def main():
    print("Building Hungarian B2 Culture Units 19, 20, and 21...")
    build_culture_unit(UNIT_19_TAJEGYSEGEK)
    build_culture_unit(UNIT_20_FALUTORTENET)
    build_culture_unit(UNIT_21_GAZDASAGIATMENET)
    print("Successfully built Culture Units 19, 20, and 21!")


if __name__ == "__main__":
    main()
