from tkinter import *
from tkinter import messagebox as mb


def proverka():
    answer = mb.askyesno()
    title="Вопрос"
    message="Перенести данные?"
    if answer:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s 


root = Tk()
entry = Entry()
entry.pack(pady=10)
Button(text='Передавать',command=proverka).pack()
label = Label(height=3)
label.pack()

root.mainloop()

