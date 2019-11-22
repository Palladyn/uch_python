from tkinter import *
import random
import time

tk=Tk()
canvas=Canvas(tk, width=500,height=500)
canvas.pack()

def kvadro(width,height):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=x2+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)

def duga(grad):
    canvas.create_arc(10,10,200,100,extent=grad, style=ARC)

def mnogougol():
    canvas.create_polygon(10,10,100,10,100,110, fill="",outline="red")

def text_p():
    canvas.create_text(150,100, text='Много людей тут', fill='red', font=('Times',15))

def animat():
    canvas.create_polygon(10, 10, 10, 60, 50, 35)
    for x in range(0,90):
        canvas.move(1,5,5)
        tk.update()
        time.sleep(0.05)

def ruh():
    canvas.create_polygon(10,10,10,60,50,35)
    def mov(event):
        if event.keysym == 'Up':
            canvas.move(1,0,-3)
        elif event.keysym == 'Down':
            canvas.move(1, 0, 3)
        elif event.keysym == 'Left':
            canvas.move(1, -3, 0)
        else:
            canvas.move(1, 3, 0)
    canvas.bind_all('<KeyPress-Up>', mov)
    canvas.bind_all('<KeyPress-Down>', mov)
    canvas.bind_all('<KeyPress-Left>', mov)
    canvas.bind_all('<KeyPress-Right>', mov)

ruh()

tk.mainloop()