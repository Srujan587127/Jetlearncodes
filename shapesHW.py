import pgzrun
from random import randint 

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(120, 255)
    radius = 100  
    for i in range(20):
        screen.draw.circle((WIDTH /2 , HEIGHT /2), radius, (r, g, b))
        r -= 10
        g += 10
        radius -= 5

pgzrun.go()
