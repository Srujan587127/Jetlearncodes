import random 
from random import randint
from time import time
import pgzrun
WIDTH = 600
HEIGHT = 600
satelites = []
lines = []
next_satelite = 0
start_time = 0
end_time = 0
total_time = 0
number_satelites = 8

def create_satelites():
    global start_time
    for count in range (0,9):
        satelite = Actor("satelite")
        satelite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        satelites.append(satelite)
    start_time = time()
    
def draw():
    global total_time
    screen.blit("starry", (0,0))
    number = 1
    for satelite in satelites:
        screen.draw.text(str(number),(satelite.pos[0], satelite.pos[1] + 20))
        satelite.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next_satelite < number_satelites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)

def on_mouse_down(pos):
    global next_satelite, lines
    if next_satelite < number_satelites:
        if satelites [next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((satelites[next_satelite - 1].pos, satelites[next_satelite].pos))
            next_satelite+=1
        else:
            lines = []
            next_satelite = 0

create_satelites()
pgzrun.go()

