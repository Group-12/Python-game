#### RUN ON WINDOWS ###
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#from Vector import Vector
#control + BREAK to kill process, control + C does not work

### RUN ON CODESKULPTOR ###
import simplegui
from user304_rsf8mD0BOQ_1 import Vector

from math import pi
import random

message = "GROUP 12 PYTHON GAME"
guide_text1 = ""
guide_text2 = ""
guide_text3 = ""
guide_text4 = ""
guide_text5 = ""
guide_text6 = ""
guide_text7 = ""
currentArea = ""
currentLives = ""

img = simplegui.load_image("slime.png")


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
interval = 100
pause = False
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
        global pause
        if key == simplegui.KEY_MAP['left']:
            self.left = True

        elif key == simplegui.KEY_MAP['right']:
            self.right = True

        elif key == simplegui.KEY_MAP['up']:
            self.up = True

        elif key == simplegui.KEY_MAP['down']:
            self.down = True

        elif key == simplegui.KEY_MAP['p'] and pause == False:
                pause = True



    def keyUp(self, key):
        global pause
        if key == simplegui.KEY_MAP['left']:
            self.left = False

        elif key == simplegui.KEY_MAP['right']:
            self.right = False

        elif key == simplegui.KEY_MAP['up']:
            self.up = False

        elif key == simplegui.KEY_MAP['down']:
            self.down = False

        elif key == simplegui.KEY_MAP['p'] and pause == True:
                pause = False

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
        self.radius = radius
        self.color = color
        self.border = 1

        #width = 512
        #height = 192
        #columns = 3
        #rows = 8
#https://py3.codeskulptor.org/#user305_OeE5CQwr4D_2.py



    def offset_l(self): # left
        return self.pos.x - self.radius

    def offset_r(self): # right
        return self.pos.x + self.radius

    def offset_t(self): # top
        return self.pos.y - self.radius

    def offset_b(self): # bottom
        return self.pos.y + self.radius


    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)
        self.update()

    def update(self):
        self.pos.add(self.vel)

    def bounce(self, wall):
        self.vel.reflect(wall.normal)



class PowerUps:
    def __init__(self, pos, vel, radius):
        self.pos = pos
        self.vel = 0
        self.radius = radius
        self.color = 'White'
        self.border = 1

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)

    def update(self):
        self.pos.add(self.vel)


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
    def __init__(self, balls, walls, keyboard, player, pups):
        self.balls = balls
        self.walls = walls
        self.keyboard = Keyboard
        self.player = player
        self.pups = pups

        self.in_collision = set()

        #hit between two balls or a ball and a player

    def collisionPup(self):
        pass

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


    def absorb1(self, b1, b2):
        if self.hit(b1, b2):
            absorb_1v2 = (b1, b2) in self.in_collision
            absorb_2v1 = (b2, b1) in self.in_collision
            if absorb_1v2 == absorb_2v1:
                if b1.radius < b2.radius:
                    powerUps.remove(b1)
                    typePowerUp = random.randint(1, 3)
                    print(typePowerUp)
                    if typePowerUp == 1:
                        pass
                    if typePowerUp == 2:
                        b2.radius = b2.radius * 1.5
                    if typePowerUp == 3:
                        pass
                    print('here')


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

        for ball1 in self.pups:
            for ball2 in self.pups:
                if ball1 != ball2:
                    self.absorb1(ball1, ball2)

        for ball1 in self.pups:
            if ball1.radius < self.player.radius:
                self.absorb1(ball1, self.player)
            if ball1.radius > self.player.radius:
                self.absorb1(ball1, self.player)


    def draw(self, canvas):
        currentArea = str(self.player.radius)
        canvas.draw_text('Current Area: ' + currentArea, [10,480], 24, "White")

        if not pause:
            self.update()
            inter.update()
            Player.update()
            Player.draw(canvas)

            for ball in self.balls:
                ball.draw(canvas)
            for w in self.walls:
                w.draw(canvas)
            for p in self.pups:
                p.draw(canvas)


        else:
            canvas.draw_text("Press 'p' to unpause", [CANVAS_WIDTH / 2 - 100, CANVAS_HEIGHT / 2 - 200], 28, "White")



######

powerUps = []
num_powerups = 5
for i in range(num_powerups):
        rad = 10
        powerUps.append(PowerUps(Vector(RandPosX(rad), RandPosY(rad)),Vector(vel_x(), vel_y()), rad))
        print("fixme")

balls = []
num_balls = 15
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
Player = Player(Vector(CANVAS_WIDTH/2,CANVAS_HEIGHT/2), 12.5)

inter = KBInteraction(Player, kbd) #test player without balls getting in the way
interaction = Interaction(balls, walls, kbd, Player, powerUps)

def play():
    global message, guide_text1, guide_text2, guide_text3, guide_text4, guide_text5, guide_text6, guide_text7, currentArea, currentLives
    message = ""
    lives = 3
    radius = 5
    currentSize = round((pi * radius ** 2), 1)
    currentArea = "Current Size : " + str(currentSize)
    currentLives = "Lives : " + str(lives)
    guide_text1 = ""
    guide_text2 = ""
    guide_text3 = ""
    guide_text4 = ""
    guide_text5 = ""
    guide_text6 = ""
    guide_text7 = ""
    frame.set_draw_handler(interaction.draw)

def guide():
    global message, guide_text1, guide_text2, guide_text3, guide_text4, guide_text5, guide_text6, guide_text7, currentArea, currentLives
    message = ""
    currentArea = ""
    currentLives = ""
    guide_text1 = "The aim of the game is to grow yourself from a small mote"
    guide_text2 = "into as large of a mote as possible. This can be done by"
    guide_text3 = "colliding with smaller motes in order to get bigger. "
    guide_text4 = "However, colliding with a mote than is larger than your "
    guide_text5 = "current size will result in your current life to end."
    guide_text6 = "You will have start with 3 lives, once these lives have"
    guide_text7 = "been used up, the game will end. Have FUN !"

def exitGame():
    global message, guide_text1, guide_text2, guide_text3, guide_text4, guide_text5, guide_text6, guide_text7, currentArea, currentLives
    message = "Thanks for playing!"
    currentLives = ""
    currentArea = ""
    guide_text1 = ""
    guide_text2 = ""
    guide_text3 = ""
    guide_text4 = ""
    guide_text5 = ""
    guide_text6 = ""
    guide_text7 = ""
    exit()

def draw(canvas):
    canvas.draw_text(message, [75,250], 54, "White")
    canvas.draw_text(currentArea, [10,190], 10, "White")
    canvas.draw_text(currentLives, [250,190], 10, "White")
    canvas.draw_text(guide_text1, [40,110], 30, "White")
    canvas.draw_text(guide_text2, [40,140], 30, "White")
    canvas.draw_text(guide_text3, [40,170], 30, "White")
    canvas.draw_text(guide_text4, [40,200], 30, "White")
    canvas.draw_text(guide_text5, [40,230], 30, "White")
    canvas.draw_text(guide_text6, [40,260], 30, "White")
    canvas.draw_text(guide_text7, [40,290], 30, "White")

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" Group 12 python game project ", CANVAS_WIDTH , CANVAS_HEIGHT)
frame.set_canvas_background('Black')
#frame.set_draw_handler(interaction.draw) #only 1 draw handler
frame.add_button("Play", play)
frame.add_button("Guide", guide)
frame.add_button("Exit", exitGame)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_draw_handler(draw)

frame.start()
