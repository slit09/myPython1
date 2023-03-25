from tkinter import *
 
root = Tk()
mainmenu = Menu(root) 
root.config(menu=mainmenu) 

mainmenu.add_command(label='Файл')
mainmenu.add_command(label='Справка')

root.mainloop() 