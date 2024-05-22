import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("database connected")

cursor = sqliteConnection.cursor()
print("Database initlized")
insert_data_query = "INSERT INTO emp(name,address,email) values('Anil','Gaur','anil@gmail.com')"
cursor.execute(insert_data_query)
sqliteConnection.commit()
