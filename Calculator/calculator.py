# Project Calculator Using Tkinter
import parser
from tkinter import *
from tkinter import messagebox

root = Tk()  # tkinter object created
root.title('Calculator')  # added title
root.config(padx=10, pady=10)

# Adding display box
display = Entry(root, bg='#D8D8D8')
display.grid(row=1, columnspan=6, sticky=W + E, pady=10)

# Get user input in the text field
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


# For all clear option
def clear_all():
    display.delete(0, END)


# Undo Operation
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, '0')


# Get Operations
def get_operations(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length


# calculation
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except:
        clear_all()
        display.insert(0, 'Syntax Error')


# Factorial
def factorial():
    x = display.get()
    if x.isnumeric():
        x = int(x)

        def fact(x):
            if x == 1:
                clear_all()
                return 1
            else:
                return x * fact(x - 1)

        clear_all()
        display.insert(0, fact(x))
    else:
        clear_all()
        display.insert(0, 'Error')


# Adding Buttons
Button(root, text='0', width=3, command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text='1', width=3, command=lambda: get_variables(1)).grid(row=4, column=0)
Button(root, text='2', width=3, command=lambda: get_variables(2)).grid(row=4, column=1)
Button(root, text='3', width=3, command=lambda: get_variables(3)).grid(row=4, column=2)
Button(root, text='4', width=3, command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text='5', width=3, command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text='6', width=3, command=lambda: get_variables(6)).grid(row=3, column=2)
Button(root, text='7', width=3, command=lambda: get_variables(7)).grid(row=2, column=0)
Button(root, text='8', width=3, command=lambda: get_variables(8)).grid(row=2, column=1)
Button(root, text='9', width=3, command=lambda: get_variables(9)).grid(row=2, column=2)

Button(root, text='.', width=3, command=lambda: get_operations('.')).grid(row=5, column=0)
Button(root, text='=', width=3, command=lambda: calculate()).grid(row=5, column=2)
Button(root, text='AC', width=3, command=lambda: clear_all()).grid(row=2, column=3)
Button(root, text='(', width=3, command=lambda: get_operations('(')).grid(row=3, column=3)
Button(root, text='+', width=3, command=lambda: get_operations('+')).grid(row=4, column=3)
Button(root, text='-', width=3, command=lambda: get_operations('-')).grid(row=5, column=3)
Button(root, text='/', width=3, command=lambda: get_operations('/')).grid(row=5, column=4)
Button(root, text='x', width=3, command=lambda: get_operations('*')).grid(row=4, column=4)
Button(root, text=')', width=3, command=lambda: get_operations(')')).grid(row=3, column=4)
Button(root, text='<-', width=3, command=lambda: undo()).grid(row=2, column=4)
Button(root, text='%', width=3, command=lambda: get_operations('%')).grid(row=2, column=5)
Button(root, text='exp', width=3, command=lambda: get_operations('**')).grid(row=3, column=5)
Button(root, text='√', width=3, command=lambda: get_operations('*(1/2)')).grid(row=4, column=5)
Button(root, text='!', width=3, command=lambda: factorial()).grid(row=5, column=5)

root.mainloop()
