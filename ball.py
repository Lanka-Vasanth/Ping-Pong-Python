from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(0.75,0.75)
        self.x_move=5
        self.y_move=5
    
    def move(self):
        newx=self.xcor()+self.x_move
        newy=self.ycor()+self.y_move
        self.goto(newx,newy)
    
    def bouncewall(self):
        self.y_move=self.y_move*-1
    
    def bouncepaddle(self):
        self.x_move=self.x_move*-1
    
    def new(self):
        self.goto(0,0)
        self.x_move=self.x_move*-1