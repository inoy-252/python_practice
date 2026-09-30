import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)
DB_FILE = "day_28/evaluations.db"


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            score INTEGER,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/evaluate", methods=["POST"])
def evaluate():
    incoming = request.get_json()
    if not incoming or "name" not in incoming or "score" not in incoming:
        return jsonify({"error": "Please provide both 'name' and 'score'."}), 400

    name = incoming["name"]
    score = incoming["score"]

    if score >= 80:
        verdict = "Passed (Satisfactory)"
    else:
        verdict = "Needs more practice"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO evaluations (student_name, score, result)
        VALUES (?, ?, ?)
    """, (name, score, verdict))
    conn.commit()
    conn.close()

    return jsonify({
        "status": "Success",
        "student_name": name,
        "score": score,
        "result": verdict,
        "saved_to_database": True,
    })

@app.route("/history", methods=["GET"])
def history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evaluations")
    rows = cursor.fetchall()
    conn.close()

    records = []
    for r in rows:
        records.append({
            "id": r["id"],
            "name": r["student_name"],
            "score": r["score"],
            "result": r["result"],
        })
    return jsonify({"total_records": len(records), "history": records})


if __name__ == "__main__":
    init_db()
    print("Database ready. Starting API on http://127.0.0.1:5000 ...")
    app.run(port=5000)
