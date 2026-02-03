import sqlite3

conn = sqlite3.connect("ci.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS failures(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
)
""")

conn.commit()
conn.close()
