import pygame

#intializr the library
pygame.init()

screen = pygame.display.set_mode((800, 600))

#add tile and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg,(playerX, playerY))

running = True
while running:

    # adding background colour
    screen.fill((78, 123, 134))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()