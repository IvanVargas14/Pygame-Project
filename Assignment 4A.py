import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

basket = pygame.Surface((100,20))
basket.fill((255,255,255))

fruit = pygame.Surface((20,20))
fruit.fill((255,0,0))

basket_rect = pygame.Rect(350,580,100,20)
fruit_rect = pygame.Rect(200,200,20,20)
fruit_rect.x = random.randint(0, 800 - 20)
speed = 3
speedB = 10
point = 0
clock = pygame.time.Clock()
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Score:", point)
            sys.exit(0)

    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.x -= speedB
    if keys[pygame.K_RIGHT] and basket_rect.right < 800:
        basket_rect.x += speedB
    fruit_rect.y += 3
    if basket_rect.colliderect(fruit_rect):
        point += 1
        fruit_rect.x = random.randint(0, 800 - 20)
        fruit_rect.y = 10
    if fruit_rect.y >= 600:
        print("Score:", point)
        sys.exit(0)

    screen.fill((0,0,0))
    screen.blit(basket, basket_rect)
    screen.blit(fruit, fruit_rect)
    pygame.display.flip()
    clock.tick(60)
