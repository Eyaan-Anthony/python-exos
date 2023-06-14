# dropping and rebounding
#Here, the ball has to be clickable too.
#Each time the player clicks on the ball, the ball decreases in size and changes in color.
#I can set the game to stop once the ball reaches a certain size, or just set a score field to show
# the players score.
#I have to increase the size of the ball i think
from tkinter import *
from random import *
def move():
    global x, y, v, dx, dv, flag
    # horizontal displacement
    if x > 375 or x < 25 : # bouncing off the lateral walls
        dx = -dx # inverse the displacement
    x = x + dx
    # variation of vertical velocity
    v = v + dv
    # vertical displacement proportional to velocity
    y = y + v
    if y > 230: # ground level is 240 pixels
        y = 230 # stop right there
        v = -v # rebound, velocity is inverted
    # reposition the ball
    can.coords(ball, x-20, y-20, x+20, y+20)
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
    global dx, dv, flag, scr, s, size, color, n, ball
    color = ['yellow', 'green', 'orange', 'blue', 'purple', 'cyan']
    n = randrange(len(color))
    overlaping = can.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if  ball in overlaping:
        s = s + 1
        scr.set(str(s))
        size = size + 5
        can.delete(ball)
        ball = can.create_oval(x-20 + size, y-20 + size, x+20 - size, y+20 - size, fill=color[n])
    if s == 10:
        scr.set('You won')
        flag = 0
        fen.after(500, quit)


# initialisation of coordinates and velocity
x, y, v, dx, dv, flag = 25, 25, 0, 6, 5, 0
s = 0
size = 0
fen = Tk()
fen.title('Bouncing')
can = Canvas(fen, width =400, height=250, bg="white")
can.pack()
can.bind('<Button-1>', on_canvas_click)
ball = can.create_oval(x-20, y-20, x+20, y+20, fill='red')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
scr = StringVar()
score = Entry(fen, textvariable=scr).pack(side =RIGHT, padx= 10)
Label(fen, text='Score').pack(side =RIGHT, padx= 10)
Button(fen, text='Quit', command =fen.quit).pack(side =RIGHT, padx =10)
fen.mainloop()

