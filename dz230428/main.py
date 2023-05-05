import math

sizes = [8, 6, 4]

import random
import pygame as pg
import numpy as np

class Agent:
    def __init__(self):
        self.weights = self.get_random_weights(sizes)
        self.speed = 0
        self.chord = 0

    def get_random_weights(self, size):
        w = []
        for i in range(len(size) - 1):
            s = []
            for j in range(size[i]):
                d = []
                for k in range(size[i + 1]):
                    d.append(random.randint(-100, 100)/100)
                s.append(d)
            w.append(s)
        return np.array(w)

    def move(self):
        o = ff(self.weights, [self.speed, self.chord])
        o = o.index(max(o))
        if o == 1:
            self.speed += 1
        else:
            self.speed -= 1

        self.chord += self.speed


def sigmoid(x):

    return 1/ (1 + math.exp(-x))

def ff(weights, inp):

    for i in range(1, len(weights)):
        print(weights[i - 1], inp)
        w = np.matmul(weights[i - 1], inp)

        inp = list(map(sigmoid, w))
        print(inp)

    return inp

print(ff([[[1, 1], [1, 1]], [[1], [1]], [[1]]], [1, 1]))




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
