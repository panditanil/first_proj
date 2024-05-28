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

# Function to show the home frame
def show_home_frame():
    hide_all_frames()
    home_frame.pack(fill='both', expand=True)

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
main.title("School