import sqlite3

conn = sqlite3.connect("day_27/students.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER
    )
""")

students_list = [("Mehran", 95), ("Emran", 83), ("Anees", 88)]
cursor.executemany("""INSERT INTO students(name, score) VALUES (?, ?)""", students_list)

print(f"Successfully inserted {len(students_list)} students!")

cursor.execute("SELECT * FROM students")
all_rows = cursor.fetchall()

print("\n--- Current Students in Database ---")
for row in all_rows:
    print(f"ID:{row[0]} | Name: {row[1]} | Score: {row[2]}")

cursor.execute("UPDATE students SET score = ? WHERE name = ?", (91, "Emran"))
print("\nUpdated Emran's score to 91!")

cursor.execute("DELETE FROM students WHERE name = ?", ("Anees",))
print("Deleted Anees from Database")
cursor.execute("SELECT * FROM students")
print("\n--- Final Database State ---")
for row in cursor.fetchall():
    print(f"ID: {row[0]} | Name: {row[1]} | Score: {row[2]}")

conn.commit()
conn.close()

print("Database and table created successfully!")
