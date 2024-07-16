import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Enter the desired length of the password:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.entry.get().strip())
            if length <= 0:
                messagebox.showwarning("Invalid Length", "Length must be a positive integer.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            self.password_label.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer for length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

