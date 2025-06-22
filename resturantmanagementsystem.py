import tkinter as tk
from tkinter import ttk

menu_items = {
    "Burger": 150,
    "Pizza": 250,
    "Pasta": 200,
    "Salad": 100,
    "Momos": 120,
    "RC Cola": 40,
    "Coffee": 20,
}

order_list = []

def add_to_order():
    item = item_select.get()
    quantity = int(quantity_entry.get())
    price = menu_items[item]
    total_price = price * quantity
    order_list.append((item, quantity, total_price))
    order_display.insert(tk.END,f"{item} x {quantity} = {total_price} Taka")
    update_total()

def update_total():
    total = sum(item[2] for item in order_list)
    total_label.config(text = f"Total: {total} Taka")

def clear_order():
    order_list.clear()
    order_display.delete(0, tk.END)
    total_label.cofig(text = "Total: 0 Taka")

root = tk.Tk()
root.title = ("Resturant Management System")
root.geometry("400x500")
root.configure(bg = "white")

title = tk.Label(root, text = "Welcome to Irtiza's Special Kitchen", font=("Poppins", 16, "bold"), bg = "white")
title.pack(pady=10)

frame = tk.Frame(root, bg = "white")
frame.pack()

tk.Label(frame, text = "Select Item: ", bg="white").grid(row=0, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(frame)
quantity_entry.insert(0, "1")
quantity_entry.grid(row=1, column=1)

add_btn = tk.Button(frame, text="Add to Order list", command = add_to_order, bg='white', fg="black")
add_btn.pack(pady=10)

order_display = tk.Listbox(root, width=40, height=10)
order_display.pack(pady=10)

total_label = tk.Label(root, text="Total: 0 Taka", font=("Poppins", 14, "bold"), bg="white")
total_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

root.mainloop()