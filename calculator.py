import tkinter as tk
import math

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_percentage():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result / 100))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_sqrt():
    try:
        result = math.sqrt(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_trig(trig_function):
    try:
        angle = math.radians(float(entry.get()))
        if trig_function == "sin":
            result = math.sin(angle)
        elif trig_function == "cos":
            result = math.cos(angle)
        elif trig_function == "tan":
            result = math.tan(angle)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create the entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Define button symbols
button_symbols = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("=", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("%", 1, 4), ("(", 2, 4), (")", 3, 4),
    ("sin", 1, 5), ("cos", 2, 5), ("tan", 3, 5),
    ("π", 4, 4), ("√", 4, 5)
]

# Create buttons
for symbol, row, col in button_symbols:
    if symbol == "=":
        btn = tk.Button(root, text=symbol, padx=40, pady=20, command=calculate)
    elif symbol == "C":
        btn = tk.Button(root, text=symbol, padx=38, pady=20, command=clear)
    elif symbol == "%":
        btn = tk.Button(root, text=symbol, padx=37, pady=20, command=calculate_percentage)
    elif symbol == "π":
        btn = tk.Button(root, text=symbol, padx=39, pady=20, command=lambda: button_click(str(math.pi)))
    elif symbol == "√":
        btn = tk.Button(root, text=symbol, padx=40, pady=20, command=calculate_sqrt)
    elif symbol in ("sin", "cos", "tan"):
        btn = tk.Button(root, text=symbol, padx=30, pady=20, command=lambda sym=symbol: calculate_trig(sym))
    else:
        btn = tk.Button(root, text=symbol, padx=40, pady=20, command=lambda sym=symbol: button_click(sym))
    btn.grid(row=row, column=col)

root.mainloop()
