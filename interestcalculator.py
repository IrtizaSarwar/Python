from tkinter import *

root = Tk()
root.title("Interest Calculator")
root.geometry("300x300")

def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    n = float(time_entry.get())
    interest = p * r * n
    result_label.config(text="Interest: " + str(round(interest, 2)))

title = Label(root, text="Interest Calculator", font=("Arial", 14))
title.pack(pady=10)

principal_label = Label(root, text="Principal")
principal_label.pack()
principal_entry = Entry(root)
principal_entry.pack()

rate_label = Label(root, text="Rate")
rate_label.pack()
rate_entry = Entry(root)
rate_entry.pack()

time_label = Label(root, text="Time")
time_label.pack()
time_entry = Entry(root)
time_entry.pack()

calc_button = Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
