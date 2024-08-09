'''
YouTube Channel: Coder Space
Tutorial used: https://www.youtube.com/watch?v=_-KjEgCLQFw

'''

import pygame as pg
from random import randrange

# Playing Field
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange( * RANGE), randrange( * RANGE)]
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

# Snake
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
snake_dir = (0, 0)
time, time_step = 0, 110
length = 1
segments = [snake.copy()]

# Food
food = snake.copy()
food.center = get_random_position()

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

    # Check borders
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Snake and Food interaction aka eating
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Draw food
    pg.draw.rect(screen, 'red', food)

    # Draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]

    # Move the snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)