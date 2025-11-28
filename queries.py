from datetime import datetime
from .connection import get_connection

def db_get_all():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students ORDER BY if DESC").fetchall()
    conn.close()
    return [dict(r) from r in rows]