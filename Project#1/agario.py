from ball import Ball
from functions import *
import turtle, time, math
from turtle import Turtle, Screen
import random as rnd

turtle.colormode(255)
turtle.tracer(0,2)
turtle.hideturtle()

running = True

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

num_of_balls = 3

BALLS = []

ran = rnd_values(screen_width, screen_height)
my_ball = Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])

for i in range(num_of_balls):
    all_balls=[]
    all_balls.append(my_ball)
    
    for ball in BALLS:
        all_balls.append(ball)

    ran = rnd_values(screen_width, screen_height)
    r_ball = Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
    
    for x in range(len(all_balls)):
        ball = all_balls[x]
        if(check_collision(ball, r_ball) != True):
             BALLS.append(r_ball)
             all_balls.append(r_ball)
        else:
            i -= 1
            break

while(running == True):
    if(screen_width != turtle.getcanvas().winfo_width()/2 or screen_height != turtle.getcanvas().winfo_height()/2):
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
        
    movearound(screen_height, screen_width, my_ball)
    move_all_balls(screen_width, screen_height, BALLS)
    check_all_balls_collision(BALLS, my_ball, screen_width, screen_height)
    time.sleep(0.1)
        
turtle.mainloop()
