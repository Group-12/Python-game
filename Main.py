'''
https://py3.codeskulptor.org/#user305_7mUid7UcUN_2.py
'''

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
#control + BREAK to kill process, control + C does not work

import random

#import simplegui
#from user304_rsf8mD0BOQ_1 import Vector

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
interval = 100

def randCol ():

        r = random.randrange (0, 256)
        g = random.randrange (0, 256)
        b = random.randrange (0, 256)

        return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def radius_random():
        return random.randint(10,50)

def vel_x():
    return random.randint(-2,2)

def vel_y():
    return random.randint(-2,2)


class Ball:
    def __init__(self,pos, vel, radius, color):
        self.pos = pos
        self.vel = vel
        self.radius =radius
        self.color = color
        self.border = 1

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)
        self.update()

    def update(self):
        self.pos=self.pos.add(self.vel)


def RandPosX():
    return random.randrange(0, CANVAS_WIDTH)
def RandPosY():
    return random.randrange(0, CANVAS_HEIGHT)


balls = []

ballif = 2


def tick():
    """
    Timer handler
    """
    balls.append(Ball)


for obj in balls:
    print("obj")


ball1 = Ball(Vector(RandPosX(), RandPosY()),Vector(vel_x(), vel_y()), radius_random(), randCol ())


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Colours ", CANVAS_WIDTH , CANVAS_HEIGHT)
frame.set_draw_handler(ball1.draw)

timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start ()
timer.start()
