#!/usr/bin/env python3
"""
Master runner for Spanish (LatAm) B2 Units 2 & 3:
  - Core Unit 2: Narrative Time & Aspect (b2-02)
  - LatAm Unit 2: Mexico II: The North, the Border & Industrial Modernity (b2-mexiconorte)
  - Core Unit 3: Hypothesizing & Probability (b2-03)
  - LatAm Unit 3: Mexico III: The South, Indigenous Pueblos & Biodiversity (b2-mexicosur)
"""

from generate_es_latam_b2_core_02 import generate_core_unit_2
from generate_es_latam_b2_latam_02 import generate_latam_unit_2
from generate_es_latam_b2_core_03 import generate_core_unit_3
from generate_es_latam_b2_latam_03 import generate_latam_unit_3


def main():
    print("=== Generating Core Unit 2 ===")
    generate_core_unit_2()

    print("\n=== Generating LatAm Unit 2 ===")
    generate_latam_unit_2()

    print("\n=== Generating Core Unit 3 ===")
    generate_core_unit_3()

    print("\n=== Generating LatAm Unit 3 ===")
    generate_latam_unit_3()

    print("\n=== All 4 units (24 lessons) generated successfully! ===")


if __name__ == "__main__":
    main()
