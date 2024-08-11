'''
First Tutorial: Coder Space, https://www.youtube.com/watch?v=_-KjEgCLQFw
Second Tutorial: Clear Code, https://www.youtube.com/watch?v=QFvqStqPCRU // https://github.com/clear-code-projects/Snake/blob/main/snake.py
'''

import pygame as pg
import sys
from random import randrange

pg.init()

# Playing Field
WINDOW = 700
TILE_SIZE = 20

RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

def get_random_position():
    return [randrange( * RANGE), randrange( * RANGE)]

screen = pg.display.set_mode((700, 700))
clock = pg.time.Clock()

# Create a surface (to not have a black background), and convert it into a Rect (Rectangle)
x_pos = 0 # can be used to generate animation by moving the test_surface

rectangle_1_5 = pg.rect.Rect((0, 400, 100, 300))
rectangle_6_10 = pg.rect.Rect((0, 350, 350, 100))

# Snake
snake = pg.rect.Rect([get_random_position()[0], get_random_position()[1], 20, 20]) # needs x, y, width and height
snake.center = get_random_position()
snake_dir = (0, 0)
rectangle_1_5_v = [1, 0]
rectangle_6_10_v = [1, 0]
time, time_step = 0, 70
length = 1
segments = [snake.copy()]
allowed_keys = {'K_UP': 1, 'K_DOWN': 1, 'K_LEFT': 1, 'K_RIGHT': 1}

# Food
food = snake.copy()
food.center = get_random_position()

def snake_death():
    global length, snake_dir, segments, allowed_keys, snake, food, rectangle

    snake.center, food.center = get_random_position(), get_random_position()
    # zwischen 300 und 700
    
    length, snake_dir = 1, (0, 0)
    segments = [snake.copy()]
    allowed_keys = {'K_UP': 1, 'K_DOWN': 1, 'K_LEFT': 1, 'K_RIGHT': 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and allowed_keys['K_UP']:
                snake_dir = (0, -TILE_SIZE)
                allowed_keys = {'K_UP': 1, 'K_DOWN': 0, 'K_LEFT': 1, 'K_RIGHT': 1}
            if event.key == pg.K_DOWN and allowed_keys['K_DOWN']:
                snake_dir = (0, TILE_SIZE)
                allowed_keys = {'K_UP': 0, 'K_DOWN': 1, 'K_LEFT': 1, 'K_RIGHT': 1}
            if event.key == pg.K_LEFT and allowed_keys['K_LEFT']:
                snake_dir = (-TILE_SIZE, 0)
                allowed_keys = {'K_UP': 1, 'K_DOWN': 1, 'K_LEFT': 1, 'K_RIGHT': 0}
            if event.key == pg.K_RIGHT and allowed_keys['K_RIGHT']:
                snake_dir = (TILE_SIZE, 0)
                allowed_keys = {'K_UP': 1, 'K_DOWN': 1, 'K_LEFT': 0, 'K_RIGHT': 1}
    screen.fill('grey')
    
    # Move rectange_1-5
    rectangle_1_5.move_ip(rectangle_1_5_v)
    if rectangle_1_5.left < 0:
        rectangle_1_5_v[0] *= -1
    if rectangle_1_5.right > WINDOW:
        rectangle_1_5_v[0] *= -1

    # Move rectangle 6-10
    rectangle_6_10.move_ip(rectangle_6_10_v)
    if rectangle_6_10.left < 0:
        rectangle_6_10_v[0] *= -1
    if rectangle_6_10.right > WINDOW:
        rectangle_6_10_v[0] *= -1

    # Check borders and prevent self-eating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:  
        snake_death()

    # Run into block (moved into variables)
    


    font = pg.font.SysFont(None, 24)
    img = font.render(f'Current Score: {length}', True, 'black')
    screen.blit(img, (20, 20))

    # Snake and Food interaction aka eating
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Draw food
    pg.draw.ellipse(screen, 'purple', food)

    # Determine the phase based on the current length
    phase = ((length - 1) // 5) % 2

    if phase == 0:
        rectangle = rectangle_1_5
        color = 'blue'
    else:
        rectangle = rectangle_6_10
        color = 'light blue'

    # Draw the selected rectangle
    pg.draw.rect(screen, color, rectangle)

    # Check for collision between the snake and the rectangle
    if snake.colliderect(rectangle):
        snake_death()

    # Draw snake
    [pg.draw.rect(screen, 'black', segment) for segment in segments] # need to pass a screen, color and rectangle

    # Move the snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)