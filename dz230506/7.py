
import collections
from collections import deque
import math

def deic(d, b):

    was = set()
    dwas = dict.fromkeys(d.keys(), math.inf)

    dwas[b] = 0
    m = []
    while len(d.keys()) > len(was):
        was.add(b)

        for i in d[b].keys():

            if i not in was:
                if i in dwas.keys():
                    dwas[i] = min(dwas[b] + d[b][i], dwas[i])
                m.append(i)


        g = sorted(m, key=lambda x: dwas[x])
        for i in g:
            if i not in was:
                b = i
                break
        else:

            break
    return dwas


def f():
    n = int(input())
    twns = list(map(int, input().split()))
    m = int(input())

    if m == 0 and n != 1:
        print(-1)
        return -1

    if n == 1:
        print(0)
        return 0

    d = collections.defaultdict(dict)
    for i in range(m):
        n1, n2 = list(map(int, input().split()))
        if n1 < 1 and n2 < 1:
            continue
        d[n1].update({n2: twns[n1 - 1]})

        d[n2].update({n1: twns[n2 - 1]})




    o = deic(d, 1)

    if o.get(n) == math.inf or o.get(n) == None:
        print(-1)
    else:
        print(o.get(n))

f()