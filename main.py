import math
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

#display game objects
def show_object(obj):
    screen.blit(pygame.image.load(obj.icon), (obj.positionx, obj.positiony))
def show_shots(obj,position):
    screen.blit(pygame.image.load(obj.icon), position)

#calculate distance
def distance(obj1,obj2):
    res = math.sqrt((obj1.positionx-obj2.positionx)  2 + (obj1.positiony-obj2.positiony)  2)
    return res

#check if target is hit
def is_hit(player):
    if distance(player,target1) < 20:
        return([True,target1])
    elif distance(player,target2) < 20:
        return([True,target2])
    elif distance(player,target3) < 20:
        return([True,target3])
    return([False,None])

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #move player 1 and limit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player1.positionx > 0:
                player1.positionx -= 10
            if event.key == pygame.K_RIGHT and player1.positionx < 780:
                player1.positionx += 10
            if event.key == pygame.K_UP and player1.positiony > 0:
                player1.positiony -= 10
            if event.key == pygame.K_DOWN and player1.positiony < 580:
                player1.positiony += 10
            #player 1 shoot
            if event.key == pygame.K_SPACE:
                player1.shoot()
                res = is_hit(player1)
                if res[0]:
                    res[1].positionx = round(random.randrange(50, 800), -1)
                    res[1].positiony = round(random.randrange(50, 600), -1)
                    player1.set_score(player1.shots[len(player1.shots) - 2],player1.shots[len(player1.shots) - 1])

        #move player 2 and limit
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player2.positiony > 0:
                player2.positiony -= 10
            if event.key == pygame.K_s and player2.positiony < 580:
                player2.positiony += 10
            if event.key == pygame.K_a and player2.positionx > 0:
                player2.positionx -= 10
            if event.key == pygame.K_d and player2.positionx < 780:
                player2.positionx += 10
            #player 2 shoot
            if event.key == pygame.K_x:
                player2.shoot()


    #set background color
    screen.fill((255, 255, 255))

    #display objects
    show_object(target1)
    show_object(target2)
    show_object(target3)
    for i in player1.shots:
        show_shots(player1, (i[0],i[1]))
    for i in player2.shots:
        show_shots(player2, (i[0],i[1]))
    pygame.display.update()
