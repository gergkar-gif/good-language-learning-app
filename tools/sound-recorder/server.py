#!/usr/bin/env python3
"""Local server for tools/sound-recorder/index.html.

Serves the recorder page and saves each take the page POSTs to
tools/sound-recorder/recordings/<name>.wav, overwriting a redo. Also serves
review.html: the processed MP3s (content/hu/audio/sounds/) and the review
flags (flags.json). Listens on
127.0.0.1 only — localhost counts as a secure context, which the browser
requires before it will hand a page the microphone.

    python tools/sound-recorder/server.py [port]
"""

import json
import re
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECORDINGS = HERE / 'recordings'
SOUNDS = HERE.parents[1] / 'content' / 'hu' / 'audio' / 'sounds'
FLAGS = HERE / 'flags.json'
NAME_RE = re.compile(r'^[a-z0-9-]+$')


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_GET(self):
        if self.path == '/status':
            names = sorted(p.stem for p in RECORDINGS.glob('*.wav'))
            return self._json({'recorded': names})
        if self.path == '/flags':
            return self._json(json.loads(FLAGS.read_text(encoding='utf-8')) if FLAGS.exists() else {})
        match = re.match(r'^/sounds/([a-z0-9-]+)\.mp3', self.path)
        if match and (SOUNDS / f'{match.group(1)}.mp3').exists():
            data = (SOUNDS / f'{match.group(1)}.mp3').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'audio/mpeg')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return self.wfile.write(data)
        return super().do_GET()

    def do_POST(self):
        if self.path == '/flags':
            length = int(self.headers.get('Content-Length', 0))
            FLAGS.write_text(self.rfile.read(length).decode('utf-8'), encoding='utf-8')
            return self._json({'saved': True})
        match = re.match(r'^/save/([^/?]+)$', self.path)
        if not match or not NAME_RE.match(match.group(1)):
            return self._json({'error': 'bad name'}, 400)
        length = int(self.headers.get('Content-Length', 0))
        RECORDINGS.mkdir(exist_ok=True)
        (RECORDINGS / f'{match.group(1)}.wav').write_bytes(self.rfile.read(length))
        return self._json({'saved': match.group(1)})

    def _json(self, body, status=200):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8132
    server = ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, directory=str(HERE)))
    print(f'Sound recorder on http://127.0.0.1:{port}/')
    server.serve_forever()
