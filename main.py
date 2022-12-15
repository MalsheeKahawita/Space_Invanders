import pygame
import random
import math

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
enemyX = random.randint(0, 735)
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

score = 0
def player(x, y) :
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet (x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

#checking for boundries of spaceship
    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

#enemy movements

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 1.0
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1.0
        enemyY += enemyY_change

    #bullet Movement added
    if bulletY <= 0:
        bulletY =480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)



    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
