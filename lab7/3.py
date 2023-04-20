#двигается на 1 шаг пр нажатии на кнопку

import random
import pygame as pg

pg.init()

WIDTH = 510
HEIGHT = 510
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 25
y = 25

dx = 20
dy = 20

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
screen.fill(WHITE)
running  = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and x < WIDTH - 25:
                x += dx
               
            if event.key == pg.K_LEFT and x > 25:
                x -= dx
               
            if event.key == pg.K_DOWN and y < HEIGHT - 25:
                y += dy
                
            if event.key == pg.K_UP and y > 25:
                y -= dy
                
    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), 25)

    pg.display.flip()
pg.quit()