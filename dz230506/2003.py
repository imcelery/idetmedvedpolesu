import collections
from collections import deque

def f():
    n , m, x, y, x1, y1= list(map(int, input().split()))

    carta = []

    def bo(x):

        if x == ".":
            return 1
        if x == "#":
            return 2
        if x == "W":
            return 0

    for i in range(n):
        b = input().strip()

        a = list(map(bo, b))

        carta.append(a)




    print(carta)
    def g(carta, x, y, x1, y1, n, m):

        q = deque([(x - 1, y - 1)])

        was = set()

        dotkuda = {}
        dwas = {}

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while len(q) != 0:
            a = q.popleft()
            was.add(a)

            for i in moves:
                np = (a[0] + i[0], a[1] + i[1])
                if 0 > np[0] or m <= np[0] or 0 > np[1] or n <= np[1]:
                    continue

                if np not in was:
                    dwas.update({np : a})
                    if i == s:
                        k = i
                        oar = [k]

                        while k != b:
                            k = dwas[k]

                            oar.append(k)
                        return oar

                    q.append(i)
        return -1

    o = g(carta, x, y, x1, y1)
    if o != -1:
        print(len(o) - 1)
        print(" ".join(map(str, reversed(o))))
    else:
        print(o)

f()