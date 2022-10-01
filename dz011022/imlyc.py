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


    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()


    def turn_left(self):
        n_a = np.zeros((self.img.shape[1], self.img.shape[0], self.img.shape[2]), dtype=np.uint8)
        for irow in range(self.img.shape[1]):
            for icol in range(self.img.shape[0]):
                n_a[irow, icol] = self.img[self.img.shape[0] - icol - 1, self.img.shape[1] - irow - 1]
        self.new_img = n_a
