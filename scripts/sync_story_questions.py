"""Copy es-es comprehension questions to es-latam stories, in es-latam's
words (ROADMAP 153). es-latam's story questions drift from es-es (older
explanation wording, questions copied from other stories in A1), so the
fixes a reader makes to es-es questions often don't mirror (old text not
found). After a batch, this sets each listed es-latam story's
narration.pedagogical.comprehensionQuestions to the es-es ones, converted
with course_variants (*billetes* -> *boletos*); it refuses a story whose
converted questions still hold *vosotros* forms or a word the converter
refuses, and writes nothing then.

    python scripts/sync_story_questions.py <level> <story stem>... [--dry-run]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import course_variants as cv  # noqa: E402

VOS = re.compile(r"\b(vosotr[oa]s|os|habéis|\w+áis|\w+éis)\b", re.I)


def conv(x, bad):
    if isinstance(x, str):
        y, _, refused = cv.convert(x, "es-latam")
        if refused or VOS.search(y):
            bad.append(y[:60])
        return y
    if isinstance(x, list):
        return [conv(i, bad) for i in x]
    if isinstance(x, dict):
        return {k: conv(v, bad) for k, v in x.items()}
    return x


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    if len(args) < 2:
        sys.exit(__doc__)
    level, stems = args[0], args[1:]
    out, failed = {}, False
    for s in stems:
        pa = ROOT / f"content/es-es/stories/original/{level}/{s}.json"
        pb = ROOT / f"content/es-latam/stories/original/{level}/{s}.json"
        a, text = json.loads(pa.read_text(encoding="utf-8")), pb.read_text(encoding="utf-8")
        b = json.loads(text)
        bad = []
        qs = conv(a["narration"]["pedagogical"]["comprehensionQuestions"], bad)
        if bad:
            print(f"refused {s}: {bad}")
            failed = True
            continue
        changed = qs != b["narration"]["pedagogical"].get("comprehensionQuestions")
        b["narration"]["pedagogical"]["comprehensionQuestions"] = qs
        indent = len(re.search(r'\n( +)"', text).group(1))
        out[pb] = json.dumps(b, ensure_ascii=False, indent=indent) + "\n"
        print(f"{s}: {'updated' if changed else 'already the same'}")
    if failed:
        sys.exit("nothing written")
    if "--dry-run" not in sys.argv:
        for p, t in out.items():
            p.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    main()
