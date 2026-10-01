# 🌐 Day 29: Building an End-to-End AI Web Application

## 📌 Overview

On **Day 29**, we took every foundational concept learned throughout the 30-day curriculum—functions, dictionaries, multi-factor decision logic, web servers (Flask), databases (SQLite), and templating—and integrated them into a **complete, interactive, end-to-end AI product**.

Instead of interacting with code solely through terminal commands or API clients, this project provides a full-stack experience:
- An interactive **Web User Interface (HTML form)** for end users.
- A **Rule-Weighted AI Decision Engine** for clinical cardiovascular risk scoring.
- A **Permanent SQLite Database** (`health_predictions.db`) logging every assessment.
- A **Dynamic Live Dashboard** rendering real-time results and past patient history.

---

## 🏗️ System Architecture & Data Flow

```text
[ Web Browser ]
      │
      │ 1. User visits http://127.0.0.1:5000 (GET /)
      ▼
[ Flask Backend (home) ] ──────────► [ SQLite: health_predictions.db ]
      │                                       │ (Fetches last 10 records)
      │ 2. Renders index.html (result=None)   ▼
      ▼
[ Clean Webpage with Input Form ]
      │
      │ 3. User submits Name, Age, BMI, Heart Rate (POST /predict)
      ▼
[ Flask Backend (predict) ]
      │
      │ 4. Extracts form values & casts strings to numeric types (int, float)
      ▼
[ AI Decision Engine (predict_health_risk) ]
      │ - Evaluates BMI thresholds (Underweight, Normal, Overweight, Obese)
      │ - Evaluates Resting Heart Rate (Severe Bradycardia, Athletic, Normal, Elevated, Tachycardia)
      │ - Applies age resistance factor
      │ - Computes composite score (capped at 100) & AI confidence percentage
      ▼
[ SQLite Database Insertion ]
      │ - Executes INSERT INTO health_predictions ...
      │ - Commits transaction to disk
      ▼
[ Dynamic Template Re-rendering ]
      │ 5. Sends updated HTML with AI Result Card & Updated History Table
      ▼
[ User sees Verdict, Score, Confidence Badge & Real-Time History Row ]
```

---

## 🧠 The AI Decision Engine

The AI model evaluates cardiovascular risk using multi-variable clinical biomarker logic:

```python
def predict_health_risk(age, bmi, heart_rate):
    risk_points = 0.0

    # 1. BMI Evaluation
    if bmi < 18.5:
        risk_points += 15.0
    elif 18.5 <= bmi <= 24.9:
        risk_points += 5.0
    elif 25 <= bmi <= 29.9:
        risk_points += 25.0
    else:
        risk_points += 45.0

    # 2. Resting Heart Rate Evaluation (with Bradycardia Edge-Case Protection)
    if heart_rate < 45:
        risk_points += 45.0   # Severe bradycardia (acute medical emergency)
    elif 45 <= heart_rate < 60:
        risk_points += 6.0    # Athletic baseline or mild bradycardia
    elif 60 <= heart_rate <= 75:
        risk_points += 4.0    # Ideal normal resting range
    elif 76 <= heart_rate <= 90:
        risk_points += 20.0   # Elevated resting pulse
    else:
        risk_points += 35.0   # High resting pulse (tachycardia)

    # 3. Age Factor
    if age > 50:
        risk_points += 15.0
    elif age > 35:
        risk_points += 8.0

    # Capped at 100%
    final_score = min(round(risk_points, 1), 100.0)
    ...
```

### Key Engineering Decision: The Bradycardia Edge Case
During implementation, a critical domain edge-case was identified: a simplistic ladder (`heart_rate < 60`) would classify a dangerously low heart rate (e.g. 25–31 BPM) as athletic conditioning. We separated severe bradycardia (`< 45 BPM`) with maximum emergency penalty points (`+45.0`), ensuring critical patients are flagged as High Risk.

---

## 🗄️ Database Schema

The application automatically initializes `day_29/health_predictions.db` with the following table:

```sql
CREATE TABLE IF NOT EXISTS health_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    age INTEGER,
    bmi REAL,
    heart_rate INTEGER,
    risk_level TEXT,
    risk_score REAL,
    confidence REAL
);
```

- **`id`**: Auto-incrementing primary key tracking the order of submissions.
- **`patient_name`**: Patient or student identifier.
- **`age`**, **`bmi`**, **`heart_rate`**: Raw numerical input features.
- **`risk_level`**: Qualitative verdict (`Low Risk (Optimal)`, `Moderate Risk`, or `High Risk`).
- **`risk_score`**: Normalized composite score ($0.0$ to $100.0$).
- **`confidence`**: Statistical model confidence rating ($91.2\%$ to $96.5\%$).

---

## 💡 Key Architectural Concepts Mastered

### 1. `GET` vs. `POST`
- **`GET` (Read-only):** Fetches the webpage so the browser can display the initial form and history table without modifying any server state.
- **`POST` (Write / Create):** Packages user inputs inside the request body, delivers them to Flask, triggers AI scoring, and permanently creates a new database record.

### 2. Side-Effect Functions vs. Value-Returning Functions
- **`init_db()` (Side-Effect):** Performs an action on the disk (creates the table, commits, and closes). It does not return data to the caller.
- **`get_db_connection()` & `predict_health_risk()` (Value-Returning):** Provide objects (`conn`) and structured calculation dictionaries (`ai_result`) that subsequent lines of code depend upon.

### 3. What "Confidence" Means in AI Systems
In machine learning, models make probabilistic predictions rather than deterministic statements. An AI system outputs both the prediction and its confidence level. When biomarker features align with baseline health norms, confidence is high ($96.5\%$). In real-world production environments, lower confidence scores trigger human-in-the-loop validation.

### 4. Dynamic Templating (Jinja2)
- **`result=None` on initial page load:** Prevents empty result cards from displaying before the user has submitted data (`{% if result %}`).
- **`result=ai_result` after submission:** Injects the computed scores, colored badge classes, and clinical recommendations directly into the HTML response.

---

## 🚀 How to Run and Test

### 1. Activate Environment
```bash
source day_29/day_29_env/bin/activate
```

### 2. Start Web Application
```bash
python day_29/day_29.py
```

### 3. Open in Browser
Visit: **`http://127.0.0.1:5000`**

---

## 🤖 Connection to AI & Machine Learning Engineering

This project mirrors the end-to-end lifecycle of production AI applications:
1. **Feature Ingestion:** Sanitizing and casting raw user inputs into numerical feature vectors.
2. **Model Inference:** Passing features into a prediction pipeline to compute scores and confidence.
3. **Audit Logging & Telemetry:** Persisting inference inputs and outputs to a database for drift monitoring, auditability, and retraining pipelines.
4. **User Delivery:** Serving real-time predictions via an accessible web interface.
