STRETCH_WIDTH = 5
STRETCH_LENGTH = 1
PADDLE_COLOR= "white"

class player1(object):
    def __init__(self, turtle, speed, shape, shapesize, color, penup, goto, ycor, sety):
        self.turtle = turtle.Turtle()
        self.speed = speed(0)
        self.shape = shape("square")
        self.shapesize= shapesize(STRETCH_WIDTH, STRETCH_LENGTH)
        self.color = color(PADDLE_COLOR)
        self.penup = penup()
        self.goto = goto(-350, 0)
        self.ycor = ycor()
        self.sety = sety()
    

def up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def dw():
    y = player1.ycor()
    y -= 20
    player1.sety(y)
    
