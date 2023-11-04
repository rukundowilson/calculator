import tkinter as tk
from tkinter import *

def button_press(num):
    global equation_text
    equation_text=equation_text+str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    total=str(eval(equation_text))
    equation_label1.set(total)
    equation_text=total
def clear():
    global equation_text
    equation_label.set('')
    equation_label1.set('')
    equation_text=' '

root=Tk()
root.title('rukundo.dev')
root.geometry('500x500')
header=Label(text='rukundo.dev calculator',font=('timesnewroman',12))
header.pack()
try:
    equation_text=""
    equation_label=StringVar()
    equation_label1=StringVar()
except ArithmeticError:
    equation_text=''
    equation_label=StringVar('XXXX from rukundo.dev')
    equation_label1=StringVar()
    equation_label1.set('Arithematic error.')
    equation_text=''


# ---text field ----

textarea=Label(master=root, textvariable=equation_label,height=5, width=30, bg='white',font=('arial',13))
textarea.pack()
textarea2=Label(master=root,textvariable=equation_label1, height=2, width=15, bg='white',font=('arial',13))
textarea2.pack()

# ---- buttons ----
frm=Frame(root)
frm.pack()

btn1=tk.Button(frm , text='1', height=3,width=7, command=lambda:button_press(1))
btn1.grid(row=0, column=0)

btn2=tk.Button(frm , text='2', height=3,width=7, command=lambda:button_press(2))
btn2.grid(row=0 ,column=1)
btn3=tk.Button(frm , text='3', height=3,width=7, command=lambda:button_press(3))
btn3.grid(row=0 ,column=2)
btn4=tk.Button(frm , text='4', height=3,width=7, command=lambda:button_press(4))
btn4.grid(row=1,column=0)
btn5=tk.Button(frm , text='5', height=3,width=7, command=lambda:button_press(5))
btn5.grid(row=1,column=1)
btn6=tk.Button(frm , text=6, height=3,width=7, command=lambda:button_press(6))
btn6.grid(row=1,column=2)
btn7=tk.Button(frm , text='7', height=3,width=7, command=lambda:button_press(7))
btn7.grid(row=2,column=0)
btn8=tk.Button(frm , text='8', height=3,width=7, command=lambda:button_press(8))
btn8.grid(row=2,column=1)
btn9=tk.Button(frm , text='9', height=3,width=7, command=lambda:button_press(9))
btn9.grid(row=2,column=2)
btn0=tk.Button(frm , text='0', height=3,width=7, command=lambda:button_press(0))
btn0.grid(row=3,column=0)
btndot=tk.Button(frm , text='.', height=3,width=7, command=lambda:button_press('.'))
btndot.grid(row=3,column=1)
btnE=tk.Button(frm , text='=', height=3,width=7, command=equals)
btnE.grid(row=3,column=2)
btnP=tk.Button(frm , text='+', height=3,width=7, command=lambda:button_press('+'))
btnP.grid(row=0,column=3)
btnM=tk.Button(frm , text='-', height=3,width=7, command=lambda:button_press('-'))
btnM.grid(row=1,column=3)
btnT=tk.Button(frm , text='x', height=3,width=7, command=lambda:button_press('*'))
btnT.grid(row=2,column=3)
btnD=tk.Button(frm , text='/', height=3,width=7, command=lambda:button_press('/'))
btnD.grid(row=3,column=3)

clear=tk.Button(master=root, text='clear', height=3,width=7, command=clear)
clear.pack()

exit=tk.Button(root, text='exit rukundo.dev', command=root.destroy)
exit.pack()

root.mainloop()