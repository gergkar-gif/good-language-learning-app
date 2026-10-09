#!/usr/bin/env python3
"""Every mechanical content check in one pass (ROADMAP 149, audit § 5).

    python scripts/check-content.py <course> [level] [unit id]   # report
    python scripts/check-content.py <course> [level] --summary   # counts per check
    python scripts/check-content.py --changed                    # gate (pre-push)

What it checks is listed in CHECKS below; the rules behind them are in
docs/course-generation-brief.md (§ numbers in the descriptions).

Gate policy (audit § 6, decision 3). The existing courses (hu, es-es,
es-latam) were written before these rules, so a report on them never fails.
`--changed` compares the units a change touches with origin/master and fails
only on findings the change introduces: editing an exercise that was already
flagged doesn't block, adding a new problem does. A course not in
LEGACY_COURSES is new and held to everything: every finding fails, and the
lesson-shape checks (brief § 2) run on it too (`--shape` forces them on an
existing course, for testing).

Frozen units (ROADMAP 153). A unit listed in content/<course>/frozen-units.json
(written by scripts/freeze_unit.py) is finished: its accepted findings (checked
by a reader and kept, each with a reason) are not reported again, and
`--changed` blocks any edit to it unless the same change unfreezes it.

Not covered here: schemas, tags and skill rules (validate-content.py), and
everything a reader has to judge (brief § 8.2).
"""
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY_COURSES = {"hu", "es-es", "es-latam"}
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]
CHOICE = ("multiple-choice", "dialogue-complete", "listening-choice")
RENDERED = {"multiple-choice", "matching", "fill-blank", "sentence-builder", "sentence-order",
            "dialogue-complete", "structured-writing", "listening-choice", "dictation", "substitution"}
NEW_COURSE_TYPES = RENDERED - {"substitution"}  # brief § 6.1: it renders, but new lessons don't use it
LENGTH_RATIO = 1.3          # brief § 6.3 rule 4
LENGTH_MIN_DIFF = 4         # characters; keeps "sí"/"no"-sized options out of it

CHECKS = {
    # options (brief § 6.3)
    "choice-index": "`correct` is not a valid option index",
    "duplicate-options": "two options are the same",
    "length-giveaway": f"the correct option is the longest, over {LENGTH_RATIO}x the longest wrong one",
    "slash-giveaway": "only the correct option joins two phrases with ' / '",
    "tell-time-word": "a time word only in wrong options",
    "tell-absolute": "an absolute only in wrong options",
    "tell-opener": "an opener only on the correct option, or on every wrong one but not the correct",
    "tell-punctuation": "the correct option alone differs in final punctuation or first-letter case",
    "option-language": "options mix English and the target language",
    "dont-know-option": "'I don't know' as a wrong reply (it answers anything)",
    # prompts and answers (§ 6.2, § 6.4)
    "blank-count": "a fill-blank without exactly one blank",
    "blank-appended": "the blank comes after a complete sentence",
    "blank-letters-repeated": "the answer repeats letters printed next to the blank",
    "hint-is-answer": "the hint contains the answer",
    "hint-person": "a person-marked answer, but no person in the hint, sentence or English line",
    "answer-in-prompt": "the answer is printed in the prompt",
    "exchange-reference": "the question refers to an exchange that isn't shown",
    "missing-english": "a fill-blank or sentence-builder without `english`",
    "question-answer-type": "the correct option doesn't answer the question word (number, yes/no)",
    # language appendices (§ 9)
    "hu-case-noun": "an -n/-ra/-ról noun with -ban/-ba/-ból",
    "hu-archaic": "an archaic -tatik/-tetik passive",
    "latam-vosotros": "a vosotros form in es-latam",
    # lessons and units (§ 2, § 4, § 6.2, § 7)
    "non-rendering-type": "a lesson uses an exercise type lessons don't render",
    "adjacent-repeat": "two adjacent exercises share a question line",
    "unit-copy": "an exercise copies one from an earlier lesson of the unit",
    "taught-later": "a grammar skill is used before the lesson whose screen teaches it",
    "vocab-unused": "a vocabulary word no exercise of its lesson uses",
    # shape, new courses only (§ 2)
    "shape-groups": "a teaching lesson's exercise groups differ from the brief's shape",
    "shape-types": "a lesson uses fewer than 5 exercise types",
    "shape-stage": "an exercise has no `stage`, or one that isn't its group",
    "shape-goal": "a lesson has not 2-4 goal items",
    "shape-consolidation": "a consolidation differs from the brief's shape",
    "shape-story": "the unit story is outside the level's length band",
}
# Patterns a reader confirms: always printed, never gated. Every other check is an error.
SUSPECTS = {"tell-opener", "tell-punctuation", "option-language", "question-answer-type",
            "answer-in-prompt", "hu-case-noun", "vocab-unused"}

