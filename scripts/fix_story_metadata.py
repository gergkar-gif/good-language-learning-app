"""Fix placeholder story metadata that check-content reports (ROADMAP 153).

Three defects left by the bulk story commits of 2026-09-19/20, each a
`check-content` check:

- `story-voice-gender`: a recurring character's narration voice has the
  wrong gender (Daniela "male"). Set from check-content's CHARACTER_GENDER.
- `story-questions-copy` (es-latam): the comprehension questions are a
  placeholder set copied into many stories. Where es-es has the same story
  (same file path) with its own questions, copy those, with es-latam's
  course words (*zumo* -> *jugo*, scripts/course_variants.py).
- `story-key-vocab` (A1-A2): `keyVocabulary` words that aren't in the story
  (the *conocer*/*intercambio* placeholder). Rebuilt from the vocabulary
  list of the lesson that shows the story: up to three of its words that
  occur in the story text.

It refuses rather than guesses: a story with copied questions and no es-es
twin (es-latam B1/B2 world stories, HU B1 world stories), or a key-word
list with fewer than two list words in the story, is listed, not changed.
Narration audio is not touched: a voice change needs the story's audio
regenerated (list them in ROADMAP 153).

    python scripts/fix_story_metadata.py <course> [--write]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)
sys.path.insert(0, str(ROOT / "scripts"))
import course_variants as cv  # noqa: E402


def load(p):
    text = p.read_text(encoding="utf-8")
    m = re.search(r'\n( +)"', text)
    return json.loads(text), (len(m.group(1)) if m else 2), text.endswith("\n")


def dump(p, data, indent, nl):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ("\n" if nl else ""), encoding="utf-8")


def story_hosts(src, course):
    """{story ref: (level, vocabulary ref of the lesson that shows it)}."""
    out = {}
    for level in cc.LEVELS:
        for u in cc.units_of(src, course, level):
            for stem in u.get("stems", []):
                secs = (src.read(f"content/{course}/lessons/{level}/{stem}.json") or {}).get("sections", [])
                voc = next((s.get("ref") for s in secs if s.get("type") == "vocabulary"), None)
                for s in secs:
                    if s.get("type") == "story" and s.get("ref"):
                        out.setdefault(s["ref"], (level, voc))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    course, write = args[0], "--write" in sys.argv
    lang = course.split("-")[0]
    src = cc.Source()
    genders = cc.CHARACTER_GENDER.get(lang, {})
    L = cc.LANG.get(lang, {})
    sets = cc.story_question_sets(src, course)
    copied = {q for q, refs in sets.items() if len(refs) > 1}
    hosts = story_hosts(src, course)
    changed, refused = [], []
    for p in sorted((ROOT / "content" / course / "stories").rglob("*.json")):
        if p.name == "manifest.json":
            continue
        rel = p.relative_to(ROOT / "content" / course).as_posix()
        try:
            data, indent, nl = load(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        notes = []
        nar = data.get("narration") if isinstance(data.get("narration"), dict) else {}
        for name, spk in (nar.get("speakers") or {}).items():
            want = genders.get(name)
            if want and isinstance(spk, dict) and spk.get("gender") not in (None, want):
                notes.append(f"voice {name} {spk.get('gender')} -> {want}")
                spk["gender"] = want
        ped = nar.get("pedagogical") if isinstance(nar.get("pedagogical"), dict) else None
        if ped:
            qs = ped.get("comprehensionQuestions") or []
            key = tuple(cc.fold(q.get("question", "")).strip() for q in qs)
            if qs and key in copied:
                twin = ROOT / "content" / "es-es" / rel
                tq = None
                if course == "es-latam" and twin.is_file():
                    tq = ((json.loads(twin.read_text(encoding="utf-8")).get("narration") or {})
                          .get("pedagogical") or {}).get("comprehensionQuestions")
                    tkey = tuple(cc.fold(q.get("question", "")).strip() for q in tq or [])
                    if not tq or tkey in copied:
                        tq = None
                if tq:
                    ped["comprehensionQuestions"] = json.loads(cv.to_course(json.dumps(tq, ensure_ascii=False), "es-latam"))
                    notes.append("questions copied from es-es")
                else:
                    refused.append(f"{rel}: questions shared with other stories" + (", no es-es twin to copy from" if course == "es-latam" else "") + " (write them; the set's source story keeps its own)")
            host = hosts.get(rel)
            kv = ped.get("keyVocabulary")
            if host and host[0] in ("a1", "a2") and isinstance(kv, list):
                body = " ".join(x.get("text", "") for x in data.get("paragraphs", []) if x.get("lang") != "en")
                hay = set(re.findall(r"\w+", cc.fold(body)))

                def present(lemma):
                    sw = cc.stem_words(re.sub(r"(ar|er|ir)se$", r"\1", lemma), L.get("articles", ()))
                    return bool(sw) and any(any(h.startswith(x) for h in hay) for x in sw)
                if any(not present(k.get("lemma", "")) for k in kv):
                    voc = (src.read(f"content/{course}/{host[1]}") or {}).get("words", []) if host[1] else []
                    picks = [w for w in voc if present(w.get("lemma", ""))][:3]
                    if len(picks) >= 2:
                        ped["keyVocabulary"] = [{"lemma": w["lemma"], "pos": w.get("pos", ""), "cefr": host[0].upper(),
                                                 "gloss": w.get("translation", "")} for w in picks]
                        notes.append("keyVocabulary from the lesson list: " + ", ".join(w["lemma"] for w in picks))
                    else:
                        refused.append(f"{rel}: keyVocabulary not in the story, and under two lesson-list words in it")
        if notes:
            changed.append(f"{rel}: " + "; ".join(notes))
            if write:
                dump(p, data, indent, nl)
    print(f"{course}: {len(changed)} stor{'y' if len(changed) == 1 else 'ies'} {'fixed' if write else 'to fix'}, {len(refused)} refused")
    for c in changed:
        print("  " + c)
    for r in refused:
        print("  REFUSED " + r)


if __name__ == "__main__":
    main()
