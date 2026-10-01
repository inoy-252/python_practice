"""
day_30/database.py - Persistence Layer for Health Predictions.
Handles all SQLite connections, table initialization, and queries.
"""

import sqlite3

DB_FILE = "day_30/health_predictions.db"


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            age INTEGER,
            bmi REAL,
            heart_rate INTEGER,
            risk_level TEXT,
            risk_score REAL,
            confidence REAL
        )
    """)
    conn.commit()
    conn.close()


def insert_prediction(name, age, bmi, heart_rate, risk_level, risk_score, confidence):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO health_predictions (
            patient_name, age, bmi, heart_rate, risk_level, risk_score, confidence
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (name, age, bmi, heart_rate, risk_level, risk_score, confidence),
    )
    conn.commit()
    conn.close()


def get_recent_history(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM health_predictions ORDER BY id DESC LIMIT ?", (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
