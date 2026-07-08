import tkinter as tk
from tkinter import ttk

# ---------- Conversion functions ----------


def convert_length(value, from_u, to_u):
    to_meters = {"Meters": 1, "Kilometers": 1000,
                 "Miles": 1609.34, "Feet": 0.3048}
    meters = value * to_meters[from_u]
    return meters / to_meters[to_u]


def convert_weight(value, from_u, to_u):
    to_grams = {"Kilograms": 1000, "Pounds": 453.592,
                "Grams": 1, "Ounces": 28.3495}
    grams = value * to_grams[from_u]
    return grams / to_grams[to_u]


def convert_temperature(value, from_u, to_u):
    if from_u == to_u:
        return value
    if from_u == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_u == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value

    if to_u == "Fahrenheit":
        return celsius * 9/5 + 32
    elif to_u == "Kelvin":
        return celsius + 273.15
    else:
        return celsius


# ---------- Main app ----------
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.resizable(False, False)

units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Pounds", "Grams", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

category_var = tk.StringVar(value="Length")
from_var = tk.StringVar()
to_var = tk.StringVar()
result_var = tk.StringVar(value="Result: ")


def update_units(*args):
    unit_list = units[category_var.get()]
    from_menu["values"] = unit_list
    to_menu["values"] = unit_list
    from_var.set(unit_list[0])
    to_var.set(unit_list[1])


def do_convert():
    try:
        value = float(entry_value.get())
    except ValueError:
        result_var.set("Enter a valid number!")
        return

    cat = category_var.get()
    f, t = from_var.get(), to_var.get()

    if cat == "Length":
        result = convert_length(value, f, t)
    elif cat == "Weight":
        result = convert_weight(value, f, t)
    else:
        result = convert_temperature(value, f, t)

    result_var.set(f"Result: {result:.4f} {t}")


category_menu = ttk.Combobox(root, textvariable=category_var,
                             values=list(units.keys()), state="readonly")
category_menu.pack(pady=10)
category_menu.bind("<<ComboboxSelected>>", update_units)

entry_value = tk.Entry(root, font=("Arial", 14))
entry_value.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

from_menu = ttk.Combobox(frame, textvariable=from_var,
                         state="readonly", width=12)
from_menu.grid(row=0, column=0, padx=5)

tk.Label(frame, text="→").grid(row=0, column=1)

to_menu = ttk.Combobox(frame, textvariable=to_var, state="readonly", width=12)
to_menu.grid(row=0, column=2, padx=5)

update_units()

convert_btn = tk.Button(root, text="Convert", command=do_convert,
                        bg="#4CAF50", fg="white", font=("Arial", 12))
convert_btn.pack(pady=10)

result_label = tk.Label(root, textvariable=result_var,
                        font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
