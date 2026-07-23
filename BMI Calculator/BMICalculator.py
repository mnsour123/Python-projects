import tkinter as tk
from tkinter import ttk, messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Please enter positive numbers.")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("370x350")
root.resizable(False, False)


style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10))


title_label = ttk.Label(root, text="BMI Calculator",
                        font=("Segoe UI", 16, "bold"))
title_label.pack(pady=15)


weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.pack(pady=(5, 0))
weight_entry = ttk.Entry(root, width=20, justify="center")
weight_entry.pack(pady=5)


height_label = ttk.Label(root, text="Height (cm):")
height_label.pack(pady=(5, 0))
height_entry = ttk.Entry(root, width=20, justify="center")
height_entry.pack(pady=5)


button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

calc_button = ttk.Button(button_frame, text="Calculate", command=calculate_bmi)
calc_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)


result_label = ttk.Label(root, text="", font=(
    "Segoe UI", 12, "bold"), justify="center")
result_label.pack(pady=10)

root.mainloop()
