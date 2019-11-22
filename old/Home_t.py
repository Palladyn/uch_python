import turtle
t=turtle.Pen()
t.reset()

def mycircle():
    for x in range(1, 9):
        t.forward(100)
        t.left(45)


mycircle()




turtle.mainloop()