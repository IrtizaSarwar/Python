import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "Irtiza"
VALID_PASSWORD = "iryasaif"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Log-in Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Log-in Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x300")

tk.Label(root, text = "Username: ").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')
username_entry = tk.Entry(root, width = 25)
username_entry.grid(row = 0, column = 1)

tk.Label(root, text = "Password: ").grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'w')
password_entry = tk.Entry(root, width = 25, show = "*")
password_entry.grid(row = 1, column = 1)

login_button = tk.Button(root, text = "Log-in", width = 15, command = login)
login_button.grid(row = 2, column = 1, pady = 20)

root.mainloop()
