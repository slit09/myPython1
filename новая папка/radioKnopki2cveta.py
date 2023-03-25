from tkinter import *

def chang():
    if r_var.get() == 0:
        label['bg'] = '+8-800-535-35-55'
    elif r_var.get() == 1:
        label['bg'] = '+7-739-348-45-67'
    elif r_var.get() == 2:
        label['bg'] = '+1 634 485 47-56'

root = Tk()

r_var = IntVar()
r_var.set(0)


red = Radiobutton(text='Красный',variable=chang,value=0)
green = Radiobutton(text='Зеленый',variable=chang,value=1)
blue = Radiobutton(text='Синий',variable=chang,value=2)
red = Radiobutton(text='Красный',variable=chang,value=0)
button = Button(text = 'Изменипть',command=chang)
label = Label(width=20,height=10)

red.pack()
green.pack()
blue.pack()
label.pack()

root.mainloop()