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
resolution = (800,600)

grass = pygame.image.load("Grassland.jpg").convert()
grass = pygame.transform.scale(grass, (800,600))

space = pygame.image.load("Space.jpg").convert()
space = pygame.transform.scale(space, (800,600))

#anotherb background image
desert = pygame.image.load("desert.jpg").convert()
desert = pygame.transform.scale(desert, (800,600))

jungle = pygame.image.load("jungle.jpg").convert()
jungle = pygame.transform.scale(jungle, (800, 600))

tundra = pygame.image.load("Tundra.jpg").convert()
tundra = pygame.transform.scale(tundra, (800, 600))

fire = pygame.image.load("fire.jpg").convert()
fire = pygame.transform.scale(fire, (800, 600))
back = desert

#sounds
win_sound = pygame.mixer.Sound("roblox-victory-sound-made-with-Voicemod.mp3")
win_sound.set_volume(0.3)
pop_sound = pygame.mixer.Sound ("pop-39222.mp3")
pop_sound.set_volume(0.3)
close_sound = pygame.mixer.Sound ("game_close.mp3")
close_sound.set_volume(0.3)


# defining the paddle
paddle = pygame.Surface((100, 20))
paddle.fill((255, 255, 255))
paddle_rect = pygame.Rect(350, 580, 100, 20)


# defining the ball
ball = pygame.Surface((20, 20))
ball.fill((0,255,0))
ball_rect = pygame.Rect(200, 200, 20, 20)


ball2 = pygame.Surface((20, 20))
#ball2.fill((0, 255, 0))
ball2_rect = pygame.Rect(350, 0, 20, 20)
#ball_rect.x = random.randint(0, 800 - 20)

ball3 = pygame.Surface((20, 20))
ball3_rect = pygame.Rect(500, 0, 20, 20)

# variables
speed = 4
speed2 = 4
speed3= 5
speedB = 10
point = 0
level = 1 #initialize level

#blacl/white
increasing = True



color = 0
idk = (0,0)
color_surface = pygame.Surface(idk)

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
goingRight3 = True
goingDown3 = True

font = pygame.font.SysFont(None, 36) #Use default system font, size 36


