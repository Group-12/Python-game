#### RUN ON WINDOWS ###
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
#control + BREAK to kill process, control + C does not work

### RUN ON CODESKULPTOR ###
#import simplegui
#from user304_rsf8mD0BOQ_1 import Vector

import random

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
interval = 100

#####

"""
Creates a randomomised properties for the balls
Returns: Random RGB color, Random radius,
         Random X and random Y
"""
def randCol ():

        r = random.randrange (0, 256)
        g = random.randrange (0, 256)
        b = random.randrange (0, 256)

        return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'


def radius_random():
    return random.randint(3,20)

def vel_x():
    return random.randint(-2,2)

def vel_y():
    return random.randint(-2,2)

######

class Player:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'

    def draw(self, canvas):
        #print(self.pos.get_p())
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, self.colour, self.colour)


    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)

class Keyboard:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.left = True

        elif key == simplegui.KEY_MAP['right']:
            self.right = True

        elif key == simplegui.KEY_MAP['up']:
            self.up = True

        elif key == simplegui.KEY_MAP['down']:
            self.down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['left']:
            self.left = False

        elif key == simplegui.KEY_MAP['right']:
            self.right = False

        elif key == simplegui.KEY_MAP['up']:
            self.up = False

        elif key == simplegui.KEY_MAP['down']:
            self.down = False

#####

class KBInteraction:
    def __init__(self, player, keyboard):
        self.player = player
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.left:
            self.player.vel.add(Vector(-1, 0))

        elif self.keyboard.right:
            self.player.vel.add(Vector(1, 0))

        elif self.keyboard.up:
            self.player.vel.add(Vector(0, -1))

        elif self.keyboard.down:
            self.player.vel.add(Vector(0, 1))


    def draw(self, canvas):
        inter.update()
        Player.update()
        Player.draw(canvas)

#####

class Wall:
    def __init__(self, border, color):
        self.border = border
        self.color = color

        self.x = CANVAS_WIDTH
        self.y = CANVAS_HEIGHT

        self.edge = self.x + self.border

    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

        canvas.draw_line((0, 0),
                         (0, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

        canvas.draw_line((0, 0),
                         (CANVAS_WIDTH, 0),
                         self.border*2+1,
                         self.color)

        canvas.draw_line((0, CANVAS_HEIGHT),
                         (CANVAS_WIDTH, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

    def hitRight(self, ball):
        self.normal = Vector(1,0)
        h1 = (ball.offset_x() >= self.edge - 50)
        return h1

    def hitLeft(self, ball):
        self.normal = Vector(-1,0)
        h2 = (ball.offset_x() <= self.edge)
        return h2

    def hitTop(self, ball):
        self.normal = Vector(0,1)
        h3 = (ball.offset_y() >= self.edge - 50)
        return h3

    def hitBottom(self, ball):
        self.normal = Vector(0,-1)
        h4 = (ball.offset_y() <= self.edge)
        return h4

#####

class Ball:
    def __init__(self,pos, vel, radius, color):
        self.pos = pos
        self.vel = vel
        self.radius =radius
        self.color = color
        self.border = 1

    def offset_x(self):
        return self.pos.x - self.radius

    def offset_y(self):
        return self.pos.y - self.radius

    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)
        self.update()

    def update(self):
        #self.pos=self.pos.add(self.vel)
        self.pos.add(self.vel)

    def bounce(self, wall):
        self.vel.reflect(wall.normal)



def RandPosX():
    return random.randrange(0, CANVAS_WIDTH)
def RandPosY():
    return random.randrange(0, CANVAS_HEIGHT)

######

class Interaction:
    def __init__(self, ball, walls, keyboard, player):
        self.balls = balls
        self.walls = walls
        self.keyboard = Keyboard
        self.player = player

        self.in_collision = set()

    def hit(self, b1, b2):
        distance = b1.pos.copy().subtract(b2.pos).length()
        return distance <= b1.radius + b2.radius

    # def do_bounce(self, b1, b2):
    #     normal = b1.pos.copy().subtract(b2.pos).normalize()
    #
    #     b1_perp = b1.vel.get_proj(normal)
    #     b2_perp = b2.vel.get_proj(normal)
    #     b1_par = b1.vel.copy().subtract(b1_perp)
    #     b2_par = b2.vel.copy().subtract(b2_perp)
    #
    #     b1.vel = b1_par + b2_perp
    #     b2.vel = b2_par + b1_perp

    def collide(self, b1, b2):
        if self.hit(b1, b2):
            b1vb2 = (b1, b2) in self.in_collision
            b2vb1 = (b2, b1) in self.in_collision
            if not b1vb2 and not b2vb1:
                #self.do_bounce(b1, b2)
                self.in_collision.add((b1, b2))
            else:
               self.in_collision.discard((b1, b2))
               self.in_collision.discard((b2, b1))


    def update(self):
        for w in self.walls:
            for i in self.balls:
                if w.hitRight(i) or w.hitLeft(i) or w.hitTop(i) or w.hitBottom(i):
                    if not self.in_collision:
                        i.bounce(w)

                        w.in_collision = True
                else:
                    w.in_collision = False
                    i.update()


        for ball1 in self.balls:
            for ball2 in self.balls:
                if ball1 != ball2:
                    self.collide(ball1, ball2)

    def draw(self, canvas):

        self.update()
        inter.update()
        Player.update()
        Player.draw(canvas)

        for ball in self.balls:
            ball.draw(canvas)
        for w in self.walls:
            w.draw(canvas)

######

balls = []
num_balls = 50
for i in range(num_balls):
#   def timer_handler():
        balls.append(Ball(Vector(RandPosX(), RandPosY()),Vector(vel_x(), vel_y()), radius_random(), randCol ()))

######

def timer_handler():
    pass
timer = simplegui.create_timer(100, timer_handler)
print(timer.is_running())
timer.start()
print(timer.is_running())
timer.stop()
print(timer.is_running())

######

wl = Wall(5, 'red')
wr = Wall(5, 'red')
wt = Wall(5, 'red')
wb = Wall(5, 'red')
walls=[wl, wr, wt, wb]

kbd = Keyboard()
Player = Player(Vector(CANVAS_WIDTH/2,CANVAS_HEIGHT/2), 40)

inter = KBInteraction(Player, kbd)
interaction = Interaction(balls, walls, kbd, Player)

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Group 12 python game project ", CANVAS_WIDTH , CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw) #only 1 draw handler
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()
