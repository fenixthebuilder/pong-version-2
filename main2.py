from modules.player1 import player1
from modules.player2 import player2
from modules.win import win
from modules.ball import ball

initial_score = 0
end_score = 0

win.listen()
win.onkeypress((player1.up, "w"), (player1.dw, "s"), (player2.up, "Up"), (player2.dw, "Down"))

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.OperationsOnTheBallYCoordinates
    ball.OperationsOnTheBallXCoordinates
    ball.OperationsOnTheBallAndPlayersCoordinates