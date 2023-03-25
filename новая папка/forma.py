from tkinter import *
from tkinter import ttk 

click = 0 

def click_button():
    global click 
    click += 1
    btn["text"] =f"Нажми меня"
    if click == 1:
        btn["text"] =f"Привет Оля{click}"
    elif click == 2:
        btn["text"] =f"Привет Данил{click}"
    elif click == 3:
        btn ["text"] =f"Привет Игорь{click}"
    elif click == 4:
        btn["text"] =f"Привет Леонид{click}"
    elif click == 5:
        btn["text"] =f"Привет Глеб{click}"
    else:
        btn['text'] = f"некого нет{click}"
        btn['text'] = [DISABLED]

window = Tk()
window.title('Кнопка')
window.geometry('800x600')

btn = ttk.Button(text="Нажми меня",command=click_button)

btn.pack()
window.mainloop()




