import math
import random
import pygame
import gameObjects

#creating target objects
target1 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1), 'icon/target.png')
target2 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1), 'icon/target.png')
target3 = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1), 'icon/target.png')
bonus_target = gameObjects.target(round(random.randrange(50, 750), -1), round(random.randrange(50, 550), -1), 'icon/؟.png')
#getting players name
pn1 = input('enter name of first player')
pn2 = input('enter name of second player')

#creat player object
player1 = gameObjects.Player(pn1,round(random.randrange(50, 750), -1), round(random.randrange(50, 550),-1), 'icon/blue-dot.png')
player2 = gameObjects.Player(pn2,round(random.randrange(50, 750), -1), round(random.randrange(50, 550),-1), 'icon/red-dot.png')


#intialize pygame
pygame.init()

#creat the screen
screen = pygame.display.set_mode((800, 700))

#game icon & title
pygame.display.set_caption("Mini Game")
pygame.display.set_icon(pygame.image.load('icon/gun.png'))


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
    elif distance(player,bonus_target) < 13:
        return([True,bonus_target])
    return([False,None])

#show timer and scores
font = pygame.font.Font('freesansbold.ttf', 18)

def display_game_stats(player,timer,score,bullets,positionx,positiony):
    game_stats = font.render(f'{player} - score : {score} - timer : {timer} - bullets: {bullets}', True, (0,0,0))
    screen.blit(game_stats, (positionx, positiony))

#game loop
running = True

# Create a clock object to manage time
clock = pygame.time.Clock()

# Initialize the last tick
last_tick = pygame.time.get_ticks()

while running:
    # Get the current time
    current_tick = pygame.time.get_ticks()

    # Check if one second has passed
    if current_tick - last_tick >= 1000:
        player1.timer -= 1
        player2.timer -= 1
        last_tick = current_tick


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
                    elif res[1] == bonus_target :
                        player1.set_bonus()
                    else:
                        player1.set_score(player1.shots[len(player1.shots) - 2],player1.shots[len(player1.shots) - 1])
                    player1.lastShot = True
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
                    elif res[1] == bonus_target :
                        player2.set_bonus()
                    else:
                        player2.set_score(player2.shots[len(player2.shots) - 2], player2.shots[len(player2.shots) - 1])
                    player2.lastShot = True
                else:
                    player1.lastShot = False

    #set background color
    screen.fill((255, 255, 255))

    #display objects
    show_object(target1)
    show_object(target2)
    show_object(target3)
    show_object(bonus_target)
    for i in player1.shots[1:]:
        show_shots(player1, (i[0],i[1]))
    for i in player2.shots[1:]:
        show_shots(player2, (i[0],i[1]))
    display_game_stats(player1.name,player1.timer,player1.score,player1.bullets, 40,650)
    display_game_stats(player2.name, player2.timer, player2.score, player2.bullets, 450, 650)
    pygame.display.update()
