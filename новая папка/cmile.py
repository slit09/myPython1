from tkinter import *

def smile():
    label=Label(text=':)',bg='red')
    text.window_create(INSERT,window=label)

root =Tk()
text =Text(width=50,height=10)
text.pack()

button =Button(text=':)',command=smile)
button.pack()

root.mainloop()