ENGLISH = set(("the an to are was were of and in on at for with my your his her its it i you she we they do does did "
               "not this that have what which who how why will would can could should there their from by or but if "
               "than then them these those our us am been being very only because").split())

LANG = {
    "hu": {
        "time": r"\b(tegnap|holnap|tegnapelőtt|holnapután|tavaly|jövőre)\b",
        "absolute": r"\b(kizárólag|teljesen|soha|sohasem|mindig|mindenki|senki|semmi|semmilyen|egyáltalán|abszolút|örökre)\b",
        "openers": {"sajnos", "mert", "de", "hát", "persze", "természetesen", "talán", "igazából", "szerintem", "ó", "jaj"},
        "yesno": r"^(igen|nem)\s*([,.!]|$)",
        "dont_know": {"nem tudom", "nem értem", "fogalmam sincs"},
        "qwords": {"number": r"^(hány|mennyi)\b", "open": r"^(hány|mennyi|miért|mikor|hol|honnan|hová|hova|ki|kit|kivel|kinek|mi|mit|milyen|melyik|hogyan|hogy)\b"},
        "numbers": r"\d|\b(egy|kettő|két|három|négy|öt|hat|hét|nyolc|kilenc|tíz|tizen|húsz|huszon|harminc|negyven|ötven|hatvan|hetven|nyolcvan|kilencven|száz|ezer|fél|sok|kevés|néhány|pár|semennyi|egyik)",
        "articles": {"a", "az", "egy"},
        "function": set(("az egy és nem van vagyok vagy vagyunk hogy meg ki fel ez azt ami mi én ő nagyon már még csak "
                         "de ha akkor itt ott nincs kell lehet volt lesz igen szeretnék kérek köszönöm jó").split()),
    },
    "es": {
        "time": r"\b(ayer|anteayer|anoche|pasado mañana)\b",
        "absolute": r"\b(nunca|jamás|siempre|totalmente|completamente|exclusivamente|absolutamente|nadie|ninguno|ninguna)\b",
        "openers": {"porque", "pues", "bueno", "claro", "vaya", "lamentablemente", "desgraciadamente", "quizás", "quizá", "oye", "mira"},
        "yesno": r"^(sí|no)\s*([,.!]|$)",
        "dont_know": {"no sé", "no lo sé", "no entiendo", "ni idea"},
        "qwords": {"number": r"^¿?\s*(cuántos|cuántas|cuánto|cuánta)\b", "open": r"^¿?\s*(cuántos|cuántas|cuánto|cuánta|por qué|cuándo|dónde|adónde|de dónde|quién|quiénes|qué|cómo|cuál|cuáles)\b"},
        "numbers": r"\d|\b(un|uno|una|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieci\w*|veint\w*|treinta|cuarenta|cincuenta|sesenta|setenta|ochenta|noventa|cien|ciento|mil|media|medio|muchos|muchas|mucho|pocos|pocas|poco|varios|varias|algunos|algunas|ninguno|ninguna|nada)\b",
        "articles": {"el", "la", "los", "las", "un", "una", "unos", "unas", "lo"},
        "function": set(("el la los las un una unos unas de del al que y en es son está están me te se nos lo le les mi "
                         "mis tu tus su sus por para con muy yo tú él ella ellos ellas hay ser estar soy eres somos tengo "
                         "tiene quiero voy va vamos hace pero también cuando donde como porque este esta estos estas ese "
                         "esa aquí allí ya sí").split()),
    },
}

