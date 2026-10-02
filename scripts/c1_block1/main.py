#!/usr/bin/env python3
"""
Orchestrator for Hungarian C1 Block 1 Remaining Units Generation (Units 02 to 06).
"""

import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.generate_hu_c1_block1_rest import update_registries
from scripts.c1_block1.unit02 import generate_unit_2
from scripts.c1_block1.unit03 import generate_unit_3
from scripts.c1_block1.unit04 import generate_unit_4
from scripts.c1_block1.unit05 import generate_unit_5
from scripts.c1_block1.unit06 import generate_unit_6


def main():
    print("==================================================")
    print("Starting Generation of Hungarian C1 Block 1 (Units 02-06)")
    print("==================================================")
    
    print("\nStep 1: Updating Registries and Curriculum Units...")
    update_registries()

    print("\nStep 2: Generating Unit 02 (Core: Syntactic Compression, Discourse: Essay Art)...")
    generate_unit_2()

    print("\nStep 3: Generating Unit 03 (Core: Epistemic Hedging, Discourse: Epistemology)...")
    generate_unit_3()

    print("\nStep 4: Generating Unit 04 (Core: Rhetorical Refutation, Discourse: Debate Culture)...")
    generate_unit_4()

    print("\nStep 5: Generating Unit 05 (Core: Irony & Litotes, Discourse: Urban Satire)...")
    generate_unit_5()

    print("\nStep 6: Generating Unit 06 (Core: Metaphor & Compounding, Discourse: Landscape of Mind)...")
    generate_unit_6()

    print("\n==================================================")
    print("Successfully Generated All Block 1 Units (02-06)!")
    print("==================================================")


if __name__ == "__main__":
    main()
