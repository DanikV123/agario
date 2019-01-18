from ball import Ball
from functions import *
import turtle, time, math
from turtle import Turtle, Screen
import random as rnd

turtle.colormode(255)
turtle.tracer(0,2)
turtle.hideturtle()

running = True

loss = turtle.clone()
loss.penup()
loss.speed(100)
loss.goto(0,300)

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

num_of_balls = 1

min_ball_r = 10
max_ball_r = 100

min_ball_dx = -5
max_ball_dx = 5

min_ball_dy = -5
max_ball_dy = 5

BALLS = []

def rnd_color():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    return(r, g, b)

def rnd_values():
    x = rnd.randint(int(-screen_width + max_ball_r), int(screen_width - max_ball_r))
    y = rnd.randint(-screen_height + max_ball_r, screen_height - max_ball_r)

    dx = rnd.randint(min_ball_dx, max_ball_dx)
    while(dx == 0):
        dx = rnd.randint(min_ball_dx, max_ball_dx)

    dy = rnd.randint(min_ball_dy, max_ball_dy)
    while(dy == 0):
        dy = rnd.randint(min_ball_dy, max_ball_dy)

    r = rnd.randint(min_ball_r, max_ball_r)
    while(r == 0):
         r = rnd.randint(min_ball_r, max_ball_r)

    color = rnd_color()
    return([x, y, dx, dy, r, color])

ran = rnd_values()
my_ball = Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])

def move_all_balls(screen_width, screen_height):
    for i in BALLS:
        i.move(screen_width, screen_height)

def check_collision(ball1, ball2):
    if(ball1 == ball2):
       return False

    radii = ball1.r+ball2.r
    x1 = ball1.pos()[0]
    x2 = ball2.pos()[0]
    y1 = ball1.pos()[1]
    y2 = ball2.pos()[1]

    centers = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

    if(radii > centers):
        return(True)
    else:
        return(False)

def check_all_balls_collision():
    all_balls=[]
    all_balls.append(my_ball)
    
    for ball in BALLS:
        all_balls.append(ball)

    for ball_a in all_balls:
        for ball_b in all_balls:
            if(check_collision(ball_a, ball_b) == True):
                r_a = ball_a.r
                r_b = ball_b.r
                
                ran = rnd_values()
                
                if(r_a > r_b):
                    if(ball_b == my_ball):
                        loss.write("YOU DIED" , font=("fantasy",60,"normal"), align="center")
                        time.sleep(5)
                        quit()
                    ball_b.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_a.r = r_a + r_b/2
                else:
                    if(ball_a == my_ball):
                        loss.write("YOU DIED" , font=("fantasy",60,"normal"), align="center")
                        time.sleep(5)
                        quit()
                    ball_a.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_b.r = r_b + r_a/2

def movearound():
    my_ball_x = turtle.getcanvas().winfo_pointerx() - screen_width
    my_ball_y = screen_height - turtle.getcanvas().winfo_pointery()

    right_side_ball = my_ball_x + my_ball.r
    left_side_ball = my_ball_x - my_ball.r
    up_side_ball = my_ball_y + my_ball.r
    down_side_ball = my_ball_y - my_ball.r

    if (right_side_ball < screen_width and left_side_ball > -screen_width and up_side_ball < screen_height and down_side_ball > -screen_height):
        my_ball.goto(my_ball_x, my_ball_y)

    Screen().update()



for i in range(num_of_balls):
    ran = rnd_values()    
    r_ball = Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
    BALLS.append(r_ball)


while(running == True):
    '''
    if(screen_width != turtle.getcanvas().winfo_width()/2 or screen_height != turtle.getcanvas().winfo_height()/2):
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
    '''
    movearound()
    move_all_balls(screen_width, screen_height)
    check_all_balls_collision()
    time.sleep(.1)
        

turtle.mainloop()
