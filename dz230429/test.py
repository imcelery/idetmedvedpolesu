import numpy as np
import pygame
import random


WIDTH = 500
HEIGHT = 30
block = 10

FPS = 300
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

n = 40

class Alg:
    def __init__(self, w=None):
        if w is None:
            len_w = [2, 20, 1]
            self.w = []
            for i in range(len(len_w) - 1):
                self.w.append(np.random.random((len_w[i],len_w[i + 1])) * 2 - 1)

            # 7600 + 10000 + 2000 + 180
        else:
            self.w = w
        self.last_move = None

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def get_move(self, a):
        for i in range(len(self.w)):
            a = self.sigmoid(a.dot(self.w[i]))

        return a * 2 - 1


    def mutation(self):

        for i in range(len(self.w)):

            p = (np.random.random(self.w[i].shape) > 0.9).astype(int)
            self.w[i][p == 1] += (np.random.rand() * 2 - 1) * 0.1


    def sex(self, u1, u2):
        w1 = u1.get_w()
        w2 = u2.get_w()
        for i in range(len(self.w)):
            for j in range(len(self.w[i])):
                for k in range(len(self.w[i][j])):
                    self.w[i][j][k] = w1[i][j][k]
                    if random.randint(0, 2) > 1:
                        w1, w2 = w2, w1

    def get_w(self):
        return self.w


class Unit:
    def __init__(self):
        self.speed = random.randint(-5, 5)
        self.pos = random.randint(-30, 30)
        self.alg = Alg()

    def upd(self):
        self.speed += self.alg.get_move(np.array([self.speed/100, self.pos/100]))[0]
        self.pos += self.speed


a = []
for i in range(n):
    a.append(Unit())


pygame.init()
pygame.display.set_caption("Эволюция!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

tick = 0

gen_age = 100 + random.randint(-20, 20)
while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    s = 0

    for el in a:

        pygame.draw.rect(screen, WHITE, (el.pos + WIDTH//2, 10, block, block))
        el.upd()
        s += 1 / abs(el.pos)

    if gen_age == tick:
        gen_age = 100 + random.randint(-20, 20)
        tick = 0
        b = []
        for el in a:
            b.append(abs(1 / el.pos)/ s)
        na = []
        for i in range(len(a)):
            u1 , u2 = None, None
            while u1  == u2:
                u1 = random.choices(a, weights=b)[0]
                u2 = random.choices(a, weights=b)[0]

            u = Unit()
            u.alg.sex(u1.alg, u2.alg)
            u.alg.mutation()
            na.append(u)

        a = na

    pygame.display.flip()
    tick += 1
