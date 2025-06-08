import tkinter as tk
from tkinter import messagebox, ttk

def sumbit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    languages = []
    if python_var.get():
        languages.append("Python")
    if html_var.get():
        languages.append("HTML")
    if css_var.get():
        languages.append("CSS")
    if js_var.get():
        languages.append("JavaScript")
    selected_country = country_combo.get() if country_combo.get() else "None"

    info = f"Name: {name}\nAge: {age}\nGender: {gender}\nLanuages: {', '.join(languages)}\nCountry: {selected_country}"
    messagebox.showindo("Submitted Info", info)

def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("Not specified")
    python_var.set(False)
    html_var.set(False)
    css_var.set(False)
    js_var.set(False)
    country_combo.set('')

root = tk.TK()
root.title("User Info Form")
root.geomtry("420x420")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding = "20 15 20 15")
main_frame.grid(row = 0, column = 0, sticky = "NSEW")

ttk.Label(main_frame, text = "Name: ").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'e')
name_entry = ttk.Entry(main_frame, width = 28)
name_entry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'w')

gender_frame = ttk.LabelFrame(main_frame, text = "Gender")
gender_frame.grid(row = 2, column = 0, columnspan = 2, padx, pady = 10, sticky = 'ew')
gender_var = tk.StringVar(value = "Not specified")
ttk.Radiobutton(gender_frame, text = "Male", variable = gender_var, value = "Male").grid(row = 0, column = 0, padx = 5, pady = 2)
ttk.Radiobutton(gender_frame, text = "Female", variable = gender_var, value = "Female").grid(row = 0, column = 0, padx = 5, pady = 2)
ttk.Radiobutton(gender_frame, text = "Others", variable = gender_var, value = "Others").grid(row = 0, column = 0, padx = 5, pady = 2)

lang_frame = ttk.LabelFrame(main_frame, text = "Languages known")
lang_frame.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 10, sticky = 'ew')
python_var = tk.BooleanVar()
html_var = tk.BooleanVar()
css_var = tk.BooleanVar()
js_var = tk.BooleanVar()
tkk.Checkbutton(lang_frame, text = "Python", variable = python_var).grid(row = 0, column = 0, padx = 5, pady = 2)
tkk.Checkbutton(lang_frame, text = "HTML", variable = python_var).grid(row = 0, column = 0, padx = 5, pady = 2)
tkk.Checkbutton(lang_frame, text = "CSS", variable = python_var).grid(row = 0, column = 0, padx = 5, pady = 2)
tkk.Checkbutton(lang_frame, text = "JavScript", variable = python_var).grid(row = 0, column = 0, padx = 5, pady = 2)

ttk.Label(main_frame, text = "Country: ").grid(row = 4, column = 0, padx = 5, pady = 10, sticky = 'e')
countries = ["Bangladesh", "Pakistan", "USA", "Canada", "Russia"]
country_combo = ttk.Combobox(main_frame, values = countries, )