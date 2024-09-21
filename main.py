import pygame
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.caption("Space Adventure")

#player creation
player = Character(100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False

pygame.quit()