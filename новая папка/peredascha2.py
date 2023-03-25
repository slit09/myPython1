from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk() 
root.title("Калькулятор")


bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6","=","-",
"1", "2", "3","C","0"]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width=10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)


def calc(key):
    global memory
    if key == "=":

        str1 = "-+0123456789*" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "= Введи символы доступные на калькулято