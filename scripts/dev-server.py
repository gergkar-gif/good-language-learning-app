#!/usr/bin/env python3
"""Static dev server that never lets the browser cache a file.

`python -m http.server` sends Last-Modified and answers conditional requests
with 304, so an edited engine/*.js keeps being served from the browser cache
long after it changed. That produces the worst kind of bug hunt: you are
debugging code that is no longer running.

This sends no-store on every response and refuses to answer 304, so a reload
always fetches the current bytes.

    python scripts/dev-server.py [port]
"""

import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DEFAULT_PORT = 8131
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_header(self, keyword, value):
        # Suppress Last-Modified entirely: without it the browser has nothing
        # to build an If-Modified-Since request from, so it cannot ask for a
        # 304 and we cannot accidentally grant one.
        if keyword == "Last-Modified":
            return
        super().send_header(keyword, value)

    def log_message(self, fmt, *args):
        # One line per request, without the noisy timestamp prefix.
        sys.stderr.write("%s\n" % (fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    handler = partial(NoCacheHandler, directory=str(PROJECT_ROOT))

    with ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print("Serving %s at http://localhost:%d (caching disabled)" % (PROJECT_ROOT, port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
