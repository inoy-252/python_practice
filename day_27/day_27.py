"""
Day 27: Python Databases & Data Persistence
Focus: SQLite3, Relational Tables, Transactions, and CRUD Operations.
Context: AI Model Registry & Experiment Tracking Engine.
"""

import sqlite3
from datetime import datetime

DB_FILE = "day_27/ai_experiments.db"


def get_connection():
    """Returns a connection to the SQLite database with row factory enabled."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Enables column-name access like dicts
    return conn


def init_db():
    """Initializes the database schema if it doesn't already exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS models (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT NOT NULL,
                architecture TEXT NOT NULL,
                accuracy REAL NOT NULL,
                loss REAL NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()
    print("[DB] Initialized database and 'models' table successfully.")


def log_experiment(model_name, architecture, accuracy, loss):
    """Inserts a new model experiment record using parameterized SQL (safe from SQL injection)."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO models (model_name, architecture, accuracy, loss, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (model_name, architecture, accuracy, loss, now))
        conn.commit()
        return cursor.lastrowid


def get_all_models():
    """Retrieves all registered models ordered by accuracy (highest first)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, model_name, architecture, accuracy, loss, created_at
            FROM models
            ORDER BY accuracy DESC
        """)
        return cursor.fetchall()


def update_model_accuracy(model_id, new_accuracy, new_loss):
    """Updates the performance metrics of an existing model record."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE models
            SET accuracy = ?, loss = ?
            WHERE id = ?
        """, (new_accuracy, new_loss, model_id))
        conn.commit()
        return cursor.rowcount


def delete_failed_runs(loss_threshold=0.50):
    """Deletes low-performing experiment runs exceeding a loss threshold."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM models
            WHERE loss > ?
        """, (loss_threshold,))
        conn.commit()
        return cursor.rowcount


def main():
    print("=" * 60)
    print("--- Day 27: AI Experiment Tracker Database (SQLite3) ---")
    print("=" * 60)

    # 1. Initialize Schema
    init_db()

    # 2. Insert Sample Experiments (CRUD: Create)
    print("\n[1] Logging Model Experiments...")
    m1 = log_experiment("Llama-Vision-7B", "Transformer", 0.942, 0.12)
    m2 = log_experiment("BERT-Classifier-v2", "Encoder", 0.885, 0.28)
    m3 = log_experiment("ResNet-50-Baseline", "CNN", 0.720, 0.58)
    m4 = log_experiment("GPT-Mini-Agent", "Decoder", 0.965, 0.08)
    print(f"Logged 4 models. Example IDs: {m1}, {m2}, {m3}, {m4}")

    # 3. Read Experiments (CRUD: Read)
    print("\n[2] Querying Top Models (Sorted by Accuracy):")
    models = get_all_models()
    for row in models:
        print(f"  • ID {row['id']} | {row['model_name']:<20} | {row['architecture']:<12} | "
              f"Acc: {row['accuracy']:.3f} | Loss: {row['loss']:.2f} | Logged: {row['created_at']}")

    # 4. Update an Experiment (CRUD: Update)
    print("\n[3] Fine-tuning Model ID 2 (Updating Accuracy)...")
    updated = update_model_accuracy(m2, new_accuracy=0.915, new_loss=0.19)
    print(f"Updated {updated} record(s).")

    # 5. Delete Underperforming Experiment (CRUD: Delete)
    print("\n[4] Cleaning up failed runs (Loss > 0.50)...")
    deleted = delete_failed_runs(loss_threshold=0.50)
    print(f"Pruned {deleted} failed experiment run(s).")

    # 6. Final Table State
    print("\n[5] Final Production Registry State:")
    final_models = get_all_models()
    for row in final_models:
        print(f"  ✓ ID {row['id']}: {row['model_name']} (Accuracy: {row['accuracy']:.3f})")

    print("\n[Done] Database operations complete. Data persisted in 'day_27/ai_experiments.db'.")


if __name__ == "__main__":
    main()
