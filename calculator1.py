#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 05:37:12 2018

@author: admin
"""

from tkinter import *
import math
import parser
from tkinter import messagebox
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
        
def pi():
    global expression
    expression = expression + str(math.pi)
    equation.set(expression)

def pi2():
    global expression
    expression = expression + str(math.tau)
    equation.set(expression)

def exp():
    global expression
    expression = expression + str(math.e)
    equation.set(expression)
root = Tk()
    
root.configure(background="Powder blue")
    
root.title("scientific calculator")
    
root.geometry("320x400")
root.resizable(width = False, height = False)

calc = Frame(root)
calc.grid()
equation = StringVar()

expression_field = Entry(calc, textvariable=equation,bg="powder blue", bd=30,width = 28,justify= LEFT)
expression_field.grid(row=0,column = 0,columnspan=4, pady=1)
equation.set("0")

#txtDisplay = Entry(calc,bg="powder blue", bd=30,width = 28,justify= LEFT)
#txtDisplay.grid(row = 0, column = 0,columnspan=4, pady=1)

#txtDisplay.insert(0,"0")

#creating buttons for standard calculator

btn7 = Button(calc, text= "7",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(7)).grid(row = 2, column =0,pady = 1)
btn8 = Button(calc, text= "8",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(8)).grid(row = 2, column =1,pady = 1)
btn9 = Button(calc, text= "9",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(9)).grid(row = 2, column =2,pady = 1)
btn4 = Button(calc, text= "4",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(4)).grid(row = 3, column =0,pady = 1)
btn5 = Button(calc, text= "5",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(5)).grid(row = 3, column =1,pady = 1)      
btn6 = Button(calc, text= "6",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(6)).grid(row = 3, column =2,pady = 1)
btn1 = Button(calc, text= "1",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(1)).grid(row = 4, column =0,pady = 1)
btn2 = Button(calc, text= "2",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(2)).grid(row = 4, column =1,pady = 1)
btn3 = Button(calc, text= "3",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(3)).grid(row = 4, column =2,pady = 1)
      
      
btnclear = Button(calc, text=chr(67),width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=clear).grid(row = 1, column =0,pady = 1)
btnallclear = Button(calc, text=chr(67)+chr(69),width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 1, column =1,pady = 1)

btnsq = Button(calc, text= "v-",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 1, column =2,pady = 1)
btnadd = Button(calc, text= "+",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press("+")).grid(row = 1, column =3,pady = 1)
btnsub = Button(calc, text= "-",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press("-")).grid(row = 2, column =3,pady = 1)
btnpro = Button(calc, text= "x",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press("*")).grid(row = 3, column =3,pady = 1)
btndiv = Button(calc, text= chr(247),width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda:press("/")).grid(row = 4, column =3,pady = 1)

btnzero = Button(calc, text= "0",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=lambda : press(0)).grid(row = 5, column =0,pady = 1)
btnDot = Button(calc, text= ".",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue", command=lambda : press(".")).grid(row = 5, column =1,pady = 1)
btnPM = Button(calc, text= chr(177),width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 5, column =2,pady = 1)
btnEquals = Button(calc, text= "=",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command=equalpress).grid(row = 5, column =3,pady = 1)

#creating buttons for scientific calculator
btnpi = Button(calc, text= "n",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command= pi).grid(row = 1, column =4,pady = 1)
btncos = Button(calc, text="cos",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 1, column =5,pady = 1)

btnsin = Button(calc, text= "sin",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 1, column =6,pady = 1)
btntan = Button(calc, text= "tan",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 1, column =7,pady = 1)
btn2pi = Button(calc, text= "2n",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command= pi2).grid(row = 2, column =4,pady = 1)
btncosh = Button(calc, text= "cosh",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 2, column =5,pady = 1)
btntanh = Button(calc, text= "tanh",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 2, column =6,pady = 1)

btnsinh = Button(calc, text= "sinh",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 2, column =7,pady = 1)
btnlog = Button(calc, text= "log",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 3, column =4,pady = 1)
btnExp = Button(calc, text= "Exp",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 3, column =5,pady = 1)
btnMod = Button(calc, text= "Mod",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 3, column =6,pady = 1)

btnE = Button(calc, text= "e",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue",command = exp).grid(row = 3, column =7,pady = 1)
btnlog2 = Button(calc, text= "log2",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 4, column =4,pady = 1)
btndeg = Button(calc, text= "deg",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 4, column =5,pady = 1)
btnacosh = Button(calc, text= "acosh",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 4, column =6,pady = 1)
btnasinh = Button(calc, text= "asinh",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 4, column =7,pady = 1)
btnlog10 = Button(calc, text= "log10",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 5, column =4,pady = 1)
btnlog1p = Button(calc, text= "log1p",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 5, column =5,pady = 1)
btnexpn1 = Button(calc, text= "expn1",width =6, height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 5, column =6,pady = 1)
btn1gamma = Button(calc,text = "Igamma",width=6,height=2,font=("arial",20,"bold"),bd=4,bg="powder blue").grid(row = 5,column = 7,pady = 1)

disp = Label(calc, text= "scientific calculator", font=("arial",30,"bold"),justify=CENTER)
disp.grid(row=0,column = 4, columnspan = 4)


#creating menubar

def iExit():
    iExit= tkinter.messagebox.askyesno ("scientific calculator","Are you sure you want to Exit")
    if iExit > 0:
        root.destroy()
        return
def scientific():
     root.geometry("944x560")
     root.resizable(width = False, height = False)       
    
def standard():
     root.geometry("320x400")
     root.resizable(width = False, height = False)       
menu = Menu(calc)

#creating file menu
root.config(menu=menu)
file = Menu(menu,tearoff=0)
file.add_command(label="standard calculator",command = standard)
file.add_command(label = "scientific calculator",command = scientific)
file.add_separator()
file.add_command(label = "quit",command = iExit)
menu.add_cascade(label="File", menu=file)

#creating edit menu

edit = Menu(menu,tearoff=0)
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_separator()
edit.add_command(label="paste")
menu.add_cascade(label="Edit",menu=edit)


root.mainloop()


    
