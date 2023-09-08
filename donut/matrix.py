import math
import numpy as np



def cross(a, b):
    return np.array([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0], a[3]])


def normalize(a):
    l = np.linalg.norm(a)
    if l != 0.:
        return np.array([a[0] / l, a[1] / l, a[2] / l, a[3]])
    else:
        return np.array( [0, 0, 0, 0])


def Translation(dx, dy, dz):

        return np.array([
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1],])


def Scale(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1],
    ])

def RotationX(angle):
    rad = math.pi / 180 * angle
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(rad), -math.sin(rad), 0],
        [0, math.sin(rad), math.cos(rad), 0],
        [0, 0, 0, 1],
    ])

def RotationY(angle):
    if angle == 0:
        return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])
    rad = math.pi / 180 * angle
    return np.array([
        [math.cos(rad), 0, math.sin(rad), 0],
        [0, 1, 0, 0],
        [-math.sin(rad), 0, math.cos(rad), 0],
        [0, 0, 0, 1],])


def RotationZ(angle):

    rad = math.pi / 180 * angle
    return np.array([
        [math.cos(rad), -math.sin(rad), 0, 0],
        [math.sin(rad), math.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])


def LookAt(eye, target, up):

    vz = normalize(np.subtract(target, eye))

    vx = normalize(cross(up, vz))

    vy = normalize(cross(vz, vx))
    t = Translation(-eye[0], -eye[1], -eye[2])

    m = np.array([
        [vx[0], vx[1], vx[2], 0],
        [vy[0], vy[1], vy[2], 0],
        [vz[0], vz[1], vz[2], 0],
        [0, 0, 0, 1]])
    return np.matmul(t, m)

def PerspectiveProjection(fovy, aspect, n, f):
    radians = np.pi / 180 * fovy
    sx = (1 / np.tan(radians / 2)) / aspect
    sy = (1 / np.tan(radians / 2))
    sz = (f + n) / (f - n)
    dz = (-2 * f * n) / (f - n)
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, dz],
        [0, 0, -1, 0]])
