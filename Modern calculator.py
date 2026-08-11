import tkinter as tk

# -----------------------------
# Calculator Window
# -----------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("360x560")
root.resizable(False, False)
root.configure(bg="#000000")

# -----------------------------
# Variables
# -----------------------------
expression = ""

# -----------------------------
# Display
# -----------------------------
display = tk.Label(
    root,
    text="0",
    font=("Arial", 48),
    bg="#000000",
    fg="white",
    anchor="e",
    padx=20
)

display.pack(fill="both", expand=True, pady=(20, 10))


# -----------------------------
# Functions
# -----------------------------
def update_display(value):
    global expression

    if expression == "0":
        expression = ""

    expression += str(value)

    display.config(text=expression)


def clear():
    global expression
    expression = ""
    display.config(text="0")


def calculate():
    global expression

    try:
        # Replace Apple-style symbols with Python operators
        calculation = expression.replace("×", "*")
        calculation = calculation.replace("÷", "/")

        result = eval(calculation)

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        expression = str(result)
        display.config(text=expression)

    except:
        expression = ""
        display.config(text="Error")


def percentage():
    global expression

    try:
        result = float(expression) / 100

        if result.is_integer():
            result = int(result)

        expression = str(result)
        display.config(text=expression)

    except:
        display.config(text="Error")


def backspace():
    global expression

    expression = expression[:-1]

    if expression == "":
        display.config(text="0")
    else:
        display.config(text=expression)


# -----------------------------
# Button Styling
# -----------------------------
button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(padx=10, pady=10)

number_bg = "#333333"
function_bg = "#A5A5A5"
operator_bg = "#FF9500"

number_fg = "white"
function_fg = "black"
operator_fg = "white"


def create_button(text, row, column, bg, fg, command, colspan=1):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        relief="flat",
        command=command,
        width=4,
        height=1
    )

    button.grid(
        row=row,
        column=column,
        columnspan=colspan,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    return button

# -----------------------------
# Calculator Buttons
# -----------------------------

# Row 1
create_button("AC", 0, 0, function_bg, function_fg, clear)
create_button("%", 0, 1, function_bg, function_fg, percentage)
create_button("⌫", 0, 2, function_bg, function_fg, backspace)
create_button("÷", 0, 3, operator_bg, operator_fg,
              lambda: update_display("÷"))

# Row 2
create_button("7", 1, 0, number_bg, number_fg, lambda: update_display("7"))
create_button("8", 1, 1, number_bg, number_fg, lambda: update_display("8"))
create_button("9", 1, 2, number_bg, number_fg, lambda: update_display("9"))
create_button("×", 1, 3, operator_bg, operator_fg,
              lambda: update_display("×"))

# Row 3
create_button("4", 2, 0, number_bg, number_fg, lambda: update_display("4"))
create_button("5", 2, 1, number_bg, number_fg, lambda: update_display("5"))
create_button("6", 2, 2, number_bg, number_fg, lambda: update_display("6"))
create_button("−", 2, 3, operator_bg, operator_fg,
              lambda: update_display("-"))

# Row 4
create_button("1", 3, 0, number_bg, number_fg, lambda: update_display("1"))
create_button("2", 3, 1, number_bg, number_fg, lambda: update_display("2"))
create_button("3", 3, 2, number_bg, number_fg, lambda: update_display("3"))
create_button("+", 3, 3, operator_bg, operator_fg,
              lambda: update_display("+"))

# Row 5
create_button("0", 4, 0, number_bg, number_fg,
              lambda: update_display("0"), colspan=2)

create_button(".", 4, 2, number_bg, number_fg,
              lambda: update_display("."))

create_button("=", 4, 3, operator_bg, operator_fg, calculate)


# -----------------------------
# Keyboard Support
# -----------------------------
def keyboard_input(event):
    key = event.char

    if key in "0123456789.+-*/":
        if key == "*":
            update_display("×")
        elif key == "/":
            update_display("÷")
        else:
            update_display(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "Escape":
        clear()

    elif event.keysym == "BackSpace":
        backspace()


root.bind("<Key>", keyboard_input)


# -----------------------------
# Start Calculator
# -----------------------------
root.mainloop()