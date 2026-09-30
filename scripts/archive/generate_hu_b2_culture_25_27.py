#!/usr/bin/env python3
"""
Generates Hungarian B2 Culture, History & Society Track Units 25, 26, and 27:
  - Unit 25: b2-alkotmanytortenet (From the Historical Constitution to Constitutional Review)
  - Unit 26: b2-nemzetisegek (Thirteen Nationalities & Shared Cultural Heritage)
  - Unit 27: b2-hatarontul (Hungarian Communities Across the Carpathian Basin Today)
"""
import sys
from pathlib import Path

HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402
from data_hu_b2_culture_25 import UNIT_25_ALKOTMANYTORTENET  # noqa: E402
from data_hu_b2_culture_26 import UNIT_26_NEMZETISEGEK  # noqa: E402
from data_hu_b2_culture_27 import UNIT_27_HATARONTUL  # noqa: E402


def main():
    print("Building Hungarian B2 Culture Units 25, 26, and 27...")
    build_culture_unit(UNIT_25_ALKOTMANYTORTENET)
    build_culture_unit(UNIT_26_NEMZETISEGEK)
    build_culture_unit(UNIT_27_HATARONTUL)
    print("All 3 Culture Track units (25, 26, 27) built successfully!")


if __name__ == "__main__":
    main()
