import sqlite3
import os
from datetime import datetime, timedelta, date
import calendar
import requests
from utils import get_resource_path, get_db_path

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

# Add default stats
def add_default_user_stats(cursor):
    cursor.execute("SELECT COUNT(*) FROM user_stats")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO user_stats DEFAULT VALUES")

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
        (id,default_daily_focus_goal, all_notifications_off, theme,
            tips_and_quotes) = result
        
        return {
            "id":id,
            "default_daily_focus_goal": default_daily_focus_goal,
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

# Get ALL not archived subject names
def get_subject_names():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM subjects WHERE is_archived = 0")
    subjects = [row[0] for row in cursor.fetchall()]
    conn.close()

    return subjects

# Get ALL archived subject names
def get_archived_subject_names():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM subjects WHERE is_archived = 1")
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

# Get this month's focus in seconds
def get_this_month_focus():
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().date()

    start_of_month = today.replace(day=1)
    last_day = calendar.monthrange(today.year,today.month)[1]
    end_of_month = today.replace(day=last_day)

    cursor.execute("""
        SELECT SUM(duration) 
        FROM focus_sessions 
        WHERE date(timestamp) BETWEEN ? AND ?
    """, (start_of_month, end_of_month))
    total_focus_month = cursor.fetchone()[0] or 0
    conn.close()

    return total_focus_month

# Get user stats
def get_user_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_stats")
    result = cursor.fetchone()
    conn.close()

    return result

# Get avg focus seconds
def get_avg_focus():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(duration) FROM focus_sessions")
    result = cursor.fetchone()[0]
    conn.close()

    return result

# Count how many times was the daily goal achieved
def get_daily_goal_achieved():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM streak_log WHERE goal_achieved == True")
    result = cursor.fetchone()[0]
    conn.close()

    return result

# Calculate current streak
def get_current_streak():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today()
    yesterday = today - timedelta(days=1)

    # Get all dates from today
    cursor.execute("""
        SELECT date, goal_achieved, is_weekend
        FROM streak_log
        WHERE date <= ?
        ORDER BY date DESC
    """, (today.isoformat(),))

    rows = cursor.fetchall()
    conn.close()

    streak = 0
    for row in rows:
        log_date, goal_achieved, is_weekend = row

        # If its a weekend day
        if is_weekend:
            # But the goal was achieved
            if goal_achieved:
                streak += 1 # Then we add a streak
            else:
                continue # If there was no goal achieved, we dont reset it
        else:
            if goal_achieved:
                streak += 1
            # If no goal was achieved that day
            else:
                # But the day is today
                if log_date == today.isoformat():
                    continue  # We dont count it yet
                else:
                    break     # We break it

    return streak
    
# Calculcate karma %
def get_current_karma():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today()
    start_date = today - timedelta(days=90)

    cursor.execute("""
        SELECT COUNT(*) FROM streak_log
        WHERE date BETWEEN ? AND ?
          AND goal_achieved = 1
          AND strftime('%w', date) BETWEEN '1' AND '5'
    """, (start_date, today))
    completed_weekdays = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM streak_log
        WHERE date BETWEEN ? AND ?
          AND goal_achieved = 1
          AND (strftime('%w', date) = '0' OR strftime('%w', date) = '6')
    """, (start_date, today))
    completed_weekends = cursor.fetchone()[0]

    weekdays_past_3_months = sum(
        1 for i in range(91)
        if (start_date + timedelta(days=i)).weekday() < 5
    )

    relevant_days = weekdays_past_3_months + completed_weekends
    completed_days = completed_weekdays + completed_weekends

    karma = (completed_days / relevant_days * 100) if relevant_days > 0 else 0
    return karma

# Get focus data for statistics
def get_focus_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DATE(timestamp) AS day, SUM(duration) AS total_duration
        FROM focus_sessions
        WHERE timestamp >= DATE('now', '-29 days')
        GROUP BY day
        ORDER BY day;
    """)
    rows = cursor.fetchall()
    conn.close()

    return rows

# Get subject data for statistics
def get_subject_data_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, SUM(fs.duration) AS total_duration
        FROM focus_sessions fs
        JOIN subjects s ON fs.subject_id = s.id
        WHERE fs.timestamp >= DATE('now', '-29 days')
        GROUP BY fs.subject_id
        ORDER BY total_duration DESC;
    """)
    rows = cursor.fetchall()
    conn.close()

    return rows

# Get period data for statistics
def get_period_data_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.name, SUM(fs.duration) AS total_duration
        FROM focus_sessions fs
        JOIN periods p ON fs.period_id = p.id
        WHERE fs.timestamp >= DATE('now', '-29 days')
        GROUP BY fs.period_id
        ORDER BY total_duration DESC;
    """)
    rows = cursor.fetchall()
    conn.close()

    return rows

