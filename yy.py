# import tkinter as tk
# from tkinter import font
# from PIL import Image, ImageTk


# main = tk.Tk()
# main.title("School Management System")
# main.geometry("1440x900")  



# #Custom font
# custom_font = ("Times New Roman", 15)  

# #Adding School name
# school_name =tk.Label(main,text="Dav School Birgunj", font=("Times New Roman", 30))
# school_name.pack()


# #Adding background Image

# bg_image = Image.open(r"C:\Users\Anil Pandit\Desktop\nclass\myproject\first_proj\image\school.jpg") 
# bg_image_resized = bg_image.resize((1440, 800)) 
# bg_photo = ImageTk.PhotoImage(bg_image_resized)

# canvas = tk.Canvas(main, width=1440, height=800)
# canvas.pack(fill='both', expand=True)

# canvas.create_image(0, 0, image=bg_photo, anchor='nw')



# #Creating menu
# menu = tk.Menu(main, font=custom_font)
# main.config(menu=menu)
# file_menu = tk.Menu(menu, font=custom_font)
# menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit",command=main.quit)

# menu.add_cascade(label="Home", font=custom_font)
# menu.add_cascade(label="Add Student", font=custom_font, )
# menu.add_cascade(label="Show Student", font=custom_font)
# menu.add_cascade(label="Contact us", font=custom_font)
# menu.add_cascade(label="About", font=custom_font)



# main.mainloop()




import tkinter as tk
from tkinter import font
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

# Function to add student details to the database
def add_student():
    # Open connection to the database
    conn = sqlite3.connect('school.db')
    c = conn.cursor()

    # Insert student details into the database
    c.execute("INSERT INTO students (name, address, class, gender, mobile, fathers_name) VALUES (?, ?, ?, ?, ?, ?)",
              (name_entry.get(), address_entry.get(), class_entry.get(), gender_var.get(), mobile_entry.get(), fathers_name_entry.get()))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student added successfully.")

    # Clear the entry fields after adding the student
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    gender_var.set("")  # Clear the selected radio button
    mobile_entry.delete(0, tk.END)
    fathers_name_entry.delete(0, tk.END)

# Function to create the table in the database if it doesn't exist
def create_table():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students 
                 (id INTEGER PRIMARY KEY, name TEXT, address TEXT, class TEXT, gender TEXT, mobile TEXT, fathers_name TEXT)''')
    conn.commit()
    conn.close()

# Create the database table if it doesn't exist
create_table()

# Function to show student details from the database
def show_students():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    conn.close()

    # Display student details in a message box
    details = ""
    for student in students:
        details += f"Name: {student[1]}, Address: {student[2]}, Class: {student[3]}, Gender: {student[4]}, Mobile: {student[5]}, Father's Name: {student[6]}\n"
    messagebox.showinfo("Student Details", details)

# Function to switch back to the home screen with the background image
def go_home():
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor='nw')
    add_student_frame.place_forget()  # Hide the add_student_frame

main = tk.Tk()
main.title("School Management System")
main.geometry("1440x900")

# Custom font
custom_font = ("Times New Roman", 15)

# Adding School name
school_name = tk.Label(main, text="Dav School Birgunj", font=("Times New Roman", 30))
school_name.pack()

# Adding background Image
bg_image = Image.open(r"C:\Users\Anil Pandit\Desktop\nclass\myproject\first_proj\image\school.jpg")
bg_image_resized = bg_image.resize((1440, 800))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

canvas = tk.Canvas(main, width=1440, height=800)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor='nw')

# Creating menu
menu = tk.Menu(main, font=custom_font)
main.config(menu=menu)
file_menu = tk.Menu(menu, font=custom_font)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=main.quit)

menu.add_cascade(label="Home", font=custom_font, command=go_home)
menu.add_cascade(label="Add Student", font=custom_font, command=add_student)
menu.add_cascade(label="Show Student", font=custom_font, command=show_students)
menu.add_cascade(label="Contact us", font=custom_font)
menu.add_cascade(label="About", font=custom_font)

# Frame for adding student details
add_student_frame = tk.Frame(main)
add_student_frame.place(relx=0.5, rely=0.5, anchor='center')

# Labels and Entry fields for adding student details
tk.Label(add_student_frame, text="Name:", font=custom_font).grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(add_student_frame)
name_entry.grid(row=0, column=1)

tk.Label(add_student_frame, text="Address:", font=custom_font).grid(row=1, column=0, sticky='e')
address_entry = tk.Entry(add_student_frame)
address_entry.grid(row=1, column=1)

tk.Label(add_student_frame, text="Class:", font=custom_font).grid(row=2, column=0, sticky='e')
class_entry = tk.Entry(add_student_frame)
class_entry.grid(row=2, column=1)

tk.Label(add_student_frame, text="Gender:", font=custom_font).grid(row=3, column=0, sticky='e')
gender_var = tk.StringVar()
tk.Radiobutton(add_student_frame, text="Male", variable=gender_var, value="Male", font=custom_font).grid(row=3, column=1, sticky='w')


main.mainloop()
