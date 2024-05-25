import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")
current_input = ''

def button_click(value):
    global current_input
    current_input += str(value)
    entry_var.set(current_input)

def clear():
    global current_input
    current_input = ''
    entry_var.set('')

def calculate():
    global current_input
    try:
        result = eval(current_input)
        entry_var.set(result)
        current_input = str(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid input")
        clear()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="black", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

def create_button(text, row, col, command, bg_color, fg_color):
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=command, bg=bg_color, fg=fg_color, relief='flat')
    button.grid(row=row, column=col, sticky="nsew")

for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, calculate, "#4CAF50", "white")
    elif text in ('+', '-', '*', '/'):
        create_button(text, row, col, lambda t=text: button_click(t), "#E0E0E0", "black")
    else:
        create_button(text, row, col, lambda t=text: button_click(t), "#E0E0E0", "black")


clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear, bg="#FFC107", fg="white", relief='flat')
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
