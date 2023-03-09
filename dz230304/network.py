import numpy as np
import math
import time


class Layer:
    def __init__(self, size):
        self.size = size
        self.neurons = [0] * size
        self.biases = []
        self.weights = []


def sigmoid(x):
    if x > 700:
        x = 700
    if x < -700:
        x = -700
    return 1 / (1 + math.exp(-x))


def derivsigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


class NeuralNetwork:
    def __init__(self, learningRate, sizes):
        self.learningRate = learningRate
        self.layers = []
        for i in range(len(sizes)):
            nextSize = 0
            if i < len(sizes) - 1:
                nextSize = sizes[i + 1]
            self.layers.append(Layer(sizes[i]))
            for j in range(sizes[i]):
                self.layers[i].biases.append(np.random.normal())
                self.layers[i].weights.append([])
                for k in range(nextSize):
                    self.layers[i].weights[j].append(np.random.normal())


    def feedforward(self, inputs):
        self.layers[0].neurons = inputs
        for i in range(len(self.layers) - 1):
            for j in range(self.layers[i + 1].size):
                self.layers[i + 1].neurons[j] = 0
                for k in range(self.layers[i].size):
                    self.layers[i + 1].neurons[j] += self.layers[i].neurons[k] * self.layers[i].weights[k][j]
                self.layers[i + 1].neurons[j] = sigmoid(self.layers[i + 1].neurons[j] + self.layers[i + 1].biases[j])
        return self.layers[len(self.layers) - 1].neurons.copy()


    def backpropagation(self, targets):
        errors = []
        for i in range(self.layers[len(self.layers) - 1].size):
            errors.append(targets[i] - self.layers[len(self.layers) - 1].neurons[i])
        k = len(self.layers) - 2
        while k >= 0:
            gradients = []
            for i in range(self.layers[k + 1].size):
                gradients.append(errors[i] * derivsigmoid(self.layers[k + 1].neurons[i]) * self.learningRate)
            deltas = []
            for i in range(self.layers[k + 1].size):
                deltas.append([])
                for j in range(self.layers[k].size):
                    deltas[i].append(gradients[i] * self.layers[k].neurons[j])
            errorsNext = []
            for i in range(self.layers[k].size):
                errorsNext.append(0)
                for j in range(self.layers[k + 1].size):
                    errorsNext[i] += self.layers[k].weights[i][j] * errors[j]
            errors = errorsNext
            weightsNew = []
            for j in range(self.layers[k].size):
                weightsNew.append([])
                for i in range(self.layers[k + 1].size):
                    weightsNew[j].append(self.layers[k].weights[j][i] + deltas[i][j])
            self.layers[k].weights = weightsNew
            for i in range(self.layers[k + 1].size):
                self.layers[k + 1].biases[i] += gradients[i]
            k = k - 1

    def train(self, epochs, data, y_trues):
        start_time = time.time()
        for i in range(epochs):

            for x, y in zip(data, y_trues):
                self.feedforward(x)
                self.backpropagation(y)
        print("--- %s seconds ---" % (time.time() - start_time))

    def safe(self, file):
        with open(file, "w") as f:
            f.write(str(self.learningRate) + "\n")
            f.write(str(len(self.layers)) + "\n")
            for i in self.layers:
                f.write(str(i.size) + "\n")
                f.write(str(i.weights) + "\n")
                f.write(str(i.biases) + "\n")
            f.close()

    def load(self, file):
        with open(file, "r") as f:
            self.learningRate = float(f.readline())
            self.layers = []
            n = int(f.readline())
            for i in range(n):
                s = int(f.readline())
                a = Layer(s)
                a.weights = eval(f.readline().strip())
                a.biases = eval(f.readline())
                self.layers.append(a)

            f.close()