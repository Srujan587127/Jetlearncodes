import pygame
import os


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("images", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)), 90
)


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("images", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), 270
)


SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "space.png")), (900, 500)
)


