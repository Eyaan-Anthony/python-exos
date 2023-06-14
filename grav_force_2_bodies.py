#Program that shows two bodies(circles) in a canvas,
#The two bodies are animated (they can be moved up or down and left or right)
#The program also shows the value of the gravitational force between them in real time.
#We have been using the object oriented approach
#We create objects, and then define functions that act on the said objects
#However, i have to make it cleaner using grid() instead of pack()

from tkinter import *#
from math import sqrt

#General displacement procedure
def advance1(lr, ud):
    "To displace the first body around in the canvas, lr is left right, ud is up down"
    global x1, y1
    x1, y1 = x1 +lr, y1 + ud
    can.coords(oval1, x1,y1, x1+30,y1+30)


def advance2(lr, ud):
    "To displace the circle around in the canvas, lr is left right, ud is up down"
    global x2, y2
    x2, y2 = x2 +lr, y2 + ud
    can.coords(oval2, x2,y2, x2+30,y2+30)

#event handling
#for the first body
def left_displ1():
    "To move left"
    advance1(-10, 0)
    grav_force()

def right_displ1():
    "To move right"
    advance1(10, 0)
    grav_force()

def up_displ1():
    "To move upwards"
    advance1(0, -10)
    grav_force()

def down_displ1():
    "To move down"
    advance1(0, 10)
    grav_force()

#event handling for the second body
def left_displ2():
    "To move left"
    advance2(-10, 0)
    grav_force()

def right_displ2():
    "To move right"
    advance2(10, 0)
    grav_force()

def up_displ2():
    "To move upwards"
    advance2(0, -10)
    grav_force()

def down_displ2():
    "To move down"
    advance2(0, 10)
    grav_force()

#Add the grav_force function to each advance function, so that each time we move a body,
#The gravitational force is calculated automatically, since i couold not bind that function to a button
def grav_force():
    "Distance between the centers of the 2 circle"
    global x1, y1, x2, y2, m1, m2
    l = 6.67*10**-11
    dist = sqrt((x2-x1)**2 + (y2-y1)**2)
    F = l*(m1*m2)/dist**2
    chain.configure(text = "The gravitational force is:" + str(F) + "Newtons")
    

#### Main Program ####

# These are the global variables:
x1, y1 = 40, 40 # initial coordinates
x2, y2 = 80, 80 # initial coordinates
m1, m2 = 10000, 10000 #The two bodies are of identical mass.

#We create the master widget
fen = Tk()
fen.title("Gravitational force between two animated objects")

#We create the slave widgets
can = Canvas(fen, bg= 'dark grey', height=300, width=300)
oval1 = can.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
oval2 = can.create_oval(x2, y2, x2+30, y2+30, fill='red')
#The two circles have a radius of 15, and centers (x1, y1) and (x2, y2)
can.grid(row =1, column =1, rowspan =3, padx =10, pady =5)
chain = Label(fen)
chain.grid(row =8, column =1, rowspan =3, padx =4, pady =5)
Button(fen, text= 'C1 up', command=up_displ1).grid(row =1, column =2)
Button(fen, text= 'C1 down', command= down_displ1).grid(row =3, column =2)
Button(fen, text= 'C1 left', command= left_displ1).grid(row=2, column=2, sticky=E)
Button(fen, text= 'C1 right', command= right_displ1).grid(row=2, column=3, sticky=W)

Button(fen, text= 'C2 up', command=up_displ2).grid(row=5, column =2)
Button(fen, text= 'C2 down', command= down_displ2).grid(row=7, column =2)
Button(fen, text= 'C2 left', command= left_displ2).grid(row=6, column =2, sticky=E)
Button(fen, text= 'C2 right', command= right_displ2).grid(row=6, column =3, sticky=W)

fen.mainloop()

