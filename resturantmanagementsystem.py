import tkinter as tk
from tkinter import ttk

menu_items = {
    "Burger": 150,
    "Pizza": 250,
    "Pasta": 200,
    "Fries": 100,
    "Sprite": 40,
    "Coffee": 60
}

order_list = []

def add_to_order():
    item = item_select.get()
    qty = int(qty_entry.get())
    price = menu_items[item]
    total_price = price * qty
    order_list.append((item, qty, total_price))
    order_display.insert(tk.END, f"{item} x{qty} = Tk {total_price}")
    update_total()

def update_total():
    total = sum(item[2] for item in order_list)
    total_label.config(text=f"Total: Tk {total}")

def clear_order():
    order_list.clear()
    order_display.delete(0, tk.END)
    total_label.config(text="Total: Tk 0")

root = tk.Tk()
root.title("Restaurant Order App")
root.geometry("400x500")
root.config(bg="#f2f2f2")


title = tk.Label(root, text="Welcome to Irtiza's Kitchen", font=("Poppins", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

tk.Label(frame, text="Select Item:", bg="#f2f2f2").grid(row=0, column=0, padx=10, pady=5)
item_select = ttk.Combobox(frame, values=list(menu_items.keys()))
item_select.current(0)
item_select.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Quantity:", bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5)
qty_entry = tk.Entry(frame)
qty_entry.insert(0, "1")
qty_entry.grid(row=1, column=1)

add_btn = tk.Button(root, text="Add to Order", command=add_to_order, bg="#4CAF50", fg="white")
add_btn.pack(pady=10)

order_display = tk.Listbox(root, width=40, height=10)
order_display.pack(pady=10)

total_label = tk.Label(root, text="Total: Tk 0", font=("Helvetica", 14, "bold"), bg="#f2f2f2")
total_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_order, bg="#f44336", fg="white", width=10)
clear_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.destroy, bg="#555555", fg="white", width=10)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
