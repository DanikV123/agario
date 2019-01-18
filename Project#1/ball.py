from turtle import *
from turtle import Turtle, Screen

class Ball(Turtle):
    
    def __init__(self,  x, y, dx, dy, r, color):
        Turtle.__init__(self)
        
        self.penup()
        self.goto(x, y)
        self.shape("circle")
        self.color(color)
        
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shapesize(self.r/10)

    def move(self, screen_width, screen_height):
        current_x = self.position()[0]
        new_x = current_x + self.dx

        current_y = self.position()[1]
        new_y = current_y + self.dy

        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        up_side_ball = new_y + self.r
        down_side_ball = new_y - self.r

        self.goto(new_x,new_y)

        if(right_side_ball > screen_width or left_side_ball < -screen_width):
            self.dx = -self.dx
            if right_side_ball>screen_width:
                self.goto(screen_width-self.r,current_y+self.dy)
            if left_side_ball<-screen_width:
                self.goto(-screen_width+self.r,current_y+self.dy)

        if(up_side_ball > screen_height or down_side_ball < -screen_height):
            self.dy = -self.dy
            if up_side_ball>screen_height:
                self.goto(current_x+self.dx,screen_height-self.r)
            if down_side_ball<-screen_height:
                self.goto(current_x+self.dx,-screen_height+self.r)
            

    def new_Ball(self,  x, y, dx, dy, r, color):
        self.goto(x, y)
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        self.penup()
        
        
        self.dx = dx
        self.dy = dy
        self.r = r
