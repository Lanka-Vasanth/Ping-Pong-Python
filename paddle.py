from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)

    def go_up(self):
        newy=self.ycor()+30
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy=self.ycor()-30
        self.goto(self.xcor(), newy)