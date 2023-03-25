from tkinter import * 


def show():
    s = f'{var1.get()}, ' \
        f'{var2.get()}'
    label['text'] = s



root = Tk()

frame = Frame()
frame.pack(side=LEFT)

var1 = BooleanVar()
var1.set(0)

c1 = Checkbutton(frame,text= ' Первый',
                variable=var1,
                onvalue=1,offvalue=0,
                command=show)
c1.pack(anchor=W,padx=10)

var2 = IntVar()
var2.set(-1)

c2 = Checkbutton(frame,text='Второй',
                variable=var2,
                onvalue=1)

