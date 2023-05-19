import math


class KuchaGovna:
    def __init__(self, a):

        self._govno = sorted(a, reverse=True) + [-math.inf for i in range(2 ** math.ceil(math.log2(len(a) + 1)) - len(a) - 1)]
        self._count = len(a)
        self.maxsize = 2 ** math.ceil(math.log2(self._count)) - 1



    def __len__(self):
        return self._count

    def __str__(self):
        return str(self._govno)

    def razmeshat_vniz(self, i):

        while 2 * i + 2 < self.maxsize:
            largest = i
            left = 2 * i + 2
            right = 2 * i + 1
            if self._govno[largest] < self._govno[left]:
                largest = left

            if self._govno[largest] < self._govno[right]:
                largest = right

            self._govno[i], self._govno[largest] = self._govno[largest], self._govno[i]



            if i == largest:
                break

            i = largest

    def razmeshat_vverh(self, i):

        while i > 0:

            if self._govno[i] > self._govno[i // 2]:
                self._govno[i], self._govno[i // 2] = self._govno[i // 2], self._govno[i]
            else:
                break
            i = i // 2


    def razmeshat(self):
        for i in range(self._count):
            self.razmeshat_vniz(i)

    def nasrat(self, el):

        if not self._count < self.maxsize:
            self._govno += [-math.inf for i in range(self.maxsize + 1)]

        self.maxsize = self.maxsize * 2 + 1
        self._govno[self._count] = el
        self.razmeshat_vverh(self._count)
        self._count += 1

    def visrat(self):
        out = self._govno[0]
        self._govno[0] = self._govno[self._count - 1]
        self._govno[self._count - 1] = -math.inf
        self.razmeshat_vniz(0)
        return out
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g = KuchaGovna([1, 3, 2, -21, 23, 32, -1 ])

    for i in range(6):
        print(g.visrat())



