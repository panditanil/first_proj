import sqlite3

class Employee_database:
    def __init__(self,db_name="employee.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def Create_Table(self):
        query = """
                CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, number inteher)
            
                """

