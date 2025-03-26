import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to handle the password generation and display
def show_password():
    try:
        # Get the length from the entry box
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Length Error", "Password length should be at least 8 characters.")
            return
        
        # Generate password
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")

# Creating the GUI window
root = tk.Tk()
root.title("Complex Password Generator")

# Create UI elements
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=show_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state="readonly", width=30)
password_entry.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
