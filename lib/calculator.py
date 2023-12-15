from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator program")
window.geometry("500x600")
window.configure(bg="#f2f2f2") 

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window, bg="#666666") 
frame.pack()

button_font = ('Arial', 18, 'bold')

buttons = [
    Button(frame, text=str(i), height=4, width=9, font=button_font, command=lambda i=i: button_press(i))
    for i in range(10)
]

for i, button in enumerate(buttons[:9]):
    button.grid(row=i // 3, column=i % 3)

buttons[0].grid(row=3, column=1)

operators = ['+', '-', 'x', '/']
operator_buttons = [
    Button(frame, text=op, height=4, width=9, font=button_font, command=lambda op=op: button_press(op))
    for op in operators
]

for i, button in enumerate(operator_buttons):
    button.grid(row=i, column=3)

Button(frame, text='=', height=4, width=9, font=button_font, command=equals).grid(row=3, column=2)
Button(frame, text='.', height=4, width=9, font=button_font, command=lambda: button_press('.')).grid(row=3, column=0)

clear_button = Button(window, text='Clear', height=4, width=15, font=button_font, command=clear)
clear_button.pack()

window.mainloop()
