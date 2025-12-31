import sqlite3
import hashlib

def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        login TEXT PRIMARY KEY,
        password TEXT,
        full_name TEXT
    )
    """)

    connection.commit()
    connection.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(login, password, full_name):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (login, hashed_password, full_name)
        )
        connection.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("User already exists.")

    connection.close()

def update_password(login, new_password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    hashed_password = hash_password(new_password)

    cursor.execute(
        "UPDATE users SET password = ? WHERE login = ?",
        (hashed_password, login)
    )

    if cursor.rowcount == 0:
        print("User not found.")
    else:
        connection.commit()
        print("Password updated.")

    connection.close()

def authenticate_user(login, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    hashed_password = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE login = ? AND password = ?",
        (login, hashed_password)
    )

    result = cursor.fetchone()
    connection.close()

    if result:
        print("Authentication successful.")
    else:
        print("Authentication failed.")
