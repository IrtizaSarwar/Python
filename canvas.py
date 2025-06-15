import tkinter as tk

win = tk.Tk()
win.title("Doodle Board 2.0")
win.geometry("900x650")

current_color = "black"
brush_size = 10
drawing = False
last_x, last_y = None, None

canvas = tk.Canvas(win, bg="white")
canvas.pack(fill="both", expand=True)

def set_color(c):
    global current_color
    current_color = c

def use_eraser():
    global current_color
    current_color = "white"

def clear_canvas():
    canvas.delete("all")

def start_draw(e):
    global drawing, last_x, last_y
    drawing = True
    last_x, last_y = e.x, e.y

def stop_draw(e):
    global drawing
    drawing = False

def draw(e):
    global last_x, last_y
    if drawing:
        canvas.create_line(last_x, last_y, e.x, e.y,
                           fill=current_color, width=brush_size,
                           capstyle=tk.ROUND, smooth=True)
        last_x, last_y = e.x, e.y

canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

toolbar = tk.Frame(win, bg="#ddd")
toolbar.pack(side="top", fill="x")

colors = ["black", "red", "green", "blue", "purple", "orange"]

for color in colors:
    btn = tk.Button(toolbar, bg=color, width=3, command=lambda c=color: set_color(c))
    btn.pack(side="left", padx=2)

eraser_btn = tk.Button(toolbar, text="Eraser", command=use_eraser)
eraser_btn.pack(side="left", padx=10)

clear_btn = tk.Button(toolbar, text="Clear All", command=clear_canvas)
clear_btn.pack(side="right", padx=10)

win.mainloop()
