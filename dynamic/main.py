import pygame as pg

fps = 2
black = (0, 0, 0)
white = (255, 255, 255)
pg.init()

WIDTH = 400
HEIGHT = 200

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")

blok = 10

n = 10

l = 2

a = [0 for _ in range(n)]

a[5] = 5

k = 0.5
clock = pg.time.Clock()


while True:

    screen.fill(black)
    for i in range(len(a)):
        pg.draw.rect(screen, white, (l + i * (l + n), HEIGHT//2 + a[i], blok, blok))

    for i in range(len(a)):
        pg.draw.rect(screen, white, (l + i * (l + n), HEIGHT//2 + a[i], blok, blok))

    na = a.copy()

    for i in range(1, len(a)):
        na[i - 1] += (a[i] - a[i - 1]) * k

    a = na

    pg.display.flip()

    clock.tick(fps)