from database.db_connection import get_connection
from datetime import datetime

def add_security_event(source_id, event_type_id, message, ip=None, username=None):
    conn = get_connection()
    cur = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
        INSERT INTO SecurityEvents(timestamp, source_id, event_type_id, message, ip_address, username)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (timestamp, source_id, event_type_id, message, ip, username))

    conn.commit()
    conn.close()

def get_login_failed_last_24h():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM SecurityEvents
    JOIN EventTypes ON EventTypes.id = SecurityEvents.event_type_id
    WHERE EventTypes.type_name = 'Login Failed'
      AND timestamp >= datetime('now', '-1 day')
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

def detect_bruteforce():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT ip_address, COUNT(*) 
    FROM SecurityEvents
    JOIN EventTypes ON EventTypes.id = SecurityEvents.event_type_id
    WHERE EventTypes.type_name = 'Login Failed'
      AND timestamp >= datetime('now', '-1 hour')
    GROUP BY ip_address
    HAVING COUNT(*) > 5
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

def get_critical_last_week():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT EventSources.name, SecurityEvents.timestamp, SecurityEvents.message
    FROM SecurityEvents
    JOIN EventTypes ON EventTypes.id = SecurityEvents.event_type_id
    JOIN EventSources ON EventSources.id = SecurityEvents.source_id
    WHERE EventTypes.severity = 'Critical'
      AND timestamp >= datetime('now', '-7 days')
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

def search_events(keyword):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM SecurityEvents
    WHERE message LIKE ?
    """, ('%' + keyword + '%',))

    rows = cur.fetchall()
    conn.close()
    return rows
