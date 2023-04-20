import math

import pygame
import random

import matplotlib.pyplot as plt
WIDTH = 100
HEIGHT = 100
FPS = 300
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 2
c = 6
n = 2
dt = 0.1

class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

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
        if type(other) == float:
            return Vector(self.x * other, self.y * other)



class Mol:
    def __init__(self):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)

        vx = random.randint(0, 100) / 100
        vy = random.randint(0, 100) / 100

        self.pos = Vector(x, 20)
        self.vec = Vector(vx, 0)
        self.color = RED


    def move(self):
        new_pos = self.vec * dt + self.pos

        if new_pos.x < 0:
            new_pos.x = 0
            self.vec.x = -self.vec.x
        elif new_pos.x >= WIDTH:
            new_pos.x = WIDTH
            self.vec.x = -self.vec.x
        if new_pos.y < 0:
            new_pos.y = 0
            self.vec.y = -self.vec.y
        elif new_pos.y >= HEIGHT:
            new_pos.y = HEIGHT
            self.vec.y = -self.vec.y
        self.pos = new_pos

    def upd(self, a):
        for i in a:
            d = self.pos - i.pos


            rm = d.lengh()

            if rm != 0:
                f = (c/rm) ** 12 - (c/rm) ** 6
                f = float(max(min(1, f), -1))
                self.vec += d.normalize() * f * dt


    def get_pos(self):
        return self.pos.chords()




if __name__ == "__main__":
    # Создаем игру и окно
    pygame.init()
    # pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    # Цикл игры
    running = True
    obj = []
    for i in range(n):
        obj.append(Mol())
    obj[0].color = BLUE
    ss = []
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # Проверяем хотят ли выйти
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        s = 0
        for i in obj:
            i.upd(obj)

        for i in obj:
            pygame.draw.circle(screen, i.color, i.get_pos(), r)
            i.move()
            s += i.vec.lengh()
        ss.append((s/len(obj))**2)


        pygame.display.flip()
    p = plt.plot(ss)

    plt.show()

    pygame.quit()
