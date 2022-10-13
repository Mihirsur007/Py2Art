# Please read the license and readme before using this software

from turtle import *
from random import randint
import turtle
from tkinter import *
from tkmacosx import Button

x = ["red", 'orange', 'yellow', 'spring green', 'cyan', 'dark orchid', 'hot pink', 'cornflower blue']

def setup():
    turtle.showturtle()
    ws = turtle.Screen()
    turtle.speed(1000)
    ws.bgcolor("black")

def makeSquare():
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()


def reset():
    turtle.forward(-240)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)

def frame():
    turtle.right(90)
    turtle.color('black')
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.color("white")
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)

def makeart():

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

    reset()

    for c in range(0,len(x)):
        turtle.color(x[randint(0, (len(x) - 1))])
        makeSquare()

################################

win = Tk()
win.configure(bg="black")
win.title("Py2Art")


win.geometry("700x400")


def close_win():
   win.destroy()

def clicked():
    setup()
    win.destroy()
    makeart()
    frame()
    turtle.hideturtle()
    turtle.done()



Label(win, text="Py2Art",
font=('Poppins bold', 35), bg="black", fg='Cyan').pack(pady= 20)
Label(win, text="A Python Art Generator",
font=('Poppins bold', 25), bg="black", fg='Cyan').pack(pady= 20)
#Create a Button
Button(win, text= "Start", font=('Poppins bold', 16),
command=clicked, bg="black", fg='Cyan').pack(pady=20)


Button(win, text= "Quit", font=('Poppins bold', 16),
command=close_win, bg="black", fg='Cyan').pack(pady=20)

Label(win, text="Created by Mihir Surlaker",
font=('Poppins bold', 15), bg="black", fg='Cyan').pack(pady= 20)

win.mainloop()






