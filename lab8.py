import math
from random import randrange as rnd, choice

import pygame
from pygame.draw import *

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
i = 1

class Ball:
    def __init__(self, screen: pygame.Surface, x=60, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy += 10
        self.y += self.vy / 20
        self.x += self.vx / 30
        if self.y >= 580:
            self.vy = -self.vy/2
            self.y = 579
        if self.y <= 20:
            self.vy = -self.vy / 2
            self.y = 21
        if self.x > 780:
            self.vx = -self.vx / 2
            self.x = 779
        if self.x < 0:
            self.vx = -self.vx / 2
            self.x = 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        global i
        if (abs(obj.x - self.x) <= (self.r + obj.r) and abs(obj.y - self.y) <= (self.r + obj.r)):
            return 1
        if (abs(obj.x2 - self.x) <= (self.r + obj.r2) and abs(obj.y2 - self.y) <= (self.r + obj.r2)):
            return 2
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 500

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (40, 430,
            20,20
        ))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target():
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self, screen):
        self.points = 0
        self.new_target()
        self.new_target2()
        self.live1 = 1
        self.live2 = 1
        self.screen = screen

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(400, 700)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.color = choice(GAME_COLORS)
        self.live1 = 1
    def new_target2(self):
        """ Инициализация новой цели. """
        self.x2 = rnd(200, 600)
        self.y2 = rnd(50, 300)
        self.r2 = rnd(2, 50)
        self.color2 = choice(GAME_COLORS)
        self.live2 = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        print('YOU HAVE:', self.points, 'POINTS')

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)
        pygame.draw.circle(
            self.screen,
            self.color2,
            (self.x2, self.y2),
            self.r2)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []


clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) == 1 and target.live1:
            target.live1 = 0
            target.hit()
            target.new_target()
        if b.hittest(target) == 2 and target.live2:
            target.live2 = 0
            target.hit()
            target.new_target2()

    gun.power_up()

pygame.quit()