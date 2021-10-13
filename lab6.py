import pygame
import math
from pygame.draw import *
from random import randint

pygame.init()

FPS = 13
screen = pygame.display.set_mode((1200, 900))

koeffx = 1
koeffy = 1
koeffz = 1
koeffh = 1
x = 50
y = 80
z = 800
h = 200

ochki = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def draw_new_ball1():
    global x, y, r, koeffx, koeffy
    x = x + koeffx * randint(10, 20)
    if x > 1150 or x < 50:
        koeffx *= -1
    y = y + koeffy * randint(10, 20)
    if y > 850 or y < 50:
        koeffy *= -1
    r = 50
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    return x, y, r


def draw_new_ball2():
    global z, h, r, koeffz, koeffh
    z = z + koeffz * randint(10, 20)
    if z > 1150 or z < 50:
        koeffz *= -1
    h = h + koeffh * randint(10, 20)
    if h > 850 or h < 50:
        koeffh *= -1
    r = 50
    color = COLORS[randint(0, 5)]
    circle(screen, color, (z, h), r)


def click2(event):
    return z, h, r


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (click(event)[0] - event.pos[0]) ** 2 + (click(event)[1] - event.pos[1]) ** 2 <= \
                    click(event)[
                2] ** 2 or (click2(event)[0] - event.pos[0]) ** 2 + (click2(event)[1] - event.pos[1]) ** 2 <= \
                    click(event)[2] ** 2:
                print('yes')
                ochki = ochki + 1
                print('u vas:', ochki, 'ochkov')

    draw_new_ball1()
    draw_new_ball2()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()