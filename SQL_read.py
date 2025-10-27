import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('select * from users')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

