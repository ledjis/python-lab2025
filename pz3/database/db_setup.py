from database.db_connection import get_connection

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS EventSources (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        location TEXT,
        type TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS EventTypes (
        id INTEGER PRIMARY KEY,
        type_name TEXT UNIQUE,
        severity TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS SecurityEvents (
        id INTEGER PRIMARY KEY,
        timestamp DATETIME,
        source_id INTEGER,
        event_type_id INTEGER,
        message TEXT,
        ip_address TEXT,
        username TEXT,
        FOREIGN KEY(source_id) REFERENCES EventSources(id),
        FOREIGN KEY(event_type_id) REFERENCES EventTypes(id)
    );
    """)

    conn.commit()
    conn.close()

def insert_initial_event_types():
    conn = get_connection()
    cur = conn.cursor()

    predefined = [
        ("Login Success", "Informational"),
        ("Login Failed", "Warning"),
        ("Port Scan Detected", "Warning"),
        ("Malware Alert", "Critical"),
    ]

    for name, sev in predefined:
        cur.execute("""
            INSERT OR IGNORE INTO EventTypes(type_name, severity)
            VALUES (?, ?)
        """, (name, sev))

    conn.commit()
    conn.close()
