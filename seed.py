import sqlite3

data = [
    "Test failed because add(2,3) returned 5 but expected 100. Fix by correcting the test assertion.",
    "Dependency installation failed due to missing pytest in requirements.txt.",
    "Module import error: app.py not found. Check file path and PYTHONPATH.",
    "CI pipeline stopped because a syntax error was detected in test_app.py.",
    "Deployment skipped because CI checks did not pass."
]

conn = sqlite3.connect("ci.db")
c = conn.cursor()

for msg in data:
    c.execute("INSERT INTO failures(message) VALUES (?)", (msg,))

conn.commit()
conn.close()

print("Fake AI failures added 😈")
