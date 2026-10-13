-- Run once via D1's dashboard Console tab (Workers & Pages -> D1 ->
-- your database -> Console), after creating the database. See
-- docs/SERVICES.md for the full walkthrough.

CREATE TABLE magic_links (
    token_hash TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    expires_at INTEGER NOT NULL,
    used INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    state_json TEXT,
    updated_at INTEGER,
    created_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS user_books (
    user_id TEXT NOT NULL,
    book_key TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    updated_at INTEGER NOT NULL,
    PRIMARY KEY (user_id, book_key)
);

