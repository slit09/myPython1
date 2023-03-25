from tkinter import *

root = Tk()


l1 = Label(width=7,height=5,bg='yellow',text='1')
l2 = Label(width=7,height=5,bg='orange',text='2')
l3 = Label(width=7,height=4,bg='lightgreen',text='3')
l4 = Label(width=7,height=4,bg='lightblue',text='4')




l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)


root.mainloop()





