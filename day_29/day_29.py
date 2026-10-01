import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
DB_FILE = "day_29/health_predictions.db"


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS health_predictions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            age INTEGER,
            bmi REAL,
            heart_rate INTEGER,
            risk_level TEXT,
            risk_score REAL, 
            confidence REAl
        )
    """)
    conn.commit()
    conn.close()


def predict_health_risk(age, bmi, heart_rate):
    risk_points = 0.0

    if bmi < 18.5:
        risk_points += 15.0
    elif 18.5 <= bmi <= 24.9:
        risk_points += 5.0
    elif 25 <= bmi <= 29.9:
        risk_points += 25.0
    else:
        risk_points += 45.0

    if heart_rate < 45:
        risk_points += 45.0
    elif 45 <= heart_rate < 60:
        risk_points += 6.0
    elif 60 <= heart_rate <= 75:
        risk_points += 4.0
    elif 76 <= heart_rate <= 90:
        risk_points += 20.0
    else:
        risk_points += 35.0

    if age > 50:
        risk_points += 15.0
    elif age > 35:
        risk_points += 8.0

    final_score = min(round(risk_points, 1), 100)

    if final_score < 30.0:
        risk_level = "Low Risk (Optimal)"
        badge_class = "badge-optimal"
        recommendation = "Excellent cardiovascular indicators. Maintain current activity and nutrition."
        confidence = 96.5
    elif final_score <= 60.0:
        risk_level = "Moderate Risk (Attention Needed)"
        badge_class = "badge-moderate"
        recommendation = "Borderline biomarker metrics detected. Incorporate regular cardio and monitor diet."
        confidence = 91.2
    else:
        risk_level = "High Risk (Action Recommended)"
        badge_class = "badge-high"
        recommendation = "Elevated risk profile. Consultation with a healthcare provider is recommended."
        confidence = 94.8
    return {
        "risk_level": risk_level,
        "risk_score": final_score,
        "confidence": confidence,
        "recommendation": recommendation,
        "badge_class": badge_class,
    }


def get_recent_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_predictions ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route("/", methods=["GET"])
def home():
    history = get_recent_history()
    return render_template("index.html", result=None, history=history)


@app.route("/predict", methods=["POST"])
def predict():
    name = request.form["name"]
    age = int(request.form["age"])
    bmi = float(request.form["bmi"])
    heart_rate = int(request.form["heart_rate"])

    ai_result = predict_health_risk(age, bmi, heart_rate)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO health_predictions (
            patient_name, age, bmi, heart_rate, risk_level, risk_score, confidence
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            name,
            age,
            bmi,
            heart_rate,
            ai_result["risk_level"],
            ai_result["risk_score"],
            ai_result["confidence"],
        ),
    )
    conn.commit()
    conn.close()

    ai_result["name"] = name
    history = get_recent_history()
    return render_template("index.html", result=ai_result, history=history)


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
    print("Starting AI Health Risk Advisor on http://127.0.0.1:5000 ...")
    app.run(port=5000)
