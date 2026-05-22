import sqlite3

conn = sqlite3.connect("student.db")

conn.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT, age INTEGER)")

print("Table Created")

conn.execute("INSERT INTO students VALUES(1,'Huzaif',20)")
conn.execute("INSERT INTO students VALUES(2,'Himesh',21)")
conn.execute("INSERT INTO students VALUES(3,'Rajveer',22)")

conn.commit()

print("Records Inserted")

data = conn.execute("SELECT * FROM students")

print("\nStudent Data")
for row in data:
    print(row)

conn.execute("UPDATE students SET age = 23 WHERE id = 1")

conn.commit()

print("\nAfter Update")

data = conn.execute("SELECT * FROM students")

for row in data:
    print(row)

conn.execute("DELETE FROM students WHERE id = 3")

conn.commit()

print("\nAfter Delete")

data = conn.execute("SELECT * FROM students")

for row in data:
    print(row)

conn.close()

print("\nDatabase Closed")