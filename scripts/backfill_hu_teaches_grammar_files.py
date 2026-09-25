#!/usr/bin/env python3
"""Backfill Hungarian exercises whose lesson has a grammar file (Phase 3.3).

- Extracts grammar skill slug(s) and titles from content/hu/grammar/<level>/<lesson>*-gr.json
- Assigns reusable vocabulary-theme slugs to `vocabulary`-category exercises
- Updates content/hu/indexes/skill-registry.json and content/hu/indexes/grammar-titles.json
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent

UNIT_VOCAB_THEMES = {
    "b1-07": ("education-school-system-vocab", "Education & the Hungarian School System"),
    "b1-08": ("travel-transit-vocab", "Travel, Transit & Directions"),
    "b1-09": ("health-medical-advice-vocab", "Health, Medical Care & Advice"),
    "b1-10": ("housing-home-vocab", "Housing, Tenancy & the Home"),
    "b1-11": ("city-neighbourhood-vocab", "City Life, Neighbourhoods & Community"),
    "b1-12": ("food-cooking-gastronomy-vocab", "Food Preparation, Recipes & Gastronomy"),
    "b1-13": ("news-media-reporting-vocab", "News, Media & Journalism"),
    "b1-14": ("digital-technology-vocab", "Digital Technology & Telecommunications"),
    "b1-15": ("arts-culture-criticism-vocab", "Arts, Theatre, Film & Cultural Criticism"),
    "b1-16": ("environment-sustainability-vocab", "Environment, Ecology & Sustainability"),
    "b1-17": ("social-roles-identity-vocab", "Social Roles, Professions & Status"),
    "b1-18": ("concession-debate-vocab", "Debate, Concession & Contrasting Views"),
    "b1-19": ("personal-finance-economy-vocab", "Budgeting, Personal Finance & Economy"),
    "b1-20": ("counterfactual-past-vocab", "Past Outcomes, Regrets & Turning Points"),
    "b1-21": ("hearsay-verification-vocab", "Rumours, Hearsay & Verification"),
    "b1-22": ("probability-scenarios-vocab", "Possibility, Probability & Contingencies"),
    "b1-23": ("decision-making-dilemmas-vocab", "Decision-Making, Compromises & Dilemmas"),
    "b1-24": ("mechanisms-processes-vocab", "Technical Mechanisms, Systems & Maintenance"),
    "b1-25": ("social-change-trends-vocab", "Historical Shifts, Trends & Adaptation"),
    "b1-26": ("vocation-work-balance-vocab", "Vocation, Career & Work-Life Balance"),
    "b1-27": ("hospitality-social-relations-vocab", "Gatherings, Hospitality & Interpersonal Trust"),
    "b1-28": ("regulations-compliance-vocab", "Regulations, Rules & Institutional Compliance"),
    "b1-29": ("migration-homesickness-vocab", "Migration, Obstacles & Cultural Identity"),
    "b1-30": ("complex-characteristics-vocab", "Complex Relations, Heritage & Character"),
    "b1-31": ("future-projections-vocab", "Future Visions, Forecasts & Innovation"),
    "b1-32": ("reasoning-substantiation-vocab", "Inference, Logical Reasoning & Evidence"),
    "b1-33": ("reported-discourse-vocab", "Reported Speech & Perspective Shifts"),
    "b1-34": ("nested-opinions-debate-vocab", "Complex Opinions, Public Discourse & Ethics"),
    "b1-35": ("past-conditional-reflection-vocab", "Historical Reflection & Counterfactuals"),
    "b1-36": ("advanced-b1-synthesis-vocab", "Integrated B1 Synthesis & Expression"),
    "b1-alaptorveny": ("fundamental-law-constitution-vocab", "The Fundamental Law & Constitutional Principles"),
    "b1-allampolgarsag": ("hungarian-citizenship-law-vocab", "Hungarian Citizenship, Rights & Civic Duties"),
    "b1-allamszervezet": ("state-institutions-governance-vocab", "State Institutions, Parliament & Governance"),
    "b1-anjouk": ("angevin-era-history-vocab", "The Angevin Kings & Medieval Royal Chronicles"),
    "b1-arpadhaz": ("arpad-dynasty-history-vocab", "The Árpád Dynasty & Medieval Statehood"),
    "b1-demokracia": ("democratic-rule-of-law-vocab", "Constitutional Order, Democracy & Rule of Law"),
    "b1-erdelyaranykora": ("principality-transylvania-vocab", "The Golden Age of Transylvania"),
    "b1-europaiorokseg": ("european-literary-heritage-vocab", "European & Hungarian Literary Heritage"),
    "b1-forradalom": ("revolution-1848-history-vocab", "The 1848–1849 Revolution & War of Independence"),
    "b1-haromresz": ("tripartite-hungary-history-vocab", "Royal Hungary & the Tripartite Era"),
    "b1-honfoglalas": ("magyar-conquest-migration-vocab", "The Magyar Migration & Conquest of the Basin"),
    "b1-horthykorszak": ("interwar-regency-history-vocab", "The Interwar Period & Regency"),
    "b1-istvankiraly": ("saint-stephen-christianity-vocab", "King Saint Stephen & the Christian Kingdom"),
    "b1-kadarkorszak": ("kadar-era-history-vocab", "The Kádár Era & Late 20th-Century Society"),
    "b1-karpatmedence": ("carpathian-basin-peoples-vocab", "Early Peoples of the Carpathian Basin"),
    "b1-kiegyezes": ("austro-hungarian-compromise-vocab", "Passive Resistance & the 1867 Compromise"),
    "b1-magyarsag": ("hungarian-diaspora-heritage-vocab", "Hungarians in the Carpathian Basin & Worldwide"),
    "b1-mariaterezia": ("enlightened-absolutism-reforms-vocab", "Maria Theresa, Reconstruction & 18th-Century Reforms"),
    "b1-masodikvh": ("second-world-war-history-vocab", "Hungary in the Second World War"),
    "b1-matyas": ("king-matthias-renaissance-vocab", "King Matthias Corvinus & Renaissance Hungary"),
    "b1-mohacs": ("battle-of-mohacs-history-vocab", "The Battle of Mohács & Kingdom Crisis"),
    "b1-monarchia": ("dual-monarchy-era-vocab", "The Austro-Hungarian Dual Monarchy"),
    "b1-nemzetiertekek": ("hungarikums-scientific-heritage-vocab", "Hungarikums, Nobel Laureates & Scientific Heritage"),
    "b1-nemzetijelkepek": ("national-symbols-anthem-vocab", "National Symbols, Coat of Arms & Anthems"),
    "b1-nemzetiugy": ("emigration-national-movements-vocab", "Political Emigration & National Movements"),
    "b1-nemzetiunnepek": ("national-holidays-commemoration-vocab", "Hungarian National Holidays & Memorial Days"),
    "b1-onkormanyzat": ("local-government-autonomy-vocab", "Local Municipalities & Civic Self-Government"),
    "b1-orszagma": ("geography-of-hungary-vocab", "Geography, Regions & Demographics of Hungary"),
    "b1-otvenhat": ("revolution-1956-history-vocab", "The 1956 Hungarian Revolution"),
    "b1-rakoczi": ("rakoczi-war-of-independence-vocab", "Rákóczi's War of Independence & Kuruc Era"),
    "b1-rakosikorszak": ("postwar-totalitarianism-vocab", "Post-War Transition & the Rákosi Era"),
    "b1-reformkor": ("hungarian-reform-era-vocab", "The Hungarian Reform Era: Széchenyi & Kossuth"),
    "b1-rendszervaltas": ("democratic-transition-1989-vocab", "The 1989–1990 Democratic Transition"),
    "b1-tatarjaras": ("mongol-invasion-reconstruction-vocab", "The Mongol Invasion & King Béla IV's Reconstruction"),
    "b1-torokkiuzese": ("expulsion-of-ottomans-vocab", "Liberation of Buda & Expulsion of the Ottomans"),
    "b1-trianon": ("treaty-of-trianon-history-vocab", "The Treaty of Trianon & Border Changes"),
    "b1-vilaghaboru": ("first-world-war-history-vocab", "Hungary in the First World War"),
}


def unit_prefix(lesson_stem):
    parts = lesson_stem.split("-")
    if len(parts) >= 3:
        return "-".join(parts[:2])
    return lesson_stem


def extract_lesson_grammar_skills(lvl, lesson_stem):
    gr_dir = ROOT / "content/hu/grammar" / lvl
    gr_files = sorted(gr_dir.glob(f"{lesson_stem}*-gr.json"))
    skills = []
    for gf in gr_files:
        try:
            gd = json.loads(gf.read_text(encoding="utf-8"))
        except Exception:
            continue
        gid = gd.get("id", "")
        gtitle = gd.get("title", "")
        if not gid:
            continue
        slug = gid.split(".")[-1]
        if slug == "synthesis":
            slug = f"{unit_prefix(lesson_stem).replace('b1-', '')}-relative-clause-synthesis"
        skills.append((slug, gtitle))
    return skills


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    reg_path = ROOT / "content/hu/indexes/skill-registry.json"
    gt_path = ROOT / "content/hu/indexes/grammar-titles.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    grammar_titles = json.loads(gt_path.read_text(encoding="utf-8"))

    samples = []
    files_written = 0
    tagged_count = Counter()

    for p in sorted((ROOT / "content/hu/exercises").glob("*/*.json")):
        lvl = p.parent.name
        lesson_stem = p.stem.replace("-ex", "")
        gr_skills = extract_lesson_grammar_skills(lvl, lesson_stem)
        if not gr_skills:
            continue

        data = json.loads(p.read_text(encoding="utf-8"))
        exs = data.get("exercises", [])
        if not any(ex.get("category") != "reading" and not ex.get("teaches") for ex in exs):
            continue

        # Register grammar skills
        gr_slugs = []
        for slug, gtitle in gr_skills:
            gr_slugs.append(slug)
            if slug not in registry["skills"] or not registry["skills"][slug].get("title"):
                registry["skills"][slug] = {"title": gtitle, "kind": "grammar"}
            if gtitle and slug not in grammar_titles:
                grammar_titles[slug] = gtitle

        # Determine vocab skill slug for this lesson's unit
        upref = unit_prefix(lesson_stem)
        voc_slug, voc_title = UNIT_VOCAB_THEMES.get(upref, (f"{upref.replace('b1-', '')}-vocabulary", f"{upref.upper()} Vocabulary"))
        if voc_slug not in registry["skills"]:
            registry["skills"][voc_slug] = {"title": voc_title, "kind": "vocabulary"}

        changed = False
        for ex in exs:
            cat = ex.get("category")
            if cat == "reading":
                continue
            t = ex.get("teaches")
            if isinstance(t, list) and len(t) > 0:
                continue

            if cat == "vocabulary":
                new_t = [voc_slug]
            else:
                new_t = list(gr_slugs)

            ex["teaches"] = new_t
            changed = True
            tagged_count[cat] += 1
            prompt_text = ex.get("question") or ex.get("sentence") or ex.get("english") or str(ex.get("pairs", "")[:2])
            samples.append((lvl, p.name, ex.get("id"), cat, new_t, prompt_text))

        if changed and args.write:
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            files_written += 1

    if args.write:
        registry["skills"] = dict(sorted(registry["skills"].items()))
        with open(reg_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
        grammar_titles = dict(sorted(grammar_titles.items()))
        with open(gt_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(grammar_titles, ensure_ascii=False, indent=2) + "\n")

    print(f"=== Phase 3.3 Grammar-File Backfill Summary: {dict(tagged_count)} (total: {sum(tagged_count.values())}, files: {files_written}) ===")
    rng = random.Random(42)
    picked = rng.sample(samples, min(30, len(samples)))
    print("\n=== 30 Random Tagged Exercises (Phase 3.3) ===")
    for lvl, fname, eid, cat, new_t, txt in picked:
        print(f"  [{lvl}/{fname} :: {eid}] ({cat}) -> teaches={new_t} | {txt[:80]}")


if __name__ == "__main__":
    main()
