import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
root.setvar("first_press", 0)


def number_clicked(x):
    print(f"Button {x} clicked!")
    root.setvar("first_press", x)
    display.config(text=str(x))


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


display = tk.Label(root, text="Click a number to start mathing")
display.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

btn0 = tk.Button(root, text="0", command=click0, width=10, height=3)
btn0.grid(row=1, column=0, padx=5, pady=5)

btn1 = tk.Button(root, text="1", command=click1, width=10, height=3)
btn1.grid(row=1, column=1, padx=5, pady=5)

btn2 = tk.Button(root, text="2", command=click2, width=10, height=3)
btn2.grid(row=1, column=2, padx=5, pady=5)

btn3 = tk.Button(root, text="3", command=click3, width=10, height=3)
btn3.grid(row=2, column=0, padx=5, pady=5)

btn4 = tk.Button(root, text="4", command=click4, width=10, height=3)
btn4.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
