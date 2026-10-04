import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BASE = ROOT / "content" / "hu"


def register_unit(unit_num: int, core_title: str, core_stems: list, disc_title: str, disc_stems: list, new_skills: dict, new_titles: dict):
    # 1. skill-registry.json
    sr_path = BASE / "indexes" / "skill-registry.json"
    sr = json.loads(sr_path.read_text(encoding="utf-8"))
    for k, v in new_skills.items():
        if k not in sr["skills"]:
            sr["skills"][k] = v
    sr_path.write_text(json.dumps(sr, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated skill-registry.json for Unit {unit_num}")

    # 2. grammar-titles.json
    gt_path = BASE / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))
    for k, v in new_titles.items():
        gt[k] = v
    gt_path.write_text(json.dumps(gt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated grammar-titles.json for Unit {unit_num}")

    # 3. curriculum/units/c1.json
    u_path = BASE / "curriculum" / "units" / "c1.json"
    units = json.loads(u_path.read_text(encoding="utf-8"))
    
    # Avoid duplicate additions
    existing_stems = {stem for u in units for stem in u.get("stems", [])}
    if core_stems[0] not in existing_stems:
        units.append({
            "title": core_title,
            "stems": core_stems,
            "track": "core"
        })
    if disc_stems[0] not in existing_stems:
        disc_entry = {
            "title": disc_title,
            "stems": disc_stems,
            "track": "discourse"
        }
        core_idx = None
        for i, u in enumerate(units):
            if u.get("stems", []) == core_stems:
                core_idx = i
                break
        if core_idx is not None:
            units.insert(core_idx + 1, disc_entry)
        else:
            units.append(disc_entry)
    u_path.write_text(json.dumps(units, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated curriculum/units/c1.json for Unit {unit_num}")
