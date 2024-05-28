import sqlite3

class EmployeeDatabase:
    def __init__(self, db_name="employee.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_employee(self, name, age, department):
        query = 'INSERT INTO employees (name, age, department) VALUES (?, ?, ?)'
        self.conn.execute(query, (name, age, department))
        self.conn.commit()

    def list_employees(self):
        cursor = self.conn.execute('SELECT * FROM employees')
        return cursor.fetchall()

    def delete_employee(self, employee_id):
        query = 'DELETE FROM employees WHERE id = ?'
        self.conn.execute(query, (employee_id,))
        self.conn.commit()

class EmployeeApp:
    def __init__(self):
        self.db = EmployeeDatabase()
        self.menu()

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Delete Employee")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.list_employees()
            elif choice == '3':
                self.delete_employee()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_employee(self):
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        department = input("Enter employee department: ")

        if name and age.isdigit() and department:
            self.db.add_employee(name, int(age), department)
            print("Employee added successfully.")
        else:
            print("Invalid input. Please try again.")

    def list_employees(self):
        employees = self.db.list_employees()
        if employees:
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}")
        else:
            print("No employees found.")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")

        if employee_id.isdigit():
            self.db.delete_employee(int(employee_id))
            print("Employee deleted successfully.")
        else:
            print("Invalid ID. Please try again.")

if __name__ == "__main__":
    EmployeeApp()
