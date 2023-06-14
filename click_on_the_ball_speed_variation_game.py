#This a game where there is a ball on the canvas.
#Firstly the ball has to move in a random manner in the canvas and of course bounce of the walls of the canvas
#The ball moves a realtively small velocity.
#The ball is clickable.
#Each time the ball is clicked on, the score of the player(that will be displayed down maybe) is incremented
# by 1.
# At the same time, each time the ball is clicked on, the speed of the ball increases to make it more difficult
#to click on the ball
# dropping and rebounding
from tkinter import *
def move():
    global x, y, v, dx, dv, flag, t
    t = 80
    # horizontal displacement
    if x > 385 or x < 15 : # bouncing off the lateral walls
        dx = -dx # inverse the displacement
    x = x + dx
    # variation of vertical velocity
    v = v + dv
    # vertical displacement proportional to velocity
    y = y + v
    if y > 240: # ground level is 240 pixels
        y = 240 # stop right there
        v = -v # rebound, velocity is inverted
    # reposition the ball
    can.coords(ball, x-10, y-10, x+10, y+10)
    # and so on and so forth
    if flag > 0:
        fen.after(t,move)

def start():
    global flag
    flag = flag +1
    if flag == 1:
        move()

def stop():
    global flag
    flag =0

def on_canvas_click(event):
    global dx, dv, flag, scr, s, t
    overlaping = can.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if  ball in overlaping:
        s = s + 1
        scr.set(str(s))
        dx = dx * 2#increasing the "speed" of the x displacement of the ball
    if s == 3:
        scr.set('You won')
        flag = 0
        fen.after(500, quit)

        


# initialisation of coordinates and velocity
x, y, v, dx, dv, flag = 15, 15, 0, 6, 5, 0
s = 0
fen = Tk()
fen.title('Bouncing')
can = Canvas(fen, width =400, height=250, bg="white")
can.pack()
can.bind('<Button-1>', on_canvas_click)
ball = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
scr = StringVar()
score = Entry(fen, textvariable=scr).pack(side =RIGHT, padx= 10)
Label(fen, text='Score').pack(side =RIGHT, padx= 10)
Button(fen, text='Quit', command =fen.quit).pack(side =RIGHT, padx =10)
fen.mainloop()


