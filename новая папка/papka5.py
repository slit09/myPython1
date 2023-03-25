from tkinter import *

root = Tk()

c = Canvas(root, width=200,height=200,bg='white')
c.pack()

c.create_rectangle(50,90,140,175,
    fill='red', outline='red')

c.create_polygon(30,90,160,90,95,40,
    fill='pink', outline='pink')

c.create_oval(150,10,190,50,
    fill='orange',outline='orange')

x = -20
while x < 200:
    c.create_arc(x,170,x+40,250, outline='green',
        style=ARC,start=100,extent=-80,
        width=2)
    x += 10 

root.mainloop()
