#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Hungarian B2 Culture, History & Society Track Units 34, 35, and 36:
  - Unit 34: b2-ifjusagikultura (Beats, Festivals & Living Slang: Youth Culture Since the 1960s)
  - Unit 35: b2-tudomanyjovo (Hungary in the 21st-Century Knowledge Economy)
  - Unit 36: b2-magyaridentitas (Synthesis: What It Means to Speak and Understand Hungarian Today)
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
from data_hu_b2_culture_34 import UNIT_34_IFJUSAGIKULTURA  # noqa: E402
from data_hu_b2_culture_35 import UNIT_35_TUDOMANYJOVO  # noqa: E402
from data_hu_b2_culture_36 import UNIT_36_MAGYARIDENTITAS  # noqa: E402


def main():
    print("Building Hungarian B2 Culture Track Units 34, 35, and 36...")
    build_culture_unit(UNIT_34_IFJUSAGIKULTURA)
    build_culture_unit(UNIT_35_TUDOMANYJOVO)
    build_culture_unit(UNIT_36_MAGYARIDENTITAS)
    print("Successfully built Units 34, 35, and 36!")


if __name__ == "__main__":
    main()
