import numpy as np
import pygame

from Camera import Camera
from ScreanOutput import Grafic


class Donut:
    def __init__(self):
        self.gameObjects = []
        self.width = 1200
        self.height = 800
        self.fps = 300
        self.running = True

        self.angel = 0

        pygame.init()
        pygame.mixer.init()  # для звука
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.grafic = Grafic()
        self.lightDirection = np.array([1, 0, 0, 0])

        self.camera = Camera()

    def showScreen(self):
        self.screen.blit(self.grafic.getSurface(), (0, 0))
        pygame.display.flip()
        self.grafic.clear()

    def addObject(self, gm):
        self.gameObjects.append(gm)

    def drawObjects(self):
        for i in self.gameObjects:
            i.show(self.grafic, self.camera.direction, self.camera.position, self.lightDirection, self.width,
                   self.height, self.camera.up)

        self.showScreen()

    def moveObject(self, i, a):
        self.gameObjects[i]._position += a