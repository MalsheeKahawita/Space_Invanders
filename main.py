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

def player(x, y):
    screen.blit(playerImg,(x, y))

running = True
while running:

    # adding background colour
    screen.fill((78, 123, 134))

    playerX += 0.2
    playerY +=0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()