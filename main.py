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

def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

player_image = pygame.image.load("not added yet").convert_alpha()
player_image = scale_img(player_image, constants.SCALE)

animation_types = ["idle", "run"]
animation_list = []

for animation in animation_types:
    temp_list = []
    for i in range(4):
        img = pygame.image.load(f"{animation_types}{i}").convert_alpha()
        img = scale_img(img, constants.SCALE)
        temp_list.append(img)
    animation_list.append(img)

#player creation
player = Character(100, 100, animation_list)

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

    player.update()

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