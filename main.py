import random

import pygame
import gameObjects

#intialize pygame
pygame.init()

#creat the screen
screen = pygame.display.set_mode((800, 600))

#game icon & title
pygame.display.set_caption("Mini Game")
pygame.display.set_icon(pygame.image.load('icon/gun.png'))

#creating game objects
target1 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1))
target2 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1))
target3 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1))


#display target objects
def target(targets):
    screen.blit(pygame.image.load(targets.icon), targets.position)


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #set background color
    screen.fill((255, 255, 255))

    target(target1)
    target(target2)
    target(target3)
    pygame.display.update()
