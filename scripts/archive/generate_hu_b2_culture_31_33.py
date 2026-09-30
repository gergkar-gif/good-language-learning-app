#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Hungarian B2 Culture, History & Society Track Units 31, 32, and 33:
  - Unit 31: b2-borkultura (Paprika, Tokaj & Terroir: A Cultural History of Hungarian Cuisine)
  - Unit 32: b2-sporttortenet (From Alfréd Hajós to the Aranycsapat: Sport & National Identity)
  - Unit 33: b2-eszmetortenet (Central European Political Thought: Széchenyi, Eötvös, Polányi, Bibó)
"""
import sys
from pathlib import Path

# Add helper module path
HELPER_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\49f3f727-7f38-498b-9bfc-f33086519da1\scratch")
sys.path.insert(0, str(HELPER_DIR))

# Add scripts directory for unit data imports
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from b2_unit_builder_helper import build_culture_unit  # noqa: E402
from data_hu_b2_culture_31 import UNIT_31_BORKULTURA  # noqa: E402
from data_hu_b2_culture_32 import UNIT_32_SPORTTORTENET  # noqa: E402
from data_hu_b2_culture_33 import UNIT_33_ESZMETORTENET  # noqa: E402


def main():
    print("Building Hungarian B2 Culture Track Units 31, 32, and 33...")
    build_culture_unit(UNIT_31_BORKULTURA)
    build_culture_unit(UNIT_32_SPORTTORTENET)
    build_culture_unit(UNIT_33_ESZMETORTENET)
    print("Successfully built Units 31, 32, and 33!")


if __name__ == "__main__":
    main()
