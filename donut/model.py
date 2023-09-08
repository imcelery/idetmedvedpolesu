import math
import random

from matrix import *

import numpy as np

min_light = 0.2

class Model:
    def __init__(self):
        self.polygons = np.array([])

    def load(self, polygons):
        self.polygons = np.array([[[j[0], j[1], j[2], 1] for j in y] for y in polygons])


    def multiple(self, matrix, width, height):
        o = []
        for i in range(len(self.polygons)):
            p = []
            for j in range(len(self.polygons[i])):
                vertex = np.matmul(matrix, self.polygons[i, j])
                if vertex[3] < 0:
                    break
                vertex[0] = vertex[0] / vertex[3] * width / 2
                vertex[1] = vertex[1] / vertex[3] * height / 2
                p.append(vertex)
            else:
                o.append(p)
        return o


    def show(self, grafic, cameraDirection, cameraPosition, light_direction, matrix):
        screen_vectors = self.multiple(matrix, grafic._width, grafic._height)
        o = []
        for i in screen_vectors:
            v1 = i[0]

            v2 = i[1]

            v3 = i[2]

            t1 = np.subtract(v1, v2)

            t2 = np.subtract(v2,  v3)

            normal = normalize(cross(t1, t2))

            res = np.dot(normal, cameraDirection)

            #if res > 0:
                # grafic.drawPoly(i, np.array([255, 255, 255]))
            grafic.drawLine(v1[0], v1[1], v2[0], v2[1], np.array([255, 255, 255]))
            grafic.drawLine(v1[0], v1[1], v3[0], v3[1], np.array([255, 255, 255]))
            grafic.drawLine(v3[0], v3[1], v2[0], v2[1], np.array([255, 255, 255]))

