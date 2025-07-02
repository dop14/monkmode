import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_NAME = os.path.join(BASE_DIR, 'monkmode.db')       

# Add default period to period table, if the table is empty
def add_default_period(cursor):
    cursor.execute("SELECT COUNT(*) FROM periods")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("""
                INSERT INTO periods (name, focus_time, short_break_enabled, short_break_time, long_break_enabled, long_break_time, long_break_after, is_default)
                VALUES (?,?,?,?,?,?,?,?)
            """, ("pomodoro", 25, True, 5, True, 15, 4, True))

# Add default subject to subject table, if the table is empty
def add_default_subject(cursor):
    cursor.execute("SELECT COUNT(*) FROM subjects")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("""
                INSERT INTO subjects (name, is_default)
                VALUES (?,?)
            """, ("study", True))
        
# Get the DEFAULT period name
def get_default_period_name():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM periods WHERE is_default = 1")
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None

# Get the default subject name
def get_default_subject_name():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM subjects WHERE is_default = 1")
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else None

# Get ALL period names
def get_period_names():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM periods")
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()

    return subjects

# Get ALL subject names
def get_subject_names():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM subjects")
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()

    return subjects

# Get period data
def get_period_data(period_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM periods WHERE name = ?", (period_name,))
    row = cursor.fetchone()
    conn.close()

    if row:
        (id, name, focus_time, short_enabled, short_time,
            long_enabled, long_time, long_after, is_default) = row
        
        return {
            "id": id,
            "name": name,
            "focus_time": focus_time,
            "short_break_enabled": bool(short_enabled),
            "short_break_time": short_time,
            "long_break_enabled": bool(long_enabled),
            "long_break_time": long_time,
            "long_break_after": long_after,
            "is_default": bool(is_default)
        }
    else:
        return None

# Calculates the session lenght with the current period setting
def calculate_session_length(user_sessions, period_name):
    period_data = get_period_data(period_name)

    # If no breaks
    if not period_data["long_break_enabled"] and not period_data["short_break_enabled"]:
        total_length = user_sessions * (period_data["focus_time"])
    # If short_breaks only
    elif not period_data["long_break_enabled"] and period_data["short_break_enabled"]:
        total_length = user_sessions * period_data["focus_time"] + (user_sessions-1) * period_data["short_break_time"]
        short_break_occurence = (user_sessions -1)
        long_break_occurence = 0
    # If long_breaks only
    elif period_data["long_break_enabled"] and not period_data["short_break_enabled"]:
        long_break_occurence = (user_sessions - 1) // period_data["long_break_after"]
        short_break_occurence = 0
        total_length = (user_sessions * (period_data["focus_time"])) + (long_break_occurence * period_data["long_break_time"])
    # If short_breaks and long_breaks
    else:
        long_break_occurence = (user_sessions - 1) // period_data["long_break_after"]
        short_break_occurence = (user_sessions -1) - long_break_occurence
        total_length = (user_sessions * period_data["focus_time"]) + (short_break_occurence * period_data["short_break_time"]) + (long_break_occurence * period_data["long_break_time"])

    # Convert it to hours and minutes if needed
    if total_length < 60:
        return [total_length, short_break_occurence, long_break_occurence]
    else:
        hours = total_length // 60
        minutes = total_length % 60
        return [hours, minutes, short_break_occurence, long_break_occurence]

# Save new period settings
def save_period_settings(data: dict):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO periods (
            name,
            focus_time,
            short_break_enabled,
            short_break_time,
            long_break_enabled,
            long_break_time,
            long_break_after
        ) VALUES (
            :name,
            :focus_time,
            :short_break_enabled,
            :short_break_time,
            :long_break_enabled,
            :long_break_time,
            :long_break_after
        )
    """

    cursor.execute(query, data)
    conn.commit()
    conn.close()

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
     