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

# defining the paddle
paddle = pygame.Surface((100, 20))
paddle.fill((255, 255, 255))
paddle_rect = pygame.Rect(350, 580, 100, 20)

# defining the ball
ball = pygame.Surface((20, 20))
ball.fill((255, 0, 0))
ball_rect = pygame.Rect(200, 200, 20, 20)
#ball_rect.x = random.randint(0, 800 - 20)

# variables
speed = 3
speedB = 10
point = 0
level = 1 #initialize level
clock = pygame.time.Clock()
goingRight = True
goingDown = True
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

    if ball_rect.y == 580:
        print("Score:", point)
        sys.exit(0)
    elif point == 5:
        level = 2
        speed = 5
    elif point == 10:
        level = 3
    elif point == 20:
        level = 4
        speed = 7
    elif point == 35:
        level = 5
    elif point == 50:
        level = 6
        speed = 9
    elif point == 60:
        level = 7
    elif point == 75:
        level = 8
        speed = 11
    elif point == 90:
        level = 9
    elif point == 100:
        level = 10
        speed = 13
    # Render the score and level as text
    score_text = font.render(f'Score: {point}', True, (255,255,255))
    level_text = font.render(f'Level: {level}', True, (255,255,255))


    screen.fill((0, 0, 0))
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    screen.blit(score_text, (10,10))#Display at top left corner
    screen.blit(level_text, (10,50))#Display level below the score
    pygame.display.flip()
    clock.tick(60)
