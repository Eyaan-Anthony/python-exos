#We will simulate two planets orbiting around the sun
# of course the two orbits are cicular and each planet follows its own orbit.
#The sun will be at the center of the canvas
from tkinter import * 
from math import sin, cos

def move():
    "To move the circle in the canvas"
    global x1, y1, angle, x2, y2, flag
    xp, yp = x1, y1 #to store initial coordinates
    xq, yq = x2, y2 #to store initial coordinates
    angle = angle + 0.1 #rotation  of 0.1 rads
    x1, y1 = sin(angle), cos(angle)
    x2, y2 = sin(angle), cos(angle)
    #coordinates of circular path
    x1, y1 = x1*120 + 225, y1*120 + 225
    x2, y2 = x2*180 + 225, y2*180 + 225
    #120 is the radius of the circle described, 150 is center of canvas
    #we put the coordinates up to scale
    can.coords(circle1, x1 - 20, y1 - 20, x1 + 20, y1 + 20)
    can.coords(circle2, x2 - 20, y2 - 20, x2 + 20, y2 + 20)
    can.create_line(xp, yp, x1, y1, fill='light gray')
    can.create_line(xq, yq, x2, y2, fill='light gray') 
    #to draw trajectory, just draw a line connecting the initial point to the final point each time you move
    
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


flag = 0
angle, x1, y1 = 0, 268, 337
x2, y2 = 307, 388
x, y = 225, 225
fen = Tk()
fen.title('Sun and Two planets')
can = Canvas(fen, width = 450, height = 450)
can.pack(side = TOP)
circle1 = can.create_oval(x1-20, y1-20, x1 + 20, y1 + 20, fill = 'red')
circle2 = can.create_oval(x2-20, y2-20, x2 + 20, y2 + 20, fill = 'red')
sun = can.create_oval(x-45, y-45, x + 45, y + 45, fill = 'yellow')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
Button(fen, text='Quit', command =fen.quit).pack(side =RIGHT, padx =10)
fen.mainloop()