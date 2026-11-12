"""Fetch a public-domain text from es.wikisource.org as plain text, for a
batch's `sources/` folder (docs/unit-pipeline-log.md § "Pipeline", ES B1).

    python scripts/fetch_wikisource.py "<page title or URL>" <out.txt>

Wikisource answers plain HTTPS from the cloud container (its API does not):
the page HTML is fetched, the article body is cut out, page-number
templates and tags are removed, and a source line is written first.
Refuses rather than guesses: it writes nothing when the page is missing or
the body cannot be found.
"""
import datetime
import html
import re
import sys
import urllib.parse
import urllib.request


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    title, out = sys.argv[1], sys.argv[2]
    url = title if title.startswith("http") else "https://es.wikisource.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))
    try:
        page = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "parlour-sources/1.0"}), timeout=60).read().decode("utf-8")
    except Exception as e:  # 404 and network errors
        sys.exit(f"{url}: {e}; nothing written")
    m = re.search(r'<div[^>]*class="[^"]*mw-parser-output[^"]*"[^>]*>(.*)<div[^>]*class="printfooter', page, re.S)
    if not m:
        sys.exit(f"{url}: article body not found; nothing written")
    t = m.group(1)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", t, flags=re.S)
    t = re.sub(r"</p>|<br ?/?>|</div>|</h\d>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r'<span>",\{"template".*?\}\]\}\'>', "", t, flags=re.S)  # page-number templates
    t = re.sub(r"\[\[File:.*?'/>", "", t, flags=re.S)
    t = re.sub(r"\n\s*\n+", "\n\n", t).strip()
    if len(t.split()) < 100:
        sys.exit(f"{url}: only {len(t.split())} words; check the title; nothing written")
    head = f"Source: {url} (es.wikisource.org, public domain), fetched {datetime.date.today()}\n\n"
    open(out, "w", encoding="utf-8").write(head + t + "\n")
    print(f"wrote {out}: {len(t.split())} words")


if __name__ == "__main__":
    main()
