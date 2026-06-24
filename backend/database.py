import sqlite3

conn = sqlite3.connect(
    "evaluation.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS runs(
    id INTEGER PRIMARY KEY,
    prompt TEXT,
    status TEXT,
    latency REAL
)
""")

conn.commit()