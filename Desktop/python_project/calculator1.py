#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:24:42 2020

@author: admin
"""

from tkinter import *
expression = ""

def press(num):
    global expression
    
    expression = expression + str(num)
    
    equation.set(expression)
    
def equalpress():#function to evaluate the final result
    try:
        global expression
        
        result = str(eval(expression))
        
        equation.set(result)
        
        expression = ""
        
    except:
        
        equation.set("error")
        expression = ""
        
def clear() :#function to clear the content of the screen
        global expression
        expression = ""
        equation.set("")
        

    
root = Tk()
    
root.configure(background="Powder blue")
    
root.title("simple calculator")
    
root.geometry("350x200")


    
equation = StringVar()
    
expression_field = Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
equation.set('enter your expression')
    
btn1 = Button(root,text= ' 1 ',fg= 'black',bg= 'Powder blue',command=lambda: press(1),height=1,width=7 )
btn1.grid(row=2, column=0)

btn2 = Button(root,text= ' 2 ',fg= 'black',bg= 'Powder blue',command=lambda: press(2),height=1,width=7 )
btn2.grid(row=2, column=1)

btn3 = Button(root,text= ' 3 ',fg= 'black',bg= 'Powder blue',command=lambda: press(3),height=1,width=7 )
btn3.grid(row=2, column=2)

btn4 = Button(root,text= ' 4 ',fg= 'black',bg= 'Powder blue',command=lambda: press(4),height=1,width=7 )
btn4.grid(row=3, column=0)

btn5 = Button(root,text= ' 5 ',fg= 'black',bg= 'Powder blue',command=lambda: press(5),height=1,width=7 )
btn5.grid(row=3, column=1)

btn6 = Button(root,text= ' 6 ',fg= 'black',bg= 'Powder blue',command=lambda: press(6),height=1,width=7 )
btn6.grid(row=3, column=2)

btn7 = Button(root,text= ' 7 ',fg= 'black',bg= 'Powder blue',command=lambda: press(7),height=1,width=7 )
btn7.grid(row=4, column=0)

btn8 = Button(root,text= ' 8 ',fg= 'black',bg= 'Powder blue',command=lambda: press(8),height=1,width=7 )
btn8.grid(row=4, column=1)

btn9 = Button(root,text= ' 9 ',fg= 'black',bg= 'Powder blue',command=lambda: press(9),height=1,width=7 )
btn9.grid(row=4, column=2)

btn0 = Button(root,text= ' 0 ',fg= 'black',bg= 'Powder blue',command=lambda: press(0),height=1,width=7 )
btn0.grid(row=5, column=0)

plus = Button(root,text= ' + ',fg= 'black',bg= 'Powder blue',command=lambda: press("+"),height=1,width=7 )
plus.grid(row=2, column=3) 

minus = Button(root,text= ' - ',fg= 'black',bg= 'Powder blue',command=lambda: press("-"),height=1,width=7 )
minus.grid(row=3, column=3)

multiply = Button(root,text= ' * ',fg= 'black',bg= 'Powder blue',command=lambda: press("*"),height=1,width=7 )
multiply.grid(row=4, column=3)

divide = Button(root,text= ' / ',fg= 'black',bg= 'Powder blue',command=lambda: press("/"),height=1,width=7 )
divide.grid(row=5, column=3)

equal = Button(root,text= ' = ',fg= 'black',bg= 'Powder blue',command= equalpress ,height=1,width=7 )
equal.grid(row=5, column=2)

clear = Button(root,text= ' c ',fg= 'black',bg= 'Powder blue',command= clear,height=1,width=7 )
clear.grid(row=5, column=1)             


root.mainloop()