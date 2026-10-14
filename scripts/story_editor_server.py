#!/usr/bin/env python3
"""
story_editor_server.py — Local interactive editor server for Hungarian A1 stories.

Serves the streamlined Script Editor on http://localhost:8080, parses natural
screenplay text & questions, validates schemas, updates manifests, and automatically
commits & pushes changes to GitHub.

Usage:
    python scripts/story_editor_server.py
"""

import http.server
import json
import os
import re
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


def parse_script_to_story(script_text: str, orig_story: dict, new_title: str = None) -> dict:
    parts = re.split(r'\n\s*===+\s*QUESTIONS\s*===+\s*\n?', script_text, flags=re.IGNORECASE)
    story_part = parts[0]
    questions_part = parts[1] if len(parts) > 1 else ""

    new_paragraphs = []
    characters = set()

    for raw in story_part.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            new_paragraphs.append({
                "type": "narration",
                "lang": "en",
                "text": line[1:-1].strip()
            })
        elif ":" in line:
            colon_idx = line.index(":")
            spk = line[:colon_idx].replace("**", "").strip()
            txt = line[colon_idx + 1:].strip()
            if spk:
                characters.add(spk)
            new_paragraphs.append({
                "type": "dialogue",
                "speaker": spk or "Narrator",
                "text": txt
            })
        else:
            new_paragraphs.append({
                "type": "narration",
                "lang": "en",
                "text": line
            })

    # Parse questions if provided
    parsed_questions = []
    if questions_part.strip():
        q_blocks = re.split(r'\n(?=\s*\d+\.\s+)', "\n" + questions_part)
        for block in q_blocks:
            b_lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
            if not b_lines:
                continue
            first = b_lines[0]
            m = re.match(r'^\d+\.\s*(.+)$', first)
            q_text = m.group(1).strip() if m else first
            options = []
            correct_idx = 0
            explanation = ""
            for l in b_lines[1:]:
                if l.startswith("[x]") or l.startswith("- [x]") or l.startswith("* [x]"):
                    correct_idx = len(options)
                    options.append(re.sub(r'^[*\-]?\s*\[x\]\s*', '', l).strip())
                elif l.startswith("[ ]") or l.startswith("- [ ]") or l.startswith("* [ ]"):
                    options.append(re.sub(r'^[*\-]?\s*\[ \]\s*', '', l).strip())
                elif l.startswith(">"):
                    explanation = l[1:].strip()
                elif l.lower().startswith("explanation:"):
                    explanation = l[12:].strip()

            if q_text and len(options) == 4:
                parsed_questions.append({
                    "question": q_text,
                    "options": options,
                    "correctIndex": correct_idx,
                    "explanation": explanation
                })

    result = json.loads(json.dumps(orig_story))
    if new_title:
        result["title"] = new_title.strip()
    result["paragraphs"] = new_paragraphs
    if characters:
        result["characters"] = sorted(list(characters))

    if parsed_questions:
        if "narration" not in result:
            result["narration"] = {}
        if "pedagogical" not in result["narration"]:
            result["narration"]["pedagogical"] = {}
        result["narration"]["pedagogical"]["comprehensionQuestions"] = parsed_questions

    return result


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

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/save":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                payload = json.loads(post_body.decode("utf-8"))
                unit_key = payload.get("unitKey")
                script_text = payload.get("script")
                new_title = payload.get("title")

                if not unit_key:
                    raise ValueError("Missing unitKey.")

                safe_name = os.path.basename(unit_key)
                if not safe_name.endswith(".json"):
                    safe_name += ".json"
                target_path = STORIES_DIR / safe_name

                if not target_path.exists():
                    raise FileNotFoundError(f"File not found: {target_path}")

                orig_story = json.loads(target_path.read_text(encoding="utf-8"))
                
                # Parse or direct data
                if script_text is not None:
                    story_data = parse_script_to_story(script_text, orig_story, new_title)
                else:
                    story_data = payload.get("data")
                    if not story_data:
                        raise ValueError("No script or story data provided.")

                # Write formatted JSON
                formatted_json = json.dumps(story_data, ensure_ascii=False, indent=2) + "\n"
                target_path.write_text(formatted_json, encoding="utf-8")
                print(f"[Save] Written: {target_path.name}")

                # 1. Regenerate manifest so story is linked to unit
                print("[Manifest] Regenerating stories manifest...")
                subprocess.run([sys.executable, str(REPO_ROOT / "build-manifest.py")], cwd=str(REPO_ROOT), check=True, capture_output=True)

                # 2. Validate content
                print("[Validate] Running validate-content.py --changed...")
                val_proc = subprocess.run(
                    [sys.executable, str(REPO_ROOT / "scripts" / "validate-content.py"), "--changed"],
                    cwd=str(REPO_ROOT), capture_output=True, text=True
                )

                if val_proc.returncode != 0:
                    err_msg = f"Validation failed:\n{val_proc.stdout}\n{val_proc.stderr}"
                    print(err_msg)
                    resp = {"ok": False, "error": err_msg}
                else:
                    # 3. Commit and push to git
                    print("[Git] Staging and committing changes...")
                    rel_story_file = f"content/hu/stories/original/a1/{safe_name}"
                    rel_manifest = "content/hu/stories/manifest.json"

                    subprocess.run(["git", "add", rel_story_file, rel_manifest], cwd=str(REPO_ROOT), check=True)
                    
                    commit_msg = f"content(hu): update story {unit_key}"
                    commit_proc = subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(REPO_ROOT), capture_output=True, text=True)
                    print(f"[Git] {commit_proc.stdout.strip()}")

                    # Push
                    print("[Git] Pushing to origin master...")
                    push_proc = subprocess.run(["git", "push", "origin", "master"], cwd=str(REPO_ROOT), capture_output=True, text=True)
                    if push_proc.returncode == 0:
                        print("[Git] Pushed successfully!")
                        msg = f"Saved {unit_key}, updated manifest, validated, and pushed to GitHub!"
                    else:
                        print(f"[Git Push Error] {push_proc.stderr}")
                        msg = f"Saved and validated locally! (Push note: {push_proc.stderr.strip()})"

                    resp = {"ok": True, "message": msg}

                resp_bytes = json.dumps(resp, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp_bytes)))
                self.end_headers()
                self.wfile.write(resp_bytes)

            except Exception as ex:
                print(f"[Error] {ex}")
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
    print("  [HU] Parlour Hungarian A1 Story Studio (Script Mode)")
    print(f"  Serving at: {url}")
    print("  Save & Push directly commits and pushes to GitHub.")
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
