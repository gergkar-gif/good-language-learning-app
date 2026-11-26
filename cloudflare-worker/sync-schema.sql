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

CREATE TABLE IF NOT EXISTS user_profiles (
    user_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    friend_code TEXT UNIQUE NOT NULL,
    social_opt_in INTEGER NOT NULL DEFAULT 0,
    public_board_opt_in INTEGER NOT NULL DEFAULT 0,
    active_course TEXT NOT NULL DEFAULT 'es-latam',
    updated_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS user_weekly_stats (
    user_id TEXT NOT NULL,
    week_key TEXT NOT NULL,
    capped_xp INTEGER NOT NULL DEFAULT 0,
    active_days_json TEXT NOT NULL DEFAULT '[]',
    daily_xp_json TEXT NOT NULL DEFAULT '{}',
    lessons_done INTEGER NOT NULL DEFAULT 0,
    stories_done INTEGER NOT NULL DEFAULT 0,
    rank INTEGER NOT NULL DEFAULT 1,
    streak_days INTEGER NOT NULL DEFAULT 0,
    updated_at INTEGER NOT NULL,
    PRIMARY KEY (user_id, week_key)
);

CREATE INDEX IF NOT EXISTS idx_weekly_board
    ON user_weekly_stats (week_key, capped_xp DESC);

CREATE TABLE IF NOT EXISTS friendships (
    user_a TEXT NOT NULL,
    user_b TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at INTEGER NOT NULL,
    updated_at INTEGER NOT NULL,
    PRIMARY KEY (user_a, user_b)
);

CREATE TABLE IF NOT EXISTS friend_quests (
    id TEXT PRIMARY KEY,
    week_key TEXT NOT NULL,
    user_a TEXT NOT NULL,
    user_b TEXT NOT NULL,
    quest_type TEXT NOT NULL,
    target INTEGER NOT NULL,
    progress_a INTEGER NOT NULL DEFAULT 0,
    progress_b INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'pending',
    cheer_a_at INTEGER,
    cheer_b_at INTEGER,
    completed_at INTEGER,
    created_at INTEGER NOT NULL
);
