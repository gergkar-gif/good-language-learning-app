#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Hungarian B2 Culture, History & Society Track Units 28, 29, and 30:
  - Unit 28: b2-diaszpora (Global Hungarians: Émigré Waves & Returnees)
  - Unit 29: b2-kulpolitika (Central European Geopolitics & Visegrád Cooperation)
  - Unit 30: b2-jogvedelem (Public Administration, Ombudsman & Civic Rights)
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
from data_hu_b2_culture_28 import UNIT_28_DIASZPORA  # noqa: E402
from data_hu_b2_culture_29 import UNIT_29_KULPOLITIKA  # noqa: E402
from data_hu_b2_culture_30 import UNIT_30_JOGVEDELEM  # noqa: E402


def main():
    print("Building Hungarian B2 Culture Track Units 28, 29, and 30...")
    build_culture_unit(UNIT_28_DIASZPORA)
    build_culture_unit(UNIT_29_KULPOLITIKA)
    build_culture_unit(UNIT_30_JOGVEDELEM)
    print("Successfully built Units 28, 29, and 30!")


if __name__ == "__main__":
    main()
