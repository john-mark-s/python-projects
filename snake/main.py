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