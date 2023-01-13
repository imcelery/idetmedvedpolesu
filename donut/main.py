import pygame

import sys

from model import *

from matrix import *

import numpy as np

from stl import mesh



class Donut:

    def __init__(self):
        self.gameObgects = []
        self.width = 1200
        self.height = 800
        self.fps = 30

        pygame.init()
        pygame.mixer.init()  # для звука
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface((self.width, self.height))


    def show(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

    def clear(self):
        self.surface.fill((0,0,0))

    def drawpixel(self, x, y, color):


        x += self.width // 2

        y = -(y - self.height // 2)

        self.surface.set_at((x, y), color)

    def drawLine(self, x1, y1, x2, y2, color):

        c1 = y2 - y1
        c2 = x2 - x1
        if c1 == 0 and c2 == 0:
            return None
        length = math.sqrt(c1 * c1 + c2 * c2)

        xStep = c2 / length
        yStep = c1 / length

        for i in range(int(length)):
            self.drawpixel(
                math.trunc(x1 + xStep * i),
                math.trunc(y1 + yStep * i),
                color)

    def addObject(self, gm):
        self.gameObgects.append(gm)



class GameObject:
    def __init__(self):
        self._position = [[0], [0], [0], [1]]
        self._rotation = [[0], [0], [0], [1]]
        self._model = Model()

    def set_model(self, polygons):
        self._model.load(polygons)

    def show(self, screen, cameraDirection, matrix):
        self._model.show(screen, cameraDirection, matrix)


if __name__ == "__main__":
    donut = Donut()

    running = True

    cameraDirection = [[0], [0], [-1], [0]]

    cameraPos = [[0], [0], [0], [1]]

    speed = 10

    angel = 0

    your_mesh = mesh.Mesh.from_file('Toilet.stl')

    model = Model(polygons=your_mesh.vectors)


    while running:

        donut.clock.tick(donut.fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            cameraPos = add_vector(cameraPos,  mul_vector_by_scalar(cameraDirection, speed))

        elif keys[pygame.K_s]:
            cameraPos = sub_vector(cameraPos,  mul_vector_by_scalar(cameraDirection, speed))

        if keys[pygame.K_a]:
            normal = normalize(crossProduct([[0], [1], [0], [1]], cameraDirection))
            cameraPos = add_vector(cameraPos,  mul_vector_by_scalar(normal, speed))

        elif keys[pygame.K_d]:
            normal = normalize(crossProduct([[0], [1], [0], [1]],  cameraDirection))
            cameraPos = sub_vector(cameraPos,  mul_vector_by_scalar(normal, speed))

        m = RotationZ(-90)

        m = mul_matrix(RotationX(angel), m)

        # m = mul_matrix(RotationY(angel), m)


        angel = (angel + 1) % 360

        m = mul_matrix(Scale(10, 10, 10), m)

        m = mul_matrix(Translation(0 , 0, -3000), m)

        m = mul_matrix(LookAt(cameraPos, add_vector(cameraPos, cameraDirection), [[0], [1], [0], [0]]), m)

        m = mul_matrix(PerspectiveProjection(100, donut.width/donut.height, 1, 10000), m)


        donut.clear()


        model.show(donut, cameraDirection, m)


        donut.show()