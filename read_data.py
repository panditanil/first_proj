import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("database connected")

cursor = sqliteConnection.cursor()
print("Database initlized")

sql_read_query = "SELECT * FROM emp"
cursor.execute(sql_read_query)
print(cursor.fetchall())

sqliteConnection.close()