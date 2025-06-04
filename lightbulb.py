import pygame

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Switch")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

bulb_on = False
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if 150 < mx < 250 and 300 < my < 350:
                bulb_on = not bulb_on

    pygame.draw.circle(screen, YELLOW if bulb_on else GRAY, (200, 150), 50)
    pygame.draw.rect(screen, BLACK, (150, 300, 100, 50))
    font = pygame.font.SysFont(None, 30)
    text = font.render("Switch", True, WHITE)
    screen.blit(text, (165, 315))

    pygame.display.flip()

pygame.quit()