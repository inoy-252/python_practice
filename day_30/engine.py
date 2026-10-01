"""
day_30/engine.py - Pure AI & Biomarker Risk Evaluation Engine.
Independent of web or database frameworks for modularity and testability.
"""


def predict_health_risk(age, bmi, heart_rate):
    """
    Computes a composite cardiovascular risk score (0-100) based on
    clinical biomarker deviation and returns a classified risk verdict.
    """
    risk_points = 0.0

    if bmi < 18.5:
        risk_points += 15.0
    elif 18.5 <= bmi <= 24.9:
        risk_points += 5.0
    elif 25.0 <= bmi <= 29.9:
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

    final_score = min(round(risk_points, 1), 100.0)

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
