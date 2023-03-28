#1. crear la interfaz con tkinter
from bars_brain import *

window = Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

bar_colors = ["purple", "green", "yellow", "orange", "red"]
bar_x_position = -335
bar_y_position = 0
bar = Bar()

for color in bar_colors:
    for n in range(1, 8):
        bar = Bar()
        bar.color(color)
        bar.goto(bar_x_position, bar_y_position)
        bar_x_position += 110
        if bar_x_position == 435:
            bar_x_position = -335
            bar_y_position += 30
    window.update()









window.mainloop()


#2. crear un clase para el cerebro de las barras de colores que se puede importar al main

#3. crear una clase para la barrita

#4. crear una clase para la bola

#5. crear una clase de Score y (quizá crear un archivo con Pandas para el HighScore)

#6. integrar los elementos en el main