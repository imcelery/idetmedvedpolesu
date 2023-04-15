import math

import pygame
import random
import matplotlib.pyplot as plt


WIDTH = 500
HEIGHT = 500
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 2

n = 10000

wallspeed = -1
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
        a = 0
        if new_pos.x < 0:
            new_pos.x = 0
            a += 1
            self.vec.x = -self.vec.x

        elif new_pos.x >= WIDTH:
            new_pos.x = WIDTH
            self.vec.x = -self.vec.x + wallspeed
            a += 1
        if new_pos.y < 0:
            new_pos.y = 0
            self.vec.y = -self.vec.y
            a += 1
        elif new_pos.y >= HEIGHT:
            new_pos.y = HEIGHT
            self.vec.y = -self.vec.y
            a += 1
        self.pos = new_pos
        return a

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
    f1 = pygame.font.Font(None, 36)
    ss = []
    pp = []
    vv = []
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
        p = 0
        for i in obj:
            pygame.draw.circle(screen, RED, i.get_pos(), r)
            p += i.move()
            s += i.vec.lengh()

        text1 = f1.render("температура :" +  str((s/len(obj)) ** 2), True,
                          (180, 0, 0))
        text2 = f1.render("обьем :" + str( WIDTH * HEIGHT/ 10000), True,
                          (180, 0, 0))

        text3 = f1.render("давление :" + str(p / ( 2 * (WIDTH + HEIGHT))), True,
                          (180, 0, 0))

        screen.blit(text1, (10, 50))
        screen.blit(text2, (10, 100))
        screen.blit(text3, (10, 150))

        ss.append((s / len(obj)) ** 2)
        vv.append(WIDTH * HEIGHT/ 10000)

        pp.append(p / ( 2 * (WIDTH + HEIGHT)))

        pygame.display.flip()
        WIDTH += wallspeed
        if WIDTH <= 0:
            break
    p = plt.plot(ss)
    a = plt.plot(vv)
    s = plt.plot(pp)
    plt.show()
    pygame.quit()
