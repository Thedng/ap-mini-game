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
target1 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1), 'icon/target.png')
target2 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1), 'icon/target.png')
target3 = gameObjects.target(round(random.randrange(50, 800), -1), round(random.randrange(50, 600), -1), 'icon/target.png')

#creat player object
player1 = gameObjects.Player(round(random.randrange(50, 800), -1), round(random.randrange(50, 600),-1), 'icon/blue-dot.png')
player2 = gameObjects.Player(round(random.randrange(50, 800), -1), round(random.randrange(50, 600),-1), 'icon/red-dot.png')

#display target objects
def show_object(targets):
    screen.blit(pygame.image.load(targets.icon), (targets.positionx, targets.positiony))


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #move player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.positionx -= 10
            if event.key == pygame.K_RIGHT:
                player1.positionx += 10
            if event.key == pygame.K_UP:
                player1.positiony -= 10
            if event.key == pygame.K_DOWN:
                player1.positiony += 10

        #move player 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2.positiony -= 10
            if event.key == pygame.K_s:
                player2.positiony += 10
            if event.key == pygame.K_a:
                player2.positionx -= 10
            if event.key == pygame.K_d:
                player2.positionx += 10
    #set background color
    screen.fill((255, 255, 255))

    #display objects
    show_object(target1)
    show_object(target2)
    show_object(target3)
    show_object(player1)
    show_object(player2)
    pygame.display.update()
