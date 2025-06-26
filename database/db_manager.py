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

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database successfully initialized")