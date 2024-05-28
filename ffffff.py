import tkinter as tk

root = tk.Tk()
root.title("Student Input")

frame1 = tk.Frame(root, width=300, height=100, background='lightblue')
frame1.pack(side="top", fill="both", expand=True)

student1_label = tk.Label(frame1, text="Student 1:")
student1_label.place(x=10, y=20)

student1_entry = tk.Entry(frame1, width=20)
student1_entry.place(x=80, y=20)

frame2 = tk.Frame(root, width=300, height=100, background='lightgreen')
frame2.pack(side="top", fill="both", expand=True)

student2_label = tk.Label(frame2, text="Student 2:")
student2_label.place(x=10, y=20)

student2_entry = tk.Entry(frame2, width=20)
student2_entry.place(x=80, y=20)

root.mainloop()