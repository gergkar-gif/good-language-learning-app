#!/usr/bin/env python3
"""
Master runner for Spanish (LatAm) B2 Units 4, 5 & 6:
  - Core Unit 4: Influence, Will & Value Judgments (b2-04)
  - LatAm Unit 4: Guatemala: Mayan Heritage, Highland Communities & Modern Transitions (b2-guatemala)
  - Core Unit 5: Doubt, Denial & Epistemic Stance (b2-05)
  - LatAm Unit 5: El Salvador & Honduras: Copán, Memory, Migration & Resilience (b2-salvadorhonduras)
  - Core Unit 6: Emotional Reactions & Affective Stance (b2-06)
  - LatAm Unit 6: Nicaragua: Land of Lakes, Volcanoes & Poetry (b2-nicaragua)
"""

from generate_es_latam_b2_core_04 import generate_core_unit_4
from generate_es_latam_b2_latam_04 import generate_latam_unit_4
from generate_es_latam_b2_core_05 import generate_core_unit_5
from generate_es_latam_b2_latam_05 import generate_latam_unit_5
from generate_es_latam_b2_core_06 import generate_core_unit_6
from generate_es_latam_b2_latam_06 import generate_latam_unit_6


def main():
    print("=== Generating Core Unit 4 ===")
    generate_core_unit_4()

    print("\n=== Generating LatAm Unit 4 (Guatemala) ===")
    generate_latam_unit_4()

    print("\n=== Generating Core Unit 5 ===")
    generate_core_unit_5()

    print("\n=== Generating LatAm Unit 5 (El Salvador & Honduras) ===")
    generate_latam_unit_5()

    print("\n=== Generating Core Unit 6 ===")
    generate_core_unit_6()

    print("\n=== Generating LatAm Unit 6 (Nicaragua) ===")
    generate_latam_unit_6()

    print("\n=== All 6 units (36 lessons) generated successfully! ===")


if __name__ == "__main__":
    main()
