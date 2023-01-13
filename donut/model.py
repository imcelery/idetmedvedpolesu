from matrix import *


class Model:
    def __init__(self):
        self.polygons = []

    def load(self, polygons):
        self.polygons = []

        for i in polygons:
            ss = []
            for j in i:
                s = [[j[0]], [j[1]], [j[2]], [1]]
                ss.append(s)
            self.polygons.append(ss)

    def multiple(self, matrix, screen):
        o = []
        for i in range(len(self.polygons)):
            p = []
            for j in range(len(self.polygons[i])):
                vertex = mul_matrix(matrix, self.polygons[i][j])
                vertex[0][0] = vertex[0][0] / vertex[3][0] * screen.width / 2
                vertex[1][0] = vertex[1][0] / vertex[3][0] * screen.height / 2
                p.append(vertex)
            o.append(p)
        return o

    def show(self, screen, cameraDirection, matrix):
        screen_vectrors = self.multiple(matrix, screen)
        for i in screen_vectrors:
            v1 = i[0]

            v2 = i[1]

            v3 = i[2]

            t1 = sub_vector(v1, v2)

            t2 = sub_vector(v2,  v3)

            normal = normalize(crossProduct(t1, t2))
            
            res = scalarProduct(normal, cameraDirection)

            if res > 0 or True:
                screen.drawLine(
                    v1[0][0],
                    v1[1][0],
                    v2[0][0],
                    v2[1][0],
                    (0, 0, 255))

                screen.drawLine(
                    v2[0][0],
                    v2[1][0],
                    v3[0][0],
                    v3[1][0],
                    (0, 0, 255))

                screen.drawLine(
                    v1[0][0],
                    v1[1][0],
                    v3[0][0],
                    v3[1][0],
                    (0, 0, 255))


