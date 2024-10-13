from itertools import filterfalse
from posix import PRIO_PGRP

import pygame
import random
import sys
from pygame.locals import *

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

basket_width, basket_height = 100, 20
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - basket_height - 20
basket_speed = 10

basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height )
basket_surface = pygame.Surface((100,20))
basket_surface.fill(white)

fruit_width, fruit_height = 20, 20
fruit_speed = 3
fruit_x= random.randint(0,screen_width - fruit_width)
fruit_y = 0

fruit_rect = pygame.Rect(fruit_x, fruit_y, fruit_width, fruit_height)
fruit_surface = pygame.Surface((20,20))
fruit_surface.fill(red)

score = 0

clock = pygame.time.Clock()

def check_quit():
    if event.type == QUIT:
        sys.exit()
    if keys[pygame.K_ESCAPE]:
        sys.exit()

running = True
while running:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        check_quit()
# left and right keys = movement
    if keys[pygame.K_LEFT] and basket_rect.x >=0:
        basket_rect.x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_rect.x <=700:
        basket_rect.x += basket_speed

    if fruit_rect.y >= 0:
        fruit_rect.y += fruit_speed
    if fruit_rect.y > screen_height - fruit_height:
        fruit_rect.x = random.randint(0, screen_width - fruit_width)
        fruit_rect.y = 0

    if fruit_rect.colliderect(basket_rect):
        fruit_rect.y = 0
        fruit_rect.x = random.randint(0,screen_width - fruit_width)
        score+=1
        print("score: ",score)


# fruit is caught

    screen.fill((0, 0, 0))
    screen.blit(basket_surface,basket_rect )
    screen.blit(fruit_surface, fruit_rect)

    pygame.display.flip()
    clock.tick(60)

#yooooooo
# bing bong
