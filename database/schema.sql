CREATE TABLE IF NOT EXISTS periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    focus_time INTEGER NOT NULL,
    short_break_enabled BOOLEAN NOT NULL,
    short_break_time INTEGER,
    long_break_enabled BOOLEAN NOT NULL,
    long_break_time INTEGER,
    long_break_after INTEGER,
    is_default BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    is_default BOOLEAN NOT NULL DEFAULT 0,
    is_archived BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS focus_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    period_id INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(subject_id) REFERENCES subjects(id),
    FOREIGN KEY(period_id) REFERENCES periods(id)
);

CREATE TABLE IF NOT EXISTS user_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    default_daily_focus_goal INTEGER NOT NULL DEFAULT 1,
    all_notifications_off BOOLEAN NOT NULL DEFAULT 0,
    theme TEXT CHECK(theme IN ('light', 'dark')) NOT NULL DEFAULT 'dark',
    tips_and_quotes BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    author TEXT,
    date DATE UNIQUE
);

CREATE TABLE IF NOT EXISTS user_stats (
    total_focus_time_mins INTEGER DEFAULT 0,
    focus_sessions_completed INTEGER DEFAULT 0,
    longest_focus_session INTEGER DEFAULT 0,
    longest_streak INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS streak_log (
    date DATE PRIMARY KEY,
    goal_achieved BOOLEAN, 
    is_weekend BOOLEAN NOT NULL DEFAULT 0
);


