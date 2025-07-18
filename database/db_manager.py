import sqlite3
import os
from datetime import datetime, timedelta

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

# Add default values to user_preferences, if the table is empty
def add_default_user_preferences(cursor):
    cursor.execute("SELECT COUNT(*) FROM user_preferences")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO user_preferences DEFAULT VALUES")

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

# Get default user_preferences
def get_user_preferences():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_preferences")
    result = cursor.fetchone()
    conn.close()

    if result:
        (id,default_daily_focus_goal, week_mode, all_notifications_off, theme,
            tips_and_quotes) = result
        
        return {
            "id":id,
            "default_daily_focus_goal": default_daily_focus_goal,
            "week_mode": week_mode,
            "all_notifications_off": bool(all_notifications_off),
            "theme": theme,
            "tips_and_quotes": bool(tips_and_quotes)
        }
    else:
        return None

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

# Get subject data
def get_subject_data(subject_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM subjects WHERE name = ?", (subject_name,))
    row = cursor.fetchone()
    conn.close()

    return row

# Get today's focus in seconds
def get_today_focus():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(duration) 
        FROM focus_sessions 
        WHERE date(timestamp) = date('now', 'localtime')
    """)
    total_focus_today = cursor.fetchone()[0] or 0
    conn.close()

    return total_focus_today

# Get this week's focus in seconds
def get_this_week_focus():
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().date()

    start_of_week = today - (timedelta(days=today.weekday()))
    end_of_week = start_of_week  + timedelta(days=6)

    cursor.execute("""
        SELECT SUM(duration) 
        FROM focus_sessions 
        WHERE date(timestamp) BETWEEN ? AND ?
    """, (start_of_week, end_of_week))
    total_focus_week = cursor.fetchone()[0] or 0
    conn.close()

    return total_focus_week

# Calculates the session lenght with the current period setting
def calculate_session_length(user_sessions, period_name):
    period_data = get_period_data(period_name)
    short_break_occurence = 0
    long_break_occurence = 0
    
    # If no breaks
    if not period_data["long_break_enabled"] and not period_data["short_break_enabled"]:
        total_length = user_sessions * (period_data["focus_time"])
    # If short_breaks only
    elif not period_data["long_break_enabled"] and period_data["short_break_enabled"]:
        total_length = user_sessions * period_data["focus_time"] + (user_sessions-1) * period_data["short_break_time"]
        short_break_occurence = (user_sessions -1)
    # If long_breaks only
    elif period_data["long_break_enabled"] and not period_data["short_break_enabled"]:
        long_break_occurence = (user_sessions - 1) // period_data["long_break_after"]
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

# Save new subject settings
def save_subject_settings(subject_name):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO subjects(name) VALUES (?)"
    cursor.execute(query,(subject_name,))

    conn.commit()
    conn.close()

# Update the period setting
def update_period_settings(data: dict, id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE periods SET
            name = :name,
            focus_time = :focus_time,
            short_break_enabled = :short_break_enabled,
            short_break_time = :short_break_time,
            long_break_enabled = :long_break_enabled,
            long_break_time = :long_break_time,
            long_break_after = :long_break_after
        WHERE id = :id
    """

    # Add the id key to the data dict for the WHERE clause
    data_with_id = data.copy()
    data_with_id["id"] = id

    cursor.execute(query, data_with_id)
    conn.commit()
    conn.close()

# Update the subject setting    
def update_subject_settings(id:int, name:str):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE subjects SET
            name = ?
        WHERE id = ?
    """
    cursor.execute(query, (name, id))
    conn.commit()
    conn.close()

# Update user_preferences
def update_user_preferences(data:dict, id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE user_preferences SET
            default_daily_focus_goal =:default_daily_focus_goal,
            week_mode = :week_mode,
            all_notifications_off = :all_notifications_off,
            theme = :theme,
            tips_and_quotes= :tips_and_quotes
        WHERE id = :id
    """

    # Add the id key to the data dict for the WHERE clause
    data_with_id = data.copy()
    data_with_id["id"] = id

    cursor.execute(query, data_with_id)
    conn.commit()
    conn.close()

# Delete period setting
def delete_period_settings(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM periods WHERE id = ?"
    cursor.execute(query,(id,))

    conn.commit()
    conn.close()

# Delete subject setting
def delete_subject_settings(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM subjects WHERE id = ?"
    cursor.execute(query,(id,))

    conn.commit()
    conn.close()

# Change default period
def change_def_period(period_name):
    conn = get_connection()
    cursor = conn.cursor()

    # Change current default period values to 0
    cursor.execute("UPDATE periods SET is_default = 0")

    # Change new default value to 1
    cursor.execute("UPDATE periods SET is_default = 1 WHERE name = ?", (period_name,))

    conn.commit()
    conn.close()

# Change default subject
def change_def_subject(subject_name):
    conn = get_connection()
    cursor = conn.cursor()

    # Change current default period values to 0
    cursor.execute("UPDATE subjects SET is_default = 0")

    # Change new default value to 1
    cursor.execute("UPDATE subjects SET is_default = 1 WHERE name = ?", (subject_name,))

    conn.commit()
    conn.close()

# Save a focus session
def save_focus_session_db(data:dict):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO focus_sessions (
            subject_id,
            period_id,
            duration
        ) VALUES (
            :subject_id,
            :period_id,
            :duration
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
    add_default_user_preferences(cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database successfully initialized")
     