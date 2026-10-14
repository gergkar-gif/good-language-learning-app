#!/usr/bin/env python3
"""
story_editor_server.py — Local interactive editor server for Hungarian A1 stories.

Runs a lightweight local web server that serves the Hungarian A1 Story Studio,
allows visual & screenplay editing of all 33 unit stories, and saves changes
directly to disk while automatically running Parlour's schema validator.

Usage:
    python scripts/story_editor_server.py
"""

import http.server
import json
import os
import subprocess
import sys
import webbrowser
from pathlib import Path

PORT = 8080
REPO_ROOT = Path(__file__).resolve().parent.parent
STORIES_DIR = REPO_ROOT / "content" / "hu" / "stories" / "original" / "a1"
LOCAL_HTML = REPO_ROOT / "scripts" / "hungarian_story_editor.html"
ARTIFACT_HTML = Path(r"C:\Users\Admin\.gemini\antigravity\brain\95c4b1e2-9e4a-4db4-bf56-3335afd281a3\hungarian_story_editor.html")
HTML_FILE = LOCAL_HTML if LOCAL_HTML.exists() else ARTIFACT_HTML


class StoryEditorHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            if not HTML_FILE.exists():
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Editor HTML artifact not found.")
                return

            content = HTML_FILE.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        elif self.path == "/api/stories":
            stories = {}
            for p in sorted(STORIES_DIR.glob("a1-unit-*.json")):
                stem = p.stem
                try:
                    stories[stem] = json.loads(p.read_text(encoding="utf-8"))
                except Exception as e:
                    print(f"Error reading {p}: {e}")

            resp_data = json.dumps(stories, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(resp_data)))
            self.end_headers()
            self.wfile.write(resp_data)
            return

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/save":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                payload = json.loads(post_body.decode("utf-8"))
                unit_key = payload.get("unitKey")
                story_data = payload.get("data")

                if not unit_key or not story_data:
                    raise ValueError("Missing unitKey or data payload.")

                # Target file path
                safe_name = os.path.basename(unit_key)
                if not safe_name.endswith(".json"):
                    safe_name += ".json"
                target_path = STORIES_DIR / safe_name

                # Write formatted JSON
                formatted_json = json.dumps(story_data, ensure_ascii=False, indent=2) + "\n"
                target_path.write_text(formatted_json, encoding="utf-8")

                print(f"Saved {safe_name} to {target_path}")

                # Validate
                val_cmd = [sys.executable, str(REPO_ROOT / "scripts" / "validate-content.py"), "--changed"]
                val_proc = subprocess.run(val_cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)

                if val_proc.returncode != 0:
                    print(f"Validation warning/error: {val_proc.stdout} {val_proc.stderr}")
                    result = {
                        "ok": True,
                        "validated": False,
                        "message": f"Saved {safe_name}, but validator reported issues:\n{val_proc.stdout}"
                    }
                else:
                    result = {
                        "ok": True,
                        "validated": True,
                        "message": f"Saved {safe_name} and validated cleanly against schema!"
                    }

                resp_bytes = json.dumps(result, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp_bytes)))
                self.end_headers()
                self.wfile.write(resp_bytes)

            except Exception as ex:
                err_resp = json.dumps({"ok": False, "error": str(ex)}).encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_resp)))
                self.end_headers()
                self.wfile.write(err_resp)
            return

        self.send_response(404)
        self.end_headers()


def main():
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    os.chdir(str(REPO_ROOT))
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, StoryEditorHandler)
    url = f"http://localhost:{PORT}"
    print("\n=======================================================")
    print("  [HU] Parlour Hungarian A1 Story Studio")
    print(f"  Serving at: {url}")
    print("  All 33 Hungarian A1 stories ready to edit.")
    print("  Press Ctrl+C to stop the server.")
    print("=======================================================\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping story editor server.")
        httpd.server_close()


if __name__ == "__main__":
    main()
