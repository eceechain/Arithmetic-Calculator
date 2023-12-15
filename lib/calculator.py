from tkinter import *
from tkinter import ttk

def button_press(value):
    global equation_text
    equation_text = equation_text + str(value)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, ZeroDivisionError):
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def delete():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator program")
window.geometry("500x600")
window.configure(bg="black")  

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 30), bg="black", fg="white", width=24, height=2)
label.pack()

frame = Frame(window, bg="black")  
frame.pack()


button_font = ('Arial', 32, 'bold')

style = ttk.Style()
style.configure("DarkBlue.TButton", foreground="white", background="#001f3f", font=button_font, padding=(40, 40)) 

buttons = [
    ttk.Button(frame, text=str(i), style="DarkBlue.TButton", command=lambda i=i: button_press(i))
    for i in range(10)
]


for i, button in enumerate(buttons[:9]):
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)


buttons[0].grid(row=3, column=1, padx=5, pady=5)

operators = ['+', '-', '*', '/']
operator_buttons = [
    ttk.Button(frame, text=op, style="DarkBlue.TButton", command=lambda op=op: button_press(op))
    for op in operators
]

for i, button in enumerate(operator_buttons):
    button.grid(row=i, column=3, padx=5, pady=5)


ttk.Button(frame, text='=', style="DarkBlue.TButton", command=equals).grid(row=3, column=2, padx=5, pady=5)
ttk.Button(frame, text='.', style="DarkBlue.TButton", command=lambda: button_press('.')).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(frame, text='Delete', style="DarkBlue.TButton", command=delete).grid(row=0, column=0, padx=5, pady=5)

clear_button = ttk.Button(window, text='Clear', style="DarkBlue.TButton", command=clear)
clear_button.pack(pady=10)

window.mainloop()
