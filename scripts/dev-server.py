#!/usr/bin/env python3
"""Static dev server that never lets the browser cache a file.

`python -m http.server` sends Last-Modified and answers conditional requests
with 304, so an edited engine/*.js keeps being served from the browser cache
long after it changed. That produces the worst kind of bug hunt: you are
debugging code that is no longer running.

This sends no-store on every response and refuses to answer 304, so a reload
always fetches the current bytes.

    python scripts/dev-server.py [port]
    python scripts/dev-server.py [port] --lan   # reachable from your phone

Without --lan it listens on 127.0.0.1 only, which is right for everyday work
and means nothing else on the network can reach it. Pass --lan to bind every
interface so a phone or tablet on the same wifi can open the app — useful for
tools/voice-check.html, since which voices exist is a property of the device
and cannot be answered from a desktop. Anyone on that network can then read
the files, so use it on a network you trust and stop the server afterwards.
"""

import os
import socket
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


def lan_address():
    """This machine's address on the local network. Nothing is sent: connect()
    on a UDP socket just asks the routing table which interface would be used."""
    try:
        probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        probe.connect(("192.0.2.1", 1))       # TEST-NET-1, guaranteed unroutable
        address = probe.getsockname()[0]
        probe.close()
        return address
    except OSError:
        return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lan = "--lan" in sys.argv[1:]

    # Argument first, then $PORT, then the default. The environment variable is
    # how a tool that assigns its own port asks for one; two of these servers
    # running at once should not fight over 8131.
    port = int(args[0]) if args else int(os.environ.get("PORT") or DEFAULT_PORT)
    handler = partial(NoCacheHandler, directory=str(PROJECT_ROOT))
    host = "0.0.0.0" if lan else "127.0.0.1"

    with ThreadingHTTPServer((host, port), handler) as httpd:
        print("Serving %s at http://localhost:%d (caching disabled)" % (PROJECT_ROOT, port))
        if lan:
            address = lan_address()
            print("On this network: http://%s:%d" % (address or "<this-machine-ip>", port))
            print("  phone voice check: http://%s:%d/tools/voice-check.html"
                  % (address or "<this-machine-ip>", port))
            print("  Reachable by anything on the wifi. Stop it when you are done.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
