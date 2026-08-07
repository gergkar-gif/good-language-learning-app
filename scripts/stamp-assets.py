#!/usr/bin/env python3
"""Stamp a version onto index.html's local CSS and JS URLs.

The dev server (scripts/dev-server.py) keeps the local loop honest, but a
deployed copy is served by someone else's CDN, and a returning visitor will
happily run last week's engine/*.js against this week's content. A query
string the browser has never seen forces a fresh fetch.

Run before deploying:

    python scripts/stamp-assets.py            # stamp with today's date
    python scripts/stamp-assets.py 2026-08-07 # or an explicit version
"""

import datetime
import re
import sys
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index.html"

# href="styles/x.css" or src="engine/x.js", with or without an existing ?v=
ASSET = re.compile(r'\b(href|src)="((?:styles|engine|imports|scripts)/[^"?]+\.(?:css|js))(?:\?v=[^"]*)?"')


def main():
    version = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()

    html = INDEX.read_text(encoding="utf-8")
    stamped, count = ASSET.subn(lambda m: '%s="%s?v=%s"' % (m.group(1), m.group(2), version), html)

    if stamped == html:
        print("index.html already at v=%s (%d assets)" % (version, count))
        return

    INDEX.write_text(stamped, encoding="utf-8", newline="\n")
    print("Stamped %d assets in index.html with v=%s" % (count, version))


if __name__ == "__main__":
    main()