HU_ON_NOUNS = r"(posta|állomás|pályaudvar|piac|egyetem|repülőtér|repülőtere|munkahely|sziget|strand|Budapest|Magyarország|koncert|előadás|tanfolyam|meccs|kirándulás|konferencia|értekezlet)"
HU_CASE = re.compile(r"\b" + HU_ON_NOUNS + r"(ba|be|ban|ben|ból|ből)\b", re.I)
# Only back-vowel -tatik: front-vowel -tetik is also the ordinary definite 3rd plural of a
# -tet verb (egyeztetik, késztetik), so a -tetik passive needs the read.
HU_ARCHAIC = re.compile(r"\w+tatik\b", re.I)
VOSOTROS = re.compile(r"\b(vosotros|vosotras|vuestro|vuestra|vuestros|vuestras|os)\b|\b\w+(áis|(?<!s)éis)\b", re.I)  # not dieciséis
EXCHANGE = re.compile(r"\b((starts?|begins?|opens?|continues?|follows?|ends?|finishes) (this|the|that) (exchange|conversation|dialogue)|this exchange)\b", re.I)
ES_PERSON = re.compile(r"\b(yo|t[uú]|[eé]l|ella|usted|nosotros|nosotras|vosotros|vosotras|ellos|ellas|ustedes|I|you|he|she|we|they)\b", re.I)
ES_AUX = {"he", "has", "ha", "hemos", "habéis", "han"}
BLANK = re.compile(r"_{2,}")
COPY_KEYS = ("question", "sentence", "options", "pairs", "solution", "prompt", "template", "answer", "answers",
             "correct", "text", "english", "words", "tiles", "sentences", "solutions", "hint")
NOT_TEXT = {"id", "teaches", "type", "category", "stage", "english", "explanation", "hint", "distractor_skills", "audio"}


# --- reading files, from the working tree or a git revision ----------------

class Source:
    def __init__(self, rev=None):
        self.rev, self.cache = rev, {}

    def read(self, rel):
        rel = rel.replace("\\", "/")
        if rel not in self.cache:
            try:
                if self.rev:
                    out = subprocess.run(["git", "show", f"{self.rev}:{rel}"], cwd=ROOT, capture_output=True)
                    self.cache[rel] = json.loads(out.stdout.decode("utf-8")) if out.returncode == 0 else None
                else:
                    p = ROOT / rel
                    self.cache[rel] = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None
            except json.JSONDecodeError:
                self.cache[rel] = None
        return self.cache[rel]


# --- helpers ---------------------------------------------------------------

def words(t):
    return re.findall(r"[^\W\d_]+", (t or "").lower())


