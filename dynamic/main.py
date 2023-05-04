import pygame as pg


fps = 30
black = (0, 0, 0)
white = (255, 255, 255)
pg.init()

WIDTH = 400
HEIGHT = 200

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")

blok = 2
l = 1

n = 65

lm = 1
hm = 2
clock = pg.time.Clock()

class Point:
    def __init__(self, type):
        self.vec = 0
        self.type = type
        self.h = 0

        if type == "light":
            self.m = lm
        elif type == "havy":
            self.m = hm
        else:
            self.m = 100000000

    def update(self, prevH, nextH):

        self.vec +=nextH.h  * nextH.m / 2 + prevH.h * prevH.m / 2 - self.m * self.h

    def move(self):
        self.h += self.vec

a = [Point("static")] + [Point("light") for _ in range(n)] + [Point("light") for _ in range(n)] + [Point("static")]


a[20].vec = 30




while True:

    screen.fill(black)
    for i in range(len(a)):
        pg.draw.rect(screen, white, (l + i * (l + blok), HEIGHT//2 + a[i].h, blok, blok))


    for i in range(1, len(a) - 1):
        nextP = a[i + 1]
        prevP = a[i - 1]
        a[i].update(prevP, nextP)
    s = 0
    for i in range(len(a)):
        a[i].move()
        s += abs(a[i].h)



    pg.display.flip()

    clock.tick(fps)

