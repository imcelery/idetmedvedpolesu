import pygame

import sys

from model import *

from matrix import *

import numpy as np

from stl import mesh



class Donut:
    def __init__(self):
        self.gameObjects = []
        self.width = 1200
        self.height = 800
        self.fps = 30
        self.running = True

        pygame.init()
        pygame.mixer.init()  # для звука
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.grafic = Grafic()

        self.cameraDirection = [[0], [0], [-1], [0]]
        self.cameraPosition = [[0], [0], [0], [1]]

    def showScreen(self):
        self.screen.blit(self.grafic.getSurface(), (0, 0))
        pygame.display.flip()
        self.grafic.clear()

    def addObject(self, gm):
        self.gameObjects.append(gm)

    def drowObjects(self):
        # print()
        # print(self.cameraPosition)
        # print()
        for i in self.gameObjects:
            i.show(self.grafic, self.cameraDirection, self.cameraPosition, self.width, self.height)
        self.showScreen()


class Grafic:
    def __init__(self):
        self._width = 1200
        self._height = 800
        self._surface = pygame.Surface((self._width, self._height))


    def getSurface(self):
        return self._surface

    def clear(self):
        self._surface.fill((0,0,0))

    def drawPixel(self, x, y, color):
        x += self._width // 2
        y = -(y - self._height // 2)
        self._surface.set_at((x, y), color)

    def drawLine(self, x1, y1, x2, y2, color):
        c1 = y2 - y1
        c2 = x2 - x1
        if c1 == 0 and c2 == 0:
            return None
        length = math.sqrt(c1 * c1 + c2 * c2)

        xStep = c2 / length
        yStep = c1 / length

        for i in range(int(length)):
            self.drawPixel(
                math.trunc(x1 + xStep * i),
                math.trunc(y1 + yStep * i),
                color)


class GameObject:
    def __init__(self):
        self._position = [0, -300, -3000]
        self._rotation = [[0], [0], [0], [1]]
        self._model = Model()

    def set_model(self, polygons):
        self._model.load(polygons)

    def show(self, grafic, cameraDirection, cameraPosition, width, height):
        m = RotationX(-90)

        m = mul_matrix(Scale(10, 10, 10), m)

        m = mul_matrix(Translation(*self._position), m)

        m = mul_matrix(LookAt(cameraPosition, add_vector(cameraPosition, cameraDirection), [[0], [1], [0], [0]]), m)

        m = mul_matrix(PerspectiveProjection(100, width / height, 1, 10000), m)

        self._model.show(grafic, cameraDirection, m)


if __name__ == "__main__":
    donut = Donut()


    speed = 10

    angel = 0

    your_mesh = mesh.Mesh.from_file('pikachu_1gen_flowalistik.stl')

    gm = GameObject()
    gm.set_model(your_mesh.vectors)
    donut.addObject(gm)


    while donut.running:

        donut.clock.tick(donut.fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            donut.cameraPosition = add_vector(donut.cameraPosition,  mul_vector_by_scalar(donut.cameraDirection, speed))

        elif keys[pygame.K_s]:
            donut.cameraPosition = sub_vector(donut.cameraPosition,  mul_vector_by_scalar(donut.cameraDirection, speed))

        if keys[pygame.K_a]:
            normal = normalize(crossProduct([[0], [1], [0], [1]], donut.cameraDirection))
            donut.cameraPosition = add_vector(donut.cameraPosition,  mul_vector_by_scalar(normal, speed))

        elif keys[pygame.K_d]:
            normal = normalize(crossProduct([[0], [1], [0], [1]],  donut.cameraDirection))
            donut.cameraPosition = sub_vector(donut.cameraPosition,  mul_vector_by_scalar(normal, speed))

        if keys[pygame.K_SPACE]:
            donut.cameraPosition = add_vector(donut.cameraPosition,  mul_vector_by_scalar([[0], [1], [0], [1]], speed))

        elif keys[pygame.K_c]:

            donut.cameraPosition = sub_vector(donut.cameraPosition,  mul_vector_by_scalar([[0], [1], [0], [1]], speed))


        donut.drowObjects()