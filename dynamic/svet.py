import pygame as pg


fps = 10
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pg.init()

WIDTH = 210
HEIGHT = 210

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")

blok = 1
l = 0

n = 200

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

    def update(self, near):
        if self.type != "static":
            s = 0
            for i in near:
                s += i.h * i.m
            self.vec +=  s / 4 - self.m * self.h

    def move(self):
        self.h += self.vec

a = [[Point("static") for _ in range(n + 2)]]
a += [[Point("static")] + [Point("light") for _ in range(n//2)]   + [Point("havy") for _ in range(n//2)]+ [Point("static")] for i in range(n)]

a += [[Point("static") for _ in range(n + 2)]]

a[20][50].vec = 100

a[20][150].vec = 100

# a[40] = [Point("static") for _ in range(n + 2)]
#
# a[40][20] = Point("light")
# a[40][21] = Point("light")
# a[40][40] = Point("light")
# a[40][41] = Point("light")




while True:

    screen.fill(black)
    for i in range(len(a)):
        for j in range(n + 2):
            if a[i][j].type == "static":
                pg.draw.rect(screen, blue, (l + j * (l + blok), l + i * (l + blok), blok, blok))
            else:
                g = abs(a[i][j].h/5)

                g = min(1, g)
                pg.draw.rect(screen, (255 * g, 255 * g, 255 * g ) , (l + j * (l + blok), l + i * (l + blok), blok, blok))


    for i in range(1, len(a) - 1):
        for j in range(1, n+ 2 - 1):
            near = []
            near.append(a[i + 1][j + 1])
            near.append(a[i + 1][j - 1])
            near.append(a[i - 1][j + 1])
            near.append(a[i - 1][j - 1])
            a[i][j].update(near)

    s = 0
    vs = 0
    for i in range(len(a)):
        for j in range(1, n+ 2 - 1):
            a[i][j].move()
            s += a[i][j].h
            vs += a[i][j].vec




    pg.display.flip()

    clock.tick(fps)

