import pygame
import time
import sys

pygame.init()


WIDTH = 600
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Card")


WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

page1 = pygame.image.load("images/santa merry christmas.jpg")
page1 = pygame.transform.scale(page1, (WIDTH, HEIGHT))

tree = pygame.image.load("images/christmas tree.png")
tree = pygame.transform.scale(tree, (150, 200))

presents = pygame.image.load("images/christmass presents.png")
presents = pygame.transform.scale(presents, (200, 100))


title_font = pygame.font.SysFont("times new roman", 60, bold=True)
msg_font = pygame.font.SysFont("arial", 30)


title_text = title_font.render("Merry Christmas!", True, GOLD)
msg_text = msg_font.render("Wishing you joy, peace, and presents!", True, WHITE)


display_surface.blit(page1, (0, 0))
pygame.display.update()
time.sleep(3)  


display_surface.fill((0, 0, 0))  
display_surface.blit(tree, (50, 350))
display_surface.blit(presents, (350, 450))
display_surface.blit(title_text, (100, 50))
display_surface.blit(msg_text, (60, 130))
pygame.display.update()
time.sleep(5)  


pygame.quit()
sys.exit()
