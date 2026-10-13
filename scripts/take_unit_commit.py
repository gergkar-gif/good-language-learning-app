"""Take a unit agent's commit into the current branch (ROADMAP 153).

Cherry-picks <commit>, resolves the two conflicts parallel units always
cause (challenges.json via merge_challenges.py, the generated
word-lesson-index.json by rebuilding it), then runs check-content on the
unit and validate-content --changed. Stops on any other conflict.

    python scripts/take_unit_commit.py <course> <level> <unit id> <commit>
"""
import subprocess
import sys


def run(*cmd, check=True, quiet=False):
    out = subprocess.run(cmd, capture_output=True, text=True)
    if not quiet and out.stdout.strip():
        print(out.stdout.strip().splitlines()[-1])
    if check and out.returncode:
        sys.exit(out.stderr.strip() or out.stdout.strip() or f"failed: {' '.join(cmd)}")
    return out


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    course, level, unit, commit = sys.argv[1:]
    run("git", "cherry-pick", commit, check=False, quiet=True)
    conflicts = run("git", "diff", "--name-only", "--diff-filter=U", quiet=True).stdout.split()
    for path in conflicts:
        if path.endswith("curriculum/challenges.json"):
            run("python", "scripts/merge_challenges.py", course, commit)
        elif path.endswith("indexes/word-lesson-index.json"):
            run("python", "scripts/build_word_lesson_index.py", course, quiet=True)
            # it rewrites every course's index; keep only this course's
            others = [p for p in run("git", "diff", "--name-only", quiet=True).stdout.split()
                      if p.endswith("indexes/word-lesson-index.json") and f"content/{course}/" not in p]
            if others:
                run("git", "checkout", "--", *others, quiet=True)
            run("git", "add", path, quiet=True)
        else:
            sys.exit(f"unexpected conflict in {path}; resolve by hand, then git cherry-pick --continue")
    if conflicts:
        subprocess.run(["git", "-c", "core.editor=true", "cherry-pick", "--continue"], capture_output=True)
    print(run("git", "log", "--oneline", "-1", quiet=True).stdout.strip())
    run("python", "scripts/check-content.py", course, level, unit, check=False)
    run("python", "scripts/validate-content.py", "--changed", check=False)


if __name__ == "__main__":
    main()
