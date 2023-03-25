from tkinter import *

class Block:
    def __init__(self,master,func):
         self.ent = Entry(master,width=20)
         self.but = Button(master,text='вжмыхнись вкусно))')
         self.tab = Label(master,width=20,bg='white',fg='black')
         self.but['command'] = getattr(self,func)
         self.ent.pack()
         self.but.pack()
         self.tab.pack()

    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.tab['text'] = ' '.join(s)

    def str_reverse(self):
        s = self.ent.get()
        s = s.split()
        s.reverse()
        self.tab['text'] = ' '.join(s)
        

root = Tk()

first_byl