import collections
import math
from collections import deque


def deic(d, b):
    was = set()
    dwas = dict.fromkeys(d.keys(), math.inf)
    dwas[b] = 0
    dotkuda = {}
    m = []
    while len(d.keys()) > len(was):

        was.add(b)

        for i in d[b].keys():
            if i not in was:
                if i in dwas.keys():
                    if dwas[b] + d[b][i] < dwas[i]:
                        dwas[i] = dwas[b] + d[b][i]
                        dotkuda[i] = b
                else:
                    dwas.update({i: dwas[b] + d[b][i]})
                    dotkuda.update({i: b})
                m.append(i)

        g = sorted(m, key=lambda x: dwas[x])
        for i in g:
            if i not in was:
                b = i
                break
        else:
            break

    return dwas, dotkuda



def ffdf():
    n, s, f = list(map(int, input().split()))

    d = collections.defaultdict(dict)
    for i in range(1, n + 1):
        a = list(map(int, input().split()))
        for j in range(0, n):
            if a[j] >= 0:
                d[i].update({j + 1: a[j]})

    if s == f:
        print(s)
        return


    dwas, dout = deic(d, s)

    if dwas.get(f) != None and dwas.get(f) != math.inf:
        a = [f]
        while s != f:
            f = dout[f]
            a.append(f)
        print(" ".join(map(str, reversed(a))))
    else:
        print(-1)

ffdf()