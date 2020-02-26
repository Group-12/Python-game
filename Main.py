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
        return random.randint(1,10)

def vel_x():
    return random.randint(-2,2)

def vel_y():
    return random.randint(-2,2)

class Wall:
    def __init__(self, border, color, side):
        self.border = border
        self.color = color
        self.normal = Vector(1,0)
        self.side = side
    #    if userinput == 'r':
        self.x1 = 600
    #    elif userinput == 'l':
        self.x2 = 0
    #    else:
    #        print('error')
        self.edge_r = self.x + self.border

    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

    def hit(self, ball):
        if userinput == 'l':
            h = (ball.offset_l() <= self.edge_r)
            return h
        elif userinput == 'r':
            h = (ball.offset_l() >= self.edge_r - 50)
            return h
        else:
            print('error')




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


class Interaction:
    def __init__(self, balls):
        self.balls = balls
        self.in_collision = set()

    def hit(self, b1, b2):
        distance = b1.pos.copy().subtract(b2.pos).length()
        return distance <= b1.radius + b2.radius

    def do_bounce(self, b1, b2):
        normal = b1.pos.copy().subtract(b2.pos).normalize()

        b1_perp = b1.vel.get_proj(normal)
        b2_perp = b2.vel.get_proj(normal)
        b1_par = b1.vel.copy().subtract(b1_perp)
        b2_par = b2.vel.copy().subtract(b2_perp)

        b1.vel = b1_par + b2_perp
        b2.vel = b2_par + b1_perp

    def collide(self, b1, b2):
        if self.hit(b1, b2):
            b1vb2 = (b1, b2) in self.in_collision
            b2vb1 = (b2, b1) in self.in_collision
            if not b1vb2 and not b2vb1:
                self.do_bounce(b1, b2)
                self.in_collision.add((b1, b2))
        else:
            self.in_collision.discard((b1, b2))
            self.in_collision.discard((b2, b1))

    def update(self):
        for ball in self.balls:
            ball.update()

        for ball1 in self.balls:
            for ball2 in self.balls:
                if ball1 != ball2:
                    self.collide(ball1, ball2)

    def draw(self, canvas):
        self.update()
        for ball in self.balls:
            ball.draw(canvas)



balls = []

ballif = 2


def tick():
    """
    Timer handler
    """
    balls.append(Ball)


for obj in balls:
    print("obj")


num_balls = 100
for i in range(num_balls):
    balls.append(Ball(Vector(RandPosX(), RandPosY()),Vector(vel_x(), vel_y()), radius_random(), randCol ()))

#ball1 = Ball(Vector(RandPosX(), RandPosY()),Vector(vel_x(), vel_y()), radius_random(), randCol ())


interaction = Interaction(balls)


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Colours ", CANVAS_WIDTH , CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)

timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start ()
timer.start()
