from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Title(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write("Pong",align=ALIGNMENT, font=FONT)


