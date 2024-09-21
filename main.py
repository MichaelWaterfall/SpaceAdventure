import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Adventure")

moving_left = False
moving_right = False
moving_down = False
moving_up = False

#player creation
player = Character(100, 100)

run = True
while run:

    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("left")
            if event.key == pygame.K_d:
                print("right")
            if event.key == pygame.K_w:
                print("up")
            if event.key == pygame.K_s:
                print("down")
    
    pygame.display.update()

pygame.quit()