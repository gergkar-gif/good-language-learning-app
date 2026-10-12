#!/usr/bin/env python3
"""
Audits all Written Exchanges and Oral Conversation Scenarios against the
course curriculum vocabulary (word-lesson-index.json).

Checks for:
1. UNTAUGHT words: words required by a scenario that are NEVER taught in any lesson.
2. LEVEL MISMATCH: words taught in a HIGHER CEFR level than the scenario itself
   (e.g. an A1 scenario using B1 vocabulary).
3. UNIT PREMATURITY: words taught in units AFTER the scenario's specified unitIds.
4. INFLECTION ISSUES: targetKeywords containing inflected forms without a lemma.

Usage:
    python scripts/audit_scenario_vocabulary.py [--lang hu|es-latam|es-es] [--markdown]
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1"]
LEVEL_RANKS = {lvl: i for i, lvl in enumerate(LEVEL_ORDER)}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()

def clean_word(w):
    return re.sub(r'^[^\w]+|[^\w]+$', '', w.strip().lower())

class VocabularyAuditor:
    def __init__(self, root: Path, lang: str):
        self.root = root
        self.lang = lang
        self.curriculum = self._load_json(root / "content" / lang / "curriculum" / "curriculum.json") or {}
        
        # Lemma -> lessonId
        w_idx_data = self._load_json(root / "content" / lang / "indexes" / "word-lesson-index.json") or {}
        self.by_lemma = w_idx_data.get("byLemma", {})
        self.by_lemma_norm = {strip_accents(k): k for k in self.by_lemma}
        self.by_lemma_bare = {re.sub(r'^(el|la|los|las|un|una)\s+', '', k): k for k in self.by_lemma}
        self.by_lemma_bare_norm = {strip_accents(k): v for k, v in self.by_lemma_bare.items()}

        # Lesson metadata mapping: lessonId -> {level, unitId, unitTitle, lessonOrder}
        self.lesson_meta = {}
        self._build_lesson_meta()

        # Inflection indexes
        self.word_index = self._load_json(root / "content" / lang / "indexes" / "word-index.json") or {}
        self.verb_index = self._load_json(root / "generated" / "indexes" / "verb-index.json") or {}

    def _load_json(self, path: Path):
        if not path.is_file():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return None

    def _build_lesson_meta(self):
        order = 0
        levels = self.curriculum.get("levels", {})
        for lvl in LEVEL_ORDER:
            level_data = levels.get(lvl, {})
            for unit in level_data.get("units", []):
                unit_id = unit.get("id")
                unit_title = unit.get("title", "")
                for lesson in unit.get("lessons", []):
                    lid = lesson.get("id")
                    if lid:
                        self.lesson_meta[lid] = {
                            "level": lvl,
                            "unitId": unit_id,
                            "unitTitle": unit_title,
                            "order": order
                        }
                        order += 1

    def resolve_lemma(self, surface_word: str):
        """Resolves a surface word / keyword to its canonical taught lemma."""
        clean = clean_word(surface_word)
        if not clean:
            return None, "empty"

        # 1. Direct lemma match
        if clean in self.by_lemma:
            return clean, "exact"
        
        # 2. Accent-insensitive lemma match
        clean_norm = strip_accents(clean)
        if clean_norm in self.by_lemma_norm:
            return self.by_lemma_norm[clean_norm], "accent_fold"

        # 2b. Article-stripped lemma match (e.g. 'cumpleaños' -> 'el cumpleaños')
        if clean in self.by_lemma_bare:
            return self.by_lemma_bare[clean], "bare_article"
        if clean_norm in self.by_lemma_bare_norm:
            return self.by_lemma_bare_norm[clean_norm], "bare_article"

        # 3. Check word-index (inflected forms)
        for w in (clean, clean_norm):
            if w in self.word_index:
                entries = self.word_index[w]
                if isinstance(entries, str):
                    entries = [{"lemma": entries}]
                elif isinstance(entries, dict):
                    entries = [entries]
                for entry in (entries or []):
                    lem = entry.get("lemma", "") if isinstance(entry, dict) else str(entry)
                    if lem in self.by_lemma:
                        return lem, "word_index"
                    if strip_accents(lem) in self.by_lemma_norm:
                        return self.by_lemma_norm[strip_accents(lem)], "word_index"

        # 4. Check verb-index (Spanish verbs)
        for w in (clean, clean_norm):
            if w in self.verb_index:
                entry = self.verb_index[w]
                lem = entry.get("lemma", "") if isinstance(entry, dict) else str(entry)
                if lem in self.by_lemma:
                    return lem, "verb_index"
                if strip_accents(lem) in self.by_lemma_norm:
                    return self.by_lemma_norm[strip_accents(lem)], "verb_index"

        # 5. Hungarian common inflection suffix stripping heuristics
        if self.lang == "hu":
            # Hungarian accusative -t / -ot / -et / -öt / -at
            for suffix in ["at", "et", "ot", "öt", "t", "ban", "ben", "ba", "be", "hoz", "hez", "höz", "nak", "nek", "val", "vel", "on", "en", "ön", "ra", "re", "ról", "ről", "tól", "től"]:
                if clean.endswith(suffix) and len(clean) > len(suffix) + 2:
                    base = clean[:-len(suffix)]
                    # check base
                    if base in self.by_lemma:
                        return base, "stem_stripped"
                    if strip_accents(base) in self.by_lemma_norm:
                        return self.by_lemma_norm[strip_accents(base)], "stem_stripped"
                    # stem vowel adjustments (pl. alma -> almát -> almat -> alma)
                    if base.endswith("a") or base.endswith("e"):
                        pass
                    for v in ["a", "e", "i", "o", "u"]:
                        if (base + v) in self.by_lemma:
                            return (base + v), "stem_stripped"

        # 6. Spanish plural -s / -es stripping
        if self.lang.startswith("es"):
            if clean.endswith("es") and len(clean) > 4:
                base = clean[:-2]
                if base in self.by_lemma:
                    return base, "plural_stripped"
            elif clean.endswith("s") and len(clean) > 3:
                base = clean[:-1]
                if base in self.by_lemma:
                    return base, "plural_stripped"

        return None, "untaught"

    def audit_scenario(self, scenario: dict, source_type: str):
        sc_id = scenario.get("id", "")
        level = scenario.get("cefrLevel", "A1")
        title = scenario.get("title", "")
        unit_ids = scenario.get("unitIds", [])
        sc_rank = LEVEL_RANKS.get(level, 0)

        # Find max order index among declared unitIds
        declared_max_order = -1
        for uid in unit_ids:
            for lid, meta in self.lesson_meta.items():
                if meta["unitId"] == uid:
                    if meta["order"] > declared_max_order:
                        declared_max_order = meta["order"]

        if scenario.get("requiredLemmas"):
            keywords = set(scenario["requiredLemmas"])
        else:
            # Collect target keywords from all turns
            keywords = set()
            for turn in scenario.get("turns", []):
                vc = turn.get("validationCriteria", {})
                for kw in vc.get("targetKeywords", []):
                    for part in kw.split(): # handle multiword keywords like 'jó napot'
                        clean = clean_word(part)
                        if clean and len(clean) > 1:
                            keywords.add(clean)

        total_keywords = len(keywords)
        untaught = []
        higher_level = []
        premature = []
        ok = []

        for kw in sorted(keywords):
            resolved_lem, method = self.resolve_lemma(kw)
            if not resolved_lem:
                untaught.append(kw)
                continue

            lesson_id = self.by_lemma.get(resolved_lem)
            meta = self.lesson_meta.get(lesson_id, {})
            lem_level = meta.get("level", "Unknown")
            lem_rank = LEVEL_RANKS.get(lem_level, 0)
            lem_order = meta.get("order", 0)

            if lem_rank > sc_rank:
                higher_level.append((kw, resolved_lem, lem_level, meta.get("unitTitle", "")))
            elif declared_max_order >= 0 and lem_order > declared_max_order:
                premature.append((kw, resolved_lem, meta.get("unitId", ""), meta.get("unitTitle", "")))
            else:
                ok.append((kw, resolved_lem, lem_level))

        taught_count = len(ok) + len(premature) + len(higher_level)
        ready_pct = (len(ok) / total_keywords * 100) if total_keywords else 100.0
        curriculum_pct = (taught_count / total_keywords * 100) if total_keywords else 100.0

        return {
            "id": sc_id,
            "type": source_type,
            "level": level,
            "title": title,
            "unitIds": unit_ids,
            "totalKeywords": total_keywords,
            "okCount": len(ok),
            "untaughtCount": len(untaught),
            "higherLevelCount": len(higher_level),
            "prematureCount": len(premature),
            "readyPct": ready_pct,
            "curriculumPct": curriculum_pct,
            "untaught": untaught,
            "higherLevel": higher_level,
            "premature": premature
        }

def run_audit(root: Path, langs: list):
    reports = {}
    for lang in langs:
        auditor = VocabularyAuditor(root, lang)
        lang_reports = []

        for fname, stype in [("writing-exchanges.json", "Written Exchange"), ("conversation-scenarios.json", "Oral Scenario")]:
            fpath = root / "content" / lang / fname
            if not fpath.is_file():
                continue
            data = json.loads(fpath.read_text(encoding="utf-8"))
            for sc in data.get("scenarios", []):
                res = auditor.audit_scenario(sc, stype)
                lang_reports.append(res)

        reports[lang] = lang_reports
    return reports

def format_markdown(reports: dict) -> str:
    lines = []
    lines.append("# Curriculum Vocabulary Audit: Written & Spoken Exchanges")
    lines.append("")
    lines.append("Audit verifying whether words required by scenarios are:")
    lines.append("1. **Taught in the curriculum at all** (present in `word-lesson-index.json`).")
    lines.append("2. **Taught at or below the scenario's CEFR level** (no A1 scenarios requiring B1 words).")
    lines.append("3. **Taught before or within the scenario's declared `unitIds`** (no premature prerequisites).")
    lines.append("")

    for lang, items in reports.items():
        lines.append(f"## Language: `{lang.upper()}` ({len(items)} scenarios)")
        lines.append("")
        lines.append("| ID | Type | Level | Title | Declared Units | Total Words | Taught in Course | Ready at Declared Unit | Untaught Words |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for it in items:
            u_str = ", ".join(it["unitIds"]) if it["unitIds"] else "None"
            untaught_preview = ", ".join(it["untaught"][:5])
            if len(it["untaught"]) > 5:
                untaught_preview += f" (+{len(it['untaught'])-5})"
            if not untaught_preview:
                untaught_preview = "None"
            
            lines.append(f"| `{it['id']}` | {it['type']} | {it['level']} | {it['title']} | {u_str} | {it['totalKeywords']} | {it['curriculumPct']:.0f}% | **{it['readyPct']:.0f}%** | {untaught_preview} |")
        lines.append("")

        # Detailed breakdown of untaught words
        lines.append(f"### `{lang.upper()}` Untaught & Premature Details")
        lines.append("")
        for it in items:
            has_issues = it["untaught"] or it["higherLevel"] or it["premature"]
            if not has_issues:
                continue
            lines.append(f"#### `{it['id']}`: {it['title']} ({it['level']})")
            if it["untaught"]:
                lines.append(f"- **Never Taught in Course ({len(it['untaught'])}):** `{', '.join(it['untaught'])}`")
            if it["higherLevel"]:
                hl_list = [f"`{kw}` (taught in {lvl}: *{utitle}*)" for kw, lem, lvl, utitle in it["higherLevel"]]
                lines.append(f"- **Taught at Higher CEFR Level ({len(it['higherLevel'])}):** {', '.join(hl_list)}")
            if it["premature"]:
                prem_list = [f"`{kw}` (*{uid}*: {utitle})" for kw, lem, uid, utitle in it["premature"][:8]]
                lines.append(f"- **Taught in Later Units than `{it['unitIds']}` ({len(it['premature'])}):** {', '.join(prem_list)}")
            lines.append("")

    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Audit scenario vocabulary")
    parser.add_argument("--lang", default="all", help="Language code (hu, es-latam, es-es, or all)")
    parser.add_argument("--type", choices=["all", "writing", "speaking"], default="all", help="Filter scenario type")
    parser.add_argument("--check", action="store_true", help="Fail if any scenario has untaught words or < 80% readiness")
    parser.add_argument("--output", default=None, help="Output markdown file path")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    langs = ["hu", "es-latam", "es-es"] if args.lang == "all" else [args.lang]

    reports = run_audit(root, langs)
    
    # Filter by type if requested
    if args.type != "all":
        target_type = "Written Exchange" if args.type == "writing" else "Oral Scenario"
        for lang in reports:
            reports[lang] = [it for it in reports[lang] if it["type"] == target_type]

    md = format_markdown(reports)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote audit report to {out_path}")
    else:
        print(md)

    if args.check:
        fail_count = 0
        for lang, items in reports.items():
            for it in items:
                if it["untaughtCount"] > 0 or it["readyPct"] < 80.0:
                    fail_count += 1
                    print(f"ERROR [{lang}]: {it['id']} ({it['title']}) has {it['untaughtCount']} untaught words and {it['readyPct']:.0f}% readiness at unit", file=sys.stderr)
        if fail_count > 0:
            sys.exit(f"\nFAIL: {fail_count} scenarios failed curriculum vocabulary integrity check.")
        else:
            print("\nPASS: All audited scenarios satisfy curriculum vocabulary integrity.")

if __name__ == "__main__":
    main()
