import collections
from collections import deque


def g(d, b):
    q = deque([b])

    was = set()

    dwas = {}
    while len(q) != 0:
        a = q.popleft()

        for i in d[a]:
            if i not in was:
                was.add(i)
                dwas.update({i: a})
                q.append(i)

    return dwas


def f():
    n = int(input())

    c = 0
    d = collections.defaultdict(list)
    for i in range(1, n + 1):
        d.update({i: []})
        a = list(map(int, input().split()))
        c += sum(a)
        for j in range(0, n):
            if a[j] == 1:
                d[i].append(j + 1)

    b, s = list(map(int, input().split()))

    if b == s:
        print(0)
        return None



    o = g(d, b)
    if s in o.keys():
        k = s
        oar = [k]

        while k != b:
            k = o[k]

            oar.append(k)
        print(len(oar) - 1)
        print(" ".join(map(str, reversed(oar))))

    else:
        print(-1)


f()