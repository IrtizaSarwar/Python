import tkinter as tk
import random

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")

target = random.randint(1, 10)
attempts = 0

def check_guess():
    global attempts
    guess = guess_entry.get()
    if not guess.isdigit():
        feedback_label.config(text="Please enter a number")
        return
    guess_num = int(guess)
    attempts += 1
    if guess_num < target:
        feedback_label.config(text="Too low, try again")
    elif guess_num > target:
        feedback_label.config(text="Too high, try again")
    else:
        feedback_label.config(text=f"You got it in {attempts} tries!")
        guess_btn.config(state="disabled")
        guess_entry.config(state="disabled")

def reset_game():
    global target, attempts
    target = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1 and 10")
    guess_btn.config(state="normal")
    guess_entry.config(state="normal")
    guess_entry.delete(0, tk.END)

tk.Label(root, text="Number Guessing Game").pack(pady=10)
tk.Label(root, text="Guess a number between 1 and 10").pack()
guess_entry = tk.Entry(root)
guess_entry.pack(pady=5)

guess_btn = tk.Button(root, text="Guess", command=check_guess)
guess_btn.pack(pady=5)

feedback_label = tk.Label(root, text="Start guessing...")
feedback_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.pack()

root.mainloop()
