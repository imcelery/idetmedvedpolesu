from matrix import *
from model import *

class GameObject:
    def __init__(self):
        self.position = np.array([0, 0, 300])
        self.rotation = np.array([0, 0, 0, 1])
        self.model = Model()

    def set_model(self, polygons):
        self.model.load(polygons)

    def show(self, grafic, cameraDirection, cameraPosition, lightDirection, width, height, up):

        m = RotationX(-90)

        m = np.matmul(Scale(10, 10, 10), m)

        m = np.matmul(Translation(*self.position), m)



        m = np.matmul(LookAt(cameraPosition,  np.add(cameraDirection, cameraPosition), up), m)

        m = np.matmul(PerspectiveProjection(100, width / height, 1, 10000), m)
        #


        self.model.show(grafic, cameraDirection, cameraPosition, lightDirection, m)
