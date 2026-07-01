import tkinter as tk

root = tk.Tk()

root.title('Calculator')
root.geometry("425x540")
root.resizable(False, False)

expression = ""


def press(key):
    """Add the pressed button to the expression."""
    global expression
    expression += str(key)
    display_var.set(expression)


def clear():
    """Clear the display."""
    global expression
    expression = ""
    display_var.set("")


def backspace():
    """Delete the last character."""
    global expression
    expression = expression[:-1]
    display_var.set(expression)


def equal():
    """Calculate the answer."""
    global expression

    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result

    except:
        display_var.set("Error")
        expression = ""


display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    justify="right",
    bd=10
)

display.grid(row=0, column=0, columnspan=4,
             ipadx=8, ipady=20, padx=10, pady=10)


buttons = [

    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),

]


for (text, row, col) in buttons:

    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=6,
            height=2,
            command=equal
        )

    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=6,
            height=2,
            command=lambda t=text: press(t)
        )

    btn.grid(row=row, column=col, padx=5, pady=5)


clear_button = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    width=13,
    height=2,
    bg="red",
    fg="white",
    command=clear
)

clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


back_button = tk.Button(
    root,
    text="⌫",
    font=("Arial", 18),
    width=13,
    height=2,
    bg="orange",
    command=backspace
)

back_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)


root.mainloop()
