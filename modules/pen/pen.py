PEN_COLOR = "white"

initial_score = 0
end_score = 0

class pen(object):
    def __init__(self, turtle, speed, color, penup, hideturtle, goto, write, clear):
        self.turtle = turtle.Turtle()
        self.speed = speed(0)
        self.color = color(PEN_COLOR)
        self.penup = penup()
        self.hideturtle = hideturtle()
        self.goto = goto(0, 260)
        self.write = write("Giocatore 1: 0  Giocatore 2: 0", align="center", font=("Sans Serif", 24, "normal"))
        self.clear = clear()
    
    def writeUpdatedScore():
        pen.write("Giocatore 1: {}  Giocatore 2: {}".format(initial_score, end_score), align="center", font=("Sans Serif", 24, "normal"))