from tkinter import *

def paint(color):
    label['bg'] = color

class RBColor:
    def __init__(self,color,val):
        Radiobutton (
            text=color,
            command=lambda i=color: paint(i),
            variable=r_var,value=val
        ).pack()


        

root = Tk()

r_var = IntVar()
r_var.set(0)

RBColor('red',0)
RBColor('green',1)
RBColor('blue',2)

label = Label(width=20,height=10,bg='red')

label.pack()


root.mainloop()