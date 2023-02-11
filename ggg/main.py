import pygame as pg

import random





if __name__ == '__main__':
    WIDTH = 360
    HEIGHT = 480
    FPS = 30

    pg.init()
    pg.mixer.init()  # для звука
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("My Game")
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

    pg.quit()