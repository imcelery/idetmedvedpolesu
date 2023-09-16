import random
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, m, s):
        Thread.__init__(self)
        self.m = m
        self.s = s
        self.value = 0

    def run(self):
        for i in range(len(self.m)):
            self.value += self.m[i] * self.s[i]


if __name__ == "__main__":
    r = 100
    m, n = map(int, input().split())
    matrix = []
    for i in range(n):
        s = []
        for j in range(m):
            s.append(random.randint(-r, r))
        matrix.append(s)

    s = []
    for j in range(m):
        s.append(random.randint(-r, r))
    threads = []
    for i in range(n):
        th = MyThread(matrix[i], s)
        th.start()
        threads.append(th)

    output = []

    for i in range(n):
        threads[i].join()
        output.append(threads[i].value)

    print(f"Max: {max(output)}")
    print(f"Min: {min(output)}")