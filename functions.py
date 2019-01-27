import math, turtle, time
from turtle import Turtle, Screen
import random as rnd


loss = turtle.Turtle()
loss.penup()
loss.hideturtle()
loss.speed(100)
loss.goto(0,150)

replay = turtle.Turtle()
replay.penup()
replay.color('green')
replay.hideturtle()
replay.speed(100)
replay.goto(-30,50)

stop = turtle.Turtle()
stop.penup()
stop.color('red')
stop.hideturtle()
stop.speed(100)
stop.goto(100,50)


def rnd_color():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    return(r, g, b)


def rnd_values(screen_width, screen_height):
    min_ball_r = 10
    max_ball_r = 100

    min_ball_dx = -5
    max_ball_dx = 5

    min_ball_dy = -5
    max_ball_dy = 5

    x = rnd.randint(-screen_width + max_ball_r, screen_width - max_ball_r)
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


def move_all_balls(screen_width, screen_height, BALLS):
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

    if(radii >= centers):
        return(True)
    else:
        return(False)

    
def check_all_balls_collision(running, pressed, BALLS, my_ball, screen_width, screen_height):
    all_balls=[]
    all_balls.append(my_ball)
    
    for ball in BALLS:
        all_balls.append(ball)

    for ball_a in all_balls:
        for ball_b in all_balls:
            if(check_collision(ball_a, ball_b) == True):
                r_a = ball_a.r
                r_b = ball_b.r
                
                ran = rnd_values(screen_width, screen_height)

                sc = turtle.Screen()

                #clicked = False 
                
                if(r_a > r_b):
                    if(ball_b == my_ball):
                        sc.clear()
                        loss.write("YOU DIED" , font=("fantasy",60,"normal"), align="center")
                        replay.write("REPLAY" , font=("fantasy",35,"normal"), align="right")
                        stop.write("QUIT" , font=("fantasy",35,"normal"), align="left")
                        
                        '''
                        while(clicked != True):
                            stop.onclick()
                        '''
                        
                    ball_b.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_a.r = r_a + r_b/50
                    ball_a.shapesize(ball_a.r/10)
                    print(ball_a.r)
                else:
                    if(ball_a == my_ball):
                        sc.clear()
                        loss.write("YOU DIED" , font=("fantasy",60,"normal"), align="center")
                        replay.write("REPLAY" , font=("fantasy",35,"normal"), align="right")
                        stop.write("QUIT" , font=("fantasy",35,"normal"), align="left")
                        
                        '''
                        while(clicked != True):
                            #stop.onclick() 
                        '''

                    ball_a.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_b.r = r_b + r_a/50
                    ball_b.shapesize(ball_b.r/10)
                    print(ball_b.r)
 
    

def movearound(screen_height, screen_width, my_ball):
    my_ball_x = turtle.getcanvas().winfo_pointerx() - screen_width*2
    my_ball_y = screen_height*1.5 - turtle.getcanvas().winfo_pointery()

    right_side_ball = my_ball_x + my_ball.r
    left_side_ball = my_ball_x - my_ball.r
    up_side_ball = my_ball_y + my_ball.r
    down_side_ball = my_ball_y - my_ball.r

    if (right_side_ball < screen_width and left_side_ball > -screen_width and up_side_ball < screen_height and down_side_ball > -screen_height):
        my_ball.goto(my_ball_x, my_ball_y)

    Screen().update()


