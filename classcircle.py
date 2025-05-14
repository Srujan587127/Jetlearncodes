import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three Circles")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


circle1 = Circle(150, 200, 40, RED)
circle2 = Circle(300, 200, 50, GREEN)
circle3 = Circle(450, 200, 30, BLUE)

running = True
while running:
    screen.fill(WHITE)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    circle1.draw(screen)
    circle2.draw(screen)
    circle3.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
