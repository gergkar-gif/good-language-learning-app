"""Copy a fix list from one course to its sibling course (ROADMAP 153).

es-es and es-latam share most lesson files byte for byte (A1: 147 of 156
exercise files, 115 of 134 screens); the rest differ on purpose (*vosotros*
in es-es, *ustedes* and *jugo* in es-latam). A Spanish unit is read once,
in es-es, and its filtered fix list is mirrored here instead of reading
es-latam again. This rewrites each fix's path to the other course and
checks it there in order, as apply_replacements.py would apply it:

- a text fix whose old text occurs exactly once in the sibling file (after
  the fixes before it) is mirrored;
- a `set` fix whose id exists once in the sibling file is mirrored;
- anything else (the file is missing, the text differs or occurs twice, the
  id is absent) goes to <out>.unmatched.json for the reviewer: usually a
  course variant that needs its own wording, or a fix that doesn't apply.

Nothing is written to content; run check_fixes.py on the mirrored list for
the sibling course, then apply_replacements.py, as for any list.

    python scripts/mirror_fixes.py <fixes.json> <from course> <to course> <out.json>
    python scripts/mirror_fixes.py fixes-u5.json es-es es-latam fixes-u5.latam.json
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("apply_replacements", ROOT / "scripts/apply_replacements.py")
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    src, frm, to, out = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
    fixes = [ar.norm(f) for f in json.loads(Path(src).read_text(encoding="utf-8"))]
    texts, mirrored, unmatched = {}, [], []
    for fix in fixes:
        path = fix.get("file", "").replace("\\", "/")
        prefix = f"content/{frm}/"
        if prefix not in path:
            unmatched.append({**fix, "why_unmatched": f"not a {frm} file"})
            continue
        new_path = path.replace(prefix, f"content/{to}/", 1)
        p = ROOT / new_path[new_path.index("content/"):]
        if not p.is_file():
            unmatched.append({**fix, "why_unmatched": f"no {p.relative_to(ROOT)}"})
            continue
        text = texts.get(p, p.read_text(encoding="utf-8"))
        if "set" in fix:
            new_text, err = ar.set_fields(text, fix.get("id"), fix["set"])
        elif text.count(fix.get("old", "")) == 1 and fix.get("old"):
            new_text, err = text.replace(fix["old"], fix["new"], 1), None
        else:
            new_text, err = text, f"old text found {text.count(fix.get('old', '')) if fix.get('old') else 0}x"
        if err:
            unmatched.append({**fix, "file": new_path, "why_unmatched": err})
            continue
        texts[p] = new_text
        mirrored.append({**fix, "file": new_path})
    out.write_text(json.dumps(mirrored, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    um = out.with_suffix(".unmatched.json")
    um.write_text(json.dumps(unmatched, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(mirrored)} mirrored to {out}, {len(unmatched)} unmatched in {um}")
    for f in unmatched:
        print(f"  unmatched: {f.get('file')} {f.get('id') or repr(f.get('old', ''))[:60]}  ({f['why_unmatched']})")


if __name__ == "__main__":
    main()
