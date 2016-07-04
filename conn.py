import sqlite3

conn = sqlite3.connect('F:\SQLiteSpy_1.9.10\World.db3')

cursor = conn.cursor()

cursor.execute('select * from city')

values = cursor.fetchall()

values