import tkinter as tk
from tkinter import messagebox

DENOMINATIONS = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

COLOR_MAP = {
    1000: "#6B5E7D",
    500: "#9E4244",
    200: "#B9A672",
    100: "#3D877C",
    50: "#DA4A91",
    20: "#C5D86D",
    10: "#F4A941",  # Fixed invalid hex color (added missing digit)
    5: "#F4A941",
    2: "#B9A672",
    1: "#9E4244"
}

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        if amount < 10:
            raise ValueError("Amount must be at least 10.")
        remaining = amount
        for widget in frame_result.winfo_children():
            widget.destroy()
        for note in DENOMINATIONS:
            count = remaining // note
            remaining %= note
            if count > 0:
                label = tk.Label(
                    frame_result,
                    text=f"{note} Taka x {count} = {note * count} Taka",
                    bg=COLOR_MAP[note],
                    fg="black",
                    font=("Arial", 12, "bold"),
                    width=30
                )
                label.pack(pady=3)
        if remaining > 0:
            tk.Label(
                frame_result,
                text=f"Remaining: {remaining} Taka (No matching notes)",
                fg="red",
                font=("Arial", 11, "italic"),
                bg="#f0f8ff"
            ).pack(pady=5)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x500")
root.config(bg="#f0f8ff")

tk.Label(
    root,
    text="Taka Denominator",
    font=("Arial", 16, "bold"),
    fg="#24f4f4",
    bg="#f0f8ff"
).pack(pady=15)

tk.Label(
    root,
    text="Enter amount in taka: ",
    font=("Arial", 12),
    bg="#f0f8ff"
).pack()

entry_amount = tk.Entry(root, font=("Arial", 12), justify="center")
entry_amount.pack(pady=10)

btn_calculate = tk.Button(
    root,
    text="Calculate Notes",
    font=("Arial", 12, "bold"),
    bg="#4682b4",
    fg="white",
    command=calculate_denominations
)
btn_calculate.pack(pady=10)

frame_result = tk.Frame(root, bg="#f0f8ff", bd=2, relief="ridge")
frame_result.pack(pady=10, fill="both", expand=True)

root.mainloop()
