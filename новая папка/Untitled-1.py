from tkinter import *

def insert_text():
    s = 'Привет мир'
    text.insert(1,8,s)

def get_text():
    s = text.get(1,8,END)
    label['text'] = s

def delete_text():
    text.delete(1,8,END)


root = Tk()

text = Text(width=25,height=5)
text.pack()

frame = Frame()
frame.pack()

Button(frame,text='Вставить',command=insert_text).pack(side=LEFT)
Button(frame,text='Взять',command=get_text).pack(side=LEFT)
Button(frame,text='Удалить',command=delete_text).pack(side=LEFT)

label = Label()
label.pack()

root.mainloop()