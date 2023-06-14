#Here we have to simulate the motion of dropping ball due to gravity.
#Each time the ball hits the ground, it bounces, each time it bounces the vertical displacement  reduces
#until it eventually reaches 0 before we reset it to the initial height
#The velocity of the ball increases with time since it is acted upon by gravity
from tkinter import *
# define event handlers
def move():
    "Dropping the ball"
    global x1, y1, dx, dy, flag, velocity, gravity

    x1, y1 = x1 , y1 + dy
    if y1 < 220:
        dy = 15
    
    can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0: 
        fen1.after(50,move) # => loop after 50 milliseconds
        #reducing the time increases the "speed" of the animation

def stop_it():
    "Stop animation"
    global flag 
    flag =0


def start_it():
    "Start animation"
    global flag
    if flag ==0: # to start a single loop
        flag =1
        move()


#========== Main program =============
# these are the global variables :
x1, y1 = 125, 10 # initial coordinates
dx, dy = 15, 15# step length
gravity = 0.05
velocity = 0
flag =0 # indicator flag

# Parent widget :
fen1 = Tk()
fen1.title("Tkinter Animation Exercise")

# child widget :
can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
can1.pack(side=LEFT, padx =5, pady =5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
btn1 = Button(fen1,text='Quit', width =8, command=fen1.quit)
btn1.pack(side=BOTTOM)
btn2 = Button(fen1, text='Start', width =8, command=start_it)
btn2.pack()
btn3 = Button(fen1, text='Stop', width =8, command=stop_it)
btn3.pack()

# Start the event receiver
fen1.mainloop()