from tkinter import *


def create_tringle(canvas,x1,y1,x2,y2,x3,y3):
    

    x1 = input('Введите первую кординату для х1')
    y1 =input('ввудите вторую кординату для x1')
    canvas.create_line(x1,y1,x2,y2)

    x2 = input('Введите первую кординату для х2')
    y2 = input('ввудите вторую кординату для x2')
    canvas.create_line(x1,y1,x3,y3)

    x3 = input('Введите первую кординату для х3')
    y3 = input('ввудите вторую кординату для x3')

    canvas.create_line(x3,y3,x2,y2)
