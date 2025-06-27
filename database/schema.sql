CREATE TABLE IF NOT EXISTS periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    focus_time INTEGER NOT NULL,
    short_break_enabled BOOLEAN NOT NULL,
    short_break_time INTEGER,
    long_break_enabled BOOLEAN NOT NULL,
    long_break_time INTEGER,
    long_break_after INTEGER,
    default BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    default BOOLEAN NOT NULL
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