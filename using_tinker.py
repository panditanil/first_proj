import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
            print(e)
    elif text == "C":
        screen.set("")
    else:
        current_text = screen.get()
        screen.set(current_text + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# StringVar to hold the screen content
screen = tk.StringVar()
screen.set("")

# Create the screen entry
entry = tk.Entry(root, textvar=screen, font='Helvetica 20', bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    b = tk.Button(root, text=button, font='Helvetica 20', padx=20, pady=20)
    b.grid(row=row_val, column=col_val, sticky="nsew")
    b.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
