# dropping and rebounding
#We have to insert about 4 more balls, to have multiple balls bouncing off the walls and off each other
from tkinter import *
from math import sqrt
def move():
    global x1, y1, v, dx1, dv, flag, x2, y2, dx2, d1, x5, y5, dx5, x4, y4, dx4, x3, y3, dx3
    d1 = sqrt((x2-x1)**2 + (y2-y1)**2)
    d2 = sqrt((x3-x1)**2 + (y3-y1)**2)
    d3 = sqrt((x4-x1)**2 + (y4-y1)**2)
    d4 = sqrt((x5-x1)**2 + (y5-y1)**2)

    db1 = sqrt((x3-x2)**2 + (y3-y2)**2)
    db2 = sqrt((x4-x2)**2 + (y4-y2)**2)
    db3 = sqrt((x5-x2)**2 + (y5-y2)**2)

    dc1 = sqrt((x4-x3)**2 + (y4-y3)**2)
    dc2 = sqrt((x5-x3)**2 + (y5-y3)**2)

    dd1 = sqrt((x5-x4)**2 + (y5-y4)**2)

    #All these distances represent the distances between the centers of the circles.
    #Since each ball has a radius of 10, if 2 balls collide, then the distance between the centers
    # is equal to radius*2.
    #Therefore i set a conditionn to check if that distance is equal to or less than the distance between 
    # two circles that collides (radius*2), if it is the case, then inverse displacement
    #However the game is too monotous, i can make it more interesting and less predictable
    #but for now it works.

    # horizontal displacement
    if x1 > 385 or x1 < 15  or d1 <= 20 or d2 <= 20 or d3 <= 20 or d4 <= 20: # bouncing off the lateral walls
        dx1 = -dx1 # inverse the displacement
        
    x1 = x1 + dx1
    if x2 > 385 or x2 < 15 or d1 <= 20 or db1 <= 20 or db2 <=20 or db3 <=20: # bouncing off the lateral walls
        dx2 = -dx2 # inverse the displacement
    x2 = x2 + dx2
    if x3 > 385 or x3 < 15 or d2 <= 20 or db1 <= 20 or dc1 <= 20 or dc2 <= 20  : # bouncing off the lateral walls
        dx3 = -dx3 # inverse the displacement
    x3 = x3 + dx3
    if x4 > 385 or x4 < 15 or d3 <= 20 or db2 <= 20 or dc1 <= 20 or dd1 <= 20 : # bouncing off the lateral walls
        dx4 = -dx4 # inverse the displacement
    x4 = x4 + dx4
    if x5 > 385 or x5 < 15 or d4 <= 20 or db3 <=20 or dc2 <= 20 or dd1 <= 20 : # bouncing off the lateral walls
        dx5 = -dx5 # inverse the displacement
    x5 = x5 + dx5

    # variation of vertical velocity
    v = v + dv
    # vertical displacement proportional to velocity
    y1 = y1 + v 
    y2 = y2 + v 
    y3 = y3 + v
    y4 = y4 + v 
    y5 = y5 + v 
    if y1 > 240: # ground level is 240 pixels
        y1 = 240 # stop right there
        v = -v # rebound, velocity is inverted
    if y2 > 240: # ground level is 240 pixels
        y2 = 240 # stop right there
        v = -v # rebound, velocity is inverted
    if y3 > 240: # ground level is 240 pixels
        y3 = 240 # stop right there
        v = -v # rebound, velocity is inverted
    if y4 > 240: # ground level is 240 pixels
        y4 = 240 # stop right there
        v = -v # rebound, velocity is inverted
    if y5 > 240: # ground level is 240 pixels
        y5 = 240 # stop right there
        v = -v # rebound, velocity is inverted
    
    # reposition the ball
    can.coords(ball, x1-10, y1-10, x1+10, y1+10)
    can.coords(ball2, x2-10, y2-10, x2+10, y2+10)
    can.coords(ball3, x3-10, y3-10, x3+10, y3+10)
    can.coords(ball4, x4-10, y4-10, x4+10, y4+10)
    can.coords(ball5, x5-10, y5-10, x5+10, y5+10)
    
    # and so on and so forth
    if flag > 0:
        fen.after(50,move)

def start():
    global flag
    flag = flag +1
    if flag == 1:
        move()

def stop():
    global flag
    flag =0

def on_canvas_click(event):
    global flag, scr, s, ball, ball2, ball3, ball4, ball5
    overlaping = can.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if  ball in overlaping:
        s = s + 1
        scr.set(str(s))
    if ball2 in overlaping:
        s = s -1
        scr.set(str(s))
    
    if ball3 in overlaping:
        s = s -1
        scr.set(str(s))
    
    if ball4 in overlaping:
        s = s -1
        scr.set(str(s))
    
    if ball5 in overlaping:
        s = s -1
        scr.set(str(s))
    
    if s < 0:
        scr.set('Haha sucker, you loose')
        fen.after(500, quit)

    if s == 5:
        scr.set('You won')
        flag = 0
        fen.after(500, quit)



# initialisation of coordinates and velocity
x1, y1, v, dx1, dv, flag = 15, 15, 0, 10, 5, 0
x2, y2, dx2 = 65, 15, 10 
x3, y3, dx3 = 135, 15, 10
x4, y4, dx4 = 185, 15, 10
x5, y5, dx5 = 245, 15, 10
s = 0

fen = Tk()
fen.title('Bouncing')
can = Canvas(fen, width =400, height=250, bg="white")
can.pack()
can.bind('<Button-1>', on_canvas_click)
ball = can.create_oval(x1-10, y1-10, x1+10, y1+10, fill='red')
ball2 = can.create_oval(x2-10, y2-10, x2+10, y2+10, fill='blue')
ball3 = can.create_oval(x3-10, y3-10, x3+10, y3+10, fill='violet')
ball4 = can.create_oval(x4-10, y4-10, x4+10, y4+10, fill='green')
ball5 = can.create_oval(x5-10, y5-10, x5+10, y5+10, fill='orange')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
scr = StringVar()
score = Entry(fen, textvariable=scr).pack(side =RIGHT, padx= 10)
Label(fen, text='Score').pack(side =RIGHT, padx= 10)
Button(fen, text='Quit', command =fen.quit).pack(side =RIGHT, padx =10)
fen.mainloop()

