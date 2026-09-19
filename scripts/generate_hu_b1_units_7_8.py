#!/usr/bin/env python3
"""Generate Hungarian B1 Unit-Pair 7 and Unit-Pair 8:
- Core Unit 7: Education & Learning (b1-07)
- Citizenship Unit 7: The Angevin & Later Medieval Kings (b1-anjouk)
- Core Unit 8: Travel & Mobility (b1-08)
- Citizenship Unit 8: Matthias Corvinus & the Renaissance Court (b1-matyas)
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_json(rel_path, data):
    full_path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

print("Generator script template ready.")
