
import math

import numpy as np
width = 9
r = 1
R = 2.5
degrees = 0
n = 10

def INSIDE_TORUS(p, TOROIDAL_RADIUS, POLOIDAL_RADIUS):
    angle_xy = np.arctan2(p[1], p[0])
    p = [p[0] - TOROIDAL_RADIUS * np.cos(angle_xy), p[1] - TOROIDAL_RADIUS * np.sin(angle_xy), p[2]]
    return -POLOIDAL_RADIUS <= np.linalg.norm(p) <= POLOIDAL_RADIUS

for i in range(n):

    rad = math.radians(degrees)
    print(rad)
    a = np.zeros((width, width, width))
    for x in range(-(width//2), (width//2) + 1):
        for y in range(-(width//2), (width//2) + 1):
           for z in range(-(width//2), (width//2) + 1):
               h = math.hypot(x, z)
               nz, nx = h * math.sin(rad), h * math.cos(rad)
               if INSIDE_TORUS([nx, y, nz,], R, r):
                   a[x + (width)//2, y+ (width)//2, z+ (width)//2] = 1
    s = ""
    for x in range(width):
        for y in range(width):
            if sum(a[x,y]) > 0:
                s += "@"
            else:
                s += "_"
        s += "\n"
    degrees = (degrees + 360 // n) % 180

    print(s)