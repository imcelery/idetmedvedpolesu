import pygame

import sys

from Donut import Donut
from GameObject import GameObject

from stl import mesh

if __name__ == "__main__":

    donut = Donut()

    speed = 3

    angelSpeed = 1

    your_mesh = mesh.Mesh.from_file('arrow.stl')

    gm = GameObject()
    gm.set_model(your_mesh.vectors)
    donut.addObject(gm)

    clock = pygame.time.Clock()

    while donut.running:
        # print(donut.clock.get_fps())

        donut.clock.tick(donut.fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            donut.camera.moveForward(speed)

        elif keys[pygame.K_s]:
            donut.camera.moveForward(-speed)

        if keys[pygame.K_a]:
            donut.camera.moveRight(-speed)

        elif keys[pygame.K_d]:
            donut.camera.moveRight(speed)

        if keys[pygame.K_SPACE]:
            pass
            # vy = 100

        elif keys[pygame.K_c]:
            pass
            # donut.cameraPosition = np.subtract(donut.cameraPosition,  np.array([0, 1, 0, 1]) * speed)

        if keys[pygame.K_q]:
            donut.camera.rotateCamera(-angelSpeed)

        elif keys[pygame.K_e]:
            donut.camera.rotateCamera(angelSpeed)

        donut.drawObjects()
