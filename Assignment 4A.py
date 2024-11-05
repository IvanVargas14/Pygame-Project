#Class: CSE 1321
#Section: BD
#Term: Fall 2024
#Instructor: Mamo
#Name: Jakob Shelton, Ivan, Ramone, Kellen
#Pygame Project

import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
#
# def spawn_ball():
#     size = 20
#     side = (["top"])
#     speed2 = speed + (currentime + 5000)
#
#     if side == "top":
#         ball_rect = pygame.Rect(random.randint(0,800-size),0 , size , size )
#         dx = 0
#         dy = speed3
#     list_of_balls.append((ball_rect, dx, dy))
#
#
# def update_screen():
#     for ball, _, _ in list_of_balls:
#         pygame.draw.rect(screen, color(random_color), meteor)
#

def generate_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

random_color = generate_random_color()


# defining the paddle
paddle = pygame.Surface((100, 20))
paddle.fill((255, 255, 255))
paddle_rect = pygame.Rect(350, 580, 100, 20)


# defining the ball
ball = pygame.Surface((20, 20))
ball.fill((random_color))
ball_rect = pygame.Rect(200, 200, 20, 20)


ball2 = pygame.Surface((20, 20))
#ball2.fill((0, 255, 0))
ball2_rect = pygame.Rect(400, 0, 20, 20)
#ball_rect.x = random.randint(0, 800 - 20)


# variables
speed = 3
speedB = 10
point = 0
level = 1 #initialize level


# time variables
survival_time = 0
currentime = pygame.time.get_ticks()
clock = pygame.time.Clock()


#lists
list_of_balls = []


# going signs
goingRight = True
goingDown = True
goingRight2 = True
goingDown2 = True
font = pygame.font.SysFont(None, 36) #Use default system font, size 36


# while running statement, begins with quit
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Score:", point)
            sys.exit(0)
#movement of paddle
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
        paddle_rect.x -= speedB
    if keys[pygame.K_RIGHT] and paddle_rect.right < 800:
        paddle_rect.x += speedB

#movement of ball up and down y-axis
    if goingDown:
        ball_rect = ball_rect.move(0,speed)
    else:
         ball_rect = ball_rect.move(0, -speed)


    if ball_rect.y < 0:
        goingDown = True
# adds point and reflects ball upon collision
    if paddle_rect.colliderect(ball_rect):
        point += 1
        goingDown = False

# sends ball up if rect touches very bottom of screen
    if ball_rect.y > 580:
        ball_rect.x = random.randint(0, 800 - 20)
        ball_rect.y = 10
        point -= 1

#movement of ball right and left across X-axis
    if goingRight:
        ball_rect = ball_rect.move(speed,0)
    else:
         ball_rect = ball_rect.move(-speed, 0)
#borders of right and left screen
    if ball_rect.x > 780:
        goingRight = False
    if ball_rect.x < 0:
        goingRight = True

# transition between levels
    # maybe have a for statement, saying for every i of level, clear list?

    if ball_rect.y == 580:
        print("Score:", point)
        sys.exit(0)
    elif 2 <= point <=3:

            level = 2
            speed = 5
            ball2 = pygame.Surface((20, 20))
            ball2.fill((255,0,0))  # most important line to have this visible?
            pygame.display.flip()
            clock.tick(60)
            if goingDown2:
                ball2_rect = ball2_rect.move(0, speed)
            else:
                ball2_rect = ball2_rect.move(0, -speed)

            if ball2_rect.y < 0:
                goingDown2 = True
            # adds point and reflects ball upon collision
            if paddle_rect.colliderect(ball2_rect):
                point += 1
                goingDown2 = False

            # sends ball up if rect touches very bottom of screen
            if ball2_rect.y > 580:
                ball2_rect.x = random.randint(0, 800 - 20)
                ball2_rect.y = 10
                point -= 1

            # movement of ball right and left across X-axis
            if goingRight2:
                ball2_rect = ball2_rect.move(speed, 0)
            else:
                ball2_rect = ball2_rect.move(-speed, 0)
            # borders of right and left screen
            if ball2_rect.x > 780:
                goingRight2 = False
            if ball2_rect.x < 0:
                goingRight2 = True

    elif 4 <= point <=6:
        level = 3
        speed = 6

        if goingDown2:
            ball2_rect = ball2_rect.move(0, speed)
        else:
            ball2_rect = ball2_rect.move(0, -speed)

        if ball2_rect.y < 0:
            goingDown2 = True
        # adds point and reflects ball upon collision
        if paddle_rect.colliderect(ball2_rect):
            point += 1
            goingDown2 = False

        # sends ball up if rect touches very bottom of screen
        if ball2_rect.y > 580:
            ball2_rect.x = random.randint(0, 800 - 20)
            ball2_rect.y = 10
            point -= 1

        # movement of ball right and left across X-axis
        if goingRight2:
            ball2_rect = ball2_rect.move(speed, 0)
        else:
            ball2_rect = ball2_rect.move(-speed, 0)
        # borders of right and left screen
        if ball2_rect.x > 780:
            goingRight2 = False
        if ball2_rect.x < 0:
            goingRight2 = True

        #list_of_balls.clear()
    elif 7 <= point <=9:
        level = 4
        speed = 6.1

        # include flashing black and white screen

        if goingDown2:
            ball2_rect = ball2_rect.move(0, speed)
        else:
            ball2_rect = ball2_rect.move(0, -speed)

        if ball2_rect.y < 0:
            goingDown2 = True
            # adds point and reflects ball upon collision
        if paddle_rect.colliderect(ball2_rect):
            point += 1
            goingDown2 = False

            # sends ball up if rect touches very bottom of screen
        if ball2_rect.y > 580:
            ball2_rect.x = random.randint(0, 800 - 20)
            ball2_rect.y = 10
            point -= 1

            # movement of ball right and left across X-axis
        if goingRight2:
            ball2_rect = ball2_rect.move(speed, 0)
        else:
            ball2_rect = ball2_rect.move(-speed, 0)
            # borders of right and left screen
        if ball2_rect.x > 780:
            goingRight2 = False
        if ball2_rect.x < 0:
            goingRight2 = True

    elif 10 <= point <11:
        level = 5
    elif 12 <= point <13:
        level = 6
        speed = 8
    elif 14 <= point <15:
        level = 7
        speed = 9
    # Render the score and level as text
    score_text = font.render(f'Score: {point}', True, (255,255,255))
    level_text = font.render(f'Level: {level}', True, (255,255,255))


    screen.fill((0, 0, 0))
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    screen.blit(ball2, ball2_rect)

    #ball2 = pygame.Surface((20, 20))
    screen.blit(score_text, (10,10))#Display at top left corner
    screen.blit(level_text, (10,50))#Display level below the score
    pygame.display.flip()
    clock.tick(60)
