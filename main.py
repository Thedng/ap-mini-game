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
    res = math.sqrt(((obj1.positionx-2)-(obj2.positionx-11))** 2 + ((obj1.positiony-2)-(obj2.positiony-11))** 2)
    return res

#check if target is hit
def is_hit(player):
    if distance(player,target1) < 10:
        return([True,target1])
    elif distance(player,target2) < 10:
        return([True,target2])
    elif distance(player,target3) < 10:
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
                player1.move(True,False)
            if event.key == pygame.K_RIGHT and player1.positionx < 780:
                player1.move(True,True)
            if event.key == pygame.K_UP and player1.positiony > 0:
                player1.move(False,False)
            if event.key == pygame.K_DOWN and player1.positiony < 580:
                player1.move(False, True)

            #player 1 shoot target
            if event.key == pygame.K_SPACE  and player1.bullets > 0 and player1.timer > 0:
                player1.shoot()
                res = is_hit(player1)
                if res[0]:
                    res[1].set_position()
                    if player1.lastShot:
                        player1.score_prize()
                    else:
                        player1.set_score(player1.shots[len(player1.shots) - 2],player1.shots[len(player1.shots) - 1])
                    player1.lastShot = True
                    print(player1.score)
                else:
                    player1.lastShot = False
            #move player 2 and limit
            if event.key == pygame.K_a and player2.positionx > 0:
                player2.move(True, False)
            if event.key == pygame.K_d and player2.positionx < 780:
                player2.move(True, True)
            if event.key == pygame.K_w and player2.positiony > 0:
                player2.move(False, False)
            if event.key == pygame.K_s and player2.positiony < 580:
                player2.move(False, True)

            # player 2 shoot target
            if event.key == pygame.K_x and player2.bullets > 0 and player2.timer > 0:
                player2.shoot()
                res = is_hit(player2)
                if res[0]:
                    res[1].set_position()
                    if player2.lastShot:
                        player2.score_prize()
                    else:
                        player2.set_score(player2.shots[len(player2.shots) - 2], player2.shots[len(player2.shots) - 1])
                    player2.lastShot = True
                    print(player2.score)
                else:
                    player1.lastShot = False

    #set background color
    screen.fill((255, 255, 255))

    #display objects
    show_object(target1)
    show_object(target2)
    show_object(target3)
    for i in player1.shots[1:]:
        show_shots(player1, (i[0],i[1]))
    for i in player2.shots[1:]:
        show_shots(player2, (i[0],i[1]))
    pygame.display.update()
