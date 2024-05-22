import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("database connected")

cursor = sqliteConnection.cursor()
print("Database initlized")

create_table_query = "CREATE TABLE  emp (id integer primary key AUTOINCREMENT, name text, address text, email text)"
cursor.execute(create_table_query)
print("Table created successfully")