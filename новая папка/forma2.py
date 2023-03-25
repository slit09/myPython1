from tkinter import *
from forma3 import create_tringle
 
window = Tk()
window.title("Треугольник")
canvas = Canvas(window,width=800,height=600,background='white')
create_tringle(canvas,100,50,100,200,400,100)
canvas.pack(expand=True,fill=BOTH)
window.mainloop()