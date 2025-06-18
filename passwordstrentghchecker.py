import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)
    if length == 0:
        strength_label.config(text="Please enter a password", fg="gray")
    elif length < 6:
        strength_label.config(text="Weak", fg="red")
    elif length < 10:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x200")
app.config(bg="#1e1e1e")

label = tk.Label(app, text="Enter your password:", font=("Arial", 12), bg="#1e1e1e", fg="white")
label.pack(pady=10)

entry = tk.Entry(app, show="*", font=("Arial", 12), width=30)
entry.pack(pady=5)

check_button = tk.Button(app, text="Check Strength", command=check_strength, font=("Arial", 12), bg="#333", fg="white")
check_button.pack(pady=10)

strength_label = tk.Label(app, text="", font=("Arial", 14, "bold"), bg="#1e1e1e")
strength_label.pack(pady=10)

app.mainloop()
