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
    if point == 5:
        print("Congratulations! On to level 2.")
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
    screen.fill((0,0,0))
    screen.blit(basket, basket_rect)
    screen.blit(fruit, fruit_rect)
    pygame.display.flip()
    clock.tick(60)
