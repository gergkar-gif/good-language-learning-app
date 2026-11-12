"""Resolve a rebase stopped by conflicts in generated files only (the
"Auto-sync generated content" commits on master rewrite the same manifests,
decks, curricula and indexes a content commit rebuilds; their "generated"
timestamps always conflict). Seen three times on 2026-11-12, so scripted.

    python scripts/resolve_generated_conflicts.py

Refuses rather than guesses: if any conflicted path is not a generated file,
it changes nothing and lists it. Otherwise it takes this commit's side,
reruns build-manifest.py so the files match the merged content, stages them
and continues the rebase.
"""
import re
import subprocess
import sys

GENERATED = re.compile(r"(^|/)(stories/manifest\.json|decks/decks\.json|curriculum/curriculum\.json)$|/indexes/")


def git(*args, check=True):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=check)


def main():
    conflicted = [p for p in git("diff", "--name-only", "--diff-filter=U").stdout.split() if p]
    if not conflicted:
        sys.exit("no conflicted files")
    other = [p for p in conflicted if not GENERATED.search(p)]
    if other:
        sys.exit("not generated, resolve by hand (nothing changed):\n  " + "\n  ".join(other))
    for p in conflicted:
        git("checkout", "--theirs", "--", p)   # during a rebase, "theirs" is the commit being replayed
    subprocess.run([sys.executable, "build-manifest.py"], check=True, capture_output=True)
    git("add", "-A", "content")
    r = subprocess.run(["git", "-c", "core.editor=true", "rebase", "--continue"], capture_output=True, text=True)
    print(f"resolved {len(conflicted)} generated file(s); rebase: {(r.stdout or r.stderr).strip().splitlines()[-1:]}")


if __name__ == "__main__":
    main()
