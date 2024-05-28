import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import sqlite3

# Function to initialize the database
def initialize_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        class TEXT,
        fathers_name TEXT,
        mobile TEXT
    )
    ''')
    conn.commit()
    conn.close()

# # Function to show the home frame
# def show_home_frame():
#     hide_all_frames()
#     home_frame.pack(fill='both', expand=True)

# Function to show the add student frame
def show_add_student_frame():
    hide_all_frames()
    add_student_frame.pack(fill='both', expand=True)

# Function to show the student details frame
def show_student_frame():
    hide_all_frames()
    student_listbox.delete(0, tk.END)  # Clear the listbox
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        student_listbox.insert(tk.END, f"{row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]}")
    conn.close()
    show_student_frame.pack(fill='both', expand=True)

# Function to show the delete student frame
def show_delete_student_frame():
    hide_all_frames()
    delete_student_listbox.delete(0, tk.END)  # Clear the listbox
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        delete_student_listbox.insert(tk.END, row[1])
    conn.close()
    delete_student_frame.pack(fill='both', expand=True)

# Function to hide all frames
def hide_all_frames():
    for frame in main.winfo_children():
        frame.pack_forget()

# Function to add a student
def add_student():
    name = name_entry.get()
    address = address_entry.get()
    class_name = class_entry.get()
    fathers_name = fathers_name_entry.get()
    mobile = mobile_entry.get()
    
    if name and address and class_name and fathers_name and mobile:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, address, class, fathers_name, mobile) VALUES (?, ?, ?, ?, ?)",
                       (name, address, class_name, fathers_name, mobile))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully!")
        name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        fathers_name_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to delete a student
def delete_student():
    selected_student = delete_student_listbox.get(tk.ACTIVE)
    if selected_student:
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE name=?", (selected_student,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student deleted successfully!")
        show_delete_student_frame()

# Main application setup
main = tk.Tk()
main.title("School Management System")
main.geometry("1440x900")

# Initialize the database
initialize_db()


# Custom font
custom_font = ("Times New Roman", 15)

# Adding School name
school_name = tk.Label(main, text="Dav School Birgunj", font=("Times New Roman", 30))
school_name.pack()



def go_home():
    hide_all_frames()
    canvas.create_image(0, 0, image=bg_photo, anchor='nw')
    add_student_frame.place_forget() 


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

menu.add_command(label="Home", command=go_home)
menu.add_command(label="Add Student", command=show_add_student_frame)
menu.add_command(label="Show Student", command=show_student_frame)
menu.add_command(label="Delete Student", command=show_delete_student_frame)
menu.add_command(label="About")
menu.add_command(label="Contact Us")

# Home frame
home_frame = tk.Frame(main, width=1440, height=800)
home_label = tk.Label(home_frame, text="Welcome to the School Management System")
home_label.pack(pady=20)

# Add student frame
add_student_frame = tk.Frame(main, width=1440, height=800)
add_student_label = tk.Label(add_student_frame, text="Add Student Form")
add_student_label.pack(pady=10)

name_label = tk.Label(add_student_frame, text="Name:")
name_label.pack()
name_entry = tk.Entry(add_student_frame)
name_entry.pack(pady=5)

address_label = tk.Label(add_student_frame, text="Address:")
address_label.pack()
address_entry = tk.Entry(add_student_frame)
address_entry.pack(pady=5)

class_label = tk.Label(add_student_frame, text="Class:")
class_label.pack()
class_entry = tk.Entry(add_student_frame)
class_entry.pack(pady=5)

fathers_name_label = tk.Label(add_student_frame, text="Father's Name:")
fathers_name_label.pack()
fathers_name_entry = tk.Entry(add_student_frame)
fathers_name_entry.pack(pady=5)

mobile_label = tk.Label(add_student_frame, text="Mobile Number:")
mobile_label.pack()
mobile_entry = tk.Entry(add_student_frame)
mobile_entry.pack(pady=5)

add_button = tk.Button(add_student_frame, text="Add", command=add_student)
add_button.pack(pady=10)

# Show student frame
show_student_frame = tk.Frame(main, width=1440, height=800)
student_listbox = tk.Listbox(show_student_frame, width=100, height=20)
student_listbox.pack(pady=20)
show_student_label = tk.Label(show_student_frame, text="List of Students")
show_student_label.pack()

# Delete student frame
delete_student_frame = tk.Frame(main, width=1440, height=800)
delete_student_listbox = tk.Listbox(delete_student_frame, width=100, height=20)
delete_student_listbox.pack(pady=20)
delete_student_button = tk.Button(delete_student_frame, text="Delete", command=delete_student)
delete_student_button.pack(pady=10)
delete_student_label = tk.Label(delete_student_frame, text="Select a student to delete")
delete_student_label.pack()

# About frame
about_frame = tk.Frame(main, width=1440, height=800)
about_label = tk.Label(about_frame, text="About Us\nThis is a simple school management system application.")
about_label.pack(pady=20)

# Contact Us frame
contact_us_frame = tk.Frame(main, width=1440, height=800)
contact_us_label = tk.Label(contact_us_frame, text="Contact Us\nFor support, contact us at support@school.com.")
contact_us_label.pack(pady=20)

# Show home frame initially
home_frame.pack(fill='both', expand=True)

main.mainloop()
