import sqlite3

DB_NAME = "monkmode.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)

    add_default_period(cursor)
    add_default_subject(cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database successfully initialized")


# Add default period to period table if not exists
def add_default_period(cursor):
    cursor.execute("SELECT COUNT(*) FROM periods")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("""
                INSERT INTO periods (name, focus_time, short_break_enabled, short_break_time, long_break_enabled, long_break_time, long_break_after, default)
                VALUES (?,?,?,?,?,?,?)
            """, ("pomodoro", 25, True, 5, True, 15, 4, True))

# Add default subject to subject table if not exists
def add_default_subject(cursor):
    cursor.execute("SELECT COUNT(*) FROM subjects")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("""
                INSERT INTO subjects (name, default)
                VALUES (?,?)
            """, ("study", True))
        

# Gets the currrent period setting from UI
def get_current_period(active_period):
    pass
        
# Calculates the session lenght with the current period setting
def calculate_session_lenght(session_count):
    pass