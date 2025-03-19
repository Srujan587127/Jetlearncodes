import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

ship = Actor("galaga")
bug = Actor("bug")

ship.pos = (WIDTH // 2, HEIGHT - 60)

speed = 5

bullets = []
enemies = []

for x in range(8):
    for y in range(4):
        enemy = Actor("bug")
        enemy.x = 100 + 50 * x
        enemy.y = 80 + 50 * y
        enemies.append(enemy)

score = 0
direction = 1
ship.dead = False
ship.countdown = 90

def displayScore():
    screen.draw.text(str(score), (50, 30), color=WHITE, fontsize=40)

def gameOver():
    screen.draw.text("GAME OVER", (500, 250), color=WHITE, fontsize=60)

def on_key_down(key):
    if not ship.dead:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullet.x = ship.x
            bullet.y = ship.y - 50
            bullets.append(bullet)

def update():
    global score, direction
    moveDown = False

    if not ship.dead:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0

        if keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH

    for bullet in bullets[:]:  
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    if len(enemies) == 10:
        gameOver()

    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 80):
        moveDown = True
        direction *= -1

    for enemy in enemies[:]:  
        enemy.x += 5 * direction
        if moveDown:
            enemy.y += 70
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
                break  

        if enemy.colliderect(ship):
            ship.dead = True

    if ship.dead:
        ship.countdown -= 1
        if ship.countdown == 0:
            ship.dead = False
            ship.countdown = 90

def draw():
    screen.clear()
    screen.fill(BLUE)

    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if not ship.dead:
        ship.draw()
    displayScore()
    if len(enemies) == 0:
        gameOver()

pgzrun.go()
