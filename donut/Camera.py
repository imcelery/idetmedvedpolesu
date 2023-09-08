import numpy as np

from matrix import normalize, cross


class Camera:
    def __init__(self):
        self.angelX = 0
        self.angelY = -90
        self.direction = np.zeros((4))
        self.position = np.array([0., 0., 0., 0.])
        self.up = np.array([0., 1., 0., 0.])
        self.right = np.zeros((4))

        self.rotateCamera(0)

    def moveForward(self, s):
        self.position += s * self.direction



    def moveRight(self, s):
        self.position += self.right * s;

    def rotateCamera(self, a):
        self.angelY += a
        self.direction = np.zeros((4))
        self.direction[0] = np.cos(np.radians(self.angelX)) * np.cos(np.radians(self.angelY))
        self.direction[1] = np.sin(np.radians(self.angelX))
        self.direction[2] = np.cos(np.radians(self.angelX)) * np.sin(np.radians(self.angelY))

        self.direction = normalize(self.direction)
        self.right = normalize(cross(self.direction, self.up))



