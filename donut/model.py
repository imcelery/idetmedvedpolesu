import math
import random

from matrix import *

import pycuda
import pycuda.driver as cuda
from pycuda import compiler, gpuarray, tools
import threading
import numpy as np
import time


# -- initialize the device
import pycuda.autoinit

min_light = 0.2


# Inheritance for using thread


def matmul(a_gpu, b_gpu):
    kernel_code_template = """
    __global__ void MatrixMulKernel(float *A, float *B, float *C)
    {
      const int bx = blockIdx.x;
      const int by = blockIdx.y;


      const int tx = threadIdx.x;
      const int ty = threadIdx.y;

      
    


    float Csub = 0;
    
    int c = by * %(mx)s * %(gr)s * 4 + bx * %(gr)s * 4;
    
    for(int i = 0; i < 4; i++){
     Csub += B[tx * 4 + i] * A[ty * 4 + i + c];
    }

      C[4 * ty + tx + c] = Csub;
    }
    """


    gr = 4


    m = math.ceil(len(a_gpu) / gr)

    mx = int(m / math.ceil(math.sqrt(m)))
    my = int(math.ceil(m / mx))


    kernel_code = kernel_code_template % {
        'mx': mx,
        'gr': gr

        }

    # compile the kernel code
    mod = compiler.SourceModule(kernel_code)
    # create empty gpu array for the result (C = A * B)

    c_gpu = gpuarray.empty((len(a_gpu), 4), np.float32)

    # get the kernel function from the compiled module
    matrixmul = mod.get_function("MatrixMulKernel")

    # call the kernel on the card



    matrixmul(
        # inputs
        a_gpu, b_gpu,
        # output
        c_gpu,
        # grid of multiple blocks
        grid = (mx, my),

        # block of multiple threads
        block = (4, gr, 1),
        )

    return c_gpu






class Model:
    def __init__(self):
        self.polygons = np.array([])

    def load(self, polygons):
        self.polygons = np.array([[[j[0], j[1], j[2], 1] for j in y] for y in polygons])


    def multiple(self, matrix, width, height):

        beg = time.time()
        some_list = self.polygons.reshape(len(self.polygons)*3, 4)

        some_list = some_list.astype(np.float32)

        some_list_gpu = gpuarray.to_gpu(some_list)


        some_matrix = matrix.astype(np.float32)
        some_matrix_gpu = gpuarray.to_gpu(some_matrix)

        output = matmul(some_list_gpu, some_matrix_gpu).get()

        print(time.time() - beg)
        beg = time.time()
        for i in range(len(output)):
            output[i][0] = output[i][0] / output[i][3] * width / 2
            output[i][1] = output[i][1] / output[i][3] * height / 2

        pol = output.reshape((len(output)//3, 3, 4))
        print(time.time() - beg)



        o = []
        beg = time.time()
        for i in range(len(self.polygons)):
            p = []
            for j in range(len(self.polygons[i])):
                vertex = np.matmul(matrix, self.polygons[i, j])
                # vertex[0] = vertex[0] / vertex[3] * width / 2
                # vertex[1] = vertex[1] / vertex[3] * height / 2
                p.append(vertex)
            o.append(p)
        print(time.time() - beg)
        print()
        return o


    def show(self, grafic, cameraDirection, cameraPosition, light_direction, matrix):
        screen_vectrors = self.multiple(matrix, grafic._width, grafic._height)
        o = []
        for i in screen_vectrors:
            v1 = i[0]

            v2 = i[1]

            v3 = i[2]

            t1 = np.subtract(v1, v2)

            t2 = np.subtract(v2,  v3)

            normal = normalize(cross(t1, t2))
            
            res = np.dot(normal, cameraDirection)

            if res < 0:
                p = [0, 0, 0, 0]
                for j in range(3):
                    p[0] += v1[j]/3
                    p[1] += v2[j] / 3
                    p[2] += v3[j] / 3

                l = np.linalg.norm(cameraPosition - p)
                s = np.dot(normal, light_direction)
                s = max(min_light, s)
                o.append([l, i, s])\


        on = np.array(o, dtype=object)

        on = on[on[:, 0].argsort()]


        for i in on[::-1]:
            grafic.drawPoly(i[1],np.array([255, 255, 255]) * i[2])