def fold(t):
    t = unicodedata.normalize("NFD", (t or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def texts(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for y in x:
            yield from texts(y)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in NOT_TEXT:
                yield from texts(v)


def answer_text(e):
    opts = e.get("options") or []
    k = e.get("correct")
    if isinstance(k, int) and 0 <= k < len(opts) and isinstance(opts[k], str):
        return opts[k]
    a = e.get("answers") or e.get("answer")
    return (a[0] if isinstance(a, list) and a else a) if a else ""


def prompt_text(e):
    if e.get("type") == "dialogue-complete":
        return " ".join(l.get("text", "") for l in e.get("prompt") or [] if "_" not in l.get("text", ""))
    return e.get("sentence") or e.get("question") or ""


def question_line(e):
    """The question a choice item asks, in the target language if it is one."""
    if e.get("type") == "dialogue-complete":
        lines = [l.get("text", "") for l in e.get("prompt") or []]
        for i, t in enumerate(lines):
            if BLANK.search(t) and i:
                return lines[i - 1]
        return lines[-1] if lines else ""
    return e.get("question") or ""


GLOSS = re.compile(r"\s*\[[^\]]*\]")
TARGET_MARKS = {"hu": r"[áéíóöőúüű]", "es": r"[áéíóúñ¿¡]"}


def looks_english(t):
    w = words(GLOSS.sub("", t))
    n = len([x for x in w if x in ENGLISH])
    return n >= 1 and n * 3 >= len(w)


def looks_target(t, lang):
    """Positive evidence the text is in the course language: its accents or function words."""
    s = GLOSS.sub("", t)
    L = LANG.get(lang)
    if not L:
        return False
    if re.search(TARGET_MARKS[lang], s, re.I):
        return True
    return any(w in L["function"] for w in words(s))


def string_options(e):
    o = e.get("options")
    return o if isinstance(o, list) and len(o) > 1 and all(isinstance(x, str) for x in o) else None


# --- exercise checks --------------------------------------------------------

def check_exercise(e, course, lang):
    out = []

    def hit(check, msg=""):
        out.append((check, msg))

    L = LANG.get(lang)
    t = e.get("type")
    opts = string_options(e)
    if t in CHOICE and opts:
        k = e.get("correct")
        if not isinstance(k, int) or not 0 <= k < len(opts):
            hit("choice-index")
        else:
            right, wrong = opts[k], [x for j, x in enumerate(opts) if j != k]
            if len({o.strip() for o in opts}) < len(opts):  # case kept: "el Doce de Mayo" can be the wrong one
                hit("duplicate-options")
            bare = [GLOSS.sub("", x).strip() for x in opts]
            b_right, b_wrong = bare[k], [x for j, x in enumerate(bare) if j != k]
            longest = max(len(x) for x in b_wrong)
            if len(b_right) > LENGTH_RATIO * longest and len(b_right) - longest >= LENGTH_MIN_DIFF:
                hit("length-giveaway", f"{len(b_right)} vs {longest} characters")
            if " / " in right and not any(" / " in x for x in wrong):
                hit("slash-giveaway")
            stem = prompt_text(e) + " " + question_line(e)
            if L:
                for check, pat in (("tell-time-word", L["time"]), ("tell-absolute", L["absolute"])):
                    hits = [m.group(0) for x in wrong for m in [re.search(pat, x, re.I)] if m]
                    # a prompt that sets up the time contrast itself ("¿Qué harás mañana?") is not a tell
                    if hits and not re.search(pat, right, re.I) and not (check == "tell-time-word" and re.search(pat + r"|\b(mañana|holnap)\b", stem, re.I)):
                        hit(check, hits[0])
                first = lambda s: (words(s) or [""])[0]
                why = re.search(r"\b(miért|por qué|why)\b", stem, re.I)
                if len(opts) >= 3 and all(len(words(x)) >= 3 for x in bare) and not why:
                    if first(right) in L["openers"] and not any(first(x) == first(right) for x in wrong):
                        hit("tell-opener", first(right))
                    elif all(first(x) in L["openers"] for x in wrong) and first(right) not in L["openers"]:
                        hit("tell-opener", first(wrong[0]))
                if t == "dialogue-complete" and any(fold(x).strip(" .!?¡¿") in {fold(d) for d in L["dont_know"]} for x in wrong):
                    hit("dont-know-option")
            if len(opts) >= 3:
                # "?" against "." is a question against a statement: meaning, not a tell
                end = lambda s: s[-1:] if s[-1:] in ".!…" else ""
                cap = lambda s: s[:1].isupper()
                if len({end(x) for x in b_wrong}) == 1 and end(b_right) != end(b_wrong[0]) and not any(x.endswith("?") for x in bare):
                    hit("tell-punctuation", "final punctuation")
                elif len({cap(x) for x in b_wrong}) == 1 and cap(b_right) != cap(b_wrong[0]):
                    hit("tell-punctuation", "first-letter case")
            if L:
                eng = [looks_english(x) and not looks_target(x, lang) for x in opts]
                tgt = [looks_target(x, lang) and not looks_english(x) for x in opts]
                if any(eng) and any(tgt):
                    hit("option-language", next(x for x, en in zip(opts, eng) if en)[:40])
            if L and t != "listening-choice":
                q = fold(question_line(e)).strip(" ¿¡\"'«")
                bare_reply = t != "dialogue-complete" or any(BLANK.fullmatch(l.get("text", "").strip()) for l in e.get("prompt") or [])
                if q and bare_reply and not BLANK.search(q) and not looks_english(q):
                    qw = {k2: re.compile(fold(v)) for k2, v in L["qwords"].items()}
                    if qw["open"].search(q) and re.search(fold(L["yesno"]), fold(right).strip(" ¿¡\"'«")):
                        hit("question-answer-type", "yes/no reply to an open question")
                    elif qw["number"].search(q) and not re.search(fold(L["numbers"]), fold(right)):
                        hit("question-answer-type", "no number in the answer to a how-many question")

    if t == "multiple-choice" and EXCHANGE.search(e.get("question") or ""):
        hit("exchange-reference")

    if t == "fill-blank":
        s = e.get("sentence") or ""
        blanks = BLANK.findall(s)
        if len(blanks) != 1:
            hit("blank-count", f"{len(blanks)} blanks")
        elif re.search(r"[.!?][\"”»']?\s+_{2,}\s*[.!?]?\s*$", s):
            hit("blank-appended")
        answers = [a for a in (e.get("answers") or [e.get("answer")]) if isinstance(a, str) and a]
        m_pre, m_suf = re.search(r"(\w+)_{2,}", s), re.search(r"_{2,}(\w+)", s)
        for a in answers:
            if m_pre and fold(a).startswith(fold(m_pre.group(1))):
                hit("blank-letters-repeated", f"{m_pre.group(1)}____ + {a}")
                break
            if m_suf and fold(a).endswith(fold(m_suf.group(1))):
                hit("blank-letters-repeated", f"____{m_suf.group(1)} + {a}")
                break
        h = e.get("hint") if isinstance(e.get("hint"), str) else ""
        if h and any(re.search(r"(?<!\w)" + re.escape(a.lower()) + r"(?!\w)", h.lower()) for a in answers if len(a) > 1):
            hit("hint-is-answer", h)
        ans = answers[0] if answers else ""
        last = (words(ans) or [""])[-1]
        # Hungarian person endings can't be told from noun endings (egyetem, barátok) without a
        # morphology lookup, so only the Spanish haber case is checked (brief § 6.4 "Pin the person").
        if lang == "es" and last in ES_AUX and not ES_PERSON.search(" ".join([h, e.get("english") or "", s])):
            hit("hint-person", ans)

    ans, ptxt = answer_text(e), prompt_text(e)
    aw = words(ans)
    # dialogue-complete is left out: a reply echoing the line before it (Jó reggelt! → Jó reggelt!) is natural
    if len("".join(aw)) >= 4 and t in ("fill-blank", "multiple-choice") and ptxt:
        pw = words(ptxt)
        if any(pw[i:i + len(aw)] == aw for i in range(len(pw) - len(aw) + 1)):
            hit("answer-in-prompt", ans)

    if t in ("fill-blank", "sentence-builder") and not e.get("english"):
        hit("missing-english")

    body = " ".join(texts(e))
    if lang == "hu":
        m = HU_CASE.search(body)
        if m:
            hit("hu-case-noun", m.group(0))
        m = HU_ARCHAIC.search(body)
        if m:
            hit("hu-archaic", m.group(0))
    if course == "es-latam":
        m = VOSOTROS.search(body)
        if m:
            hit("latam-vosotros", m.group(0))
    return out


# --- lesson and unit checks -------------------------------------------------

def stem_words(lemma, articles):
    """Prefixes that stand for a lemma in an inflected text. A "(Madrid)" note is
    dropped, and of "a / b" alternatives the first is taken."""
    lemma = re.sub(r"\([^)]*\)", " ", lemma).split(" / ")[0]
    ws = [w for w in words(fold(lemma)) if w not in {fold(a) for a in articles}]
    return [w[:max(3, len(w) - 2)] if len(w) > 4 else w for w in ws if len(w) >= 2]


def lesson_groups(lesson):
    return [s for s in lesson.get("sections", []) if s.get("type") == "exercise-group"]


SHAPE_TEACH = {"a1": [("Introduce", 2), ("Controlled", 4), ("Practice", 5), ("Dialogue", 2), ("Production", 2), ("Check", 2)]}
SHAPE_TEACH_UP = [("Introduce", 2), ("Controlled", 4), ("Practice", 4), ("Listening", 2), ("Dialogue", 2), ("Production", 2), ("Check", 2)]
SHAPE_CONSOL = [("Recognize", 5), ("Recall", 5), ("In Context", 5), ("Produce", 5)]
STORY_BAND = {"a1": (80, 150), "a2": (120, 200), "b1": (300, 400)}


def check_unit(src, course, level, unit, shape):
    """Findings for one unit: [(check, id, msg, file)]."""
    lang = course.split("-")[0]
    L = LANG.get(lang, {})
    out = []
    skills = (src.read(f"skills/{lang}.json") or {}).get("skills", {})
    order, screen = unit_positions(src, course, level)
    seen = {}
    stems = unit["stems"]
    for stem in stems:
        ex_rel = f"content/{course}/exercises/{level}/{stem}-ex.json"
        data = src.read(ex_rel) or {}
        exs = data.get("exercises", []) if isinstance(data, dict) else []
        by_id = {e.get("id"): e for e in exs}
        consolidation = "consolidation" in stem
        for e in exs:
            eid = e.get("id")
            for check, msg in check_exercise(e, course, lang):
                out.append((check, eid, msg, ex_rel))
            if not consolidation:
                key = json.dumps({k: e.get(k) for k in COPY_KEYS if k in e}, ensure_ascii=False, sort_keys=True)
                key = re.sub(r"\s*\((?:Lesson|Lecke|Lección) ?\d+\)", "", key)
                if key in seen:
                    out.append(("unit-copy", eid, f"copy of {seen[key]}", ex_rel))
                else:
                    seen[key] = eid
            for slug in e.get("teaches") or []:
                sk = skills.get(slug) or {}
                if sk.get("kind") == "grammar" and sk.get("level", "").lower() == level:
                    where = order.get(screen.get(sk.get("taught_in")))
                    if where is not None and stem in order and where > order[stem]:
                        out.append(("taught-later", eid, f"{slug} is taught at {sk['taught_in']}", ex_rel))

        lesson_rel = f"content/{course}/lessons/{level}/{stem}.json"
        lesson = src.read(lesson_rel)
        if not lesson:
            continue
        groups = lesson_groups(lesson)
        refs = [r for g in groups for r in g.get("exerciseRefs") or []]
        prev = None
        for r in refs:
            e = by_id.get(r)
            if not e:
                continue
            if e.get("type") not in RENDERED:
                out.append(("non-rendering-type", r, e.get("type"), lesson_rel))
            q = (e.get("question") or "").strip()
            if q and prev and q == prev:
                out.append(("adjacent-repeat", r, q[:60], lesson_rel))
            prev = q
        vocab_ref = next((s.get("ref") for s in lesson.get("sections", []) if s.get("type") == "vocabulary"), None)
        if vocab_ref:
            voc = src.read(f"content/{course}/{vocab_ref}") or {}
            hay = fold(" ".join(" ".join(texts(e)) for e in exs))
            hay_words = set(re.findall(r"\w+", hay))
            for w in voc.get("words", []) if isinstance(voc, dict) else []:
                sw = stem_words(w.get("lemma", ""), L.get("articles", ()))
                if sw and not all(any(h.startswith(s) for h in hay_words) for s in sw):
                    out.append(("vocab-unused", stem, w.get("lemma"), f"content/{course}/{vocab_ref}"))

        if shape:
            out += check_shape(src, course, level, stem, lesson, lesson_rel, groups, by_id, consolidation)
    return out


def check_shape(src, course, level, stem, lesson, lesson_rel, groups, by_id, consolidation):
    out = []
    goal = lesson.get("goal") or []
    if not 2 <= len(goal) <= 4:
        out.append(("shape-goal", stem, f"{len(goal)} goal items", lesson_rel))
    want = SHAPE_CONSOL if consolidation else SHAPE_TEACH.get(level, SHAPE_TEACH_UP)
    have = [(g.get("title"), len(g.get("exerciseRefs") or [])) for g in groups if g.get("title") != "Reading"]
    if have != want:
        out.append(("shape-consolidation" if consolidation else "shape-groups", stem,
                    "has " + ", ".join(f"{t} {n}" for t, n in have), lesson_rel))
    refs = [r for g in groups for r in g.get("exerciseRefs") or []]
    types = {by_id[r].get("type") for r in refs if r in by_id}
    if len(types) < 5:
        out.append(("shape-types", stem, f"{len(types)} types", lesson_rel))
    for r in refs:
        if r in by_id and by_id[r].get("type") not in NEW_COURSE_TYPES:
            out.append(("shape-types", r, f"{by_id[r].get('type')} is not used in new lessons", lesson_rel))
    if consolidation:
        tags = {s for r in refs if r in by_id for s in by_id[r].get("teaches") or []}
        if len(tags) < 6:
            out.append(("shape-consolidation", stem, f"{len(tags)} different teaches tags (6 needed)", lesson_rel))
    for g in groups:
        stage = (g.get("title") or "").lower()
        for r in g.get("exerciseRefs") or []:
            e = by_id.get(r)
            if e and e.get("stage") != stage and not consolidation:
                out.append(("shape-stage", r, f"stage {e.get('stage')!r}, group {stage!r}", lesson_rel))
    story_ref = next((s.get("ref") for s in lesson.get("sections", []) if s.get("type") == "story"), None)
    if story_ref and level in STORY_BAND:
        story = src.read(f"content/{course}/{story_ref}") or {}
        n = sum(len(words(p.get("text", ""))) for p in story.get("paragraphs", []) if p.get("lang", course) != "en")
        lo, hi = STORY_BAND[level]
        if not lo <= n <= hi:
            out.append(("shape-story", stem, f"{n} words, band {lo}-{hi}", f"content/{course}/{story_ref}"))
    return out


def unit_positions(src, course, level):
    """stem -> position in the unit table; grammar screen id -> first stem that shows it."""
    key = (course, level)
    if key not in src.cache:
        order, screen = {}, {}
        for u in src.read(f"content/{course}/curriculum/units/{level}.json") or []:
            for stem in u.get("stems", []):
                order[stem] = len(order)
                for sec in (src.read(f"content/{course}/lessons/{level}/{stem}.json") or {}).get("sections", []):
                    if sec.get("type") == "grammar" and sec.get("ref"):
                        screen.setdefault(Path(sec["ref"]).stem, stem)
        src.cache[key] = (order, screen)
    return src.cache[key]


# --- driving ----------------------------------------------------------------

def units_of(src, course, level):
    return src.read(f"content/{course}/curriculum/units/{level}.json") or []


def frozen_units(src, course):
    """{"<level>/<unit id>": entry} from content/<course>/frozen-units.json."""
    return (src.read(f"content/{course}/frozen-units.json") or {}).get("units", {})


def run(src, course, levels, unit_id=None, shape=False):
    found = []
    frozen = frozen_units(src, course)
    for level in levels:
        for u in units_of(src, course, level):
            if unit_id and u.get("id") != unit_id:
                continue
            accepted = {(a["check"], a["id"]) for a in frozen.get(f"{level}/{u.get('id')}", {}).get("accepted", [])}
            for check, eid, msg, f in check_unit(src, course, level, u, shape):
                if (check, eid) not in accepted:
                    found.append((course, level, u.get("id"), check, eid, msg, f))
    return found


def changed_units():
    """{(course, level, unit id)} for every content file that differs from origin/master."""
    names = set()
    for args in (["diff", "--name-only", "origin/master"], ["diff", "--name-only", "origin/master...HEAD"],
                 ["ls-files", "--others", "--exclude-standard", "content"]):
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        names |= {n for n in r.stdout.split() if n.startswith("content/")}
    head = Source()
    out = set()
    for n in names:
        parts = n.split("/")
        if len(parts) < 4:
            continue
        course = parts[1]
        if parts[2] in ("curriculum",) and parts[-1].endswith(".json") and parts[3] == "units":
            level = parts[-1][:-5]
            out |= {(course, level, u.get("id")) for u in units_of(head, course, level)}
            continue
        level = parts[3] if len(parts) > 4 else None
        stem = re.sub(r"(-ex|-voc|-gr|-[ab]-gr)?\.json$", "", parts[-1])
        for lv in ([level] if level in LEVELS else LEVELS):
            for u in units_of(head, course, lv):
                if any(stem == s or stem.startswith(s + "-") for s in u.get("stems", [])):
                    out.add((course, lv, u.get("id")))
    return out


def gate():
    head, base = Source(), Source("origin/master")
    new, blocked = [], []
    for course, level, uid in sorted(changed_units()):
        key = f"{level}/{uid}"
        if key in frozen_units(base, course) and key in frozen_units(head, course):
            blocked.append(f"{course} {key}")
        is_new = course not in LEGACY_COURSES
        now = run(head, course, [level], uid, shape=is_new)
        before = set() if is_new else {(c, i) for *_, c, i, _m, _f in run(base, course, [level], uid)}
        new += [x for x in now if (x[3], x[4]) not in before]
    show(new)
    if blocked:
        print("\ncheck-content: these units are frozen (content/<course>/frozen-units.json) and were edited: "
              + ", ".join(blocked) + ". Unfreeze first: `python scripts/freeze_unit.py --unfreeze <course> <level> "
              "<unit> --reason ...`, in the same change. Push blocked.")
        return 1
    errors = [x for x in new if x[3] not in SUSPECTS]
    if errors:
        print(f"\ncheck-content: {len(errors)} new error(s) in the changed units; push blocked. "
              f"The rule behind each check is in docs/course-generation-brief.md.")
        return 1
    print(f"check-content: no new errors in the changed units"
          + (f" ({len(new)} new suspect(s) above: fix them or say why they stay)" if new else ""))
    return 0


def show(found):
    for course, level, uid, check, eid, msg, f in sorted(found, key=lambda x: (x[3] in SUSPECTS, x[6], x[4] or "")):
        print(f"{'suspect' if check in SUSPECTS else 'ERROR':7}  {check:22} {eid}  {msg}  ({f})")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if "--changed" in flags:
        sys.exit(gate())
    if not args:
        sys.exit(__doc__)
    course = args[0]
    levels = [args[1].lower()] if len(args) > 1 else [lv for lv in LEVELS if (ROOT / "content" / course / "curriculum" / "units" / f"{lv}.json").is_file()]
    unit_id = args[2] if len(args) > 2 else None
    is_new = course not in LEGACY_COURSES
    found = run(Source(), course, levels, unit_id, shape=is_new or "--shape" in flags)
    if "--summary" in flags:
        counts = Counter((x[1], x[3]) for x in found)
        lvls = sorted({x[1] for x in found}, key=LEVELS.index)
        print(f"{'check':24}" + "".join(f"{lv:>7}" for lv in lvls) + "   total")
        for check in CHECKS:
            row = [counts[(lv, check)] for lv in lvls]
            if any(row):
                print(f"{check + (' ?' if check in SUSPECTS else ''):24}" + "".join(f"{n:>7}" for n in row) + f"{sum(row):>8}")
        print(f"{'all':24}" + "".join(f"{sum(counts[(lv, c)] for c in CHECKS):>7}" for lv in lvls) + f"{len(found):>8}")
        print("(? = suspect: a pattern a reader confirms, never gated)")
    else:
        show(found)
    errors = [x for x in found if x[3] not in SUSPECTS]
    print(f"{len(errors)} error(s), {len(found) - len(errors)} suspect(s)"
          + ("" if is_new else " (existing course: a report, nothing fails; --changed gates new findings)"))
    sys.exit(1 if is_new and errors else 0)


if __name__ == "__main__":
    main()
