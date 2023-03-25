from tkinter import *

def event_info(event):
    print(type(event))
    print(event)
    print(event.time)
    print(event.x_root)
    print(event.y_root)

root = Tk()
root.minsize(width=500,height=400)

root.bind('a',event_info)

root.mainloop()