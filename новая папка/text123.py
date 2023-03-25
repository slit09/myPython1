from tkinter import *

root = Tk()

text = Text(width=20,height=7)
text.pack(side=LEFT)

scrolt = Scrollbar(command=text.yview)
scrolt.pack(side=LEFT,fill=Y)

text.config(yscroltcommand=scrolt.set)

root.mainloop()
