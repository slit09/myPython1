from tkinter import * 

def Change():
    lab['text'] = 'Выдано'


root = Tk()

Label(text='Пункт выдачи').pack()
Button(text='Получить',command=Change).pack()

lab =Label(width=10,height=1)
lab.pack()

root.mainloop()