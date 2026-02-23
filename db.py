import sqlite3
from pathlib import Path

DB_PATH = Path("assignments.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS assignments(
                assignment_id TEXT PRIMARY KEY,
                due_at TEXT
                )
""")
    conn.commit()
    conn.close()


def has_assignment(assignment_id:str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT 1 FROM assignments WHERE assignment_id = ?",(assignment_id,)
        )
    
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def save_assignment(assignment_id: str, due_at: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO assignments (assignment_id,due_at) VALUES (?,?)",
        (assignment_id,due_at)
    )
    conn.commit()
    conn.close()

    