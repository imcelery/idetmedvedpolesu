import math

class KuchaGovna:
    def __init__(self, a = []):
        if len(a) > 0:
                self._govno = a + [(math.inf, math.inf) for i in range(2 ** math.ceil(math.log2(len(a) + 1)) - len(a) - 1)]
                self._count = len(a)
                self.maxsize = 2 ** math.ceil(math.log2(self._count)) - 1
                self.razmeshat()
        else:
                self._govno = []
                self._count = 0
                self.maxsize = 0

    
    
    def __len__(self):
        return self._count

    def __str__(self):
        return str(self._govno)

    def razmeshat_vniz(self, i):

        while 2 * i + 2 < self.maxsize:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if self._govno[largest] > self._govno[left]:
                largest = left

            if self._govno[largest] > self._govno[right]:
                largest = right

            self._govno[i], self._govno[largest] = self._govno[largest], self._govno[i]

            if i == largest:
                break

            i = largest

    def razmeshat_vverh(self, i):
        while i > 0:
            if self._govno[i] < self._govno[i // 2]:
                self._govno[i], self._govno[i // 2] = self._govno[i // 2], self._govno[i]
            else:
                break
            i = i // 2


    def razmeshat(self):
        for i in range(self._count):
            self.razmeshat_vniz(i)

    def nasrat(self, el):

        if self._count >= self.maxsize:
            self._govno += [(math.inf, math.inf) for i in range(self.maxsize + 1)]
            self.maxsize = self.maxsize * 2 + 1
        self._govno[self._count] = el
        self.razmeshat_vverh(self._count)
        self._count += 1

    def visrat(self):
        out = self._govno[0]
        self._govno[0] = self._govno[self._count - 1]
        self._govno[self._count - 1] = (math.inf, math.inf)
        self.razmeshat_vniz(0)
        self._count -= 1
        return out

class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d.keys():
                d.update({i : 1})
            else:
                d[i] += 1
        g = KuchaGovna()
        for i in d.keys():
            g.nasrat((- d[i], i))



        s = ""

        while len(g) != 0:
            o = g.visrat()
            s += o[1] * -o[0]

        return s




