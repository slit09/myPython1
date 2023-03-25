from tkinter import *

def proverka():
    if r_var.get() == 0:
        label['bg'] = 'red'
    elif r_var.get() == 1:
        label['bg'] = 'green'
    elif r_var.get() == 2:
        label['bg'] = 'blue'

root = Tk()

r_var = IntVar()
r_var.set(0)

red = Radiobutton(text='Красный',command=proverka,variable=r_var,value=0)
green = Radiobutton(text='Зеленый',command=proverka,variable=r_var,value=1)
blue = Radiobutton(text='Голубой',command=proverka,variable=r_var,value=2)
label = Label(width=20,height=10)

label.pack()
red.pack()
green.pack()
blue.pack()

root.mainloop()