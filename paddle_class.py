from turtle import Turtle



class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        

    
        

    def move_up(self):
        new_y_cord = self.ycor() + 20
        if new_y_cord < 260:
            self.goto(self.xcor(), new_y_cord )

    def move_down(self):
        new_y_cord = self.ycor() - 20
        if new_y_cord > -245:
            self.goto(self.xcor(), new_y_cord )

    
    