"""
day_30/app.py - Web Presentation & Routing Layer.
Connects the web frontend to the AI engine and database modules.
"""

from database import get_recent_history, init_db, insert_prediction
from engine import predict_health_risk
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


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

    insert_prediction(
        name=name,
        age=age,
        bmi=bmi,
        heart_rate=heart_rate,
        risk_level=ai_result["risk_level"],
        risk_score=ai_result["risk_score"],
        confidence=ai_result["confidence"],
    )

    ai_result["name"] = name
    history = get_recent_history()
    return render_template("index.html", result=ai_result, history=history)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON request body"}), 400

    name = data.get("name", "Unknown")
    age = int(data.get("age", 25))
    bmi = float(data.get("bmi", 22.0))
    heart_rate = int(data.get("heart_rate", 70))

    ai_result = predict_health_risk(age, bmi, heart_rate)

    insert_prediction(
        name=name,
        age=age,
        bmi=bmi,
        heart_rate=heart_rate,
        risk_level=ai_result["risk_level"],
        risk_score=ai_result["risk_score"],
        confidence=ai_result["confidence"],
    )

    return jsonify(
        {"status": "Success", "patient": name, "ai_prediction": ai_result}
    ), 200


if __name__ == "__main__":
    init_db()
    print("Database ready.")
    print("Starting AI Health Risk Advisor on http://127.0.0.1:5000 ...")
    app.run(port=5000)
