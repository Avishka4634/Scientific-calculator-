from tkinter import *
from tkinter import ttk
import math

window1 = Tk()
window1.title("My Scientific Calculator")
window1.geometry("590x820")
window1.configure(bg="#2C3E50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10, background="#3498DB", foreground="white")
style.configure("TLabel", font=("Arial", 16), background="#2C3E50", foreground="white")
style.configure("TEntry", font=("Arial", 16), padding=5)

label1 = Label(window1, text=" My Scientific Calculator ", font=('Arial', 30), bg="#2C3E50", fg="#ECF0F1")
label1.grid(row=0, column=0, columnspan=4, pady=20)

label2 = Label(window1, text="Number 1: ", font=('Arial', 20), bg="#2C3E50", fg="#ECF0F1")
label2.grid(row=1, column=0, pady=10)
text1 = Text(window1, height=1, width=10, font=('Arial', 20))
text1.grid(row=1, column=1, pady=10)

label3 = Label(window1, text="Number 2: ", font=('Arial', 20), bg="#2C3E50", fg="#ECF0F1")
label3.grid(row=2, column=0, pady=10)
text2 = Text(window1, height=1, width=10, font=('Arial', 20))
text2.grid(row=2, column=1, pady=10)

result_label = Label(window1, text="Result: ", font=('Arial', 20), bg="#2C3E50", fg="#ECF0F1")
result_label.grid(row=3, column=0, columnspan=2, pady=20)


def display_result(result):
    result_label.config(text="Result: " + str(result))

def clear_fields():
    text1.delete("1.0", "end")
    text2.delete("1.0", "end")
    result_label.config(text="Result: ")
    
def add():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    display_result(x + y)

def sub():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    display_result(x - y)

def multiply():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    display_result(x * y)

def divide():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    if y != 0:
        display_result(x / y)
    else:
        display_result("Error (Div by 0)")

def power():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    display_result(x ** y)

def remainder():
    x = float(text1.get("1.0", "end-1c"))
    y = float(text2.get("1.0", "end-1c"))
    display_result(x % y)

def sin_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.sin(math.radians(x)))

def cos_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.cos(math.radians(x)))

def tan_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.tan(math.radians(x)))

def log_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.log10(x))

def ln_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.log(x))

def sqrt_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.sqrt(x))

def asin_func():
    x = float(text1.get("1.0", "end-1c"))
    if -1 <= x <= 1:
        display_result(math.degrees(math.asin(x)))
    else:
        display_result("Error (out of range)")

def acos_func():
    x = float(text1.get("1.0", "end-1c"))
    if -1 <= x <= 1:
        display_result(math.degrees(math.acos(x)))
    else:
        display_result("Error (out of range)")

def atan_func():
    x = float(text1.get("1.0", "end-1c"))
    display_result(math.degrees(math.atan(x)))


buttons = [
    ('Add', add), ('Subtract', sub), ('Multiply', multiply), ('Divide', divide),
    ('Power', power), ('Remainder', remainder),
    ('Sqrt', sqrt_func), ('Log', log_func), ('Ln', ln_func), 
    ('Sin', sin_func), ('Cos', cos_func), ('Tan', tan_func),
    ('Inverse_sin', asin_func), ('Inverse_cos', acos_func), ('Inverse_tan', atan_func),
]


row = 4
col = 0
for (text, command) in buttons:
    button = Button(window1, text=text, command=command, height=2, width=15, font=('Arial', 15))
    button.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 2:
        col = 0
        row += 1


clear_button = Button(window1, text="Clear", command=clear_fields, height=2, width=10, font=('Arial', 15))
clear_button.grid(row=row, column=0, columnspan=3, pady=20)


window1.mainloop()