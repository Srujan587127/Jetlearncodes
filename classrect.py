import pygame, sys
from pygame.locals import QUIT
from random import randint

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Hello World")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("white")
pygame.display.update()
while True:

    class Rect():
        def __init__(self,color,dimensions):
            self.rect_surf = screen
            self.rect_color = color
            self.rect_dimensions = dimensions

        def draw(self):
            self.Draw_Rect = pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimensions)

    greenRect=Rect(green,(50,20,100,100))
    redRect=Rect(red,(150,200,150,150))
    blueRect=Rect(blue,(300,400,200,200))

    greenRect.draw()
    blueRect.draw()
    redRect.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
