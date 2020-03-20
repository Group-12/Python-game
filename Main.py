#### RUN ON WINDOWS ###
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
#control + BREAK to kill process, control + C does not work

### RUN ON CODESKULPTOR ###
#import simplegui
#from user304_rsf8mD0BOQ_1 import Vector

import random

img = simplegui.load_image("http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png")
#img = simplegui.load_image("https://i.imgur.com/mT2HJvW.png")

width = 512
height = 192
columns = 8
rows = 3
#https://py3.codeskulptor.org/#user305_OeE5CQwr4D_2.py
frame_width = width / columns
frame_height = height / rows
frame_centre_x = frame_width / 2
frame_centre_y = frame_height / 2

frame_index = [2,1]

CANVAS_WIDTH = 800
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

""" Returns random radius between a range of two numbers"""
def radius_random():
    return random.randint(10,15)

""" Returns Random velocity for X-axis between set range """
def vel_x():
    return random.randint(-2,2)

""" Returns Random velocity for Y-axis between set range """
def vel_y():
    return random.randint(-2,2)

######

class Player:
    """
    Creates a object for the user to control
    params: Position and Player size
    Returns: None
    """
    def __init__(self, pos, radius):
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

#######

class Keyboard:
    """
    Detects button plresses
    params: None
    Returns: None
    """
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
    """
    Creates the interaction between the keyboard and the player
    params: Player and Keyboard classes
    Returns: None
    """
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
    """
    Creates the walls and detects if a hit has happened
    params: start and end points of each line,
            width of each border and color.
    Returns: None
    """

    def __init__(self, point1, point2, border, color):
        self.point1 = point1
        self.point2 = point2
        self.border = border
        self.color = color

        # (x, y) is midpoint of the wall
        self.x = (self.point1[0] + self.point2[0])/2
        self.y = (self.point1[1] + self.point2[1])/2

        self.minx = min(self.point1[0],self.point2[0])
        self.miny = min(self.point1[1],self.point2[1])

        self.maxx = max(self.point1[0],self.point2[0])
        self.maxy = max(self.point1[1],self.point2[1])

        self.edge = self.x + self.border

    def draw(self, canvas):
        canvas.draw_line(self.point1,
                         self.point2,
                         self.border*2+1,
                         self.color)

    def hitTest(self, ball):
            #left hit
        if self.x < CANVAS_WIDTH/2:
            self.normal = Vector(1,0)
            isHit = (ball.offset_l() <= self.x + self.border/2)
            #print("fixme hit left")

            #right hit
        elif self.x > CANVAS_WIDTH/2:
            self.normal = Vector(1,0)
            isHit = (ball.offset_r() >= self.x - self.border/2)
            #print("fixme hit right")

            #top hit
        elif self.y < CANVAS_HEIGHT/2:
            self.normal = Vector(0,1)
            isHit = (ball.offset_t() <= self.y + self.border/2)
            #print("fixme hit top")

            #bottom hit
        elif self.y > CANVAS_HEIGHT/2:
            self.normal = Vector(0,-1)
            isHit = (ball.offset_b() >= self.y - self.border/2)
            #print("fixme y = {}".format(self.y))
            #print("fixme hit bottom")

        else:
            print("ERROR: No such wall!")

        #print("fixme = {}".format(isHit))
        return isHit

#####

class Ball:
    """
    Creates each ball
    params: Position, velocity, ball size and color
    Returns: None
    """
    def __init__(self, pos, vel, radius, color):
        self.pos = pos
        self.vel = vel
        self.radius =radius
        self.color = color
        self.border = 1

    def offset_l(self): # left
        return self.pos.x - self.radius

    def offset_r(self): # right
        return self.pos.x + self.radius

    def offset_t(self): # top
        return self.pos.y - self.radius

    def offset_b(self): # bottom
        return self.pos.y + self.radius

    def update_index():
        #frame_index = [2,1]
        global frame_index
        frame_index[0] = (frame_index[0] + 1) % columns
        if frame_index[0] == 0:
            frame_index[1] = (frame_index[1] + 1) % rows

    def draw(self, canvas):
        Ball.update_index()
        source_centre = (frame_width * frame_index[0] + frame_centre_x,
        frame_height * frame_index[1] + frame_centre_y)
        #print (source_centre)
        source_size = (frame_width, frame_height)
        print(source_size)
        dest_centre = (300, 300)
        #print(dest_centre)
        # doesn't have to be same aspect ration as frame!
        dest_size = (200, 200)
        #canvas.draw_image(img, source_centre, source_size, dest_centre, dest_size)
        canvas.draw_image(img, source_centre, source_size, dest_centre, dest_size)

        '''
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)
        '''
        self.update()

    def update(self):
        self.pos.add(self.vel)

    def bounce(self, wall):
        self.vel.reflect(wall.normal)

