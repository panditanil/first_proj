import tkinter as tk

def show_frame1():
    frame2.pack_forget()
    frame1.pack(fill="both", expand=True)

def show_frame2():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Example")
root.geometry("400x300")

# Frame 1
frame1 = tk.Frame(root)
label1 = tk.Label(frame1, text="Welcome to my project")
label1.grid(row=0, column=0)
button_to_frame2 = tk.Button(frame1, text="Go to Frame 2", command=show_frame2)
button_to_frame2.grid(row=1, column=0)

text = tk.Entry(frame1)
text.grid(row=2, column=0)
text = tk.Entry(frame1)
text.grid(row=2, column=0)

# Frame 2
frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="2nd label")
label2.grid(row=0, column=0)
button_to_frame1 = tk.Button(frame2, text="Go to Frame 1", command=show_frame1)
button_to_frame1.grid(row=1, column=0)

text1 = tk.Entry(frame2)
text1.grid(row=2, column=0)
text12 = tk.Entry(frame2)
text12.grid(row=2, column=1)

# Initially show Frame 1
frame1.pack(fill="both", expand=True)

root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.title("Example")
# root.geometry("400x300")

# label = tk.Label(root,text="Welcome to my project")
# label.grid(row=0,column=1)

# text1 = tk.Entry(root)
# text1.grid(row=0, column=2)

# label1 = tk.Label(root,text="2nd label")
# label1.grid(row=0,column=2)

# root.mainloop()  