import math


class KuchaGovna:
    def __init__(self, a=[]):
        if len(a) > 0:
            self._govno = a + [math.inf for i in range(2 ** math.ceil(math.log2(len(a) + 1)) - len(a) - 1)]
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
            if self._govno[largest] == self._govno[left] or self._govno[largest] == self._govno[right]:
                self._govno[largest] = math.inf

            if self._govno[left] == self._govno[right]:
                self._govno[left] = math.inf
                self.razmeshat_vniz(left)


            if self._govno[largest] > self._govno[left]:
                largest = left

            if self._govno[largest] > self._govno[right]:
                largest = right

            if i == largest:
                break

            self._govno[i], self._govno[largest] = self._govno[largest], self._govno[i]

            i = largest

    def razmeshat_vverh(self, i):
        while (i -1)//2 > 0:
            if self._govno[i] == self._govno[(i - 1) // 2]:
                self._govno[i] = math.inf
                self.razmeshat_vniz(i)
                self._count -= 1
                break
            if self._govno[i] < self._govno[(i - 1) // 2]:
                self._govno[i], self._govno[(i - 1) // 2] = self._govno[(i - 1) // 2], self._govno[i]
            else:
                break

            i = (i - 1) // 2

    def razmeshat(self):
        for i in range(self._count):
            self.razmeshat_vniz(i)

    def nasrat(self, el):
        #print("астрать", el)
        if self._count >= self.maxsize:
            self._govno += [math.inf for i in range(self.maxsize + 1)]
            self.maxsize = self.maxsize * 2 + 1
        self._govno[self._count] = el
        self.razmeshat_vverh(self._count)
        self._count += 1

    def visrat(self):
        self.razmeshat_vniz(0)
        out = self._govno[0]
        self._govno[0] = self._govno[self._count - 1]
        self._govno[self._count - 1] = math.inf
        self._count -= 1
        self.razmeshat_vniz(0)
        print(self)
        return out


class SmallestInfiniteSet:

    def __init__(self):
        self.s = 0
        self.g = KuchaGovna()

    def popSmallest(self) -> int:
        self.s += 1
        self.g.nasrat(self.s)

        return self.g.visrat()

    def addBack(self, num: int) -> None:
        self.g.nasrat(num)

# g = SmallestInfiniteSet()
# l = ["SmallestInfiniteSet","addBack","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","addBack","popSmallest","popSmallest","addBack","addBack","addBack","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","addBack","popSmallest","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","addBack","addBack","popSmallest","addBack","popSmallest","popSmallest","addBack","addBack","addBack","popSmallest","popSmallest","addBack","addBack"]
# h = [[],[356],[879],[],[757],[721],[],[],[639],[],[],[258],[576],[857],[],[213],[],[74],[433],[],[],[],[],[139],[],[175],[],[558],[],[],[],[602],[856],[15],[],[],[],[],[638],[608],[],[817],[171],[],[31],[585],[],[454],[],[],[],[408],[203],[],[147],[],[213],[30],[],[827],[],[],[208],[927],[663],[],[],[184],[410]]
# for i in range(len(l)):
#
#     if l[i] == "addBack":
#         g.addBack(h[i][0])
#         print("------------------------------------------")
#     if l[i] == "popSmallest":
#         print(g.popSmallest())
#     print(g.g)

