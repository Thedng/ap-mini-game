import pygame

#intialize pygame
pygame.init()

#creat the screen
screen = pygame.display.set_mode((800, 600))

#game icon & title
pygame.display.set_caption("Mini Game")
pygame.display.set_icon(pygame.image.load('icon/gun.png'))

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #set background color
    screen.fill((255, 255, 255))
    pygame.display.update()