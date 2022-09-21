BALL_COLOR = "white"
from modules.chime import chime
from modules.pen import pen
from modules.player1 import player1
from modules.player2 import player2

class ball(object):
    def __init__(self, turtle,speed, shape, color, penup, goto, dx, dy, xcor, ycor, setx, sety):
        self.turtle = turtle.Turtle()
        self.speed = speed(0)
        self.shape = shape("square")
        self.color = color(BALL_COLOR)
        self.penup = penup()
        self.goto = goto(0, 0)
        self.dx = dx()
        self.dy = dy()
        self.xcor = xcor()
        self.ycor = ycor()
        self.setx = setx()
        self.sety = sety()

    dx = 0.1
    dy = -0.1

def OperationsOnTheBallYCoordinates():
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        chime()
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        chime()   

def OperationsOnTheBallXCoordinates():
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        chime()
        initial_score += 1
        pen.clear()
        pen.writeUpdatedScore()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        end_score += 1
        chime()
        pen.clear()
        pen.writeUpdatedScore()
        
def OperationsOnTheBallAndPlayersCoordinates():
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        chime()
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        chime()