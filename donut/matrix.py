import math


def crossProduct(a, b):
    return [[a[1][0] * b[2][0] - a[2][0] * b[1][0]], [a[2][0] * b[0][0] - a[0][0] * b[2][0]], [a[0][0] * b[2][0] - a[1][0] * b[1][0]], [a[3][0]]]


def mul_vector_by_scalar(a, b):
    return [[a[0][0] * b], [a[1][0] * b], [a[2][0] * b], [a[3][0] * b]]
    

def add_vector(a, b):
    return [[a[0][0] + b[0][0]], [a[1][0] + b[2][0]], [a[2][0] + b[2][0]], [a[3][0]]]


def sub_vector(a, b):
    return [[a[0][0] - b[0][0]], [a[1][0] - b[1][0]], [a[2][0] - b[2][0]], [a[3][0]]]


def scalarProduct(a, b):
    return a[0][0] * b[0][0] + a[1][0] * b[1][0] + a[2][0] * b[2][0]


def lenght(a):
    return math.sqrt(a[0][0] ** 2 + a[1][0] ** 2 + a[2][0] ** 2)


def normalize(a):
    l = lenght(a)
    if l != 0.:
        return [[a[0][0] / l], [a[1][0] / l], [a[2][0] / l], [a[3][0]]]
    else:
        return [[0], [0], [0], [0]]


def mul_matrix(a, b):

    m = [[ 0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]

            m[i][j] = s
    return m


def Translation(dx, dy, dz):

        return [
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1],]


def Scale(sx, sy, sz):
    return[
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1],
    ]

def RotationX(angle):
    rad = math.pi / 180 * angle
    return[
        [1, 0, 0, 0],
        [0, math.cos(rad), -math.sin(rad), 0],
        [0, math.sin(rad), math.cos(rad), 0],
        [0, 0, 0, 1],
    ]

def RotationY(angle):
    rad = math.pi / 180 * angle
    return[
        [math.cos(rad), 0, math.sin(rad), 0],
        [0, 1, 0, 0],
        [-math.sin(rad), 0, math.cos(rad), 0],
        [0, 0, 0, 1],
    ]


def RotationZ(angle):

    rad = math.pi / 180 * angle
    return[
        [math.cos(rad), -math.sin(rad), 0, 0],
        [math.sin(rad), math.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]


def LookAt(eye, target, up):

    vz = normalize(sub_vector(eye, target))
    vx = normalize(crossProduct(up, vz))
    vy = normalize(crossProduct(vz, vx))
    t = Translation(-eye[0][0], -eye[1][0], -eye[2][0])

    m = [
        [vx[0][0], vx[1][0], vx[2][0], 0],
        [vy[0][0], vy[1][0], vy[2][0], 0],
        [vz[0][0], vz[1][0], vz[2][0], 0],
        [0, 0, 0, 1]]
    return mul_matrix(t, m)

def PerspectiveProjection(fovy, aspect, n, f):
    radians = math.pi / 180 * fovy
    sx = 1 / math.tan(radians / 2) / aspect
    sy = 1 / math.tan(radians / 2)
    sz = (f + n) / (f - n)
    dz = (-2 * f * n) / (f - n)
    return[
    [sx, 0, 0, 0],
    [0, sy, 0, 0],
    [0, 0, sz, dz],
    [0, 0, -1, 0]]
