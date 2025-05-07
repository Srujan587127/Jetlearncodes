import pgzrun
from random import randint, uniform

TITLE = "Bouncy Ball Simulation"
WIDTH = 800
HEIGHT = 600

GRAVITY = 2000.0

class Ball:
    def __init__(self, initial_x, initial_y, radius, color, bounce_factor):
        self.x = initial_x
        self.y = initial_y
        self.vx = uniform(100, 300)
        self.vy = 0
        self.radius = radius
        self.color = color
        self.bounce_factor = bounce_factor  

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self, dt):
        
        uy = self.vy
        self.vy += GRAVITY * dt
        self.y += (uy + self.vy) * 0.5 * dt

        
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * self.bounce_factor

        
        self.x += self.vx * dt
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx

def random_color():
    return (randint(0,255), randint(0,255), randint(0,255))


balls = []
for _ in range(5):
    radius = randint(20, 50)
    color = random_color()
    bounce = uniform(0.5, 0.95)  
    x = randint(radius, WIDTH - radius)
    y = randint(radius, HEIGHT // 2)
    balls.append(Ball(x, y, radius, color, bounce))

def draw():
    screen.clear()
    for ball in balls:
        ball.draw()

def update(dt):
    for ball in balls:
        ball.update(dt)

def on_key_down(key):
    if key == keys.SPACE:
        for ball in balls:
            ball.vy = -500  

pgzrun.go()
