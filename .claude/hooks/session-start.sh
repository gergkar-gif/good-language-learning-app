#!/bin/bash
# Cloud sessions only: turn on the repo's pre-push gate (schema, check-content,
# recommendation tests), which a fresh clone has off, and make sure the
# validator's one Python dependency is there. Local checkouts set this once.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
git config core.hooksPath .githooks

if ! python3 -c "import jsonschema" 2>/dev/null; then
  python3 -m pip install --quiet -r requirements-dev.txt
fi
