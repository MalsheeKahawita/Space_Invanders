import pygame
import random

#intializr the library
pygame.init()

screen = pygame.display.set_mode((800, 600))

#add tile and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

#add background imag
bgImg = pygame.image.load("game_background.png")

#player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 40

#ready state - can't see bullet on the screen
#fire - bullets are firing
#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x, y) :
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, x+16, y+10)



running = True
while running:

    # adding background colour
    screen.fill((78, 123, 134))

    #ADD BACKGROUND IMAGE
    screen.blit(bgImg, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keystroke check whether it's right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

#checking for boundries of spaceship
    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

#checking for boundries of enemy

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1.0
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1.0
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
