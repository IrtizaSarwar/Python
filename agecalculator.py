from tkinter import *
from datetime import date

def show_age():
    try:
        d = int(day.get())
        m = int(month.get())
        y = int(year.get())
        birth = date(y, m, d)
        today = date.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        result.config(text=f"You are {age} years old")
    except:
        result.config(text="Please enter a valid date")

root = Tk()
root.title("Age Calculator")

Label(root, text="Day").pack()
day = Entry(root)
day.pack()

Label(root, text="Month").pack()
month = Entry(root)
month.pack()

Label(root, text="Year").pack()
year = Entry(root)
year.pack()

Button(root, text="Calculate", command=show_age).pack()

result = Label(root, text="")
result.pack()

root.mainloop()
