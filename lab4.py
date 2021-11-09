import pygame
from pygame.draw import *

pygame.init()

FPS = 30
pi = 3.14
screen = pygame.display.set_mode((600, 1000))
surface = pygame.Surface((300, 300))
surface2 = pygame.Surface((300, 300))
surface3 = pygame.Surface((150, 150))
surface4 = pygame.Surface((150, 150))
surface5 = pygame.Surface((150, 150))
surface6 = pygame.Surface((200, 200))
surface7 = pygame.Surface((200, 200))
surface8 = pygame.Surface((200, 200))
surface9 = pygame.Surface((200, 200))
surface10 = pygame.Surface((200, 200))
surface12 = pygame.Surface((220, 115))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
BROWN = (101, 67, 33)
HEAD3 = (238, 238, 238)
HEAD1 = (225, 223, 196)

rect(screen, GRAY, (0, 0, 600, 400))
rect(screen, WHITE, (0, 400, 600, 110))
rect(screen, WHITE, (0, 720, 600, 300))

surface.fill((255, 255, 255))
surface.set_colorkey((255, 255, 255))

surface2.fill((255, 255, 255))
surface2.set_colorkey((255, 255, 255))

surface3.fill((255, 255, 255))
surface3.set_colorkey((255, 255, 255))

surface4.fill((255, 255, 255))
surface4.set_colorkey((255, 255, 255))

surface5.fill((255, 255, 255))
surface5.set_colorkey((255, 255, 255))

surface6.fill((255, 255, 255))
surface6.set_colorkey((255, 255, 255))

surface7.fill((255, 255, 255))
surface7.set_colorkey((255, 255, 255))

surface8.fill((255, 255, 255))
surface8.set_colorkey((255, 255, 255))

surface9.fill((255, 255, 255))
surface9.set_colorkey((255, 255, 255))

surface10.fill((255, 255, 255))
surface10.set_colorkey((255, 255, 255))

surface12.fill((255, 255, 255))
surface12.set_colorkey((255, 255, 255))


def under(high, weight, colour):
    pygame.draw.rect(surface5, colour, (0, 0, weight, high))
under(20, 100, BLACK)

def body(high, weight, colour):
    pygame.draw.ellipse(surface2, colour, (50, 10, weight, high))
    rect(surface2, BLACK, (70, 35, weight/2+10, high/2+15))
body(200, 100, BROWN)

def lefthand(high, weight, colour):
    pygame.draw.ellipse(surface3, colour, (0, 0, weight, high))
lefthand(150, 50, BROWN)

def righthand(high, weight, colour):
    pygame.draw.ellipse(surface4, colour, (0, 0, weight, high))
righthand(150, 50, BROWN)

def arca(radius, colour):
    circle(surface, colour, (150, 150), radius)
    circle(surface, BLACK, (150, 150), radius, 3)
    x1 = 150 - radius
    y1 = 150 + 1
    N = 3
    h = radius//(N+1)
    y = y1 - h
    x = x1 + h
    line(surface, BLACK, (x1, 149), (x1+2*radius, 149))
    for i in range(N):
        line(surface, BLACK, (x-25, y), (2*radius - x + 40, y))
        y-=h
        x+=h
    rect(surface, GRAY, (0, 150, 300, 150))
arca(130, GRAY)

def head3(radius, colour):
    circle(surface6, colour, (100, 100), radius)
head3(100, HEAD3)

def head2(radius, colour):
    circle(surface7, colour, (100, 100), radius)
head2(70, GRAY)

def head1(radius, colour):
    circle(surface8, colour, (100, 100), radius)
head1(50, HEAD1)

def leftleg(colour):
    ellipse(surface9, colour, (100, 0, 50, 100))
    ellipse(surface9, colour, (20, 60, 100, 50))
leftleg(BROWN)

def rightleg(colour):
    ellipse(surface10, colour, (0, 0, 50, 100))
    ellipse(surface10, colour, (0, 60, 100, 50))
rightleg(BROWN)

def fish():
    polygon(surface12, (102, 99, 112), ((160, 60), (171, 58), (196, 73), (168, 88)), width=0)
    arc(surface12, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74, 30)
    arc(surface12, (71, 136, 147), (65, 13, 148, 50), 3.44, 6, 30)
    polygon(surface12, (71, 136, 147), ((67, 45), (14, 80), (4, 35)), width=0)
    polygon(surface12, (102, 99, 112), ((135, 33), (94, 0), (164, 15), (172, 24), (171, 35)), width=0)
    polygon(surface12, (102, 99, 112), ((97, 59), (80, 79), (112, 84), (114, 62)), width=0)
    circle(surface12, (2, 57, 147), (170, 47), 7, width=0)
    circle(surface12, (5, 64, 85), (170, 47), 5, width=0)
fish()



