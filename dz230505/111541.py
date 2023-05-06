import collections
from collections import deque

def obhod(d, s, was):
    if s not in was:
        was.add(s)
        for i in d[s]:
            was.update(obhod(d, i, was))
    return was


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

    def g(d, b, s):

        q = deque([b])

        was = set()

        while len(q) != 0:
            a = q.popleft()
            for i in d[a]:
                if i not in was:
                    if i == s:
                        return None
                    q.append(i)
        return -1

    print(g(d, b, s))

a = f()