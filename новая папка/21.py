from tkinter import *

def button1():
    a1['text'] = 'красный'
    b1.delete(0,END)
    b1.insert(0,'#ff0000')

def button2():
    a1['text'] = 'оранжевый'
    b1.delete(0,END)
    b1.insert(0,'#ff7d00')

def button3():
    a1['text'] = 'желтый'
    b1.delete(0,END)
    b1.insert(0,'#ffff00')

def button4():
    a1['text'] = 'зеленый'
    b1.delete(0,END)
    b1.insert(0,'#00ff00')

def button5():
    a1['text'] = 'голубой'
    b1.delete(0,END)
    b1.insert(0,'#007dff')

def button6():
    a1['text'] = 'синий'
    b1.delete(0,END)
    b1.insert(0,'#0000ff')

def button7():
    a1['text'] = 'фиолетовый'
    b1.delete(0,END)
    b1.insert(0,'#7d00ff')

root = Tk()

fr_t = Frame(root)

a1 = Label(width=50,anchor=CENTER)
b1 = Entry(width=50,justify=CENTER)
l1 = Button(fr_t,width=2,command=button1,bg='#ff0000')
l2 = Button(fr_t,width=2,command=button2,bg='#ff7d00')
l3 = Button(fr_t,width=2,command=button3,bg='#ffff00')
l4 = Button(fr_t,width=2,command=button4,bg='#00ff00')
l5 = Button(fr_t,width=2,command=button5,bg='#007dff')
l6 = Button(fr_t,width=2,command=button6,bg='#0000ff')
l7 = Button(fr_t,width=2,command=button7,bg='#7d00ff')

a1.pack()
b1.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)
l5.pack(side=LEFT)
l6.pack(side=LEFT)
l7.pack(side=LEFT)

fr_t.pack()

root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               