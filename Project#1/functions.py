import random, math, turtle


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)


def random_values():
    x = random.randint(-screen_width + max_ball_r, screen_width - max_ball_r)
    y = random.randint(-screen_height + max_ball_r, screen_height - max_ball_r)

    dx = random.randint(min_ball_dx, max_ball_dx)
    while(dx == 0):
        dx = random.randint(min_ball_dx, max_ball_dx)

    dy = random.randint(min_ball_dy, max_ball_dy)
    while(dy == 0):
        dy = random.randint(min_ball_dy, max_ball_dy)

    r = random.randint(min_ball_r, max_ball_r)
    while(r == 0):
         r = random.randint(min_ball_r, max_ball_r)

    color = random_color()
    return([x, y, dx, dy, r, color])


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
                
                ran = random_values()
                
                if(r_a > r_b):
                    if(ball_b == my_ball):
                        #running = False
                        exit()
                    ball_b.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_a.r = r_a + 1
                else:
                    if(ball_a == my_ball):
                        #running = False
                        exit()
                    ball_a.new_Ball(ran[0], ran[1], ran[2], ran[3], ran[4], ran[5])
                    ball_b.r = r_b + 1


def movearound():
    my_ball_x = turtle.getcanvas().winfo_pointerx() - screen_width
    my_ball_y = screen_height - turtle.getcanvas().winfo_pointery()

    my_ball.goto(my_ball_x, my_ball_y)

    Screen().update()

