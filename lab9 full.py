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
koeff11 = 1
koeff12 = 1
koeff21 = 1
koeff22 = 1

surface12 = pygame.Surface((220, 115))
surface12.fill((255, 255, 255))
surface12.set_colorkey((255, 255, 255))
x = 0


class AbstractBall:
    def __init__(self, screen: pygame.Surface, x, y=450):
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
        self.live = 100

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
            self.vy = -self.vy / 2
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


class FishBall(AbstractBall):
    def draw_fish(self):
        polygon(surface12, (102, 99, 112), ((160, 60), (171, 58), (196, 73), (168, 88)), width=0)
        arc(surface12, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74, 30)
        arc(surface12, (71, 136, 147), (65, 13, 148, 50), 3.44, 6, 30)
        polygon(surface12, (71, 136, 147), ((67, 45), (14, 80), (4, 35)), width=0)
        polygon(surface12, (102, 99, 112), ((135, 33), (94, 0), (164, 15), (172, 24), (171, 35)), width=0)
        polygon(surface12, (102, 99, 112), ((97, 59), (80, 79), (112, 84), (114, 62)), width=0)
        circle(surface12, (2, 57, 147), (170, 47), 7, width=0)
        circle(surface12, (5, 64, 85), (170, 47), 5, width=0)
        new_image12 = pygame.transform.scale(surface12, (50, 50))
        screen.blit(new_image12, (self.x, self.y))

    def hittest(self, obj):
        if ((self.x + 25 - obj.x) ** 2 + (self.y - 10 - obj.y) ** 2) <= (15 + obj.r) ** 2:
            return 1
        if ((self.x + 25 - obj.x2) ** 2 + (self.y - 10 - obj.y2) ** 2) <= (15 + obj.r2) ** 2:
            return 2
        else:
            return False

class BombBall():
    def __init__(self, screen: pygame.Surface, x, y=450):

        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 100

    def move(self):

        self.vy += 10
        self.y += self.vy / 20
        if self.y >= 580:
            self.vy = -self.vy / 2
            self.y = 579
        if self.y <= 20:
            self.vy = -self.vy / 2
            self.y = 21


    def drawball(self):
        pygame.draw.circle(
            self.screen,
            BLUE,
            (self.x, self.y),
            20)

    def hittest(self, obj):
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + 20) ** 2:
            return 1
        else:
            return False


class Gun:
    def __init__(self, screen, x=20, y=450, koeff=1):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = x
        self.y = y
        self.vx = 15

    def fire2_start(self, event):
        self.f2_on = 1

    def move_gun(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= self.vx
            if event.key == pygame.K_RIGHT:
                self.x += self.vx

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = FishBall(self.screen, self.x, self.y)
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
            self.an = math.atan2((event.pos[1] - 430), (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.circle(
            self.screen,
            GREEN,
            (self.x, 430),
            20, 20
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class AbstractTarget():
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self, screen):
        self.x = 100
        self.y = 450
        self.x2 = 400
        self.y2 = 100
        self.r = 30
        self.r2 = 20
        self.points = 0
        self.new_target1()
        self.new_target2()
        self.live1 = 1
        self.live2 = 1
        self.screen = screen
        self.color = choice(GAME_COLORS)

    def hit(self, points=1):
        global x
        """Попадание шарика в цель."""
        x += points
        print('YOU HAVE:', x, 'POINTS')

    def new_target1(self):
        pass

    def new_target2(self):
        pass


class EasyTarget(AbstractTarget):

    def new_target1(self):
        self.x = rnd(200, 600)
        self.y = rnd(50, 300)
        self.r = rnd(30, 60)
        self.color = choice(GAME_COLORS)
        self.live1 = 1

    def move1(self):
        global koeff11, koeff12, koeff21, koeff22
        self.y += koeff11 * 10 + 1
        self.x += koeff12 * 10 + 3
        if self.y >= 500 or self.y <= 20:
            koeff11 *= -1
            self.y += 10 * koeff11
        if self.x > 780 or self.x < 0:
            koeff12 *= -1
            self.x += 10 * koeff12

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)


class HardTarget(AbstractTarget):

    def new_target2(self):
        self.x2 = rnd(200, 600)
        self.y2 = rnd(50, 300)
        self.r2 = rnd(5, 15)
        self.color = choice(GAME_COLORS)
        self.live2 = 1

    def move2(self):
        global koeff21, koeff22
        self.y2 += koeff21 * 20
        self.x2 += koeff22 * 20
        if self.y2 >= 500 or self.y2 <= 20:
            koeff21 *= -1
            self.y2 += 30 * koeff21
        if self.x2 > 780 or self.x2 < 0:
            koeff22 *= -1
            self.x2 += 30 * koeff22

    def draw2(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x2, self.y2),
            self.r2, 2)


class Enemies:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = rnd(20, 500)
        self.y = rnd(10, 20)
        self.vx = 10
        self.r = 20
        self.color = choice(GAME_COLORS)

    def fire_end(self, event):

        global bombs
        new_angryball = BombBall(self.screen, self.x, self.y)
        new_angryball.r += 5
        new_angryball.vx = 0
        new_angryball.vy = 10
        bombs.append(new_angryball)

    def move(self):
        self.x += self.vx
        if self.x > 780:
            self.vx = -self.vx
            self.x = 779
        if self.x < 0:
            self.vx = -self.vx
            self.x = 1


    def draw_enemy(self):
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r)




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
bombs = []


clock = pygame.time.Clock()
enemie = Enemies(screen)
gun = Gun(screen)
Bomb1 = BombBall(screen, x)
target1 = EasyTarget(screen)
target2 = HardTarget(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    enemie.draw_enemy()
    enemie.move()
    gun.draw()
    target1.draw()
    target1.move1()
    target2.draw2()
    target2.move2()
    for b in balls:
        b.draw_fish()
        pygame.display.update()
    for s in bombs:
        s.drawball()
        pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        gun.move_gun(event)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            enemie.fire_end(event)
            Bomb1.move()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        b.live -= 1
        if b.live <= 0:
            balls.remove(b)
        if b.hittest(target1) == 1 and target1.live1:
            target1.live1 = 0
            target1.hit()
            target1.new_target1()
            balls.remove(b)
        if b.hittest(target2) == 2 and target2.live2:
            target2.live2 = 0
            target2.hit()
            target2.new_target2()
            balls.remove(b)

    for s in bombs:
        s.move()
        if s.hittest(gun) == 1:
            bombs.remove(s)
            print('В ВАС ПОПАЛИ: -5 очков')
            x = x - 5
            print('YOU HAVE:', x, 'POINTS')

    gun.power_up()

pygame.quit()