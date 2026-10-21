"""Refreeze frozen units that this change edits, keeping their accepted findings (ROADMAP 153).

A course-wide script (fix_variant_vocab.py, fix_story_metadata.py,
move_unit.py) edits units that are already frozen; `check-content.py
--changed` then blocks the push until each is unfrozen and frozen again in
the same change, and `freeze_unit.py --unfreeze` drops a unit's accepted
findings. This does both for every frozen unit that differs from
origin/master, passing the stored accepted findings back. A unit with a
finding that isn't accepted is refused and listed: fix it (or accept it with
freeze_unit.py by hand), then run this again.

    python scripts/refreeze_changed.py --reason "..." [--accept "<check>:<id>:<why>" ...] [--dry-run]

--accept adds a newly accepted finding to whichever changed unit has it
(a new check's false positive in a frozen unit).
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def main():
    if "--reason" not in sys.argv:
        sys.exit(__doc__)
    reason = sys.argv[sys.argv.index("--reason") + 1]
    dry = "--dry-run" in sys.argv
    extra = {}
    for i, a in enumerate(sys.argv):
        if a == "--accept":
            check, eid, why = sys.argv[i + 1].split(":", 2)
            extra[(check, eid)] = why
    base = cc.Source("origin/master")
    refused = 0
    for course, level, uid in sorted(cc.changed_units()):
        key = f"{level}/{uid}"
        was = cc.frozen_units(base, course).get(key)
        now = cc.frozen_units(cc.Source(), course).get(key)
        if was is None or now != was:
            continue  # not frozen, or already refrozen in this change
        accepted = list(was.get("accepted") or [])
        keep = {(a["check"], a["id"]) for a in accepted}
        found = cc.run(cc.Source(), course, [level], uid)
        accepted += [{"check": c, "id": i, "why": extra[(c, i)]} for c, i in dict.fromkeys((f[3], f[4]) for f in found)
                     if (c, i) in extra and (c, i) not in keep]
        keep = {(a["check"], a["id"]) for a in accepted}
        open_ = [f for f in found if (f[3], f[4]) not in keep]
        if open_:
            refused += 1
            print(f"REFUSED {course} {key}: {len(open_)} finding(s) not accepted")
            for f in open_:
                print(f"    {f[3]} {f[4]} {f[5][:90]}")
            continue
        print(f"{'would refreeze' if dry else 'refreezing'} {course} {key} ({len(accepted)} accepted finding(s) kept)")
        if dry:
            continue
        run = lambda *a: subprocess.run(["python3", str(ROOT / "scripts/freeze_unit.py"), *a], cwd=ROOT,
                                        capture_output=True, text=True, check=True)
        run("--unfreeze", course, level, uid, "--reason", reason)
        # an accepted finding the edit removed (a rewritten consolidation copy) is
        # dropped: freeze_unit refuses to accept what is no longer reported
        present = {(f[3], f[4]) for f in cc.run(cc.Source(), course, [level], uid)}
        gone = [a for a in accepted if (a["check"], a["id"]) not in present]
        if gone:
            print(f"    dropped {len(gone)} accepted finding(s) no longer reported: " + ", ".join(f"{a['check']}:{a['id']}" for a in gone))
        accepted = [a for a in accepted if (a["check"], a["id"]) in present]
        args = [course, level, uid, "--reason", (was.get("reason") or "") + f" | refrozen: {reason}"]
        for a in accepted:
            args += ["--accept", f"{a['check']}:{a['id']}:{a.get('why', '')}"]
        run(*args)
    sys.exit(1 if refused else 0)


if __name__ == "__main__":
    main()
