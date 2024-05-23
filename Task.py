import sqlite3

while True:

        comm = input(" Enter add, list, delete and  exit : ")

        match comm:

            case 'add':
                database_connection = sqlite3.connect("emp_database.db") #Database created
            
                cursor = database_connection.cursor() #Database initilized
                
                create_table = "CREATE TABLE IF NOT EXISTS employee (id integer primary key AUTOINCREMENT, name text, address text, email text, number integer)"
                cursor.execute(create_table)

                #input Data from User
                name = input("Enter name: ")
                address = input("Enter Address: ")
                email = input("Enter email: ")
                number = input("Enter number: ")

                #data inserted into table
                insert_data = "INSERT INTO employee(name,address,email,number) values (?,?,?,?)"
                cursor.execute(insert_data,(name, address,email,number))
                database_connection.commit()
                print("Data added successfully.")

            case 'list':
                database_connection = sqlite3.connect("emp_database.db")
                cursor = database_connection.cursor()
                select_data = "SELECT * FROM employee"
                cursor.execute(select_data)
                data = cursor.fetchall()
                if data:
                    for user_data in data:
                        print(f'''Employee Id: {user_data[0]}
                                  Name: {user_data[1]}
                                  Address: {user_data[2]}
                                  Email: {user_data[3]}
                                  M_Number: {user_data[4]}''')
                else:
                    print("No records")
            case 'delete':
                database_connection = sqlite3.connect("emp_database.db")
                cursor = database_connection.cursor()

                rec_id = int(input("Enter id to delete record: "))
                del_data = "DELETE FROM employee WHERE id = ?"
                cursor.execute(del_data, (rec_id,))
                database_connection.commit()
                print("Deleted successfully")

            case 'exit':
                print("Exit program........")
                break
            case _: 
                print("Please Enter add, list, delete and  exit : ")
                



