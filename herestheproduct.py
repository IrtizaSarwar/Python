from tkinter import *

def multiply_numbers():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    product = number1 * number2
    result_label.config(text="Answer: " + str(product))

window = Tk()
window.title("Multiply Two Numbers")

Label(window, text="Number 1:").pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text="Number 2:").pack()
entry2 = Entry(window)
entry2.pack()

Button(window, text="Multiply", command=multiply_numbers).pack()

result_label = Label(window, text="Answer: ")
result_label.pack()

window.mainloop()
