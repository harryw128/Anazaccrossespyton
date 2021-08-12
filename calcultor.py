# Python GUI program to
# add two numbers
# Using Labels, Entry and Button
# widgets - Python 3 tkinter module

from tkinter import *

# Command to add both inputs together
def add_numbers():
    res=int(e1.get())+int(e2.get())
    label_text.set(res)
 
window = Tk()
label_text=StringVar();
Label(window, text="First Number:").grid(row=0)
Label(window, text="Second Number:").grid(row=1)
Label(window, text="Result of Addition:").grid(row=3)
result=Label(window, text="", textvariable=label_text).grid(row=3,column=1)
# Prints out add_number command

# Inputs for both numbers
e1 = Entry(window)
e2 = Entry(window)

# Postion for where entries are
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Button runs add_number command to add both numbers
b = Button(window, text="Calculate", command=add_numbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
