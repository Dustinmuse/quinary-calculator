import tkinter as tk
import basic_operations as bo
import advanced_operations as ao
import quinary_logic as ql

root = tk.Tk()
root.title("My First Tkinter App")
root.setvar("first_press", "")
root.setvar("second_press", "")
root.setvar("quinaryDisplay", True)  # Initialize to True (quinary mode by default)
root.setvar("solution", "0")  # Store the actual quinary solution
ql = ql.QuinaryCalculator()


def number_clicked(x):
    print(f"Button {x} clicked!")
    print(root.getvar("first_press"))
    if root.getvar("first_press") == "":
        root.setvar("first_press", x)
        display.config(text=str(x))
    else:
        root.setvar("second_press", x)
        display.config(
            text=str(root.getvar("first_press"))
            + " "
            + str(root.getvar("operation"))
            + " "
            + str(x)
        )


# One handler per button (manual wiring)
def click0():
    number_clicked(0)


def click1():
    number_clicked(1)


def click2():
    number_clicked(2)


def click3():
    number_clicked(3)


def click4():
    number_clicked(4)


def click_add():
    print("Add operation selected!")
    root.setvar("operation", "+")
    display.config(text=str(root.getvar("first_press")) + " + ")


def click_sub():
    print("Subtract operation selected!")
    root.setvar("operation", "-")
    display.config(text=str(root.getvar("first_press")) + " - ")


def click_div():
    print("Divide operation selected!")
    root.setvar("operation", "/")
    display.config(text=str(root.getvar("first_press")) + " / ")


def click_mul():
    print("Multiply operation selected!")
    root.setvar("operation", "*")
    display.config(text=str(root.getvar("first_press")) + " * ")


def click_sqr():
    print("Square operation selected!")
    root.setvar("operation", "^2")
    display.config(text=str(root.getvar("first_press")) + "^2")


def click_sqr_root():
    print("Square root operation selected!")
    display.config(text=str(root.getvar("first_press")) + "√")
    root.setvar("operation", "√")


def click_clear():
    print("Memory Cleared!")
    root.setvar("first_press", "")
    root.setvar("second_press", "")
    root.setvar("operation", "")
    root.setvar("solution", "0")
    root.setvar("quinaryDisplay", True)
    display.config(text="")


def click_eql():
    x1_raw = root.getvar("first_press")
    x2_raw = root.getvar("second_press")
    op = root.getvar("operation")

    # Normalize empties
    x1 = None if x1_raw in (None, "") else int(x1_raw)
    x2 = None if x2_raw in (None, "") else int(x2_raw)

    val = "Error"
    if op in (None, ""):
        val = "Select operation"
    elif op in ("^2", "√"):
        if x1 is None:
            val = "Select operands"
        elif op == "^2":
            val = ao.square(x1)
        else:
            val = ao.square_root(x1)
    else:
        if x1 is None or x2 is None:
            val = "Select operands"
        elif op == "+":
            val = bo.add(x1, x2)
        elif op == "-":
            val = bo.subtract(x1, x2)
        elif op == "*":
            val = bo.multiply(x1, x2)
        elif op == "/":
            val = bo.divide(x1, x2)
        else:
            val = "Select operation"
    # Clear the variables for next calculation
    root.setvar("first_press", "")
    root.setvar("second_press", "")
    root.setvar("operation", "")
    # Store the solution as quinary (operations already return quinary)
    root.setvar("solution", val)

    # Display the result according to current mode
    if root.getvar("quinaryDisplay") == True:
        # Quinary mode: show quinary directly
        display.config(text=str(val))
    else:
        # Decimal mode: convert quinary to decimal for display
        if val not in ["Error", "Select operands", "Select operation"]:
            display.config(text=str(ql.quinary_to_decimal(int(val))))
        else:
            display.config(text=str(val))


def click_toggle():
    # Get the stored solution (which is in quinary format)
    quinary_solution = root.getvar("solution")
    if quinary_solution is None or quinary_solution == "":
        quinary_solution = "0"

    if root.getvar("quinaryDisplay") == True:
        # Currently in quinary mode, switch to decimal
        root.setvar("quinaryDisplay", False)
        print("Switched to Decimal")
        # Convert quinary to decimal for display
        if quinary_solution not in ["Error", "Select operands", "Select operation"]:
            decimal_value = ql.quinary_to_decimal(int(quinary_solution))
            display.config(text=str(decimal_value))
        else:
            display.config(text=str(quinary_solution))
    else:
        # Currently in decimal mode, switch to quinary
        root.setvar("quinaryDisplay", True)
        print("Switched to Quinary")
        # Display the stored quinary value directly
        display.config(text=str(quinary_solution))


display = tk.Label(root, text="Click a number to start mathing")
display.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

btn0 = tk.Button(root, text="0", command=click0, width=10, height=3)
btn0.grid(row=1, column=0, padx=5, pady=5)

btn1 = tk.Button(root, text="1", command=click1, width=10, height=3)
btn1.grid(row=1, column=1, padx=5, pady=5)

btn2 = tk.Button(root, text="2", command=click2, width=10, height=3)
btn2.grid(row=2, column=0, padx=5, pady=5)

btn3 = tk.Button(root, text="3", command=click3, width=10, height=3)
btn3.grid(row=2, column=1, padx=5, pady=5)

btn4 = tk.Button(root, text="4", command=click4, width=10, height=3)
btn4.grid(row=3, column=0, padx=5, pady=5)

add_btn = tk.Button(root, text="+", command=click_add, width=10, height=3)
add_btn.grid(row=1, column=3, padx=5, pady=5)

sub_btn = tk.Button(root, text="-", command=click_sub, width=10, height=3)
sub_btn.grid(row=1, column=4, padx=5, pady=5)

div_btn = tk.Button(root, text="/", command=click_div, width=10, height=3)
div_btn.grid(row=2, column=3, padx=5, pady=5)

mul_btn = tk.Button(root, text="*", command=click_mul, width=10, height=3)
mul_btn.grid(row=2, column=4, padx=5, pady=5)

eql_btn = tk.Button(root, text="=", command=click_eql, width=10, height=3)
eql_btn.grid(row=2, column=3, padx=5, pady=5)

sqr_btn = tk.Button(root, text="^2", command=click_sqr, width=10, height=3)
sqr_btn.grid(row=3, column=3, padx=5, pady=5)

sqr_root_btn = tk.Button(root, text="√", command=click_sqr_root, width=10, height=3)
sqr_root_btn.grid(row=3, column=4, padx=5, pady=5)

clear_btn = tk.Button(root, text="C", command=click_clear, width=8, height=3)
clear_btn.grid(row=3, column=2, padx=5, pady=5)

toggle_btn = tk.Button(root, text="Toggle", command=click_toggle, width=8, height=3)
toggle_btn.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
