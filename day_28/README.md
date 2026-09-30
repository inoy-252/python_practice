# 🌐 Day 28: Full-Stack Web API & SQLite Database Integration

## 📌 Overview

On **Day 28**, we bridged the gap between **Web APIs (Day 26)** and **Persistent Databases (Day 27)** to build a complete backend service.

Prior to this:
- In **Day 26**, our API lost its data every time the server restarted because variables stored in memory are wiped when Python exits.
- In **Day 27**, we learned how to store and query data in an SQLite database file using SQL statements.

**Day 28 unites both concepts:** A client sends data over the web via an HTTP request, Flask processes and evaluates the logic, SQLite saves the result permanently to disk, and the client receives a structured JSON confirmation.

---

## 🏗️ Architecture & Data Flow

```text
[ Client / Browser / curl ]
         │
         │ 1. HTTP Request (POST /evaluate with JSON body)
         ▼
[ Flask Web Server (day_28.py) ]
         │
         │ 2. Validate input ("name", "score")
         │ 3. Apply business logic (Pass >= 80 vs Needs practice)
         ▼
[ SQLite Database (evaluations.db) ]
         │
         │ 4. INSERT INTO evaluations (student_name, score, result)
         ▼
[ Flask Response Generator ]
         │
         │ 5. Return JSON response with HTTP status 200/400
         ▼
[ Client Receives Structured Output ]
```

---

## 🛠️ API Endpoints

### 1. `POST /evaluate` — Submit & Store Student Score

- **Purpose:** Receives a student's name and test score, decides whether the student passed or needs practice, and writes the record permanently to `evaluations.db`.
- **Method:** `POST`
- **Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "name": "Mehran",
    "score": 92
  }
  ```
- **Response (`200 OK`):**
  ```json
  {
    "result": "Passed (Satisfactory)",
    "saved_to_database": true,
    "score": 92,
    "status": "Success",
    "student_name": "Mehran"
  }
  ```
- **Error Guardrail (`400 Bad Request`):**
  Returned if `name` or `score` is missing or invalid:
  ```json
  {
    "error": "Please provide both 'name' and 'score'."
  }
  ```

---

### 2. `GET /history` — Retrieve All Stored Evaluations

- **Purpose:** Queries the SQLite database table `evaluations` and returns all stored records as a JSON list.
- **Method:** `GET`
- **Response (`200 OK`):**
  ```json
  {
    "total_records": 2,
    "history": [
      {
        "id": 1,
        "name": "Mehran",
        "score": 92,
        "result": "Passed (Satisfactory)"
      },
      {
        "id": 2,
        "name": "Emran",
        "score": 65,
        "result": "Needs more practice"
      }
    ]
  }
  ```

---

## 🗄️ Database Schema

The application automatically creates the `evaluations.db` database with the following table:

```sql
CREATE TABLE IF NOT EXISTS evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    score INTEGER,
    result TEXT
);
```

- **`id`**: Unique integer identifier, automatically incremented for each new entry.
- **`student_name`**: Text string storing the student's name.
- **`score`**: Integer value representing the examination score.
- **`result`**: Text verdict computed by the Python application (`"Passed (Satisfactory)"` or `"Needs more practice"`).

---

## 💡 Key Architectural Concepts & FAQs

### 1. Why does JSON output order look different from how we typed it?
In Python and JSON specifications, objects (dictionaries) represent **key-value pairs**, not ordered lists. When serializing data using `flask.jsonify()`, Python dictionaries may output keys in alphabetical order or by internal hash lookup. Clients consuming the API access data by key name (e.g. `response["student_name"]`), so the visual order in the raw string does not affect functionality.

### 2. Why does submitting the same student twice create multiple entries?
Unless a database column has an explicit `UNIQUE` constraint, each SQL `INSERT` statement is treated as a new historical event. In evaluation and log systems, multiple submissions represent distinct test attempts or submission timestamps, each receiving its own auto-incremented `id`.

### 3. Why does the browser display the response on a single line?
Raw HTTP JSON responses are transmitted without extra whitespace or line breaks to minimize network payload size. Browsers render raw text on a single line unless formatted by a developer console, a JSON formatter extension, or a frontend UI.

---

## 🚀 How to Run and Test

### 1. Activate the Virtual Environment
```bash
source day_28/day_28_env/bin/activate
```

### 2. Start the Server
```bash
python day_28/day_28.py
```
*The server will start listening at `http://127.0.0.1:5000`.*

### 3. Send an Evaluation (in a separate terminal)
```bash
curl -X POST http://127.0.0.1:5000/evaluate \
     -H "Content-Type: application/json" \
     -d '{"name": "Mehran", "score": 92}'
```

### 4. View Stored Records
Open in your browser or run:
```bash
curl http://127.0.0.1:5000/history
```

---

## 🤖 Connection to AI & Machine Learning

In real-world AI/ML production pipelines:
1. **Model Serving APIs:** Machine learning models are wrapped inside web frameworks (like Flask or FastAPI) that expose prediction endpoints (e.g. `POST /predict`).
2. **Persistent Inference Logs:** Every input feature and model prediction is logged to a database for auditing, drift detection, and monitoring accuracy.
3. **Historical Retrieval:** Dashboards and retraining pipelines query these databases via `GET` endpoints to evaluate model performance over time.
