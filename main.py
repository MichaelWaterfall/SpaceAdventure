import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Adventure")

clock = pygame.time.Clock()

moving_left = False
moving_right = False
moving_down = False
moving_up = False

player_image = pygame.image.load("not added yet").convert_alpha()

#player creation
player = Character(100, 100)

run = True
while run:

    clock.tick(constants.FPS)
    screen.fill(constants.BG)
    dx = 0
    dy = 0
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED

    player.move(dx, dy)
    print(str(dx), str(dy))

    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
    
    pygame.display.update()

pygame.quit()