new_image = pygame.transform.scale(surface, (300, 300))
new_image2 = pygame.transform.scale(surface2, (300, 300))
new_image3 = pygame.transform.scale(surface3, (250, 50))
new_image4 = pygame.transform.scale(surface4, (250, 50))
new_image44 = pygame.transform.rotate(new_image4, 120)
new_image5 = pygame.transform.scale(surface5, (150, 100))
new_image6 = pygame.transform.scale(surface6, (100, 100))
new_image7 = pygame.transform.scale(surface7, (90, 90))
new_image8 = pygame.transform.scale(surface8, (85, 85))
new_image9 = pygame.transform.scale(surface9, (85, 85))
new_image10 = pygame.transform.scale(surface10, (85, 85))

screen.blit(new_image, (20, 400))

rect(screen, WHITE, (0, 720, 600, 300))
rect(screen, GRAY, (0, 510, 600, 210))


screen.blit(new_image2, (400, 500))
screen.blit(new_image3, (380, 540))
screen.blit(new_image44, (440, 380))

rect(screen, GRAY, (0, 650, 600, 300))
rect(screen, WHITE, (0, 700, 600, 300))

screen.blit(new_image6, (440, 450))
screen.blit(new_image7, (445, 460))
screen.blit(new_image8, (449, 465))
screen.blit(new_image9, (430, 650))
screen.blit(new_image10, (500, 650))
screen.blit(new_image5, (450, 650))
screen.blit(surface12, (50, 700))

line(screen, BLACK, (480, 500), (490, 505))
line(screen, BLACK, (500, 505), (510, 495))
line(screen, BLACK, (485, 520), (505, 520))
line(screen, BLACK, (440, 650), (398, 500))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



import math
from random import randrange as rnd,choice

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


class Ball:
    def __init__(self, screen: pygame.Surface, x=60, y=800):
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
        self.color = BLACK
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y<=580:
            self.vy-=1.2
            self.y=-self.vy
            self.x+=self.vx
            
            
        else:
            if self.vx**2+self.vy**2>10:
                self.vy=-self.vy/2
                self.vx=self.vx/2
               
        if self.x>780:
            self.vx=-self.vx/2
            self.x=779
			

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
        new_ball = Ball(self.screen)
        if abs(new_ball.x-self.x)<=(self.r+new_ball.r ) and abs(new_ball.y-self.y)<=(self.r+new_ball.r):
            return True
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
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        new_ball = Ball(self.screen)
        pygame.draw.circle(
            self.screen,
            self.color,
            (20, 500),
            20
        )

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
    def __init__(self):
        self.points=0
        self.new_target()
        self.live=1
        self.screen = screen
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
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
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()



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
        if ((self.x+25-obj.x)**2+(self.y-10-obj.y)**2) <= (15+obj.r)**2:
            return 1
        if ((self.x+25-obj.x2)**2+(self.y-10-obj.y2)**2) <= (15+obj.r2)**2:
            return 2
        else:
            return False
            

	



class Gun:
    def __init__(self, screen, x = 20, y = 450, koeff = 1):
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
        
        new_angryball = Bombs(self.screen, self.x, self.y)
        bombs.append(new_angryball)

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1] - 430) , (event.pos[0] - self.x))
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

class Enemies():
	def __init__(self, screen: pygame.Surface, x=300, y=30):
		self.screen = screen
		self.x = x
		self.y = y
		self.vx = 10
		self.r = 20
		self.color = choice(GAME_COLORS)

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
            
class Bombs():
     def __init__(self, screen: pygame.Surface, x, y=30):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10

     def draw_bombs(self):
	     pygame.draw.circle(
            self.screen,
            RED,
            (self.x, self.y),
            self.r)
     def move(self):
         self.y+=10
         
     def hittest(self, obj):
        if ((self.x-obj.x)**2+(self.y-obj.y)**2) <= (self.r+obj.r)**2:
            print('V VAS POPALI!')
		  
      
		
		

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
bombs = []


clock = pygame.time.Clock()
enemie = Enemies(screen)
gun = Gun(screen)
bomb = Bombs(screen, x)
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
		for i in bombs:
			b.draw_fish()
			i.draw_bombs()
			i.move()
			pygame.display.update()

	clock.tick(FPS)
	for event in pygame.event.get():
		gun.move_gun(event)
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
		b.live -= 1
		if b.live <=0:
			balls.remove (b)
		if b.hittest(target1) == 1 and target1.live1:
			bomb.draw_bombs()
			bomb.move()
			target1.live1 = 0
			target1.hit()
			target1.new_target1()
			balls.remove(b)
		if b.hittest(target2) == 2 and target2.live2:
			bomb.draw_bombs()
			bomb.move()
			target2.live2 = 0
			target2.hit()
			target2.new_target2()
			balls.remove(b)

	gun.power_up()

pygame.quit()
