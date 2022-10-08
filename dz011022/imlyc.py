import numpy
import numpy as np
from PIL import Image
from copy import deepcopy

class ImageL:
    def __init__(self, filepath):
        with Image.open(filepath) as img:
            img.load()
        self.img = np.asarray(img)
        self.new_img = deepcopy(self.img)


    def save_img(self, fileanme):
        new_img = Image.fromarray(self.new_img)
        new_img.save(fileanme)


    def grey_img(self):
        n_a = np.zeros(self.img.shape, dtype=np.uint8)
        for irow in range(self.img.shape[0]):
            for icol in range(self.img.shape[1]):
                r = np.mean(self.img[irow, icol])
                n_a[irow, icol] = (r, r, r)
        self.new_img = n_a


    def upside_down(self):
        n_a = np.zeros(self.img.shape, dtype=np.uint8)
        for irow in range(self.img.shape[0]):
            for icol in range(self.img.shape[1]):
                r = self.img[self.img.shape[0] - irow - 1, icol]
                n_a[irow, icol] = r
        self.new_img = n_a
    def umnoshenie(self,a, b, c):
        n_a = np.zeros(a.shape, dtype=np.uint8)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                n_a[i, j, c] = a[i, j, c] * b[i,j]
        return n_a

    def blur(self):
        g_a = np.ones((10, 10))
        b = g_a.shape[0] // 2
        n_a = np.zeros(self.img.shape, dtype=np.uint8)
        n_ch = np.ones((2 * b + n_a.shape[0], 2 * b + n_a.shape[1], n_a.shape[2]), dtype=np.uint8)
        n_ch[b: -b, b: -b] = self.img
        for i in range( n_a.shape[0]):
            for j in range(n_a.shape[1]):
                n_a[i, j] = (np.mean(n_ch[i: 2 * b + i , j : j+2 * b, 0] * g_a), np.mean(n_ch[i: 2 * b + i , j : j+2 * b, 1] * g_a), np.mean(n_ch[i: 2 * b + i , j : j+2 * b, 2] * g_a))
        self.new_img = n_a



    def turn_left(self):
        n_a = np.zeros((self.img.shape[1], self.img.shape[0], self.img.shape[2]), dtype=np.uint8)
        for irow in range(self.img.shape[1]):
            for icol in range(self.img.shape[0]):
                n_a[irow, icol] = self.img[icol, self.img.shape[1] - irow - 1]
        self.new_img = n_a

    def turn_right(self):
        n_a = np.zeros((self.img.shape[1], self.img.shape[0], self.img.shape[2]), dtype=np.uint8)
        for irow in range(n_a.shape[0]):
            for icol in range(n_a.shape[1]):
                n_a[irow, icol] = self.img[self.img.shape[0] - icol - 1, irow]
        self.new_img = n_a
