import sqlite3
import datetime import datetime


DB_FILE = 'students.db'

def get_connection():
    """Get database connection"""
    conn = sqllite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

    def init_database():
        """Initialize database and create tables"""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
           CREATE TABLE IF NOT EXISTS students(
           id INTEGER PRIMARY KEY AUTOINCREMENT
           name TEXT NOT NULL,
           email TEXT NOT NULL,
           course TEXT NOT NULL,
           year TEXT NOT NULL,
           created_at TEXT NOT NULL.
           updated_at TEXT
           )
    ''')

    conn.commit()
    conn.close()
    print(" Database initialized")