# Get subject with duration for statistics (last 30 days)
def get_subject_time_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, SUM(fs.duration) as total_duration
        FROM focus_sessions fs
        JOIN subjects s ON fs.subject_id = s.id
        WHERE fs.timestamp >= DATE('now', '-29 days')
        GROUP BY fs.subject_id
        ORDER BY total_duration DESC;
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

# Get subject with duration for statistics (all history)
def get_subject_time_data_all_include_archived():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, SUM(fs.duration) as total_duration
        FROM focus_sessions fs
        JOIN subjects s ON fs.subject_id = s.id
        GROUP BY fs.subject_id
        ORDER BY total_duration DESC;
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

# Get subject with duration for statistics (all history withou)
def get_subject_time_data_all_not_include_archived():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, SUM(fs.duration) as total_duration
        FROM focus_sessions fs
        JOIN subjects s ON fs.subject_id = s.id
        WHERE s.is_archived = 0
        GROUP BY fs.subject_id
        ORDER BY total_duration DESC;
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows

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

# Save daily goal to streak_log
def save_daily_goal():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()

    # Query if there's a row for today
    cursor.execute("SELECT 1 FROM streak_log WHERE date = ?", (today,))
    existing = cursor.fetchone()

    if existing:
        # if there's a row, then we update it
        cursor.execute(
            "UPDATE streak_log SET goal_achieved = 1 WHERE date = ?",
            (today,)
        )
    else:
        # If there's no row, then we insert it
        cursor.execute(
            "INSERT INTO streak_log (date, goal_achieved, is_weekend) VALUES (?, ?, ?)",
            (today, 1, 1 if date.today().weekday() >= 5 else 0)
        )

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

# Update user_stats
def update_user_stats(data:dict):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE user_stats SET
            total_focus_time_mins =:total_focus_time_mins,
            focus_sessions_completed = :focus_sessions_completed,
            longest_focus_session = :longest_focus_session,
            longest_streak = :longest_streak
    """

    cursor.execute(query,data)
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

# Archive subject setting
def archive_subject_settings(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE subjects SET
            is_archived = ?
        WHERE id = ?
    """
    cursor.execute(query, (1, id))
    conn.commit()
    conn.close()

# Unarchive subject setting
def unarchive_subject_settings(id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE subjects SET
            is_archived = ?
        WHERE id = ?
    """
    cursor.execute(query, (0, id))
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

# Get daily quote
def get_today_quote():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().isoformat()
    cursor.execute("SELECT text, author FROM quotes WHERE date = ?", (today,))
    result = cursor.fetchone()

    if result:
        return result[0], result[1]
    
    response = requests.get("https://zenquotes.io/api/today")
    if response.status_code == 200:
        data = response.json()[0]
        text = data["q"]
        author = data["a"]

        cursor.execute("INSERT INTO quotes (text, author, date) VALUES (?,?,?)", (text, author, today))
        conn.commit()
        return text, author
    
    return "monkmode is the way of life", "dop14"

# Check the streak_log for missing days
def check_streak_log():
    conn = get_connection()
    cursor = conn.cursor()

    # Get the last row
    cursor.execute("SELECT date FROM streak_log ORDER BY date DESC LIMIT 1")
    last_row = cursor.fetchone()

    today = date.today()

    # if there's a last row
    if last_row:
        last_date = datetime.strptime(last_row[0], "%Y-%m-%d").date()
        delta = (today - last_date).days

        # If there are missing days between last date and today
        if delta > 0:
            for i in range(1, delta + 1):
                missing_date = last_date + timedelta(days=i)
                is_weekend = 1 if missing_date.weekday() >= 5 else 0
                cursor.execute(
                    "INSERT OR IGNORE INTO streak_log (date, goal_achieved, is_weekend) VALUES (?, ?, ?)",
                    (missing_date, False, is_weekend)
                )
    # if there is no last row, then we add today as the first day with goal_achieved = False
    else:
        is_weekend = 1 if today.weekday() >= 5 else 0
        cursor.execute(
            "INSERT INTO streak_log (date, goal_achieved, is_weekend) VALUES (?, ?, ?)",
            (today, False, is_weekend)
        )

    conn.commit()
    conn.close()

def get_connection():
    db_path = get_db_path()
    return sqlite3.connect(db_path)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    schema_path = get_resource_path("database/schema.sql")
    with open(schema_path, "r") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)

    add_default_period(cursor)
    add_default_subject(cursor)
    add_default_user_preferences(cursor)
    add_default_user_stats(cursor)

    conn.commit()
    conn.close()

     