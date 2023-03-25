from tkinter import * 

root = Tk()

l1 = Label(text='Машинное обучение',font='Arial 32')
l2 = Label(text='я не знабю что тут писать',font=('Khmer os',24,'bold'))

l1.config(bd=20,bg='#ffaaaa')
l2.config(bd=20,bg='#aaffff')
l1.pack()
l2.pack()

root.mainloop()