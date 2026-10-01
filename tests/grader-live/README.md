# Live grader tests (need network)

These call a running grader endpoint (`GRADER_ENDPOINT`, else `OMNIROUTE_URL`,
else `http://localhost:20128`) and fail without one. They are kept apart from
`tests/grader/`, whose tests run offline.

    node tests/grader-live/test-spanish.js
    node tests/grader-live/test-hungarian.js
    node tests/grader-live/test-consistency.js
