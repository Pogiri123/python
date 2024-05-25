import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate():
    length = int(length_entry.get())
    password = generate_password(length)
    password_display.config(text=password)


root = tk.Tk()
root.title("Password Generator")
root.configure(bg="black")

heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16), fg="yellow", bg="black")
heading_label.pack(pady=10)

length_label = tk.Label(root, text="Enter password length:", font=("Helvetica", 12), fg="white", bg="black")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate, bg="blue", fg="white")
generate_button.pack(pady=5)

password_display = tk.Label(root, text="", font=("Helvetica", 14), bg="white", padx=10, pady=5)
password_display.pack(pady=10)

root.mainloop()
