from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("ci.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    conn = get_db()
    c = conn.cursor()
    total = c.execute("SELECT COUNT(*) FROM failures").fetchone()[0]
    last = c.execute("SELECT message FROM failures ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return jsonify({
        "total": total,
        "last": last[0] if last else "No failures yet"
    })

@app.route("/api/logs")
def logs():
    conn = get_db()
    c = conn.cursor()
    data = c.execute("SELECT message FROM failures ORDER BY id DESC LIMIT 10").fetchall()
    conn.close()
    return jsonify(data)

@app.route("/api/failure", methods=["POST"])
def add_failure():
    msg = request.json["message"]
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO failures(message) VALUES (?)", (msg,))
    conn.commit()
    conn.close()
    return {"status":"ok"}

app.run(debug=True)
