from database.db_connection import get_connection
import sqlite3

def add_event_type(type_name, severity):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO EventTypes(type_name, severity)
            VALUES (?, ?)
        """, (type_name, severity))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Такий тип події вже існує!")
    conn.close()

def get_event_types():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, type_name, severity FROM EventTypes ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows
