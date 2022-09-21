WIDTH = 800
HEIGHT = 600
WIN_BGCOLOR = "black"

class win(object):
    def __init__(self, turtle, title, bgcolor, setup, tracer, listen, onkeypress, update):
        self.turtle = turtle.Screen()
        self.title = title("PONG")
        self.bgcolor = bgcolor(WIN_BGCOLOR)
        self.setup = setup(WIDTH, HEIGHT)
        self.tracer = tracer(0)
        self.listen = listen()
        self.onkeypress = onkeypress()
        self.update = update()

