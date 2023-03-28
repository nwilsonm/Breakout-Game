from turtle import *


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=5)
        self.shape("square")
        self.color("yellow")

    def dissapear(self):
        None



class BarDos(Turtle):
    def __int__(self):
        super().__int__()
        self.penup()
        self.color("white")
        self.shape("square")

# green_bars = Turtle()
# green_bars.shape("square")
# green_bars.color("green")
# green_bars.shapesize(stretch_len=5)


#1. crear las barras de colores y ordenarlas en filas. SUPER CLASS from TURTLE

#2. crear funcion para que desaparezcan si la bola las toca (distancia eje y=0)