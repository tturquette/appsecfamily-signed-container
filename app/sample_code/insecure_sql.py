import sqlite3

def get_user_by_id(user_id):
    # Vulnerable to SQL Injection
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchall()