# while running statement, begins with quit
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            close_sound.play()
            if not pygame.mixer.get_busy():
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
        pop_sound.play()

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
        print("Score:", point, " Try again?")
        close_sound.play()
        sys.exit(0)
    if ball2_rect.y == 580:
        close_sound.play()
        print("Score:", point, " Try again?")
        sys.exit(0)
    if ball3_rect.y == 580:
        close_sound.play()
        print("Score:", point, " Try again?")
        sys.exit(0)

    elif 2 <= point <=3:

            back = grass
            level = 2
            speed = 5

            ball2 = pygame.Surface((20, 20))
            ball2.fill((255,0,0))  # most important line to have this visible?
            pygame.display.flip()
            #clock.tick(60)
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
                pop_sound.play()

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

            if paddle_rect.colliderect(ball_rect) and level == 2 and point == 2:
               win_sound.play()


    elif 4 <= point <=6:

            level = 3
            speed = 6
            back = space

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
                pop_sound.play()

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

            if ball_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)
            if ball2_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

            if paddle_rect.colliderect(ball_rect) and level == 3 and point == 4:
                win_sound.play()
            if paddle_rect.colliderect(ball2_rect) and level == 3 and point == 4:
                win_sound.play()




    elif 7 <= point <=9:

            back = jungle
            level = 4
            speed = 6

            if paddle_rect.colliderect(ball_rect) and point == 7:
                win_sound.play()
            if paddle_rect.colliderect(ball2_rect) and point == 7:
                win_sound.play()
            if paddle_rect.colliderect(ball3_rect) and point == 7:
                win_sound.play()


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
                pop_sound.play()


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


            if ball_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)
            if ball2_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

    elif 10 <= point <=12:
            back = tundra
            level = 5
            speed = 6
            speed2 = 4
            Speed2 = 4


            ball3 = pygame.Surface((20, 20))
            ball3.fill((0, 0, 255))  # most important line to have this visible?
            pygame.display.flip()
            # clock.tick(60)
            if goingDown3:
                ball3_rect = ball3_rect.move(0, speed2)
            else:
                ball3_rect = ball3_rect.move(0, -speed2)

            if ball3_rect.y < 0:
                goingDown3 = True
            # adds point and reflects ball upon collision
            if paddle_rect.colliderect(ball3_rect):
                point += 1
                goingDown3 = False


            # movement of ball right and left across X-axis
            if goingRight3:
                ball3_rect = ball3_rect.move(speed2, 0)
            else:
                ball3_rect = ball3_rect.move(-speed2, 0)
            # borders of right and left screen
            if ball3_rect.x > 780:
                goingRight3 = False
            if ball3_rect.x < 0:
                goingRight3 = True




            if increasing:
                color += 1
            else:
                color -= 1
            if color >= 255:
                increasing = False
            if color <= 0:
                increasing = True


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

            if ball2_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

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

            if ball_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

            if ball2_rect.y > 580:
                print("Score:", point)
                sys.exit(0)
            if ball3_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

            if paddle_rect.colliderect(ball_rect) and level == 5 and point == 10:
                win_sound.play()
            if paddle_rect.colliderect(ball2_rect) and level == 5 and point == 10:
                win_sound.play()
            if paddle_rect.colliderect(ball3_rect) and level == 5 and point == 10:
                win_sound.play()

    elif 13 <= point <=14:
            back = fire
            level = 6
            speed = 8
            speed2 = 6
            speed3 = 4

            ball3 = pygame.Surface((20, 20))
            ball3.fill((0, 0, 255))  # most important line to have this visible?
            pygame.display.flip()
            # clock.tick(60)
            if goingDown3:
                ball3_rect = ball3_rect.move(0, speed3)
            else:
                ball3_rect = ball3_rect.move(0, -speed3)

            if ball3_rect.y < 0:
                goingDown3 = True
            # adds point and reflects ball upon collision
            if paddle_rect.colliderect(ball3_rect):
                point += 1
                goingDown3 = False

            # sends ball up if rect touches very bottom of screen
            # if ball3_rect.y > 580:
            #     ball3_rect.x = random.randint(0, 800 - 20)
            #     ball3_rect.y = 10
            #     point -= 1

            # movement of ball right and left across X-axis
            if goingRight3:
                ball3_rect = ball3_rect.move(speed3, 0)
            else:
                ball3_rect = ball3_rect.move(-speed3, 0)
            # borders of right and left screen
            if ball3_rect.x > 780:
                goingRight3 = False
            if ball3_rect.x < 0:
                goingRight3 = True

            if increasing:
                color += 1
            else:
                color -= 1
            if color >= 255:
                increasing = False
            if color <= 0:
                increasing = True

            if goingDown2:
                ball2_rect = ball2_rect.move(0, speed2)
            else:
                ball2_rect = ball2_rect.move(0, -speed2)

            if ball2_rect.y < 0:
                goingDown2 = True
                # adds point and reflects ball upon collision
            if paddle_rect.colliderect(ball2_rect):
                point += 1
                goingDown2 = False


                # movement of ball right and left across X-axis
            if goingRight2:
                ball2_rect = ball2_rect.move(speed2, 0)
            else:
                ball2_rect = ball2_rect.move(-speed2, 0)
                # borders of right and left screen
            if ball2_rect.x > 780:
                goingRight2 = False
            if ball2_rect.x < 0:
                goingRight2 = True

            if ball_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

            if ball2_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)
            if ball3_rect.y > 580:
                print("Score:", point, " Try again?")
                sys.exit(0)

            if paddle_rect.colliderect(ball_rect) and level == 6 and point == 13:
                win_sound.play()
            if paddle_rect.colliderect(ball2_rect) and level == 6 and point == 13:
                win_sound.play()
            if paddle_rect.colliderect(ball3_rect) and level == 6 and point == 13:
                win_sound.play()

    elif 15 <= point <=17:
                #back = pygame.Surface((0,0))
                level = 7
                speed = 8

                speed2 = 7
                speed3 = 5

                ball3 = pygame.Surface((20, 20))
                ball3.fill((0, 0, 255))  # most important line to have this visible?
                pygame.display.flip()
                # clock.tick(60)
                if goingDown3:
                    ball3_rect = ball3_rect.move(0, speed3)
                else:
                    ball3_rect = ball3_rect.move(0, -speed3)

                if ball3_rect.y < 0:
                    goingDown3 = True
                # adds point and reflects ball upon collision
                if paddle_rect.colliderect(ball3_rect):
                    point += 1
                    goingDown3 = False

                # movement of ball right and left across X-axis
                if goingRight3:
                    ball3_rect = ball3_rect.move(speed3, 0)
                else:
                    ball3_rect = ball3_rect.move(-speed3, 0)
                # borders of right and left screen
                if ball3_rect.x > 780:
                    goingRight3 = False
                if ball3_rect.x < 0:
                    goingRight3 = True

                if increasing:
                    color += 1
                else:
                    color -= 1
                if color >= 255:
                    increasing = False
                if color <= 0:
                    increasing = True

                if goingDown2:
                    ball2_rect = ball2_rect.move(0, speed2)
                else:
                    ball2_rect = ball2_rect.move(0, -speed2)

                if ball2_rect.y < 0:
                    goingDown2 = True
                    # adds point and reflects ball upon collision
                if paddle_rect.colliderect(ball2_rect):
                    point += 1
                    goingDown2 = False

                    # movement of ball right and left across X-axis
                if goingRight2:
                    ball2_rect = ball2_rect.move(speed2, 0)
                else:
                    ball2_rect = ball2_rect.move(-speed2, 0)
                    # borders of right and left screen
                if ball2_rect.x > 780:
                    goingRight2 = False
                if ball2_rect.x < 0:
                    goingRight2 = True

                if ball_rect.y > 580:
                    print("Score:", point, " try again?")
                    sys.exit(0)

                if ball2_rect.y > 580:
                    print("Score:", point," try again?")
                    sys.exit(0)
                if ball3_rect.y > 580:
                    print("Score:", point, " try again?")
                    sys.exit(0)

    elif point == 18:
                    win_sound.play()
                    print("Congratulations ! You won. Score:", point)
                    sys.exit(0)


    # Render the score and level as text
    score_text = font.render(f'Score: {point}', True, (255,255,255))
    level_text = font.render(f'Level: {level}', True, (255,255,255))

    screen.blit(back,(0, 0))

    #screen.fill((color, color, color))
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    screen.blit(ball2, ball2_rect)
    screen.blit(ball3, ball3_rect)

    #ball2 = pygame.Surface((20, 20))
    screen.blit(score_text, (10,10))#Display at top left corner
    screen.blit(level_text, (10,50))#Display level below the score
    pygame.display.flip()
    clock.tick(60)

    #make the paddle smaller as levels progress
