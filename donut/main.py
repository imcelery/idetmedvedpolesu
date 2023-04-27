import pygame

import sys

from model import *

from matrix import *

import numpy as np

from stl import mesh

import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

import os
if (os.system("cl.exe")):
    os.environ['PATH'] += ';'+r"D:\programs\vs\VC\Tools\MSVC\14.35.32215\bin\Hostx64\x64"


class Donut:
    def __init__(self):
        self.gameObjects = []
        self.width = 1200
        self.height = 800
        self.fps = 30
        self.running = True
        self.angel = 0

        pygame.init()
        pygame.mixer.init()  # для звука
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.grafic = Grafic()

        self.cameraDirection = np.array([0, 0, -1, 0])
        self.lightDirection = np.array([1, 0, 0, 0])

        self.cameraPosition = np.array([0, 0, 0, 1])

    def showScreen(self):
        self.screen.blit(self.grafic.getSurface(), (0, 0))
        pygame.display.flip()
        self.grafic.clear()

    def addObject(self, gm):
        self.gameObjects.append(gm)

    def drowObjects(self):
        for i in self.gameObjects:
            i.show(self.grafic, self.cameraDirection, self.cameraPosition, self.lightDirection, self.width, self.height, self.angel)
        self.showScreen()

    def moveObject(self, i, a):
        self.gameObjects[i]._position += a


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
        pygame.draw.line(self._surface, color, (x1 + self._width // 2, -(y1 - self._height // 2)), (x2 + self._width // 2, -(y2 - self._height // 2)))

        # c1 = y2 - y1
        # c2 = x2 - x1
        # if c1 == 0 and c2 == 0:
        #     return None
        # length = math.sqrt(c1 * c1 + c2 * c2)
        #
        # xStep = c2 / length
        # yStep = c1 / length
        #
        # for i in range(int(length)):
        #     self.drawPixel(
        #         math.trunc(x1 + xStep * i),
        #         math.trunc(y1 + yStep * i),
        #         color)

    def drawPoly(self, vec, color):
        b = []
        for i in range(3):
            x = int(vec[i][0]) + self._width // 2
            y = -(int(vec[i][1]) - self._height // 2)
            b.append((x,y))
        print(b)
        pygame.draw.polygon(self._surface, color, b)


class GameObject:
    def __init__(self):
        self._position = np.array([0, 0, -1300])
        self._rotation = np.array([0, 0, 0, 1])
        self._model = Model()

    def set_model(self, polygons):
        self._model.load(polygons)

    def show(self, grafic, cameraDirection, cameraPosition, lightDirection, width, height, angel):

        m = RotationX(-90)

        m = np.matmul(RotationY(angel), m)

        m = np.matmul(Scale(100, 100, 100), m)

        m = np.matmul(Translation(*self._position), m)


        m = np.matmul(LookAt(cameraPosition, np.add(cameraPosition, cameraDirection), [0, 1, 0, 0]), m)

        m = np.matmul(PerspectiveProjection(100, width / height, 1, 10000), m)

        self._model.show(grafic, cameraDirection, cameraPosition,lightDirection, m)


if __name__ == "__main__":


    donut = Donut()


    speed = 30

    angelspeed = 5

    your_mesh = mesh.Mesh.from_file('xxx.stl')

    gm = GameObject()
    gm.set_model(your_mesh.vectors)
    donut.addObject(gm)
    vy = 0
    y = 0

    clock = pygame.time.Clock()



    while donut.running:
        #ssprint(donut.clock.get_fps())

        donut.clock.tick(donut.fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()



        # vy -= 10
        # y = y + vy



        if keys[pygame.K_w]:
            donut.moveObject(0, speed * np.array([0, 0, -1]))
            #donut.cameraPosition = np.add(donut.cameraPosition,  donut.cameraDirection * speed)

        elif keys[pygame.K_s]:
            donut.moveObject(0, speed * np.array([0, 0, 1]))
            #donut.cameraPosition = np.subtract(donut.cameraPosition, donut.cameraDirection * speed)

        if keys[pygame.K_a]:
            donut.moveObject(0, speed * np.array([-1, 0, 0]))
            #normal = normalize(cross(np.array([0, 1, 0, 1]), donut.cameraDirection))
            #donut.cameraPosition = np.add(donut.cameraPosition,  normal * speed)

        elif keys[pygame.K_d]:
            donut.moveObject(0, speed * np.array([1, 0, 0]))
            # normal = normalize(cross(np.array([0, 1, 0, 1]),  donut.cameraDirection))
            # donut.cameraPosition = np.subtract(donut.cameraPosition,  normal * speed)

        if keys[pygame.K_SPACE]:
            pass
            #vy = 100




        elif keys[pygame.K_c]:
            pass
            #donut.cameraPosition = np.subtract(donut.cameraPosition,  np.array([0, 1, 0, 1]) * speed)

        donut.moveObject(0, vy * np.array([0, 1, 0]))

        if keys[pygame.K_q]:
            donut.angel += angelspeed

        elif keys[pygame.K_e]:

            donut.angel -= angelspeed



        donut.drowObjects()

