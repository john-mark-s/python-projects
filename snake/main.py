import pygame as pg
from random import randrange

WINDOW = 800
TILE_SIZE = 20
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange( * RANGE), randrange( * RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
snake_dir = (0, 0)
length = 1
segments = [snake.copy()]

screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)
    screen.fill('black')