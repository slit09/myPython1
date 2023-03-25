from tkinter import *

root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
#w = w//2
#h = h//2
w = w - 200
h = h - 200 
root.geometry('400x400+{}+{}'.format(w,h))

root.mainloop()