#rad is the radius of the ball. using rad stops
#balls from spawning on the border, causing them to stick
def RandPosX(rad):
    return random.randrange(rad, CANVAS_WIDTH - rad)
def RandPosY(rad):
    return random.randrange(rad, CANVAS_HEIGHT - rad)

######

class Interaction:
    """
    Controls all interations between the other classes
    params: list of balls, list of walls,
            keyboard and player
    Returns: None
    """
    def __init__(self, balls, walls, keyboard, player):
        self.balls = balls
        self.walls = walls
        self.keyboard = Keyboard
        self.player = player

        self.in_collision = set()

        #hit between two balls or a ball and a player
    def hit(self, b1, b2):
        distance = b1.pos.copy().subtract(b2.pos).length()
        return distance <= b1.radius + b2.radius

        #creates a bounce between two balls
    def do_bounce(self, b1, b2):
        normal = b1.pos.copy().subtract(b2.pos).normalize()

        b1_perp = b1.vel.get_proj(normal)
        b2_perp = b2.vel.get_proj(normal)
        b1_par = b1.vel.copy().subtract(b1_perp)
        b2_par = b2.vel.copy().subtract(b2_perp)

        b1.vel = b1_par + b2_perp
        b2.vel = b2_par + b1_perp

    #detects if two balls have collided
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

    #determines if a ball should be absorbed
    def absorb(self, b1, b2):
        if self.hit(b1, b2):
            absorb_1v2 = (b1, b2) in self.in_collision
            absorb_2v1 = (b2, b1) in self.in_collision
            if absorb_1v2 == absorb_2v1:
                if b1.radius < b2.radius:
                    balls.remove(b1)
                    b2.radius = b2.radius + b1.radius/2
                if b1.radius >= b2.radius:
                    if b2 in self.balls:
                        balls.remove(b2)
                        b2.radius = b2.radius + b1.radius/2
                    else:
                        print("You were absorbed! GAME OVER")

                        ### LIFE COUNTER AND STATMENT HERE ###
                        # three lifes, update GUI/HUD

                        ### DEATH ANIMATION HERE ###
                        # set player color to red?
                        exit()

    def update(self):
        for w in self.walls:
            for i in self.balls:
                if w.hitTest(i):
                    if not self.in_collision:
                        i.bounce(w)
                        w.in_collision = True
                    else:
                        w.in_collision = False
                        i.update()

        for ball1 in self.balls:
            for ball2 in self.balls:
                if ball1 != ball2:
                    self.absorb(ball1, ball2)

        for ball1 in self.balls:
            if ball1.radius < self.player.radius:
                self.absorb(ball1, self.player)
            if ball1.radius > self.player.radius:
                self.absorb(ball1, self.player)

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
num_balls = 30
for i in range(num_balls):
#   def timer_handler():
        rad = radius_random()
        balls.append(Ball(Vector(RandPosX(rad), RandPosY(rad)),Vector(vel_x(), vel_y()), rad, randCol ()))

######
'''
def timer_handler():
    pass
timer = simplegui.create_timer(100, timer_handler)

motes = 0
timer.start()

else:
    timer.stop()
'''
######

wl = Wall((CANVAS_WIDTH, 0), (CANVAS_WIDTH, CANVAS_HEIGHT), 5, 'red')
wr = Wall((0, 0),(0, CANVAS_HEIGHT), 5, 'red')
wt = Wall((0, 0),(CANVAS_WIDTH, 0),5, 'red')
wb = Wall((0, CANVAS_HEIGHT), (CANVAS_WIDTH, CANVAS_HEIGHT), 5, 'red')

walls=[wl, wr, wt, wb]

kbd = Keyboard()

TotalPlayers =1 #fixme
Player = Player(Vector(CANVAS_WIDTH/2,CANVAS_HEIGHT/2), 12.5)
if TotalPlayers == 2:
    Player2 = Player(Vector(CANVAS_WIDTH/3,CANVAS_HEIGHT/3), 12.5)


inter = KBInteraction(Player, kbd) #test player without balls getting in the way
interaction = Interaction(balls, walls, kbd, Player)

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Group 12 python game project ", CANVAS_WIDTH , CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw) #only 1 draw handler
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()
