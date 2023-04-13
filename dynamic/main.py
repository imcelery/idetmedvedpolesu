import pygame as pg

fps = 10
black = (0, 0, 0)
white = (255, 255, 255)
pg.init()

WIDTH = 400
HEIGHT = 200

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")

blok = 10
l = 2

n = 30

k = 0.7

clock = pg.time.Clock()

class Point:
    def __init__(self):
        self.vec = 0
        self.k = k
        self.h = 0

    def update(self, prevP, nextP):
        if prevP is not None:
            self.vec += (prevP.h - self.h) * self.k

        if nextP is not None:
            self.vec += (nextP.h - self.h) * self.k

    def move(self):
        self.h += self.vec

a = [Point() for _ in range(n)]

a[0].h = 50
a[29].h = 50

while True:

    screen.fill(black)
    for i in range(len(a)):
        pg.draw.rect(screen, white, (l + i * (l + blok), HEIGHT//2 + a[i].h, blok, blok))


    for i in range(len(a)):
        nextP = None
        prevP = None
        if i + 1 < len(a):
            nextP = a[i + 1]
        if i - 1 >= 0:
            prevP = a[i - 1]
        a[i].update(prevP, nextP)

    for i in range(len(a)):
        a[i].move()


    pg.display.flip()

    clock.tick(fps)

