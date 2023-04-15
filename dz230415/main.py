import math

import pygame
import random


WIDTH = 100
HEIGHT = 100
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 2

n = 300

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
            self.x = self.x * other[0][0] + self.y * other[0][1]
            self.y = self.x * other[1][0] + self.y * other[1][1]


class Mol:
    def __init__(self):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)

        vx = random.randint(0, 100) / 100
        vy = random.randint(0, 100) / 100

        self.pos = Vector(x, y)
        self.vec = Vector(vx, vy)

    def move(self):
        new_pos = self.vec + self.pos
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
            pygame.draw.circle(screen, RED, i.get_pos(), r)
            i.move()
            s += i.vec.lengh()
        print((s/len(obj))**2)

        pygame.display.flip()

    pygame.quit()
