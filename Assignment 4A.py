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
clock = pygame.time.Clock()
goingRight = True
goingDown = True

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
# without the break, line 76 would print endlessly, perhaps create a method?
    if ball_rect.y == 580:
        print("Score:", point)
        sys.exit(0)
    if point == 5:
        print("Congratulations! On to level 2.")
        break
    if point == 10:
        print("Congratulations! On to level 3.")
    if point == 20:
        print("Congratulations! On to level 4.")
    if point == 35:
        print("Congratulations! On to level 5.")
    if point == 50:
        print("Congratulations! On to level 6.")
    if point == 60:
        print("Congratulations! On to level 7.")
    if point == 75:
        print("Congratulations! On to level 8.")
    if point == 90:
        print("Congratulations! On to level 9.")
    if point == 100:
        print("Congratulations! On to level 10.")

    screen.fill((0, 0, 0))
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
    clock.tick(60)
