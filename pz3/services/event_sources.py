from database.db_connection import get_connection

def add_event_source(name, location, type_):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO EventSources(name, location, type)
        VALUES (?, ?, ?)
    """, (name, location, type_))

    conn.commit()
    conn.close()

def get_event_sources():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, location FROM EventSources")
    rows = cur.fetchall()

    conn.close()
    return rows
