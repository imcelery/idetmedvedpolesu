import collections
import math
from collections import deque

def f():
    n , m, y, x, y1, x1 = list(map(int, input().split()))


    x -= 1
    y -= 1
    x1 -= 1
    y1 -= 1

    carta = []

    def bo(x):

        if x == ".":
            return 1
        if x == "#":
            return 0
        if x == "W":
            return 2

    for i in range(n):
        b = input().strip()

        a = list(map(bo, b))

        carta.append(a)


    def g(carta, x, y, n, m):

        q = deque([(y, x)])

        was = set()

        dotkuda = {}
        dwas = {(y, x) : 0}

        moves = [(1, 0, "S"), (0, 1, "E"), (0, -1, "W"), (-1, 0, "N")]

        while len(q) != 0:
            a = q.popleft()
            was.add(a)

            for i in moves:
                np = (a[0] + i[0], a[1] + i[1])
                if 0 > np[0] or n <= np[0] or 0 > np[1] or m <= np[1] or carta[np[0]][np[1]] == 0:
                    continue

                if np not in was:
                    b = False
                    if np in dwas:
                        if dwas[a] + carta[a[0]][a[1]] < dwas[np]:
                            dwas.update({np : dwas[a] + carta[a[0]][a[1]]})
                            dotkuda.update({np: i[2]})
                            if carta[a[0]][a[1]] == 1:
                                b = True
                    else:

                        dwas.update({np: dwas[a] + carta[a[0]][a[1]]})
                        dotkuda.update({np: i[2]})
                        if carta[a[0]][a[1]] == 1:
                            b = True
                    if b:
                        q.appendleft(np)
                    else:
                        q.append(np)
        return dwas, dotkuda

    dwas, dotkuda = g(carta, x, y, n, m)

    s = dwas.get((y1, x1))
    if s != None:
        print(s)
        d = { "S" :(1, 0), "E" :  (0, 1) , "W" : (0, -1),"N": (-1, 0)}
        s = ""

        while x  != x1 or y  != y1:

            l = dotkuda[(y1, x1)]
            s += l
            m = d[l]
            x1 -= m[1]
            y1 -= m[0]
        print(s[::-1])
    else:
        print(-1)

f()