import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import sqlite3



root = tk.Tk()
root.title("School Management System")
root.geometry("1440x900")

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

def home_screen():
    add_student_frame.pack_forget()
    frame1.pack(fill="both", expand=True)

def show_add_student_frame():
    frame1.pack_forget()
    add_student_frame.pack(fill='both', expand=True)

def show_student_frame():
    hide_all_frames()
    add_student_frame.pack(fill='both', expand=True)

# def show_frame2():
#     frame1.pack_forget()
#     frame2.pack(fill="both", expand=True)

# Load and resize the image
bg_image = Image.open(r"C:\Users\Anil Pandit\Desktop\nclass\myproject\first_proj\image\school.jpg")
bg_image_resized = bg_image.resize((1440, 800))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

#Custom Font and size

custom_font = ("Times New Roman", 15)  



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


# Function to hide all frames
def hide_all_frames():
    for frame in root.winfo_children():
        frame.pack_forget()

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


# Show student frame
show_student_frame = tk.Frame(root, width=1440, height=800)
student_listbox = tk.Listbox(show_student_frame, width=100, height=20)
student_listbox.pack(pady=20)
show_student_label = tk.Label(show_student_frame, text="List of Students")
show_student_label.pack()



#Creating Menu
menu = tk.Menu(root, font=custom_font)
root.config(menu=menu)
file_menu = tk.Menu(menu, font=custom_font)
menu.add_command(label="Home", command=home_screen)
menu.add_cascade(label="Student", menu=file_menu)
file_menu.add_command(label="Add Student", command=show_add_student_frame)
file_menu.add_command(label="Show Student", command=show_student_frame)
file_menu.add_command(label="Delete Student")

menu.add_command(label="Exit", command=root.quit)


# Frame 1
frame1 = tk.Frame(root)
frame1.pack(fill="both", expand=True)

canvas = tk.Canvas(frame1, width=1440, height=800)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor='nw')

label1 = tk.Label(frame1, text="DAV School Birgunj", bg="lightgrey", font= ("Times New Roman", 40))
label1.place(x=430, y=50)






# Add student frame
add_student_frame = tk.Frame(root, width=1440, height=800)
# add_student_label = tk.Label(add_student_frame, text="Add Student Form")
# add_student_label.grid(row=0,column=0)

name_label = tk.Label(add_student_frame, text="Name:")
name_label.grid(row=0,column=5)
name_entry = tk.Entry(add_student_frame)
name_entry.grid(row=1,column=5)

address_label = tk.Label(add_student_frame, text="Address:")
address_label.grid(row=0,column=6)
address_entry = tk.Entry(add_student_frame)
address_entry.grid(row=1,column=6)

class_label = tk.Label(add_student_frame, text="Class:")
class_label.grid(row=0,column=7)
class_entry = tk.Entry(add_student_frame)
class_entry.grid(row=1,column=7)

fathers_name_label = tk.Label(add_student_frame, text="Father's Name:")
fathers_name_label.grid(row=0,column=8)
fathers_name_entry = tk.Entry(add_student_frame)
fathers_name_entry.grid(row=1,column=8)

mobile_label = tk.Label(add_student_frame, text="Mobile Number:")
mobile_label.grid(row=0,column=9)
mobile_entry = tk.Entry(add_student_frame)
mobile_entry.grid(row=1,column=9)

add_button = tk.Button(add_student_frame, text="Add", command=add_student)
add_button.grid(row=1,column=10)



# Initially show Frame 1
frame1.pack(fill="both", expand=True)

root.mainloop()