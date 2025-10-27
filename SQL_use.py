import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John', 25))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Nikola', 32))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Pepi', 32))


conn.commit()
conn.close()
