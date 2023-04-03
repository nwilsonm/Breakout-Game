#1. crear la interfaz con tkinter
from turtle import *
from bars_brain import *
from paddle_brain import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


bar_colors = ["purple", "green", "yellow", "orange", "red"]
bar_x_position = -335
bar_y_position = 110
bars = []

for color in bar_colors:
    for n in range(1, 8):
        bar = Bar()
        bar.color(color)
        bar.goto(bar_x_position, bar_y_position)
        bar_x_position += 110
        if bar_x_position == 435:
            bar_x_position = -335
            bar_y_position += 30

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


game_is_on = True
while game_is_on:
    screen.update()

screen.mainloop()


#2. crear un clase para el cerebro de las barras de colores que se puede importar al main

#3. crear una clase para la barrita

#4. crear una clase para la bola

#5. crear una clase de Score y (quizá crear un archivo con Pandas para el HighScore)

#6. integrar los elementos en el main