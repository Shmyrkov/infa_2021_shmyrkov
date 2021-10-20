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
