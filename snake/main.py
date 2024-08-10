'''
First Tutorial: Coder Space, https://www.youtube.com/watch?v=_-KjEgCLQFw
Second Tutorial: Clear Code, https://www.youtube.com/watch?v=QFvqStqPCRU // https://github.com/clear-code-projects/Snake/blob/main/snake.py
'''

import pygame as pg
import sys
from random import randrange

# Playing Field
WINDOW = 700
TILE_SIZE = 20

RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange( * RANGE), randrange( * RANGE)]

screen = pg.display.set_mode((700, 700))
clock = pg.time.Clock()

# Create a surface (to not have a black background), and convert it into a Rect (Rectangle)
test_surface = pg.Surface((100, 200))
test_surface.fill((0, 0, 255))
x_pos = 0 # can be used to generate animation by moving the test_surface

test_rectangle = test_surface.get_rect(center = (0, 400))

# Snake
snake = pg.rect.Rect([get_random_position()[0], get_random_position()[1], 20, 20]) # needs x, y, width and height
snake.center = get_random_position()
snake_dir = (0, 0)
time, time_step = 0, 70
length = 1
segments = [snake.copy()]

# Food
food = snake.copy()
food.center = get_random_position()

surface_direction = "RIGHT"

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (TILE_SIZE, 0)
    screen.fill((175, 215, 70))
    if surface_direction == "RIGHT":
        x_pos += 1
        if x_pos == 500:
            surface_direction = "LEFT"
    else:
        x_pos -=1
        if x_pos == 0:
            surface_direction = "RIGHT"
    screen.blit(test_surface, (x_pos, 250))

    # Check borders and prevent self-eating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Run into block
    if pg.Rect.colliderect(snake, test_rectangle):
        snake.center = get_random_position()


    # Snake and Food interaction aka eating
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Draw food
    pg.draw.ellipse(screen, 'red', food)
    pg.draw.rect(screen, 'red', test_rectangle)

    # Draw snake
    [pg.draw.rect(screen, 'black', segment) for segment in segments] # need to pass a screen, color and rectangle

    # Move the snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        # test_rectangle.move_ip(x_pos, 200)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)