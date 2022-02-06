from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import tkinter
#from tk import *
expression = ""

 
def press(num):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)

def invertNumber():
    global expression
    if expression > 0:
        expression = 0 - expression
        equation.set(expression)
    else:
        expression = expression
        equation.set(expression)
 
def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

window = tkinter.Tk()
window.title("Calculadora do Mari")
window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(1920, 1080)
equation = StringVar()
e = Entry(window, textvariable=equation)
e.grid(columnspan=10, ipadx=50)


labelLeft= tk.Label(window,text = "Choose your favourite month")
popup = Combobox(window,width= 8)
popup['values']= ("Basic","Cientific", "Programing")
popup.current(0)
popup.grid(column=0, row=2)

  
btplus = Button (window, text="+", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press("+")) 
btsub = Button (window, text="-", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press("-")) 
btmult = Button (window, text="*", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press("*")) 
btdiv = Button (window, text="/", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press("/")) 
bt1 = Button (window, text="1", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(1)) 
bt2 = Button (window, text="2", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(2)) 
bt3 = Button (window, text="3", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(3)) 
bt4 = Button (window, text="4", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(4)) 
bt5 = Button (window, text="5", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(5)) 
bt6 = Button (window, text="6", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(6)) 
bt7 = Button (window, text="7", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(7)) 
bt8 = Button (window, text="8", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(8)) 
bt9 = Button (window, text="9", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(9)) 
bt0 = Button (window, text="0", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(0)) 
btsubplus = Button (window, text="+/-", bg="light grey", fg="Black",height= 1,width=7,command=lambda: press(invertNumber()))
btequal = Button (window, text="=", bg="light grey", fg="Black",height= 1,width=7,command=equalpress)
clear = Button(window, text='Clear', bg='light grey', fg='Black',command=clear, height=1, width=7)
bt1.grid (column=1, row=2)
bt2.grid (column=2, row=2)
bt3.grid (column=3, row=2)
bt4.grid (column=1, row=3)
bt5.grid (column=2, row=3)
bt6.grid (column=3, row=3)
bt7.grid (column=1, row=4)
bt8.grid (column=2, row=4)
bt9.grid (column=3, row=4)
bt0.grid (column=2, row=5)
btequal.grid (column=3, row=5)
btplus.grid (column=4, row=2)
btsub.grid (column=4, row=3)
btmult.grid (column=4, row=4)
btdiv.grid (column=4, row=5)
btsubplus.grid(column=1, row=5)
clear.grid(column = 5, row =2)
mainloop()