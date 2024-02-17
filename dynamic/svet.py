import pygame as pg
import numpy as np

fps = 1000
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pg.init()

WIDTH = 200
HEIGHT = 200

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")

block = 1

clock = pg.time.Clock()

values = np.zeros((HEIGHT, WIDTH))
newValues = np.zeros((HEIGHT, WIDTH))
sizes = np.ones((HEIGHT, WIDTH))

for i in range(WIDTH):
    values[50, i] = 100


while True:
    screen.fill(black)
    for i in range(1, HEIGHT - 1):
        for j in range(1, WIDTH - 1):
            s = 0
            for y in [i - 1, i + 1]:
                s += values[y, j] * sizes[y, j]
            for x in [j - 1, j + 1]:
                s += values[i, x] * sizes[i, x]
            newValues[i, j] = s / (4 * sizes[i, j])
            g = newValues[i, j] / 100
            pg.draw.rect(screen, (255 * g, 255 * g, 255 * g ), (j * block, i * block, j * block + block, i * block + block))

    values = newValues.copy()
    pg.display.flip()
    print(1)
    clock.tick(fps)