import pygame
import math
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))
surface12 = pygame.Surface((220, 115))
surface12.fill((255, 255, 255))
surface12.set_colorkey((255, 255, 255))

koeffx = 1
koeffy = 1
koeffz = 1
koeffh = 1
koeffk = 1
koeffl = 1
x = 100
y = 80
z = 800
h = 200
k = 500
l = 500
ochki = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

print("Vvedite svoi nickname: ")
nickname = input()


def draw_new_ball1():
    global x, y, r, koeffx, koeffy
    x = x + koeffx * randint(5, 10)
    if x > 1100 or x < 80:
        koeffx *= -1
        x += 10 * koeffx
    y = y + koeffy * randint(5, 10)
    if y > 850 or y < 80:
        koeffy *= -1
        y += 10 * koeffy
    r = 50
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    return x, y, r


def draw_new_ball2():
    global z, h, r, koeffz, koeffh
    z = z + koeffz * randint(5, 10)
    if z > 1100 or z < 80:
        koeffz *= -1
        z += 10 * koeffz
    h = h + koeffh * randint(5, 10)
    if h > 850 or h < 80:
        koeffh *= -1
        h += 10 * koeffh
    r = 50
    color = COLORS[randint(0, 5)]
    circle(screen, color, (z, h), r)


def click2(event):
    return z, h, r


def draw_fish():
    polygon(surface12, (102, 99, 112), ((160, 60), (171, 58), (196, 73), (168, 88)), width=0)
    arc(surface12, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74, 30)
    arc(surface12, (71, 136, 147), (65, 13, 148, 50), 3.44, 6, 30)
    polygon(surface12, (71, 136, 147), ((67, 45), (14, 80), (4, 35)), width=0)
    polygon(surface12, (102, 99, 112), ((135, 33), (94, 0), (164, 15), (172, 24), (171, 35)), width=0)
    polygon(surface12, (102, 99, 112), ((97, 59), (80, 79), (112, 84), (114, 62)), width=0)
    circle(surface12, (2, 57, 147), (170, 47), 7, width=0)
    circle(surface12, (5, 64, 85), (170, 47), 5, width=0)


draw_fish()


def draw_swimming_fish():
    global k, l, koeffk, koeffl
    k = k + koeffk * randint(1, 5)
    if k > 1000 or k < 60:
        koeffk *= -1
        k += 10 * koeffk
    l = l + koeffl * randint(1, 5)
    if l > 800 or l < 80:
        koeffl *= -1
        l += 10 * koeffl
    screen.blit(surface12, (k, l))


def click3(event):
    return k + 55, l - 10


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (click(event)[0] - event.pos[0]) ** 2 + (click(event)[1] - event.pos[1]) ** 2 <= click(event)[
                2] ** 2 or (click2(event)[0] - event.pos[0]) ** 2 + (click2(event)[1] - event.pos[1]) ** 2 <= \
                    click(event)[2] ** 2:
                print('yes')
                ochki = ochki + 1
                print('u vas:', ochki, 'ochkov')
            elif (click3(event)[0] - event.pos[0]) ** 2 + (click3(event)[1] - event.pos[1]) ** 2 <= 110 ** 2:
                print('yes, vi poimali ribky')
                ochki = ochki + 5
                print('u vas:', ochki, 'ochkov')

    draw_new_ball1()
    draw_new_ball2()
    draw_swimming_fish()
    pygame.display.update()
    screen.fill(BLACK)

output = open('output.txt', 'a')
print(nickname, ochki, file=output)
pygame.quit()