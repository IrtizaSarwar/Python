import tkinter as tk

def convert():
    inches = entry.get()
    if inches.isdigit():
        cm = float(inches) * 2.54
        result_label.config(text=str(cm) + " cm")
    else:
        result_label.config(text="Please enter a number")

root = tk.Tk()
root.title("Length Converter")

tk.Label(root, text="Inches:").pack()
entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Convert", command=convert)
btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
