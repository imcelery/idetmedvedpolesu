import math

import pygame
import random
import numpy as np

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 2

x, y = (WIDTH-r//2)//2 + 100 , (HEIGHT-r//2)//2
g = 10
dt = 0.1
vy = 0
vx = 10


def draw_lines(surface: pygame.surface.Surface, color: pygame.color.Color, xs: list[int], ys: list[int]) -> None:
    """
    Рисуем параболу с помощью pyGame
    :param surface:
    :param color:
    :param xs:
    :param ys:
    :return: None
    """
    # print(xs[:3])
    # print(ys[:3])
    x1 = xs[0]
    y1 = ys[0]
    for i in range(1, len(xs)):
        x2 = xs[i]
        y2 = ys[i]
        pygame.draw.line(surface, color, (x1, y1), (x2, y2))
        # print(x1,y1, x2, y2)
        x1, y1 = x2, y2


x_parable = np.arange(0, WIDTH+1, 1)


def f_parabble(x, xs):
    m = max((xs - WIDTH//2)**2)
    return HEIGHT - (((x - WIDTH//2)**2)/m*HEIGHT)

def pf_parabble(x, xs):
    y1 = f_parabble(x - 0.1, xs)
    y2 = f_parabble(x+ 0.1, xs)
    return (y2 - y1) / 0.2

def rotate_matrix(d):
    return  [[np.cos(d), -np.sin(d)],
         [np.sin(d), np.cos(d)]]

class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def lengh(self):
        return math.sqrt(self.x ** 2 + self.y**2)

    def normalize(self):
        l = self.lengh()
        if l != 0:
            return Vector(self.x/l, self.y/l)

    def chords(self):
        return (self.x, self.y)

    def __mul__(self, other):
        if type(other) == list:
            x = self.x * other[0][0] + self.y * other[0][1]
            y = self.x * other[1][0] + self.y * other[1][1]
            return Vector(x, y)

    def __str__(self):
        return str(self.x) + ' '+ str(self.y)

y_parable = f_parabble(x_parable, x_parable)

# print(x_parable)
# print(y_parable)
# Создаем игру и окно
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем хотят ли выйти
        if event.type == pygame.QUIT:
            running = False


    #print("x,y, v, E:", x, y, np.sqrt(vx**2 + vy**2), (vx**2 + vy**2)/2 + g*y)
    # if y > HEIGHT:
    #     y = HEIGHT
    #     vy = -vy

    # a = dv / dt -> dv = a * dt
    vy = vy + g * dt
    vx = vx
    # v = dy  / dt -> dy = v * dt
    y = y + vy * dt
    x = x + vx * dt

    if f_parabble(np.array([x]), x_parable)[0] <= y:
        y = f_parabble(np.array([x]), x_parable)[0]
        tg_parabol = pf_parabble(x, x_parable)
        d = np.arctan(tg_parabol)
        m = rotate_matrix(-d)


        v = Vector(vx, vy)

        print(v)

        v = v * m

        print(v)

        v.y = -v.y

        m = rotate_matrix(d)

        v = v * m

        vx, vy = v.chords()





    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, [x, y], r)
    draw_lines(screen, GREEN, x_parable, y_parable)
    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    pass