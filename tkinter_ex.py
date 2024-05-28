import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window")
root.geometry("400x300")

#Adding label
label = tk.Label(root, text="Hello")
label.pack()

#Adding button 
def submit():
    print("Button clicked")

button = tk.Button(root, text="Submit" , command=submit)
button.pack()

#Adding entry from user

entry = tk.Entry(root)
entry.pack()

#adding text area 
textare = tk.Text(root,height=5, width=40)
textare.pack()

#frame
frame = tk.Frame(root)

#Adding checkbox
check1 = tk.IntVar()
check2 = tk.IntVar()
checkbutton = tk.Checkbutton(frame,text="Check me",variable=check1,height=2, width=10 )
checkbutton2 = tk.Checkbutton(frame, text="Check ", variable=check2)
checkbutton.pack()
checkbutton2.pack()


#Radio button 
radio_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(frame, text="Make",variable=radio_var, value="M")
radiobutton2 = tk.Radiobutton(frame, text="Female",variable=radio_var, value="F")
radiobutton1.pack()
radiobutton2.pack()

frame.pack()


#adding menu 

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

menu.add_cascade(label="Print")
menu.add_cascade(label="Contact Us")
menu.add_cascade(label="About")
root.mainloop()